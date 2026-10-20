# Rolex New Watches 2026 - Where a New World Begins  (Rolex, 2026-04-13, 1:07, 16:9, YouTube @ROLEX)
URL: https://www.youtube.com/watch?v=iqhAhsdTm0Y
Purpose: product reveal / launch film (Watches and Wonders 2026 novelties)
One-sentence point: Each new 2026 watch is shown as a set of perfect parts that come together over water and light.

## Structure (cut list; no voice found - music only, as far as the analysis shows)
- 0.0-1.9 hook: macro of a dial "100 YEARS" with gold indices (one slow push).
- 1.88-6.08 rhythm intro: 7 shots of exactly 0.60 s each - one new watch per beat, each lying on a moving water surface with sun glints.
- 6.08-7.96 title: "OYSTER" in huge metallic letters behind a hazy horizon, camera flying low over water (1.9 s).
- 8-30 Oyster Perpetual chapter: crown "100" macro, exploded parts floating and settling on a white sweep (bezel ring, dial, bracelet links that click together 19-23 s), the colourful "celebration" dial, green and blue dials.
- 30-52 other models: Datejust green fumé dial, Yacht-Master bezel parts flying in and assembling (36-42 s, 6.7 s longest shot), Day-Date "MONDAY" macro (45 s), Daytona parts on white (50-51 s).
- 54.16-60.24 line-up: each watch stands upright in shallow water at the horizon, sun behind - 7 shots of 0.88 s.
- 60.24-65.16 hero: one Oyster Perpetual standing in the water, sun flare (4.9 s).
- 65.16-67.2 logo: green ROLEX + gold crown on white.

## Cut rhythm
- 38 shots in 67 s. ASL 1.77 s, median 1.46 s. ASL per quarter 1.20 / 2.40 / 2.10 / 1.40 s.
- Longest 6.72 s (36.96, bezel assembly), 4.92 s (end hero), 4.12 s, 4.08 s. Shortest 0.60 s (the intro grid).
- Metronomic: intro cuts at 1.88, 2.48, 3.08 ... 6.08 (every 0.60 s = one beat at ~100 BPM); line-up cuts every 0.88 s (~1.5 beats). The middle is free (1.4-6.7 s per shot), following the part animations.
- 37 % under 1 s, 11 % over 3 s. Onset sync 14 % vs 10 % chance - the music is smooth; the grid comes from the tempo, not from hits.

## Typography
- Only one title: "OYSTER" - wide geometric sans caps (closest free: Syncopate Bold or Michroma), silver/grey with the sky showing through, cap height ~18 % of frame height, spans ~88 % width, centred at ~42 % height. Its lower part is hidden by the horizon haze (type placed "in" the 3D scene, behind the horizon).
- Logo card: green ROLEX serif wordmark + gold crown on pure white, ~3 % height, centred at ~55 % height.
- Product names are NOT written; dials carry the text (model names, "SUPERLATIVE CHRONOMETER").

## Colour/grade
- Bright, airy, high-key: silver-blue water, white sweeps, warm sun flares. Accent colours come only from dials (green, blue, multicolour).
- Very clean CGI surfaces, soft shadows, shallow depth of field.

## Camera/shots
- 100 % CGI as far as visible (water, floating parts, impossible camera paths) - a render product film, not live action.
- Moves: slow push-ins and orbits on macro, low fast flight over water for the title, parts flying in on curved paths and landing with tiny bounces.
- Composition: one object centred, lots of empty space.

## Transitions
- Hard cuts on a tempo grid; continuity through the water/sun motif. No dissolves, no wipes.

## Sound
- Orchestral/ambient score, light percussion; integrated -14.0 LUFS; loudest 0.5 s at 55.0 s (line-up). Small hits at 2.15 s and 8.25 s (+19 dB). No drop-outs.

## What makes it premium
- Parts assembling = proof of engineering without a single spec on screen.
- One perfect object per frame, centred, high-key - no clutter.
- Tempo-grid editing in the intro and line-up, free timing in the middle.
- Type used once, as a landscape element.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Product on white sweep: real macro footage on a white table (or renders). Exploded-parts look in HTML: each part as a transparent PNG; `gsap.from(parts, {y: -120, rotation: 8, autoAlpha: 0, duration: 1.2, ease: 'power3.out', stagger: .25})` then a 2 % `scale` bounce on landing.
- Grid cuts: set `beat = 60 / BPM` (0.6 s at 100 BPM); intro shots = 1 beat each x 7, line-up shots = 1.5 beats.
- Landscape title: `font-family: Syncopate; font-weight: 700; font-size: 18vh; letter-spacing: .08em; color: rgba(210,215,225,.85); mix-blend-mode: luminosity`; mask the bottom 35 % with a horizontal gradient `mask-image: linear-gradient(to bottom, #000 60%, transparent 85%)` so it sinks into the horizon; drift `x: -2vw` over 2 s.
- End: white card, logo 3vh, 2 s.
