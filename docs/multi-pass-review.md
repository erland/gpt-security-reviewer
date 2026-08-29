# Steg 24 - deterministisk flerpassgranskning

Steg 24 inför en obligatorisk intern flerpassmodell för Standard och Deep.

Bakgrunden är att riskdriven LLM-granskning kan hitta olika legitima fynd i olika körningar om analysen sker som ett enda fritt pass. Den nya modellen kombinerar riskdriven fördjupning med en kontrollmatris och en coverage gate.

Arbetsordningen är:

1. inventering och säkerhetsmodell,
2. obligatorisk kontrollmatris,
3. riskdriven fördjupning,
4. kandidatfynd,
5. challenge pass,
6. coverage gate,
7. konsolidering och rapportering.

Användaren behöver normalt inte mata fram faserna med flera promptar. Om underlaget är för stort för en komplett Standard/Deep-granskning ska systemet redovisa `not_reviewed` i stället för att låtsas att hela området har analyserats.

Challenge-passet har särskilda påminnelser om current/stale authorization, privilegiegränser, resursförbrukning/timeouts, process/filsystemsgränser, klientdistribuerade capabilities, supply chain och deploymentantaganden. Detta är avsiktligt valt för att fånga riskfamiljer som annars lätt varierar mellan körningar.
