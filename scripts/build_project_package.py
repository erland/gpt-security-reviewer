#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, os, shutil, tempfile, zipfile

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
DIST.mkdir(exist_ok=True)
version=(os.environ.get("RELEASE_VERSION") or (ROOT/"VERSION").read_text(encoding="utf-8").strip()).lstrip("v")
out=DIST/f"sakerhetsgranskaren-it-stod-project-{version}.zip"
FIXED=(2020,1,1,0,0,0)

include_dirs=["canonical","knowledge","schemas","scripts","tests","docs","chat","custom-gpt","runtime-contracts",".github/workflows"]
include_files=[
    "README.md","VERSION","gpt-project.yaml","project-status.yaml","PROJECT.md","STATUS.md",
    "runtime-parity.yaml","requirements-reporting.txt"
]

with tempfile.TemporaryDirectory() as td:
    stage=Path(td)/"project"
    stage.mkdir()
    for rel in include_dirs:
        src=ROOT/rel
        if src.exists():
            shutil.copytree(src,stage/rel,ignore=shutil.ignore_patterns("__pycache__",".pytest_cache","*.pyc"))
    for rel in include_files:
        src=ROOT/rel
        if src.exists():
            dst=stage/rel
            dst.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(src,dst)
    (stage/"VERSION").write_text(version+"\n",encoding="utf-8")

    files=[]
    for p in sorted(x for x in stage.rglob("*") if x.is_file()):
        rel=p.relative_to(stage).as_posix()
        files.append({"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"bytes":p.stat().st_size})
    manifest={"name":"Säkerhetsgranskaren för IT-stöd","distribution":"project","version":version,"start_file":"gpt-project.yaml","file_count":len(files),"files":files}
    (stage/"MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    if out.exists(): out.unlink()
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(x for x in stage.rglob("*") if x.is_file()):
            info=zipfile.ZipInfo(p.relative_to(stage).as_posix(),FIXED)
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print(out)
