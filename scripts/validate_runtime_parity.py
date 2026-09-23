#!/usr/bin/env python3
from pathlib import Path
import json,sys,yaml

ROOT=Path(__file__).resolve().parents[1]
errors=[]
cfg=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
parity=yaml.safe_load((ROOT/"runtime-parity.yaml").read_text(encoding="utf-8"))
expected={"chatgpt_chat","chatgpt_custom","claude_project","opencode","openai_plugin"}
categories={"behavior","capability","artifact","workspace_state","tool"}

if set(parity.get("registered_runtimes",[]))!=expected:
    errors.append("runtime parity must register all five runtimes")
if set(parity.get("compared_categories",[]))!=categories:
    errors.append("runtime parity categories differ")

candidates={x["runtime_id"]:x for x in cfg["analysis"]["runtime"]["candidates"]}
if set(candidates)!=expected:
    errors.append("project runtime candidates differ")

active={"chatgpt_chat","chatgpt_custom","opencode"}
for rid in active:
    if candidates[rid].get("suitability")!="ready" or candidates[rid].get("activate_by_default") is not True:
        errors.append(f"{rid}: project assessment not ready/active")
    p=parity["runtimes"][rid]
    if p.get("suitability")!="ready" or p.get("active") is not True:
        errors.append(f"{rid}: parity assessment not ready/active")

for rid in {"claude_project","openai_plugin"}:
    if candidates[rid].get("suitability")!="reduced" or candidates[rid].get("activate_by_default") is not False:
        errors.append(f"{rid}: project assessment not reduced/inactive")
    p=parity["runtimes"][rid]
    if p.get("suitability")!="reduced" or p.get("active") is not False:
        errors.append(f"{rid}: parity assessment not reduced/inactive")

required_common={
    "behavior":{"canonical":"canonical/runtime-contract.md","workflow":"canonical/workflow.md","stateful_standard_deep":True,"review_state_schema":"schemas/review-process.schema.json"},
    "capabilities":{"filesystem_read":"required","filesystem_write":"recommended","shell":"recommended","code_execution":"recommended","structured_data":"required","persistent_state":"required","web":"optional"},
    "artifacts":{"review_report":"required","review_data":"required","confluence_report":"conditional","word_report":"conditional","pdf_report":"conditional","runtime_package":"required","project_package":"required"},
    "workspace_state":{"workspace":"required","separate_from_assistant":True,"state":"required","authority":"workspace_file","schema":"schemas/review-process.schema.json"},
    "tools":{"review_integrity":"required","report_delivery":"required"}
}
for rid,path in {
    "chatgpt_chat":"runtime-contracts/chatgpt-chat.json",
    "chatgpt_custom":"runtime-contracts/chatgpt-custom.json",
    "opencode":"runtime-contracts/opencode.json",
}.items():
    data=json.loads((ROOT/path).read_text(encoding="utf-8"))
    if data.get("runtime_id")!=rid:
        errors.append(f"{rid}: wrong runtime_id")
    for key,val in required_common.items():
        if data.get(key)!=val:
            errors.append(f"{rid}: {key} contract drift")

if errors:
    print("RUNTIME PARITY VALIDATION FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("RUNTIME PARITY VALIDATION OK")
print("active=chatgpt_chat,chatgpt_custom,opencode")
print("reduced=claude_project,openai_plugin")
