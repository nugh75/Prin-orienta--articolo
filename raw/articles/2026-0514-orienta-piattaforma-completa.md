# ORIENTA+ — Documentazione completa della piattaforma

Fonte: istruzioni di progetto (14 maggio 2026)

---

## Cosa fa la piattaforma

Orienta+ analizza la presenza nei PTOF di contenuti rilevanti per l'orientamento. Attraverso un sistema basato sull'intelligenza artificiale, la piattaforma legge i documenti scolastici per identificare, estrarre e valutare le informazioni relative alle attività, alle metodologie e alla governance dell'orientamento.

Restituisce una lettura comparabile e trasparente dell'orientamento scolastico, integrando punteggi strutturati, report narrativi e strumenti di confronto per territorio e profilo di scuola, mantenendo sempre il legame con le evidenze testuali dei documenti.

Inoltre, il sistema elabora una categorizzazione delle attività (consultabile nella pagina Attività della sezione Esplorazione): le iniziative estratte vengono classificate per tipologia (es. metodologie innovative, partnership, inclusione), creando un catalogo navigabile delle pratiche di orientamento.

### ⚠️ Importante: Natura dell'Analisi

Questa piattaforma NON giudica la qualità della scuola né crea una classifica delle scuole più virtuose. L'obiettivo è esclusivamente analizzare la documentazione PTOF: gli indici prodotti rappresentano il grado di copertura informativa delle dimensioni indagate dalla ricerca. Un punteggio basso non significa che la scuola non faccia orientamento, ma che tali azioni non sono esplicitamente o dettagliatamente riportate nel Piano Triennale dell'Offerta Formativa.

## 1. Il Contesto del Progetto

