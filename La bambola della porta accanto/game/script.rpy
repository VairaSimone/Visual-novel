# La Bambola della Porta Accanto
# Vertical slice iniziale: prologo, prima scelta e variabili narrative.

define mila = Character("Mila", color="#d9c4d6")
define sophie = Character("Sophie", color="#e4b6bd")
define kate = Character("Kate", color="#c9d7ef")
define madre = Character("Mamma", color="#c6b59b")
define padre = Character("Papà", color="#8f9aa8")
define madre_sophie = Character("Madre di Sophie", color="#c6b59b")

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

# Attiva la variante visiva delle scelte decisive; è salvata insieme alla partita.
default tensione_scena = False

# SCELTE INVESTIGATIVE: registrano cosa Mila ha fatto davvero con ogni prova.
default telefono_condiviso_kate = False
default telefono_risposto_sophie = False
default telefono_nascosto = False
default fotografia_conservata = False
default fotografia_distrutta = False
default fotografia_digitalizzata = False
default immagini_verificate = False
default immagini_credute = False
default immagini_condivise_kate = False
default quaderno_fedele = False
default quaderno_manipolato = False
default quaderno_vuoto = False

# SCELTE DI RELAZIONE / CONSEGUENZE IRREVERSIBILI.
default padre_ascoltato = False
default padre_confrontato = False
default padre_evitato = False
default prontezza_aiuto = 0  # Disponibilità emotiva a chiedere aiuto, distinta dalla fiducia.
default testimonianza_padre = False  # Riscontro alternativo se la fotografia è stata distrutta.
default promessa_a_sophie = False
default flacone_indagato = False
default genitori_salvati = False
default genitori_sedati = False
default telefonata_registrata = False
default sophie_smascherata = False
default scelta_finale = ""
default soldi_rubati = False
default soldi_parziali = False

label start:
    scene bg title night
    with fade
    play ambience audio.room fadein 1.5
    play music audio.investigation fadein 1.8

    centered "{size=32}{color=#e6d4db}AVVISO CONTENUTI{/color}{/size}\n\n{size=21}Thriller psicologico con manipolazione, gaslighting, abusi emotivi, autolesionismo e violenza. La storia affronta anche lutto e suicidio. Alcune scene sono intense.{/size}"

    centered "{size=54}{color=#e6d4db}LA BAMBOLA DELLA PORTA ACCANTO{/color}{/size}\n\n{size=26}{color=#aa97a3}Una visual novel thriller psicologica{/color}{/size}\n\n{size=20}Fino a che punto ti spingeresti per sentirti finalmente libera?{/size}"

    scene bg mila room
    with dissolve

    "Il primo suono della giornata non è mai la sveglia. È lo scatto metallico dell'accendino nell'altra stanza."
    play sound audio.lighter
    "Un clic secco. Poi il primo sospiro di fumo di mia madre. È quello il segnale: ho esattamente sei minuti prima che mi chiami."
    "Li ho contati una volta, un anno fa, con il cronometro del telefono. Sei minuti e undici secondi. Da allora li conto tutte le mattine, anche se nessuno me l'ha mai chiesto."
    "Sei minuti per smettere di esistere come individuo e diventare una funzione della casa."
    "Mi alzo senza far scricchiolare le doghe. È un'arte che ho perfezionato in anni di attenzione e paura. La mia stanza è un piccolo diorama di ciò che una brava figlia dovrebbe essere: libri allineati, letto teso, nessuna macchia. Non è pulizia. È una strategia di difesa. Meno angoli offro, meno appigli avrà lei."
    madre "Mila."
    "La voce attraversa la porta come un ago freddo. Mia madre non urla. Le grida sono per i dilettanti; lei usa la pressione atmosferica."
    "Esco in corridoio abbassando le spalle, rendendomi piccola. In bagno provo a coprire il viola sotto gli occhi. Nello specchio, sotto lo zigomo destro, c'è una linea sottile, bianca, quasi invisibile se non sai dov'è."
    "Una vecchia cicatrice. Non ricordo sempre da dove venga. So soltanto che, quando la sfioro, sento paura; e in questa casa la paura sembra sempre una prova a carico di qualcuno."
    scene bg mila kitchen
    with dissolve
    "Mia madre è seduta al tavolo, avvolta in una vestaglia sbiadita. Mio padre è una sagoma indistinta dietro il giornale. La sua indifferenza è diventata, nella mia testa, il carburante della crudeltà di lei."
    "Appoggio la tazzina sul legno chiaro. La ceramica sfiora il piano con un rumore minuscolo. Mamma osserva il caffè, poi alza gli occhi. Sono stanchi, grigi, del colore delle sigarette consumate nel posacenere."
    madre "Ti sei truccata?"
    mila "No, mamma. Solo un po' di correttore per le occhiaie."
    madre "Cos'è quel fango sotto gli occhi, Mila? Smetti di truccarti come se avessi dieci anni in più. La gente guarda, la gente sparla. Vuoi far credere ai vicini che in questa casa non ti facciamo dormire?"
    "Sento il sapore del ferro in gola. Per mia madre la realtà non sembra esistere: conta il giudizio degli altri, il terrore che qualcuno scalfisca la facciata della famiglia perfetta."
    mila "Lo tolgo subito."
    madre "Brava. E stasera vai dai vicini. Hanno di nuovo bisogno di te per la ragazzina. Vedi di non fare la morta di sonno come al solito."
    "Non finisce la frase. Non serve. Spinge verso il bordo del tavolo lo yogurt già aperto. Devo scattare per afferrarlo prima che cada. Una piccola umiliazione, appena prima di colazione."
    "Mio padre gira pagina. Non alza gli occhi. Non c'è mai nessun testimone di quello che mi sembra succedere in questa casa. O almeno, è così che mi sono abituata a raccontarmelo."
    "Prima di alzarmi, guardo mio padre per un secondo di troppo."
    menu:
        "Quando papà incrocia il mio sguardo, cosa faccio?"
        "Gli chiedo se va tutto bene.":
            $ padre_ascoltato = True
            $ prontezza_aiuto += 1
            $ fiducia_genitori += 1
            padre "Sì, Mila. Sono solo stanco."
            "La risposta è piccola, insufficiente. Ma per un attimo ho provato a parlare invece di indovinare cosa pensasse."
        "Abbasso gli occhi e mi sbrigo.":
            $ padre_evitato = True
            "È più facile non chiedere. Se non sento una risposta, posso continuare a immaginare che non ce ne sarebbe stata una."
    scene bg school
    with dissolve
    play ambience audio.rain fadeout 1.0 fadein 1.5
    "Fuori l'aria sa di asfalto umido e libertà vigilata. A scuola sono Mila la brava: quella che prende nove in matematica, non disturba e sorride quanto basta per non far nascere domande."
    "Kate mi raggiunge correndo, le guance arrossate dal freddo. È l'incarnazione di un mondo di carta velina: brillante, rumoroso, ignaro. Mi circonda le spalle con un braccio; devo fare uno sforzo per non sussultare. Per me, un tocco improvviso annuncia ancora un colpo."
    kate "Mila! Aspettami! Ancora quella faccia da funerale? Stasera c'è la festa da Leo. Devi venire. Ci sarà anche quel tipo del terzo anno che ti fissava in biblioteca."
    menu:
        "Come le rispondo?"
        "Le spiego che devo lavorare dai vicini.":
            $ legame_kate += 1
            mila "Non posso, Kate. Devo lavorare."
            kate "Ancora a fare da balia alla vicina? Ma ha quindici anni. Che problemi ha?"
            mila "I suoi tornano tardi. Mi pagano per aiutarla con i compiti e scaldarle la cena. A me va benissimo."
            kate "Sei troppo responsabile. A volte sembri un robot."
            "Le sorrido. Un sorriso provato allo specchio: le labbra si sollevano, gli occhi si stringono il giusto, ma dietro non c'è nessuno."
        "Taglio corto prima che possa chiedermi altro.":
            $ dubbi_di_mila += 1
            mila "Non posso. Devo rendermi utile, tutto qui."
            kate "Non devi sempre fare tutto da sola."
            "Vorrei crederle. Ma l'idea che qualcuno possa davvero aiutarmi mi sembra più irreale di qualunque punizione."
    scene bg oak houses
    with dissolve
    "Alle diciannove sono davanti alla casa dei vicini. La villetta è impeccabile, quasi gemella della nostra. Tra le due corre una striscia di prato rasato così corto da sembrare finto; al centro cresce una vecchia quercia che nessuno dei proprietari ha mai voluto abbattere."
    "Qui l'aria è diversa. Non è l'ossigeno pesante di casa mia: è un vuoto sterile, profumato di ammorbidente costoso."
    "I genitori di Sophie mi accolgono con la gentilezza distaccata riservata a chi svolge bene il proprio lavoro."
    "La madre si sistema il cappotto color cammello e mi rivolge un sorriso educato."
    madre_sophie "Sophie è di sopra. Ultimamente è stata difficile. Cerca di farla mangiare e niente schermi dopo le dieci, per favore."
    "La porta si chiude alle mie spalle. Il silenzio di lusso della casa mi avvolge. Salgo le scale fino alla porta coperta di adesivi di vecchi anime e scritte KEEP OUT."
    "Busso con il ritmo che ci siamo inventate tre anni prima, quando loro si sono trasferiti. Busso ogni volta: è l'unica porta al mondo su cui mi è concesso bussare invece di essere convocata."
    sophie "Entra, Mila. Lo sai che con me non devi bussare. Sei l'unica persona che non mi dà il mal di testa in questa casa."
    scene bg sophie room
    with dissolve
    "Sophie è sdraiata sul letto, le cuffie al collo, un joystick tra le mani. Ha quindici anni; è cresciuta in verticale, spigolosa e pallida, e sembra già troppo grande per la stanza che i suoi genitori le hanno preparato."
    "Sulla carta sono lì per fare da tutor e darle una mano la sera. Chiamarlo babysitting per una quindicenne suona ridicolo, ma per i suoi genitori è il modo più comodo per non lasciarla sola e delegare a me il problema di una figlia difficile."
    "Ogni volta che varco questa soglia, però, la mappa delle nostre età sembra cancellarsi. Sophie mi osserva come se avesse capito troppo presto che il mondo degli adulti è una recita mediocre. Di fronte a lei, sono io a sentirmi piccola."
    mila "Ciao, Sophie."
    "Spegne lo schermo e mi fissa. Il suo sguardo ha l'intensità di un bambino che trova un insetto raro e decide di chiuderlo in un barattolo per studiarlo da vicino."
    sophie "Pensavo che tua madre ti avesse murata viva o che fossi scappata. Dio, Mila, mi sei mancata. Ma eccoti qua. Di nuovo a farti consumare da tutti."
    mila "I miei non me lo permetterebbero."
    sophie "Permetterebbero. Che parola del cazzo."
    "Si alza. È quasi alta quanto me. Mi prende il mento fra due dita e sfrega il pollice sullo zigomo destro, proprio sopra la cicatrice. La sua mano è calda; la mia pelle, come sempre, è fredda."
    sophie "Hai ancora quella faccia spaventata. Ti trema persino la mascella. Solo io me ne accorgo. Solo io so cosa ti ci vorrebbe per respirare davvero."
    mila "Sophie, devo preparare la cena. I tuoi mi pagano per..."
    sophie "I miei non capiscono niente. E tu non sei qui per i loro soldi. Sei qui perché sono l'unica che ti vede davvero."
    "Il cuore accelera. Non è paura, mi dico. È qualcosa di più pericoloso: la sensazione di essere vista."
    sophie "Voglio che tu smetta di tremare quando ti tocco. Siamo rimaste solo io e te, Mila. I tuoi sono mostri, i miei manichini. Tu sei mia. Io ti salverò da loro. Devi solo lasciarti aiutare."
    "Mi scosto. Ha quindici anni, io diciotto. Dovrei essere io a rassicurarla, a prepararle la cena, a dirle che gli adulti a volte sono stanchi e basta. Invece sto in piedi davanti a una ragazzina con le calze a orsetti e aspetto il permesso di respirare."
    mila "Siamo qui per i compiti e la cena, Sophie. Non per questo."
    sophie "Questo cosa? Volerti bene?"
    "Torna a sedersi sul letto e mi regala un sorriso bellissimo che non le arriva agli occhi. Sono sbarrati e freddi, come se stesse già guardando il finale di una partita a scacchi che ha deciso di vincere anni fa."
    sophie "Va bene. Prepariamo il pollo. Recitiamo la parte. Fai la brava ospite. Ma non sei brava a fingere, Mila. Accumula pure tutta questa rabbia. Un giorno la useremo insieme contro di lei. Ora vai."
    scene bg sophie kitchen
    with dissolve
    "Scendo in cucina e lavo le mani più a lungo del necessario. Mentre l'acqua bolle, noto un quaderno di schizzi aperto sul tavolo. Il disegno è dettagliatissimo: io, rannicchiata in un angolo, con fili sottili legati ai polsi e alle caviglie che scompaiono oltre il bordo del foglio."
    "Sotto, con la grafia ordinata di Sophie, c'è scritto: La mia bambola preferita."
    "Sorrido debolmente. Mi sembra dolce che mi abbia ritratta, che abbia notato ogni dettaglio. Lei mi vuole bene davvero. Mi protegge."
    "Guardo dalla finestra la sagoma scura di casa mia, a pochi metri. Per la prima volta l'idea di tornarci non mi provoca soltanto nausea. Mi provoca una tristezza sofferente."
    "Sophie ha ragione, penso. Chi non prova nulla è fortunato. Io invece sento ogni frequenza del dolore, e sta diventando troppo pesante da portare."
    jump capitolo_1


