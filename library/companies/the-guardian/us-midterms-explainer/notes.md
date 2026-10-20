# US Midterms: What are they and why do presidents dread them? | Explainer  (The Guardian, uploaded 2026-10-07 per yt-dlp, 3:37, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=wzU2YvfquQw
Purpose: explainer (civics primer, narrator only, tabletop stop-motion)
One-sentence point: The midterm elections can take Congress away from the sitting president, and history shows that usually happens, which is why presidents dread them.

Analysed: the full film (217 s).

Structure:
- 0.0-10.7 cold open: archive clips (election-night crowd, past presidents) play inside a walnut-framed "TV" prop standing on a black table; 2 hard cuts inside the frame (4.84, 7.12). Black for 0.9 s.
- 11.6-14.2 a spot-lit white cube with a US flag on black (the same object returns as the end card).
- 14.2-22.6 tabletop of game pieces, campaign cards and pawns; 16.9-22.6 title "THE MIDTERMS / EXPLAINED" on two paper flags pinned into wooden blocks (held ≈5 s).
- 22.6-71 chapter 1 "THE MIDTERMS": locked overhead view of a black desk; paper label card at top centre, a Capitol card, calendar sheets, then 14 president trading cards laid down one by one (stop-motion), red/blue backing = party. The desk is re-dressed between set-ups, so each cut is a new arrangement of the same world.
- 71.2-85 chapter 2 "THE CONGRESS": label card held 3.6 s on its own, then a pull-back to the full desk; 85-104 a real paper road map of the US; tokens are placed state by state (stop-motion) to show seats.
- 104-123 House vs Senate: one Capitol card torn in two ("House of Representatives" / "Senate"), two TV-frame props each playing a clip of the chamber's leader.
- 123-146 chapter 3 "THE PRESIDENT": TV frames with signing ceremonies, face cards beside them (Obama, Trump).
- 146.1-176.2 the longest set-up (30.1 s): one TV frame cycling through hearing clips on kraft paper while three paper labels "WASTE / FRAUD / CORRUPTION" drop in one by one at an angle.
- 176-204 history: Clinton, George W. Bush cards next to clips; 204.4 black.
- 205-212 title flags and pawns return; 209-217 end card: flag cube on black, small serif credits on the left, masthead under them.

Cut rhythm: 41 shots in 217 s, ASL 5.29 s, median 3.64 s, 0 % under 1 s, 59 % over 3 s, 11.3 shots/min (scene detector + 6 verified cuts inside the TV-frame clips; clip changes inside the small framed "TV" during the long holds are not counted, so the real picture-change rate is higher). ASL per quarter 4.17 / 5.43 / 4.52 / 6.03 s. Cuts per 10 s: 0-4, never more. Longest 30.1 s (146 s), 13.2 s (22.6 s), 12.6 s (49.8 s). Shortest 1.12 s.

Typography:
- Masthead "The Guardian" two-line serif logo top right (≈8 % H tall, white), always on, also over the prop scenes.
- All labels are physical: bold sans caps printed on cream paper strips (Guardian Headline/Sans look; closest free "Archivo" ExtraBold or "Work Sans" Bold). Title flags "THE MIDTERMS" cap ≈8 % H on cream, "EXPLAINED" in a white serif on navy (≈8 % H). Chapter label cards on the desk ≈4.5 % H caps. "WASTE / FRAUD / CORRUPTION" ≈8 % H black slab-ish caps on mint paper, rotated 10-15°.
- Trading cards: tiny white sans names on a coloured strip (≈1.5 % H).
- End credits: small serif, role bold ≈2.3 % H, names regular, flush left at x ≈52 % W, y ≈65-75 % H.
- No subtitles, no lower thirds (narrator never appears).

Colour/grade: black table (≈#0A0A0A), warm walnut frames, cream (#F1E7B8), navy (#3D4A86) and mint (#CDEBDA) paper, red/blue party cards. Soft single key light from above-left with real shadows. Archive inside frames keeps its own look. No grain, no letterbox.

Camera/shots: locked top-down and low 3/4 tabletop shots of real props; stop-motion placement of cards and tokens (≈ several frames per placement, judged at 1 fps); archive news video composited into the TV-frame props. No presenter.

Transitions: hard cuts between desk set-ups; two short holds on black (10.7-11.6 s, 204.4 s). Elements arrive by stop-motion, not by digital fades.

Sound: female narrator, music bed under the voice. Integrated -21.3 LUFS, LRA 4.7 LU (very even), true peak -2.6 dBTP. 8 drop-outs of 0.3-1.5 s; the chapter turns are marked by silence: 72.9 s (0.95 s, to -73 dBFS) before "THE CONGRESS" settles and 117.65 s (1.5 s) before "THE PRESIDENT", each followed by a re-entry of +55-58 dB measured from the gap floor. Cuts are not on onsets (50 % vs 57 % chance).

What makes it premium:
- One physical world for the whole film: every graphic is a real object on one black desk, lit like a product shot.
- News archive is shown inside a prop (wooden TV frame), so borrowed footage becomes part of the tabletop and never fills the screen.
- Chapters are physical paper labels, then a silence, then the new desk.
- Stop-motion placement makes counting visible (14 presidents, seats per state, three charges).

Recipe (real props or HTML/GSAP, Hyperframes):
- Shoot or build a black desk plate (`#0A0A0A`, soft top light, vignette `radial-gradient(circle at 40% 35%, #1b1b1b, #050505 70%)`).
- TV frame: a rounded rect `border-radius:4vh; border:3.2vh solid #6B4226; box-shadow: inset 0 0 2vh rgba(0,0,0,.6), 0 2vh 4vh rgba(0,0,0,.7)` with the clip inside; clips change by hard cut inside the frame.
- Paper labels: `background:#F1E7B8; padding:.8vh 2vh; font:800 4.5vh "Archivo",sans-serif; text-transform:uppercase; box-shadow:0 .6vh 1.2vh rgba(0,0,0,.5)`; rotate -12° to 12°.
- Stop-motion placement: `tl.set(card,{autoAlpha:1,x:..,rotation:gsap.utils.random(-4,4)},t+i*0.32)` (no tween, 3-8 frames apart) to fake hand placement.
- Hold each desk set-up 4-13 s; one long 25-30 s set-up for the strongest list; cuts per 10 s ≤ 4.
- Mix: VO at about -18 LUFS short-term, bed ≈12 dB under, 1-1.5 s silence before each chapter label, master -21 LUFS (web: -16).
