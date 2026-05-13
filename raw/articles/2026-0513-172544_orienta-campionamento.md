# ORIENTA+ | Campionamento

URL: https://orienta.ai4educ.org/Campionamento
Data: 2026-05-13T17:25:44.090043

---

Navigazione

📘 PROGETTO

Progetto

▸ Campionamento

Documentazione

📊 ANALISI

KPI

Territorio

Dimensioni

Analisi Statistiche

Analytics

🌟 ESPLORAZIONE

Scuola

Attività

Report

Metodologie e Progetti

Impatto Metodologie e Progetti

🎓 SERVIZI

Invio

Verifica

Revisione

🛠️ ADMIN

Amministrazione

Login Admin

Password

Accedi

📊 Campionamento e Bilanciamento

Metodologia di campionamento stratificato e report di estrazione PTOF

📖 Metodologia

📊 Analisi e Copertura

📚 Nota Tecnica

📖 Metodologia di Campionamento
Obiettivo del Campionamento

Il campionamento è stato progettato per ottenere un campione rappresentativo delle scuole italiane di ogni ordine e grado, garantendo:

✅ Copertura territoriale di tutte le regioni italiane
✅ Rappresentatività di tutti gli ordini scolastici (Infanzia, Primaria, I e II Grado)
✅ Inclusione sia di scuole statali che paritarie
✅ Equilibrio tra aree metropolitane e non metropolitane
Procedura di Campionamento Stratificato

Il campionamento segue un approccio stratificato multi-stage:

🔹 Fase 1: Definizione degli Strati

Ogni scuola è classificata in uno strato definito da:

Dimensione	Categorie
Gestione	Statale, Paritaria
Area Geografica	Nord Ovest, Nord Est, Centro, Sud, Isole
Territorio	Metropolitano, Non Metropolitano
Ordine	Infanzia, Primaria, Sec. Primo, Sec. Secondo, Altro

Questo genera 2 × 5 × 2 × 5 = 100 strati potenziali

🔹 Fase 2: Estrazione Proporzionale

Da ogni strato viene estratto un numero di scuole proporzionale alla sua dimensione:

n_strato = (N_strato / N_totale) × n_campione_target

Dove:

N_strato = numero scuole nello strato
N_totale = numero scuole nella popolazione
n_campione_target = dimensione campione desiderata
🔹 Fase 3: Estrazione Automatica PTOF

Per ogni scuola selezionata:

Ricerca URL PTOF sul sito istituzionale della scuola
Download automatico del documento PDF
Conversione in Markdown per l'analisi testuale
Analisi AI per l'estrazione delle dimensioni dell'orientamento

⚠️ Fallimenti: Se il PTOF non è reperibile automaticamente, la scuola viene registrata come "fallimento" e può essere gestita con procedura manuale.

🔹 Fase 4: Validazione e Controllo Qualità
Verifica della completezza dei dati estratti
Controllo della coerenza dei punteggi
Eventuale revisione manuale per casi dubbi
🔹 Fase 5: Pulizia e Standardizzazione dei Codici

Al termine del Ciclo 53 di estrazione, è stata eseguita una procedura di bonifica massiva per garantire la qualità del dataset:

Riconciliazione Codici: Verifica della corrispondenza tra il codice meccanografico nel nome del file e quello contenuto nel testo del PTOF.
Rimozione "Impostori": Eliminazione automatica di file che, pur avendo un nome valido, contenevano dati di altre scuole (spesso dovuto a errori di pubblicazione sui siti scolastici).
Standardizzazione: Eliminazione di tutti i file orfani o incompleti per garantire che ogni scuola nel dataset finale abbia la catena completa: PDF → Markdown → Analisi → Attività.

Questo processo ha comportato la rimozione di circa 300+ entry non valide, migliorando significativamente l'affidabilità delle analisi statistiche.

📈 Report dei Cicli di Estrazione

Cicli Completati

78

Scuole Selezionate (Totale)

15,035

PTOF Scaricati (Totale)

3,082

Resa Globale

54.1%

keyboard_arrow_right

📋 Ciclo 1 - 2026-01-05

keyboard_arrow_right

📋 Ciclo 2 - 2026-01-21

keyboard_arrow_right

📋 Ciclo 3 - 2026-01-22

keyboard_arrow_right

📋 Ciclo 4 - 2026-01-22

keyboard_arrow_right

📋 Ciclo 5 - 2026-01-25

keyboard_arrow_right

📋 Ciclo 6 - 2026-01-25

keyboard_arrow_right

