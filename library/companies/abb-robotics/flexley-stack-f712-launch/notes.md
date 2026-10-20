# A new chapter in autonomous intralogistics: the AMR Flexley Stack F712  (ABB Robotics, 2026-07-09, 1:31, 16:9, YouTube @ABBRobotics)
URL: https://www.youtube.com/watch?v=794O92l-6QA
Purpose: launch film (product reveal at a launch event; interviews + kinetic type + stunt b-roll)
One-sentence point: The F712 autonomous forklift-AMR brings AI Visual SLAM, safe 24/7 operation and fleet software - "a turning point in industrial robotics".

## Structure (cut list + English captions)
- 0.0-4 hook: dark warehouse, a BMX rider puts on his helmet, LED walls, a rider jumps (1-3 s). Host VO: "I've covered a lot of events like this..."
- 4-11 host: "LUKAS M. ZIEGLER / Robotics influencer & Host" super; giant "ABB Robotics" letters behind him; "what we are about to see is truly, truly game-changing."
- 11-24 president: "MARC SEGURA / President of ABB Robotics" (13-18 s): "we are at the turning point in industrial robotics. Not because robots are getting faster or stronger only, but because AI is moving ... into the physical space." Kinetic words "FASTER" (16 s) and "STRONGER" (17 s) slam in over BMX shots; camera close-up of the stereo camera (19 s); 3D SLAM visualisation with feature points and green corner brackets, "ABSOLUTE CONTROL" (20-21 s); robot reveal "ABB Flexley Stack AMR F712" on the body (23-24 s).
- 24-41 benefits (AMR manager): "ALFONSO GONZALEZ / Global AMR Manager" super; kinetic captions repeat the spoken words: "INCREASE ROI" (27-30 s), "OPERATE|" -> "OPERATE SAFELY 24/7" (31-33 s, typed with a cursor and a red-to-white colour wipe), robot driving into racks, BMX rider weaving around the moving AMR (39-41 s).
- 41-57 features (R&D product manager): "RICARDO MARTINEZ / AMR R&D Product Technical Manager" super; "MAXIMIZE EVERY SQUARE METER" (45-47 s, words stack), mast lifting a pallet (48-52 s), "COMPATIBLE WITH MASTS AND ADD-ONS" (54-56 s).
- 57-69 navigation (R&D lead, panel on stage): "AI-Powered / Visual SLAM / navigation technology" (57-60 s) over a grey 3D-scanned warehouse, "RENAUD DUBE / R&D Unit Lead - Sevensense by ABB Robotics" super, "Rich 3D maps" (65-67 s).
- 69-82 software (UX designer): "WITH AMR STUDIO(R) / One software platform for the entire AMR fleet" (70-71 s), screen recording "Flexible" (75 s), "Flexible layout configuration and modification" (76-77 s), "AINHOA NARVAEZ / AMR Studio UX Designer" super, panel shot.
- 82-87 finale: BMX rider jumps over AMRs, "Flexley(R) Stack / F712" huge title with the robot in front of the numbers (84-87 s).
- 87.1-90.5: ABB Robotics logo on white.

## Cut rhythm
- 54 shots in 90.5 s. ASL 1.68 s, median 1.40 s. ASL per quarter 1.19 / 1.62 / 1.74 / 2.06 s - fastest at the hook, slower as the explanation grows.
- Longest 3.96 s (83.12, final title), 3.88 s, 3.72 s, 3.40 s. Shortest 0.68 s.
- 20 % under 1 s, 7 % over 3 s. 7-8 cuts per 10 s in the first 30 s, 3 in the last 10 s.
- Cuts follow the interview edit (43 % on onsets vs 56 % chance).

## Typography (data/specs on screen)
- Wide extended geometric caps (ABB's brand face; closest free: Lexend Zetta / Michroma) for kinetic words and names; a humanist sans (closest free: Open Sans/Inter) for name subtitles and small lines.
- Name supers: name in wide caps ~4 % height + role in sentence case ~2.3 %, white, bottom-left (x ~6 %, y ~68-80 %), no box; hold ~4-5 s.
- Kinetic captions = the speaker's key phrase, in caps, centred or left, 4-8 % height, 2-4 words per line, stacked up to 3 lines. In: typed with a block cursor ("OPERATE|"), red ABB colour sweeping into white, or words scaling/sliding in; one keyword huge and full-width ("STRONGER" ~10 % height, edge to edge).
- Product title: "Flexley(R) Stack" ~5 % + "F712" ~28 % height in the same wide face, white, with the real robot composited IN FRONT of the numbers (depth layering).
- Feature lines with a bold middle line: "AI-Powered / **Visual SLAM** / navigation technology".
- End: ABB logo red + "Robotics" black on white.

## Colour/grade
- Club-like magenta/red/blue practical lighting in a dark warehouse (event look), interviews in bright neutral daylight with soft background, one 3D-scan section in grey/black with green and red feature points.

## Camera/shots
- Mix: event interviews (2-camera, stage with giant brand letters), real product b-roll in a lit warehouse, BMX stunt rider around the robots (energy/scale device), 3D SLAM visualisation, screen recording of the software, final hero wide.
- The robot moves slowly and realistically; the energy comes from the rider and the lights, not from speeding up the robot.

## Transitions
- Hard cuts; kinetic type often bridges cuts (a word stays while the shot changes).

## Sound
- VO = interview voices (host, president, managers) over a driving electronic track. Integrated -14.5 LUFS, loudest at 69.8 s. Short silences 43.35, 47.8, 54.25 s (0.15-0.2 s) before word slams; biggest rise 51.15 s (+43 dB).

## What makes it credible / premium
- Named people with titles from CEO to UX designer - the company stands behind the claims.
- Specific feature words on screen exactly when they are spoken.
- Real robot moving at real speed; SLAM point view shows how it navigates; real software UI.
- Weak spot: stunt rider and club lights are "event energy" - fun, but they say nothing about the job.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Interview supers: `<div class="name"><b>ANNA MULLER</b><span>Head of Robotics, Company</span></div>`; `b{font: 600 4vh 'Lexend Zetta'; letter-spacing:.04em}`, `span{font: 400 2.3vh Inter}`, `left:6vw; bottom:20vh`; `gsap.from(name.children,{autoAlpha:0,x:-20,duration:.4,stagger:.1})`.
- Kinetic keyword synced to the transcript: typewriter with a cursor `<i class="cur">|</i>` blinking (`repeat:-1, yoyo:true, duration:.4`), plus a colour sweep: `background: linear-gradient(90deg,#fff 50%,#ff000f 50%); background-size:200%; -webkit-background-clip:text; color:transparent; gsap.to(el,{backgroundPosition:'0% 0', duration:.5})`.
- Depth title: a rotoscoped PNG/WebM of the machine on top of the giant number: z-order `video bg < text < machine matte`.
- Scan view: real point cloud or a screen recording of your perception UI with green corner brackets and a caps label "ABSOLUTE CONTROL".
