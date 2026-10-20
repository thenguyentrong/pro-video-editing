# Conference Room Mess Cleanup Test: Unitree WVLA 2.0 Model  (Unitree Robotics, 2026-05-25, 3:31, 16:9, YouTube @UnitreeRobotics)
URL: https://www.youtube.com/watch?v=zqqIpVsMYkE
Purpose: capability demo / AI-model test (research-style proof video)
One-sentence point: Unitree's own vision-language-action model lets a humanoid tidy a messy meeting room by itself in one long uncut run.

## Structure (measured)
- 0.00-0.32 thumbnail frame: robot + a staff member at the table, title "Conference Room / Mess Cleanup Test / Unitree WVLA 2.0 Model".
- 0.32-209.16 ONE take of 208.8 s, shown as a split screen:
  - left ≈61 % of the frame: handheld third-person camera that follows the robot around the room;
  - right ≈39 %: two rows of two robot camera feeds (head and wrist cams) with live terminal logs between them (policy step, action vectors, "inference latency" in ms).
  - Tasks in order: pick up pens and a remote from the table, straighten chairs, face a TV wall, carry rubbish to a bin (100 s: a staff member moves the bin while the robot approaches = disturbance), wipe/clear a side table, fetch bottled water from a carton (≈140-155 s), tidy brochures, push chairs in.
- 209.16-211.4 UNITREE wordmark + disclaimer card.

## Cut rhythm
- 3 shots in 211.4 s: thumbnail, one 208.8 s take, end card. ASL 70.5 s (all detectors agree, both on the full frame and on a crop of only the left pane: 0 cuts inside the take; the room changes were checked by eye and are camera walks, not cuts).
- 0.9 shots/min. This is the purest one-take proof in the library after BD's Atlas hands-on.

## Typography
- Title frame only: rounded geometric sans (closest free: Poppins SemiBold), sentence case, white-to-lilac gradient, ≈8 % H for the two title lines, ≈6 % H for the model name, right-aligned over a dark gradient on the right half.
- During the take: no captions, no labels, no speed badge. The only text is the real terminal log (monospace ≈1.5 % H, green/white on black) inside the right panel.

## Colour/grade
- Ungraded office daylight, white walls, light wood tables; the right panel is black. 16:9, no letterbox.

## Camera/shots
- One handheld operator following at 1.5-3 m, framing the whole robot plus the task; the robot cameras show its own view of the gripper and object.
- Staff members stay in the room: one hands objects, one moves the bin.

## Transitions
- None inside the take.

## Sound
- Upbeat music bed over the whole run (integrated -9.9 LUFS, loudness range 3.9 LU, true peak +4.8 dBTP: clipped). No room tone audible as a layer; no voice.

## What makes it credible
- 208.8 s without a cut, with the robot's own camera feeds and running inference logs on screen at the same time: "show the machine's mind" in its most literal form.
- A person disturbs the scene (moves the bin) and the robot adapts.
- Weak spots: no statement of playback speed (no "1x" label), no explicit "autonomous" label, no mention whether any step was assisted; the terminal could be a replay, nothing on screen proves sync. Music hides the real motor and contact sounds.

## Recipe
- Split screen: `grid-template-columns: 61fr 39fr`; right side = 2x2 grid of robot/sensor feeds (each 16:9, 0.5vw gap) with a real log panel (`font: 400 1.5vh 'JetBrains Mono'; color:#9f9`) between the rows.
- Record the third-person camera and the robot streams at the same time; sync them by a clap or LED flash, and keep one uncut take of the whole task (2-4 min).
- Add what this film lacks: a fixed corner label "1x · autonomous" (Inter 600, 2vh, bottom-right of the left pane) and real room sound under a quiet bed (-18 LUFS music, contact sounds on top).
