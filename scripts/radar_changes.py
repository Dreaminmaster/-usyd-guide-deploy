"""Conservative public-event snapshot comparison for USYD Radar.

A disappearing entry is NEVER treated as confirmed cancellation. Source outages,
pagination, changes in website HTML and organiser edits can all remove listings.
"""
from __future__ import annotations
from collections import defaultdict
from datetime import datetime, timezone
from urllib.parse import urlsplit


def permalink(url: str) -> str:
    try:
        parsed = urlsplit(url or "")
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            return ""
        return parsed.hostname.lower().removeprefix("www.") + parsed.path.rstrip("/").lower()
    except (ValueError, TypeError):
        return ""


def index_events(events):
    return {e["id"]: e for e in events if isinstance(e, dict) and e.get("id") and e.get("date") and e.get("url")}


def healthy_enough(previous, current):
    if not previous or current.get("status") != "ok":
        return False
    prev_events = previous.get("events") or []
    current_events = current.get("events") or []
    # A large drop signals a broken extractor, not mass cancellations.
    if len(prev_events) >= 20 and len(current_events) < len(prev_events) * 0.75:
        return False
    return (current.get("summary") or {}).get("failedSources", 0) == 0


def compare(previous, current, previous_streaks=None, checked_at=None):
    checked_at = checked_at or datetime.now(timezone.utc).isoformat()
    today = current.get("today", "")
    old = index_events((previous or {}).get("events") or [])
    now = index_events(current.get("events") or [])
    by_url_old = defaultdict(list)
    by_url_now = defaultdict(list)
    for record in old.values():
        by_url_old[permalink(record["url"])].append(record)
    for record in now.values():
        by_url_now[permalink(record["url"])].append(record)

    # A source newly connected or recovered from extraction failure often
    # exposes many pre-existing listings. These were newly OBSERVED by Radar,
    # not necessarily newly published by the event organiser.
    prev_sources = {s.get("name"): s.get("status") for s in
                    (previous or {}).get("sources", []) if isinstance(s, dict)}
    source_recovered = any(
        prev_sources.get("City discovery · " + key) not in (None, "ok")
        and any(s.get("name") == "City discovery · " + key
                and s.get("status") == "ok" for s in current.get("sources", []))
        for key in ("city-free", "city-tech", "city-seminars", "city-tours")
    )

    changes = []
    accounted = set()
    for id_, new in now.items():
        prior = old.get(id_)
        if prior:
            differences = {}
            for name in ("title", "date", "time", "location"):
                a, b = str(prior.get(name) or "").strip(), str(new.get(name) or "").strip()
                if a != b:
                    differences[name] = {"before": a, "after": b}
            if differences:
                changes.append({"kind": "updated", "id": id_, "title": new.get("title"),
                                "date": new["date"], "url": new["url"], "differences": differences,
                                "priority": new.get("priority"), "detectedAt": checked_at})
            accounted.add(id_)
            continue

        key = permalink(new["url"])
        old_matches = by_url_old[key]
        new_matches = by_url_now[key]
        # A unique URL occurrence that moved date is plausible rescheduling.
        # Never infer rescheduling from recurring events sharing a landing page.
        if key and len(old_matches) == 1 and len(new_matches) == 1:
            before = old_matches[0]
            # A multi-day City listing can appear once per daily snapshot at
            # today's date. Advancing across midnight is NOT rescheduling.
            # Suppress this ambiguity rather than notifying the user falsely.
            if (id_.startswith("city-discovery-")
                    and str(before.get("id", "")).startswith("city-discovery-")
                    and before.get("date") == (previous or {}).get("today")
                    and new.get("date") == today
                    and new.get("date") > before.get("date")):
                accounted.add(before["id"])
                continue
            if before["id"] not in now and before.get("date") != new.get("date"):
                changes.append({"kind": "possible_reschedule", "id": id_, "title": new["title"],
                                "oldDate": before["date"], "date": new["date"], "url": new["url"],
                                "priority": new.get("priority"), "detectedAt": checked_at,
                                "notice": "Date differs across public snapshots; verify at organiser."})
                accounted.add(before["id"])
                continue
        # If the exact public URL and date is unchanged, skip id renames.
        if any(e.get("date") == new.get("date") for e in old_matches):
            continue
        kind = "newly_observed" if source_recovered and id_.startswith("city-discovery-") else "new"
        changes.append({"kind": kind, "id": id_, "title": new["title"],
                        "date": new["date"], "url": new["url"],
                        "priority": new.get("priority"), "detectedAt": checked_at,
                        "notice": "New to Radar; not proof of new publication" if kind == "newly_observed" else "First observed in Radar snapshot"})

    previous_streaks = previous_streaks or {}
    streaks = {}
    safe_missing = healthy_enough(previous, current)
    if safe_missing:
        for id_, prev in old.items():
            if id_ in now or id_ in accounted or prev.get("date", "") < today:
                continue
            if any(e.get("date") == prev.get("date") for e in by_url_now[permalink(prev["url"])]):
                continue
            missed = int((previous_streaks.get(id_) or {}).get("observations", 0)) + 1
            streaks[id_] = {"observations": missed, "firstMissingAt": (previous_streaks.get(id_) or {}).get("firstMissingAt", checked_at),
                            "title": prev.get("title"), "date": prev.get("date"),
                            "url": prev.get("url")}
            if missed == 2:
                changes.append({"kind": "not_observed", "id": id_, "title": prev.get("title"),
                                "date": prev.get("date"), "url": prev.get("url"), "priority": prev.get("priority"),
                                "detectedAt": checked_at,
                                "notice": "Not found in 2 healthy snapshots. NOT confirmation of cancellation."})
    else:
        # Do not count missing observations when the feed is unhealthy.
        streaks = {k: v for k, v in previous_streaks.items()
                   if k not in now and isinstance(v, dict) and v.get("date", "") >= today}

    return changes, streaks


def history_update(old_history, changes, limit=100):
    combined = list(changes) + list(old_history or [])
    result, used = [], set()
    for e in combined:
        if not isinstance(e, dict):
            continue
        key = (e.get("kind"), e.get("id"), e.get("oldDate"), e.get("date"),
               tuple(sorted((e.get("differences") or {}).keys())))
        if key in used:
            continue
        used.add(key)
        result.append(e)
        if len(result) >= limit:
            break
    return result
