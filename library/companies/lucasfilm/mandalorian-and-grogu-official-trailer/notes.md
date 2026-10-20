# The Mandalorian and Grogu | Official Trailer  (Lucasfilm / Star Wars channel, 17 Feb 2026, 131.7 s, 16:9 file / 2.39:1 picture, cards full frame, YouTube)
URL: https://www.youtube.com/watch?v=IHWlvwu8t1w
Purpose: main trailer (about 3 months before release)
One-sentence point: a father-and-son bounty-hunter team takes one more job across the galaxy, and the kid is growing up.

## Structure (beats with timestamps; % of 131.7 s)
- 0.0–4.0 **graphic opening image**: a huge red-orange sun on the horizon with starfighter silhouettes crossing (4.0 s), loud on frame 1 (−11 dBFS) then falling to −30.
- 4.0–15.4 **fast cold open (12 %)**: ship interior, cockpit, Grogu at the controls, a ship over a beach, ASL ≈0.9 s, hits at 8.1 (+16.7 dB) and 13.5 (+32.4 dB).
- 15.4–17.2 **Lucasfilm logo on black** (1.8 s, at 12 %), quiet (−19…−23 dBFS).
- 17.2–44.8 **Act 1, the job**: a dark city, an information broker scene with comic dialogue, a throne room, an Imperial meeting, a beach, Grogu low-angle hero shot, an explosion in a corridor (ASL ≈1.4 s). Hits on each new location (+16…+18 dB).
- 44.8–70.7 **Act 2, the stakes**: a commander at a desk, Grogu in the snow, a jungle fight, hyperspace, a rainy planet, a duel silhouette; ASL ≈1.2 s.
- 70.7–72.6 **card "ON MAY 22"** on a starfield (1.9 s, at 54 %).
- 72.6–104.4 **Act 3, action**: speeder fight, a desert ride, jungle creature, arena fight, a sea monster, a desert battle and a fire blast (loudest 0.5 s at 98.7, −9.3 dBFS). Densest 90–100 s, 11 cuts per 10 s (68–76 %).
- 104.4–106.6 **quiet comic beat** (−21…−27 dBFS), then a chase through neon corridors, shots lengthen to 2.0–3.7 s, music at −10 dBFS.
- 119.2–122.8 **title**: green 3D logo (3.6 s, at 91 %).
- 122.8–128.2 **button**: Grogu and the Mandalorian in a quiet exchange (1.5 + 1.9 + 1.9 s, music down to −29 dBFS).
- 128.2–131.7 "FORGED FOR IMAX" then "MAY 22" + billing (3.4 s); last hits at 128.4 and 129.55 (+16…+17 dB).

## Cut rhythm
- 97 shots (adaptive detector; scene detector found only 39 cuts, it misses the dark cuts). **ASL 1.36 s**, median 1.08 s.
- ASL per quarter **1.37 · 1.18 · 1.10 · 1.83 s**. 43 % under 1 s, 5 % over 3 s. 44.2 shots per minute.
- Cuts per 10 s: 7 8 7 6 8 9 8 8 8 11 8 4 4 0 (flat until 100 s, then it slows for the chase, title and button).
- Shortest 0.21 s (92.7, inside the action run); longest 4.0 s (opening sun), 3.7 s (chase), 3.6 s (title).
- 4 black holds of 1.6–3.4 s (logo, card, a chapter break at 77.1, end block).
- Cuts on audio onsets 25 % vs 21 % chance. Speech in ≈116 s of 132 s: dialogue and jokes carry the edit.

## Typography
- Only three text moments: month card, title, end block. No taglines, no director card.
- Month card and end card: semi-bold geometric caps (closest free: Montserrat 600) in pale green-white with a slight bevel, ≈8 % H, centred at ≈48 % H, on a dark starfield (not flat black).
- Title: a **3D extruded, italic, slanted pulp logo** in pale green (#9fd08a-ish) with a dark side face, tilted ≈10°, spanning ≈15–85 % W, main word ≈16 % H (closest free: Russo One or Bungee with a −12° skew and a CSS extrusion). It reads like a vintage serial poster.
- In: hard cut; the title logo slides in slightly in depth. Out: hard cut.

## Colour / grade
2.39:1 picture (61 px bars at 480p). Warm amber interiors, green jungle, blue rain and snow, pastel desert sunsets; many practical lights. Cards use the starfield as their plate.

## Camera / shots
Low-angle hero shots of the small character, cockpit POVs, wide sci-fi vistas, creature reveals, handheld action. A lot of comic two-shots for dialogue.

## Transitions
Hard cuts; black dips into the logo, the card and one chapter break; no dissolves except fades on the logo.

## Sound
- Integrated **−14.1 LUFS**, LRA 8.6 LU, true peak −0.5 dBTP.
- Starts loud on the first image, then quiet for the logo; from there hits of +15…+18 dB on new scenes, with dialogue lines riding between hits.
- No pre-title silence. The quiet moments are comic beats (104.4–106.6) and the button after the title (−25…−30 dBFS), then the end block hits twice.

## What makes it premium
- One graphic, poster-like first image (a sun with silhouettes) instead of a logo.
- Humour in the edit: comic dialogue beats break every action run.
- Text is almost absent; the date card sits on a starfield, not on flat black.
- A post-title button that returns to the two characters, so the trailer ends on the relationship, not on an explosion.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. 0–4 s: one strong silhouette image (sunset, horizon, a shape crossing), full level at frame 1.
2. 4–15 s: 12 shots at ≈0.9 s with two hits; studio logo on black for 1.8 s at ≈12 %.
3. Body at ASL 1.1–1.4 s; put a 2–3 s comic dialogue beat after each action run.
4. Date card at ≈54 %: `font: 600 76px Montserrat; color:#dfeee0; letter-spacing:.04em` on a starfield (`radial-gradient` dots or a stock star plate), hold 1.9 s.
5. Last 25 %: action densest at 70–76 %, then a quiet beat, a chase with longer shots, title at 91 % (3.5 s: `transform: skewX(-12deg) rotate(-8deg)`, extrusion with 8 stacked `text-shadow` steps of #2c4a2a), a 5 s button, then the date.
6. Master −14 LUFS, true peak −1 dBTP.
