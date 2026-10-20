# Dusty Robotics + DPR: Multi-trade layout eliminates misinterpretation for all trades  (Dusty Robotics, 2022-09-14, 3:09, 16:9, YouTube @DustyRobotics)
URL: https://www.youtube.com/watch?v=6HBl5BUiGs4
Purpose: customer case study / testimonial (general contractor DPR Construction + trade partners on a hospital addition)
One-sentence point: Site people from the GC and the trades say that one robot-printed layout from the signed-off model means every trade follows the same mark, so clashes are caught on the floor, not a month later.

## Structure (interview-led, no narrator)
- 0.0-2.8 (0-1.5 %) fade in co-brand card on white: Dusty logo | thin divider | DPR logo.
- 2.8-14.3 (1.5-8 %) cold-open: top-down / wide of printed lines on a raw deck, crew walking; first speaker (subcontractor BIM technician) states the core benefit - every trade looks at the same correct mark.
- 14.3-56.9 (8-30 %) context: the project (hospital addition, interior and exterior), which items are printed (walls, soffits, shafts, electrical devices, plumbing centrelines), layer types. Second speaker (GC BIM manager). B-roll: crew with tablet, robot printing, Dusty-branded vest close-up.
- 56.9-85.5 (30-45 %) before/after told in words: before, each trade snapped its own lines from grid lines -> discrepancies; now one source on the floor. Third speaker (field engineer). Robot b-roll in 6-10 s shots.
- 85.5-122.8 (45-65 %) workflow proof: robot with total station on tripod (10.8 s, longest shot), crew reading the floor, macro of the robot body, tablet UI close-up (green octagon target on a floor-plan map), fourth speaker (superintendent): the model is signed off by all trades and goes straight to the floor.
- 122.8-154.5 (65-82 %) the concrete story: a pipe penetration found slightly off by looking at the floor, instead of a framer finding it a month later; extra details (door openings, room names) printed; owners pleased. Fifth speaker.
- 154.5-184.7 (82-98 %) verdict + warm close: "no-brainer", recommend; a speaker smiles about bringing his kids to watch the robot; robot hero shots (low, "16" unit number on the shell).
- 184.7-188.7 (98-100 %) co-brand end card on white, fades to grey.

## Cut rhythm
- 36 shots in 188.7 s (32 detected + 3 verified: dissolve at 2.8 s, cuts at 161.62 and 184.69 from the adaptive detector). ASL 5.24 s, median 5.19 s, 0 % under 1 s; shortest 1.17 s (last interview tail), 1.96 s.
- ASL per quarter 4.29 / 6.74 / 4.72 / 4.29 s. Longest 10.76 s (robot + total station, 85.5 s), 9.97 s (interview, 122.8 s), 8.88 s (interview, 56.9 s).
- Cuts per 10 s: 1-3 everywhere. Talk shots 4-10 s; b-roll blocks of 1-4 shots under the voice, each 2-6 s.

## Typography
- Name super: thin condensed caps (Bebas Neue Light / Oswald Light look; free: Oswald 300 or Bebas Neue), white. Name cap height ≈7 % H; role line ("SENIOR BIM TECHNICIAN - COMPANY") ≈2.7 % H caps, on a 2 px orange (#F07C1E) underline rule with a short vertical tick at the outer end. Placed bottom-left (x ≈3 %, y ≈83-92 %) or bottom-right - always on the empty side opposite the speaker. Hold ≈4-5 s on the first appearance only; slide/wipe in along the rule.
- No captions, no data cards, no titles inside the film. Co-brand logo card both ends: logos ≈10 % H on white, 1 px grey divider.

## Colour/grade
- Natural daylight in an open concrete structure; neutral, slightly lifted shadows, soft contrast. Colour comes from PPE: hi-vis yellow and orange vests, yellow/white hard hats, the orange robot. No grain, no letterbox.

## Camera/shots
- Interviews: medium close-up, speaker off-centre (rule of thirds), looking off-camera to an interviewer, 50-85 mm look with shallow depth of field, site and working crew soft behind. All in full PPE (hard hat, vest, safety glasses).
- B-roll: gimbal at robot height, top-down printed lines, tripod-mounted total station with robot, tablet UI over the shoulder (real app), crew walking the printed layout, logo on vest and robot body macros.
- No drone, no timelapse, no CGI, no screen recording full-frame.

## Transitions
- Hard cuts; dissolve only from the opening and into the closing logo card (≈0.5 s), fade to grey at the end.

## Sound
- Lavalier interview dialogue carries everything; soft corporate piano/acoustic bed underneath (LRA 3.6 LU: very compressed, flat). Integrated -18.0 LUFS, true peak -0.6 dBTP (clipping risk). No drop-outs; silence only in the last 0.35 s. Biggest rises are speech onsets (+25-27 dB at 20 s, 166 s, 173 s).
- Cut-to-onset sync 25 % vs 53 % chance: cuts follow sentences, not beats.

## What makes it credible
- Five named people with full titles from the GC and three trade companies (the customers' customers say it, not Dusty).
- One concrete, checkable anecdote (an off-position pipe penetration found early) instead of adjectives.
- The real tool chain is visible: total station, tablet app, printed floor, crew reading it.
- Missing: no numbers (time saved, accuracy, area), no captions for sound-off viewing.

## Recipe (real footage + HTML/GSAP)
- Film 4-6 interviews on site in PPE, 85 mm, speaker on one third with the working floor behind; 2 lavaliers; ask for one concrete "before vs now" story and one problem caught.
- B-roll list: top-down print 3 shots, robot + total station 10 s, tablet over shoulder 4 s, crew reading the floor, logo macros, hero low shot.
- Super: `<div class="super"><b>NAME</b><i></i><span>ROLE - COMPANY</span></div>`; `b{font:300 7vh Oswald;text-transform:uppercase}` `span{font:300 2.7vh Oswald;letter-spacing:.04em}` `i{height:2px;background:#F07C1E}`; `gsap.from(i,{scaleX:0,transformOrigin:'left',duration:.4})` then text `from {x:-20,opacity:0}` stagger .08; hold 4.5 s; side = empty side of frame.
- Cut on sentences; ASL ≈5 s; b-roll 2-6 s under the voice; co-brand card `fade .5 s` at both ends. Add burned-in captions and one number card to lift it.
