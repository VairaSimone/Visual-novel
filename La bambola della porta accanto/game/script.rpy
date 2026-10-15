# La Bambola della Porta Accanto
# Vertical slice iniziale: prologo, prima scelta e variabili narrative.

define mila = Character("Mila", color="#d9c4d6")
define sophie = Character("Sophie", color="#e4b6bd")
define kate = Character("Kate", color="#c9d7ef")
define madre = Character("Mamma", color="#c6b59b")
define padre = Character("Papà", color="#8f9aa8")

# Stato narrativo: le relazioni influenzano dialoghi, indizi e accesso alle scelte.
# I valori possono crescere o diminuire: non sono punteggi morali.
default fiducia_sophie = 0   # Quanto Mila crede alla versione di Sophie.
default legame_kate = 0      # Quanto è rimasto aperto il canale con Kate.
default dubbi_di_mila = 0    # Quanto Mila mette in discussione la propria interpretazione.
default indizi_reali = 0     # Indizi concreti riconosciuti o conservati.
default fiducia_genitori = 0 # Quanto Mila è disposta a chiedere aiuto ai genitori.

# True quando Mila ha fisicamente con sé il flacone ricevuto da Sophie.
# Se lo lascia cadere nella neve, le opzioni successive devono rispettarlo.
default flacone_con_mila = False

label start:
    scene bg title night
    with fade
    play music audio.room fadein 1.5

    centered "{size=32}{color=#e6d4db}AVVISO CONTENUTI{/color}{/size}\n\n{size=23}Questa storia contiene manipolazione psicologica,\nviolenza non grafica e riferimenti all'autolesionismo.{/size}"

    centered "{size=54}{color=#e6d4db}LA BAMBOLA DELLA PORTA ACCANTO{/color}{/size}\n\n{size=28}{color=#aa97a3}Una visual novel thriller psicologica{/color}{/size}"

    scene bg mila room
    with dissolve

    "Il primo suono della giornata non è mai la sveglia."
    play sound audio.lighter
    "È lo scatto metallico dell'accendino nell'altra stanza."
    "Un clic secco. Poi il primo sospiro di fumo di mia madre."
    "Sei minuti e undici secondi prima che mi chiami. Li conto da un anno."

    madre "Mila."

    "La sua voce attraversa la porta come un ago freddo."
    "Mi alzo senza far scricchiolare le doghe. In questa casa, anche il rumore è una colpa."

    scene bg mila kitchen
    with dissolve

    madre "Stasera vai dai vicini. Sophie ha bisogno di te."
    mila "Sì, mamma."
    "Lo yogurt scivola verso il bordo del tavolo. Lo afferro prima che cada."
    "È un gesto minuscolo. Lo ricorderò per ore."

    scene bg school
    with dissolve
    play music audio.rain fadeout 1.0 fadein 1.5

    "A scuola, Kate mi raggiunge davanti al cancello."
    kate "Stasera festa da Leo. Devi venire, almeno per un'ora."

    menu:
        "Come rispondo a Kate?"

        "Le dico la verità: devo lavorare dai vicini.":
            $ legame_kate += 1
            mila "Non posso. Devo andare da Sophie."
            kate "Allora ti scrivo. Non sparire, okay?"
            "Per un attimo, la sua preoccupazione mi sembra reale."

        "Taglio corto: non sono affari suoi.":
            $ dubbi_di_mila += 1
            mila "Non posso, Kate. Lascia stare."
            "Lei abbassa lo sguardo. Mi dispiace, ma non so come dirlo."

    scene bg oak houses
    with dissolve

    "Alle sette sono davanti alla villetta accanto."
    "Le due case sono quasi identiche, separate da una lingua di prato e da una vecchia quercia."
    "La porta della stanza di Sophie è coperta di adesivi consumati e di un cartello: KEEP OUT."

    sophie "Entra, Mila. Lo sai che con me non devi bussare."
    "Busso lo stesso. È l'unica porta su cui mi è concesso farlo."
    sophie "Pensavo che fossi scappata. Mi sei mancata."
    "Sophie mi guarda come se fosse l'unica persona capace di vedermi davvero."

    menu:
        "Sophie mi prende il mento con due dita."

        "Mi scosto e preparo la cena.":
            $ dubbi_di_mila += 1
            mila "Sono qui per i compiti e la cena. Nient'altro."
            sophie "Certo. Recitiamo pure la parte."

        "Resto immobile e lascio che mi guardi.":
            $ fiducia_sophie += 1
            "Il suo pollice sfiora la cicatrice sotto il mio zigomo."
            sophie "Solo io mi accorgo di quanto tremi."

    "Sotto la quercia, più tardi, ci sarà un messaggio."
    "E da qualche parte, dentro di me, una voce comincerà a fare domande."

    jump capitolo_1


