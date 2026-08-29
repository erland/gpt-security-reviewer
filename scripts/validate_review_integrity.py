#!/usr/bin/env python3
from pathlib import Path
import argparse,json,sys
ROOT=Path(__file__).resolve().parents[1]
REQUIRED_FAMILIES={
'authentication/session','authorization/object ownership/current authorization','input/archive/path handling','injection/output/browser sinks','secrets/cryptography','external HTTP/API integrations','local process/Git/file-system operations','data stores','resource consumption/timeouts/concurrency','error handling/logging/audit','dependency/supply chain','deployment/runtime/network exposure','architecture/trust boundaries/privilege boundaries'}
FINAL={'confirmed','probable','review-point','dismissed','coverage-gap','merged'}
REPORTING={'confirmed','probable','review-point'}

def validate(report):
    errors=[]
    mode=(report.get('metadata') or {}).get('review_mode')
    rp=report.get('review_process')
    if mode in {'standard','deep'} and not rp:
        return ['Standard/Deep requires review_process before rendering']
    if not rp:
        return errors
    matrix=rp.get('control_matrix') or []
    by={x.get('control_family'):x for x in matrix}
    missing=sorted(REQUIRED_FAMILIES-set(by))
    if missing: errors.append('control_matrix missing families: '+', '.join(missing))
    for name,x in by.items():
        if x.get('status') not in {'reviewed','not_reviewed','not_verifiable','not_applicable'}:
            errors.append(f'invalid control status: {name}')
    if rp.get('challenge_completed') is not True: errors.append('challenge pass not completed')
    if rp.get('coverage_gate_passed') is not True: errors.append('coverage gate not passed')
    findings={f.get('id'):f for f in report.get('findings',[])}
    candidates=rp.get('candidate_findings') or []
    seen=set()
    for c in candidates:
        cid=c.get('candidate_id')
        if not cid or cid in seen: errors.append(f'duplicate/missing candidate id: {cid}')
        seen.add(cid)
        disp=c.get('disposition')
        if disp not in FINAL: errors.append(f'candidate {cid} unresolved/invalid disposition: {disp}')
        if disp in REPORTING:
            fid=c.get('finding_id')
            if not fid or fid not in findings: errors.append(f'candidate {cid} disposition {disp} lacks matching report finding')
            elif findings[fid].get('status') != disp: errors.append(f'candidate {cid} disposition differs from finding {fid}')
        elif disp=='merged':
            if not c.get('merged_into'): errors.append(f'merged candidate {cid} lacks merged_into')
            if not c.get('rationale'): errors.append(f'merged candidate {cid} lacks rationale')
        else:
            if not c.get('rationale'): errors.append(f'{disp} candidate {cid} lacks rationale')
    # Every report finding must come from at least one surviving candidate.
    mapped={c.get('finding_id') for c in candidates if c.get('disposition') in REPORTING}
    for fid in findings:
        if fid not in mapped: errors.append(f'report finding {fid} has no candidate disposition')
    # Coverage gate consistency: material not reviewed/verifiable must not disappear completely.
    cov=report.get('coverage') or {}
    if any(x.get('status')=='not_reviewed' for x in matrix) and not cov.get('not_reviewed'):
        errors.append('matrix has not_reviewed but report coverage.not_reviewed is empty')
    if any(x.get('status')=='not_verifiable' for x in matrix) and not cov.get('not_verifiable'):
        errors.append('matrix has not_verifiable but report coverage.not_verifiable is empty')
    return errors

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input_json',nargs='?',default=str(ROOT/'tests/fixtures/report-standard-example.json')); a=ap.parse_args()
    report=json.loads(Path(a.input_json).read_text(encoding='utf-8')); errors=validate(report)
    if errors:
        print('REVIEW INTEGRITY VALIDATION FAILED'); [print('- '+e) for e in errors]; sys.exit(1)
    print('REVIEW INTEGRITY VALIDATION OK'); print('candidate_register=resolved'); print('coverage_gate=enforced')
if __name__=='__main__': main()
