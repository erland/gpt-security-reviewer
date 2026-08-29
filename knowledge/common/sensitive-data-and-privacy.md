# Sensitive data and minimization

## Applicability
Använd när systemet hanterar personuppgifter, credentials, sekretessbelagd eller annan skyddsvärd information, eller när dataklassning kan utläsas ur arkitektur/dokumentation.

## Security objectives
- känsliga data ska endast exponeras, lagras och loggas där det behövs,
- trust boundaries och externa mottagare ska vara synliga,
- behörighet och skydd ska stå i proportion till datakänslighet.

## High-value review areas
- data i API-responses,
- frontend/browser storage,
- loggar och fel,
- databaser/index,
- exports/batch,
- cache och temporära filer,
- externa integrationer,
- testdata och fixtures.

## Common weaknesses
- onödigt bred dataexponering,
- känsliga uppgifter i URL/querystring,
- produktionsdata i testartefakter,
- känsliga fält i klientlagring,
- sökindex med bredare åtkomst än källsystem.

## Evidence limits
Juridisk klassning eller verksamhetsmässigt skyddsvärde får inte hittas på. När datakänslighet är okänd ska det anges som osäkerhet.

## Manual verification triggers
- dataklassning saknas,
- retention/backup hanteras externt,
- regulatoriska krav eller sekretessbedömning kräver verksamhets-/juridisk kompetens.