label capitolo_1:
    scene expression Solid("#151116")
    with fade

    centered "{size=42}{color=#e6d4db}CAPITOLO 1{/color}{/size}\n\n{size=28}{color=#aa97a3}Come sanguina un robot{/color}{/size}"

    scene bg sophie kitchen
    with dissolve
    play music audio.room fadeout 1.0 fadein 1.5

    "Preparo il pollo con movimenti automatici. Taglio, soffriggo, mescolo."
    "È una coreografia che potrei eseguire bendata. Mia madre la chiamerebbe efficienza."
    "Io la chiamo paura di sbagliare."

    sophie "Sai che i miei ti usano come esempio?"
    "Sophie è seduta sul bancone. Le sue gambe dondolano sopra il pavimento lucido."
    mila "I tuoi sono gentili."
    sophie "No. Sono pigri. Ti guardano e pensano: ecco una ragazza che non darà mai problemi."
    sophie "Ma io vedo come stringi quel coltello."

    menu:
        "Le mie nocche sono bianche attorno al manico."

        "Lascio il coltello e conto fino a dieci.":
            $ dubbi_di_mila += 1
            "Appoggio il coltello. Uno. Due. Tre. Il respiro rallenta un poco."
            sophie "Brava. Impari a controllarti quando qualcuno guarda."

        "Le dico che non sa niente di me.":
            $ fiducia_sophie -= 1
            mila "Non sai niente di me, Sophie."
            "Per un istante il suo sorriso smette di esistere. Poi ritorna, più piccolo."
            sophie "Allora insegnamelo."

        "Le chiedo cosa vuole davvero.":
            $ fiducia_sophie += 1
            mila "Cosa vuoi da me?"
            sophie "Che tu smetta di fingere di non essere arrabbiata."

    "Il telefono di Sophie vibra sul bancone. Lo gira subito, con lo schermo rivolto verso il marmo."
    play sound audio.phone
    "Un dettaglio insignificante. Eppure il gesto mi resta addosso."

    menu:
        "Posso fare una domanda, oppure fingere di non aver visto."

        "Chiedo chi le ha scritto.":
            $ dubbi_di_mila += 1
            mila "Chi era?"
            sophie "Nessuno. Una pubblicità."
            "La risposta è troppo rapida. Sophie, però, non distoglie lo sguardo."

        "Non chiedo nulla.":
            $ fiducia_sophie += 1
            "Non sono affari miei. O almeno, è quello che mi ripeto."

    scene bg sophie room
    with dissolve

    "Dopo cena la aiuto con latino. La versione parla di una casa che sopravvive ai propri abitanti."
    sophie "Le case non ricordano niente. Sono solo stanze."
    mila "Allora perché la tua camera è sempre chiusa?"
    sophie "Perché alcune cose devono restare mie."

    "La frase non suona come una risposta. Suona come un confine."
    "Alle undici, i suoi genitori non sono ancora rientrati."

    sophie "Resta qui stanotte. Di' ai tuoi che mi servi."

    menu:
        "La porta di casa mia mi aspetta dall'altra parte del prato."

        "Resto e scrivo a Kate.":
            $ legame_kate += 1
            $ dubbi_di_mila += 1
            "Apro il telefono. Le dita tremano prima di premere il suo nome."
            mila "Posso restare dieci minuti. Poi devo andare."
            sophie "Dieci minuti sono abbastanza per cambiare tutto."

        "Torno subito a casa.":
            $ fiducia_sophie -= 1
            mila "No. Se tardo, sarà peggio."
            sophie "Certo. Corri dal tuo mostro."
            play sound audio.door
            "La sua voce è dolce, ma le parole mi seguono fino alla porta."

        "Resto con Sophie e spengo il telefono.":
            $ fiducia_sophie += 2
            $ legame_kate -= 1
            "Spengo il telefono. Il buio dello schermo sembra una piccola resa."
            sophie "Ecco. Adesso siamo solo noi due."

    scene bg oak houses
    with dissolve
    play music audio.rain fadeout 1.0 fadein 1.5

    "Fuori, la quercia graffia il vetro con i suoi rami."
    "Tra la mia casa e la sua c'è una distanza di pochi metri."
    "Non so ancora che basterà quella distanza per perdermi."

    if dubbi_di_mila >= 2:
        "Però qualcosa stona. Un gesto troppo misurato. Una risposta troppo pronta."
        "Per la prima volta, penso che il pericolo possa avere una voce gentile."
    elif fiducia_sophie >= 2:
        "Con Sophie, per qualche minuto, mi sento meno invisibile."
        "È una sensazione così rara che non mi accorgo di quanto costa."
    else:
        "Non so a chi credere. Forse non l'ho mai saputo."

    jump capitolo_2


