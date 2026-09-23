#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]
warnings=[]

# Generated distribution content must not be versioned. CI may still have generated files in dist/.
tracked=subprocess.run(
    ["git","ls-files","dist"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=True,
).stdout.splitlines()
unexpected=[p for p in tracked if p!="dist/.gitkeep"]
if unexpected:
    errors.append("generated dist content is versioned: "+", ".join(sorted(unexpected)))

gitignore=(ROOT/".gitignore").read_text(encoding="utf-8")
for token in ["dist/*","!dist/.gitkeep","__pycache__/","*.pyc"]:
    if token not in gitignore:
        errors.append(f".gitignore missing {token}")

tracked_all=subprocess.run(
    ["git","ls-files"],
    cwd=ROOT,
    text=True,
    capture_output=True,
    check=True,
).stdout.splitlines()
for rel in tracked_all:
    parts=Path(rel).parts
    if Path(rel).name==".DS_Store":
        errors.append(f"temporary file is versioned: {rel}")
    if "__pycache__" in parts:
        errors.append(f"cache content is versioned: {rel}")
    if rel.endswith(".pyc"):
        errors.append(f"compiled Python is versioned: {rel}")

required=[
    "gpt-project.yaml","project-status.yaml","PROJECT.md","STATUS.md",
    "runtime-parity.yaml","tests/test-manifest.yaml",
    "canonical/runtime-contract.md","schemas/review-process.schema.json"
]
for rel in required:
    if not (ROOT/rel).exists():
        errors.append(f"missing required project file: {rel}")

if errors:
    print("PROJECT HYGIENE FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("PROJECT HYGIENE OK")
