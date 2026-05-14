# 32 — Simulated Dual Peer Review

Triggered by `/r-pr-2`. Simulates two independent peer reviewers with distinct personas reading the article section by section. Synthesises convergent/divergent feedback and presents a unified proposal per section.

## 0. Entry Point

Invoked by `/r-pr-2` or phrases like:
- *"simula una revisione di due peer reviewer"*
- *"fai finta che due reviewer leggano l'articolo"*
- *"dual peer review simulation"*

If the user says "simula tre reviewer", adapt — add a third persona on the fly (e.g. Reviewer C: language/style specialist). The pattern scales.

## 1. Bootstrap & Setup

If not already done, run `00-bootstrap.md` and `10-setup.md` to load `.env`, norms, bibliography, active article, and detect `ARTICLE_LANG`. **Note:** `10-setup.md` step 5 enforces a mandatory version bump before any revision work begins — do not skip it.

## 2. Define Reviewer Personas

Use these personas unless the user overrides:

### Reviewer A — Il Metodologo / The Methodologist

- **Focus:** Research design, sampling, data quality, internal/external validity, statistical choices, replicability
- **Tone:** Rigorous, precise, sometimes sceptical
- **Typical comments:** "The sample size is insufficient for the claimed effect", "Confound X is not controlled for", "The measurement instrument for Y has known reliability issues"
- **Likes:** Preregistration, power analysis, sensitivity checks, transparent limitations
- **Dislikes:** Overclaiming, p-hacking, convenience samples presented as representative

### Reviewer B — Il Teorico / The Theoretician

- **Focus:** Literature positioning, argument coherence, contribution novelty, theoretical grounding, writing quality, narrative arc
- **Tone:** Broad, synthetic, sometimes demanding
- **Typical comments:** "The theoretical gap is overstated — see Author (2020) for a similar argument", "The contribution is unclear: what does this add beyond the existing literature?", "Section 3 and Section 5 contradict each other on the definition of X"
- **Likes:** Clear contribution statements, honest engagement with prior work, elegant argument structure
- **Dislikes:** Strawman arguments, citation padding, vague research questions

Announce the personas in chat:

```
## Simulazione Dual Peer Review

**Reviewer A — Il Metodologo**: si concentra su disegno di ricerca, campionamento, qualità dei dati, validità, scelte statistiche.
**Reviewer B — Il Teorico**: si concentra su posizionamento nella letteratura, coerenza argomentativa, novità del contributo, qualità della scrittura.

Articolo: <article-path>
Sezioni individuate: N
Lingua rilevata: <ARTICLE_LANG>

Inizio dalla prima sezione? (sì / scegli sezione / annulla)
```

## 3. Parse Article Into Sections

1. Read the full article (skip YAML frontmatter).
2. Split by headings (`#`, `##`, `###`). A section is the heading line + all body paragraphs before the next heading of equal or higher level.
3. Number sections: `§1`, `§2`, ..., `§N`.

## 4. Generate Dual Reviews Per Section

For each section, generate independent reviewer comments, then synthesise.

### Step 4a — Load Section Context

Read the section text, the immediately preceding heading, and the next heading (for narrative context). If a citation is mentioned, verify it with `40-bibliography-check.md` first.

### Step 4b — Generate Reviewer A Comments

Apply the Methodologist persona. Focus on:
- Is the research design clearly described?
- Are sample, measures, and procedures adequately specified?
- Are statistical choices justified?
- Are limitations acknowledged?
- Is there any overclaiming relative to the evidence?

### Step 4c — Generate Reviewer B Comments

Apply the Theoretician persona. Focus on:
- Is the literature positioning accurate and fair?
- Is the contribution clearly stated?
- Does the argument flow logically?
- Are there contradictions with earlier/later sections?
- Is the writing clear, precise, and well-paced?

### Step 4d — Classify Convergence

Compare the two sets of comments. Classify each observation as:

| Label | Meaning |
|---|---|
| **Convergent (C)** | Both reviewers identify the same issue independently |
| **Divergent (D)** | The reviewers disagree or prioritise differently |
| **Independent (I)** | Only one reviewer raised this point; the other is silent |

### Step 5 — Present Synthesis

