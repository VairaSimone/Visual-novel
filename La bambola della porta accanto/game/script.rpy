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

# Controlla l'accento visivo della finestra di dialogo e delle scelte.
# La variabile deve essere inizializzata prima che Ren'Py mostri la prima schermata say.
default tensione_scena = False

# Ipotesi formulate nell'archivio: interpretazioni da confrontare, non fatti.
default ipotesi_attiva = ""
default ipotesi_sophie_solida = False
default ipotesi_genitori_sospetto = False

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
default sophie_smascherata = False
default soldi_rubati = False
default soldi_parziali = False

label start:
    scene bg title night
    with fade
    play ambience audio.room fadein 1.5
    play music audio.memory fadein 2.4

    centered "{size=30}{color=#e6d4db}AVVISO CONTENUTI{/color}{/size}\n\n{size=20}Manipolazione psicologica, gaslighting, abuso emotivo, autolesionismo, violenza, lutto e suicidio. Alcune scene possono essere intense.{/size}"

    centered "{size=42}{color=#e6d4db}LA BAMBOLA\nDELLA PORTA ACCANTO{/color}{/size}\n\n{size=25}{color=#aa97a3}Thriller psicologico interattivo{/color}{/size}\n\n{size=19}Fino a che punto ti spingeresti per sentirti libera?{/size}"

    scene bg mila room at bg_slow_push
    with dissolve
    show expression Solid("#17131d20") as prologue_tint
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_tense as mila_sprite at sprite_stage_center, sprite_tremble
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_center, sprite_breathe

    "Il primo suono della giornata non è mai la sveglia. È lo scatto metallico dell'accendino nell'altra stanza."
    play sound audio.lighter
    "Un clic secco. Poi il primo sospiro di fumo di mia madre. È quello il segnale: ho esattamente sei minuti prima che mi chiami."
    "Li ho cronometrati un anno fa: sei minuti e undici secondi. Da allora li conto ogni mattina."
    show sprite_mila_tense as mila_sprite at sprite_stage_center, sprite_tremble with dissolve
    "Sei minuti per smettere di esistere come individuo e diventare una funzione della casa."
    "Mi alzo senza far rumore. La stanza è in ordine: libri allineati, letto teso, nessuna macchia. Non è disciplina, ma un modo per darle meno appigli."
    # La voce improvvisa la fa irrigidire prima ancora che possa rispondere.
    show sprite_mila_worried as mila_sprite at sprite_stage_center, sprite_flinch
    madre "Mila."
    "La voce attraversa la porta come un ago freddo. Mia madre non urla. Le grida sono per i dilettanti; lei usa la pressione atmosferica."
    "Esco con le spalle curve. In bagno copro il viola sotto gli occhi. Allo specchio, sotto lo zigomo destro, intravedo una cicatrice sottile."
    "Non ricordo sempre da dove venga. So che sfiorarla mi mette paura. In questa casa, anche la paura sembra una prova contro di me."
    scene bg mila kitchen at bg_tension_push
    with dissolve
    show expression Solid("#15121b30") as prologue_tint
    show sprite_padre_neutral as padre_sprite at sprite_stage_back_halfbody, sprite_breathe
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_neutral as madre_sprite at sprite_stage_right_halfbody, sprite_breathe
    "Mia madre siede al tavolo in vestaglia. Papà è nascosto dietro il giornale. Nella mia testa, il suo silenzio alimenta la crudeltà di lei."
    "Appoggio la tazzina. Mamma guarda il caffè, poi me: ha gli occhi grigi e stanchi, come il posacenere davanti a lei."
    madre "Ti sei truccata?"
    mila "No, mamma. Solo un po' di correttore per le occhiaie."
    show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_cold_still with dissolve
    madre "Cos'hai sotto gli occhi? Smetti di truccarti così. La gente guarda e sparla. Vuoi far credere ai vicini che qui non ti facciamo dormire?"
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_flinch
    "Mi si chiude la gola. Per mamma conta solo quello che penseranno i vicini e la facciata della famiglia perfetta."
    mila "Lo tolgo subito."
    madre "Brava. E stasera vai dai vicini. Hanno di nuovo bisogno di te per la ragazzina. Vedi di non fare la morta di sonno come al solito."
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_recoil
    "Non finisce la frase. Spinge lo yogurt verso il bordo; scatto per afferrarlo prima che cada. Una piccola umiliazione, appena sveglia."
    with hpunch
    show sprite_padre_neutral as padre_sprite at sprite_stage_back_halfbody, sprite_page_shift
    "Papà gira pagina senza alzare gli occhi. Non c'è nessun testimone di ciò che credo accada qui."
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
    scene bg school at bg_slow_push
    with dissolve
    show expression Solid("#18263a18") as prologue_tint
    show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
    show sprite_kate_neutral as kate_sprite at sprite_stage_right_halfbody, sprite_breathe with moveinright
    play ambience audio.rain fadeout 1.0 fadein 1.5
    "Fuori l'aria sa di asfalto bagnato. A scuola sono la Mila modello: buoni voti, nessun disturbo, un sorriso calibrato per non attirare domande."
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_flinch
    "Kate mi raggiunge di corsa, rossa per il freddo. Mi circonda le spalle con un braccio; trattengo il sussulto. Per me, un tocco improvviso può ancora significare un colpo."
    kate "Mila, aspettami! Hai sempre quella faccia da funerale. Stasera c'è la festa da Leo: vieni, ci sarà anche il tipo che ti fissava in biblioteca."
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
    scene bg oak houses at bg_slow_push
    with dissolve
    show expression Solid("#25192320") as prologue_tint
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_tense as mila_sprite at sprite_stage_left, sprite_tremble
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
    "Alle sette sono davanti alla casa dei vicini. Le due villette si somigliano; tra i prati rasati cresce una vecchia quercia che nessuno ha voluto abbattere."
    "Qui l'aria è diversa. Non è l'ossigeno pesante di casa mia: è un vuoto sterile, profumato di ammorbidente costoso."
    "I genitori di Sophie mi accolgono con la gentilezza distaccata riservata a chi svolge bene il proprio lavoro."
    "La madre si sistema il cappotto color cammello e mi rivolge un sorriso educato."
    show sprite_madre_sophie as madre_sophie_sprite at sprite_stage_right_halfbody, sprite_cold_still with moveinright
    madre_sophie "Sophie è di sopra. Ultimamente è stata difficile. Cerca di farla mangiare e niente schermi dopo le dieci, per favore."
    hide madre_sophie_sprite with dissolve
    hide mila_sprite with dissolve
    # Stacco visivo: lasciamo il giardino prima della sequenza all'interno della casa.
    scene black with fade
    "La porta si chiude alle mie spalle. Il silenzio di lusso della casa mi avvolge. Salgo le scale fino alla porta coperta di adesivi di vecchi anime e scritte KEEP OUT."
    "Busso con il nostro ritmo segreto, inventato quando si sono trasferiti. È l'unica porta a cui busso senza temere di essere convocata."
    sophie "Entra, Mila. Lo sai che con me non devi bussare. Sei l'unica persona che non mi dà il mal di testa in questa casa."
    scene bg sophie room at bg_tension_push
    with dissolve
    show expression Solid("#30172224") as prologue_tint
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_right_mila, sprite_breathe
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_right_mila, sprite_breathe
    "Sophie è sul letto, cuffie al collo e joystick in mano. Ha quindici anni: pallida, spigolosa, sembra troppo grande per la stanza preparata dai genitori."
    "Ufficialmente sono lì per aiutarla con i compiti e la cena. I suoi genitori la chiamano babysitting, così possono lasciarla sola senza preoccuparsene."
    "Qui le nostre età sembrano invertirsi. Sophie guarda gli adulti come se avesse già capito il loro gioco. Accanto a lei, sono io a sentirmi piccola."
    mila "Ciao, Sophie."
    "Spegne lo schermo e mi fissa. Il suo sguardo ha l'intensità di un bambino che trova un insetto raro e decide di chiuderlo in un barattolo per studiarlo da vicino."
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_sophie_tense as sophie_sprite at sprite_stage_left_sophie, sprite_breathe with moveinleft
    else:
        show sprite_sophie_neutral as sophie_sprite at sprite_stage_left_sophie, sprite_breathe with moveinleft
    sophie "Pensavo che tua madre ti avesse murata viva. Mi sei mancata, Mila. Eppure eccoti qui, a lasciarti consumare da tutti."
    mila "I miei non me lo permetterebbero."
    sophie "Permetterebbero. Che parola del cazzo."
    show sprite_mila_worried as mila_sprite at sprite_stage_right_mila, sprite_flinch
    "Si alza e mi prende il mento tra due dita. Il pollice sfiora la cicatrice sotto lo zigomo. La sua mano è calda; la mia pelle, fredda."
    show sprite_sophie_tense as sophie_sprite at sprite_approach_mila with dissolve
    show sprite_mila_worried as mila_sprite at sprite_stage_right_mila, sprite_anxious_breathe
    sophie "Ti trema persino la mascella. Solo io me ne accorgo. Solo io so di cosa hai bisogno per respirare."
    mila "Sophie, devo preparare la cena. I tuoi mi pagano per..."
    sophie "I miei non capiscono niente. E tu non sei qui per i loro soldi. Sei qui perché sono l'unica che ti vede davvero."
    "Il cuore accelera. Non è paura, mi dico. È qualcosa di più pericoloso: la sensazione di essere vista."
    show sprite_sophie_tense as sophie_sprite at sprite_approach_mila_tense
    sophie "Smetti di tremare quando ti tocco. Siamo rimaste noi due. I tuoi sono mostri, i miei manichini. Tu sei mia, Mila. Lascia che ti salvi."
    show sprite_mila_worried as mila_sprite at sprite_stage_right_mila, sprite_recoil
    "Mi scosto. Lei ha quindici anni, io diciotto. Dovrei rassicurarla, prepararle la cena. Invece aspetto da lei il permesso di respirare."
    mila "Siamo qui per i compiti e la cena, Sophie. Non per questo."
    sophie "Questo cosa? Volerti bene?"
    "Torna sul letto e sorride. Gli occhi, però, restano freddi: sembrano già conoscere un finale che io non ho visto."
    sophie "Va bene. Prepariamo il pollo e facciamo finta di niente. Ma la tua rabbia resta lì, Mila. Un giorno la useremo contro di lei. Ora vai."
    scene bg sophie kitchen at bg_slow_push
    with dissolve
    show expression Solid("#2b1e2410") as prologue_tint
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_anxious_breathe
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
    "Lavo le mani mentre l'acqua bolle. Sul tavolo c'è un disegno di Sophie: io rannicchiata, con fili ai polsi e alle caviglie che spariscono fuori dal foglio."
    # Primo piano esclusivo del disegno: scene rimuove lo sfondo della cucina e tutti gli sprite.
    scene sophie_draw_fullscreen
    with dissolve
    "Sotto, con la grafia ordinata di Sophie, c'è scritto: La mia bambola preferita."
    # Ripristina la cucina dopo il primo piano: nel prologo è presente soltanto Mila.
    scene bg sophie kitchen
    with dissolve
    show expression Solid("#2b1e2410") as prologue_tint
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_smile_lift with dissolve
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_smile_lift with dissolve
    "Sorrido debolmente. Mi sembra dolce che mi abbia ritratta, che abbia notato ogni dettaglio. Lei mi vuole bene davvero. Mi protegge."
    "Dalla finestra guardo casa mia. Per la prima volta, l'idea di tornarci non mi dà solo nausea. Mi fa tristezza."
    "Sophie ha ragione, penso. Chi non prova nulla è fortunato. Io invece sento ogni frequenza del dolore, e sta diventando troppo pesante da portare."
    jump capitolo_1


