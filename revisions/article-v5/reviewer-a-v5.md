---
reviewer: "A — Il Metodologo"
article: articles/article-v5-2026-05-14-1427.md
version: v5
created: 2026-05-14
persona: "Rigorous, method-focused. Focus: research design, sampling, data quality, validity, statistics, replicability."
---

# Reviewer A Report — Il Metodologo

## Overall Assessment

L'articolo presenta una metodologia di campionamento e analisi ben documentata e complessivamente solida. La pipeline multi-agente è descritta con sufficiente dettaglio tecnico, e la trasparenza sui limiti (§5.4) è apprezzabile. La validazione tramite confronto con lettura umana (§3.6, §4.7) aggiunge credibilità, sebbene il campione di validazione (16 PTOF) sia modesto e il report citato non sia peer-reviewed.

Segnalo tuttavia criticità metodologiche significative: (1) la rappresentatività del campione è compromessa da distorsioni sistematiche non corrette; (2) l'IIPO come media aritmetica semplice è giustificato ma non testato contro alternative; (3) manca una discussione del numero di cluster ottimale nell'analisi dei profili; (4) la validazione tecnica (§3.6) descrive un processo ma non riporta metriche quantitative di accordo inter-agente.

Il contributo è metodologicamente rilevante e ben contestualizzato nel PRIN. Il mio giudizio complessivo è: **accettabile con revisioni maggiori**, con particolare attenzione ai punti 1–5 della Priority Ranking.

---

## §1 — Introduzione

### Comments
1. **Riga 15**: il dataset MIM è citato come «circa 60.000 record» ma mancano la data di estrazione e la versione. Per riproducibilità, servono data precisa e link permanente.
2. **Riga 15–16**: la frase «la sola raccolta dei PTOF costituisce un'impresa titanica» è suggestiva ma non quantificata. Sarebbe utile un dato concreto, ad esempio il numero di ore-uomo stimate o la resa effettiva del download (54,1%).
3. **Riga 17–18**: ORIENTA+ è descritto come in grado di «rilevare cosa le scuole documentano e con quale grado di informatività». Manca una definizione operativa di «grado di informatività» — il lettore la scopre solo al §3.2.
4. **Riga 20**: la distinzione «l'indice non giudica la qualità di una scuola, ma la completezza con cui essa documenta» è metodologicamente cruciale ma è solo enunciata. Meritava una breve argomentazione già qui.
5. **Riga 21**: il posizionamento nel PRIN è confinato all'ultimo paragrafo. Il contesto istituzionale andrebbe anticipato.

### Flagged Issues
- [Reproducibility] Data e versione del dataset MIM assenti (riga 15)
- [Overclaiming] «impresa titanica» non quantificata (riga 16)
- [Measurement] «grado di informatività» non definito operativamente nell'introduzione (riga 17)

---

## §2 — Obiettivi della ricerca

### Comments
1. **Riga 27**: l'Obiettivo 1 («definire un framework di analisi multidimensionale») è formulato come obiettivo di design, non di ricerca. Andrebbe riformulato in termini di validazione del framework.
2. **Riga 29**: l'Obiettivo 2 parla di «affiancare l'analisi umana su scala nazionale» — questa è un'affermazione forte che richiederebbe un benchmark più robusto dei 16 PTOF citati al §3.6.
3. **Riga 33**: l'Obiettivo 4 menziona «la resa del campionamento e del download» — è un obiettivo tecnico-operativo, non di ricerca. Potrebbe essere assorbito nella sezione metodo.
4. **Riga 35**: l'Obiettivo 5 (catalogo attività) è descrittivo. Manca una domanda di ricerca specifica sul catalogo: cosa ci si aspetta di trovare? Quali ipotesi sulla distribuzione delle attività?
5. **Generale**: i cinque obiettivi mescolano livelli diversi (design, tecnico, descrittivo, esplorativo). Sarebbe utile ordinarli per priorità logica.

### Flagged Issues
- [Measurement] Obiettivo 2 sovradimensionato rispetto all'evidenza di validazione disponibile (riga 29)
- [Validity] Obiettivi 4 e 5 formulati come task operativi, non come domande di ricerca falsificabili (righe 33, 35)

---

## §3.1 — Campionamento

