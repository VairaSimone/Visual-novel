# Colonna sonora originale procedurale del progetto (WAV mono, 22.05 kHz, PCM 16 bit).
# Musica, ambiente e SFX usano canali distinti: i crossfade non interrompono la pioggia.
# I nuovi temi usano armoniche morbide, note con coda risonante e droni lenti; nessun brano
# di terzi è incorporato, quindi non sono necessarie attribuzioni esterne per queste tracce.

init python:
    # Condivide il mixer Effetti con i suoni, ma non interrompe il canale Musica.
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, tight=True)
    renpy.music.set_volume(0.42, delay=0, channel="ambience")

define audio.rain = "audio/ambience_rain.wav"
define audio.room = "audio/ambience_room.wav"

# Tema principale: malinconico e ambiguo, condiviso dal menu e dai ricordi di Mila.
define audio.menu_theme = "audio/music_memory.wav"
define audio.memory = "audio/music_memory.wav"

# La musica cambia con l'indagine, il livello di sospetto e il tipo di finale.
define audio.investigation = "audio/music_investigation_new.wav"
define audio.tension = "audio/music_tension_new.wav"
define audio.ending = "audio/music_ending_new.wav"

define audio.lighter = "audio/sfx_lighter.wav"
define audio.window_knock = "audio/sfx_window_knock.wav"
define audio.phone = "audio/sfx_phone.wav"
define audio.heartbeat = "audio/sfx_heartbeat.wav"
define audio.glass = "audio/sfx_glass.wav"
define audio.door = "audio/sfx_door.wav"

# Ren'Py esegue questa label quando torna al menu principale.
label before_main_menu:
    play music audio.menu_theme fadein 2.5
    return
