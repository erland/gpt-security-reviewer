#!/usr/bin/env python3
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "tests" / "scenarios"
INDEX = SCENARIOS / "index.json"
errors = []

valid_classes = {"positive", "negative", "uncertainty", "architecture", "recommendation"}
required_sections = ["## Class", "## Tags", "## Input", "## Expected"]

try:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
except Exception as e:
    print(f"TEST VALIDATION FAILED\n- Invalid or missing index: {e}")
    sys.exit(1)

items = data.get("scenarios", [])
if not items:
    errors.append("No indexed scenarios")

ids = [x.get("id") for x in items]
if len(ids) != len(set(ids)):
    errors.append("Duplicate scenario ids")

counts = {}
for item in items:
    rel = item.get("file")
    cls = item.get("class")
    if cls not in valid_classes:
        errors.append(f"{item.get('id')}: invalid class {cls!r}")
    else:
        counts[cls] = counts.get(cls, 0) + 1

    if not rel:
        errors.append(f"{item.get('id')}: missing file")
        continue
    p = ROOT / rel
    if not p.exists():
        errors.append(f"{item.get('id')}: file missing: {rel}")
        continue
    txt = p.read_text(encoding="utf-8")
    for sec in required_sections:
        if sec not in txt:
            errors.append(f"{rel} missing section: {sec}")
    if f"## Class\n{cls}" not in txt:
        errors.append(f"{rel} class does not match index")

for required_class in ["positive", "negative", "uncertainty", "recommendation"]:
    if counts.get(required_class, 0) == 0:
        errors.append(f"No indexed scenarios of class {required_class}")

if errors:
    print("TEST VALIDATION FAILED")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("TEST VALIDATION OK")
for k in sorted(counts):
    print(f"- {k}: {counts[k]}")
print(f"- total indexed: {len(items)}")
