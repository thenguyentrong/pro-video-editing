# Optimus Navigating Around | Tesla  (Tesla, 2024-10-18, 1:24, 16:9, YouTube @tesla)
URL: https://www.youtube.com/watch?v=DrNcXgoFv20
Purpose: robot demo / progress update (capabilities + how they work)
One-sentence point: Optimus now navigates unseen spaces, docks to charge, carries 11 kg and hands out items - all autonomous, learned by one neural net, and every speed-up is labelled.

## Structure (cut list + on-screen captions; no voice, music only)
The captions form one running sentence across shots (they end with commas and continue in the next shot).
- 0.0-4.8 "Optimus' walk has become more confident" - real factory floor, robot walking past robot cells. Badge "AUTONOMOUS".
- 4.8-13.5 "It can now explore unseen spaces autonomously, / avoiding people and obstacles using neural nets running on its computer" - badge "AUTONOMOUS 2X"; a round-masked mini-map in the bottom-right shows the robot's path (blue) and goal (green).
- 13.5-18.5 "all while capturing visual cues specific to its environment" - the robot's own fisheye camera view, vignetted, badge "AUTONOMOUS".
- 18.5-25.7 "Together, multiple bots build a shared understanding of their surroundings / which they can later tap into for navigation" - a 3D point-cloud map on black, with 4 small live camera feeds of different robots stacked on the right.
- 25.7-34.3 "Optimus can locate & navigate to the nearest charging station, / dock itself precisely using its rear camera only," - wide with mini-map, then split screen: real robot docking (left 2/3) + a grey panel with a 3D robot model and the rear-camera view with green tracked markers (right 1/3).
- 34.3-51.2 "and head back to work later on / It can now also pick up significant payloads, such as this 11kg battery tray / and carry it around autonomously without overheating" - badge "AUTONOMOUS 8X" (37-39 s), split screen with the head-camera view (40-43 s), "AUTONOMOUS 2X".
- 51.2-56.3 "Optimus is also now venturing on non-flat terrain!" - stairs, with a cyan 3D perception mesh of the stairs and feet in the corner (54-55 s).
- 56.3-78.9 ONE 22.6 s shot: "We've trained its AI to interact with people / It can react to unsafe behaviors / and hand out different items upon request / These new skills are all learned by a single neural net / also running in real-time on Optimus' embedded computer" - real crowd of employees, robot hands out drinks from a cart; badges "AUTONOMOUS 2X" then "AUTONOMOUS 10X" (71-78 s).
- 78.9-83.6 Tesla "T" logo on black.

## Cut rhythm
- 14 shots in 83.6 s. ASL 5.97 s, median 4.79 s. ASL per quarter 5.22 / 3.48 / 4.18 / 10.45 s.
- Longest 22.62 s (56.29, people interaction), 8.67 s, 7.21 s, 6.46 s. Shortest 2.08 s, 2.21 s. 0 % under 1 s, 71 % over 3 s.
- Shot length follows the caption: one caption line (or sentence part) per 2.5-5 s.

## Typography (data on screen)
- Captions: Tesla's geometric sans (Gotham-like; closest free: Montserrat Regular or Inter), white, sentence case, ~3 % frame height per line, max 2 lines, bottom-left (x ~5 %, y ~83-88 %), soft shadow only. They type on letter by letter (half-written lines visible at 3 s and 18 s) and fade out.
- Speed/autonomy badge: "AUTONOMOUS" / "AUTONOMOUS 2X" / "8X" / "10X", tracked caps, white on a dark translucent rectangle, ~2.5 % height, top-right corner, changes with every speed change.
- Data panels: round-masked mini-map (bottom-right, ~25 % width, soft edges), 3D point cloud full frame, 4 live camera feeds stacked right (~11 % width each), split-screen grey panel with a CAD-style robot model and the camera image with green tracked markers, cyan perception mesh.

## Colour/grade
- Neutral, bright factory/lab white; panels in grey/black with brand-neutral accents (blue path, green goals and markers, cyan mesh).

## Camera/shots
- Real footage: gimbal medium-wide shots following the robot, the robot's own cameras (fisheye head cam, rear dock cam), one long static shot of a crowd interaction. Lots of real people and real clutter.
- Speed: openly sped up (2x, 8x, 10x) with the label on screen; no slow motion.

## Transitions
- Hard cuts; split screens and full-frame data views are inserted as their own shots.

## Sound
- Upbeat electronic music, no VO, no robot sound. Integrated -9.9 LUFS (loud). Hits around 47.5-52.65 s (stair section).

## What makes it credible
- Every speed-up is labelled (AUTONOMOUS 2X / 8X / 10X) - the edit admits what it changes.
- "How it works" is shown, not claimed: robot camera views, shared point-cloud map, docking markers, perception mesh.
- One sentence of plain-language captions explains each capability in order.
- A 22.6 s unbroken shot with a real crowd for the human-interaction claim.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Badge: `<div class="badge">AUTONOMOUS 2X</div>` `top:4vh; right:4vw; padding:.6vh 1vw; background:rgba(0,0,0,.55); font: 500 1.9vh Inter; letter-spacing:.1em; color:#fff`. Update the text with `tl.set(badge,{textContent:'AUTONOMOUS 8X'}, t)` exactly at each speed change (`video.playbackRate` changes in the same frame).
- Captions: `left:5vw; bottom:10vh; max-width:40vw; font: 400 3vh Montserrat; line-height:1.3`; typewriter in (0.03 s per character), hold, fade .3 s; end lines with commas when the sentence continues on the next shot.
- Mini-map: an `<svg>` of the site plan inside a `div` with `mask-image: radial-gradient(circle, #000 55%, transparent 75%)`, path drawn with `stroke-dashoffset` synced to the robot's walk.
- Split screen: 2/3 real footage + 1/3 grey panel (`#3a3a3a`) with the sensor/camera view and green tracked dots.
- For a construction robot: badges "AUTONOMOUS 4X", captions like "It finds the next wall from the BIM model, / lays the course, / and checks it with its laser scanner."
