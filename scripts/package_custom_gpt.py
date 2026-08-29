#!/usr/bin/env python3
from pathlib import Path
import os, zipfile

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"dist"/"custom-gpt"
version=(os.environ.get("RELEASE_VERSION") or (ROOT/"VERSION").read_text(encoding="utf-8").strip()).lstrip("v")
out=ROOT/"dist"/f"sakerhetsgranskaren-it-stod-custom-gpt-{version}.zip"
if out.exists(): out.unlink()
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
    for p in sorted(SRC.iterdir()):
        if p.is_file(): z.write(p,p.name)
print(out)
