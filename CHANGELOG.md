# Changelog

## [0.1.0-rc.1] - 2026-08-29

### Added
- Canonical runtime-, review-, rapport- och leveranskontrakt.
- Teknik- och common security-profiler med falskpositivskydd.
- Structured findings, review summary och report schemas.
- Quick / Standard / Deep.
- Markdown, Confluence markup, Word och PDF.
- Chat ZIP och Custom GPT distributionsbuilders.
- GitHub Actions CI/release, taggbaserad versionering och SHA-256 checksums.
- Eval-/regressionssvit och V1 quality gate.

### Changed
- Standard/Deep-rapporter visar systemets huvudkomponenter, deployment, aktörer och externa integrationer före fynden.
- Ny strukturerad översikt över analyserade säkerhetsrelevanta flöden/attackytor med coverage-status.
- Rapportmodellen skyddar mot att saknad topologi eller integration presenteras som verifierad.

### Known limitations
Se `RELEASE-NOTES.md`.

- Steg 23: målgruppsingångar för utvecklare/säkerhetsgranskare, resultat/nästa steg i attackytekartan samt berörda komponenter och acceptance criteria per fynd.
