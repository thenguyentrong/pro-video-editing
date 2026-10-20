# Tesla Optimus - style

Examples (official @tesla uploads):
| Example | Date | Length | Shots | ASL | Median | Sub-style |
|---|---|---|---|---|---|---|
| [optimus-gen-2](optimus-gen-2/notes.md) | 2023-12 | 1:43 | 22 | 4.69 s | 4.50 s | version reveal with feature captions + tactile HUD |
| [optimus-navigating-around](optimus-navigating-around/notes.md) | 2024-10 | 1:24 | 14 | 5.97 s | 4.79 s | capability update, speed badges, data panels |
| [tesla-bot-sort-and-stretch](tesla-bot-sort-and-stretch/notes.md) | 2023-09 | 1:18 | 11 | 7.07 s | 7.50 s | one task explained, subtitle captions, robot POV |

## The Tesla "engineering update" look
- **Real footage, long shots** (median 4.5-7.5 s, 0 % under 1 s): the viewer can judge the motion.
- **Captions instead of VO**: plain sentences, one claim per shot, small (1.8-3 % height), white Gotham-like sans, no boxes. Sort & Stretch = subtitle bar at the bottom; Navigating = 2-line caption bottom-left that types on and runs as one sentence across shots; Gen 2 = caption in the empty third next to the robot, lines added one by one.
- **Honesty labels**: "1.5x Speed", "AUTONOMOUS", "AUTONOMOUS 2X / 8X / 10X" in the top-right corner, changed at each speed change.
- **Show the machine's mind**: robot camera POV in rounded insets, cyan virtual arm aligned to the real arm, tactile pad HUD that lights on contact, point-cloud map from several robots, docking markers, stair mesh, mini-map.
- **Music only**, upbeat electronic, -9.9 to -14.9 LUFS; cuts loosely on bars (Sort & Stretch: every 2 bars = 7.5 s; Gen 2: macro section on a 1.375 s grid).
- **End**: Tesla "T" on black 4-5 s; sometimes a light-hearted extra (dance, yoga) after or before it.

## Credibility toolkit (most relevant for a construction-robot startup)
1. Locked-off or gimbal medium-wide with the whole machine + task in frame, 5-10 s per shot.
2. A person disturbs the task; the machine recovers ("dealing with the dynamic reality of our world").
3. A speed badge whenever footage is sped up.
4. One "how it works" view per capability (sensor view, map, overlay), clearly labelled as the machine's view.
5. Measurable claims in captions: "11kg battery tray", "30% walk speed boost", "10kg total weight reduction".

## Recipe (real footage + HTML/GSAP)
- Caption: Montserrat 400, 1.9-3vh, white, bottom-left or bottom bar; typewriter at 0.03 s/char; one sentence split over shots with commas.
- Badge: `AUTONOMOUS 4X`, Inter 500 1.9vh, letter-spacing .1em, `rgba(0,0,0,.55)` box, top-right; `tl.set` its text in the same frame as the `playbackRate` change.
- Data views: POV inset with 2.5vh radius on black; overlays in one cool accent (cyan/blue/green); a mini-map with a radial mask.
- Timeline: 1 caption per shot, shot = 2 musical bars; logo 4 s; optional 8 s humour tag.
