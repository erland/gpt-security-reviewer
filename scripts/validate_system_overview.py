#!/usr/bin/env python3
from pathlib import Path
import json, importlib.util, sys
R=Path(__file__).resolve().parents[1]
errors=[]
d=json.loads((R/'tests/fixtures/report-export-example.json').read_text(encoding='utf-8'))
for key in ['major_components','actors','external_systems','deployment']:
    if key not in d['system_overview']: errors.append('Missing system_overview.'+key)
flows=d.get('analyzed_security_flows',[])
if len(flows)<3: errors.append('Expected at least three analyzed security flows in fixture')
for x in flows:
    if x.get('status') not in ['reviewed','partially_reviewed','not_verifiable']: errors.append('Invalid flow status')
    if not x.get('flow') or not x.get('review_focus'): errors.append('Flow missing content')
contract=(R/'canonical/report-model.md').read_text(encoding='utf-8')
for token in ['systemdelar/komponenter','deploymentenheter','aktörer','externa system','får inte hitta på','attackytor']:
    if token.lower() not in contract.lower(): errors.append('Report model missing: '+token)
for rel in ['scripts/render_report_markdown.py','scripts/render_report_confluence.py','scripts/render_report_docx.py']:
    t=(R/rel).read_text(encoding='utf-8')
    for token in ['major_components','analyzed_security_flows']:
        if token not in t: errors.append(f'{rel} missing {token}')
if errors:
    print('SYSTEM OVERVIEW VALIDATION FAILED')
    [print('-',e) for e in errors]
    sys.exit(1)
print('SYSTEM OVERVIEW VALIDATION OK')
print('sections=components,deployment,actors,integrations,security-flows')
