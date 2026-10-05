#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
if (ROOT/'VERSION').read_text(encoding='utf-8').strip()!='0.1.0-rc.1': errors.append('VERSION must be 0.1.0-rc.1')
for rel in ['README.md','START-HERE.md','CHANGELOG.md','RELEASE-NOTES.md','docs/release-checklist.md','docs/release-process.md','docs/v1-quality-review.md','.github/workflows/ci.yml','.github/workflows/release.yml']:
 if not (ROOT/rel).exists(): errors.append(f'Missing: {rel}')
release=(ROOT/'.github/workflows/release.yml').read_text(encoding='utf-8')
for token in ['types: [published]','GITHUB_REF_NAME','validate_release.py','generate_checksums.py','gh release upload']:
 if token not in release: errors.append(f'release.yml missing: {token}')
ci=(ROOT/'.github/workflows/ci.yml').read_text(encoding='utf-8')
if 'release-smoke' not in ci: errors.append('ci.yml missing release-smoke')
for p in (ROOT/'scripts').glob('*.py'):
 first=p.read_text(encoding='utf-8').splitlines()[0] if p.stat().st_size else ''
 if first!='#!/usr/bin/env python3': errors.append(f'Missing Python shebang: {p.name}')
if errors:
 print('RC READINESS FAILED'); [print('-',e) for e in errors]; sys.exit(1)
print('RC READINESS OK'); print('version=0.1.0-rc.1'); print('tag=v0.1.0-rc.1')
