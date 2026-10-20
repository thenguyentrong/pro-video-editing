# Feel it all on the new Sky Sports  (Sky Sports, uploaded 2017-07-18, 60.0 s, 16:9, YouTube / Sky Sports channel)
URL: https://www.youtube.com/watch?v=o23AO9BaRWo
Purpose: channel relaunch / rebrand spot (:60) introducing the new channel line-up; used on air and online
One-sentence point: one small moment at home grows, like the butterfly effect, into the feeling in every stadium, and the new channels let you feel all of it.

Structure (times from metrics.json):
- 0.0–2.9 HOOK: macro of one blue butterfly on a coffee mug in a kitchen; 0.9 s of silence, then music.
- 2.9–9.2 GROW: kitchen wide, butterfly flies out of the house (a long glide with a white-out at ≈7 s: soft transition), aerial over a city to an empty stadium.
- 9.2–49.9 TOUR: the swarm grows and passes through empty venues of each sport: stadium seats, a meadow, a golf course, a race circuit hotel and start lights, a rugby ground under floodlights, a national stadium arch at night, confetti in a bowl, a boxing ring, a football stadium; butterflies turn the colours of the venue (red, blue). 2–3 s per shot, very even.
- 49.9–52.6 TAGLINE: small centred line over a hazy aerial of a stadium in a cloud of butterflies.
- 52.6–60.0 LOCKUP 7.4 s (one aerial shot): the channel logo cycles through the channel names (≈1 s each), then the plain logo, then the endline either side of the logo.

Cut rhythm: 23 shots in 60.0 s, ASL 2.61 s, median 2.36 s, only 4 % under 1 s. ASL per quarter 2.50 / 1.88 / 2.14 / 3.00. Cuts per 10 s ≈3–4 all through: a calm metronome, the only long shot is the lockup (7.4 s). Adaptive and scene detectors agreed (no cross-check warnings). Cuts on onsets 9 % vs 4 % chance: mildly on the music.

Typography:
- Tagline: thin wide caps, white, cap ≈2 % of frame height, centred at ≈45 % height, tracking ≈0.1 em, fade in/out. Closest free: Montserrat 300 caps.
- Lockup: the channel logo (blue "sky" box + red "sports" box, ≈8.5 % H tall) centred at ≈48 %; channel names swap inside the logo every ≈1 s; endline split around the logo in light caps, cap ≈3.5 % H, white. Closest free for the endline: Montserrat 400 caps.
- No other type, no sport names, no rights list.

Colour/grade: soft, airy, slightly hazy daylight; venues at golden hour or under floodlights at night; butterflies take blue and red (the brand's two colours). Picture never fully saturated.

Camera/shots: macro at the start, then mostly slow aerials, cranes and dolly moves through EMPTY venues; no athletes, no fans, no action. Every shot contains the CG butterfly swarm as the moving element.

Transitions: hard cuts on a steady grid; a few white-outs (sun flare) and passes through the swarm as soft transitions (6.7, 7.5 s); the swarm itself carries continuity across cuts.

Sound: music only (build from a quiet start). Measured: 0.9 s silence at the start, then momentary −21 to −27 LUFS for the whole spot, integrated −23.1 LUFS (the European broadcast target is −23 LUFS), LRA 4.1 LU, true peak −14.2 dBTP; loudest 0.5 s at 23.6 s; no drop-outs; 0.35 s silence at the end. I did not listen; voice-over not verified.

What makes it premium:
- One visual metaphor (the swarm) carries the whole spot and links every sport without showing a single match.
- Empty venues: the brand sells anticipation and feeling, not footage it has the rights to.
- Brand colours appear only inside the metaphor (blue and red butterflies) until the logo.
- A calm 2–3 s rhythm and a long 7 s lockup: a channel launch, not a highlights reel.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes; butterflies as a licensed CG/alpha element or a particle system):
- 20 shots of 2–3 s: macro hook → home → aerial → 12–15 empty venues (drone or crane, golden hour / floodlights) → hazy aerial for the lockup.
- Swarm layer over every shot: 40→400 butterfly sprites (alpha video or SVG with wing-flap `scaleX 1→0.2` 0.12 s yoyo), Perlin-noise paths, density grows across the film; tint 60 % blue `#1f4fd1` / 40 % red `#e10a1e`.
- Tagline: Montserrat 300 caps 22 px (≈2 % H), tracking 0.1 em, fade 0.6 s in/out.
- Lockup (7 s): logo box 90 px tall centred; channel-name slot swaps every 1.0 s (hard swap), then endline words fade in left and right (0.5 s, `power2.out`).
- Mix to −23 LUFS for EU broadcast; keep momentary inside −21…−27.
- Stock queries: "drone empty stadium golden hour", "empty football stadium seats", "floodlights stadium night aerial", "boxing ring empty spotlight", "butterfly macro kitchen", "motorsport start lights".
