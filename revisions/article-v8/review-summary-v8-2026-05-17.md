# Review summary — article-v8 — 2026-05-17

Articolo revisionato: `articles/article-v8-2026-05-17-1107.md`

## Modalità

Revisione paragrafo per paragrafo (`/r-pp`), con interventi approvati progressivamente dall'utente tramite workflow A/R/M.

## Versioning

- Versione di partenza: `articles/article-v7-2026-05-15-2008.md`
- Bump obbligatorio di sessione: `articles/article-v8-2026-05-17-1107.md`
- Diff iniziale: `revisions/article-v8/diff-v7-to-v8.md`

## Interventi principali effettuati

### Introduzione

- Chiarita la doppia difficoltà affrontata da ORIENTA+: reperimento dei PTOF e analisi sistematica di documenti numerosi ed estesi.
- Spostata la frase di transizione su ORIENTA+ dal paragrafo sul problema al paragrafo successivo, rendendo ORIENTA+ la risposta diretta alla difficoltà descritta.
- Eliminato un paragrafo conclusivo dell'introduzione ritenuto ridondante.

### Obiettivi della ricerca

- Riscritta la formulazione dei tre obiettivi in forma più lineare.
- Eliminato il paragrafo sulle sei dimensioni perché anticipava contenuti poi spiegati nella metodologia.
- Alleggerita la frase sul catalogo delle attività, eliminando la formula ridondante “rese consultabili”.

### Metodo — campionamento e strumenti

- Inserito un paragrafo autonomo sugli strumenti computazionali utilizzati, collocato subito dopo `## 3. Metodo` e non dentro `§3.1 Campionamento`.
- Corretta la descrizione dell'hardware: workstation locale con GPU NVIDIA GeForce RTX 5090, circa 32 GB di memoria video e 125 GiB di RAM di sistema.
- Precisato che le variabili di stratificazione erano presenti nel CSV open data MIM o deducibili con precisione da esso.
- Chiarita la catena numerica: 9.984 file candidati, 5.399 download riusciti, fase di verifica/raffinamento, 2.095 PTOF finali.
- Esplicitata la fase di verifica dei documenti: esclusione dei file sotto soglia e identificazione dei file “impostori”.
- Definito il concetto di “agente” come modulo basato su LLM configurato per un compito delimitato.

### Metodo — framework e pipeline

- Chiarita la dimensione “Obiettivi di Incidenza”, spiegando che rileva il collegamento tra orientamento ed esiti attesi come contrasto alla dispersione, riduzione NEET e lifelong learning.
- Precisato che i giudizi Likert valutano il grado di documentazione nel PTOF, non direttamente la qualità delle pratiche realizzate.
- Aggiunta la soglia di esclusione dei documenti con punteggio inferiore a 2, considerati non riconducibili a PTOF.
- Spiegato cos'è Markdown e perché viene usato nella pipeline.
- Corretti i modelli LLM usati nella pipeline locale: `Gemma 3 27B` e `Qwen3:32B`.
- Spiegato cos'è JSON e perché viene usato per rendere aggregabili e confrontabili gli output.
- Sostituito “modulo dedicato” con “altro agente della pipeline” per coerenza terminologica.

### Metodo — elaborazione, report e modelli proprietari

- Spostata la dashboard fuori dalla metodologia e collocata all'inizio dei risultati.
- Chiarita la distinzione tra:
  - analisi dei singoli PTOF con modelli locali;
  - produzione di report sintetici e analisi aggregate con modelli proprietari.
- Reintrodotti `Gemini 3 Pro`, `GLM-5` e `MiniMax M2.5` solo come modelli usati nella fase di sintesi/redazione dei report.
- Spiegata la generazione dei report in tre passaggi: scheletro statistico deterministico, compilazione narrativa tramite LLM con evidenze RAG, revisione automatica di coerenza.
- Rivisti i titoli delle sottosezioni metodologiche:
  - `3.3 Pipeline multi-agente e output strutturati`
  - `3.4 Elaborazione aggregata, cluster e report sintetici`
  - `3.5 Validazione della piattaforma`

### Risultati

- Inserito all'inizio di `§4. Risultati` il riferimento alla dashboard ORIENTA+:
  - https://orienta.ai4educ.org/
- Corretta la coerenza interna del riferimento alla validazione: `cfr. §3.6` → `cfr. §3.5`.

### Discussione

- Aggiunta nei limiti metodologici una frase sulla diversa reperibilità/scaricabilità dei PTOF, per spiegare che la sproporzione del campione dipende anche dalla disponibilità effettiva dei documenti.

## Controlli finali effettuati

- Verificata la numerazione delle sezioni.
- Verificati i riferimenti interni principali.
- Verificata la coerenza dei modelli LLM citati:
  - pipeline locale: `Gemma 3 27B`, `Qwen3:32B`;
  - reportistica sintetica: `Gemini 3 Pro`, `GLM-5`, `MiniMax M2.5`.
- Conteggio finale rilevato: `37.936` caratteri, `5.305` parole.

## Stato finale

- La review della sessione è conclusa.
- Restano modifiche non committate.
- Nessun commit è stato eseguito.
- L'articolo resta sopra il limite editoriale di 30.000 caratteri di circa 7.936 caratteri.

## Prossimo passo consigliato

Eseguire una passata separata di riduzione della lunghezza, con obiettivo di tagliare circa 8.000 caratteri senza perdere i contenuti metodologici essenziali.
