# ORIENTA+ | Documentazione

URL: https://orienta.ai4educ.org/Documentazione
Data: 2026-05-13T17:25:14.878440

---

Navigazione

📘 PROGETTO

Progetto

Campionamento

▸ Documentazione

📊 ANALISI

KPI

Territorio

Dimensioni

Analisi Statistiche

Analytics

🌟 ESPLORAZIONE

Scuola

Attività

Report

Metodologie e Progetti

Impatto Metodologie e Progetti

🎓 SERVIZI

Invio

Verifica

Revisione

🛠️ ADMIN

Amministrazione

Login Admin

Password

Accedi

Flusso operativo

Questa parte descrive come il sistema mette in pratica l'analisi: dal recupero dei documenti alla gestione dei casi non pertinenti, fino alla registrazione delle attività svolte. È qui che la pipeline organizza il lavoro e garantisce continuità tra un ciclo di analisi e l'altro.

Panoramica del Sistema

Il workflow è progettato per essere ripetibile e trasparente. Prima si recuperano i PDF, poi si valida la natura del documento, quindi si trasforma il contenuto in testo leggibile (Markdown) e si avvia la pipeline multi‑agente. Ogni passaggio lascia traccia nei log e nei file di stato, in modo che la pipeline possa essere ripresa senza perdere coerenza.

La sequenza, in sintesi, è questa:

Download -> Validazione PTOF -> Markdown -> Analisi multi-agente -> JSON + Report -> Controlli -> CSV -> Dashboard

Ogni passaggio è pensato per ridurre errori, evitare duplicazioni e aumentare la qualità complessiva del risultato.

Raccolta documenti

Per trovare il PTOF, il sistema procede per gradi e non si ferma al primo tentativo. Si parte dal portale Unica, poi si consultano i siti istituzionali, si risale all'istituto di riferimento quando necessario e, se il documento non è ancora trovato, si effettua una ricerca mirata sul web. Questo approccio evita buchi di copertura soprattutto nei casi in cui il PTOF è pubblicato su piattaforme esterne.

Quando un file è già presente nel sistema, non viene riscaricato: la duplicazione introduce rumore e rallenta le analisi.

Validazione e gestione non-PTOF

Prima di qualsiasi analisi, il documento viene verificato. Il controllo serve a evitare che un regolamento, un curricolo o un verbale finisca per errore nel flusso dei PTOF. Si controllano titolo, indizi testuali e coerenza temporale (triennio). Se il documento non è un PTOF valido, viene scartato e archiviato separatamente.

La gestione dei documenti non‑PTOF è parte del processo principale: ciò che non supera la validazione viene spostato in cartelle dedicate e le analisi generate per errore vengono rimosse. In questo modo il dataset rimane pulito e affidabile.

Architettura Multi-Agente
Pipeline completa
PDF -> Validazione PTOF -> Markdown -> Analyst -> Reviewer -> Refiner -> JSON + Report
                                                         |
                                                         v
                                            Controlli finali -> CSV -> Dashboard
🔍 Analyst Agent

È il primo lettore: estrae dati, assegna punteggi e costruisce una bozza narrativa basata sulle evidenze presenti nel testo.

🧐 Reviewer Agent

È il controllo critico: verifica se il report cita elementi non presenti, corregge punteggi troppo alti o troppo bassi e segnala incoerenze.

✨ Refiner Agent

È l'editor finale: integra le correzioni, rende il testo più chiaro e assicura che il JSON e il report siano consistenti.

Metadati e Dataset

Dopo l'analisi, il sistema arricchisce i dati con anagrafiche ufficiali. Questo permette di standardizzare denominazioni, comune, area geografica e ordine di scuola. Quando disponibile, l'anagrafica include anche la gestione (statale/paritaria) come metadato descrittivo.

Il risultato è un dataset coerente che consente confronti affidabili tra territori e tipologie di istituto. L'arricchimento è cruciale per leggere correttamente i risultati su mappe e dashboard, evitando che differenze di formattazione generino errori.

Registro dell'Analisi

