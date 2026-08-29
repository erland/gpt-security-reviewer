#!/usr/bin/env python3
from pathlib import Path
import importlib.util, json, sys, tempfile

ROOT=Path(__file__).resolve().parents[1]
fixture=ROOT/'tests/fixtures/report-export-example.json'
policy=json.loads((ROOT/'canonical/report-delivery-policy.json').read_text(encoding='utf-8'))
cases=json.loads((ROOT/'tests/report-delivery-cases.json').read_text(encoding='utf-8'))['cases']
errors=[]
alias={'md':'markdown','docx':'word','confluence-markup':'confluence'}

def plan(mode, raw=None):
    explicit=None if raw is None else []
    if explicit is not None:
        for x in raw.split(','):
            x=alias.get(x.strip().lower(),x.strip().lower())
            if x and x not in explicit: explicit.append(x)
    formats=list(policy[mode]['default_artifacts']) if explicit is None else explicit
    bad=[x for x in formats if x not in policy[mode]['available_formats']]
    if bad: raise ValueError(bad)
    return formats

for c in cases:
    try: got=plan(c['mode'],c['formats'])
    except Exception: errors.append(c['id']+':planner'); continue
    if got!=c['expected']: errors.append(c['id']+f':{got}')

# Quick default is chat only.
if plan('quick')!=[]: errors.append('quick-default-artifacts')
if plan('standard')!=['markdown']: errors.append('standard-default-artifact')
if plan('deep')!=['markdown']: errors.append('deep-default-artifact')

# Import Markdown renderer directly to avoid nested process startup overhead.
spec=importlib.util.spec_from_file_location('render_md',ROOT/'scripts/render_report_markdown.py')
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
report=json.loads(fixture.read_text(encoding='utf-8'))
md=mod.render(report)
for token in ['F-001','high','confirmed','Produktions-IAM','Rekommenderad fortsatt granskning']:
    if token not in md: errors.append('markdown:'+token)

# Reproduce chat-summary invariants directly from canonical data.
from collections import Counter
counts=Counter(f['severity'] for f in report.get('findings',[]))
if counts.get('high')!=1: errors.append('summary:1 high')
if 'Produktions-IAM' not in '; '.join(report['coverage']['not_verifiable']): errors.append('summary:not-verifiable')
types={x['type'] for x in report.get('follow_up_review',[])}
for t in ['manual-review','configuration-review']:
    if t not in types: errors.append('summary:'+t)

if errors:
    print('REPORT WORKFLOW VALIDATION FAILED')
    for e in errors: print('-',e)
    raise SystemExit(1)
print('REPORT WORKFLOW VALIDATION OK')
print(f'delivery_cases={len(cases)}')
print('defaults=quick:chat,standard:markdown,deep:markdown')