La piattaforma Orienta+ fa parte del progetto di dottorato di Daniele Dragoni ed ha lo scopo di analizzare i PTOF (Piani Triennali dell'Offerta Formativa) delle scuole italiane.

Essendo le scuole italiane oltre 60.000, non è possibile analizzarle tutte manualmente. Di conseguenza, si esegue un campionamento a strati per avere un campione rappresentativo.

## Come funziona l'analisi

L'analisi automatizzata non si limita a cercare parole chiave, ma legge e interpreta il testo del PTOF su due livelli complementari:

1. **Analisi Strutturale (Compliance)** — Il sistema verifica anzitutto la conformità formale rispetto alle Linee Guida (DM 328/2022). Identifica la presenza di una sezione esplicitamente dedicata all'orientamento nell'indice o nel corpo del testo, valutandone la visibilità e la struttura nel documento.

2. **Analisi Semantica e di Contenuto** — Attraverso modelli di linguaggio avanzati (LLM), la piattaforma "legge" l'intero documento per estrarre informazioni sulla copertura informativa delle 6 dimensioni chiave del framework. In questa fase, il sistema distingue le semplici dichiarazioni di intenti dalle azioni concrete, mappando la presenza di progetti, risorse, tempi e responsabilità. L'algoritmo rileva il contesto in cui appaiono i termini: se l'orientamento è citato in una lista generica o se è descritto attraverso laboratori con obiettivi e modalità di verifica.

Il risultato è una fotografia della ricchezza documentale: l'indice misura in che grado il PTOF riporti non solo intenzioni ma dettagli operativi e strutturali.

## 2. Framework di Valutazione (Analisi Qualitativa)

L'analisi si basa su sei dimensioni chiave che valutano la presenza e la qualità delle azioni di orientamento descritte nei documenti.

### 1. Dimensione Strutturale e di Contesto

**Sezione dedicata (Spazio esplicito all'orientamento):** verifica se l'orientamento ha dignità strutturale nel documento. Una sezione è considerata solida quando:
- È facilmente rintracciabile nel sommario.
- Non disperde le informazioni in paragrafi frammentati ma offre un quadro organico.
- Definisce chiaramente strumenti, tempi e responsabilità organizzative.

**Partnership (Reti territoriali e soggetti esterni):** indicatori di apertura della scuola verso l'esterno. La valutazione premia:
- Qualità del coinvolgimento: descrizioni di attività congiunte, co-progettazione di percorsi, visite aziendali o laboratori universitari.
- Soggetti nominati: citazione esplicita di università, ITS, imprese, enti locali o associazioni del terzo settore.
- Consistenza: presenza di accordi formali, obiettivi condivisi e continuità nel tempo.

### 2. Finalità dell'Orientamento

Indaga perché la scuola fa orientamento e quali obiettivi educativi si pone:
- **Attitudini e Talenti:** azioni per far scoprire allo studente i propri punti di forza.
- **Interessi Professionali:** esplorazione di ambiti disciplinari e mondo del lavoro.
- **Progetto di Vita:** supporto alla costruzione di una traiettoria personale, coinvolgendo la famiglia.
- **Transizioni Formative:** accompagnamento nei passaggi critici (media→superiore, superiore→università/lavoro).
- **Capacità Orientativa (Empowerment):** insegnare allo studente a sapersi orientare autonomamente.

### 3. Obiettivi di Incidenza

Impatti sociali e sistemici che la scuola intende generare:
- **Contrasto alla Dispersione:** prevenzione dell'abbandono, tutoraggio per studenti a rischio.
- **Riduzione dei NEET:** collegamento tra scuola e futuro occupazionale.
- **Continuità Territoriale:** ponti stabili tra i diversi gradi di istruzione.
- **Lifelong Learning:** orientamento come competenza per tutto l'arco della vita.

### 4. Governance e Organizzazione

Analizza "chi fa cosa":
- **Coordinamento:** presenza di Funzioni Strumentali, commissioni orientamento o referenti.
- **Dialogo Interno:** integrazione nella didattica quotidiana, condivisione nel Consiglio di Classe.
- **Alleanza con le Famiglie:** azioni per informare e supportare i genitori.
- **Monitoraggio e Valutazione:** dati, questionari di feedback, analisi degli esiti a distanza.
- **Inclusione:** attenzione a BES e differenze culturali.

### 5. Didattica Orientativa

Il cuore dell'azione formativa:
- **Laboratoriale ed Esperienziale:** imparare facendo (simulazioni, project work).
- **Esperienza degli Studenti:** centralità dell'alunno come protagonista attivo.
- **Interdisciplinarità:** orientamento dentro le materie curricolari.
- **Flessibilità Organizzativa:** adattamento di orari, gruppi e spazi.

### 6. Opportunità Formative

L'ecosistema delle proposte:
- Attività Culturali, Espressive e Artistiche.
- Sport e Benessere.
- Volontariato e Cittadinanza Attiva.
- Proposte Ludiche e di Socializzazione.

Il punteggio cresce quando queste attività sono presentate come tessere di un mosaico che contribuisce alla crescita globale dello studente.

## 3. Metrica di Valutazione (Analisi Quantitativa)

### Criteri di Punteggio (Scala Likert 1-7)

| Punteggio | Livello | Descrizione |
|-----------|---------|-------------|
| 1 | Assente | Nessun riferimento |
| 2 | Generico | Menzionato vagamente, copia-incolla normativo |
| 3 | Limitato | C'è un'intenzione, ma mancano i dettagli attuativi |
| 4 | Sufficiente | Azioni descritte chiaramente ma basilari |
| 5 | Buono | Azioni strutturate, con metodologie definite |
| 6 | Ottimo | Azioni integrate, innovative e ben monitorate |
| 7 | Eccellente | Best practice sistemica, valutata e migliorata ciclicamente |

### Griglia di valutazione sintetica delle dimensioni (1-7)

| Punteggio | Descrizione |
|-----------|-------------|
| 0.0 - 1.0 | Nessun riferimento |
| 1.1 - 2.2 | Accenni minimi |
| 2.3 - 3.4 | Riferimenti generici, poco strutturati |
| 3.5 - 4.6 | Presenza di azioni basilari ma non coordinate |
| 4.7 - 5.8 | Sistema strutturato, buona copertura |
| 5.9 - 7.0 | Sistema eccellente, dettagliato e monitorato |

### IIPO (Indice Informativo delle Pratiche di Orientamento)

```
IIPO = (S + F + O + G + D + Op) / 6
```

Interpretazione:
- 0.0 - 1.0: Non classificabile / Errore (scartato)
- 1.1 - 2.2: Accenni minimi
- 2.3 - 3.4: Riferimenti generici, poco strutturati
- 3.5 - 4.6: Presenza di azioni basilari ma non coordinate
- 4.7 - 5.8: Sistema strutturato, buona copertura
- 5.9 - 7.0: Sistema eccellente, dettagliato e monitorato

### Note Metodologiche sull'IIPO

**Sensibilità Strumentale:** L'indice è progettato per riflettere variazioni incrementali nelle singole dimensioni. Ogni miglioramento nella documentazione si traduce in un incremento del valore finale.

**Standard di Settore:** L'adozione della media aritmetica su scala Likert (1-7) è conforme alle metodologie internazionali per gli indici di maturità (es. Digital Maturity Index).

**Effetto Compensazione (Limiti della Media):** La media aritmetica può generare un "effetto compensazione": una performance eccellente in una dimensione può mascherare carenze critiche in altre aree. L'IIPO deve essere sempre analizzato in combinazione con i punteggi delle singole dimensioni.

## 4. Report Narrativo e Output

Accanto ai punteggi, il sistema produce un report narrativo standardizzato:
1. Sintesi generale
2. Analisi dimensionale (dettaglio sezione per sezione)
3. Punti di forza
4. Aree di debolezza
5. Gap analysis (mancanze strutturali)
6. Conclusioni

L'output finale è doppio: JSON strutturato per analisi tecniche e Markdown per la lettura umana.

## 5. Categorizzazione e Catalogo Attività

La piattaforma costruisce un Catalogo Navigabile delle Attività. Il sistema estrae le singole iniziative descritte nei PTOF e le classifica automaticamente:
- **Categorie Principali:** Metodologie Didattiche Innovative, Progetti Esemplari, Partnership, Inclusione, ecc.
- **Ambiti di Attività:** STEM, Educazione Civica, PCTO, Arte & Creatività, ecc.
- **Tipologie di Metodologia:** Peer Tutoring, Gamification, Cooperative Learning, Debate, ecc.

Sono disponibili meta-report tematici generati aggregando informazioni su base trasversale (es. L'Inclusione nelle scuole del Sud, Le nuove metodologie nei Licei).

## 6. Strumenti di Analisi e Navigazione

- **📈 KPI (Dashboard):** visione d'insieme con KPI principali, IIPO medio nazionale, distribuzione punteggi.
- **🗺️ Analisi Territoriale:** mappe di calore, confronti tra macro-aree, regioni, gestione statale/paritaria.
- **📊 Analisi Dimensionale:** variazione delle dimensioni e sotto-indicatori per provincia, tipo istituto, dimensione scolastica.
- **🔬 Analytics Avanzati:** clustering, PCA, matrici di correlazione, analisi lessicale (Word Cloud).

## 7. Ricerca e Impatto

- **🔎 Metodologie e Progetti:** motore di ricerca semantico per individuare scuole che adottano pratiche specifiche (Debate, STEM, Service Learning, PCTO).
- **📉 Impatto Metodologie e Progetti:** analisi statistica per misurare l'efficacia delle pratiche (differenza media, p-value, Cohen's d).

## 8. Analisi di Dettaglio

**🏫 Scuola: Dettaglio e Gap Analysis:** scheda completa per ogni istituto con radar di posizionamento, partnership attive, metodologie citate. Include analisi gap con suggerimento aree prioritarie di miglioramento e individuazione scuole "gemelle" (Peer).
