# Will Japan bring down the world economy?  (The Economist, uploaded 2026-08-19 per yt-dlp, 8:46 full / first 150 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=QBorPsQpEzU
Purpose: explainer in a studio-discussion format (editors at the red table + one remote editor)
One-sentence point: Japan's bond and yen troubles could spill into world markets, explained by three Economist editors in conversation.

Structure (first 150 s):
- 0.0-3.7 hook: host Henry Curr asks the question straight to the table, lower third "Henry Curr / Acting business affairs editor, The Economist".
- 3.7-21.4 set-up: wide three-way shot (two editors at a red round table, the third editor on a large screen behind them), medium side angles of the host.
- 21.4-33.4 first visuals: three press photos, ~4 s each with a slow push - Treasury Secretary Bessent at a White House TV position shot through foreground lights/stands, Bessent with Trump in the Oval Office, Vance and Bessent at a cabinet table.
- 33.4-59.4 correspondent Josh Roberts explains (lower third on the right side, opposite his eyeline), cut with wide and reaction shots.
- 59.4-75.0 one 15.6 s held still: a "To Do / Buy Japanese Yen (JPY) $5-10 bil" note on a cabinet-meeting desk in front of a "SCOTT BESSENT" name card, slow push. (It looks like an illustration/composite built on a press photo, not a real document - guess.)
- 75.0-103.3 back-and-forth: correspondent, host reaction, wides.
- 103.3-150 remote editor Ethan Wu (Asia business & finance editor) on a webcam-style shot against black, lower third at 105-110 s, one unbroken 46.7 s take.

Cut rhythm: 20 shots in 150 s, ASL 7.5 s, median 4.62 s (cuts2; dropped a false cut at 0.08 s). ASL per quarter 4.17 / 5.36 / 6.25 / 37.5 s - it slows down as the remote guest takes over. Cuts per 10 s: 3,1,3,2,2,2,0,1,2,1,2,0,0,0,0. Longest: 46.7 s remote guest (103.3 s), 15.6 s prop still (59.4 s), 9.4 s correspondent (75.0 s). Shortest 1.9 s. 0% of shots under 1 s, 90% over 3 s. Cuts follow speaker turns, not music (35% on audio onsets vs 62% chance - they avoid cutting on a syllable).

Typography (measured on 854x480 frames):
- Bug: white circle with a serif "E" top-left (x 3.5-7.5% W, y 5-13% H, ~7% H diameter), always on.
- Lower third, flush to the frame edge on the side the speaker is NOT looking at (left for the host, right for the correspondent), ~42% W wide: black bar 9.6% H with the name in white serif (looks like the Economist's own serif; closest free "Source Serif 4"), cap ~3.5% H, followed by an Economist-red dot (~2.5% H); under it a grey ~85% bar 6.5% H with the job title in white sans (looks like Econ Sans/Milo; closest free "Fira Sans"), cap ~2.3% H, sentence case, always ends ", The Economist". Holds ~4-5 s.
- No captions/subtitles, no chart text, no headlines in this window.

Colour/grade: neutral-warm studio, cream walls, black shelves and table base, one strong brand red (#E3120B-ish) on the table top and mic flags; the remote guest is lit blue-shirt on near-black. Press photos keep their own colour; no grade unification, no grain, no letterbox.

Camera/shots: 3-camera studio (wide, two mediums from the side), locked off, eye-level; a remote webcam feed shown full screen; press photos with slow pushes; one illustrative still. No b-roll video, no charts, no maps in the first 150 s.

Transitions: hard cuts only; soft detections at 106-110 s are the lower third fading in/out.

Sound: integrated -22.4 LUFS (broadcast level). Voice only: no music bed under the conversation - the 50 ms gaps between phrases fall to -80...-90 dBFS (digital silence) all through, which a music bed would never allow. Loudest moment 62 s (-14.7 LUFS momentary). Median momentary level steady at -21 to -24 LUFS per 30 s.

What makes it premium:
- The brand IS the set: red table, E-flags on the mics, black/cream architecture; no motion graphics needed to say "Economist".
- Experts are the Economist's own editors, each with a job title that ends ", The Economist" - authority from the masthead.
- Restraint: one bug, one lower-third design, hard cuts on speaker turns, silence between sentences instead of music.
- Evidence is only photographic (news photos) and held long with slow pushes.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Shoot 3 locked cameras (wide 3-shot + 2 side mediums at ~30 degrees), warm key, cream/black set with one red object; remote guest full screen on near-black.
- Lower third: `.lt{position:absolute;top:74%;left:0;width:42%}` (right:0 for speakers looking left) name bar `background:#0d0d0d;height:9.6%;color:#fff;font:400 4.2vh "Source Serif 4";padding-left:5%` + red dot `width:2.4vh;height:2.4vh;border-radius:50%;background:#E3120B;margin-left:1vh` + title bar `background:rgba(70,70,70,.85);height:6.5%;font:500 2.5vh "Fira Sans";color:#fff`. GSAP: bar `xPercent:-100 -> 0` 0.4 s `power3.out`, text fades 0.2 s after, hold 4 s, reverse.
- Bug: 7vh white circle, serif "E", top-left at 3.5% / 5%.
- Press photos: hold 4 s each, `scale 1 -> 1.05` linear; a prop/illustration may hold up to 15 s with `scale 1 -> 1.08`.
- Cut on speaker turns at a pause (not on a word), never shorter than ~1.9 s.
- Mix: dialogue only, gated room tone, -22 LUFS integrated (raise to -16 for social), no bed.
