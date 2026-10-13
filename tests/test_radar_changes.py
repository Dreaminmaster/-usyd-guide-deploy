"""No false claims of cancelled events in public feed comparison."""
import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from radar_changes import compare, healthy_enough


def event(id_, date, url, title="AI seminar", time="18:00"):
    return {"id": id_, "date": date, "url": url, "title": title, "time": time, "priority": "medium"}


def snapshot(events, status="ok", failed=0):
    return {"today": "2026-10-13", "events": events, "status": status, "summary": {"failedSources": failed}}


class RadarComparisonTests(unittest.TestCase):
    def test_new_and_time_update(self):
        old = snapshot([event("a", "2026-10-20", "https://sydney.edu.au/a")])
        new = snapshot([event("a", "2026-10-20", "https://sydney.edu.au/a", time="19:00"),
                        event("b", "2026-10-21", "https://usu.edu.au/b")])
        changes, _ = compare(old, new)
        self.assertEqual([x["kind"] for x in changes], ["updated", "new"])
        self.assertIn("time", changes[0]["differences"])

    def test_rescheduling_unique_url_only(self):
        old = snapshot([event("oct20", "2026-10-20", "https://usu.edu.au/movie")])
        new = snapshot([event("oct22", "2026-10-22", "https://usu.edu.au/movie")])
        changes, _ = compare(old, new)
        self.assertEqual(changes[0]["kind"], "possible_reschedule")

    def test_recurring_url_does_not_claim_reschedule(self):
        url = "https://usu.edu.au/multi-day"
        old = snapshot([event("day1", "2026-10-20", url), event("day2", "2026-10-21", url)])
        new = snapshot([event("day1", "2026-10-20", url), event("day2", "2026-10-21", url),
                        event("day3", "2026-10-22", url)])
        changes, _ = compare(old, new)
        self.assertEqual([x["kind"] for x in changes], ["new"])

    def test_missing_is_never_cancelled(self):
        old = snapshot([event("a", "2026-10-20", "https://usu.edu.au/a"),
                        event("b", "2026-10-21", "https://usu.edu.au/b")])
        new = snapshot([old["events"][0]])
        first, state = compare(old, new)
        self.assertFalse(any(x["kind"] == "not_observed" for x in first))
        second, _ = compare(old, new, state)
        self.assertEqual([x["kind"] for x in second], ["not_observed"])

    def test_source_failure_does_not_create_missing_claim(self):
        old = snapshot([event("a", "2026-10-20", "https://usu.edu.au/a")])
        new = snapshot([], status="partial", failed=1)
        changes, state = compare(old, new)
        self.assertEqual(changes, [])
        self.assertEqual(state, {})


if __name__ == "__main__":
    unittest.main()