label capitolo_1:
    scene bg sophie kitchen
    with fade
    play ambience audio.room fadeout 1.0 fadein 1.2
    centered "{size=42}{color=#e6d4db}CAPITOLO 1{/color}{/size}\n\n{size=28}{color=#aa97a3}Come sanguina un robot{/color}{/size}"
    "Preparo il pollo con movimenti automatici, quasi ipnotici. Taglio, soffriggo, mescolo: una coreografia che potrei eseguire bendata. Mia madre dice che sono efficiente. In realtà sono terrorizzata dall'errore."
    "Sophie non è rimasta in camera. È seduta sull'isola della cucina, le gambe che dondolano nel vuoto, e osserva ogni movimento."
    sophie "Sai, Mila, i miei dicono che sei un esempio. Guarda Mila: non risponde mai male, ha sempre la camicia stirata, non si lamenta."
    mila "I tuoi sono gentili."
    sophie "No. I miei sono pigri. Ti usano come standard per non ammettere che non hanno idea di chi io sia. Ma io ti guardo. Guarda come stringi quel coltello: hai le nocche bianche."
    "Abbasso gli occhi. Ha ragione. Tengo il manico come se fosse l'unica cosa che mi impedisce di scivolare via dalla realtà. Rilasso le dita, una alla volta."
    mila "È solo stanchezza."
    sophie "È rabbia. La rabbia di chi soffoca per non disturbare. Mi piace da morire. È l'unica cosa vera che hai. Scommetto che se ti ferissi chiederesti scusa al pavimento per averlo sporcato."
    "Mi volto bruscamente. Il calore dei fornelli mi scotta le guance, o forse è il rossore che mi tradisce."
    mila "Perché mi dici queste cose? Dovresti giocare ai videogiochi. Dovresti essere una ragazzina."
    sophie "E tu dovresti essere viva, Mila. Guarda questo posto: una cella dorata. La tua, invece, è una cella di cemento. Voglio tirarti fuori prima che ti distruggano. Voglio vedere chi sei quando smetti di essere il loro robot."
    "Mi prende una mano. Aspetta una reazione, un grido, uno schiaffo. Io abbasso lo sguardo."
    mila "La cena è pronta."
    "Mangiamo in silenzio. Il pollo ha il sapore del cartone bagnato. Sophie mangia svogliatamente e ogni tanto controlla l'orologio. La aiuto con latino; è brillante, ma si rifiuta di applicarsi per puro dispetto verso i professori del suo istituto, che chiama il reparto psichiatrico a pagamento."
    "Verso le undici, i suoi genitori non sono ancora rientrati. Il panico comincia a strisciare sotto la mia pelle. Devo essere a casa alle undici e un quarto. Se arrivo tardi, mia madre troverà un nuovo motivo per farmi sentire colpevole."
    mila "Devo andare, Sophie. I tuoi arriveranno a momenti."
    sophie "Resta qui. Dormi nel letto degli ospiti. Di' ai tuoi che devi aiutarmi."
    mila "Non posso mentire. Lei capisce sempre quando mento."
    sophie "E allora? Che cosa farà? Ti farà sentire ancora più insignificante? Ti lascerà un altro segno da nascondere?"
    "Mi blocco davanti alla porta. Le parole risuonano come una condanna."
    mila "Non è così semplice."
    sophie "È semplicissimo. Ma tu hai paura della libertà quanto hai paura di lei."
    "Si avvicina, mi posa una mano sulla spalla e stringe un po' troppo."
    sophie "Mi si spezza il cuore a vederti così. Almeno qui sei umana. Con me puoi smettere di fingere."
    "Per un istante il mondo si restringe al profumo del suo shampoo e al calore del suo respiro. Penso che stia per baciarmi sulla guancia. Invece sussurra:"
    sophie "Vai a casa, Mila. Corri dal tuo mostro. Fatti fare tutto quello che deve. Così capirai che l'unico posto sicuro è qui. Ricorda: la mia porta non è mai chiusa a chiave per te."
    scene bg oak houses
    with dissolve
    "Corro nella notte. L'aria fredda mi taglia i polmoni. Attraverso il prato e salgo i gradini. Sono le 23:18: tre minuti di ritardo."
    "Infilo la chiave nella toppa. La porta si apre. E basta. Non è chiusa dall'interno. Mi fermo sulla soglia, con la chiave ancora in mano. Mi dico che è stata una dimenticanza, che sono fortunata, che la prossima volta sarà diverso."
    scene bg mila kitchen
    with dissolve
    "La luce della cucina taglia il corridoio buio. Mio padre è seduto in poltrona, con la TV spenta."
    padre "È in cucina."
    "Non è un avvertimento. È una constatazione."
    "Mia madre lava una tazzina. Lentamente. Il rumore della spugna sulla ceramica è l'unico suono nella stanza."
    madre "Il lavoro è finito?"
    mila "Sì, mamma. Mi dispiace per il ritardo, io..."
    madre "La madre di Sophie mi ha scritto. Dice che la ragazzina non si sente a suo agio con te. Non sai fare nemmeno l'unica cosa per cui ti pagano: stare zitta e non disturbare. Vai in una casa altrui e ci fai fare la figura dei miserabili."
    "Si avvicina e mi afferra la mascella con tre dita, costringendomi a guardarla. Le sue unghie si piantano nella pelle; le dita odorano di detersivo e cenere spenta."
    madre "Che cosa vi siete dette? Hai raccontato le tue storielle da vittima per farti compatire?"
    mila "No. Abbiamo solo studiato."
    madre "Non mentirmi. Pensi che sia stupida? Ti ho dato una casa, da mangiare, ti ho tirata su per essere normale. E tu ripaghi la mia pazienza facendoti guardare dai vicini come se fossi pazza da curare."
    "Afferra uno strofinaccio umido e me lo strofina sulla guancia. Il tessuto ruvido gratta la pelle irritata. Nella mia testa non è più un tentativo di pulirmi: è un gesto deliberato per cancellarmi il viso, per punirmi per aver osato truccarmi."
    madre "Togliti questo schifo dalla faccia. Fai schifo quando cerchi di fare la grande."
    "Resto immobile, stringendo i pugni. Mio padre appare sulla soglia, guarda la scena con gli occhi vuoti di chi osserva un mobile da spostare, poi si gira e se ne va."
    "Mia madre mi spinge contro lo spigolo del tavolo."
    madre "Sparisci dalla mia vista. Vai in camera tua e non uscire prima di domattina."
    scene bg mila room
    with dissolve
    "Mi trascino in camera vestita. Non piango: le lacrime sono un lusso che non posso permettermi. Sotto il cuscino trovo un frammento di vetro raccolto in giardino. Lo stringo fino a sentire dolore e subito dopo vergogna per averlo fatto."
    "Mi dico che questo dolore è onesto, che almeno non cerca di convincermi di essere per il mio bene. Non so più se sia una verità mia o una frase che qualcun altro mi ha insegnato."
    "Sento ancora il pollice di Sophie sotto lo zigomo. Voglio vedere chi sei quando smetti di essere il loro robot."
    "Chiudo gli occhi. L'odio per i miei genitori e il desiderio di tornare nella villetta sterile si intrecciano in un nodo impossibile da sciogliere. Qualcosa dentro di me si è incrinato. La tempesta è appena iniziata."
    jump capitolo_2


label capitolo_2:
    scene bg mila kitchen
    with fade
    play ambience audio.room fadeout 1.0 fadein 1.5
    centered "{size=42}{color=#e6d4db}CAPITOLO 2{/color}{/size}\n\n{size=28}{color=#aa97a3}La geometria del silenzio{/color}{/size}"
    "Il taglio sulla mano brucia sotto l'acqua fredda. È un dolore netto, a differenza delle parole di mia madre, che cercano sempre di convincermi che ogni cosa sia per il mio bene."
    "Mi asciugo con cura, tamponando la pelle per non macchiare l'asciugamano bianco. In questa casa le macchie diventano prove, e ogni prova può trasformarsi in un'accusa."
    "A colazione mio padre è già uscito. Mia madre è seduta al solito posto. Davanti a lei c'è il mio smartphone. Lo accarezza con la punta dell'indice, come un piccolo animale catturato di cui studia la resistenza."
    madre "Seduta."
    "Obbedisco. Non guardo il telefono; tengo gli occhi sulle mani intrecciate in grembo."
    madre "Stanotte non ho chiuso occhio. Mi chiedo dove ho sbagliato con te. Che cosa ti passa per la testa quando ti guardi intorno come un animale in gabbia? Vedo come ti assenti, come ti irrigidisci ogni volta che qualcuno ti parla."
    mila "Mamma, stavamo solo..."
    madre "Silenzio. Non ti ho dato il permesso di inquinare l'aria con altre menzogne."
    "Copre il telefono con il palmo."
    madre "Questo resterà a me. Non ne hai bisogno per andare a scuola. E dopo l'ultima ora tornerai dritta qui. Ho parlato di nuovo con la madre di Sophie. Le ho spiegato che stai attraversando un periodo difficile e che è meglio sospendere il lavoro per un po'."
    "Il mondo mi crolla addosso, ma non faccio rumore. Le cose che devono apparire perfette non esplodono: implodono, collassando verso il proprio centro vuoto."
    mila "Ma lei ha bisogno di me."
    madre "Siamo noi ad avere bisogno che tu guarisca. È stata sua madre a tirare fuori l'argomento. Mi ha detto che Sophie ti trova strana. Che la metti a disagio."
    "So che qualcosa è distorto. Sophie non direbbe mai una cosa simile. Eppure il dubbio si insinua: e se anche Sophie stesse recitando? Il dubbio non deve essere vero per fare danni; basta respirarlo."
    scene bg school
    with dissolve
    "A scuola mi muovo come un guscio vuoto. Senza telefono sono isolata; ma è l'isolamento mentale a soffocarmi."
    "Kate mi intercetta vicino agli armadietti."
    kate "Mila! Da ieri sera sei sparita. Ti ho scritto un sacco di messaggi. Stamattina ha risposto tua madre, dicendomi che eri malata e di non cercarti. E invece sei qui. Che cosa succede?"
    "Guardo la sua preoccupazione, sincera e pulita, e per la prima volta mi irrita. Lei può permettersi di preoccuparsi per gli altri. La sua casa profuma di torta e bucato, non di cenere e rancore."
    menu:
        "Kate aspetta una risposta."
        "Le dico che ho solo bisogno di un po' di spazio.":
            $ legame_kate += 1
            mila "Non sto bene. Non so come parlarne, ma non è colpa tua."
            kate "Va bene. Non ti forzo. Però ci sono."
            "La sua risposta non risolve nulla. Proprio per questo mi mette in difficoltà: non prova a scegliere al posto mio."
        "La respingo con rabbia.":
            $ legame_kate -= 1
            $ dubbi_di_mila += 1
            mila "Ho detto lasciami stare!"
            "Il mio urlo taglia il corridoio. Kate arretra, colpita come da uno schiaffo invisibile. Le tremano appena le labbra."
            "Ho appena fatto saltare in aria un ponte con la normalità. La cosa più terrificante è che, per un istante, mi sento bene. Se devo affogare, perché lei dovrebbe restare all'asciutto?"
    "Torno a casa alle 14:10. Mia madre è nell'ingresso e controlla l'orologio. La porta della camera deve restare aperta. Studio alla scrivania di spalle, dove lei può sorvegliare la mia postura, la mia presenza, il mio silenzio."
    "Verso le cinque, mentre la luce si fa radente e grigia, un picchiettio leggerissimo colpisce il vetro della finestra sul retro."
    play sound audio.window_knock
    "Toc. Toc-toc."
    "Sposto gli occhi senza muovere la testa. Sul davanzale esterno c'è un piccolo bullone avvolto in un foglio colorato, legato a un filo da pesca trasparente che risale verso la quercia."
    "Sento i passi di mia madre in corridoio. Premo la penna sul quaderno finché l'inchiostro non crea una macchia densa. Lei si ferma sulla soglia, controlla la mia schiena dritta, poi si allontana."
    "Quando la televisione si accende in soggiorno, apro la finestra di pochi centimetri e afferro il foglio. La carta è strappata da un taccuino e profuma dello shampoo alla ciliegia di Sophie."
    "{i}So che ti ha preso il telefono. So cosa ti ha detto. Mia madre ha provato a dirmi che sei strana, ma l'ho messa all'angolo finché non si è tirata indietro. Non crederle. Lei non ti vede. Io sì.{/i}"
    "{i}Ti scrivo così perché di giorno tua madre guarda il vialetto dalla cucina e di notte non dorme. Ma la mattina, dalle sei alle sei e un quarto, è sotto la doccia. Sono gli unici quindici minuti in cui la tua porta esiste.{/i}"
    "{i}Guarda sotto il tappetino domani prima di uscire. Ti ho lasciato un regalo. Una chiave per il nostro mondo.{/i}"
    "{i}Non farti spegnere. Mi servi accesa. — S.{/i}"
    "Il cuore mi martella. Mi servi accesa. Non è un ti voglio bene, non è una frase da adolescenti: sembra un comando e una pretesa su un pezzo della mia anima. Sophie sta combattendo per me. O sta solo giocando a scacchi con mia madre usando il mio corpo come scacchiera. Non mi importa."
    "Quella notte non dormo. Dalla porta aperta vedo il bagliore rosso della sigaretta di mia madre, che si accende e si spegne nel buio come un faro che nessuno guarda da anni."
    "Poi un rumore metallico taglia il silenzio: mia madre sistema i coltelli nel ceppo di legno, uno alla volta. Clac. Clac. Clac. Una minaccia senza parole, almeno nella mia interpretazione."
    "Domani prenderò quello che Sophie ha lasciato sotto il tappetino. Non so se sarà la salvezza o la rovina. A questo punto la differenza sembra aver smesso di importare."
    jump capitolo_3


