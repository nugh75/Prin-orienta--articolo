# LLM Wiki - Schema & Conventions

## Architecture
Three layers:
- **raw/** — Immutable source documents (articles, papers, notes, assets). LLM reads, never modifies.
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

## Index Format (`wiki/index.md`)
```markdown
# Wiki Index

## Concepts
- [[Concept Name]] — One-line summary

## Entities
- [[Entity Name]] — One-line summary

## Sources
- [source-name](raw/articles/source-name.md) — Brief description
```

## Log Format (`wiki/log.md`)
```markdown
## [YYYY-MM-DD] ingest | Source Title
- Summary: ...
- Pages touched: [[Page1]], [[Page2]]
```