📋 Ciclo 7 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 8 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 9 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 10 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 11 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 12 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 13 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 14 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 15 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 16 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 17 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 18 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 19 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 20 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 21 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 22 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 23 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 24 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 25 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 26 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 27 - 2026-01-26

keyboard_arrow_right

📋 Ciclo 28 - 2026-01-27

keyboard_arrow_right

📋 Ciclo 29 - 2026-01-27

keyboard_arrow_right

📋 Ciclo 30 - 2026-01-27

keyboard_arrow_right

📋 Ciclo 31 - 2026-01-27

keyboard_arrow_right

📋 Ciclo 32 - 2026-01-27

keyboard_arrow_right

📋 Ciclo 33 - 2026-01-27

keyboard_arrow_right

📋 Ciclo 34 - 2026-01-28

keyboard_arrow_right

📋 Ciclo 35 - 2026-01-28

keyboard_arrow_right

📋 Ciclo 36 - 2026-01-28

keyboard_arrow_right

📋 Ciclo 37 - 2026-01-28

keyboard_arrow_right

📋 Ciclo 38 - 2026-01-28

keyboard_arrow_right

📋 Ciclo 39 - 2026-01-29

keyboard_arrow_right

📋 Ciclo 40 - 2026-01-29

keyboard_arrow_right

📋 Ciclo 41 - 2026-01-29

keyboard_arrow_right

📋 Ciclo 42 - 2026-01-29

keyboard_arrow_right

📋 Ciclo 43 - 2026-01-29

keyboard_arrow_right

📋 Ciclo 44 - 2026-01-29

keyboard_arrow_right

📋 Ciclo 45 - 2026-01-30

keyboard_arrow_right

📋 Ciclo 46 - 2026-01-30

keyboard_arrow_right

📋 Ciclo 47 - 2026-01-30

keyboard_arrow_right

📋 Ciclo 48 - 2026-01-30

keyboard_arrow_right

📋 Ciclo 49 - 2026-01-30

keyboard_arrow_right

📋 Ciclo 50 - 2026-01-30

keyboard_arrow_right

📋 Ciclo 51 - 2026-01-31

keyboard_arrow_right

📋 Ciclo 52 - 2026-01-31

keyboard_arrow_right

📋 Ciclo 53 - 2026-01-31

keyboard_arrow_right

📋 Ciclo 54 - 2026-01-31

keyboard_arrow_right

📋 Ciclo 55 - 2026-01-31

keyboard_arrow_right

📋 Ciclo 56 - 2026-01-31

keyboard_arrow_right

📋 Ciclo 57 - 2026-02-01

keyboard_arrow_right

📋 Ciclo 58 - 2026-02-01

keyboard_arrow_right

📋 Ciclo 59 - 2026-02-01

keyboard_arrow_right

📋 Ciclo 60 - 2026-02-01

keyboard_arrow_right

📋 Ciclo 61 - 2026-02-01

keyboard_arrow_right

📋 Ciclo 62 - 2026-02-02

keyboard_arrow_right

📋 Ciclo 63 - 2026-02-02

keyboard_arrow_right

📋 Ciclo 64 - 2026-02-05

keyboard_arrow_right

📋 Ciclo 65 - 2026-02-05

keyboard_arrow_right

📋 Ciclo 66 - 2026-02-05

keyboard_arrow_right

📋 Ciclo 67 - 2026-02-05

keyboard_arrow_right

📋 Ciclo 68 - 2026-02-05

keyboard_arrow_right

📋 Ciclo 69 - 2026-02-05

keyboard_arrow_right

📋 Ciclo 70 - 2026-02-05

keyboard_arrow_right

📋 Ciclo 71 - 2026-02-07

keyboard_arrow_right

📋 Ciclo 72 - 2026-02-08

keyboard_arrow_right

📋 Ciclo 73 - 2026-02-11

keyboard_arrow_right

📋 Ciclo 74 - 2026-02-11

keyboard_arrow_right

📋 Ciclo 75 - 2026-02-11

keyboard_arrow_right

📋 Ciclo 76 - 2026-02-11

keyboard_arrow_right

📋 Ciclo 77 - 2026-02-13

keyboard_arrow_right

📋 Ciclo 78 - 2026-02-13

🧭 ORIENTA+
Piattaforma di Analisi della Robustezza dell'Orientamento nei PTOF • Sviluppato da Daniele Dragoni — Dottorando, Università Roma Tre • 📧 daniele.dragoni@uniroma3.it
Quest'opera è distribuita con Licenza Creative Commons Attribuzione - Non commerciale - Non opere derivate 4.0 Internazionale • ORIENTA+ è un marchio registrato.