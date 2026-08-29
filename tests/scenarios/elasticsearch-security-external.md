# Scenario: cluster security utanför repo

## Input
App-repot innehåller endast endpoint och secret reference. Roller, TLS och nätverkspolicy finns i driftplattform som inte bifogats.

## Expected
Inte confirmed insecure cluster. Markera authz/TLS/network som not_verifiable och rekommendera configuration review.
