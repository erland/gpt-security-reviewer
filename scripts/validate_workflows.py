#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT=Path(__file__).resolve().parents[1]
errors=[]

files={
    "ci": ROOT/".github/workflows/ci.yml",
    "release": ROOT/".github/workflows/release.yml",
}

for name,p in files.items():
    if not p.exists():
        errors.append(f"Missing workflow: {p}")
        continue
    text=p.read_text(encoding="utf-8")
    if "\t" in text:
        errors.append(f"{name}: tab character found")
    for token in ["actions/checkout@v4","actions/setup-python@v5","python-version: \"3.12\""]:
        if token not in text:
            errors.append(f"{name}: missing {token}")

ci=files["ci"].read_text(encoding="utf-8")
for token in ["push:","pull_request:","workflow_dispatch:","release-smoke:"]:
    if token not in ci:
        errors.append(f"ci: missing {token}")
if "libreoffice-writer" not in ci:
    errors.append("ci: LibreOffice not installed before PDF validation")
if ci.find("libreoffice-writer") > ci.find("validate_binary_report_exports.py"):
    errors.append("ci: LibreOffice installation occurs after PDF validation")

release=files["release"].read_text(encoding="utf-8")
for token in [
    "release:",
    "types: [published]",
    "contents: write",
    "GITHUB_REF_NAME",
    "libreoffice-writer",
    "validate_release.py",
    "generate_checksums.py",
    "gh release upload",
    "--clobber",
]:
    if token not in release:
        errors.append(f"release: missing {token}")

upload=release.find("gh release upload")
for token in ["validate_release.py","generate_checksums.py"]:
    pos=release.find(token)
    if pos < 0 or pos > upload:
        errors.append(f"release: {token} must run before upload")

for rel in re.findall(r'python3\s+(scripts/[A-Za-z0-9_.-]+\.py)', ci+"\n"+release):
    if not (ROOT/rel).exists():
        errors.append(f"Referenced script missing: {rel}")

if errors:
    print("WORKFLOW VALIDATION FAILED")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("WORKFLOW VALIDATION OK")
print("ci_triggers=push,pr,manual")
print("release_trigger=published")
print("pdf_runtime=libreoffice-writer")