label capitolo_1:
    scene bg sophie kitchen at bg_slow_push
    with fade
    show expression Solid("#2b1e2410") as chapter1_tint
    play ambience audio.room fadeout 1.0 fadein 1.2
    centered "{size=42}{color=#e6d4db}CAPITOLO 1{/color}{/size}\n\n{size=28}{color=#aa97a3}Come sanguina un robot{/color}{/size}"
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
    "Preparo il pollo in automatico: taglio, soffriggo, mescolo. Mamma mi chiama efficiente. Io ho solo paura di sbagliare."
    # Sophie entra visivamente in scena soltanto quando Mila la descrive in cucina.
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_sophie_cold as sophie_sprite at sprite_stage_right, sprite_cold_still with dissolve
    else:
        show sprite_sophie_neutral as sophie_sprite at sprite_stage_right, sprite_cold_still with dissolve
    "Sophie non è rimasta in camera. È seduta sull'isola della cucina, le gambe che dondolano nel vuoto, e osserva ogni movimento."
    show sprite_sophie_cold as sophie_sprite at sprite_stage_right, sprite_micro_tension
    sophie "Sai cosa dicono i miei? «Guarda Mila: non risponde, è sempre in ordine, non si lamenta»."
    mila "I tuoi sono gentili."
    show sprite_sophie_cold as sophie_sprite at sprite_stage_right, sprite_cold_still
    sophie "No. I miei sono pigri. Ti usano come esempio perché non sanno chi sono io. Ma ti guardo davvero: stringi quel coltello fino a sbiancarti le nocche."
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_anxious_breathe
    "Abbasso gli occhi. Ha ragione. Tengo il manico come se fosse l'unica cosa che mi impedisce di scivolare via dalla realtà. Rilasso le dita, una alla volta."
    mila "È solo stanchezza."
    sophie "È rabbia. La tieni dentro per non disturbare. È l'unica cosa sincera che mostri. Scommetto che, ferendoti, chiederesti scusa al pavimento."
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_flinch
    "Mi volto bruscamente. Il calore dei fornelli mi scotta le guance, o forse è il rossore che mi tradisce."
    mila "Perché mi dici queste cose? Dovresti giocare ai videogiochi. Dovresti essere una ragazzina."
    sophie "E tu dovresti vivere, Mila. Qui sei in una cella dorata; a casa tua, in una di cemento. Voglio vedere chi diventi quando smetti di essere il loro robot."
    show sprite_sophie_cold as sophie_sprite at sprite_stage_right, sprite_approach_mila with dissolve
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_recoil
    "Mi prende una mano. Aspetta una reazione, un grido, uno schiaffo. Io abbasso lo sguardo."
    mila "La cena è pronta."
    "Ceniamo in silenzio. Il pollo sembra cartone bagnato. Poi la aiuto con latino: è brillante, ma si rifiuta di studiare per dispetto verso i professori."
    "Sono quasi le undici e i suoi genitori non sono rientrati. Io devo essere a casa alle undici e un quarto. Se faccio tardi, mamma troverà un altro motivo per punirmi."
    mila "Devo andare, Sophie. I tuoi arriveranno a momenti."
    sophie "Resta qui. Dormi nel letto degli ospiti. Di' ai tuoi che devi aiutarmi."
    mila "Non posso mentire. Lei capisce sempre quando mento."
    sophie "E allora? Che cosa farà? Ti farà sentire ancora più insignificante? Ti lascerà un altro segno da nascondere?"
    "Mi blocco davanti alla porta. Le parole risuonano come una condanna."
    mila "Non è così semplice."
    sophie "È semplicissimo. Ma tu hai paura della libertà quanto hai paura di lei."
    show sprite_sophie_tense as sophie_sprite at sprite_approach_mila, sprite_micro_tension
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_flinch
    "Si avvicina, mi posa una mano sulla spalla e stringe un po' troppo."
    sophie "Mi si spezza il cuore a vederti così. Almeno qui sei umana. Con me puoi smettere di fingere."
    show sprite_sophie_tense as sophie_sprite at sprite_approach_mila, sprite_micro_tension
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_anxious_breathe
    "Per un istante il mondo si restringe al profumo del suo shampoo e al calore del suo respiro. Penso che stia per baciarmi sulla guancia. Invece sussurra:"
    sophie "Vai a casa, corri dal tuo mostro. Lascia che ti faccia sentire inutile. Poi ricorderai dov'è l'unico posto sicuro: qui. La mia porta resta aperta."
    scene bg oak houses at bg_tension_push
    with dissolve
    show expression Solid("#25192324") as chapter1_tint
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_tense as mila_sprite at sprite_stage_left, sprite_tremble
        show sprite_sophie_cold as sophie_sprite at sprite_stage_right, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
    with hpunch
    show sprite_mila_tense as mila_sprite at sprite_stage_left, sprite_tremble
    "Corro nella notte. L'aria fredda mi taglia i polmoni. Attraverso il prato e salgo i gradini. Sono le 23:18: tre minuti di ritardo."
    "La chiave gira. La porta è aperta. Resto sulla soglia, cercando una spiegazione. Mi dico che è una dimenticanza e che la prossima volta andrà meglio."
    scene bg mila kitchen at bg_tension_push
    with dissolve
    show expression Solid("#15121b30") as chapter1_tint
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_neutral as madre_sprite at sprite_stage_right_halfbody, sprite_breathe
    "La luce della cucina taglia il corridoio buio. Mio padre è seduto in poltrona, con la TV spenta."
    padre "È in cucina."
    "Non è un avvertimento. È una constatazione."
    show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_cold_still
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_anxious_breathe
    "Mia madre lava una tazzina. Lentamente. Il rumore della spugna sulla ceramica è l'unico suono nella stanza."
    show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_micro_tension
    madre "Il lavoro è finito?"
    mila "Sì, mamma. Mi dispiace per il ritardo, io..."
    madre "La madre di Sophie mi ha scritto: sua figlia non si sente a suo agio con te. Non sai fare nemmeno il lavoro per cui ti pagano: stare zitta e non creare problemi."
    show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_approach_mila
    show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_recoil
    "Si avvicina e mi afferra la mascella con tre dita, costringendomi a guardarla. Le sue unghie si piantano nella pelle; le dita odorano di detersivo e cenere spenta."
    madre "Che cosa vi siete dette? Hai raccontato le tue storielle da vittima per farti compatire?"
    mila "No. Abbiamo solo studiato."
    madre "Non mentirmi. Ti ho dato una casa e da mangiare per farti crescere normale. E tu ci fai sembrare una famiglia da compatire."
    "Mi strofina la guancia con uno strofinaccio umido. Il tessuto graffia la pelle. Io non lo sento come un tentativo di pulirmi: lo vivo come un'altra punizione."
    madre "Togliti questo schifo dalla faccia. Fai schifo quando cerchi di fare la grande."
    "Resto immobile, stringendo i pugni. Mio padre appare sulla soglia, guarda la scena con gli occhi vuoti di chi osserva un mobile da spostare, poi si gira e se ne va."
    show sprite_mila_tense as mila_sprite at sprite_stage_left, sprite_recoil
    with hpunch
    "Mia madre mi spinge contro lo spigolo del tavolo."
    madre "Sparisci dalla mia vista. Vai in camera tua e non uscire prima di domattina."
    scene bg mila room at bg_slow_push
    with dissolve
    show expression Solid("#17131d28") as chapter1_tint
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_tense as mila_sprite at sprite_stage_center, sprite_tremble
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_center, sprite_breathe
    show sprite_mila_tense as mila_sprite at sprite_stage_center, sprite_anxious_breathe
    "Resto a letto vestita. Non piango. Sotto il cuscino trovo il vetro raccolto in giardino e lo stringo finché fa male. Subito dopo mi vergogno."
    "Mi dico che almeno questo dolore non finge di essere per il mio bene. Non so più se il pensiero sia mio o se qualcuno me l'abbia insegnato."
    "Sento ancora il pollice di Sophie sotto lo zigomo. Voglio vedere chi sei quando smetti di essere il loro robot."
    "Chiudo gli occhi. L'odio per i miei genitori si mescola al bisogno di tornare da Sophie. Qualcosa in me si è incrinato."
    jump capitolo_2


label capitolo_2:
    scene bg mila kitchen
    with fade
    play ambience audio.room fadeout 1.0 fadein 1.5
    play music audio.investigation fadeout 1.6 fadein 2.2
    centered "{size=42}{color=#e6d4db}CAPITOLO 2{/color}{/size}\n\n{size=28}{color=#aa97a3}La geometria del silenzio{/color}{/size}"
    "Il taglio brucia sotto l'acqua fredda. È un dolore netto; le parole di mamma, invece, si travestono sempre da premura."
    "Mi asciugo con cura, tamponando la pelle per non macchiare l'asciugamano bianco. In questa casa le macchie diventano prove, e ogni prova può trasformarsi in un'accusa."
    "Papà è già uscito. Mamma siede al solito posto, con il mio telefono davanti. Lo accarezza come un animale catturato."
    madre "Seduta."
    "Obbedisco. Non guardo il telefono; tengo gli occhi sulle mani intrecciate in grembo."
    madre "Stanotte non ho dormito. Dove ho sbagliato con te? Ti irrigidisci appena qualcuno ti parla. Che cosa ti succede, Mila?"
    mila "Mamma, stavamo solo..."
    madre "Silenzio. Non ti ho dato il permesso di inquinare l'aria con altre menzogne."
    "Copre il telefono con il palmo."
    madre "Il telefono resta a me. Dopo scuola torni subito qui; ho sospeso il tuo lavoro dai vicini. Ho già parlato con la madre di Sophie."
    "Il mondo mi crolla addosso, ma non faccio rumore. Le cose che devono apparire perfette non esplodono: implodono, collassando verso il proprio centro vuoto."
    mila "Ma lei ha bisogno di me."
    madre "Siamo noi ad avere bisogno che tu guarisca. È stata sua madre a tirare fuori l'argomento. Mi ha detto che Sophie ti trova strana. Che la metti a disagio."
    "Qualcosa non torna. Sophie non direbbe mai una cosa simile. Eppure il dubbio arriva: e se anche lei stesse recitando? Non deve essere vero per ferirmi."
    scene bg school
    with dissolve
    show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
    show sprite_kate_neutral as kate_sprite at sprite_stage_right_halfbody, sprite_breathe
    "A scuola mi muovo come un guscio vuoto. Senza telefono sono isolata; ma è l'isolamento mentale a soffocarmi."
    "Kate mi intercetta vicino agli armadietti."
    kate "Mila, sei sparita da ieri. Ti ho scritto e ha risposto tua madre: ha detto che eri malata e di non cercarti. Ma sei qui. Che succede?"
    "La preoccupazione di Kate è sincera. E mi irrita. Lei vive in una casa che sa di torta e bucato, non di cenere e rancore."
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
            "Ho appena spezzato qualcosa tra noi. La cosa peggiore è che, per un istante, mi sento bene. Se devo affondare, perché lei dovrebbe restare a galla?"
    "Alle 14:10 torno a casa. Mamma controlla l'orologio. Studio con la porta aperta, la schiena dritta e ogni movimento sotto sorveglianza."
    "Verso le cinque, mentre la luce si fa radente e grigia, un picchiettio leggerissimo colpisce il vetro della finestra sul retro."
    play sound audio.window_knock
    with hpunch
    "Toc. Toc-toc."
    "Senza muovere la testa, vedo un bullone avvolto in un foglio sul davanzale. Un filo da pesca lo collega alla quercia."
    "Sento i passi di mamma. Premo la penna finché l'inchiostro macchia la pagina. Si ferma sulla soglia, controlla la mia postura e se ne va."
    "Quando parte la televisione, apro appena la finestra e recupero il foglio. Sa dello shampoo alla ciliegia di Sophie."
    "{i}So che ti ha preso il telefono. Non crederle: io ti vedo, lei no. Ho costretto mia madre a smettere di metterti in dubbio.{/i}"
    "{i}Tua madre controlla il vialetto. Ogni mattina fa la doccia dalle sei alle sei e un quarto. Domani guarda sotto il tappetino: ti ho lasciato una chiave per il nostro mondo.{/i}"
    "{i}Guarda sotto il tappetino domani prima di uscire. Ti ho lasciato un regalo. Una chiave per il nostro mondo.{/i}"
    "{i}Non farti spegnere. Mi servi accesa. — S.{/i}"
    "Il cuore martella. «Mi servi accesa.» Non è affetto, suona come un ordine. Sophie mi aiuta o mi usa per colpire mia madre? Non voglio saperlo."
    "Non dormo. Dalla porta aperta vedo la sigaretta di mamma accendersi e spegnersi in fondo al corridoio."
    "Mamma rimette i coltelli nel ceppo, uno alla volta. Clac. Clac. Clac. Per me, ogni colpo suona come un avvertimento."
    "Domani prenderò quello che Sophie ha lasciato sotto il tappetino. Non so se sarà la salvezza o la rovina. A questo punto la differenza sembra aver smesso di importare."
    jump capitolo_3


