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
