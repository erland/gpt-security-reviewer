#!/usr/bin/env python3
from pathlib import Path
import json,sys,importlib.util
ROOT=Path(__file__).resolve().parents[1]
def load(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
src=json.loads((ROOT/'tests/fixtures/report-export-example.json').read_text(encoding='utf-8'));md=load('render_report_markdown').render(src);cf=load('render_report_confluence').render(src);errors=[]
for token in ['# Säkerhetsgranskning av Exempelsystem','### För utvecklingsteamet','### För säkerhetsgranskaren','## Systemöversikt','## Analyserade säkerhetsrelevanta flöden och attackytor','Webbläsare → backend API','## Fynd','F-001','high','## Coverage','## Rekommenderad fortsatt granskning','## Kvarvarande risk']:
 if token not in md:errors.append(f'Markdown missing: {token}')
for token in ['h1. Säkerhetsgranskning av Exempelsystem','h3. För utvecklingsteamet','h3. För säkerhetsgranskaren','h2. Systemöversikt','h2. Analyserade säkerhetsrelevanta flöden och attackytor','Webbläsare → backend API','h2. Fynd','F-001','high','h2. Coverage','h2. Rekommenderad fortsatt granskning','h2. Kvarvarande risk']:
 if token not in cf:errors.append(f'Confluence missing: {token}')
for f in src['findings']:
 for rendered,name in [(md,'Markdown'),(cf,'Confluence')]:
  for token in [f['id'],f['severity'],f['confidence'],f['status']]:
   if token not in rendered:errors.append(f'{name} lost invariant {f["id"]}:{token}')
for x in src['coverage']['not_verifiable']:
 if x not in md or x not in cf:errors.append(f'Coverage lost: {x}')

for f in src['findings']:
 for rendered,name in [(md,'Markdown'),(cf,'Confluence')]:
  if (f.get('acceptance_criteria') or f.get('verification_goal')) not in rendered: errors.append(f'{name} lost acceptance criteria: {f["id"]}')

for x in src.get('analyzed_security_flows',[]):
 for rendered,name in [(md,'Markdown'),(cf,'Confluence')]:
  for token in [x['flow'],x['review_focus'],x['status']]:
   if token not in rendered:errors.append(f'{name} lost analyzed flow: {token}')
if 'h1.' in md:errors.append('Confluence heading leaked into Markdown')
if '|---|---|' in cf:errors.append('Markdown table syntax leaked into Confluence')
if errors:
 print('REPORT EXPORT VALIDATION FAILED');[print('- '+e) for e in errors];sys.exit(1)
print('REPORT EXPORT VALIDATION OK');print('formats=markdown,confluence')
