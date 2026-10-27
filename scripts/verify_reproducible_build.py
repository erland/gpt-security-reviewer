#!/usr/bin/env python3
"""Rebuild the six canonical archives twice and compare SHA-256 outputs."""
from pathlib import Path
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
version = (os.environ.get("RELEASE_VERSION") or (ROOT / "VERSION").read_text(encoding="utf-8").strip()).lstrip("v")
names = [f"security-reviewer-{target}-{version}.zip" for target in
         ("project", "chat", "plugin", "claude-project", "claude-skills", "opencode")]
names += ["SHA256SUMS.txt", "DELIVERY-MANIFEST.json"]


def build_once():
    if DIST.exists():
        for path in DIST.iterdir():
            if path.name != ".gitkeep":
                shutil.rmtree(path) if path.is_dir() else path.unlink()
    subprocess.run([sys.executable, str(ROOT / "scripts/build_distributions.py"),
                    "--project-root", str(ROOT), "--version", version],
                   cwd=ROOT, check=True)
    hashes = {}
    for name in names:
        path = DIST / name
        if not path.is_file():
            raise RuntimeError(f"missing canonical artifact: {name}")
        hashes[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


with tempfile.TemporaryDirectory():
    first = build_once()
    second = build_once()
if first != second:
    print("REPRODUCIBILITY FAILED")
    for name in names:
        if first.get(name) != second.get(name):
            print("-", name, first.get(name), second.get(name))
    sys.exit(1)
print("REPRODUCIBILITY OK")
