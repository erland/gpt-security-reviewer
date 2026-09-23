#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
ci=(ROOT/".github/workflows/ci.yml").read_text(encoding="utf-8")
release=(ROOT/".github/workflows/release.yml").read_text(encoding="utf-8")
errors=[]

common=[
    "scripts/lint_gpt_project.py",
    "scripts/validate_project.py",
    "scripts/validate_workflows.py",
    "scripts/validate_rc_readiness.py",
    "scripts/validate_multi_pass_review.py",
    "scripts/validate_review_integrity.py",
    "scripts/validate_tests.py",
    "scripts/validate_model_robustness_evals.py",
    "scripts/validate_defensive_reporting.py",
    "scripts/build_chat_zip.py",
    "scripts/build_custom_gpt.py",
    "scripts/validate_custom_gpt.py",
    "scripts/package_custom_gpt.py",
    "scripts/validate_distribution.py",
    "scripts/build_opencode.py",
    "scripts/validate_opencode.py",
]
for token in common:
    if token not in ci: errors.append(f"CI missing common gate: {token}")
    if token not in release: errors.append(f"Release missing common gate: {token}")

release_only=[
    "scripts/build_project_package.py",
    "scripts/validate_runtime_parity.py",
    "scripts/validate_release.py",
    "scripts/generate_checksums.py",
    "scripts/build_delivery_manifest.py",
    "scripts/validate_release_readiness.py",
    "scripts/project_hygiene.py",
    "scripts/validate_workflow_parity.py",
    "scripts/verify_reproducible_build.py",
]
for token in release_only:
    if token not in release:
        errors.append(f"Release missing final gate: {token}")

smoke=ci.split("release-smoke:",1)[1] if "release-smoke:" in ci else ""
for token in [
    "scripts/build_project_package.py",
    "scripts/validate_runtime_parity.py",
    "scripts/validate_release.py",
    "scripts/generate_checksums.py",
    "scripts/build_delivery_manifest.py",
    "scripts/validate_release_readiness.py",
    "scripts/project_hygiene.py",
    "scripts/validate_workflow_parity.py",
    "scripts/verify_reproducible_build.py",
]:
    if token not in smoke:
        errors.append(f"release-smoke missing final gate: {token}")

upload=release.find("gh release upload")
for token in [
    "scripts/validate_runtime_parity.py",
    "scripts/validate_release_readiness.py",
    "scripts/project_hygiene.py",
    "scripts/validate_workflow_parity.py",
    "scripts/verify_reproducible_build.py",
]:
    pos=release.find(token)
    if pos<0 or pos>upload:
        errors.append(f"{token} must execute before release upload")

if errors:
    print("WORKFLOW PARITY FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("WORKFLOW PARITY OK")
