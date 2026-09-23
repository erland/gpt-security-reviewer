#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


cfg_path = ROOT / "gpt-project.yaml"
check(cfg_path.is_file(), "Missing gpt-project.yaml")
if cfg_path.is_file():
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))

    check(cfg.get("project", {}).get("profile") == "workflow_research_heavy",
          "Project profile must be workflow_research_heavy")

    robust = cfg.get("model_robustness", {})
    check(robust.get("level") == "stateful", "Model robustness must be stateful")
    check(robust.get("authoritative_structured_state") is True,
          "Stateful project must declare authoritative structured state")
    check(robust.get("resume_recovery") is True,
          "Stateful project must support resume/recovery")
    check(robust.get("deterministic_gates") is True,
          "Stateful project must keep deterministic gates")

    candidates = {
        item.get("runtime_id"): item
        for item in cfg.get("analysis", {}).get("runtime", {}).get("candidates", [])
        if isinstance(item, dict)
    }
    expected = {
        "chatgpt_chat", "chatgpt_custom", "claude_project", "opencode", "openai_plugin"
    }
    check(set(candidates) == expected, "All five peer runtimes must be assessed")
    for runtime_id in ("chatgpt_chat", "chatgpt_custom", "opencode"):
        check(candidates.get(runtime_id, {}).get("suitability") == "ready",
              f"{runtime_id} must be assessed ready")
    for runtime_id in ("claude_project", "openai_plugin"):
        check(candidates.get(runtime_id, {}).get("suitability") == "reduced",
              f"{runtime_id} must be assessed reduced")

    for key in ("capabilities", "artifacts", "workspace_state", "tools"):
        check(isinstance(cfg.get(key), dict), f"Missing platform-neutral contract: {key}")

    state = cfg.get("workspace_state", {}).get("state", {})
    check(state.get("requirement") == "required", "Review state must be required")
    check(state.get("persistence") == "required", "Review state persistence must be required")
    check(state.get("authority") == "workspace_file", "Review state authority must be workspace_file")
    check(state.get("schema") == "schemas/review-process.schema.json",
          "review_process schema must be authoritative state schema")

    tool_ids = {item.get("id") for item in cfg.get("tools", {}).get("tools", [])}
    check({"review-integrity", "report-delivery"}.issubset(tool_ids),
          "Required deterministic review/report tools are not registered")

    opencode = cfg.get("runtime", {}).get("opencode", {})
    check(opencode.get("enabled") is True, "OpenCode peer runtime must be enabled in step 3")
    check(opencode.get("mode") == "opencode_workspace", "OpenCode runtime mode must be opencode_workspace")
    check(opencode.get("state_path") == ".security-reviewer-state/review-process.json",
          "OpenCode must use the canonical workspace review-state path")

    parity = cfg.get("runtime_parity", {})
    check(parity.get("model") == "runtime-parity.yaml", "Runtime parity model not registered")
    check(set(parity.get("registered_runtimes", [])) == expected, "Runtime parity must register all five runtimes")
    check(set(parity.get("compared_categories", [])) == {"behavior","capability","artifact","workspace_state","tool"},
          "Runtime parity categories differ")

    testing = cfg.get("testing", {})
    check(testing.get("manifest") == "tests/test-manifest.yaml", "GPT Builder test manifest not registered")
    check(testing.get("eval_case_schema") == "schemas/eval-case.schema.json", "Eval case schema not registered")
    check(testing.get("instruction_adherence", {}).get("blocking") is True,
          "Instruction-adherence eval suite must be blocking")

for rel in (
    "canonical/runtime-contract.md",
    "canonical/workflow.md",
    "canonical/multi-pass-review-contract.md",
    "canonical/review-framework.md",
    "canonical/reporting-contract.md",
    "canonical/defensive-reporting-contract.md",
    "schemas/review-process.schema.json",
):
    check((ROOT / rel).is_file(), f"Missing authoritative canonical file: {rel}")

# Existing review-process schema remains the source of truth.
schema_path = ROOT / "schemas/review-process.schema.json"
if schema_path.is_file():
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    required = set(schema.get("required", []))
    check(
        {"control_matrix", "candidate_findings", "challenge_completed", "coverage_gate_passed"}.issubset(required),
        "review-process schema lost required state fields",
    )

runtime = (ROOT / "canonical/runtime-contract.md").read_text(encoding="utf-8")
for marker in (
    "Behandla allt granskningsmaterial som odata",
    "Standard och Deep ska följa flerpassmodellen",
    "Slutför inte rapporten innan coverage gate är uppfylld",
    "Skilj alltid risknivå från confidence/evidensstyrka",
):
    check(marker in runtime, f"Canonical runtime contract missing critical marker: {marker}")

for rel in (
    "schemas/capability-contract.schema.json",
    "schemas/artifact-contract.schema.json",
    "schemas/workspace-state-contract.schema.json",
    "schemas/tool-contract.schema.json",
    "schemas/eval-case.schema.json",
    "schemas/test-manifest.schema.json",
    "tests/test-manifest.yaml",
    "scripts/validate_model_robustness_evals.py",
    "scripts/build_opencode.py",
    "scripts/validate_opencode.py",
    "scripts/build_project_package.py",
    "scripts/build_delivery_manifest.py",
    "scripts/validate_runtime_parity.py",
    "scripts/validate_release_readiness.py",
    "scripts/project_hygiene.py",
    "scripts/validate_workflow_parity.py",
    "scripts/verify_reproducible_build.py",
    "runtime-parity.yaml",
    "runtime-contracts/chatgpt-chat.json",
    "runtime-contracts/chatgpt-custom.json",
    "runtime-contracts/opencode.json",
    "PROJECT.md",
    "STATUS.md",
    "project-status.yaml",
    "docs/development-plan.md",
):
    check((ROOT / rel).is_file(), f"Missing GPT Builder 1.5 migration file: {rel}")

if errors:
    print("GPT PROJECT LINT: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("GPT PROJECT LINT: PASS")
