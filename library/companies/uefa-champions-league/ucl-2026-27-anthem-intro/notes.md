# Official UEFA Champions League Anthem  (UEFA, uploaded 2026-09-08, 61.6 s, 16:9, YouTube / UEFA channel)
URL: https://www.youtube.com/watch?v=LaADHznVSNg
Purpose: season-opening brand promo built from the pre-match anthem ritual (not the broadcast title graphics; see ucl-2024-25-intro for those)
One-sentence point: the anthem ceremony itself is the brand: every club, standing in line with child mascots, while the same 30-year-old anthem plays.

Structure:
- 0.0–1.8 HOOK: wide high shot of a stadium during the opening ceremony: a giant starball banner and a club-crest banner held by volunteers on a purple pitch cover printed with light-line patterns; full tifo in the stands (0.5 s frame).
- 1.8–58.0 BODY: ~28 line-up shots, one club per shot (Dortmund, Atlético, Barcelona, Galatasaray, Arsenal, Lens, Liverpool, Man City, Sporting, Villarreal ...). Mix of medium line-ups (5–6 players + mascots, waist up) and tighter 2–3-player shots; a star close-up (Haaland, 47.5 s) arrives in the last third.
- 58.0–61.5 PAYOFF: the longest shot (3.5 s): wide Bayern line-up with Kane under the floodlight flares; music decays from 59.5 s. No end card, no logo, no text.

Cut rhythm: 30 shots in 61.5 s, ASL 2.05 s, median 1.96 s. ASL per quarter 1.92 / 1.71 / 1.71 / 2.20 s. Exactly 5 cuts in every 10-second window (4 in the last). Shortest 1.12 s, longest 3.50 s (the final shot), 0 % under 1 s. This is a metronome: same shot length from start to finish, only the last shot is held longer. Cuts do not sit on audio onsets (7 % vs 10 % by chance); they follow the phrasing, not hits (the anthem is legato choir, few sharp onsets). Soft-detector candidates at 44.2, 53.6, 56.9, 59.6 s were checked by eye: slow pans/zooms inside a shot, not cuts.

Typography: none added. The only overlay is the UEFA.tv bug top-right (white "UEFA.tv" between two thin rules, ~5 % of frame height including the rules, at ~84–95 % x / 5–10 % y). All brand type lives inside the footage: LED boards "UEFA CHAMPIONS LEAGUE", starball sleeve badges, the centre-circle banner.

Colour/grade: natural broadcast colour, night games under floodlights, no visible stylised grade. A recurring colour motif comes from the event itself: the child mascots wear the same orange-and-black kit in almost every shot (bottom third of frame), which ties 28 different clubs together. 0 % of frames are "mostly empty"; the frame is always full of faces.

Camera/shots: broadcast touchline cameras: slow lateral tracking along the line, slow push-ins, eye level, long lenses with shallow depth of field on the tighter shots (24.5 s). No drone, no CG, no slow motion that I could see.

Transitions: 29 hard cuts, nothing else. No dissolves, no wipes, no graphics.

Sound: the UEFA Champions League Anthem (Tony Britten, 1992, adapted from Handel's "Zadok the Priest"; known track, I did not listen). Measured: audio starts at 0.5 s around −27 LUFS momentary, first big rise at 7.95 s (+15.7 dB; probably the full choir/orchestra entry, a guess), then mostly −15 to −19 LUFS; from 26 s to 59 s it is a flat plateau at −15. Integrated −17.5 LUFS, LRA 7.0 LU, true peak −6.9 dBFS. Ends with a decay at 59.5 s. No voice-over, no SFX, no crowd sound audible in the level curve.

What makes it premium:
- The ritual is the content: no graphics needed because the anthem plus line-ups are already the brand.
- Strict, even rhythm (one club every ~2 s) makes 28 clubs feel like one competition.
- A colour motif found in the event (mascot kits) does the job a grade would do.
- Sonic logo with 30+ years of equity: two bars of the anthem identify the brand faster than any logo.
- Restraint: the only "end card" is a held wide shot.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Footage: 25–30 real "people standing in line" shots (team, staff, students, crew) shot at eye level, 85–135 mm, slow lateral slider move or slow push (2–3 % zoom over the shot). Put one consistent colour element in every shot (same lanyard, scarf or shirt colour) in the lower third.
- Edit: shot length 2.0 s ± 0.3 s for the whole piece, hard cuts only; final shot 3.5 s, wide.
- Hyperframes: one track of clips, each `data-duration="2.0"`; per clip a GSAP push `gsap.fromTo(clip, {scale:1.0}, {scale:1.03, duration:2.0, ease:"none"})`; no text layers except an optional small bug top-right (white, 3.5 % of frame height, opacity 0.9).
- Audio: one ceremonial anthem-like cue (choir/orchestra), enters quiet, full by ~8 s, flat plateau around −15 LUFS momentary, decays in the last 2 s. No SFX, no VO.
