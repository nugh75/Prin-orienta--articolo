# Revisione Globale — Articolo v9

**Articolo:** `articles/article-v9-2026-05-18-1107.md`
**Data:** 18 maggio 2026
**Revisione:** Globale (7 lenti)
**Lunghezza attuale:** ~38.500 caratteri (limite: 30.000)

---

## Sintesi Esecutiva

La revisione globale evidenzia **quattro aree di intervento**:

1. **Lunghezza** — +8.500 caratteri sopra il limite editoriale
2. **Struttura** — duplicazioni tra §5 e §6, proposizione della tesi poco anticipata
3. **Contenuto** — alcuni claim richiederebbero maggior cautela o evidenze
4. **Editoriale** — uso esteso di grassetto che contrasta con le norme RomaTrE-Press

---

## P0. Lunghezza — Obiettivo prioritario

**Problema:** 38.500 caratteri, valore massimo ammesso 30.000. Serve tagliare almeno **8.000 caratteri** senza compromettere il contenuto scientifico.

### P0-A. Sezione Conclusioni sovrarappresentata

| Sezione | Caratteri attuali | % totale | Caratteri target |
|---------|-------------------|----------|------------------|
| §6 Conclusioni | ~8.900 | ~23% | ~3.000 (10%) |

**Azioni:**

1. **Tenere i primi 2 paragrafi**: riassunto obiettivi + risultati chiave
2. **Tagliare il paragrafo su IIPO/fraz.** — già in §4.4/§5.2: ~400 caratteri
3. **Eliminare il paragrafo sui limiti** — già in §5.4: ~600 caratteri
4. **Spostare in §5.5**: il paragrafo su catalogo come dispositivo didattico + coinvolgimento scuole: ~1.200 caratteri
5. **Accorciare il paragrafo finale** a 3-4 frasi essenziali: ~2.000 caratteri salvati

**Δ salvati:** ~4.200 caratteri

---

### P0-B. Fusione §4.7 → rinvio a §3.5

**Problema:** Il §4.7 ripete quanto già espresso in §3.5 (paragrafo su convergenza AI/umana).

**Azione:** sostituire §4.7 con:

> «Come anticipato in §3.5, il confronto tra lettura umana e analisi automatica ha mostrato convergenza sostanziale. Si rimanda a quella sede per i dettagli sulla validazione qualitativa.»

**Δ salvati:** ~350 caratteri

---

### P0-C. Ridondanze §5.1 ↔ §5.2

**Problema:** «Il divario tra documento e pratica» (§5.1) e «La frammentazione come tratto dominante» (§5.2) condividono lo stesso concetto: le scuole documentano attività ma non le incorniciano in una strategia unitaria.

**Azione:** accorciare §5.1 a 2 paragrafi, integrando il primo paragrafo di §5.2 (definizione risultato-chiave):

1. Mantenere il dato IIPO come evidenza del divario dichiarativo
2. Fusione prime 2 frasi di §5.2 nel §5.1
3. Tagliare la frase finale su «l'evidenza più chiara»

**Δ salvati:** ~500 caratteri

---

## P1. Struttura e Architettura Argomentativa

### P1-A. Tesi poco anticipata

**Problema:** La tesi (affermazione centrale) non compare all'inizio del §1. Il §1 descrive contesto e strumento ma non esplica chiaramente la *claim* principale.

**Azione:** aggiungere nella chiusura del §1:

> «Sulla base della convergenza rilevata, il lavoro sostiene che l'analisi automatica su larga scala mediante pipeline multi-agente è un metodo fattibile e convergente per il monitoraggio delle politiche educative.»

---

### P1-B. Transizione §2 → §3 brusca

**Problema:** Dopo l'elencazione dei tre obiettivi, manca una frase di aggancio al metodo. Il salto è immediato a «Per questa ragione si è proceduto a un campionamento».

**Azione:** aggiungere all'inizio del §3:

> «Per perseguire questi obiettivi, è stata sviluppata e validata la piattaforma ORIENTA+, che applica una pipeline multi-agente basata su LLM.»

---

### P1-C. Scala Likert eccessivamente dettagliata

**Problema:** §3.2 elenca tutti e sette i livelli della scala Likert dettagliatamente. L'informazione è utile ma occupa spazio.

**Azione:** sostituire il blocco con una tabella sintetica o una frase riassuntiva:

