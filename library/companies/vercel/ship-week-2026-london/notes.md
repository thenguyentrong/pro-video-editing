# Ship Week 2026 London  (Vercel, 2026-06-22, 61.1 s, 16:9, YouTube / social)
URL: https://www.youtube.com/watch?v=YbzBt--HSOE
Purpose: keynote/event sizzle (recap of a launch week: keynote, talks, meetups, party)
One-sentence point: Thousands of builders came to the first Ship outside the US, and the message was agents.

Structure: beats with timestamps (% of runtime)
- 0-2.4 s (0-4 %) street hook: a London street, then the event's mural "Built in [mark] London" on a brick wall, then a mono line types on a dark brick arch.
- 2.4-7.3 s (4-12 %) the longest shot (4.9 s): the keynote stage, wide, then the CEO on stage with a huge word on the screen behind; name super bottom-left.
- 7.3-20 s (12-33 %) keynote → community: a typed word card, a glitch transition, a speaker, meetups under brick arches, a URL projected over the crowd, a panel on stage.
- 20-32 s (33-52 %) the city/outdoor week: branded van driving, food truck, pizza oven inserts, venue signage macros (densest 10 s window: 13 cuts in 20-30 s).
- 32-55 s (52-90 %) talks, rooftop meetups, a party with a DJ, a pixel-dissolve audience shot, faces in the crowd; one word card with the logo triangle wiping across the text.
- 55-58 s (90-95 %) a big wide of the full hall, crowd.
- 58.1-61.1 s (95-100 %) end card: event lockup on black (≈1.8 s) then silence.

Cut rhythm (verified)
- Scene detection 38 cuts, adaptive 52; checked on before/after pairs. Dropped 1 false cut (19.96 s, same van shot), added 1 (20.16 s, cut to the van side). 52 cuts.
- 53 shots, ASL 1.15 s, median 0.92 s, 58.5 % under 1 s, 1.9 % over 3 s, 52 shots/min. Per quarter 1.27 / 0.90 / 1.17 / 1.09: flat and fast from the start. Cuts per 10 s: 6 / 8 / 13 / 8 / 8 / 9. Shortest 0.52 s, longest 4.92 s (keynote wide), end card 3.0 s.

Typography
- Kinetic mono words over picture: lowercase, light grey-white, a slab/typewriter mono, line box ≈17 % H (x-height ≈8 % H), typed on with a solid block cursor, or broken into pixel noise when leaving. 1-3 words per card, on screen 0.6-1.5 s.
- Persistent corner bug: event lockup top-left, ≈3.5 % H, at x ≈5 %, y ≈10 %, on most shots.
- Name super: two lines, caps, regular sans, cap ≈4 % H, bottom-left at x ≈5 %, y ≈81-88 %; the company mark as the bullet before the title.
- End card: event lockup (word + outlined city tag) centred, cap ≈10 % H.
- Closest free fonts: Geist Mono or Courier Prime for the typed words; Geist / Inter for supers and lockups.

Colour/grade
- Night-club dark (mean luma 0.14): black stage, cool blue and magenta stage light, warm tungsten pizza/food inserts, daylight street shots as contrast. Black text cards. No letterbox.

Camera/shots
- Event documentary: handheld, gimbal, a few drone/vehicle tracking shots, macros of signage and food, stage shots on long lenses, crowd wides. Real people only, no UI footage.

Transitions
- Hard cuts almost everywhere; graphic accents: a glitch/scan-line transition (≈7.9 s), a logo triangle wiping over a word card (≈42 s), a pixel-dissolve on an audience shot (≈49 s), typed text over picture.

Sound
- Speech nearly all the way: keynote and attendee sound bites edited into a VO line (0.6-57.8 s, ≈152 words, ≈2.5 words/s with gaps; speech detection only).
- Pulsing electronic music bed under it; hits up to +26 dB (54.4 s) at the hall reveal. No drop-outs; 1.2 s silence at the end.
- Integrated −13.5 LUFS, loudness range 4.9 LU. Cuts on onsets 54 % vs 53 % chance: cut to the voice and the action, not to the beat.

What makes it premium
- A mood, not a schedule: city, food, people, light, with the keynote as the spine.
- One graphic language (typed mono words + block cursor + corner bug), used sparsely.
- Speed with structure: ≈1 s cutting but each section is one place (stage, street, venue, party).

Recipe (real footage + Hyperframes, 1920×1080, 60 s)
- Footage: 50-60 clips of 0.5-2 s from the event (stage wides, speaker CUs, crowd, signage macros, food, city B-roll); one 4-5 s keynote shot at 5-12 % of the runtime; one big hall wide at 90 %.
- Spine: a sound-bite VO from the keynote and attendees (≈2.5 words/s), music bed at −18 to −14 LUFS-S, a hit on the final wide.
- Typed words: `400 16vh 'Geist Mono'`, `color:#e8e8e8`, lowercase, type-on 0.04 s/char with a block cursor, hold 0.6-1.2 s; exit with a pixel-noise mask 0.2 s.
- Corner bug `3.5vh` at `left:5%; top:7%` for the whole film; name super 2 lines caps `4vh` at `left:5%; bottom:12%`.
- End: lockup on black 1.8 s, then 1.2 s silence. Master −14 LUFS.