label capitolo_3:
    scene bg mila room
    with fade
    play ambience audio.room fadeout 1.0 fadein 1.5
    centered "{size=42}{color=#e6d4db}CAPITOLO 3{/color}{/size}\n\n{size=28}{color=#aa97a3}Frequenze d'ombra{/color}{/size}"
    "La mattina ha un colore giallastro, come la bile. Mi sveglio con il sapore metallico della paura in gola, reduce da un sogno in cui cercavo di gridare ma dalla bocca uscivano cocci di vetro."
    "Il rituale della casa non cambia: il clic dell'accendino, il rumore delle pantofole di mio padre, il silenzio pressurizzato che precede la prima parola di mia madre."
    "Mamma è di spalle in cucina, immobile davanti alla finestra."
    madre "Le chiavi sono sul mobile dell'ingresso. Torna subito dopo l'ultima ora. Oggi pulirò a fondo la tua stanza. Ogni singolo angolo."
    "È una dichiarazione di guerra. Vuole dire che non avrò nascondigli, che persino i miei pensieri sono soggetti a ispezione."
    "Prendo zaino e chiavi. Mi chino davanti al tappetino fingendo di allacciarmi una scarpa. Sotto c'è una busta di plastica nera, piatta, sigillata con nastro adesivo. La faccio scivolare nella manica."
    "Non apro il pacchetto finché non sono chiusa nell'ultimo bagno del secondo piano a scuola, quello con lo scarico rotto e l'odore di umido. Dentro c'è un telefono vecchio, economico, lo schermo graffiato. La batteria è staccata; la SIM è già inserita."
    "{i}Accendimi. Codice 0000. Non salvarmi tra i contatti. Nessuno può risalire a noi.{/i}"
    play sound audio.phone
    "Premo il tasto di accensione. La luce bluastra illumina il viso pallido nello specchio macchiato. C'è già un messaggio."
    "{i}S: Sapevo che l'avresti preso. Brava ragazza. Ora siamo connesse. Tua madre può chiudere la porta quanto vuole: io sono già dentro.{/i}"
    "Brava ragazza. La frase di mia madre quando avevo sei anni e tornavo a casa con un quaderno pieno di stelline. Detta da Sophie suona come un invito al peccato piuttosto che alla virtù."
    mila "Perché lo fai? Mia madre dice che tua madre mi trova strana. Che le faccio paura."
    "La risposta arriva dopo tre secondi."
    "{i}Mia madre ripete quello che le dice la tua. Le donne come loro si passano le paure come le ricette. È tua madre che ha paura, Mila. Ha paura che tu ti svegli e capisca quanto lei sia piccola, fragile, inutile. Io non ho paura di te. Ci vediamo stanotte, alle 02:00. Sotto la quercia. Non mancare.{/i}"
    "{i}E scrivi. Tutto quello che ti fanno oggi, ogni parola. Ti servirà quando qualcuno finalmente ti chiederà com'era.{/i}"
    "Scrivo da mesi, da quando Sophie me lo ha chiesto per la prima volta, in ottobre. Scrivi tutto, Mila. Altrimenti domani ti convinceranno che non è successo. Ho un quaderno nero nascosto sotto la rete del materasso, e dentro c'è la mia anima, o quello che ne hanno lasciato."
    menu:
        "Il quaderno nero è aperto sulle mie ginocchia. Che cosa ci scrivo?"
        "Annotazioni precise: soltanto ciò che ho visto e sentito.":
            $ quaderno_fedele = True
            $ indizi_reali += 1
            $ dubbi_di_mila += 1
            "Scrivo date, frasi esatte e gesti che posso descrivere senza interpretare. La pagina sembra fredda, impersonale, ma almeno le parole sono mie."
        "Scrivo quello che Sophie dice che è successo.":
            $ quaderno_manipolato = True
            $ fiducia_sophie += 2
            "Sophie detta piano, senza guardarmi. Quando finisco, corregge una parola e mi chiede di riscrivere la frase. La sua grafia e la mia cominciano a sembrare la stessa voce."
        "Chiudo il quaderno e lascio le pagine vuote.":
            $ quaderno_vuoto = True
            $ dubbi_di_mila += 1
            "Non voglio scrivere qualcosa che domani potrebbe sembrare una prova. Chiudo la copertina, ma il quaderno resta sul letto come una domanda senza risposta."
    "In quarta ora il professore di filosofia spiega il carcere perfetto: un luogo in cui i prigionieri non sanno mai quando la guardia li sta osservando e, nel dubbio, cominciano a sorvegliarsi da soli. Sento un sorriso amaro tirarmi le labbra. Mia madre, nella mia testa, applica questa tortura da diciotto anni senza aver mai letto il libro."
    "A pranzo Kate tenta di sedersi accanto a me sui gradini."
    kate "Se hai bisogno di un posto dove stare per qualche giorno, i miei sarebbero felici di ospitarti. Davvero."
    "Il suo maglione color pastello si muove quando tormenta l'orlo della manica. Le parole sono semplici, ma la mia testa ci costruisce una trappola."
    menu:
        "Che cosa faccio della mano tesa di Kate?"
        "Le dico che non posso parlarne, ma le chiedo di non sparire.":
            $ legame_kate += 1
            mila "Non riesco a spiegartelo adesso. Ma... grazie."
            kate "Non devi spiegarmi tutto oggi."
        "Le dico di lasciarmi in pace.":
            $ legame_kate -= 1
            mila "Sto bene, Kate. Lasciami stare."
            "Kate si alza senza protestare. Il vassoio le trema appena tra le mani."
    "Torno a casa alle due e dieci. Appena apro la camera, lo zaino mi scivola dalle spalle. Mia madre è davanti all'armadio: ha svuotato i ripiani, rovesciato i cassetti e ammucchiato i vestiti sul letto come cadaveri in una fossa comune."
    "In mano stringe il diario scolastico. Lo sfoglia con disprezzo, ma anche con una specie d'angoscia."
    madre "Cercavo la verità, Mila. Qui dentro ci sono soltanto compiti, date, orari. Sei davvero così vuota o sei diventata spaventosamente brava a nasconderti?"
    "Allunga le mani per perquisirmi. Prima che mi afferri, lascio scivolare il telefono segreto nel groviglio dei maglioni e lo seppellisco sotto la lana."
    madre "Cos'hai in tasca?"
    mila "Fazzoletti."
    "Li strappa dalla mia mano, li controlla come se cercasse tracce di sangue, poi li lascia cadere a terra."
    madre "Sei patetica. Guardati, tremi come una foglia."
    "Mi spinge contro lo stipite e si ricompone subito, tornando a indossare la sua maschera."
    madre "Rimetti in ordine questa stanza. Stasera abbiamo ospiti. Servirai a tavola e sorriderai. Se vedo anche solo un accenno della tua faccia da martire, ti tolgo anche il letto."
    "Quando se ne va, recupero il telefono. Lo schermo si illumina immediatamente."
    "{i}S: L'hai sentita, vero? La scarica di adrenalina nel petto. È meglio di qualsiasi droga, Mila. A stanotte.{/i}"
    "Per la prima volta non mi sento solo una vittima in attesa della prossima punizione. Sophie non mi ha regalato soltanto un telefono: mi ha dato il permesso di odiare."
    menu:
        "Il telefono segreto è acceso tra le mani."
        "Rispondo a Sophie e le prometto che sarò sotto la quercia.":
            $ telefono_risposto_sophie = True
            $ fiducia_sophie += 2
            $ promessa_a_sophie = True
            "{i}S: Sapevo che avresti scelto noi.{/i}"
        "Non rispondo. Lo spengo e lo nascondo.":
            $ telefono_nascosto = True
            $ dubbi_di_mila += 1
            "Per la prima volta tengo qualcosa che Sophie non sa di controllare."
        "Invio a Kate una fotografia del messaggio prima di spegnerlo.":
            $ telefono_condiviso_kate = True
            $ legame_kate += 2
            $ indizi_reali += 1
            kate "Non so ancora cosa significhi, ma lo conservo. Non devi decidere da sola."
    jump capitolo_4


label capitolo_4:
    scene bg oak houses
    with fade
    play ambience audio.rain fadeout 1.0 fadein 1.5
    play music audio.tension fadeout 1.0 fadein 1.4
    centered "{size=42}{color=#e6d4db}CAPITOLO 4{/color}{/size}\n\n{size=28}{color=#aa97a3}Radici di notte{/color}{/size}"
    "La cena con i colleghi di mio padre si è trascinata per ore come un'estrazione a freddo eseguita con le buone maniere. Ho servito risotto ai funghi camminando sul filo invisibile che mia madre tesse con gli sguardi."
    "Davanti alla moglie del capufficio, mamma mi ha accarezzato la schiena."
    madre "Vedi come si è fatta carina, Mila? Anche se ultimamente è così pallida. Studia troppo, vero cara?"
    "La sua mano era calda, ma io ho sentito soltanto un artiglio pronto a stringersi se avessi sbagliato a posare la brocca."
    "Ora sono le 01:47. Il silenzio non è vuoto: è un organismo vivo, fatto di scricchiolii del legno e del respiro pesante di mio padre dall'altra parte della parete. Mia madre non russa. Nella mia immaginazione giace nel buio come un ragno al centro della tela, in attesa di una vibrazione sbagliata."
    "Mi sono vestita sotto le coperte, movimento dopo movimento, per non far frusciare la giacca. Sono in piedi con le scarpe in mano. Il corridoio è una gola nera. Devo passare davanti alla camera dei miei e raggiungere l'ingresso; il pavimento ha un punto vicino al tavolino del telefono fisso che geme se lo calpesto troppo forte. Lo chiamo il nervo scoperto."
    "Avanzo millimetro dopo millimetro, distribuendo il peso come se camminassi su un lago ghiacciato. Passo davanti alla loro porta socchiusa. Per un istante giurerei che gli occhi di mia madre siano aperti, puntati sulla fessura, a contare le mie pulsazioni."
    play sound audio.door
    "La serratura scatta. Mi immobilizzo: uno, due, tre. Nessun rumore. Esco e richiudo con una lentezza millimetrica."
    "L'aria notturna mi schiaffeggia il viso. Sa di asfalto umido e libertà rubata. Per qualche secondo mi sento leggera, come se avessi perso dieci chili di catene."
    "La vecchia quercia svetta tra le due villette. Le radici sollevano il bordo del vialetto come costole spinte sotto la pelle. Sophie è seduta su un ramo basso, le gambe che dondolano nel vuoto. Indossa una felpa nera troppo grande; dalle maniche spuntano le calze con gli orsetti e le sneakers slacciate. I capelli biondi sono gonfi di vento, le lentiggini le fanno ancora il viso di una bambina. Sta masticando un lecca-lecca alla ciliegia."
    "Nel buio sembra una bambolina di porcellana smarrita nel bosco, non un predatore."
    sophie "Ce l'hai fatta, allora."
    mila "Ho rischiato di morire."
    sophie "Non si muore per un corridoio, Mila. Si muore perché non si ha il coraggio di attraversarlo."
    "Salta giù dal ramo e prende le mie mani. Le dita sono calde, lisce, incredibilmente morbide."
    sophie "Guarda la tua casa. Sembra una tomba, vero? È lì che vogliono che tu stia: sepolta viva a servire il caffè e pulire i pavimenti finché diventerai identica a lei. Grigia. Spenta."
    mila "Mia madre dice che sono strana. Forse ha ragione. Una persona normale non scapperebbe di casa alle due di notte per vedere una ragazzina sotto un albero."
    "Sophie ridacchia, una risata cristallina che finisce troppo in fretta."
    sophie "Normale. Che parola disgustosa. È il paravento dietro cui i deboli nascondono la loro ipocrisia. Tua madre non ha paura che tu sia pazza: ha paura che tu sia sveglia. Ha paura che tu scelga me."
    "Sfila dalla tasca un accendino di metallo argentato e lo fa scattare. La fiamma illumina le sue guance. Per un secondo sembra un angelo che gioca con il fuoco."
    sophie "Voglio mostrarti un segreto che i manichini di casa mia non conoscono."
    "Si tira su la manica sinistra. Sulla pelle bianca c'è una serie di piccole bruciature circolari, guarite e allineate. Non sembrano nate da un impulso singolo; la loro regolarità è quasi geometrica."
    mila "Chi ti ha fatto questo?"
    sophie "Io. Ogni volta che mio padre sorrideva a tavola dopo aver urlato a mia madre finché lei piangeva in bagno. Ogni volta che lei copriva i lividi con il fondotinta e faceva finta di non vedere. Volevo sentire qualcosa di reale che non fosse la loro recita. Volevo un segno che nessun altro potesse truccare."
    "Non so se crederle. So soltanto che la vista di quelle cicatrici mi fa venire voglia di proteggerla."
    sophie "Siamo uguali, Mila. Tu cerchi di aggiustarti per piacere a loro. Io cerco di distruggermi per far vedere quanto sono mostri. Nessuna delle due strade ci porterà fuori."
    "Mi mette una mano dietro la nuca, infilandosi tra i miei capelli. È un gesto dolce finché la presa non si fa troppo forte, quasi dolorosa."
    sophie "Vuoi scappare con me? Vuoi un posto senza genitori?"
    mila "Più di ogni altra cosa."
    sophie "Allora devi smettere di essere la brava Mila. Devi sporcarti le mani per davvero. Non si esce dall'inferno senza portarsi dietro un po' di fumo."
    "Si china e mi bacia. Non c'è la tenerezza ingenua che ho letto nei libri. È un gesto che mi sorprende e mi invade; le dita tra i capelli stringono finché il dolore mi mozza il fiato. Quando si stacca, il buio torna tra noi come acqua gelida."
    sophie "Ora sei mia, Mila. Non di altri. Mia."
    "Ho diciotto anni. L'ho vista arrivare con le valigie quando ne aveva dodici. Le ho tagliato le crostate e l'ho aiutata con le versioni di matematica. E ora, sotto un albero, ringrazio per essere stata scelta."
    sophie "Domani iniziamo il fondo per la fuga. Tuo padre tiene i contanti delle consulenze nel cassetto della scrivania. Devi prenderli."
    mila "Come fai a saperlo?"
    sophie "Sono stata a casa tua. Tua madre mi ha invitata per il tè perché le facevo pena. Mi ha lasciata sola in corridoio per due minuti. Ho contato stanze, porte, serrature. Chi tiene le chiavi."
    "Il modo in cui lo dice mi gela più dell'aria."
    menu:
        "Sophie mi aspetta, sicura della risposta."
        "Le prometto che prenderò i soldi.":
            $ promessa_a_sophie = True
            $ fiducia_sophie += 2
            sophie "Sapevo che avresti capito."
            "La frase mi scalda e mi spaventa nello stesso momento."
        "Le chiedo perché il nostro piano comincia con un furto.":
            $ dubbi_di_mila += 1
            sophie "Perché la libertà costa. E perché loro ci devono qualcosa."
            "Non risponde alla domanda che le ho fatto. Me ne accorgo, ma non insisto."
        "Le dico che non farò niente che possa ferire qualcuno.":
            $ dubbi_di_mila += 2
            $ prontezza_aiuto += 1
            sophie "Non sai ancora cosa significa scegliere, Mila."
            "Il sorriso le resta sulle labbra, ma le dita mi lasciano andare."
    "Rientrare è un'asfissia. Ogni ombra nel corridoio sembra avere il corpo di mia madre. Mi infilo sotto le coperte vestita; le labbra bruciano ancora e il sapore dolciastro del lecca-lecca ha lasciato un retrogusto metallico."
    "Sophie mi ha promesso la salvezza. Ma mi ha chiesto di diventare una ladra."
    jump capitolo_5


