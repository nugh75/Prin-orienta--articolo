# Piattaforma ORIENTA+ — Documentazione Tecnica

Data acquisizione: 2026-05-13
Fonte: orienta.ai4educ.org

## Cosa fa la piattaforma

Orienta+ analizza la presenza nei PTOF di contenuti rilevanti per l'orientamento. Attraverso un sistema basato sull'intelligenza artificiale, la piattaforma legge i documenti scolastici per identificare, estrarre e valutare le informazioni relative alle attività, alle metodologie e alla governance dell'orientamento.

Restituisce una lettura comparabile e trasparente dell'orientamento scolastico, integrando punteggi strutturati, report narrativi e strumenti di confronto per territorio e profilo di scuola, mantenendo sempre il legame con le evidenze testuali dei documenti.

Inoltre, il sistema elabora una categorizzazione delle attività (consultabile nella pagina Attività della sezione Esplorazione): le iniziative estratte vengono classificate per tipologia (es. metodologie innovative, partnership, inclusione), creando un catalogo navigabile delle pratiche di orientamento.

### ⚠️ Importante: Natura dell'Analisi

Questa piattaforma **NON** giudica la qualità della scuola né crea una classifica delle scuole più virtuose. L'obiettivo è esclusivamente analizzare la documentazione PTOF: gli indici prodotti rappresentano il grado di copertura informativa delle dimensioni indagate dalla ricerca. Un punteggio basso non significa che la scuola non faccia orientamento, ma che tali azioni non sono esplicitamente o dettagliatamente riportate nel Piano Triennale dell'Offerta Formativa.

---

## 1. Il Contesto del Progetto

La piattaforma Orienta+ fa parte del progetto di dottorato di Daniele Dragoni ed ha lo scopo di analizzare i PTOF (Piani Triennali dell'Offerta Formativa) delle scuole italiane.

Essendo le scuole italiane oltre 60.000, non è possibile analizzarle tutte manualmente. Di conseguenza, si esegue un campionamento a strati per avere un campione rappresentativo.

### Come funziona l'analisi

L'analisi automatizzata non si limita a cercare parole chiave, ma legge e interpreta il testo del PTOF su due livelli complementari:

**Analisi Strutturale (Compliance)**
Il sistema verifica anzitutto la conformità formale rispetto alle Linee Guida (DM 328/2022). Identifica la presenza di una sezione esplicitamente dedicata all'orientamento nell'indice o nel corpo del testo, valutandone la visibilità e la struttura nel documento.

**Analisi Semantica e di Contenuto**
Attraverso modelli di linguaggio avanzati (LLM), la piattaforma "legge" l'intero documento per estrarre informazioni sulla copertura informativa delle 6 dimensioni chiave del framework (che vengono dettagliate nel paragrafo successivo). In questa fase, il sistema distingue le semplici dichiarazioni di intenti dalle azioni concrete, mappando la presenza di progetti, risorse, tempi e responsabilità. L'algoritmo rileva il contesto in cui appaiono i termini: se l'orientamento è citato in una lista generica o se è descritto attraverso laboratori con obiettivi e modalità di verifica.

Il risultato è una fotografia della ricchezza documentale: l'indice misura in che grado il PTOF riporti non solo intenzioni ma dettagli operativi e strutturali.

---

## 2. Framework di Valutazione (Analisi Qualitativa)

L'analisi si basa su dimensioni chiave che valutano la presenza e la qualità delle azioni di orientamento descritte nei documenti. Di seguito presentiamo le dimensioni indagate, specificando cosa viene ricercato nel testo per considerare l'informazione "completa".

### 1. Dimensione Strutturale e di Contesto

**Sezione dedicata (Spazio esplicito all'orientamento)**
Questa dimensione verifica se l'orientamento ha dignità strutturale nel documento. Non ci si limita a cercare la parola "orientamento", ma si osserva se esiste un capitolo riconoscibile (nell'indice o con un titolo chiaro) che faccia da "casa" per tutte le azioni. Una sezione è considerata solida quando:

- È facilmente rintracciabile nel sommario.
- Non disperde le informazioni in paragrafi frammentati ma offre un quadro organico.
- Definisce chiaramente strumenti, tempi e responsabilità organizzative.

**Partnership (Reti territoriali e soggetti esterni)**
L'orientamento non si fa da soli. Le partnership sono lette come indicatori di apertura della scuola verso l'esterno. La valutazione premia:

- **Qualità del coinvolgimento**: non si cercano elenchi di nomi, ma si cercano descrizioni di attività congiunte, co-progettazione di percorsi, visite aziendali o laboratori universitari.
- **Soggetti nominati**: la citazione esplicita di università, ITS, imprese, enti locali o associazioni del terzo settore indica un rapporto reale e non solo teorico.
- **Consistenza**: presenza di accordi formali, obiettivi condivisi e continuità nel tempo.

### 2. Finalità dell'Orientamento

Questa dimensione indaga perché la scuola fa orientamento e quali obiettivi educativi si pone per gli studenti. Si articola in:

- **Attitudini e Talenti**: azioni volte a far scoprire allo studente i propri punti di forza e le proprie inclinazioni personali.
- **Interessi Professionali**: attività che permettono di esplorare ambiti disciplinari e il mondo del lavoro, per scelte informate e non basate su stereotipi.
- **Progetto di Vita**: la scuola come supporto alla costruzione di una traiettoria personale, coinvolgendo anche la famiglia in una visione a lungo termine.
- **Transizioni Formative**: l'accompagnamento nei momenti critici di passaggio (es. dalla media alla superiore, o verso l'università/lavoro), momenti in cui il rischio di dispersione è più alto.
- **Capacità Orientativa (Empowerment)**: non solo "dare informazioni", ma insegnare allo studente a sapersi orientare autonomamente (competenze trasversali di scelta e auto-valutazione).

