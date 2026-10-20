# Sonos | Sound for how you live  (Sonos, 2025-08-11, 1:10, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=DwIdo-4jwNk
Purpose: system explainer / brand film (narrated)
One-sentence point: One continuous flight through a cut-away house shows how every Sonos product fits a room and a moment of the day.

Structure (one CG take, 0.0-67.1 s, then the logo):
- 0.0-6.5 fade from black to a dolls-house cross-section of a modern house at dusk, every room lit (frames/t003.0s.jpg); VO opens.
- 6.5-12 the camera flies into the bedroom: a small speaker on a bedside table, plants, morning light (t009.0s).
- 12-14.5 pull back out to the house.
- 14.5-19.5 into the kitchen: a round table, a speaker, a mug (t016.0s).
- 19.5-28 long hold on the full house while the VO explains grouping (t030.0s area).
- 28-33.5 drop down to the patio at night: portable speaker by a fire pit.
- 33.5-48 into the living room: soundbar macro skim along the wood (t040.0s), headphones on a stand in front of the TV.
- 48-53 out to the house again.
- 53-60 into a child's room: speaker on a desk with pencils (t056.0s).
- 60-67.1 final pull back to the whole house, held ≈ 6 s.
- 67.1-70 SONOS wordmark white on black (t068.5s), 2.2 s of silence at the end.

Cut rhythm: 2 shots. ASL 35 s is meaningless; the real rhythm is the camera: 5 room visits of 5-14 s, separated by 4-8 s holds on the full house. Every visit = one product + one use case + one VO sentence.

Typography: none in the body; no supers at all. End: SONOS wordmark (wide geometric caps, its own logotype), cap ≈ 4 % H, centred, white on black.

Colour/grade: dusk palette (median luma 64), slightly warm (R-B +11), moderate contrast (p95-p5 115): slate-blue night outside, warm amber room lights inside, oak wood, olive and terracotta accents. Products are matte black or white and never re-coloured.

Camera/shots: photoreal CG; a single motion-control-style path: push-in through the cut-away wall, slow orbit or skim over the product (macro on the soundbar's fabric and logo), pull-back out. No people, no hands.

Transitions: no cuts; the camera move IS the transition (in through the wall, out to the overview). One fade from black, one cut to the logo.

Sound: male VO from 0.2 to 67 s, calm and friendly, one sentence per room; music bed under it plus small room sounds; −16.5 LUFS, LRA 2.9 LU, true peak −2.3 dBTP. Logo in silence (2.2 s).

What makes it premium:
- One uninterrupted camera path feels engineered and expensive, and makes "it all works together" literal.
- The overview shot comes back between rooms, so the viewer never gets lost.
- No text: VO + picture carry the features; the frame stays clean.
- Products shown small in real-looking rooms, then a single macro skim for craft.

Recipe (CG or HTML/GSAP 2.5D):
1. Build or license a cut-away house render (one large still at ≥ 4K works for 2.5D).
2. HTML version: one `<img>` of the house; each room visit = `gsap.to(house,{scale:3.2, xPercent:…, yPercent:…, duration:2.2, ease:'power2.inOut'})`, cross-fade to a real room clip at the end of the push (0.4 s), hold 4-8 s, reverse out.
3. Order: overview 6 s → room → overview 3-8 s → room ...; 4-6 rooms in 60 s.
4. VO: one sentence per room, starting as the push begins.
5. No supers; logo on black 2-3 s in silence. Master −16 LUFS.
