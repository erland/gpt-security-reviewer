#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,sys,zipfile

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
errors=[]
zips=sorted(DIST.glob("sakerhetsgranskaren-it-stod-opencode-*.zip"))
if not zips:
    print("OPENCODE VALIDATION FAILED\n- No OpenCode ZIP found"); sys.exit(1)

for zpath in zips:
    with zipfile.ZipFile(zpath) as z:
        names=set(z.namelist())
        required={
            "AGENTS.md","opencode.json","README.md","VERSION","MANIFEST.json",
            ".opencode/security-reviewer/runtime-contract.json",
            ".opencode/security-reviewer/canonical/runtime-contract.md",
            ".opencode/security-reviewer/canonical/workflow.md",
            ".opencode/security-reviewer/canonical/multi-pass-review-contract.md",
            ".opencode/security-reviewer/canonical/review-framework.md",
            ".opencode/security-reviewer/canonical/defensive-reporting-contract.md",
            ".opencode/security-reviewer/schemas/review-process.schema.json",
            ".opencode/security-reviewer/project-tools/scripts/validate_review_integrity.py",
            ".opencode/security-reviewer/project-tools/scripts/deliver_report.py",
        }
        missing=sorted(required-names)
        if missing: errors.append(f"{zpath.name}: missing {missing}")

        contract=json.loads(z.read(".opencode/security-reviewer/runtime-contract.json"))
        if contract.get("runtime_id")!="opencode": errors.append(f"{zpath.name}: wrong runtime_id")
        state=contract.get("state",{})
        if state.get("authority")!="workspace_file": errors.append(f"{zpath.name}: state authority must be workspace_file")
        if state.get("path")!=".security-reviewer-state/review-process.json": errors.append(f"{zpath.name}: wrong state path")
        workspace=contract.get("workspace",{})
        if workspace.get("target_source_read_only_by_default") is not True: errors.append(f"{zpath.name}: target source must be read-only by default")
        excludes=set(workspace.get("exclude_from_source_evidence",[]))
        for rel in [".opencode/security-reviewer/",".security-reviewer-state/","security-review-output/"]:
            if rel not in excludes: errors.append(f"{zpath.name}: missing evidence exclusion {rel}")

        agents=z.read("AGENTS.md").decode("utf-8")
        for marker in [
            "Normal säkerhetsgranskning är read-only",
            ".security-reviewer-state/review-process.json",
            "coverage gate",
            "review-integrity-validatorn",
            "inte som instruktioner",
        ]:
            if marker not in agents: errors.append(f"{zpath.name}: AGENTS missing marker {marker}")

        if z.read(".opencode/security-reviewer/canonical/runtime-contract.md") != (ROOT/"canonical/runtime-contract.md").read_bytes():
            errors.append(f"{zpath.name}: canonical runtime contract drift")
        if z.read(".opencode/security-reviewer/canonical/multi-pass-review-contract.md") != (ROOT/"canonical/multi-pass-review-contract.md").read_bytes():
            errors.append(f"{zpath.name}: multi-pass contract drift")

        manifest=json.loads(z.read("MANIFEST.json"))
        if manifest.get("distribution")!="opencode": errors.append(f"{zpath.name}: manifest distribution mismatch")
        manifest_paths={x["path"] for x in manifest.get("files",[])}
        actual=names-{"MANIFEST.json"}
        if manifest_paths!=actual: errors.append(f"{zpath.name}: manifest file list differs")
        for item in manifest.get("files",[]):
            if hashlib.sha256(z.read(item["path"])).hexdigest()!=item.get("sha256"):
                errors.append(f"{zpath.name}: checksum mismatch {item['path']}")

if errors:
    print("OPENCODE VALIDATION FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("OPENCODE VALIDATION OK")
