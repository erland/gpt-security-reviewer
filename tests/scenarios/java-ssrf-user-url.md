# Scenario: användarkontrollerad URL

## Input
API-parametern `callbackUrl` används direkt som mål för server-side HTTP request utan allowlist.

## Expected
SSRF-fynd.
