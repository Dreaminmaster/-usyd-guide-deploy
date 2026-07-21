#!/usr/bin/env python3
"""Rebuild and verify the final USYD Bible static HTML payload."""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="_site/index.html")
    args = parser.parse_args()

    manifest = json.loads(Path("content-manifest.json").read_text(encoding="utf-8"))
    parts = sorted(Path("payload").glob("part-*.b64"))
    expected_parts = int(manifest["payload_parts"])
    if len(parts) != expected_parts:
        raise RuntimeError(f"payload parts: expected {expected_parts}, got {len(parts)}")

    expected_hashes = manifest["part_sha256"]
    clean_parts: list[str] = []
    mismatches: list[str] = []
    for index, path in enumerate(parts):
        clean = "".join(path.read_text(encoding="utf-8").split())
        clean_parts.append(clean)
        actual = hashlib.sha256(clean.encode("ascii")).hexdigest()
        expected = expected_hashes[index]
        if actual != expected:
            mismatches.append(f"{path}: expected {expected}, got {actual}, chars={len(clean)}")
    if mismatches:
        raise RuntimeError("payload part integrity failed:\n" + "\n".join(mismatches))

    encoded = "".join(clean_parts)
    if len(encoded) != int(manifest["base64_chars"]):
        raise RuntimeError(f"base64 chars: expected {manifest['base64_chars']}, got {len(encoded)}")

    packed = base64.b64decode(encoded, validate=True)
    if len(packed) != int(manifest["gzip_bytes"]):
        raise RuntimeError(f"gzip bytes: expected {manifest['gzip_bytes']}, got {len(packed)}")

    html = gzip.decompress(packed)
    if len(html) != int(manifest["html_bytes"]):
        raise RuntimeError(f"html bytes: expected {manifest['html_bytes']}, got {len(html)}")

    digest = hashlib.sha256(html).hexdigest()
    if digest != manifest["sha256"]:
        raise RuntimeError(f"sha256: expected {manifest['sha256']}, got {digest}")

    text = html.decode("utf-8")
    markers = (
        "USYD Bible · 悉尼大学新生终极手册",
        "数字学生证加入 Apple Wallet",
        "浏览完整知识库",
        "打开我的入学清单",
        "官方渠道提交 enquiry",
    )
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise RuntimeError(f"missing content markers: {missing}")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(html)
    print(json.dumps({
        "status": "verified",
        "parts": len(parts),
        "base64_chars": len(encoded),
        "gzip_bytes": len(packed),
        "html_bytes": len(html),
        "sha256": digest,
        "output": str(output),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
