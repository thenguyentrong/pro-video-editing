# YFQ-44A: The Road to First Flight  (Anduril, 2026-02-23, 3:12, 2.39:1 letterbox in a 16:9 upload, YouTube @Anduril)
URL: https://www.youtube.com/watch?v=vhczBn2Yu-8
Purpose: field-proof mini documentary (milestone film)
One-sentence point: an uncrewed fighter went from contract to first flight in a stated number of days, and the film shows the build, the ground station and the real flight.

## Structure
- 0.0-8.8 cold open: black, runway markings, an operator silhouetted at a ground control station, macro of a status word on a screen. Real radio traffic (tower and aircraft call-signs) is the only sound until ≈25 s.
- 8.8-23.2 context on black: two short text cards in a two-column layout (date + customer + mission; then the task in one sentence). Black holds of 5.0 s and 4.4 s.
- 23.2-29.6 the aircraft at dusk on the runway; runway POV.
- 29.6-31.4 0.9 s drop-out, then the biggest hit (+41 dB at 31.0) into an intake macro.
- 31.4-56 build montage (densest: 17 cuts in 40-50 s): code terminal, CNC machining, composite parts, landing-gear test, engineers' hands, terminal words typed in macro (a standby state, then ready), an Enter key.
- 55-58.6 date card: day + the words "day of first flight" in two columns.
- 58.6-86.9 pre-flight: hangar reveal, ground station, a finger pressing the real takeoff-confirm button on a touchscreen, taxi.
- 86.9-96.1 take-off roll in one 9.26 s shot (the longest).
- 96-105 program emblem; a four-part claim super laid over the flying aircraft (time from clean sheet to flight + comparison).
- 105-166 flight montage: formation with a chase jet, landing, a super stating the aircraft is now flying, a multiple-flights super, the mission-route screen.
- 166-170.4 logo on black.
- 170.4-191.9 epilogue: black-and-white footage in a small centred window (≈45 % frame width): the team watching, applause, embraces; then the aircraft far away.

## Cut rhythm
- 111 shots in 191.9 s (adaptive detector, one false cut removed by eye). ASL 1.73 s, median 1.33 s. ASL per quarter 1.50 / 1.85 / 1.37 / 2.28 s.
- Longest 9.26 s (take-off roll), 6.63 s, 5.0 s (black text card). 36 % of shots under 1 s, 15 % over 3 s.
- Cuts per 10 s range from 2 (text cards, take-off) to 17 (build montage). Rhythm = documentary: fast in process, long at the moment of proof.

## Typography
- Text cards and supers: grotesk 500, sentence case, ≈4.5 % of picture height, white; two columns (left at x ≈6 %, right at x ≈52 %); the sentence is split across the columns and words arrive one by one. Closest free: Inter 500.
- Date card: same face, ≈3.5 %, date left, label right, on black or over a dark hangar door.
- UI words: monospaced terminal text filmed as macro (≈18 % H) with a blinking cursor. Closest free: JetBrains Mono.
- Claim supers over flight: same two-column grid, four fragments, ≈3.5 %.

## Colour/grade
- Cool blue-grey interiors, warm amber dusk and desert exteriors; desaturated, filmic, letterboxed 2.39:1. Epilogue in black and white.

## Camera/shots
- Real throughout: long-lens tracking of the aircraft, runway POV, gimbal in the factory, macro on screens and keys. Operator and screens appear before every flight beat.

## Transitions
- Hard cuts; fades to black text cards; the epilogue shrinks the picture into a window.

## Sound
- Real radio traffic as the cold-open voice (no narrator); music after ≈25 s.
- Integrated -12.4 LUFS, LRA 9.2 LU, true peak +0.5 dBTP. Drop-outs: 29.8-30.7 (then +41 dB hit), 169.3-171.5 (between logo and epilogue). Ending: fade.

## What makes it premium
- The proof moment (take-off) is the longest shot.
- Human control is shown on screen (operator, button, route screen) right before the machine acts.
- Dates and day counts make the claim checkable.
- The quiet black-and-white epilogue after the logo lets the team, not the brand, end the film.

## Recipe (real footage + HTML/GSAP)
- Cold open with 8-10 s of real radio or control-room audio over dark shots; no music.
- Text cards: `font:500 4.5vh Inter`, a 2-column CSS grid (6vw / 52vw), each word `gsap.from({autoAlpha:0}, 0.15 s, stagger 0.12)`; hold the full card 2 s.
- Put 1 s of silence before the first big reveal; land the hit on the cut.
- Show screen + hand + button for 2-3 s before the machine moves; hold the proof take 8-10 s uncut.
- After the logo: 15-20 s black-and-white epilogue in a `width:45vw` centred box, music low.
