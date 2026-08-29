# Reporting contract

## Core principle
Alla rapporter ska följa `canonical/report-model.md`.

Rapporten ska vara evidensbaserad, tydligt avgränsad och formatneutral i sin semantik.

## Chat summary
När en fullständig filrapport genereras ska chatten normalt endast innehålla kort övergripande bedömning, antal och nivå på viktigaste fynd, största granskningsluckorna, kort rekommendation om nästa steg och länk till rapportartefakten.

## Full report
En full rapport ska innehålla Metadata, Sammanfattning, Scope och analyserat underlag, System- och tekniköversikt, Arkitekturell säkerhetsbild, Fynd, Coverage, Rekommenderade åtgärder, Rekommenderad fortsatt granskning, Kvarvarande risk och Bilaga.

## Findings
Varje fynd ska följa fyndschemat och innehålla minst ID, titel, kategori, severity, confidence, status, observation, rekommendation och manual_verification.

## Coverage
Separata avsnitt: Granskat, Ej granskat och Ej verifierbart. Frånvaro av fynd får inte ersätta coverage-redovisning.

## Follow-up review
Varje rekommendation ska ange typ, prioritet, motivering, scope och verifieringsmål.

Tillåtna typer omfattar uttryckligen SAST, SCA, DAST, penetration-test, configuration-review, specialist-review, secrets-scan, manual-review, spot-check och none.

Rapporten ska även kunna ge slutsatsen **Ingen ytterligare djupgranskning** när underlaget och riskbilden stödjer det.

## Residual risk
Rapporten ska uttryckligen beskriva kvarvarande risk och hur stor del som beror på identifierade fynd, ej verifierbara kontroller och utanför-scope-områden.

## Format neutrality
Markdown är canonical mänskligt läsbart format. Confluence markup, PDF och Word ska genereras från samma rapportmodell och får inte ändra severity, confidence, fynd, granskningsluckor eller rekommenderad fortsatt granskning.

## Defensive detail level

Rapportens fynd ska vara tillräckligt konkreta för remediation men inte utformade som exploateringsinstruktioner. `observation` beskriver kontrollbrist/rotorsak, `impact` säkerhetskonsekvens, `reasoning` evidens och slutsats, `evidence` defensivt relevant lokalisering, `recommendation` får vara detaljerad och `verification_goal` ska beskriva defensiv verifiering. Renderers får inte lägga till exploateringsdetaljer som saknas i canonical report JSON.

## Upfront system and attack-surface overview

Efter sammanfattningen ska Standard och Deep normalt presentera en systemöversikt och en kompakt tabell över analyserade säkerhetsrelevanta flöden/attackytor innan fynden.

Översikten ska härledas från observerat material. Lägg inte till aktörer, integrationssystem, containrar eller nätverksvägar som bara är sannolika. Om deployment/integration endast delvis kan fastställas ska detta framgå.

Attackyteöversikten är defensiv: beskriv flöde, granskningsfokus och coverage-status. Beskriv inte payload, exploateringssekvens eller färdig attackkedja.

## Två primära läsare
Rapporten ska fungera för två huvudmålgrupper utan att dupliceras i två separata rapporter.

Utvecklingsteamet ska snabbt kunna hitta: prioriterade fynd, berörda komponenter, remediation och acceptance criteria.

Säkerhetsgranskaren ska snabbt kunna hitta: system-/deployment-/integrationsbild, analyserade attackytor, coverage, review points och rekommenderad fortsatt manuell eller verktygsbaserad granskning.

Sammanfattningen får därför innehålla korta målgruppsingångar för respektive läsare.
