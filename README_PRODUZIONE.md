# La Bambola della Porta Accanto

## Stato dello sviluppo

Il progetto è stato convertito dal modello Ren'Py predefinito a una visual novel interattiva completa nella sua prima versione testuale. Il menu, il testo informativo, l'avviso contenuti, il prologo, cinque capitoli e quattro finali sono pronti per ricevere grafica, suono, transizioni e una fase di revisione narrativa.

## Lettura della storia

La storia ha un nucleo forte: Mila, diciottenne fragile e isolata, interpreta la propria casa come una prigione. Sophie, quindicenne brillante e manipolatoria, trasforma quell'interpretazione in una dipendenza e poi in un piano criminale. Il colpo di scena centrale è che i genitori non erano gli aguzzini che Mila credeva: Sophie ha orientato ricordi, scrittura e percezione fino a renderla lo strumento del proprio crimine.

I suoi punti più adatti a una visual novel sono l'atmosfera claustrofobica, il rapporto ambiguo tra le due protagoniste, Kate come possibile ancora alla realtà e gli indizi che acquistano un secondo significato dopo la rivelazione.

## Sistema di relazioni, indizi e stato degli oggetti

Le scelte non sono un test di moralità: registrano come Mila interpreta ciò che accade e a chi è disposta a chiedere aiuto. Lo script mantiene cinque variabili narrative, ciascuna con conseguenze nel gioco:

- `fiducia_sophie`: modifica la lettura dei comportamenti di Sophie nel capitolo della quercia, il monologo prima della scelta conclusiva e l'interpretazione dei finali della fuga e del fascicolo.
- `legame_kate`: influenza se Kate cerca Mila dopo il messaggio del telefono, il modo in cui Mila riesce a chiederle aiuto e la risposta nel finale della verità.
- `dubbi_di_mila`: se è abbastanza alto, permette a Mila di riconoscere un'ulteriore incongruenza nell'immagine e ottenere un indizio concreto; insieme al legame con Kate può aprire la richiesta di aiuto.
- `indizi_reali`: rappresenta i dettagli e le prove che Mila ha riconosciuto o conservato. La soglia di 3 cambia la lettura degli appunti; la soglia di 4 offre un percorso basato su prove più solide e cambia la descrizione del finale della verità.
- `fiducia_genitori`: modifica il modo in cui Mila interpreta la proposta d'aiuto, può aprire una via per chiedere aiuto anche senza avere prove complete e cambia le opzioni e il dialogo del finale con i genitori.

Il flacone è gestito separatamente dalla variabile di relazione con lo stato oggetto `flacone_con_mila`. Quando Mila lo lascia nella neve, le opzioni successive e i finali rispettano quella posizione.

### Tre categorie di scelte

Le scelte sono progettate per avere conseguenze riconoscibili, senza trasformare ogni singola battuta in un ramo narrativo enorme:

- **Caratterizzazione**: il tono con cui Mila tratta Kate, Sophie e suo padre cambia la fiducia, i dialoghi successivi e il modo in cui interpreta il loro comportamento.
- **Investigazione**: il telefono segreto può essere condiviso con Kate, usato per rispondere a Sophie oppure nascosto. La fotografia può essere conservata, strappata o digitalizzata. Il quaderno può contenere fatti, frasi suggerite da Sophie oppure restare vuoto. Le immagini possono essere verificate, credute o condivise. Queste azioni vengono registrate con flag persistenti e modificano gli indizi, le scene successive e il modo in cui i finali vengono raccontati.
- **Scelte irreversibili**: lasciare il flacone nella neve, promettere di aiutare Sophie, distruggere una prova o condividere copie con Kate sono decisioni che non vengono annullate automaticamente quando la scena si chiude. Lo stato degli oggetti e delle prove viene controllato nei capitoli successivi.

La scelta di chiedere aiuto può quindi essere raggiunta attraverso prove sufficienti (`indizi_reali >= 4`), un legame con Kate insieme a dubbi concreti (`legame_kate >= 2` e `dubbi_di_mila >= 2`), fiducia nei genitori (`fiducia_genitori >= 2`) oppure la condivisione con Kate sia del messaggio sia di una delle immagini (`telefono_condiviso_kate` e `immagini_condivise_kate`). Nessuna soglia è una valutazione morale del giocatore: sono percorsi diversi e con conseguenze diverse, non risposte giuste o sbagliate.


## Struttura implementata

1. Prologo: la routine di Mila e il primo incontro giocabile con Sophie.
2. Come sanguina un robot: primo isolamento, Kate, la casa di Sophie e le reazioni emotive di Mila.
3. La geometria del silenzio: telefono segreto, quaderno e primo ricordo che contraddice Sophie.
4. Frequenze d'ombra: prove falsificate, richiesta di aiuto e possibilità di fidarsi del padre.
5. La quercia: il flacone, il piano di Sophie e il primo bivio irreversibile.
6. Il diorama: scelta conclusiva e quattro finali.

## Finali implementati

- **La verità ha una voce**: Mila chiede aiuto a Kate, le prove vengono preservate e Sophie non può più controllare il racconto.
- **La porta aperta**: Mila consegna il flacone ai genitori, spezzando il piano prima della tragedia.
- **La fuga illusoria**: Mila scappa con Sophie e scopre che la libertà promessa è un nuovo controllo.
- **Il fascicolo**: Mila segue il piano; il quaderno viene usato come una falsa confessione e Sophie resta invisibile.

## Direzione artistica

Palette: nero prugna, grigio fumo, rosa spento e giallo da luce domestica. Il progetto ora usa sette fondali originali: menu notturno, camera e cucina di Mila, scuola, quercia con le due villette, cucina e camera di Sophie. Sono illustrazioni atmosferiche progettate per dare ritmo alla prima versione giocabile; gli sprite espressivi, gli oggetti-indizio e le varianti temporali restano la prossima produzione grafica.

### Riferimenti personaggi

Le immagini di riferimento ricevute restano fuori dalla cartella del gioco e non saranno incluse nella distribuzione. Orientano soltanto due silhouette originali: Mila sarà una ragazza maggiorenne dai capelli castano scuro, postura chiusa e occhi segnati; Sophie sarà una quindicenne bionda, abbigliamento scuro, espressione calma e presenza controllante. Gli sprite finali saranno disegnati ex novo, con pose ed espressioni pensate per la visual novel.

## Audio implementato

Il gioco dispone ora di un tema per il menu, due ambienti in loop e sei effetti sonori originali. La pioggia collega scuola, quercia e villette; il ronzio interno accompagna le scene domestiche. Accendino, finestra, telefono, porta, vetro e battito cardiaco evidenziano soltanto gli snodi narrativi. I file sono generati localmente e non impiegano campioni o brani esterni.

## Contenuti sensibili

La storia contiene manipolazione psicologica, violenza e autolesionismo. La versione interattiva manterrà l'impatto del thriller evitando di trasformare le scene più dure in immagini grafiche o in meccaniche di gioco.
