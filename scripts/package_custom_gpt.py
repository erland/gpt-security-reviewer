#!/usr/bin/env python3
from pathlib import Path
import os, zipfile

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"dist"/"custom-gpt"
version=(os.environ.get("RELEASE_VERSION") or (ROOT/"VERSION").read_text(encoding="utf-8").strip()).lstrip("v")
out=ROOT/"dist"/f"sakerhetsgranskaren-it-stod-custom-gpt-{version}.zip"
FIXED_ZIP_TIME=(2020,1,1,0,0,0)

if out.exists(): out.unlink()
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(SRC.iterdir()):
        if p.is_file():
            info=zipfile.ZipInfo(p.name,FIXED_ZIP_TIME)
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
print(out)
