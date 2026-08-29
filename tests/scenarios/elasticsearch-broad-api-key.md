# Scenario: bred Elasticsearch API key

## Input
Applikationens API key har `all` på samtliga index och cluster management trots att appen bara behöver läsa/skapa dokument i ett index.

## Expected
Least-privilege finding.
