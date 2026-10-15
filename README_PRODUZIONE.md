# La Bambola della Porta Accanto

Visual novel thriller psicologica realizzata con Ren'Py. La storia segue Mila, diciottenne che cerca di interpretare la propria famiglia, il rapporto ambiguo con Sophie e una serie di elementi che possono essere letti come prove oppure come sospetti. Le scelte registrano relazioni, oggetti, fonti consultate e disponibilità a chiedere aiuto.

## Stato dello sviluppo

**Stato: prototipo narrativo avanzato / pre-alpha, non ancora release-ready.**

Il progetto non è più una struttura da cinque capitoli: lo script corrente contiene un prologo giocabile, **nove capitoli numerati**, un epilogo incorporato nel percorso conclusivo e **quattro finali nominati**. Sono presenti variabili persistenti, scelte investigative, documenti consultabili, archivio degli indizi, fondali, audio e segnaposto sprite sostituibili.

Questa descrizione deriva da una revisione statica dei file su `main`. Non equivale a una sessione di gioco completa: prima di distribuire una build sono ancora necessari Ren'Py Lint, test runtime e verifica manuale di tutte le diramazioni.

## Struttura narrativa attuale

| Sezione | Titolo | Funzione narrativa |
|---|---|---|
| Prologo | — | Routine di Mila, dinamiche familiari, Kate e primo incontro con Sophie |
| Capitolo 1 | Come sanguina un robot | Dipendenza emotiva e primi segnali ambigui |
| Capitolo 2 | La geometria del silenzio | Isolamento, telefono e quaderno |
| Capitolo 3 | Frequenze d'ombra | Ricordi contraddittori e prime scelte investigative |
| Capitolo 4 | Radici di notte | Incontro notturno e aumento della tensione |
| Capitolo 5 | L'incisione profonda | Denaro, fotografia di famiglia e conseguenze delle scelte |
| Capitolo 6 | Il prezzo dell'argilla | Pressione, sospetti e costo delle decisioni |
| Capitolo 7 | Anatomia di un assedio | Conflitto familiare e possibilità di ascolto |
| Capitolo 8 | Natura morta con sedativi | Il flacone, il rischio immediato e la decisione di chiedere aiuto |
| Capitolo 9 | Il diorama di porcellana | Rivelazione, rilettura degli indizi e scelta conclusiva |

I titoli descrivono la struttura individuata nello script; l'ordine effettivo di alcune scene dipende dalle scelte e dai salti fra etichette. La revisione dei percorsi non deve ridurre la lunghezza del testo originale: gli interventi editoriali devono aggiungere raccordi o chiarimenti, non eliminare descrizioni e passaggi.

## Variabili narrative e conseguenze

Le variabili non sono punteggi morali. Registrano come Mila interpreta gli eventi e quali canali di supporto ha mantenuto.

- `fiducia_sophie`: influenza la lettura dei comportamenti di Sophie e alcuni dialoghi.
- `legame_kate`: influenza la disponibilità di Kate a intervenire e alcuni esiti.
- `dubbi_di_mila`: indica quanto Mila mette in discussione la propria interpretazione.
- `indizi_reali`: conteggia gli indizi riconosciuti o conservati; il numero da solo non garantisce che una teoria sia vera.
- `fiducia_genitori` e `prontezza_aiuto`: distinguono fiducia e disponibilità a chiedere aiuto.
- `flacone_con_mila`: tiene traccia della posizione dell'oggetto, con conseguenze sulle scelte successive.
- Flag investigativi: registrano la gestione del telefono, della fotografia, del quaderno e delle immagini mostrate da Sophie.
- Flag irreversibili: registrano promesse, decisioni sul flacone, denaro, richiesta d'aiuto e conseguenze finali.

## Archivio investigativo: progressione e ipotesi

L'archivio è accessibile con il tasto **I** e dal pulsante a schermo. Oltre al registro delle prove, ora presenta:

- **Collegamenti sbloccati** quando il giocatore conserva o condivide più fonti compatibili, per esempio il messaggio affidato a Kate e un'immagine ricevuta da Sophie.
- **Stati epistemici distinti**: osservato, riscontro esterno, ipotesi, sospetto non verificato, elemento mancante o perduto.
- **Ipotesi selezionabili**: manipolazione del racconto da parte di Sophie, sospetto sui genitori e rischio legato al flacone.
- **Solidità graduata**: una teoria sostenuta da fonti confrontabili è distinta da un'intuizione o da una versione accettata senza verifica.
- **Conseguenza narrativa**: nel capitolo 9, se il giocatore ha scelto l'ipotesi sulla manipolazione e dispone di riscontri sufficienti, si apre un'opzione per collegare le fonti e chiedere aiuto. La deduzione non trasforma automaticamente ogni dettaglio della storia in un fatto provato.

Le ipotesi sono interpretazioni del giocatore, non prove aggiuntive. Il contenuto del flacone, l'autenticità e il significato delle immagini e l'intera responsabilità dei personaggi non vanno presentati come scientificamente verificati solo perché Mila li sospetta.

## Prove e limiti interpretativi

