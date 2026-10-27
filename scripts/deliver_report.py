#!/usr/bin/env python3
from pathlib import Path
import argparse,json,subprocess,sys
SCRIPTS=Path(__file__).resolve().parent
# Root-level Chat/OpenCode tools delegate to the complete Skill engine.
if not (SCRIPTS/'plan_report_delivery.py').is_file():
 root=SCRIPTS.parent
 for candidate in (root/'.opencode/skills/security-review/scripts',
                   root/'assistant/skills/security-review/scripts',
                   root/'skills/security-review/scripts'):
  if (candidate/'plan_report_delivery.py').is_file():
   SCRIPTS=candidate
   break
if not (SCRIPTS/'plan_report_delivery.py').is_file():
 raise SystemExit('Report engine incomplete: plan_report_delivery.py missing; use a compatible execution environment')
M={'markdown':'render_report_markdown.py','confluence':'render_report_confluence.py','word':'render_report_docx.py','pdf':'render_report_pdf.py'}
ap=argparse.ArgumentParser(); ap.add_argument('input_json'); ap.add_argument('--mode',choices=['quick','standard','deep'],required=True); ap.add_argument('--formats'); ap.add_argument('--output-dir',default='.'); a=ap.parse_args()
out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True)
# Gate Standard/Deep delivery on the canonical structured review state. This prevents
# ad-hoc rendering before candidate disposition and coverage are complete.
if a.mode in {'standard','deep'}:
 vr=subprocess.run([sys.executable,str(SCRIPTS/'validate_review_integrity.py'),str(Path(a.input_json).resolve())],text=True,capture_output=True)
 if vr.returncode:
  print(vr.stdout or vr.stderr,file=sys.stderr); raise SystemExit(vr.returncode)
cmd=[sys.executable,str(SCRIPTS/'plan_report_delivery.py'),'--mode',a.mode]
if a.formats is not None: cmd += ['--formats',a.formats]
r=subprocess.run(cmd,text=True,capture_output=True); 
if r.returncode: print(r.stderr or r.stdout,file=sys.stderr); raise SystemExit(r.returncode)
plan=json.loads(r.stdout); created=[]
for fmt in plan['formats']:
 rr=subprocess.run([sys.executable,str(SCRIPTS/M[fmt]),str(Path(a.input_json).resolve())],cwd=out,text=True,capture_output=True)
 if rr.returncode: print(rr.stderr,file=sys.stderr); raise SystemExit(rr.returncode)
 created.append(rr.stdout.strip())
print(json.dumps({'plan':plan,'created':created},ensure_ascii=False))
