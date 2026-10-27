#!/usr/bin/env python3
"""Check the six canonical 1.6.33 release archives and their checksums."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
version = (os.environ.get("RELEASE_VERSION") or (ROOT / "VERSION").read_text(encoding="utf-8").strip()).lstrip("v")
names = [f"security-reviewer-{target}-{version}.zip" for target in
         ("project", "chat", "plugin", "claude-project", "claude-skills", "opencode")]
errors = []
if subprocess.run([sys.executable, str(ROOT / "scripts/validate_runtime_parity.py")], cwd=ROOT).returncode:
    errors.append("runtime parity failed")

for name in names:
    file = DIST / name
    if not file.is_file():
        errors.append(f"missing canonical archive: {name}")
        continue
    try:
        with zipfile.ZipFile(file) as archive:
            if archive.testzip():
                errors.append(f"corrupt archive: {name}")
    except zipfile.BadZipFile:
        errors.append(f"invalid zip archive: {name}")

checksums = DIST / "SHA256SUMS.txt"
recorded = {}
if not checksums.is_file():
    errors.append("missing SHA256SUMS.txt")
else:
    for line in checksums.read_text(encoding="utf-8").splitlines():
        fields = line.split(None, 1)
        if len(fields) == 2:
            recorded[fields[1].lstrip("*").strip()] = fields[0]
    for name in names:
        path = DIST / name
        if path.is_file() and recorded.get(name) != hashlib.sha256(path.read_bytes()).hexdigest():
            errors.append(f"SHA-256 mismatch or missing entry: {name}")

manifest = DIST / "DELIVERY-MANIFEST.json"
if not manifest.is_file():
    errors.append("missing DELIVERY-MANIFEST.json")
else:
    try:
        json.loads(manifest.read_text(encoding="utf-8"))
    except (ValueError, UnicodeDecodeError) as exc:
        errors.append(f"invalid delivery manifest: {exc}")

if errors:
    print("RELEASE READINESS FAILED")
    for error in errors:
        print("-", error)
    sys.exit(1)
print("RELEASE READINESS OK")
print("version=" + version)
