# Welcome to Robot Park, where Apptronik is building the future with Apollo 2  (Apptronik, 2026-06-30, 1:14, 16:9, YouTube Apptronik)
URL: https://www.youtube.com/watch?v=iPyxwELiD9Q
Purpose: brand + second-generation launch film (Apollo 2, the company's new site)
One-sentence point: Apollo 2 is a friendly, ready-to-work humanoid built for people, already tested at a carmaker and in warehouses.

## Structure (studied from the sheet and metrics)
- 0.0-4.1 dream hook: a child in a space helmet reaches for a holographic light (0-2.5 s); kids in a classroom look at a robot hand model (2.5-7.7 s).
- 7.7-13.9 the product: macro of Apollo 2's torso; its hand opens (8-11 s); the chest display shows a status screen (NET / BAT 87 % / ID / VER / SYS Pass, 12 s) then "Planning Task …" with a spinner (13 s).
- 13.9-23 the place and people: Apollo walks through an open-plan office between staff at desks (14-17 s); low leg shot and a person's legs (18-19 s); a presenter beside Apollo on a mobile base (20-22 s); front close-up (23-24 s).
- 24-43 work: test cells with orange posts (25-29 s); two Apollos in a lobby; robots carrying totes (32-33 s); chest display "Picking" with session ID, duration and progress % (34 s); a picking cell (35 s); a carmaker's logo banner beside Apollo at an assembly-like frame (36-37 s); Apollo with staff and an engineer seated in the office (38-43 s).
- 43-60 hero: lights come on in a dark warehouse aisle (44-46 s); close-ups of head and hands picking from shelves (47-53 s); Apollo pushing a cart (53-55 s); wide fleet in a warehouse (56-57 s); walking towards camera down an aisle (60 s).
- 60.8-63.9 portrait: Apollo between vertical light bars.
- 63.9-74.3 end: black, "Robots for humans." (64-68 s), then the symbol (69-74 s).

## Cut rhythm
- 34 shots in 74.3 s (scene detector + 2 verified adds at 18.35 and 19.48). ASL 2.19 s, median 1.88 s; per quarter 2.32 / 1.69 / 1.55 / 3.1 s (end card). 2.9 % under 1 s, 27.5 shots/min.
- Cuts per 10 s: 3 / 5 / 5 / 6 / 5 / 7 / 2 - accelerates towards the warehouse hero, then the 10.4 s end card.
- Longest content shot 3.8 s (8 s, hand macro). No proof take.
- 48-52 % of cuts on an audio onset (chance 24 %): cut to music.

## Typography
- Only the end line: "Robots for humans." light grotesk, sentence case with full stop, white on black, ≈5 % H line, centred; hold ≈4.5 s. Closest free: Inter Light.
- In-picture text: the robot's own chest display (≈5-10 % H in close-ups) with status, task name ("Planning Task", "Picking"), session ID, duration and progress %. This is the film's way to show the machine's mind. Office wall posters repeat "ROBOTS FOR HUMANS".
- No supers, no captions, no speed or autonomy labels.

## Colour/grade
- Warm, filmic: amber practicals, shallow depth of field, soft contrast; the white robot with black face plate pops. Warehouse hero in dark tungsten with white light bars. Mean luma 0.28.

## Camera/shots
- Cinema look: macro slider moves, shallow focus, gimbal follows, low leg shots, symmetrical aisle wides.
- People throughout (kids, staff, an engineer, a presenter); a fleet wide for scale; the carmaker logo as social proof.
- Real robots; whether the moves are autonomous or teleoperated is not stated.

## Transitions
- Hard cuts; light-on in camera at 44 s; fade to black for the end line.

## Sound
- Music-led with possible voice (a presenter gestures on camera; not transcribed). Integrated -17.0 LUFS, LRA 6.7 LU, true peak -4.9 dBTP. Drop-out 3.25-4.0 s (0.75 s, -49 dB floor) right before the cut from the kids to the robot, then a rise; biggest hit +22.7 dB at 31.5 s. Silence at the end 73.6-74.25 s.

## What makes it premium
- Human-first story (kids, coworkers) and one line of brand promise at the end.
- The chest screen as a diegetic UI: the robot shows its own state, no graphics overlay needed.
- Lighting reveals (lights on in the aisle) and a symmetric hero portrait.

## What it does not prove
- No shot longer than 3.8 s of real work, no speed or autonomy label, no named site in text (only a logo banner).

## Recipe (real footage + HTML/GSAP)
- Beat sheet: dream (5 %) → product macro (8 %) → people + place (13 %) → work montage (25 %) → hero in light (25 %) → portrait (4 %) → end line (14 %).
- If your machine has a screen, film it in macro showing real states; otherwise build a chest-style status card: `font:600 3vh Inter`, labels 1.2vh caps grey, values white, on a rounded black panel, progress % counting with `gsap.to(obj,{v:26,snap:'v'})`.
- End line on black: Inter 300 5vh, fade in 0.6 s, hold 4 s, then logo 5 s.
