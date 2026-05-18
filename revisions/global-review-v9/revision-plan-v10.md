<!-- accepted_since_bump: 20 -->

## Esito v10 (2026-05-18)

| ID | Stato | Nota |
|----|-------|------|
| P0-A..F | Accepted | §6 7976→1995; §4.7 eliminato; §5.1/5.2 sfoltiti; abstract IT/EN ridotti; §4.5/4.6 ridotti |
| P1-A/B/C | Accepted | tesi a fine §1; transizione §2→§3; Likert compresso |
| P2-A/D/E | Accepted | def. informatività; difesa campione 16 PTOF (Corbetta); NEET (ISTAT) |
| P2-B/P2-C | Accepted (numeri reali) | calcolati da `/home/nugh75/LIste/data/analysis_summary.csv` col `ptof_idpo`: P2-C r=0,998 (geom)/0,975 (PCA1) n=939; P2-B scostamento max 0,06 (gest. ±0,03; area −0,03/+0,06). Review diceva ±0,15 e r>0,92: reali più favorevoli |
| P3-A/B/C | Accepted | grassetto rimosso (incl. label parole chiave); `*governance*`→tondo; bib `[..]`→corsivo, 25 voci |
| P3-E | Lasciato «—» | DS IIPO assente in tutte le fonti; non inventata. Da compilare da dashboard |
| P4-A | Accepted | aggiunta «estrazione 5 gennaio 2026» (no «vers. 31/12/2025», non verificata) |
| P4-B | Obsolete | il §2 attuale non contiene «affiancare l'analisi umana su scala nazionale» |
| P4-C | Obsolete | articolo ha 3 obiettivi, non 5 |
| BIB-1 | Accepted | titolo Li → forma verificata `Camel… 'mind'…` + corsivo. ⚠ confligge con norma Roma (maiuscole titoli EN): tenuta forma verificata |
| BIB-2 | Accepted | De Nardo + «(disponibile su richiesta)» |
| BIB-3 | Differito | URL repo invariato; DOI Zenodo lo aggiungi dopo |

**Lunghezza:** corpo 32.917 · bib 3.443 · tot 36.423. Limite 30.000: utente ha scelto «non fare niente» → nessun taglio ulteriore (resta sopra; da decidere se bib esclusa dal conteggio).

**TODO prima dell'invio:** numeri esatti P2-B/P2-C/P3-E dalla dashboard · DOI Zenodo (BIB-3) · maiuscoletto autori bib (in render .docx, non in MD) · nota biografica (max 300 battute).

# Revision Plan — v10 (global-review-v9)

**Article:** `articles/article-v10-2026-05-18-1403.md`
**Base:** v9-1218 (bumped) · **Limit:** 30.000 chars · **Current:** 39.176 (over by 9.176)
**Sources:** `revision-elem-v9.md`, `audit-bibliografia-v9.md`
**Mode:** batch by priority · **Lang:** it

## Status legend
`To decide` / `Accepted` / `Rejected` / `Obsolete`

## Batch P0 — Length (priority)
| ID | Point | Δ chars | Status |
|----|-------|---------|--------|
| P0-A | Cut §6 Conclusioni 7976 → ~3000 | ~−5000 | To decide |
| P0-B | §4.7 → rinvio a §3.5 | ~−390 | To decide |
| P0-C | Merge §5.1 ↔ §5.2 redundancy | ~−500 | To decide |
| P0-D | Trim IT abstract 932 → ≤700 (norm) | ~−250 | To decide |
| P0-E | Trim EN abstract 842 → ≤700 (norm) | ~−150 | To decide |
| P0-F | Trim §4.6 Empedocle example + §4.5 percentuali | ~−400 | To decide |

## Batch P1 — Structure
| ID | Point | Status |
|----|-------|--------|
| P1-A | Add explicit thesis at end of §1 | To decide |
| P1-B | Add §2→§3 transition (start of §3) | To decide |
| P1-C | Shorten Likert 7-level block (§3.2) | To decide |

## Batch P2 — Content/validity (net adds chars)
| ID | Point | Status |
|----|-------|--------|
| P2-A | Define «grado di informatività» (§1) | To decide |
| P2-B | Post-stratification paragraph (§5.4) | To decide |
| P2-C | IIPO sensitivity analysis note (§3.2) | To decide |
| P2-D | Defend 16-PTOF validation sample (§3.5) | To decide |
| P2-E | NEET «fisiologico» → evidence-based (§4.3) | To decide |

## Batch P3 — Editorial (norm-binding)
| ID | Point | Status |
|----|-------|--------|
| P3-A | Remove bold in body (§4.3, table pseudo-headings) | To decide |
| P3-B | `*governance*` → tondo in tables (§4.4) | To decide |
| P3-C | Bibliography `[Titolo]` → *corsivo* | To decide |
| P3-E | Add DS IIPO in §4.2 tables | To decide |

## Batch P4 — Clarity
| ID | Point | Status |
|----|-------|--------|
| P4-A | MIM dataset version/date (§1) | To decide |
| P4-B | Objective 2 cautious wording (§2) | To decide |
| P4-C | Objectives 4–5 reformulation | **Obsolete** — article now has 3 objectives |

## Batch BIB — Bibliography audit
| ID | Point | Status |
|----|-------|--------|
| BIB-1 | Li G. et al. (2023): `"Mind"` → `'mind'` | To decide |
| BIB-2 | De Nardo (2026): add «disponibile su richiesta» | To decide |
| BIB-3 | Dragoni (2026): add commit hash / DOI | To decide |

## Notes / conflicts
- **P3-D (abstract length):** review asked to *extend*; v9-1218 already over-extended (932/842 vs norm 500–700). Norm wins → reframed as P0-D/P0-E *trim*.
- **P4-C:** review assumed 5 objectives; article §2 now states 3. Marked Obsolete.
- **Char target:** even with all P0 + P2 adds, residual ~1.000–2.000 over; extra method/results trims may be needed (flag at end of P0).
- **Maiuscoletto authors:** norm requires small-caps for bib authors; Markdown cannot represent it — defer to .docx render pass.
- **§6 internal inconsistency:** "pipeline a quattro agenti — Analyst, Reviewer, Refiner" lists 3; "939 PTOF" vs 2.095 analytic base — fold fix into P0-A rewrite.

## Bump History
- v9 → v10 — 2026-05-18 14:03 — session-start bump (0 accepted changes)
