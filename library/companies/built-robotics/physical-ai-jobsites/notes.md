# How to Deploy Physical AI on Construction Jobsites  (Built Robotics, 2026-06-08, 1:03, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=z5Nf8Nz_zyI
Purpose: product explainer / workflow ad ("playbook" for deploying autonomous pile drivers on a solar site)
One-sentence point: A Built robot fleet is deployed in a few clear steps (safety zone, load plans, robots work, one person supervises, data comes back), so a contractor gets ROI from day one.

## Structure
- 0.0-4.8 (0-8 %) contrast hook: a humanoid robot walking in a lab (the "AI is the future" cliche), VO: some think AI is the future.
- 4.8-15.7 (8-25 %) "we use it every day": autonomous excavator cab, then the morning routine: a pickup truck on a desert site, a worker in hi-vis and white hard hat opens the door, takes out a reel of flagging tape, ties it to a stake.
- 15.7-24.3 (25-39 %) step 1 safety: tape strung across the site, a bilingual "WARNING / Do not enter" sign with the robot working behind it, a laptop in the truck with the robot UI, two workers walking the zone.
- 24.3-35.3 (39-56 %) step 2 plans: laptop UI "Configure session" with a grid of robot cards and the text label "REO / Robotic Equipment Operator" left, track close-up, robots start driving piles (wide, two machines), one operator in a truck with a laptop + split screen of the robot working (2-up).
- 35.3-42.9 (56-68 %) the human part: a worker climbs into a telehandler; a worker on the radio; "some jobs still need a human".
- 42.9-49.5 (68-79 %) data: real rows of piles with a composited glowing blue scan running along them (stylised as-built visualisation, 3.7 s), an excavator at sunset with blue lights, a pile lifted against a pink sky.
- 49.5-55.5 (79-88 %) night work: dusty site with machine lights at dusk, worker leaning into a truck window, a white pickup and the robot.
- 55.5-59.2 (88-94 %) finish: macro of a placed pile row with the sun behind; dip to black.
- 59.2-62.9 (94-100 %) logo: white "BUILT / ROBOTICS" on black, 3.7 s.

## Cut rhythm
- 29 shots in 62.9 s (one cut added by hand at the dip into the logo, 59.2 s). ASL 2.17 s, median 1.96 s, 0 % under 1 s, 21 % over 3 s, 27.7 shots/min.
- ASL per quarter 1.97 / 1.75 / 2.25 / 1.97 s: very even, 4-6 cuts per 10 s.
- Longest: opening humanoid 4.8 s, logo 3.7 s, blue data scan 3.7 s. Shortest 1.0-1.2 s (no flash cuts).

## Typography
- Almost none. One text label over a UI shot: "REO" bold + "Robotic / Equipment / Operator" regular, white, left-aligned at x ≈4 %, cap height ≈5.5 % H per line (≈7 % font size), 4 lines; geometric grotesk (closest free: Manrope / Inter). Appears with the UI shot (≈2 s).
- Persistent white "B" bug bottom-right, ≈8 % H.
- End logo: "BUILT" condensed bold ≈10 % H + spaced "ROBOTICS" ≈3 %, centred on black (closest free: Oswald Bold).

## Colour/grade
- Warm desert daylight and sunset pinks, crisp contrast, slightly teal shadows. Blue as the "AI/data" colour (scan glow, machine lights). Worker PPE yellow-green is the brightest colour.

## Camera/shots
- All real site footage except the opening humanoid lab shot and the composited blue scan.
- People-first: the worker's routine (truck, tape, stakes, laptop, radio) frames the robots; robots appear mostly in mid-wides with workers or vehicles nearby for scale.
- Real UI on a laptop in a truck (session config, robot list); split screen operator + robot (2-up, 50/50).
- No drone in this cut; low track close-ups; sun flares.

## Transitions
- Hard cuts; one 2-up split; dip to black (≈0.3 s) into the logo.

## Sound
- Calm male VO over a modern electronic track; sound of trucks, doors and the pile hammer under it. Integrated -14.3 LUFS, range 2.9 LU (very compressed, social-ready), true peak -1.0 dBTP. No drop-outs; biggest hit at 41.4 s (+25 dB) entering the data block. 2.4 s music tail on the logo.

## What makes it credible
- Written as a procedure: safety zone first, then plans, then work, then data - a buyer sees the real steps.
- The worker is the protagonist; robots are tools in the background.
- Real UI and a physical safety boundary (tape, sign) on screen.
- Weak: the blue data scan is stylised CGI over real footage without a label; no numbers in this cut.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- 25-30 shots of 1.5-3 s, one VO line per step (5-6 steps), 60 s total.
- Shoot a "day on site" with one worker: arrive in truck, mark zone (tape, sign), open laptop, start robots, supervise from the cab, a manual task, sunset/night work, finished rows macro.
- Label on UI shot: `font:700 7vh/1 Manrope` for the acronym + `400 7vh/1.05` for the words, `left:4vw; top:28vh; color:#fff`; `gsap.from(lines,{opacity:0,y:10,stagger:.08,duration:.3})`.
- Split screen: two `<video>` at `width:50vw`, 0.4vh black gutter, hold 2-3 s.
- Data glow (if you use it, mark it "visualisation"): CSS `mix-blend-mode:screen` overlay of a blue gradient tube on each pile, `gsap.fromTo(glow,{scaleY:0},{scaleY:1,stagger:.15,transformOrigin:'bottom'})`.
- Master ≈-14 LUFS, range ≤3 LU for social.
