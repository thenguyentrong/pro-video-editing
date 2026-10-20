# Superior Robot Mobility - Where AI Meets the Real World  (ANYbotics, 2023-10-30, 2:01, 16:9, YouTube @anybotics)
URL: https://www.youtube.com/watch?v=yVQkDL5l_1g
Purpose: capability explainer (technology film for the AI locomotion stack)
One-sentence point: ANYmal walks where others cannot because it learned to walk in simulation, sees the terrain, and this already works on real industrial stairs and rough ground.

## Structure (studied from the sheet and metrics)
- 0.0-2.7 cold open: black, a white line-drawing of stairs (terrain mesh) draws on in 3D.
- 2.7-17.4 claim + context: interview with the CTO (name super at 3-6 s) intercut with real plant shots (stairs in a process plant, gravel yard, night refinery with barrier, 7-12 s).
- 17.4-56 how it works: a second named expert (professor, super 18-21 s), cut against simulation renders: grid world with boxes (16-17 s), thousands of robots training on procedural terrain (22-26 s, 38-41 s), a swarm on white stairs (31-35 s), line-drawn stairs on black then a crowd of red robots climbing (44-55 s).
- 56-84 perception proof: real plant shots, then the same real shots with a colour height-map point cloud laid over the stairs (63-65 s, 68 s, 77-81 s); pure point-cloud views on grey (69-72 s, 76 s, 82-83 s).
- 84-104 field tests: robot on gravel and rock (84-88 s); lakeside park course with wooden crates, steps and a table (91-96 s, 99-104 s) - long real takes of jumps and climbs.
- 104-116 back to the job: CTO, then an ANYmal X inspecting a pump hall; a green tracked circle + tick appears on a pressure gauge (110-115 s), then a thermal/visual icon on a motor.
- 116.8-120.7 end card: coral red full frame, white wordmark, then the "N" symbol with URL.

## Cut rhythm
- 37 shots in 120.7 s (scene detector; adaptive also flags 45.96 s, a change inside the line-drawing sim - not added). ASL 3.26 s, median 2.56 s. ASL per quarter 2.74 / 2.74 / 3.35 / 3.35 s.
- 2.7 % under 1 s, 45.9 % over 3 s, 18.4 shots/min. Cuts per 10 s: 2-5, flat.
- Longest: 8.28 s (65.8, real stair climb with point-cloud overlay), 7.16 s (75.9), 6.2 s (43.8, sim crowd). Field-test takes 5.7-5.8 s.
- 56 % of cuts on an audio onset (chance 50 %): the cut follows the speech, not the beat.

## Typography
- Name super: role in tiny caps (≈2 % H, white, letter-spaced) above the name in sentence case (≈3.5 % cap height) white on a coral box (box ≈5 % H); bottom-right of the speaker, x ≈55-88 %. Closest free: Barlow SemiBold / Barlow (DIN-like grotesk).
- End card: wordmark ≈7 % H, white on coral #EE5A5A-ish; then symbol ≈5 % with a ≈1.5 % URL.
- No captions, no claims as text, no speed or autonomy labels.

## Colour/grade
- Natural, slightly cool industrial light; the robot's red and the coral brand colour are the only strong colours. Sim renders: white/grey worlds with red robots (matches the real robot). Point clouds: rainbow height map (yellow ground → green → cyan → purple).

## Camera/shots
- Interviews: two cameras, medium + medium-close, real plant/lab behind (stairs scaffold, lab with red robots).
- Real robot: locked-off or slow gimbal, low angle at stair level; field tests wide, locked, the whole obstacle course in frame.
- Sim: clean CG flyovers and top-downs, clearly synthetic (grid floors, hundreds of copies), never mixed with real in one frame. The point cloud is the one overlay on real footage, and it is the robot's own data.

## Transitions
- Hard cuts; soft candidates at 76.8 s (overlay fading on) and 116.8 s (fade into the end card).

## Sound
- Interview-led with a corporate electronic bed. Integrated -19.0 LUFS, LRA 4.0 LU, true peak -0.0 dBTP. No drop-outs; 0.35 s silence at the start only. Biggest hits +15-17 dB at 32.1, 35.0, 49.15 and 95.6 s (sim swarm and the crate jump).

## What makes it credible
- Two named experts with titles say the claims (CTO, professor of the lab the company came from).
- The machine's view is shown on top of the real take (height-map point cloud on the real stairs).
- Simulation is shown openly as simulation, then the same skill on real stairs and in a public park.
- Ends on the job (gauge reading with a green tick), not on the stunt.

## Recipe (real footage + HTML/GSAP)
- Interview A-roll 50-60 % of runtime; cut away every 2-5 s to: sim render (if you have one), real take, real take + sensor overlay.
- Overlay: export the robot's point cloud / height map as video with alpha; `mix-blend-mode:normal; opacity:.85`, fade in 0.4 s after the real shot has run 1 s, so viewers first see the real thing.
- Name super: `<div class="sup"><small>CTO SOLUTIONS</small><b>Dr. Name</b></div>`; `small{font:600 2vh Barlow;letter-spacing:.08em}`, `b{font:500 3.5vh Barlow;background:#ee5a5a;padding:.4vh .8vw}`; wipe in with `clip-path` 0.35 s.
- Inspection proof: track a 2 px green circle (r ≈8 % H) on the gauge, tick badge pops `back.out(1.7)` 0.25 s.
- End card: full-frame brand colour, wordmark 7 % H, 3-4 s.