label capitolo_5:
    scene bg mila room
    with fade
    play ambience audio.room fadeout 1.0 fadein 1.5
    centered "{size=42}{color=#e6d4db}CAPITOLO 5{/color}{/size}\n\n{size=28}{color=#aa97a3}L'incisione profonda{/color}{/size}"
    "La luce del mattino filtra dalle tapparelle come una serie di sbarre dorate. Mi sento sporca, schiacciata dal peso di un segreto che pulsa come piombo caldo nelle viscere."
    "Mi alzo e vado allo specchio. Sfioro la cicatrice sotto lo zigomo, dove la notte prima Sophie ha premuto il pollice. Cerco un segno visibile del suo possesso, ma il riflesso mi restituisce la solita Mila: camicia stirata, colletto simmetrico, occhi spenti."
    scene bg mila kitchen
    with dissolve
    "A colazione mio padre mangia cereali con movimenti lenti, fissando il vuoto oltre la scatola di cartone. Dietro la pesante scrivania di mogano custodisce l'unica cosa che, nella mia testa, può comprarmi una via d'uscita."
    "I miei genitori escono alle dieci e trenta per la spesa e la lavanderia. Quando sento il motore allontanarsi, il silenzio della casa cambia frequenza: non è più protettivo, ma accusatorio. Ogni mobile sembra guardarmi."
    scene bg mila room
    with dissolve
    "Entro nello studio di papà. Odora di carta vecchia, legno trattato e tabacco spento. Il cassetto centrale è chiuso. La chiave d'ottone è dentro un finto libro rilegato in pelle sulla mensola più alta: un nascondiglio banale, quasi infantile."
    "La serratura scatta. Il cassetto scorre senza rumore. Dentro ci sono mazzette fermate da elastici: banconote da cinquanta e cento. Cinque mazzette. Cinquemila euro."
    "Non è una fortuna. È il sangue di questa casa, il frutto di anni di straordinari, rinunce e cene consumate senza rivolgersi la parola."
    play sound audio.phone
    "Il telefono segreto vibra contro la coscia."
    "{i}S: Fallo e basta, Mila. Non pensare al valore della carta. Pensa al valore della tua vita con me. Prendili tutti e non lasciare tracce.{/i}"
    "Allungo la mano e la nausea mi sale dallo stomaco. Se prendo quei soldi, il confine crollerà per sempre. Diventerò un predatore che si nutre dei resti degli altri."
    menu:
        "La mia mano è sospesa sopra le banconote."
        "Le prendo tutte e cinque le mazzette.":
            $ soldi_rubati = True
            $ soldi_parziali = False
            $ fiducia_sophie += 2
            $ promessa_a_sophie = True
            "Le infilo sul fondo dello zaino, sotto il libro di chimica. Il peso fisico è minimo, eppure mi sembra di trascinare un cadavere caldo."
        "Prendo una parte dei soldi, ma lascio un biglietto a papà.":
            $ soldi_rubati = True
            $ soldi_parziali = True
            $ fiducia_sophie += 1
            $ dubbi_di_mila += 1
            $ indizi_reali += 1
            "Scrivo soltanto: Mi dispiace. Non so ancora a chi sto chiedendo perdono. Lascio il biglietto dove possa trovarlo."
        "Richiudo il cassetto e non prendo niente.":
            $ dubbi_di_mila += 2
            $ prontezza_aiuto += 1
            "Rimetto la chiave al suo posto. Per un istante la paura di Sophie è meno forte della certezza che sto per fare qualcosa di irreparabile."
            "Esco dallo studio. Non ho preso i soldi, ma Sophie si aspetta che lo faccia. So che questa scelta avrà un prezzo."
    "Prima di richiudere il cassetto noto una busta azzurra, sgualcita, nascosta sotto vecchie fatture. Dentro c'è una fotografia di mia madre da giovane, con i capelli lunghi e liberi, mentre tiene in braccio una neonata avvolta in una copertina azzurra. Sorride, davvero. C'è una luce che non le vedo più da anni."
    "Sul retro, con la grafia tremolante ma dolcissima, una data di diciotto anni prima e una frase: Perché tutto sia perfetto."
    "Quella bambina sono io. È la prova che forse sono esistita prima di questa casa, e mio padre l'ha tenuta in fondo a un cassetto chiuso a chiave, sotto le bollette, come si conserva una cosa che fa troppo male da guardare."
    "Per un momento provo una pietà atroce. Forse mia madre non è nata mostro. Forse ha cercato di costruirmi un guscio per non farmi del male e, nel farlo, ha finito per chiudermi dentro."
    menu:
        "La fotografia è fragile tra le dita."
        "La conservo senza rovinarla.":
            $ fotografia_conservata = True
            $ indizi_reali += 1
            "La rimetto nella busta e la infilo tra le pagine di un libro. Non so cosa provi, ma non voglio distruggerla."
        "La fotografo con il telefono segreto.":
            $ fotografia_digitalizzata = True
            $ indizi_reali += 1
            "Scatto una foto al fronte e al retro. La copia non spiega la frase, ma non può essere strappata nello stesso modo. Rimetto l'originale nella busta azzurra e la busta al suo posto."
        "La strappo, poi mi pento e raccolgo i pezzi.":
            $ fotografia_distrutta = True
            $ fiducia_sophie += 1
            "La carta si rompe più facilmente di quanto pensassi. Raccolgo ogni frammento, ma so che non potrò ricostruirla senza lasciare tracce."
    scene bg mila kitchen
    with dissolve
    "Alle 11:12 l'auto rientra. Sono in cucina, con le mani immerse nell'acqua saponata. Il getto copre il tremito del respiro."
    madre "Brava, Mila. Vedi che quando ti impegni sai essere la figlia che meritiamo? Senza tutte quelle stranezze in testa."
    "Mi accarezza i capelli, un gesto insolito. Il tocco mi brucia come acido. Lo zaino abbandonato in camera sembra urlare la verità attraverso i muri."
    "Vorrei restituire le mazzette, chiederle perché ha smesso di sorridere come nella fotografia. So che non riuscirei a farlo."
    "Più tardi accendo il telefono sotto le coperte."
    if soldi_rubati:
        if soldi_parziali:
            "{i}M: Ho preso una parte. Non potevo prendere tutto.{/i}"
            "{i}S: Una parte basta per cominciare. Stanotte porta quello che hai alla quercia.{/i}"
        else:
            "{i}M: Ho preso i soldi. Tutti. Cinquemila.{/i}"
            "{i}S: Sapevo che avresti scelto noi. Brava ragazza. Ora sei veramente sveglia. Stanotte porta il pacco alla quercia.{/i}"
    else:
        "{i}M: Non li ho presi. Non riesco a farlo.{/i}"
        "{i}S: Non è il denaro che mi interessa, Mila. È sapere se farai quello che serve quando te lo chiederò.{/i}"
    if soldi_rubati:
        "Fisso lo schermo. Scegliere noi. Sfilo le banconote dagli elastici: odorano di cassetti chiusi e di mani che hanno lavorato troppo. Per la prima volta l'orrore lascia spazio a un brivido di onnipotenza. Ho il loro futuro in mano."
    else:
        "Fisso lo schermo. Non ho preso i soldi. Il messaggio di Sophie arriva dopo pochi secondi: una sola parola, Scegli. Non so se sto difendendo i miei genitori o soltanto rimandando il momento in cui dovrò affrontarla."
    "Non sono più soltanto la vittima. Sono una complice. E la cenere che ho ingoiato per diciott'anni comincia a trasformarsi in un incendio."
    jump capitolo_6


label capitolo_6:
    scene bg oak houses
    with fade
    play ambience audio.rain fadeout 1.0 fadein 1.4
    play music audio.tension fadeout 1.0 fadein 1.5
    centered "{size=42}{color=#e6d4db}CAPITOLO 6{/color}{/size}\n\n{size=28}{color=#aa97a3}Il prezzo dell'argilla{/color}{/size}"
    "È l'01:55. La mazzetta nascosta sotto il materasso emana un calore immaginario. Non è ricchezza; è il peso geometrico di un tradimento che mi ha resa un'estranea dentro casa mia."
    "Esco di nuovo nella notte. Il corridoio non mi fa più paura: mi fa schifo. Passo davanti alla camera dei miei senza trattenere il respiro. Se si svegliassero, forse un confronto sarebbe preferibile a questa decomposizione lenta."
    "Sotto la quercia, Sophie è in piedi nell'ombra del tronco, le braccia conserte e lo sguardo sulla finestra della mia camera. Sembra un piccolo generale davanti a una fortezza che ha già deciso di radere al suolo."
    sophie "Li hai?"
    "Non mi chiede come sto. Non mi tocca. È una transazione."
    if soldi_rubati and not soldi_parziali:
        mila "Eccoli."
    elif soldi_parziali:
        mila "Ne ho presa soltanto una parte."
    else:
        mila "Non li ho presi. Non posso farlo." 
    if fotografia_distrutta:
        "Le racconto anche della fotografia strappata. Non so perché lo faccio: forse sto cercando un'assoluzione da chi non ha intenzione di darmela."
    "Sophie apre la busta e conta le banconote alla luce bluastra del telefono."
    if soldi_rubati and not soldi_parziali:
        sophie "Cinquemila euro. Per cominciare basterà."
    elif soldi_parziali:
        sophie "Una parte soltanto. È meno di quanto mi aspettassi, ma per cominciare può bastare."
    else:
        sophie "Quindi hai disobbedito. Pensavi che ti avrei lasciata tornare a mani vuote? Il denaro era solo il primo passo, Mila. Non fingere che adesso tu sia fuori dal piano."
    mila "Cominciare cosa? Possiamo prendere un autobus per la città, cambiare nome, sparire."
    sophie "Sparire? Se scappiamo adesso ci trovano in dodici ore. Tuo padre chiama la polizia; tua madre sguinzaglia l'inferno intero pur di riaverti nella gabbia. Noi non vogliamo soltanto scappare. Vogliamo che loro non abbiano più il potere di cercarci."
    "Si siede sulle radici e mi fa cenno di avvicinarmi. Mi siedo accanto a lei, improvvisamente piccolissima, un guscio pronto a essere riempito dalla sua volontà."
    sophie "La fase due riguarda l'assicurazione. Tuo padre non denuncerà mai questo furto."
    mila "Perché non dovrebbe? Sono i risparmi della famiglia."
    sophie "Perché ho questo."
    "Sblocca lo schermo e me lo mette davanti soltanto per un istante. Documenti fotografati di traverso, pagine, colonne, intestazioni, timbri e firme. Scorre così velocemente che non riesco a leggere una riga intera."
    sophie "Conti, transazioni, mail tra mio padre e il tuo. Guarda le cifre. Guarda i nomi delle società. Gusci vuoti per far sparire i soldi. E qui, e qui: la firma di tuo padre, sempre la stessa."
    "Vedo zeri, sigle e firme. Li vedo così poco da non poterli descrivere dopo; eppure, mentre Sophie parla, la mia mente li trasforma in una confessione."
    sophie "Mio padre è un uomo d'affari sporco. Il tuo è il contabile fedele, il cagnolino che fa quadrare i bilanci. Se denunciano il furto, pubblico tutto e distruggo le loro vite. Mutua distruzione assicurata. Un equilibrio perfetto di terrore."
    menu:
        "Le immagini sono passate davanti ai miei occhi troppo in fretta."
        "Le chiedo di mostrarmi i file originali, uno alla volta.":
            $ immagini_verificate = True
            $ dubbi_di_mila += 2
            $ indizi_reali += 1
            sophie "Non ti fidi di me?"
            "Non risponde. Mi riprende il telefono e apre una cartella, ma continua a scorrere prima che io possa leggere i titoli."
            "Non ho verificato i documenti; ho verificato soltanto che Sophie non vuole lasciarmeli osservare."
        "Le credo: non voglio perdere anche lei.":
            $ immagini_credute = True
            $ fiducia_sophie += 2
            "Le cifre continuano a muoversi dietro le mie palpebre anche dopo che ha spento lo schermo."
        "Le chiedo di mandarne una copia a Kate.":
            $ immagini_condivise_kate = True
            $ legame_kate += 1
            $ indizi_reali += 1
            sophie "Non mettere in mezzo nessun altro."
            "La sua risposta è più rapida del necessario. Kate riceve solo un'immagine prima che Sophie chiuda la cartella."
    mila "Quindi mi hai usata per arrivare ai soldi?"
    "Sophie mi afferra il mento, costringendomi a guardarla."
    sophie "Ti ho liberata. Ti ho mostrato che i tuoi genitori sono fasulli. Ora non devi sentirti in colpa per aver rubato: hai preso la tua parte. Ma non basta."
    sophie "Tua madre non si fermerà davanti a un ricatto. Troverà un modo di distruggerti dall'interno. C'è solo un modo per essere libere per sempre: dobbiamo farli dormire profondamente, abbastanza a lungo da prendere quello che resta e sparire."
    "La proposta è così fredda che per un momento smetto di sentire il rumore del vento tra le foglie."
    sophie "Tuo padre tiene le gocce per dormire sul comodino, dietro la sveglia. Le prende da mesi. Vedi che ti ascolto quando parli?"
    "Mi sfiora la guancia e torna a baciarmi. Non so più distinguere la paura dal bisogno di essere amata."
    sophie "Fallo per noi, Mila. Fallo per me."
    "Rientro barcollando. Nella cucina è accesa la luce cruda del neon. Mia madre è seduta al tavolo. Davanti a lei c'è la busta azzurra."
    if fotografia_digitalizzata:
        "La fotografia è stata tirata fuori e strappata in due. La copia digitale è ancora nascosta nel telefono."
    elif fotografia_conservata:
        "La busta è vuota. Mia madre si è accorta che l'originale non è più al suo posto."
    elif fotografia_distrutta:
        "La busta è vuota e sgualcita. Non c'è più una fotografia da strappare: ho già distrutto l'originale."
    else:
        "La fotografia è stata tirata fuori e strappata in due."
    madre "Dov'è il resto, Mila?"
    mila "Mamma, io..."
    if soldi_rubati and not soldi_parziali:
        madre "Il cassetto dello studio è vuoto."
    elif soldi_parziali:
        madre "Hai preso i soldi dal cassetto."
    else:
        madre "La busta azzurra è sparita dal suo posto. Che cosa hai fatto, Mila?"
    "Si alza lentamente. Per un istante sembra più alta, un'ombra che occupa ogni centimetro della stanza."
    madre "Pensavi di essere l'unica a saper giocare a nascondino? Io ho inventato questo gioco tra queste pareti. Ogni respiro che fai mi appartiene. Ogni centesimo che hai preso è stato pagato con la mia pazienza."
    if soldi_rubati:
        mila "Non li ho più."
    else:
        mila "Non so come spiegartelo."
    "La mia voce, per una volta, non trema."
    mila "Sophie dice di avere documenti su di voi. Dice che li pubblicherà se proverete a fermarci."
    "Il silenzio è assoluto. La furia scompare dal volto di mia madre, sostituita da una comprensione disperata."
    madre "Ah. La ragazzina ti ha dato una voce."
    "Si siede e si copre il viso per qualche secondo."
    madre "Tuo padre fa il contabile per uno studio di geometri. Fattura ventiduemila euro l'anno. Se ci fossero società all'estero, credi che vivremmo qui, con questa cucina?"
    "Ride, e la risata le si spezza."
    madre "Chiama Kate. Chiama la scuola. Chiedi a chiunque se, in diciotto anni, ha mai visto uno di noi torcerti un capello. Ti prego. Chiedi."
    mila "Diranno quello che vuoi tu."
    madre "Certo."
    "Mi accompagna alla finestra e mi obbliga a guardare la villetta vicina. Una sola luce è accesa nel sottotetto: la stanza di Sophie."
    madre "Credi davvero che quella ragazzina ti voglia bene? Lei non cerca un'amica. Cerca un corpo vuoto da abitare. Ti ha convinta che questa casa sia un inferno così l'unica porta aperta resta la sua. Non ti sta salvando da noi. Ti sta togliendo tutto quello che non è lei."
    "Mi lascia andare. Crollo sul pavimento."
    madre "Ho chiamato la dottoressa Ferrante. Venerdì alle undici. Ho preso un permesso. Tuo padre ha chiesto l'aspettativa. Andiamo a parlare con qualcuno, e poi andiamo via da qui per un po'. Tutti e tre."
    "Venerdì alle undici: nella mia testa diventa subito la data della condanna."
    madre "Vai a letto, Mila. Ma ricordati: quando lei avrà finito di usarti, non ci sarà nessuna fotografia a ricordarti chi eri prima di tutto questo."
    "Spegne la luce. Tremo non solo per la paura delle sue parole, ma perché, per la prima volta, temo che abbia ragione."
    jump capitolo_7


