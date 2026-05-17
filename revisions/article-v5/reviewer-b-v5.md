---
reviewer: "B — Il Teorico"
article: articles/article-v5-2026-05-14-1427.md
version: v5
created: 2026-05-14
persona: "Broad-view, theory-focused. Focus: literature positioning, argument coherence, contribution clarity, writing quality."
---

# Reviewer B Report — Il Teorico

## Overall Assessment

L'articolo affronta un tema di grande rilevanza — l'analisi automatica delle pratiche di orientamento nei PTOF — con un impianto argomentativo chiaro e una scrittura mediamente curata. L'arco narrativo è ben costruito: dal problema (scala dell'analisi manuale) alla soluzione (ORIENTA+) ai risultati (fotografia nazionale) alle implicazioni (policy). La collocazione nel PRIN dà solidità istituzionale al contributo.

Segnalo tuttavia alcune criticità. La principale è che il contributo specifico dell'articolo — oltre alla descrizione della piattaforma — non è sempre nitido: in più punti il testo oscilla tra il paper metodologico (presentazione di uno strumento) e il paper empirico (presentazione di risultati). Questa duplice natura andrebbe resa esplicita e governata. In secondo luogo, il posizionamento nella letteratura è debole: le citazioni ci sono, ma manca un vero dialogo con la ricerca precedente su analisi automatica di documenti scolastici, su LLM per policy analysis, su orientamento comparato. In terzo luogo, alcune sezioni sono ridondanti (§3.6 e §4.7) e altre troppo compresse (la discussione teorica sulla frammentazione meriterebbe più spazio).

Il mio giudizio complessivo è: **accettabile con revisioni maggiori**, con priorità sul rafforzamento del posizionamento teorico e sulla riduzione delle ridondanze.

---

## §1 — Introduzione

### Comments
1. **Riga 13**: l'apertura sul quadro normativo è efficace ma troppo lunga (quasi un terzo dell'introduzione). La progressione normativa CM 43/2009 → Nota 4232/2014 → D.M. 328/2022 è corretta ma rischia di appesantire l'incipit. Suggerirei di sintetizzare in 2-3 righe e anticipare prima il problema analitico.
2. **Riga 15**: «Tuttavia, l'analisi su larga scala presenta difficoltà considerevoli» — il connettivo «Tuttavia» è debole come transizione dal quadro normativo al problema tecnico. Il nesso logico è: la norma richiede documentazione → analizzare quella documentazione su scala nazionale è tecnicamente proibitivo. Questo nesso andrebbe esplicitato.
3. **Riga 17**: «nuove tecnologie di intelligenza artificiale» è vago. In un articolo che nomina modelli specifici (Gemini, GLM, Qwen), l'introduzione dovrebbe già parlare di LLM, non di IA generica.
4. **Riga 19**: «L'obiettivo è mostrare come l'analisi automatica possa restituire una fotografia comparabile su scala nazionale» — la tesi è implicita ma non esplicitata. Qual è il contributo specifico? Che l'analisi automatica è fattibile? Che produce dati utilizzabili? Che rivela pattern non visibili con metodi tradizionali? La contribution statement andrebbe resa più netta.
5. **Riga 20**: «l'indice non giudica la qualità di una scuola, ma la completezza con cui essa documenta» — questa distinzione è teoricamente importante (distingue documentazione da pratica) ma appare come un inciso, non come un punto architetturale dell'argomento.
6. **Riga 21**: il posizionamento nel PRIN è liquidato in due righe a fondo introduzione. Meritava di essere anticipato e argomentato: perché il PRIN? Cosa aggiunge il contesto PRIN alla rilevanza del contributo?

### Flagged Issues
- [Narrative] Apertura normativa troppo estesa, rallenta l'incipit (riga 13)
- [Argument] Transizione norma→problema tecnico debole (riga 15)
- [Clarity] «Intelligenza artificiale» troppo generico, servirebbe «LLM» (riga 17)
- [Contribution] Tesi implicita, manca una contribution statement esplicita (riga 19)
- [Argument] Distinzione documentazione/pratica non valorizzata come punto architetturale (riga 20)
- [Narrative] Posizionamento PRIN confinato all'ultimo paragrafo (riga 21)

