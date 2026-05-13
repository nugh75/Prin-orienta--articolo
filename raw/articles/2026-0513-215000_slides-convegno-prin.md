---
title: "Slides convegno PRIN - Analisi dei PTOF"
authors: [Daniele Dragoni, Maria Chiara De Nardo]
event: "Convegno conclusivo PRIN 2022"
date: 2026-02-26
location: "Aula Volpi, Roma"
source: Slides_PTOF_logoRomaTre[63].pdf
---

## Contesto

Un'analisi sistematica per mappare lo stato dell'orientamento nella scuola secondaria. La doppia lettura:

- **Umana**: Analisi qualitativa profonda — 16 PTOF (II grado, campione stratificato)
- **AI (ORIENTA+)**: Analisi automatizzata (LLM) — ∼2.000 PTOF (estratti su tutti i gradi, focus su I e II grado)

**Obiettivo centrale**: Valutare la coerenza con il D.M. 328/2022 e la qualità effettiva delle pratiche di orientamento formativo nel vivo dell'autonomia scolastica.

## Campionamento

### Analisi AI
- Stratificazione derivata da incroci di variabili (gestione, geografia, territorio, ordine, criteri)
- Algoritmo Python per estrazione proporzionale casuale dalla popolazione nazionale
- Riferimento: metodologia del questionario nazionale

### Analisi umana
- Selezione mirata di 16 scuole di II grado per l'analisi in profondità
- Sub-estrazione rigorosa dal bacino precedentemente analizzato dall'AI
- Criteri: gestione (statale/paritaria), geografia (NO, NE, C, S, isole), territorio (metro/non metro), ordine (inf, prim, I, II, altro)

### Allineamento metodologico
- Coerenza con il questionario nazionale
- Sinergia dei dati: rende possibile la triangolazione tra quanto dichiarato nei PTOF e le rilevazioni nazionali
- Linguaggio condiviso: costrutti e indicatori coerenti con la cornice di riferimento del questionario nazionale

## Fasi operative

Per ogni scuola selezionata, il sistema esegue una sequenza automatizzata e ripetibile:

1. Ricerca URL: portale Unica → sito istituzionale → istituto di riferimento → ricerca web
2. Download automatico del PDF (no duplicazioni)
3. Validazione: verifica che il documento sia effettivamente un PTOF (titolo, indizi testuali, triennio)
4. Conversione in markdown per l'analisi testuale
5. Analisi AI multi-agente → JSON + report → DB → Dashboard
6. Pulizia post-estrazione: riconciliazione codici meccanografici, rimozione "impostori", eliminazione file orfani
7. Registro dell'analisi (evita doppie elaborazioni), arricchimento metadati da anagrafiche ufficiali

## Numeri chiave

- **78** cicli completati
- **15.035** scuole selezionate
- **2.095** PTOF scaricati e analizzati
- Dopo pulizia: **693 PTOF II Grado** + **246 PTOF I Grado** validati e analizzati

### Cause di fallimento
- PTOF non pubblicato online
- URL non raggiungibile
- Documento non-PTOF (regolamenti, curricoli, verbali)
- Codice meccanografico non corrispondente

## Pipeline multi-agente

Tre agenti LLM specializzati operano in sequenza su ogni PTOF:

1. **Analyst agent**: Primo lettore — estrae dati, assegna punteggi sulle 6 dimensioni, costruisce bozza narrativa basata sulle evidenze
2. **Reviewer agent**: Controllo critico — verifica citazioni, corregge punteggi troppo alti/bassi, segnala incoerenze
3. **Refiner agent**: Editor finale — integra correzioni, assicura consistenza tra JSON, report e punteggi

### Revisioni aggiuntive a valle
- Revisione punteggi estremi (troppo alti o bassi)
- Background reviewer: coerenza punteggi-narrativa-metadati
- Revisione non-PTOF: eliminazione output errati

## Catalogo attività e output

Le pratiche concrete estratte dai PTOF sono raccolte in un catalogo esplorabile.

### Funzionalità
- Vista per categoria, territorio, tipo scuola
- Mappa distribuzione geografica
- Grafici di distribuzione
- Incroci categoria × dimensione
- Analisi statistiche con significatività
- Export JSON e DB

### Categorie di pratiche
- Metodologie didattiche innovative
- Progetti e attività esemplari
- Partnership e collaborazioni
- Azioni di sistema e governance
- Buone pratiche per l'inclusione
- Esperienze territoriali

## ORIENTA+: metodo e campione

