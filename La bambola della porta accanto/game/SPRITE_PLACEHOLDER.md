# Segnaposto sprite — guida alla sostituzione

Questa versione usa displayable Ren'Py provvisori definiti in `characters.rpy`. Non sono illustrazioni finali: servono a verificare posizionamento, ritmo visivo e cambi d'espressione senza aggiungere dipendenze o file immagine binari.

## Nomi da mantenere

- Mila: `sprite_mila_neutral`, `sprite_mila_worried`, `sprite_mila_tense`
- Sophie: `sprite_sophie_neutral`, `sprite_sophie_cold`, `sprite_sophie_tense`
- Kate: `sprite_kate_neutral`, `sprite_kate_worried`
- Madre: `sprite_madre_neutral`, `sprite_madre_cold`
- Padre: `sprite_padre_neutral`
- Madre di Sophie: `sprite_madre_sophie`
- Chloe: `sprite_chloe_neutral`

## Quando arriveranno gli sprite definitivi

1. Preparare immagini PNG con sfondo trasparente, idealmente con altezza uniforme e piedi allineati alla stessa baseline.
2. Mantenere silhouette, abiti e palette riconoscibili tra le espressioni dello stesso personaggio.
3. Sostituire le definizioni in `characters.rpy` con percorsi alle immagini, mantenendo gli stessi nomi `sprite_...` usati nello script.
4. Conservare le trasformazioni `sprite_stage_left`, `sprite_stage_right` e `sprite_stage_center`, oppure regolarle una sola volta per tutto il cast.
5. Creare almeno queste espressioni per Mila e Sophie: neutra, preoccupata, tesa e rivelazione; per Kate: neutra e preoccupata. Le espressioni devono cambiare soprattutto occhi, bocca e inclinazione del capo, senza cambiare identità.
6. Eseguire **Check Script (Lint)** dal launcher Ren'Py e provare tutte le scene ramificate.

## Regia già predisposta

Le scene di camera, cucina, scuola e casa dei vicini mostrano i segnaposto in posizioni coerenti. La variabile narrativa `tensione_scena` seleziona alcune varianti più tese. Le schermate di titolo dei capitoli restano libere da personaggi per mantenere leggibile il cartello narrativo.

**Nota:** questi segnaposto sono intenzionalmente temporanei; non vanno considerati asset artistici definitivi per una release.
