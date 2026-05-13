# Prin-orienta+

Knowledge base personale basato sul paradigma **LLM Wiki** di Andrej Karpathy.
Personal knowledge base based on Andrej Karpathy's **LLM Wiki** paradigm.

---

## Architettura / Architecture

Tre strati — Three layers:

```
Prin-orienta+/
├── AGENTS.md         # Schema — dice all'LLM come gestire il wiki
│                     # Schema — tells the LLM how to maintain the wiki
├── raw/              # Layer 1: Fonti immutabili (tu inserisci)
│                     # Layer 1: Immutable sources (you add files)
│   ├── articles/     #   Articoli web / Web articles
│   ├── papers/       #   Paper accademici / Academic papers
│   ├── notes/        #   Appunti personali / Personal notes
│   └── assets/       #   Immagini, diagrammi / Images, diagrams
└── wiki/             # Layer 2: Wiki generato dall'LLM
                      # Layer 2: LLM-generated wiki
    ├── index.md      #   Catalogo dei contenuti / Content catalog
    ├── log.md        #   Registro cronologico (append-only)
    │                 #   Chronological action log (append-only)
    ├── entities/     #   Persone, organizzazioni, modelli
    │                 #   People, organizations, models
    ├── concepts/     #   Argomenti, idee, definizioni
    │                 #   Topics, ideas, definitions
    └── comparisons/  #   Analisi comparative / Side-by-side analyses
```

---

## Operazioni / Operations

### Ingest — aggiungere una fonte / adding a source

1. Metti il file in `raw/<categoria>/` — Place the file in `raw/<category>/`
2. Chiedi all'LLM: *"Ingesta raw/articles/nome-file.md nel wiki"*
   Ask the LLM: *"Ingest raw/articles/nome-file.md into the wiki"*
3. L'LLM legge la fonte, discute con te, crea/aggiorna pagine wiki, aggiorna `index.md`, scrive in `log.md`
   The LLM reads the source, discusses with you, creates/updates wiki pages, updates `index.md`, writes to `log.md`

### Query — interrogare la conoscenza / querying knowledge

1. L'LLM cerca pagine wiki pertinenti (usa `index.md` o `qmd`)
   The LLM finds relevant wiki pages (via `index.md` or `qmd`)
2. Sintetizza una risposta con `[[wikilink]]` alle fonti
   Synthesizes an answer with `[[wikilinks]]` to sources
3. Le risposte di valore possono essere salvate come nuove pagine wiki
   Valuable answers can be filed back as new wiki pages

### Lint — manutenzione / maintenance

Chiedi periodicamente: *"Fai un health-check del wiki"* per trovare contraddizioni, pagine orfane, riferimenti mancanti.
Periodically ask: *"Run a health-check on the wiki"* to find contradictions, orphan pages, missing references.

---

## Strumenti sul server / Server tools

| Tool | Install | Usage |
|------|---------|-------|
| **opencode** | Preinstallato / Preinstalled | `opencode` per interagire con il wiki / to interact with the wiki |
| **claude** | Preinstallato / Preinstalled | `claude` come LLM agent alternativo / alternative LLM agent |
| **qmd** | `source ~/.bashrc && qmd --help` | Ricerca full-text + semantica / Full-text + semantic search |

### Configurare qmd / Setting up qmd

```bash
source ~/.bashrc
qmd collection add /home/nugh75/Prin-orienta+/wiki --name prin-orienta
qmd update
qmd query "la tua domanda / your question"
```

### Git (versionamento / version control)

```bash
git add -A
git commit -m "Describe your changes"
```

---

## Formato pagina wiki / Wiki page format

Ogni pagina wiki ha frontmatter YAML — Every wiki page has YAML frontmatter:

```yaml
---
title: "Titolo Pagina / Page Title"
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [nome-fonte.md]
---
```

Usa `[[wikilink]]` per collegare pagine tra loro.
Use `[[wikilinks]]` for cross-references between pages.

---

## Scrittura articolo / Article Writing

Usa il wiki Karpathy per scrivere articoli — Use the Karpathy wiki to write articles:

```
1. Ingest fonti in raw/ → LLM compila wiki/
2. Chiedi bozza: "Scrivi un articolo su [tema] basato sul wiki"
   Ask draft: "Write an article on [topic] based on the wiki"
3. Salva in articles/article-v1-YYYY-MM-DD-HHMM.md
4. Per revisione: carica i commenti dei revisori e invoca la skill
   For revision: load reviewer comments and invoke the skill
```

## Revisione articolo / Article Revision

Il progetto include la skill **article-revision** per revisioni iterative con revisori.
The project includes the **article-revision** skill for iterative peer-review rounds.

```bash
# Attivare la revisione / Start a revision round:
# 1. Metti i commenti del revisore in revisions/<nome>/
# 2. Chiedi all'LLM: "Processa i commenti del revisore [nome]"
#    Ask the LLM: "Process reviewer [name]'s comments"
```

### Struttura revisione / Revision layout

```
articles/article-v1-*.md              # Bozza / Draft
bibliography/reference.bib             # Bibliografia / Bibliography
editorial-norms/norms.md              # Norme editoriali / Editorial norms
revisions/<reviewer>/
├── revision-plan-v1.md               # Piano / Plan
└── final-sheet-v1.md                 # Report finale / Final report
.env                                  # Configurazione / Configuration
.venv/                                # Python env per script skill
```

### Trigger skill / Skill triggers

- *"revise the article" / "revisiona l'articolo"*
- *"apply reviewer X comments" / "applica i commenti del revisore X"*
- *"revise paragraph 3" / "revisiona il paragrafo 3"*
- *"let's process the reviewer comments"*