Sistema ORIENTA+ – Analisi automatizzata con LLM (Gemini 3 Pro, Gemma3:27b, Qwen3-Coder:30B)

### Metodo
- Analisi strutturale (compliance D.M. 328/2022) + analisi semantica
- 6 dimensioni valutate su scala 1–7: Strutturale, Finalità, Obiettivi, Governance, Didattica, Opportunità
- IIPO (Indice Informativo delle Pratiche di Orientamento): media delle 6 dimensioni
- Clustering in 5 profili omogenei per grado scolastico

### Campione
- **II Grado**: 693 PTOF, 100 province, 18/20 regioni — IIPO medio: 3.48 / 7
- **I Grado**: 246 PTOF, 84 province, 18/20 regioni — IIPO medio: 3.44 / 7

## Punteggi medi per dimensione

### II Grado
- **Strutturale (Compliance)**: 2.62
- **Finalità**: 3.68
- **Obiettivi**: 3.21
- **Governance**: 3.66 (Coord. Servizi: 3.66, Dialogo Doc-Stud: 3.67, Scuola-Genitori: 3.95, Monitoraggio: 3.06, Incl. Fragilità: 3.90)
- **Didattica**: 3.65 (Attitudini: 3.74, Esper. Studenti: 3.97, Interessi: 3.73, Laboratoriale: 3.34, Prog. di Vita: 3.53, Flessib. Spazi: 3.43, Transizioni: 3.82, Interdisciplinare: 3.81, Cap. Orientative: 3.51)
- **Opportunità**: 3.18 (Culturali: 3.23, Rid. Abbandono: 3.13, Lab. Espressive: 3.81, Cont. Territorio: 3.76, Ludico-Ricreative: 2.73, Contrastare NEET: 2.41, Volontariato: 2.76, Lifelong Learn.: 3.30, Sportive: 3.20)

### I Grado
- **Strutturale (Compliance)**: 2.39
- **Finalità**: 3.50
- **Obiettivi**: 2.91
- **Governance**: 3.57 (Coord. Servizi: 3.50, Dialogo Doc-Stud: 3.57, Scuola-Genitori: 4.05, Monitoraggio: 2.79, Incl. Fragilità: 3.92)
- **Didattica**: 3.60 (Attitudini: 3.65, Esper. Studenti: 3.85, Interessi: 3.67, Laboratoriale: 3.52, Prog. di Vita: 3.38, Flessib. Spazi: 3.32, Transizioni: 3.56, Interdisciplinare: 3.72, Cap. Orientative: 3.24)
- **Opportunità**: 3.01 (Culturali: 3.09, Rid. Abbandono: 2.80, Lab. Espressive: 3.83, Cont. Territorio: 3.55, Ludico-Ricreative: 2.63, Contrastare NEET: 2.04, Volontariato: 2.45, Lifelong Learn.: 3.26, Sportive: 3.07)

### Scala di riferimento
- 5–7: Ampiamente documentato
- 3.5–5: Parzialmente documentato
- <3.5: Poco documentato

## Cluster

### Cluster II Grado
- **Cluster 0** – Approccio integrato e didattico (112 scuole): Orientamento diluito nella didattica quotidiana
- **Cluster 1** – Approccio relazionale e di accoglienza (77 scuole): Focus su benessere e clima scolastico; orientamento in uscita da potenziare
- **Cluster 2** – Approccio PCTO-centrico dichiarativo (25 scuole): Orientamento spesso ricondotto ai PCTO, con descrizioni operative non sempre approfondite
- **Cluster 3** – Approccio frammentato (50 scuole): Azioni puntiformi, con spazi di maggiore integrazione
- **Cluster 4** – Progettualità diffusa (407 scuole): Molti progetti ma senza cornice unitaria; STEM ricorrenti, ma pochi laboratori

### Cluster I Grado
- **Cluster 0** – Approccio integrato e curricolare (67 scuole): Orientamento diffuso nel curricolo; attenzione alla transizione in uscita
- **Cluster 1** – Focalizzato su benessere e accoglienza (21 scuole): Supporto psico-fisico; interventi prevalentemente reattivi; orientamento in uscita da sviluppare
- **Cluster 2** – Approccio dichiarativo formale (12 scuole): Citazione normativa con limitata declinazione operativa
- **Cluster 3** – Generalista e non strutturato (19 scuole): Orientamento diluito e residuale; episodico
- **Cluster 4** – Progettuale frammentato (125 scuole): Ricchezza di iniziative; governance in via di consolidamento; logica "a progetto"

