#!/usr/bin/env python3
from pathlib import Path
import argparse,json,re
SEVERITY_ORDER={"critical":0,"high":1,"medium":2,"low":3,"informational":4}
def esc(v):return str(v or '').replace('|',r'\|').replace('\n',' ')
def clean_name(value):
 value=(value or 'it-stod').strip().lower();value=re.sub(r'[^a-z0-9åäö]+','-',value,flags=re.I).strip('-');return value or 'it-stod'
def bullets(items,empty='Inga identifierade poster.'):
 return empty if not items else '\n'.join(f'* {x}' for x in items)
def table(h,rows):return '\n'.join([''.join(f'||{esc(x)}' for x in h)+'||']+[''.join(f'|{esc(x)}' for x in r)+'|' for r in rows])
def render(report):
 m=report['metadata'];e=report['executive_summary'];s=report['scope'];sy=report['system_overview'];a=report['architecture_security'];flows=report.get('analyzed_security_flows',[]);c=report['coverage'];rr=report['residual_risk'];ap=report.get('appendix') or {};fs=sorted(report.get('findings',[]),key=lambda f:(SEVERITY_ORDER.get(f['severity'],99),f['id']))
 o=[f"h1. {m['title']}",'','h2. Metadata','',table(['Fält','Värde'],[['System/IT-stöd',m.get('system_name') or 'Ej angivet'],['Granskningsdatum',m.get('review_date') or 'Ej angivet'],['Granskningsläge',m.get('review_mode')],['Version',m.get('version')],['Underlagsreferens',m.get('source_reference') or 'Ej angivet']]),'','h2. Sammanfattning','',e['overall_assessment'],'','h3. Viktigaste fynd','',bullets(e['key_findings']),'','h3. Viktigaste osäkerheter','',bullets(e['key_uncertainties']),'','h3. Rekommenderade nästa steg','',bullets(e['next_steps']),'','h2. Systemöversikt','']
 comps=sy.get('major_components',[])
 if comps:
  o += ['h3. Huvudkomponenter','',table(['Komponent','Typ','Teknik','Ansvar','Deploymentenhet'],[[x['name'],x['type'],x.get('technology') or '–',x.get('responsibility') or '–',x.get('deployment_unit') or '–'] for x in comps]),'']
 for k,l in [('frontend','Frontend'),('backend','Backend'),('data_stores','Datalager'),('deployment','Deployment'),('actors','Aktörer'),('external_systems','Externa system'),('integrations','Integrationer')]:
  if sy.get(k):o += [f'h3. {l}','',bullets(sy.get(k,[])),'']
 o += ['h2. Analyserade säkerhetsrelevanta flöden och attackytor','']
 if flows:o += [table(['Flöde/attackyta','Analyserat fokus','Status','Evidensgrund'],[[x['flow'],x['review_focus'],x['status'],x.get('evidence_basis') or '–'] for x in flows]),'']
 else:o += ['Inga separata säkerhetsrelevanta flöden dokumenterade.','']
 o += ['h2. Scope och analyserat underlag','',s['requested_scope'],'','h3. Analyserat underlag','',bullets(s['reviewed_material']),'','h3. Avgränsningar','',bullets(s['limitations']),'','h2. Arkitekturell säkerhetsbild','']
 for k,l in [('trust_boundaries','Trust boundaries'),('authentication_points','Autentiseringspunkter'),('authorization_points','Auktoriseringspunkter'),('administrative_interfaces','Administrativa gränssnitt'),('sensitive_data_flows','Känsliga dataflöden'),('observations','Observationer')]:o += [f'h3. {l}','',bullets(a.get(k,[])),'']
 o += ['h2. Fynd','']
 if fs:
  o += [table(['ID','Severity','Confidence','Status','Titel'],[[f['id'],f['severity'],f['confidence'],f['status'],f['title']] for f in fs]),'']
  for f in fs:
   o += [f"h3. {f['id']} – {f['title']}",'',f"*Kategori:* {f['category']}",f"*Severity:* {f['severity']}",f"*Confidence:* {f['confidence']}",f"*Status:* {f['status']}",f"*Komponent:* {f.get('component') or 'Ej angivet'}",f"*Manuell verifiering:* {f['manual_verification']}",'','*Observation*','',f['observation'],'']
   if f.get('impact'):o += ['*Möjlig konsekvens*','',f['impact'],'']
   if f.get('reasoning'):o += ['*Resonemang*','',f['reasoning'],'']
   o += ['*Rekommenderad åtgärd*','',f['recommendation'],'']
   ev=f.get('evidence_details') or []
   if ev:
    o += ['*Evidens*','']
    for x in ev:o.append(f"* {{code}}{x['source']}{{code}}"+(f" ({x.get('location')})" if x.get('location') else '')+f": {x['description']}")
    o.append('')
   elif f.get('evidence'):o += ['*Evidens*','',bullets(f['evidence']),'']
 else:o += ['Inga identifierade fynd.','']
 o += ['h2. Coverage','','h3. Granskat','',bullets(c['reviewed']),'','h3. Ej granskat','',bullets(c['not_reviewed']),'','h3. Ej verifierbart','',bullets(c['not_verifiable']),'','h2. Rekommenderade åtgärder','']
 acts=report.get('recommended_actions',[])
 if acts:o += [table(['Prioritet','Åtgärd','Motivering','Relaterade fynd'],[[x['priority'],x['action'],x['reason'],', '.join(x.get('related_findings',[])) or '–'] for x in acts]),'']
 else:o += ['Inga ytterligare åtgärder identifierade.','']
 o += ['h2. Rekommenderad fortsatt granskning','']
 fol=report.get('follow_up_review',[])
 if fol:o += [table(['Typ','Prioritet','Scope','Motivering','Verifieringsmål'],[[x['type'],x['priority'],x['scope'],x['reason'],x['verification_goal']] for x in fol]),'']
 else:o += ['Ingen ytterligare särskild granskning rekommenderas.','']
 o += ['h2. Kvarvarande risk','',rr['summary'],'','h3. Från identifierade fynd','',bullets(rr['from_findings']),'','h3. Från ej verifierbara områden','',bullets(rr['from_unverified']),'','h3. Från områden utanför scope','',bullets(rr['from_out_of_scope']),'','h2. Bilaga','','h3. Metod','',bullets(ap.get('method',[])),'','h3. Evidensregister','',bullets(ap.get('evidence_register',[])),'','h3. Använda profiler','',bullets(ap.get('profiles_used',[])),'','h3. Referenser','',bullets(ap.get('references',[])),'']
 return '\n'.join(o).rstrip()+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('input_json');p.add_argument('-o','--output');a=p.parse_args();r=json.loads(Path(a.input_json).read_text(encoding='utf-8'));out=Path(a.output) if a.output else Path(f"sakerhetsgranskning-{clean_name(r['metadata'].get('system_name'))}.confluence.txt");out.write_text(render(r),encoding='utf-8');print(out)
if __name__=='__main__':main()
