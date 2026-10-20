# Sound. Elevated.  (Bang & Olufsen, 2025-11-17, 1:30, 16:9, YouTube; 100-year campaign film, also cut to 53/31/16 s)
URL: https://www.youtube.com/watch?v=ocgjl0VKwQ0
Purpose: brand anthem / centenary campaign
One-sentence point: A woman rides a lift through 100 years of B&O; each door opens on a decade of sound, and the brand line closes the trip.

Structure:
- 0.0-3.2 wordmark builds letter by letter over a dark wood hotel corridor, then "100 years. One journey." centred (frames/t002.5s.jpg).
- 3-9 the woman walks to the lift, red bag (the accent), a grid of speaker cones, a blue B&O nameplate.
- 9-20 first door: a black-and-white 1920s-style ballroom with chandeliers, a radio dial macro, dancers (t013.0s).
- 20-32 lift again; a beige 1950s-style living room with a TV on legs, a couple on a sofa (t028.0s), a small brass detail macro.
- 32-47 a round 1970s-style lounge with a turntable seen from above (t039.0s), she dances, a light-trail spin.
- 47-56 a family in the lift, a baby close-up, a man with a vintage speaker (t057.0s area).
- 56-65 a black void with glowing white door frames; she walks through them (longest shot, 6.2 s).
- 65-78 the lift opens onto a night meadow: grass, a sheep, a man with a speaker, wide field.
- 78-86 she floats out of the lift into a starfield; an eye macro reflects the cosmos.
- 86-87 she smiles wearing headphones (the only clear product shot).
- 87-90 back in the corridor: "Sound. / Elevated." built letter by letter in two offset lines, then the wordmark (t087.5s, t088.5s).

Cut rhythm: 60 shots (adaptive detector: the film is dark, ffmpeg scene found only 22), ASL 1.50 s, median 1.18 s, 40 % under 1 s, 12 % over 3 s, 40 shots/min. Quarters 1.50 / 1.18 / 1.61 / 1.50 s: flat. Longest 6.2 s (door frames), 4.8 s. Cuts on onsets 20 % vs 13 % chance. Each "door" section is 8-15 s and opens with a 2-4 s establishing wide, then 0.6-1.2 s details.

Typography: "100 years. One journey." in a rounded geometric sans (closest free: Jost / Outfit), sentence case with full stops, white, cap ≈ 4.6 % H, centred at y ≈ 50 %. End line "Sound. Elevated." heavier weight (≈ 600), cap ≈ 6.3 % H, two staggered lines, letters fly in with wide spacing and settle (tracking animates from ≈ +0.4 em to 0). Wordmark wide-tracked caps ≈ 4 % H on the corridor.

Colour/grade: very dark (median luma 13, 81 % of frames dark), low contrast in the shadows (p95-p5 91), neutral R-B 0. Each decade has its own grade: B&W ballroom, beige-amber 1950s, olive-green 1970s, deep green night meadow, blue cosmos; the red bag and B&O blue nameplate link them.

Camera/shots: large studio sets, symmetric lift-door frames, slow dolly-ins through doors, overheads (turntable, round room), motion-blur spins, VFX starfield. People-led; products appear as period objects (radio, TV, turntable, speaker) and only once as a modern headphone.

Transitions: hard cuts; lift doors as natural wipes between decades; a light-trail spin hides one change; no dissolves except the opening wordmark.

Sound: music only (no VO), period-shifting score; −14.0 LUFS integrated, LRA 10.8 LU (dynamic), true peak +0.9 dBTP. Big rises +18-23 dB at 7.2, 15.7, 38.2 (biggest, +22.6 dB, the 1970s room) and 58.7 s (door frames). No drop-outs.

What makes it premium:
- One simple device (a lift through time) carries 100 years without a single explanation.
- Production design does the storytelling; product is a period prop, not a hero.
- Bookend: the same corridor opens and closes the film; text only at both ends.
- Letter-build typography with settling tracking = the brand line feels "assembled", like the products.

Recipe (real footage + HTML/GSAP):
1. Choose a frame device (door, lift, window) that can open onto 4-6 worlds; give each world one grade and one era object.
2. Each world 8-15 s: 2-4 s wide, then 0.6-1.2 s details; end the film in the opening location.
3. Letter-build end line: split into letter spans, `gsap.from(letters,{opacity:0, x:()=>gsap.utils.random(-40,40), letterSpacing:'0.4em', duration:.9, ease:'power3.out', stagger:.05})`; second line offset right and up by ≈ 1 line.
4. Opening line: `font: 400 6.3vh 'Jost'` (cap ≈ 4.6 % H), centred, fade 0.5 s, hold 1.5 s.
5. Grade: crush to near-black (`brightness(.75) contrast(1.1)`), one warm practical light per set; keep a red accent object in every world.
6. Music-only master −14 LUFS for social; true peak ≤ −1 dBTP.