### 3. Obiettivi di Incidenza

Qui si valutano gli impatti sociali e sistemici che la scuola intende generare attraverso l'orientamento:

- **Contrasto alla Dispersione**: misure specifiche di prevenzione dell'abbandono, tutoraggio per studenti a rischio e motivazione allo studio.
- **Riduzione dei NEET**: collegamento tra scuola e futuro occupazionale, lavorando sulle competenze chiave per l'occupabilità e sulla fiducia nel futuro.
- **Continuità Territoriale**: creazione di "ponti" stabili tra i diversi gradi di istruzione del territorio, per evitare fratture nel percorso formativo.
- **Lifelong Learning**: promozione dell'idea che l'orientamento non finisce con la scuola, ma è una competenza per tutto l'arco della vita.

### 4. Governance e Organizzazione

Un buon orientamento richiede un'organizzazione stabile. Questa dimensione analizza "chi fa cosa":

- **Coordinamento**: serve una regia. Si cerca la presenza di Funzioni Strumentali, commissioni orientamento o referenti chiaramente identificati.
- **Dialogo Interno**: l'orientamento non è delega di un solo docente, ma deve essere integrato nella didattica quotidiana e condiviso dal Consiglio di Classe.
- **Alleanza con le Famiglie**: azioni per informare e supportare i genitori, evitando che le scelte siano guidate solo dal "passaparola" o dall'ansia.
- **Monitoraggio e Valutazione**: la presenza di dati, questionari di feedback o analisi degli esiti a distanza indica un sistema che impara e si migliora.
- **Inclusione**: attenzione specifica ai Bisogni Educativi Speciali (BES) e alle differenze culturali, per un orientamento davvero democratico.

### 5. Didattica Orientativa

Il cuore dell'azione formativa. Si misura il passaggio dalle parole ai fatti didattici:

- **Laboratoriale ed Esperienziale**: l'imparare facendo. Attività pratiche in cui lo studente si mette alla prova (es. simulazioni, project work).
- **Esperienza degli Studenti**: centralità dell'alunno, che non è spettatore passivo di conferenze informative, ma protagonista attivo.
- **Interdisciplinarità**: quando l'orientamento entra nelle materie curricolari (es. orientamento narrativo in lettere, STEM in scienze) e non è recintato in ore extra-curricolari.
- **Flessibilità Organizzativa**: capacità di adattare orari, gruppi e spazi per personalizzare i percorsi.

### 6. Opportunità Formative

L'ecosistema delle proposte. Un'offerta ricca permette a ciascuno di trovare la sua strada. Si valuta la presenza e la varietà di:

- Attività Culturali, Espressive e Artistiche.
- Sport e Benessere.
- Volontariato e Cittadinanza Attiva.
- Proposte Ludiche e di Socializzazione.

Il punteggio cresce quando queste attività non sono presentate come "eventi isolati", ma come tessere di un mosaico che contribuisce alla crescita globale dello studente (accesso, continuità e ricadute educative).

---

## 3. Metrica di Valutazione (Analisi Quantitativa)

