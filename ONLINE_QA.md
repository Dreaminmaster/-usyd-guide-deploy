# Online release QA

- Status: successful
- Edition: concise-source-labelled-2026
- URL: https://dreaminmaster.github.io/-usyd-guide-deploy/
- Expected HTML bytes: 333239
- Expected HTML SHA-256: 5cdacc4e0193b85ee7e8f809000bb3791b681e3dd5dfcbff8886fbabbe140b31
- Verified: common shortcuts, concise article structure, source labels, removed meta copy and JavaScript syntax
- Checked at: 2026-07-21T13:11:35Z

```text
attempt=1 path=index.html status=200 bytes=333239 sha256=5cdacc4e0193b85ee7e8f809000bb3791b681e3dd5dfcbff8886fbabbe140b31
attempt=1 path=assets/source-labels.css status=200 bytes=3220 sha256=e785547a0bf5faef6a18551fc8b807c48f4b124ea172cdb1822490f782e138bd
attempt=1 path=assets/source-labels.js status=200 bytes=15993 sha256=94a898c786145a5cdf20c0a7c0d08533a43a267f102ee8f4181ff08ba536e310
attempt=1 error=RuntimeError('unexpected assets/source-labels.js: status=200 bytes=15993 sha256=94a898c786145a5cdf20c0a7c0d08533a43a267f102ee8f4181ff08ba536e310')
attempt=2 path=index.html status=200 bytes=333239 sha256=5cdacc4e0193b85ee7e8f809000bb3791b681e3dd5dfcbff8886fbabbe140b31
attempt=2 path=assets/source-labels.css status=200 bytes=3220 sha256=e785547a0bf5faef6a18551fc8b807c48f4b124ea172cdb1822490f782e138bd
attempt=2 path=assets/source-labels.js status=200 bytes=12330 sha256=22374fd6d562669dcd5443b44df8be6c60f99d07c95414ff2622663803d86f7b
LIVE_CONTENT_MARKERS_SUCCESS
```
