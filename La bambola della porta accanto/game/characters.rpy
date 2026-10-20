# Sprite definitivi — collegamento agli asset in images/characters.
# Le immagini hanno ora tutte la stessa tela: le normalizziamo con un'unica altezza
# visiva (1185 px). La scala finale dipende solo dal transform della scena, non dalla
# singola espressione: i cambi di volto non devono far ingrandire o rimpicciolire il personaggio.

# Posizionamento coerente per sprite con tela uniforme (canvas 16:9, 1920x1080).
# Posizionamento dedicato alla scena iniziale nella camera di Sophie:
# Sophie è leggermente più bassa e sta a sinistra; Mila si sposta a destra.
transform sprite_stage_left_sophie:
    xalign 0.34
    yalign 1.0
    zoom 0.64

# Sophie resta leggermente più bassa di Mila anche sul lato destro, nel capitolo 1.
transform sprite_stage_right_sophie:
    xalign 0.69
    yalign 1.0
    zoom 0.64

transform sprite_stage_right_mila:
    xalign 0.72
    yalign 1.0
    zoom 0.70

# Posizioni statiche e di avvicinamento: usare la variante coerente con il lato
# da cui arriva il personaggio. Le varianti "near" servono ai cambi d'espressione
# dopo che il movimento è terminato, così lo sprite non riparte da lontano.
transform sprite_approach_mila:
    xalign 0.43
    yalign 1.0
    zoom 0.64
    ease 0.65 xalign 0.49

transform sprite_stage_near_mila_left:
    xalign 0.49
    yalign 1.0
    zoom 0.64

transform sprite_approach_mila_from_right:
    xalign 0.69
    yalign 1.0
    zoom 0.64
    ease 0.65 xalign 0.53

transform sprite_stage_near_mila_from_right:
    xalign 0.53
    yalign 1.0
    zoom 0.64

# La madre avanza appena verso Mila durante la presa alla mascella.
transform sprite_mother_approach:
    xalign 0.69
    yalign 1.0
    zoom 0.70
    ease 0.55 xalign 0.63

# Posizione stabile ravvicinata: evitare che un cambio d'espressione faccia
# ripartire da capo l'animazione di avvicinamento.
transform sprite_mother_close:
    xalign 0.63
    yalign 1.0
    zoom 0.70

# Il padre appare appena sulla soglia: più arretrato, spostato a destra e semi-trasparente.
transform sprite_father_threshold_hidden:
    xalign 0.89
    yalign 1.0
    zoom 0.60
    alpha 0.60
    ease 0.9 xalign 0.86 alpha 0.66

# Trasformazione unica per l'avvicinamento teso: mantiene una sola scala (0.64)
# e aggiunge il tremore senza applicare un secondo zoom allo sprite.
transform sprite_approach_mila_tense:
    xalign 0.43
    yalign 1.0
    zoom 0.64
    ease 0.65 xalign 0.49
    block:
        ease 0.85 xoffset -2
        ease 0.90 xoffset 2
        ease 0.85 xoffset 0
        repeat

# Disegno di Sophie su fondo bianco uniforme: le aree trasparenti del PNG
# non devono mostrare la scacchiera di trasparenza ai lati. Il disegno resta intero,
# centrato e proporzionato sul canvas 16:9 (1920x1080).
image sophie_draw_fullscreen = Composite(
    (1920, 1080),
    (0, 0), Solid("#ffffff", xysize=(1920, 1080)),
    (0, 0), Transform(
        "images/backgrounds/sophie_draw.png",
        xysize=(1920, 1080),
        fit="contain",
        xalign=0.5,
        yalign=0.5
    )
)

# Movimento d'inquadratura: piccoli push-in cinematografici, senza tagli bruschi.
transform bg_slow_push:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    ease 18.0 zoom 1.035

transform bg_tension_push:
    xalign 0.5
    yalign 0.5
    zoom 1.0
    ease 8.0 zoom 1.045

# Reazioni fisiche brevi, sincronizzate con le frasi che fanno scattare la paura.
transform sprite_flinch:
    xoffset 0
    ease 0.08 xoffset -5
    ease 0.14 xoffset 3
    ease 0.22 xoffset 0

transform sprite_recoil:
    xoffset 0
    ease 0.12 xoffset 11
    ease 0.35 xoffset 0

transform sprite_page_shift:
    xoffset 0
    ease 0.22 xoffset -2
    ease 0.32 xoffset 0