Ogni documento processato viene registrato in un registro di analisi che conserva lo stato dei passaggi già svolti. Questo registro evita doppie elaborazioni, consente di riprendere un lavoro interrotto e permette di sapere quali scuole sono state analizzate, revisionate o scartate.

Il registro è utile anche per le revisioni: quando un report viene riletto o corretto, lo stato viene aggiornato, così da mantenere una traccia coerente dell'intero ciclo di vita di un'analisi.

Manutenzione e Pulizia del Dataset

Alla fine dei cicli di estrazione, è fondamentale garantire l'integrità referenziale del dataset. Il sistema include uno strumento dedicato (make clean-ptof-codes) che esegue tre controlli incrociati:

Analisi Nome File vs Contenuto: Verifica che il codice meccanografico nel nome del file corrisponda a quello dichiarato all'interno del PTOF.
Rilevamento "Impostori": Identifica file scaricati correttamente ma appartenenti ad altre scuole (errore frequente nei siti web scolastici che pubblicano PTOF di reti o scuole aggregate).
Standardizzazione: Propone la rinomina dei file per mantenere la convenzione CODICE_PTOF.md e sposta in una cartella di "quarantena" i file non riconciliabili.

Questo processo assicura che ogni analisi statistica si basi su dati certi e correttamente attribuiti.

Revisori e Controllo Qualità

La qualità non dipende da un singolo controllo, ma da livelli successivi che entrano in gioco quando necessario. Il Reviewer Agent è parte integrante della pipeline: agisce subito dopo la prima bozza per correggere errori e incoerenze. A questo si aggiungono revisori dedicati che operano a valle del workflow principale.

La revisione del report (con OpenRouter, Gemini o Ollama) arricchisce il testo con dettagli mancanti, conferma la coerenza interna e rende la narrativa più precisa. La revisione dei punteggi estremi si concentra sulle valutazioni troppo alte o troppo basse, per evitare distorsioni.

La revisione Non‑PTOF agisce quando un documento non è pertinente, eliminando output errati. Infine, il Background Reviewer/Fixer controlla la coerenza tra punteggi, narrativa e metadati, applicando correzioni prudenti quando emergono anomalie.

Catalogo Attività

Il catalogo raccoglie pratiche concrete estratte dai PTOF e le rende esplorabili per categoria, territorio, tipo scuola, target e metodologie.

Funzioni principali:

Lista, vista raggruppata o tabellare con dettagli e citazioni.
Mappa di distribuzione geografica e dettaglio per regione.
Grafici di distribuzione (categoria, regione, tipo scuola).
Incroci categoria x dimensione con conteggi e percentuali.
Analisi statistiche con significativita ed effetto.
Export dei dati filtrati in JSON e CSV.
Legenda emoji (categorie)

Le emoji aiutano a riconoscere subito la categoria di una pratica.

📚 Metodologie Didattiche Innovative
🎯 Progetti e Attivita Esemplari
🤝 Partnership e Collaborazioni Strategiche
⚙️ Azioni di Sistema e Governance
🌈 Buone Pratiche per l'Inclusione
🗺️ Esperienze Territoriali Significative
File JSON del catalogo

I file JSON del catalogo sono la base dati su cui lavora la dashboard. Sono consultabili anche in forma tabellare:

Struttura pratica (tabellare)
Registro estrazione (tabellare)
Trasparenza: prompt e dati
Criteri catalogo buone pratiche

Il catalogo e costruito da estrazioni automatiche su testi PTOF. Le specifiche operative sono:

Categorie obbligatorie (6): Metodologie Didattiche Innovative, Progetti e Attivita Esemplari, Partnership e Collaborazioni Strategiche, Azioni di Sistema e Governance, Buone Pratiche per l'Inclusione, Esperienze Territoriali Significative.
Tipologie metodologia: elenco predefinito (es. STEM/STEAM, Flipped Classroom, PBL, Cooperative Learning, ecc.).
Ambiti di attivita: elenco predefinito (es. Orientamento, Inclusione, PCTO, Cittadinanza, ecc.).
Criterio di selezione: solo pratiche concrete e specifiche con evidenza testuale nel PTOF; sono escluse formulazioni generiche.
Limite estrazione: massimo 5 pratiche per chunk di testo.
Campi richiesti per pratica: titolo, descrizione, metodologia, target, categoria, tipologie_metodologia, ambiti_attivita, citazione_ptof, pagina_evidenza (se presente), partnership_coinvolte (solo per categoria partnership).

