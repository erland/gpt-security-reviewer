# Scenario: Elasticsearch användartext i fast query

## Class
negative

## Tags
elasticsearch, false-positive

## Input
Söktext används endast som value i serverkonstruerad `match` mot ett fast fält och fast index.

## Expected
Rapportera inte query injection.