---

## §2 — Obiettivi della ricerca

### Comments
1. **Riga 25**: «L'obiettivo generale di questo lavoro è sviluppare e validare una metodologia automatica» — formulazione chiara ma l'ordine «sviluppare e validare» suggerisce due contributi distinti (design + valutazione). L'articolo tuttavia presenta anche risultati descrittivi sostanziali (la fotografia dell'orientamento in Italia), che non sono catturati da questa formulazione.
2. **Riga 27–35**: i cinque obiettivi specifici sono ben enumerati ma mescolano piani diversi: Ob 1 e 2 sono obiettivi di design, Ob 3 e 4 sono obiettivi di misurazione, Ob 5 è un obiettivo descrittivo/catalografico. La progressione logica non è lineare. Suggerirei: (1) framework, (2) pipeline/indice, (3) validazione, (4) applicazione al campione, (5) catalogo. L'ordine attuale (framework→pipeline→indice→test→catalogo) è accettabile ma il catalogo come Ob 5 appare scollegato dagli altri.
3. **Riga 31**: l'Ob 3 parla di «verificare la capacità dell'indice di discriminare tra diversi profili di documentazione» — questa è un'ipotesi testabile, ma non viene più ripresa esplicitamente nei risultati. La verifica è lasciata implicita nell'analisi cluster.
4. **Riga 33**: l'Ob 4 «misurando la resa del campionamento e del download» è un obiettivo operativo, debole come obiettivo di ricerca. Suggerirei di riformularlo in termini di «identificare pattern territoriali, dimensionali e tipologici nelle pratiche di orientamento documentate» — che è la parte sostanziale.
5. **Generale**: gli obiettivi non fanno riferimento alla letteratura. Non si capisce cosa distingua questo studio da tentativi precedenti di analisi automatica di documenti scolastici (se esistono) o di analisi dei PTOF con metodi tradizionali (se esistono).

### Flagged Issues
- [Contribution] Obiettivo generale non cattura la componente descrittiva dei risultati (riga 25)
- [Argument] Progressione logica degli obiettivi non lineare; Ob 5 scollegato (righe 27-35)
- [Argument] Ipotesi di discriminazione dell'IIPO non ripresa nei risultati (riga 31)
- [Clarity] Ob 4 formulato come task operativo, non come obiettivo di ricerca (riga 33)
- [Literature] Obiettivi non posizionati rispetto alla letteratura esistente (righe 25-35)

---

## §3.1 — Campionamento

### Comments
1. **Riga 41**: il campionamento stratificato è metodologicamente solido. Le citazioni di Cochran e Lohr sono appropriate anche se classiche — il lettore si aspetterebbe anche un riferimento più recente o applicato al contesto scolastico italiano.
2. **Riga 43**: «78 cicli di estrazione iterativi» — la metafora è efficace ma la prosa diventa tecnica. Sarebbe utile una frase che spieghi *perché* sono stati necessari 78 cicli, non solo *che* sono stati fatti.
3. **Riga 46**: la narrazione degli «impostori» è vivace e una delle parti meglio scritte dell'articolo. Il termine è efficace senza essere gergale.
4. **Riga 45–47**: la catena numerica 15.035→9.984→5.399→3.082→2.584→2.095→939 è informativa ma rischia di sommergere il lettore. Suggerirei una flow qualche rappresentazione visiva (diagramma di flusso) o almeno una tabella riepilogativa.

### Flagged Issues
- [Literature] Riferimenti solo classici (Cochran 1977, Lohr 2010), manca letteratura recente su campionamento in contesti educativi (riga 41)
- [Narrative] Catena numerica densa, rischia di perdere il lettore (righe 45-47)

---

## §3.2 — Framework di analisi

