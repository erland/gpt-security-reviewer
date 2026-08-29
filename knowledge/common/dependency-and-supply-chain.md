# Dependency and supply chain

## Applicability
Använd när projektet har package manifests, lockfiler, build plugins, containers eller andra externa komponentberoenden.

## Security objectives
- beroenden ska vara identifierbara och reproducerbara där möjligt,
- onödiga eller osäkra källor/plugins ska undvikas,
- aktuell sårbarhetsstatus ska verifieras med specialverktyg när det behövs,
- build/release-integritet ska bedömas från tillgängligt underlag.

## High-value review areas
- package manifests och lockfiler,
- dynamiska/flytande versioner,
- okända package repositories,
- build plugins/scripts,
- dependency confusion-indikationer,
- container base images,
- nedladdning/exekvering av artefakter i build,
- pinning/verifiering av CI-actions när relevant.

## Evidence limits
GPT:n får inte påstå att en dependency har en aktuell CVE endast utifrån versionsnumret utan aktuell verifierad sårbarhetsdata.

## Common weaknesses
- credentials i repository-konfiguration,
- osäkra externa build scripts,
- dependency utan låsning i högriskflöde,
- oavsiktlig public/private package-name-kollision,
- överprivilegierad CI-token i kombination med tredjepartskod.

## Follow-up rule
Rekommendera `SCA` när aktuell komponent-/CVE-status behöver verifieras. Rekommendera inte SCA som ett konstaterat fynd; det är en kompletterande aktivitet.

## Manual verification triggers
- privat artefaktrepository,
- provenance/signering,
- release credentials,
- produktionsimage-policy,
- organisationsspecifika tillitskrav.
