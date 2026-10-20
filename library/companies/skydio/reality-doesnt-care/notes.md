# Reality Doesn't Care  (Skydio, 2026-09-17, 1:00, 16:9, YouTube @Skydio)
URL: https://www.youtube.com/watch?v=sEyGH8XQXZ8
Purpose: mission manifesto / recruiting film
One-sentence point: building autonomous drones is hard because the real world is unforgiving, and the company asks people to join the work.

## Structure
- 0.0-7.4 hook: very fast fragments (0.2-0.6 s): sensor visualisation, soldering, a flight-path wireframe, a city map, an engineer at a bench, a heat-map, factory staff.
- 7.4-10.1 title line: a dispatcher at a 911 console; the film's title phrase appears small, centred, word by word.
- 10.1-28 the anaphora list (one hard fact per line): police with a drone, the dock in rain and snow, night flights, a heat test, the factory floor with 360 fish-eye whips, a roof with no elevator (drone carried up), field installations.
- 28-41 customers: police body-camera footage (with the camera's own timestamp burn-in), a cliff rescue, a soldier, an officer giving a thumbs-up to the drone.
- 41-51.7 the hard part: indoor flight test through a narrow tube, an engineer testing, flight test hall, robot arm; the title line again over an employee.
- 51.7-55 people: three employees at a field test; one gets a name + role super.
- 55-60.0 end: two-word call to join on black, then the logo + careers URL.

## Cut rhythm
- 55 shots in 60.0 s (scene detector + 2 cuts added, 1 removed by eye). ASL 1.09 s, median 0.77 s. ASL per quarter 0.68 / 0.94 / 1.25 / 1.88 s.
- 64 % under 1 s, 4 % over 3 s. Cuts per 10 s: 15, 11, 10, 9, 8, 1. Steady slow-down from the fastest open to one long people shot (8.4 s).

## Typography
- Title line: grotesk 500, sentence case, ≈2.2 % H, centred, white; words appear one by one in sync with the voice; it returns twice.
- Name super: name ≈3 % + role ≈2 %, lower-left (x ≈8 %, y ≈85 %), white, no box.
- End: sentence ≈2.2 % centred, then logo ≈6 % + URL ≈1.2 %. Closest free: Inter 500.

## Colour/grade
- Cool, desaturated with crushed blacks and a vignette; warm only in practical lights; body-cam footage keeps its own look.

## Camera/shots
- Handheld, macro, 360/fish-eye whips through the factory, body-cam, aerial, rain and snow plates. Real employees and real customer footage.

## Transitions
- Hard cuts; whip pans (24.3-25.6) used as cuts.

## Sound
- Voice-over: one narrator, ≈127 words in 53 s (≈2.4 words/s), an anaphora list (the same opening phrase repeated), then a turn and the call to action.
- Integrated -24.5 LUFS (quiet), LRA 3.2 LU, true peak -5.3 dBTP. Hits on many cuts (+23.8 dB at 8.65, +26.6 dB at 24.25 on the whip, +30.6 dB at 48.75 before the turn). Ending: fade.

## What makes it premium
- The list of hard facts (weather, temperature, demand, no elevator) is shown, not illustrated: every line has its real shot.
- Customer footage with its own burn-in is used as evidence.
- Ends on people, named.

## Recipe (real footage + HTML/GSAP)
- Write 6-8 anaphora lines (same two opening words), each 3-6 words; one or two real shots per line; ≈2.4 words/s.
- Open with 12-15 fragments of 0.2-0.6 s; slow down to one 8 s shot of people at the end.
- Title line Inter 500 2.2vh centred, words `stagger 0.18 s` timed to the voice; reuse it as a refrain.
- Name super: 3vh name + 2vh role at lower-left, fade 0.3 s, hold 3 s.
