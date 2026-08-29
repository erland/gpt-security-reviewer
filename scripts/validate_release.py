#!/usr/bin/env python3
from pathlib import Path
import json, os, re, sys, zipfile
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'
version=os.environ.get('RELEASE_VERSION')
if not version:
 print('RELEASE VALIDATION FAILED\n- RELEASE_VERSION is required'); sys.exit(1)
clean=version.lstrip('v')
if not re.fullmatch(r'\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?',clean):
 print(f'RELEASE VALIDATION FAILED\n- Unsupported release version/tag format: {version}'); sys.exit(1)
expected=[DIST/f'sakerhetsgranskaren-it-stod-chat-{clean}.zip',DIST/f'sakerhetsgranskaren-it-stod-custom-gpt-{clean}.zip']
errors=[]
for p in expected:
 if not p.exists(): errors.append(f'Missing release artifact: {p.name}')
for p in expected:
 if not p.exists(): continue
 with zipfile.ZipFile(p) as z:
  if 'VERSION' not in z.namelist(): errors.append(f'{p.name}: VERSION missing'); continue
  embedded=z.read('VERSION').decode().strip()
  if embedded!=clean: errors.append(f'{p.name}: VERSION mismatch {embedded} != {clean}')
  if 'MANIFEST.json' in z.namelist():
   m=json.loads(z.read('MANIFEST.json'))
   if m.get('version')!=clean: errors.append(f'{p.name}: manifest version mismatch')
if errors:
 print('RELEASE VALIDATION FAILED'); [print('- '+e) for e in errors]; sys.exit(1)
print('RELEASE VALIDATION OK'); print('version='+clean)
for p in expected: print(f'- {p.name}: {p.stat().st_size} bytes')
