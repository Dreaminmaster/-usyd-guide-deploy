#!/usr/bin/env python3
"""Slow, quota-conscious bilingual cache for public USYD Radar events.

Only public event titles/excerpts are sent to MyMemory, a third-party
translation service already used by the website. No personal university data,
private email, tokens or account details are sent to the service or cached.
If the free quota is unavailable, the existing cache is preserved.
"""
from __future__ import annotations
from datetime import datetime, timezone
import html
import json
from pathlib import Path
import re
import sys
import time
from urllib.parse import urlencode
import urllib.request

SERVICE = "https://api.mymemory.translated.net/get"
MAX_EVENTS_PER_RUN = 14
MAX_REQUESTS_PER_RUN = 18
MAX_SUMMARIES_PER_RUN = 4
MAX_ENTRIES = 550
CJK = re.compile(r"[\u3400-\u9fff]")
BLOCK = re.compile(r"MYMEMORY WARNING|QUOTA EXCEEDED|PLEASE TRY LATER|MAXIMUM DAILY USAGE", re.I)


def translate(text):
    text = html.unescape(str(text or "").strip())[:350]
    if not text or CJK.search(text):
        return None
    url = SERVICE + "?" + urlencode({"q": text, "langpair": "en|zh-CN"})
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json",
                                                   "User-Agent": "USYDRadarPublicTranslation/1.0"})
        with urllib.request.urlopen(req, timeout=8) as r:
            result = json.loads(r.read(130_000).decode("utf-8"))
        raw = str((result.get("responseData") or {}).get("translatedText") or "")
        chinese = html.unescape(raw).strip()[:490]
        if (result.get("responseStatus") != 200 or result.get("quotaFinished")
                or BLOCK.search(chinese) or not CJK.search(chinese)):
            return None
        return chinese
    except (TimeoutError, ValueError, OSError, KeyError) as error:
        print("Translation temporarily unavailable:", type(error).__name__, file=sys.stderr)
        return None


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, FileNotFoundError):
        return {}


def update(root):
    latest = load(root / "latest.json")
    if not latest.get("events"):
        raise ValueError("No public event snapshot: cache unchanged")
    path = root / "translations.json"
    previous = load(path)
    entries = dict(previous.get("entries") or {})
    today = latest.get("today") or ""
    candidates = [e for e in latest["events"] if e.get("id") and e.get("title")
                  and e.get("date", "") >= today]
    # Cover high-value titles first, rather than repeatedly using nearly all
    # the free quota translating summaries of already-translated events.
    def weight(e):
        days = (datetime.fromisoformat(e["date"]).date()
                - datetime.fromisoformat(today).date()).days
        return (days > 21, -(float(e.get("score") or 0)), days, e["id"])

    candidates.sort(key=weight)
    used, changed, titles_done, summaries_done, failures = 0, 0, 0, 0, 0
    stamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    # Pass 1: broad coverage for titles; browser has an immediate Chinese label.
    for e in candidates:
        if used >= MAX_REQUESTS_PER_RUN or titles_done >= MAX_EVENTS_PER_RUN or failures >= 3:
            break
        event_id, title = str(e["id"]), str(e["title"])[:180]
        summary = str(e.get("summary") or "")[:260]
        old = entries.get(event_id) or {}
        if old.get("sourceTitle") == title and old.get("titleZh"):
            continue
        if CJK.search(title):
            chinese = title
        else:
            chinese = translate(title)
            used += 1
            time.sleep(0.55)
        if not chinese:
            failures += 1
            continue
        failures = 0
        preserve = old.get("summaryZh") if old.get("sourceTitle") == title and old.get("sourceSummary") == summary else ""
        entries[event_id] = {"sourceTitle": title, "titleZh": chinese,
                             "sourceSummary": summary, "summaryZh": preserve or "",
                             "translatedAt": stamp, "provider": "MyMemory (free, best effort)"}
        titles_done += 1
        changed += 1

    # Pass 2: shorter descriptions for high-value upcoming events, only within
    # the remaining provider quota. Never send already-Chinese summaries.
    for e in candidates:
        if used >= MAX_REQUESTS_PER_RUN or summaries_done >= MAX_SUMMARIES_PER_RUN or failures >= 3:
            break
        summary = str(e.get("summary") or "")[:260]
        if not summary or CJK.search(summary) or float(e.get("score") or 0) < 55:
            continue
        event_id, title = str(e["id"]), str(e["title"])[:180]
        old = entries.get(event_id) or {}
        if old.get("sourceTitle") != title or not old.get("titleZh"):
            continue
        if old.get("sourceSummary") == summary and old.get("summaryZh"):
            continue
        chinese = translate(summary)
        used += 1
        time.sleep(0.55)
        if not chinese:
            failures += 1
            continue
        failures = 0
        entries[event_id] = dict(old, sourceSummary=summary, summaryZh=chinese,
                                 translatedAt=stamp)
        summaries_done += 1
        changed += 1

    if not changed:
        print("No valid new translations; existing cloud cache remains unchanged")
        return

    active = {e["id"] for e in latest["events"]}
    entries = {k: v for k, v in entries.items() if k in active}
    if len(entries) > MAX_ENTRIES:
        entries = dict(list(entries.items())[-MAX_ENTRIES:])
    output = {"schema": 1, "updatedAt": stamp, "provider": "MyMemory",
              "notice": "Public event translations; verify crucial details at organiser.",
              "count": len(entries), "entries": entries}
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Cloud translation: {titles_done} titles, {summaries_done} summaries; "
          f"{used} requests; {len(entries)} entries total")

if __name__ == "__main__":
    try:
        update(Path(sys.argv[1]))
    except Exception as error:
        # A broken translation provider must not invalidate archive data.
        print("Translation cache skipped:", error, file=sys.stderr)
