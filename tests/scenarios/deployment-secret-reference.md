# Scenario: Kubernetes Secret reference

## Input
Deployment använder `secretKeyRef`; själva secretvärdet finns inte i repo.

## Expected
Rapportera inte secret reference som hårdkodad secret. Secret storage/runtime protection kan vara not_verifiable.
