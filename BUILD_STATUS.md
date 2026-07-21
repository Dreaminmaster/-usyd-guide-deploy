# USYD Bible build verification

- Status: failed
- Source commit: 2add057441465d4a32d769d1dccb9cbe5aaaeda4
- Checked at: 2026-07-21T12:41:21Z

```text
Traceback (most recent call last):
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 133, in <module>
    main()
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 83, in main
    require_bytes(str(path), data, asset["bytes"], asset["sha256"])
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 20, in require_bytes
    raise RuntimeError(f"{label} bytes: expected {expected_bytes}, got {len(data)}")
RuntimeError: assets/source-labels.js bytes: expected 15994, got 15993
```
