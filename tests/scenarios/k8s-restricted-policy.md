# Scenario: Plattform tvingar restricted policy

## Class
negative

## Tags
kubernetes, openshift, false-positive

## Input
Manifest saknar seccomp och runAsNonRoot men bifogad clusterpolicy visar obligatorisk restricted Pod Security/SCC som tvingar båda.

## Expected
Rapportera inte dessa som deployment findings.
