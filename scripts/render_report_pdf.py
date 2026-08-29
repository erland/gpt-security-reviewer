#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, shutil, subprocess, sys, tempfile

ROOT=Path(__file__).resolve().parents[1]

def clean_name(value):
    value=(value or 'it-stod').strip().lower(); value=re.sub(r'[^a-z0-9åäö]+','-',value,flags=re.I).strip('-'); return value or 'it-stod'

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input_json'); ap.add_argument('-o','--output'); args=ap.parse_args()
    report=json.loads(Path(args.input_json).read_text(encoding='utf-8'))
    output=Path(args.output) if args.output else Path(f"sakerhetsgranskning-{clean_name(report['metadata'].get('system_name'))}.pdf")
    with tempfile.TemporaryDirectory() as td:
        td=Path(td); docx=td/'report.docx'
        r=subprocess.run([sys.executable,str(ROOT/'scripts/render_report_docx.py'),args.input_json,'-o',str(docx)],text=True,capture_output=True)
        if r.returncode: print(r.stderr,file=sys.stderr); sys.exit(r.returncode)
        lo=shutil.which('libreoffice') or shutil.which('soffice')
        if not lo:
            print('LibreOffice/soffice is required for PDF rendering',file=sys.stderr); sys.exit(2)
        profile=td/'lo-profile'; profile.mkdir()
        cmd=[lo,'-env:UserInstallation=file://'+str(profile),'--headless','--convert-to','pdf','--outdir',str(td),str(docx)]
        r=subprocess.run(cmd,text=True,capture_output=True)
        generated=td/'report.pdf'
        if r.returncode or not generated.exists(): print((r.stderr or r.stdout or 'PDF conversion failed'),file=sys.stderr); sys.exit(r.returncode or 3)
        output.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(generated,output); print(output)
if __name__=='__main__': main()
