#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT/"dist"/"custom-gpt"
CONFIG = json.loads((ROOT/"custom-gpt/package-config.json").read_text(encoding="utf-8"))
errors=[]

required = {
    CONFIG["output_files"]["instructions"],
    CONFIG["output_files"]["core"],
    CONFIG["output_files"]["common"],
    CONFIG["output_files"]["frontend"],
    CONFIG["output_files"]["backend"],
    CONFIG["output_files"]["data"],
    CONFIG["output_files"]["architecture_deployment"],
    "finding.schema.json",
    "review-summary.schema.json",
    "report.schema.json",
    "VERSION",
    "MANIFEST.json",
}
for name in required:
    p=DIST/name
    if not p.exists(): errors.append(f"Missing: {name}")
    elif not p.read_bytes(): errors.append(f"Empty: {name}")

if not errors:
    manifest=json.loads((DIST/"MANIFEST.json").read_text(encoding="utf-8"))
    instructions=(DIST/CONFIG["output_files"]["instructions"]).read_text(encoding="utf-8")
    if len(instructions)>int(CONFIG["instructions_max_chars"]):
        errors.append("Instructions exceed max")
    knowledge=[p for p in DIST.iterdir() if p.is_file() and p.name not in {CONFIG["output_files"]["instructions"],"VERSION","MANIFEST.json"}]
    if len(knowledge)>int(CONFIG["knowledge_max_files"]):
        errors.append("Knowledge file count exceeds max")

    mf={x["path"]:x for x in manifest.get("files",[])}
    actual={p.name for p in DIST.iterdir() if p.is_file() and p.name!="MANIFEST.json"}
    if set(mf)!=actual:
        errors.append("Manifest file list differs from bundle")

    for name,item in mf.items():
        if hashlib.sha256((DIST/name).read_bytes()).hexdigest()!=item.get("sha256"):
            errors.append(f"Checksum mismatch: {name}")

    for phrase in [
        "Inventera underlaget",
        "Presentera inte spekulation som verifierad sårbarhet",
        "Granskat",
        "Ej verifierbart",
        "penetrationstest",
    ]:
        if phrase not in instructions:
            errors.append(f"Critical instruction missing: {phrase}")

if errors:
    print("CUSTOM GPT VALIDATION FAILED")
    for e in errors: print(f"- {e}")
    sys.exit(1)

print("CUSTOM GPT VALIDATION OK")
print(f"instructions_chars={len((DIST/CONFIG['output_files']['instructions']).read_text(encoding='utf-8'))}")
print(f"knowledge_files={len([p for p in DIST.iterdir() if p.is_file() and p.name not in {CONFIG['output_files']['instructions'],'VERSION','MANIFEST.json'}])}")