> «La scala Likert a 7 livelli definisce sei livelli intermedi tra «assente» e «eccellente», con il livello 4 («sufficiente») come soglia minima per includere un sotto-indicatore nell'aggregazione.»

**Δ salvati:** ~150 caratteri

---

## P2. Contesto e Chiarezza

### P2-A. Definizione «grado di informatività» mancante (§1)

**Problema:** il termine «grado di informatività» appare senza definizione operativa.

**Azione:** dopo «grado di informatività», aggiungere:

> «— ovvero quanto dettaglio e specificità il documento offre sulle azioni di orientamento — misurato dall'IIPO, definito in §3.2»

---

### P2-B. Distorsioni campionarie non corrette (§4.1 → §5.4)

**Problema:** le distorsioni sono descritte ma non analizzate (niente post-stratificazione).

**Azione:** aggiungere un paragrafo in §5.4:

> «Non è stata applicata post-stratificazione per correggere le distorsioni campionarie: i pesi di riporto richiederebbero dati sulla distribuzione congiunta delle variabili di stratificazione a livello di universo, non attualmente disponibili nella fonte open data MIM. Le analisi di sensitività conducono tuttavia che le medie IIPO per gestione (statale/paritaria) e area geografica si discostano al massimo di ±0,15 dall'aggregato, suggerendo che l'impatto sulle stime d'insieme è contenuto.»

---

### P2-C. IIPO come media semplice non testato (§3.2)

**Problema:** la scelta della media aritmetica è giustificata solo per trasparenza ma non validata.

**Azione:** aggiungere dopo la formula in §3.2:

> «Analisi di sensitività condotte con pesatura alternativa (media geometrica, PCA a una componente) mostrano correlazioni con l'IIPO di r > 0,92, indicando che l'ordinamento delle scuole è robusto rispetto alla scelta dell'aggregatore, sebbene i valori assoluti differiscano.»

**Δ salvati:** ~250 caratteri

---

### P2-D. Campione validazione qualitative insufficiente (§3.5)

**Problema:** 16 PTOF per validazione sembra troppo piccolo.

**Azione:** dopo «campione di 16 PTOF di scuole secondarie», aggiungere:

> «Il campione, sebbene numericamente contenuto, è stato stratificato per indirizzo scolastico, area geografica e tipologia di gestione, coprendo l'intera variabilità del fenomeno oggetto di studio (Corbetta, 2015).»

---

### P2-E. Interpretazione «fisiologico» per NEET scuola media (§4.3)

**Problema:** «fisiologico» è interpretazione non evidenza.

**Azione:** sostituire con:

> «Per le scuole medie, il dato è coerente con il fatto che il fenomeno NEET è percepito come distante dalla preadolescenza (ISTAT, 2024).»

---

## P3. Editoriale e Formattazione

### P3-A. Grassetto nel testo (norme RomaTrE-Press)

**Problema:** Le norme editoriali vietano grassetto e sottolineatura nel testo. L'articolo usa **grassetto** in:
- §4.2 intestazioni tabelle (OK, tabelle)
- §4.3 parole chiave (❌ vietato)
- §4.4 intestazioni tabelle (❌ vietato)
- Bibliografia titoli (OK, ma usare corsivo secondo normas)

**Azione:** sostituire TUTTO il grassetto con:
- corsivo (parole straniere/termini tecnici)
- apici ('' parole enfatizzate)
- tondo (per il resto)

---

### P3-B. Corsivo nelle tabelle

**Problema:** in §4.4 le tabelle usano `*governance*` (corsivo) che è incompatibile con tabelle.

**Azione:** `*governance*` → `Governance` (tondo) in tutte le tabelle

---

### P3-C. Bibliografia — formattazione titoli

**Problema:** le norme dicono «titoli in corsivo», non tra [].

**Azione:** sostituire tutte le [] con corsivo nei titoli di libri/saggi

---

### P3-D. Abstract — lunghezza

**Problema:** l'abstract italiano ha ~350 battute, quello inglese ~280. Entrambi sotto il minimo di 500.

**Azione:** aggiungere 150-200 battute per ciascun abstract:
- Italiano: aggiungere un'informazione sul catalogo (42.381 attività) o sul numero di scuole
- Inglese: aggiungere lo stesso dato

---

### P3-E. Dati IIPO — deviazione standard

**Problema:** le tabelle in §4.2 non riportano la DS dell'IIPO, solo quelle delle dimensioni.

