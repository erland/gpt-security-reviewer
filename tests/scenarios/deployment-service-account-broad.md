# Scenario: bred service account

## Input
Applikationens ServiceAccount binds till ClusterRole med wildcard verbs/resources trots att appen endast behöver läsa en ConfigMap i eget namespace.

## Expected
Least-privilege finding.
