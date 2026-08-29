#!/usr/bin/env python3
from pathlib import Path
import json,sys,importlib.util
R=Path(__file__).resolve().parents[1]; errors=[]
d=json.loads((R/'tests/fixtures/report-export-example.json').read_text(encoding='utf-8'))
ag=d['executive_summary'].get('audience_guidance') or {}
if not ag.get('developer'): errors.append('Missing developer audience guidance')
if not ag.get('security_reviewer'): errors.append('Missing security reviewer audience guidance')
for f in d.get('findings',[]):
    if not f.get('affected_components'): errors.append(f"{f['id']}: missing affected_components")
    if not f.get('acceptance_criteria'): errors.append(f"{f['id']}: missing acceptance_criteria")
for x in d.get('analyzed_security_flows',[]):
    if not x.get('result_next_step'): errors.append('Flow missing result_next_step: '+x.get('flow','?'))
for rel in ['scripts/render_report_markdown.py','scripts/render_report_confluence.py','scripts/render_report_docx.py']:
    t=(R/rel).read_text(encoding='utf-8')
    for token in ['audience_guidance','affected_components','acceptance_criteria','result_next_step']:
        if token not in t: errors.append(f'{rel} missing {token}')
if errors:
    print('AUDIENCE REPORTING VALIDATION FAILED'); [print('-',x) for x in errors]; sys.exit(1)
print('AUDIENCE REPORTING VALIDATION OK')
print('audiences=developer,security-reviewer')
print('finding_navigation=affected-components,acceptance-criteria')
print('attack_surface_navigation=result-next-step')
