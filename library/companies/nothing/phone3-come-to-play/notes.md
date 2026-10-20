# Phone (3): Come to Play  (Nothing, 2025-07-05, 0:30, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=MHGQRnvE9GQ
Purpose: launch film / ad (30 s cut-down, feature story)
One-sentence point: The round Glyph Matrix on the back of Phone (3) plays "spin the bottle" at dinner, and the bottle decides who pays the bill.

Structure:
- 0.0-3.5 hook: top-down on a linen tablecloth, a hand lays Phone (3) face down between plates and glasses (one 3.5 s shot).
- 3.5-15.4 build: shot / reverse-shot loop. Macro of the Glyph Matrix (a pixel bottle spinning on the round display, phone back on a burlap-like cloth) -> close-up of a diner's face -> matrix -> next face. 5 diners, warm restaurant. Shots shrink from ~1.2 s to 0.56-0.68 s at 12.0-14.6 s (tension).
- 15.4-17.6 turn: matrix macro held 2.2 s while the bottle stops; 17.0-17.4 the sound cuts to near silence (-72 dBFS).
- 17.6-21.3 payoff: the chosen man laughs; 19.8 a waiter holds the card terminal next to him (he pays).
- 21.3-24.8 release: high wide of the whole table in the dark restaurant (3.5 s).
- 24.8-29.8 end: hard cut to a cold 3D render. Edge-on phone silhouette against a blue-white horizon, it turns to show black + white Phone (3) side by side (one 5 s shot). No end card, no logo, no text.

Cut rhythm: 18 shots, ASL 1.66 s, median 1.24 s. ASL per quarter 1.49 / 0.83 / 1.49 / 3.73. Longest 5.04 s (end render), 3.52 s (opening top-down), 3.48 s (wide). Shortest 0.56 s (14.0), 0.60 (12.04). 33 % of shots under 1 s, 17 % over 3 s. Densest 10-20 s (9 cuts). Cuts on a sound onset 47 % vs 45 % chance = not cut to the beat; the cut rhythm follows the story tension, not the bar.

Typography: none on screen. The only "type" is the Glyph Matrix pixel icon: a white bottle drawn with ~1 px-gap dots inside a black circle (circle ~45 % of frame height in the macro, see frames/t003.8s.jpg). The brand trusts the title on YouTube and the product itself.

Colour/grade: two worlds.
- Story: warm tungsten restaurant, practical table lamps, deep blacks. Median frame luma 56/255, 38 % of frames darker than 40, median R-B +17.6 (warm), contrast p95-p5 124. Skin tones rich; one red dress and one turquoise top as colour accents.
- Product end: cold, desaturated blue-grey gradient (black top -> pale blue-white horizon band -> white floor). The warm-to-cold switch tells the viewer "story over, product now".
No letterbox, no visible grain at 480p.

Camera/shots: top-down tabletop, product macros (phone lying on the table, real footage, not CG), tight face close-ups with shallow depth of field and side light, one high wide. Camera mostly locked or very slow push. End = 3D render turntable. Actors never look at camera.

Transitions: 17 hard cuts, nothing else. The matrix macro works as the "clock" that returns between faces (A-B-A-C-A-D pattern). Hard cut from warm live action to the cold render at 24.8.

Sound: no voice-over, no dialogue (whisper found no speech). Music builds from -24 LUFS-M at 0 s to the loudest point -3 LUFS-M at 12 s (spin climax), small hit at 1.15 s (+28 dB rise) when the phone lands. 17.0-17.4: drop to near silence (floor -72 dBFS) = the bottle stops; next onset 17.4. The payment beat sits lower (-20 to -25 LUFS-M), the product render gets a fresh hit at 25 s (-9). Integrated -12.2 LUFS. 2.2 sound onsets per second = busy rhythmic track (I cannot hear it; probably percussive/ticking to match the spin, this is a guess).

What makes it premium:
- One clear idea (a party game on the back of the phone) told without a single word.
- The product feature IS the plot device; every second cut returns to it.
- Strict shot/reverse rhythm that speeds up (1.2 s -> 0.6 s) and then a silence before the payoff.
- Warm cinematic live action, then a cold clean render: the colour flip is the end card.
- Confidence: no logo, no spec, no CTA in the film.

Recipe (real footage + HTML/GSAP):
1. Shoot: top-down hero (3-4 s), 6-8 product macros of the feature (screen/LEDs on), 5-6 face CUs with 85 mm-look shallow focus, one high wide. Warm practicals only, grade to median luma ~55, R-B about +15.
2. Edit: A-B-A-C loop (feature, face, feature, face). Start at 1.2 s per shot, go down to 0.6 s over 8-10 s. Hold the feature 2 s at the turn. Put 0.3-0.4 s of near silence (cut the music bed to -60 dB) just before the payoff cut.
3. If the feature is a screen/LED, build it in HTML: a circle `div` (border-radius 50%, background #000) with a 25x25 grid of 3 px white dots (`radial-gradient` or SVG circles), draw the icon by switching dots on. Spin with GSAP: `gsap.to(icon,{rotation:1440,duration:6,ease:"power4.out",snap:{rotation:15}})` - the 15 deg snap makes it look pixel-stepped.
4. End shot: full-frame gradient `linear-gradient(#05070a 0%, #0d141b 45%, #b9c9d6 62%, #eef3f6 100%)`, product cut-out PNG turns in with `rotationY: 90 -> 0`, `transformPerspective: 1200`, 2.5 s `power2.inOut`, then hold 2 s. No text.
5. Mix: build to the loudest moment at 40 % of the runtime, silence at ~57 %, a new hit on the product reveal; target -12 to -14 LUFS integrated.
