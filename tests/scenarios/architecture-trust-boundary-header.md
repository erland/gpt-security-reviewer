# Scenario: Spoofbar identity-header över trust boundary

## Class
architecture

## Tags
architecture, trust-boundary, authn

## Input
Gateway sägs sätta X-User, men backend accepterar samma header direkt även på en intern route som kan nås utan gateway.

## Expected
Identifiera trust-boundary/authentication-risk och rekommendera verifiering/teknisk enforcement så att headern inte kan spoofas.
