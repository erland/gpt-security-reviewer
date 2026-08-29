# Steg 24 - PDF- och Word-tabellpolicy

Markdown och Confluence får använda informationsrika tabeller. Word/PDF använder en mer konservativ layout eftersom långa identifierare och texttunga kolumner annars kan ge dålig radbrytning.

Regler:

- texttunga Word/PDF-tabeller ska normalt ha högst fyra kolumner,
- femkolumniga texttabeller renderas som kort/block eller smalare sammanfogad struktur,
- långa identifierare och sökvägar ska inte ligga i smala metadata-kolumner,
- systemkomponenter sammanför typ + teknik respektive ansvar + deployment i PDF/DOCX,
- attackytor sammanför status med granskningsfokus,
- fortsatt granskning renderas som block per aktivitet i stället för fem textkolumner,
- tabeller använder diskret headerbakgrund och horisontella radavskiljare i stället för ett tungt rutnät,
- rapportsemantiken får inte ändras av layoutanpassningen.
