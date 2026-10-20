# Israel bombed journalist at work and appeared to attack ambulances aiding her, NGOs say – explainer  (The Guardian, uploaded 2026-10-06 per yt-dlp, 3:33, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=szDFb1boAGk
Purpose: explainer (correspondent-led news explainer built on NGO reports, user video and social posts)
One-sentence point: NGO investigations say a journalist in south Lebanon was struck while working and the ambulances sent to reach her were attacked too, and the film walks through the evidence and the army's own statements.

Analysed: the full film (213 s).

Structure:
- 0.0-9.2 cold open: agency footage of a memorial (a poster of the journalist held up), 5 cuts in 9 s, credit "Reuters" top left.
- 9.2-18 the guide: Middle East correspondent at a desk in the Guardian office, two angles (frontal close-up and 3/4 profile), lower third at 9.5 s.
- 18-24 first evidence: an NGO report web page, sharp in the centre over a blurred, enlarged copy of the same page (credit top left).
- 24-32 who she was: archive of the journalist on location.
- 32-54 what happened: dash-cam / phone video ("Video provided"), a dark slate 3D map of south Lebanon with the occupied strip in yellow and a black pin label (35-41 s, credit "IDF", date line "As of 21 April 2026"), then the user video of the strike area.
- 54-104 correspondent returns every 10-20 s between ambulance footage, Arab TV clips (their red chyron kept) and the Red Cross.
- 104-133 the ambulances: Red Cross logo stills, night footage with blue lights, rescue in rubble.
- 135-157 the army's version: its posted statement in Arabic/English with one phrase in a yellow highlighter, an aerial of the ruins, chat messages.
- 158-189 the counter-evidence: correspondent (longest talking shot), screenshots of posts with yellow highlights.
- 190-199 funeral, correspondent's last line.
- 199.6-212.7 close: a grid of 11 black-and-white portraits building in, caption "Journalists killed by Israel in Lebanon since 2023" (13.1 s, the longest shot).

Cut rhythm: 52 shots in 213 s, ASL 4.09 s, median 3.48 s, 0 % under 1 s, 56 % over 3 s, 14.7 shots/min. ASL per quarter 3.32 / 3.32 / 4.43 / 4.84 s (slows as the evidence gets heavier). Cuts per 10 s: 5 in the cold open, then 1-4. Longest 13.1 s (portrait grid), 9.6 s (user video at 41 s), 9.0 s. Shortest 1.08 s. Adaptive detector suggested 3 more (117.8, 148, 207.8 s): changes inside the night footage and the grid, left out.

Typography:
- Masthead: two-line serif "The Guardian" top right, ≈8 % H, white at ≈60-100 % opacity.
- Credit: bold serif (Guardian Text Egyptian look; closest free "Merriweather" Bold / "Source Serif 4" Bold) top left at x 5 % W, y ≈6 % H, cap ≈2.4 % H, white, no box: "Reuters", "Video provided", "Human Rights Watch", "IDF", "Union of Journalists in Lebanon".
- Lower third (no box): name in bold serif ≈4 % H, role in regular serif ≈3 % H with the masthead in italics after a thin bar ("Middle East correspondent | The Guardian"), placed in the open side of the frame (x ≈55 % W, y ≈80-89 % H). Held ≈4-5 s.
- Map: white sans place names ≈3.5 % H; a black box label with white sans ≈2.8 % H and a yellow dot pin; bold serif date line top left ≈3.5 % H.
- Documents and posts: screenshots shown full width; the key phrase gets a flat yellow highlighter (≈#FFE500); NGO report page in the centre over a blurred 150 % copy of itself.
- Closing caption: bold white serif ≈3.5 % H under the portrait grid.
- No running subtitles (all speech is English).

Colour/grade: agency and user footage kept as shot; the office is daylight, grey-green, shallow focus. Map: charcoal relief (#3A3A3A) with near-black sea, one yellow (#E5B000) territory fill. Portrait grid: black and white on black. Yellow is the only accent.

Camera/shots: correspondent at a desk (2 angles, handheld-steady), agency footage, user-submitted phone video, a 3D relief map with a slow push, screen captures of reports and posts, still logos, photo grid.

Transitions: hard cuts only. Map and grid build inside a shot (fills and photos appear in place).

Sound: correspondent's voice dominates; integrated -27.1 LUFS (the quietest film in this set), LRA 7.1 LU, true peak -4.6 dBTP, median RMS -36.5 dBFS. 15 silences ≥0.3 s and only 5 drop-outs (0.3-1.2 s; longest 79.45 s, 1.2 s), consistent with a sparse or absent music bed (not confirmed by ear). Natural sound of the footage enters hard: +36 to +46 dB rises at 9.2, 76.7 and 85.4 s. Cuts not on onsets (43 % vs 47 % chance).

What makes it premium:
- The correspondent is the guide but appears only between pieces of evidence; the proof (reports, maps, user video, the army's own posts) fills most of the screen time.
- Every borrowed frame is credited top left in one quiet serif.
- The other side's statement is shown in its original form with one highlighted phrase, then tested.
- The ending widens the story with a portrait grid held for 13 s in silence-like restraint.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Guide shots: 2 angles of the reporter at a real desk, 4-12 s each, every 10-25 s.
- Credit: `.credit{position:absolute;left:5%;top:5%;font:700 2.4vh "Merriweather",serif;color:#fff;text-shadow:0 1px 4px rgba(0,0,0,.5)}` on every borrowed shot.
- Lower third: `.lt .n{font:700 4vh "Merriweather"} .lt .r{font:400 3vh "Merriweather"} .lt .r i{font-style:italic}`, no box, in the open side of the frame, fade 0.3 s, hold 4-5 s.
- Document card: page at 70 % width in the centre over `filter:blur(12px) brightness(.7)` copy scaled 1.5; highlight `background:#FFE500` wiped `scaleX 0→1` in 0.5 s `power2.out`.
- Map: charcoal relief still, `fill:#E5B000` territory at 90 %, push `scale 1→1.15` over 6 s `none`.
- Close: B/W photo grid 5×3, photos pop in with `stagger:0.15`, caption fades last; hold 10-13 s.
- Mix: voice at about -20 LUFS short-term, no bed or a very low one; let natural sound hit for ≈1 s; master -24 to -27 LUFS for this quiet register (or -16 for social).
