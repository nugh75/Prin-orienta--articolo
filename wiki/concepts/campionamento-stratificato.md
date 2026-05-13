---
title: "Campionamento Stratificato (scuole italiane)"
tags: [campionamento, statistica, PTOF, metodologia]
created: 2026-05-13
updated: 2026-05-13
sources: [2026-0513-172544_orienta-campionamento.md, 2026-0513-220000_catena-numeri-orienta.md]
---

# Campionamento Stratificato

Metodologia di campionamento utilizzata da [[ORIENTA+]] per selezionare un campione rappresentativo delle scuole italiane.

## Strati

Ogni scuola è classificata in uno strato definito da 4 dimensioni:

| Dimensione | Categorie |
|------------|-----------|
| Gestione | Statale, Paritaria |
| Area Geografica | Nord Ovest, Nord Est, Centro, Sud, Isole |
| Territorio | Metropolitano, Non Metropolitano |
| Ordine | Infanzia, Primaria, Sec. Primo, Sec. Secondo, Altro |

Totale: 2 × 5 × 2 × 5 = **100 strati potenziali**

## Procedura

1. **Definizione strati** — classificazione scuole
2. **Estrazione proporzionale** — $n_{strato} = (N_{strato} / N_{totale}) \times n_{target}$
3. **Download PTOF** — ricerca URL + download PDF + conversione Markdown
4. **Validazione** — completezza e coerenza
5. **Pulizia codici** — rimozione file "impostori" (PTOF con codice meccanografico errato)

## Catena operativa

| Passaggio | Dato | Fonte |
|-----------|------|-------|
| Popolazione | 61.854 plessi MIM → ~19.365 istituzioni uniche | `SCUANAGRAFESTAT*.csv` + `SCUANAGRAFEPAR*.csv` |
| Scuole selezionate | 15.035 in 78 cicli | `strata_cycle_registry.jsonl` |
| Tentativi download | 9.984 (5.399 riusciti + 4.585 falliti) | `strata_cycle_state.json` |
| Resa download | **54,1%** (5.399 / 9.984) | `strata_cycle_state.json` |
| Istituti unici raggiunti | **3.082** | PRIN avanzamento |
| File entrati in pulizia | **2.584** (~500 scartati: non-PTOF, corrotti) | `ptof_cleaner.log` |
| Dopo bonifica codici | **2.095** (−289 «impostori» rimossi) | `ptof_cleaner.log` + `analysis_summary.csv` |
| Campione secondaria | **939** (693 II grado + 246 I grado) | `analysis_summary.csv` |
| Letture qualitative | 16 PTOF II grado | PRIN avanzamento |

Il passaggio 2.584 → 2.295 (−289) corrisponde ai «circa trecento» rimossi nella bonifica dei codici meccanografici.
