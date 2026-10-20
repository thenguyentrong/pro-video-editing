# Introducing Figma Motion: Your canvas now has a timeline  (Figma, 2026-06-25, 68.1 s, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=l3HuAYXyOTo
Purpose: launch film (software feature), rendered UI demo
One-sentence point: Animation now happens inside the design file, so a designer can move from a static frame to a finished, exportable motion piece in one place.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-3.9 hook (0-6 %): extreme close-up of an animated graphic shape on lime ≈#d9ff82; it keeps moving while the "camera" pulls back.
- 3.9-6.8 (6-10 %): pull back to the whole design canvas with panels: the shape was a frame in a real file.
- 6.8-9.8 (10-14 %): a 3D asset on black, then the product name in two big orange lines among a floating collage of design cards (title held ≈1.8 s).
- 9.8-22.0 (14-32 %): feature 1 on violet ≈#4b00c9: a toggle button gets keyframes; the view punches into the timeline (0.0-1.2 s ruler), the easing curve panel, back to the button, then the finished "unlocked" card.
- 22.0-26.6 (32-39 %): feature 2: objects follow a motion path on a grey line map.
- 26.6-36.8 (39-54 %): feature 3 (the turn): an AI prompt box types an instruction over a poster; the glitchy type animation plays with the timeline under it (10.2 s, the longest shot).
- 36.8-44.2 (54-65 %): feature 4: 3D transform on an image card (hand cursor drags it).
- 44.2-50.5 (65-74 %): feature 5: collaboration: comment bubble pinned to a time, avatars on the timeline, "looking good" chat.
- 50.5-56.5 (74-83 %): feature 6: reusable easing styles applied to an icon set (greens).
- 56.5-62.6 (83-92 %): feature 7: an app screen animates on black; a code panel shows exported CSS keyframes.
- 62.6-64.9 (92-95 %): end line in two orange lines among the same collage.
- 64.9-68.1 (95-100 %): coloured shapes bounce and morph into the brand logo on black. No URL.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 22 set-ups, ASL 3.10 s, median 2.63 s, 14 % under 1 s, 41 % over 3 s, 19 per minute. Quarters 2.13 / 2.84 / 2.84 / 3.40 s: it slows down as features get richer.
- Shortest 0.5 s (punch-in / punch-out on the button), longest 10.2 s (prompt-to-result), 6.3 s, 6.0 s.
- Inside each set-up the UI itself animates all the time (panels pop, values change, cursor moves), so the eye sees a change every ≈0.5-1 s even when the shot is long.
- Verified by eye with a 4 fps strip: "cut" here = a hard change to another screen or a hard punch-in/out. Panel pop-ins are not cuts (one dropped at 15.75 s); four hard changes added (13.9, 38.2, 54.3, 64.9 s). A different reading of punch-ins could move the count ±3.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Title and end line: the brand's own grotesque (free: Inter Tight 500 or Inter Display), sentence case, orange ≈#f2643a on black. Title cap ≈14.6 % H, two lines (line pitch ≈22 % H), left of centre. End line cap ≈11 % H, two lines, right of centre. 2-4 words. Hold 1.8-2.3 s. Words build in one by one (≈0.2 s apart).
- All other text is UI text, shown at 200-400 % zoom so labels read at ≈3-5 % H. The prompt box types character by character.
- Big black arrow cursor with white outline (≈8-10 % H at zoom), hand cursor for drags.

Colour/grade: palette, contrast, grain, letterbox
- Each feature gets its own flat background colour: lime ≈#d9ff82, violet ≈#4b00c9 with lilac ≈#c9b8ff, grey map, orange, black, greens. Brand orange ≈#f2643a for words. Product UI stays light grey/white. No grain, no letterbox.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- 100 % rendered UI (designed product scenes, not raw screen capture): virtual camera zooms, pans and punch-ins on the canvas; floating cards with drop shadows; one 3D asset; no people, no live action.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- About half the changes are hard cuts on a new colour; the rest are continuous camera moves inside the canvas (zoom out from a detail, punch in to the timeline) and morphs (cards scatter to black, shapes become the logo). One slide wipe (26 s).

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- No voice. One upbeat electronic track with UI clicks and pops on cursor actions. Integrated −13.4 LUFS, LRA 2.0 LU, true peak −0.1 dBTP. No drop-outs or silences. Biggest rise +18 dB at 18.8 s (button result).
- Cuts on onsets 24 % vs 27 % chance: picture follows the UI action, not the beat.

What makes it premium (3-5 bullets)
- The hook is the result (a moving graphic), the pull-back reveals it was made in the tool.
- One feature per colour world: the viewer always knows where a new feature begins.
- UI is zoomed until it is readable; the cursor acts like a hand with intent.
- Words only twice (name, end line), big and in one brand colour.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920×1080, 60-70 s, 7 features × 4-10 s, ASL ≈3 s, the longest beat = the AI or "magic" feature.
- Build each scene as a real HTML mock of the UI at 2× scale inside a `#stage` div; the virtual camera is a GSAP tween on `scale` + `x/y` of the stage (`power3.inOut`, 0.8-1.2 s for pull-backs; `set()` for hard punch-ins).
- Background per feature: `#d9ff82`, `#4b00c9`, `#e6e6e6`, `#f58b2c`, `#000`. Title: `Inter Tight 500 15vh #f2643a`, words `stagger:0.2, y:20 → 0, opacity 0 → 1`, hold 1.8 s.
- Cursor: SVG arrow 80 px with 3 px white stroke, path moves with `power2.inOut` 0.6 s, click = `scale 0.85 → 1` 0.12 s + a 0.05 s click SFX.
- Prompt box: white card, `Inter 400 3.2vh`, type-on 0.035 s/char, then result plays.
- End: shapes `back.out(2)` bounce, morph into the logo (`MorphSVG` or crossfade 0.3 s) on black, hold 1.5 s.
- Sound: one track at −13 to −14 LUFS, UI clicks/pops on every action, no VO.
