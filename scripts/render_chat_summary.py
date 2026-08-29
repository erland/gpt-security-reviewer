#!/usr/bin/env python3
from pathlib import Path
import argparse,json
from collections import Counter
ap=argparse.ArgumentParser(); ap.add_argument('input_json'); a=ap.parse_args(); r=json.loads(Path(a.input_json).read_text(encoding='utf-8'))
c=Counter(f['severity'] for f in r.get('findings',[])); order=['critical','high','medium','low','informational']; s=', '.join(f'{c[x]} {x}' for x in order if c[x]) or 'inga identifierade fynd'
print('Granskningen är klar.'); print(r['executive_summary']['overall_assessment']); print(f'Fynd: {s}.')
nv=r['coverage']['not_verifiable']; print('Ej verifierbart: '+('; '.join(nv) if nv else 'inga centrala områden')+'.')
t=[]
for x in r.get('follow_up_review',[]):
 if x['type'] not in t: t.append(x['type'])
if t: print('Fortsatt granskning: '+', '.join(t)+'.')
