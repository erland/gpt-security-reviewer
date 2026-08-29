#!/usr/bin/env python3
from pathlib import Path
import hashlib, os, sys
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'
clean=(os.environ.get('RELEASE_VERSION') or (ROOT/'VERSION').read_text().strip()).lstrip('v')
arts=[DIST/f'sakerhetsgranskaren-it-stod-chat-{clean}.zip',DIST/f'sakerhetsgranskaren-it-stod-custom-gpt-{clean}.zip']
missing=[p.name for p in arts if not p.exists()]
if missing: print('Missing artifacts: '+', '.join(missing),file=sys.stderr); sys.exit(1)
out=DIST/f'sakerhetsgranskaren-it-stod-{clean}-SHA256SUMS.txt'
out.write_text('\n'.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}' for p in arts)+'\n')
print(out)
