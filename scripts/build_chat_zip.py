#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json
import os
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
STAGE = DIST / "chat-package"
DIST.mkdir(exist_ok=True)

version = os.environ.get("RELEASE_VERSION") or (ROOT / "VERSION").read_text(encoding="utf-8").strip()
version = version.lstrip("v")
out = DIST / f"sakerhetsgranskaren-it-stod-chat-{version}.zip"

if STAGE.exists():
    shutil.rmtree(STAGE)
STAGE.mkdir(parents=True)

def copy(src_rel, dst_rel=None):
    src = ROOT / src_rel
    dst = STAGE / (dst_rel or src_rel)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

# Entry point and runtime contract.
copy("chat/START-HERE.md", "START-HERE.md")
copy("canonical/runtime-contract.md", "runtime/instructions.md")
copy("canonical/workflow.md", "runtime/workflow.md")
copy("canonical/review-framework.md", "runtime/review-framework.md")
copy("canonical/reporting-contract.md", "runtime/reporting-contract.md")
copy("canonical/report-model.md", "runtime/report-model.md")
copy("canonical/report-modes.md", "runtime/report-modes.md")
copy("canonical/report-export-contract.md", "runtime/report-export-contract.md")
copy("canonical/report-delivery-workflow.md", "runtime/report-delivery-workflow.md")
copy("canonical/report-delivery-policy.json", "runtime/report-delivery-policy.json")
copy("canonical/report-binary-export-contract.md", "runtime/report-binary-export-contract.md")
copy("schemas/report.schema.json")

# Runtime knowledge.
for p in sorted((ROOT / "knowledge" / "common").glob("*.md")):
    copy(str(p.relative_to(ROOT)))

for p in sorted((ROOT / "knowledge" / "technologies").glob("*.md")):
    copy(str(p.relative_to(ROOT)))

# Schemas used as structured output guidance.
copy("schemas/finding.schema.json")
copy("schemas/review-summary.schema.json")

# Metadata.
(STAGE / "VERSION").write_text(version + "\n", encoding="utf-8")

files = []
for p in sorted(STAGE.rglob("*")):
    if p.is_file():
        rel = p.relative_to(STAGE).as_posix()
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        files.append({"path": rel, "sha256": digest, "bytes": p.stat().st_size})

manifest = {
    "name": "Säkerhetsgranskaren för IT-stöd",
    "distribution": "chat",
    "version": version,
    "start_file": "START-HERE.md",
    "file_count": len(files),
    "files": files,
}
(STAGE / "MANIFEST.json").write_text(
    json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

if out.exists():
    out.unlink()

with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted(STAGE.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(STAGE)
        info = zipfile.ZipInfo.from_file(p, arcname=rel.as_posix())
        info.external_attr = (p.stat().st_mode & 0xFFFF) << 16
        with open(p, "rb") as f:
            z.writestr(info, f.read(), compress_type=zipfile.ZIP_DEFLATED)

print(out)