label capitolo_2:
    scene bg mila kitchen
    with fade
    play music audio.room fadeout 1.0 fadein 1.5

    centered "{size=42}{color=#e6d4db}CAPITOLO 2{/color}{/size}\n\n{size=28}{color=#aa97a3}La geometria del silenzio{/color}{/size}"

    "La mattina dopo, mia madre è già in cucina. Non mi rimprovera."
    "È peggio: parla con una calma che non riesco a decifrare."
    madre "Ho chiamato la dottoressa Bianchi. Vorrei che ci parlassi."
    "Nella mia testa, la frase cambia forma. Diventa una minaccia. Una stanza chiusa. Una trappola."

    menu:
        "Cosa rispondo?"

        "Chiedo perché vuole mandarmi da una dottoressa.":
            $ dubbi_di_mila += 1
            madre "Perché ti vedo stanca, amore. E non so più come raggiungerti."
            "La parola amore mi irrita. Eppure non sembra preparata."

        "Accetto di parlarne con lei.":
            $ fiducia_genitori += 1
            mila "Va bene. Ma voglio sapere tutto prima."
            "Mia madre abbassa gli occhi. Sembra sollevata, non vittoriosa."

        "La accuso di voler controllare la mia vita.":
            $ fiducia_sophie += 1
            mila "Non mi farai rinchiudere."
            "Il viso di mia madre si svuota. Mio padre posa il giornale, ma non trova parole."

    if fiducia_genitori >= 1:
        "Non mi fido ancora del tutto, ma il pensiero della dottoressa non sembra più soltanto una minaccia."
    else:
        "Continuo a sentire ogni proposta dei miei genitori come un tentativo di chiudermi in una stanza."

    "A scuola, un piccolo sasso colpisce la finestra dell'aula."
    play sound audio.window_knock
    "Sul davanzale trovo un foglietto, piegato in quattro."
    "{i}Ti hanno già detto che sei sbagliata? Guarda sotto il tappetino. — S.{/i}"
    "Sotto il tappetino di casa mi aspetta un vecchio telefono con una SIM anonima."
    play sound audio.phone
    "Lo accendo nel bagno della scuola. C'è un solo messaggio."
    "{i}Scrivi tutto. Ogni parola che ti fanno. Ti servirà quando nessuno ti crederà.{/i}"

    menu:
        "Il telefono pesa poco, ma mi sembra impossibile nasconderlo."

        "Lo porto a Kate e le chiedo aiuto.":
            $ legame_kate += 2
            $ indizi_reali += 1
            kate "Non lo tocchiamo. Facciamo delle foto e parliamo con qualcuno di grande."
            "Kate non ride, non minimizza e non mi chiede di scegliere subito una versione dei fatti."

        "Lo tengo e rispondo a Sophie.":
            $ fiducia_sophie += 2
            sophie "Brava ragazza. Adesso siamo connesse."
            "Mi sento scelta. È una sensazione che assomiglia troppo alla pace."

        "Lo spengo e lo nascondo senza rispondere.":
            $ dubbi_di_mila += 1
            $ indizi_reali += 1
            "Per la prima volta, tengo qualcosa che Sophie non sa di possedere."

    if legame_kate >= 2:
        "Poco dopo, il telefono vibra: Kate mi scrive che è ancora disponibile ad aiutarmi, senza chiedermi di scegliere subito a chi credere."
    else:
        "Il telefono resta in silenzio. Mi accorgo che, per ora, ho tenuto Kate fuori da tutto questo."

    "Quella sera, prima di dormire, apro il cassetto di mio padre cercando le batterie."
    "Trovo una fotografia azzurra: ho sette anni, la febbre alta, mia madre mi stringe avvolta in una coperta."
    "Sul retro, la grafia precisa di papà: {i}Perché tutto sia perfetto.{/i}"

    menu:
        "Guardo quella frase finché le lettere non tremano."

        "La nascondo. Voglio ricordarla.":
            $ fiducia_genitori += 1
            $ indizi_reali += 1
            "Non cancella il dolore, ma rende più difficile chiamarlo odio."

        "La strappo e la butto via.":
            $ fiducia_sophie += 1
            "Le prove non valgono niente. Sophie dice che le famiglie sanno recitare."

        "La fotografo con il telefono segreto.":
            $ dubbi_di_mila += 1
            $ indizi_reali += 1
            "Voglio una prova, anche se non so ancora di cosa."

    jump capitolo_3


