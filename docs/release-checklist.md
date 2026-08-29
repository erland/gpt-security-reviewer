# Release checklist – v0.1.0-rc.1

## Repository
- [ ] `.github/` ligger på samma nivå som `README.md`.
- [ ] Python-scripts har executable bit.
- [ ] `VERSION` är `0.1.0-rc.1`.
- [ ] README, CHANGELOG och RELEASE-NOTES är uppdaterade.
- [ ] `dist/` innehåller inga checkade byggartefakter.

## CI
- [ ] Workflow static validation passerar.
- [ ] Ubuntu-jobbet installerar LibreOffice före Word/PDF-validering.
- [ ] CI passerar på aktuell commit.
- [ ] Release-smoke passerar.

## Release
- [ ] Skapa och publicera GitHub Release `v0.1.0-rc.1`.
- [ ] Kontrollera att release-workflow triggas.
- [ ] Kontrollera Chat ZIP, Custom GPT ZIP och SHA-256SUMS.

## Efter release
- [ ] Kontrollera inbäddad VERSION i båda ZIP-filerna.
- [ ] Verifiera checksummor.
- [ ] Testa Chat ZIP i ny konversation.
- [ ] Testa Custom GPT-paketet.
- [ ] Kör minst ett Quick-, Standard- och Deep-scenario.
