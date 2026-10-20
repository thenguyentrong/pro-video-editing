# Success Story: Pressure-tight laser welding of aluminum cooling units with TRUMPF and HAGO  (TRUMPF, 2025-09-23, 3:40, 16:9, YouTube @TRUMPFtube)
URL: https://www.youtube.com/watch?v=jWNA7pBPj3w
Purpose: customer case film (German precision-parts maker, TRUMPF laser cell with multifocus optics)
One-sentence point: For the first time, the customer welds pressure-tight aluminium cooling units in series with a TRUMPF laser cell, BrightLine Weld and multifocus optics.

## Structure
- 0-7.2 drone over the customer's plant; a TRUMPF-blue gradient panel slides over the left 60 %: title (light, ≈9 % H, two lines) + 5-line summary + "you win" mark; 4 s of silence under the opening.
- 7.2-24 three managers walk and talk at the laser cell; first interview (head of product management) with a white name box.
- 24-50 process: TruLaser Cell 7040 wide, weld head macro with sparks, a weld-seam cross-section on a screen (≈38 s), cold blue macros of finished seams, operator at the cell.
- 50-67 second interviewee, aerial of the plant with a white fact box (company, location, employees "over 600", products).
- 67-122 production and engineering: walk-and-talks, workers, CAD on a whiteboard screen, seam close-ups, third and fourth interviewees, parts in hand.
- 122-158 technology: "TruLaser Cell 7040" on the machine (≈124-127 s), a flat explainer of the beam ("Option Multifokus + BrightLine Weld", core and ring spots, ≈144-150 s), macro of a red laser spot moving along a seam (151-158 s).
- 158-207 results and people: seam macros, apprentices ("training" wall), closing interviews, the team in a row.
- 207-212 "you win" blue end card; 212-219.5 TRUMPF logo on white (7 s silence).

## Cut rhythm
- 67 shots in 219.5 s, ASL 3.28 s, median 2.04 s, 0 % < 1 s, 30 % > 3 s, 18.3 shots/min. ASL per quarter 2.9 / 2.9 / 3.1 / 3.9 s.
- A strict 2-second grid: 43 of 65 cut-to-cut gaps are 1.9-2.1 s (e.g. 28.1, 30.1, 32.1, 35.2, 37.1, 39.0, 41.0, 43.0, 45.0 ...). Interviews run longer (4-9 s). Longest 15.7 s (end card + logo), 9.2 s, 8.1 s.

## Typography
- TRUMPF face: light humanist sans (closest free: Noto Sans Light / Open Sans Light).
- Opening panel: blue gradient (#1a1aff → transparent) over the left 60 %; title light ≈9 % H, sentence case, two lines at x ≈6 %, y ≈20-42 %; summary regular ≈3.5 % H, 5 lines; "you win" bold lowercase mark ≈7 % H bottom-left.
- Name box: white rectangle (x ≈6-66 %, y ≈75-89 %), name regular ≈4 % H black + role/company ≈2.7 % grey, one line each.
- Fact box: white rectangle top-left (≈34 % W × 38 % H), company name ≈4 %, three "›" bullet lines ≈2.8 % with bold labels; lines fade in one by one.
- Explainer: flat white/yellow drawing with labels ≈3 % H bold.
- No subtitles: German interviews without on-screen translation in this upload.

## Colour/grade
- Bright, clean, high-key factory (white walls, daylight), cool blue macros of aluminium, orange sparks; TRUMPF electric blue only in the opening panel and end card.

## Camera/shots
- Real customer site: drone, gimbal walk-and-talks of 2-3 people, interviews at 50-85 mm with soft white backgrounds, macro of the weld head, seams and sparks, operator at the HMI.

## Transitions
- Hard cuts; the opening panel slides over the drone shot; blue gradient wipe into the "you win" card; cut to white logo.

## Sound
- German interviews ≈202 s of speech (≈450 words) over a light, bright corporate track. Integrated -19.1 LUFS, LRA 6.7 LU, true peak -0.6 dBTP. 4.05 s silence at the start, 7 s at the end. Nine short drop-outs (0.3-0.55 s) between interview bites (10.4, 55.3, 59.8, 71.7, 73.7, 157.7, 175.2, 184.2, 201.9 s), each followed by a rise of +30-38 dB; biggest +38.4 dB at 24.25 s.

## What makes it credible
- Named customer, location, head-count and products on a fact box; four named people.
- Close-ups of the actual seams and a cross-section on a screen as quality proof.
- A simple explainer for the optical trick (core + ring beam).
- Weak: no number for leak rate, speed or cycle time; no subtitles for non-German viewers in the English-titled upload.

## Recipe (real footage + HTML/GSAP)
- Opening panel: `background:linear-gradient(90deg,rgba(20,20,255,.95) 0%,rgba(20,20,255,.6) 45%,transparent 70%)`, title `font:300 9vh 'Noto Sans'`, summary `400 3.5vh`; `gsap.from(panel,{xPercent:-100,duration:.8,ease:'power3.out'})`.
- Name box: `background:#fff; left:6vw; bottom:11vh; padding:2vh 3vw`, name `400 4vh`, role `400 2.7vh #666`; fade 0.3 s, hold 4-5 s.
- Cut b-roll on a 2.0 s grid (every 2 s at 25p = 50 frames), interviews 4-9 s.
- Leave 0.3-0.5 s of music silence before each new interview bite.
