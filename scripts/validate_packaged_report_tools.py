#!/usr/bin/env python3
"""Smoke-test report delivery inside each built runtime Skill ZIP.

This deliberately executes extracted archive scripts, not repository source scripts.
"""
from pathlib import Path
import json
import os
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = (os.environ.get("RELEASE_VERSION") or (ROOT / "VERSION").read_text(encoding="utf-8").strip()).lstrip("v")
FIXTURE = ROOT / "tests" / "fixtures" / "report-export-example.json"
REQUIRED = {
    "deliver_report.py",
    "validate_review_integrity.py",
    "plan_report_delivery.py",
    "render_report_markdown.py",
    "render_report_confluence.py",
    "render_report_docx.py",
    "render_report_pdf.py",
}
ERRORS = []

for target in ("chat", "plugin", "claude-skills", "opencode"):
    package = ROOT / "dist" / f"security-reviewer-{target}-{VERSION}.zip"
    if not package.is_file():
        ERRORS.append(f"{target}: missing archive {package.name}")
        continue
    with tempfile.TemporaryDirectory(prefix=f"report-{target}-") as temp:
        folder = Path(temp)
        with zipfile.ZipFile(package) as archive:
            archive.extractall(folder)
        runners = sorted(folder.rglob("deliver_report.py"))
        if not runners:
            ERRORS.append(f"{target}: missing packaged report runner")
            continue
        for runner in runners:
            if "skills" in runner.parts:
                scripts = runner.parent
                missing = REQUIRED - {p.name for p in scripts.glob("*.py")}
                policy = scripts.parent / "assets" / "report-delivery-policy.json"
                if missing or not policy.is_file():
                    ERRORS.append(f"{target}: missing Skill dependencies {sorted(missing)}; policy={policy.is_file()}")
                    continue
            output = folder / ("out-" + str(len(ERRORS)))
            result = subprocess.run(
                [sys.executable, str(runner), str(FIXTURE), "--mode", "quick",
                 "--formats", "markdown", "--output-dir", str(output)],
                text=True, capture_output=True, cwd=folder, timeout=45,
            )
            if result.returncode:
                ERRORS.append(f"{target}: report runner failed: {(result.stderr or result.stdout)[-1000:]}")
                continue
            try:
                payload = json.loads(result.stdout)
                if not payload.get("created") or not list(output.glob("*.md")):
                    ERRORS.append(f"{target}: report script did not produce Markdown output")
            except ValueError:
                ERRORS.append(f"{target}: report script did not return JSON")
    print(f"{target}: checked extracted Skill report engine")

if ERRORS:
    print("PACKAGED REPORT TOOLS FAILED")
    for error in ERRORS:
        print("-", error)
    sys.exit(1)
print("PACKAGED REPORT TOOLS PASS")