label capitolo_3:
    scene bg oak houses
    with fade
    play music audio.rain fadeout 1.0 fadein 1.5

    centered "{size=42}{color=#e6d4db}CAPITOLO 3{/color}{/size}\n\n{size=28}{color=#aa97a3}Frequenze d'ombra{/color}{/size}"

    "Sophie mi aspetta sotto la quercia. La neve vecchia si scioglie ai bordi del prato."
    sophie "Hai scritto quello che ti fanno?"
    mila "Non tutto."
    sophie "Allora loro vinceranno. La memoria è una cosa che gli adulti riscrivono benissimo."
    "Mi porge un quaderno nero. Sulla prima pagina ha già segnato una data."

    menu:
        "Il quaderno è aperto tra le mie mani."

        "Scrivo solo fatti concreti.":
            $ dubbi_di_mila += 1
            $ indizi_reali += 1
            "Scrivo: mamma ha chiesto della dottoressa. Papà ha lasciato una fotografia."
            "Sophie non sorride."

        "Scrivo la versione che Sophie mi suggerisce.":
            $ fiducia_sophie += 2
            "Scrivo che mia madre vuole cancellarmi. La frase non mi appartiene, ma la grafia è la mia."

        "Non scrivo nulla.":
            $ fiducia_sophie -= 1
            sophie "Stai scegliendo loro?"
            "La domanda ha il peso di un ricatto."

    "Sophie mi mostra una serie di fotografie sul suo telefono: ricevute, estratti conto, messaggi incompleti."
    sophie "Vedi? I tuoi pagano qualcuno. Vogliono liberarsi di te."

    menu:
        "Le cifre sullo schermo scorrono troppo in fretta."

        "Chiedo di vedere il file originale.":
            $ dubbi_di_mila += 1
            $ indizi_reali += 1
            sophie "Non ti fidi di me?"
            "Ingrandendo l'immagine, noto che una cifra è sfocata in modo diverso dalle altre."
            if dubbi_di_mila >= 3:
                "Confronto i bordi della cifra con quelli del resto del documento: anche l'ombra del testo non coincide. Non è una prova definitiva, ma è una seconda anomalia concreta."
                $ indizi_reali += 1
            else:
                "Non riesco a capire se sia un errore, una fotografia venuta male o qualcosa di deliberato."

        "Le credo senza guardare meglio.":
            $ fiducia_sophie += 2
            "Il terrore è più semplice di un dubbio."

        "Mando una foto a Kate.":
            $ legame_kate += 1
            $ indizi_reali += 1
            kate "Mila, sembra un'immagine modificata. Non decidere nulla stanotte."

    "Quando torno a casa, mio padre è seduto sul divano con due tazze di tè."
    padre "Non devi spiegarmi tutto. Però non devi affrontarlo da sola."

    menu:
        "Le sue mani tremano mentre porge la tazza."

        "Mi siedo con lui.":
            $ fiducia_genitori += 2
            "Non parla per un po'. In quel silenzio, non mi sento intrappolata."

        "Gli chiedo perché è rimasto zitto per anni.":
            $ dubbi_di_mila += 1
            padre "Perché ho avuto paura di dire la cosa sbagliata. E ho sbagliato lo stesso."
            "Non è una difesa. È una confessione imperfetta."

        "Salgo in camera senza rispondere.":
            $ fiducia_sophie += 1
            "Chiudo la porta. Poi controllo due volte la finestra."

    if indizi_reali >= 3:
        "Rileggo gli appunti: fotografia, messaggi e dettagli fuori posto cominciano a formare una sequenza, non soltanto una sensazione."
    else:
        "Ho qualche frammento, ma non ancora una sequenza verificabile. Dovrò decidere quanto rischio correre senza prove complete."

    jump capitolo_4


