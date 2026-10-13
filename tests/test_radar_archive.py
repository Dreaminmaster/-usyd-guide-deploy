"""Public-only archival projection: preserve approved translations and exclude secrets."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from radar_archive import NEWS_FIELDS, PUBLIC_FIELDS, get_feed, project
from unittest.mock import patch
import json


class RadarArchiveProjectionTests(unittest.TestCase):
    def test_event_translations_survive_snapshot(self):
        event = {
            "id": "verified-ai-talk",
            "title": "Public AI talk", "titleZh": "人工智能公开讲座",
            "date": "2026-10-22", "time": "17:30",
            "location": "Sydney", "locationZh": "悉尼",
            "summary": "Open public event", "summaryZh": "公开活动",
            "url": "https://www.sydney.edu.au/events/example",
            "privateEmail": "should-never-be-archived",
            "canvasToken": "should-never-be-archived",
        }
        saved = project(event, PUBLIC_FIELDS)
        self.assertEqual(saved["titleZh"], "人工智能公开讲座")
        self.assertEqual(saved["locationZh"], "悉尼")
        self.assertEqual(saved["summaryZh"], "公开活动")
        self.assertNotIn("privateEmail", saved)
        self.assertNotIn("canvasToken", saved)

    def test_public_news_translation_survives(self):
        record = {
            "id": "news-1", "title": "University update",
            "titleZh": "大学动态", "summaryZh": "公开说明",
            "privateStudentId": "should-never-be-archived",
        }
        saved = project(record, NEWS_FIELDS)
        self.assertEqual(saved["titleZh"], "大学动态")
        self.assertEqual(saved["summaryZh"], "公开说明")
        self.assertNotIn("privateStudentId", saved)

    def test_live_fetch_uses_fresh_cache_key(self):
        payload = {
            "events": [{"id": "public", "url": "https://www.sydney.edu.au/", "date": "2026-10-22"}],
            "checkedAt": "2026-10-14T00:00:00Z",
            "status": "ok",
            "summary": {"events": 1},
        }

        class FakeReply:
            status = 200

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def read(self, _limit):
                return json.dumps(payload).encode("utf-8")

        with patch("radar_archive.urllib.request.urlopen", return_value=FakeReply()) as mocked:
            self.assertEqual(get_feed()["status"], "ok")
        request = mocked.call_args.args[0]
        self.assertIn("?github_archive=", request.full_url)
        self.assertNotIn("?github_archive=1", request.full_url)
        self.assertEqual(request.get_header("Cache-control"), "no-cache")

    def test_missing_translations_are_not_fabricated(self):
        saved = project({"id": "plain", "title": "Event"}, PUBLIC_FIELDS)
        self.assertNotIn("titleZh", saved)
        self.assertNotIn("summaryZh", saved)


if __name__ == "__main__":
    unittest.main()
