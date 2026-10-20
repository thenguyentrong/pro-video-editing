# 2026 NBA Finals – Game 5 Intro: "Everything on the line"  (NBA on ESPN, uploaded 2026-06-14, 92.7 s incl. a 10 s channel end screen, 16:9, YouTube / NBA on ESPN channel)
URL: https://www.youtube.com/watch?v=qQcIOYIdUdE
Purpose: game-broadcast open / cold-open tease (the piece that opens the network's game coverage), uploaded after air
One-sentence point: every past champion's moment lives inside the gold of the trophy, and tonight's game decides who joins them.

Structure (times from metrics.json; content ends at 82.4 s, then a YouTube end screen):
- 0.0–7.0 HOOK, CG: gold world in macro: a ball on a mirror floor, a glowing ring, a liquid-gold sculpture, the league logo in gold, then the "Finals" script wordmark in gold particles (6–7 s).
- 7.0–30.6 ARCHIVE IN GOLD FRAMES: champions' celebrations from 1980s–2020s tape, each shown inside a gold CG frame, porthole or screen panel that the camera flies past; frames have depth and reflections.
- 30.6–55.8 CG VAULT FLY-THROUGH: three long continuous CG moves (8.1 s, 5.2 s, 7.3 s) through a gold vault: archive appears in a glass globe, on curved screens; ends in a gold particle burst and the wordmark on a gold floor (55 s).
- 55.8–76.5 FULL-FRAME ARCHIVE: celebrations full screen with gold bloom and falling confetti/particles added; the fastest part (10 cuts in 60–70 s).
- 76.5–81.8 LOCKUP: trophy on a gold stage with light fans, "Finals" wordmark in gold in front of it, hold ≈4 s.
- 81.8–82.4 NETWORK STING: a red-black organic CG shape with the league silhouette and a ball (the network's NBA brand), then the end screen.

Cut rhythm (content 0–82.4 s): 53 shots, ASL 1.55 s, median 1.08 s, 45 % under 1 s, 13 % over 3 s. ASL per quarter 1.37 / 2.29 / 1.47 / 1.14. Cuts per 10 s 9, 4, 7, 2, 5, 6, 10, 7: two slow CG valleys (10–20 s and 30–50 s) between fast archive bursts. Cuts on audio onsets 25 % vs 9 % chance: this piece IS cut to the music. Adaptive detector + 4 scene-detector cuts checked by eye (5.44, 28.56, 72.32, 77.2); 3 other scene candidates were movement inside one CG shot.

Typography: no supers, no names, no dates. The only type is the brand script wordmark, built in 3D gold (≈20 % of frame height at 6 s; ≈25 % in the trophy lockup), with the league logo to its left. Closest free for mock-ups: an upright brush script such as "Yellowtail", extruded and gold-shaded.

Colour/grade: one-material world: gold (#c9a14a highlights, #5a3d10 mids) on black. Archive footage is pushed warm/gold and gets bloom, haze and gold particle overlays so it belongs to the material. The only other colour is the red of the network sting at the end.

Camera/shots: CG macro and slow fly-throughs with reflections and depth of field; archive tape composited onto CG surfaces (frames, globe, curved screens); full-frame archive with slow push-ins; trophy hero on a stage with light fans.

Transitions: camera moves through CG geometry (portholes, frame edges), particle bursts that reveal the wordmark, hard cuts in the archive sections; ≈28 soft transition candidates = moves and flares, not dissolves.

Sound: measured at US broadcast level: integrated −24.3 LUFS (the US TV target is −24 LKFS), LRA 6.0 LU, true peak −6.7 dBTP; momentary max per second −20 to −28 for the whole open, the loudest 0.5 s at 89 s is the channel end screen, not the open. One rise at 5.4 s (logo → wordmark). I did not listen: whether a narrator speaks over it is not verified (the level pattern allows it).

What makes it premium:
- One material (gold) for the whole open, including the archive: like a title sequence, not like a promo.
- History is placed INSIDE the brand object (the trophy's world), so 40 years of tape feel like one collection.
- Long CG moves (5–8 s) alternate with fast archive bursts: two speeds, each clear.
- It is mixed to the broadcast spec (−24 LUFS) rather than to online loudness.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes; CG plates pre-rendered or licensed):
- Material: a gold macro plate set (licensed CG or real brass/gold macro), 6–8 plates of 3–8 s with slow moves.
- Archive-in-frame: footage inside a div with `border:18px solid; border-image: linear-gradient(135deg,#f6e3a1,#8a5a14,#f1d27a,#6b430d) 1`, `transform: perspective(1400px) rotateY(18deg)`, a gloss overlay `linear-gradient(120deg,rgba(255,255,255,.25),transparent 40%)`, and the panel flying past camera (`translateZ -600→+300px`, 3 s `power1.inOut`).
- Full-frame archive: `filter: sepia(.35) saturate(1.2) contrast(1.1)`, bloom = blurred copy at 40 % `screen`, gold particles canvas (200 sprites, 2–6 px, falling 60–120 px/s).
- Rhythm: 7 s CG hook → 23 s archive in frames (1–3 s each) → 25 s of 3 long CG moves → 20 s fast archive (≈1 s) → 5 s wordmark + trophy lockup. Cut on the music's onsets.
- Mix to −24 LUFS integrated for broadcast delivery (−14 to −16 for online cut-downs).
- Stock queries: "liquid gold macro abstract", "gold particles black background", "brass trophy macro rotating", "vintage basketball celebration archive" (archive needs a league licence).
