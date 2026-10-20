# Wolf Ranch: The World's First 3D-printed Community  (ICON, 2025-12-23, 10:47, 16:9, YouTube, official ICON channel)
URL: https://www.youtube.com/watch?v=VChT9hHpu4Q
Purpose: project documentary / case study (100 printed homes built with a national homebuilder partner, from empty field to families moving in)
One-sentence point: ICON and its homebuilder partner turned a Texas field into a finished community of 3D-printed homes, and the people who built, sold and live in them tell how.

Note: the video has no captions on YouTube, so the story is reconstructed from pictures, supers and the edit, not from speech.

## Structure (646.8 s)
- 0-8 (0-1 %) title: slow drone push over the finished community, white bold caps title "BUILDING THE WORLD'S FIRST 3D-PRINTED COMMUNITY" bottom-left.
- 8-41 (1-6 %) news cold open: real TV news clips (national morning show, network news, a business channel) with their own lower thirds and bugs - gantry printer, nozzle, site - then a partner executive interviewed on TV. Third-party press used as proof.
- 41-60 (6-9 %) the partner's executive chairman on a business-TV interview (18.6 s, second-longest shot).
- 60-77 (9-12 %) site from the air, then a top-down drone of the finished streets.
- 77-82 (12-13 %) chapter title "PROJECT: WOLF RANCH" in huge white caps, the ICON founder walks in and sits; his body passes in front of the letters (text layered behind the person). A crew member claps a slate in the wide - the "making-of" is left in on purpose.
- 82-195 (13-30 %) the deal: the founder on a stool in an empty white printed room (wide + CU, two cameras), the partner's co-CEO in a model home (name super), drone of the empty land, aerial of the start of the works. Longest shot 22.1 s (co-CEO, 130 s).
- 195-325 (30-50 %) logistics + build: printer arrives on trucks, highway shot, drone over rails and slabs, crew in PPE at the gantry, nozzle macro, low-angle passes along the layered walls (fast pan along the bead at 317-322 s), crew on ladders at roof height, homebuyer couple in a sales office.
- 325-470 (50-73 %) scale: drone grids of dozens of slabs and printed walls, unlabelled timelapses of the gantry printing (385-390 s), site superintendent interview in hard hat + hi-vis on site, founder interview.
- 470-600 (73-93 %) people: sales event crowds, buyers' interviews (couples, a retiree in her kitchen), families on the street, a toast with the printing crew under the gantry (cheering).
- 600-630 (93-97 %) wrap: partner co-CEO and founder last lines, drone wides, a child running.
- 630-647 (97-100 %) final drone reveal of the whole community (17.1 s), ICON logo white on black.

## Cut rhythm (after dropping 24 false cuts in a hyperlapse drone flight, a fast pan along a wall and timelapse flicker, and adding 3 by eye)
- 138 shots, ASL 4.69 s, median 3.37 s, 0 % under 1 s, 12.8 shots/min. ASL per quarter 5.05 / 4.04 / 3.67 / 6.47 s.
- Longest: 22.1 s (co-CEO interview), 18.6 s (TV interview), 17.1 s (final aerial). Densest: news cold open (4-5 cuts per 10 s) and the build montage at 200-220 s (5 per 10 s); interview blocks 0-2 per 10 s.

## Typography
- Opening title: bold neo-grotesk caps (Helvetica Neue Bold / Inter Bold look), white, 3 lines, cap height ≈5 % H, left-aligned at x ≈8 %, bottom ≈20-12 %, over the drone shot.
- Chapter title: same face, cap height ≈10.4 % per line, 3 lines, x ≈2.5 %, top ≈21 %, the speaker walks in front of it (needs a rotoscoped matte).
- Name super: name bold caps ≈3.3 % cap height + role caps ≈2 %, white, slightly transparent, bottom-left at x ≈4 %, y ≈78-86 %, no box.
- Borrowed TV graphics (news lower thirds, channel bugs) kept as they aired - they read as press coverage.

## Colour/grade
- Natural Texas sun, saturated green lawns and blue sky in the finished community; the interview room is white printed concrete with soft window light (high-key). No letterbox, no grain.

## Camera/shots
- Drone: a large share of the b-roll (eyeball) - top-down grids, reveal push-ins, a sped-up hyperlapse flight (36-39 s), final wide.
- Timelapse of printing (unlabelled) and fast low-angle pans along the bead.
- Wide-angle low shots under the gantry and with crew on ladders (scale: people next to 3 m walls).
- Two-camera interviews: wide on a stool in an empty room + CU; partner execs in a furnished model home.
- PPE: hard hats, hi-vis vests, safety glasses on all crew.

## Transitions
- Hard cuts (no dissolve verified by eye). Logo after a cut to black.

## Sound
- Interview-led with a soft music bed; integrated -13.3 LUFS, LRA 7.9 LU, true peak +2.4 dBTP (clips).
- Many 0.3-1.25 s quiet gaps (speech pauses + music stops), clusters at 179-195 s and 539-567 s; a 2.55 s gap at 478.6 s before the people section; a 1.25 s full stop at 89.9 s after the chapter title.
- Biggest hits 471.9 s and 549.7 s (+29-30 dB) in the cheering/celebration section.

## What makes it premium / credible
- Third-party TV coverage in the first 40 s = instant proof.
- Real scale: dozens of slabs and printed walls from the air, then real families living there.
- Every group speaks: builder founder, partner leadership, site superintendent, buyers.
- Making-of left in (slate) and a huge chapter title layered behind the speaker = confident, documentary feel.

## Recipe (real footage + HTML/GSAP)
- Title: `font:700 6vh/1.05 Inter; text-transform:uppercase; color:#fff; left:8vw; bottom:12vh`, 3 lines, `tl.from(lines,{autoAlpha:0,y:12,stagger:.08,duration:.5})`, hold 6 s over a slow drone push (`scale 1 -> 1.06` over 8 s).
- Chapter card behind a person: export a matte of the speaker (rotoscope/AI matte) as a PNG sequence or alpha video; stack `video bg` < `h1` (Inter 800, 13vh, line-height .95) < `video matte`. Hold 4-5 s.
- Name super: name Inter 700 3.3vh caps + role Inter 500 2vh caps, `left:4vw; bottom:14vh; opacity:.92`, in 0.4 s, hold 4 s.
- Use earned media only with permission; otherwise use press headline screenshots as document shots.
- Drone: one reveal per chapter, 6-17 s; timelapse with a small "Timelapse" tag if you show printing speed.
