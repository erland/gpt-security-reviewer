#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
errors = []

chat_zips = sorted(DIST.glob("sakerhetsgranskaren-it-stod-chat-*.zip"))
if not chat_zips:
    print("DISTRIBUTION VALIDATION FAILED")
    print("- No Chat ZIP found")
    sys.exit(1)

for zpath in chat_zips:
    with zipfile.ZipFile(zpath) as z:
        names = set(z.namelist())

        required = {
            "START-HERE.md",
            "VERSION",
            "MANIFEST.json",
            "runtime/instructions.md",
            "runtime/workflow.md",
            "runtime/review-framework.md",
            "runtime/reporting-contract.md",
            "runtime/report-model.md",
            "runtime/report-modes.md",
            "schemas/report.schema.json",
            "schemas/finding.schema.json",
            "schemas/review-summary.schema.json",
        }
        for rel in required:
            if rel not in names:
                errors.append(f"{zpath.name}: missing {rel}")

        forbidden_prefixes = (
            ".github/",
            "tests/",
            "scripts/",
            "docs/",
            "dist/",
            "canonical/",
            "chat/",
        )
        for name in names:
            if name.startswith(forbidden_prefixes):
                errors.append(f"{zpath.name}: development-only path leaked into Chat ZIP: {name}")

        try:
            manifest = json.loads(z.read("MANIFEST.json").decode("utf-8"))
        except Exception as e:
            errors.append(f"{zpath.name}: invalid MANIFEST.json: {e}")
            continue

        if manifest.get("start_file") != "START-HERE.md":
            errors.append(f"{zpath.name}: invalid start_file in manifest")

        manifest_paths = {x["path"] for x in manifest.get("files", [])}
        actual_without_manifest = names - {"MANIFEST.json"}
        if manifest_paths != actual_without_manifest:
            errors.append(f"{zpath.name}: manifest file list differs from ZIP content")

        for item in manifest.get("files", []):
            path = item["path"]
            if path not in names:
                errors.append(f"{zpath.name}: manifest path missing: {path}")
                continue
            digest = hashlib.sha256(z.read(path)).hexdigest()
            if digest != item.get("sha256"):
                errors.append(f"{zpath.name}: checksum mismatch for {path}")

        common_count = len([n for n in names if n.startswith("knowledge/common/") and n.endswith(".md")])
        tech_count = len([n for n in names if n.startswith("knowledge/technologies/") and n.endswith(".md")])
        if common_count < 3:
            errors.append(f"{zpath.name}: too few common knowledge modules ({common_count})")
        if tech_count < 9:
            errors.append(f"{zpath.name}: too few technology profiles ({tech_count})")

        print(f"{zpath.name}: {len(names)} files, common={common_count}, tech={tech_count}")

if errors:
    print("DISTRIBUTION VALIDATION FAILED")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("DISTRIBUTION VALIDATION OK")
