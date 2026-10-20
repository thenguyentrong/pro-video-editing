# Next generation of construction dumpers: Bosch Rexroth and Fiori Group teamed up!  (Bosch Rexroth, 2026-06-17, 4:00, 16:9, YouTube @BoschRexroth, [EN] subtitles)
URL: https://www.youtube.com/watch?v=HZV1VRpvZ-k
Purpose: customer case film (Italian construction-machine maker, Rexroth electronic transmission in a site dumper)
One-sentence point: With Rexroth's electronic transmission, Fiori's new site dumper is cheaper, lighter, safer and easier to drive - say its CTO and a test driver.

## Structure
- 0-5.2 Rexroth logo builds from coloured stripes on white.
- 5.2-15 drone over the factory, the dumper on a gravel road, title in a cyan box ("The next Generation of Mobile Machines").
- 15-23.5 statement card on navy: one sentence with key words highlighted in cyan boxes (partnership, both company names, the sector).
- 23.5-26 dumper; 26-30 question card typed on navy ("Tell us about the new DF70 ... What are the most innovative elements?").
- 30-53 CTO interview outdoors with the machine and factory behind (name super), English subtitles of the Italian answer, b-roll of the dumper driving and tipping.
- 53-57 question card "What are the main fields of application?"; 57-95 interview + b-roll incl. golden-hour road shots.
- 95-99 question card about the electronic transmission; 99-131 answer + b-roll with cyan benefit tags ("INCREASED SAFETY FOR THE OPERATOR").
- 131.6-183.7 one 52 s technical animation: blue x-ray CGI of the dumper, components flown out and labelled (axial piston motor, axial piston pump, control unit + software), a benefits slide "BENEFITS OF THE NEW ELECTRONIC TRANSMISSION BY REXROTH:" with three caps columns.
- 174-178 question "Is it easy to drive?"; 178-205 test driver interview (super), cab POV, joystick and display close-ups, tag "INCREASED DRIVING COMFORT".
- 205-209 question "Do the new features make life easier for you?"; 209-236 answer, b-roll, sunset drive away.
- 236-240 Rexroth logo again.

## Cut rhythm
- 67 shots in 240.2 s, ASL 3.58 s, median 1.96 s, 22 % < 1 s, 30 % > 3 s, 16.7 shots/min. ASL per quarter 3.0 / 3.3 / 12.0 / 2.2 s (the 52 s animation fills the third quarter).
- Longest 52.2 s (CGI), 23.4 s (15 s: statement card + dumper), 13.2 s. Shortest 0.36 s: stripe-wipe flashes (12.4-14.9 s: seven cuts 0.4 s apart; 229.5-231.1 s).
- Interview sections 3-6 cuts per 10 s; 0 cuts for the 52 s animation.

## Typography
- Bosch Sans-like grotesk (closest free: Inter Bold), white.
- Question / statement cards: navy (#0b2a45) full frame, bold white ≈7 % H, centred, 3-5 lines; key words on cyan (#3fc1e6) highlight boxes; typed word by word with the highlight box growing behind the word.
- Name super: navy box with bold name ≈4.5 % H + navy box with role ≈2.8 % H, offset cyan/grey/red stripe bars behind (bottom-left to centre, y ≈68-90 %).
- Subtitles: white ≈3.3 % H on a translucent dark box, bottom centre (y ≈93 %), the English translation of every Italian line.
- Benefit tags: cyan box with bold white caps ≈3 % H, two lines, slid in from the left.
- CGI labels: small caps ≈2 % white; benefit columns bold caps ≈3.5 %.

## Colour/grade
- Natural Italian daylight and golden hour, green fields, white machine; cool navy/cyan graphics; the CGI section is dark blue x-ray with cyan and red light streaks.

## Camera/shots
- Real: drone, gimbal tracking of the moving dumper, low angles of the tipping bucket, cab POV, macro of joystick and display, interviews outdoors at 35-50 mm with the machine and factory behind. CGI: x-ray model with exploded components.

## Transitions
- Stripe wipes in brand colours (cyan, grey, red) with 0.4 s flash cuts; hard cuts; the CGI section enters through a blue light streak.

## Sound
- Italian interviews ≈199 s of speech (≈385 words) over a calm corporate bed. Integrated -22.5 LUFS (quiet), LRA 5.6 LU, true peak -6.1 dBTP. Short silences 0.3-0.45 s in the logo build and the statement card (4.85, 7.1, 10.4, 17.0, 17.75 s) and at the end logo (234.85 s). Biggest rises +37 dB at 119.0 s and +32 dB at 95.6 s (music under the question cards).

## What makes it credible
- The customer's CTO and a real driver speak; the machine works on real gravel.
- Interviewer questions shown as cards give clear chapters.
- The x-ray animation explains a hidden system (the transmission) that footage cannot show, and keeps its own clearly stylised look.
- Weak: benefits are claims without numbers (no % cost, kg or fuel figures).

## Recipe (real footage + HTML/GSAP)
- Question card: navy background, `font:700 7vh Inter; text-align:center`; words split, highlight words wrapped in `<mark>` with `background:#3fc1e6; padding:0 .3em`; `gsap.from(words,{autoAlpha:0,duration:.01,stagger:.12})`, `gsap.from('mark',{scaleX:0,transformOrigin:'left',duration:.25})` when its word appears.
- Stripe wipe: 6-8 bars `height:4-8vh` in `#0b2a45 #3fc1e6 #d0d6db #e20015` cross the frame in 0.4 s (`xPercent:-110 → 110`, stagger .03), cut under them.
- Subtitles on a translucent box `rgba(0,0,0,.45)` for every non-English line.
- Add one number per benefit tag (e.g. "-x kg").
