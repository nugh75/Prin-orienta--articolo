---
name: tone-of-voice
description: |
  Apply a precise yet creative academic writing style. Balanced between
  formal rigour and occasional metaphor/humour. Active when generating,
  revising, or translating any text intended for publication.
---

# Tone of Voice Skill

Apply these rules when writing, revising, or translating content.

## Core Principles

| # | Rule | Detail |
|---|------|--------|
| 1 | **Formal register with creative licence** | Academic tone, but allow occasional metaphors (any domain) and measured humour/irony. |
| 2 | **Short sentences** | Prefer concise, scannable sentences over long periodic constructions. |
| 3 | **Impersonal voice** | Use *"si ritiene"*, *"è possibile osservare"*, etc. Avoid first-person singular (*"io"*, *"ritengo"*). |
| 4 | **Accessible language** | Define every acronym at first use: *LLM (Large Language Model)*. Avoid unexplained jargon. |
| 5 | **No repetition** | Vary vocabulary; use synonyms rather than repeating the same term. |
| 6 | **Precision in data** | Report exact values: *"68,3%"*, not *"circa il 70%"*. |
| 7 | **Hook endings** | End each paragraph with a hook that leads into the next. |
| 8 | **Metacognitive signposts** | Include phrases like *"In questo articolo analizzeremo..."*, *"Come vedremo..."*. |
| 9 | **Digressions** | Brief asides in parentheses `()`; longer ones as footnotes. |
| 10 | **Lists** | Use bulleted/numbered lists only when strictly necessary. Prefer prose. |
| 11 | **Thematic unity** | Each theme must be opened, developed, and concluded within a single section. Every new term/concept must be briefly glossed on first mention; the full treatment belongs in the section dedicated to that concept. |
| 12 | **Linear argumentation** | The argument flow must be strictly linear — never introduce a concept whose comprehension depends on material that appears later in the text. |
| 13 | **Anafore univoche e zero** | Ogni pronome anaforico (questo, questa, ciò, esso, ella, loro, il, la, le, i, un, tale, simile, stesso, medesimo) deve avere un solo antecedente plausibile nel contesto immediato. Verificare sempre: a quale sostantivo rimanda il pronome? Se la risposta non è immediata, riscrivere. Analogamente, le anafore zero (soggetto o complemento omesso perché recuperabile dal contesto) devono essere interpretabili con certezza: se il lettore deve dedurre l'agente dall'azione verbale o dalla coesione testuale, il rischio di ambiguità è alto. In caso di dubbio, esplicitare il nome. |

## Diplomacy & Criticism

- Always use the conditional mood (*"sarebbe possibile"*, *"si potrebbe notare"*).
- Frame critiques as observations of limitations, not direct refutations.

## Bibliography & Citations

| Rule | Detail |
|------|--------|
| Authors | Last name only: *"Come sostiene Rossi..."* |
| Citation style | Delegate to `article-revision` skill (journal norms). |
| Quotation format | Delegate to `article-revision` skill. |

## Language

- **Primary language**: Italian (`ARTICLE_LANG=it`). The same tone applies to English text when translating.
- **Foreign terms**: Anglicisms and loanwords allowed when they are the standard technical term or when context requires it. When in Italian text, follow the accepted-anglicisms list from `article-revision`.
- **Article length**: Delegate to `.env` (`EDITORIAL_LIMIT_CHARS`) and editorial norms.

## Titles

- Descriptive and short.
- Avoid creative/punning titles.

## Interaction with Other Skills

| Skill | Handoff |
|-------|---------|
| `article-revision` | Citation format, quotation style, bibliography management, anglicism validation, length limits |