### Comments
1. **Riga 41**: la scelta del campionamento stratificato multi-stadio è appropriata e ben supportata da citazioni classiche (Cochran 1977, Lohr 2010). Tuttavia, la formula *n*~strato~ = (*N*~strato~ / *N*~totale~) × *n*~target~ descrive un'allocazione proporzionale, non una stratificazione con allocazione ottimale. Sarebbe utile giustificare perché non è stata usata un'allocazione di Neyman.
2. **Riga 43**: «78 cicli di estrazione iterativi» — il processo è descritto come adattivo ma non è chiaro il criterio di arresto. Quando il sistema ha smesso di estrarre? Qual era la soglia di rappresentatività considerata accettabile?
3. **Riga 45**: la resa del 54,1% è un dato importante ma viene riportata senza discussione della potenziale distorsione da non-risposta. Le scuole con PTOF non reperibili sono sistematicamente diverse da quelle con PTOF disponibili? (es. piccole scuole, aree montane, etc.)
4. **Riga 46**: la bonifica degli «impostori» (circa 300 documenti) è un'operazione metodologicamente eccellente e ben descritta. Tuttavia, il metodo di rilevazione degli impostori non è specificato: è stato un controllo automatico o manuale? Su quale criterio?
5. **Riga 47**: «diciotto regioni su venti e cento province su centosette» — quali sono le due regioni e le sette province mancanti? La loro assenza è casuale o sistematica?

### Flagged Issues
- [Sampling] Mancata giustificazione dell'allocazione proporzionale vs. allocazione ottimale di Neyman (riga 41)
- [Sampling] Criterio di arresto dei cicli iterativi non specificato (riga 43)
- [Sampling] Distorsione da non-risposta non analizzata (riga 45)
- [Reproducibility] Metodo di rilevazione impostori non documentato (riga 46)
- [Reproducibility] Regioni e province mancanti non elencate (riga 47)

---

## §3.2 — Framework di analisi

### Comments
1. **Riga 51**: le sei dimensioni sono descritte ma non è chiaro come siano state derivate. Derivano dal questionario PRIN MA1? Da una literature review? Da un'analisi fattoriale esplorativa? La genesi del framework è opaca.
2. **Riga 53**: la scala Likert 1–7 è dettagliata con ancore semantiche chiare. Tuttavia, l'affidabilità inter-valutatore non è discussa: come si comportano i diversi modelli LLM sulle stesse ancore? C'è deriva sistematica tra modelli?
3. **Riga 57**: IIPO = media aritmetica semplice. Questa scelta è discutibile: presuppone che le sei dimensioni siano indipendenti e ugualmente pesate. Non sarebbe più appropriata una media ponderata? O un'analisi delle componenti principali per derivare i pesi? La giustificazione al rigo 61 è onesta ma non risolve il problema: sarebbe utile un'analisi di sensitività (es. confronto con media geometrica, media ponderata).
4. **Riga 59**: le cinque fasce di aggregazione (1,1–2,2, 2,3–3,4, ecc.) sono definite con cut-off precisi, ma non è spiegato il criterio di scelta degli intervalli. Perché non equidistanti? Perché 1,1 come limite inferiore e non 1,0?
5. **Riga 61**: il caveat sulla compensazione è importante ma arriva dopo la definizione dell'indice. Sarebbe più efficace anticiparlo.

### Flagged Issues
- [Measurement] Genesi del framework a sei dimensioni non documentata (riga 51)
- [Measurement] Affidabilità inter-modello (LLM drift) non discussa (riga 53)
- [Statistical] IIPO come media semplice non testato contro alternative; manca analisi di sensitività (riga 57)
- [Statistical] Criterio di scelta degli intervalli per le fasce non giustificato (riga 59)

---

## §3.3 — Pipeline multi-agente

### Comments
1. **Riga 65**: la pipeline a quattro agenti è ben descritta. Tuttavia, manca una valutazione quantitativa dell'accordo inter-agente: quanto spesso Reviewer corregge Analyst? Quanto spesso Background Reviewer interviene? Queste metriche sarebbero preziose per calibrare la fiducia nell'output.
2. **Riga 67**: «la pipeline utilizza modelli LLM (Gemini 3 Pro, GLM-5, MiniMax M2.5, Qwen3) attraverso diversi provider» — quali modelli per quali agenti? La scelta è arbitraria o basata su benchmark? Senza questa informazione, la pipeline non è replicabile.
3. **Riga 69**: il catalogo attività come «modulo dedicato» è citato ma non si capisce se usa gli stessi modelli della pipeline principale o modelli separati (dettaglio che arriva solo al §3.5).

