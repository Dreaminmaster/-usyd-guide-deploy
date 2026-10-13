"""Public-only cloud translation: priority, budget, and safe fallback tests."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import radar_translate as translation


def event(n, title=None):
    return {"id": f"example-{n}", "title": title or f"Conference on quantum engineering {n}",
            "summary": f"Upcoming free science lecture number {n}, open to all.",
            "date": "2026-10-20", "score": 80}


class TranslationArchiveTests(unittest.TestCase):
    def fixture(self, root, events, translations=None):
        (root / "latest.json").write_text(
            json.dumps({"today": "2026-10-13", "events": events}), encoding="utf-8")
        if translations is not None:
            (root / "translations.json").write_text(
                json.dumps({"schema": 1, "entries": translations}), encoding="utf-8")

    def test_titles_first_with_bounded_requests(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root, [event(i) for i in range(21)])
            requests = []

            def translate_stub(text):
                requests.append(text)
                return "活动中文标题" if text.startswith("Conference") else "这是中文活动说明"

            with patch.object(translation, "translate", side_effect=translate_stub), \
                 patch.object(translation.time, "sleep", return_value=None):
                translation.update(root)
            written = json.loads((root / "translations.json").read_text())["entries"]
            self.assertEqual(len(requests), translation.MAX_REQUESTS_PER_RUN)
            self.assertEqual(len(written), translation.MAX_EVENTS_PER_RUN)
            self.assertEqual(sum(bool(v.get("summaryZh")) for v in written.values()),
                             translation.MAX_SUMMARIES_PER_RUN)
            self.assertTrue(all("sourceTitle" in v for v in written.values()))

    def test_manual_title_kept_and_summary_added(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old = {"sourceTitle": event(1)["title"], "titleZh": "人工校对标题",
                   "sourceSummary": event(1)["summary"], "summaryZh": "",
                   "provider": "human reviewed"}
            self.fixture(root, [event(1)], {"example-1": old})
            with patch.object(translation, "translate", return_value="中文简介"), \
                 patch.object(translation.time, "sleep", return_value=None):
                translation.update(root)
            got = json.loads((root / "translations.json").read_text())["entries"]["example-1"]
            self.assertEqual(got["titleZh"], "人工校对标题")
            self.assertEqual(got["summaryZh"], "中文简介")

    def test_provider_failure_keeps_old_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old = {"sourceTitle": event(1)["title"], "titleZh": "旧的人工翻译",
                   "sourceSummary": event(1)["summary"], "summaryZh": ""}
            self.fixture(root, [event(1), event(2)], {"example-1": old})
            before = (root / "translations.json").read_text()
            with patch.object(translation, "translate", return_value=None), \
                 patch.object(translation.time, "sleep", return_value=None):
                translation.update(root)
            self.assertEqual(before, (root / "translations.json").read_text())


if __name__ == "__main__":
    unittest.main()
