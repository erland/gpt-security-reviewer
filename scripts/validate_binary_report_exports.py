#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, sys, tempfile, zipfile

ROOT=Path(__file__).resolve().parents[1]; fixture=ROOT/'tests/fixtures/report-export-example.json'; errors=[]
with tempfile.TemporaryDirectory() as td:
    td=Path(td); docx=td/'report.docx'; pdf=td/'report.pdf'
    for script,out in [('render_report_docx.py',docx),('render_report_pdf.py',pdf)]:
        r=subprocess.run([sys.executable,str(ROOT/'scripts'/script),str(fixture),'-o',str(out)],text=True,capture_output=True)
        if r.returncode: errors.append(f"{script}: {r.stderr.strip()}")
    if docx.exists():
        if docx.stat().st_size<10000: errors.append('DOCX unexpectedly small')
        try:
            with zipfile.ZipFile(docx) as z:
                xml=z.read('word/document.xml').decode('utf-8')
            for token in ['F-001','high','Produktions-IAM','Kvarvarande risk']:
                if token not in xml: errors.append(f'DOCX missing invariant: {token}')
        except Exception as e: errors.append(f'DOCX invalid: {e}')
    if pdf.exists():
        if pdf.stat().st_size<5000: errors.append('PDF unexpectedly small')
        if pdf.read_bytes()[:4] != b'%PDF': errors.append('PDF signature invalid')
if errors:
    print('BINARY REPORT EXPORT VALIDATION FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print('BINARY REPORT EXPORT VALIDATION OK')
print('formats=word,pdf')