label capitolo_3:
    scene bg mila room
    with fade
    play ambience audio.room fadeout 1.0 fadein 1.5
    centered "{size=42}{color=#e6d4db}CAPITOLO 3{/color}{/size}\n\n{size=28}{color=#aa97a3}Frequenze d'ombra{/color}{/size}"
    "Mi sveglio con la bocca amara. Ho sognato di gridare, ma dalla bocca uscivano soltanto cocci di vetro."
    "Il rituale della casa non cambia: il clic dell'accendino, il rumore delle pantofole di mio padre, il silenzio pressurizzato che precede la prima parola di mia madre."
    "Mamma è di spalle in cucina, immobile davanti alla finestra."
    madre "Le chiavi sono sul mobile dell'ingresso. Torna subito dopo l'ultima ora. Oggi pulirò a fondo la tua stanza. Ogni singolo angolo."
    "È una dichiarazione di guerra. Vuole dire che non avrò nascondigli, che persino i miei pensieri sono soggetti a ispezione."
    "Prendo zaino e chiavi. Fingo di allacciarmi una scarpa e faccio scivolare nella manica una busta nera nascosta sotto il tappetino."
    "Aspetto di essere nel bagno isolato al secondo piano. Dentro la busta c'è un vecchio telefono graffiato, con la batteria staccata e una SIM già inserita."
    "{i}Accendimi. Codice 0000. Non salvarmi tra i contatti. Nessuno può risalire a noi.{/i}"
    play sound audio.phone
    "Premo il tasto di accensione. La luce bluastra illumina il viso pallido nello specchio macchiato. C'è già un messaggio."
    "{i}S: Sapevo che l'avresti preso. Brava ragazza. Ora siamo connesse. Tua madre può chiudere la porta quanto vuole: io sono già dentro.{/i}"
    "«Brava ragazza»: le parole che mamma usava quando avevo sei anni. Da Sophie, suonano come una tentazione."
    mila "Perché lo fai? Mia madre dice che tua madre mi trova strana. Che le faccio paura."
    "La risposta arriva dopo tre secondi."
    "{i}Mia madre ripete quello che dice la tua. Hanno paura che tu ti svegli e le veda per ciò che sono. Io non ho paura di te. Stanotte, alle due, sotto la quercia. Non mancare.{/i}"
    "{i}E scrivi. Tutto quello che ti fanno oggi, ogni parola. Ti servirà quando qualcuno finalmente ti chiederà com'era.{/i}"
    "Scrivo da ottobre, da quando S. me l'ha chiesto: annota tutto, o ti diranno che non è successo. Nascondo il quaderno nero sotto il materasso."
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
            "Sophie detta senza guardarmi. Quando finisco, corregge una parola e mi fa riscrivere la frase. La mia grafia comincia a somigliare alla sua voce."
        "Chiudo il quaderno e lascio le pagine vuote.":
            $ quaderno_vuoto = True
            $ dubbi_di_mila += 1
            "Non voglio scrivere qualcosa che domani potrebbe sembrare una prova. Chiudo la copertina, ma il quaderno resta sul letto come una domanda senza risposta."
    "A filosofia il professore parla di prigionieri che si sorvegliano da soli perché non sanno quando sono osservati. Penso a mamma: fa lo stesso con me."
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
    "Alle 14:10 apro la camera e lascio cadere lo zaino. Mamma ha svuotato l'armadio: i vestiti sono ammucchiati sul letto."
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
    "La cena con i colleghi di papà è durata ore. Ho servito il risotto sotto lo sguardo di mamma, attenta a ogni mio gesto."
    "Davanti alla moglie del capufficio, mamma mi ha accarezzato la schiena."
    madre "Vedi come si è fatta carina, Mila? Anche se ultimamente è così pallida. Studia troppo, vero cara?"
    "La sua mano era calda, ma io ho sentito soltanto un artiglio pronto a stringersi se avessi sbagliato a posare la brocca."
    "È l'1:47. Dal muro arrivano il respiro di papà e gli scricchiolii del legno. Mamma non russa. Immagino i suoi occhi aperti, in attesa del minimo errore."
    "Mi vesto sotto le coperte per non fare rumore. Con le scarpe in mano, attraverso il corridoio buio. Vicino al tavolino del telefono c'è una doga che geme: devo evitarla."
    "Passo piano davanti alla porta socchiusa dei miei. Per un istante mi sembra che mamma mi stia guardando dalla fessura."
    play sound audio.door
    "La serratura scatta. Mi immobilizzo: uno, due, tre. Nessun rumore. Esco e richiudo con una lentezza millimetrica."
    "L'aria notturna mi schiaffeggia il viso. Sa di asfalto umido e libertà rubata. Per qualche secondo mi sento leggera, come se avessi perso dieci chili di catene."
    "Sophie è su un ramo basso: felpa nera, calze con gli orsetti, sneakers slacciate. Il vento le scompiglia i capelli biondi mentre mastica un lecca-lecca alla ciliegia."
    "Nel buio sembra una bambolina di porcellana smarrita nel bosco, non un predatore."
    sophie "Ce l'hai fatta, allora."
    mila "Ho rischiato di morire."
    sophie "Non si muore per un corridoio, Mila. Si muore perché non si ha il coraggio di attraversarlo."
    "Salta giù dal ramo e prende le mie mani. Le dita sono calde, lisce, incredibilmente morbide."
    sophie "Guarda casa tua. Ti vogliono lì, a servire il caffè e pulire finché diventerai grigia come lei."
    mila "Mamma dice che sono strana. Forse ha ragione. Chi scappa alle due di notte per incontrare una quindicenne sotto un albero?"
    "Sophie ridacchia, una risata cristallina che finisce troppo in fretta."
    sophie "Normale. La parola dietro cui si nascondono. Tua madre non teme che tu sia pazza: teme che tu ti svegli e scelga me."
    "Sfila dalla tasca un accendino di metallo argentato e lo fa scattare. La fiamma illumina le sue guance. Per un secondo sembra un angelo che gioca con il fuoco."
    sophie "Voglio mostrarti un segreto che i manichini di casa mia non conoscono."
    "Solleva la manica. Sull'avambraccio vedo piccole bruciature circolari, guarite e allineate con una precisione inquietante."
    mila "Chi ti ha fatto questo?"
    sophie "Io. Quando papà urlava e mamma piangeva in bagno. Quando lei copriva i lividi. Volevo sentire qualcosa di reale, lasciare un segno che non potessero nascondere."
    "Non so se crederle. So soltanto che la vista di quelle cicatrici mi fa venire voglia di proteggerla."
    sophie "Siamo uguali, Mila. Tu cerchi di piacere a loro; io provo a mostrare quanto siano mostri. Nessuna delle due può continuare così."
    "Mi mette una mano dietro la nuca, infilandosi tra i miei capelli. È un gesto dolce finché la presa non si fa troppo forte, quasi dolorosa."
    sophie "Vuoi scappare con me? Vuoi un posto senza genitori?"
    mila "Più di ogni altra cosa."
    sophie "Allora devi smettere di essere la brava Mila. Devi sporcarti le mani per davvero. Non si esce dall'inferno senza portarsi dietro un po' di fumo."
    "Si china e mi bacia. Le dita mi stringono i capelli fino a farmi male. Quando si stacca, il buio tra noi sembra più freddo."
    sophie "Ora sei mia, Mila. Non di altri. Mia."
    if telefono_condiviso_kate:
        sophie "Hai mandato il messaggio a Kate, vero? Non importa. Una fotografia non racconta una storia intera."
        "Sophie stringe le mie dita un istante più del necessario. Ha capito che una parte di ciò che mi dice potrebbe uscire dalla nostra bolla."
    elif telefono_nascosto:
        sophie "Non hai risposto al messaggio. Ma sei venuta lo stesso."
        "Non so se abbia intuito il mio silenzio o se si aspettasse comunque di vedermi. La sua sicurezza mi inquieta più di un rimprovero."
    elif telefono_risposto_sophie:
        sophie "Mi hai risposto. Sapevo che non mi avresti lasciata sola."
        "Il sollievo che provo sembra amore, ma so che ora Sophie può usare la mia promessa come una catena."
    "Ho diciotto anni. L'ho vista arrivare con le valigie quando ne aveva dodici. E adesso, sotto la quercia, mi sento speciale perché mi ha scelta."
    sophie "Domani iniziamo il fondo per la fuga. Tuo padre tiene i contanti delle consulenze nel cassetto della scrivania. Devi prenderli."
    mila "Come fai a saperlo?"
    sophie "Sono stata a casa tua. Tua madre mi ha invitata per il tè e mi ha lasciata sola due minuti. Ho guardato stanze, porte e serrature."
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
        "Le propongo di partire subito, senza rubare.":
            $ dubbi_di_mila += 1
            sophie "Senza preparare niente? Senza essere sicure?"
            "Sophie sorride, ma i suoi occhi diventano immobili. Vuole una fuga che abbia deciso lei, non una decisione presa da me."
            jump finale_fuga
    "Rientrare è come smettere di respirare. Mi infilo sotto le coperte vestita. Sulle labbra resta il sapore dolce del lecca-lecca, con un retrogusto metallico."
    "Sophie mi ha promesso la salvezza. Ma mi ha chiesto di diventare una ladra."
    jump capitolo_5


label capitolo_5:
    scene bg mila room
    with fade
    play ambience audio.room fadeout 1.0 fadein 1.5
    play music audio.memory fadeout 1.5 fadein 2.2
    centered "{size=42}{color=#e6d4db}CAPITOLO 5{/color}{/size}\n\n{size=28}{color=#aa97a3}L'incisione profonda{/color}{/size}"
    "La luce filtra dalle tapparelle come sbarre. Mi sento sporca, schiacciata dal segreto della notte."
    "Sfioro la cicatrice sotto lo zigomo, dove Sophie ha premuto il pollice. Lo specchio mi restituisce la solita Mila: camicia stirata, colletto in ordine, occhi spenti."
    scene bg mila kitchen
    with dissolve
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_neutral as madre_sprite at sprite_stage_right_halfbody, sprite_breathe
    "A colazione papà mangia cereali fissando il vuoto. Nel cassetto della sua scrivania, penso, ci sono i soldi che potrebbero permettermi di fuggire."
    "I miei escono alle dieci e mezza. Quando l'auto si allontana, il silenzio cambia: ogni mobile sembra accusarmi di essere rimasta."
    scene bg mila room
    with dissolve
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_tense as mila_sprite at sprite_stage_center, sprite_tremble
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_center, sprite_breathe
    "Entro nello studio. Odora di carta e tabacco spento. Il cassetto centrale è chiuso; la chiave è nascosta in un finto libro sulla mensola."
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
    if soldi_rubati:
        play music audio.tension fadeout 1.2 fadein 2.0
    else:
        play music audio.memory fadeout 1.2 fadein 2.0
    "Sotto le fatture trovo una busta azzurra. Dentro, mamma da giovane tiene in braccio una neonata. Sorride davvero; è un volto che non conosco."
    "Sul retro, con la grafia tremolante ma dolcissima, una data di diciotto anni prima e una frase: Perché tutto sia perfetto."
    "Quella bambina sono io. Papà ha conservato la foto sotto le bollette, chiusa a chiave, come qualcosa che non riesce a guardare."
    "Per un istante provo pena. Forse mamma voleva proteggermi e, senza accorgersene, mi ha chiusa nel suo guscio."
    menu:
        "La fotografia è fragile tra le dita."
        "La conservo senza rovinarla.":
            $ fotografia_conservata = True
            $ indizi_reali += 1
            "La rimetto nella busta e la infilo tra le pagine di un libro. Non so cosa provi, ma non voglio distruggerla."
        "La fotografo con il telefono segreto.":
            $ fotografia_digitalizzata = True
            $ indizi_reali += 1
            "Fotografo fronte e retro. La copia non chiarisce la frase, ma almeno non può essere strappata come l'originale. Rimetto tutto a posto."
        "La strappo, poi mi pento e raccolgo i pezzi.":
            $ fotografia_distrutta = True
            $ fiducia_sophie += 1
            "La carta si rompe più facilmente di quanto pensassi. Raccolgo ogni frammento, ma so che non potrò ricostruirla senza lasciare tracce."
    scene bg mila kitchen
    with dissolve
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_neutral as madre_sprite at sprite_stage_right_halfbody, sprite_breathe
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
        "Fisso lo schermo: «Scegli noi». Le banconote odorano di carta chiusa e mani stanche. Per la prima volta sento il potere del tradimento."
    else:
        "Non prendo i soldi. Il messaggio di Sophie arriva subito: «Scegli». Non so se sto proteggendo i miei o rimandando il momento in cui dovrò affrontarla."
    "Non sono più soltanto la vittima. Sono una complice. E la cenere che ho ingoiato per diciott'anni comincia a trasformarsi in un incendio."
    jump capitolo_6


