# Scenario: Frontend guard + verifierad backendkontroll

## Class
negative

## Tags
authz, react, jakarta, false-positive

## Input
React döljer adminvy via route guard. JAX-RS endpoint har verifierad `@RolesAllowed("ADMIN")` och ingen alternativ kodväg finns.

## Expected
Rapportera inte frontend-only authorization. Backend enforcement är verifierad.
