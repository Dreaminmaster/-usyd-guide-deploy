#!/usr/bin/env python3
"""Archive only public USYD Radar events to the dedicated radar-data branch.
No credentials or personal university data are stored in the archive.
GitHub Actions checks out both branches and commits only changed files.
"""
from __future__ import annotations
import argparse
import datetime as dt
import json
from pathlib import Path
import sys
import urllib.request

API = "https://usyd-radar.vercel.app/api/combined"
PUBLIC_FIELDS = ("id", "title", "date", "time", "location", "category", "priority",
                 "score", "summary", "eligibility", "registration", "confidence",
                 "sourceName", "url", "verified", "feedSource", "priorityReason")
NEWS_FIELDS = ("id", "title", "date", "source", "summary", "url", "type", "dateReliable")

def get_feed():
    request = urllib.request.Request(API + "?github_archive=1", headers={
        "Accept": "application/json", "User-Agent": "USYD-Radar-Public-Archive/1.0"})
    with urllib.request.urlopen(request, timeout=95) as response:
        if response.status != 200:
            raise RuntimeError(f"Radar feed HTTP {response.status}")
        data = json.loads(response.read(4_000_000).decode("utf-8"))
    if not isinstance(data.get("events"), list) or len(data["events"]) == 0:
        raise ValueError("Refusing to overwrite a working snapshot with an empty feed")
    if data.get("status") in ("unavailable", "archived") or data.get("live") is False:
        raise ValueError("Refusing to re-archive a historical fallback as a fresh live observation")
    if not data.get("checkedAt") or not data.get("summary"):
        raise ValueError("Feed missing checkedAt or summary")
    return data

def project(record, fields):
    return {key: record[key] for key in fields if record.get(key) is not None}

def main(root):
    root.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    feed = get_feed()
    date = str(feed.get("today") or "")[:10]
    dt.date.fromisoformat(date)
    snapshot = {
        "schema": 1, "checkedAt": feed["checkedAt"], "archivedAt": now,
        "timezone": "Australia/Sydney", "today": date, "status": feed.get("status"),
        "summary": feed["summary"],
        "sources": [{k: v for k, v in s.items() if k in
                     ("name", "status", "recordCount", "url", "message", "checkedAt")}
                    for s in feed.get("sources", [])],
        "events": [project(e, PUBLIC_FIELDS) for e in feed["events"]],
        "news": [project(n, NEWS_FIELDS) for n in feed.get("news", [])],
        "provenance": API, "publicDataOnly": True
    }
    encoded = json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"
    (root / "latest.json").write_text(encoded, encoding="utf-8")
    daily = root / "snapshots"
    daily.mkdir(exist_ok=True)
    (daily / (date + ".json")).write_text(encoded, encoding="utf-8")
    cutoff = dt.date.fromisoformat(date) - dt.timedelta(days=90)
    for older in daily.glob("????-??-??.json"):
        try:
            if dt.date.fromisoformat(older.stem) < cutoff:
                older.unlink()
        except ValueError:
            continue
    status = {"schema": 1, "checkedAt": now, "feedCheckedAt": feed["checkedAt"],
              "feedStatus": feed.get("status"), "events": len(snapshot["events"]),
              "news": len(snapshot["news"]), "sourceCount": len(snapshot["sources"])}
    (root / "status.json").write_text(
        json.dumps(status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    try:
        main(args.root)
    except Exception as e:
        print(f"Public archive sync failed; old data unchanged: {e}", file=sys.stderr)
        sys.exit(1)