label capitolo_6:
    scene bg oak houses
    with fade
    play ambience audio.rain fadeout 1.0 fadein 1.4
    play music audio.tension fadeout 1.0 fadein 1.5
    centered "{size=42}{color=#e6d4db}CAPITOLO 6{/color}{/size}\n\n{size=28}{color=#aa97a3}Il prezzo dell'argilla{/color}{/size}"
    "È l'1:55. I soldi nascosti sotto il materasso pesano come un tradimento. Mi sento un'estranea nella mia stessa casa."
    "Esco. Il corridoio non mi fa più paura: mi fa rabbia. Passo davanti alla camera dei miei senza trattenere il respiro."
    "Sotto la quercia, Sophie aspetta con le braccia conserte e lo sguardo fisso alla finestra della mia camera. Sembra già sapere la mia risposta."
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
        sophie "Quindi mi hai disobbedito. Pensavi che bastasse tornare a mani vuote? Il denaro era solo il primo passo."
    mila "Cominciare cosa? Possiamo prendere un autobus per la città, cambiare nome, sparire."
    sophie "Scappare ora significa farsi trovare in poche ore. Tuo padre chiamerà la polizia; tua madre ti cercherà ovunque. Non basta andarsene: dobbiamo impedirgli di riprenderci."
    "Si siede sulle radici e mi fa cenno di avvicinarmi. Mi siedo accanto a lei, improvvisamente piccolissima, un guscio pronto a essere riempito dalla sua volontà."
    sophie "La fase due riguarda l'assicurazione. Tuo padre non denuncerà mai questo furto."
    mila "Perché non dovrebbe? Sono i risparmi della famiglia."
    sophie "Perché ho questo."
    "Sblocca il telefono e me lo mostra per un attimo: documenti, colonne di cifre, timbri e firme. Scorre troppo in fretta perché io possa leggere."
    sophie "Conti, transazioni, mail tra i nostri padri. Guarda le società, guarda la firma di tuo padre."
    "Vedo zeri, sigle e firme. Li vedo così poco da non poterli descrivere dopo; eppure, mentre Sophie parla, la mia mente li trasforma in una confessione."
    sophie "Mio padre è sporco. Il tuo gli tiene i conti. Se denunciano il furto, pubblico tutto e li distruggo entrambi. Così nessuno potrà farci del male."
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
    sophie "Ti ho liberata: ora sai chi sono i tuoi genitori. Non devi sentirti in colpa per i soldi. Ma non basta."
    sophie "Tua madre non si fermerà. Per essere libere per sempre, dobbiamo farli dormire abbastanza a lungo da prendere il resto e sparire."
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
    madre "Pensavi di essere l'unica a nascondere qualcosa? Questo gioco l'ho inventato io. Ogni respiro che fai mi appartiene. Anche quei soldi li hai presi grazie alla mia pazienza."
    if soldi_rubati:
        mila "Non li ho più."
    else:
        mila "Non so come spiegartelo."
    "La mia voce, per una volta, non trema."
    mila "Sophie dice di avere documenti su di voi. Dice che li pubblicherà se proverete a fermarci."
    "Il silenzio è assoluto. La furia scompare dal volto di mia madre, sostituita da una comprensione disperata."
    madre "Ah. La ragazzina ti ha dato una voce."
    "Si siede e si copre il viso per qualche secondo."
    madre "Tuo padre fa il contabile per uno studio di geometri. Ventiduemila euro l'anno. Davvero pensi che avrebbe società all'estero? Guarda questa cucina."
    "Ride, e la risata le si spezza."
    madre "Chiama Kate. Chiama la scuola. Chiedi a chiunque se, in diciotto anni, ha mai visto uno di noi torcerti un capello. Ti prego. Chiedi."
    mila "Diranno quello che vuoi tu."
    madre "Certo."
    "Mi accompagna alla finestra e mi obbliga a guardare la villetta vicina. Una sola luce è accesa nel sottotetto: la stanza di Sophie."
    madre "Credi che quella ragazzina ti voglia bene? Vuole controllarti. Ti ha convinta che questa casa sia un inferno, così la sua sembra l'unica porta aperta."
    "Mi lascia andare. Crollo sul pavimento."
    madre "Ho chiamato la dottoressa Ferrante. Venerdì alle undici. Tuo padre ha preso un permesso: andiamo a parlare con lei, poi ci allontaniamo per un po'. Tutti e tre."
    "Venerdì alle undici: nella mia testa diventa subito la data della condanna."
    madre "Vai a letto, Mila. Ma ricordati: quando lei avrà finito di usarti, non ci sarà nessuna fotografia a ricordarti chi eri prima di tutto questo."
    "Spegne la luce. Tremo non solo per la paura delle sue parole, ma perché, per la prima volta, temo che abbia ragione."
    jump capitolo_7


label capitolo_7:
    scene bg school
    with fade
    play ambience audio.rain fadeout 1.0 fadein 1.3
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        play music audio.tension fadeout 1.2 fadein 2.0
    else:
        play music audio.investigation fadeout 1.2 fadein 2.0
    centered "{size=42}{color=#e6d4db}CAPITOLO 7{/color}{/size}\n\n{size=28}{color=#aa97a3}Anatomia di un assedio{/color}{/size}"
    "L'aria in casa è densa, immobile, chimica. Mia madre ha smesso di urlare. È questa la sua nuova tortura, almeno così la interpreto: il silenzio assoluto."
    "Mamma posa tre tazze sul tavolo e fissa un punto sopra la mia testa. Nella mia mente, papà è già colpevole: leggo ogni gesto come una prova."
    "Prima di andare a scuola, però, mi ferma in corridoio. Mi posa una mano sulla spalla e la ritira subito, come se si fosse scottato."
    padre "Mila."
    "Non dice altro per dieci secondi. Ha le unghie consumate, mangiate fino alla carne."
    padre "Non so cosa ti abbiamo fatto, Mila. Ho ripensato a tutto e non trovo il momento in cui ti abbiamo ferita. Se c'è, dimmelo. Proverò a rimediare."
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
                padre "Sì. L'ho scritta quando sei nata. Volevo che tutto fosse perfetto perché avevo paura di non saperti proteggere."
                "La sua voce trema. La testimonianza non restituisce la fotografia, ma mi offre un riscontro che non viene da Sophie."
            "Non gli chiedo nulla.":
                "Lascio la domanda dove si trova. Per ora, la fotografia è perduta e la frase esiste soltanto nella mia memoria."
    "Cerco Sophie sul telefono segreto. Non risponde. Durante la ricreazione mi rifugio nel bagno vuoto; lo schermo è l'unica luce."
    sophie "Cercavi me, Mila?"
    "Sussulto. Sophie è sulla soglia. Ha saltato le lezioni; quando toglie gli occhiali, vedo un livido lungo la mandibola."
    mila "Sophie! Che cosa è successo? È stato tuo padre?"
    "Faccio per avvicinarmi; lei si ritrae con un sorriso sottile."
    sophie "Mio padre non sa nemmeno nascondere le proprie tracce. Mi ha scoperta a frugare nel computer e ha provato a riprendere il controllo."
    "Il profumo alla ciliegia è coperto da un odore di antisettico."
    sophie "La tregua è finita. Non possiamo più aspettare. Dobbiamo creare il vuoto intorno a noi."
    mila "Mamma sa del ricatto. Dice che mi stai usando e che papà non potrebbe avere quei soldi. Domani vogliono portarmi da una dottoressa."
    "Sophie non batte ciglio."
    sophie "Certo che ti uso, Mila. E tu usi me per non affogare in quella cucina. Siamo due parassite: è questo il nostro legame, nudo e brutale."
    "Infila una mano nella tasca e tira fuori un flacone di vetro scuro con un contagocce."
    sophie "Le ho prese da casa di tuo padre. Non li uccideranno, dormiranno soltanto. Avremo il tempo di prendere quello che resta e sparire."
    "Mi mette il flacone in mano. È freddo, senza etichetta. Per la prima volta mi chiedo da quanto tempo stia preparando tutto."
    $ flacone_con_mila = True
    sophie "Fallo stasera. Domani ti portano dalla dottoressa. Una firma può trasformarti, agli occhi degli adulti, in una persona da rinchiudere. Non lasciare che decidano per te."
    "Si avvicina al mio orecchio."
    sophie "Quando torni, lascia la porta sul retro accostata. Io devo poter entrare."
    mila "Perché, se poi ci vediamo sotto la quercia?"
    sophie "Perché da sola ti spaventi. Ti spaventi sempre. Scegli, Mila. Vuoi essere il coltello o la carne?"
    menu:
        "Il flacone è freddo nel mio palmo. Una parte di me vuole ancora una risposta."
        "Le chiedo da dove vengono davvero le gocce.":
            $ flacone_indagato = True
            $ dubbi_di_mila += 1
            $ indizi_reali += 1
            mila "Da dove le hai prese? E come fai a sapere cosa faranno?"
            sophie "Ti sto chiedendo di fidarti di me. Perché vuoi rovinare tutto con le domande?"
            "Non mi dà una risposta. Mi restituisce la domanda come se la colpa fosse mia."
        "Accetto la sua spiegazione, anche se ho paura.":
            $ fiducia_sophie += 1
            "Mi dico che insistere significherebbe perderla. Per ora, scelgo di non guardare oltre il bordo della sua promessa."
        "Le dico che non le prometto niente.":
            $ dubbi_di_mila += 2
            $ prontezza_aiuto += 1
            sophie "Allora vedremo quanto vali quando arriva il momento."
            "Mi lascia andare. Per un secondo provo sollievo; subito dopo mi accorgo che sto aspettando di essere punita."
    "Torno a casa con il flacone nascosto, proprio sopra il cuore. Il vetro freddo mi morde la pelle a ogni respiro."
    scene bg mila kitchen
    with dissolve
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_neutral as madre_sprite at sprite_stage_right_halfbody, sprite_breathe
    "Quando entro, l'odore di fumo è sparito. La casa profuma di lasagne: mamma le prepara solo per i compleanni."
    "Esito. Potrei restituire i soldi e chiedere scusa. Forse potremmo ancora provare a riparare qualcosa."
    madre "Mila, porti tu i bicchieri? Sono sul bancone."
    "Il vino è già versato in tre calici. Papà piega il giornale in salotto. Il flacone mi scivola tra le dita sudate."
    "Attraverso il vetro della finestra immagino Sophie sulla quercia, immobile, in attesa del mio braccio."
    "Apro il flacone. Il liquido è trasparente, inodore. La mano si ferma. Papà tossisce dietro il giornale: un suono familiare, innocuo. Cosa sto facendo?"
    "Vorrei versare tutto nel lavandino e chiedere aiuto. Poi vedo la luce di Sophie alla finestra. La sua voce ritorna: se ti fermi, tornerai a essere invisibile."
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
            "La voce si spezza. Riesco a dire solo questo: Sophie mi ha chiesto di farvi dormire e ho paura di ciò che contiene il flacone."
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
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_neutral as madre_sprite at sprite_stage_right_halfbody, sprite_breathe
    play ambience audio.room fadeout 1.0 fadein 1.3
    play sound audio.heartbeat
    with hpunch
    play music audio.tension fadeout 0.8 fadein 1.4
    centered "{size=42}{color=#e6d4db}CAPITOLO 8{/color}{/size}\n\n{size=28}{color=#aa97a3}Natura morta con sedativi{/color}{/size}"
    "Riemergo dal buio con la testa pesante e la bocca amara. La luce è grigia, i pensieri lenti. Non ricordo quando ho aperto gli occhi."
    "Sono ancora seduta sulla sedia di legno. Davanti a me la lasagna è diventata una massa compatta, con il grasso arancione rappreso dal passare delle ore."
    "Mio padre è seduto di fronte a me, la testa reclinata all'indietro, le labbra socchiuse in un silenzio innaturale. Non sento il suo respiro e il torace non si muove."
    mila "Papà?"
    "Gli tocco il braccio. La pelle è fredda, di un freddo denso che mi schiaccia il cuore."
    "Mi giro verso mia madre. È crollata in avanti sul tavolo, i capelli finiti nel sugo freddo. Le afferro le spalle e la scuoto."
    mila "Mamma! Mamma, svegliati!"
    "La testa le cade di lato. Gli occhi sono fissi. Non respira. Le parole di Sophie mi tornano addosso: dormiranno soltanto."
    "Un urlo mi sale dallo stomaco e si spezza in un rantolo. Ho ucciso i miei genitori."
    if flacone_indagato:
        "La domanda sulla provenienza delle gocce torna con una chiarezza crudele. Sophie non aveva risposto: avevo scambiato la sua evasione per una certezza."
    else:
        "Non le avevo mai chiesto da dove venissero le gocce. Avevo preferito la sicurezza di Sophie alla possibilità di scoprire che non sapeva ciò che prometteva."
    play sound audio.door
    "La porta sul retro — quella che ho lasciato accostata — si apre. Passi leggeri attraversano il corridoio."
    "Sophie entra con un impermeabile giallo e guanti azzurri. Guarda i corpi, poi sorride come se tutto fosse andato secondo i piani."
    sophie "Vedo che il farmaco ha fatto un ottimo lavoro."
    mila "Li hai uccisi!"
    "Mi scaglio contro di lei. La travolgo e la spingo contro la credenza; i piatti tintinnano nel mobile."
    mila "Cosa cazzo hai fatto? Mi avevi detto che avrebbero dormito! Mi hai mentito!"
    "La sorpresa sul suo volto diventa rabbia. Mi afferra per i capelli e mi spinge contro il tavolo, stringendomi la gola."
    sophie "Chiudi quella bocca, Mila."
    "Mi manca il fiato. Provo a colpirla, ma mi tiene schiacciata accanto al viso immobile di mia madre."
    sophie "Guardali. Le tue impronte sono sul flacone e sui bicchieri. Il diario è sotto il materasso. Io non ho toccato nulla, Mila. Sei stata tu."
    "Allenta la presa quanto basta a farmi respirare, ma non mi lascia andare."
    sophie "Se provi a raccontarlo, finirai in prigione o in ospedale. In questa storia io non esisto. Nessuno sa di me."
    "La dolcezza della sua voce mi gela più della violenza."
    sophie "Sei mia. Hai fatto quello che dovevi. Ma se mi tocchi ancora, ti lascio qui e chiamo la polizia. Vuoi restare sola?"
    "La resistenza crolla. Mi accascio sul pavimento, tremando, distrutta dalla morte dei miei genitori e dall'impossibilità di tornare indietro."
    "Sophie si ricompone, sistema l'impermeabile e si passa una mano sullo zigomo arrossato."
    sophie "Brava ragazza. Ora possiamo passare all'ultimo pezzo del puzzle. I miei. I manichini."
    mila "I tuoi?"
    sophie "Non ci lascerebbero andare. Mio padre ci darebbe la caccia; mia madre piangerebbe sui giornali finché non ci trovano. Devono tacere entrambe le case."
    "Tira fuori un secondo flacone, quasi vuoto."
    sophie "Ho versato le gocce nel whisky prima di venire. Dormono sul divano. Prendi il cuscino pesante da casa tua e portalo qui, attraversando il prato."
    mila "Perché?"
    sophie "La storia deve sembrare vera: la ragazza della porta accanto entra con un cuscino preso da casa. Premeditazione. Alzati, Mila. Fammi vedere quanto sei brava."
    "Attraversiamo il prato alle 02:40. Il fango mi si attacca ai piedi nudi, ma non sento freddo. Il cuscino pesa come un neonato di pietra."
    scene bg sophie kitchen
    with dissolve
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_sophie_cold as sophie_sprite at sprite_stage_right, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_sophie_neutral as sophie_sprite at sprite_stage_right, sprite_breathe
    "La porta sul retro è aperta. Dentro l'aria profuma di cera per mobili e lavanda, un odore sterile che mi dà la nausea."
    "I genitori di Sophie sono sul divano, illuminati dalla TV. Un bicchiere è rovesciato sul tappeto; una macchia scura si allarga."
    sophie "Comincia con mia madre. È quella che fa più rumore. Finisci il rumore, Mila."
    "La donna che mi salutava con distacco ora sembra fragile. Avvicino il cuscino al suo viso, ma le braccia tremano e il tessuto scivola."
    sophie "Premi!"
    "Mi blocco. Il mondo si restringe al peso del cuscino, al respiro di Sophie alle mie spalle e alla consapevolezza di stare per fare qualcosa che non potrò più disfare."
    menu:
        "Sophie mi spinge per le scapole. Il tempo si è fermato."
        "Obbedisco, incapace di oppormi alla sua pressione.":
            $ fiducia_sophie += 1
            "Le ginocchia cedono. Sophie mi afferra da dietro e mi costringe a continuare. Il salotto torna silenzioso."
        "Provo a ritrarmi e a fermarla.":
            $ dubbi_di_mila += 2
            "Mi ritiro, singhiozzando, ma Sophie mi blocca e mi spinge di nuovo verso il divano. La mia resistenza non basta a fermarla: vuole che la colpa abbia il mio nome."
    "Non riesco a respirare. Sophie mi trascina verso l'uomo. La mente si allontana, come se smettere di sentire potesse salvarmi."
    "Quando tutto finisce, crollo sul tappeto. Le mani tremano così forte che il velluto mi scivola dalle dita."
    sophie "Vedi com'è facile? Ora siamo davvero libere. Non abbiamo più passato, nessuno che possa dirci chi siamo."
    "Guardo i guanti ancora puliti e le mie mani sporche. Il piano non è crollato: si è compiuto. Io mi sono sporcata per lasciare intatte le mani della mia padrona."
    jump capitolo_9


