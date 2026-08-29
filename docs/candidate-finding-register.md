# Kandidatregister och fyndkonsistens

Standard och Deep använder ett beständigt internt kandidatregister. Alla rimliga säkerhetsproblem som upptäcks i kontrollmatris, riskpass eller challenge pass registreras innan slutlig prioritering.

En kandidat får inte försvinna tyst. Vid coverage gate måste varje kandidat vara `confirmed`, `probable`, `review-point`, `dismissed`, `coverage-gap` eller `merged`. Rapporterade kandidater pekar på finding-id; övriga dispositioner kräver ett explicit skäl.

Detta gör inte två körningar ordagrant identiska. Det minskar däremot risken att ett tidigare observerat problem trängs undan när en annan riskfamilj råkar dominera analysen.
