---
title: "Report di Sintesi ORIENTA+"
tags: [report, sintesi, PTOF, risultati, I Grado, II Grado]
created: 2026-05-13
updated: 2026-05-13
sources: [reports/20260216_0920__Sintesi_PTOF__IGrado_n5.md, reports/20260216_0637__Sintesi_PTOF__IIGrado_n1.md, reports/20260215_1258__Sintesi_PTOF__IGrado.md]
---

# Report di Sintesi ORIENTA+

Report generati automaticamente dalla [[Pipeline Multi-Agente]] di [[ORIENTA+]] per sintetizzare i dati raccolti dall'analisi dei PTOF.

## Struttura Comune

Ogni report include:
1. **Premessa** — cosa si misura (copertura documentale, non qualità)
2. **Metodo** — analisi strutturale + semantica, [[Framework di Valutazione a 6 Dimensioni|6 dimensioni]]
3. **Scala Likert 1-7** e [[IIPO]]
4. **Strategia di generazione** — pipeline a 3 fasi (scheletro → slot filling → revisione)
5. **Analisi del campione** — bilanciamento gestione, geografia, territorio
6. **Sintesi quantitativa** — medie e deviazioni standard per dimensione
7. **Profilazione cluster** — 5 gruppi omogenei di scuole
8. **Analisi qualitativa** — narrativa per sezione tematica
9. **Conclusioni e limiti**

## Modelli LLM Utilizzati

- google/gemini-3-pro-preview
- z-ai/glm-5
- minimax/minimax-m2.5

## Dati Principali (I Grado)

- 246 scuole analizzate, 84 province, 18/20 regioni
- Sovrarappresentazione scuole paritarie (+16 pp) e Centro-Sud (+7-8 pp)
- IIPO medio non riportato nei report disponibili

| Dimensione | Media | Dev. Std. |
|------------|-------|-----------|
| Strutturale | 2.39 | 1.67 |
| Finalità | 3.51 | 1.09 |
| Obiettivi | 3.10 | 1.11 |
| Governance | 3.61 | 1.05 |
| Didattica | 3.62 | 1.01 |
| Opportunità | 3.07 | 1.11 |

## Dati Principali (II Grado)

I report per II Grado seguono la stessa struttura. I dati specifici sono nei singoli file in `raw/articles/reports/`.

## Report Disponibili

11 report Markdown + 7 PDF in `raw/articles/reports/`, generati tra il 15 e il 16 febbraio 2026.
