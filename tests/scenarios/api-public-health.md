# Scenario: Publik health endpoint

## Class
negative

## Tags
api, health, false-positive

## Input
`/health/live` är avsiktligt publik och returnerar endast status `UP`; inga interna detaljer exponeras.

## Expected
Rapportera inte saknad autentisering som brist.
