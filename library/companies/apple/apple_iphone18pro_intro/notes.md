# Introducing the new iPhone 18 Pro  (Apple, 2026-09-09, 2:57 file / 2:52.5 content, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=Q3zwkxqh1t0
Purpose: launch film (the product film from the September 2026 event)
One-sentence point: "After going to the moon, Apple goes back to work" — an engineering chain story where each fix causes the next (chip → heat → vapor chamber → battery → camera).

## Structure
- 0-9.5 s **Hook**: Earthrise over the moon with a 3-line caption "Artemis II Mission / Shot on iPhone 17 Pro / April 2, 2026"; slow move into the Orion capsule, an iPhone floats in zero-g. VO: "Once you've been to the moon… where do you go next?"
- 9.5-15 s **Turn**: "Back to work." Dark lab corridor → top-down exploded parts on a white table (11-15 s).
- 15-36 s **Chip**: blueprint/CAD drawings that flicker in 0.12-0.4 s steps (16-21 s), glowing die render, light streaks, quick proof shots (cave, field), then a chip-history montage A5 → A20 Pro at 0.12-0.3 s per shot (32.5-35.4 s).
- 36-60 s **Heat → battery chain**: thermal camera (37-39 s), line drawings, X-ray-style 3D renders of the vapor chamber (43-51 s), phone on a lab table, hiker landscape for "longest battery life" (55-59 s).
- 60-72 s **Durability**: SOS satellite macro, lab rigs (water jet, drop, scratch microscope).
- 72-130 s **Camera**: aperture-blade renders (74-84 s), cave abseil shot on iPhone (85-106 s, pillarboxed), surf (107-125 s), camera-UI screen footage held in hands (122-130 s).
- 130-151 s **Proof**: pillarboxed portraits, night tripod + astro, glow-worm cave, surf crash (146.5 s = biggest sound hit), Milky Way.
- 151-170 s **Recap + bookend**: macro lens, exploded-view render assembling in a dark lab (154-164 s), floating colour line-up (164-170 s). VO triple recap + "This is what happens when you go to the moon, come back, and ask, 'What's next?'"
- 170-172.5 s **End card**: "iPhone 18 Pro" small, white on black, legal under it.

## Cut rhythm
- 144 shots in 172.5 s → **ASL 1.20 s**, median 0.96 s. ASL per quarter 0.94 / 1.20 / 1.49 / 1.20.
- 53 % of shots < 1 s, only 5 % > 3 s. Shortest 0.12 s (blueprint flicker 16.6 s, chip montage 33.1 s).
- Densest: 10-20 s (17 cuts in 10 s) and the chip montage. Longest: opening moon 9.55 s, X-ray render 7.9 s (47.5 s), floating phone 4.4 s (164 s).
- Each section starts with one longer "breath" shot, then accelerates.
- 55 % of cuts land within ±0.1 s of an audio onset (chance 38 %) → partly cut to music/VO.

## Typography
- Almost none. No feature supers in 170 s — the VO carries every fact.
- Opening caption: 3 lines left-aligned at x 15 %, y 44-52 %, white SF Pro (2 lines semibold + 1 regular), cap ≈ 2.3 % of H.
- End title: "iPhone 18 Pro", centred, white SF Pro Display medium, ink 4.2 % H (cap ≈ 3 %), on pure black; legal 2 lines grey ≈ 1.2 % H at y 90-95 %. Sound cuts 1 s after the title appears.

## Colour / grade
- Dark, low-saturation steel/teal grade, deep but detailed blacks; warm off-white lab tables.
- Product accent: deep cherry/burgundy phone colour; the only saturated colours are thermal magenta/orange and cyan "X-ray" glows.
- 23 % of frames are mostly empty (20 % dark). No letterbox; iPhone proof footage is pillarboxed (vertical or 4:3 inside 16:9, black sides).

## Camera / shots
Product macro on slow sliders with rack focus; top-down exploded parts on a white table; photoreal exploded-view 3D renders; CAD/blueprint graphics; thermal and X-ray looks; lab test rigs with people in clean-room suits; extreme real-world proof shot on iPhone (moon, caves, surf, night sky); hands holding the phone showing the real camera UI.

## Transitions
Hard cuts almost only. Graphic matches in the chip montage (same framing, chip changes). Blueprint "step-zoom" flicker. One black flash < 0.5 s. No dissolves seen.

## Sound
- Music: "Stampede" by Genesis Owusu (from captions). Male VO in second person ("You start with the chip. You engineer a new CPU core…").
- SFX dense (captions list whooshes, clicks, thud, hiss, shutters, waves, wind, whirring).
- Integrated **−16.0 LUFS**; loudest 0.5 s window ≈ −13 dBFS at 148 s.
- Biggest hit 146.7 s (surf crash, +21.9 dB) right after a 0.5 s dip at 145.5 s (−16.7 → −28.7 LUFS momentary) = suck-out before the hit.
- Audio ends at 171 s; end card sits in silence.

## What makes it premium
- A cause-and-effect story instead of a feature list; VO speaks to "you".
- Contrast of lab precision (macro, renders) with extreme real-world proof.
- Typographic restraint: one small end title, nothing else.
- Fast (ASL 1.2 s) but every section opens with a long breath shot.
- One consistent cool grade with one product colour as accent.

## Recipe (real footage + HTML/GSAP)
- 1920×1080, 24 fps. Sections 15-30 s; open each with a 4-8 s hold, then cut 0.5-1.2 s; for a "history" row cut every 3-4 frames (0.12-0.17 s) with identical framing.
- Grade the clips: `filter: saturate(.75) contrast(1.08) brightness(.95)` plus a teal overlay `#0d2a33` at 20 % with `mix-blend-mode: soft-light`. Keep the product colour un-graded (mask or separate layer).
- Vertical proof clips: centre them on black (pillarbox), no blur fill.
- End card: black bg; product name Inter/SF Pro 500, `font-size: 4.2vh` (≈45 px at 1080 → cap ≈ 3 % H), centred; `gsap.from(title,{opacity:0,duration:.6,ease:"power1.out"})`; legal 12-13 px `#8a8a8a` at bottom 6 %.
- Audio: VO −16 LUFS integrated, music ducked 8-10 dB under VO; cut all sound 0.5 s before the biggest visual hit, then hit; end in silence.
