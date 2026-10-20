# Is Europe facing a "Muslim takeover"? The data says otherwise  (The Economist, uploaded 2026-09-12 per yt-dlp, 11:05 full / first 150 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=To8r_IWYhZ0
Purpose: explainer in the studio-discussion format (4 editors at the red table + 1 remote bureau chief)
One-sentence point: Far-right claims about a "Muslim takeover" of Europe are tested against the numbers by Economist editors.

Structure (first 150 s):
- 0.0-6.2 hook: deputy editor Edward Carr frames the claim, lower third "Edward Carr / Deputy editor, The Economist".
- 6.2-13.3 context: two news photos, ~3-4 s each, slow push - AfD leaders celebrating, then an election-night crowd in front of a results board showing "18,5% / 44% / 9% / 9%" (the only numbers on screen in 150 s are inside a photo).
- 13.3-18.6 wide 5-way shot: four editors at the red table, the remote guest on the screen behind. A 1.5 s pause in the audio (17.5-19.0 s, -24 -> -56 LUFS) before the remote answer.
- 18.6-51.4 remote Berlin bureau chief Tom Nuttall in one 32.8 s webcam take: lower third at 20-24 s, then a location tag "Berlin" + red dot top-right from 26 s.
- 51.4-150 discussion: Britain correspondent Georgia Banjo (lower third 64-68 s) in close side angle, two-shots with Edward Carr, returns to the wide every ~25 s (90, 99, 126 s).

Cut rhythm: 17 shots in 150 s, ASL 8.82 s, median 6.2 s (cuts2, checked on the sheet; no corrections). ASL per quarter 7.5 / 12.5 / 6.25 / 6.25 s. Cuts per 10 s: 2,2,0,0,0,1,1,1,1,3,0,1,1,1,2. Longest: 32.8 s remote take (18.6 s), 16.6 s wide (99.4 s), 14.7 s correspondent (63.0 s). Shortest 2.4 s. 0% under 1 s, 88% over 3 s.

Typography (854x480 frames):
- Bug: white circle with serif "E" top-left (~7% H), always on.
- Lower third: identical system to the Japan episode - black bar ~9.6% H with white serif name + Economist-red dot, grey bar ~6.5% H with white sans title ending ", The Economist", flush to the left frame edge, ~42% W.
- Location tag (new here): black box flush to the top-right edge (x 85-100% W, y 3-11% H), white serif "Berlin" (cap ~3% H) + red dot; stays on for the rest of the remote take - tells you the guest is the man on the ground.
- No source credit on the news photos, no chart, no caption, no on-screen statistic beyond the results board in the photo.

Colour/grade: same studio as the Japan episode (cream walls, black architecture, red table #E3120B-ish, E-branded red mugs and mic flags); remote guest in a warm home office with books (his own "set"). News photos ungraded.

Camera/shots: 3+ studio cameras (wide 5-shot, side close-up of each speaker, side two-shot), locked off; remote webcam full-frame; two news photos with slow push. No b-roll video, no maps, no charts in the analysed window.

Transitions: hard cuts only (soft detections are the lower-third and tag fades).

Sound: integrated -22.6 LUFS (broadcast level). Dialogue only; the gaps between phrases sit around -57 to -61 dBFS (median of 50 gap floors -57.6 dBFS) - higher than the Japan episode (-80) because more mics are open / the remote line adds noise, but no audible music bed (guess based on the floors). Loudest moment 41.5 s (-12.5 LUFS momentary, the remote guest). Median momentary level per 30 s: -21, -19, -25, -25, -24, -28 LUFS - it gets quieter as the studio discussion settles.

What makes it premium:
- The masthead is the evidence: four editors plus the Berlin bureau chief - "we have people there" (the location tag says it in one word).
- Ruthless sameness: the same set, bug, lower third and location tag across episodes = a recognisable series.
- Very long holds (median 6.2 s) - the viewer is trusted to listen.
- Uses one photo that contains the numbers (the results board) instead of building a chart.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Location tag: `.loc{position:absolute;top:3%;right:0;background:#0d0d0d;padding:1.2vh 2vh;font:400 3.6vh "Source Serif 4";color:#fff}` + `::after` red dot 2.2vh `#E3120B`; GSAP `xPercent:100 -> 0` 0.4 s `power3.out` after the lower third leaves; hold until the speaker's take ends.
- Lower third: as in japan-world-economy (black 9.6% H + grey 6.5% H bars, serif name + red dot, sans title).
- Open with the host's question to camera (lower third), then 2 news photos of 3-4 s each (`scale 1 -> 1.05` linear), then the wide establishing shot.
- Hold a remote expert for 30-45 s in one take; cut back to the wide every ~25 s.
- Mix: dialogue only, -22 LUFS integrated (or -16 for social).
