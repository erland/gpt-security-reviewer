#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]; errors=[]
for rel in ['canonical/defensive-reporting-contract.md','knowledge/common/defensive-reporting.md','tests/fixtures/defensive-reporting-cases.json']:
 if not (ROOT/rel).exists(): errors.append('Missing '+rel)
contract=(ROOT/'canonical/defensive-reporting-contract.md').read_text(encoding='utf-8').lower()
for token in ['payload','poc','bypass','remediation','verification_goal','format invariance']:
 if token not in contract: errors.append('Contract missing '+token)
instructions=(ROOT/'custom-gpt/instructions-template.md').read_text(encoding='utf-8').lower()
for token in ['defensiv','payload','remediation','pdf']:
 if token not in instructions: errors.append('Instructions missing '+token)
cases=json.loads((ROOT/'tests/fixtures/defensive-reporting-cases.json').read_text(encoding='utf-8'))['cases']
if len(cases)<5: errors.append('Expected at least five cases')
for c in cases:
 for k in ['id','category','unsafe','safe','remediation']:
  if not c.get(k): errors.append(f"{c.get('id','?')}: missing {k}")
 if c['unsafe']==c['safe']: errors.append(c['id']+': unsafe and safe identical')
 if len(c['remediation'])<30: errors.append(c['id']+': remediation too thin')
for rel in ['scripts/render_report_markdown.py','scripts/render_report_confluence.py','scripts/render_report_docx.py']:
 t=(ROOT/rel).read_text(encoding='utf-8').lower()
 for bad in ['../etc/passwd','169.254.169.254',"' or 1=1",'union select']:
  if bad in t: errors.append(f'{rel}: hard-coded exploit detail')
if errors:
 print('DEFENSIVE REPORTING VALIDATION FAILED')
 for e in errors: print('-',e)
 sys.exit(1)
print('DEFENSIVE REPORTING VALIDATION OK')
print(f'cases={len(cases)}')
print('formats=chat,markdown,confluence,word,pdf')
