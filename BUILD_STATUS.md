# USYD Bible build verification

- Status: failed
- Source commit: c06f61a6bea15def1c23f86e44dff51f02f3a0ce
- Checked at: 2026-07-21T11:31:13Z

```text
Traceback (most recent call last):
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 80, in <module>
    main()
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 35, in main
    raise RuntimeError("payload part integrity failed:\n" + "\n".join(mismatches))
RuntimeError: payload part integrity failed:
payload/part-03a.b64: expected 0a6f3c772c3d22a4e3795bd3ba9dc2a0beaa662e3f2733e7d55fc0ce60a4e46f, got 9f3e8d2a07c329533c332ee04d18d85fe992e24f6028a2b1aa8b10996298b0a4, chars=4000
```
