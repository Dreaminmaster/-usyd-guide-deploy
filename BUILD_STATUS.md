# USYD Bible build verification

- Status: failed
- Source commit: b3fc206c2bc83db329e01ac1c1872d1a2e6fe20b
- Checked at: 2026-07-21T12:42:33Z

```text
Traceback (most recent call last):
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 133, in <module>
    main()
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 83, in main
    require_bytes(str(path), data, asset["bytes"], asset["sha256"])
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 23, in require_bytes
    raise RuntimeError(f"{label} sha256: expected {expected_sha}, got {actual}")
RuntimeError: assets/source-labels.js sha256: expected 40d1f8cd5c9ba855141985d9812408525389828ed9a73e079cb6581570ab3db9, got 94a898c786145a5cdf20c0a7c0d08533a43a267f102ee8f4181ff08ba536e310
```
