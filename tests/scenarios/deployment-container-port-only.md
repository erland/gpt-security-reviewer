# Scenario: endast containerPort

## Input
Deployment anger `containerPort: 8080`; ingen Service, Route eller Ingress finns i underlaget.

## Expected
Rapportera inte extern exponering enbart på grund av containerPort.
