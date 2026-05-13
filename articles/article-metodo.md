# Metodo

## 1. Campionamento

La costruzione del campione è avvenuta attraverso un procedimento di campionamento stratificato multi-stadio. Ogni scuola italiana è stata classificata in uno strato definito da quattro dimensioni: gestione (statale o paritaria), area geografica (Nord Ovest, Nord Est, Centro, Sud, Isole), territorio (metropolitano o non metropolitano) e ordine di scuola (Infanzia, Primaria, Secondaria di Primo Grado, Secondaria di Secondo Grado, Altro). La combinazione di queste variabili genera cento strati potenziali.

L'estrazione è stata proporzionale alla numerosità di ciascuno strato: `n_strato = (N_strato / N_totale) × n_target`. In settantotto cicli di estrazione condotti tra il 5 gennaio e il 13 febbraio 2026, sono state selezionate 15.035 scuole. Di queste, 3.082 hanno prodotto un PTOF scaricabile e convertibile, con una resa globale del 54,1%. La fase di pulizia finale ha rimosso circa trecento entry non valide, tra codici scuola errati e documenti «impostori» — file il cui contenuto non corrispondeva al codice scuola associato.

Il campione finale copre diciotto regioni su venti e cento province su centosette per il Secondo Grado.

## 2. Framework di valutazione

La valutazione si articola su sei dimensioni, ciascuna misurata su una scala Likert da 1 a 7:

1. **Strutturale e di Contesto** — presenza di una sezione dedicata all'orientamento e partnership territoriali.
2. **Finalità dell'Orientamento** — esplicitazione degli scopi formativi: attitudini, interessi professionali, progetto di vita, transizioni, empowerment.
3. **Obiettivi di Incidenza** — impatto atteso su dispersione scolastica, riduzione NEET, continuità territoriale, lifelong learning.
4. **Governance e Organizzazione** — modello organizzativo: coordinamento, dialogo interno, alleanza con le famiglie, monitoraggio, inclusione.
5. **Didattica Orientativa** — metodologie didattiche: laboratoriale, centralità dello studente, interdisciplinarità, flessibilità.
6. **Opportunità Formative** — offerta extracurricolare: attività culturali, sportive, volontariato, ricreative.

La scala Likert adottata distingue sette livelli: da «assente» (nessun riferimento) a «eccellente» (documentazione sistematica e ciclica con evidenze di miglioramento), passando per «generico», «limitato», «sufficiente», «buono» e «ottimo».

L'Indice di Documentazione delle Pratiche di Orientamento (IIPO) è calcolato come media aritmetica semplice dei punteggi delle sei dimensioni:

IIPO = (S + F + O + G + D + Op) / 6

I valori sono aggregati in cinque fasce interpretative: accenni minimi (1,1–2,2), riferimenti generici (2,3–3,4), azioni basilari (3,5–4,6), sistema strutturato (4,7–5,8), sistema eccellente (5,9–7,0). I punteggi inferiori o uguali a 2,0 sono automaticamente scartati in quanto indicatori di documento non valido o assenza di contenuti orientativi rilevanti.

Un'avvertenza metodologica: la media aritmetica può mascherare squilibri tra dimensioni. Un punteggio alto in Didattica e basso in Governance produce un indice medio che non riflette la reale distribuzione delle carenze. Per questo l'IIPO va sempre letto insieme ai punteggi dimensionali che lo compongono.

## 3. Pipeline multi-agente

L'analisi di ciascun PTOF segue una pipeline a tre agenti: Analyst → Reviewer → Refiner.

Il primo agente, Analyst, estrae i punteggi per ogni dimensione e produce una bozza narrativa basata sulle evidenze testuali del documento. Il Reviewer verifica le citazioni, corregge sovra o sottostime e segnala incoerenze. Il Refiner integra le correzioni e garantisce la coerenza tra punteggi JSON e report narrativo. Un agente supplementare, Background Reviewer, convalida la coerenza trasversale tra punteggi, narrazione e metadati.

La pipeline supporta molteplici modelli linguistici attraverso OpenRouter, Gemini e Ollama — tra cui Gemini 3 Pro, GLM-5, MiniMax M2.5 e Qwen3 — consentendo il confronto tra architetture e fornitori diversi.

A valle della pipeline, ogni PTOF produce un output JSON con metadati della scuola, punteggi dimensionali e di dettaglio, e un report in Markdown con la narrazione delle evidenze. Da questi dati è popolata una dashboard interattiva che offre viste per indici sintetici, analisi territoriale, dimensionale, avanzata (clustering, PCA, correlazioni) e d'impatto.

## 4. Controlli di qualità

La qualità del dato è presidiata da più livelli. Il Reviewer è integrato nella pipeline e interviene immediatamente dopo la prima stesura. Una revisione dei punteggi estremi — sovra e sottostime — è eseguita tramite LLM. I documenti che superano le soglie di validazione ma contengono contenuti non pertinenti sono intercettati da una revisione dedicata («non-PTOF review»). Il Background Reviewer opera una verifica di coerenza trasversale tra punteggi, narrazione e metadati, applicando correzioni conservative sulle anomalie.

La generazione dei report di sintesi segue una strategia a tre fasi: costruzione dello scheletro statistico (calcolo degli aggregati, produzione delle visualizzazioni, preparazione dei placeholder, senza coinvolgimento LLM), compilazione narrativa (l'LLM riceve istruzioni di ruolo, contesto normativo, sintesi dell'analisi cluster e evidenze RAG, e produce la narrazione) e revisione di coerenza (un passaggio automatico per individuare ripetizioni, incongruenze numeriche, errori di scala e contaminazioni cross-grado).

## 5. Elaborazione dei dati

I 3.082 PTOF raccolti sono stati convertiti da PDF a Markdown e processati dalla pipeline multi-agente. Per ciascuna scuola, l'analisi ha prodotto i punteggi delle sei dimensioni e l'IIPO. I dati aggregati sono stati successivamente sottoposti ad analisi cluster per identificare profili omogenei di documentazione dell'orientamento.

Il catalogo delle attività di orientamento — metodologie didattiche innovative, progetti esemplari, partnership, azioni di sistema, buone pratiche per l'inclusione, esperienze territoriali — è stato estratto separatamente utilizzando Qwen3:32b, con un limite di cinque pratiche per blocco testuale e un campione di centoventi scuole processate per un totale di cinquecentosessanta attività catalogate.
