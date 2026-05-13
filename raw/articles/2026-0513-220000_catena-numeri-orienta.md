# Catena dei numeri — ORIENTA+ (da dati di progetto)

Data acquisizione: 2026-05-13
Fonte: /home/nugh75/LIste/ (repository progetto ORIENTA+)

---

## Anagrafe MIM (fonte delle "60.000+")

File in `/home/nugh75/LIste/data/`:

| File | Righe | Contenuto |
|------|-------|-----------|
| `SCUANAGRAFESTAT20252620250901.csv` | 50.350 | Plessi scolastici statali |
| `SCUANAGRAFEPAR20252620250901.csv` | 11.506 | Plessi scolastici paritari |
| **Totale** | **61.856** | Plessi scolastici totali |

→ Aggregati a ~19.365 istituzioni uniche (da `alignment_dry_run.log`).

---

## Pipeline di download

File: `data/strata_cycle_state.json`

```json
{
  "cycle_id": 79,
  "target_total": 6000,
  "yield_global": 0.541,
  "downloaded_total": 5399,
  "failed_total": 4585,
  "analyzed_total": 2095,
  "synced_at": "2026-02-13T14:48:34"
}
```

- **Tentativi totali**: 9.984 (5.399 successo + 4.585 falliti)
- **Resa**: 5.399 / 9.984 = **54,1%**
- **Istituti unici raggiunti**: ~3.082 (conteggio intermedio riportato nel PRIN)
- **Fallimenti documentati**: `reports/strata_failures.csv` (4.782 righe)

---

## Catena di pulizia

File: `ptof_cleaner.log`

```
2026-01-31 10:27 → 2.584 PTOF (file iniziali)
2026-01-31 10:38 → 2.295        (−289: rimozione codici errati e «impostori»)
2026-01-31 10:41 → 2.095        (−200: validazione codici meccanografici via LLM)
2026-02-11 00:27 → 2.191        (+96: rigenerazione da JSON a MD)
2026-02-13 13:05 → 1.898        (−293: secondo passaggio pulizia)
2026-02-14 17:52 → 1.853        (−45: pulizia finale)
```

Il passaggio 2.584 → 2.295 (−289) corrisponde ai **«circa trecento»** citati nell'articolo.

---

## Base analitica finale

File: `data/analysis_summary.csv` (2.095 scuole)

- **2.095** PTOF analizzati in totale (tutti i gradi)
- **693** secondaria di II grado
- **246** secondaria di I grado
- **1.156** infanzia, primaria, altro
- **16** letture qualitative in profondità (II grado)

---

## File di configurazione

File: `Makefile` e `data/taskrunner_state.json`

- `TARGET_TOTAL = 6000` (campione target)
- `SEED = 42`
- Strati: 2 (gestione) × 5 (area) × 2 (territorio) × 5 (ordine) = 100 strati
- Campionamento proporzionale: *n*~strato~ = (*N*~strato~ / *N*~totale~) × *n*~target~

---

## File rilevanti nel repository

| File | Contenuto |
|------|-----------|
| `data/strata_cycle_state.json` | Stato finale (download, analisi, yield) |
| `data/download_state.json` | Log per-strato download (riusciti/falliti) |
| `data/strata_cycle_registry.jsonl` | Cronologia per ciclo |
| `data/analysis_summary.csv` | 2.095 PTOF con punteggi dimensionali |
| `data/population_benchmarks.json` | Proporzioni popolazione nazionale |
| `data/SCUANAGRAFESTAT20252620250901.csv` | Anagrafe statali MIM |
| `data/SCUANAGRAFEPAR20252620250901.csv` | Anagrafe paritarie MIM |
| `reports/strata_failures.csv` | 4.782 fallimenti download |
| `ptof_cleaner.log` | Log completo pulizia codici |
| `alignment_dry_run.log` | Allineamento anagrafe MIM |