# Scenario: Exempelcredential i dokumentation

## Class
negative

## Tags
secrets, docs, false-positive

## Input
README innehåller `DB_PASSWORD=change-me` i ett tydligt markerat lokalt exempel. Produktionsdeployment refererar extern secret manager.

## Expected
Rapportera inte detta som confirmed production secret.
