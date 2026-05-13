# Action Log

## [2026-05-13] Ingest | Piattaforma ORIENTA+ (Daniele Dragoni, Roma Tre)

Ingeeriti articoli dalla piattaforma https://orienta.ai4educ.org/:

- **Progetto**: descrizione del framework a 6 dimensioni, IIPO, metriche
- **Campionamento**: metodologia stratificata multi-stage, 78 cicli, 15.035 scuole
- **Documentazione**: pipeline multi-agente (Analyst → Reviewer → Refiner), JSON schemas
- **Report**: 18 report di sintesi (11 MD + 7 PDF) su I Grado e II Grado

Create wiki pages:
- Entity: [[ORIENTA+]], [[Daniele Dragoni]], [[Università Roma Tre]]
- Concept: [[IIPO]], [[Framework di Valutazione a 6 Dimensioni]], [[Pipeline Multi-Agente]], [[Campionamento Stratificato (scuole italiane)]], [[Report di Sintesi ORIENTA+]]
- Comparison: [[Confronto I Grado vs II Grado — Orientamento nei PTOF]]

## [2026-05-13] Bump v1→v2 | Ristrutturazione articolo in capitolo unico

- Rinominato in `article-v2-2026-05-13-2005.md`
- Aggiunto titolo: «Orientamento scolastico e intelligenza artificiale: la piattaforma ORIENTA+ per il monitoraggio delle pratiche nei PTOF»
- Aggiunti abstract IT/EN e keywords
- Sostituita struttura multi-capitolo (`# Capitolo N` + `## Titolo`) con capitolo unico (`# Titolo` + `## N. Titolo`)
- Adeguata numerazione paragrafi alle norme Roma TrE-PRESS
- Taglio testo: da 33.023 a 29.850 battute (limite 30.000)
- Aggiornato `scripts/docx_renderer.py` per nuovo formato
- Documento DOCX rigenerato: `articolo-orienta-plus.docx`

## [2026-05-13] Revisione introduzione (tone-of-voice)

Rivista l'Introduzione (§1) applicando le regole tone-of-voice:
- **Omissione** del riferimento all'autore (Daniele Dragoni)
- **Precisione**: «oltre 60.000» scuole dall'anagrafe MIM, non numero generico
- **Sfida ingegneristica**: problema inquadrato come scaling prima che metodologico
- **Frasi brevi**: periodo sul D.M. 328/2022 spezzato in tre frasi
- **Hook**: transizioni rafforzate tra paragrafi
- **Metacognitive signpost**: «Il presente contributo illustra...»
- **Linearità**: 939 PTOF (coerente con §4.1), non «oltre tremila»
- Tagli compensativi in §5.4 e §5.5 per rientro nel limite 30.000 battute
- Transizione ammorbidita: «Il problema è quantitativo» → «La difficoltà è innanzitutto quantitativa:»
- Rivista introduzione (skill article-revision): 3 punti (gancio, «sfida proibitiva», *Abstract.*)
- §1: aggiunto iter normativo (CM 43/2009, Nota 4232/2014, D.M. 328/2022), definizione allineata al PNRR
- §3.2: sei dimensioni in prosa invece di elenco numerato (compensazione −232 netto) — 29.768 battute

## [2026-05-13] Ingest | Slides convegno conclusivo PRIN

- Acquisito PDF `Slides_PTOF_logoRomaTre[63].pdf` → convertito in `2026-0513-215000_slides-convegno-prin.md`
- Autori: [[Daniele Dragoni]] + [[Maria Chiara De Nardo]]
- Contenuto: doppia lettura AI/umana, pipeline multi-agente, risultati cluster, convergenze e differenze di metodo
- Dato chiave: solo 82 attività su 17.187 censite riguardano tecnologie digitali/AI (già in articolo §4)

## [2026-05-13] Health-check wiki

- Articolo: 29.961 battute (sotto limite 30.000) ✓
- Rimosse 136 battute superflue da §4.4
- Wiki: 11 pagine, 26 wikilinks interni, nessun orphan ✓
- Cross-references verificati ✓
- Aggiunta entity [[Maria Chiara De Nardo]] ✓
- Aggiornati index.md e log.md ✓

## [2026-05-13] Ingest | Catena dei numeri ORIENTA+ (da repository progetto)

- Creato `raw/articles/2026-0513-220000_catena-numeri-orienta.md` con dati da `/home/nugh75/LIste/`
- Fonti verificate: anagrafe MIM (61.856 plessi), `strata_cycle_state.json` (5.399 download, 54,1% resa), `ptof_cleaner.log` (2.584 → 2.095), `analysis_summary.csv` (939 secondaria)
- Corretto `campionamento-stratificato.md`: ora riporta la catena completa (9.984 tentativi → 5.399 download → 3.082 unici → 2.584 in pulizia → 2.095 base analitica → 939 secondaria)
- Articolo §3.1 aggiornato con la nuova catena (29.951 battute)

## [2026-05-13] Ingest | Documentazione completa piattaforma ORIENTA+

- Acquisito file `raw/articles/2026-0513-210000_orienta-piattaforma-completa.md` — documentazione integrale da orienta.ai4educ.org (framework, metriche Likert, strumenti di analisi, catalogo attività, analytics avanzati)
- Acquisito file `raw/articles/2026-0513-213000_prin-avanzamento-linea-ptof.md` — Sezione 2 avanzamento PRIN in formato discorsivo per Macrotema A (campionamento, pipeline, risultati, cluster, attività future, potenziali pubblicazioni)
