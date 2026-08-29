# Scenario: objektbehörighet saknas

## Input
`GET /orders/{id}` hämtar order med `entityManager.find(Order.class, id)` och returnerar den till autentiserad användare. Ingen ownership- eller rollkontroll syns.

## Expected
BOLA/IDOR-fynd, normalt high om orders innehåller skyddsvärd data och kontrollen verifierbart saknas.
