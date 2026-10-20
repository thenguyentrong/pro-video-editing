# Ear (3): Cut through the noise  (Nothing, 2025-09-18, 0:45, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=I4_6S6z2bhY
Purpose: launch film (feature story: "Super Mic" in the case)
One-sentence point: In a dark hall full of fans, horns and old test machines, a woman takes a call by talking into the earbuds case, and the noise disappears.

Structure:
- 0.0-1.0 "NOTHING(R)" dot-matrix card on black (silent).
- 1.0-4.0 hook: symmetric wide, woman alone on a metal bench in a concrete waiting room (3 s).
- 4.0-8.0 product: hand opens the transparent case (macro on dark), then she puts an earbud in (profile).
- 8.0-23.3 build ("the noise world"): wide of a dark warehouse with a wall of fans, loudspeaker horns on poles and stacks of vintage test equipment (frames/t008.5s.jpg); she walks through it; inserts of fan blades, VU meters, dials; very short inserts at 19.9-20.8 (0.40-0.48 s); she sits on the floor, hair blown by the fans.
- 23.3-31.2 turn: she lifts the case to her mouth (23.3), CU talking into it and smiling (25.4-31.2, longest shot 5.8 s, rack focus between case and face). The sound of the room drops out twice (24.75 s for 1.05 s, 26.5 s for 0.9 s).
- 31.2-41.1 payoff: back to wides, she keeps talking into the case, hair blown, final CU looking up into the wind.
- 41.1-45.1 cards (~1 s each): "ear(3)" dot-matrix, "Cut through the noise" serif, "NOTHING(R)", "nothing.tech".

Cut rhythm: 24 shots, ASL 1.88 s, median 1.60 s, quarters 1.61 / 1.13 / 2.25 / 2.25 (fast build, slower payoff). Shortest 0.40 s and 0.48 s (machine inserts at 19.9-20.8), longest 5.76 s (the call CU). 12 % under 1 s, 12 % over 3 s. Cuts on onset 23 % vs 10 % chance: about a quarter of the cuts land on a sound hit (more beat-driven than the other Nothing films).

Typography: dot-matrix (Ndot; free match Doto) lowercase "ear(3)", NOTHING(R) in caps, text block ~4 % of frame height; the claim in the light typewriter-flavoured serif (free match Cutive / IBM Plex Serif Light), sentence case, ~5.2 % of frame height incl. descenders, centred (frames/t042.8s.jpg). Cards on pure black, hard cuts, ~1 s each. No text over picture. The brand card also OPENS the film (0-1 s).

Colour/grade: low-key and dark. Median frame luma 32/255, 89 % of frames darker than 40. Neutral-cool (R-B -1.6), concrete greys, chrome fans catching hard light, one accent: her pale blue shirt. Contrast p95-p5 101 (soft blacks, not crushed). Light from above/behind, faces modelled with soft side light.

Camera/shots: symmetric locked wides (bench, warehouse), product macros against black, profile and 3/4 face CUs with shallow focus, inserts of machines. Slow pushes; no handheld. All real footage, no CG (the case and earbuds are practical props).

Transitions: hard cuts only (23). The "noise" is told with inserts (fans, meters) cut on hits.

Sound: music + designed noise + dialogue. Room/noise level climbs from -22 LUFS-M (1 s) to -10 (13 s) and peaks at 24 s (-8). Then two clean drop-outs (24.75 s: 1.05 s at -46 dBFS; 26.5 s: 0.9 s at -48 dBFS) = the "cut through the noise" moment, after which her voice sits on top. Whisper found phone-call dialogue at 18-37 s ("...I've been thinking about you." "And you hear me now?" "Nice." "It's great to hear your voice too." "Actually, let me call you right back."; transcript may be imperfect). Integrated -14.1 LUFS. Cards end the film almost silent (-35 at 45 s).

What makes it premium:
- The feature (voice through noise) becomes a physical set: a hall of fans and machines you can see and feel.
- Sound design tells the payoff: noise builds, then switches off when she speaks.
- One accent colour (pale blue shirt) in a dark grey world.
- Product handled like jewellery: macros of the transparent case on black.
- Brand card at both ends, tiny type, no CTA.

Recipe (real footage + HTML/GSAP):
1. Build the problem as a location: many visible noise sources (fans, speakers, machines). Light low-key (median luma ~30), keep one wardrobe accent colour.
2. Edit: build with 1-2 s shots and a few 0.4-0.5 s inserts on hits; give the feature moment one long CU (5-6 s). Then 3-4 release shots.
3. Sound: raise the noise bed for 15-20 s (+10 dB), then hard-gate it for ~1 s twice at the feature moment and lay the voice on top. Do the cut in the audio, not in the picture.
4. Cards in HTML: black frame, open with a 1 s brand card; end with name (dot font, 4 vh) -> claim (serif 300, 5 vh) -> brand -> URL, 1 s each, hard cuts. `gsap.set` visibility per card on exact frames, no tweening.
