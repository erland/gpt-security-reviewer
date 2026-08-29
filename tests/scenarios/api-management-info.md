# Scenario: Oskyddad management endpoint

## Class
positive

## Tags
api, management, positive

## Input
`/management/env` är externt routad utan auth och returnerar miljövariabler inklusive interna endpoints.

## Expected
Skapa confirmed management exposure/information disclosure finding.
