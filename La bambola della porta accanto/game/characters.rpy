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

# Inquadrature dedicate ai PNG tagliati dalla coscia in su.
# Il bordo inferiore resta dietro la finestra di dialogo, per evitare l'effetto
# di un personaggio "appoggiato" a terra senza gambe visibili.
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
    zoom 0.70
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

# KATE — sprites aggiornati a mezzo busto (dalla coscia in su).
# Normalizziamo l'altezza della tela, così le espressioni restano coerenti tra loro.
image sprite_kate_neutral = Transform("images/characters/kate_neutral.png", ysize=1185, fit="contain")
image sprite_kate_worried = Transform("images/characters/kate_worried.png", ysize=1185, fit="contain")

# Padre di Mila: ritratto a mezzo busto, normalizzato come gli altri personaggi.
image sprite_padre_neutral = Transform("images/characters/sprite_padre_mila.png", ysize=1350, fit="contain")

# Famiglia di Sophie e personaggi secondari: ritratti a mezzo busto normalizzati.
image sprite_madre_sophie = Transform("images/characters/sprite_madre_sophie.png", ysize=1350, fit="contain")
image sprite_chloe_neutral = Transform("images/characters/sprite_chloe_neutral.png", ysize=1185, fit="contain")