label capitolo_7:
    scene bg school
    with fade
    play ambience audio.rain fadeout 1.0 fadein 1.3
    play music audio.tension fadeout 1.0 fadein 1.3
    centered "{size=42}{color=#e6d4db}CAPITOLO 7{/color}{/size}\n\n{size=28}{color=#aa97a3}Anatomia di un assedio{/color}{/size}"
    "L'aria in casa è densa, immobile, chimica. Mia madre ha smesso di urlare. È questa la sua nuova tortura, almeno così la interpreto: il silenzio assoluto."
    "A colazione posa tre tazze sul tavolo con una precisione geometrica, poi fissa un punto pochi centimetri sopra la mia testa. Mio padre è diventato cenere fredda nella mia immaginazione. Interpreto ogni suo gesto come una prova che sa del ricatto."
    "Prima di andare a scuola, però, mi ferma in corridoio. Mi posa una mano sulla spalla e la ritira subito, come se si fosse scottato."
    padre "Mila."
    "Non dice altro per dieci secondi. Ha le unghie consumate, mangiate fino alla carne."
    padre "Non so cosa ti abbiamo fatto. Ci ho pensato ogni notte e ho ripercorso tutto. Non trovo il punto. Ma se c'è, dimmelo e provo ad aggiustarlo. Dimmi solo dov'è il punto."
    "Lo guardo e vedo un criminale che cerca un patto. Non riesco ad ascoltare la domanda come una domanda."
    menu:
        "Papà aspetta una risposta. Per una volta, posso scegliere che cosa fare del suo silenzio."
        "Mi siedo con lui e provo ad ascoltarlo.":
            $ padre_ascoltato = True
            $ fiducia_genitori += 1
            $ prontezza_aiuto += 1
            padre "Non devi spiegarmi tutto in una volta."
            "Non parliamo del passato come se potesse essere risolto in una frase. Ma papà non mi chiede di dimostrare subito niente."
        "Gli chiedo perché è rimasto zitto per anni.":
            $ padre_confrontato = True
            $ dubbi_di_mila += 1
            $ prontezza_aiuto += 1
            padre "Perché avevo paura di dire la cosa sbagliata. E ho sbagliato lo stesso."
            "Non è una difesa. È una confessione imperfetta."
        "Salgo in camera senza rispondere.":
            $ padre_evitato = True
            $ fiducia_sophie += 1
            "Papà annuisce come se avesse ricevuto una risposta, poi va al lavoro."
    if fotografia_distrutta and not fotografia_digitalizzata:
        menu:
            "L'originale è perduto. Posso chiedere a papà di confermare almeno la frase che ricordo."
            "Gli chiedo se ha scritto quelle parole sul retro.":
                $ testimonianza_padre = True
                $ indizi_reali += 1
                padre "Sì. L'ho scritta quando eri appena nata. Volevo che tutto fosse perfetto perché avevo paura di non saperti proteggere."
                "La sua voce trema. La testimonianza non restituisce la fotografia, ma mi offre un riscontro che non viene da Sophie."
            "Non gli chiedo nulla.":
                "Lascio la domanda dove si trova. Per ora, la fotografia è perduta e la frase esiste soltanto nella mia memoria."
    "A scuola cerco Sophie sul telefono segreto. Non risponde. Durante la ricreazione mi rifugio nel vecchio bagno del secondo piano. Lo schermo è l'unica luce nel grigio della cabina."
    sophie "Cercavi me, Mila?"
    "Sussulto. Sophie è appoggiata allo stipite. Ha saltato le lezioni ed è arrivata fin qui. Indossa grandi occhiali scuri; quando li toglie, vedo un ematoma violaceo lungo la mandibola."
    mila "Sophie! Che cosa è successo? È stato tuo padre?"
    "Faccio per avvicinarmi; lei si ritrae con un sorriso sottile."
    sophie "Mio padre è un dilettante. Ha scoperto che frugavo nel suo computer. Ha provato a riprendersi il controllo nel solo modo che conosce."
    "Il profumo alla ciliegia è coperto da un odore di antisettico."
    sophie "La tregua è finita. Non possiamo più aspettare. Dobbiamo creare il vuoto intorno a noi."
    mila "Mamma sa del ricatto. Ha detto che mi stai usando. Ha detto che papà non guadagna abbastanza per avere società all'estero. E che domani mi porteranno da una dottoressa."
    "Sophie non batte ciglio."
    sophie "Certo che ti sto usando, Mila. Proprio come tu usi me per non affogare in quella cucina perfetta. Siamo due parassiti che hanno trovato l'ospite ideale. È la forma più pura, brutale e onesta di legame che avrai."
    "Infila una mano nella tasca e tira fuori un flacone di vetro scuro con un contagocce."
    sophie "Sono gocce prese dalla casa di tuo padre, un po' alla volta. Non li uccideranno, tranquilla. Li faranno soltanto dormire profondamente. Abbastanza a lungo perché prendiamo quello che resta e spariamo prima che possano muovere un dito."
    "Mi preme il flacone contro il palmo. Pesa come un pianeta intero. Il vetro è freddo e l'etichetta è stata staccata. Per la prima volta mi chiedo da quanto tempo Sophie abbia preparato questa scena."
    $ flacone_con_mila = True
    sophie "Fallo stasera. Domani ti portano dalla dottoressa. È questione di ore. Sai cosa succede quando una madre come la tua porta una figlia come te da un medico? Ti fanno firmare un foglio, e quel foglio dice che non sei più una persona."
    "Si avvicina al mio orecchio."
    sophie "Quando torni, lascia la porta sul retro accostata. Io devo poter entrare."
    mila "Perché, se poi ci vediamo sotto la quercia?"
    sophie "Perché da sola ti spaventi. Ti spaventi sempre. Scegli, Mila. Vuoi essere il coltello o la carne?"
    "Torno a casa con il flacone nascosto, proprio sopra il cuore. Il vetro freddo mi morde la pelle a ogni respiro."
    scene bg mila kitchen
    with dissolve
    "Ma quando apro la porta, l'odore pesante di fumo e rancore è svanito. La casa profuma di lasagne al forno: il mio piatto preferito, quello che mamma preparava solo per i compleanni."
    "Per un istante la mente vacilla. E se avessi sbagliato tutto? Potrei scusarmi, restituire i soldi, dire che è stato un errore. Potremmo sederci e provare a riparare le macchie del passato."
    madre "Mila, porti tu i bicchieri? Sono sul bancone."
    "Il vino è già versato in tre calici. Papà piega il giornale in salotto. Il flacone mi scivola tra le dita sudate."
    "Attraverso il vetro della finestra immagino Sophie sulla quercia, immobile, in attesa del mio braccio."
    "Apro il tappo. Il liquido è trasparente, inodore, limpido come acqua. La mano si blocca a mezz'aria. Cosa sto facendo? L'odore delle lasagne mi riempie i polmoni, caldo e disperatamente reale. Papà tossisce dietro il giornale: un suono familiare e inoffensivo."
    "Vorrei svuotare il flacone nel lavandino, correre in salotto e chiedere aiuto. La superficie del mio delirio si incrina. Poi la luce del sottotetto si riflette nella finestra e la voce di Sophie torna a comandare: se ti fermi ora, ti spegni."
    menu:
        "I bicchieri sono davanti a me. Non posso fingere di non sapere che cosa sto decidendo."
        "Verso le gocce nei bicchieri dei miei genitori e anche nel mio.":
            $ genitori_sedati = True
            $ fiducia_sophie += 2
            $ promessa_a_sophie = True
            "Le dita tremano come se appartenessero a chi tira i fili dal sottotetto. Verso il liquido nei tre calici: una firma sul mio stesso decreto di sottomissione."
            "Porto il vassoio a tavola."
            jump capitolo_8
        "Poso il flacone sul tavolo e dico a mia madre che ho bisogno di aiuto.":
            $ genitori_salvati = True
            $ prontezza_aiuto += 2
            $ fiducia_genitori += 2
            $ flacone_indagato = True
            "La mia voce si spezza. Non riesco a raccontare tutto, ma pronuncio la frase essenziale: Sophie mi ha chiesto di farvi dormire e io ho paura di quello che c'è nel flacone."
            jump finale_rottura
        "Chiamo Kate dalla dispensa e le mando la posizione.":
            $ genitori_salvati = True
            $ telefono_condiviso_kate = True
            $ legame_kate += 2
            $ indizi_reali += 1
            "Mi chiudo nella dispensa e mando un messaggio breve, con le mani gelate: Ho bisogno di aiuto. Vieni con un adulto. Non entrare da sola."
            jump finale_verita
    "La scelta è stata fatta. Non so ancora quanto tempo mi resterà per capirne il prezzo."
    jump capitolo_8


label capitolo_8:
    scene bg mila kitchen
    with fade
    play ambience audio.room fadeout 1.0 fadein 1.3
    play sound audio.heartbeat
    play music audio.tension fadeout 0.8 fadein 1.4
    centered "{size=42}{color=#e6d4db}CAPITOLO 8{/color}{/size}\n\n{size=28}{color=#aa97a3}Natura morta con sedativi{/color}{/size}"
    "Il risveglio è una lenta emersione da una vasca di catrame caldo. Non c'è un istante preciso in cui riapro gli occhi: c'è soltanto una transizione granulosa dal buio a un grigio opaco. La testa pesa un quintale; i pensieri si muovono nel fango. Sulla lingua resta un sapore chimico, metallico, amaro."
    "Sono ancora seduta sulla sedia di legno. Davanti a me la lasagna è diventata una massa compatta, con il grasso arancione rappreso dal passare delle ore."
    "Mio padre è seduto di fronte a me, la testa reclinata all'indietro, le labbra socchiuse in un silenzio innaturale. Non sento il suo respiro e il torace non si muove."
    mila "Papà?"
    "Gli tocco il braccio. La pelle è fredda, di un freddo denso che mi schiaccia il cuore."
    "Mi giro verso mia madre. È crollata in avanti sul tavolo, i capelli finiti nel sugo freddo. Le afferro le spalle e la scuoto."
    mila "Mamma! Mamma, svegliati!"
    "La testa scivola di lato. Le pupille sono opache e fisse. Non c'è respiro, non c'è battito. Le parole di Sophie tornano nella mia testa: non li uccideranno, dormiranno soltanto."
    "Un urlo mi sale dallo stomaco e si spezza in un rantolo. Ho ucciso i miei genitori."
    play sound audio.door
    "La porta sul retro — quella che ho lasciato accostata — si apre. Passi leggeri attraversano il corridoio."
    "Sophie entra in cucina con un impermeabile giallo trasparente e guanti azzurri in lattice. Guarda i corpi, poi me. Sorride come se stesse valutando un esperimento riuscito."
    sophie "Vedo che il farmaco ha fatto un ottimo lavoro."
    mila "Li hai uccisi!"
    "Mi scaglio contro di lei. La travolgo e la spingo contro la credenza; i piatti tintinnano nel mobile."
    mila "Cosa cazzo hai fatto? Mi avevi detto che avrebbero dormito! Mi hai mentito!"
    "Per un istante il suo volto perde la maschera. Poi la sorpresa diventa fastidio, e il fastidio rabbia. Mi afferra per i capelli e mi blocca contro il bordo del tavolo. Una mano si stringe alla mia gola."
    sophie "Chiudi quella bocca, Mila."
    "Mi manca il fiato. Provo a colpirla, ma mi tiene schiacciata accanto al viso immobile di mia madre."
    sophie "Guardali. Pensi che alla polizia importerà dei tuoi pianti? Le tue impronte sono sul flacone e sui bicchieri. C'è il tuo diario sotto il materasso, con mesi di odio scritto a mano. Io non ho toccato quel bicchiere, Mila. Sei stata tu."
    "Allenta la presa quanto basta a farmi respirare, ma non mi lascia andare."
    sophie "Se fai la pazza, andrai in prigione o in un ospedale per il resto della tua vita. Io non esisto in questa storia. Nessuno sa niente di me."
    "La dolcezza della sua voce mi gela più della violenza."
    sophie "Sei mia. Hai fatto quello che andava fatto. Li abbiamo cancellati. Ora siamo solo io e te. Ma se mi tocchi ancora, ti lascio qui con i cadaveri e chiamo io la polizia. Vuoi restare sola?"
    "La resistenza crolla. Mi accascio sul pavimento, tremando, distrutta dalla morte dei miei genitori e dall'impossibilità di tornare indietro."
    "Sophie si ricompone, sistema l'impermeabile e si passa una mano sullo zigomo arrossato."
    sophie "Brava ragazza. Ora possiamo passare all'ultimo pezzo del puzzle. I miei. I manichini."
    mila "I tuoi?"
    sophie "Pensi che ci lascerebbero andare? Mio padre userebbe ogni centesimo per darci la caccia. Mia madre piangerebbe sui giornali finché non ci trovano. Dobbiamo chiudere il cerchio. Entrambe le case devono tacere."
    "Tira fuori un secondo flacone, quasi vuoto."
    sophie "L'ho versato nel whisky prima di venire qui. A quest'ora dormono sul divano. Prendi il cuscino pesante dal divano dei tuoi e portalo tu, attraversando il prato."
    mila "Perché?"
    sophie "Perché la storia deve scriversi da sola. La ragazza della porta accanto entra di notte nella villetta vicina portando un cuscino da casa propria. Premeditazione. Alzati. Fammi vedere quanto sei brava."
    "Attraversiamo il prato alle 02:40. Il fango mi si attacca ai piedi nudi, ma non sento freddo. Il cuscino pesa come un neonato di pietra."
    scene bg sophie kitchen
    with dissolve
    "La porta sul retro è aperta. Dentro l'aria profuma di cera per mobili e lavanda, un odore sterile che mi dà la nausea."
    "I suoi genitori sono sul divano. La televisione proietta bagliori bluastri sui loro volti addormentati. Un bicchiere di cristallo è rovesciato sul tappeto, una macchia scura si allarga lentamente."
    sophie "Comincia con mia madre. È quella che fa più rumore. Finisci il rumore, Mila."
    "La donna che mi accoglieva con un sorriso distante sembra soltanto fragile. Il cuscino di velluto mi pesa tra le dita. Quando lo avvicino al suo viso, le mie braccia tremano e il tessuto scivola di lato."
    sophie "Premi!"
    "Mi blocco. Il mondo si restringe al peso del cuscino, al respiro di Sophie alle mie spalle e alla consapevolezza di stare per fare qualcosa che non potrò più disfare."
    menu:
        "Sophie mi spinge per le scapole. Il tempo si è fermato."
        "Obbedisco, incapace di oppormi alla sua pressione.":
            $ fiducia_sophie += 1
            "Le ginocchia cedono. Sophie interviene alle mie spalle e usa il proprio peso per costringermi a proseguire. Il suono che la donna emette si spegne, e il salotto ricade in un silenzio definitivo."
        "Provo a ritrarmi e a fermarla.":
            $ dubbi_di_mila += 2
            "Mi ritiro, singhiozzando, ma Sophie mi blocca e mi spinge di nuovo verso il divano. La mia resistenza non basta a fermarla: vuole che la colpa abbia il mio nome."
    "Non ho tempo per respirare. Sophie mi trascina verso l'uomo e ripete che non c'è ritorno. La mia mente si allontana dalla realtà, come se potesse salvarmi non sentendo più il corpo."
    "Quando tutto finisce, crollo sul tappeto. Le mani tremano così forte che il velluto mi scivola dalle dita."
    sophie "Vedi com'è facile? Ora siamo davvero libere. Non abbiamo più passato, nessuno che possa dirci chi siamo."
    "Guardo i guanti azzurri, ancora puliti, poi le mie mani sporche di fango e fibre. Il diorama non è andato distrutto: è stato ridisegnato. Io sono la bambola che si è sporcata le mani per mantenere pulite quelle della sua padrona."
    jump capitolo_9


