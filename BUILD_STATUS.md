# USYD Bible build verification

- Status: failed
- Source commit: bef706718f0219bcfce7090afaf72f7c4e75295e
- Checked at: 2026-07-21T11:29:46Z

```text
Traceback (most recent call last):
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 80, in <module>
    main()
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 35, in main
    raise RuntimeError("payload part integrity failed:\n" + "\n".join(mismatches))
RuntimeError: payload part integrity failed:
payload/part-03.b64: expected 0a6f3c772c3d22a4e3795bd3ba9dc2a0beaa662e3f2733e7d55fc0ce60a4e46f, got 5c5e759f7fa18c522d1a98c18ae655dbd2297a7419b37bbd45f3b7d09d5c999c, chars=8000
```
