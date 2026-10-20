# Liebherr - LR 1300.1 SX crawler crane: SMC Marine's experience  (Liebherr, 2021-09-08, 3:41, 16:9, YouTube @Liebherr)
URL: https://www.youtube.com/watch?v=cdDLmeF9JOI
Purpose: customer case study / testimonial (marine contractor in Sydney, crane on a barge for a waterfront megaproject)
One-sentence point: A marine contractor's director explains why they bought this crawler crane for a building constructed over the water: vertical-line finder for barge lifts, lift-planning software, modular counterweights, reliability, lower fuel burn and good support.

## Structure (one speaker, no narrator)
- 0.0-9.7 (0-4 %) title: white box top-left with model name in two lines + logo on a yellow strip that wipes in; harbour wide with the crane, a bridge and the city skyline; slow aerial; the client's logo on a hi-vis shirt (close-up).
- 9.7-38.8 (4-18 %) who: director intro shot (arms crossed, smiling, crane and bridge behind) with name super; company profile (locally owned, safe and efficient delivery, past harbourfront projects); the next project, a fish market built over the water; team walking on the wharf, crane on site.
- 38.8-65.1 (18-29 %) the project challenge: structure partly under water, heavy marine foundations, water level lowered by about four metres; b-roll of barge, boom sections, counterweights ("10t" / "14t" stencils), harness check, a young operator.
- 65.1-114 (29-52 %) favourite feature: operators queue to drive it; the vertical-line finder explained (barge trims and heels under load, crane slews to keep the hook central); cab touchscreen with a finger on the lift view; real lift of a load off the barge, hook against sky and sun.
- 114-158 (52-71 %) software + cab: lift data feed to naval architects, cab tilts/rises for visibility; reliability matters because barges are hard to service; assembly of the lattice boom (LIEBHERR on the boom), crane on the barge from the water.
- 158-200 (71-90 %) modular counterweights, sustainability (emissions, fuel burn), deadlines met, support through shipping and assembly; crew assembling, wrench on a bolt.
- 200-217 (90-98 %) closing: investment in safety, sustainability, quality; sunset aerial of the harbour and city, crane silhouette, last smile.
- 217.1-221.4 (98-100 %) logo on white.

## Cut rhythm
- 83 shots in 221.4 s (80 detected + 3 adaptive-only cuts verified). ASL 2.67 s, median 2.68 s, 4.8 % under 1 s.
- ASL per quarter 2.52 / 2.52 / 2.64 / 2.64 s - completely flat; cuts per 10 s 2-5 everywhere.
- Longest 5.16 s (director intro with super), 4.88 s, 4.44 s. Shortest 0.72-0.88 s (two quick boom details at 63-65 s, one at 175 s).
- The interview is cut into short sections of 3-5 s; b-roll inserts of 2-3 s each between nearly every sentence.

## Typography
- Liebherr grotesk (free: Barlow 600/400). Title box: white, top-left, ≈42 % H tall incl. logo strip; model name 700 ≈5.5 % H, black, two lines; logo below on a yellow (#FFD000-like) strip that wipes in from left. Holds ≈7 s across 3 shots.
- Name super: white box at x ≈4-38 %, y ≈70-92 %, name 700 ≈4.5 % H + role 400 ≈4.5 % H, black, sentence case; on for ≈5 s on the first appearance only.
- On-machine text does the data job: counterweight stencils "10t / 14t", "LIEBHERR" on the boom, UI values (bar pressures, slew angle) on the cab screen. No graphic data cards.

## Colour/grade
- Bright, clean Australian daylight: deep blue water and sky, saturated yellow crane and hi-vis; mild contrast; golden-hour and sunset for the ending. No letterbox, no grain.

## Camera/shots
- Interview: medium shot, speaker right-of-centre, crane and the harbour bridge soft behind, outdoor on the wharf, eyes just off camera, PPE (hard hat, hi-vis shirt).
- Drone: opening harbour wide, crane on barge from the water, sunset skyline (≈8 drone shots). Gimbal along boom sections, low angle under the boom, hook against the sun, cab interior with operator, macro hands (wrench, finger on touchscreen, harness clip), real lift off a barge.
- Location identity: two famous bridges in many backgrounds = "this is a real city project". No timelapse, no CGI, no graphic data cards.

## Transitions
- Hard cuts only; title strip wipe; fade into the logo card.

## Sound
- Light corporate guitar/electronic bed under the voice, ducked; short music-only passages at 0-7 s, 38-42 s, 137-143 s and 174-178 s mark sections. Integrated -20.7 LUFS, LRA 6.9 LU, true peak -4.1 dBTP. No drop-outs; 0.75 s silence at the very end.
- Hits are speech onsets and music accents (+27 to +30 dB at 26.7, 54.95, 77.95 s). Cut-to-onset 47 % vs 53 % chance (cuts follow sentences).

## What makes it credible
- The buyer says it, with his name, title and company, on the real site, with the real project explained (water level, foundations).
- One killer feature explained in operational terms (barge tilts -> crane follows -> no hook swing) and shown on the real screen and a real lift.
- Famous landmarks behind make the place checkable.
- Missing: no numbers on screen (lift capacity, time saved), no captions.

## Recipe (real footage + HTML/GSAP)
- One customer, 20 min interview on site, cut to 12-15 bites of 3-5 s; b-roll 2-3 s between almost every bite; ASL ≈2.7 s flat.
- Title: `<div class="tbox"><h1>Model 1300<br>Crawler Crane</h1><div class="strip"><img logo></div></div>` `top:0;left:2.5vw;background:#fff;padding:3vh 2vw` `h1{font:700 5.5vh Barlow;line-height:1.05}` `.strip{background:#FFD000}`; `gsap.from('.strip',{scaleX:0,transformOrigin:'left',duration:.5,delay:.3})`.
- Super: white box `font:700 4.5vh Barlow` + role 400, `bottom:8vh;left:4vw`, `clip-path` wipe 0.35 s, hold 5 s, first appearance only.
- Shot list: harbour/site drone opener, speaker arms-crossed intro, client logo on shirt, feature on screen (finger on UI), the same feature as a real lift (hook + load + barge), assembly hands, sunset drone ending.
