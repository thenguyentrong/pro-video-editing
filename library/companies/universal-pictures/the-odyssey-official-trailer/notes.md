# The Odyssey | Official Trailer  (Universal Pictures, 22 Dec 2025, 113.6 s incl. 5.0 s MPA band, 16:9 file / 2.39:1 picture, YouTube)
URL: https://www.youtube.com/watch?v=Mzw2ttJD2qQ
Purpose: main trailer (first full trailer, about 7 months before release)
One-sentence point: an ancient war is over and one man must cross a hostile sea to get home; sold on scale, mud and darkness rather than on plot.

## Structure (beats with timestamps; % of 113.6 s)
- 0.0–5.0 green MPA band, digital silence (counted as one shot in metrics).
- 5.0–6.45 black; music enters at about −31 dBFS.
- 6.45–10.7 **Universal logo** (fade up), 10.7–14.75 **Syncopy logo** (metal maze letters). No cold open: the logos come first (6–13 %).
- 14.75–21.6 **first image, held 6.8 s**: a desert battlefield of fallen helmets and one kneeling warrior; first hit at 14.85 (+22.7 dB).
- 21.6–28.1 **one handheld 6.5 s take** of two helmeted warriors face to face (hit +19.8 dB at 21.75, the first loud moment, −10 dBFS).
- 28.1–29.6 black. 29.6–37.1 army walking through a forest of ship masts (3.6 + 4.0 s). 37.1–37.9 black. 37.9–42.5 fortress on a cliff in fog (4.6 s).
- 42.5–44.8 two close-ups (1.38, 0.96 s), the only fast pair in the first half. 44.8–52.6 night sea, ship silhouettes (3.9 + 3.9 s).
- 52.6–56.4 **card "FROM / CHRISTOPHER NOLAN"** on black (3.8 s, 46 %).
- 56.4–83.6 **Act 2**: rider on a beach, men in a dark hold, mud, a cave, firelight, running soldiers on a green coast, a helmet close-up, campfire (ASL ≈1.9 s, densest 6 cuts per 10 s at 70–80 s = 62–70 %).
- 83.6–87.5 **card "THIS SUMMER"** (3.9 s, 74 %).
- 87.5–98.8 storm at sea: deck, oars, waves (ASL ≈1.9 s), the loudest stretch (−10 to −12 dBFS RMS, peak 0.5 s at 92.05).
- 98.8–101.8 **black, 3.0 s**: the music falls from −11 to −23 dBFS (no hard silence). 101.8–103.75 one face in firelight (1.95 s).
- 103.75–109.8 **title** "THE / ODYSSEY" fades up (6.05 s, at 91 %). 109.8–111.8 date "07.17.26" (2.0 s). 111.8–113.6 billing block + "SHOT ENTIRELY WITH IMAX FILM CAMERAS" (1.75 s).

## Cut rhythm
- 41 shots incl. band, logos and cards (adaptive detector + 8 cuts added by eye for fades out of black and card changes). **ASL 2.77 s**, median 2.38 s; without the MPA band ≈2.7 s.
- ASL per quarter **4.06 · 2.58 · 2.03 · 2.37 s**. 10 % of shots under 1 s, 37 % over 3 s. 21.7 shots per minute.
- Longest story shots 6.8 s and 6.5 s (the first two images). Shortest 0.78 s (black) and 0.83 s.
- Cuts per 10 s: 2 2 3 3 4 3 3 6 5 5 3 1. Cuts on audio onsets 25 % vs 21 % chance: the edit follows the score's long phrases, not its beats.
- 8 black holds of 0.8–3.9 s (two of them carry the text cards).
- Speech detection found only ≈1 s of dialogue: the trailer is carried by music and images.

## Typography
- One system for every card: a wide geometric sans in caps (closest free font: Montserrat 500), **extreme tracking** (≈1 em on the title, ≈0.4 em on the cards), centred at 50 % H.
- Colour: dark slate blue-grey (#252a40 to #292a49) on pure black: the type is barely brighter than the black. It reads as engraved, not as a graphic.
- Sizes (bounding box at 480p, ≈): small lead word ("FROM", "THE") ≈2.5–3 % H; name and "THIS SUMMER" ≈4.5–5 % H; title and date ≈11 % H, spanning 13–87 % of the width.
- In: slow fade up from black (≈0.8–1 s). Out: fade to black. Holds 3.8–6.0 s, the longest card holds in the library's trailer set.

## Colour / grade
2.39:1 letterbox (61 px bars at 480p) on every shot. Desaturated sand and grey-blue sea, deep low-key interiors with one fire source, a few bright fog exteriors (fortress, coast). No coloured cards: the grade carries all the colour.

## Camera / shots
Locked wides of scale (fortress, masts, ship silhouettes), long handheld takes close to the actors, firelit faces, storm deck action. Practical, in-camera feeling; no VFX showcase shot is held.

## Transitions
Hard cuts, plus fades through black between chapters (8 black holds). The title fades up out of black. No dissolves between shots.

## Sound
- Integrated **−14.0 LUFS**, LRA 18.4 LU (very wide: the logo section sits around −30 dBFS RMS), true peak +0.9 dBTP.
- A single long crescendo: RMS ≈−30 dBFS (logos) → −18 (Q2) → −16 (Q3) → −11 (storm, 87–98 s). Hits only at the first two images (+20…+23 dB).
- The "stop" is a 3 s fall on black (−11 → −23 dBFS), not a silence; the title lands on the lower level after one face.

## What makes it premium
- Confidence: the first story shot is held 6.8 s and the second is a 6.5 s take; ASL near 3 s in a blockbuster trailer.
- Text whispers: tiny-to-medium wide-tracked caps in dark slate on black, held 4–6 s.
- Black as punctuation: eight holds of 0.8–3.9 s divide the trailer into chapters.
- One continuous score crescendo; no braams on every cut, no dialogue.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Canvas 1920×1080, bars 138 px top and bottom (2.39:1) on everything.
2. 0–8 s: two logos on black, each 3–4 s, fade in 0.8 s; music bed at about −30 dBFS.
3. Then hold the first two images 6–7 s each (a wide of scale, then a close handheld take); hit +20 dB on each cut in.
4. Body at ASL 2–2.5 s, a 1–3 s black hold every 10–15 s.
5. Cards: `font: 500 50px Montserrat; letter-spacing:.4em; color:#272c44; text-transform:uppercase` on `#000`; title 118 px with `letter-spacing:1em`; `opacity 0→1` 0.9 s `power1.out`, hold 3–5 s, out 0.6 s.
6. Last act: score at its loudest (−11 dBFS RMS) over a storm or action montage at ASL ≈2 s; then 3 s of black while the music falls 12 dB; one face 2 s; title fade-up 6 s; date 2 s.
7. Master −14 LUFS, true peak −1 dBTP (the original runs hot at +0.9 dBTP).
