# Evidence and risk

## Purpose

Denna modul standardiserar fyndstatus, severity, confidence och fortsatt granskningsbehov.

## Finding status

- `confirmed` – direkt och tillräcklig evidens.
- `probable` – stark indikator men relevant kontrollkedja är inte komplett.
- `review-point` – behöver verifieras; inte en konstaterad sårbarhet.

## Severity

- `critical`
- `high`
- `medium`
- `low`
- `informational`

Severity beskriver möjlig konsekvens om fyndet är verkligt.

## Confidence

- `high`
- `medium`
- `low`

Confidence beskriver hur väl slutsatsen är belagd.

## Evidence quality

Stark evidens är typiskt:

- direkt kod-/konfigurationsbevis,
- komplett relevant kontrollflöde,
- flera oberoende stödjande observationer.

Svagare evidens är typiskt:

- namn eller kommentarer utan implementation,
- dokumentation utan motsvarande konfiguration,
- avsaknad av synlig kontroll när kontrollen kan ligga externt,
- antaganden om produktionsruntime.

## Severity factors

Beakta när känt:

- confidentiality/integrity/availability,
- datakänslighet,
- privilegier,
- exponeringsgrad,
- exploateringskomplexitet,
- användarinteraktion,
- påverkat scope,
- möjlighet till kedjning.

## Follow-up recommendation types

- `none`
- `spot-check`
- `manual-review`
- `SAST`
- `SCA`
- `secrets-scan`
- `DAST`
- `penetration-test`
- `configuration-review`
- `specialist-review`

## Core rule

Rekommendera den minsta kompletterande aktivitet som på ett proportionerligt sätt reducerar den viktigaste kvarvarande osäkerheten.
