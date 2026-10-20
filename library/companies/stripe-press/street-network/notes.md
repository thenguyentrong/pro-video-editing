# The Street Network (La Red Callejera)  (Stripe / Stripe Press, 2022-10-03, 21:29, 16:9, YouTube / Stripe channel)
URL: https://www.youtube.com/watch?v=G8L0Y7ORrHo
Measured: first 300 s only (of 1289 s). Everything below is about 0:00–5:00.
Purpose: short documentary from a company's publishing imprint (tech-culture story, no product)
One-sentence point: with almost no internet access, young people in Havana built their own city-wide network to play games together, and it became a community of its own.

Structure (first 5 min):
- 0–1.75 silence on a dark, stormy city wide; "A STRIPE PRESS SHORT FILM" in small mono caps fades in (≈2 s), centred, upper third.
- 3–9.6 the same city wide in colour; a location tag "HAVANA, CUBA 2019" in condensed caps on two diagonal colour ribbons (blue and red, the flag colours) top-right.
- 9.6–35 FIRST VOICE: a man on a rooftop (7.8 s), then a sit-down interview by his gaming PC (17.7 s, the longest early shot) with a name tag in the same ribbon design; subtitles under him. Short drop-outs to -54…-60 dB between his phrases (18.6, 24.2, 26.8, 28.8 s): the edit leaves real pauses.
- 35–48 a slow shot of a home-built antenna against the sky; TITLE "THE STREET NETWORK / LA RED CALLEJERA" fades on over it (43.5–48).
- 48–65 CONTEXT ON BLACK: two serif text cards (2 short paragraphs each), ≈8 s each, music up to -16 dBFS (the loudest part).
- 65–100 THE GAME: screen-captured game footage with dictionary-style definition cards in serif ("term, n/v: meaning"), speaker close-ups, a red-lit speaker macro (83–87, three 0.2–0.6 s cuts), hands on a keyboard.
- 100–157 PLAYERS: interviews in homes with ribbon name tags, more game capture, a teenager at his PC (122–143, 9.7 s and 11.8 s holds), street life.
- 157.7–179 EXPLAINER GRAPHIC: a white screen with a pixel dinosaur game and serif statistics in blue and red, typed on line by line (21.6 s, the longest shot); the level drops to -31…-33 dBFS.
- 179–300 HAVANA TODAY: phones, a young woman walking with friends through old streets (observational, 1.5–3.5 s shots), interviews with a university expert and residents, rooftop antennas; pace rises to 6–7 cuts per 10 s in 240–260 s.

Cut rhythm (0–300 s): 77 shots, ASL 3.90 s, median 2.59 s (adaptive detector; the scene detector found 63 and missed 13 real cuts). The 34.2 s block at 35.1 is the antenna shot + title + 17 s of text on black (fades, not cuts). ASL per quarter 12.5 / 3.57 / 3.26 / 2.50 s: very slow open, then a steady build. 17 % of shots under 1 s, 42 % over 3 s. Cuts per 10 s in the first minute: 1, 1, 0, 1, 0, 0; later 3–7. Shortest 0.17–0.6 s (speaker macro flashes). 39 % of cuts on an audio onset = chance.

Typography:
- Opening credit: small mono caps (closest free: IBM Plex Mono 400), cap ≈1.6 % H, tracking ≈0.1 em, light grey, centred at y ≈45 %.
- Location and name tags: tall condensed bold caps (closest free: Bebas Neue / Oswald 600), white, cap ≈5.5 % H for the location, ≈4.5 % H for names, role in smaller caps ≈2.8 % H; placed on two slanted colour ribbons (blue `#3a8fd8`-like and crimson `#c0304a`-like) that slide in; top-right for place, right of the speaker for names.
- Title: same condensed caps, white, cap ≈7 % H, Spanish subtitle ≈4 % H below, centred on footage.
- Context cards and definitions: a book serif (closest free: Source Serif 4 / Libre Caslon Text), regular, white on black or on blurred footage, cap ≈3.2 % H, centred or left-aligned, 2–3 lines; definitions use bold term + italic part of speech.
- Explainer: black UI sans for the game, then serif lines in navy and crimson on white.
- Subtitles: white sans ≈3 % H, bottom centre.

Colour/grade: warm, natural, humid Havana colours (pastel walls, green trees), interiors lit by window light and RGB PC lights; game captures are saturated blue/purple. 16:9, no letterbox.

Camera/shots: classic observational doc: sit-down interviews in the subject's own room (medium shots, kit in frame), rooftops and antennas, handheld street walks, macro details (speaker, keyboard, phone), screen captures of games and phone screens.

Transitions: hard cuts; text cards fade in and out on black; title fades on footage; ribbons slide in. No stylised transitions.

Sound: (I could not listen; from level data and picture.) Integrated -22.2 LUFS, LRA 9.3 LU, true peak -3.0 dBTP. Starts in silence (1.75 s) and ambience at -29…-31 dBFS (5 s RMS); music peaks at -16 dBFS under the context cards (50–60 s); interviews sit at -23…-28. 21 silences and 9 drop-outs in 5 min (many 0.3–1.0 s pauses kept between spoken phrases).

What makes it premium:
- The company is present only as "a Stripe Press short film"; the story belongs to the people.
- Typography is a small system with local meaning (flag-colour ribbons, serif dictionary cards).
- It waits: 35 s before the title, real pauses in speech, a 21 s explainer.
- One playful explainer (the offline dinosaur game) makes a statistic personal.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- Open: 2 s silence on a wide; credit `400 1.6vh "IBM Plex Mono"; letter-spacing:.1em; text-transform:uppercase; color:#ccc`, fade 1 s.
- Place tag: two skewed ribbons `transform: skewX(-25deg)`, colours of the place, slide `x: 40% → 0` 0.6 s `power3.out`; text `600 5.5vh Oswald; text-transform:uppercase`; hold 4 s.
- First interview 15–18 s with pauses left in; name tag the same ribbon system, `4.5vh` + role `2.8vh`.
- Title on a symbolic object shot at ≈40 s: `600 7vh Oswald` + subtitle `4vh`, fade 1 s.
- Context: 2 serif cards on black, `400 3.2vh "Source Serif 4"; line-height:1.35; max-width: 40%`, 8 s each, music up.
- Body: ASL 3–4 s; interviews 8–12 s holds; a 20 s explainer with lines typed in (`stagger .03 s per char`).
- Master -18 to -22 LUFS.
- Stock queries: `havana rooftop antenna`, `gamer bedroom rgb pc`, `old city street walking handheld`, `wifi router antenna sky`.