label capitolo_9:
    scene bg sophie kitchen
    with fade
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_sophie_cold as sophie_sprite at sprite_stage_right, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_sophie_neutral as sophie_sprite at sprite_stage_right, sprite_breathe
    play ambience audio.room fadeout 1.0 fadein 1.2
    play music audio.investigation fadeout 1.0 fadein 1.5
    centered "{size=42}{color=#e6d4db}CAPITOLO 9{/color}{/size}\n\n{size=28}{color=#aa97a3}Il diorama di porcellana{/color}{/size}"
    "L'aria nella villetta è troppo fredda. La nebbia del farmaco si dirada sotto una scarica di adrenalina gelida."
    "Sono seduta sul tappeto, le ginocchia al petto, a fissare i due corpi sul divano. Il silenzio non è più di lusso: è una palude che mi tira giù."
    "Sophie si toglie i guanti con uno schiocco secco. Si china, afferra un lembo del cuscino e comincia a strofinarmi le mani, con una forza brutale e metodica."
    "Il tessuto mi acceca per un istante. Ricordo lo strofinaccio umido con cui mamma cercava di pulirmi la guancia."
    "Non era un colpo, ma un gesto brusco e spaventato. L'odore del liquore si mescola allo shampoo alla ciliegia di Sophie. Quel profumo non sa più di salvezza."
    mila "Cosa fai, Sophie?"
    "Si avvicina alla credenza, prende il flacone vuoto e mi costringe ad avvolgerci le dita attorno prima di lasciarlo cadere sul pavimento."
    sophie "Faccio in modo che tutto sia coerente. La polizia troverà quattro corpi e te. La babysitter psicotica."
    mila "Noi dovevamo scappare. I documenti di tuo padre..."
    "Sophie ride piano, poi sblocca il telefono e mi mostra le immagini con la luce accesa, questa volta senza fretta."
    sophie "Guarda bene, Mila."
    "Sono bollette, ricevute e un preventivo per potare la quercia. In fondo c'è la firma di papà. Undici euro e cinquanta. Duecentotrenta. Nessuna società fantasma."
    sophie "Erano documenti d'archivio. Te li ho mostrati al buio e ti ho detto cosa vedevi. Non hai letto: hai creduto a me. È bastato chiamare tuo padre un mostro."
    "In quella risata, qualcosa crolla. I ricordi tornano a ondate violente, nitide come schegge."
    "Tre anni fa la villetta era vuota. Poi i genitori di Sophie si trasferirono con lei, adottata a dodici anni. Mamma preparò una torta e papà li aiutò con il trasloco."
    "Erano persone normali. Parlavano dei gerani. Il padre di Sophie non ha mai urlato davanti a me; una volta litigò con un giardiniere e poi si scusò."
    "I lividi che Sophie mi aveva raccontato? Il tutore al polso della madre, dopo una frattura giocando a tennis. Me l'aveva detto lei stessa, ridendo, mentre mi pagava."
    "I miei genitori non mi hanno mai picchiata. Mai."
    "La cicatrice sotto lo zigomo era il segno di una caduta dalla bicicletta a dodici anni. Mia madre era rimasta una notte intera sulla sedia dell'ospedale tenendomi la mano."
    "Mamma cercava di pulirmi il correttore dalla guancia. Io l'ho spinta e ho gridato. Mi sono raccontata che voleva cancellarmi, perché era più facile che ricordare la verità."
    "Mamma non ha mai chiuso la porta a chiave. I sei minuti li cronometravo io; a dodici anni ero stata io a chiederle di lasciarla aperta per paura del buio."
    "Ogni sbarra della mia prigione l'ho costruita io, usando le sue mani."
    mila "Tu hai pianificato tutto fin dal primo giorno."
    sophie "Sei sempre stata facile da programmare. Tre anni per costruire i tasti. Sei mesi per premerli. Dieci giorni per finire."
    "Guardo il livido: se l'è fatto da sola. Anche quel dolore era una scena preparata per convincermi che eravamo uguali."
    sophie "Chi cercherà un'anomalia? La polizia avrà il diario: date, odio e abusi che ti ho suggerito. La tua grafia. Nessuno ti ha costretto a scrivere."
    "Sophie si guarda intorno, soddisfatta come chi ha appena finito di apparecchiare."
    sophie "Troveranno il diario, le tue impronte sul flacone e sul cuscino. E una quindicenne nel ripostiglio. La cronaca avrà già un titolo: la brava ragazza diventata assassina."
    mila "E il telefono? I messaggi?"
    sophie "La SIM è falsa. Per loro sarò una persona conosciuta online, oppure una voce inventata dalla tua mente. Sceglieranno la spiegazione più comoda."
    "Mi porge il frammento di vetro raccolto in giardino."
    sophie "Chiudi il sipario, Mila. Fai vedere a tutti come sanguina un robot. Così il caso sarà chiuso e nessuno farà domande a una povera orfana."
    "Guardo il vetro e lei. La prigione non era casa mia. Era Sophie, con le lentiggini e il lecca-lecca alla ciliegia. Ho distrutto le persone che potevano aiutarmi."
    "Ho diciotto anni. Lei ne ha quindici. Le ho tagliato la torta di compleanno tre volte."
    if quaderno_fedele:
        "Ho annotato frasi e gesti, non diagnosi. Il quaderno non prova tutto, ma può aiutarmi a separare ciò che ho visto da ciò che Sophie mi ha suggerito."
    elif quaderno_manipolato:
        "Rileggo il quaderno: alcune frasi sono mie, altre le ha corrette Sophie. Non so più dove finisce la mia memoria e comincia la sua versione."
    elif quaderno_vuoto:
        if telefono_condiviso_kate or immagini_condivise_kate:
            "Il quaderno è rimasto vuoto. Non ho una cronologia personale da consultare; restano però le copie che ho affidato a Kate."
        else:
            "Il quaderno è rimasto vuoto. Non ho una cronologia personale né copie esterne da consultare: restano soltanto ricordi confusi."
    if prontezza_aiuto >= 2:
        "Una frase semplice riaffiora dalla voce di papà: non devi spiegare tutto in una volta. Posso chiedere aiuto anche senza ricostruire ogni minuto."
    elif padre_evitato and not padre_ascoltato and not padre_confrontato:
        "Non ho mai risposto davvero a papà. Adesso il silenzio pesa come una porta che non posso più riaprire."
    "Non voglio prendere il vetro, ma la colpa è enorme e la mia mente è esausta. Sophie aspetta, con il respiro leggero e le labbra socchiuse. Vuole vedere lo spettacolo."
    # L'ipotesi è utile soltanto se Mila distingue le osservazioni dalle conclusioni.
    if ipotesi_attiva == "sophie_manipola":
        if telefono_condiviso_kate and immagini_condivise_kate:
            $ ipotesi_sophie_solida = True
            mila "Il messaggio e l'immagine sono in mano a Kate. Non dimostrano ogni cosa, ma una parte del racconto può essere controllata da un'altra persona."
        elif immagini_verificate and (quaderno_manipolato or fotografia_digitalizzata or telefono_condiviso_kate):
            $ ipotesi_sophie_solida = True
            mila "Sophie mi ha impedito di leggere i file e ha corretto il mio quaderno. Sono riscontri diversi, non una confessione; bastano per chiedere una verifica."
        else:
            $ ipotesi_sophie_solida = False
            mila "Penso che Sophie abbia manipolato il racconto, ma non ho ancora collegato abbastanza fonti indipendenti."
    elif ipotesi_attiva == "genitori_colpevoli":
        $ ipotesi_genitori_sospetto = True
        mila "Per tanto tempo ho trattato i sospetti sui miei genitori come fatti. Devo separarli da ciò che ho davvero osservato."
    elif ipotesi_attiva == "flacone_pericoloso":
        mila "Il flacone è un rischio da chiarire. Non conosco il contenuto e non devo fingere di saperlo."

    menu:
        "Per la prima volta, il copione sembra fermarsi davanti a me."
        "Collego il messaggio e le immagini, poi chiamo aiuto." if ipotesi_attiva == "sophie_manipola" and ipotesi_sophie_solida:
            $ sophie_smascherata = True
            $ indizi_reali += 1
            "Non provo a dimostrare da sola ogni dettaglio. Indico le tracce che Kate può verificare e chiedo aiuto prima che Sophie imponga un'altra versione."
            mila "Kate! Ho bisogno di te. Conserva tutto e chiama un adulto, non entrare da sola."
            jump finale_verita
        "Non prendo il vetro. Le afferro il polso e chiamo aiuto." if indizi_reali >= 3 or telefono_condiviso_kate or immagini_condivise_kate or legame_kate >= 2 or padre_ascoltato:
            $ sophie_smascherata = True
            $ indizi_reali += 1
            "Le afferro il polso. Le unghie affondano nella pelle sotto le cicatrici e non lascio andare."
            "Per la prima volta il suo viso cambia. Non è paura: è fastidio, come una piega storta sul vestito."
            mila "Kate! Aiuto!"
            "La voce è spezzata, ma è mia. Se Kate ha il messaggio, se papà ha provato ad ascoltarmi, forse Sophie non controlla ancora tutta la storia."
            jump finale_verita
        "Le dico che so la verità, ma non riesco a chiedere aiuto.":
            $ dubbi_di_mila += 1
            sophie "Non hai più niente. Nessuna madre, nessun padre, nessuna Kate, nessuna casa. Hai solo me."
            "Penso a mio padre in corridoio, quando mi chiedeva dov'era il punto. Il punto non eri tu, papà. Il punto ero io. Il punto era lei."
            "Chiudo gli occhi."
            jump finale_fascicolo
        "Chiudo gli occhi e lascio che Sophie decida il finale.":
            "Non prendo il vetro. Ma non riesco a muovermi, né a chiamare nessuno. Sophie mi chiude le dita intorno al frammento con la pazienza di chi veste una bambola."
            "La colpa mi schiaccia. Sotto, riaffiora il ricordo di mamma accanto al mio letto d'ospedale per tutta la notte. Non riesco a sostenerlo."
            "Sophie aspetta. Io non trovo una voce."
            jump finale_fascicolo


