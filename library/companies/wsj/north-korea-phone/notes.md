# What a Smuggled North Korean Smartphone Reveals About the Regime  (The Wall Street Journal, uploaded 2026-08-28 per yt-dlp, 5:02 full / first 150 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=nBRZKG1kjBM
Purpose: explainer (object-led "show and tell" with a reporter + a defector interview)
One-sentence point: A real smuggled North Korean phone, handled on camera, shows how the regime controls and sells to its richest citizens.

Structure (first 150 s):
- 0.0-10.7 hook: reporter Dasl Yoon at a white desk in a dark bookshelf set, holding up a red phone; lower third "Dasl Yoon / WSJ Reporter" 0-3.7 s. One 10.7 s take.
- 10.7-21.9 first inserts: macro of hands scrolling the home screen, the red back, her face defocused behind the phone, a payment app, a store app with prices (cuts every 1-2 s, 6 cuts in 10-20 s).
- 21.9-32.4 provenance: reporter to camera, then a macro of the back with a "DAILY NK" sticker and the model "해양 701" - the proof of where the object came from.
- 32.4-69.9 demonstration: home screen, quick-settings panel in extreme close-up with a finger, shopping app, app list; intercut with the reporter using the phone at the desk.
- 69.9-100 reporter presents the phone to camera (7.4 s hold), shopping and TV apps, landscape video on the phone shown to the lens, a football game.
- 100.0-101.98 sound drops for 1 s (-17 -> -39 LUFS), then a wide: a North Korean defector walks in and sits beside the reporter (101.98-107.5).
- 107.5-150 interview: side two-shots and singles of the defector, lower third "Ryu Seong-hyeon / North Korean Defector" (117-119 s), English subtitles of his Korean in short chunks ("250 U.S. dollars." / "So, it's pretty expensive" / "for North Koreans."), a phone-app insert at 143 s, back to the reporter at 145.6 s.

Cut rhythm: 46 shots in 150 s, ASL 3.26 s, median 2.54 s (cuts2, no corrections; soft detections are focus pulls and screen changes, not cuts). ASL per quarter 3.13 / 2.89 / 2.68 / 3.75 s - very even. Cuts per 10 s: 0,6,3,3,2,3,6,1,4,4,3,2,3,2,3. Longest: 10.7 s opening (0 s), 7.4 s presenting (69.9 s), 7.1 s interview (113.2 s). Shortest ~1.0 s. 4% under 1 s, 43% over 3 s.

Typography (854x480 frames):
- Bug: serif "WSJ" top-right, ~4% H, always on.
- Lower third: same WSJ system as the Neom film - black condensed serif name on a white box (box ~8% H, name cap ~3.3% H) and a white sans job title on a dark box (cap ~2.1% H), flush left at x 5% W, top ~61% H. "WSJ Reporter" / "North Korean Defector" - 2-3 words.
- Subtitles: white semibold sans, ONE line, 2-5 words per chunk, centred, baseline ~87% H, cap ~2.5% H, no box, faint shadow; chunks change every ~1.5-3 s, following his phrasing.
- No other text: no maps, no charts, no titles, no labels on the phone screens.

Colour/grade: dark charcoal bookshelf set, warm practicals, slightly lifted blacks; both people in black so the red phone is the brightest colour; a red retro TV on the shelf repeats the red (deliberate set dressing). Macro shots keep the screens bright and saturated (blue UI), backgrounds blurred to red/black bokeh.

Camera/shots: reporter medium to camera at the desk (locked), a dedicated macro camera with very shallow depth of field for hands + screen, close side angles, a wide for the defector's entrance, side two-shots during the interview. The real object in real hands is the evidence - no screen recordings, every screen is filmed.

Transitions: hard cuts only; focus pulls inside the macro shots act as soft "reveals".

Sound: integrated -19.0 LUFS (louder than the Neom film, closer to web level). A quiet bed under the voice (gap floors about -43 to -57 dBFS, never digital silence - probably music or room tone, not certain). One structural drop: 100.0 s, 1.0 s to -39 LUFS before the defector enters. Loudest moment 127 s (-10 LUFS momentary, the defector's voice); the second half is ~3 dB louder (median momentary -16 LUFS vs -19 in the first half) because his on-mic Korean is hotter. Cuts not on the beat (47% vs 53% chance).

What makes it premium:
- The object is the evidence and the hero: filmed like a product film (macro, shallow focus, hands), but proving a news story (the DAILY NK sticker = chain of custody).
- Colour discipline: black clothes, charcoal set, one red object (and one red prop echoing it).
- Zero graphics for 150 s - the screens themselves carry the information.
- A human witness enters on camera (wide shot of him walking in), not just a cut to a talking head.
- Subtitles in tiny chunks matched to his speech rhythm - easy to read, never two lines.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Shoot: reporter locked medium at a desk (dark set, one colour accent), a second camera on a macro lens for hands + object (f/2-2.8, background 1.5-2 m away), side angles for an interview.
- Edit: open on a 10 s reporter take holding the object; then 6-8 inserts of 1-2 s each; return to the reporter every 10-20 s; a 1 s audio dip + wide shot to bring in the witness.
- Lower third (same as WSJ system): `.lt{left:5%;top:61%}` name `background:#fff;color:#111;font:600 3.4vh "Libre Caslon Condensed",serif` + title `background:rgba(0,0,0,.7);color:#fff;font:500 2.1vh "Inter"`; hard cut on/off, hold 2-4 s.
- Subtitle chunker: split the translation at phrase boundaries into 2-5 words, `font:600 2.6vh/1 "Inter";color:#fff;text-shadow:0 1px 6px rgba(0,0,0,.6);bottom:13%;text-align:center`, one line only, each chunk shown for its spoken duration (1.5-3 s), no fade (hard swap).
- No graphics layer; if needed, only the WSJ bug.
- Mix: voice -18 to -20 LUFS short-term, a bed 18-20 dB under it, master around -19 LUFS integrated.
