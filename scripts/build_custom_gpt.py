#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, os, shutil, sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT/"dist"/"custom-gpt"
CONFIG = json.loads((ROOT/"custom-gpt/package-config.json").read_text(encoding="utf-8"))

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir(parents=True)

version = (os.environ.get("RELEASE_VERSION") or (ROOT/"VERSION").read_text(encoding="utf-8").strip()).lstrip("v")

def read(rel):
    return (ROOT/rel).read_text(encoding="utf-8").strip()

def merge(out_name, title, rels):
    parts = [f"# {title}"]
    for rel in rels:
        parts.append(read(rel))
    (DIST/out_name).write_text("\n\n---\n\n".join(parts).strip()+"\n", encoding="utf-8")

instructions = read("custom-gpt/instructions-template.md") + "\n"
max_chars = int(CONFIG["instructions_max_chars"])
if len(instructions) > max_chars:
    print(f"Custom GPT instructions too large: {len(instructions)} > {max_chars}", file=sys.stderr)
    sys.exit(2)
(DIST/CONFIG["output_files"]["instructions"]).write_text(instructions, encoding="utf-8")

merge(CONFIG["output_files"]["core"], "Granskningskärna", [
    "canonical/review-framework.md",
    "canonical/multi-pass-review-contract.md",
    "canonical/reporting-contract.md",
    "canonical/report-model.md",
    "canonical/report-modes.md",
    "canonical/report-export-contract.md",
    "canonical/report-delivery-workflow.md",
    "canonical/defensive-reporting-contract.md",
    "canonical/report-binary-export-contract.md",
    "canonical/workflow.md",
])
merge(CONFIG["output_files"]["common"], "Gemensamma säkerhetsprofiler",
      sorted(str(p.relative_to(ROOT)) for p in (ROOT/"knowledge/common").glob("*.md")))
merge(CONFIG["output_files"]["frontend"], "Frontendprofiler", [
    "knowledge/technologies/frontend-web.md",
    "knowledge/technologies/react.md",
    "knowledge/technologies/angular.md",
])
merge(CONFIG["output_files"]["backend"], "Backendprofiler", [
    "knowledge/technologies/java-jakarta.md",
])
merge(CONFIG["output_files"]["data"], "Data- och sökprofiler", [
    "knowledge/technologies/relational-database.md",
    "knowledge/technologies/oracle.md",
    "knowledge/technologies/postgresql.md",
    "knowledge/technologies/elasticsearch.md",
])
merge(CONFIG["output_files"]["architecture_deployment"], "Arkitektur och deployment", [
    "knowledge/common/architecture-security.md",
    "knowledge/common/deployment-security.md",
    "knowledge/technologies/deployment-container-platform.md",
])

shutil.copy2(ROOT/"schemas/finding.schema.json", DIST/"finding.schema.json")
shutil.copy2(ROOT/"schemas/review-summary.schema.json", DIST/"review-summary.schema.json")
shutil.copy2(ROOT/"schemas/report.schema.json", DIST/"report.schema.json")
(DIST/"VERSION").write_text(version+"\n", encoding="utf-8")

excluded = {CONFIG["output_files"]["instructions"], "VERSION", "MANIFEST.json"}
knowledge_files = [p for p in DIST.iterdir() if p.is_file() and p.name not in excluded]
if len(knowledge_files) > int(CONFIG["knowledge_max_files"]):
    print(f"Too many knowledge files: {len(knowledge_files)}", file=sys.stderr)
    sys.exit(3)

files=[]
for p in sorted(DIST.iterdir()):
    if p.is_file():
        files.append({"path":p.name,"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})

manifest = {
    "name": CONFIG["name"],
    "distribution": "custom-gpt",
    "version": version,
    "instructions_file": CONFIG["output_files"]["instructions"],
    "instructions_chars": len(instructions),
    "instructions_max_chars": max_chars,
    "knowledge_file_count": len(knowledge_files),
    "knowledge_max_files": int(CONFIG["knowledge_max_files"]),
    "files": files,
}
(DIST/"MANIFEST.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

print(DIST)
print(f"instructions_chars={len(instructions)}")
print(f"knowledge_files={len(knowledge_files)}")
