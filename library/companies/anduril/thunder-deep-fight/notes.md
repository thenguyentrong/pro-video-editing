# Thunder: Autonomous Attack Rotorcraft for the Deep Fight  (Anduril, 2026-07-20, 0:56, 16:9, YouTube @Anduril)
URL: https://www.youtube.com/watch?v=kmPaiqfywd8
Purpose: product reveal (hardware spec teaser)
One-sentence point: a new autonomous tiltrotor is shown as one dark, green-lit object, part by part, with one capability label per section.

Honesty note: everything is one aircraft in a dark studio/hangar with a green key light. At 480p it cannot be decided whether this is photographed hardware or a render; nothing in the film says either way. No flight, no people, no environment.

## Structure (no voice, music + SFX)
- 0.0-7.2 hook/title: front-on hero of the aircraft in green light; a giant one-word title bleeds off the top edge; a 3-line category super sits centred under the aircraft.
- 7.2-17.3 propulsion: prop and nacelle macros, 2-line spec label top-left; two orbit shots inside a glowing light ring (12.2-15.6).
- 17.3-17.8 three 0.25 s light-streak shots = section wipe.
- 17.8-28.0 sensors: underside sensor windows, label for the perception stack top-left, logo embossed on the skin.
- 28.0-28.5 second light-streak burst (three 0.25 s shots).
- 28.5-43.4 payload: payload bays open, rockets; small header label top-left with a numbered list (1 / 2), and a bottom row of 3-4 role words spread across the full width that resolve letter by letter.
- 42.5-43.0 drop-out (0.5 s), then the loudest hit (+29.2 dB at 43.25) on the cut to the loaded aircraft head-on (43.4-51.4).
- 51.4-56.0 logo on black (small wordmark left of centre, tiny legal metadata in the top corners).

## Cut rhythm
- 20 shots in 56.0 s (adaptive detector; the scene detector found only 7 in the dark footage, every extra cut checked by eye). ASL 2.80 s, median 2.15 s. ASL per quarter 3.50 / 1.40 / 2.80 / 3.50 s.
- Longest 7.22 s (title), 6.67 s (payload reveal at 36.7), 4.62 s (logo). Shortest 0.25 s x 4 (light-streak bursts).
- Cuts per 10 s: 2, 6, 6, 2, 2, 1. 20 % of shots under 1 s, 40 % over 3 s. Slow-fast-slow: fast only in the two light-streak bursts.

## Typography
- Title: one word, white grotesk 700, tight tracking, cap height ≈35 % of frame height, top-aligned and cropped by the frame edge; the aircraft stays readable under it. Closest free: Inter Tight 700.
- Category super: 3 lines caps ≈2.3 %, centred, under the aircraft.
- Spec label: 2 lines caps ≈4.5 %, top-left (x ≈5 %, y ≈8 %), white, no box, held for the whole section (≈10 s).
- Section header: caps ≈2 % top-left plus a numbered list (number column + word column, ≈2 %).
- Role row: 3-4 caps words ≈4.5 % on the bottom line, spread at equal intervals from left to right edge.
- Animation: characters resolve in a scramble/decode (wrong letters for ≈0.3-0.5 s, then the right word); no fades.

## Colour/grade
- Near-black (mean luma 0.115) with one saturated green key + a warm amber practical on the skin; green also rims the floor. One-colour lighting is the whole look.

## Camera/shots
- Slow dolly and orbit moves (≈1-2 % of frame per second), macro details, low angles. The whole aircraft only at the start (title) and the end (hero). No people.

## Transitions
- Hard cuts; two bursts of three 0.25 s light-streak shots act as section wipes. Fade from hero to the black logo card.

## Sound
- Music-led, no voice. Integrated -10.7 LUFS, LRA 7.5 LU, true peak +1.1 dBTP (hot). Hits: 18.0 s (+16.9 dB, after the first streak burst), 43.25 s (+29.2 dB after a 0.5 s drop-out). Ending: fade.

## What makes it premium
- One light colour, one object, black everything else.
- Title as architecture: a word so big it is cut by the frame.
- Labels as engineering data (category + list), no marketing adjectives on screen.
- A real drop-out before the final reveal.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Shoot the real machine in a dark space with one coloured key (LED tube or gelled light) and one warm practical; slider moves 2-4 s per shot; keep 70 % of the frame dark.
- Title: `font: 700 48vh/0.8 'Inter Tight'; letter-spacing:-.04em; top:-6vh` so the top is cut; fade-in 0.4 s; hold 5-7 s over the hero.
- Labels: Inter Tight 600 caps 4.5vh (2 lines) top-left; scramble each character with a random glyph every 0.04 s for 0.4 s, then set the real letter (seek-safe: compute glyph from `Math.floor(t/0.04)` and a seed).
- Bottom role row: `display:flex; justify-content:space-between; bottom:5vh; left:3vw; right:3vw`.
- Section wipe: three 0.25 s light-streak clips back to back.
- Sound: cut music to silence 0.5 s before the hero cut, land the biggest hit on the hero frame.
