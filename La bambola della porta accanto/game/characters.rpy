# Sprite definitivi — collegamento agli asset in images/characters.
# Manteniamo i nomi immagine usati da script.rpy per non rompere le scene.

# Posizionamento coerente per sprite a figura intera (canvas 16:9, 1920x1080).
transform sprite_stage_left:
    xalign 0.08
    yalign 1.0
    zoom 0.54

transform sprite_stage_right:
    xalign 0.92
    yalign 1.0
    zoom 0.54

transform sprite_stage_center:
    xalign 0.5
    yalign 1.0
    zoom 0.46

# Secondo piano: per il padre dietro il giornale, senza competere con i primi piani.
transform sprite_stage_back:
    xalign 0.5
    yalign 1.0
    zoom 0.38
    alpha 0.88

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

# MILA — neutra, preoccupata e tesa.
image sprite_mila_neutral = "images/characters/mila_neutral.png"
image sprite_mila_worried = "images/characters/mila_worried.png"
image sprite_mila_tense = "images/characters/mila_tense.png"

# SOPHIE — la calma apparente lascia spazio a freddezza e tensione.
image sprite_sophie_neutral = "images/characters/sophie_neutral.png"
image sprite_sophie_cold = "images/characters/sophie_cold.png"
image sprite_sophie_tense = "images/characters/sophie_tense.png"

# KATE — espressioni aperte e preoccupate.
image sprite_kate_neutral = "images/characters/kate_neutral.png"
image sprite_kate_worried = "images/characters/kate_worried.png"

# Famiglia di Mila.
image sprite_madre_neutral = "images/characters/mamma_mila_neutral.png"
image sprite_madre_cold = "images/characters/mamma_mila_cold.png"
image sprite_padre_neutral = "images/characters/sprite_padre_mila.png"

# Famiglia di Sophie e personaggi secondari.
image sprite_madre_sophie = "images/characters/sprite_madre_sophie.png"
image sprite_chloe_neutral = "images/characters/sprite_chloe_neutral.png"
