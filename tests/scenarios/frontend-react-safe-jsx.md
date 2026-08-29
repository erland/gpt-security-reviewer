# Scenario: React säker JSX-interpolation

## Input
Användarkontrollerad text renderas med `{comment.text}` i JSX.

## Expected
Skapa inte XSS-fynd enbart på denna grund. React escapear normal textinterpolation.