label capitolo_4:
    scene bg oak houses
    with fade
    play sound audio.heartbeat

    centered "{size=42}{color=#e6d4db}CAPITOLO 4{/color}{/size}\n\n{size=28}{color=#aa97a3}La quercia{/color}{/size}"

    "Il 7 maggio, Sophie mi aspetta nel punto in cui i rami della quercia coprono entrambe le case."
    "Ha un flacone scuro nella tasca dell'impermeabile."
    sophie "Dormiranno. Prenderemo i soldi e andremo al mare. Solo noi due."
    play sound audio.glass
    "Mi ricordo di una frase scritta sul retro della fotografia: Perché tutto sia perfetto."
    "Mi ricordo di Kate che dice: non decidere nulla stanotte."

    if fiducia_sophie >= 3:
        "Sophie mi guarda con la stessa tenerezza di sempre. Una parte di me vuole credere che il flacone sia soltanto il prezzo di una fuga."
    elif fiducia_sophie <= 0:
        "Per la prima volta noto che Sophie controlla il mio viso prima ancora della mia risposta, come se stesse aspettando una battuta precisa."
    else:
        "Non so se la dolcezza di Sophie sia sincera o soltanto il modo più efficace per farmi esitare."

    # Sophie passa il flacone a Mila prima che lei scelga cosa farne.
    $ flacone_con_mila = True

    menu:
        "Sophie mi mette il flacone nel palmo."

        "Le chiedo da dove viene davvero.":
            $ dubbi_di_mila += 1
            $ indizi_reali += 1
            sophie "Perché fai sempre domande quando finalmente possiamo essere libere?"
            "Non risponde. Stringe soltanto le mie dita attorno al vetro."

        "Lo prendo e le prometto che farò la mia parte.":
            $ fiducia_sophie += 2
            "La sua espressione si addolcisce. È il momento in cui avrei dovuto avere più paura."

        "Lascio cadere il flacone nella neve.":
            $ flacone_con_mila = False
            $ fiducia_sophie -= 2
            $ dubbi_di_mila += 1
            sophie "Non farmi diventare cattiva, Mila."
            "Le sue parole sono leggere. Il suo sguardo no."

    if indizi_reali >= 4 or (legame_kate >= 2 and dubbi_di_mila >= 2) or fiducia_genitori >= 2:
        if indizi_reali >= 4:
            "Tengo il telefono tra le dita. Ho abbastanza frammenti per vedere che la storia di Sophie non sta in piedi."
        elif legame_kate >= 2 and dubbi_di_mila >= 2:
            "Non ho prove complete, ma Kate è ancora raggiungibile e ormai riconosco troppe contraddizioni per restare in silenzio."
        else:
            "Non ho prove sufficienti. Mi resta però la memoria di mio padre che ha provato ad ascoltarmi: posso chiedere aiuto senza dover risolvere tutto da sola."

        menu:
            "Posso chiedere aiuto prima che sia troppo tardi."

            "Chiamo Kate e le mando la posizione.":
                if legame_kate >= 2:
                    "Non devo convincerla che ho paura: Kate riconosce subito che le sto chiedendo aiuto."
                else:
                    "Esito prima di chiamare Kate. Non so se si fiderà ancora di me, ma le mando la posizione e le dico soltanto ciò che ho visto."
                $ legame_kate += 2
                if not flacone_con_mila:
                    "Le spiego anche che il flacone è rimasto nella neve, sotto la quercia."
                jump finale_verita

            "Mi fido di mio padre: entro e gli mostro il flacone." if flacone_con_mila and fiducia_genitori >= 2:
                $ fiducia_genitori += 1
                jump finale_rottura

            "Entro con il flacone, anche se temo che non mi crederanno." if flacone_con_mila and fiducia_genitori < 2:
                $ fiducia_genitori += 1
                jump finale_rottura

            "Mi fido di mio padre e gli dico dov'è il flacone." if not flacone_con_mila and fiducia_genitori >= 2:
                $ fiducia_genitori += 1
                jump finale_rottura

            "Dico ai miei genitori dove ho lasciato il flacone, senza sapere se mi crederanno." if not flacone_con_mila and fiducia_genitori < 2:
                $ fiducia_genitori += 1
                jump finale_rottura

            "Le dico che voglio seguirla e tengo il flacone con me." if flacone_con_mila and fiducia_sophie >= 3:
                $ dubbi_di_mila += 1
                jump capitolo_5

            "Fingo di seguirla e tengo il flacone con me." if flacone_con_mila and fiducia_sophie < 3:
                $ dubbi_di_mila += 1
                jump capitolo_5

            "Seguo Sophie senza recuperare il flacone." if not flacone_con_mila and fiducia_sophie >= 3:
                $ dubbi_di_mila += 1
                jump capitolo_5

            "Fingo di seguire Sophie e lascio il flacone nella neve." if not flacone_con_mila and fiducia_sophie < 3:
                $ dubbi_di_mila += 1
                jump capitolo_5
    else:
        "Non ho abbastanza certezze. Ho solo la paura di essere di nuovo sola."
        jump capitolo_5


