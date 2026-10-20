# introducing EP-1320 medieval  (teenage engineering, 2024-08-06, 1:05, 16:9, YouTube; source 360p)
URL: https://www.youtube.com/watch?v=LVLsRvGMwMk
Purpose: launch film (art-house concept film for a sampler with medieval instruments)
One-sentence point: A strange medieval ritual (fire ring, horse, masked people, banners) slowly gathers around a red altar, and on the altar sits the EP-1320 - "the world's very first medieval electronic instrument".

Structure:
- 0.0-4.4 hook: wide on a grey hillside, a ring of fire on the ground, a rider on a horse in white robes, a girl standing (frames/t001.5s.jpg). Quiet ambience until 3.3 s, then the music starts (+51 dB hit).
- 4.4-23.8 build: tableau after tableau, each 1-3 s: feathered black mask CU, a white bird, the horse led away, silhouette with a flag at dusk (t010.8s), a man with a moustache, a liquid bowl from below, a geometric white cardboard mask (t014.8s), banners in a meadow with seated hooded figures, smoke in a forest with a red-masked figure, fire on a slope (t022.0s).
- 23.8-47.2 middle: more tableaux - bare feet in the air, a line-up of white costumes with geometric masks against a rock wall (t030.0s), feet walking on fire, a tower window, masked figures with drums, a kneeling robed man with a harp next to a horse, a wall of fire (46.1).
- 47.2-53.8 reveal: the product, a gold/cream calculator-like sampler, sits on a red cloth altar on cracked grey ground (t049.0s), held 6.6 s; a figure walks behind it.
- 53.8-60.4 payoff: high top-down wide, dozens of black-robed people with banners in a geometric formation around the red altar (t057.0s), 6.6 s.
- 60.4-64.9 end: blackletter title "Medieval" (big red decorated initial M, cream letters) + small caps "ELECTRONICUM INSTRUMENTALIS" on dark brown-black (t061.0s); then the TE pictogram logo + "EP series" + legal.

Cut rhythm: 26 shots, ASL 2.50 s, median 2.14 s, quarters 1.80 / 2.03 / 2.03 / 4.05 (it slows down for the reveal and the formation). Shortest 0.60 s (12.1), longest 6.6 s (product) and 6.56 s (formation). Only 4 % under 1 s, 23 % over 3 s. Densest 10-20 s (7 cuts). Cuts on onset 40 % vs 18 % chance = the editor cuts on the music's hits (strongest beat sync of all TE/Nothing examples).

Typography: none until the end. Title = decorated blackletter (Lombardic red initial + textura-style lowercase; free match: UnifrakturMaguntia or "Pirata One" for the lowercase, a Lombardic initial like "Lombardic Capitals" for the M), the word block ~37 % of frame height and 72 % of the width - huge, unlike TE's usual tiny type. Subtitle in a plain wide sans caps (~2.2 % height, slight tracking) under it. Background warm near-black. Then the normal TE logo (pictogram ~16 % height) + tiny legal.

Colour/grade: film-like, slightly faded teal-grey: overcast skies, grey sand and rock, desaturated greens (median saturation 23 %), lifted blacks, soft contrast. Accents: fire orange and a red/orange used on costumes, banners and the altar cloth. Median luma 111, R-B +8 (neutral-warm). Feels like 1970s European art cinema (Jodorowsky / Parajanov tableaux - my comparison, not stated by TE).

Camera/shots: mostly locked-off frontal tableaux (symmetric, people facing camera, flat staging), some close-ups and inserts (feet, bowl, bird), real fire and smoke practical effects, one high top-down drone/crane shot of the formation. Very little camera movement.

Transitions: hard cuts only; rhythm from the music. Black end card after a hard cut.

Sound: medieval-sounding music (presumably the EP-1320's own samples - drums, plucked strings, voices; I cannot hear it, this is from the product description). Opens with 3 s of quiet ambience (-39 LUFS-M), then a steady level -19 to -21 LUFS-M to the end. Integrated -21.1 LUFS - very quiet for an online ad; TE does not chase loudness. No voice-over.

What makes it premium:
- Full commitment to one world (costume, location, music, type) - the product is a prop in that world.
- The product appears only at 73 % of the runtime, on an altar: the whole film is the build-up.
- Tableau framing (frontal, symmetric, still) = art direction carries the film, not camera moves.
- Typography switches to the theme (blackletter) while the brand mark stays the same tiny TE logo.

Recipe (real footage + HTML/GSAP):
1. Pick a "world" that matches the product's sound; shoot 20-25 frontal tableaux (locked tripod, symmetric, 1 accent colour like #c8402a) + 4-5 inserts + 1 top-down formation.
2. Edit 1.5-2.5 s per tableau, cut on music hits (aim for 40 % of cuts on hits); reveal the product at ~70-75 %, hold 6 s; then a 6 s top-down payoff.
3. Grade: lift blacks (+5 %), saturation ~25 %, slight teal in shadows; keep fire and the accent colour saturated.
4. Title card HTML: `background:#140c08`, initial letter `font-family:'UnifrakturMaguntia'; color:#a8321e; font-size:30vh`, rest `color:#d6d0c4; font-size:24vh`, subtitle `font: 500 1.9vh 'Inter'; letter-spacing:.12em; text-transform:uppercase`. Fade in 0.3 s, hold 2 s, cut to the brand mark 2 s.
5. Mix: quiet open (3 s ambience), music in on a hit, keep it around -20 LUFS-M; no VO.
