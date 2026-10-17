## Questo file contiene opzioni che possono venire cambiate per personalizzare
## il gioco.
##
## Le linee che cominciano con due '#' sono commenti e non dovresti modificarle.
## Le linee con un solo '#' sono linee di codice opzionali, e potresti volerle
## modificare se appropriato.


## Fondamentali ################################################################

## Il nome del gioco in forma leggibile. E' usato per il titolo nella finestra e
## viene impiegato per i resoconti di errore e nell'interfaccia.
##
## La notazione _() che racchiude la stringa la segna come testo traducibile.

define config.name = _("La bambola della porta accanto")


## Determina se il titolo fornito più sopra è mostrato nel main menu. Imposta su
## 'False' per nascondere il titolo.

define gui.show_name = False


## La versione del gioco.

define config.version = "Prototype 0.3"


## Testo che viene inserito nella schermata informazioni del gioco. Inserisci il
## testo tra triple virgolette e lascia una riga vuota tra i paragrafi.

define gui.about = _p("""
La Bambola della Porta Accanto

Una visual novel thriller psicologica.

Contenuti sensibili: manipolazione psicologica, violenza e autolesionismo.
""")


## Un nome abbreviato impiegato dagli eseguibili e dalle cartelle nelle
## distribuzioni compilate. Deve contenere solo caratteri ASCII e non può
## contenere spazi, due punti, o punti e virgole.

define build.name = "Labamboladellaportaaccanto"


## Suoni e musica ##############################################################

## Queste tre variabili controllano, tra le altre cose, quali mixer vengono
## mostrati al giocatore per impostazione predefinita. Impostando una di queste
## a False, si nasconde il mixer appropriato.

define config.has_sound = True
define config.has_music = True
# Non esistono ancora battute doppiate: evita un mixer Voce vuoto nelle impostazioni.
define config.has_voice = False


## Per consentire al giocatore di eseguire un test sonoro sui canali Suono o
## Voce, togli # dalla linea e usala per impostare un suono di esempio.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Togli # dalla linea seguente per impostare un file audio che sarà riprodotto
## durante il main menu. Continuerà a suonare fino a che non verrà interrotto o
## un altro file audio verrà suonato.

define config.main_menu_music = None


## Transizioni #################################################################
##
## Queste variabili impostano le transizioni che sono usate quando avvengono
## certi eventi. Ogni variabile deve essere impostata su una transizione, o su
## None per indicare che nessuna transizione deve venire usata.

## Entrare o uscire dal game menu.

define config.enter_transition = Dissolve(0.20)
define config.exit_transition = Dissolve(0.16)


## Tra le schermate del menu di gioco.

define config.intra_transition = Dissolve(0.18)


## Transizione usata dopo che una partita viene caricata.

define config.after_load_transition = Dissolve(0.22)


## Usata quando si torna al main menu dopo che è finita una partita.

define config.end_game_transition = Dissolve(0.30)


## Non esiste una variabile per impostare la transizione da usare quando inizia
## il gioco. Usa un comando 'with' subito dopo aver mostrato la prima 'scene'.


## Gestione finestra ###########################################################
##
## Controlla come viene mostrata la finestra dei dialoghi. Con "show", viene
## mostrata sempre. Con "hide", è mostrata solo quando ci sono linee di dialogo.
## Con "auto", la finestra è nascosta prima di un comando 'scene' e mostrata di
## nuovo al successivo dialogo.
##
## Dopo che il gioco ha avuto inizio, questo può essere cambiato coi comandi
## "window show", "window hide", and "window auto".

define config.window = "auto"


## Transizioni usate per mostrare e nascondere la finestra dei dialoghi

define config.window_show_transition = Dissolve(0.18)
define config.window_hide_transition = Dissolve(0.14)


## Opzioni predefinite #########################################################

## Controlla la velocità del testo predefinita. Lo standard, 0, è infinito,
## mentre qualunque altro numero indica il numero di caratteri al secondo da
## mostrare.

default preferences.text_cps = 0

# Mix iniziale bilanciato: musica in sottofondo, effetti chiari ma non invadenti.
default preferences.volume.music = 0.65
default preferences.volume.sfx = 0.78


## Il ritardo predefinito dell'avanzamento automatico. Numeri alti portano ad
## attese più lunghe, con un intervallo valido da 0 a 30.

default preferences.afm_time = 15


## Percorso Salvataggi #########################################################
##
## Controlla dove ren'Py pone i file di salvataggio, secondo la piattaforma. I
## file possono essere posti in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Di solito questo non dovrebbe venire cambiato, ma se lo fosse deve sempre
## essere una stringa diretta e non un'espressione.

define config.save_directory = "Labamboladellaportaaccanto-1791999556"


## Icona #######################################################################
##
## L'icona mostrata sulla dock o sulla barra applicazioni.

define config.window_icon = "gui/window_icon.png"


## Configura Compilazione ######################################################
##
## Questa sezione controlla come Ren'Py trasforma il tuo progetto in file di
## distribuzione.

init python:

    ## Le funzioni seguenti richiedono schemi di nome. Questi schemi non
    ## differenziano maiuscole e minuscole, e corrispondono al percorso relativo
    ## alla cartella base, con e senza un segno / preposto. Se più schemi
    ## corrispondono, viene usato il primo.
    ##
    ## In uno schema:
    ##
    ## / è il separatore fra cartelle.
    ##
    ## * equivale a qualunque carattere tranne il separatore fra cartelle.
    ##
    ## ** equivale a qualunque carattere inclusi i separatori fra cartelle.
    ##
    ## Per esempio, "*.txt" indica file .txt nella cartella base, "game/**.ogg"
    ## indica file .ogg nella cartella base o qualunque sua sottocartella, e
    ## "**.psd" indica file .psd ovunque nel progetto.

    ## Classifica file come 'None' per escluderli dalla compilazione.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('Mila.jpg', None)
    build.classify('Sophie.jpeg', None)

    ## Per archiviare i file, classificali come 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## I file che corrispondono a schemi di documentazione sono duplicati nella
    ## compilazione di app Macintosh, quindi appariranno sia nella app che nel
    ## file zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## Per eseguire gli acquisti in-app è necessaria una chiave di licenza
## Google Play. Si trova nella console per sviluppatori di Google Play, in
## "Monetizzazione" > "Impostazione monetizzazione" > "Licenze".

# define build.google_play_key = "..."


## L'username e project name associati a un progetto itch.io, separati da una
## slash.

# define build.itch_project = "renpytom/test-project"