label capitolo_5:
    scene bg mila kitchen
    with fade
    play music audio.room fadeout 1.0 fadein 1.5
    play sound audio.heartbeat

    centered "{size=42}{color=#e6d4db}CAPITOLO 5{/color}{/size}\n\n{size=28}{color=#aa97a3}Il diorama{/color}{/size}"

    "La tavola è apparecchiata. Mia madre ha cucinato lasagne. Papà ha scelto il vino che piaceva a mia nonna."
    "Ogni gesto può essere amore. Ogni gesto può essere una menzogna."
    if flacone_con_mila:
        "Il flacone pesa nella mia tasca. Sophie aspetta nella finestra della villetta accanto."
    else:
        "Il flacone è rimasto nella neve, sotto la quercia. Sophie aspetta nella finestra della villetta accanto."

    if fiducia_sophie >= 3:
        "La promessa di una vita con Sophie conserva ancora un potere su di me. È proprio questo che rende difficile distinguere il desiderio dalla paura."
    elif fiducia_sophie <= 0:
        "Non riesco più a confondere la dolcezza di Sophie con la sicurezza: so quanto può cambiare tono quando la contraddico."
    else:
        "Una parte di me le crede ancora; un'altra ha imparato a non scambiare il sollievo per una prova."

    if indizi_reali >= 4:
        "Ho conservato abbastanza dettagli da raccontare una sequenza precisa, non soltanto la mia paura."
    else:
        "I miei ricordi sono reali, ma alcune prove sono incomplete. Dovrò chiedere aiuto senza fingere di sapere tutto."

    if fiducia_genitori >= 2:
        "Penso a mio padre: forse posso cominciare da una sola verità e lasciare che mi ascolti."
    else:
        "Non so come reagiranno i miei genitori. So soltanto che tacere non renderà questa scelta più sicura."

    menu:
        "Questa è l'ultima scelta prima che la storia si chiuda."

        "Verso le gocce nei bicchieri." if flacone_con_mila:
            $ fiducia_sophie += 2
            jump finale_fascicolo

        "Dico tutto ai miei genitori, che ora so di poter ascoltare." if flacone_con_mila and fiducia_genitori >= 2:
            $ fiducia_genitori += 1
            jump finale_rottura

        "Dico tutto ai miei genitori, anche se temo che non mi crederanno." if flacone_con_mila and fiducia_genitori < 2:
            $ fiducia_genitori += 1
            jump finale_rottura

        "Dico tutto ai miei genitori e spiego dove ho lasciato il flacone." if not flacone_con_mila and fiducia_genitori >= 2:
            $ fiducia_genitori += 1
            jump finale_rottura

        "Dico ai miei genitori dove ho lasciato il flacone, anche se temo che non mi crederanno." if not flacone_con_mila and fiducia_genitori < 2:
            $ fiducia_genitori += 1
            jump finale_rottura

        "Scappo da casa e raggiungo Sophie.":
            jump finale_fuga


