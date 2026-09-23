#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,os,sys

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
clean=(os.environ.get("RELEASE_VERSION") or (ROOT/"VERSION").read_text().strip()).lstrip("v")
items=[
    ("project_zip",DIST/f"sakerhetsgranskaren-it-stod-project-{clean}.zip"),
    ("chat_zip",DIST/f"sakerhetsgranskaren-it-stod-chat-{clean}.zip"),
    ("custom_gpt_zip",DIST/f"sakerhetsgranskaren-it-stod-custom-gpt-{clean}.zip"),
    ("opencode_zip",DIST/f"sakerhetsgranskaren-it-stod-opencode-{clean}.zip"),
]
missing=[p.name for _,p in items if not p.exists()]
if missing:
    print("Missing delivery artifacts: "+", ".join(missing),file=sys.stderr); sys.exit(1)
payload={
    "schema_version":1,
    "version":clean,
    "artifacts":[
        {"type":kind,"file":p.name,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size}
        for kind,p in items
    ],
    "runtime_status":{
        "chatgpt_chat":"ready_active",
        "chatgpt_custom":"ready_active",
        "opencode":"ready_active",
        "claude_project":"reduced_inactive",
        "openai_plugin":"reduced_inactive"
    }
}
out=DIST/f"sakerhetsgranskaren-it-stod-{clean}-DELIVERY-MANIFEST.json"
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(out)
