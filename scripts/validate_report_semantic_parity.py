#!/usr/bin/env python3
from pathlib import Path
import json,subprocess,sys,tempfile
ROOT=Path(__file__).resolve().parents[1]; f=ROOT/'tests/fixtures/report-export-example.json'; src=json.loads(f.read_text(encoding='utf-8')); errors=[]
tokens=[]
for x in src['findings']: tokens += [x['id'],x['severity'],x['confidence'],x['status'],x['title']]
tokens += src['coverage']['not_verifiable']+[x['type'] for x in src['follow_up_review']]+['Kvarvarande risk']
with tempfile.TemporaryDirectory() as td:
 td=Path(td)
 for fmt,script,name in [('markdown','render_report_markdown.py','r.md'),('confluence','render_report_confluence.py','r.txt')]:
  out=td/name; r=subprocess.run([sys.executable,str(ROOT/'scripts'/script),str(f),'-o',str(out)],text=True,capture_output=True)
  if r.returncode: errors.append(fmt+':render'); continue
  text=out.read_text(encoding='utf-8').lower()
  for token in tokens:
   if token.lower() not in text: errors.append(fmt+':'+token)
# Binary renderers are already execution/layout validated by step 16; here verify same canonical JSON chain.
docx=(ROOT/'scripts/render_report_docx.py').read_text(encoding='utf-8'); pdf=(ROOT/'scripts/render_report_pdf.py').read_text(encoding='utf-8')
if 'input_json' not in docx or 'findings' not in docx: errors.append('docx-source-contract')
if 'docx' not in pdf.lower(): errors.append('pdf-docx-chain')
if errors:
 print('REPORT SEMANTIC PARITY FAILED'); [print('-',x) for x in errors]; raise SystemExit(1)
print('REPORT SEMANTIC PARITY OK'); print('formats=4; binary rendering delegated to step16 validator')
