# Surface Laptop Ultra | Stepping into the future  (Microsoft Surface, 7 Oct 2026, 1:22, 16:9, YouTube @surface)
URL: https://www.youtube.com/watch?v=fm6VQgCkj20
Purpose: launch film (product reveal, "engineering" register)
One-sentence point: the most powerful Surface, shown as a lab and machine-shop story - creators at work, engineers in white gloves, metal being milled - with every claim typed on screen in a glitchy pixel terminal font.

## Structure (cut times from metrics.json, adaptive detector)
- 0-15.8 s (19 %) hook: ONE continuous shot - a fast FPV-style flight down a waterfall canyon ("THE MOST POWERFUL SURFACE EVER" types on at 1-5 s), pulls back to reveal it is a render on the laptop screen; a hand with a game controller; the screen switches to a 3-D editing app ("ENGINEERED FOR EXTREME WORKLOADS", 12-14.5 s).
- 15.8-21.2 s: the creator at his desk (front and wide), top-down hands close the lid.
- 21.2-34.8 s (17 %) the lab: a white-gloved hand lifts the laptop from its box, an engineer carries it into an anechoic chamber, sensors are set ("PRECISION TUNED"), a silhouette in the dark, "OUR BRIGHTEST DISPLAY EVER" over the screen glare.
- 34.8-63.3 s (35 %) inside the machine: screwdriver macro on the chassis, knolled parts on white (exploded flat-lay), fan + "OUR MOST ADVANCED THERMAL SYSTEM", a CG fly-through of light streaks over the board, chip in tweezers, "UP TO 128GB OF UNIFIED MEMORY", keyboard deck dropped into metal shavings, a CNC spindle "CRAFTED TO WITHIN MICRONS", "TESTED. REFINED. PERFECTED." over a coolant spray.
- 63.3-78.7 s (19 %) build-up to the reveal: 15 s of slow machining (drill + sparks under a spotlight on the lid), heat-pipe macro, the logo dissolving into particles, the laptop opens with the wallpaper; lockup "SURFACE LAPTOP ULTRA / POWERED BY NVIDIA RTX SPARK" (73-78.5 s).
- 78.7-82.2 s: black end card, Windows logo + "LEARN MORE / MICROSOFT.COM/ULTRA" typed on.

## Cut rhythm
- 35 shots in 82.2 s, ASL 2.35 s (adaptive), median 1.67 s, 17 % < 1 s, 23 % > 3 s, 25.5 shots/min; the scene detector alone finds only 21 shots (ASL 3.91 s) because of the dark footage - every adaptive cut was checked on the sheet.
- ASL per quarter 5.14 / 1.37 / 1.71 / 2.94 s: one long opening shot, a dense middle (lab + machine), a slower machining build before the reveal.
- Cuts per 10 s: 0 / 3 / 7 / 6 / 5 / 6 / 4 / 3 / 0. Longest: the 15.8 s opening flight-to-screen move, the 15 s machining build (63.3 s, with in-shot changes), shortest 0.5-0.9 s in the lab.
- Cuts on music onsets 29 % vs 11 % chance: strongly cut to the beat in the middle.

## Typography
- One typeface for every word: a pixel / bitmap monospace in caps. Closest free: **Departure Mono** or **VT323** (more retro); IBM Plex Mono if pixels are too much.
- Size: cap ≈3.8 % H, letter-spaced by the monospace grid, white, centred at ≈50 % H, one line of 4-7 words; lockup two lines cap ≈4 % H.
- Animation: "decode" type-on - characters appear left to right with random glyphs that resolve into the right letters (≈0.6-1 s per line); a white block "selection" highlight runs over part of the line (black text on white) and a block cursor blinks at the end. Out: letters scramble away (≈0.5 s).
- Held 2-4 s. Claims are short statements ("OUR BRIGHTEST DISPLAY EVER", "TESTED. REFINED. PERFECTED."), no numbers except the memory spec.
- End card: logo ≈12 % H, glowing, two lines of the same font cap ≈3.8 % H, partly inverted.

## Colour / grade
- Two worlds: (1) warm-neutral creator desk and a golden-brown waterfall render; (2) cold steel-grey lab and machine shop, low key, mean luma 0.25, hard spotlights, desaturated, high contrast metal. Product: dark navy-graphite.
- Glitch accents only in the type; no colour grading tricks.

## Camera / shots
- ≈15 % creator use (POV hands, wides), ≈35 % lab/engineering people (gloves, chamber, silhouettes), ≈40 % macro engineering (CNC, drill, shavings, chips, fans, knolled parts), ≈10 % CG (light-streak fly-through, particles).
- Slow push-ins and slides on macros; FPV drone-style speed in the opener; top-down knolling.

## Transitions
- Hard cuts on the beat; one long in-camera pull-back from the screen content to the laptop (opener); particle dissolve of the logo before the reveal; the type itself glitches between lines.

## Sound
- Music only, no voice (speech detection: 0 words). Pulsing electronic/hybrid track with mechanical sound design (drills, servo, sprays).
- Integrated −13.3 LUFS, LRA 9.0 LU, true peak +0.9 dBTP (over 0, clipping risk).
- Hits: +42.5 dB at 0.5 s (start from silence), +29.1 dB at 14.75 s (cut out of the opener into the creator), +22.4 dB at 54.1 s (keyboard deck into shavings). Loudest 58.45 s (coolant spray). No drop-outs.

## What makes it premium
- One graphic idea - the decoding terminal font - carries all claims and the end card.
- Engineering made physical: gloves, chambers, machining, knolled parts. Proof by craft, not by charts.
- A long, patient build (15 s of machining) right before the reveal.
- A single opener shot that connects "what you make" to "what you make it on".

## Recipe (real footage + HTML/GSAP)
- Footage: "FPV waterfall canyon flight" or a CG landscape for the opener (scale a screen replacement into a laptop mock), "engineer white gloves electronics lab", "anechoic chamber", "CNC milling aluminium macro", "metal shavings slow motion", "circuit board macro light streaks", "knolling electronics parts top view".
- Decode type: `font: 400 3.8vh 'Departure Mono'; text-transform: uppercase; letter-spacing: .05em`; for each char run 4-6 random glyph swaps every 40 ms before the real letter, stagger 30 ms; a `<span class=sel>` with `background:#fff; color:#000` that grows with `clip-path` over 0.4 s; block cursor `▌` blinking 0.5 s.
- Pace: opener one 12-16 s continuous move; middle ≈1.5-2 s on the beat; a 12-15 s slow build before the reveal; lockup 5 s; end card 3.5 s.
- Mix: music + mechanical SFX at ≈ −13 LUFS; keep true peak under −1 dBTP; one big hit when the opener cuts out.
