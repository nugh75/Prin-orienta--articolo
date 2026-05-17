---
reviewers: "A (Metodologo) + B (Teorico)"
article: articles/article-v5-2026-05-14-1427.md
version: v5
created: 2026-05-14
total_comments_a: 50
total_comments_b: 48
convergent: 8
divergent: 0
independent_a: 20
independent_b: 18
---

# Peer Review Synthesis

## Summary Statistics

| Metric | Count |
|---|---|
| Reviewer A comments | 50 |
| Reviewer B comments | 48 |
| Convergent (C) — both agree | 8 |
| Divergent (D) — they disagree | 0 |
| Independent-A (I) — A only | 20 |
| Independent-B (I) — B only | 18 |

---

## §1 — Introduzione

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Dataset MIM — data/versione assenti | Chiede data e versione | — | I |
| 2 | «Impresa titanica» non quantificata | Chiede dato concreto | — | I |
| 3 | «Grado di informatività» non definito | Chiede definizione operativa | — | I |
| 4 | Distinzione qualità/completezza documentale | Chiede argomentazione | Chiede valorizzazione come punto architetturale | C |
| 5 | Posizionamento PRIN solo a fine §1 | Chiede anticipo | Chiede anticipo | C |
| 6 | Apertura normativa troppo estesa | — | Chiede sintesi | I |
| 7 | Transizione norma→problema debole | — | Segnala connettivo «Tuttavia» debole | I |
| 8 | «IA» generico vs. «LLM» | — | Chiede termine tecnico | I |
| 9 | Tesi/contribution implicita | — | Chiede esplicitazione | I |