### Flagged Issues
- [Reproducibility] Assegnazione modelli-agenti non specificata (riga 67)
- [Validity] Mancata metrica di accordo inter-agente (riga 65)
- [Reproducibility] Separazione tra pipeline principale e modulo catalogo non chiara in questa sezione (riga 69)

---

## §3.4 — Controlli di qualità

### Comments
1. **Riga 73**: il filtro IIPO ≤ 2,0 per scartare non-PTOF è ragionevole ma andrebbe validato: quanti documenti scartati erano effettivamente non-PTOF? Quanti PTOF validi sono stati erroneamente scartati? Un'analisi di sensibilità della soglia (es. 1,5 vs 2,0 vs 2,5) rafforzerebbe la scelta.
2. **Riga 73**: la «revisione non-PTOF» è citata ma non descritta operativamente. È automatica? Manuale? Con quali criteri?
3. **Riga 75**: la generazione dei report in tre fasi è descritta a livello architetturale ma mancano metriche di qualità: quanti report hanno richiesto correzioni in fase 3? Quali tipi di errore sono stati intercettati più frequentemente?
4. **Generale**: i controlli di qualità sono descritti come processo ma non come esito. Sarebbe utile una tabella riepilogativa: N documenti scartati da ciascun filtro, N correzioni applicate, tasso di errore residuo stimato.

### Flagged Issues
- [Validity] Soglia IIPO ≤ 2,0 non validata (riga 73)
- [Reproducibility] «Revisione non-PTOF» non descritta operativamente (riga 73)
- [Validity] Mancate metriche quantitative di qualità dell'output (riga 75)

---

## §3.5 — Elaborazione dei dati

### Comments
1. **Riga 79**: «I dati aggregati sono stati sottoposti ad analisi cluster» — quale algoritmo? K-means? Hierarchical? DBSCAN? Il metodo di clustering non è specificato, né lo è il criterio di scelta del numero di cluster (5 per entrambi i gradi). Senza questa informazione, i profili cluster del §4.4 non sono riproducibili.
2. **Riga 81**: il catalogo attività cita «molteplici modelli LLM (Qwen3:32b, Gemma3:27b, Gemini 2.5 Flash)» diversi da quelli della pipeline principale (§3.3). Perché modelli diversi? C'è un razionale?
3. **Riga 81**: «limite di 5 pratiche per blocco documentale» — questa scelta è arbitraria? Cosa succede alle pratiche oltre la quinta? Il limite potrebbe introdurre un bias di selezione.
4. **Riga 81**: 42.381 attività su 2.009 scuole = circa 21 attività per scuola in media. Questa cifra è realistica? Non viene discussa.

### Flagged Issues
- [Reproducibility] Algoritmo di clustering e criterio di scelta del numero di cluster non specificati (riga 79)
- [Reproducibility] Razionale per la scelta di modelli diversi tra pipeline e catalogo assente (riga 81)
- [Sampling] Limite di 5 pratiche per blocco potrebbe introdurre bias (riga 81)

---

## §3.6 — Validazione della piattaforma