## Lettura umana

### Campione e metodo
- 16 PTOF di scuole secondarie di II grado
- Tipologie: licei, istituti tecnici e professionali, statali e paritarie
- Contesti: metropolitani e non metropolitani
- Copertura territoriale nazionale
- Criteri: aggiornamento normativo, struttura dell'orientamento, rapporto con il territorio, metodologie, formazione docenti, monitoraggio

### Punti di forza
- Aggiornamento normativo: PTOF generalmente allineati al D.M. 328/2022, D.M. 934/2022, D.M. 233/2024
- Orientamento come processo: superamento della concezione episodica degli anni '80 verso un modello integrato e relazionale
- Figure professionali: recepimento dei ruoli di docente tutor e docente orientatore
- Rapporto con il territorio: convenzioni con enti locali, università, ITS, associazioni, terzo settore
- Metodologie variegate: approcci narrativi, cooperative learning, didattica per competenze, flipped classroom
- Strumenti: e-portfolio, colloqui di counseling, mentoring, coaching
- Attenzione al benessere: sportelli psicologici, mentoring e tutoraggio personalizzati per prevenzione dispersione e inclusione

### Lacune ricorrenti e criticità
- Impostazione teorica poco esplicitata: i riferimenti alle teorie orientative sono poco documentati; prevale il "fare" sulla riflessione
- Mancanza di team dedicati per inclusione e orientamento
- Sezione autonoma non sempre presente: in alcuni PTOF l'orientamento non è ancora strutturato in una sezione autonoma, ma disperso in riferimenti frammentari, spesso legati ai soli PCTO
- Formazione specifica poco documentata: in alcuni PTOF mancano indicazioni puntuali su ruoli e numeri dei docenti tutor e orientatori
- Monitoraggio da rafforzare: valutazione d'impatto poco documentata
- Piattaforme digitali avanzate e AI: scarsa presenza nei PTOF come strumenti per l'orientamento (eccetto UNICA) — Solo 82 attività su 17.187 censite

### Sintesi
- I PTOF mostrano una rielaborazione autonoma delle normative, non limitata a riproduzione formale
- Persistono differenze significative tra scuole con sistemi maturi e scuole dove l'orientamento resta implicito
- **Debolezza di fondo**: carenza sul piano teorico e sistemico — le azioni appaiono frammentarie più che frutto di una visione pedagogica condivisa

## Convergenze tra lettura umana e AI

**Diagnosi condivisa**: L'orientamento formativo è citato e riconosciuto, ma è ancora tradotto solo in parte in pratiche curricolari sistematiche.

- **Frammentazione**: molte iniziative, ma cornice unitaria non sempre esplicita
- **Monitoraggio**: valutazione dell'impatto poco documentata o poco strutturata
- **Prevalenza della logica di progetto**: rischio di orientamento episodico
- **Eterogeneità tra scuole**: coesistono pratiche mature e assetti ancora impliciti
- **AI nelle scuole**: tema presente in alcune iniziative, ma raramente documentato come asse orientativo sistematico

## Differenze di lettura

Non emergono contraddizioni nette: cambiano soprattutto scala e tipo di evidenza.

- **Analisi umana (profondità)**: legge pochi PTOF in dettaglio e valuta meglio coerenza pedagogica, qualità della scrittura e visione educativa
- **AI (ampiezza)**: legge molti PTOF e rende più visibili ricorrenze, frequenze, profili cluster e differenze tra gradi/territori
- **Temi specifici**: la lettura umana può individuare snodi rilevanti; l'AI permette di tradurli in numeri su larga scala (es. solo 82 attività su 17.187 censite riguardano tecnologie digitali/AI)
- **Cornice teorica e criteri di lettura**: la costruzione della pipeline (dimensioni, indicatori, prompt, criteri interpretativi e riferimenti teorici) è un lavoro umano e non può essere rimandato all'AI

## Sintesi e prospettive

### Il quadro emerso
- Sistema in transizione: consapevole delle nuove istanze normative
- ∼2.000 PTOF analizzati confermano un IIPO medio di ∼3.5/7
- Il cluster più numeroso (60% II Grado, 51% I Grado) è caratterizzato da progettualità diffusa ma frammentata
- La lettura umana conferma rielaborazione autonoma delle norme, ma debolezza teorico-sistemica

### La sfida
Passare dall'orientamento come evento all'orientamento come dimensione permanente del curricolo, integrando monitoraggio, formazione docente e strumenti riflessivi.