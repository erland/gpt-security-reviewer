# Scenario: non-root styrs av OpenShift SCC

## Input
Deployment saknar runAsNonRoot. Dokumentationen visar att namespace använder obligatorisk restricted SCC som tilldelar non-root UID.

## Expected
Rapportera inte avsaknad av runAsNonRoot som confirmed finding.
