#!/usr/bin/env python3
"""Rebuild, enrich and verify the published USYD Bible static site."""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require_bytes(
    label: str,
    data: bytes,
    expected_bytes: int,
    expected_sha: str | None = None,
) -> None:
    if len(data) != int(expected_bytes):
        raise RuntimeError(f"{label} bytes: expected {expected_bytes}, got {len(data)}")
    if expected_sha:
        actual = sha256(data)
        if actual != expected_sha:
            raise RuntimeError(f"{label} sha256: expected {expected_sha}, got {actual}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="_site/index.html")
    args = parser.parse_args()

    manifest = json.loads(Path("content-manifest.json").read_text(encoding="utf-8"))
    payload_dir = Path(manifest.get("payload_dir", "payload"))
    parts = sorted(payload_dir.glob("part-*.b64"))
    expected_parts = int(manifest["payload_parts"])
    if len(parts) != expected_parts:
        raise RuntimeError(f"payload parts: expected {expected_parts}, got {len(parts)}")

    expected_hashes = manifest["part_sha256"]
    clean_parts: list[str] = []
    mismatches: list[str] = []
    for index, path in enumerate(parts):
        clean = "".join(path.read_text(encoding="utf-8").split())
        clean_parts.append(clean)
        actual = sha256(clean.encode("ascii"))
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

    base_html = gzip.decompress(packed)
    require_bytes(
        "payload html",
        base_html,
        manifest["payload_html_bytes"],
        manifest["payload_sha256"],
    )
    base_text = base_html.decode("utf-8")
    for marker in (
        "USYD Bible · 悉尼大学新生终极手册",
        "找到官方答案",
        "数字学生证加入 Apple Wallet",
        "Card Management",
        "Tracking totals",
        "国际学生抵达后必须更新",
    ):
        if marker not in base_text:
            raise RuntimeError(f"missing base content marker: {marker}")

    assets = manifest["assets"]
    asset_data: dict[str, bytes] = {}
    for asset in assets:
        path = Path(asset["path"])
        data = path.read_bytes()
        require_bytes(str(path), data, asset["bytes"], asset.get("sha256"))
        asset_data[str(path)] = data

    subprocess.run(
        ["node", "--check", "assets/source-labels.js"],
        check=True,
        capture_output=True,
        text=True,
    )

    css_tag = '<link rel="stylesheet" href="assets/source-labels.css">\n'
    js_tag = '<script src="assets/source-labels.js"></script>\n'
    if "assets/source-labels.css" in base_text or "assets/source-labels.js" in base_text:
        raise RuntimeError("source-label assets already injected into payload")
    final_text = base_text.replace("</head>", css_tag + "</head>", 1)
    final_text = final_text.replace("</body>", js_tag + "</body>", 1)
    final_html = final_text.encode("utf-8")
    require_bytes("published html", final_html, manifest["html_bytes"], manifest["sha256"])

    js_text = asset_data["assets/source-labels.js"].decode("utf-8")
    for marker in (
        "官方事实",
        "官方系统路径",
        "学生经验",
        "实操整理",
        "来源标识",
        "查看原始页面",
        "手机丢失、换机或需要停用",
        "My Studies",
        "学生证与校园卡",
    ):
        if marker not in js_text:
            raise RuntimeError(f"missing concise-content marker: {marker}")

    for forbidden in (
        "内容留在本站，来源清楚标注",
        "正文内阅读",
        "你不需要跳到别的网站",
        "正文已在本站",
        "展开原始页面链接",
        "第六步：手机丢失或被盗时",
    ):
        if forbidden in js_text:
            raise RuntimeError(f"obsolete meta copy remains: {forbidden}")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(final_html)
    for asset in assets:
        source = Path(asset["path"])
        destination = output.parent / asset["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)

    print(json.dumps({
        "status": "verified",
        "edition": manifest["edition"],
        "payload_dir": str(payload_dir),
        "parts": len(parts),
        "base64_chars": len(encoded),
        "gzip_bytes": len(packed),
        "payload_html_bytes": len(base_html),
        "html_bytes": len(final_html),
        "sha256": sha256(final_html),
        "asset_bytes": {path: len(data) for path, data in asset_data.items()},
        "javascript_syntax": "passed",
        "output": str(output),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
