# Star Wars: Ahsoka Season 2 | Teaser Trailer  (Lucasfilm / Star Wars channel, 15 Aug 2026, 95.1 s, 16:9 file / 2.39:1 picture and cards, Disney+ series, YouTube)
URL: https://www.youtube.com/watch?v=Fdar7gTQnog
Purpose: season teaser for a streaming series (first look, shown at a fan event, months before the season)
One-sentence point: the war returns, the master comes back, and the second season is on its way.

## Structure (beats with timestamps; % of 95.1 s)
- 0.0–19.7 **cold open (21 %)**: a ship in orange haze, a battle in smoke, then a snowy night forest: the lead in the dark, a lightsaber duel lit only by the blades (11.1 s, 3.0 s hold), a held face in the dark (15.1 s, 3.8 s). Short black dips (0.2–0.3 s) between the first shots at 2.3, 3.9, 6.8 and 8.5 s, like a slow pulse. Dialogue from 1.2 s.
- 19.7–22.2 **Lucasfilm logo, rebuilt in red light** and dissolving into a red-lit room (2.5 s, at 21 %), hit +18.1 dB at 19.9.
- 22.2–24.7 three dark shots, then **card "IN 2027"** (1.6 s, at 26 %).
- 26.3–29.5 a red ring corridor, a blue villain close-up. **Card "THE / SECOND SEASON / ARRIVES"** (3.0 s, at 31 %).
- 32.5–54.9 **escalation**: star destroyer (hit +22.4 dB at 32.85), a hologram room, space battle (loudest 0.5 s at 39.65, −9.5 dBFS), a fast run of 0.25–0.46 s shots at 42–43 s, red planet, the lead in close-up, a starfighter attack, a stone landscape. ASL ≈0.9 s.
- 55.0–61.6 **quiet fog section**: blue fog silhouettes held 2.5 s and 3.3 s (the slowest moment after the open).
- 61.6–83.8 **montage at 0.75–0.9 s per shot** (densest 70–80 s, 12 cuts per 10 s = 74–84 %): hangar, cockpit, fleet, creatures, sabers, flame thrower, explosions.
- 83.8–86.0 dark two-shot of master and pupil (2.3 s); **drop-out 85.4–85.9 s** to −42.5 dBFS, then the biggest rise, +31.9 dB at 86.15.
- 86.0–89.3 two last space shots and a green blade.
- 89.3–91.8 **title** "STAR WARS / AHSOKA / SEASON TWO" over a glowing red planet rim (2.5 s, at 94 %).
- 91.8–95.1 **platform logo** on a teal gradient (3.3 s), fade to silence.

## Cut rhythm
- 80 shots (adaptive detector), **ASL 1.19 s**, median 0.85 s. ASL per quarter 1.49 · 0.95 · 1.13 · 1.13 s.
- **66 % of shots under 1 s**, 5 % over 3 s. 50.5 shots per minute.
- Cuts per 10 s: 7 6 8 10 10 8 9 12 8 1. Shortest 0.25 s.
- Cuts on audio onsets 29 % vs 19 % chance: partly cut to the music.
- Speech in ≈54 s of 95 s; the last 15 s have no dialogue.

## Typography
- A thin geometric caps face (the show's own; closest free: Jost 400 or Josefin Sans 400), white with a soft glow, tracking ≈0.12 em, centred, **inside the 2.39:1 letterbox**, on a dark nebula plate (deep red and blue clouds with one lens-flare star).
- Sizes (≈): main line 7.5 % H, small lead word ("THE", "IN") ≈4 % H, year "2027" ≈7 % H.
- Title: the show logo ≈11 % H with a small "STAR WARS" wordmark above and "SEASON TWO" ≈4 % H below, over the red rim of a planet.
- A small platform bug (Disney+ logo, ≈3 % H) sits in the lower right corner for the whole trailer.
- Holds: 1.6 s, 3.0 s, title 2.5 s. In and out by hard cut or a short fade.

## Colour / grade
2.39:1 everywhere, cards included (61 px bars at 480p). Three worlds: orange smoke battle, blue night forest and fog, red space; most frames are very dark with one light source (a blade, a window, a flare).

## Camera / shots
Lightsaber-lit faces, held portraits, star-destroyer and fleet wides, cockpit shots, a large practical-looking set in white (corridor). Space action is fast and short (0.25–0.9 s).

## Transitions
Hard cuts; four short black dips in the first 9 s; the logo dissolves into a set; no dissolves elsewhere.

## Sound
- Integrated **−14.1 LUFS**, LRA 5.9 LU, true peak −1.0 dBTP.
- Quiet, dialogue-led open (−20…−33 dBFS), hits of +15…+27 dB at each new scene.
- One drop-out before the last act (0.5 s, floor −42.5 dBFS) and the biggest rise right after it; the title and platform logo ride the decay (−16 → −31 dBFS), then silence.

## What makes it premium
- The open is the darkest and slowest part: a duel lit only by the sabers, a 3.8 s face.
- Cards look like the show's own title design (thin glowing caps on a nebula), never like a template.
- The fog section (2.5–3.3 s shots) gives the eye a rest before the final montage.
- The drop-out and +32 dB rise land on the last act, not on the title.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Bars 138 px (2.39:1) on footage and cards; a 48 px platform bug at bottom right, opacity .8.
2. 0–19 s: dark open, 3–4 tiny 0.2–0.3 s black dips between shots, two held shots of 3–4 s.
3. Studio logo at ≈21 % (2.5 s), then two cards at 26 % and 31 %: `font:400 80px Jost; letter-spacing:.12em; color:#f4ffff; text-shadow:0 0 14px rgba(200,240,255,.5)` on a plate of two radial gradients (`#5a0b10` at 80 % 30 %, `#0d2a3a` at 25 % 40 %) over `#020407` with a small white flare.
4. Body ASL 0.9 s, one 6 s quiet section with 2.5–3.3 s shots at ≈58–65 %.
5. Densest 74–84 %, then a 2 s held two-shot, a 0.5 s mute and a +30 dB hit, two shots, title at 94 % (2.5 s), platform logo 3.3 s, fade out.
6. Master −14 LUFS, true peak −1 dBTP.
