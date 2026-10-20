# HOKUM | Official Trailer  (NEON, 11 Mar 2026, 119.9 s, 16:9 file / 2.39:1 picture, YouTube)
URL: https://www.youtube.com/watch?v=jP2nDyQWBOU
Purpose: main trailer for an original horror film (7 weeks before release); sells the director's earlier films
One-sentence point: a writer checks into a remote hotel where something lives in the bridal suite.

## Structure (beats with timestamps; % of 119.9 s)
- 0.0–4.6 **pre-hook**: five flashes of the scariest images (a lantern in a corridor, fire, two carved figures, a shape), 0.5–1.1 s each, for viewers who would skip.
- 4.6–6.5 **card "TRAILER STARTS NOW"** in small serif caps on black, then 0.6 s of digital silence.
- 6.5–24.2 **slow cold open**: a dark corridor held 5.2 s, a bellboy behind a lift grille in red light, a match lit in the dark; a **3.65 s drop-out** (20.3–23.95, floor −48 dBFS), then a +29 dB hit at 24.4.
- 24.2–26.8 **NEON logo rebuilt as a red neon sign inside the hotel set** (1.8 s, at 21 %).
- 26.8–58.7 **Act 1, arrival**: aerial of a lonely road, the hotel in rain, a bell on a desk, the lobby, staff and guests, an old box in the grass, forest; dialogue-led (ASL ≈1.5 s; a hit +31.7 dB at 37.85).
- 58.7–63.3 **card "FROM THE DIRECTOR OF / ODDITY AND CAVEAT"** (≈2.5 s on black, then the text dissolves over a dark forest; at 49 %).
- 63.3–65.9 lantern in the woods, a woman and the bellboy. 65.9–67.9 **card "AND THE PRODUCER OF / WEAPONS AND BARBARIAN"** (2.0 s, at 55 %).
- 67.9–82.4 **Act 2**: a sign painted on a red wall inside the set, the house at night, a doll's head, a TV with static.
- 82.4–85.4 **second drop-out, 3.0 s** (floor −44 dBFS), then the biggest hit at 85.5 (+35.3 dB, loudest 0.5 s, −10.5 dBFS).
- 86.0–88.0 **card "THIS / SPRING"** dissolving into a forest (2.0 s, at 72 %).
- 88.0–109.6 **escalation**: a hidden speaker, black dips, the carved figures again, then a montage at ≈0.5 s per shot with five short black holds (0.5–0.9 s) and the lead's name card at 103 s; densest 100–110 s, 19 cuts per 10 s (83–92 %).
- 109.6–114.0 a dark shot and a **2.0 s drop-out** (111.95–113.95, floor −55 dBFS), then a last scare (+42.8 dB at 114.1).
- 114.6–116.4 **title "HOKUM"** on black (at 96 %). 116.4–117.4 billing block. 117.4–119.9 date written as a room number "CHECK IN / 5.1".

## Cut rhythm
- 90 shots (adaptive detector). **ASL 1.33 s**, median 1.12 s.
- ASL per quarter 1.58 · 1.50 · 1.50 · 0.88 s: even until the last quarter, then fast.
- 41 % under 1 s, 3 % over 3 s; 45.0 shots per minute. Shortest 0.33 s.
- Cuts per 10 s: 7 5 6 7 6 6 5 7 8 9 19 4.
- 16 black holds of 0.5–4.6 s (several carry cards). Cuts on audio onsets 26 % vs 21 % chance.

## Typography
- One classic serif in caps (closest free: Cormorant SC 500 or Cinzel 400), light grey to white, centred on black, small: lead line ≈2 % H, film names ≈6 % H on two lines with a small "AND".
- Cards fade in (≈0.5 s) and dissolve into the next shot; holds 2.0–2.5 s.
- Text inside the world: the distributor logo as a neon sign in the set; a painted sign on a red wall; the date as a hotel room number.
- Title: a custom serif wordmark with one stylised letter, ≈9 % H, white on black.

## Colour / grade
2.39:1 (61 px bars at 480p). Deep red and tungsten hotel interiors, cold grey-green Irish exteriors, blue-black nights; many frames nearly black with one lamp.

## Camera / shots
Locked symmetrical corridors, slow push-ins, an aerial of a road, inserts of objects (bell, box, doll, speaker), creature glimpses under 0.6 s.

## Transitions
Hard cuts plus many dips to black; cards dissolve into footage; no flashes except the pre-hook.

## Sound
- Integrated **−16.2 LUFS**, LRA 9.7 LU, true peak −0.8 dBTP.
- **Three long drop-outs** (3.65 s, 3.0 s, 2.0 s; floors −44 to −55 dBFS), each followed by the three biggest hits (+29, +35, +43 dB). The pre-hook ends in 0.6 s of digital silence.
- Bed mostly −15…−25 dBFS with dialogue; no wall of music.

## What makes it premium
- The pre-hook and "trailer starts now" card are used once, then the trailer is patient (a 5.2 s corridor).
- Every piece of branding lives in the set: neon logo, painted sign, room-number date.
- Credits sell the director's earlier films twice (director, then producer), in a quiet serif.
- Silence before each scare, three times, longer each time it matters.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Bars 138 px (2.39:1).
2. 0–4.6 s: 5 flashes of 0.5–1 s; card "TRAILER STARTS NOW" 1.5 s; 0.6 s full mute.
3. 6.5–24 s: 4–6 shots of 1.5–5 s, then mute the bed for 3 s and hit +30 dB.
4. Logo as an object in the set (neon sign, plaque) 1.8 s at ≈20 %.
5. Credit cards: `font:500 54px "Cormorant SC"; color:#e8e8e8; letter-spacing:.06em` with a 16 px lead line; fade 0.5 s, hold 2 s, dissolve into the next shot over 1 s.
6. Second silence (3 s) and the biggest hit at ≈70 %, month card, then a 10 s montage at 0.5 s per shot with short black holds, a 2 s silence, a last scare, title on black, date as an in-world object.
7. Master −16 LUFS, true peak −1 dBTP.
