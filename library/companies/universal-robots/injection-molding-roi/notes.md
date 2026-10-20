# Injection molding with collaborative robots realizes ROI in 1,500 hours  (Universal Robots, 2025-10-20, 3:10, 16:9, YouTube @UniversalRobotsVideo)
URL: https://www.youtube.com/watch?v=wjSuYvGwz1Y
Purpose: customer case film (US family-owned injection-moulding shop, cobots tending machines)
One-sentence point: A third-generation moulding shop put UR cobots on its machines, paid them back in about 1,500 hours and now runs parts unattended.

## Structure
- 0-2 drone over the shop's building in trees (no title card).
- 2-24 company: owner/manager interview with the cobot behind him, hand-guiding a cobot, building sign, a framed family certificate in macro, walk through the hall.
- 24-47 the problem: products (coloured moulded parts), old-style automation, interview.
- 47-105 the cobots: cobot at a blue moulding machine taking parts, line of five machines with cobots (68 s), production staff and engineer interviews, boxes of finished parts.
- 105-160 results and people: engineer interview, operator packing parts ("over 600 days" in the subtitle), programming on a PC and on the teach pendant, two colleagues talking at a cell.
- 160-182.6 closing: interviews, wide of the machine line.
- 182.6-190.4 UR logo + line on dark teal, 7.8 s.

## Cut rhythm
- 68 shots in 190.4 s, ASL 2.80 s, median 2.49 s, 0 % < 1 s, 37 % > 3 s, 21.4 shots/min. ASL per quarter 2.4 / 2.8 / 2.5 / 3.2 s.
- Even pulse of 2-5 cuts per 10 s from start to end; many b-roll shots are exactly 2.0 s or 3.0 s (148.5-152.5 s: four cuts 2.0 s apart). Longest 7.8 s (end card), 6.9 s, 5.4 s. Shortest 1.0 s.
- Interview pieces 3-7 s, b-roll 2-3 s.

## Typography
- Only burned-in subtitles: humanist sans (closest free: Open Sans / Noto Sans), regular, white, ≈4 % H, bottom centre (y ≈88-93 %), one or two lines, soft shadow, no box. They carry every spoken line, including the numbers.
- No name supers, no title card, no data card; the ROI number lives only in the upload title and the subtitles.
- End card: UR logo white + small line ≈1.5 % on dark teal (#0b3540-ish).

## Colour/grade
- Natural, slightly cool documentary look; blue moulding machines, grey cobots, orange/red product colour accents.

## Camera/shots
- Real site only: drone exterior, gimbal walks, slider moves along machines, macro of parts and the certificate, handheld over-the-shoulder at PC and pendant. Interviews at 35-50 mm, subject off-centre with machines behind.

## Transitions
- Hard cuts, one dissolve into the certificate macro (≈12 s); cut to the end card.

## Sound
- Interviews ≈180 s of speech (≈524 words, ≈2.9 words/s) over a light acoustic/corporate bed. Integrated -20.3 LUFS (quiet), LRA 8.3 LU, true peak 0.0 dBTP. One 0.55 s drop-out at 78.15 s, then the biggest music rise (+40.8 dB at 79.0 s). 4.35 s silence under the end card.

## What makes it credible
- Real shop, real owner and staff, cobots in daily use on several machines.
- Payback number said by the customer and in the upload title.
- Weak: no names or roles on screen, no number card, no long take of one tending cycle (longest b-roll ≈5 s).

## Recipe (real footage + HTML/GSAP)
- Subtitles: `font:400 4vh 'Open Sans'; color:#fff; text-shadow:0 1px 3px rgba(0,0,0,.8); bottom:5vh; text-align:center; max-width:70vw`, one phrase per card, cut with the speech.
- Cut grid: b-roll at 2.0 or 3.0 s, interview bites 3-7 s, 2-5 cuts per 10 s.
- Add what it lacks: a name super for each speaker, a big number card when the ROI is said (`font:700 12vh Montserrat` "1,500 h" + `400 3vh` "to payback"), and one 10-15 s locked take of a full cycle.
