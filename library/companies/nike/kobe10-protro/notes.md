# Nike Kobe 10 Protro  (Nike, 2026-08-04, 27.8 s, 9:16, YouTube Shorts / Reels)
URL: https://www.youtube.com/shorts/RaSZusY8SMA
Purpose: launch teaser (product hero, "sculpted out of endless curiosity", drop date only in the post caption)
One-sentence point: The shoe is shown as an object being sculpted, scanned and dissected, ending on the Kobe logo pressed into clay.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-1.1 hook: a robotic rig with the Kobe sheath logo presses into grey material, hand in silhouette; 1.1 s extreme macro of a drill bit carving clay; 2.5 s a hole tears open. Process curiosity, no text.
- 3.3-14.7 build: fast "lab" montage: wireframe scan outline on black, false-colour thermal insoles (magenta/yellow), X sole pattern, yellow macro of a ball texture, hands placing a footbed, scanned shoe in a bounding box.
- 14.7-22.6 turn: exploded view of the layers, clay surface, upper mesh macros, X-ray of the shoe, grey exploded stack.
- 22.6-25.2 payoff: first clean hero: two hands lift the white shoe against a grey sky (2.5 s, the longest shot).
- 25.2-27.8 end: the Kobe sheath logo embossed in clay; light rakes across it. No text, no date, no swoosh card.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 32 shots, ASL 0.87 s, median 0.71 s, 72 % under 1 s, shortest 0.21 s. Quarters 1.00 / 0.70 / 0.54 / 1.39: accelerates to 0.5 s in Q3, then holds the hero (2.5 s) and logo (2.6 s).
- Cuts do not follow audio onsets (13 % vs 9 % chance): picture-driven cutting.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- None. 0 words on screen in 27.8 s.

Colour/grade: palette, contrast, grain, letterbox
- Near-monochrome: grey clay, white, black, desaturated sky; 3-4 false-colour shots (thermal magenta/orange, yellow) as accents. Soft contrast, slight grain/softness, matte.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Extreme macros (clay, mesh, sole), studio inserts with hands, CG scans / X-ray / exploded views, one hero hand-held product shot. Slow push-ins inside shots.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 31 hard cuts; graphic matches by shape (insole outline -> real insole -> thermal insole).

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Sound design and low drone, sparse (0.5 onsets/s), biggest rise +19.9 dB at 6.55 s, one 0.5 s drop at 27.5 s. No VO. Integrated -10.4 LUFS.

What makes it premium (3-5 bullets)
- Shape rhyme montage: every shot shows the same object in a different material (clay, scan, heat, X-ray).
- Restraint: no text, no price, no CTA; the logo in clay is the end card.
- Monochrome with rare colour bursts keeps it "museum" not "ad".
- Speed curve: fast middle, slow hero.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 28 s, 30-32 shots: 0.4-0.9 s macros, last two shots 2.5 s each.
- Grade: `filter: grayscale(0.85) contrast(0.95) brightness(1.02)` on all real footage; 3 shots with a false-colour LUT (gradient map black -> #5A1A6E -> #E0458B -> #FFB000).
- CG feel without CG: SVG outline traces drawn over a frame (`stroke-dasharray` draw 0.4 s), bounding-box lines, exploded layers as separate PNGs offset in y with `stagger:0.05`.
- End: logo PNG as embossed relief (two copies, ±2 px offset, white/black at 30 %), a 1080 px wide linear-gradient light band sweeping `x: -1080 -> 1080` over 2 s.
- Audio: drone at -18 LUFS + foley hits; no music beat.