### Criteri di Punteggio (Scala Likert 1-7)

| Punteggio | Livello | Descrizione |
|-----------|---------|-------------|
| 1 | Assente | Nessun riferimento. |
| 2 | Generico | Menzionato vagamente, copia-incolla normativo. |
| 3 | Limitato | C'è un'intenzione, ma mancano i dettagli attuativi. |
| 4 | Sufficiente | Azioni descritte chiaramente ma basilari. |
| 5 | Buono | Azioni strutturate, con metodologie definite. |
| 6 | Ottimo | Azioni integrate, innovative e ben monitorate. |
| 7 | Eccellente | Best practice sistemica, valutata e migliorata ciclicamente. |

### Griglia di valutazione sintetica delle dimensioni (1-7)

Ogni dimensione è valutata rispetto alla sua completezza informativa. Il punteggio indica quanto il PTOF trasforma le intenzioni in azioni documentate.

| Punteggio | Descrizione |
|-----------|-------------|
| 0.0 - 1.0 | Nessun riferimento |
| 1.1 - 2.2 | Accenni minimi |
| 2.3 - 3.4 | Riferimenti generici, poco strutturati |
| 3.5 - 4.6 | Presenza di azioni basilari ma non coordinate |
| 4.7 - 5.8 | Sistema strutturato, buona copertura |
| 5.9 - 7.0 | Sistema eccellente, dettagliato e monitorato |

### IIPO (Indice di Documentazione Pratiche Orientamento)

L'IIPO è un indicatore sintetico che quantifica la completezza della documentazione delle pratiche di orientamento nel PTOF.

**Formula:**
```
IIPO = (Media_Strutturale + Media_Finalità + Media_Obiettivi + Media_Governance + Media_Didattica + Media_Opportunità) / 6
```

**Interpretazione:**

- 0.0 - 1.0: Non classificabile / Errore (scartato)
- 1.1 - 2.2: Accenni minimi
- 2.3 - 3.4: Riferimenti generici, poco strutturati
- 3.5 - 4.6: Presenza di azioni basilari ma non coordinate
- 4.7 - 5.8: Sistema strutturato, buona copertura
- 5.9 - 7.0: Sistema eccellente, dettagliato e monitorato

### Note Metodologiche sull'IIPO

**Sensibilità Strumentale**
L'indice è progettato per riflettere variazioni incrementali nelle singole dimensioni. Ogni miglioramento nella documentazione di una specifica area si traduce in un incremento del valore finale, permettendo un monitoraggio preciso dell'evoluzione qualitativa del PTOF.

**Standard di Settore**
L'adozione della media aritmetica su scala Likert (1-7) è conforme alle metodologie internazionali utilizzate per gli indici di maturità (es. Digital Maturity Index). Questo approccio tratta i punteggi come variabili quasi-numeriche, garantendo rigore statistico e facilità di interpretazione.

**Effetto Compensazione (Limiti della Media)**
È fondamentale rilevare che la media aritmetica può generare un "effetto compensazione": una performance eccellente in una dimensione può mascherare carenze critiche in altre aree. Pertanto, l'IIPO deve essere sempre analizzato in combinazione con i punteggi delle singole dimensioni per identificare eventuali squilibri strutturali nel sistema di orientamento.

---

## 4. Report Narrativo e Output

Accanto ai punteggi, il sistema produce un report narrativo che spiega le valutazioni, riporta le evidenze e collega le dimensioni tra loro. La struttura del report è standardizzata:

- Sintesi generale
- Analisi dimensionale (dettaglio sezione per sezione)
- Punti di forza
- Aree di debolezza
- Gap analysis (mancanze strutturali)
- Conclusioni

L'output finale è doppio: un JSON strutturato per analisi tecniche e un Markdown per la lettura umana.

---

## 5. Categorizzazione e Catalogo Attività

Oltre all'analisi dei documenti, la piattaforma costruisce un **Catalogo Navigabile delle Attività** (consultabile nella sezione Esplorazione → Attività). Il sistema estrae le singole iniziative descritte nei PTOF e le classifica automaticamente in categorie predefinite per facilitarne la consultazione e il confronto:

- **Categorie Principali**: raggruppamento macro, come Metodologie Didattiche Innovative, Progetti Esemplari, Partnership, Inclusione, ecc.
- **Ambiti di Attività**: il tema specifico trattato, ad esempio STEM, Educazione Civica, PCTO, Arte & Creatività.
- **Tipologie di Metodologia**: il metodo pedagogico utilizzato, come Peer Tutoring, Gamification, Cooperative Learning, Debate.

