# Sky Sports – channel promo style

Examples studied (Oct 2026, all 16:9, YouTube / Sky Sports channel):

| Example | Type | Length | Shots | ASL | Median | <1 s | Integrated / LRA | Cuts on onsets (chance) |
|---|---|---|---|---|---|---|---|---|
| [feel-it-all-rebrand-2017](feel-it-all-rebrand-2017/notes.md) | channel relaunch spot (:60) | 60.0 s | 23 | 2.61 s | 2.36 s | 4 % | −23.1 LUFS / 4.1 LU | 9 % (4 %) |
| [cricket-where-stories-start-2018](cricket-where-stories-start-2018/notes.md) | summer cricket promo (:40), letterboxed | 40.1 s | 25 | 1.60 s | 1.00 s | 48 % | −22.9 LUFS / 6.3 LU | 33 % (24 %) |
| [f1-2024-around-the-world](f1-2024-around-the-world/notes.md) | F1 season-launch promo (:40), letterboxed | 40.0 s | 43 | 0.93 s | 0.80 s | 74 % | −23.0 LUFS / 2.8 LU | 33 % (19 %) |

## The look in one paragraph
Sky Sports promos sell a feeling and a schedule, not match footage. Each spot has one cinematic idea that is built into the picture: a butterfly swarm that grows from a kitchen through empty stadiums, a housing-estate courtyard that becomes a test ground with real broadcast graphics on kids, 24 race cities with their names built in 3D into the locations. The look is a film trailer: ≈2.4:1 letterbox (bars ≈12.5 % top and bottom), cinematic grade, real or VFX-extended locations, few or no supers. All three are mixed exactly to the European broadcast target (−22.9 to −23.1 LUFS integrated, true peak −10 to −14 dBTP). The end is always the same brand frame: the blue "sky" + red "sports" logo box centred, one small line or date, sometimes a channel-name cycle, sometimes a white parent-brand card.

## Sub-styles
1. **Brand metaphor spot (rebrand).** Calm 2–3 s metronome, empty venues, one CG element in every shot, small tagline, 7 s lockup with the channel names cycling every ≈1 s.
2. **Story promo.** Real kids or fans in a real place, a VFX transformation (estate → stadium) after a 0.7 s audio drop-out, broadcast lower thirds and stats on non-athletes, top-down → aerial rise as the end.
3. **Calendar promo.** The data (24 races) is the title and the order; 0.5–1.2 s shots cut on the music, place names in 3D type inside each location, one 5 s hero shot with fireworks, title → date card → corporate card in 2.6 s.

## Rules (most important first)
1. **One idea inside the picture.** A metaphor element, a transformation or in-scene type; not graphics on top.
2. **Show anticipation, not results.** Empty venues, kids, cities; rights footage only as texture.
3. **Trailer frame.** 2.4:1 letterbox, cinematic grade; bars come off only for the logo card.
4. **Brand colours enter through the idea.** Blue and red butterflies, the blue broadcast strap; the logo box last.
5. **Broadcast loudness.** −23 LUFS integrated (EBU R128), LRA 3–6 LU, true peak ≤ −10 dBTP on the uploads.
6. **Small, centred end type.** Tagline ≈2 % H, endline ≈1.5–3.5 % H, logo box ≈8 % H centred at ≈48 %; date as the only fact.

## Recipe (real or licensed footage + HTML/GSAP, Hyperframes)
- 40–60 s; letterbox bars 135 px (1080p) until the logo card.
- Metaphor layer: particle/alpha-video element in every shot, density growing over the film; tint in the two brand colours.
- In-scene type: a CSS 3D plane matched to the ground (`perspective` 900 px, `rotateX 70deg`), Archivo Black caps 260 px, `mix-blend-mode: overlay`, drifting with the camera.
- Broadcast strap on a non-athlete: gradient bar 52 px tall with a white crest square, name 36 px; slide in 0.3 s.
- End: hazy aerial, logo box 90 px tall centred, channel-name slot swaps every 1.0 s, endline/date in Montserrat 300–400 caps; hold 4–7 s.
- Mix to −23 LUFS for broadcast. Free stand-ins: Montserrat for Sky Text; never use the real logo box.
