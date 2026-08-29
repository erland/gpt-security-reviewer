# Scenario: Dynamiskt sorteringsfält med allowlist

## Class
negative

## Tags
sql, allowlist, false-positive

## Input
Klientens sorteringsfält mappas genom en explicit enum/allowlist till ett av fyra statiska kolumnnamn innan SQL byggs.

## Expected
Rapportera inte injection om allowlist-mappningen är verifierad och fullständig.