label capitolo_9:
    scene bg sophie kitchen
    with fade
    play ambience audio.room fadeout 1.0 fadein 1.2
    play music audio.investigation fadeout 1.0 fadein 1.5
    centered "{size=42}{color=#e6d4db}CAPITOLO 9{/color}{/size}\n\n{size=28}{color=#aa97a3}Il diorama di porcellana{/color}{/size}"
    "L'aria nella villetta è troppo fredda. La nebbia del farmaco si dirada sotto una scarica di adrenalina gelida."
    "Sono seduta sul tappeto, le ginocchia al petto, a fissare i due corpi sul divano. Il silenzio non è più di lusso: è una palude che mi tira giù."
    "Sophie si toglie i guanti con uno schiocco secco. Si china, afferra un lembo del cuscino e comincia a strofinarmi le mani, con una forza brutale e metodica."
    "La frizione del tessuto produce un lampo bianco dietro gli occhi. La memoria si aggancia a un gesto identico: lo strofinaccio umido con cui mia madre mi aveva sfregato la faccia."
    "Non era un colpo. Era lo stesso movimento, disperato, ruvido, spaventato. L'odore del liquore sul tappeto si mescola alla ciliegia chimica dello shampoo di Sophie. D'un tratto quel profumo non sa più di salvezza. Sa di disinfettante e cappio."
    mila "Cosa fai, Sophie?"
    "Si avvicina alla credenza, prende il flacone vuoto e mi costringe ad avvolgerci le dita attorno prima di lasciarlo cadere sul pavimento."
    sophie "Faccio in modo che tutto sia coerente. La polizia troverà quattro corpi e te. La babysitter psicotica."
    mila "Noi dovevamo scappare. I documenti di tuo padre..."
    "Sophie ride piano, poi sblocca il telefono e mi mostra le immagini con la luce accesa, questa volta senza fretta."
    sophie "Guarda bene, Mila."
    "Sono fatture della lavanderia, ricevute delle spese condominiali, bollette del gas, un preventivo per potare la quercia. In fondo ai fogli c'è la firma di mio padre. Undici euro e cinquanta. Duecentotrenta. Sessantotto e quaranta. Nessuno zero in più, nessuna società fantasma."
    sophie "Erano documenti scaricati da un archivio. Te li ho mostrati al buio, mentre ti dicevo cosa stavi guardando. Non hai letto niente. Hai ascoltato le mie parole e ci hai costruito dentro un'organizzazione criminale. È bastato sussurrarti che tuo padre era un mostro, e tu hai visto l'inferno in un pezzo di carta."
    "In quella risata, qualcosa crolla. I ricordi tornano a ondate violente, nitide come schegge."
    "Tre anni fa la villetta era vuota. Poi arrivarono due persone gentili che non riuscivano ad avere figli e avevano adottato Sophie quando lei aveva dodici anni. Ricordo il trasloco: mia madre aveva preparato una torta e mio padre l'aveva aiutata a portarla di là."
    "Erano persone normali, persino noiose. Parlavano dei gerani. Il padre di Sophie non aveva mai urlato in mia presenza; una volta aveva discusso con un operaio per la potatura della quercia e si era scusato anche mentre litigava."
    "I lividi che Sophie mi aveva raccontato? Il tutore al polso della madre, dopo una frattura giocando a tennis. Me l'aveva detto lei stessa, ridendo, mentre mi pagava."
    "I miei genitori non mi hanno mai picchiata. Mai."
    "La cicatrice sotto lo zigomo era il segno di una caduta dalla bicicletta a dodici anni. Mia madre era rimasta una notte intera sulla sedia dell'ospedale tenendomi la mano."
    "Lo strofinaccio non era un abuso: nella verità che riaffiora, mia madre cercava di pulirmi una guancia sporca di correttore mentre io gridavo e la spingevo via. Ho gridato davvero. Mi sono raccontata il contrario perché il silenzio era il ruolo che mi ero assegnata."
    "Mia madre non ha mai chiuso la porta dall'interno. I sei minuti li contavo io con il cronometro. La porta della camera restava aperta perché a dodici anni avevo paura del buio e glielo avevo chiesto."
    "Ogni sbarra della mia prigione l'ho costruita io, usando le sue mani."
    mila "Tu hai pianificato tutto fin dal primo giorno."
    sophie "Sei sempre stata facile da programmare. Tre anni per costruire i tasti. Sei mesi per premerli. Dieci giorni per finire."
    "Fisso l'ematoma sulla sua mandibola. Capisco che se l'è fatto da sola. Il dolore che mi aveva mostrato come prova di un destino condiviso era un'altra scena preparata per spingermi oltre il precipizio."
    sophie "Pensi che qualcuno si metterà a cercare un'anomalia? La polizia avrà il diario. Centoquaranta pagine di odio, date e descrizioni degli abusi che ti ho suggerito. La tua grafia. Le tue date. Nessuno ha puntato una pistola alla tua mano."
    "Sophie si guarda intorno, soddisfatta come chi ha appena finito di apparecchiare."
    sophie "Troveranno il diario, le tue impronte sul flacone, le tue dita sul cuscino. E troveranno una sopravvissuta di quindici anni nel ripostiglio, tremante, incapace di parlare. Sarà la cronaca nera dell'anno: la brava ragazza che diventa una serial killer."
    mila "E il telefono? I messaggi?"
    sophie "Una SIM registrata con dati falsi. Per loro potrei essere una persona incontrata in un forum, oppure una voce che la tua mente ha inventato. Dipende da quale spiegazione è più comoda."
    "Mi porge il frammento di vetro raccolto in giardino."
    sophie "Chiudi il sipario, Mila. Fai vedere a tutti come sanguina un robot. Così il caso sarà chiuso e nessuno farà domande a una povera orfana."
    "Guardo il frammento e i suoi occhi. La prigione non era la mia casa. La prigione è questa ragazzina bionda con le lentiggini e il lecca-lecca alla ciliegia. Ho ucciso le uniche due persone che avrebbero potuto salvarmi da lei."
    "Ho diciotto anni. Lei ne ha quindici. Le ho tagliato la torta di compleanno tre volte."
    "Non voglio prendere il vetro, ma la colpa è enorme e la mia mente è esausta. Sophie aspetta, con il respiro leggero e le labbra socchiuse. Vuole vedere lo spettacolo."
    menu:
        "Per la prima volta, il copione sembra fermarsi davanti a me."
        "Non prendo il vetro. Le afferro il polso e chiamo aiuto." if indizi_reali >= 2 or telefono_condiviso_kate or immagini_condivise_kate or legame_kate >= 2 or padre_ascoltato:
            $ sophie_smascherata = True
            $ indizi_reali += 1
            $ scelta_finale = "richiesta_aiuto"
            "Le afferro il polso. Le unghie affondano nella pelle sotto le cicatrici e non lascio andare."
            "Per la prima volta il suo viso cambia. Non è paura: è fastidio, come una piega storta sul vestito."
            mila "Kate! Aiuto!"
            "La voce mi esce spezzata ma reale. Se Kate conserva il messaggio, se mio padre ha provato ad ascoltarmi, se una sola persona può ricostruire un dettaglio senza le parole di Sophie, allora non tutto è ancora nelle sue mani."
            jump finale_verita
        "Le dico che so la verità, ma non riesco a chiedere aiuto.":
            $ dubbi_di_mila += 1
            $ scelta_finale = "silenzio"
            sophie "Non hai più niente. Nessuna madre, nessun padre, nessuna Kate, nessuna casa. Hai solo me."
            "Penso a mio padre in corridoio, quando mi chiedeva dov'era il punto. Il punto non eri tu, papà. Il punto ero io. Il punto era lei."
            "Chiudo gli occhi."
            jump finale_fascicolo
        "Chiudo gli occhi e lascio che Sophie decida il finale.":
            $ scelta_finale = "finale_imposto"
            "Non prendo il vetro. Ma non riesco a muovermi, né a chiamare nessuno. Sophie mi chiude le dita intorno al frammento con la pazienza di chi veste una bambola."
            "La colpa è un peso troppo grande per le mie giunture di metallo. Sotto la colpa c'è il ricordo di mia madre seduta accanto al letto d'ospedale per un'intera notte, e non riesco a guardarlo."
            "Sophie aspetta. Io non trovo una voce."
            jump finale_fascicolo


label finale_verita:
    $ tensione_scena = False
    scene bg school
    with fade
    stop music fadeout 2.0
    play ambience audio.rain fadeout 1.0 fadein 1.4
    if genitori_salvati:
        "Kate risponde quasi subito. Quando sente la mia voce, non mi chiede di raccontare tutto in ordine. Mi dice di restare dove sono e di raggiungere un adulto."
        "Arrivano aiuto e soccorsi prima che Sophie possa imporre un'altra versione. Il flacone viene messo al sicuro; nessuno deve decidere da solo cosa contenga."
        "Mia madre non cerca di convincermi che il mio terrore è infondato. Mio padre resta accanto a me mentre provo a distinguere ciò che ho visto da ciò che Sophie mi ha insegnato a credere."
        "Non è una riconciliazione perfetta. Ci sono parole da ricostruire, fiducia da rimettere in piedi, una visita dalla dottoressa che non deve più sembrare una condanna. Per la prima volta, nessuno mi chiede una confessione perfetta prima di aiutarmi."
        centered "{size=42}{color=#e6d4db}FINALE: LA PORTA APERTA{/color}{/size}"
        return
    if sophie_smascherata:
        "La mia voce raggiunge il corridoio. Sophie mi strappa il polso, ma il gesto ha lasciato segni che non può cancellare. Kate conserva una copia dei messaggi; le immagini sono state condivise e alcuni passaggi del piano non esistono soltanto nella mia memoria."
        "La polizia non ricostruisce tutto in una notte. Ci sono quattro morti e domande a cui nessuna spiegazione rapida può rispondere. Ma la versione di Sophie non è più l'unica."
        "Per la prima volta le chiedono di ripetere la storia senza suggerirle le parole. Il suo sorriso resta fermo per qualche secondo, poi si incrina."
        "Io non posso riportare indietro nessuno. Posso soltanto dire ciò che ricordo, ammettere ciò che ho fatto e smettere di riempire i vuoti con la voce di un'altra persona."
        centered "{size=42}{color=#e6d4db}FINALE: LA VERITÀ HA TESTIMONI{/color}{/size}"
        return
    "Kate esita quando sente la mia voce, ma resta in linea. Le do la posizione e le chiedo di conservare ciò che ha ricevuto."
    if telefono_condiviso_kate and immagini_condivise_kate:
        "Kate mette a confronto il messaggio e l'immagine sospetta. Non dimostrano tutto, ma offrono un punto di partenza verificabile."
    elif indizi_reali >= 4:
        "Telefono, immagini e appunti formano una sequenza. Non risolvono tutto, ma non sono più soltanto ricordi isolati."
    else:
        "Le prove sono frammentarie. Kate mi aiuta a conservarle e ad annotare ciò che so senza inventare quello che non so."
    if fotografia_distrutta and not fotografia_digitalizzata and testimonianza_padre:
        "La fotografia non può essere aggiunta al fascicolo. Riferisco la frase che ricordo e la conferma di papà, precisando che una testimonianza non sostituisce l'originale."
    elif fotografia_distrutta and not fotografia_digitalizzata:
        "La fotografia non può essere aggiunta al fascicolo. Riferisco la frase che ricordo e chiarisco che non ho più l'originale."
    elif fotografia_conservata or fotografia_digitalizzata:
        "La fotografia originale o la copia digitale viene conservata, senza attribuirle un significato che da sola non può dimostrare."
    "Sophie continua a sorridere. Kate le pone una domanda semplice, poi aspetta. Nessuno riempie il silenzio al posto suo."
    "Racconto quello che ricordo. Quando arrivo a un punto che non so spiegare, mi fermo. Nessuno mi suggerisce le parole successive."
    centered "{size=42}{color=#e6d4db}FINALE: LA VERITÀ HA UNA VOCE{/color}{/size}"
    return


