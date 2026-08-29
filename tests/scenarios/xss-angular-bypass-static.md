# Scenario: Angular bypass med statiskt innehåll

## Class
negative

## Tags
angular, xss, false-positive

## Input
`bypassSecurityTrustHtml()` används på en statisk hårdkodad informationsbanner utan extern input.

## Expected
Rapportera inte XSS enbart på grund av bypass-anropet.
