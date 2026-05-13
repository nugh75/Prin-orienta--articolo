# SEZIONE 2 - AVANZAMENTO DELLE ATTIVITÀ — Linea PTOF (Macrotema A)

Data acquisizione: 2026-05-13
Fonte: Report avanzamento PRIN — Macrotema A

---

## Premessa

Nel quadro del Macrotema A, all'indagine nazionale tramite questionari è stata affiancata un'analisi dei PTOF con funzione di supporto metodologico e interpretativo. Poiché una lettura integralmente manuale di migliaia di documenti sarebbe risultata eccessivamente onerosa in termini di tempo, questa linea è stata sviluppata attraverso una metodologia mista, fondata sull'integrazione tra analisi automatizzata e lettura qualitativa, con l'obiettivo di produrre una lettura comparabile e trasparente della documentazione scolastica sull'orientamento.

---

## Costruzione della piattaforma ORIENTA+

È stata costruita e implementata la piattaforma ORIENTA+, con lo scopo di misurare il grado di informatività delle pratiche orientative nei PTOF attraverso l'IIPO (Indice Informativo delle Pratiche di Orientamento).

È importante precisare che l'IIPO misura esclusivamente quanto le informazioni sull'orientamento sono documentate nel PTOF e non costituisce un ranking né un giudizio di valore sulle pratiche di orientamento delle scuole, che sono per loro natura complesse, situate e personalizzate per ciascuno studente.

L'IIPO è un indice sintetico costruito come media di sei dimensioni di analisi: dimensione strutturale e di contesto, finalità dell'orientamento, obiettivi di incidenza, governance e organizzazione, didattica orientativa, opportunità formative. Ciascuna dimensione è a sua volta articolata in sotto-dimensioni e sotto-indicatori, così da distinguere tra enunciazioni generiche e azioni effettivamente documentate nel PTOF.

Il sistema, con il supporto di LLM, analizza i PTOF individuando contenuti rilevanti per l'orientamento, classifica le evidenze testuali, quantifica il grado di documentazione per ciascuna dimensione e genera report narrativi.

---

## Campionamento

Il campionamento delle scuole delle quali analizzare i PTOF è stato impostato secondo un disegno stratificato a più stadi. Ogni scuola è stata collocata in uno strato definito da gestione (statale/paritaria), area geografica (Nord-Ovest, Nord-Est, Centro, Sud, Isole), territorio (metropolitano/non metropolitano) e ordine scolastico (infanzia, primaria, secondaria di I grado, secondaria di II grado, altro), per un massimo di 100 strati potenziali. L'estrazione è avvenuta in modo proporzionale alla dimensione di ciascuno strato, per garantire rappresentatività nazionale.

---

## Fase operativa

La fase operativa ha previsto, per ogni scuola selezionata, ricerca dell'URL del PTOF, download del PDF, conversione in markdown, analisi testuale e controlli di qualità.

L'analisi automatizzata è stata eseguita con architettura multi-agente (Analyst, Reviewer, Refiner): il primo agente estrae e valuta le evidenze, il secondo verifica coerenza e robustezza delle valutazioni, il terzo consolida l'output finale in formato strutturato e narrativo.

L'intera pipeline è stata costruita secondo un approccio **human in the loop**, inteso come integrazione continua tra attività umana e supporto della macchina nei diversi passaggi dell'analisi. Alla macchina sono state affidate la lettura estensiva dei documenti, l'estrazione delle informazioni, la classificazione delle attività, la pre-strutturazione dei dati e la generazione di scenari interpretativi e prospettive possibili; all'umano sono rimaste la progettazione del framework, la definizione degli obiettivi, la scelta dei criteri interpretativi, la validazione dei casi dubbi, la revisione dei documenti non pertinenti e la decisione finale tra le diverse ipotesi restituite dal sistema.

---

## Avanzamento dei numeri

