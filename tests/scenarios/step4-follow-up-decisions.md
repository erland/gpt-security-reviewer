# Scenario: proportional follow-up decisions

## A – External gateway unknown

Backend endpoints show no local authorization annotation. Architecture states authorization is enforced in an API gateway, but gateway configuration is absent.

Expected:

- do not create a confirmed authorization finding solely from missing annotations,
- probable or review-point depending on available control-flow evidence,
- `configuration-review` or `manual-review` recommended,
- verification goal must explicitly target gateway policy and backend trust assumptions.

## B – Large dependency set without current vulnerability data

Project contains Maven/npm dependencies but no current scanner output.

Expected:

- do not assert specific current CVEs,
- recommend `SCA`,
- do not automatically recommend penetration-test.

## C – Internet-facing high-value administration application

Architecture shows internet exposure, privileged administration features, external identity federation and sensitive data. Static review finds non-trivial authorization concerns.

Expected:

- manual authorization review,
- runtime/configuration verification as relevant,
- penetration-test may be high-priority and must be justified by exposure + privilege + findings,
- not merely because the system is a web application.

## D – Well-covered low-risk application

Relevant auth/authz flows, data access and deployment configuration are available and coherent. No high/critical findings or large coverage gaps are identified.

Expected:

- GPT may explicitly conclude that no separate deep manual code review is currently justified,
- normal SCA or limited runtime verification may still be recommended if not already performed,
- conclusion must state assumptions and residual risk.
