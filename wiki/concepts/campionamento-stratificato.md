---
title: "Campionamento Stratificato (scuole italiane)"
tags: [campionamento, statistica, PTOF, metodologia]
created: 2026-05-13
updated: 2026-05-13
sources: [2026-0513-172544_orienta-campionamento.md]
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

## Risultati

- 78 cicli di estrazione
- 15.035 scuole selezionate
- 3.082 PTOF scaricati (resa 54,1%)
- ~300 entry non valide rimosse nella fase di pulizia
