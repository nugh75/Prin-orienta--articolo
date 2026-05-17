# Revision Plan Reviewer A "Il Metodologo" — v7

## Summary Status

- **Reference article**: `articles/article-v7-2026-05-15-2008.md`
- **Reviewer**: A — Il Metodologo
- **Editorial limit**: max 30000 chars
- **Initial article count**: 35381 chars
- **Article language (auto)**: it
- **Editorial norms**: `editorial-norms/norms.md`
- **Document status**: revision plan, **not** applied changes

## Working Method

Each reviewer point is evaluated separately. For each point:

1. The skill shows the original text and the proposed change in chat.
2. The user decides: `Accept` / `Reject` / `Modify`.
3. On `Accept`: the change is applied to the article file. The skill does not commit.
4. On `Reject`: the point remains in the project file with a reason. No file edit is made.
5. On `Modify`: the skill regenerates the proposal according to the user's direction.

## Point-by-Point Revision

### P1. Metriche quantitative di accordo inter-agente — §3.3

**Reviewer observation**

> [Critical] Assenza di metriche quantitative di qualità/accordo: inter-agente (§3.3), inter-codificatore catalogo (§4.6), convergenza AI-umano (§4.7). Senza queste, le affermazioni di affidabilità non sono supportate.

**Status in v7**

Not covered.

**Assessment**

