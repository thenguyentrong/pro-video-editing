# How Zipline Delivers with Platform 2  (Zipline, 2025-04-04, 0:59, 16:9, YouTube @FlyZipline)
URL: https://www.youtube.com/watch?v=airEzThGlx8
Purpose: product process demo (how it works, step by step)
One-sentence point: one real order is followed from the phone to the store, the dock, the sky and the customer's yard.

## Structure (no voice, no captions after the title)
- 0.0-2.5 title over a wide of the dock towers: three lines of bold condensed type, right half.
- 2.5-5.3 order: a hand holding a phone with the order app (real UI).
- 5.3-9.6 store: a staff member in a high-vis vest picks items, packs a bag.
- 9.6-15.3 the dock: tower array; the drone parked on its tower from below.
- 15.3-23 loading: the bag goes into the delivery droid hanging from a numbered tower (5.3 s shot), the staff member checks the phone.
- 23-33 take-off: the drone leaves the tower from below, a fly-past, the site at dusk, departure over the town.
- 33.2-45.8 flight: the drone small in the sky over the suburbs (4.2 and 4.7 s held shots).
- 45.8-52.4 delivery: aerial of a house, the droid lowered on a tether into a yard, the package released (6.6 s, the longest shot).
- 52.4-56.6 return: the drone climbs into the sun.
- 56.6-59.1 logo on brand red.

## Cut rhythm
- 23 shots in 59.1 s (adaptive detector; all extra cuts checked by eye). ASL 2.57 s, median 2.42 s. ASL per quarter 1.64 / 2.11 / 2.46 / 3.70 s.
- 4 % under 1 s, 26 % over 3 s. Cuts per 10 s: 6, 3, 5, 4, 2, 2. Calm and even; the shots get longer as the drone gets closer to the customer.

## Typography
- Title only: condensed bold, sentence case, ≈7 % H per line, 3 lines, left-aligned in the right half (x ≈60 %, vertically centred). Closest free: Barlow Condensed 700.
- End: logo mark + wordmark white on brand red, centred, ≈7 % H.

## Colour/grade
- Natural daylight, clear blue sky, white hardware with brand red/orange accents. No grade effects.

## Camera/shots
- All real: handheld at human height in the store, low angles under the dock, long lens on the drone in the sky, aerial over the house, ground-level in the yard.

## Transitions
- Hard cuts; a hard cut to the solid red end card.

## Sound
- No voice. Light rhythmic music, hits every ≈2.5 s from 22 s on (22.25, 24.75, 27.25 ...). Integrated -20.0 LUFS, LRA 4.1 LU, true peak -6.7 dBTP. Ending: button.

## What makes it premium
- One continuous job told in order, every step real, no explanation needed.
- The longest shot is the delivery itself, in one take.
- The real app UI starts the story.

## Recipe (real footage + HTML/GSAP)
- Shoot one real job in order: phone (3 s), pick (4 s), dock (5 s), load (5 s), take-off (2-3 shots), flight (two 4-5 s holds), delivery (one 6-7 s take), return (3 s).
- Title: Barlow Condensed 700 7vh, 3 lines, `left:60vw; top:50%; transform:translateY(-50%)`, fade 0.3 s, hold 2 s.
- Cut on every second music hit (≈2.5 s); end on a solid brand-colour card with a button.