### Comments
1. **Riga 87**: la validazione qualitativa su 16 PTOF è un buon punto di partenza ma è insufficiente per affermare che l'analisi automatica possa «affiancare l'analisi umana su scala nazionale» (Obiettivo 2). Servirebbe un campione di validazione più ampio e una metrica di accordo quantitativa (es. Cohen's kappa, ICC).
2. **Riga 87**: De Nardo (2026) è citato come «report interno non pubblicato». Questo è trasparente ma indebolisce la validazione: il lettore non può verificare il metodo della lettura umana. 
3. **Riga 89**: la validazione tecnica descrive un «processo iterativo tracciato tramite versionamento» ma non fornisce metriche: quanti bug risolti? Quale tasso di correzione? L'issue tracking è menzionato ma non quantificato.
4. **Generale**: la validazione è presentata su due livelli (qualitativo e tecnico) ma manca una validazione quantitativa: metriche di accuratezza, precisione, recall rispetto a un gold standard.

### Flagged Issues
- [Validity] Campione di validazione qualitativa (16 PTOF) troppo ridotto per le affermazioni dell'Obiettivo 2 (riga 87)
- [Validity] Validazione basata su fonte non peer-reviewed e non verificabile (riga 87)
- [Measurement] Assenza di metriche quantitative di accordo/accuratezza (righe 87-89)

---

## §4.1 — Copertura campionaria

### Comments
1. **Riga 97**: le distorsioni del campione sono descritte con precisione e onestà. Molto apprezzabile. Tuttavia, non viene proposta nessuna correzione (es. post-stratificazione, pesi di riporto all'universo). Le distorsioni sono solo descritte, non trattate.
2. **Riga 99**: l'interpretazione delle distorsioni è cauta e appropriata. La frase «i risultati vanno pertanto letti come tendenze significative all'interno del perimetro osservato, non come stime puntuali perfettamente rappresentative» è metodologicamente corretta ma potrebbe essere rafforzata da un'analisi di sensitività: quanto cambierebbero le medie con pesi di post-stratificazione?

### Flagged Issues
- [Statistical] Distorsioni campionarie descritte ma non corrette (nessuna post-stratificazione) (riga 97)
- [Validity] Assenza di analisi di sensitività con pesi di riporto (riga 99)

---

## §4.2 — Sintesi quantitativa

### Comments
1. **Riga 103**: IIPO medio 3,44–3,48. Le deviazioni standard sono riportate solo per le dimensioni, non per l'IIPO. Perché? L'IIPO è una media di medie: la sua variabilità è informativa.
2. **Riga 115, 127**: le tabelle riportano medie e deviazioni standard ma non intervalli di confidenza. Con 246 e 693 osservazioni, gli IC sono calcolabili e informerebbero sulla precisione delle stime.
3. **Riga 129**: la dimensione Strutturale ha deviazione standard elevata (1,67 e 2,02), suggerendo forte eterogeneità. Questo andrebbe commentato: la media di 2,39–2,62 è rappresentativa di un fenomeno bimodale?

### Flagged Issues
- [Statistical] Deviazione standard dell'IIPO non riportata (riga 103)
- [Statistical] Intervalli di confidenza assenti (righe 115, 127)
- [Statistical] Eterogeneità della dimensione Strutturale non commentata (riga 129)

---

## §4.3 — Analisi dei sotto-indicatori

### Comments
1. **Riga 135–137**: l'analisi dei sotto-indicatori è pertinente e ben argomentata. Il dato su Monitoraggio (2,79–3,06) vs. Alleanza Famiglie (3,95–4,05) è illuminante.
2. **Riga 137**: Riduzione NEET a 2,04 nel I Grado è commentato come «fisiologico» — questa è un'interpretazione, non un dato. Andrebbe distinto chiaramente ciò che è evidenza empirica da ciò che è interpretazione.

### Flagged Issues
- [Validity] Interpretazione «fisiologico» per il dato NEET I Grado non supportata da evidenza (riga 137)

---

## §4.4 — Profili cluster

### Comments
1. **Riga 143**: l'analisi cluster ha identificato 5 gruppi per entrambi i gradi. Tuttavia, non è riportato nessun criterio statistico per la scelta di k=5 (elbow method, silhouette score, gap statistic). Senza questa informazione, i cluster potrebbero essere un artefatto della scelta di k.
2. **Riga 147, 155**: le tabelle dei cluster sono descrittive ma non riportano la numerosità dei cluster come percentuale del campione. Per il II Grado, il cluster 4 ha 407 scuole su 693 (58,7%) — questa informazione è data solo al §5.2, non qui dove sarebbe più pertinente.
3. **Generale**: i cluster non sono caratterizzati quantitativamente (medie per dimensione, variabilità intra-cluster). Il lettore non sa quanto sono compatti o sovrapposti.

### Flagged Issues
- [Statistical] Criterio di scelta del numero di cluster non riportato (riga 143)
- [Statistical] Mancata caratterizzazione quantitativa dei cluster (medie, variabilità) (righe 147, 155)
- [Statistical] Percentuali dei cluster non riportate nella sezione risultati (righe 147, 155)

---

## §4.5 — Reti territoriali e metodologie didattiche

### Comments
1. **Riga 169**: le percentuali di partnership sono riportate senza specificare la base di calcolo (scuole che hanno almeno una partnership? tutte le scuole?). Questo rende il dato ambiguo.
2. **Riga 171**: STEM nel 99,2% dei PTOF — un dato così estremo merita una verifica. Potrebbe riflettere un artefatto di codifica (qualunque riferimento a scienze/tecnologia viene classificato come STEM) piuttosto che una reale adozione di metodologia STEM.

### Flagged Issues
- [Measurement] Base di calcolo delle percentuali di partnership non specificata (riga 169)
- [Validity] 99,2% STEM potrebbe essere un artefatto di codifica, non verificato (riga 171)

---

## §4.6 — Catalogo delle attività

### Comments
1. **Riga 175**: la classificazione a tre livelli (6 categorie, 18 tipologie, 22 ambiti) è ricca ma la tassonomia non è validata. C'è accordo inter-codificatore tra i modelli LLM usati? Qual è il tasso di accordo sulla classificazione?
2. **Riga 179**: «solo 82 attività su oltre 42.000 catalogate (0,5%) riguardano l'intelligenza artificiale» — questo dato è suggestivo ma andrebbe contestualizzato: quante scuole hanno almeno un'attività AI? Il dato a livello di attività può essere fuorviante se poche scuole generano molte attività.
3. **Generale**: il catalogo è presentato come risultato ma è anche metodo (classificazione). La distinzione non è chiara.

### Flagged Issues
- [Measurement] Tassonomia del catalogo non validata (accordo inter-codificatore assente) (riga 175)
- [Statistical] Dato 0,5% AI calcolato su attività, non su scuole — potenzialmente fuorviante (riga 179)

---

## §4.7 — Convergenza tra lettura umana e analisi automatica

### Comments
1. **Riga 183**: questa sezione ripete quasi verbatim quanto già detto al §3.6. È una duplicazione. La validazione andrebbe trattata in una sede sola (metodo o risultati), non in entrambe.
2. **Riga 183**: «convergenza sostanziale» e «complementarità» sono affermazioni qualitative. Sarebbe più forte riportare una metrica di accordo, anche solo percentuale di concordanza sui temi principali.

### Flagged Issues
- [Validity] Duplicazione del contenuto tra §3.6 e §4.7 (riga 183)
- [Measurement] Convergenza solo qualitativa, nessuna metrica di accordo (riga 183)

---

## §5.1 — Il divario tra documento e pratica

### Comments
1. **Riga 191**: «Un IIPO basso riflette tanto l'assenza di pratiche quanto l'incapacità di descriverle» — questa distinzione è cruciale ma non è supportata da evidenza empirica. Come fa la pipeline a distinguere i due casi? Se non lo fa, l'affermazione è speculativa.
2. **Riga 193**: Fiorin (2019) è citato a sostegno ma è una fonte singola e non recentissima. La letteratura sulla funzione dichiarativa dei PTOF meriterebbe un supporto più ampio.

### Flagged Issues
- [Overclaiming] Distinzione assenza-pratiche vs. incapacità-descrizione non supportata empiricamente (riga 191)
- [Validity] Supporto bibliografico limitato per la tesi della funzione dichiarativa (riga 193)

---

## §5.2 — La frammentazione come tratto dominante

### Comments
1. **Riga 201**: «125 scuole su 246 (50,8%), 407 su 693 (58,7%)» — queste percentuali NON sono nel §4.4, dove il lettore le cercherebbe. Appaiono solo qui, nella discussione. Andrebbero riportate anche nei risultati.
2. **Riga 203**: il parallelo con Cavalli e Argentin (2010) e Colombo (2021) è pertinente ma il meccanismo «innesto di attività aggiuntive senza revisione strutturale» è un'interpretazione, non un dato. La pipeline non misura l'innovazione normativa, solo la documentazione.

### Flagged Issues
- [Validity] Dati quantitativi sulla frammentazione assenti nei risultati, presenti solo in discussione (riga 201)

---

## §5.4 — Limiti metodologici

### Comments
1. **Riga 221**: i quattro limiti sono pertinenti e ben articolati. Apprezzo particolarmente l'onestà sul punto 2 (effetto compensazione) e sul punto 4 (distanza documento-pratica).
2. **Riga 225**: il limite 3 cita «Gemini 3 Pro, GLM-5, MiniMax M2.5» ma omette Qwen3, citato al §3.3 e §3.5. Inconsistenza.
3. **Generale**: manca un limite importante: la dipendenza dalla qualità della conversione PDF→Markdown. Se il PDF è scansionato, illeggibile o ha tabelle complesse, la pipeline fallisce silenziosamente?

### Flagged Issues
- [Reproducibility] Elenco modelli inconsistente tra §3.3/§3.5 e §5.4 (riga 225)
- [Validity] Mancata discussione del limite di conversione PDF→Markdown (righe 221-227)

---

## §6 — Conclusioni

### Comments
1. **Riga 243**: la pipeline è descritta come «a quattro agenti — Analyst, Reviewer, Refiner» ma ne vengono elencati solo tre. Il Background Reviewer è omesso. Inconsistenza con §3.3.
2. **Riga 249**: «il campione non è pienamente rappresentativo» — formulazione più debole di quanto emerso al §4.1, dove le distorsioni sono quantificate (+16–19 pp per le paritarie). La conclusione dovrebbe essere più precisa.
3. **Riga 251–253**: la chiusura è retoricamente efficace ma l'affermazione «l'analisi automatica su larga scala della documentazione scolastica è possibile e produce dati utilizzabili» è già stata dimostrata. La conclusione potrebbe spingersi oltre: cosa serve per passare da «possibile» a «affidabile»?

### Flagged Issues
- [Reproducibility] Pipeline descritta come «a quattro agenti» ma ne elenca tre; Background Reviewer omesso (riga 243)
- [Validity] Formulazione della non-rappresentatività meno precisa dei dati disponibili (riga 249)

---

## Bibliography Check

- **Cochran 1977 e Lohr 2010**: citazioni corrette, presenti in .bib. Tuttavia Lohr è citato come supporto generico al campionamento stratificato — la reference specifica (capitolo, pagina) rafforzerebbe la precisione.
- **Fiorin 2019**: citato al §5.1. Presenza in .bib verificata. La citazione è pertinente ma singola — la letteratura sulla funzione dichiarativa dei PTOF meriterebbe 1-2 riferimenti aggiuntivi.
- **De Nardo 2026**: correttamente qualificato come «report interno non pubblicato». Tuttavia, il suo uso come fonte primaria di validazione (§3.6, §4.7) è metodologicamente fragile.
- **Cavalli e Argentin 2010, Colombo 2021**: presenti in .bib, citazioni pertinenti.
- **Gemini 3 Pro, GLM-5, MiniMax M2.5, Qwen3**: citati come modelli ma non hanno riferimenti bibliografici formali.
- **Assenti**: mancano riferimenti alla letteratura su inter-rater reliability per LLM, accordo inter-codificatore, metriche di validazione per analisi automatica del testo.

---

## Priority Ranking

1. **Critical** — Assenza di metriche quantitative di qualità/accordo: inter-agente (§3.3), inter-codificatore catalogo (§4.6), convergenza AI-umano (§4.7). Senza queste, le affermazioni di affidabilità non sono supportate.
2. **Critical** — Algoritmo di clustering e criterio di scelta k=5 non specificati (§3.5, §4.4). I profili cluster non sono riproducibili.
3. **High** — Distorsioni campionarie descritte ma non corrette (nessuna post-stratificazione, §4.1). Le stime puntuali potrebbero essere distorte in modo noto e non corretto.
4. **High** — IIPO come media semplice non testato contro alternative; manca analisi di sensitività (§3.2). La scelta dell'indice condiziona tutti i risultati.
5. **High** — Campione di validazione qualitativa (16 PTOF) insufficiente per l'affermazione «affiancare l'analisi umana su scala nazionale» (Obiettivo 2, §3.6).
6. **Medium** — Duplicazione §3.6/§4.7 sulla validazione.
7. **Medium** — Modelli LLM non mappati agli agenti in modo riproducibile (§3.3).
8. **Medium** — Soglia IIPO ≤ 2,0 per filtro non-PTOF non validata con analisi di sensitività (§3.4).
9. **Low** — Elenco modelli inconsistente tra §3.3/§3.5 e §5.4.
10. **Low** — Dato 0,5% AI calcolato su attività, non su scuole (§4.6).
