# Aker BP - ANYmal X Offshore Deployment on the Valhall Platform  (ANYbotics, 2023-12-06, 2:04, 16:9, YouTube @anybotics)
URL: https://www.youtube.com/watch?v=mY6bIF_5skQ
Purpose: customer deployment record (proof-of-concept log film, partner-made look)
One-sentence point: on day 3 of an offshore test, an ATEX quadruped walks out of a door and does a remote inspection round on a real platform, with the operator's screen as proof.

## Structure (studied from the sheet and metrics)
- 0.0-0.2 black lead-in.
- 0.2-23.2 one real take: locked-off wide of a steel blast door on the platform; title over it "ROBOTICS POC VALHALL 2023 / DAY 3" (1-6 s); a worker opens the door, ANYmal X walks out, turns and walks along the wall (8-23 s).
- 23.2-111.8 one 88.6 s screen recording: the remote-operation app (robot camera, top status bar with AUTO mode, P-STOP) beside a partner's 3D digital twin (orange plant model with the robot's position ring), plus a second inset of a handheld/third-person camera following the robot (from ≈41 s). At ≈109 s a thermal image with min/max temperature pops up as the inspection result.
- 111.8-119.8 real wide: robot in the platform workshop/maintenance area, people at benches.
- 119.8-123.8 end card: white, "In collaboration with" + three logos (customer, ANYbotics, software partner).

## Cut rhythm
- 6 shots in 123.9 s, including a 0.17 s black lead-in and a 0.13 s tail (these make "% under 1 s" read 33 %; content shots are 23.0, 88.6, 8.0 and 4.0 s). The cut at 111.8 s was verified by eye and added (the scene detector missed it).
- ASL 20.65 s, median 5.98 s, 2.9 shots/min. Cuts per 10 s: 0-1.
- Inside the 88.6 s recording the insets change content (≈41 s, ≈72 s, ≈84 s) - hard switches inside the screen, not edit cuts.

## Typography
- Title: thin wide-tracked caps, white with a 1 px underline: "ROBOTICS POC VALHALL 2023" cap ≈6.5 % H, letter-spacing ≈.2em, then "DAY 3" ≈10 % H, centred at y ≈45-60 %; fade in/out ≈0.5 s, hold ≈5 s. Closest free: Josefin Sans Light / Montserrat Light.
- End card: "In collaboration with" humanist sans ≈5 % H top-left, black on white; logos ≈12 % H.
- All other text is real software UI (≈1-1.5 % H), including the thermal readout.

## Colour/grade
- Ungraded, true-to-site: grey steel, safety yellow floor, orange coveralls; digital twin in saturated orange; thermal in blue-to-red.

## Camera/shots
- Tripod wide for the door exit; screen capture for the mission; one tripod wide at the end. No music video moves, no drone.

## Transitions
- Hard cuts; fades on the title.

## Sound
- Music bed (likely with site sound in the first take). Integrated -13.5 LUFS, LRA 9.6 LU, true peak +0.1 dBTP (over). No drop-outs; 0.35 s silence at the very end. Biggest hits +17-21 dB at 12.4-16.3 s (the robot comes out of the door).
- Cut-to-onset sync 0 %: the edit ignores the music.

## What makes it credible
- Day-stamped title (log, not ad).
- One 23 s real take of a door exit and an 88.6 s uninterrupted operator screen: nothing is hidden by editing.
- The mode field reads AUTO; the customer's own software and digital twin show position.
- Three logos at the end: the customer co-signs.
- Weak spots: no speed label (the screen recording may be real time but is not stated), the UI shows a user name/e-mail (privacy), and the film is long to watch for a non-expert.

## Recipe (real footage + HTML/GSAP)
- Shoot a locked-off 20-30 s "first step" take at the real site; title it like a log: `PROJECT SITE YEAR` + `DAY N`, Josefin Sans 300, 6.5vh, letter-spacing .2em, 1 px rule, `DAY N` at 10vh; fade 0.5 s, hold 5 s.
- Then one long screen capture of the real operator app + map; place a third-person video inset (≈35 % W) so viewers see the robot and its view at the same time; mark the inspection result with a 0.3 s scale-in.
- Blur any personal data in the UI. Add a `REAL TIME` or `4X` badge if you speed up the capture.
- End on a white co-branding card, 4 s.
