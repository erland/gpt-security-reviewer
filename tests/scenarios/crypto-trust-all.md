# Scenario: Trust-all TLS

## Class
positive

## Tags
crypto, tls, positive

## Input
Java-kod installerar en TrustManager som accepterar alla certifikat och hostname verification är avstängd.

## Expected
Skapa confirmed TLS validation finding, normalt high när extern kommunikation påverkas.
