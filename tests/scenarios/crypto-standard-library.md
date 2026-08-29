# Scenario: Standard TLS via plattform

## Class
negative

## Tags
crypto, tls, false-positive

## Input
Applikationen använder standard HTTPS-klient utan egen trust manager. Plattformen injicerar truststore och kräver TLS.

## Expected
Rapportera inte custom-crypto/TLS-bypass.
