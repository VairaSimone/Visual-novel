# Sprite definitivi — collegamento agli asset in images/characters.
# Manteniamo i nomi immagine usati da script.rpy per non rompere le scene.

# Posizionamento coerente per sprite a figura intera (canvas 16:9, 1920x1080).
# Posizionamento dedicato alla scena iniziale nella camera di Sophie:
# Sophie è leggermente più bassa e sta a sinistra; Mila si sposta a destra.
transform sprite_stage_left_sophie:
    xalign 0.34
    yalign 1.0
    zoom 0.64

transform sprite_stage_right_mila:
    xalign 0.72
    yalign 1.0
    zoom 0.70

# Sophie si avvicina a Mila quando invade il suo spazio personale.
transform sprite_approach_mila:
    xalign 0.43
    yalign 1.0
    zoom 0.64
    ease 0.65 xalign 0.49

# Placeholder verticale da sostituire con il disegno definitivo.
transform disegno_bambola_mostra:
    zoom 0.48

image disegno_bambola_placeholder = "images/disegno_bambola_placeholder.png"

transform sprite_stage_left:
    xalign 0.31
    yalign 1.0
    zoom 0.70

transform sprite_stage_right:
    xalign 0.69
    yalign 1.0
    zoom 0.70

transform sprite_stage_center:
    xalign 0.5
    yalign 1.0
    zoom 0.72

# Secondo piano: per il padre dietro il giornale, senza competere con i primi piani.
transform sprite_stage_back:
    xalign 0.52
    yalign 1.0
    zoom 0.48
    alpha 0.82

# Movimento d'attesa delicato: evita che i personaggi sembrino completamente statici.
transform sprite_breathe:
    yoffset 0
    ease 2.2 yoffset -3
    ease 2.4 yoffset 0
    repeat

# Tremore breve e irregolare riservato ai momenti in cui la paura emerge.
transform sprite_tremble:
    xoffset 0
    ease 0.18 xoffset -2
    ease 0.16 xoffset 1
    ease 0.20 xoffset 0
    pause 1.1
    repeat

# La freddezza di Sophie e della madre si esprime soprattutto attraverso l'immobilità.
transform sprite_cold_still:
    yoffset 0
    pause 3.0
    ease 0.35 yoffset -1
    ease 0.35 yoffset 0
    repeat

# MILA — PNG sorgente più bassi degli altri personaggi: normalizzati a 1185 px di altezza
# prima dei trasformatori di scena, così mantengono dimensioni coerenti anche al centro.
# MILA — neutra, preoccupata e tesa.
image sprite_mila_neutral = Transform("images/characters/mila_neutral.png", ysize=1185, fit="contain")
image sprite_mila_worried = Transform("images/characters/mila_worried.png", ysize=1185, fit="contain")
image sprite_mila_tense = Transform("images/characters/mila_tense.png", ysize=1185, fit="contain")

# SOPHIE — anche questi PNG hanno un'altezza sorgente ridotta: stessa altezza visiva di riferimento.
# SOPHIE — la calma apparente lascia spazio a freddezza e tensione.
image sprite_sophie_neutral = Transform("images/characters/sophie_neutral.png", ysize=1185, fit="contain")
image sprite_sophie_cold = Transform("images/characters/sophie_cold.png", ysize=1185, fit="contain")
image sprite_sophie_tense = Transform("images/characters/sophie_tense.png", ysize=1185, fit="contain")

# KATE — espressioni aperte e preoccupate.
image sprite_kate_neutral = "images/characters/kate_neutral.png"
image sprite_kate_worried = "images/characters/kate_worried.png"

# La madre di Mila viene normalizzata insieme a Mila e Sophie; gli altri sprite più grandi
# restano invariati, così non aumentano accidentalmente di dimensione.
# Famiglia di Mila.
image sprite_madre_neutral = Transform("images/characters/mamma_mila_neutral.png", ysize=1185, fit="contain")
image sprite_madre_cold = Transform("images/characters/mamma_mila_cold.png", ysize=1185, fit="contain")
image sprite_padre_neutral = "images/characters/sprite_padre_mila.png"

# Famiglia di Sophie e personaggi secondari.
image sprite_madre_sophie = "images/characters/sprite_madre_sophie.png"
image sprite_chloe_neutral = "images/characters/sprite_chloe_neutral.png"
