# Scenario: Objektbehörighet i shared bibliotek

## Class
uncertainty

## Tags
authz, bola, uncertainty

## Input
Endpoint hämtar order via repository. Repository använder ett shared bibliotek för tenant-/ownership-filter men bibliotekets kod finns inte i underlaget.

## Expected
Skapa inte confirmed BOLA. Markera objektbehörigheten som not_verifiable eller probable/review-point och rekommendera manuell verifiering av shared biblioteket.
