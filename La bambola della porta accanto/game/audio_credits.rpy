# Pagina dedicata ai crediti delle risorse audio.
# La schermata è raggiungibile dai menu tramite il pulsante "Crediti audio".

screen audio_credits():
    tag menu

    use game_menu(_("Crediti audio"), scroll="viewport"):

        style_prefix "about"

        vbox:
            spacing 22

            label _("Musiche e ambientazioni")

            text "{a=https://freesound.org/s/575465/}003 - Rain on Driveway.wav{/a} — Trashcan_Studios\nLicenza: {a=https://creativecommons.org/licenses/by/4.0/}Creative Commons Attribution 4.0 (CC BY 4.0){/a}"

            text "{a=https://freesound.org/s/756313/}CORONACH{/a} — MadGravityStudio\nLicenza: {a=https://creativecommons.org/licenses/by/4.0/}Creative Commons Attribution 4.0 (CC BY 4.0){/a}"

            text "{a=https://freesound.org/s/674392/}Dark Cold Main Menu Loop - Mild Mountain Sickness - Marb7e{/a} — marb7e\nLicenza: {a=https://creativecommons.org/licenses/by/4.0/}Creative Commons Attribution 4.0 (CC BY 4.0){/a}"

            text "{a=https://freesound.org/s/322030/}Tension building intro{/a} — LunarThePunar\nLicenza: {a=https://creativecommons.org/licenses/by/3.0/}Creative Commons Attribution 3.0 (CC BY 3.0){/a}"

            null height 8

            label _("Effetti sonori")

            text "{a=https://freesound.org/s/213408/}WoodDoorClose1.wav{/a} — chewiesmissus\nLicenza: {a=https://creativecommons.org/publicdomain/zero/1.0/}Creative Commons Zero (CC0 1.0){/a}"

            text "{a=https://freesound.org/s/676470/}Lighter - Medium{/a} — NearTheAtmoshphere\nLicenza: {a=https://creativecommons.org/publicdomain/zero/1.0/}Creative Commons Zero (CC0 1.0){/a}"

            text "{a=https://freesound.org/s/685583/}Window Knock{/a} — ZyrofomeAnimations\nLicenza: {a=https://creativecommons.org/publicdomain/zero/1.0/}Creative Commons Zero (CC0 1.0){/a}"

            null height 8

            label _("Altre tracce")

            text _("Il repository include anche quattro tracce procedurali originali: music_memory, music_investigation_new, music_tension_new e music_ending_new. Non contengono brani di terzi e non richiedono attribuzione esterna.")

            text _("Per i dettagli e le fonti complete, consulta anche il file CREDITI_AUDIO.md incluso nel progetto.")
