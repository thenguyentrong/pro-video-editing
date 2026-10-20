# CA-1 Europa: Autonomous Air Dominance  (Helsing, 2025-09-25, 1:01, 16:9, YouTube @HelsingAI)
URL: https://www.youtube.com/watch?v=zzg65k6WONY
Purpose: product reveal teaser (announcement of an aircraft programme)
One-sentence point: a new autonomous combat aircraft is revealed as a dark, symmetrical object between light bars, then named in two quiet words.

Honesty note: the frames read as a high-end render (perfect reflections, no wear, no people, no environment). The film does not label it as render or as real hardware.

## Structure (no voice)
- 0.0-3.3 hook: horizontal and vertical light bars switching on in black; flicker.
- 3.3-22.5 fragments: macro of panels, an intake, a tail marking with the type name, the underside, the brand mark on the fuselage. ≈0.6 s per shot, many separated by 1-2 frame black dips.
- 22.5-26.5 strobe passage: vertical light tubes flashing 6-8 times per second (counted as one shot), crossed light beams, a grain/noise frame at 26.
- 26.5-47.6 reveal: the aircraft head-on and perfectly centred between vertical light tubes; the hangar ceiling lights switch on in rows; side profile; cuts slow down (5.2 s and 2.7 s shots).
- 47.6-55.0 black; the type designation appears, then the name fades in beside it in grey (centred, ≈5 % H). 0.5 s drop-out at 53.0.
- 55.0-61.1 brand mark (≈13 % H) + small wordmark, fade out.

## Cut rhythm
- 58 shots in 61.1 s (scene detector corrected by eye: 6 dark cuts added, 21 light-flicker events removed). ASL 1.05 s, median 0.60 s. ASL per quarter 0.61 / 0.85 / 0.95 / 7.64 s.
- 66 % of shots under 1 s, 3 % over 3 s. Cuts per 10 s: 16, 14, 11, 9, 7, 0. A steady deceleration from 16 to 0: fragments -> whole object -> name.
- Longest: 13.5 s (title + logo on black), 5.2 s (first head-on reveal).

## Typography
- Only at the end. Light grotesk (≈300), sentence case, ≈5 % of frame height, centred on black; the second word is grey (≈55 % white). Closest free: Inter 300.
- The aircraft's own markings carry the name earlier (tail lettering, brand mark on skin).

## Colour/grade
- Monochrome teal-grey: black, cold white light, dark gunmetal; no other colour. Mean luma 0.155. Light grain on dark frames.

## Camera/shots
- Macro slides along the skin, symmetrical front-on wides, low angle under the fuselage. The light (tubes, beams, rows of ceiling lights) moves; the camera barely moves.

## Transitions
- Hard cuts with 1-3 frame black dips between fragments (11 dips measured); light flicker used as transition; fade to the title.

## Sound
- No voice. Integrated -12.4 LUFS, LRA 11.6 LU (wide: very quiet start, loud middle), true peak +0.2 dBTP. Hits at 8.2, 18.5 and 37.0 s; drop-out 53.0-53.5 before the logo. Ending: fade, 2.1 s silence.

## What makes it premium
- Strict monochrome and symmetry: it looks like an object, not an advert.
- The name is withheld until 80 % of the runtime and then set small.
- Light is the editor: switching tubes and ceiling rows mark the beats.

## Recipe (real footage + HTML/GSAP)
- Shoot (or render) the object between vertical LED tubes in a black space; switch tubes on/off in time with the music; 0.4-0.8 s fragments for the first third.
- Grade: `filter: saturate(0) contrast(1.15)` then a teal tint (`sepia(.2) hue-rotate(150deg)`), keep blacks crushed.
- Add 1-2 frame black dips between fragments (`<div class=dip>` opacity 1 for 0.04-0.08 s).
- End: black, Inter 300 5vh centred, first word white, second word `rgba(255,255,255,.55)`, each fades in 0.6 s, 1 s apart; 0.5 s silence; logo 6 s.
