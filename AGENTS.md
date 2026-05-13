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