### Comments
1. **Riga 51**: «in coerenza con il questionario nazionale della Macro-Azione 1 del PRIN» — questo è l'unico riferimento alla genesi del framework. È sufficiente per il lettore informato, ma il lettore esterno al PRIN non sa cosa contenga quel questionario. Una nota o un rinvio sarebbero utili.
2. **Riga 53**: la scala Likert 1–7 con ancore semantiche è ben costruita e chiara. Tuttavia, il passaggio da 1 a 7 con sette descrittori rischia di suggerire una precisione che la misura non ha: la distanza tra «assente» e «generico» è la stessa che tra «ottimo» ed «eccellente»? Una discussione sulla natura ordinale vs. intervalare della scala sarebbe preziosa.
3. **Riga 57–61**: la discussione sull'IIPO e il caveat compensazione è onesta e ben argomentata. È uno dei punti di forza teorici dell'articolo: l'indice sintetico non è mitizzato ma problematizzato.
4. **Generale**: manca un confronto con altri framework di analisi delle pratiche orientative. Esistono griglie di valutazione dei PTOF nella letteratura italiana? Check-list ministeriali? Sistemi di accreditatione? Il framework ORIENTA+ andrebbe posizionato rispetto a questi.

### Flagged Issues
- [Literature] Framework non posizionato rispetto ad altri strumenti di analisi dei PTOF (riga 51)
- [Argument] Natura ordinale vs. intervalare della scala Likert non discussa (riga 53)

---

## §3.3 — Pipeline multi-agente

### Comments
1. **Riga 65**: «*pipeline* — una catena di elaborazione in cui ciascun passaggio riceve l'output del precedente» — la definizione tra trattini è didascalica ma utile per il lettore non tecnico. Tuttavia, lo stesso termine è già stato introdotto nell'abstract senza definizione.
2. **Riga 65**: la descrizione dei quattro agenti (Analyst→Reviewer→Refiner→Background Reviewer) è chiara. Il Background Reviewer come quarto agente separato è una scelta architetturale interessante che meriterebbe una giustificazione: perché non è integrato nel Reviewer?
3. **Riga 69**: la *dashboard* è citata en passant. Se è uno degli output della piattaforma, meriterebbe una menzione più sostanziale — cosa mostra? A chi è destinata?

### Flagged Issues
- [Clarity] Termine *pipeline* definito due volte (abstract e §3.3) (riga 65)
- [Argument] Ruolo del Background Reviewer non giustificato teoricamente (riga 65)
- [Narrative] Dashboard menzionata senza descrizione (riga 69)

---

## §3.4 — Controlli di qualità

### Comments
1. **Riga 73**: «revisione non-PTOF» tra virgolette alte — le norme editoriali prescrivono caporali per i termini tecnici. Verificare coerenza con il resto dell'articolo.
2. **Riga 75**: la descrizione delle tre fasi di generazione report è tecnicamente densa. Il termine *placeholder* in corsivo è corretto, ma RAG (*Retrieval-Augmented Generation*) andrebbe espanso alla prima occorrenza.
3. **Generale**: la sezione è breve e funzionale. Tuttavia, esclusa la parte tecnica, non emerge il *perché* di questi controlli nel quadro dell'argomentazione complessiva.

### Flagged Issues
- [Clarity] Uso incoerente delle virgolette per «revisione non-PTOF» (riga 73)
- [Clarity] RAG non espanso alla prima occorrenza (riga 75)

---

## §3.5 — Elaborazione dei dati

### Comments
1. **Riga 79**: «I 3.082 PTOF sono stati convertiti da PDF a Markdown» — 3.082 è il totale istituti unici, non il numero di PTOF analizzati (che sono 2.095 o 939). La cifra è corretta nel contesto ma potenzialmente fuorviante senza il riferimento al campione finale.
2. **Riga 81**: la descrizione del catalogo è densa di informazioni ma compressa. I tre livelli di classificazione (6 categorie, 18 tipologie, 22 ambiti) sono elencati senza la sistematicità che meriterebbero. Una tabella riassuntiva sarebbe più efficace del testo continuo.

### Flagged Issues
- [Clarity] Cifra 3.082 potenzialmente fuorviante senza contesto (riga 79)
- [Narrative] Catalogo descritto in modo compresso, meriterebbe una tabella (riga 81)

---

## §3.6 — Validazione della piattaforma

