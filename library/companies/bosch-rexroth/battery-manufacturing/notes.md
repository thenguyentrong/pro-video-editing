# How do you achieve maximum precision and high speed in Battery Manufacturing?  (Bosch Rexroth, 2026-08-06, 2:15, 16:9, YouTube @BoschRexroth, [EN])
URL: https://www.youtube.com/watch?v=iU3n0HoLaTc
Purpose: trade-fair film (stand walk-through + one expert talking at a demonstrator, Battery Show Europe 2026)
One-sentence point: At the Battery Show, Rexroth's linear-motion team shows guides, axes, servo-press kits and module/pack assembly solutions, explained by its battery expert.

## Structure
- 0-4.5 hall entrance with show banners; title in cyan boxes ("Battery Show Europe 2026" / "Linear Motion Technology"), Rexroth logo bottom-right.
- 4.5-45 continuous gimbal walk through the stand (wide-angle, phone/action-cam look) with labels on each exhibit: "Always the Right Linear Guides and Axes" (≈11-13 s), "Smart Function Kit / Subsystem for Servo Presses" (≈22-25 s), a servo press pressing into a glass of green liquid (28-32 s), "Solutions for Module and Pack Assembly" (≈34-35 s), a gantry demo moving parts (36-45 s).
- 45-126 one long piece to camera: the head of the battery centre of competence (name super, 46-49 s) stands in front of a Cartesian demonstrator; the axes move behind him; printed stand labels give the numbers ("X-axis: up to 770 kg").
- 126-131 cyan/red stripe wipe, wide of the demonstrator with visitors.
- 131-135.5 Rexroth logo build from stripes on white.

## Cut rhythm
- Neither detector finds a hard cut (1 "shot" of 135.5 s). By eye (≈) the film is 3-4 pieces joined with whip/blur moves and one stripe wipe: walk-through ≈4.5-45 s (40 s), talk ≈45-126 s (≈81 s uncut), wide ≈126-131 s, logo.
- So: no edit rhythm at all; the walk and the talk are each one take.

## Typography
- Bosch Sans-like grotesk (closest free: Inter / Arial-like sans).
- Exhibit label: two stacked boxes bottom-left - navy box with bold white ≈4 % H title + navy box with regular ≈3.3 % subline - plus offset cyan, grey and Rexroth-red stripes behind them (x ≈2-58 %, y ≈80-97 %). In: stripes slide from the left, ≈0.4 s.
- Name super: same stripe system, name bold ≈3 %, role ≈2 %.
- The specs are printed on the demonstrator itself (black on white, ≈4 % H in frame) - the edit adds no data.

## Colour/grade
- Ungraded event look: bright hall, blue carpet, wood and glass stand; slight wide-angle distortion.

## Camera/shots
- One gimbal/phone walk-through, then a locked medium-wide talk with the moving machine behind the speaker. Lavalier audio with hall noise.

## Transitions
- Whip/blur moves in the walk, stripe wipe in brand colours, logo stripe animation.

## Sound
- Expert speech ≈124 s (≈206 words, ≈1.7 words/s, natural pauses) plus hall ambience and a light music bed. Integrated -14.8 LUFS, LRA 4.8 LU, true peak -0.4 dBTP. 1.4 s silence at the start; no drop-outs.

## What makes it credible
- Real stand, real visitors, real machines moving behind the speaker in one take.
- An expert with a real title speaks freely; numbers are visible on the hardware.
- Cheap to make: one camera, one afternoon.
- Weak: 81 s of talk without a cut-away; text is small; the walk-through is shaky in places.

## Recipe (real footage + HTML/GSAP)
- Shoot: 40 s gimbal walk past 3-4 exhibits (pause 3 s at each), then a 60-90 s locked talk with the machine running behind.
- Label: `<div class="lbl"><b>Smart Function Kit</b><span>Subsystem for Servo Presses</span><i class="s1"></i><i class="s2"></i><i class="s3"></i></div>`; boxes `background:#0b2a45; color:#fff`, `b{font:700 4vh Inter}`, `span{font:400 3.3vh Inter}`; stripes `#3fc1e6`, `#d0d6db`, `#e20015`, `height:1.5vh`, offset by 2-6vw; `gsap.from('.lbl i',{xPercent:-100,stagger:.06,duration:.35})`.
- Cut the long talk with 2-3 inserts of the machine (3-4 s each) to break the 81 s block.
