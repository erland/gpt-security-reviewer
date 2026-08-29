# V1 quality review

## Status
**Redo för release candidate efter genomförd Step 18-validering**, förutsatt att GitHub Actions också passerar i målrepositoryt.

## Scope reviewed
- canonical runtime/workflow/review/report contracts,
- common security knowledge,
- React/Angular/Java/Jakarta/Oracle/PostgreSQL/Elasticsearch/container profiles,
- false-positive/eval scenarios,
- Chat ZIP,
- Custom GPT package,
- report exports and delivery modes,
- CI/release workflows,
- executable permissions and release versioning.

## V1 gaps fixed in Step 18
1. Untrusted instructions/prompt injection inside reviewed material are now explicitly ignored as runtime instructions.
2. Repository hygiene now separates first-party code from generated/vendor content such as `node_modules`, build output and minified bundles.
3. Large repository handling is explicitly risk-driven and coverage-aware.
4. Partial-input behavior is explicitly tested.
5. No-findings reporting is explicitly tested so absence of findings is not presented as proof of security.
6. Architecture eval coverage is strengthened with a trust-boundary/header scenario.

## Accepted V1 limitations
- The GPT is not a substitute for dynamic penetration testing or specialist review where those are warranted.
- Current CVE claims require current SCA/web/tool evidence; versions alone are not treated as proof of vulnerability.
- Cluster/platform controls outside supplied material may remain `not_verifiable`.
- Full repository coverage may require SAST/SCA/secrets scanning rather than exhaustive manual review.
- PDF/DOCX generation depends on the execution environment having the required reporting tooling.

## Release candidate gate
Before publishing RC:
- `validate_project.py` passes,
- `validate_tests.py` passes,
- report model/export/workflow validations pass,
- Chat and Custom GPT builds pass,
- distribution validation passes,
- synthetic release validation passes,
- GitHub Actions CI passes on the actual repository.