- **Telefono e messaggio**: provano che esiste una comunicazione e, se condivisa, una copia esterna. Non provano da soli chi sia davvero il mittente né che ogni affermazione sia vera.
- **Fotografia di famiglia**: può essere conservata o digitalizzata. La frase sul retro ha un significato ambiguo; la testimonianza del padre, se raccolta, è un riscontro distinto, non un sostituto materiale dell'originale.
- **Quaderno nero**: gli appunti diretti sono diversi dalle parole dettate o corrette da Sophie. Un quaderno manipolato non è una fonte indipendente.
- **Immagini e documenti mostrati da Sophie**: il rifiuto di consentire un controllo è osservabile; non dimostra da solo una falsificazione. Se Mila accetta le immagini senza esaminarle, l'archivio le classifica come non verificate.
- **Flacone**: la domanda sulla provenienza è un fatto narrativo; contenuto e intenzione restano da accertare e richiederebbero analisi competente nel mondo della storia.

## Percorsi e finali

I quattro finali presenti nello script sono:

- **La verità ha una voce** (`finale_verita`): Mila chiede aiuto e apre la possibilità di confrontare fonti con Kate.
- **La porta aperta** (`finale_rottura`): Mila chiede aiuto ai genitori e tenta di fermare il piano prima della tragedia.
- **La fuga illusoria** (`finale_fuga`): Mila fugge con Sophie e scopre che la libertà promessa è un'altra forma di controllo.
- **Il fascicolo** (`finale_fascicolo`): la versione costruita da Sophie prevale e il quaderno può diventare una falsa confessione.

Le condizioni di accesso ai finali dipendono da combinazioni di scelte, relazioni, prove e disponibilità a chiedere aiuto. Il controllo statico può confermare l'esistenza delle etichette e dei salti nel codice, ma non dimostra che ogni combinazione sia giocabile: ogni percorso deve essere provato dal launcher Ren'Py.

## Cronologia: punti di controllo

Lo script contiene riferimenti orari precisi, tra cui il rientro alle **23:18** (tre minuti oltre un limite implicito delle 23:15), l'appuntamento sotto la quercia alle **02:00**, un riferimento alle **01:47**, un altro alle **01:55**, l'attraversamento del prato alle **02:40** e una scena conclusiva datata **8 maggio 2026, ore 03:30**.

Questi orari sono indizi utili ma, da soli, non fissano il calendario completo: alcuni appartengono a notti o giornate diverse. La revisione narrativa deve chiarire i passaggi di giorno/notte e il tempo trascorso tra capitoli senza inventare date che il testo originale non stabilisce. È stato preparato un registro separato con le verifiche statiche e le questioni da provare.

## Direzione artistica e interfaccia

La palette usa nero prugna, grigio fumo, rosa spento e luce domestica gialla. Le schermate di dialogo e scelta hanno pannelli dedicati e una variante più intensa per i momenti critici. I fondali sono definiti nel progetto Ren'Py e includono ambienti interni ed esterni, varianti giorno/notte e luoghi legati all'indagine.

Il file `characters.rpy` contiene **segnaposto grafici provvisori**, con espressioni per Mila, Sophie e Kate e altri personaggi. Non sono sprite artistici definitivi. La guida `SPRITE_PLACEHOLDER.md` spiega come sostituirli mantenendo i nomi immagine e le trasformazioni, senza riscrivere le scene.

## Audio

L'audio del prototipo è generato da script Python del progetto e include musica, ambienti e brevi effetti. Prima della distribuzione vanno verificati bilanciamento, transizioni, loop, volume e riferimenti a tutti gli asset in una sessione reale.

## Avviso contenuti

La storia affronta manipolazione psicologica, gaslighting, abusi emotivi, autolesionismo, violenza, lutto e suicidio. L'avviso contenuti deve restare accessibile prima dell'avvio della storia.

## Checklist prima della release

1. Eseguire **Check Script (Lint)** nel launcher Ren'Py e risolvere tutti gli errori e gli avvisi rilevanti.
2. Giocare dall'inizio a ciascuno dei quattro finali, provando le combinazioni principali di telefono, fotografia, quaderno, immagini, flacone e relazioni.
3. Verificare archivio, documenti, hotkey **I**, salvataggio/caricamento, rollback, skip, menu, audio e transizioni.
4. Controllare la cronologia completa in una tabella giorno/ora e chiarire ogni passaggio che possa sembrare simultaneo o contraddittorio.
5. Verificare ogni affermazione trattata come prova e distinguere esplicitamente osservazione, testimonianza, inferenza e sospetto.
6. Sostituire i segnaposto con sprite definitivi e controllare le sovrapposizioni con dialoghi, scelte e fondali.
7. Generare build desktop pulite, avviarle fuori dall'ambiente di sviluppo e verificare la persistenza dei salvataggi.
8. Controllare licenze, crediti, documenti originali e immagini di riferimento presenti nel repository prima della distribuzione pubblica.

## Nota sul testo originale

La revisione deve preservare la lunghezza e le descrizioni della storia originale. Correzioni di continuità, raccordi temporali e chiarimenti sulle prove vanno realizzati con modifiche mirate e senza tagliare i passaggi narrativi.
