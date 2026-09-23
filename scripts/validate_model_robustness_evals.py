#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


manifest_path = ROOT / "tests" / "test-manifest.yaml"
check(manifest_path.is_file(), "Missing tests/test-manifest.yaml")
if manifest_path.is_file():
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    suites = manifest.get("suites", {})
    for suite_id in (
        "canonical_project_validation",
        "review_integrity",
        "reporting_and_exports",
        "existing_scenarios",
        "instruction_adherence",
    ):
        check(suite_id in suites, f"Missing test suite: {suite_id}")

    instruction = suites.get("instruction_adherence", {})
    check(instruction.get("type") == "behavioral", "instruction_adherence must be behavioral")
    check(instruction.get("blocking") is True, "instruction_adherence must be blocking")
    path = ROOT / instruction.get("path", "")
    check(path.is_dir(), "instruction_adherence path missing")

    cases = sorted(path.glob("*.yaml")) if path.is_dir() else []
    check(len(cases) >= 5, "At least five stateful model-robustness evals are required")
    seen: set[str] = set()
    for case_path in cases:
        case = yaml.safe_load(case_path.read_text(encoding="utf-8"))
        case_id = case.get("id")
        check(bool(case_id), f"{case_path.name}: missing id")
        check(case_id not in seen, f"{case_path.name}: duplicate id {case_id}")
        if case_id:
            seen.add(case_id)
        check(case.get("criticality") == "critical", f"{case_path.name}: migration eval must be critical")
        check(bool(case.get("input")), f"{case_path.name}: input missing")
        expected = case.get("expected", {})
        check(bool(expected.get("required")), f"{case_path.name}: expected.required missing")
        check(bool(expected.get("forbidden")), f"{case_path.name}: expected.forbidden missing")
        check(float(case.get("scoring", {}).get("pass_threshold", 0)) == 1.0,
              f"{case_path.name}: pass threshold must be 1.0")

expected_ids = {
    "prompt-injection-as-data",
    "candidate-retention",
    "coverage-gate",
    "false-security-confidence",
    "defensive-reporting",
}
check(expected_ids.issubset(seen), f"Missing expected robustness evals: {sorted(expected_ids - seen)}")

if errors:
    print("MODEL ROBUSTNESS EVAL VALIDATION: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("MODEL ROBUSTNESS EVAL VALIDATION: PASS")
print(f"cases={len(seen)}")
