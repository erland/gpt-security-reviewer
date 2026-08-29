# Scenario: extern XML med osäker parser

## Input
Uppladdad XML parsas med factory där DTD/external entities inte explicit stängs av och inga shared defaults kan verifieras.

## Expected
Probable/review-point eller confirmed beroende på parserns faktiska default och tillgänglig evidens. Rekommendera verifiering av parserhardening.
