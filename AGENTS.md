# LLM Wiki — Schema & Conventions

## Architecture
Three layers:
- **raw/** — Immutable source documents. LLM reads, never modifies.
- **wiki/** — LLM-generated markdown files. LLM owns this layer entirely.
- **AGENTS.md** — This schema file. Co-evolved between human and LLM.

## Directory Structure
```
raw/
├── articles/     # Web articles, clippings
├── papers/       # Academic papers, PDFs
├── notes/        # Personal notes, meeting notes
└── assets/       # Images, diagrams
wiki/
├── index.md      # Content catalog with one-line summaries, organized by category
├── log.md        # Chronological action log (append-only)
├── entities/     # People, organizations, products, models
├── concepts/     # Topics, ideas, definitions
└── comparisons/  # Side-by-side analyses
```

## Wiki Page Format
Every wiki page MUST have YAML frontmatter:
```yaml
---
title: "Page Title"
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-file-name.md]
---
```
Use `[[wikilinks]]` for cross-references between pages.

## Operations

### Ingest
1. User drops source into `raw/<category>/`
2. LLM reads the source
3. LLM discusses key takeaways with user
4. LLM writes/updates wiki pages (summary, entities, concepts)
5. LLM updates `index.md`
6. LLM appends entry to `log.md`
7. LLM links to source in `raw/`

### Query
1. Read `index.md` to find relevant pages
2. Drill into specific pages
3. Synthesize answer with `[[wikilinks]]` citations
4. File valuable answers back into wiki as new pages

### Lint
Periodically scan for: contradictions, stale claims, orphan pages, missing cross-references, gaps to fill via web search.

---

# Article Writing & Revision

## Article Writing Workflow (Wiki-based)

Use the wiki paradigm to write an academic article:

1. **Ingest sources** → place documents in `raw/`, have LLM compile them into `wiki/`
2. **Draft article** → LLM writes bozza in `articles/article-v1-YYYY-MM-DD-HHMM.md` based on wiki content
3. **Store in wiki** → summarise the article in `wiki/index.md` and log in `wiki/log.md`

## Article Format
Articles live in `articles/` following the convention:
```
articles/article-v<N>-YYYY-MM-DD-HHMM[-anonymous].md
```

## article-revision
See `.claude/skills/article-revision/AGENTS.md` for the full review/revision workflow.

## tone-of-voice
See `.claude/skills/tone-of-voice/SKILL.md`. Apply this tone when writing,
revising, or translating any text for publication.

### When to use the revision skill
When the user says: *"revise the article"*, *"apply reviewer X comments"*, *"revise paragraph 3"*, *"let's process the reviewer comments"*.

### Project layout for revision
```
articles/                         # Article drafts
bibliography/
└── reference.bib                 # .bib file
editorial-norms/
└── norms.md                      # Journal norms
revisions/                        # Revision plans and final sheets
data/                             # Optional: sample data for stats
.env                              # Config (EDITORIAL_LIMIT_CHARS, etc.)
```

---

# Fonte dati ORIENTA+ (portale)

**I numeri dell'articolo (IIPO, medie dimensionali, conteggi, attività, cluster, statistiche territoriali) provengono dalla piattaforma ORIENTA+, il cui codice e dati stanno in `/home/nugh75/LIste`** (vedi `.env`: `ORIENTA_DATA_PATH`, `ORIENTA_MASTER_CSV`). La dashboard pubblica `https://orienta.ai4educ.org/` è l'app Streamlit in `LIste/app/` (JS-rendered: NON estraibile via WebFetch — leggere i file locali).

## Regola di integrità (vincolante)
Quando l'articolo richiede una cifra (DS, correlazioni di sensitività, scostamenti di post-stratificazione, medie, percentuali) **NON inventarla e NON copiarla da un documento di review**: ricavarla dai dati in `/home/nugh75/LIste`. Se non ricavabile lì, lasciare il valore aperto e segnalarlo, mai un numero plausibile.

## Dove guardare
| Cosa | Percorso |
|---|---|
| Tabella master per-scuola (2.095 righe, 54 col) | `LIste/data/analysis_summary.csv` |
| IIPO per scuola | colonna `ptof_idpo` del master CSV |
| Definizione IIPO | `LIste/src/processing/align_metadata.py:545` — `calc_avg([m for m in all_means if m>0])` (media delle medie dimensionali non nulle) |
| Media IIPO come la calcola la dashboard | `df['ptof_idpo'].mean()` (vedi `LIste/src/taskrunner/web/routes/strata.py:194`) |
| Analisi per-PTOF (json/md) | `LIste/analysis_results/` |
| Sintesi/aggregati | `LIste/reports/`, `LIste/docs/analysis/` |
| Registro attività / cluster | `LIste/data/activity_registry.json`, `LIste/data/analysis_registry.json` |

Campi utili nel master: `ordine_grado` (`I Grado` n=246, `II Grado` n=693, …), `statale_paritaria`, `area_geografica`, `territorio`, `2_1_score` (dim. Strutturale), `mean_finalita|mean_obiettivi|mean_governance|mean_didattica_orientativa|mean_opportunita`.

## Caveat di riproducibilità
Il calcolo naive «media di 6 colonne» **non** riproduce le medie IIPO pubblicate (3,44 I / 3,48 II): usare `ptof_idpo`, e per riprodurre i totali delle tabelle replicare il filtro/snapshot della dashboard, non una formula propria. Differenze residue → segnalarle, non aggiustare i numeri.
