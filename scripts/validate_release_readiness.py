#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,os,subprocess,sys,zipfile

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
clean=(os.environ.get("RELEASE_VERSION") or (ROOT/"VERSION").read_text().strip()).lstrip("v")
errors=[]

r=subprocess.run([sys.executable,str(ROOT/"scripts/validate_runtime_parity.py")],cwd=ROOT)
if r.returncode: errors.append("runtime parity failed")

artifacts=[
    DIST/f"sakerhetsgranskaren-it-stod-project-{clean}.zip",
    DIST/f"sakerhetsgranskaren-it-stod-chat-{clean}.zip",
    DIST/f"sakerhetsgranskaren-it-stod-custom-gpt-{clean}.zip",
    DIST/f"sakerhetsgranskaren-it-stod-opencode-{clean}.zip",
]
delivery=DIST/f"sakerhetsgranskaren-it-stod-{clean}-DELIVERY-MANIFEST.json"
sums=DIST/f"sakerhetsgranskaren-it-stod-{clean}-SHA256SUMS.txt"

for p in artifacts:
    if not p.exists():
        errors.append(f"missing release artifact: {p.name}")
        continue
    try:
        with zipfile.ZipFile(p) as z:
            bad=z.testzip()
            if bad: errors.append(f"CRC error in {p.name}: {bad}")
    except zipfile.BadZipFile:
        errors.append(f"invalid zip: {p.name}")

if not delivery.exists(): errors.append("delivery manifest missing")
else:
    data=json.loads(delivery.read_text(encoding="utf-8"))
    types={x.get("type") for x in data.get("artifacts",[])}
    if types!={"project_zip","chat_zip","custom_gpt_zip","opencode_zip"}:
        errors.append(f"delivery artifact types differ: {sorted(types)}")

checks={}
if not sums.exists(): errors.append("checksum file missing")
else:
    for line in sums.read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest,name=line.split(None,1); checks[name.strip()]=digest
for p in artifacts:
    if p.exists() and checks.get(p.name)!=hashlib.sha256(p.read_bytes()).hexdigest():
        errors.append(f"checksum mismatch: {p.name}")

if errors:
    print("RELEASE READINESS FAILED")
    for e in errors: print("-",e)
    sys.exit(1)
print("RELEASE READINESS OK")
print("version="+clean)