Grazie a questa strutturazione, è possibile filtrare e ricercare le attività non solo per scuola, ma anche per parole chiave, territorio o tipologia, permettendo di scoprire buone pratiche e idee da replicare.

Inoltre, nella pagina Report (sezione Esplorazione), sono disponibili dei **meta-report tematici** generati aggregando le informazioni su base trasversale. Questi dossier offrono approfondimenti verticali su specifici argomenti (es. L'Inclusione nelle scuole del Sud, Le nuove metodologie nei Licei), sfruttando la ricchezza informativa del catalogo attività.

---

## 6. Strumenti di Analisi e Navigazione

Per esplorare i dati raccolti, la piattaforma offre quattro strumenti principali di indagine, ciascuno con un filtro e una prospettiva specifica:

### 📈 KPI (Dashboard)

Il punto di partenza per una visione d'insieme.

- **Cosa mostra**: I KPI principali, l'Indice di Completezza medio nazionale e la distribuzione dei punteggi.
- **Variabili**: Permette di filtrare rapidamente per Macro-area, Regione e Livello Scolastico per ottenere un primo spaccato dei dati.

### 🗺️ Analisi Territoriale

Focalizzata sulla geografia e sui divari regionali.

- **Cosa mostra**: Mappe di calore e confronti statistici tra le diverse zone d'Italia.
- **Variabili**: Analizza le differenze tra Macro-aree (Nord/Centro/Sud) e singole Regioni, confrontando anche la gestione (Statale vs Paritaria) per evidenziare pattern di distribuzione territoriali.

### 📊 Analisi Dimensionale

Scende nel dettaglio qualitativo del framework.

- **Cosa mostra**: Come variano le 5 dimensioni (Finalità, Obiettivi, Governance, Didattica, Opportunità) e i relativi sotto-indicatori.
- **Variabili**: Offre i filtri più granulari, permettendo di incrociare Provincia, Tipo di Istituto (Licei, Tecnici, Professionali, Comprensivi) e Dimensione scolastica, per capire ad esempio se la "Didattica Orientativa" è più presente in un certo tipo di scuola o territorio.

### 🔬 Analytics Avanzati

Strumenti statistici e di data mining per approfondimenti.

- **Cosa mostra**: Relazioni nascoste tra i dati che non emergono dalle medie semplici.
- **Variabili**: Utilizza Clustering e PCA per raggruppare le scuole in base alla similitudine dei contenuti (indipendentemente dalla posizione), Matrici di Correlazione per scoprire legami tra le dimensioni (es. "Una buona governance influenza la didattica?") e Analisi Lessicale (Word Cloud) per visualizzare i temi ricorrenti nei testi.

---

## 7. Ricerca e Impatto

Queste due sezioni permettono di andare oltre la fotografia dell'esistente per indagare l'efficacia delle pratiche educative:

### 🔎 Metodologie e Progetti

Un motore di ricerca semantico per individuare le scuole che adottano specifiche pratiche didattiche.

- **Funzione**: Permette di trovare istituti che citano nel PTOF parole chiave come Debate, STEM, Service Learning, PCTO, ecc.
- **Utilità**: Ideale per creare reti di scuole, scoprire chi sta innovando su temi specifici e analizzare la diffusione territoriale di certe metodologie.

### 📉 Impatto Metodologie e Progetti

Uno strumento di analisi statistica per misurare l'efficacia delle pratiche.

- **Funzione**: Confronta le scuole che adottano una certa metodologia con quelle che non la usano, calcolando se esiste una differenza significativa nell'IIPO.
- **Utilità**: Risponde a domande come "Le scuole che fanno Debate hanno mediamente un IIPO più alto?", fornendo dati su differenza media, significatività statistica (p-value) e dimensione dell'effetto (Cohen's d).

---

## 8. Analisi di Dettaglio

Questi strumenti operano a livello granulare, scendendo nel dettaglio del singolo istituto:

### 🏫 Scuola: Dettaglio e Gap Analysis

La scheda completa di ogni singolo istituto censito.

- **Cosa mostra**: Il Radar di posizionamento della scuola rispetto alla media (nazionale, regionale o per tipologia), l'elenco delle partnership attive e le metodologie citate.
- **Analisi Gap**: Include una funzione avanzata che suggerisce le aree prioritarie di miglioramento e identifica scuole "gemelle" (Peer) da cui prendere ispirazione.