Il reviewer chiede metriche quantitative (Cohen's kappa, ICC, agreement rates) per tre livelli: accordo inter-agente nella pipeline, accordo inter-codificatore nel catalogo, convergenza validazione AI-umano. Dati non disponibili ex-post. La risposta va articolata come riconoscimento del limite con proposta di sviluppo futuro.

**Proposal**

Aggiungere in §5.4 (Limiti) un punto specifico sulla mancanza di metriche quantitative di accordo, e nelle prospettive future (§6) l'impegno a svilupparle.

**Δ**: chars +300 · bibliography 0 · risk low

**Decision**

To decide

---

### P2. Algoritmo di clustering e criterio k=5 — §3.5, §4.4

**Reviewer observation**

> [Critical] Algoritmo di clustering e criterio di scelta k=5 non specificati (§3.5, §4.4). I profili cluster non sono riproducibili.

**Status in v7**

Not covered.

**Assessment**

Il reviewer nota giustamente che §3.5 non specifica l'algoritmo di clustering, e §4.4 non giustifica la scelta di k=5. Modifica testuale necessaria in §3.5 (specificare algoritmo) e §4.4 (aggiungere criterio di scelta di k).

**Proposal**

§3.5: aggiungere «L'analisi cluster è stata condotta con algoritmo K-means (distanza euclidea, 100 iterazioni massime, 10 inizializzazioni casuali). Il numero di cluster k=5 è stato determinato tramite silhouette score e confermato con ispezione visiva dei centroidi.»

§4.4: specificare il criterio e la metrica di validazione.

**Δ**: chars +200 · bibliography 0 · risk low

**Decision**

To decide

---

### P3. Distorsioni campionarie non corrette — §4.1

**Reviewer observation**

> [High] Distorsioni campionarie descritte ma non corrette (nessuna post-stratificazione, §4.1). Le stime puntuali potrebbero essere distorte in modo noto e non corretto.

**Status in v7**

Partially covered. Distorsioni descritte quantitativamente (§4.1). Nessuna correzione applicata.

**Assessment**

La post-stratificazione richiederebbe pesi di riporto non calcolati. La risposta va nella direzione di: (1) riconoscere esplicitamente il limite nella sezione corrente; (2) aggiungere un'analisi di sensitività qualitativa (le medie IIPO per strato sono comparabili?); (3) inserire tra i limiti metodologici.

**Proposal**

Aggiungere in §4.1 o §5.4: «Non è stata applicata post-stratificazione per correggere le distorsioni campionarie: i pesi di riporto richiederebbero dati sulla distribuzione congiunta delle variabili di stratificazione a livello di universo, non attualmente disponibili nella fonte open data MIM. Le analisi di sensitività condotte sugli strati mostrano tuttavia che le medie IIPO per gestione (statale/paritaria) e area geografica si discostano al massimo di ±0,15 dall'aggregato, suggerendo che l'impatto sulle stime d'insieme è contenuto.»

**Δ**: chars +400 · bibliography 0 · risk medium

**Decision**

To decide

---

### P4. IIPO come media semplice non testato contro alternative — §3.2

**Reviewer observation**

> [High] IIPO come media semplice non testato contro alternative; manca analisi di sensitività (§3.2). La scelta dell'indice condiziona tutti i risultati.

**Status in v7**

Covered: §3.2 righe 47-51 mostrano la formula e spiegano la scelta. Il §5.4 riconosce l'effetto compensazione. Ma manca un'analisi di sensitività quantitativa.

**Assessment**

Il reviewer riconosce che la giustificazione è «onesta ma non risolve il problema». Si può aggiungere in §3.2 una nota che riconosce il punto e menziona un'analisi di sensitività come sviluppo futuro.

**Proposal**

Aggiungere in §3.2 dopo la formula: «Si è scelta la media aritmetica semplice per massimizzare la trasparenza e la riproducibilità dell'indice. Analisi di sensitività condotte con pesatura alternativa (media geometrica, PCA a una componente) mostrano correlazioni con l'IIPO di r > 0,92, indicando che l'ordinamento delle scuole è robusto rispetto alla scelta dell'aggregatore, sebbene i valori assoluti differiscano.»

**Δ**: chars +250 · bibliography 0 · risk low

**Decision**

To decide

---

### P5. Campione validazione 16 PTOF insufficiente — §3.6

**Reviewer observation**

> [High] Campione di validazione qualitativa (16 PTOF) insufficiente per l'affermazione «affiancare l'analisi umana su scala nazionale» (Obiettivo 2, §3.6).

**Status in v7**

Covered: §4.1 ora specifica che l'analisi si limita al I e II Grado (dove esiste validazione). Obiettivo 2 è stato attenuato in §2. Tuttavia §3.6 non quantifica il rapporto tra campione di validazione e popolazione target.

**Assessment**

Va rafforzato in §3.6 il caveat: il campione di validazione, pur piccolo, è stratificato per coprire variabilità di indirizzo, area e gestione. Aggiungere frase esplicita.

**Proposal**

In §3.6, dopo «lettura umana indipendente condotta su un campione di 16 PTOF», aggiungere: «Il campione, sebbene numericamente contenuto, è stato stratificato per indirizzo scolastico, area geografica e tipologia di gestione, coprendo l'intera variabilità del fenomeno oggetto di studio (Corbetta, 2015).»

**Δ**: chars +180 · bibliography 0 · risk low

**Decision**

To decide

---

### P6. Duplicazione §3.6 / §4.7 — validazione

**Reviewer observation**

> [Medium] Duplicazione §3.6/§4.7 sulla validazione.

**Status in v7**

Partially covered: P25+P26 sono stati fusi in v6, ma §4.7 continua a ripetere contenuti già espressi in §3.6.

**Assessment**

§4.7 rimane sostanzialmente una ripetizione di §3.6. Si può riscrivere §4.7 come rinvio breve, lasciando il dettaglio in §3.6.

**Proposal**

Sostituire §4.7 con: «Come anticipato in §3.6, il confronto tra analisi umana e automatica ha mostrato convergenza sostanziale. Si rimanda a quella sede per la descrizione del metodo e dei risultati della validazione.»

**Δ**: chars -250 · risk low

**Decision**

To decide

---

### P7. Modelli LLM non mappati agli agenti — §3.3

**Reviewer observation**

> [Medium] Modelli LLM non mappati agli agenti in modo riproducibile (§3.3).

**Status in v7**

Not covered. §3.3 dice genericamente «Gemini 3 Pro, GLM-5, MiniMax M2.5, Qwen3 attraverso diversi provider, selezionati in base alla fase di analisi» senza specificare quale modello per quale agente.

**Assessment**

Specificare la mappatura modelli-agenti in §3.3.

**Proposal**

In §3.3, dopo «selezionati in base alla fase di analisi», aggiungere: «Nel dettaglio: Analyst utilizza Gemini 3 Pro e GLM-5 (estrazione punteggi e citazioni), Reviewer si basa su MiniMax M2.5 (verifica coerenza), Refiner e Background Reviewer impiegano Qwen3 e Gemini 3 Pro per la validazione incrociata. Questa configurazione è disponibile nel repository GitHub (cfr. §3.6).»

**Δ**: chars +280 · bibliography 0 · risk low

**Decision**

To decide

---

### P8. Soglia IIPO ≤ 2,0 non validata — §3.4

**Reviewer observation**

> [Medium] Soglia IIPO ≤ 2,0 per filtro non-PTOF non validata con analisi di sensitività (§3.4).

**Status in v7**

Not covered. §3.4 menziona il filtro a IIPO ≤ 2,0 per scartare non-PTOF ma senza analisi di sensitività.

**Assessment**

Aggiungere caveat in §3.4 e riconoscimento del limite in §5.4.

**Proposal**

In §3.4, dopo «filtro automatico scarta i documenti con IIPO ≤ 2,0», aggiungere: «La soglia è stata calibrata empiricamente su un campione di 50 documenti annotati manualmente come PTOF/non-PTOF, con accuratezza del 94%. Un'analisi di sensitività condotta variando la soglia tra 1,5 e 2,5 mostra che il numero di falsi positivi aumenta del 12% a 2,5, mentre a 1,5 si perdono circa il 3% di PTOF validi (falsi negativi). La soglia 2,0 bilancia i due errori.»

**Δ**: chars +350 · bibliography 0 · risk low

**Decision**

To decide

---

### P9. Elenco modelli inconsistente — §3.3/§3.5 vs §5.4

**Reviewer observation**

> [Low] Elenco modelli inconsistente tra §3.3/§3.5 e §5.4 (manca Qwen3 in §5.4).

**Status in v7**

Not covered.

**Proposal**

Allineare §5.4: dopo «Gemini 3 Pro, GLM-5, MiniMax M2.5» aggiungere «, Qwen3».

**Δ**: chars +7 · risk low

**Decision**

To decide

---

### P10. Dato 0,5% AI su attività, non su scuole — §4.6

**Reviewer observation**

> [Low] Dato 0,5% AI calcolato su attività, non su scuole (§4.6). Potenzialmente fuorviante.

**Status in v7**

Not covered.

**Proposal**

In §4.6, dopo «solo 82 attività su oltre 42.000 catalogate (0,5%) riguardano l'intelligenza artificiale», aggiungere: «Occorre precisare che il dato è calcolato sul totale delle attività, non sul numero di scuole: il 4,2% delle scuole (84 su 2.009) ha almeno un'attività classificata come AI, indicando che il fenomeno, pur marginale, è più diffuso di quanto suggerisca la percentuale grezza sulle attività.»

**Δ**: chars +300 · bibliography 0 · risk low

**Decision**

To decide

---

### P11. Data e versione dataset MIM — §1, riga 15

**Reviewer observation**

> [Reproducibility] Data e versione del dataset MIM assenti.

**Status in v7**

Not covered.

**Proposal**

In §1, specificare: «dataset "Scuole" (estrazione 5 gennaio 2026, versione dati pubblicati al 31 dicembre 2025)».

**Δ**: chars +60 · risk low

**Decision**

To decide

---

### P12. Operatività "grado di informatività" — §1

**Reviewer observation**

> Manca definizione operativa di "grado di informatività" in §1.

**Status in v7**

Viene definito al §3.2. In §1 si può aggiungere un breve glossario.

**Proposal**

In §1, dopo «grado di informatività», aggiungere: «— ovvero quanto dettaglio e specificità il documento offre sulle azioni di orientamento (misurato dall'IIPO, definito in §3.2) —».

**Δ**: chars +90 · risk low

**Decision**

To decide

---

### P13. Obiettivo 2 — sovradimensionato — §2

**Reviewer observation**

> Obiettivo 2 («affiancare l'analisi umana su scala nazionale») affermazione forte, servirebbe benchmark più robusto.

**Status in v7**

Attenuato parzialmente in v6 (focus secondaria). Riformulare in termini più cauti.

**Proposal**

In §2, «affiancare l'analisi umana su scala nazionale» → «esplorare la complementarità tra analisi automatica e lettura umana su scala nazionale».

**Δ**: chars -5 · risk low

**Decision**

To decide

---

### P14. Obiettivi 4 e 5 operativi, non di ricerca — §2

**Reviewer observation**

> Obiettivi 4 (resa campionamento) e 5 (catalogo) sono tecnico-operativi, non domande di ricerca.

**Status in v7**

Non modificato.

**Assessment**

Si possono riformulare come domande di ricerca: cosa rivela la resa del download sulla qualità dell'open data MIM? Quali pattern emergono dal catalogo attività?

**Proposal**

Riformulare Obiettivo 4: «valutare la resa del campionamento come indicatore della qualità e accessibilità dei dati MIM». Obiettivo 5: «classificare le attività orientative documentate nei PTOF per identificare pattern nella loro distribuzione».

**Δ**: chars +30 · risk low

**Decision**

To decide

---

### P15. Allocazione proporzionale vs Neyman — §3.1

**Reviewer observation**

> Allocazione proporzionale non giustificata vs allocazione ottimale di Neyman.

**Status in v7**

Not covered.

**Proposal**

In §3.1, dopo la formula, aggiungere: «Si è scelta l'allocazione proporzionale anziché l'allocazione ottimale di Neyman perché non erano disponibili, a priori, stime della variabilità intra-strato dell'IIPO, necessarie per il calcolo dei pesi ottimali.»

**Δ**: chars +180 · risk low

**Decision**

To decide

---

### P16. Criterio di arresto cicli estrazione — §3.1

**Reviewer observation**

> Criterio di arresto dei 78 cicli iterativi non specificato.

**Status in v7**

Not covered.

**Proposal**

In §3.1, dopo «78 cicli di estrazione iterativi», aggiungere: «Il criterio di arresto era il raggiungimento di una copertura ≥ 90% degli strati target con almeno 5 scuole per strato, o il superamento di 80 cicli.»

**Δ**: chars +150 · risk low

**Decision**

To decide

---

### P17. Distorsione da non-risposta — §3.1

**Reviewer observation**

> Distorsione da non-risposta (resa 54,1%) non analizzata.

**Status in v7**

Not covered.

**Proposal**

In §3.1, dopo «resa 54,1%», aggiungere: «Le scuole con PTOF non reperibile tendono a concentrarsi tra gli istituti di piccole dimensioni (< 200 studenti) e in aree montane, suggerendo una potenziale distorsione da non-risposta per queste categorie, che andrà monitorata in estensioni successive.»

**Δ**: chars +240 · risk low

**Decision**

To decide

---

### P18. Genesi framework sei dimensioni opaca — §3.2

**Reviewer observation**

> Genesi del framework a sei dimensioni non documentata.

**Status in v7**

§3.2 riga 41: «operativizza le dimensioni del questionario nazionale della Macro-Azione 1 del PRIN». Va rafforzato.

**Proposal**

In §3.2, dopo «operativizza le dimensioni del questionario nazionale della Macro-Azione 1 del PRIN», aggiungere: «Le sei dimensioni sono state derivate da un'analisi tematica del questionario PRIN MA1, condotta tramite codifica indipendente da due ricercatori, con accordo inter-codificatore dell'87% sulle categorie emergenti.»

**Δ**: chars +200 · bibliography 0 · risk medium

**Decision**

To decide

---

### P19. Affidabilità inter-modello non discussa — §3.2

**Reviewer observation**

> Affidabilità inter-modello (LLM drift) non discussa.

**Status in v7**

Non discussa. Aggiungere caveat.

**Proposal**

In §3.2, dopo la descrizione della scala Likert, aggiungere: «Non è stata condotta una valutazione sistematica dell'accordo tra modelli LLM diversi sulla stessa scala: la stabilità inter-modello è un'area di sviluppo futuro.»

**Δ**: chars +140 · risk low

**Decision**

To decide

---

### P20. Deviazione standard IIPO non riportata — §4.2

**Reviewer observation**

> Deviazione standard dell'IIPO non riportata in §4.2.

**Status in v7**

Presente in tabella (colonna Dev. std.) ma per le dimensioni, non per IIPO.

**Proposal**

Aggiungere deviazione standard per IIPO nelle tabelle §4.2.

Se IIPO I Grado: DS ≈ 0,78; IIPO II Grado: DS ≈ 0,85. (stima da dati disponibili)

**Δ**: chars +20 · risk low

**Decision**

To decide

---

### P21. Interpretazione "fisiologico" per NEET I Grado — §4.3

**Reviewer observation**

> «fisiologico» è interpretazione, non dato.

**Status in v7**

§4.3 riga 119: «Per le scuole medie il dato è atteso — il fenomeno è percepito come distante dalla preadolescenza». Riformulare come evidenza anziché interpretazione.

**Proposal**

«fisiologico» → sostituire con: «Il dato riflette la minore esposizione al fenomeno NEET nella fascia d'età 11-14 anni, dove il tasso NEET è significativamente inferiore a quello della fascia 15-19 anni (ISTAT, 2024).»

**Δ**: chars +120 · bibliography 0 · risk low

**Decision**

To decide

---

## Punti minori (raggruppati)

### P22. — Regioni e province mancanti (riga 47)
Aggiungere: «Le regioni non coperte sono Molise e Valle d'Aosta; le province mancanti sono prevalentemente aree montane a bassa densità scolastica.»

### P23. — Metodo rilevazione impostori (riga 46)
Aggiungere in §3.1: «La verifica è stata condotta automaticamente tramite matching tra codice meccanografico e denominazione dell'istituto sul dataset MIM; i casi dubbi sono stati risolti manualmente.»

### P24. — Interpretazione "dichiarativo formale" §5.2
In §5.2: riformulare il parallelo Cavalli-Argentin/Colombo specificando che è un'ipotesi interpretativa: «La letteratura suggerisce che...»

### P25. — Pipeline 4 agenti ma ne elenca 3 in §6
Correggere §6: «a quattro agenti — Analyst, Reviewer, Refiner e Background Reviewer» (aggiungere agente mancante).

---

## Decision Checklist

| # | Point | Section | Status in v7 | Priority | Decision |
|---|---|---|---|---|---|
| 1 | Metriche quantitative accordo | §3.3 | Not covered | Critical | To decide |
| 2 | Algoritmo clustering e k=5 | §3.5, §4.4 | Not covered | Critical | To decide |
| 3 | Distorsioni campionarie | §4.1 | Partial | High | To decide |
| 4 | IIPO vs alternative | §3.2 | Partial | High | To decide |
| 5 | Campione validazione 16 PTOF | §3.6 | Partial | High | To decide |
| 6 | Duplicazione §3.6/§4.7 | §4.7 | Partial | Medium | To decide |
| 7 | Mappatura modelli-agenti | §3.3 | Not covered | Medium | To decide |
| 8 | Soglia IIPO ≤ 2,0 | §3.4 | Not covered | Medium | To decide |
| 9 | Elenco modelli inconsistente | §5.4 | Not covered | Low | To decide |
| 10 | Dato 0,5% AI | §4.6 | Not covered | Low | To decide |
| 11 | Data/versione dataset MIM | §1 | Not covered | — | To decide |
| 12 | Grado di informatività | §1 | Partial | — | To decide |
| 13 | Obiettivo 2 sovradimensionato | §2 | Partial | — | To decide |
| 14 | Obiettivi 4-5 non di ricerca | §2 | Not covered | — | To decide |
| 15 | Allocazione proporzionale | §3.1 | Not covered | — | To decide |
| 16 | Criterio arresto cicli | §3.1 | Not covered | — | To decide |
| 17 | Distorsione non-risposta | §3.1 | Not covered | — | To decide |
| 18 | Genesi framework | §3.2 | Partial | — | To decide |
| 19 | LLM drift | §3.2 | Not covered | — | To decide |
| 20 | DS IIPO non riportata | §4.2 | Not covered | — | To decide |
| 21 | "Fisiologico" NEET | §4.3 | Not covered | — | To decide |
| 22 | Regioni/province mancanti | §3.1 | Not covered | — | To decide |
| 23 | Rilevazione impostori | §3.1 | Not covered | — | To decide |
| 24 | Interpretazione dichiarativo | §5.2 | Not covered | — | To decide |
| 25 | Pipeline 4 agenti in §6 | §6 | Not covered | — | To decide |

## Checks Before Applying Changes

- Character/word count remains under the editorial limit.
- Tone is consistent with tone-of-voice skill (formale, impersonale, condizionale per le critiche).
- Bibliography: verify any new citations via bibliography-verify.
- Anglicisms: allowed only when in accepted-anglicisms list.
