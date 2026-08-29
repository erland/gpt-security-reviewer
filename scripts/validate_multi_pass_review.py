#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
contract=(ROOT/'canonical/multi-pass-review-contract.md')
instructions=(ROOT/'custom-gpt/instructions-template.md')
runtime=(ROOT/'canonical/runtime-contract.md')
for p in [contract,instructions,runtime]:
    if not p.exists() or not p.read_text(encoding='utf-8').strip(): errors.append(f'missing/empty {p.relative_to(ROOT)}')
if contract.exists():
    txt=contract.read_text(encoding='utf-8').lower()
    for token in ['kontrollmatris','challenge pass','coverage gate','not_applicable','current authorization','resource consumption','kandidatfynd']:
        if token not in txt: errors.append(f'multi-pass contract missing: {token}')
for p in [instructions,runtime]:
    if p.exists():
        txt=p.read_text(encoding='utf-8').lower()
        for token in ['kontrollmatris','challenge pass','coverage gate']:
            if token not in txt: errors.append(f'{p.name} missing: {token}')
idx=json.loads((ROOT/'tests/scenarios/index.json').read_text(encoding='utf-8'))
ids={x['id'] for x in idx['scenarios']}
required={'multipass-stale-authorization','multipass-resource-timeouts','coverage-gate-relevant-controls','multipass-combined-findings'}
for x in required-ids: errors.append(f'missing indexed scenario: {x}')
if errors:
    print('MULTI-PASS REVIEW VALIDATION FAILED'); [print('- '+e) for e in errors]; sys.exit(1)
print('MULTI-PASS REVIEW VALIDATION OK')
print('passes=inventory,matrix,risk,candidates,challenge,coverage,report')
print(f'scenarios={len(required)}')