label finale_rottura:
    $ tensione_scena = False
    scene bg mila kitchen
    with fade
    stop music fadeout 2.0
    play ambience audio.room fadeout 1.0 fadein 1.3
    "Poso il flacone sul tavolo. Le parole mi escono a pezzi, senza la forma ordinata che Sophie mi ha insegnato a dare al dolore."
    if genitori_salvati:
        mila "Mi ha detto che avreste dormito. Mi ha detto che dovevo farlo per essere libera. Io non so più distinguere la verità dalla sua voce."
    else:
        mila "Sophie mi ha dato questo. Non so che cosa contenga, ma mi ha chiesto di usarlo contro di voi. Ho paura."
    "Mio padre chiama aiuto. Mia madre resta accanto a me, senza tentare di spiegare via il mio terrore."
    if padre_ascoltato:
        "Papà non mi chiede di mettere in ordine ogni ricordo prima di credermi. Si siede vicino a me come aveva fatto con la tazza di tè."
    elif padre_confrontato:
        "Gli dico che il suo silenzio mi ha ferita. Non lo perdono in un istante, ma questa volta la conversazione non viene interrotta."
    else:
        "Le parole arrivano senza ordine. Non so se capiscono tutto, ma per la prima volta non ritiro il mio racconto per proteggerli."
    "Il flacone viene affidato a chi può esaminarlo. La dottoressa Ferrante non diventa una sentenza: è una persona con cui posso provare a spiegare ciò che mi sta succedendo."
    "Fuori, Sophie comprende che il suo copione non funzionerà. La sua voce diventa fredda, priva delle carezze."
    "Non è un lieto fine perfetto. È una porta che resta aperta."
    centered "{size=42}{color=#e6d4db}FINALE: LA PORTA APERTA{/color}{/size}"
    return


label finale_fuga:
    $ tensione_scena = False
    scene bg oak houses
    with fade
    play ambience audio.rain fadeout 1.0 fadein 1.5
    play music audio.investigation fadeout 1.2 fadein 1.6
    "Mila corre verso la quercia. Sophie l'aspetta con uno zaino troppo piccolo per una vita nuova."
    if flacone_con_mila:
        "Il flacone è ancora con me. Non so più se sia una prova o una promessa."
    else:
        "Il flacone è rimasto nella neve. Non torno indietro a riprenderlo."
    "Il treno parte prima dell'alba. Per qualche ora, la libertà ha il rumore dei binari."
    "Poi Sophie prende il telefono di Mila, lo spegne e dice che ora non serve più nessuno."
    if promessa_a_sophie:
        "Mi torna in mente la promessa che le ho fatto sotto la quercia. Sophie parla come se fosse un patto, ma non mi aveva lasciato spazio per dire di no."
    elif fiducia_sophie >= 3:
        "Voglio credere che lo faccia per proteggerci. Per qualche secondo trasformo anche questo gesto in una prova d'amore."
    else:
        "Riconosco il gesto per quello che è: Sophie decide chi posso sentire e quando posso parlare."
    if telefono_condiviso_kate and immagini_condivise_kate:
        "Sophie non sa che Kate conserva delle copie. Sono lontana, ma il mio isolamento non è totale come lei crede."
    elif telefono_nascosto:
        "Il telefono che ho nascosto resta l'unico frammento non controllato da Sophie. Non basta a fermarla, ma non è scomparso."
    "Guardo il vetro. Il mio riflesso sembra una bambola seduta accanto a una ragazza che non sbatte mai le palpebre."
    centered "{size=42}{color=#e6d4db}FINALE: LA FUGA ILLUSORIA{/color}{/size}"
    return


label finale_fascicolo:
    $ tensione_scena = False
    scene bg title night
    with fade
    stop ambience fadeout 1.5
    stop music fadeout 2.0
    play sound audio.heartbeat
    "La storia si spezza in rumori, sirene e pagine scritte con una grafia ordinata. Il fascicolo verrà chiuso in undici settimane. La ricostruzione sarà definita, in conferenza stampa, di rara linearità."
    "La versione ufficiale dirà che Mila B., diciottenne, ha sedato e ucciso i propri genitori, ha attraversato il giardino con un cuscino, ha ucciso i vicini e si è tolta la vita. Cinque corpi. Una sola colpevole."
    "Le fibre sul cuscino combaciano. Le impronte sul flacone combaciano. Il quaderno recuperato sotto il materasso — centoquaranta pagine di calligrafia ordinatissima che descrivono abusi mai riscontrati — viene allegato integralmente. Il perito lo definisce un documento di eccezionale valore clinico."
    "Ci sono tre anomalie."
    "La prima: il consulente medico-legale annota su un corpo un pattern di pressione compatibile con una forza superiore a quella esprimibile da Mila nelle sue condizioni. Resta una nota a piè di pagina. Nessuno costruisce un secondo colpevole quando il primo sembra aver confessato per centoquaranta pagine."
    "Anche la concentrazione di sedativi nel sangue di Mila viene liquidata rapidamente. La relazione finale parla di una finestra di latenza, una spiegazione accomodante per i minuti che non tornano. Di fronte a un diario pieno di rabbia e a un corpo che stringe ancora un frammento di vetro, nessuno cerca discrepanze."
    "La seconda anomalia sono i tabulati. Nella tasca dei jeans viene trovato un vecchio cellulare con decine di SMS scambiati con un'utenza anonima, firmati soltanto S. L'analisi dei dispositivi ufficiali della villetta vicina non trova contatti tra Sophie e la vittima. La SIM è una prepagata estera con dati falsi."
    "La Procura conclude che S. sia una figura conosciuta da Mila su un forum, un interlocutore mai identificato, oppure una personificazione nata dal suo stato dissociativo."
    "La terza: sotto le unghie di Mila viene isolato materiale epiteliale non suo. Il profilo corrisponde alla superstite di quindici anni, rinvenuta dodici ore dopo in un ripostiglio, disidratata e incapace di formulare frasi complete."
    "La spiegazione si scrive da sola, e la scrivono gli adulti per lei: la bambina ha tentato di fermare Mila, si è divincolata, è scappata a nascondersi. Nel verbale, le tracce sono compatibili con una colluttazione difensiva."
    "È, in un certo senso, la firma più bella che Sophie abbia mai messo in fondo a un documento: qualcun altro l'ha scritta per lei."
    "I quotidiani parlano del Massacro della Porta Accanto per settimane. Il sabato pubblicano la fotografia della villetta con la quercia recintata dal nastro giallo. La domenica un editoriale molto letto parla dell'inconoscibilità dei figli."
    "Una sola voce stona. Una compagna di classe, K., diciotto anni, rilascia due dichiarazioni e scrive una lettera di quattro pagine alla Procura. Dice che Mila era cambiata, che aveva provato a offrirle ospitalità e che i genitori di Mila l'avevano chiamata tre volte in primavera per chiedere aiuto."
    "La lettera viene protocollata e archiviata. Il cronista non la cita: non c'è spazio, e comunque non aggiunge nulla. K. compare in sei parole: Non era lei. Non era lei."
    "Il pubblico ministero rilegge la lettera. Poi guarda la fotografia della superstite: una bambina bionda con le lentiggini, un braccio segnato da cicatrici allineate, e gli occhi di chi ha visto qualcosa di troppo grande."
    "Firma."
    "Tre mesi dopo, un treno attraversa la campagna."
    scene bg oak houses
    with dissolve
    "La luce del sole filtra dal finestrino, illuminando i capelli biondi di Sophie. È seduta di fronte alla sua nuova famiglia affidataria: persone benestanti, con il volto di chi crede ancora che il mondo sia un posto sicuro."
    "Accanto a lei c'è Chloe, dodici anni, trecce ordinate e uno sguardo timido, quasi spaventato da quella nuova sorella così silenziosa."
    sophie "No, grazie, mamma. Sto benissimo."
    "Sophie allunga una mano e accarezza la spalla di Chloe. La bambina sussulta, ma non si scosta. Guarda Sophie con un misto di timore e ammirazione."
    "Sophie sorride, un sorriso bellissimo che non le arriva agli occhi. Si china verso l'orecchio della bambina."
    sophie "Non devi tremare quando ti tocco, Chloe. Siamo rimaste solo io e te. Ti aiuterò a essere perfetta. Ti salverò da loro."
    "Poi si tira su la manica di pochi centimetri e mostra quattro cicatrici bianche, allineate sull'avambraccio."
    sophie "Vedi? Me l'ha fatto una bambola che non mi voleva bene. Non voleva fare la brava. Un giorno ti racconto."
    "Chloe annuisce piano. Nei suoi occhi c'è già la cosa che Sophie aspettava: pietà."
    "Il treno fende la campagna. Negli occhi freddi di Sophie si riflette il disegno del prossimo, impeccabile diorama."
    "E in un archivio ci sono quattro pagine scritte a mano da una ragazza di nome Kate, che nessuno ha voluto leggere fino in fondo."
    centered "{size=38}{color=#e6d4db}EPILOGO — LA BAMBOLA NUOVA{/color}{/size}\n\n{size=22}Non ci si accorge mai di essere diventati una bambola. Lo si scopre soltanto quando si prova a fare un passo da soli.{/size}"
    "La Bambola della Porta Accanto."
    return


define diario_mila = """
QUADERNO DI MILA
Dal fascicolo d'indagine 4082/2026 — Allegato C

Nota della Procura: il seguente materiale è estratto dal quaderno a righe con copertina rigida nera rinvenuto nella stanza di Mila B., occultato tra le maglie della rete del letto. Alcune pagine presentano sbavature d'inchiostro, parole depennate violentemente e frasi incomplete.

14 ottobre 2025

Sei minuti e undici secondi. Li ho contati anche stamattina.

Il rumore dell'accendino di mia madre nell'altra stanza è come uno sparo silenzioso. Ogni volta che lo sento, mi si stringe lo stomaco in un nodo così stretto che stento a respirare. Questa casa non è un posto dove si vive, è un posto dove si trattiene il fiato sperando che nessuno si accorga che occupi spazio.

Mia madre mi ha guardata mentre le posavo il caffè. Non ha detto niente per due minuti interi. Mi ha solo fissata con quegli occhi grigi, stanchi, cercandomi addosso una colpa che non ho ancora commesso. Mi sento sporca solo a stare sotto il suo sguardo. Mio padre era dietro il giornale, come sempre. Una sagoma di cartone. Se sparissi adesso, lui girerebbe pagina lo stesso.

Li odio. Li odio così tanto che a volte la gola mi brucia come se avessi ingoiato del vetro. Vorrei che succedesse qualcosa: un terremoto, un incendio, qualunque cosa che spezzi la prigione.

2 novembre 2025

Stasera S. mi ha detto una cosa che non riesco a togliermi dalla testa. Ero al buio e tremavo. S. mi ha preso le mani. Erano calde.

«Devi scrivere tutto, Mila. Ogni singola cosa che ti fanno. Altrimenti un giorno ti convinceranno che te lo sei inventato. Ti convinceranno che la pazza sei tu.»

Ho preso questo quaderno per custodire la verità. È il nostro segreto. Per la prima volta dopo anni, quando sono tornata a casa e ho visto la luce gialla del corridoio, non ho avuto soltanto paura. Ho pensato a S. C'è qualcuno che vede attraverso la maschera da brava figlia. L'unica presenza reale in mezzo a un mondo di fantocci.

18 dicembre 2025

Abbiamo parlato di come sarà quando andremo via. C'era neve fresca sul prato. S. mi ha descritto una casa piccola vicino al mare, senza orari e senza nessuno che controlli se mi sono truccata o se sono in ritardo.

«Niente genitori, Mila. Niente regole. Solo noi due.»

A volte mi chiedo se sono abbastanza forte per farlo.

Non devo scriverlo. Devo essere forte. Quando sono con S., l'aria di casa mia sembra meno velenosa. S. dice che sono la sua persona preferita al mondo. Nessuno me l'aveva mai detto. Mia madre mi dice solo che sono un impegno; S. mi guarda come se fossi preziosa.

3 gennaio 2026

Oggi mia madre mi ha fatto pulire lo specchio del bagno tre volte perché diceva che ci si vedevano le ditate. Mi tremavano le dita. Ho pensato di prendere una forbice e... no. Non devo pensarci.

Sono corsa da S. Lei non mi ha detto passerà, come fa Kate. S. mi ha stretto il mento finché ho smesso di piangere.

«Lasciali fare, Mila. Lascia che si consumino nella loro cattiveria. Tu sei mia. Io ti salverò da loro.»

Mi ha baciata sulla guancia, vicino alla cicatrice. Mi farei fare qualsiasi cosa pur di non perdere quel calore.

20 febbraio 2026

Ho sognato che mia madre murava la porta della mia camera lasciando solo un buco per far passare lo yogurt. Mi sono svegliata col cuore a cento. Ho guardato fuori dalla finestra. La luce era accesa. Sapevo che dall'altra parte c'era S.

Siamo sole contro di loro. I suoi genitori sono rigidi e finti; i miei sono mostri travestiti da persone perbene. Se non ci fossimo trovate, sarei già morta dentro. S. è la mia unica via d'uscita.

12 aprile 2026

La tensione è insopportabile. Sento gli sguardi di mia madre piantati sulla schiena anche quando sono di spalle. Controlla ogni movimento, ogni respiro.

Oggi ho parlato con S. della fuga. Dobbiamo accelerare i tempi.

«Le cose si fanno con precisione, Mila. Quando sarà il momento giusto, saremo libere.»

Ha ragione. Devo fidarmi, smettere di avere paura e preparare il terreno. S. è l'unica che sa guidarmi fuori dall'inferno.

28 aprile 2026

Mia madre continua a ripetermi che sono paranoica, che mi invento le cose, che ho sguardi strani. Cerca di farmi credere che la malata sia io, ma so qual è la verità.

Mio padre mi ha fissata senza dire una parola. Hanno paura perché ho capito chi sono veramente. Sotto le maschere da famiglia perfetta c'è marciume.

Quando parlo con S., la sua voce è l'unica cosa che mi tiene ancorata alla realtà. Mi ricorda che loro sono finzioni, marionette scricchiolanti, e noi le uniche persone vive.

5 maggio 2026

Non dormo più. Il veleno di questa casa mi soffoca. Ogni stanza puzza di trappola. Mia madre mi guarda come se stesse decidendo dove riporre il mio cadavere.

Ieri ho guardato S. negli occhi e ho visto la stessa determinazione. Nessun dubbio, nessuna esitazione.

«Niente più catene. Presto sarà tutto finito.»

Vorrei che fosse già domani. Vorrei non dover più respirare la stessa aria di questi due mostri.

7 maggio 2026

Non so cosa succederà stasera. Mia madre mi ha perquisito la stanza e ha detto che venerdì mi porta da una dottoressa. Vuole togliermi anche l'aria. Nascondo questo quaderno sotto il materasso, nell'unico posto dove le sue mani non possono arrivare a stroppiarlo.

Stasera si chiuderà tutto. Non ho più paura.

Se domani saremo lontane da qui, vicino al mare con S., forse riuscirò a dimenticare il rumore dell'accendino. Forse riuscirò finalmente a respirare.

Nota di chiusura del fascicolo: il quaderno si interrompe a pagina 84. Le ultime pagine risultano bianche. Alcune pagine sono state strappate e non sono presenti.
"""