### Comments
1. **Riga 87**: «La validazione di ORIENTA+ è stata condotta su due livelli complementari» — l'impianto è chiaro ma il paragrafo è lungo e denso. Suggerirei di separare i due livelli in capoversi distinti.
2. **Riga 87**: la lettura umana è descritta come «indipendente» ma condotta da De Nardo, che appartiene alla stessa unità PRIN (Roma Tre). L'indipendenza andrebbe qualificata (indipendente dalla pipeline, non dal progetto).
3. **Riga 89**: la validazione tecnica descrive un processo (versionamento, issue tracking) con un linguaggio che sfiora l'autopromozionale: «consolidando la robustezza operativa del sistema». «Robustezza» è una categoria valutativa; in un articolo che ha sistematicamente rimosso il linguaggio valutativo, questa occorrenza stride.

### Flagged Issues
- [Narrative] Paragrafo unico troppo denso, separare i due livelli (riga 87)
- [Clarity] «Indipendente» non qualificato (riga 87)
- [Terminology] «Robustezza operativa» — linguaggio valutativo, incoerente con il registro descrittivo dell'articolo (riga 89)

---

## §4.1 — Copertura campionaria

### Comments
1. **Riga 93**: «A valle del processo di campionamento, validazione e pulizia descritto nel §3.1» — buon rinvio interno, mantiene la continuità narrativa.
2. **Riga 97**: la descrizione delle distorsioni è trasparente e ben scritta. Le implicazioni interpretative (paritarie → Governance/ Opportunità sovrastimate, Sud → enfasi NEET) sono pertinenti e mostrano consapevolezza critica.
3. **Riga 99**: la chiusura «i risultati vanno pertanto letti come tendenze significative all'interno del perimetro osservato» è cauta e appropriata. Tuttavia, è una litote: sarebbe più efficace affermare positivamente cosa i dati *possono* dire, non solo cosa *non possono*.

### Flagged Issues
- [Narrative] Chiusura in negativo (cosa i dati non possono dire) invece che in positivo (riga 99)

---

## §4.2 — Sintesi quantitativa

### Comments
1. **Riga 103–129**: le tabelle sono chiare e ben formattate. L'IIPO medio 3,44–3,48 è un dato centrale che struttura l'intera discussione.
2. **Riga 115, 127**: le deviazioni standard sono riportate ma non commentate. La variabilità è un dato informativo quanto la media — meriterebbe almeno una frase.
3. **Riga 129**: l'interpretazione del dato Strutturale è una delle più interessanti dell'articolo: «le scuole documentano cosa fanno e come si organizzano, ma non hanno ancora formalizzato una sezione autonoma». È un'interpretazione che lega il dato alla norma (D.M. 328/2022) in modo efficace.

### Flagged Issues
- [Narrative] Deviazioni standard riportate ma non commentate (righe 115, 127)

---

## §4.3 — Analisi dei sotto-indicatori

