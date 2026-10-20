# Unitree Introducing | Unitree A2 Stellar Explorer  (Unitree Robotics, 2025-08-05, 2:07, 16:9, YouTube @UnitreeRobotics)
URL: https://www.youtube.com/watch?v=ve9USu7zpLU
Purpose: quadruped launch film / field capability demo
One-sentence point: the A2 quadruped is tough, fast and strong enough for real terrain, and the film proves each claim with a real take and a number.

## Structure (measured; music only, no voice found)
- 0.00-0.32 thumbnail frame: A2 carrying a red bag up a forest slope, title "Unitree A2 / Stellar Hunter" (the on-screen name differs from the upload title).
- 0.32-5.84 hook stunt: A2 runs through a glass pane in a tunnel; top-left label "No Speed-Up in This Video" from ≈1 s to ≈4 s.
- 5.84-28.88 agility in a quarry cave: jumps, handstand walk, fall-and-recover, flips (5-9 s takes).
- 28.88-32.48 "Running Speed: 5 M/S" over a running take.
- 32.48-52.04 rubble, scree and a stone staircase; rocks fall around it.
- 52.04-59.72 load test: a man jumps onto the standing robot; labels "Approx. 175CM /100KG" with a dotted arrow, and "Total Weight: ~37KG" bottom-right.
- 59.72-72.80 "Climb Height: 1M" over a step-up onto a stone block, then boulder climbing.
- 72.80-89.08 steep grass slope, stairs, slope traverse.
- 89.08-95.16 "Ultra-Wide LiDAR 3D Perception": a close tracking shot, then a cyan point-cloud overlay on the real footage.
- 95.16-107.36 delivery on hotel steps with a box and a basket; carries a red bag next to a hiker.
- 107.36-121.56 ONE 14.2 s endurance sequence: chase cam behind the robot with a 30 kg weight plate on top; label "Only This Part 100+× Speed-Up"; arrow label "PAYLOAD: 30KG"; a fitness-app style route map inset top-right with a live km counter (1.21 → 12.55 km), day to night; ends on "Duration: 3h 8min / Distance: 12.55KM".
- 121.56-125.0 product on black: leg version, then wheel-leg version (render or studio, labelled "Leg Version").
- 125.0-126.9 UNITREE wordmark + disclaimer block.

## Cut rhythm
- 23 shots in 126.9 s (scene detector + 3 verified cuts added by eye at 4.56, 8.56, 45.52 s). ASL 5.52 s, median 5.32 s, 4.3 % under 1 s, 87 % over 3 s, 10.9 shots/min.
- ASL per quarter 3.97 / 5.29 / 4.53 / 6.34 s: flat. Cuts per 10 s stay at 1-4 all film long.
- Longest 14.2 s (the labelled 100x time-lapse), then 8.2 s and 8.0 s real-speed takes.

## Typography
- One grotesk throughout (closest free: Inter Medium / HarmonyOS Sans look), white, no box, soft shadow.
- Speed and section labels top-left, x ≈2 %, ≈5.5 % H cap+descender (font ≈6.5vh), sentence/title case: "No Speed-Up in This Video", "Ultra-Wide LiDAR 3D Perception".
- Spec labels: "Running Speed: 5 M/S", "Climb Height: 1M" top-left ≈5 % H; "Total Weight: ~37KG" bottom-right ≈6 % H; "PAYLOAD: 30KG" bottom-left caps ≈6 % H with a white hand-drawn style arrow to the plate; "Approx. 175CM /100KG" tracked caps ≈3.5 % H on the person with a dotted vertical measuring line.
- Result card: two lines "Duration: 3h 8min / Distance: 12.55KM" ≈7 % H each, bottom-right.
- Labels pop on and off with a fast fade (≈0.2 s); hold = the take (3-6 s).

## Colour/grade
- Natural, slightly lifted daylight; warm quarry browns, green hillsides; night street at the end. No letterbox.

## Camera/shots
- Mostly tripod or gimbal at robot height, full body in frame, 3-9 s takes; low-angle slow push for the hero stunt; chase cam for endurance.
- Real people as scale and stress: a man jumps on it, a hiker walks next to it, people at the hotel door.

## Transitions
- Hard cuts only; two short dips to black at the product cards (122.4, 124.7 s).

## Sound
- One music track: integrated -13.8 LUFS, loudness range 1.2 LU (flat), true peak +1.2 dBTP. No drop-outs, no measurable hits; no impact SFX on the stunts.

## What makes it credible
- A global speed statement in the first seconds, and the one sped-up part is labelled with its factor (100+x) and backed by a distance/time result.
- Each claim = one number + one real take where the number is visible (a 1 m block, a 100 kg man, a 30 kg plate).
- Real terrain, real falls and recoveries, real bystanders.
- Weak spots: no word on autonomy vs remote control (the stunts are almost certainly joystick-driven, the endurance walk may be too); the map inset looks like a consumer fitness-app screenshot, not the robot's own UI.

## Recipe
- Put a 6.5vh Inter 500 label top-left (`left:2vw; top:3vh`) on frame 1: "No speed-up in this video". When you speed something up, change the label for exactly that part: `tl.set(lbl,{textContent:'Only this part 100x speed-up'},t)`.
- One spec per take, written as `Label: value UNIT` (5 vh), placed in empty sky/ground; draw a 2 px arrow from the label to the object it measures.
- Stress beat: a person adds load on camera, show the person's height/weight as a small tracked caps label (3.5vh, letter-spacing .15em).
- End the field section with a result card (7vh, two lines) over the last frame of the long run.
