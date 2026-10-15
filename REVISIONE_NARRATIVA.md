# Revisione narrativa e coerenza — stato statico

Questa nota accompagna la revisione del 15 ottobre 2026. È una verifica del testo sorgente e dei collegamenti nel codice, non sostituisce una partita completa né Ren'Py Lint.

## Esito rapido

- Trovati i label `start`, `capitolo_1`–`capitolo_9` e i quattro finali: `finale_verita`, `finale_rottura`, `finale_fuga`, `finale_fascicolo`.
- I salti `jump` presenti nello script puntano a label esistenti nel controllo statico.
- Il codice conserva 16 menu e 36 dichiarazioni `default` al momento della scansione. Questo dato non dimostra che ogni ramo sia raggiungibile o privo di errori a runtime.
- L'archivio distingue ora osservazioni, riscontri, sospetti e ipotesi; le ipotesi selezionate possono cambiare il dialogo e, con riscontri sufficienti, sbloccare una scelta conclusiva.
- Non è stata eseguita una build Ren'Py né una sessione interattiva in questa revisione.

## Registro cronologico da verificare in gioco

| Riferimento nel testo | Lettura attuale | Controllo da fare |
|---|---|---|
| 23:18, Mila rientra in ritardo di tre minuti | Implica un limite alle 23:15 | Verificare che il limite sia già chiaro nel contesto precedente, senza affidarlo solo all'inferenza |
| Messaggio: incontro alle 02:00 sotto la quercia | Appuntamento notturno | Confermare che la scena successiva mostri la stessa notte e non una notte diversa |
| 01:47 nel capitolo 4 | Attesa prima dell'appuntamento | Verificare la continuità fino alle 02:00 e che nessun dialogo faccia pensare a un salto temporale |
| 01:55 nel capitolo 6 | Nuova scena notturna, in un altro segmento della storia | Segnalare con un raccordo che si tratta di un'altra notte, se questo è ciò che intende il testo originale |
| 02:40 nel capitolo 8 | Attraversamento del prato durante la crisi | Controllare l'ordine degli eventi rispetto alla scena del flacone e al passaggio al capitolo 9 |
| 8 maggio 2026, ore 03:30 | Data esplicita del finale/fascicolo | Verificare che eventuali schermate o salvataggi narrativi non presentino una data incompatibile |

Il testo usa anche riferimenti relativi come “tre anni prima”, “tre anni per costruire”, “sei mesi per premerli” e “dieci giorni per finire”. La corrispondenza tra questi intervalli e la successione degli eventi va confermata in una tabella cronologica completa prima di aggiungere altre date. Non sono state inventate date mancanti e non sono stati rimossi passaggi descrittivi.

## Registro delle prove: criteri applicati

- **Telefono anonimo**: il possesso o la condivisione dimostra l'esistenza della traccia; non dimostra da solo l'identità del mittente o la veridicità del messaggio.
- **Fotografia**: l'originale, la copia digitale e la testimonianza del padre sono trattati come fonti diverse. La testimonianza può confermare la frase ricordata, non ricreare l'oggetto perduto.
- **Quaderno**: gli appunti diretti sono distinguibili dal contenuto suggerito o corretto da Sophie. Il secondo non viene trattato come fonte indipendente.
- **Immagini mostrate da Sophie**: il rifiuto di lasciarle esaminare è un comportamento osservabile; non è una prova automatica di frode.
- **Flacone**: la provenienza non chiarita è una domanda aperta. Il contenuto non viene dichiarato noto senza un'analisi competente.
- **Sospetti sui genitori**: se Mila ha creduto alle immagini senza controllarle, l'archivio mantiene esplicitamente lo stato “non verificato”.

## Percorsi e prove da eseguire manualmente

La matrice sotto serve a pianificare il collaudo; non afferma che le prove siano già state eseguite.

| Percorso | Combinazione da provare | Esito da verificare |
|---|---|---|
| Verità tramite Kate | Condividere il telefono e condividere un'immagine | Collegamento sbloccato, ipotesi selezionabile, opzione di deduzione nel capitolo 9 |
| Verità tramite confronto | Chiedere di verificare le immagini e avere un secondo riscontro (quaderno manipolato, fotografia digitalizzata o telefono condiviso) | L'ipotesi viene classificata come sostenuta ma non definitiva |
| Sospetto non verificato | Credere alle immagini e scegliere l'ipotesi sui genitori | Dialogo che segnala la differenza tra sospetto e fatto; nessuna falsa conferma nell'archivio |
| Flacone | Indagare il flacone e scegliere l'ipotesi di rischio | Il dialogo mantiene il contenuto come non accertato |
| Finale verità | Richiesta d'aiuto con Kate o scelta conclusiva basata sui collegamenti | `finale_verita` raggiungibile e coerente con le prove raccolte |
| Finale rottura | Scegliere di rivolgersi ai genitori | `finale_rottura` raggiungibile senza richiedere una prova che il ramo non consente di raccogliere |
| Finale fuga | Accettare la fuga con Sophie nelle scelte precedenti | `finale_fuga` raggiungibile e conseguenze coerenti con la promessa di libertà |
| Finale fascicolo | Non chiedere aiuto nel capitolo 9 o lasciare che Sophie imponga la scelta | `finale_fascicolo` raggiungibile; distinguere la versione narrativa dalla verità oggettiva |

