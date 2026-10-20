# Introducing Meta Ray-Ban Display AI Glasses  (Ray-Ban | Meta, 19 Sep 2025, 0:57, 16:9, YouTube @raybanmeta)
URL: https://www.youtube.com/watch?v=hrj4NQuE93M
Purpose: launch teaser / announcement spot
One-sentence point: glasses with a display inside the lens and a wristband you control with tiny finger moves - shown as five short sentences, through-the-lens POV shots and one man walking through a city.

## Structure (cut times from metrics.json)
- 0-6.2 s (11 %) hook: black; "You'll want to put down your phone for this" centred (0-2.8 s), black hold.
- 6.2-14.2 s (14 %) product: slow macro glide over the glasses (5-8 s), then "In-lens display is here" over a magenta light burst that turns into a floating music card seen through the lens (one 6 s shot).
- 14.2-21.7 s (13 %) first uses: the wearer looks up in a concrete atrium, pinches his fingers; through-the-lens POV (dark round lens edge as a vignette) with a map and a message floating in the world; black beat at 20.75 s (1 s).
- 21.7-39.5 s (31 %) the band + montage: "A breakthrough way / to interact" split left and right of the floating wristband; finger-gesture close-ups; POV cards (photo viewfinder, messages, AI answer about the building); a crowd crossing from above; a woman on a red bus background; shots of 0.3-0.6 s; black beat at 39.5 s (1.4 s).
- 39.5-41 s: "The world's most advanced AI glasses" on black.
- 41-51.9 s (19 %) second montage: city at day, POV cards (music, video call, live captions), coast at sunset; "Look Forward" over a wide of the man on a cliff (50-51.9 s).
- 51.9-56.8 s: wristband and glasses float and turn on a blue-to-peach gradient (product end, no logo card).

## Cut rhythm
- 45 shots in 56.8 s, ASL 1.26 s, median 0.83 s, 58 % < 1 s, 7 % > 3 s, 48 shots/min.
- ASL per quarter 4.73 / 0.89 / 0.83 / 1.18 s: slow product open, then a fast montage to the end.
- Cuts per 10 s: 2 / 7 / 9 / 12 / 13 / 1. Longest: opening statement + black 6.2 s, the in-lens reveal 6.1 s, the product end 4.9 s. Shortest 0.29 s.
- Two black beats (1.0 s at 20.75 s, 1.4 s at 39.5 s) split the film into three acts.
- Cuts on music onsets 16 % vs 23 % chance: cut to picture rhythm, not the beat.

## Typography
- Meta's sans (Optimistic, proprietary). Closest free: **Figtree Medium** or **Inter Medium**.
- Statements: sentence case, no full stop, white, cap ≈4.2 % H, one line of 4-8 words, centred on black or over the product; "Look Forward" in title case as the sign-off.
- Split line: two halves placed left and right of the floating product at ≈75 % H ("A breakthrough way" | product | "to interact").
- Animation: soft fade + blur in (≈0.5 s), hold 1.5-2.5 s, fade out.
- In-lens UI cards: rounded, frosted, small (≈20-25 % W), with tiny UI text; the lens edge is a dark circular vignette.

## Colour / grade
- Cool-neutral city (concrete, glass, grey sky) with one hot accent per shot (magenta burst, red bus, tie-dye shirt), then warm sunset coast. Mean luma 0.30.
- Product end on a soft sky gradient (deep blue top → peach/grey bottom).
- Clean, no grain, no letterbox.

## Camera / shots
- ≈30 % through-the-lens POV (looking through the actual glasses, round lens edge visible, UI floating in the world), ≈40 % the wearer in the city (low angles, close faces, hands doing pinch gestures), ≈20 % product macros and floating renders, ≈10 % type on black.
- Slow glides on the product; handheld follow and low-angle portraits on people; one top-down crowd.

## Transitions
- Hard cuts; two 1-1.4 s black beats; the magenta light burst as a flash transition into the first lens POV.

## Sound
- Music only, no voice (speech detection: 0 words). Electronic track that builds from the hook.
- Integrated −14.0 LUFS, LRA 4.1 LU, true peak −1.6 dBTP. No silences or drop-outs (the black beats keep the music).
- Hits +20-22 dB at 15.9-23 s (first POV uses and the band), +15.6 dB at 41.1 s after the second black beat.

## What makes it premium
- The hook names a human desire (put the phone down) before showing any product.
- Shooting THROUGH the lens shows exactly what the wearer sees - the proof is the point of view.
- Very little, very calm type against a fast montage.
- Ends on the object floating in sky colour, no logo card.

## Recipe (real footage + HTML/GSAP)
- Footage: "man walking city concrete architecture low angle", "crowd crossing top view", "woman portrait red bus", "man on cliff sunset coast"; product renders on a gradient.
- Lens POV: footage inside a circle mask with a dark rim `radial-gradient(circle at 50% 50%, transparent 52%, rgba(0,0,0,.85) 70%)`, slight barrel blur on the edges (`filter: blur(1px)` on an outer ring), a frosted card `width:22%; border-radius:18px; background:rgba(255,255,255,.18); backdrop-filter:blur(14px)` floating right of centre.
- Statements: `font:500 6vh/1.2 Figtree` (cap ≈4.2 % H), centred, `opacity 0→1, filter blur(8px)→0` 0.5 s, hold 2 s.
- Pace: 0-25 % slow (one statement, product), then 0.3-1 s shots; two 1-1.4 s black beats with one statement each.
- Mix: music only at ≈ −14 LUFS, keep the bed under the black beats.
