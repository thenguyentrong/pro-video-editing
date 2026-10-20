# What's Next? | Patagonia  (Patagonia, 2023-03-10, 2:00, 16:9, YouTube / Patagonia channel)
URL: https://www.youtube.com/watch?v=eV_753wIUzo
Purpose: brand film for the company's 50th year (activist brand anthem built from its own documentary archive)
One-sentence point: 50 years of surfing, climbing, protest and repair footage add up to one line: the next thing the company does is protect the planet.

Structure:
- 0.0–0.9 black, sound rises from -25 dBFS.
- 0.9–5.0 OPEN: 1970s 16 mm footage of a white van with surfboards on a coast road; the "patagonia 50 ▸" logo sits centred over it for ~2 s (cap ≈4 % H, white), then a driver close-up. Archive look (soft, faded greens) sets "history".
- 5–19 SPORT ARCHIVE: skiing, ice climbing, big-wave surf, kayak in heavy sea. Shots 1.2–2.8 s.
- 19–30 PROTEST TURN: a giant pair of scissors painted on a dam at night (20 s), an older Japanese woman tying a protest headband, a scream in black and white, a crowd march, a child with a hand-made sign. The film switches from "sport" to "activism" with no title card.
- 30–67 BOTH AT ONCE: surf and climbing intercut with refinery smoke, wildfire, clear-cut stumps, banners ("UN-DAM THE KLAMATH NOW!" 49.8–51.3), kayak protest spelling a slogan on water (52.8–54.2), families, a dog, a worker's overall with a patch. ASL ≈1.4 s.
- 67–108 JOY MONTAGE (densest): laughing faces, climbing, biking kids, a shark with a free-diver, a baby on a staircase, a 0.4–0.5 s burst of 5 shots at 103.6–105.9 (fastest point, 86–88 % of the runtime).
- 108–114 THE DECISION: founder at his desk writing; a handwritten line on ruled paper ("Earth is now our only shareholder", the company's 2022 ownership change) appears in blue ink as the pen moves away (109.6–112.5); level drops ~0.9 s to -33/-35 dBFS (112.25–113.1), then the founder in a forest interview set-up (112.5–114.1).
- 114.07–120.1 END: one 6.1 s shot of clouds over a peak. Line types on at 114.5 s left of centre: "Next ▸ is" (bold sans) + "saving our home planet" (italic serif), then it erases letter by letter from the right (~116.8–117.2), the ▸ stays alone, the logo "patagonia 50 ▸" builds around it (~117.5) and the clouds fade to black (118–120). Music tail at -33…-38 dBFS.

Cut rhythm: 83 shots in 120.1 s, ASL 1.45 s, median 1.33 s (adaptive detector added 3 real cuts at 71.7 / 95.1 / 110.7, checked on before/after pairs). ASL per quarter 1.67 / 1.50 / 1.07 / 1.50 s. 23 % of shots under 1 s, only 1 % over 3 s. Cuts per 10 s: 5, 6, 6, 7, 6, 6, 8, 7, 10, 6, 10, 2. Longest: end card 6.06 s, then 3.7 s (93.8) and 3.0 s. Shortest 0.38–0.50 s (the 5-shot burst at 103.6). 30 % of cuts on an audio onset vs 29 % by chance: cut to the phrase feel, not to the beat.

Typography:
- Logo "patagonia 50 ▸": bold rounded wordmark + condensed numerals + right-pointing triangle, white, centred, cap ≈4 % H; on footage only, no plate.
- End line: "Next ▸ is" in a heavy geometric sans (closest free: Inter 800 / Manrope 800), cap ≈4.5 % H; "saving our home planet" in a light italic serif at the same size (closest free: Source Serif 4 Italic / Newsreader Italic). Left-aligned at x ≈25 %, y ≈50 %. Types on in ~0.5 s, holds ≈2 s, erases right to left in ≈0.4 s; the ▸ glyph becomes the bridge into the logo.
- In-picture text only otherwise: real protest banners, a slogan spelled by kayaks, a patch, a handwritten line. No captions, no lower thirds, no names.

Colour/grade: no unified grade on purpose: 16 mm archive (faded, warm, soft), 1990s video, modern digital (clean, natural). Natural greens, ocean blues, wildfire orange; one black-and-white shot. 16:9 full frame, no letterbox.

Camera/shots: almost all real documentary footage from the brand's own film library: athletes in action (surf, alpine, climbing, bike), wide landscapes, faces in close-up, protest crowds, hands at work. Handheld and long-lens; drones rare. No product shots at all.

Transitions: hard cuts throughout (82 cuts); the only soft moves are the fade up from black at the start, the type-on/erase at the end and the fade to black under the logo.

Sound: (I could not listen; from level data and picture.) Music-led and loud: -9.7 LUFS integrated, LRA 5.6 LU, true peak +2.0 dBTP (hot master). Body steady at -8…-15 dBFS (1 s RMS). One clear drop-out before the founder speaks: -33…-35 dBFS for ≈0.9 s (112.25–113.1), then a short loud phrase at 113.25 (+31 dB rise), then the tail at -30…-38 dBFS under the end line. Whether there is voice-over in the body is not verified.

What makes it premium:
- No product, no price, no claim: the archive is the proof that the brand has done this for 50 years.
- The turn from sport to protest happens inside the montage (19–30 s), so activism reads as the same story, not an add-on.
- Real text in the world (banners, kayak slogan, handwriting) replaces graphics.
- One quiet beat before the payoff: the handwritten line, a 0.9 s drop, the founder's face.
- End line in two voices (bold sans + italic serif) with the logo's own triangle as the link.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- Pick 80–85 clips: 25 % archive (grain, faded), 30 % sport, 25 % protest/landscape harm, 20 % faces and joy. Order: archive → sport → protest turn at ≈16 % of the runtime → mixed → joy → quiet decision → end.
- Cut 1.2–2.0 s per shot, faster (0.9–1.1 s) in the last third, one burst of 5 shots at 0.4–0.5 s around 85 % of the runtime, then slow to 1.5–1.9 s.
- Open: fade up from black over 0.9 s, logo centred `font: 800 4vh Manrope; color:#fff` for 2 s, `opacity 0→1` 0.3 s.
- Before the payoff: drop the music to ≈-34 dBFS for 0.9 s, then let one real sentence play.
- End shot 6 s (moving clouds or water). Line at `left:25%; top:50%`: `<b>Next ▸ is</b> <i>your line</i>`, sans `800 4.5vh Inter` + serif `italic 300 4.5vh Newsreader`; type on per letter (stagger 0.03 s), hold 2 s, erase from the right (stagger 0.02 s), keep the glyph, build the logo around it (0.5 s), fade the plate to black over 2 s. Master -10 to -14 LUFS, true peak ≤ -1 dBTP (the original clips at +2).
- Stock queries if you lack archive: `16mm film surfing 1970s`, `protest march banner crowd`, `kayak protest water`, `clouds mountain peak timelapse`.
