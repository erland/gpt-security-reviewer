# Canonical report model

## Purpose
Alla mänskligt läsbara rapportformat ska bygga på samma innehållsmodell.

Den canonical rapportmodellen består av:
1. metadata,
2. executive summary,
3. scope och underlag,
4. system- och tekniköversikt,
5. arkitekturell säkerhetsbild,
6. fynd,
7. coverage,
8. rekommenderade åtgärder,
9. rekommenderad fortsatt granskning,
10. kvarvarande risk,
11. bilaga med evidens och metodinformation.

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

### 3. Scope och analyserat underlag
- vad användaren bad om
- analyserade komponenter
- dokument/filer som ingått
- kända avgränsningar

### 4. System- och tekniköversikt
- frontend
- backend
- datalager
- integrationer
- deploymentmiljö när verifierbar

### 5. Arkitekturell säkerhetsbild
- trust boundaries
- autentiseringspunkter
- auktoriseringspunkter
- administrativa gränssnitt
- externa integrationer
- känsliga dataflöden
- arkitekturella observationer

### 6. Fynd
Fynd grupperas primärt efter severity och sekundärt efter kategori.

Varje fynd bör innehålla ID, titel, kategori, severity, confidence, status, komponent, evidens, observation, möjlig konsekvens, resonemang, rekommenderad åtgärd, manuell verifiering och relevanta referensramar.

### 7. Coverage
Tre obligatoriska perspektiv:
- Granskat
- Ej granskat
- Ej verifierbart

### 8. Rekommenderade åtgärder
Prioritera omedelbara säkerhetsåtgärder, strukturella förbättringar och mindre hardening-/hygienåtgärder.

### 9. Rekommenderad fortsatt granskning
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

### 10. Kvarvarande risk
Beskriv vad som fortfarande inte kan uteslutas, vilka risker som kvarstår efter föreslagna åtgärder och om ytterligare verifiering krävs före starkare slutsats.

### 11. Bilaga
Kan innehålla detaljerad evidens, metod, teknikprofiler som användes, fyndregister och referenser.

## Ordering
Normal ordning ska följas i alla format. Semantiken får inte ändras mellan format.
