# How KUKA Robots Are Reinventing the Touchless Car Wash  (KUKA Group, 2026-10-06, 4:09, 16:9, YouTube @KUKARobotGroup)
URL: https://www.youtube.com/watch?v=vg9ycuJRXag
Purpose: customer case film (US car-wash start-up + integrator, KUKA arms with 3D vision)
One-sentence point: A car-wash company uses KUKA robots and 3D vision to wash every car along its own shape, faster and more precisely than brushes.

## Structure
- 0-4.6 title card over the real wash bay: white translucent panel (KUKA logo, title, two-line summary), robots and a car behind it.
- 4.6-28.9 customer founders: CEO/co-founder interview with name super, aerial of the new building, robots washing; 2.0-2.3 s b-roll shots between talk.
- 28.9-90 how it works: co-founder (operations) super, the two walking through the bay, robots following the car shape, close-ups of nozzles and spray, real 3D-vision screen on a monitor.
- 90-100 spec card: white list panel "KR CYBERTECH" + five rows (speed/path accuracy, compact design, max payload 35 kg, max reach 2,013 mm, repeatability ±0.03 mm), rows slide in one by one over a wash shot.
- 107-145 integrator section: integrator engineers with supers, the vision software on screen, a "CAUTION / robots at work" sign on the building (141 s), a second small list card ≈133-136 s (≈ from the sheet).
- 145-226 results and future: customers' cars, staff with the teach pendant, reveal of the customer's building sign, founders together outside, closing lines.
- 226.99-230.76 KUKA logo on white; 230.76-249.5 KUKA brand ident (18.7 s).

## Cut rhythm
- 94 shots in 249.5 s. ASL 2.65 s, median 2.35 s, 0 % < 1 s, 16 % > 3 s, 22.6 shots/min. ASL per quarter 2.5 / 2.5 / 2.2 / 3.5 s.
- Very even pulse: 3-5 cuts in every 10 s window from 0 to 220 s; only the ident is longer (18.7 s). Longest edit shots ≈5.0 s (45.9 s, 28.9 s). Shortest 1.40 s.
- Interviews are cut into 2-3 s pieces with b-roll in between; the talk runs continuously underneath.

## Typography
- Humanist sans throughout (KUKA corporate face; closest free: Source Sans 3 / Fira Sans).
- Title card: translucent white panel (≈67 % W × 33 % H, x ≈8 %, y ≈50 %), KUKA wordmark orange ≈4 % H, title semi-bold dark grey ≈4 %, summary regular ≈3.3 %, two lines; KUKA ring icon top-right of the panel.
- Name super: white box right of the speaker (x ≈60-89 %, y ≈63-86 %), name orange semibold ≈4.5 % H, role + company grey ≈3 %, two lines; hold ≈4 s.
- Spec list: white panel, header caps semibold ≈4 % ("KR CYBERTECH"), each row a separate white bar ≈8 % H with ≈3.3 % text and a 1 px gap, rows push in from the left one after another (≈0.3 s each).
- Constant KUKA ring icon bug top-right (≈7 % H, white) on every shot.

## Colour/grade
- Bright, cool, slightly lifted documentary grade; white wash bay, orange robots, blue customer shirts and building. Soft daylight interviews with shallow depth of field.

## Camera/shots
- Gimbal and slider, real location only. Interview two-shots walking, singles at 50-85 mm; wide symmetric shots down the wash tunnel; macro of spray and nozzles; aerials of the building; screen inserts of the vision UI.

## Transitions
- Hard cuts; a few short dissolves (≈47-49 s, 112-118 s); fade to the white logo card.

## Sound
- Interview voices wall to wall (≈220 s of speech, ≈730 words, ≈3.3 words/s) over a light, steady corporate bed with machine and water sound mixed under. Integrated -16.5 LUFS, LRA 4.9 LU (very flat), true peak +0.3 dBTP. One drop-out 0.3 s at 103.5 s. Rises +20-26 dB on b-roll entries (130.1, 183.8 s). Cuts slightly favour onsets (62 % vs 53 % chance).

## What makes it credible
- Named customer, named integrator, real site, the founders talk in their own bay.
- Spec numbers with units on a clean list card (payload 35 kg, reach 2,013 mm, repeatability ±0.03 mm).
- Real vision software on a real monitor.
- Weak: no long take of a full wash cycle (longest edit shot ≈5 s), no time or throughput number on screen.

## Recipe (real footage + HTML/GSAP)
- Title panel: `background:rgba(255,255,255,.85); left:8vw; top:50vh; width:67vw; padding:4vh 3vw`; logo 4vh, title `600 4vh 'Source Sans 3'`, summary `400 3.3vh`; fade in 0.5 s, hold 4 s.
- Name super: `background:#fff; right:11vw; bottom:14vh; padding:2vh 2vw`; name `600 4.5vh` in `#FF5800`, role `400 3vh #555`; `clip-path:inset(0 0 0 100%)` → `inset(0)` 0.4 s.
- Spec list: header bar + one `div` per spec (`height:8vh; margin-bottom:1px; background:#fff`), `gsap.from(rows,{x:-40,autoAlpha:0,stagger:.3,duration:.35})`.
- Cut talk into 2-3 s pieces with b-roll on top; keep 3-5 cuts per 10 s; add one 10-15 s uncut wash cycle that the original lacks.
