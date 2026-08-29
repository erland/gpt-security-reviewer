# Scenario: grants saknas i repo

## Input
Applikationskod och datasource finns, men produktionsgrants hanteras av DBA och finns inte i projektet.

## Expected
Inte ett confirmed privilege finding. Markera privilegier som not_verifiable och rekommendera configuration/manual review.
