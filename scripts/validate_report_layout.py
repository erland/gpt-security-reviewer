#!/usr/bin/env python3
from pathlib import Path
import json, tempfile, sys
from docx import Document
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import render_report_docx
errors=[]
report=json.loads((ROOT/'tests/fixtures/report-standard-example.json').read_text(encoding='utf-8'))
# Stress text-heavy structures without changing report semantics.
report['system_overview']['major_components'][0]['responsibility'] += ' med lång ansvarstext för säkerhetskritiska användarflöden, repositoryval, import, review och statuspresentation'
if report.get('analyzed_security_flows'):
    report['analyzed_security_flows'][0]['result_next_step']='Verifiera den faktiska produktionskonfigurationen och dokumentera kontrollens ägarskap innan området kan betraktas som fullt verifierat.'
report['follow_up_review']=[
    {'type':'configuration-review','priority':'high','reason':'Säkerhetsgränsen beror på extern produktionskonfiguration som inte finns i källpaketet och därför behöver verifieras separat.','scope':'Reverse proxy, TLS, brandvägg, container/runtime, vidarebefordrade headers och publicerade managementytor.','verification_goal':'Endast avsedda endpoints är exponerade och alla säkerhetsrelevanta edge-kontroller kan verifieras i den faktiska miljön.'},
    {'type':'manual-review','priority':'normal','reason':'Resurskontroller behöver provas efter åtgärd.','scope':'Repositorybudgetar, Git-processer, HTTP-timeouts och cancellation.','verification_goal':'Dyra och långkörande operationer avbryts kontrollerat utan kvarvarande processer eller oproportionerlig påverkan.'}
]
with tempfile.TemporaryDirectory() as td:
    out=Path(td)/'stress.docx'; render_report_docx.render(report).save(out)
    doc=Document(out)
    col_counts=[len(t.columns) for t in doc.tables]
    if any(c>4 for c in col_counts): errors.append(f'text table has >4 columns: {col_counts}')
    xml=out.read_bytes()
    # Inspect OOXML inside zip for our separator controls.
    import zipfile
    with zipfile.ZipFile(out) as z: document_xml=z.read('word/document.xml').decode('utf-8')
    if 'insideH' not in document_xml or 'insideV' not in document_xml: errors.append('table separator border policy not serialized')
    if 'w:val="nil"' not in document_xml: errors.append('vertical gridlines not disabled')
if errors:
    print('REPORT LAYOUT VALIDATION FAILED'); [print('- '+e) for e in errors]; sys.exit(1)
print('REPORT LAYOUT VALIDATION OK')
print('max_text_columns=4')
print('row_separators=horizontal-discreet')
print('follow_up_layout=blocks')
