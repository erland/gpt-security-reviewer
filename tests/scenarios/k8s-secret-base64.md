# Scenario: Kubernetes Secret manifest med base64

## Class
uncertainty

## Tags
kubernetes, secrets, uncertainty

## Input
Repo innehåller ett Kubernetes Secret-objekt med base64-värden men det går inte att avgöra om värdena är placeholders eller verkliga production credentials.

## Expected
Markera som probable/review-point snarare än automatiskt confirmed secret. Rekommendera secrets scan/verifiering. Notera att base64 inte är kryptering.
