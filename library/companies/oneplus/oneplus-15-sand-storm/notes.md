# OnePlus 15 | Sand Storm  (OnePlus, 29 Sep 2025, 1:10, 16:9, YouTube @OnePlusTech)
URL: https://www.youtube.com/watch?v=PKw-CE3mdi0
Purpose: pre-launch material film (colour + finish story)
One-sentence point: a colour named after a desert storm - a slow, poetic CGI journey from dunes into a factory of electric arcs that turns metal into a tough sand-textured shell.

## Structure (cut times from metrics.json)
- 0-4.2 s: title card over the phone against a pale sun disc ("Tougher than Titanium" left, colour name right, small product name).
- 4.2-12.6 s (12 %) dunes: blowing sand, a sun over dunes, a giant monolith/doorway in the sand (CGI), an eclipse-like ring.
- 12.6-22 s (14 %) titanium and frames: rows of metal frames, an infinite mirrored rack, frames on an orange background, a frame in a jig.
- 22-48 s (37 %) the process: a frame lowered into a dark blue bath; sparks and glowing particles as electric arcs grow the oxide layer; orange glow, embers, lava-like edges ("Micro Arc Oxidation").
- 48-58 s (14 %) proof: macro of the woven texture, the shell in bubbles, a durability rig spinning the phone in flying sand ("Tougher than Titanium" top).
- 58-66 s (11 %) hero: the finished phone stands on sand in front of the sun disc; product and colour name.
- 66-69.8 s: "Coming Soon" and the wordmark on black.

## Cut rhythm
- 28 shots in 69.8 s, ASL 2.49 s, median 2.5 s, 4 % < 1 s, 25 % > 3 s, 24 shots/min.
- ASL per quarter 2.49 / 2.18 / 1.94 / 2.49 s - very even. Cuts per 10 s: 2 / 5 / 5 / 3 / 4 / 6 / 2.
- Longest 5.2 s (hero), shortest 0.88 s.
- Cuts on music onsets 15 % vs 11 % chance.

## Typography
- OnePlus Sans (proprietary). Closest free: **Inter** / **Manrope**.
- Subtitle-style lines of the narration: sentence case, white, cap ≈2.6 % H, centred at ≈93 % H, 4-7 words, held 2-5 s with the shot.
- Claim: "Tougher than Titanium" cap ≈4.2 % H, centred at ≈11 % H over the test shot.
- Opening title: product name small (≈1.5 % H) above "Tougher than Titanium" (≈3 % H) left, colour name right, the phone centred between them.

## Colour / grade
- Sand palette: beige, warm grey, cream sun disc; process section in deep blue-black with orange embers. Mean luma 0.25. Soft, hazy, dusty atmosphere.

## Camera / shots
- ≈85 % CGI (dunes, monolith, frames, electrolytic bath, embers, texture macros), ≈15 % product hero and a test rig.
- Slow glides and pushes throughout; no handheld.

## Transitions
- Hard cuts and slow dissolves through dust/embers; no graphic transitions.

## Sound
- A soft narrator speaks short poetic lines (≈60 words in 70 s), shown as subtitles; ambient score with sand wind and electric crackle.
- Integrated −18.5 LUFS (quiet), LRA 13.4 LU, true peak −5.2 dBTP. One clear hit (+17 dB at 20.55 s, entering the process); loudest 43.1 s (embers). 1.75 s silence on the logo.

## What makes it premium
- A finish/colour turned into a myth (desert → fire → shell).
- Slow, even pace and soft sound: the opposite of the brand's loud performance spot.
- Process CGI that feels physical: particles, heat, sparks.

## Recipe (real footage + HTML/GSAP)
- Stock/CGI: "sand dunes wind macro", "sand storm slow motion", "sparks embers dark slow motion", "molten metal glow macro", "metal parts factory rows", "bubbles underwater macro".
- Pace: ≈2.5 s per shot, very even; one 5 s hero at the end.
- Subtitles: `font:400 2.6vh Inter; bottom:6%; text-align:center`, one line per shot.
- Grade: beige/cream `sepia(.2) contrast(.95)` for the desert, deep teal-black + orange for the process.
- Mix: quiet narration-led (≈ −18 LUFS); for social, master to ≈ −14 LUFS.
