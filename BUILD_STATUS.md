# USYD Bible build verification

- Status: failed
- Source commit: c3cecdd1c272a1b0be9d2d376a7ca74143443717
- Checked at: 2026-07-21T12:43:50Z

```text
Traceback (most recent call last):
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 133, in <module>
    main()
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 83, in main
    require_bytes(str(path), data, asset["bytes"], asset["sha256"])
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 23, in require_bytes
    raise RuntimeError(f"{label} sha256: expected {expected_sha}, got {actual}")
RuntimeError: assets/source-labels.js sha256: expected None, got 94a898c786145a5cdf20c0a7c0d08533a43a267f102ee8f4181ff08ba536e310
```
