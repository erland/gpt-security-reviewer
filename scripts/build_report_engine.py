#!/usr/bin/env python3
"""Create standalone, versioned runtime engine from the generated Plugin Skill."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument("--version", required=True)
a = p.parse_args()
version = a.version.removeprefix("v")
dist = ROOT / "dist"
plugin = dist / f"security-reviewer-plugin-{version}.zip"
if not plugin.is_file():
    raise SystemExit(f"Missing Plugin distribution {plugin}")
engine = dist / f"security-reviewer-engine-{version}.zip"
prefix = "skills/security-review/"
payload = {}
with zipfile.ZipFile(plugin) as source:
    for member in source.namelist():
        at = member.find(prefix)
        if at < 0 or member.endswith("/"):
            continue
        relative = member[at + len(prefix):]
        if relative.startswith(("scripts/", "assets/", "references/")):
            payload[relative] = source.read(member)
required = {
    "scripts/deliver_report.py", "scripts/validate_review_integrity.py",
    "scripts/validate_report_schema.py",
    "scripts/plan_report_delivery.py", "scripts/render_report_docx.py",
    "scripts/render_report_pdf.py", "scripts/render_report_markdown.py",
    "assets/report.schema.json", "assets/finding.schema.json",
    "assets/review-process.schema.json", "assets/report-delivery-policy.json",
    "assets/pdf-table-layout.md",
}
missing = sorted(required - payload.keys())
if missing:
    raise SystemExit(f"Incomplete Skill engine: {missing}")
readme = f"""# Security Reviewer standalone report engine {version}

This is the executable companion to Security Reviewer's installed Skill.
It is NOT needed if the host can execute installed Skill scripts directly.

Prerequisites: Python 3, jsonschema for all formats, python-docx for Word, LibreOffice for PDF.
Extract this archive and run:

python3 scripts/deliver_report.py report.json --mode standard --formats markdown,word,pdf --output-dir output

Standard/Deep always invokes the review-integrity gate.
This distribution does not circumvent unavailable code-execution capabilities.
"""
payload["README.md"] = readme.encode("utf-8")
payload["ENGINE-MANIFEST.json"] = json.dumps({
    "engine": "security-reviewer", "version": version,
    "files": {name: hashlib.sha256(data).hexdigest() for name, data in sorted(payload.items())}
}, indent=2).encode("utf-8")
with zipfile.ZipFile(engine, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for name, data in sorted(payload.items()):
        info = zipfile.ZipInfo(name, date_time=(2020,1,1,0,0,0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, data)
print(engine)
