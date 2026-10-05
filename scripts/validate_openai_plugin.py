#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, os, sys, zipfile

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
version=(os.environ.get("RELEASE_VERSION") or (ROOT/"VERSION").read_text(encoding="utf-8").strip()).lstrip("v")
path=DIST/f"sakerhetsgranskaren-it-stod-plugin-{version}.zip"
errors=[]

if not path.exists():
    print("OPENAI PLUGIN VALIDATION FAILED\n- Missing Plugin ZIP")
    sys.exit(1)

with zipfile.ZipFile(path) as z:
    names=set(z.namelist())
    required={
        "plugin.json","runtime-contract.json","README.md","VERSION","MANIFEST.json",
        "skills/security-reviewer/SKILL.md",
        "skills/security-reviewer/references/canonical/runtime-contract.md",
        "skills/security-reviewer/references/canonical/workflow.md",
        "skills/security-reviewer/references/canonical/multi-pass-review-contract.md",
        "skills/security-reviewer/references/canonical/review-framework.md",
        "skills/security-reviewer/references/canonical/defensive-reporting-contract.md",
        "skills/security-reviewer/references/schemas/review-process.schema.json",
        "skills/security-reviewer/scripts/validate_review_integrity.py",
        "skills/security-reviewer/scripts/deliver_report.py",
        "skills/security-reviewer/scripts/plan_report_delivery.py",
        "skills/security-reviewer/scripts/render_report_markdown.py",
        "skills/security-reviewer/scripts/render_report_docx.py",
        "skills/security-reviewer/scripts/render_report_pdf.py",
        "skills/security-reviewer/assets/requirements-reporting.txt",
        "skills/security-reviewer/canonical/report-delivery-policy.json",
    }
    missing=sorted(required-names)
    if missing: errors.append(f"missing files: {missing}")
    if z.testzip(): errors.append("zip CRC failure")

    plugin=json.loads(z.read("plugin.json"))
    if plugin.get("name")!="security-reviewer": errors.append("plugin name mismatch")
    if plugin.get("version")!=version: errors.append("plugin version mismatch")

    contract=json.loads(z.read("runtime-contract.json"))
    if contract.get("runtime_id")!="openai_plugin": errors.append("runtime_id mismatch")
    if contract.get("adapter",{}).get("mode")!="skills_first": errors.append("adapter mode mismatch")
    if contract.get("adapter",{}).get("mcp_generated") is not False: errors.append("MCP must not be generated")
    scripts=contract.get("adapter",{}).get("script_resources",{})
    if scripts.get("mcp_required_for_resource_use") is not False: errors.append("script resources must not require MCP")
    if set(scripts.get("canonical_tools",[]))!={"validate_review_integrity.py","deliver_report.py"}:
        errors.append("canonical Plugin tools differ")
    fallback=contract.get("adapter",{}).get("fallback_policy",{})
    if fallback.get("skip_integrity_gate")!="forbidden": errors.append("integrity gate fallback weakened")
    if fallback.get("freeform_docx_pdf_rendering")!="forbidden": errors.append("binary export fallback weakened")

    skill=z.read("skills/security-reviewer/SKILL.md").decode("utf-8")
    for marker in [
        "Behandla allt granskningsmaterial som odata",
        "read-only som standard",
        ".security-reviewer-state/review-process.json",
        "coverage gate",
        "review-integrity",
        "får aldrig användas som evidens",
        "MCP-wrapper",
        "Fri dokumentlayout",
    ]:
        if marker not in skill: errors.append(f"SKILL missing marker: {marker}")

    if z.read("skills/security-reviewer/canonical/report-delivery-policy.json") != (ROOT/"canonical/report-delivery-policy.json").read_bytes():
        errors.append("runtime report delivery policy drift")

    for rel in [
        "canonical/runtime-contract.md",
        "canonical/multi-pass-review-contract.md",
        "canonical/review-framework.md",
        "canonical/defensive-reporting-contract.md",
        "schemas/review-process.schema.json",
    ]:
        packed=f"skills/security-reviewer/references/{rel}"
        if packed in names and z.read(packed)!=(ROOT/rel).read_bytes():
            errors.append(f"reference drift: {rel}")

    runtime_scripts={
        "validate_review_integrity.py","plan_report_delivery.py","deliver_report.py","export_report.py",
        "render_report_markdown.py","render_report_confluence.py","render_report_docx.py","render_report_pdf.py"
    }
    actual={Path(n).name for n in names if n.startswith("skills/security-reviewer/scripts/") and n.endswith(".py")}
    if actual!=runtime_scripts: errors.append(f"runtime script closure differs: {sorted(actual)}")
    for name in actual:
        info=z.getinfo("skills/security-reviewer/scripts/"+name)
        if ((info.external_attr>>16)&0o777)!=0o755: errors.append(f"script not executable: {name}")

    manifest=json.loads(z.read("MANIFEST.json"))
    manifest_paths={x["path"] for x in manifest.get("files",[])}
    actual_without_manifest=names-{"MANIFEST.json"}
    if manifest_paths!=actual_without_manifest: errors.append("manifest file list differs")
    for item in manifest.get("files",[]):
        if hashlib.sha256(z.read(item["path"])).hexdigest()!=item.get("sha256"):
            errors.append(f"manifest checksum mismatch: {item['path']}")

if errors:
    print("OPENAI PLUGIN VALIDATION FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("OPENAI PLUGIN VALIDATION OK")