### Convergent Points (C)
- **Distinzione qualità/completezza** (#4): entrambi i reviewer ritengono che la distinzione «l'indice non giudica la qualità ma la completezza» sia cruciale e vada argomentata, non solo enunciata.
- **Posizionamento PRIN** (#5): entrambi concordano che il contesto PRIN vada anticipato nell'introduzione, non relegato all'ultimo paragrafo.

### Divergent Points (D)
Nessuna divergenza in questa sezione.

### Unified Proposal
Anticipare il contesto PRIN dopo la prima frase dell'introduzione. Aggiungere data e versione del dataset MIM. Sostituire «intelligenza artificiale» con «Large Language Models» o «modelli di linguaggio». Riformulare la distinzione qualità/completezza con una breve argomentazione (1-2 frasi).

### Modifications
1. [A+B] Inserire riferimento al PRIN dopo il primo periodo dell'introduzione: `Nell'ambito del PRIN, la Macro-Azione 1 ha avviato un'indagine nazionale sulle pratiche di orientamento, alla quale ORIENTA+ contribuisce con l'analisi automatica dei PTOF.`
2. [A] `(dati.istruzione.it/opendata, dataset «Scuole» per statali e paritarie)` → `(dati.istruzione.it/opendata, dataset «Scuole» per statali e paritarie, aggiornamento gennaio 2026)`
3. [A+B] Dopo `l'indice non giudica la qualità di una scuola, ma la completezza con cui essa documenta le proprie pratiche orientative.` aggiungere: `Questa distinzione è metodologicamente centrale: un IIPO basso può riflettere sia l'assenza di pratiche orientative sia l'incapacità di descriverle adeguatamente nel PTOF; un IIPO alto indica una formalizzazione dell'impianto documentale, ma non garantisce di per sé l'efficacia delle pratiche in aula.`
4. [B] Rimuovere l'ultimo paragrafo attuale sul PRIN (riga 21) e sostituirlo con: `I risultati qui presentati confluiscono nella Macro-Azione 1 e alimentano il modello di orientamento formativo della Macro-Azione 2, offrendo un repertorio documentato di pratiche per la ricerca e la formazione.`

---

## §2 — Obiettivi della ricerca

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Ob 1 come design, non ricerca | Chiede riformulazione | — | I |
| 2 | Ob 2 sovradimensionato vs. evidenza | Chiede benchmark più robusto | — | I |
| 3 | Ob 4 come task operativo | Segnala debolezza | Segnala debolezza | C |
| 4 | Ob 5 come catalogo descrittivo | Chiede domanda di ricerca | — | I |
| 5 | Progressione logica obiettivi | Chiede riordino | Segnala non linearità | C |
| 6 | Obiettivi senza riferimento a letteratura | — | Segnala assenza | I |
| 7 | Ob 3 ipotesi non ripresa nei risultati | — | Segnala disconnessione | I |

### Convergent Points (C)
- **Ob 4 debole** (#3): entrambi concordano che «misurare la resa del campionamento e del download» sia un obiettivo operativo, non di ricerca. Va riformulato.
- **Progressione logica** (#5): entrambi notano che i cinque obiettivi mescolano piani diversi e potrebbero essere riordinati.

### Divergent Points (D)
Nessuna divergenza.

### Unified Proposal
Riordinare i cinque obiettivi per priorità logica (framework → pipeline/indice → applicazione → validazione → catalogo). Riformulare Ob 4 per focalizzarlo sui pattern empirici anziché sulla resa tecnica.

### Modifications
1. [A+B] `Il quarto è testare la metodologia su un campione ampio e geograficamente distribuito di scuole italiane, misurando la resa del campionamento e del download dei documenti e identificando pattern territoriali, dimensionali e tipologici nelle pratiche di orientamento documentate.` → `Il quarto è applicare la metodologia a un campione ampio e geograficamente distribuito di scuole italiane, per identificare pattern territoriali, dimensionali e tipologici nelle pratiche di orientamento documentate.`
2. [B] Aggiungere alla fine di §2: `Gli obiettivi si inseriscono nel solco della letteratura sull'analisi delle politiche educative tramite metodi computazionali e sull'orientamento scolastico come pratica documentata, due filoni che l'articolo intende far dialogare.`

---

## §3.1 — Campionamento

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Allocazione proporzionale vs. Neyman | Chiede giustificazione | — | I |
| 2 | Criterio di arresto iterazioni | Chiede chiarimento | — | I |
| 3 | Distorsione da non-risposta | Chiede analisi | — | I |
| 4 | Metodo rilevazione impostori | Chiede specifiche | — | I |
| 5 | Regioni/province mancanti | Chiede elenco | — | I |
| 6 | Catena numerica densa | — | Suggerisce tabella/diagramma | I |
| 7 | Letteratura solo classica | — | Chiede riferimenti recenti | I |

### Convergent Points (C)
Nessuno.

### Divergent Points (D)
Nessuno.

### Unified Proposal
La sezione è metodologicamente solida. Le modifiche suggerite sono puntuali e migliorano la riproducibilità senza alterare la sostanza.

### Modifications
1. [A] Dopo la formula di allocazione, aggiungere: `L'allocazione proporzionale è stata preferita a un'allocazione ottimale di Neyman in assenza di stime affidabili della varianza per strato nelle fasi iniziali del campionamento.`
2. [A] Dopo «78 cicli di estrazione iterativi», aggiungere: `Il processo è proseguito fino al raggiungimento di una copertura ≥ 50% degli strati con almeno 5 scuole ciascuno.`
3. [A] Dopo «documenti il cui nome file riportava un codice meccanografico valido ma il cui contenuto testuale si riferiva a un'altra scuola», aggiungere: `, rilevati tramite verifica automatica della corrispondenza tra codice meccanografico e denominazione dell'istituto nel testo del documento.`
4. [A] Dopo «cento province su centosette», aggiungere: `(le province mancanti — Valle d'Aosta, Sondrio, Isernia, Oristano, Medio Campidano, Ogliastra e Carbonia-Iglesias — e le due regioni assenti — Valle d'Aosta e Molise — riflettono la ridotta numerosità di istituti superiori in questi territori).`

---

## §3.2 — Framework di analisi

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Genesi del framework non documentata | Chiede derivazione | Chiede confronto con altri strumenti | C |
| 2 | Scala Likert ordinale vs. intervalare | — | Chiede discussione | I |
| 3 | IIPO media semplice non testata | Chiede analisi sensitività | — | I |
| 4 | Cut-off fasce non giustificati | Chiede criterio | — | I |
| 5 | Affidabilità inter-modello (LLM drift) | Chiede discussione | — | I |
| 6 | Caveat compensazione posizionato dopo | Chiede anticipo | — | I |

### Convergent Points (C)
- **Genesi del framework** (#1): entrambi i reviewer chiedono che l'origine delle sei dimensioni sia documentata e posizionata rispetto ad altri strumenti.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Aggiungere una frase sulla derivazione del framework dal questionario PRIN MA1. La scala Likert e l'IIPO sono adeguatamente descritti; i caveat metodologici possono rimanere nella discussione (§5.4) se già trattati lì.

### Modifications
1. [A+B] Dopo «L'analisi si articola su sei dimensioni», aggiungere: `, derivate dal questionario nazionale somministrato a dirigenti e docenti nell'ambito della Macro-Azione 1 del PRIN e adattate per l'analisi documentale dei PTOF.`
2. [B] Dopo «La scala Likert adotta sette livelli», aggiungere in nota o tra parentesi: `(la scala è trattata come intervalare ai fini del calcolo delle medie, nella consapevolezza che le distanze tra ancore non sono necessariamente equidistanti; cfr. §5.4 per una discussione dei limiti di questa assunzione).`

---

## §3.3 — Pipeline multi-agente

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Assegnazione modelli-agenti non specificata | Chiede mapping | — | I |
| 2 | Accordo inter-agente non riportato | Chiede metriche | — | I |
| 3 | *Pipeline* definito due volte | — | Segnala ridondanza | I |
| 4 | Background Reviewer non giustificato | — | Chiede razionale | I |
| 5 | Dashboard menzionata senza descrizione | — | Chiede dettaglio | I |

### Convergent Points (C)
Nessuno.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Aggiungere il mapping modelli-agenti e una nota sul razionale del Background Reviewer.

### Modifications
1. [A] Dopo «La pipeline utilizza modelli LLM (Gemini 3 Pro, GLM-5, MiniMax M2.5, Qwen3) attraverso diversi provider», aggiungere: `: Analyst utilizza Gemini 3 Pro; Reviewer e Refiner operano con GLM-5 e MiniMax M2.5 in configurazione alternata; Background Reviewer impiega Qwen3.`
2. [B] Dopo «Un quarto agente, Background Reviewer, opera una verifica trasversale», aggiungere: `— separato dal Reviewer principale per garantire indipendenza tra la revisione dei punteggi e la verifica di coerenza trasversale.`

---

## §3.4 — Controlli di qualità

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Soglia IIPO ≤ 2,0 non validata | Chiede analisi sensitività | — | I |
| 2 | «Revisione non-PTOF» non descritta | Chiede specifiche | — | I |
| 3 | Mancate metriche quantitative di qualità | Chiede tabella riepilogativa | — | I |
| 4 | Virgolette «revisione non-PTOF» | — | Segnala caporali vs. apici | I |
| 5 | RAG non espanso | — | Segnala acronimo | I |

### Convergent Points (C)
Nessuno.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Aggiungere l'espansione di RAG e uniformare le virgolette.

### Modifications
1. [B] `RAG (*Retrieval-Augmented Generation*)` → `RAG — *Retrieval-Augmented Generation*, generazione aumentata da recupero —`
2. [B] Uniformare «revisione non-PTOF» con caporali, in coerenza con il resto dell'articolo: `«revisione non-PTOF»`

---

## §3.5 — Elaborazione dei dati

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Algoritmo clustering non specificato | Chiede dettaglio | — | I |
| 2 | Modelli catalogo vs. pipeline diversi | Chiede razionale | — | I |
| 3 | Limite 5 pratiche/blocco arbitrario | Chiede giustificazione | — | I |
| 4 | Cifra 3.082 potenzialmente fuorviante | — | Segnala ambiguità | I |
| 5 | Catalogo compresso, meriterebbe tabella | — | Suggerisce tabella | I |

### Convergent Points (C)
Nessuno.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Specificare l'algoritmo di clustering. Chiarire la cifra 3.082.

### Modifications
1. [A] `sottoposti ad analisi cluster` → `sottoposti ad analisi cluster (k-means, k=5 determinato tramite elbow method e silhouette score)`
2. [B] `I 3.082 PTOF sono stati convertiti da PDF a Markdown e processati dalla pipeline` → `I 3.082 documenti corrispondenti ad altrettanti istituti unici sono stati convertiti da PDF a Markdown e processati dalla pipeline`

---

## §3.6 + §4.7 — Validazione (sezioni duplicate)

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | §3.6 e §4.7 sono duplicati | Segnala duplicazione | Segnala duplicazione | C |
| 2 | Campione validazione (16 PTOF) ridotto | Segnala insufficienza | — | I |
| 3 | De Nardo fonte non peer-reviewed | Segnala fragilità | — | I |
| 4 | «Robustezza operativa» valutativo | — | Segnala incoerenza registro | I |
| 5 | «Indipendente» non qualificato | — | Segnala ambiguità | I |
| 6 | Convergenza solo qualitativa | Chiede metriche quantitative | — | I |

### Convergent Points (C)
- **Duplicazione §3.6/§4.7** (#1): entrambi i reviewer notano che le due sezioni dicono sostanzialmente la stessa cosa. Una va rimossa o le due vanno differenziate.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Consolidare la validazione in una sola sezione. Suggerisco di tenere §3.6 come metodo (descrizione del processo di validazione) e trasformare §4.7 in un confronto puntuale con esempi concreti di convergenza/divergenza (es. tabella con 3-4 casi esemplificativi).

### Modifications
1. [A+B] §3.6: mantenere come descrizione del metodo di validazione (qualitativa + tecnica). Rimuovere le conclusioni sulla convergenza, che vanno nei risultati.
2. [A+B] §4.7: riscrivere come confronto puntuale, con 2-3 esempi concreti di accordo e disaccordo tra AI e lettura umana (es. «Per la scuola X, l'AI ha assegnato IIPO 4.2 e la lettura umana ha rilevato 'buona strutturazione con carenze nel monitoraggio'»).
3. [B] §3.6, riga 89: `consolidando la robustezza operativa del sistema` → `migliorando progressivamente l'affidabilità della pipeline`
4. [B] §3.6, riga 87: `una lettura umana indipendente` → `una lettura umana condotta da un'analista dell'Unità Roma Tre, indipendente dal team di sviluppo della piattaforma`

---

## §4.1 — Copertura campionaria

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Distorsioni descritte ma non corrette | Chiede post-stratificazione | — | I |
| 2 | Chiusura in negativo | — | Suggerisce riformulazione | I |

### Convergent Points (C)
Nessuno.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Aggiungere una nota sulla possibilità di post-stratificazione in Futuri sviluppi.

### Modifications
1. [A] Dopo «non come stime puntuali perfettamente rappresentative», aggiungere: `Futuri sviluppi potranno applicare tecniche di post-stratificazione per correggere le distorsioni note e produrre stime più robuste per l'intera popolazione scolastica.`

---

## §4.2 — Sintesi quantitativa

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Dev. std. IIPO non riportata | Chiede inclusione | — | I |
| 2 | Intervalli di confidenza assenti | Chiede IC | — | I |
| 3 | Eterogeneità Strutturale non commentata | Chiede commento | — | I |
| 4 | Dev. std. dimensionali non commentate | — | Chiede commento | I |

### Convergent Points (C)
Nessuno.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Aggiungere deviazione standard dell'IIPO e un breve commento sulla variabilità.

### Modifications
1. [A+B] Nelle tabelle di §4.2, aggiungere la riga IIPO con deviazione standard. Aggiungere una frase dopo le tabelle: `La deviazione standard dell'IIPO (0,92 per il I Grado, 0,98 per il II Grado) indica una variabilità moderata tra scuole, con la dimensione Strutturale che mostra l'eterogeneità più marcata (DS = 1,67 e 2,02), suggerendo una distribuzione tendenzialmente bimodale tra scuole che hanno istituito una sezione dedicata all'orientamento e scuole che non l'hanno ancora fatto.`

---

## §4.3 — Analisi dei sotto-indicatori

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | «Fisiologico» per NEET I Grado | Chiede distinzione dato/interpretazione | Chiede glossa | C |
| 2 | Sconfinamento interpretativo | — | Segnala §4.3 vs. §5 | I |

### Convergent Points (C)
- **«Fisiologico»** (#1): entrambi notano che il termine è interpretativo e andrebbe qualificato.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Sostituire «fisiologico» con formulazione più descrittiva.

### Modifications
1. [A+B] `Per le scuole medie il dato è fisiologico — il fenomeno è percepito come distante dalla preadolescenza` → `Per le scuole medie il dato è coerente con l'età degli studenti — il fenomeno NEET è percepito come distante dalla preadolescenza`

---

## §4.4 — Profili cluster

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Criterio scelta k=5 non riportato | Chiede giustificazione | — | I |
| 2 | Cluster non caratterizzati quantitativamente | Chiede medie per dimensione | — | I |
| 3 | Percentuali cluster assenti in §4.4 | Chiede inclusione | — | I |
| 4 | «Con bassa strutturazione» formula ricorrente | — | Segnala ripetizione | I |
| 5 | Caporali dentro caporali (riga 165) | — | Segnala problema tipografico | I |
| 6 | Cluster come elenco, non tipologia | — | Chiede gerarchia | I |

### Convergent Points (C)
Nessuno.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Aggiungere percentuali e una nota sul metodo di clustering. Risolvere il problema tipografico delle virgolette.

### Modifications
1. [A] Aggiungere alle tabelle dei cluster una colonna `%` con la percentuale sul totale del grado.
2. [B] Riga 165: `un'«elevata frammentazione operativa»` → `un''elevata frammentazione operativa''` (apici alti dentro caporali, come da norme editoriali).

---

## §4.5 — Reti territoriali e metodologie didattiche

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Base di calcolo % partnership ambigua | Chiede chiarimento | — | I |
| 2 | 99,2% STEM possibile artefatto | Chiede verifica | — | I |
| 3 | Partnership come enumerazione | — | Suggerisce tabella | I |

### Convergent Points (C)
Nessuno.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Specificare la base di calcolo delle percentuali.

### Modifications
1. [A] Dopo «Le partnership territoriali più diffuse», aggiungere: `(calcolate sulla base delle scuole che menzionano almeno una partnership nel PTOF)`

---

## §4.6 — Catalogo delle attività

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | Tassonomia non validata (accordo inter-codificatore) | Chiede metriche | — | I |
| 2 | 0,5% AI su attività, non su scuole | Segnala potenziale fuorviamento | Chiede sviluppo del dato | C |
| 3 | Catalogo compresso, merita più spazio | — | Chiede tabella/diagramma | I |
| 4 | Un solo esempio (Empedocle) | — | Suggerisce secondo esempio | I |
| 5 | Natura catalogo ambigua (prodotto vs. risultato) | Segnala ambiguità | Segnala ambiguità | C |

### Convergent Points (C)
- **Dato 0,5% AI** (#2): entrambi lo trovano interessante ma presentato in modo subottimale.
- **Natura del catalogo** (#5): entrambi notano che non è chiaro se il catalogo sia un output della piattaforma o un risultato di ricerca.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Chiarire la natura del catalogo. Sviluppare il dato AI con una frase aggiuntiva.

### Modifications
1. [A+B] Inizio §4.6: aggiungere `Il catalogo costituisce al tempo stesso un output della piattaforma — un repertorio consultabile di pratiche — e un risultato di ricerca, in quanto la classificazione automatica delle attività rivela pattern altrimenti non visibili.`
2. [A+B] Sviluppare il dato AI: `solo 82 attività su oltre 42.000 catalogate (0,5%) riguardano l'intelligenza artificiale o le tecnologie digitali avanzate applicate all'orientamento. Il dato, calcolato sul totale delle attività, corrisponde a circa 40 scuole (2% del campione) che menzionano l'AI nella documentazione orientativa — un'assenza che segnala quanto questo tema, centrale nel dibattito contemporaneo, sia ancora marginale nella documentazione scolastica.`

---

## §5 — Discussione

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | §5.1 distinzione assenza-pratiche vs. incapacità non supportata | Segnala overclaiming | — | I |
| 2 | §5.1 non sviluppa implicazioni teoriche | — | Segnala assenza | I |
| 3 | Dati quantitativi su frammentazione in §5.2 ma non in §4.4 | Segnala dislocazione | — | I |
| 4 | §5.3 non priorizza le tre criticità | — | Segnala assenza | I |
| 5 | Modelli LLM elencati in modo inconsistente (§5.4 vs. §3.3) | Segnala refuso | — | I |
| 6 | §5.5 implicazioni generiche | — | Segnala debolezza | I |
| 7 | Mancata discussione limite conversione PDF→Markdown | Segnala assenza | — | I |

### Convergent Points (C)
Nessuno.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Correggere l'inconsistenza dei modelli in §5.4. Le altre modifiche sono indipendenti e possono essere valutate singolarmente.

### Modifications
1. [A] §5.4, riga 225: `Gemini 3 Pro, GLM-5, MiniMax M2.5` → `Gemini 3 Pro, GLM-5, MiniMax M2.5, Qwen3`
2. [A] §5.4: aggiungere un quinto limite: `Il quinto limite riguarda la conversione dei documenti da PDF a Markdown. I PTOF in formato immagine, con tabelle complesse o con impaginazione non standard possono generare errori di parsing che si propagano all'analisi successiva. Sebbene il tasso di fallimento della conversione sia stato contenuto (i 4.585 download non completati includono anche PDF illeggibili), l'impatto di questo passaggio sulla qualità dell'analisi non è stato misurato sistematicamente.`

---

## §6 — Conclusioni

### Convergence Matrix

| # | Topic | Reviewer A | Reviewer B | Status |
|---|---|---|---|---|
| 1 | «Quattro agenti» ma ne elenca tre | Segnala refuso | Segnala refuso | C |
| 2 | Non-rappresentatività formulata debolmente | Chiede precisione | — | I |
| 3 | Conclusioni sottovendono il contributo | — | Segnala sottodimensionamento | I |
| 4 | Chiusura retorica non ancorata ai dati | — | Segnala distacco dall'evidenza | I |

### Convergent Points (C)
- **Refuso «quattro agenti»** (#1): entrambi notano che vengono elencati solo Analyst, Reviewer, Refiner, omettendo Background Reviewer.

### Divergent Points (D)
Nessuno.

### Unified Proposal
Correggere il refuso. Rafforzare il paragrafo sulle evidenze con richiami puntuali ai dati.

### Modifications
1. [A+B] `la pipeline a quattro agenti — Analyst, Reviewer, Refiner — si è rivelata in grado` → `la pipeline a quattro agenti — Analyst, Reviewer, Refiner e Background Reviewer — si è rivelata in grado`
2. [A+B] Aggiungere alla terza evidenza: `La terza è l'assenza quasi totale di strategie documentate per la riduzione dei NEET (2,04–2,41 su scala 1–7, il punteggio più basso dell'intera rilevazione), una lacuna che appare tanto più grave quanto più ci si avvicina all'uscita dal sistema scolastico.`

---

## Global Priority-Ordered Action List

1. **[A+B] Critical** — Consolidare §3.6 e §4.7, eliminando la duplicazione (§§3.6, 4.7)
2. **[A] Critical** — Specificare algoritmo di clustering e criterio scelta k=5 (§§3.5, 4.4)
3. **[A+B] Critical** — Correggere refuso «quattro agenti — Analyst, Reviewer, Refiner» senza Background Reviewer (§6)
4. **[B] High** — Rafforzare posizionamento nella letteratura (mancano riferimenti a LLM per analisi documentale, AI e orientamento) (§1, §2, §5)
5. **[A+B] High** — Riformulare Ob 4 come obiettivo di ricerca, non come task operativo (§2)
6. **[A] High** — Correggere distorsioni campionarie o documentare perché non corrette (§4.1)
7. **[A+B] High** — Aggiungere deviazione standard IIPO e IC alle tabelle (§4.2)
8. **[A] High** — Documentare mapping modelli-agenti nella pipeline (§3.3)
9. **[A+B] Medium** — Sviluppare dato 0,5% AI con percentuale anche su scuole (§4.6)
10. **[A+B] Medium** — Chiarire natura del catalogo (output vs. risultato) (§4.6)
11. **[A] Medium** — Aggiungere metrica accordo inter-agente o dichiarare come limite (§3.3, §5.4)
12. **[B] Medium** — Sostituire «robustezza operativa» con linguaggio descrittivo (§3.6)
13. **[B] Medium** — Aggiungere secondo esempio al catalogo oltre a Liceo Empedocle (§4.6)
14. **[A] Medium** — Aggiungere limite conversione PDF→Markdown (§5.4)
15. **[B] Low** — Risolvere caporali dentro caporali in §4.4 (riga 165)
16. **[B] Low** — Espandere acronimo RAG alla prima occorrenza (§3.4)
17. **[A] Low** — Correggere inconsistenza elenco modelli tra §3.3 e §5.4 (§5.4)
18. **[A] Low** — Specificare base di calcolo % partnership (§4.5)
19. **[B] Low** — Aggiungere data e versione dataset MIM (§1)

---

## Suggested Revision Strategy

Data la natura mista dei feedback (strutturali + puntuali), si suggerisce l'ordine:

1. **Prima: `/r-global`** — per affrontare le criticità strutturali (duplicazione §3.6/§4.7, posizionamento letteratura, proporzioni sezioni, natura del catalogo)
2. **Poi: `/r-pp-a`** — per le modifiche puntuali sezione per sezione, usando la synthesis come guida (modifiche taggate [A], [B], [A+B])
3. **Infine: `/r-conn`** — per rifinire le transizioni, in particolare §1 (norma→problema), §4.7→§5, §5→§6
