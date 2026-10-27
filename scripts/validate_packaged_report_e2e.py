#!/usr/bin/env python3
"""Acceptance-test the actual extracted Plugin ZIP, including rejected review state."""
from pathlib import Path
import copy
import json
import os
import subprocess
import sys
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[1]
version=(os.environ.get("RELEASE_VERSION") or (ROOT/"VERSION").read_text().strip()).lstrip("v")
package=ROOT/"dist"/f"security-reviewer-plugin-{version}.zip"
fixture=json.loads((ROOT/"tests/fixtures/report-standard-example.json").read_text(encoding="utf-8"))
if not package.is_file():
    raise SystemExit(f"Missing packaged Plugin: {package}")
with tempfile.TemporaryDirectory() as temp:
    root=Path(temp)
    with zipfile.ZipFile(package) as archive:
        archive.extractall(root)
    runner=next(root.rglob("skills/security-review/scripts/deliver_report.py"),None)
    if runner is None:
        raise SystemExit("Missing packaged deliver_report.py")
    assets=runner.parent.parent/"assets"
    for name in ("report-delivery-policy.json","report.schema.json","review-process.schema.json"):
        if not (assets/name).is_file():
            raise SystemExit(f"Missing packaged schema/policy: {name}")
    valid=root/"valid.json"
    valid.write_text(json.dumps(fixture,ensure_ascii=False),encoding="utf-8")
    out=root/"output"
    result=subprocess.run([sys.executable,str(runner),str(valid),"--mode","standard",
                           "--formats","markdown,word,pdf","--output-dir",str(out)],
                          cwd=root,capture_output=True,text=True,timeout=90)
    if result.returncode:
        raise SystemExit("Packaged report pipeline failed: "+(result.stderr or result.stdout)[-1600:])
    for suffix in ("md","docx","pdf"):
        found=list(out.glob("*."+suffix))
        if not found or any(p.stat().st_size==0 for p in found):
            raise SystemExit(f"Missing rendered {suffix}")
    invalid_schema=copy.deepcopy(fixture)
    invalid_schema["metadata"]["review_mode"]="invalid-mode"
    schema_path=root/"invalid-schema.json"
    schema_path.write_text(json.dumps(invalid_schema,ensure_ascii=False),encoding="utf-8")
    schema_output=root/"schema-rejected"
    schema_run=subprocess.run([sys.executable,str(runner),str(schema_path),"--mode","standard","--formats","markdown","--output-dir",str(schema_output)],cwd=root,capture_output=True,text=True,timeout=30)
    if schema_run.returncode==0 or schema_output.exists():
        raise SystemExit("Invalid report schema created output or passed gate")
    bad=copy.deepcopy(fixture)
    for control in bad["review_process"]["control_matrix"]:
        if control["status"]=="reviewed":
            control.pop("evidence_refs",None)
    invalid=root/"invalid.json"
    invalid.write_text(json.dumps(bad,ensure_ascii=False),encoding="utf-8")
    rejected=subprocess.run([sys.executable,str(runner),str(invalid),"--mode","standard",
                             "--formats","markdown","--output-dir",str(root/"rejected")],
                            cwd=root,capture_output=True,text=True,timeout=30)
    if rejected.returncode==0 or list((root/"rejected").glob("*.md")):
        raise SystemExit("Invalid reviewed controls passed integrity gate")
print("PACKAGED REPORT END-TO-END PASS (Markdown/DOCX/PDF, invalid coverage blocked)")
