"""Public-only archival projection: preserve approved translations and exclude secrets."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from radar_archive import NEWS_FIELDS, PUBLIC_FIELDS, get_feed, project, coverage_summary
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


    def test_coverage_distinguishes_empty_from_http_failure(self):
        entries = [
            {"name": "USU", "status": "ok", "recordCount": 0},
            {"name": "USYD Museum", "status": "ok", "recordCount": 8},
            {"name": "Sydney Ideas", "status": "partial", "recordCount": 0},
            {"name": "SRC Students", "status": "failed", "recordCount": 0},
        ]
        report = coverage_summary(entries)
        self.assertEqual(report["sourceCount"], 4)
        self.assertEqual(report["failed"], ["SRC Students"])
        self.assertEqual(report["partial"], ["Sydney Ideas"])
        self.assertEqual(report["zeroExtracted"], ["USU", "Sydney Ideas"])
        self.assertEqual(report["campusZeroExtracted"], ["USU", "Sydney Ideas"])
        self.assertFalse(report["complete"])

    def test_provider_rollup_distinguishes_legacy_zero_channels(self):
        sources = [
            {"name": "USU 学生会", "status": "partial", "recordCount": 0},
            {"name": "USU · Official public event calendar", "status": "partial", "recordCount": 8},
            {"name": "SUPRA 研究生协会", "status": "partial", "recordCount": 0},
            {"name": "SUPRA · 活动接口", "status": "ok", "recordCount": 5},
            {"name": "City of Sydney · What's On", "status": "partial", "recordCount": 0},
            {"name": "City of Sydney · Workshops", "status": "ok", "recordCount": 48},
            {"name": "City of Sydney · Technology", "status": "ok", "recordCount": 17},
            {"name": "SRC · 本科生代表组织活动", "status": "partial", "recordCount": 0},
        ]
        result = coverage_summary(sources)
        self.assertEqual(result["priorityProviderGaps"], ["SRC"])
        self.assertEqual(result["providerCoverage"]["USU"]["maxChannelRecordCount"], 8)
        self.assertTrue(result["providerCoverage"]["SUPRA"]["hasExtractedRecords"])
        self.assertEqual(result["providerCoverage"]["City of Sydney"]["maxChannelRecordCount"], 48)
        self.assertIn("USU 学生会", result["zeroExtracted"])
        self.assertIn("USU 学生会", result["providerCoverage"]["USU"]["zeroChannels"])
        self.assertFalse(result["complete"])

if __name__ == "__main__":
    unittest.main()
