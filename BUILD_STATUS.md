# USYD Bible build verification

- Status: failed
- Source commit: 357d44de89c128ab5d9183a253a19981d556df7a
- Checked at: 2026-07-21T11:30:37Z

```text
Traceback (most recent call last):
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 80, in <module>
    main()
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 22, in main
    raise RuntimeError(f"payload parts: expected {expected_parts}, got {len(parts)}")
RuntimeError: payload parts: expected 8, got 7
```
