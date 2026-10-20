# Helsing Cirra: AI For Electronic Warfare  (Helsing, 2026-01-22, 1:12, 16:9, YouTube @HelsingAI)
URL: https://www.youtube.com/watch?v=OPK5URcHDHo
Purpose: field-proof demo told by an engineer (flight-test film)
One-sentence point: an engineer explains, on a real airfield during a flight test, how the AI reads unknown radar signals and why it has to be tested in the real world.

## Structure (interview audio runs almost the whole film)
- 0.0-6.0 hook: aerial over a real airfield; a monospaced location super types on (place + company of the test site).
- 6.0-12.2 problem as abstraction: fast signal graphics (star field, code, waveforms, HUD symbology, grid), 0.2-1.2 s each.
- 12.2-15.0 title card: concentric wave graphic left, product name in monospaced caps + one-line descriptor right.
- 15.0-25.2 the test: airfield at dawn, the test aircraft, the engineer speaking (medium shot, brand logo on his hoodie), hands connecting cables, the aircraft taxiing.
- 25.2-44 proof: aircraft in flight, a tripod antenna emitting (signal lines composited in the air), the sensor pod under the wing, the ground van.
- 44-66 operations: van interior, crew in the cockpit with a laptop, control tower, spectrum displays and terminals, the engineer again, antenna, low fly-by.
- 66.0-72.3 brand mark on black (6.3 s).

## Cut rhythm
- 47 shots in 72.3 s (adaptive detector + 3 cuts added, 1 removed by eye). ASL 1.54 s, median 1.28 s. ASL per quarter 1.06 / 1.51 / 1.39 / 2.26 s.
- 34 % under 1 s. Cuts per 10 s: 10, 7, 7, 5, 7, 6, 4. Densest in the abstract graphics at 6-12 s.
- 54 % of cuts land on an audio onset (chance 40 %).

## Typography
- Location super: monospaced caps ≈2.5 % H, letter-spacing ≈.1em, typed on, centred-left over the aerial. Closest free: JetBrains Mono / IBM Plex Mono.
- Title: monospaced caps ≈4.5 % + descriptor ≈1.8 % caps, left-aligned at x ≈58 %. No name super for the speaker.

## Colour/grade
- Cool, overcast, slightly desaturated real footage; graphics in teal/cyan on near-black. Brand logo white on black.

## Camera/shots
- Real airfield and aircraft; aerial drone shots; handheld in the van and cockpit; macro of connectors; interview handheld medium-close with a shallow background.

## Transitions
- Hard cuts; graphic glitch frames between abstract shots; a composited signal-beam effect over a real shot (the only VFX).

## Sound
- Interview voice (one engineer), ≈61 s of speech, ≈2.2 words/s, cut into short sentences that run over b-roll. Music bed under it.
- Integrated -15.4 LUFS, LRA 8.1 LU, true peak +0.4 dBTP. Hits: 0.5 s, 6.15 s (+20.1 dB, start of graphics), 60.6 s (+23.8 dB), 62.9 s. Silence under the logo (70.2-72.3).

## What makes it premium (and credible)
- A named place on screen in the first seconds, real aircraft, real test equipment.
- The explanation comes from an engineer at the site, not a narrator.
- Abstract graphics are kept to 6 s; the rest is the test.

## Recipe (real footage + HTML/GSAP)
- Aerial of the real site 5 s with a mono location super: `font:400 2.5vh 'JetBrains Mono'; letter-spacing:.1em`, typewriter 0.03 s/char, hold 3 s.
- 6 s of 0.3-1 s abstract signal graphics (canvas or video), then a title card: mono caps 4.5vh + 1.8vh descriptor at x 58 %.
- Interview the engineer at the site (lavalier); cut their sentences tight and lay b-roll of the test over 70 % of the talk.
- End on 6 s logo with silence in the last 2 s.
