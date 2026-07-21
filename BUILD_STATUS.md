# USYD Bible build verification

- Status: failed
- Source commit: f706c156f9ae4b0213c258ae291bd319f194fcf6
- Checked at: 2026-07-21T11:28:33Z

```text
Traceback (most recent call last):
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 68, in <module>
    main()
  File "/home/runner/work/-usyd-guide-deploy/-usyd-guide-deploy/scripts/verify_payload.py", line 33, in main
    html = gzip.decompress(packed)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/gzip.py", line 638, in decompress
    raise BadGzipFile("CRC check failed")
gzip.BadGzipFile: CRC check failed
```