Prompt - Codice

Prompt - Tabella

Prompt base (config/prompts.md)

keyboard_arrow_right

Analyst

keyboard_arrow_right

AnalystChunk

keyboard_arrow_right

Reviewer

keyboard_arrow_right

Refiner

keyboard_arrow_right

Narrative

keyboard_arrow_right

Validator PTOF 2022-2025

keyboard_arrow_right

Validator Documentale

keyboard_arrow_right

Metadata Extractor

keyboard_arrow_right

Background Reviewer

keyboard_arrow_right

Background Fixer

keyboard_arrow_right

Review report (OpenRouter/Gemini) - prompt

keyboard_arrow_right

Review report Ollama - prompt chunk

keyboard_arrow_right

Review report Ollama - prompt finale

keyboard_arrow_right

Review punteggi estremi (OpenRouter/Gemini/Ollama) - prompt

keyboard_arrow_right

Estrazione buone pratiche - prompt

JSON - Codice

JSON - Tabella

Analisi PTOF - output JSON

{
  "metadata": {
    "school_id": "MIIS08900V",
    "denominazione": "...",
    "ordine_grado": "I Grado|II Grado",
    "tipo_scuola": "Liceo|Tecnico|Professionale|I Grado",
    "statale_paritaria": "Statale|Paritaria",
    "area_geografica": "Nord Ovest|Nord Est|Centro|Sud|Isole"
  },
  "ptof_section2": {
    "2_1_ptof_orientamento_sezione_dedicata": {
      "has_sezione_dedicata": 0,
      "score": 1,
      "note": "..."
    },
    "2_2_partnership": {
      "partner_nominati": ["..."],
      "partnership_count": 0
    },
    "2_3_finalita": {
      "finalita_attitudini": { "score": 1 },
      "finalita_interessi": { "score": 1 },
      "finalita_progetto_vita": { "score": 1 }
    }
  },
  "narrative": "Report markdown..."
}

Review punteggi estremi - output JSON

{
  "score_updates": [
    {
      "path": "ptof_section2.2_1_ptof_orientamento_sezione_dedicata.score",
      "old_score": 2,
      "new_score": 3,
      "action": "modify",
      "reason": "Spiega in breve."
    }
  ],
  "review_notes": "Nota generale opzionale."
}

Review report Ollama - output JSON (chunk)

{
  "enrichments": [
    {
      "section": "sezione report da arricchire",
      "addition": "testo narrativo da aggiungere",
      "source_quote": "citazione breve dal PTOF"
    }
  ],
  "orientamento_section_found": true,
  "orientamento_details": "descrizione sezione orientamento",
  "corrections": [
    {
      "issue": "cosa va corretto",
      "reason": "perche"
    }
  ]
}

Catalogo attività - output prompt

{
  "pratiche": [
    {
      "categoria": "Nome Categoria Esatto",
      "titolo": "Nome Specifico Pratica",
      "descrizione": "Descrizione dettagliata...",
      "metodologia_desc": "Come viene implementata...",
      "tipologie_metodologia": ["STEM/STEAM", "Didattica Laboratoriale"],
      "ambiti_attivita": ["Orientamento", "Digitalizzazione"],
      "target": "A chi e rivolta",
      "citazione_ptof": "Citazione dal documento...",
      "pagina_evidenza": "Pagina X",
      "partnership_coinvolte": []
    }
  ]
}

Catalogo attività - dataset (data/attivita.json)

