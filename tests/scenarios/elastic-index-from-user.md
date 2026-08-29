# Scenario: Elasticsearch index från klient

## Class
positive

## Tags
elasticsearch, positive

## Input
API-parametern `index` används direkt som indexnamn och servicekontot har read på flera känsliga index.

## Expected
Skapa access-control/query-scope finding.
