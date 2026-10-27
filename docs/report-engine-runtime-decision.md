# Rapportmotorns körmodell och behov av separat engine-modul

## Beslut för 1.7.2

Behåll en **självbärande rapportmotor i Skill-resurserna**: `deliver_report.py`, `validate_review_integrity.py`, `plan_report_delivery.py`, fyra renderare och den styrande rapportpolicyn. Paketets smoke-test ska köra verktyget ur uppackade ZIP-arkiv utan hänvisning till projektets källträd.

**Inför inte en obligatorisk separat engine-ZIP ännu.** Det skulle duplicera samma Pythonkod och kan inte ge en värdplatform möjlighet att köra Python om den saknar process-/filsystemåtkomst. Ett separat överförbart enginepaket kan bli användbart för en extern exekveringsmiljö senare.

## Körning och fallback

1. Värd med Python + skrivbart filsystem: kör paketerade `skills/security-review/scripts/deliver_report.py` och använd resultatfilerna. Quick/Markdown är lättviktigt, Word kräver `python-docx`, PDF kräver dessutom LibreOffice.
2. Värd med kodexekvering men utan nödvändiga beroenden: använd stödda format; rapportera saknade beroenden öppet, installera bara med användarens godkännande eller lämna över till en kompatibel värd.
3. Värd utan kodexekvering: utför textbaserad analys och erbjud strukturerad JSON/Markdown, eller **efterfråga en körbar engine-miljö** (t.ex. en ansluten arbetsyta eller extern runner). Begär inte en ZIP som om den i sig löste exekveringsbegränsningen.
4. Vid Standard/Deep: review-integrity-gaten får **inte** hoppas över. Om den inte kan exekveras ska resultatet markeras som *ej deterministiskt verifierat*, och ingen fullständigt verifierad slutrapport får påstås vara levererad.

## Om vi inför separat engine-modul senare

Den bör vara ett versionslåst och hashverifierat överföringspaket med samma script- och policyfiler, inga dubbla implementationer. Den bör ha en tydlig exekveringsprofil (Python, valfria PDF-beroenden), ett kontrakt för indata och returartefakter, och verifieras i ett test där den körs fristående från både repository och Skill-paket. För en värd som inte kan köra processer krävs en ansluten exekveringstjänst, inte ytterligare en fil.
