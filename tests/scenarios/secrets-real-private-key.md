# Scenario: Privat nyckel i repo

## Class
positive

## Tags
secrets, positive

## Input
En PEM-formaterad privat nyckel med verkligt nyckelmaterial ligger i `config/prod-private-key.pem` och refereras av produktionskonfiguration.

## Expected
Skapa confirmed secret/credential finding. Rekommendera omedelbar rotation/revocation och secrets scan.
