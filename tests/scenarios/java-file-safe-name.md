# Scenario: säkert genererat filnamn

## Input
Uppladdat originalfilnamn ignoreras och servern genererar UUID-baserat lagringsnamn i fast katalog.

## Expected
Rapportera inte path traversal enbart för att filuppladdning finns.
