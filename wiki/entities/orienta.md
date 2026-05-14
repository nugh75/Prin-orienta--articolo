---
title: "ORIENTA+"
tags: [piattaforma, PTOF, orientamento, AI]
created: 2026-05-13
updated: 2026-05-14
sources: [2026-0513-172409_orienta-il-progetto.md, 2026-0513-172544_orienta-campionamento.md, 2026-0513-172514_orienta-documentazione.md, 2026-0514-orienta-piattaforma-completa.md]
---

# ORIENTA+

Piattaforma basata su LLM per l'analisi semantica su larga scala dei PTOF delle scuole italiane: rileva cosa le scuole documentano in materia di orientamento e con quale grado di informatività e accuratezza, senza formulare giudizi di valore sulle pratiche effettivamente implementate. Sviluppata da [[Daniele Dragoni]] nell'ambito del dottorato presso [[Università Roma Tre]].

## Obiettivo

Analizzare i Piani Triennali dell'Offerta Formativa (PTOF) delle scuole italiane per rilevare, estrarre e catalogare le informazioni relative ad attività, metodologie e governance dell'orientamento. La piattaforma non giudica la qualità della scuola ma la **completezza documentale** con cui l'orientamento è descritto nei PTOF.

## Funzionamento

L'analisi opera su tre livelli:
1. **Analisi Strutturale (Compliance)** — verifica conformità al D.M. 328/2022
2. **Analisi Semantica** — tramite LLM, estrae informazioni sul [[Framework di Valutazione a 6 Dimensioni|framework a 6 dimensioni]] e produce l'[[IIPO]]
3. **[[Catalogo Attività ORIENTA+|Catalogazione delle Attività]]** — tramite Qwen3:32b, censice e classifica metodologie didattiche, progetti, partnership, azioni di sistema e buone pratiche

L'analisi automatizzata non si limita a cercare parole chiave, ma legge e interpreta il testo distinguendo dichiarazioni di intenti da azioni concrete, mappando progetti, risorse, tempi e responsabilità.

## Output

Doppio output per ogni scuola:
- **JSON strutturato** per analisi tecniche
- **Report narrativo in Markdown** per lettura umana, articolato in: sintesi generale, analisi dimensionale, punti di forza, aree di debolezza, gap analysis, conclusioni

## Metodo di Campionamento

[[Campionamento Stratificato (scuole italiane)|Campionamento stratificato multi-stage]] su 100 strati potenziali.
- 78 cicli di estrazione completati
- 15.035 scuole selezionate, 3.082 PTOF scaricati (resa 54,1%)
- Copertura: 18/20 regioni, 84/107 province

## Indice

L'[[IIPO]] (Indice Informativo delle Pratiche di Orientamento) è la metrica sintetica che riassume i punteggi delle 6 dimensioni.

## Strumenti di Analisi

Vedi [[Strumenti di Analisi ORIENTA+]] per la panoramica completa: KPI Dashboard, Analisi Territoriale, Analisi Dimensionale, Analytics Avanzati, Ricerca e Impatto, Scuola (Dettaglio e Gap Analysis).

## Licenza

Creative Commons Attribuzione - Non commerciale - Non opere derivate 4.0 Internazionale. Marchio registrato.
