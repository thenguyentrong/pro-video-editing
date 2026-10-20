# The world's strongest FANUC robot | M-2000iA/2300  (FANUC Europe, 2016-06-16, 1:36, 16:9, YouTube @FANUCEurope)
URL: https://www.youtube.com/watch?v=UkZc3lIwfSM
Purpose: product launch film, filmed at a trade-fair stand (real robot lifting a car)
One-sentence point: The M-2000iA/2300 lifts 2.3 t with 3.7 m reach - strong, precise and more flexible than a crane.

## Structure
- 0-9.4 brand card: FANUC wordmark red on FANUC yellow, fades in and out in silence (0-5.7 s), model name "M-2000iA/2300" fades in black on yellow.
- 9.4-21.4 reveal: macro pass along the yellow wrist and bolts, then the robot holding a car in the dark hall; statement card "It defies / gravity" (white line + yellow line, ≈5 % H) over a darkened macro (19.6-21.4 s).
- 21.4-58.2 specs, one per shot: "it lifts up to / 2300 kg" (small white label next to the car, 24-27 s); "3.7 m horizontal reach" in a yellow box top-left + a white dimension ruler on the floor (34-41 s); "Extra strong sealed wrist" and "IP 67 protected" small yellow tags next to the wrist (43-49 s).
- 58.2-60.4 statement card "more flexible / than a crane".
- 60.4-86.3 precision: the car wheel set down onto a yellow target circle on the floor, tag "Excellent repeatability" (70-73 s); low-angle passes; end title "FANUC M-2000iA/2300" over a wide (83-86 s) after a 3.6 s silence.
- 86.3-96.3 end: FANUC logo on yellow, round "Smart · Strong · Yellow" sticker, "Push the button", URL.

## Cut rhythm
- 19 shots in 96.3 s, ASL 5.07 s, median 4.24 s, 5 % < 1 s (a 0.05 s end frame), 74 % > 3 s, 11.8 shots/min. ASL per quarter 4.0 / 6.0 / 4.0 / 4.0 s.
- Longest 10.0 s (end card), 9.4 s (brand card), 8.8 s (21.4 s: the 2300 kg shot). Shortest real shot 1.76 s.
- Flat: 1-3 cuts per 10 s all the way. The robot moves slowly in real time; the camera does the moving (slow slider, low angle).

## Typography
- Bold DIN-style sans (closest free: Barlow SemiBold / D-DIN Bold), sentence case.
- Statement cards: two centred lines ≈5 % H each, line 1 white, line 2 FANUC yellow, over a darkened (≈60 % black) macro; hold ≈2 s.
- Spec in a box: yellow rectangle top-left (x ≈3 %, y ≈5 %, ≈20 % W × 13 % H), black text 2 lines ≈4.5 % H ("3.7 m / horizontal reach"); white dimension ruler on the floor with tick marks and the value centred above (≈3 % H).
- Small spec tags: yellow box ≈6 % W with black text ≈1.5 % H, placed next to the feature (wrist, wheel) - too small at 480p.
- End title: "FANUC" yellow + model white ≈3 % H, centred, over the hero wide.

## Colour/grade
- Dark trade-fair hall, crushed blacks, yellow robot as the only saturated colour; brand cards in flat FANUC yellow (#FFD800-ish) with red logo.

## Camera/shots
- Real robot, real car, real stand. Slow slider/dolly passes, very low angles, macros of bolts and the wrist, a top-down on the wheel target. No people, no CGI.

## Transitions
- Hard cuts; fades in and out of the yellow cards; statement cards cut in over darkened footage.

## Sound
- Male VO ≈69 s (≈109 words, slow ≈1.6 words/s) over epic orchestral-electronic music. Integrated -17.0 LUFS, LRA 7.5 LU, true peak +0.1 dBTP. Silence 0-5.7 s on the logo; a 4.55 s drop-out at 81.95 s before the end title (biggest rise after it); short 0.4-0.6 s gaps at 89.7 s. Biggest rise +25.6 dB at 15.75 s (reveal of the car).

## What makes it premium / credible
- The claim is shown live: a real 2.3 t robot holding a real car.
- One spec per shot, with a physical reference (ruler on the floor, target circle under the wheel).
- Brand colour discipline: yellow robot, yellow cards, yellow graphics.
- Weak: no speed or cycle-time number; tiny tags unreadable on phones.

## Recipe (real footage + HTML/GSAP)
- Statement card: dark overlay `rgba(0,0,0,.6)` on a macro; two lines `font:600 5vh Barlow`, first `#fff`, second `#FFD800`; `gsap.from(lines,{y:20,autoAlpha:0,stagger:.15,duration:.4})`, hold 2 s.
- Spec box: `background:#FFD800; color:#000; left:3vw; top:5vh; padding:1.5vh 1.2vw; font:600 4.5vh Barlow`; ruler = SVG line with ticks every 2 % W across the floor, draw `scaleX` 0→1 in 0.8 s from the base of the machine.
- Target circle: SVG ellipse in yellow under the load, `stroke-dashoffset` draw 0.6 s right before the load touches down.
- Open and close on flat brand-colour cards with silence under the opening logo.