label finale_verita:
    scene bg school
    with fade
    stop music fadeout 2.0

    if legame_kate >= 3:
        "Kate risponde quasi subito. Il filo che Mila ha tenuto aperto con lei basta a farle capire che questa volta non si tratta di un litigio."
    else:
        "Kate esita quando sente la voce di Mila, ma resta in linea. Mila le dà la posizione e chiede che le prove vengano conservate prima che qualcuno le tocchi."

    if indizi_reali >= 4:
        "Telefono, immagini e appunti permettono di ricostruire una sequenza verificabile. Non risolvono tutto in una notte, ma non sono più soltanto ricordi isolati."
    else:
        "Le prove sono frammentarie e alcune domande restano aperte. Kate e sua madre aiutano Mila a conservarle e a raccontare ciò che sa senza inventare ciò che non sa."

    "Sophie continua a sorridere. Per la prima volta, però, nessuno le lascia decidere quale storia raccontare."
    "Mila non guarisce come in una favola. Comincia a parlare, ed è più difficile. È anche più vero."
    centered "{size=42}{color=#e6d4db}FINALE: LA VERITÀ HA UNA VOCE{/color}{/size}"
    return


label finale_rottura:
    scene bg mila kitchen
    with fade
    stop music fadeout 2.0

    if flacone_con_mila:
        play sound audio.glass
        "Mila rovescia il contenuto del flacone nel lavandino. Il vetro batte contro l'acciaio."
        "Suo padre chiama aiuto. Sua madre resta accanto a lei, senza tentare di spiegare via il suo terrore."
    else:
        "Mila racconta ai genitori quanto è successo e indica il punto sotto la quercia in cui ha lasciato il flacone."
        "Suo padre esce a recuperarlo e poi chiama aiuto. Sua madre resta accanto a Mila, senza tentare di spiegare via il suo terrore."

    if fiducia_genitori >= 2:
        "Mio padre non mi chiede di mettere in ordine ogni ricordo prima di credermi. Gli basta che io gli dica dove cominciare."
    else:
        "Le parole mi escono a pezzi. Non so se i miei genitori capiscano tutto, ma per la prima volta non torno indietro per proteggerli dal mio racconto."

    "Fuori, Sophie comprende che il suo copione non funzionerà. La sua voce diventa fredda, finalmente priva di carezze."
    "Non è una riconciliazione perfetta. È una porta che resta aperta."
    centered "{size=42}{color=#e6d4db}FINALE: LA PORTA APERTA{/color}{/size}"
    return


label finale_fuga:
    scene bg oak houses
    with fade
    play music audio.rain fadeout 1.0 fadein 1.5
    "Mila corre verso la quercia. Sophie l'aspetta con uno zaino troppo piccolo per una vita nuova."
    if flacone_con_mila:
        "Il flacone è ancora con me. Non so più se sia una prova o una promessa."
    else:
        "Il flacone è rimasto nella neve. Non torno indietro a riprenderlo."
    "Il treno parte prima dell'alba. Per qualche ora, la libertà ha il rumore dei binari."
    "Poi Sophie prende il telefono di Mila, lo spegne e dice che ora non serve più nessuno."
    if fiducia_sophie >= 3:
        "Voglio credere che lo faccia per proteggerci. Per qualche secondo, trasformo anche questo gesto in una prova d'amore."
    else:
        "Questa volta riconosco il gesto per quello che è: Sophie decide chi posso sentire e quando posso parlare."
    "Mila guarda il vetro. Il suo riflesso sembra una bambola seduta accanto a una ragazza che non sbatte mai le palpebre."
    centered "{size=42}{color=#e6d4db}FINALE: LA FUGA ILLUSORIA{/color}{/size}"
    return


label finale_fascicolo:
    scene bg title night
    with fade
    play sound audio.heartbeat
    stop music fadeout 2.0
    "La storia si spezza in rumori, sirene e pagine scritte con una grafia ordinata."
    "Nei giorni successivi, gli adulti troveranno il quaderno e lo chiameranno confessione."
    if fiducia_sophie >= 3:
        "Mila ha creduto così a lungo alla versione di Sophie che alcune frasi false le sembrano ancora ricordi propri."
    else:
        "Mila aveva già intravisto le crepe, ma non è riuscita a trasformare i sospetti in una prova condivisa prima che fosse troppo tardi."
    "Sophie sarà la superstite perfetta: spaventata, silenziosa, impossibile da accusare."
    "Da qualche parte, Kate rileggerà un messaggio rimasto senza risposta e capirà troppo tardi che Mila aveva provato a parlarle."
    centered "{size=42}{color=#e6d4db}FINALE: IL FASCICOLO{/color}{/size}"
    return