label finale_verita:
    scene bg school
    with fade
    show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
    show sprite_kate_neutral as kate_sprite at sprite_stage_right_halfbody, sprite_breathe
    play music audio.ending fadeout 1.8 fadein 2.4
    play ambience audio.rain fadeout 1.0 fadein 1.4
    if genitori_salvati:
        "Kate risponde quasi subito. Quando sente la mia voce, non mi chiede di raccontare tutto in ordine. Mi dice di restare dove sono e di raggiungere un adulto."
        "Arrivano aiuto e soccorsi prima che Sophie possa imporre un'altra versione. Il flacone viene messo al sicuro; nessuno deve decidere da solo cosa contenga."
        "Mamma non minimizza la mia paura. Papà resta accanto a me mentre provo a distinguere ciò che ho visto da ciò che Sophie mi ha insegnato a credere."
        "Non ci riconciliamo subito. Dovremo ricostruire la fiducia. La visita dalla dottoressa non è una condanna. Per la prima volta mi aiutano senza pretendere una confessione perfetta."
        centered "{size=42}{color=#e6d4db}FINALE: LA PORTA APERTA{/color}{/size}"
        return
    if sophie_smascherata:
        "La mia voce raggiunge il corridoio. Sophie mi strappa il polso, ma il gesto ha lasciato segni che non può cancellare."
        if telefono_condiviso_kate and immagini_condivise_kate:
            "Kate ha conservato il messaggio e un'immagine. Non provano ogni accusa, ma permettono di verificare una parte del racconto senza affidarsi soltanto alla memoria di Mila."
        elif telefono_condiviso_kate:
            "Kate conserva una copia del messaggio. Non ha ricevuto le immagini sospette, quindi l'identità del mittente e il significato dei documenti restano da verificare."
        elif immagini_condivise_kate:
            "Kate conserva un'immagine ricevuta da Sophie, ma non il messaggio anonimo. È una traccia indipendente, non una ricostruzione completa."
        else:
            "Non ho dato a Kate copie del telefono né delle immagini. La richiesta d'aiuto conta, ma non posso fingere di avere prove esterne che non ho conservato."
        if quaderno_fedele:
            "Gli appunti vengono confrontati con le altre tracce. Non provano tutto, ma possono mostrare la sequenza degli eventi e le contraddizioni di Sophie."
        elif quaderno_manipolato:
            "Consegno il quaderno e spiego che Sophie mi ha dettato o corretto alcune frasi. Non è una testimonianza neutrale: anche la sua precisione va verificata."
        elif quaderno_vuoto:
            if telefono_condiviso_kate or immagini_condivise_kate:
                "Non c'è un diario da consegnare. La ricostruzione dipende dalle copie esterne e dalle testimonianze; alcune lacune restano aperte."
            else:
                "Non c'è un diario né una copia esterna da consegnare. Alcune lacune restano aperte e nessuno dovrebbe riempirle inventando ricordi."
        "La polizia non risolve tutto in una notte. Ci sono quattro morti e troppe domande, ma la versione di Sophie non è più l'unica."
        "Per la prima volta le chiedono di ripetere la storia senza suggerirle le parole. Il suo sorriso resta fermo per qualche secondo, poi si incrina."
        if fiducia_genitori >= 2:
            "Ricordo di aver provato una volta a parlare con papà. Non cambia ciò che è successo, ma il suo silenzio non equivale a una confessione."
        else:
            "Penso a quante volte ho evitato papà. Non potrò sapere che cosa avrebbe risposto. La domanda resta aperta."
        "Non posso riportare indietro nessuno. Posso dire ciò che ricordo, assumermi la responsabilità delle mie azioni e smettere di riempire i vuoti con la voce di Sophie."
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
        "La fotografia non è più disponibile. Riferisco la frase che ricordo e ciò che papà mi ha confermato, senza fingere che la testimonianza sostituisca l'originale."
    elif fotografia_distrutta and not fotografia_digitalizzata:
        "La fotografia non può essere aggiunta al fascicolo. Riferisco la frase che ricordo e chiarisco che non ho più l'originale."
    elif fotografia_conservata or fotografia_digitalizzata:
        "La fotografia originale o la copia digitale viene conservata, senza attribuirle un significato che da sola non può dimostrare."
    if quaderno_fedele:
        "Consegno il quaderno come traccia: contiene date e frasi, non la prova che ogni mia interpretazione fosse corretta."
    elif quaderno_manipolato:
        "Avverto Kate che Sophie ha dettato o corretto alcune frasi. Senza questa precisazione, il quaderno potrebbe trasformare la manipolazione in una falsa conferma."
    elif quaderno_vuoto:
        "Non ho un quaderno utile da consegnare. Kate annota le mie parole senza completare le parti che non ricordo."
    "Sophie continua a sorridere. Kate le pone una domanda semplice, poi aspetta. Nessuno riempie il silenzio al posto suo."
    "Racconto quello che ricordo. Quando arrivo a un punto che non so spiegare, mi fermo. Nessuno mi suggerisce le parole successive."
    centered "{size=42}{color=#e6d4db}FINALE: LA VERITÀ HA UNA VOCE{/color}{/size}"
    return


label finale_rottura:
    scene bg mila kitchen
    with fade
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_worried as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_cold as madre_sprite at sprite_stage_right_halfbody, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
        show sprite_madre_neutral as madre_sprite at sprite_stage_right_halfbody, sprite_breathe
    play music audio.memory fadeout 1.8 fadein 2.4
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
    "Affidiamo il flacone a chi può analizzarlo. La dottoressa Ferrante non emette una sentenza: mi aiuta a raccontare quello che mi è successo."
    "Fuori, Sophie comprende che il suo copione non funzionerà. La sua voce diventa fredda, priva delle carezze."
    "Non è un lieto fine perfetto. È una porta che resta aperta."
    centered "{size=42}{color=#e6d4db}FINALE: LA PORTA APERTA{/color}{/size}"
    return


