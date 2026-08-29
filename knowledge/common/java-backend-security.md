# Java backend security

## Applicability
Används tillsammans med Java/Jakarta-profilen för generella Java-backendfrågor.

## Security objectives
Skilj framework/container-säkerhet från applikationslogik och följ säkerhetskontrollen hela vägen till den skyddsvärda operationen.

## High-value review areas
- global vs lokal authn/authz
- interceptors och filters
- persistence boundary
- parser/deserializer boundary
- outbound network boundary
- filesystem boundary
- process execution
- exception boundary

## Evidence expectations
När kontrollen kan ligga i container eller shared library ska avsaknad i en enskild klass inte behandlas som bekräftad brist.

## False-positive guards
Bedöm call chain och global konfiguration innan du slutsatsar om saknad kontroll.

## Manual verification triggers
När security enforcement sker i gemensamma bibliotek eller runtime utanför projektet.

## Defensive reporting note

Behåll rotorsak, evidens, severity/confidence, remediation och defensivt verifieringsmål. Abstrahera exploitpayloads, steg-för-steg-angrepp, bypass-recept och attackkedjor om de inte behövs för defensiv förståelse.