# Respiro più irregolare nei momenti di ansia: visibile, ma non caricaturale.
transform sprite_anxious_breathe:
    yoffset 0
    ease 0.75 yoffset -5
    ease 1.05 yoffset 1
    ease 0.65 yoffset 0
    repeat

# Un sollevamento minimo della posa per accompagnare il sorriso forzato di Mila.
transform sprite_smile_lift:
    yoffset 0
    ease 0.75 yoffset -5
    pause 0.3
    ease 0.7 yoffset 0

# Micro-tensione di Sophie: un'oscillazione laterale minima durante le frasi possessive.
# È separata dal posizionamento dello sprite, così può essere combinata con sprite_stage_right.
transform sprite_micro_tension:
    xoffset 0
    ease 0.85 xoffset -2
    ease 0.90 xoffset 2
    ease 0.85 xoffset 0
    repeat

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

# Alias di posizionamento mantenuti per non cambiare i riferimenti nelle scene.
# Poiché le tele sono uniformi, questi alias non applicano più una scala diversa
# rispetto agli sprite laterali standard.
transform sprite_stage_left_halfbody:
    xalign 0.31
    yalign 1.0
    zoom 0.70

transform sprite_stage_right_halfbody:
    xalign 0.69
    yalign 1.0
    zoom 0.70

transform sprite_stage_back_halfbody:
    xalign 0.52
    yalign 1.0
    zoom 0.58
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

# Tutte le espressioni sono normalizzate alla stessa altezza. Non usare valori diversi
# per neutral/worried/tense/fury: cambiare espressione non deve alterare la sagoma.
# MILA
image sprite_mila_neutral = Transform("images/characters/mila_neutral.png", ysize=1185, fit="contain")
image sprite_mila_worried = Transform("images/characters/mila_worried.png", ysize=1185, fit="contain")
image sprite_mila_tense = Transform("images/characters/mila_tense.png", ysize=1185, fit="contain")
image sprite_mila_fear = Transform("images/characters/mila_fear.png", ysize=1185, fit="contain")
image sprite_mila_smile = Transform("images/characters/mila_smile.png", ysize=1185, fit="contain")

# SOPHIE — la calma apparente lascia spazio a freddezza e tensione.
image sprite_sophie_neutral = Transform("images/characters/sophie_neutral.png", ysize=1185, fit="contain")
image sprite_sophie_cold = Transform("images/characters/sophie_cold.png", ysize=1185, fit="contain")
image sprite_sophie_tense = Transform("images/characters/sophie_tense.png", ysize=1185, fit="contain")
image sprite_sophie_sweet = Transform("images/characters/sophie_sweet.png", ysize=1185, fit="contain")
image sprite_sophie_anger = Transform("images/characters/sophie_anger.png", ysize=1185, fit="contain")
image sprite_sophie_fury = Transform("images/characters/sophie_fury.png", ysize=1185, fit="contain")

# KATE — tutte le espressioni condividono la stessa altezza di tela.
image sprite_kate_neutral = Transform("images/characters/kate_neutral.png", ysize=1185, fit="contain")
image sprite_kate_worried = Transform("images/characters/kate_worried.png", ysize=1185, fit="contain")
image sprite_kate_smile = Transform("images/characters/kate_smile.png", ysize=1185, fit="contain")
image sprite_kate_fear = Transform("images/characters/kate_fear.png", ysize=1185, fit="contain")

# Madre di Mila: tutte le varianti, compresa la rabbia, hanno la stessa altezza di tela.
image sprite_madre_neutral = Transform("images/characters/sprite_madre_neutral.png", ysize=1185, fit="contain")
image sprite_madre_cold = Transform("images/characters/sprite_madre_cold_accappatoio.png", ysize=1185, fit="contain")
image sprite_madre_neutral_accappatoio = Transform("images/characters/sprite_madre_neutral_accappatoio.png", ysize=1185, fit="contain")
image sprite_madre_neutral_2 = Transform("images/characters/sprite_madre_neutral_2.png", ysize=1185, fit="contain")
image sprite_madre_fury = Transform("images/characters/sprite_madre_fury.png", ysize=1185, fit="contain")

# Padre di Mila: normalizzato come gli altri personaggi.
image sprite_padre_neutral = Transform("images/characters/sprite_padre_mila.png", ysize=1185, fit="contain")

# Famiglia di Sophie e personaggi secondari: stessa normalizzazione delle immagini principali.
image sprite_madre_sophie = Transform("images/characters/sprite_madre_sophie.png", ysize=1185, fit="contain")
image sprite_chloe_neutral = Transform("images/characters/sprite_chloe_neutral.png", ysize=1185, fit="contain")
