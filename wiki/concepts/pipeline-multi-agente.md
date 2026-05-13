---
title: "Pipeline Multi-Agente ORIENTA+"
tags: [pipeline, AI, LLM, analisi, PTOF]
created: 2026-05-13
updated: 2026-05-13
sources: [2026-0513-172514_orienta-documentazione.md]
---

# Pipeline Multi-Agente

Architettura di analisi automatica dei PTOF utilizzata da [[ORIENTA+]].

## Flusso

```
PDF → Validazione PTOF → Markdown → Analyst → Reviewer → Refiner → JSON + Report
                                                                  ↓
                                                         Controlli → CSV → Dashboard
```

## Agenti

| Agente | Ruolo |
|--------|-------|
| **Analyst** | Prima lettura: estrazione punteggi, bozza narrativa |
| **Reviewer** | Controllo critico: verifica citazioni, correzione punteggi |
| **Refiner** | Editor finale: integra correzioni, produce JSON + report coerente |
| **Background Reviewer/Fixer** | Controllo coerenza punteggi-narrativa-metadati |

## Fasi

1. **Download** — ricerca URL PTOF su portale Unica + siti istituzionali + web
2. **Validazione** — verifica che il documento sia un PTOF valido (titolo, indizi testuali, triennio)
3. **Conversione** — PDF → Markdown
4. **Analisi multi-agente** — pipeline a 3 agenti
5. **Pulizia dataset** — `make clean-ptof-codes`: riconciliazione codici, rimozione "impostori"

## Modelli

Supporta OpenRouter, Gemini, Ollama (qwen3:32b per il catalogo attività).
