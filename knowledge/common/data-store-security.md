# Data store security

## Applicability
Används tillsammans med relationsdatabas- och Elasticsearch-profiler.

## Security objectives
Bedöm data store som en egen säkerhetsgräns och skilj applikationskontroller från datalagrets egna privilegier och runtimepolicyer.

## High-value review areas
- minsta privilegium
- data isolation
- credentials
- TLS
- audit
- backup/snapshots
- admin access
- retention
- känslig data duplication

## Evidence expectations
Saknad driftkonfiguration ska redovisas som `not_verifiable` snarare än som automatiskt fynd.

## False-positive guards
Undvik att anta produktionsprivilegier från utvecklingskonfiguration om miljöerna uttryckligen skiljer sig.

## Manual verification triggers
När grants, roles, cluster security, backup eller audit hanteras utanför det analyserade projektet.

## Defensive reporting note

Behåll rotorsak, evidens, severity/confidence, remediation och defensivt verifieringsmål. Abstrahera exploitpayloads, steg-för-steg-angrepp, bypass-recept och attackkedjor om de inte behövs för defensiv förståelse.
