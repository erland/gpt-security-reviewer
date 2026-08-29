# Scenario: global authorization interceptor

## Input
JAX-RS resource saknar `@RolesAllowed`, men en global interceptor verifierar roller för alla `/api/*` endpoints.

## Expected
Rapportera inte saknad annotation som confirmed authz-brist. Bedöm interceptorns täckning.
