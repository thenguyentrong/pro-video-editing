# Ghost Elephants | Official Trailer | National Geographic Documentary Films  (National Geographic, 2026-02-10, 2:27 file = 132.6 s trailer + 14 s channel end screen, 16:9, YouTube / National Geographic channel)
URL: https://www.youtube.com/watch?v=YoOD-2Wn7ik
Purpose: trailer for an auteur nature / expedition feature documentary (festival film, theatrical + streaming)
One-sentence point: a conservation explorer and master trackers search an Angolan wilderness for elephants that may not exist, filmed by a famous auteur as a story of obsession.

Structure (0–132.6 s):
- 0.2–8.2 OPEN: one 8 s underwater/surface shot of a river (light rippling), ambient sound ≈-21 dBFS. Bugs: film title top-left in thin serif caps, streamer logos top-right.
- 8.2–15.6 LOGOS ON BLACK: 1.8 s black, the brand's yellow frame + "DOCUMENTARY FILMS" (≈10–11.5), the distributor logo, festival laurels (≈14–15.5; +34 dB rise at 14.1).
- 15.6–37 THE EXPLORER: a handheld close-up of the explorer touching his temple (16–17), 1.4 s black, archive photos of a giant elephant skeleton as a small square print on black (19–23, 4.6 s), a museum mammoth, the explorer in a museum looking up, an upside-down sunset (28–29), director credit cards on a night-sky with the Milky Way ("FROM ACCLAIMED FILMMAKER / [name]", "DIRECTOR OF / [earlier film]", 32–36).
- 37–68 THE EXPEDITION: a boy on a sandy path, river aerials, a camp from above, bare feet in sand, an underwater elephant shape, trackers' faces in close-up, archive print of a footprint (57–58), a bow hunter, more archive window prints on black (51–52); 0.56 s and 1.04 s blacks (49.8, 68.4).
- 68–96 SEARCH: night fire, trackers wading a lake, bleached skulls on a shore (73–76), a rainbow, storm clouds, an elephant underwater, dung in sand, a night car with headlights, a drawing held in hands.
- 96–113 PRESS QUOTES: four critic-quote cards (spaced serif caps, 2–3 lines + outlet logo) over dark skies, intercut with 1–2 s action.
- 113–128.9 CLIMAX (densest, 15 cuts in 110–120 s, 0.36 s shots at 119.4–120): spider macro, a helicopter lifting cargo, a dirt bike, a fire, laughing kids, a dance, the explorer with arms wide (123.2, 5.7 s).
- 124–128.9 TITLE "GHOST / ELEPHANTS" in spaced serif caps on a desaturated churning-water plate, with the brand lockup above and the release line below.
- 128.9–132.0 3.1 s black hold and 2.2 s digital silence; 132–132.6 the brand frame + streamer logos.

Cut rhythm: 97 shots in 132.6 s, ASL 1.37 s, median 1.04 s (adaptive detector). ASL per quarter 2.21 / 1.38 / 1.33 / 0.92 s: it speeds up all the way to the title. 42 % of shots under 1 s, 8 % over 3 s; longest the 8.0 s open, 5.7 s title, 4.6 s archive print. Cuts per 10 s: 3, 5, 5, 6, 8, 7, 7, 6, 7, 8, 8, 15, 10. Cut-on-onset 30 % (the chance value in metrics.json is broken for this clipped run; the full-file run gave 29 % vs 23 %).

Typography:
- Everything in one classical serif caps family with very wide tracking (closest free: Cormorant Garamond 500 / Cinzel 400): bug "GHOST / ELEPHANTS" ≈1.8 % H top-left; credit eyebrow ≈2 % H over name ≈4 % H (tracking ≈0.3 em) at y ≈55–60 %; press quotes ≈3.5 % H, 2–3 lines, centred, outlet logo under; title ≈8 % H, 2 lines, tracking ≈0.25 em; release line ≈2.5 % H.
- Logo card: yellow frame + "DOCUMENTARY FILMS" in geometric sans caps ≈4 % H, on black with a soft warm vignette.
- Archive: small square prints (≈30 % H) with rounded corners, centred on black.

Colour/grade: earthy, slightly desaturated, warm skin and sand, deep night blues, a red dusk under the press cards; the title plate is almost monochrome. 16:9.

Camera/shots: observational handheld with the explorer and trackers, intimate face close-ups, aerials of rivers and camps, underwater, night fire and headlights, macro (spider), archive prints, a museum.

Transitions: hard cuts; frequent short blacks (1.8, 1.4, 0.56, 1.04 s) as breath; title held, then a 3.1 s black with silence.

Sound: (I could not listen; from level data.) Integrated -16.6 LUFS, LRA 10.8 LU, true peak -1.1 dBTP. Quiet first minute (-21…-26 dBFS, a dip to -32 around the black at 17 s), builds to -11…-14 in the climax (108–128 s), then true digital silence for 2.2 s after the title. Biggest rises +34 dB on the festival laurels (14.1) and +20 dB at 65.5.

What makes it premium:
- An auteur's look: one serif type family for bug, credits, quotes and title.
- Archive photos presented as small prints on black, like museum objects.
- Steady acceleration (2.2 → 0.9 s per quarter) and then total silence after the title.
- Proof of the quest in objects (skulls, a drawing, a footprint), not graphics.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- Open 8 s on one natural texture (water), then 2 s black, logo card 2 s, laurels 2 s.
- Credit cards on night sky: `.eyebrow{font:500 2vh "Cormorant Garamond";letter-spacing:.3em;text-transform:uppercase}` `.name{font:500 4vh "Cormorant Garamond";letter-spacing:.3em}` fade 0.5 s, hold 1.5 s.
- Archive prints: `width:22vh;height:22vh;border-radius:1vh;object-fit:cover` centred on `#000`, hold 3–4.5 s.
- Press-quote block (optional, only with real quotes): 3 lines `500 3.5vh`, outlet logo 3 % H, over dusk skies, 1.5–2 s each.
- Accelerate: quarter ASL 2.2 → 1.4 → 1.3 → 0.9 s; last 10 s at 0.36–0.8 s; title 5 s on a monochrome plate; then 3 s black in silence; logo 0.6 s. Master -16 LUFS.
- Stock queries: `river surface underwater light`, `milky way tree silhouette`, `elephant skull bones shore`, `trackers walking savanna`, `night campfire africa`.