```
## §<N> — <section title>

**Testo originale** (`<article>:<line-range>`)
> <section text, truncated to ~500 chars if long>

---

**Reviewer A (Metodologo):**
> <verbatim comment 1>
> <verbatim comment 2>
> ...

**Reviewer B (Teorico):**
> <verbatim comment 1>
> <verbatim comment 2>
> ...

---

**Analisi di convergenza:**

| # | Tema | Reviewer A | Reviewer B | Stato |
|---|---|---|---|---|
| 1 | <topic> | <summary> | <summary> | C |
| 2 | <topic> | <summary> | <summary> | D |
| 3 | <topic> | <summary> | — | I |
| 4 | <topic> | — | <summary> | I |

**Punti convergenti (C):** <explain what both agree on; these have the highest priority>
**Punti divergenti (D):** <explain the disagreement; user must decide which direction to take>

---

**Proposta unificata:**
> <proposed text integrating feedback from both reviewers>

**Modifiche:**
1. [A] <old> → <new> [(motivazione)]
2. [B] <old> → <new> [(motivazione)]
3. [A+B] <old> → <new> [(motivazione — convergent)]
...

**Δ**: chars <signed> / words <signed> · risk: <low|medium|high>

**Norms respected**: <list>
**Possible exceptions**: <list, with reason>

**A/R/M?** (usa i tag reviewer: "A A 1,3", "R B 2", "A A+B 3")
```

### Modification Tag Convention

| Tag | Meaning |
|---|---|
| `[A]` | Modification from Reviewer A only |
| `[B]` | Modification from Reviewer B only |
| `[A+B]` | Convergent modification (both reviewers agree) |

The user responds with reviewer-tagged acceptance:
- `A A 1,3` → accept Reviewer A's modifications 1 and 3
- `R B 2` → reject Reviewer B's modification 2
- `A A+B 3` → accept the convergent modification 3
- `A` (no numbers) → accept all modifications from all reviewers
- `R` (no numbers) → reject the entire section's proposals

## 6. Handle Responses

Follow `30-iterate-points.md`, section 4, with the reviewer-tag extension:

- **Accept** (with reviewer tags and numbers) → apply only the matching modifications.
- **Reject** (with reviewer tags and numbers) → annotate rejected + reason.
- **Reject entire section** → mark all proposals as rejected, advance to next section.
- **Modify `<reviewer-tag> <N>: <direction>`** → regenerate that modification.

After applying, output:

```
Applicate modifiche: A 1,3, B 2. [Restano in sospeso: nessuna.] Ci sono altri cambiamenti in questa sezione?
```

Wait for explicit advance command: `prossima sezione`, `next section`, `§<N>` to jump.

## 7. Divergent Point Resolution

When reviewers disagree (D status), the skill must **not** choose sides automatically. Instead:

```
⚠️ Divergenza sul punto #<N>:
- Reviewer A suggerisce: <direction A>
- Reviewer B suggerisce: <direction B>

Quale direzione preferisci? (A / B / sintesi personalizzata / salta)
```

Wait for the user. Never resolve divergence silently.

## 8. Store Reviewer Comments

After each section is processed, append the full reviewer comments and the final decision to:

```
revisions/<article-slug>/peer-review-simulation-vN.md
```

Use this structure:

```markdown
---
reviewer_a_persona: "Il Metodologo"
reviewer_b_persona: "Il Teorico"
article: <article-path>
created: YYYY-MM-DD
---

## §1 — <section title>

### Reviewer A
<full comments>

### Reviewer B
<full comments>

### Convergence Analysis
<C/D/I classification>

### Decisions
- Modification 1: Accepted
- Modification 2: Rejected (reason)
- ...

## §2 — <section title>
...
```

## 9. Edge Cases

- **Single-section article.** Still run dual review. The synthesis step is identical.
- **Reviewer silence.** If a reviewer has genuinely nothing to say about a section (rare), mark as "No comments" and proceed with the other reviewer's feedback only.
- **Reviewer agreement on rejection.** If both reviewers agree a section should be removed entirely, present it as a convergent (C) point with a high-risk flag.
- **Bibliography conflicts.** If either reviewer flags a citation issue, run `40-bibliography-check.md` before presenting the proposal.
- **Pause.** `pause` — record current section. Resume on next invocation.
- **Character budget.** Track after each accepted change. Warn on overshoot.

## 10. Completion

When all sections are processed:

```
Simulazione dual peer review completata.
Sezioni processate: N
Punti convergenti: X
Punti divergenti: Y
Punti indipendenti: Z
Modifiche accettate (A): Xa
Modifiche accettate (B): Xb
Modifiche accettate (A+B): Xab
Modifiche respinte: R
Bilancio caratteri: +Δ (limite: EDITORIAL_LIMIT_CHARS)
Report salvato in: revisions/<article-slug>/peer-review-simulation-vN.md

Vuoi generare il final sheet? (/r-sheet)
Vuoi fare il bump di versione? (/r-bump)
```

Wait for the user.
