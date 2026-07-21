# USYD Bible build verification

- Status: failed
- Source commit: 80db6766f095dbc20b51481f1c3559fc752371ac
- Checked at: 2026-07-21T12:03:44Z

```text
Traceback (most recent call last):
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 84, in <module>
    main()
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 36, in main
    raise RuntimeError("payload part integrity failed:\n" + "\n".join(mismatches))
RuntimeError: payload part integrity failed:
payload-v2/part-18.b64: expected a9681f96ced1feef6a012c658ce0429c4435ac33145bc8813df5a2d2021310e7, got e0dd3c39909045fc561957ee67e883c904e14c05e3597985107ebefdda6acb1c, chars=4368
```
