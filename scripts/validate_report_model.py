#!/usr/bin/env python3
from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]; e=[]
for x in ['canonical/report-model.md','canonical/reporting-contract.md','canonical/report-modes.md','schemas/report.schema.json','tests/fixtures/report-standard-example.json']:
    if not (R/x).exists(): e.append('Missing: '+x)
for x in ['schemas/finding.schema.json','schemas/review-summary.schema.json','schemas/report.schema.json','tests/fixtures/report-standard-example.json']:
    try: json.loads((R/x).read_text(encoding='utf-8'))
    except Exception as ex: e.append(f'Invalid JSON {x}: {ex}')
for tok in ['### 1. Metadata','målgruppsingång för utvecklingsteamet','målgruppsingång för säkerhetsgranskaren','### 3. Systemöversikt','### 4. Analyserade säkerhetsrelevanta flöden och attackytor','result_next_step','### 7. Fynd','affected_components','acceptance_criteria','### 8. Coverage','### 10. Rekommenderad fortsatt granskning','### 11. Kvarvarande risk']:
    if tok not in (R/'canonical/report-model.md').read_text(encoding='utf-8'): e.append('Missing report section: '+tok)
for tok in ['## Quick','## Standard','## Deep']:
    if tok not in (R/'canonical/report-modes.md').read_text(encoding='utf-8'): e.append('Missing mode: '+tok)
if e:
 print('REPORT MODEL VALIDATION FAILED'); [print('-',x) for x in e]; sys.exit(1)
print('REPORT MODEL VALIDATION OK'); print('modes=3'); print('canonical_human_format=markdown')
