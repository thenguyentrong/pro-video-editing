# EVERY Champions League Goal From Matchday 2 | Highlights  (UEFA, uploaded 2026-10-16, full video 24:12; analysed 0–125 s only, 16:9, YouTube / UEFA channel)
URL: https://www.youtube.com/watch?v=SKv0pg-sUqI
Purpose: highlights compilation; studied for the in-match graphics package (score bar, scorer strap, "FINAL SCORE" tab, how the bar changes between matches)
One-sentence point: one persistent centre-bottom score bar tells you match, score and scorer for every goal, and it rebuilds itself centre-out whenever the match changes.

Structure (first 125 s = 3 matches, 6 complete goals, about 20 s per goal):
- 0.0–27.6 Goal 1, LENS 0-1 SPORTING CP (Luis Suárez): live wide shot of the build-up and goal (0–14.7), second wide angle (14.7–21.7), behind-the-goal replay (21.7–27.6).
- 27.6–47.7 Goal 2, LENS 0-2 SPORTING CP (Issa Doumbia): bar now has the "FINAL SCORE" tab on top (last goal of the match); wide (27.6–36.5), high wide (36.5–43.9), tight tracking replay (43.9–45.8), behind-the-goal replay (45.8–47.7).
- 47.7–87.2 Goals 3–4, SABAH vs SLAVIA PRAHA (Kaheem Parris 1-0, Joy-Lance Mickels 2-0 with FINAL SCORE tab); the bar disappears on the hard cut at 47.65 and rebuilds (see Typography).
- 87.2–125 Goals 5–7, INTER vs CLUB BRUGGE (0-1 Nicolò Tresoldi, 1-1 Lautaro Martínez, 1-2 at 121 s).
- No intro, no title card, no music: the video starts directly on the first goal.

Cut rhythm: 23 shots in 125 s, ASL 5.43 s, median 4.76 s. ASL per quarter 7.81 / 4.46 / 5.21 / 3.47 s. 70 % of shots are longer than 3 s; longest 14.7 s (first live shot). Each goal = one long live shot (7–15 s) + 1–3 replays (1–7 s). The shortest shots (0.9–1.5 s) are fast replay angle changes at 115–120 s. Verified by eye: cuts at 45.8, 116.0, 117.3, 119.5 s were added (replay angle changes during fast camera motion, missed by the detector); 61.9, 72.2, 76.4 and 78.7 s are pans inside one shot.

Typography / graphics package (measured on 854×480 frames):
- Score bar: centre-bottom, spans 20–80 % of frame width, rows 75–85 % of frame height. Three parts: centre score box (bright royal blue ~#0726f2, ~10 % of width, 9.4 % of frame height) with white condensed digits "0 - 1"; left and right "wings" (~6 % of frame height, vertical gradient #2c39e7 at the top → #29336e at the bottom, ends cut on a slant like a parallelogram) carrying the team names right/left-aligned against the score box and the club crests at the outer ends.
- Team names: white condensed bold caps, cap height 4.2 % of frame height. Closest free match: Barlow Condensed 700 or Oswald 600. Digits are the same family, larger (~7 % of frame height, estimated).
- Scorer strap: small box under the score box, 10–11 % of width, 4.2 % of frame height, ~#1e3cbe, white regular caps ("LUIS SUÁREZ"), gap ~1.2 % of frame height. Closest free match: Barlow 500, letter-spacing +2 %.
- "FINAL SCORE" tab: same size box above the score box (70.4–74.4 % y), shown only on the clip of a match's last goal.
- Behaviour: within a match, score, scorer and tab change instantly on the hard cut (no animation, 27.4 → 27.5 s). Between matches the bar vanishes on the cut and rebuilds centre-out in ~0.8 s: 47.8 s a thin vertical line appears at centre → 47.9 it opens into the dark score box → 48.0 the box fills blue and the digits come in → 48.1 thin lines shoot out left and right to the full bar width → 48.2 the wings thicken to full height, names wipe outward from the centre → 48.3–48.4 crests appear at the ends → 48.4–48.6 the scorer strap grows down from the score box.
- UEFA.tv bug top-right throughout (~5 % of frame height).

Colour/grade: untouched broadcast colour (green pitch, sponsor boards). The only brand colour is the blue bar, which works because blue is complementary to the green pitch.

Camera/shots: standard broadcast coverage: main high wide camera follows play; replays from behind the goal, low tracking tele, reverse angle. No slow motion I could detect at 1 fps (replays may be real-time).

Transitions: hard cuts only (23 cuts). The score bar build is the only "designed" transition and it marks the change of match.

Sound: natural stadium sound only; no music, and no commentary detectable from the level curve (a guess, I did not listen). Base about −36 LUFS momentary, crowd swells on goals to −25…−28 (e.g. 22 s, 56 s, 84–86 s, 106–108 s). Integrated −33.2 LUFS (very quiet), LRA 10.1 LU, true peak −17.6 dBFS.

What makes it premium:
- One graphic does everything: match, score, scorer, "final" state, in one centred bar that never moves.
- Information is stable: the bar stays still during play; it only changes on cuts.
- The rebuild animation is short (0.8 s), geometric and centre-out, like the brand's symmetric starball.
- Blue on green: maximum contrast with one brand colour, no extra decoration.
- Raw, uncut live shots of 7–15 s let the goal breathe; replays are short.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Bar layout (1920×1080): container centred, width 1152 px (60 %), top at 814 px (75.4 %). Score box 190×102 px, background #0726f2, digits Barlow Condensed 700 at font-size 104 px (cap height ~75 px = 7 %), white, letter-spacing 0.02em, "0 - 1" with spaced hyphen. Wings 481×65 px each, background linear-gradient(180deg, #2c39e7 0%, #2b34b5 50%, #29336e 100%), outer end clip-path polygon slanted 12 px; names Barlow Condensed 700 at font-size 62 px (cap height 45 px = 4.2 %), uppercase, 14 px padding from the score box; crest 52 px at the outer end. Scorer strap 200×45 px, #1e3cbe, Barlow 500 at 26 px uppercase, 13 px below the box. Tab "FINAL SCORE" same style, 11 px above the box.
- Build (GSAP, total 0.8 s): tl.from(box, {scaleX:0.02, duration:0.1}) .from(box, {backgroundColor:"#0b1250", duration:0.1}) .from(digits, {opacity:0, duration:0.1}) .from(wingLines, {scaleX:0, transformOrigin:"center", duration:0.12, ease:"power2.out"}) .from(wings, {scaleY:0.1, duration:0.12}) .from(names, {clipPath:"inset(0 50% 0 50%)", duration:0.15}) .from(crests, {opacity:0, scale:0.6, duration:0.12}) .from(strap, {scaleY:0, transformOrigin:"top", duration:0.15}).
- Updates within a match: swap text on the cut frame, no animation. Exit between matches: remove on the cut, no animation.
- Edit: per item one long live shot (8–14 s) + 1–3 replays (2–5 s); hard cuts; natural sound only, crowd swell on the key moment.