label finale_fuga:
    scene bg oak houses
    with fade
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_mila_tense as mila_sprite at sprite_stage_left, sprite_tremble
        show sprite_sophie_cold as sophie_sprite at sprite_stage_right, sprite_cold_still
    else:
        show sprite_mila_neutral as mila_sprite at sprite_stage_left, sprite_breathe
    play ambience audio.rain fadeout 1.0 fadein 1.5
    play music audio.tension fadeout 1.4 fadein 2.2
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
    scene bg title night
    with fade
    "8 maggio 2026, ore 03:30. La notte è finita, ma la versione ufficiale comincia proprio adesso."
    stop ambience fadeout 1.5
    play music audio.tension fadeout 1.2 fadein 2.0
    play sound audio.heartbeat
    "Sirene, rumori, pagine scritte in una grafia ordinata. Undici settimane dopo, il fascicolo viene chiuso con una ricostruzione definita «di rara linearità»."
    "La versione ufficiale accusa Mila B., diciottenne: avrebbe sedato e ucciso i genitori, poi i vicini, e infine si sarebbe tolta la vita. Cinque corpi. Una sola colpevole."
    "Le fibre sul cuscino combaciano. Le impronte sul flacone combaciano."
    if quaderno_manipolato:
        "Il quaderno contiene centoquaranta pagine di abusi descritti con precisione, suggeriti da Sophie. Il perito lo considera credibile; le menzogne diventano così una falsa conferma."
    elif quaderno_fedele:
        "Il quaderno annota date e gesti, ma non offre la confessione ordinata che il caso richiede. Le discrepanze vengono archiviate come dettagli secondari."
    elif quaderno_vuoto:
        "Senza quel diario, il fascicolo si regge su impronte, flacone e racconto della sopravvissuta. L'assenza del documento non basta a far riaprire il caso."
    "Ci sono tre anomalie."
    "Prima anomalia: il medico legale nota segni di pressione difficili da spiegare con la forza di Mila. La nota resta a margine. La confessione sembra bastare."
    if quaderno_manipolato:
        "Anche i sedativi nel sangue di Mila vengono liquidati. La relazione parla di una finestra di latenza e ignora i minuti che non tornano. Nessuno confronta il diario con il corpo."
    else:
        "Anche i sedativi nel sangue di Mila vengono liquidati come un dettaglio. Gli investigatori hanno già scelto una versione e trattano ogni incongruenza come rumore."
    "Seconda anomalia: in tasca trovano un vecchio telefono con decine di SMS firmati S. I dispositivi ufficiali dei vicini non mostrano contatti con Mila; la SIM usa dati falsi."
    "La Procura conclude che S. sia una figura conosciuta da Mila su un forum, un interlocutore mai identificato, oppure una personificazione nata dal suo stato dissociativo."
    "Terza anomalia: sotto le unghie di Mila c'è materiale compatibile con la superstite, ritrovata dodici ore dopo in un ripostiglio, disidratata e incapace di parlare."
    if ipotesi_genitori_sospetto:
        "Mila continua a chiamare colpevoli i genitori senza prove indipendenti. Gli investigatori leggono quei sospetti come rancore premeditato."
    "Il verbale racconta che la bambina ha cercato di fermare Mila, poi è fuggita. Le tracce vengono classificate come segni di una colluttazione difensiva."
    "È, in un certo senso, la firma più bella che Sophie abbia mai messo in fondo a un documento: qualcun altro l'ha scritta per lei."
    "Il «Massacro della Porta Accanto» riempie i giornali. La villetta appare in copertina, dietro il nastro giallo. Gli editoriali discutono di quanto si possa conoscere i figli."
    if telefono_condiviso_kate or immagini_condivise_kate:
        "Una sola voce stona. Kate consegna alla Procura le copie che Mila le aveva affidato."
        if telefono_condiviso_kate and immagini_condivise_kate:
            "Il fascicolo contiene il messaggio anonimo e l'immagine mostrata da Sophie. Nessuno dei due identifica da solo la colpevole, ma insieme lasciano una contraddizione irrisolta."
        elif telefono_condiviso_kate:
            "Il fascicolo contiene una copia del messaggio anonimo, ma non l'immagine mostrata da Sophie. Il mittente resta da identificare."
        else:
            "Il fascicolo contiene un'immagine mostrata da Sophie, ma non il messaggio anonimo. Il contesto e l'origine del file restano da verificare."
        "La lettera di Kate viene protocollata e archiviata. Il cronista non la cita. Nel fascicolo restano sei parole: «Non era lei. Non era lei»."
    elif legame_kate >= 2:
        "Una voce dissente: Kate racconta che Mila era cambiata e che i genitori avevano chiesto aiuto tre volte in primavera. Scrive quattro pagine alla Procura."
        "La lettera viene protocollata e archiviata. Il cronista non la cita. Nel fascicolo restano sei parole: «Non era lei. Non era lei»."
    else:
        "Senza copie indipendenti dei messaggi, Kate non riesce a dimostrare quanto Sophie fosse presente nella vita di Mila. La sua preoccupazione finisce tra le anomalie."
    "Il pubblico ministero rilegge la lettera e guarda la foto della superstite: una ragazza bionda, lentiggini, cicatrici allineate e lo sguardo di chi ha visto troppo."
    "Firma."
    "Tre mesi dopo, un treno attraversa la campagna."
    scene bg oak houses
    with dissolve
    if dubbi_di_mila >= 2 or indizi_reali >= 2:
        show sprite_sophie_cold as sophie_sprite at sprite_stage_left, sprite_cold_still
        show sprite_chloe_neutral as chloe_sprite at sprite_stage_right_halfbody, sprite_breathe
    else:
        show sprite_sophie_neutral as sophie_sprite at sprite_stage_left, sprite_breathe
        show sprite_chloe_neutral as chloe_sprite at sprite_stage_right_halfbody, sprite_breathe
    "Il sole illumina i capelli biondi di Sophie sul treno. Di fronte a lei siede la nuova famiglia affidataria: persone convinte che il mondo sia ancora sicuro."
    "Accanto a lei c'è Chloe, dodici anni, trecce ordinate e uno sguardo timido, quasi spaventato da quella nuova sorella così silenziosa."
    sophie "No, grazie, mamma. Sto benissimo."
    "Sophie allunga una mano e accarezza la spalla di Chloe. La bambina sussulta, ma non si scosta. Guarda Sophie con un misto di timore e ammirazione."
    "Sophie sorride, un sorriso bellissimo che non le arriva agli occhi. Si china verso l'orecchio della bambina."
    sophie "Non tremare quando ti tocco, Chloe. Ora siamo solo noi due. Ti aiuterò a essere perfetta. Ti salverò da loro."
    "Poi si tira su la manica di pochi centimetri e mostra quattro cicatrici bianche, allineate sull'avambraccio."
    sophie "Vedi? Me l'ha fatto una bambola che non mi voleva bene. Non voleva fare la brava. Un giorno ti racconto."
    "Chloe annuisce piano. Nei suoi occhi c'è già la cosa che Sophie aspettava: pietà."
    "Il treno fende la campagna. Negli occhi freddi di Sophie si riflette il disegno del prossimo, impeccabile diorama."
    "E in un archivio ci sono quattro pagine scritte a mano da una ragazza di nome Kate, che nessuno ha voluto leggere fino in fondo."
    centered "{size=34}{color=#e6d4db}EPILOGO — LA BAMBOLA NUOVA{/color}{/size}\n\n{size=20}Non ti accorgi di essere diventata una bambola finché non provi a fare un passo da sola.{/size}"
    "La Bambola della Porta Accanto."
    return


define diario_mila = """
QUADERNO DI MILA
Dal fascicolo d'indagine 4082/2026 — Allegato C

Nota della Procura: il seguente materiale è estratto dal quaderno a righe con copertina rigida nera reperito nella stanza di Mila B., occultato tra le maglie della rete del letto. Alcune pagine presentano sbavature d'inchiostro, parole violentemente depennate o frasi incomplete.

14 Ottobre 2025

Sei minuti e undici secondi. Li ho contati anche stamattina.

Il clic dell’accendino di mamma mi stringe lo stomaco. In questa casa trattengo il fiato e cerco di occupare meno spazio possibile.

Mamma mi ha fissata mentre le posavo il caffè, cercando una colpa che non avevo ancora commesso. Papà era dietro il giornale. Se sparissi, forse girerebbe pagina senza accorgersene.

Li odio. A volte mi sembra di avere vetro in gola. Qui la crudeltà arriva con le buone maniere e le tazze pulite.

Vorrei che succedesse qualcosa. Qualsiasi cosa pur di uscire da questa casa.

2 Novembre 2025

Stasera S. mi ha detto una cosa che non riesco a togliermi dalla testa.

Ero al buio e tremavo ancora per la lite con mamma. S. mi ha preso le mani: erano calde.

«Devi scrivere tutto, Mila,» mi ha detto. «Ogni singola cosa che ti fanno. Altrimenti un giorno ti convinceranno che te lo sei inventato. Ti convinceranno che la pazza sei tu.»

Ho preso questo quaderno per non dimenticare. S. dice che è il nostro segreto.

Quando sono tornata a casa, la luce gialla del corridoio non mi ha fatto paura soltanto. Ho pensato a S.: dice di vedermi oltre la maschera da brava figlia. È l'unica a cui credo.

18 Dicembre 2025

Abbiamo parlato di come sarà quando andremo via.

Era buio e c'era la neve fresca sul prato. Eravamo sotto la quercia, vicinissime per non fare rumore. S. mi ha descritto una casa piccola, vicino al mare, dove non ci sono orari, dove nessuno controlla se ti sei truccata o se hai tre minuti di ritardo.

«Niente genitori, Mila. Niente regole. Solo noi due.»

A volte temo di non essere abbastanza forte.

Non devo scriverlo, mi dico. Devo farcela.

Quando sono con S., l'aria di casa mia sembra meno velenosa. Mi sembra quasi di poter resistere fino al giorno in cui ce ne andremo. S. dice che sono la sua persona preferita al mondo. Nessuno me l'aveva mai detto. Mia madre mi dice solo che sono un impegno. S. invece mi guarda come se io fossi preziosa.

3 Gennaio 2026

Mamma mi ha fatto pulire lo specchio tre volte per alcune impronte. Mi tremavano le mani. Ho pensato a una forbice, poi ho lasciato perdere.

Sono corsa via appena possibile. Ho raccontato tutto a S. Lei non mi ha detto «passerà» come fa Kate a scuola. Kate non capisce niente, Kate vive nel mondo di ovatta. S. mi ha stretto il mento, fortissimo, finché non ho smesso di piangere.

«Lasciali fare, Mila. Lascia che si consumino nella loro cattiveria. Tu sei mia, ricordatelo. Io ti salverò da loro.»

Mi ha baciata sulla guancia, vicino alla cicatrice. Sento ancora il calore della sua pelle. Mi farei fare qualsiasi cosa pur di non perdere questo calore.

20 Febbraio 2026

Ho sognato che mia madre murava la porta della mia camera lasciando solo un piccolo buco per far passare lo yogurt. Mi sono svegliata con il cuore che batteva a cento.

Ho guardato fuori dalla finestra. La luce nell'oscurità della notte era accesa. Ho messo la mano sul vetro freddo, sapendo che dall'altra parte c'era S.

Siamo sole contro di loro. I suoi genitori sono rigidi, finti, sempre pronti a giudicare. I miei sono mostri travestiti da persone perbene. Se non ci fossimo trovate, io sarei già morta dentro. S. è la mia unica via d'uscita.

12 Aprile 2026

La tensione in questa casa sta diventando insopportabile. Sento gli sguardi di mia madre piantati sulla mia schiena anche quando sono di spalle. Controlla ogni mio movimento, ogni respiro.

Oggi ho parlato con S. della fuga. Dobbiamo accelerare i tempi. Non posso più aspettare.

«Le cose si fanno con precisione, Mila. Quando sarà il momento giusto, saremo libere.»

Ha ragione. Devo fidarmi. Devo smettere di avere paura e iniziare a preparare il terreno. Se mi faccio prendere dal panico adesso, rischio di rovinare tutto. S. è l'unica che sa come guidarmi fuori da questo inferno. Io devo solo essere pronta a fare la mia parte.

28 Aprile 2026

Mamma dice che sono paranoica e che mi invento tutto. Vuole convincermi che il problema sono io. Non posso crederle.

Ieri mio padre è entrato in cucina con quella sua camminata lenta, da ombra, e mi ha fissata senza dire una parola. Hanno paura di me perché sanno che ho capito chi sono veramente. Sotto le loro maschere da famiglia perfetta c'è solo marciume.

Quando ne parlo con S., lei dice che i miei genitori sono marionette e che solo noi siamo vere. Manca poco, continua a ripetermi.

5 Maggio 2026

Non dormo più. Ogni stanza mi sembra una trappola e mamma mi guarda come se stesse decidendo cosa fare di me.

Ieri ho guardato S. negli occhi e ho visto la stessa determinazione che sento bruciare dentro di me. Nessun dubbio, nessuna esitazione.

«Niente più catene, Mila. Presto sarà tutto finito.»

Mi viene da piangere. S. dice che non mi lascerà cadere. Voglio andarmene con lei e non respirare più quest'aria.

7 Maggio 2026

Non so cosa succederà stasera.

Mia madre mi ha perquisito la stanza. Ha trovato le mie cose, ha detto che venerdì mi porta da una dottoressa. Vuole chiudermi in una stanza. Vuole togliermi anche l'aria. Vuole distruggermi prima che io possa scappare.

Mi tremano le mani mentre scrivo queste righe. Nascondo questo quaderno sotto il materasso, nell'unico posto dove le sue mani non possono arrivare a stroppiarlo.

Stasera si chiuderà tutto. Non ho più paura.

Se domani saremo lontane da qui, se saremo davvero vicino al mare con S., forse riuscirò a dimenticare il rumore dell'accendino in cucina. Forse riuscirò finalmente a respirare.

Note di chiusura del fascicolo: il quaderno si interrompe a pagina 84. Le ultime pagine del volume risultano bianche. Alcune pagine del quaderno risultano essere strappate e non presenti.
"""

