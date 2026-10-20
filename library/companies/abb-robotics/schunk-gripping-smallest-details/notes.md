# Sometimes the smallest details make the biggest difference  (ABB Robotics, 2026-07-02, 2:31, 16:9, YouTube @ABBRobotics)
URL: https://www.youtube.com/watch?v=kbqn1KumldU
Purpose: B2B partner film / trade-show interview (ABB x SCHUNK at Automate 2026, Chicago) - the "brand film" of this set, in the most common B2B format
One-sentence point: Robot + gripper suppliers that engineer together de-risk automation for customers - "the gripper is the thing that touches the part".

## Structure (cut list + English captions)
- 0.0-6.4 title card: white-to-ABB-red/lilac gradient (soft blurred blob), "The importance of gripping technology" (small, sentence case) above "SCHUNK + ABB ROBOTICS" (wide caps). Pushed off by a horizontal slide at 6.4 s.
- 6.4-20.5 two-shot on the booth (ABB marketing head + SCHUNK manager, cobots in glass cells behind, booth slogan "Hand in hand for tomorrow"); name super "Marina Bill / Global Head of Marketing & Sales, Software & Digital" (7-11 s).
- 20.5-74.5 interview intercut: two-shot from 2 angles + singles, then the first b-roll block (24-35 s, 55-62 s) - GoFa cobot with SCHUNK gripper picking and placing small parts, slow slider moves, cross-dissolves.
- 74.5-77.6 SCHUNK logo on the booth's LED wall.
- 77.6-138 more interview, b-roll blocks 77-95 s and 117-138 s: macro on the cobot's joints ("ABB" logo, green status ring, "CRB 15000" label), gripper fingers closing on a part.
- 138-148 closing single of the ABB speaker to camera ("that really shows the importance of technology collaboration... working in an ecosystem"), fade to white at ~147.8 s.
- 148-151: ABB Robotics logo on white.

## Cut rhythm
- 31 shots in 151 s (20 hard cuts from cuts2 + 11 dissolves/slides verified by eye). ASL 4.87 s, median 3.80 s. ASL per quarter 5.40 / 5.40 / 3.78 / 3.78 s.
- Longest 14.08 s (6.4, first two-shot), 13.2 s, 13.04 s (closing single), 12.44 s. Shortest 0.88 s, 0.96 s (b-roll inside dissolves).
- Interview shots 5-14 s; b-roll 1-4 s with ~0.5 s cross-dissolves; 6 % under 1 s, 55 % over 3 s.

## Typography
- Title card: wide extended geometric caps (closest free: Lexend Zetta / Michroma) ~4 % height for "SCHUNK + ABB ROBOTICS", humanist sans (closest free: Inter Light) ~2 % above it, black, top-left (x 4 %, y 25-45 %), on a red/white/lilac gradient-blob background (ABB 2026 look).
- Name super: small white sans, 2 lines (name bold ~2 %, role regular ~1.8 %), left of the speaker at chest height, no box.
- End: "ABB Robotics" logo (red ABB + black "Robotics") on white, ~4 % height.

## Colour/grade
- Natural trade-show light, clean whites and the booth's navy blue; cobots white/grey with green status LEDs; soft shallow depth of field. Title and end in white + ABB red.

## Camera/shots
- Interview: 2 cameras (wide two-shot, tighter singles), speakers standing in front of the booth so the product is always behind them.
- B-roll: slider/gimbal macro of the real cobot and gripper in a glass demo cell, shallow focus, slow lateral moves (1-3 % frame per second), close-ups of the gripper picking.
- No slow motion visible; no data overlays.

## Transitions
- Hard cuts in the interview; 0.5 s cross-dissolves in b-roll blocks; a horizontal slide from the title card; fade to white before the logo.

## Sound
- Interview dialogue + soft corporate music bed. Integrated -9.4 LUFS (loud master for a talk piece).

## What makes it credible / premium
- Two real executives, named, on the real booth, with the real product working behind them.
- Product b-roll is real macro of the actual cobot + gripper doing a pick task; the camera lingers on details ("smallest details").
- Calm: long interview shots, slow b-roll moves, dissolves.
- Weak spot: no numbers or data; the claims stay general.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Title card: `background: radial-gradient(circle at 20% 90%, #ff000f 0, transparent 45%), radial-gradient(circle at 90% 70%, #b9a7ff 0, transparent 40%), #fff; filter: blur(0)`; text `small{font:300 2vh Inter}`, `h1{font:600 4vh 'Lexend Zetta'; letter-spacing:.03em}` at left 4vw, top 25vh. Exit: `gsap.to(card,{xPercent:-100,duration:.5,ease:'power2.inOut'})` while the interview slides in.
- Name super: `font: 600 2vh Inter` + `400 1.8vh`, white, left of speaker, `gsap.from(super,{autoAlpha:0,y:6,duration:.3})`, hold 4 s.
- B-roll blocks every ~20-30 s of talk: 4-6 macro slider shots of the machine at work, 1-4 s each, 0.5 s cross-dissolves.
- End: fade to white 0.4 s, logo 3 s.
