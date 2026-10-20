# Skydio F10 | Real Flights. No CGI.  (Skydio, 2026-04-17, 0:36, 16:9, YouTube @Skydio)
URL: https://www.youtube.com/watch?v=pAhog1EGEOg
Purpose: field-proof teaser (product tease that states its own honesty in the title)
One-sentence point: a fixed-wing drone is shown only in real flight footage, with one plain spec sentence per shot.

## Structure (no voice; captions carry the text)
- 0.0-7.3 hook: onboard camera on the wing over a coastline (horizon tilted); a centred caption naming the job it is for; launch from a robotic arm seen from below. 0.6 s drop-out 6.55-7.15.
- 7.3-10.4 name: product name wordmark ≈25 % H over the sea and a launch site (+40.6 dB hit at 7.3).
- 10.4-16.1 specs: one centred sentence per shot (top speed; flight time) over real sky and aerial footage.
- 16.1-23.4 docking: the real dock UI on a tablet, a public demo of autonomous docking (event stage), the arm catching the drone, the indoor test hall with markers; one word of the sentence in blue (the proof word).
- 23.4-28.0 deployment claim: real docks on a roof, a drone at dusk, a police officer in a car at night.
- 28.0-29.2 black (1.17 s).
- 29.2-36.1 payoff: the drone flies past in a grey sky with the last sentence (en route at a stated speed), then a URL card on black.

## Cut rhythm
- 20 shots in 36.1 s (scene detector + 1 cut added by eye). ASL 1.81 s, median 1.15 s. ASL per quarter 3.01 / 1.51 / 0.90 / 2.26 s.
- 45 % under 1 s, 20 % over 3 s. Cuts per 10 s: 3, 7, 9, 0. Accelerates to the claim of scale, then one long held shot (6.98 s) for the payoff.

## Typography
- Captions: grotesk 500, sentence case with a full stop, ≈3.5 % H, white, centred in the middle of the frame (y ≈50 %), soft shadow, no box. One word coloured brand blue when it is the proof word. Closest free: Inter 500.
- Animation: letters appear in a fast random-order flicker (≈0.4 s), hold the whole shot (2-4 s).
- Wordmark: wide geometric product logo ≈25 % H, centred.
- End card: URL bold ≈3.5 %, centred on black.

## Colour/grade
- Natural, slightly cool; real sunrise/sunset skies; no stylised grade.

## Camera/shots
- Onboard wing camera, ground long lens on a small drone in the sky, aerial over towns, public event footage, indoor test hall, police in-car. Everything real; the title promises it.

## Transitions
- Hard cuts; one 1.2 s black hold before the payoff.

## Sound
- No voice. Quiet mix: integrated -21.8 LUFS, LRA 7.5 LU, true peak -2.6 dBTP. Drop-outs 6.55-7.15 (then +40.6 dB hit on the wordmark) and 28.9-29.2. Silence under the URL card.

## What makes it premium (and credible)
- The title itself is a claim about the footage (real flights, no CGI) and the footage keeps it.
- Specs are full sentences with units, set like subtitles, not like ads.
- One word in colour marks the evidence ("proven" type word).

## Recipe (real footage + HTML/GSAP)
- 6-8 real flight shots of 1-4 s, one spec sentence each: `font:500 3.5vh Inter; position:absolute; top:50%; width:100%; text-align:center; text-shadow:0 1px 6px rgba(0,0,0,.4)`.
- Letter flicker: split letters, each `autoAlpha 0->1` at a random offset within 0.4 s (seeded).
- One proof word in brand colour per film, not more.
- 0.6 s silence before the product name; 1.2 s black before the final shot; end on a URL.
