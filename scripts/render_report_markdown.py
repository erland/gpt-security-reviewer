#!/usr/bin/env python3
from pathlib import Path
import argparse,json,re
SEVERITY_ORDER={"critical":0,"high":1,"medium":2,"low":3,"informational":4}
def clean_name(value):
 value=(value or "it-stod").strip().lower(); value=re.sub(r"[^a-z0-9åäö]+","-",value,flags=re.I).strip("-"); return value or "it-stod"
def bullets(items,empty="Inga identifierade poster."):
 return empty if not items else "\n".join(f"- {x}" for x in items)
def render(report):
 m=report['metadata']; e=report['executive_summary']; s=report['scope']; sy=report['system_overview']; a=report['architecture_security']; flows=report.get('analyzed_security_flows',[]); c=report['coverage']; rr=report['residual_risk']; ap=report.get('appendix') or {}
 findings=sorted(report.get('findings',[]),key=lambda f:(SEVERITY_ORDER.get(f['severity'],99),f['id']))
 o=[f"# {m['title']}","","## Metadata","","| Fält | Värde |","|---|---|"]
 for k,l in [('system_name','System/IT-stöd'),('review_date','Granskningsdatum'),('review_mode','Granskningsläge'),('version','Version'),('source_reference','Underlagsreferens')]: o.append(f"| {l} | {m.get(k) or 'Ej angivet'} |")
 o += ["","## Sammanfattning","",e['overall_assessment'],"","### Viktigaste fynd","",bullets(e['key_findings']),"","### Viktigaste osäkerheter","",bullets(e['key_uncertainties']),"","### Rekommenderade nästa steg","",bullets(e['next_steps']),""]
 o += ["## Systemöversikt",""]
 comps=sy.get('major_components',[])
 if comps:
  o += ["### Huvudkomponenter","","| Komponent | Typ | Teknik | Ansvar | Deploymentenhet |","|---|---|---|---|---|"]
  for x in comps:o.append(f"| {x['name']} | {x['type']} | {x.get('technology') or '–'} | {x.get('responsibility') or '–'} | {x.get('deployment_unit') or '–'} |")
  o.append("")
 for k,l in [('frontend','Frontend'),('backend','Backend'),('data_stores','Datalager'),('deployment','Deployment'),('actors','Aktörer'),('external_systems','Externa system'),('integrations','Integrationer')]:
  if sy.get(k): o += [f"### {l}","",bullets(sy.get(k,[])),""]
 o += ["## Analyserade säkerhetsrelevanta flöden och attackytor",""]
 if flows:
  o += ["| Flöde/attackyta | Analyserat fokus | Status | Evidensgrund |","|---|---|---|---|"]
  for x in flows:o.append(f"| {x['flow']} | {x['review_focus']} | {x['status']} | {x.get('evidence_basis') or '–'} |")
  o.append("")
 else:o += ["Inga separata säkerhetsrelevanta flöden dokumenterade.",""]
 o += ["## Scope och analyserat underlag","",s['requested_scope'],"","### Analyserat underlag","",bullets(s['reviewed_material']),"","### Avgränsningar","",bullets(s['limitations']),""]
 o += ["## Arkitekturell säkerhetsbild",""]
 for k,l in [('trust_boundaries','Trust boundaries'),('authentication_points','Autentiseringspunkter'),('authorization_points','Auktoriseringspunkter'),('administrative_interfaces','Administrativa gränssnitt'),('sensitive_data_flows','Känsliga dataflöden'),('observations','Observationer')]: o += [f"### {l}","",bullets(a.get(k,[])),""]
 o += ["## Fynd",""]
 if findings:
  o += ["| ID | Severity | Confidence | Status | Titel |","|---|---|---|---|---|"]
  for f in findings:o.append(f"| {f['id']} | {f['severity']} | {f['confidence']} | {f['status']} | {f['title']} |")
  o.append("")
  for f in findings:
   o += [f"### {f['id']} – {f['title']}","",f"- **Kategori:** {f['category']}",f"- **Severity:** {f['severity']}",f"- **Confidence:** {f['confidence']}",f"- **Status:** {f['status']}",f"- **Komponent:** {f.get('component') or 'Ej angivet'}",f"- **Manuell verifiering:** {f['manual_verification']}","","**Observation**","",f['observation'],""]
   if f.get('impact'):o += ["**Möjlig konsekvens**","",f['impact'],""]
   if f.get('reasoning'):o += ["**Resonemang**","",f['reasoning'],""]
   o += ["**Rekommenderad åtgärd**","",f['recommendation'],""]
   ev=f.get('evidence_details') or []
   if ev:
    o += ["**Evidens**",""]
    for x in ev:o.append(f"- `{x['source']}`"+(f" ({x.get('location')})" if x.get('location') else "")+f": {x['description']}")
    o.append("")
   elif f.get('evidence'):o += ["**Evidens**","",bullets(f['evidence']),""]
   if f.get('references'):o += ["**Referenser**","",bullets(f['references']),""]
 else:o += ["Inga identifierade fynd.",""]
 o += ["## Coverage","","### Granskat","",bullets(c['reviewed']),"","### Ej granskat","",bullets(c['not_reviewed']),"","### Ej verifierbart","",bullets(c['not_verifiable']),""]
 o += ["## Rekommenderade åtgärder",""]
 acts=report.get('recommended_actions',[])
 if acts:
  o += ["| Prioritet | Åtgärd | Motivering | Relaterade fynd |","|---|---|---|---|"]
  for x in acts:o.append(f"| {x['priority']} | {x['action']} | {x['reason']} | {', '.join(x.get('related_findings',[])) or '–'} |")
  o.append("")
 else:o += ["Inga ytterligare åtgärder identifierade.",""]
 o += ["## Rekommenderad fortsatt granskning",""]
 fol=report.get('follow_up_review',[])
 if fol:
  o += ["| Typ | Prioritet | Scope | Motivering | Verifieringsmål |","|---|---|---|---|---|"]
  for x in fol:o.append(f"| {x['type']} | {x['priority']} | {x['scope']} | {x['reason']} | {x['verification_goal']} |")
  o.append("")
 else:o += ["Ingen ytterligare särskild granskning rekommenderas.",""]
 o += ["## Kvarvarande risk","",rr['summary'],"","### Från identifierade fynd","",bullets(rr['from_findings']),"","### Från ej verifierbara områden","",bullets(rr['from_unverified']),"","### Från områden utanför scope","",bullets(rr['from_out_of_scope']),"","## Bilaga","","### Metod","",bullets(ap.get('method',[])),"","### Evidensregister","",bullets(ap.get('evidence_register',[])),"","### Använda profiler","",bullets(ap.get('profiles_used',[])),"","### Referenser","",bullets(ap.get('references',[])),""]
 return "\n".join(o).rstrip()+"\n"
def main():
 p=argparse.ArgumentParser();p.add_argument('input_json');p.add_argument('-o','--output');a=p.parse_args();r=json.loads(Path(a.input_json).read_text(encoding='utf-8'));out=Path(a.output) if a.output else Path(f"sakerhetsgranskning-{clean_name(r['metadata'].get('system_name'))}.md");out.write_text(render(r),encoding='utf-8');print(out)
if __name__=='__main__':main()