## Regole editoriali per la revisione completa

1. Conservare la lunghezza, le descrizioni sensoriali e i passaggi della storia originale. Non usare tagli di prosa come soluzione a problemi di ritmo o continuità.
2. Se un orario o un salto di scena è ambiguo, aggiungere un raccordo breve e coerente invece di cambiare arbitrariamente la cronologia.
3. Separare sempre: fatto osservato, testimonianza, inferenza, ipotesi e conclusione confermata.
4. Non far dire a un personaggio che una prova “dimostra” più di quanto il suo contenuto consenta.
5. Quando una scelta distrugge o non raccoglie un oggetto, verificare che dialoghi, archivio e finali rispettino lo stato dell'oggetto.
6. Per ogni menu, verificare sia la condizione che mostra l'opzione sia i flag impostati dalla scelta e i percorsi successivi.
7. Dopo le verifiche statiche, eseguire Ren'Py Lint e giocare tutti i percorsi principali con salvataggi separati.

## Limiti di questa revisione

Questa passata aggiorna l'archivio, introduce una conseguenza narrativa per una deduzione sostenuta e allinea la documentazione alla struttura attuale. Non dichiara completata la revisione definitiva della cronologia: gli orari sopra elencati sono i punti da controllare nel playtest, perché lo script non ancora ancora ogni segmento a una data di calendario esplicita.


## Audit delle conseguenze delle variabili — 15 ottobre 2026

La revisione è stata concentrata sulle variabili già esistenti. Non sono stati aggiunti nuovi flag narrativi; sono stati riutilizzati stati esistenti e rimossi tre flag che non producevano effetti osservabili (`tensione_scena`, `scelta_finale`, `telefonata_registrata`). La tensione visiva dipende ora dai dubbi e dagli indizi già accumulati, anziché da un booleano che non diventava mai vero.

### Conseguenze collegate

| Scelta/stato già presente | Conseguenza aggiunta o resa più esplicita |
|---|---|
| `telefono_condiviso_kate`, `telefono_nascosto`, `telefono_risposto_sophie` | Incontro sotto la quercia nel capitolo 4: Sophie reagisce diversamente al messaggio condiviso, al silenzio o alla risposta ricevuta. |
| `flacone_indagato` | Nel capitolo 8 Mila ricorda se aveva chiesto la provenienza delle gocce e se Sophie aveva evitato la domanda. |
| `quaderno_fedele`, `quaderno_manipolato`, `quaderno_vuoto` | Il capitolo 9 richiama la qualità del proprio resoconto; la gestione delle note cambia inoltre la ricostruzione del finale della verità e il peso attribuito al diario nel finale del fascicolo. |
| `prontezza_aiuto` | Se Mila ha già compiuto passi concreti verso l'aiuto, nel capitolo 9 riesce a ricordare che può chiedere aiuto senza avere ogni dettaglio in ordine. |
| `fiducia_genitori`, `padre_evitato`, `padre_ascoltato`, `padre_confrontato` | Il ricordo del padre e il dialogo conclusivo cambiano in base a come Mila ha gestito le occasioni precedenti di ascolto o confronto. |
| `telefono_condiviso_kate`, `immagini_condivise_kate`, `legame_kate` | Il finale del fascicolo distingue tra copie esterne conservate da Kate, una relazione che le permette di testimoniare e una preoccupazione che resta più fragile. |
| `ipotesi_genitori_sospetto` | Nel finale del fascicolo, il sospetto non verificato di Mila può essere reinterpretato dagli investigatori come prova di rancore, rendendo visibile il rischio di confondere convinzioni e fatti. |

### Flag rimossi

- `tensione_scena`: era inizializzata a `False` e non veniva mai impostata a `True`. Le condizioni di presentazione sono state semplificate usando `dubbi_di_mila` e `indizi_reali`, che già esprimono lo stato narrativo.
- `scelta_finale`: veniva assegnata in vari punti ma non veniva mai letta per determinare una scena o un finale.
- `telefonata_registrata`: era dichiarata ma non veniva né impostata né letta.

Dopo questa pulizia, lo script dichiara 33 variabili `default` invece delle 36 precedenti. L'obiettivo non è ridurre il sistema a un unico punteggio: i flag di oggetti e fonti restano distinti perché descrivono stati narrativi irreversibili diversi.

### Verifiche statiche dopo la modifica

- I label dei nove capitoli e dei quattro finali sono ancora presenti.
- I salti `jump` del file continuano a puntare a label esistenti nel controllo statico.
- Le nuove conseguenze si appoggiano a flag già presenti; non sono stati aggiunti nuovi `default`.
- La revisione non è ancora un collaudo runtime: **Ren'Py Lint e il playtest di ogni combinazione restano da eseguire**. In particolare, verificare i rami del finale del fascicolo con quaderno fedele/manipolato/vuoto e con/senza copie condivise con Kate.
