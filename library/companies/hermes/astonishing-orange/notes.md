# Astonishing orange  (Hermès, 2023-09-19, 0:45, 16:9, YouTube @hermes)
URL: https://www.youtube.com/watch?v=5lYcf5k0ieE
Purpose: seasonal brand film (fashion, colour story), no voice
One-sentence point: The Hermès orange is a mood that moves through the city, from warm ochre through blue night into full red.

## Structure (colour chapters)
- 0-3.7 **Ochre**: one wide, locked shot of a woman in a camel suit against a sandstone wall in hard sunlight (3.7 s).
- 3.7-14 ochre/yellow: low angle on her face, legs over yellow road markings, a top shot of her shadow on a zebra crossing, a red car passes.
- 13.8-22 **Smoke and grey**: a smoke cloud fills the street (4.6 s, longest shot), a white horse led by a young man in grey appears in the smoke.
- 22-32 **Blue night**: canted silhouettes against a deep blue sky, a cyclist on a wet street seen from above, a man in a black coat, a spinning shot through a round hole.
- 32-45 **Red**: through a round hole in a red wall into the red world; a woman in all red with a riding crop, a red car with flame reflections, extreme top and tilted angles; "Astonishing orange" written on the picture (41-43 s); final top shot of her red cap.

## Cut rhythm
- 28 shots in 45 s. ASL 1.61 s, median 1.42 s, 25 % under 1 s, 37 shots per minute.
- ASL per quarter 1.88 / 1.13 / 1.25 / 1.88 s.
- Cuts per 10 s: 5, 5, 9, 6, 2.
- Longest 4.56 s (13.76, smoke), 3.68 s (opening wide), 2.54 s (42.48, end). Shortest 0.52 s.
- Cuts on onsets 7 % vs 16 % chance (not cut to the beat).

## Typography
- One line only: "Astonishing orange", humanist/geometric sans, sentence case, white (closest free: Jost / Outfit), cap height ≈3.3 % H, set on the diagonal of the canted frame (≈30°) across the subject, ≈40 % from the left. No logo end card at all.

## Colour/grade
- The film is a colour progression: ochre/amber → grey smoke → saturated blue → saturated red. Each chapter matches wardrobe, location and grade to one hue; skin stays natural.
- High contrast, hard sun, deep shadows, light grain.

## Camera/shots
- Fashion-film grammar: canted frames (20-35°), top shots, extreme low angles, fast whip/spin moves in the blue section, locked wides at the start and end.
- A horse as the brand symbol, never explained.

## Transitions
- Hard cuts; smoke used as a wipe (14-18 s); a round hole (porthole) as a mask transition from the blue world into the red world (31-33 s).

## Sound
- No voice. Music with a strong groove; integrated -13.7 LUFS, LRA 10.5 LU, true peak -0.2 dBTP. One big rise at the start (+25 dB at 0.55 s); 1.05 s silence at the very end.

## What makes it premium
- Colour as the story: no words needed.
- Few shots (28), each a composed fashion photograph.
- The only text is the name of the colour, placed like graffiti on the image, and there is no logo card.

## Recipe
- Plan 3-4 colour chapters of 8-12 s; wardrobe, set and grade in the chapter hue (CSS: one `filter` per chapter, e.g. blue `saturate(1.3) hue-rotate(10deg) brightness(.85)`).
- 25-30 shots for 45 s, 0.5-4.6 s, open and close on locked wides.
- Chapter change by a physical wipe (smoke, a hole in a wall): `clip-path: circle(0% at 50% 50%)` → `circle(75%)` over 0.8 s.
- One text line at 3.3vh, `transform: rotate(-30deg)`, on the last chapter; no end card.
