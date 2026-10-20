# Headphone (1): Control your sound  (Nothing, 2025-07-01, 0:54, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=7k1DxGDnT_I
Purpose: launch film (fashion-style brand film for a product)
One-sentence point: In a cold test lab, people stand in front of giant photo backdrops (forest, moon, city) wearing Headphone (1): the headphones decide what world you hear, so you control your sound.

Structure:
- 0.0-0.6 "NOTHING(R)" dot-matrix card on black.
- 0.6-2.6 hook: a real-looking pine forest.
- 2.6 turn: hard cut wide shows the forest is a printed backdrop in a concrete lab: lab-coat assistants with clipboards and trolleys, a model walking on a treadmill (frames/t003.5s.jpg).
- 5-12 woman puts the headphones on: low-angle close-ups, then she stands in front of the forest print.
- 13-27 second model, moon-surface backdrop: acoustic foam panels, treadmill, man lying on the floor with arms out (22 s, upside-down CU), wide of the room with a screen showing the product.
- 28-37 woman again: side CU, macro of the finger on the ear-cup control (30-31 s), aerial-city backdrop, close-ups.
- 38-45 release: she dances freely in the lab (wides and mediums), wide of the whole set at 44 s.
- 45.7-47.9 black card "headphone(1)" (dot-matrix).
- 47.9-49.4 one last hero shot (she turns, ear cup to camera).
- 49.4-54 black cards: "control your sound", "NOTHING(R)", "nothing.tech" (~1.2-1.5 s each).

Cut rhythm: 26 shots, ASL 2.08 s, median 1.96 s, quarters 2.25 / 1.69 / 1.69 / 1.93. Very regular: only 4 % of shots under 1 s, 8 % over 3 s; longest 4.56 s (end cards) and 4.32 s (5.3 s, putting the headphones on). Shortest 1.12-1.28 s in the dance (40-44 s). Cuts on onset 28 % vs 33 % chance = cut on a steady ~2 s pulse, not on beats.

Typography: only dot-matrix (Ndot style; free match Doto), lowercase, white on pure black, centred, tiny: text block ~3.5-4 % of frame height, 16-25 % of frame width. 1-3 words per card, 1.2-2.2 s hold, hard cut in and out. Product name written as "headphone(1)" (no space, brackets). Never over picture.

Colour/grade: cold and muted. Concrete grey, white lab coats, pale blue chairs, green-grey forest. Median luma 109 (mid-bright, no crushed blacks in picture), median R-B -19.9 (clearly cool), median saturation 20 % with p90 only 23.5 % (no shot breaks out of the muted palette), contrast p95-p5 151. Soft daylight-like top light, matte skin. Looks like a fashion editorial (the channel lists a separate cut "Shot by Jordan Hemingway", fashion photographer).

Camera/shots: tableau wides with several people in frame (symmetric, flat staging, people not interacting), low-angle close-ups looking up at faces, side profiles that show the ear cup, one macro of fingers on the control, an upside-down CU of a man lying down. Mostly locked or slow drift; handheld only in the dance. Mixed lenses: wide 24-28 mm look for the lab, long lens for CUs.

Transitions: 25 hard cuts, no effects. The "backdrop reveal" at 2.6 s is a cut from a tight crop of the print to the wide of the lab: the reveal is done by framing, not by VFX.

Sound: no voice-over (whisper only returned one low-confidence Japanese phrase at 1-3 s, probably a sung sample; treat as music). Music is dynamic: loudest early (6.5 s, -8 LUFS-M), quiet passages at 14-17 s (-19 to -21) and 28-32 s (-23 to -25, exactly around the finger-on-control macro), then a big return at 35.45 s (+38.5 dB rise). My reading (a guess, I cannot hear it): the music level/filter follows the product's controls, like noise cancelling on/off. Integrated -13.6 LUFS. Music runs under the end cards and stops at 52.5 s.

What makes it premium:
- A strong art-direction idea (fake worlds in a lab) that explains the product without one spec.
- Editorial casting and styling; people look like a fashion shoot, not an ad.
- A metronome cut (~2 s, very low variance) that feels calm and expensive.
- Muted cool palette held for 50 s; the product's silver/white fits in, never pops artificially.
- Tiny lowercase dot-matrix cards on black as the only text.

Recipe (real footage + HTML/GSAP):
1. Shoot a "set inside a set": a big print or projection behind talent, plus wides that show the studio around it. Cast 2-3 models, grey/olive/white wardrobe. Grade cool: R-B about -20, saturation ~20 %, lift blacks slightly (median luma ~105).
2. Edit at a fixed pulse: 1.8-2.2 s per shot, open with a 2 s crop of the backdrop, cut to the wide reveal. End with a release scene (dance/movement) at 70-80 % of the runtime.
3. Cards in HTML: `body{background:#000}`, one centred `div`, font Doto 500 lowercase, `font-size: 3.6vh`, `letter-spacing:0.04em`, color #f2f2f2. Hard cut in/out (no fade). Sequence: product name 2.2 s -> hero shot 1.5 s -> claim 1.4 s -> brand 1.2 s -> URL 1.2 s.
4. Optional dot-matrix look in CSS: render text into a canvas, sample every 4 px and draw 2.4 px circles, so letters are made of dots.
5. Sound: drop the music by 10-15 dB (or a low-pass at 400 Hz) for 2-4 s when the hand touches the control, then bring it back with a hit.