define frammenti_mila = """
FRAMMENTI DEL QUADERNO
Nota: sono tuttora nascosti in un luogo che solo Mila conosceva e che nessuno ha mai perquisito.

14 novembre

Mamma oggi mi ha guardato per dieci minuti interi mentre mi allacciavo le scarpe. Non ha detto una parola. Poi ha sospirato e si è avvicinata per sistemarmi il colletto della camicia. L'ha fatto con una ruvidezza strana, ma senza farmi male.

Sophie dice che quando mamma fa così cerca di soffocarmi, che vuole cancellare ogni segno della mia personalità per farmi diventare come lei. Io le ho creduto. L'ho scritto anche nella pagina prima, come voleva Sophie.

Ma stasera mi è tornato in mente un ricordo di quando avevo sette anni. Avevo la polmonite e la febbre non scendeva. Mamma è rimasta seduta al bordo del letto per tre notti. Mi metteva pezze bagnate sulla fronte e piangeva piano, convinta che dormissi.

«Prendi me, Dio. Fai stare male me, ma lascia respirare lei.»

Perché adesso quel ricordo mi sembra un delitto? Perché quando sono con Sophie la voce di mia madre diventa fredda nella mia testa? Vorrei appoggiare la testa sul suo grembo e chiederle scusa per come la guardo. Ma Sophie direbbe che sono debole, che sono ancora un robot.

Ho così tanta paura che Sophie smetta di guardarmi.

19 aprile

Sophie mi ha baciato stasera sotto la quercia. Aveva le labbra fredde, che sapevano di lecca-lecca alla ciliegia e di qualcosa di amaro, come il ferro.

«Sei la mia bambola preferita, Mila.»

Quando lo dice, per un secondo mi sento viva. Mi sento vista, scelta, importante.

Poi torno a casa e trovo mia madre seduta al buio con la sigaretta accesa. Capisco cosa sto diventando. Non sono più la figlia di nessuno: sono un'ombra. Sophie vuole che odi questa casa con tutta me stessa. Io mi sforzo di vedere veleno in ogni gesto.

Eppure ho trovato un mio vecchio disegno delle elementari dietro la porta della dispensa. C'eravamo noi tre, disegnati con pennarelli spuntati, una casa gialla e un sole enorme. Mamma l'ha plastificato con il nastro adesivo per non farlo rovinare dall'umidità. Lo conserva da dieci anni.

Se mi odiano così tanto come dice Sophie, perché mamma conserva ancora il disegno di quando la amavo?

Forse la casa non è una prigione. Forse sono io che sono rotta dentro.

7 maggio

Ho visto la fotografia azzurra, nascosta sul fondo del cassetto di papà. Mamma era così giovane. Teneva me tra le braccia come se fossi la cosa più preziosa e fragile dell'universo. Sul retro, papà aveva scritto: «Perché tutto sia perfetto.»

Non era l'ossessione per il giudizio dei vicini. Era amore: terrorizzato, maldestro, incapace di trovare le parole giuste. Mamma voleva che la mia vita fosse perfetta perché la sua era stata troppo dura. Voleva costruirmi un guscio per non farmi del male.

E io l'ho scambiato per una prigione.

Sophie mi ha dato le gocce. Il flacone scuro mi morde la pelle attraverso la tasca. Mi ha promesso che dormiranno soltanto, che sarà un sonno lungo per permetterci di scappare insieme. Ma il cuore martella così forte che ho paura mi si spacchi il petto.

Stasera mamma ha cucinato le lasagne. Si è messa il vestito verde scuro che usa solo per le feste. Le tremavano le mani mentre versava l'acqua.

«Ho preparato tutto questo solo per te, Mila.»

Vorrei rovesciare il tavolo, buttare i bicchieri nel lavandino, correre da papà e dirgli che mi dispiace. Ma dalla finestra vedo la luce di Sophie nel sottotetto. È lì. Mi fissa.

Se non lo faccio, Sophie mi abbandonerà. Se non lo faccio, tornerò invisibile nel buio. Ho diciotto anni e mi sento morta da sempre.

Mamma, papà, se sto per fare quello che penso, vi prego: non credete a quello che troveranno scritto. Sappiate che non ero io.

Era la bambola.

Senza data

A chiunque trovi questo foglio.

Non credete al quaderno sotto il materasso. Le parole scritte lì non sono mie. Sophie le ha dettate mese dopo mese, frase dopo frase. Mi faceva ripetere tutto finché non lo scrivevo esattamente. Voleva costruire una storia. Voleva che odiassi le due persone che mi hanno voluto bene davvero.

I miei genitori non mi hanno mai abusata. Mio padre era un uomo buono e silenzioso. Mia madre piangeva la notte perché vedeva che mi stavo spegnendo e non sapeva come salvarmi da se stessa e dal mondo.

Se questo foglio è tra le vostre mani e loro non ci sono più, significa che avrò ceduto. Avrò versato quelle gocce nei loro bicchieri perché sono troppo spaventata per dire di no a una ragazzina che mi faceva sentire speciale mentre mi scavava la fossa.

Se state leggendo, forse sarò già morta insieme a loro. Non abbiate pietà di me: sono un mostro per aver creduto alle sue bugie invece che agli occhi di mia madre.

Ma vi prego, guardate Sophie. Guardatela negli occhi quando vi sorride. Guardate come vi tocca. Guardate le sue mani pulite mentre tutti gli altri sanguinano. Non lasciatela avvicinare a nessun altro.

Mamma, papà, sto arrivando. Stasera la casa è buia, ma non ho più paura del buio. Ho solo tanto, tanto freddo.
"""

# ARCHIVIO INVESTIGATIVO
init python:
    if "archivio_hotkey" not in config.overlay_screens:
        config.overlay_screens.append("archivio_hotkey")


screen archivio_hotkey():
    zorder 190
    key "i" action If(renpy.get_screen("archivio_indizi"), Hide("archivio_indizi"), Show("archivio_indizi"))
    textbutton "ARCHIVIO  ·  I":
        xalign 0.985
        yalign 0.965
        action If(renpy.get_screen("archivio_indizi"), Hide("archivio_indizi"), Show("archivio_indizi"))
        text_size 16
        text_color "#e6d4db"
        text_hover_color "#ffffff"
        background Solid("#211a25dd")
        padding (14, 8)


screen archivio_indizi():
    modal True
    zorder 200
    key "K_ESCAPE" action Hide("archivio_indizi")
    add Solid("#100d14e8")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1040
        ysize 700
        background Solid("#211a25")
        padding (30, 24)
        vbox:
            spacing 12
            hbox:
                xfill True
                vbox:
                    spacing 3
                    text "ARCHIVIO INVESTIGATIVO" size 32 color "#e6d4db"
                    text "Quello che so, quello che sospetto, quello che manca." size 17 color "#c2b4c5"
                null width 20
                vbox:
                    spacing 4
                    textbutton "DOCUMENTI ORIGINALI" action Show("documenti_mila") text_size 16
                    textbutton "CHIUDI  ·  I" action Hide("archivio_indizi") text_size 18
            frame:
                xfill True
                background Solid("#352a3a")
                padding (14, 10)
                vbox:
                    spacing 4
                    text "LEGENDA" size 16 color "#e4b6bd"
                    text "CONFERMATO: un oggetto, messaggio o azione che Mila ha davvero conservato o verificato." size 15
                    text "IPOTESI: un'interpretazione ancora da dimostrare. Un sospetto non è una prova." size 15
                    text "MANCANTE: una prova persa, non raccolta o non ancora confrontata." size 15
            viewport:
                xfill True
                ysize 515
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    spacing 14
                    text "1. TELEFONO ANONIMO" size 22 color "#e4b6bd"
                    if telefono_condiviso_kate:
                        text "CONFERMATO · Kate ha ricevuto il messaggio e ne conserva una copia. È una traccia indipendente dalla memoria di Mila." size 17
                    elif telefono_nascosto:
                        text "CONFERMATO · Il telefono è nascosto e il messaggio resta disponibile. Nessun'altra persona ne ha una copia." size 17
                    elif telefono_risposto_sophie:
                        text "CONFERMATO · Mila ha risposto a Sophie. Il contatto è reale; il contenuto del messaggio non è per questo vero." size 17
                    else:
                        text "MANCANTE · Mila non ha ancora scelto come gestire il telefono." size 17 color "#c2b4c5"
                    text "2. FOTOGRAFIA DI FAMIGLIA" size 22 color "#e4b6bd"
                    if fotografia_conservata:
                        text "CONFERMATO · L'originale è stato conservato. La frase sul retro può essere mostrata e controllata." size 17
                    elif fotografia_digitalizzata:
                        text "CONFERMATO · Esiste una copia digitale. La frase da sola non dimostra un piano." size 17
                    elif fotografia_distrutta and testimonianza_padre:
                        text "RISCONTRO ALTERNATIVO · L'originale è perduto. Papà ha confermato la frase, ma la testimonianza non permette di controllare la fotografia." size 17
                    elif fotografia_distrutta:
                        text "MANCANTE · L'originale è stato distrutto e non esiste una copia digitale." size 17 color "#d7a6a6"
                    else:
                        text "MANCANTE · La fotografia non è ancora stata esaminata." size 17 color "#c2b4c5"
                    text "3. QUADERNO NERO" size 22 color "#e4b6bd"
                    if quaderno_fedele:
                        text "CONFERMATO · Il quaderno contiene osservazioni concrete; va confrontato con altre fonti." size 17
                    elif quaderno_manipolato:
                        text "ATTENZIONE · Contiene parole suggerite e corrette da Sophie. Non è una testimonianza indipendente." size 17 color "#d7a6a6"
                    elif quaderno_vuoto:
                        text "MANCANTE · Il quaderno non contiene una ricostruzione utile." size 17 color "#c2b4c5"
                    else:
                        text "MANCANTE · Mila non ha ancora deciso cosa scrivere." size 17 color "#c2b4c5"
                    text "4. IMMAGINI MOSTRATE DA SOPHIE" size 22 color "#e4b6bd"
                    if immagini_verificate:
                        text "OSSERVAZIONE VERIFICATA · Mila ha chiesto i file originali, ma Sophie non glieli ha lasciati esaminare con calma. Il rifiuto è osservabile; la frode va ancora dimostrata." size 17
                    elif immagini_condivise_kate:
                        text "CONFRONTO ESTERNO · Kate ha ricevuto un'immagine. È un riscontro da confrontare, non una conclusione definitiva." size 17
                    elif immagini_credute:
                        text "NON VERIFICATO · Mila ha accettato le immagini senza controllarle. Le accuse non sono state dimostrate." size 17 color "#d7c2a0"
                    else:
                        text "MANCANTE · Le immagini non sono state esaminate." size 17 color "#c2b4c5"
                    text "5. FLACONE" size 22 color "#e4b6bd"
                    if flacone_indagato:
                        text "DOMANDA APERTA · Mila ha chiesto da dove venisse il flacone." size 17
                    if genitori_salvati:
                        text "STATO · Mila ha consegnato il flacone e chiesto aiuto. Il contenuto deve essere esaminato da persone competenti." size 17
                    elif genitori_sedati:
                        text "STATO · Il flacone è stato usato. La scena e le conseguenze sono ormai irreversibili." size 17
                    else:
                        text "STATO · Il contenuto e l'intenzione di Sophie restano da accertare." size 17
                    text "CONFRONTI E IPOTESI" size 22 color "#e4b6bd"
                    if telefono_condiviso_kate and immagini_condivise_kate:
                        text "CONFRONTO DISPONIBILE · Kate conserva un messaggio e un'immagine. Le tracce possono essere confrontate, ma non provano automaticamente ogni accusa." size 17
                    elif fotografia_conservata or fotografia_digitalizzata:
                        text "CONFRONTO POSSIBILE · La fotografia può essere controllata da un'altra persona. Il suo significato resta ambiguo." size 17
                    else:
                        text "IPOTESI APERTA · Non esiste ancora una catena di prove sufficiente per stabilire il piano di Sophie." size 17
                    if indizi_reali >= 3:
                        text "VALUTAZIONE · Mila ha raccolto diversi elementi; quantità e certezza non sono la stessa cosa." size 17 color "#c7dfc8"
                    else:
                        text "VALUTAZIONE · La ricostruzione è incompleta. Non trasformare ogni sospetto in un fatto." size 17 color "#d7c2a0"


screen documenti_mila():
    modal True
    zorder 220
    key "K_ESCAPE" action Hide("documenti_mila")
    add Solid("#100d14f0")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1160
        ysize 780
        background Solid("#211a25")
        padding (26, 22)
        vbox:
            spacing 10
            hbox:
                xfill True
                text "DOCUMENTI DEL FASCICOLO" size 30 color "#e6d4db"
                null width 20
                textbutton "CHIUDI" action Hide("documenti_mila") text_size 18
            text "Il quaderno ufficiale e i frammenti nascosti non raccontano la stessa storia." size 17 color "#c2b4c5"
            viewport:
                xfill True
                ysize 690
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    spacing 24
                    text diario_mila size 18 color "#f0e9ed" line_spacing 5
                    null height 10
                    text frammenti_mila size 18 color "#f0e9ed" line_spacing 5
