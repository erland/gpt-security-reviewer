#!/usr/bin/env python3
from pathlib import Path
import argparse,json
ROOT=Path(__file__).resolve().parents[1]
policy=ROOT/'canonical/report-delivery-policy.json'
if not policy.is_file():
 policy=ROOT/'assets/report-delivery-policy.json'
if not policy.is_file():
 raise SystemExit('Missing report-delivery-policy.json: portable engine resources are incomplete')
P=json.loads(policy.read_text(encoding='utf-8'))
alias={'md':'markdown','docx':'word','confluence-markup':'confluence'}
ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['quick','standard','deep'],required=True); ap.add_argument('--formats'); a=ap.parse_args()
explicit=None if a.formats is None else []
if explicit is not None:
 for x in a.formats.split(','):
  x=alias.get(x.strip().lower(),x.strip().lower())
  if x and x not in explicit: explicit.append(x)
formats=list(P[a.mode]['default_artifacts']) if explicit is None else explicit
bad=[x for x in formats if x not in P[a.mode]['available_formats']]
if bad: raise SystemExit('Unsupported format(s): '+', '.join(bad))
print(json.dumps({'review_mode':a.mode,'chat_summary':True,'formats':formats,'explicit_format_override':explicit is not None},ensure_ascii=False))