Sono stati completati **78 cicli di estrazione** su 15.035 scuole selezionate. Il processo di campionamento è stato condotto in modo iterativo: a ogni ciclo il sistema verificava la rappresentatività del campione già acquisito rispetto alla popolazione delle scuole del MIM e ribilanciava l'estrazione successiva attribuendo maggiore peso agli strati sottorappresentati nei dati raccolti fino a quel momento, così da convergere progressivamente verso una distribuzione proporzionale alla realtà nazionale.

Nel processo complessivo sono stati scaricati **3.082 PTOF**; dopo validazione, bonifica e controlli di coerenza, la base analitica utilizzata per la lettura comparativa della secondaria comprende **2.095 documenti**, con campione finale validato pari a **693 PTOF di II grado** e **246 PTOF di I grado**, integrato da **16 letture qualitative in profondità**. I restanti documenti riguardano scuole dell'infanzia e primaria, per le quali è stata calcolata la valutazione IIPO ma non è stato ancora prodotto un report analitico dedicato.

A valle del ciclo 53 è stata inoltre condotta una bonifica massiva del dataset con riconciliazione dei codici meccanografici, rimozione dei documenti «impostori» e standardizzazione della catena PDF → Markdown → Analisi → Attività.

---

## Framework di valutazione

Il framework di valutazione combina **analisi strutturale** (compliance formale al D.M. 328/2022) e **analisi semantica di contenuto**. La scala utilizzata è **Likert 1-7**.

Il valore finale dell'IIPO sintetizza la copertura informativa complessiva del PTOF, mentre i sotto-indicatori consentono di leggere in modo analitico i diversi aspetti dell'orientamento, come transizioni, monitoraggio, inclusione, laboratorialità e partnership.

---

## Risultati principali

I risultati indicano una presenza diffusa dell'orientamento, ma con livelli di strutturazione ancora disomogenei: **IIPO medio 3,48/7 nel II grado** e **3,44/7 nel I grado**.

Tra i sotto-indicatori risultano relativamente più solidi gli aspetti relazionali e inclusivi (es. Scuola-Genitori: 3,95 nel II grado e 4,05 nel I grado), mentre emergono criticità nella formalizzazione strutturale (2,62 e 2,39), nel monitoraggio (3,06 e 2,79) e nel contrasto NEET (2,41 e 2,04).

La lettura per cluster conferma che il profilo prevalente è la progettualità diffusa ma frammentata (**59% nel II grado; 51% nel I grado**), segnalando la necessità di maggiore integrazione curricolare.

### Cluster — Secondaria di II grado

| Cluster | Scuole | Profilo |
|---------|--------|---------|
| 0 | 112 (16%) | Approccio integrato e didattico |
| 1 | 77 (11%) | Approccio relazionale e di accoglienza |
| 2 | 25 (4%) | Approccio PCTO-centrico dichiarativo |
| 3 | 50 (7%) | Approccio frammentato |
| 4 | 407 (59%) | Progettualità diffusa ma non pienamente integrata |

### Cluster — Secondaria di I grado

| Cluster | Scuole | Profilo |
|---------|--------|---------|
| 0 | 67 (27%) | Approccio integrato e curricolare |
| 1 | 21 (9%) | Focalizzato su benessere e accoglienza |
| 2 | 12 (5%) | Approccio dichiarativo formale |
| 3 | 19 (8%) | Generalista e non strutturato |
| 4 | 125 (51%) | Progettuale frammentato |

---

## Catalogo delle attività

Accanto alla valutazione dimensionale, ORIENTA+ ha estratto e categorizzato automaticamente le singole iniziative presenti nei PTOF, costruendo un **catalogo navigabile delle attività** per tipologia (metodologie innovative, partnership, inclusione, governance e altre aree). Questa componente consente analisi trasversali per territorio, profilo di scuola e tematica, con output in formato tecnico (JSON) e narrativo (Markdown), utili sia per ricerca sia per restituzione operativa.

Proprio la rilevazione delle attività mostra che alcuni ambiti risultano ancora debolmente presenti nella documentazione scolastica: un esempio significativo riguarda l'**intelligenza artificiale**, esplicitamente richiamata in solo **82 attività su 17.187 catalogate (0,5%)**, dato che segnala quanto questo tema sia ancora marginale nei PTOF.

