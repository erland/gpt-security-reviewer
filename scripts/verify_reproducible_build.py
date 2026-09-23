#!/usr/bin/env python3
from pathlib import Path
import hashlib, os, shutil, subprocess, sys, tempfile

ROOT=Path(__file__).resolve().parents[1]
version=(os.environ.get("RELEASE_VERSION") or (ROOT/"VERSION").read_text(encoding="utf-8").strip()).lstrip("v")

def snapshot(dist: Path):
    names=[
        f"sakerhetsgranskaren-it-stod-project-{version}.zip",
        f"sakerhetsgranskaren-it-stod-chat-{version}.zip",
        f"sakerhetsgranskaren-it-stod-custom-gpt-{version}.zip",
        f"sakerhetsgranskaren-it-stod-opencode-{version}.zip",
        f"sakerhetsgranskaren-it-stod-{version}-SHA256SUMS.txt",
        f"sakerhetsgranskaren-it-stod-{version}-DELIVERY-MANIFEST.json",
    ]
    out={}
    for name in names:
        p=dist/name
        if not p.exists():
            raise SystemExit(f"REPRODUCIBILITY FAILED\n- missing {name}")
        out[name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return out

def build_once(target: Path):
    env=os.environ.copy()
    env["RELEASE_VERSION"]=version
    dist=ROOT/"dist"
    if dist.exists():
        for p in dist.iterdir():
            if p.name!=".gitkeep":
                if p.is_dir(): shutil.rmtree(p)
                else: p.unlink()
    commands=[
        "scripts/build_chat_zip.py",
        "scripts/build_custom_gpt.py",
        "scripts/package_custom_gpt.py",
        "scripts/build_opencode.py",
        "scripts/build_project_package.py",
        "scripts/generate_checksums.py",
        "scripts/build_delivery_manifest.py",
    ]
    for rel in commands:
        subprocess.run([sys.executable,str(ROOT/rel)],cwd=ROOT,env=env,check=True)
    target.mkdir(parents=True,exist_ok=True)
    for p in dist.iterdir():
        if p.is_file() and p.name!=".gitkeep":
            shutil.copy2(p,target/p.name)
    return snapshot(target)

with tempfile.TemporaryDirectory() as td:
    a=build_once(Path(td)/"first")
    b=build_once(Path(td)/"second")
    if a!=b:
        print("REPRODUCIBILITY FAILED")
        for name in sorted(set(a)|set(b)):
            if a.get(name)!=b.get(name):
                print(f"- {name}: {a.get(name)} != {b.get(name)}")
        sys.exit(1)

print("REPRODUCIBILITY OK")
