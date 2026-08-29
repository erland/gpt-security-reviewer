#!/usr/bin/env python3
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    "README.md",
    "scripts/validate_defensive_reporting.py",
    "knowledge/common/defensive-reporting.md",
    "canonical/defensive-reporting-contract.md",
    "scripts/validate_rc_readiness.py",
    "scripts/validate_workflows.py",
    "scripts/validate_system_overview.py",
    "docs/release-checklist.md",
    "RELEASE-NOTES.md",
    "CHANGELOG.md",
    "START-HERE.md",
    "chat/chat-package.json",
    "scripts/package_custom_gpt.py",
    "scripts/generate_checksums.py",
    "scripts/validate_release.py",
    "scripts/validate_custom_gpt.py",
    "custom-gpt/instructions-template.md",
    "custom-gpt/package-config.json",
    "chat/START-HERE.md",
    "VERSION",
    "canonical/runtime-contract.md",
    "canonical/review-framework.md",
    "canonical/reporting-contract.md",
    "scripts/validate_report_model.py",
    "tests/fixtures/report-export-example.json",
    "scripts/validate_report_exports.py",
    "tests/report-delivery-cases.json",
    "scripts/validate_report_semantic_parity.py",
    "scripts/validate_report_workflow.py",
    "scripts/render_chat_summary.py",
    "scripts/deliver_report.py",
    "scripts/plan_report_delivery.py",
    "canonical/report-delivery-policy.json",
    "canonical/report-delivery-workflow.md",
    "scripts/validate_binary_report_exports.py",
    "scripts/render_report_pdf.py",
    "scripts/render_report_docx.py",
    "canonical/report-binary-export-contract.md",
    "scripts/export_report.py",
    "scripts/render_report_confluence.py",
    "scripts/render_report_markdown.py",
    "canonical/report-export-contract.md",
    "schemas/report.schema.json",
    "canonical/report-modes.md",
    "canonical/report-model.md",
    "canonical/workflow.md",
    "schemas/finding.schema.json",
    "schemas/review-summary.schema.json",
    "scripts/validate_tests.py",
    "tests/eval-contract.md",
    "knowledge/common/application-security.md",
    "knowledge/common/evidence-and-risk.md",
    "knowledge/common/architecture-security.md",
    "knowledge/common/browser-security.md",
    "knowledge/common/java-backend-security.md",
    "knowledge/common/data-store-security.md",
    "knowledge/common/deployment-security.md",
    "knowledge/common/input-and-repository-hygiene.md",
    "knowledge/common/authentication.md",
    "knowledge/common/authorization.md",
    "knowledge/common/input-output-and-injection.md",
    "knowledge/common/secrets-and-cryptography.md",
    "knowledge/common/logging-and-error-handling.md",
    "knowledge/common/api-security.md",
    "knowledge/common/dependency-and-supply-chain.md",
    "knowledge/common/sensitive-data-and-privacy.md",
    "docs/manual-review-decision-model.md",
    "tests/scenarios/step4-follow-up-decisions.md",
    "tests/expected/step4-follow-up-rules.md",
    "tests/scenarios/step5-common-security.md",
    "tests/expected/step5-common-security-rules.md",
]

profile_sections = [
    "## Applicability",
    "## High-value review areas",
    "## Code patterns",
    "## Configuration patterns",
    "## Common weaknesses",
    "## Evidence expectations",
    "## Manual verification triggers",
]

errors = []

for rel in required:
    p = ROOT / rel
    if not p.exists():
        errors.append(f"Missing required file: {rel}")
    elif p.is_file() and not p.read_text(encoding="utf-8").strip():
        errors.append(f"Empty required file: {rel}")

for schema_rel in ["schemas/finding.schema.json", "schemas/review-summary.schema.json"]:
    try:
        json.loads((ROOT/schema_rel).read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"Invalid JSON schema {schema_rel}: {e}")

for p in sorted((ROOT/"knowledge/technologies").glob("*.md")):
    txt = p.read_text(encoding="utf-8")
    for section in profile_sections:
        if section not in txt:
            errors.append(f"{p.relative_to(ROOT)} missing section: {section}")

# Step 4 contract checks
framework = (ROOT / "canonical/review-framework.md").read_text(encoding="utf-8")
reporting = (ROOT / "canonical/reporting-contract.md").read_text(encoding="utf-8")
for token in ["confirmed", "probable", "review-point", "critical", "high", "medium", "low", "informational", "Confidence", "Fyndkonsolidering"]:
    if token not in framework:
        errors.append(f"review-framework missing Step 4 token: {token}")
for token in ["SAST", "SCA", "DAST", "penetration-test", "configuration-review", "specialist-review", "Ingen ytterligare djupgranskning"]:
    if token not in reporting:
        errors.append(f"reporting-contract missing Step 4 token: {token}")

finding_schema = json.loads((ROOT / "schemas/finding.schema.json").read_text(encoding="utf-8"))
follow_types = set(finding_schema.get("properties", {}).get("follow_up", {}).get("items", {}).get("properties", {}).get("type", {}).get("enum", []))
expected_follow_types = {"none", "spot-check", "manual-review", "SAST", "SCA", "secrets-scan", "DAST", "penetration-test", "configuration-review", "specialist-review"}
if follow_types != expected_follow_types:
    errors.append("finding.schema.json follow-up type enum does not match canonical Step 4 contract")


# Step 5 common security profile checks
common_profiles = {
    "authentication.md": ["## Security objectives", "## High-value review areas", "## Evidence indicators", "## Common weaknesses", "## False-positive guards", "## Manual verification triggers"],
    "authorization.md": ["## Security objectives", "## High-value review areas", "## Evidence indicators", "## Common weaknesses", "## False-positive guards", "## Manual verification triggers"],
    "input-output-and-injection.md": ["## Security objectives", "## High-value sinks", "## Evidence indicators", "## Common weaknesses", "## False-positive guards", "## Manual verification triggers"],
    "secrets-and-cryptography.md": ["## Security objectives", "## High-value review areas", "## Evidence indicators", "## Common weaknesses", "## False-positive guards", "## Manual verification triggers"],
    "logging-and-error-handling.md": ["## Security objectives", "## High-value review areas", "## Common weaknesses", "## False-positive guards", "## Manual verification triggers"],
    "api-security.md": ["## Security objectives", "## High-value review areas", "## Common weaknesses", "## False-positive guards", "## Manual verification triggers"],
    "dependency-and-supply-chain.md": ["## Security objectives", "## High-value review areas", "## Evidence limits", "## Common weaknesses", "## Follow-up rule", "## Manual verification triggers"],
    "sensitive-data-and-privacy.md": ["## Security objectives", "## High-value review areas", "## Common weaknesses", "## Evidence limits", "## Manual verification triggers"],
}
for filename, sections in common_profiles.items():
    txt = (ROOT / "knowledge/common" / filename).read_text(encoding="utf-8")
    for section in sections:
        if section not in txt:
            errors.append(f"knowledge/common/{filename} missing Step 5 section: {section}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("VALIDATION OK")
print(f"Technology profiles: {len(list((ROOT/'knowledge/technologies').glob('*.md')))}")