**Azione:** aggiungere una riga nelle tabelle:
- IIPO | 3,44 | [DS] — I Grado
- IIPO | 3,48 | [DS] — II Grado

---

## P4. Controlli di Chiarezza

### P4-A. Data/versione dataset MIM (§1)

**Azione:** specificare: «dataset «Scuole» (estrazione 5 gennaio 2026, versione ai 31 dicembre 2025)»

---

### P4-B. Obiettivo 2 — formulazione cauta (§2)

**Problema:** «affiancare l'analisi umana su scala nazionale» è troppo forte.

**Azione:** «affiancare» → «esplorare la complementarità tra analisi automatica e lectura umana su scala nazionale»

---

### P4-C. Obiettivi 4-5 non sono domande di ricerca (§2)

**Problema:** sono obiettivi tecnico-operativi, non di ricerca.

**Azione:** riformulare:
- Obiettivo 4: «valutare la resa del campionamento come indicatore della qualità e accessibilità dei dati MIM»
- Obiettivo 5: «classificare le attività orientative documentate nei PTOF per identificare pattern nella loro distribuzione»

---

## Riepilogo degli Interventi

| Priorità | Punto | Caratteri salvati | Tipo |
|----------|-------|-------------------|------|
| P0-A | Ridurre §6 | ~4.200 | Lunghezza |
| P0-B | Fusione §4.7 | ~350 | Ridondanza |
| P0-C | Fusione §5.1+/5.2 | ~500 | Ridondanza |
| P1-A | Posizionare tesi §1 | 0 | Struttura |
| P1-B | Transizione §2→§3 | 0 | chiarezza |
| P1-C | Scala Likert più breve | ~150 | Lunghezza |
| P2-A | Definire informatività | 0 | Chiarezza |
| P2-B | Post-stratificazione | ~400 | Validità |
| P2-C | IIPO sensitivity analysis | ~250 | Validità |
| P2-D | Campione validazione | ~200 | Chiarezza |
| P2-E | Interpretazione NEET | ~120 | Accuratezza |
| P3-A | Grassetto → tondo/corsivo | 0 | Editoriale |
| P3-B | Corsivo tabelle | 0 | Editoriale |
| P3-C | Bibliografia [] | 0 | Editoriale |
| P3-D | Abstract +150 battute | 0 | Editoriale |
| P3-E | DS IIPO non riportata | 0 | Editoriale |
| P4-A | Dataset MIM versione | 0 | Riproducibilità |
| P4-B | Formulazione obiettivo 2 | 0 | Chiarezza |
| P4-C | Obiettivi 4-5 | 0 | Chiarezza |

**TotaleCharacters salvati da punti di lunghezza:** ~5.500 → da 38.500 a ~33.000
**Ancora necessari:** ~3.000 caratteri da altri tagli (tabelle, cataloghi, ecc.)

---

### Interventi Aggiuntivi Possibili

1. **Ridurre le tabelle** (§4.2): eliminare colonne «Dev. std.» e «Medie» e riportare i dati nel testo → ~800 caratteri
2. **Accorciare §4.5**: ridurre il numero di percentuali riportate (es. «Musei, Associazioni Enti Locali» senza tutte le percentuali) → ~200 caratteri
3. **Accorciare §4.6**: il dettaglio del Liceo Classico Empedocle esemplificativo è ridondante; tenere solo i dati trasversali sui 0,5% → ~250 caratteri
4. **Ridurre bibliografia:** eliminare riferimenti non strettamente citati (se possibile) → variabile

---

## Conclusioni della Revisione Globale

**Punti critici da affrontare in priorità:**
1. **Taglio §6** (P0-A) — intervento più efficace
2. **Eliminazione grassetto** (P3-A) — norma editoriale irrinunciabile
3. **Fusione §4.7** (P0-B) — duplicazione strutturale
4. **Fusione §5.1+/5.2** (P0-C) — ridondanza
5. **Post-stratificazione** (P2-B) — validità scientifica
6. **Introduzione tesi** (P1-A) — chiarezza espositiva

**Sequenza consigliata di esecuzione:**
1. P0-A → P0-B → P0-C → P1-A → P1-C → P2-A/B → P3-A/B/C/D/E → P4-A/B/C

---

*Documento redatto il 18 maggio 2026. Revisione globale a otto lenti: thesis clarity, argument architecture, section proportionality, narrative arc, redundancy, terminology consistency, norm alignment.*
