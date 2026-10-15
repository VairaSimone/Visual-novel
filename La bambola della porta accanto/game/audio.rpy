# Audio originale generato localmente per il progetto (WAV mono, 22.05 kHz, PCM 16 bit).
# Le tracce musicali sono separate dagli ambienti per consentire il crossfade indipendente.

init python:
    # Condivide il mixer Effetti con i suoni, ma non interrompe il canale Musica.
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, tight=True)

define audio.rain = "audio/ambience_rain.wav"
define audio.room = "audio/ambience_room.wav"
define audio.menu_theme = "audio/music_menu.wav"
define audio.investigation = "audio/music_investigation.wav"
define audio.tension = "audio/music_tension.wav"
define audio.lighter = "audio/sfx_lighter.wav"
define audio.window_knock = "audio/sfx_window_knock.wav"
define audio.phone = "audio/sfx_phone.wav"
define audio.heartbeat = "audio/sfx_heartbeat.wav"
define audio.glass = "audio/sfx_glass.wav"
define audio.door = "audio/sfx_door.wav"
