# Deployment security

## Applicability
Används tillsammans med containerplattformprofilen och vid applikationsnära driftkonfiguration.

## Security objectives
Skilj mellan vad applikationsprojektet styr och vad plattformen kan tvinga externt. Gör inte frånvaro i repo till automatiskt bevis på osäker runtime.

## High-value review areas
- runtime identity
- secrets
- external exposure
- management exposure
- privilege
- environment separation
- transport security
- platform-enforced policies
- image provenance
- debug/runtime diagnostics

## Evidence expectations
För varje viktig deploymentkontroll, klassificera coverage som reviewed, not_reviewed eller not_verifiable.

## False-positive guards
Admission, SCC, network policy, TLS och secret management kan ligga helt utanför applikationsrepot.

## Manual verification triggers
Rekommendera `configuration-review` när en säkerhetskritisk runtimekontroll uppenbart ägs av plattformen och inte kan verifieras från materialet.
