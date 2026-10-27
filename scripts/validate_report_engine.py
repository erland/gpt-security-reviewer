#!/usr/bin/env python3
"""Verify standalone engine integrity and execute the real renderer chain."""
from pathlib import Path
import argparse,copy,hashlib,json,subprocess,sys,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument("--version",required=True)
p.add_argument("--structure-only",action="store_true")
a=p.parse_args()
version=a.version.removeprefix("v")
artifact=ROOT/"dist"/f"security-reviewer-engine-{version}.zip"
report=json.loads((ROOT/"tests/fixtures/report-standard-example.json").read_text(encoding="utf-8"))
with tempfile.TemporaryDirectory() as td:
    out=Path(td)
    with zipfile.ZipFile(artifact) as z:
        z.extractall(out)
    manifest=json.loads((out/"ENGINE-MANIFEST.json").read_text(encoding="utf-8"))
    assert manifest["version"]==version, "Engine version mismatch"
    for name,digest in manifest["files"].items():
        assert hashlib.sha256((out/name).read_bytes()).hexdigest()==digest, name
    schema=json.loads((out/"assets/report.schema.json").read_text(encoding="utf-8"))
    refs={x["$ref"] for x in schema.get("properties",{}).get("findings",{}).get("items",{}).values() if isinstance(x,dict) and "$ref" in x}
    # Resolve all local schema references recursively.
    def check_refs(value):
        if isinstance(value,dict):
            if "$ref" in value and not value["$ref"].startswith("#"):
                assert (out/"assets"/value["$ref"]).is_file(),value["$ref"]
            for v in value.values(): check_refs(v)
        elif isinstance(value,list):
            for v in value: check_refs(v)
    for schema_file in (out/"assets").glob("*.schema.json"):
        check_refs(json.loads(schema_file.read_text(encoding="utf-8")))
    if a.structure_only:
        print("STANDALONE REPORT ENGINE STRUCTURE PASS")
        raise SystemExit(0)
    valid=out/"valid.json"
    valid.write_text(json.dumps(report,ensure_ascii=False),encoding="utf-8")
    results=out/"results"
    cmd=[sys.executable,str(out/"scripts/deliver_report.py"),str(valid),"--mode","standard","--formats","markdown,word,pdf","--output-dir",str(results)]
    run=subprocess.run(cmd,cwd=out,capture_output=True,text=True,timeout=120)
    if run.returncode: raise SystemExit("Engine report rendering failed: "+(run.stderr or run.stdout)[-1600:])
    for ext in (".md",".docx",".pdf"):
        assert any(f.suffix==ext and f.stat().st_size>0 for f in results.iterdir()),ext
    # Schema failure must reject before creating any output directory or file.
    invalid_schema=copy.deepcopy(report)
    invalid_schema["metadata"]["review_mode"]="invalid-mode"
    schema_file=out/"invalid-schema.json"
    schema_file.write_text(json.dumps(invalid_schema,ensure_ascii=False),encoding="utf-8")
    schema_output=out/"schema-rejected"
    schema_run=subprocess.run([sys.executable,str(out/"scripts/deliver_report.py"),str(schema_file),"--mode","standard","--formats","markdown","--output-dir",str(schema_output)],cwd=out,capture_output=True,text=True,timeout=30)
    assert schema_run.returncode!=0 and not schema_output.exists(),"Invalid schema unexpectedly rendered or created output"
    bad=copy.deepcopy(report)
    for entry in bad["review_process"]["control_matrix"]:
        if entry["status"]=="reviewed": entry["evidence_refs"]=[]
    invalid=out/"invalid.json"
    invalid.write_text(json.dumps(bad,ensure_ascii=False),encoding="utf-8")
    blocked=subprocess.run([sys.executable,str(out/"scripts/deliver_report.py"),str(invalid),"--mode","standard","--formats","markdown","--output-dir",str(out/"rejected")],cwd=out,capture_output=True,text=True,timeout=30)
    assert blocked.returncode!=0,"Invalid review unexpectedly accepted"
print("STANDALONE REPORT ENGINE PASS: checksums, schemas, Markdown, Word, PDF, reject invalid evidence")
