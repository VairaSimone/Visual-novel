# Sprite provvisori per "La bambola della porta accanto".
# Sono displayable Ren'Py costruiti con forme e tipografia: non richiedono file binari.
# Quando arrivano le illustrazioni definitive, basta sostituire queste definizioni
# mantenendo gli stessi nomi immagine (sprite_mila_neutral, sprite_mila_tense, ecc.).
#
# Regia: le varianti "tense" cambiano postura, contrasto e micro-espressione.
# Sono volutamente segnaposto, non concept art definitiva.

init python:
    def _portrait_placeholder(name, hair, skin, clothes, mood, subtitle):
        moods = {
            "neutral": ("•  •", "—", "#f0dfe6"),
            "worried": ("•  •", "﹏", "#e7c5c9"),
            "tense": ("◉  ◉", "︵", "#f1a8ad"),
            "cold": ("•  •", "⌁", "#c9c0d4"),
            "sad": ("•  •", "﹀", "#aebddd"),
            "smile": ("•  •", "⌣", "#d9e7cf"),
        }
        eyes, mouth, accent = moods[mood]
        # Il pannello resta trasparente: il fondale continua a essere visibile.
        return Fixed(
            Transform(Text("●", size=260, color=hair), xpos=115, ypos=35),
            Transform(Text("●", size=205, color=skin), xpos=143, ypos=70),
            Transform(Text("▲", size=430, color=clothes), xpos=40, ypos=270),
            Transform(Text(eyes, size=36, color="#241b24"), xpos=207, ypos=166),
            Transform(Text(mouth, size=58, color="#6b3542"), xpos=224, ypos=211),
            Transform(Text(name.upper(), size=31, color="#fff2f5", outlines=[(2, "#201923", 0, 0)]), xpos=115, ypos=680),
            Transform(Text("SPRITE PROVVISORIO", size=16, color=accent), xpos=118, ypos=724),
            Transform(Text(subtitle.upper(), size=17, color="#d6c4d0"), xpos=118, ypos=752),
            xsize=520, ysize=820
        )

# Posizionamento coerente sullo schermo; sostituibile senza toccare le scene.
transform sprite_stage_left:
    xalign 0.08
    yalign 1.0
    zoom 0.72

transform sprite_stage_right:
    xalign 0.92
    yalign 1.0
    zoom 0.72
    
transform sprite_stage_center:
    xalign 0.5
    yalign 1.0
    zoom 0.58

# MILA — palette fredda, posture raccolte; la tensione irrigidisce il volto.
image sprite_mila_neutral = _portrait_placeholder("Mila", "#352b3b", "#e6c2b1", "#64788c", "neutral", "controllo")
image sprite_mila_worried = _portrait_placeholder("Mila", "#352b3b", "#e6c2b1", "#64788c", "worried", "allarme")
image sprite_mila_tense = _portrait_placeholder("Mila", "#241c2c", "#e6c2b1", "#4b536b", "tense", "tensione")

# SOPHIE — colori rosa spenti; la variante fredda anticipa manipolazione e minaccia.
image sprite_sophie_neutral = _portrait_placeholder("Sophie", "#a85f72", "#f0d1c5", "#9d586f", "neutral", "controllo apparente")
image sprite_sophie_cold = _portrait_placeholder("Sophie", "#653748", "#f0d1c5", "#653748", "cold", "distanza")
image sprite_sophie_tense = _portrait_placeholder("Sophie", "#512a3a", "#f0d1c5", "#7d354d", "tense", "rivelazione")

# KATE — palette più luminosa e aperta, per dare contrasto alle scene scolastiche.
image sprite_kate_neutral = _portrait_placeholder("Kate", "#b18a52", "#f0cbb4", "#6886a8", "smile", "fiducia")
image sprite_kate_worried = _portrait_placeholder("Kate", "#8b6b45", "#f0cbb4", "#536b8a", "worried", "preoccupazione")

# GENITORI — silhouette volutamente più rigide e desaturate.
image sprite_madre_neutral = _portrait_placeholder("Mamma", "#51433d", "#d8b7a0", "#75645f", "neutral", "facciata")
image sprite_madre_cold = _portrait_placeholder("Mamma", "#382f30", "#d8b7a0", "#554448", "cold", "pressione")
image sprite_padre_neutral = _portrait_placeholder("Papà", "#77716d", "#d8b7a0", "#647078", "sad", "silenzio")
image sprite_madre_sophie = _portrait_placeholder("Madre di Sophie", "#b3a18a", "#e7c8b1", "#a99a8a", "neutral", "distanza")

# Personaggi secondari: segnaposto pronti per le scene future.
image sprite_chloe_neutral = _portrait_placeholder("Chloe", "#6c5145", "#efcbb8", "#8e9aaf", "worried", "nuovo inizio")