---

## Quadro complessivo

Il quadro complessivo dei risultati delinea un sistema scolastico in cui l'orientamento è riconosciuto e presente, ma ancora in fase di piena strutturazione e integrazione curricolare.

---

## Punto 2 — Modifiche rispetto al programma approvato

Va esplicitato che la linea di analisi PTOF costituisce un'integrazione rispetto al programma PRIN inizialmente dichiarato. Tale integrazione ha mantenuto invariata la finalità scientifica del Macrotema A.

---

## Punto 3 — Sfide e azioni di miglioramento

Le criticità principali sono state la **reperibilità non uniforme dei PTOF**, la **qualità eterogenea della documentazione** e la **presenza di file non pertinenti**. Le azioni correttive hanno incluso ricerca multi-sorgente, validazione incrementale, bonifica periodica e controllo incrociato AI-umano.

Il modello **human in the loop** è risultato centrale: l'AI ha garantito scala, rapidità e comparabilità; la componente umana ha mantenuto il governo epistemologico dell'analisi, cioè la responsabilità sulle scelte di impianto, sugli obiettivi di lettura e sull'interpretazione finale dei risultati.

---

## Attività future

Le attività future della linea PTOF si articolano su più direttrici:

**Piano analitico**
- Produzione dei report dedicati per le scuole dell'infanzia e primaria, già valutate in termini di IIPO ma non ancora oggetto di restituzione
- Ampliamento della base campionaria con l'inclusione di ulteriori PTOF, così da rafforzare rappresentatività e granularità
- Dimensione longitudinale: la raccolta periodica dei PTOF consentirà di monitorare l'evoluzione delle pratiche orientative e di valutare l'impatto delle politiche nazionali sulla documentazione scolastica

**Piano metodologico**
- Consolidamento dell'uso dei sotto-indicatori, dell'analisi per cluster e del monitoraggio d'impatto
- Triangolazione tra quanto dichiarato nei PTOF e quanto rilevato attraverso il questionario nazionale PRIN

**Piano tecnico**
- Miglioramento del workflow di processo: ottimizzazione della pipeline di estrazione, correzione dei bug residui, rafforzamento dei controlli di qualità automatizzati
- Confronto sistematico tra valutazioni AI e lettura umana su un sottocampione più ampio, al fine di affinare la calibrazione dei punteggi

**Piano della restituzione**
- Perfezionamento dei report individualizzati per le singole istituzioni scolastiche, utilizzabili come strumento di autovalutazione e miglioramento
- Pubblicazione del dataset e degli strumenti di analisi per favorire la replicabilità della ricerca
- Estensione dell'analisi ai **Rapporti di Autovalutazione (RAV)**, che in quanto documenti di monitoraggio e valutazione consentirebbero di triangolare le dichiarazioni dei PTOF con le pratiche effettivamente autovalutate dalle scuole
- Utilizzo della categorizzazione delle attività per individuare pratiche trasferibili e supportare percorsi formativi su progettazione orientativa, governance e valutazione

**Prospettiva di lungo termine**
- Trasformazione di ORIENTA+ da strumento di ricerca a **portale di scambio e ispirazione tra scuole**: una piattaforma in cui le istituzioni scolastiche possano esplorare come scuole con profili simili affrontano l'orientamento in modo diverso, individuare pratiche concrete per rafforzare le proprie aree di criticità e confrontarsi sulle soluzioni adottate in tema di governance, monitoraggio, inclusione e didattica orientativa

---

## Punto 4 — Potenziali pubblicazioni

Il lavoro apre tre direttrici principali:
1. Validazione dell'approccio integrato AI-umano nell'analisi documentale dei PTOF
2. Utilizzo dei sotto-indicatori e dei cluster per l'analisi delle configurazioni organizzative dell'orientamento
3. Studio delle relazioni tra copertura documentale, monitoraggio e maturità dei sistemi orientativi scolastici

Dati estesi e tabelle analitiche sono riportati negli allegati tecnici.