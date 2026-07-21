# USYD Bible build verification

- Status: failed
- Source commit: 3db447d6e44e2f1fd00a5c6c42a97d1a98b0b5dc
- Checked at: 2026-07-21T11:31:58Z

```text
Traceback (most recent call last):
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 80, in <module>
    main()
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 63, in main
    raise RuntimeError(f"missing content markers: {missing}")
RuntimeError: missing content markers: ['417', '已完成 0 / 92 项', 'content-manifest']
```
