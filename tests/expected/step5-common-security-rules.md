# Step 5 – expected common security rules

- Klientkontroller är inte en säkerhetsgräns för serverresurser.
- Frånvaro av annotation eller lokal kontroll är inte tillräcklig evidens när kontroll kan ligga externt.
- Ett injektionsfynd kräver relevant attacker-kontrollerad källa, farlig sink och otillräcklig neutralisering.
- Parameterisering ska skydda mot falskpositiva SQL-injektionsfynd i det granskade flödet.
- Ett verkligt hard-coded secret kan vara confirmed; en secret-referens är inte i sig säker eller osäker.
- Aktuella CVE-påståenden kräver aktuell sårbarhetsdata; annars används SCA som uppföljning.
- Loggning av tokens/secrets/känsliga data kan vara ett direkt fynd när evidensen är tydlig.
- Externa gateway-/IdP-/runtimekontroller utan konfiguration ska påverka coverage och confidence.
- Komplex authz/business logic får motivera manual-review utan att GPT:n hittar på en sårbarhet.
- Fortsatt granskning ska vara den minsta proportionerliga aktivitet som reducerar viktigaste osäkerheten.
