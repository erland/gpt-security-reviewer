# Canonical report model

## Purpose
Alla mänskligt läsbara rapportformat ska bygga på samma innehållsmodell.

Den canonical rapportmodellen består av:
1. metadata,
2. executive summary,
3. systemöversikt,
4. analyserade säkerhetsrelevanta flöden och attackytor,
5. scope och underlag,
6. arkitekturell säkerhetsbild,
7. fynd,
8. coverage,
9. rekommenderade åtgärder,
10. rekommenderad fortsatt granskning,
11. kvarvarande risk,
12. bilaga med evidens och metodinformation.

Markdown, Confluence markup, PDF och Word ska rendera samma semantiska innehåll.

## Required sections

### 1. Metadata
- rapporttitel
- system/IT-stöd
- granskningsdatum när känt
- granskningsläge
- version
- underlagsreferens när relevant

### 2. Sammanfattning
- övergripande säkerhetsbedömning
- viktigaste fynd
- största osäkerheter
- viktigaste nästa steg

### 3. Systemöversikt
Syftet är att ge läsaren en mental modell av systemet innan säkerhetsdetaljerna.

Redovisa när underlaget stödjer det:
- stora systemdelar/komponenter,
- frontend och teknik,
- backend och teknik,
- datalager,
- deploymentenheter och hur systemdelarna paketeras/körs,
- mänskliga eller tekniska aktörer,
- externa system och integrationer.

`major_components` bör användas för de viktigaste systemdelarna. Varje komponent kan ange namn, typ, teknik, ansvar och deploymentenhet.

Rapporten får inte hitta på komponenter, aktörer, integrationssystem eller deploymenttopologi. Sådant som inte stöds av materialet ska utelämnas eller markeras som ej verifierbart i coverage/arkitekturavsnittet.

### 4. Analyserade säkerhetsrelevanta flöden och attackytor
Ge en kompakt översikt över vilka säkerhetsrelevanta vägar genom systemet som faktiskt analyserats.

Varje rad ska normalt ange:
- `flow`: exempelvis `Webbläsare → frontend/backend`,
- `review_focus`: vilken säkerhetsfråga som analyserats,
- `status`: `reviewed`, `partially_reviewed` eller `not_verifiable`,
- valfri `evidence_basis`: vilket underlag som stöder analysen.

Sektionen ska vara defensiv. Den beskriver kontrollpunkter och analysfokus, inte praktiska attackkedjor, payloads eller exploateringssteg.

Skapa inte en analyserad väg enbart för att den är teoretiskt möjlig. Den ska kunna härledas från observerade komponenter, integrationer, trust boundaries, dataflöden eller faktiskt analyserad coverage.

### 5. Scope och analyserat underlag
- vad användaren bad om
- analyserade komponenter
- dokument/filer som ingått
- kända avgränsningar

### 6. Arkitekturell säkerhetsbild
- trust boundaries
- autentiseringspunkter
- auktoriseringspunkter
- administrativa gränssnitt
- externa integrationer
- känsliga dataflöden
- arkitekturella observationer

### 7. Fynd
Fynd grupperas primärt efter severity och sekundärt efter kategori.

Varje fynd bör innehålla ID, titel, kategori, severity, confidence, status, komponent, evidens, observation, möjlig konsekvens, resonemang, rekommenderad åtgärd, manuell verifiering och relevanta referensramar.

### 8. Coverage
Tre obligatoriska perspektiv:
- Granskat
- Ej granskat
- Ej verifierbart

### 9. Rekommenderade åtgärder
Prioritera omedelbara säkerhetsåtgärder, strukturella förbättringar och mindre hardening-/hygienåtgärder.

### 10. Rekommenderad fortsatt granskning
Varje rekommendation ska ange typ, prioritet, motivering, scope och vad som ska verifieras.

Tillåtna huvudtyper:
- none
- spot-check
- manual-review
- configuration-review
- SAST
- SCA
- secrets-scan
- DAST
- penetration-test
- specialist-review

### 11. Kvarvarande risk
Beskriv vad som fortfarande inte kan uteslutas, vilka risker som kvarstår efter föreslagna åtgärder och om ytterligare verifiering krävs före starkare slutsats.

### 12. Bilaga
Kan innehålla detaljerad evidens, metod, teknikprofiler som användes, fyndregister och referenser.

## Ordering
Normal ordning ska följas i alla format. Systemöversikten och de analyserade säkerhetsrelevanta flödena ska komma före scope, arkitekturdetaljer och fynd så att läsaren först förstår systemet och vad som granskats.

## Defensiv semantik för fynd

`observation` = vad som är fel eller inte kan verifieras. `impact` = möjlig säkerhetskonsekvens på övergripande nivå. `reasoning` = varför evidensen stödjer fyndet. `evidence_details` = var problemet finns och vad som observerats. `recommendation` = hur problemet åtgärdas. `verification_goal` = hur åtgärden verifieras defensivt. Fälten ska inte användas för steg-för-steg-exploatering, attackpayloads eller praktiska bypass-recept.