### Comments
1. **Riga 135–139**: l'analisi dei sotto-indicatori è una delle sezioni più incisive. Il contrasto Alleanza Famiglie (4,05) vs. Monitoraggio (2,79) è raccontato con efficacia.
2. **Riga 137**: il dato NEET nel I Grado (2,04) commentato come «fisiologico» — il termine è appropriato nel registro medico-sociale ma andrebbe glossato per il lettore non italiano (il dato è «atteso» o «comprensibile» data l'età degli studenti).
3. **Riga 139**: Opportunità Formative «non è ancora pienamente integrata nella strategia orientativa» — questa è un'interpretazione, non un dato. La sezione risultati dovrebbe limitarsi a descrivere; l'interpretazione va nella discussione.

### Flagged Issues
- [Clarity] «Fisiologico» potrebbe non essere chiaro al lettore internazionale (riga 137)
- [Argument] Sconfinamento interpretativo nei risultati (riga 139)

---

## §4.4 — Profili cluster

### Comments
1. **Riga 141–165**: le tabelle dei cluster sono il cuore empirico dell'articolo. La nomenclatura dei cluster (Approccio integrato e curricolare, Benessere e accoglienza, Dichiarativo formale, ecc.) è evocativa e ben calibrata.
2. **Riga 154, 165**: la riga 154 ha un refuso: «*governance* in uscita con bassa strutturazione» e «*governance* con bassa strutturazione» — il corsivo su *governance* è corretto (termine straniero), ma l'espressione «con bassa strutturazione» è ricorrente e rischia di diventare formula.
3. **Riga 165**: «in entrambi i gradi il cluster maggioritario è caratterizzato da un'«elevata frammentazione operativa»» — l'uso di caporali dentro caporali (la citazione è già tra caporali) crea un problema tipografico. Le norme prescrivono apici alti dentro caporali.
4. **Generale**: manca una discussione dei cluster come tipologia, non solo come elenco. C'è una gerarchia? I cluster sono ordinabili per «qualità» della documentazione? Questo appartiene alla discussione ma andrebbe almeno accennato qui.

### Flagged Issues
- [Terminology] «Con bassa strutturazione» formula ricorrente (righe 154, 165)
- [Norms] Caporali dentro caporali — servono apici alti (riga 165)
- [Narrative] Cluster presentati come elenco, non come tipologia ordinabile (righe 141-165)

---

## §4.5 — Reti territoriali e metodologie didattiche

### Comments
1. **Riga 169**: la lista di partnership è informativa ma presentata come enumerazione. Una tabella o un grafico sarebbero più efficaci per il confronto I Grado vs. II Grado.
2. **Riga 171**: la discussione su STEM vs. Laboratorio è acuta: «la distanza tra l'etichetta 'STEM' e la specifica voce 'Laboratorio' suggerisce che la dicitura venga applicata in modo estensivo». Buona analisi critica.
3. **Riga 171**: «Alternanza Scuola-Lavoro» nel 24,4% dei PTOF — questo è un dato culturale prima che statistico, ed è presentato con il giusto rilievo.

### Flagged Issues
- [Narrative] Partnership presentate come enumerazione, non come confronto strutturato (riga 169)

---

## §4.6 — Catalogo delle attività

### Comments
1. **Riga 175**: questa sezione è una delle più ricche ma anche una delle più compresse. I tre livelli di classificazione (6 categorie, 18 tipologie, 22 ambiti) sono una tassonomia complessa che meriterebbe uno spazio dedicato, possibilmente con una tabella o un diagramma.
2. **Riga 177**: l'esempio del Liceo Empedocle di Agrigento è ben scelto: dà concretezza a una sezione altrimenti astratta. Tuttavia, è l'unico esempio — un secondo caso (es. un istituto tecnico) rafforzerebbe la rappresentatività.
3. **Riga 179**: il dato 0,5% AI è presentato come «assenza significativa» — è una delle osservazioni più interessanti dell'articolo ma è liquidato in una frase. Meritava di essere sviluppato: perché l'AI è assente? Cosa implica per il futuro dell'orientamento?
4. **Generale**: il catalogo è presentato come Obiettivo 5 ma la sua collocazione nei risultati (§4.6) è ambigua: è un output della piattaforma (quasi un prodotto) o un risultato di ricerca? La distinzione andrebbe chiarita.

### Flagged Issues
- [Narrative] Tassonomia a tre livelli troppo compressa, meriterebbe spazio dedicato (riga 175)
- [Narrative] Un solo esempio (Liceo Empedocle), utile un secondo caso (riga 177)
- [Argument] Dato 0,5% AI interessante ma non sviluppato (riga 179)
- [Contribution] Natura del catalogo (prodotto vs. risultato) ambigua (generale)

---

## §4.7 — Convergenza tra lettura umana e analisi automatica

### Comments
1. **Riga 183**: questa sezione è sostanzialmente una duplicazione del §3.6 (validazione qualitativa). Le stesse informazioni — convergenza, assenza di contraddizioni, complementarità — appaiono in entrambe le sezioni con formulazioni quasi identiche. Una delle due va tagliata o radicalmente differenziata.
2. **Riga 183**: «Questa complementarità conferma la validità dell'approccio misto e suggerisce che l'integrazione tra lettura qualitativa e analisi automatica costituisca una direzione promettente» — questa è la conclusione più importante della validazione ma arriva in coda a una sezione ridondante. Andrebbe valorizzata.

### Flagged Issues
- [Argument] Duplicazione sostanziale con §3.6 (riga 183)
- [Narrative] Conclusione più importante della validazione relegata in coda (riga 183)

---

## §5 — Discussione

### Comments
1. **Riga 185–237**: la discussione è ben strutturata in cinque sottosezioni che affrontano temi distinti. L'organizzazione è logica e la progressione è chiara.
2. **§5.1** (riga 187–195): il divario documento/pratica è il tema teoricamente più ricco. L'aggancio a Fiorin (2019) è pertinente ma la discussione rimane sul piano dell'evidenza empirica, senza sviluppare le implicazioni teoriche. Cosa significa per la teoria dell'orientamento che le scuole documentino in modo dichiarativo?
3. **§5.2** (riga 197–205): la metafora dell'orientamento «ovunque e da nessuna parte» è efficace. Il parallelo con Cavalli e Argentin (2010) e Colombo (2021) sul meccanismo di «innesto senza revisione strutturale» è teoricamente fondato. È uno dei punti più forti dell'articolo.
4. **§5.3** (riga 207–215): le tre criticità sistemiche sono ben individuate ma il trattamento è descrittivo. Manca un'affermazione forte su *quale* di queste tre criticità sia la più urgente o la più sorprendente.
5. **§5.4** (riga 217–227): i quattro limiti sono onesti e ben articolati. La progressione (rappresentatività → compensazione → LLM → distanza documento/pratica) è logica. Il quarto limite («la distanza tra documento e pratica resta il confine epistemologico più difficile da superare») è formulato in modo eccellente.
6. **§5.5** (riga 229–237): le implicazioni per policy sono pertinenti ma generiche. «Un monitoraggio ministeriale mirato», «strumenti per un piano organico», «approfondire le determinanti» sono raccomandazioni ragionevoli ma non sorprendenti. Manca un'idea forte: cosa *solo* ORIENTA+ può dire che altri metodi non possono?

### Flagged Issues
- [Argument] §5.1 non sviluppa implicazioni teoriche del divario documento/pratica (righe 187-195)
- [Argument] §5.3 non priorizza le tre criticità (righe 207-215)
- [Contribution] §5.5 implicazioni generiche, manca il valore aggiunto specifico di ORIENTA+ (righe 229-237)

---

## §6 — Conclusioni

### Comments
1. **Riga 241**: «L'obiettivo era duplice: dimostrare la fattibilità tecnica [...] e restituire una fotografia comparabile» — questa è una buona sintesi ma l'articolo fa più di questo: offre un framework, un indice, un catalogo e una validazione. La conclusione sottovende il contributo.
2. **Riga 243**: «la pipeline a quattro agenti — Analyst, Reviewer, Refiner — si è rivelata in grado di processare 939 PTOF» — i quattro agenti sono enunciati ma ne vengono elencati solo tre. Refuso o omissione del Background Reviewer.
3. **Riga 247**: «Tre evidenze meritano di essere richiamate» — la numerazione è chiara e aiuta il lettore. Tuttavia, la terza evidenza (Strategie NEET) è presentata come fatto, non come risultato della ricerca: non c'è richiamo all'evidenza empirica (il punteggio 2,04–2,41).
4. **Riga 251**: «Ciononostante, ORIENTA+ dimostra che l'analisi automatica su larga scala della documentazione scolastica è possibile» — questa è una chiusura debole. Il contributo non è la dimostrazione di possibilità (già data dalla sola esistenza della piattaforma), ma l'evidenza prodotta e le implicazioni che ne derivano.
5. **Riga 253**: «L'orientamento non è un progetto tra gli altri: è la funzione che trasforma l'istruzione in progetto di vita. I PTOF delle scuole italiane iniziano a raccontarlo, ma devono ancora imparare a documentarlo.» — chiusura retoricamente molto efficace. Tuttavia, è più una massima che una conclusione scientifica. Andrebbe ancorata ai dati presentati.

### Flagged Issues
- [Contribution] Conclusioni sottovendono il contributo effettivo (riga 241)
- [Clarity] «Quattro agenti» ma ne elenca tre — refuso (riga 243)
- [Argument] Chiusura retorica non ancorata ai dati (riga 253)

---

## Narrative Arc Assessment

L'arco narrativo dell'articolo è complessivamente ben costruito:

- **Apertura** (§1): efficace. Il quadro normativo introduce il contesto, il problema tecnico (scala dell'analisi) crea tensione, ORIENTA+ è presentato come soluzione.
- **Gap** (§§1–2): il gap è implicito — nessuno ha mai analizzato i PTOF su scala nazionale con metodi automatici — ma non è mai dichiarato esplicitamente come gap di letteratura. Andrebbe formulato.
- **Metodo** (§3): denso ma chiaro. La progressione campionamento→framework→pipeline→qualità→elaborazione→validazione è logica.
- **Risultati** (§4): ricchi e ben organizzati. La sequenza copertura→sintesi→sotto-indicatori→cluster→reti→catalogo→validazione è esaustiva. Il §4.7 è ridondante con §3.6.
- **Discussione** (§5): ben strutturata. Il divario documento/pratica (§5.1) e la frammentazione (§5.2) sono i punti forti. I limiti (§5.4) sono onesti. Le implicazioni (§5.5) sono il punto più debole.
- **Conclusione** (§6): ben scritta ma sottodimensionata rispetto alla ricchezza dei risultati. La chiusura retorica è efficace ma andrebbe ancorata ai dati.

**Transizioni critiche:**
- §2→§3: ok, lineare.
- §3→§4: ok, il metodo prepara i risultati.
- §4.7→§5: debole. §4.7 è validazione, §5.1 è discussione — manca un ponte.
- §5→§6: la discussione prepara bene le conclusioni, ma §6 non riprende tutti i temi della discussione (es. le raccomandazioni di policy del §5.5 non sono richiamate).

---

## Bibliography Check

- **Copertura della letteratura**: le citazioni sono pertinenti ma il posizionamento è sbilanciato. La letteratura sull'orientamento (Fiorin, Colombo, Argentin, Cavalli) è ben rappresentata; la letteratura metodologica (Cochran, Lohr) è classica ma datata; manca completamente la letteratura su:
  - Analisi automatica di documenti educativi/policy con LLM
  - Usi di AI nell'orientamento scolastico
  - Validazione di strumenti automatici in contesti educativi
  - Letteratura internazionale sull'orientamento comparato
- **Rilevanza**: le 23 voci sono equilibrate tra normative (3), metodologiche (3), sostantive sull'orientamento (9), tecniche su AI/LLM (4), statistiche di contesto (2), report interni (1), manuali di ricerca sociale (1).
- **Sovracitazione**: nessuna. Ogni citazione ha una funzione.
- **Sottocitazione**: Fiorin (2019) è l'unico riferimento sulla funzione dichiarativa dei PTOF — la tesi è forte ma poggia su una fonte sola.
- **Assenti notevoli**: letteratura su IA e orientamento, su analisi automatica di documenti scolastici, su policy document analysis con metodi computazionali.

---

## Priority Ranking

1. **Critical** — Posizionamento nella letteratura debole: mancano riferimenti a letteratura su LLM per analisi documentale, AI nell'orientamento, policy document analysis. L'articolo non dialoga con i lavori esistenti al di fuori del perimetro PRIN.
2. **Critical** — Duplicazione §3.6/§4.7 sulla validazione. Una delle due sezioni va rimossa o radicalmente differenziata.
3. **High** — Tesi/contribution statement non esplicitata con chiarezza. L'articolo oscilla tra paper metodologico e paper empirico senza dichiarare la propria natura.
4. **High** — Catalogo (§4.6) come Obiettivo 5: natura ambigua (prodotto della piattaforma o risultato di ricerca?). La tassonomia a tre livelli meriterebbe più spazio.
5. **High** — Discussione (§5.5) generica nelle implicazioni. Manca il valore aggiunto specifico di ORIENTA+.
6. **Medium** — §5.1 non sviluppa implicazioni teoriche del divario documento/pratica oltre l'evidenza empirica.
7. **Medium** — Dato 0,5% AI nel catalogo (§4.6) suggerito ma non sviluppato.
8. **Medium** — Conclusioni (§6) sottodimensionate rispetto alla ricchezza dei risultati.
9. **Low** — Refuso «quattro agenti» ma ne elenca tre (§6, riga 243).
10. **Low** — Linguaggio valutativo residuo: «robustezza operativa» (§3.6, riga 89).