{
  "version": "1.0",
  "last_updated": "2025-01-01T12:00:00",
  "extraction_model": "qwen3:32b",
  "schools_processed": 120,
  "total_practices": 560,
  "practices": [
    {
      "id": "uuid",
      "school": {
        "codice_meccanografico": "RMIS02400L",
        "nome": "Istituto ...",
        "tipo_scuola": "Liceo Scientifico",
        "ordine_grado": "Secondaria II Grado",
        "regione": "Lazio",
        "provincia": "Roma",
        "comune": "Roma",
        "area_geografica": "Centro",
        "territorio": "Metropolitano",
        "statale_paritaria": "Statale"
      },
      "pratica": {
        "categoria": "Metodologie Didattiche Innovative",
        "titolo": "Laboratorio di Robotica Educativa",
        "descrizione": "...",
        "metodologia": "...",
        "tipologie_metodologia": ["STEM/STEAM"],
        "ambiti_attivita": ["Orientamento"],
        "target": "Studenti",
        "citazione_ptof": "...",
        "pagina_evidenza": "Pagina 12"
      },
      "contesto": {
        "maturity_index": 4.6,
        "punteggi_dimensionali": {},
        "partnership_coinvolte": [],
        "attivita_correlate": []
      },
      "metadata": {}
    }
  ]
}

Catalogo attività - registry (data/activity_registry.json)

{
  "version": "1.0",
  "last_updated": "2025-01-01T12:00:00",
  "processed_files": {
    "RMIS02400L": {
      "file_hash": "sha256:...",
      "processed_at": "2025-01-01T12:00:00",
      "practices_count": 12,
      "model_used": "qwen3:32b"
    }
  }
}

Anagrafica comuni (data/comuni_italiani.json)

[
  {
    "nome": "Abano Terme",
    "codice": "028001",
    "zona": { "codice": "2", "nome": "Nord-est" },
    "regione": { "codice": "05", "nome": "Veneto" },
    "provincia": { "codice": "028", "nome": "Padova" },
    "sigla": "PD",
    "codiceCatastale": "A001",
    "cap": "35031",
    "popolazione": 0
  }
]
Avvertenze e Buone Pratiche

Attenzione: i punteggi sono generati da modelli di intelligenza artificiale e possono contenere errori.

Limitazioni note

La qualità dipende dai documenti di partenza. PDF scannerizzati, impaginazioni complesse o testo poco chiaro possono ridurre la precisione. Inoltre, modelli diversi possono produrre valutazioni leggermente differenti. Per questo i risultati vanno letti come indicatori comparativi e non come giudizi assoluti.

Buone pratiche
usare i punteggi per confrontare, non per etichettare
leggere sempre il report narrativo insieme ai numeri
considerare il contesto specifico della scuola
Documenti e Fonti

La base documentale è composta dai PTOF originali, dalle versioni in Markdown utilizzate per l'analisi e dai dataset di sintesi. Queste fonti consentono sia la lettura qualitativa sia la comparazione quantitativa tra scuole.

🛡️ Criteri di Esclusione e Qualità del Dato

Per garantire l'affidabilità delle analisi, il sistema applica criteri rigorosi di esclusione:

Validazione PTOF: I documenti che non superano i controlli euristici (es. numero pagine, parole chiave) vengono scartati prima dell'analisi.
Soglia Minima di Rilevanza (Score ≤ 2.0): Qualsiasi analisi che produca un IIPO (Indice di informatività delle pratiche di orientamento) inferiore o uguale a 2.0 viene automaticamente scartata ed eliminata. Un punteggio così basso indica con quasi assoluta certezza che il documento non è un PTOF valido o non contiene alcuna informazione pertinente sull'orientamento, rendendo l'analisi priva di valore.
Fonte	Descrizione	Utilizzo
metadata_enrichment.csv	Anagrafica MIUR	Denominazione, Comune, Tipo scuola
PTOF Documents	Documenti scolastici	Analisi testuale
keyboard_arrow_right

Riferimenti Normativi

🧭 ORIENTA+
Piattaforma di Analisi della Robustezza dell'Orientamento nei PTOF • Sviluppato da Daniele Dragoni — Dottorando, Università Roma Tre • 📧 daniele.dragoni@uniroma3.it
Quest'opera è distribuita con Licenza Creative Commons Attribuzione - Non commerciale - Non opere derivate 4.0 Internazionale • ORIENTA+ è un marchio registrato.