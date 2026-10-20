# High-rate composite preform automation becomes a reality | Loop Technology | Case Study  (FANUC Europe, 2026-09-04, 4:25, 16:9, YouTube @FANUCEurope)
URL: https://www.youtube.com/watch?v=cgaDCRqAc74
Purpose: customer case study (UK integrator/machine builder for aerospace composites, FANUC heavy robots)
One-sentence point: A UK firm builds aerospace composite preforms at high rate with FANUC robots carrying large custom grippers, and stays cost-competitive because of them.

## Structure
- 0-6.2 title over the real cell: five-line caps title top-left + fact bar at the bottom with four icons (Company / Industry / Country / Employees).
- 6.2-23.5 one 17.3 s brand block: yellow card with FANUC red logo and the customer logo, a dissolve into the yellow-tinted factory.
- 23.5-48.7 company story: managing director interview (name super), heritage building exterior, wide of the hall.
- 48.7-68.8 "The Challenge:" yellow box over a ply-cutting table; robots, engineers; an award box (≈64-67 s).
- 68.8-141.9 the solution: 10.2 s shot of the big gripper (68.8 s); teach pendant close-ups; "The FANUC M-2000 series" style yellow box over the robots (≈92-100 s); 1.8-5 s b-roll of heavy arms, plies, blue-lit inspection.
- 141.9-219.6 engineers and second/third interviewees (supers), yellow caps key-message tags under interviews ("COST COMPETITIVE THANKS TO FANUC ROBOTS", ≈184-190 s).
- 219.6-243.4 the proof: one 23.8 s take of the gripper picking and forming a large preform (longest shot).
- 243.4-261 closing interview + b-roll; 261-265.5 FANUC logo on yellow with URL.

## Cut rhythm
- 48 shots in 265.5 s, ASL 5.53 s, median 4.72 s, 0 % < 1 s, 77 % > 3 s, 10.8 shots/min. ASL per quarter 5.5 / 4.2 / 4.7 / 7.4 s.
- Longest 23.8 s (219.6 s, process take), 17.3 s (brand block incl. dissolves), 10.2 s. Shortest 1.36 s.
- Flat 0-3 cuts per 10 s; interviews 4-8 s per piece.

## Typography
- FANUC face = bold DIN-style sans (closest free: Barlow / Barlow Condensed Bold, or D-DIN).
- Opening title: Barlow ExtraBold caps, white, ≈10.5 % H per line (cap ≈8 %), five lines left-aligned at x ≈7 %, y ≈13-75 %, tight leading.
- Fact bar: four columns at y ≈88-95 %, thin line icon ≈8 % H + label regular ≈2.5 % ("Company") over value bold ≈2.5 % ("Loop Technology"), white.
- Info box: FANUC yellow (#FFD800) at ≈85 % opacity, black text, bold heading ≈4 % ("The Challenge:") + 3 regular lines ≈3.5 %, x ≈11-43 %, y ≈55-81 %, one corner cut at 45°.
- Key-message tag: solid yellow box bottom-left (x ≈4-41 %, y ≈70-87 %), black bold caps ≈3.8 %, two lines.
- Burned-in subtitles of every spoken line: white bold ≈3.5 % H, bottom centre (y ≈94 %), soft shadow, no box.

## Colour/grade
- Clean neutral factory, slight warm cast; FANUC yellow robots dominate; one cold blue-lit inspection section. Interviews at 50-85 mm with the machine behind.

## Camera/shots
- Real customer site only. Gimbal and slider moves, wide and medium shots of heavy arms with large grippers, close-ups of plies and the teach pendant, exterior of the heritage building.

## Transitions
- Hard cuts; dissolves on the brand block (≈9-17 s); fade to the end card.

## Sound
- Interview voices for ≈243 s (≈595 words, ≈2.4 words/s) over a light corporate bed. Integrated -19.4 LUFS, LRA 7.6 LU, true peak +0.2 dBTP. One 2.65 s silence at 13.8 s inside the brand block; small 0.3-0.55 s gaps in the music between interview pieces (51.8, 56.9, 90.1, 129.2, 132.8 s). Biggest rise +35 dB at 67.4 and 74.7 s (machine b-roll entries).

## What makes it credible
- A fact bar names company, industry, country and head-count in the first 6 s.
- Problem → solution → result told by three named people from the customer.
- One 23.8 s uncut process take near the end.
- Subtitles on all speech: works muted on LinkedIn.
- Weak: no process number on screen (cycle time, ply count, rate), even though "high rate" is the claim.

## Recipe (real footage + HTML/GSAP)
- Title: `font:800 10.5vh 'Barlow'; text-transform:uppercase; line-height:.95; left:7vw; top:13vh; color:#fff`; lines in with `gsap.from(lines,{y:30,autoAlpha:0,stagger:.08,duration:.4})`.
- Fact bar: `display:grid; grid-template-columns:repeat(4,1fr); bottom:5vh; left:7vw; right:7vw`; icon SVG 8vh stroke 2 px white; label `400 2.5vh`, value `700 2.5vh`.
- Challenge box: `background:rgba(255,216,0,.85); clip-path:polygon(0 0,100% 0,100% 85%,93% 100%,0 100%)`, heading `700 4vh Barlow`, body `400 3.5vh`; slide from x -30, 0.4 s.
- Subtitles: `font:700 3.5vh Barlow; color:#fff; text-shadow:0 1px 4px rgba(0,0,0,.6); bottom:3vh`, one line per phrase.
- Add one number card over the long process take (rate or cycle time) - the original leaves it out.