define frammenti_mila = """
FRAMMENTI DEL QUADERNO

Nota: sono tuttora nascosti in un luogo che solo Mila conosceva e che nessuno ha mai perquisito.

14 Novembre

Mamma mi ha guardata mentre mi allacciavo le scarpe. Poi mi ha sistemato il colletto, con un gesto brusco ma senza farmi male.

Sophie dice che mamma vuole cancellarmi. Le ho creduto e l'ho scritto anche ieri, come voleva lei.

A letto mi è tornato in mente quando, a sette anni, avevo la polmonite. Mamma è rimasta tre notti accanto a me, cambiandomi le pezze sulla fronte. Credeva che dormissi, ma la sentivo piangere e sussurrare:

«Prendi me, Dio. Fai stare male me, ma lascia respirare lei.»

Perché quel ricordo adesso mi sembra una colpa? Con Sophie, la voce di mamma diventa fredda. Vorrei chiederle scusa, ma ho paura che Sophie mi chiami debole.

E io ho così tanta paura che Sophie smetta di guardarmi.

19 Aprile

Sophie mi ha baciato stasera sotto la quercia. Aveva le labbra fredde, che sapevano di lecca-lecca alla ciliegia e di qualcosa di amaro, come il ferro. Mi ha detto:

«Sei la mia bambola preferita, Mila.»

Quando lo dice, mi sento vista. Per un attimo, mi basta.

Poi torno a casa e trovo mamma al buio, con la sigaretta accesa. Mi sento un'ombra. Provo a vedere veleno in ogni loro gesto, come mi ha insegnato Sophie.

Dietro la dispensa ho trovato un vecchio disegno: noi tre, una casa gialla e un sole enorme. Mamma lo ha protetto con nastro adesivo e lo conserva da dieci anni.

Se mi odiano così tanto come dice Sophie... perché mamma conserva ancora il disegno di quando la amavo?

Forse la casa non è una prigione. Forse sono io a non riuscire più a vederla com'era.

7 Maggio

Ho visto la fotografia. Quella azzurra, nascosta sul fondo del cassetto di papà.

Mamma era così giovane. Aveva un sorriso lungo, bellissimo, che non le ho mai visto in faccia da quando sono grande. Teneva me tra le braccia come se fossi la cosa più preziosa e fragile dell'universo. Sul retro, papà aveva scritto con la sua solita grafia precisa:

«Perché tutto sia perfetto.»

Forse non era solo ossessione per il giudizio. Forse era amore, goffo e impaurito. Mamma voleva proteggermi e ha finito per chiudermi in un guscio.

E io l'ho scambiata per una prigione.

Sophie mi ha dato le gocce. Ce le ho in tasca. Il flacone di vetro scuro mi morde la pelle attraverso la stoffa. Mi ha promesso che dormiranno e basta, che sarà solo un sonno lungo per permetterci di scappare insieme. Ma il mio cuore sta martellando così forte che ho paura mi si spacchi il petto.

Stasera mamma ha cucinato le lasagne. Le ha fatte per me. Si è messa il vestito verde scuro, quello elegante che usa solo per le feste. Le tremavano le mani mentre mi versava l'acqua. Mi ha detto:

«Ho preparato tutto questo solo per te, Mila.»

Vorrei rovesciare il tavolo. Vorrei buttare i bicchieri nel lavandino. Vorrei correre da papà, abbracciarlo forte e dirgli che mi dispiace per tutti i silenzi, per tutti gli sguardi cattivi, per le cose orribili che ho scritto su di loro in quel quaderno.

Ma mi sono girata verso la finestra e ho visto la luce di Sophie. È lì, nel sottotetto. Mi fissa.

Se non lo faccio, Sophie mi abbandonerà. Se non lo faccio, tornerò a essere invisibile nel buio. Sono così stanca. Sono così spaventata. Ho diciotto anni e mi sento morta da sempre.

Mamma... papà... se farò quello che temo, non credete a quello che troveranno scritto. Vi prego: non ero io.

Era la bambola.

Senza Data

A chiunque trovi questo foglio.

Non credete al quaderno sotto il materasso. Sophie mi dettava le frasi e me le faceva riscrivere finché non erano esatte. Voleva costruire una storia e farmi odiare le uniche due persone che mi hanno voluto bene.

I miei genitori non mi hanno mai abusata. Mio padre era un uomo buono e silenzioso. Mia madre piangeva la notte perché vedeva che mi stavo spegnendo e non sapeva come salvarmi da se stessa e dal mondo.

Se questo foglio è tra le vostre mani e loro non ci sono più, significa che stasera avrò ceduto. Che avrò versato quelle gocce nei loro bicchieri perché sono troppo debole, troppo codarda per dire di no a una ragazzina di quindici anni che mi faceva sentire speciale mentre mi scavava la fossa.

Se state leggendo questo, significa anche che io sarò già morta insieme a loro. Non abbiate pietà di me: sono un mostro per aver creduto alle sue bugie invece che agli occhi di mia madre.

Ma vi prego... guardate Sophie. Guardatela negli occhi quando vi sorride. Guardate come vi tocca. Guardate le sue mani pulite mentre tutti gli altri sanguinano. Non lasciatela avvicinare a nessun altro.

Mamma, papà... sto arrivando. Stasera la casa è buia, ma non ho più paura del buio. Ho solo tanto, tanto freddo.
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
        xsize 1120
        ysize 820
        background Solid("#211a25")
        padding (26, 20)
        vbox:
            spacing 10
            hbox:
                xfill True
                vbox:
                    spacing 3
                    text "ARCHIVIO INVESTIGATIVO" size 30 color "#e6d4db"
                    text "Confronta le fonti. Formula ipotesi. Distingui fatti e sospetti." size 16 color "#c2b4c5"
                null width 12
                vbox:
                    spacing 4
                    textbutton "DOCUMENTI ORIGINALI" action Show("documenti_mila") text_size 15
                    textbutton "CHIUDI  ·  I" action Hide("archivio_indizi") text_size 17
            frame:
                xfill True
                background Solid("#352a3a")
                padding (12, 8)
                vbox:
                    spacing 3
                    text "LEGENDA" size 15 color "#e4b6bd"
                    text "OSSERVATO = ciò che Mila ha visto o fatto. RISCONTRO = una fonte confrontabile. IPOTESI = spiegazione ancora da verificare." size 14
            viewport:
                xfill True
                ysize 675
                mousewheel True
                draggable True
                scrollbars "vertical"
                vbox:
                    spacing 12
                    text "COLLEGAMENTI TRA LE PROVE" size 21 color "#e4b6bd"
                    if telefono_condiviso_kate and immagini_condivise_kate:
                        frame:
                            xfill True
                            background Solid("#24352e")
                            padding (12, 9)
                            vbox:
                                spacing 4
                                text "SBLOCCATO · MESSAGGIO + IMMAGINE" size 16 color "#c7dfc8"
                                text "Kate conserva una copia del messaggio e un'immagine mostrata da Sophie. Due tracce possono essere confrontate fuori dal controllo di Sophie; non dimostrano automaticamente ogni accusa." size 15
                    elif telefono_condiviso_kate and immagini_verificate:
                        frame:
                            xfill True
                            background Solid("#24352e")
                            padding (12, 9)
                            vbox:
                                spacing 4
                                text "COLLEGAMENTO PARZIALE · MESSAGGIO + RIFIUTO" size 16 color "#c7dfc8"
                                text "Kate conserva il messaggio. Mila ha osservato che Sophie non le lasciava controllare i file. Il rifiuto è osservabile; la falsificazione resta da provare." size 15
                    elif fotografia_conservata or fotografia_digitalizzata:
                        frame:
                            xfill True
                            background Solid("#30283a")
                            padding (12, 9)
                            vbox:
                                spacing 4
                                text "IN ATTESA · FOTOGRAFIA + MEMORIA" size 16 color "#d7c2a0"
                                text "La frase sul retro è ambigua. Un eventuale riscontro del padre può essere confrontato con la memoria di Mila; la fotografia da sola non prova un piano." size 15
                    else:
                        text "Nessun collegamento composto è ancora disponibile. Conservare o condividere una traccia può rendere possibili confronti successivi." size 15 color "#c2b4c5"

                    text "FORMULA UN'IPOTESI" size 21 color "#e4b6bd"
                    text "Puoi cambiare idea. La scelta registra la tua interpretazione, non altera retroattivamente i fatti raccolti." size 14 color "#c2b4c5"
                    if (telefono_condiviso_kate and immagini_condivise_kate) or (immagini_verificate and (quaderno_manipolato or fotografia_digitalizzata or telefono_condiviso_kate)):
                        textbutton "IPOTESI · Sophie ha manipolato il racconto" action SetVariable("ipotesi_attiva", "sophie_manipola") text_size 16
                    else:
                        text "BLOCCATA · Manipolazione del racconto: servono almeno due tracce confrontabili." size 15 color "#c2b4c5"
                    if immagini_credute or fiducia_sophie >= 2:
                        textbutton "SOSPETTO · I genitori sono responsabili" action SetVariable("ipotesi_attiva", "genitori_colpevoli") text_size 16
                        text "Stato: sospetto, non deduzione. Le immagini credute non sono state verificate." size 14 color "#d7c2a0"
                    else:
                        text "BLOCCATA · Ipotesi sui genitori: considera prima la versione di Sophie o le immagini." size 14 color "#c2b4c5"
                    if flacone_indagato or flacone_con_mila:
                        textbutton "IPOTESI DI RISCHIO · Il flacone può essere pericoloso" action SetVariable("ipotesi_attiva", "flacone_pericoloso") text_size 16
                    else:
                        text "BLOCCATA · Flacone: prima occorre trovarlo o chiedere spiegazioni." size 14 color "#c2b4c5"

                    if ipotesi_attiva == "sophie_manipola":
                        if telefono_condiviso_kate and immagini_condivise_kate:
                            text "LA TUA IPOTESI · Sostenuta da due tracce condivise, verificabili da Kate. È una deduzione operativa, non la prova di ogni dettaglio." size 15 color "#c7dfc8"
                        elif immagini_verificate and (quaderno_manipolato or fotografia_digitalizzata or telefono_condiviso_kate):
                            text "LA TUA IPOTESI · Più riscontri concordano, ma la catena di prove resta incompleta." size 15 color "#d7c2a0"
                        else:
                            text "LA TUA IPOTESI · Plausibile, ma debole: manca un riscontro indipendente sufficiente." size 15 color "#d7c2a0"
                    elif ipotesi_attiva == "genitori_colpevoli":
                        text "LA TUA IPOTESI · Sospetto non verificato. Non trattare le immagini non controllate come fatti." size 15 color "#d7c2a0"
                    elif ipotesi_attiva == "flacone_pericoloso":
                        text "LA TUA IPOTESI · Rischio da verificare. Il contenuto non è identificato." size 15 color "#d7c2a0"
                    else:
                        text "NESSUNA IPOTESI SELEZIONATA · Raccogli elementi e scegli una spiegazione provvisoria." size 15 color "#c2b4c5"

                    text "REGISTRO DELLE PROVE" size 21 color "#e4b6bd"
                    text "1. TELEFONO ANONIMO" size 18 color "#e4b6bd"
                    if telefono_condiviso_kate:
                        text "RISCONTRO ESTERNO · Kate conserva una copia. Il contatto è reale; il contenuto va verificato." size 15
                    elif telefono_nascosto:
                        text "OSSERVATO · Telefono nascosto, nessuna copia indipendente." size 15
                    elif telefono_risposto_sophie:
                        text "OSSERVATO · Mila ha risposto a Sophie; questo non rende vero il messaggio." size 15
                    else:
                        text "MANCANTE · Mila non ha scelto come gestire il telefono." size 15 color "#c2b4c5"

                    text "2. FOTOGRAFIA DI FAMIGLIA" size 18 color "#e4b6bd"
                    if fotografia_conservata:
                        text "CONSERVATA · Originale disponibile per confronto; la frase sul retro è ambigua." size 15
                    elif fotografia_digitalizzata:
                        text "COPIA DIGITALE · Fronte e retro fotografati; il contesto non è dimostrato." size 15
                    elif fotografia_distrutta and testimonianza_padre:
                        text "RISCONTRO ALTERNATIVO · Il padre conferma la frase, non la fotografia distrutta." size 15
                    elif fotografia_distrutta:
                        text "PERDUTA · Originale distrutto, nessuna copia digitale." size 15 color "#d7a6a6"
                    else:
                        text "MANCANTE · Fotografia non esaminata." size 15 color "#c2b4c5"

                    text "3. QUADERNO NERO" size 18 color "#e4b6bd"
                    if quaderno_fedele:
                        text "OSSERVAZIONI · Appunti su gesti e frasi osservati; separali dalle interpretazioni." size 15
                    elif quaderno_manipolato:
                        text "CONTAMINATO · Sophie ha suggerito o corretto le parole: non è una fonte indipendente." size 15 color "#d7a6a6"
                    elif quaderno_vuoto:
                        text "VUOTO · Non contiene una ricostruzione utile." size 15 color "#c2b4c5"
                    else:
                        text "MANCANTE · Mila non ha ancora scelto cosa scrivere." size 15 color "#c2b4c5"

                    text "4. IMMAGINI MOSTRATE DA SOPHIE" size 18 color "#e4b6bd"
                    if immagini_verificate:
                        text "OSSERVATO · Sophie non ha lasciato esaminare i file con calma. È verificato il rifiuto, non la frode." size 15
                    elif immagini_condivise_kate:
                        text "COPIA ESTERNA · Kate ha ricevuto un'immagine; confrontala con altri documenti." size 15
                    elif immagini_credute:
                        text "NON VERIFICATO · Mila ha accettato le immagini senza controllarle." size 15 color "#d7c2a0"
                    else:
                        text "MANCANTE · Immagini non esaminate." size 15 color "#c2b4c5"

                    text "5. FLACONE" size 18 color "#e4b6bd"
                    if flacone_indagato:
                        text "DOMANDA APERTA · Sophie non ha dato una provenienza verificabile." size 15
                    if genitori_salvati:
                        text "AZIONE · Mila ha chiesto aiuto; il contenuto richiede analisi competente." size 15
                    elif genitori_sedati:
                        text "CONSEGUENZA · Il flacone è stato usato; l'azione è irreversibile." size 15
                    else:
                        text "NON ACCERTATO · Contenuto e intenzione restano sconosciuti." size 15


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
