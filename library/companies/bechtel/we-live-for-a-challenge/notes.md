# We Live for a Challenge  (Bechtel, 2023-02-02, 1:37, 16:9, YouTube, official Bechtel Corporation channel)
URL: https://www.youtube.com/watch?v=jHQGhaeRJsU
Purpose: brand / recruiting anthem (125-year campaign)
One-sentence point: Bechtel people live for the hardest projects, because a better world has to be built, and they have done it for 125 years.

## Structure (97.3 s)
- 0-8 (0-8 %) hook: top-down drone of LNG tanks, plant from above, red machine on a mountain road, motorway paving, worker in orange hi-vis from behind; caption "Challenges".
- 8-40 (8-41 %) relay: seven employees (office and field, hard hats on site) each say one short line straight to camera; drone cut-aways of a dam and a viaduct between them.
- 40-47 (41-48 %) turn: space shot of Earth at night, extreme close-up of an eye, then a building under construction.
- 47-64 (48-66 %) list: one adjective per shot, 1.0-1.3 s each, over project b-roll (powered, connected, sustainable, safe, secure, reliable, smart...) - substations, wind farm, nuclear plant, roundabout at night, welding.
- 64-84 (66-86 %) who: the employees name the roles (designers, engineers, scientists, field leaders, craft professionals); aerial motorway through mountains.
- 84-94 (86-97 %) emotion + heritage: backlit family scene in a warm room (4.7 s, longest shot), last two lines to camera.
- 94-97.3 (97-100 %) logo builds on white (ring + wordmark + URL), 3.1 s of silence.

## Cut rhythm
- 50 shots, ASL 1.95 s, median 1.67 s, 2 % under 1 s, 30.8 shots/min. ASL per quarter 1.87 / 1.74 / 1.43 / 2.70 s.
- Longest 4.7 s (family scene), 3.75 s (employee), 3.4 s. Even 3-7 cuts per 10 s, densest in the adjective list (7 per 10 s at 50-60 s).
- Each spoken line = one shot (1.5-3 s); b-roll inserts 1.0-1.5 s.

## Typography
- Burned-in captions of every spoken line: humanist sans (Open Sans look; free: Open Sans 400), white, sentence case, cap height ≈2.9 % H, centred at y ≈86 %, no box, soft shadow. One line, 2-6 words.
- Name tags are visible on vests and hard hats, but no on-screen supers.
- End card: Bechtel ring logo ≈20 % H on white, URL below ≈2 %.

## Colour/grade
- Clean, slightly warm commercial grade; skin-friendly office light with shallow depth; saturated drone b-roll; warm amber for the family scene. No letterbox.

## Camera/shots
- Employees: locked medium shots, centred, eye level, 85 mm-ish shallow depth, direct address. Field employees in hard hats, safety glasses, hi-vis vests on real sites (desert mine, plant).
- B-roll: top-down drone (tanks, plants), drone over dam/viaduct/motorway, ground-level crew details (welding, cables), stock-like inserts (Earth from space, eye macro, family).

## Transitions
- Hard cuts only. Logo builds by drawing the ring.

## Sound
- Relay VO by the employees (no narrator) over a rising piano/strings bed; integrated -18.9 LUFS (quiet), LRA 4.2 LU, true peak -2.1 dBTP.
- Hits on each new speaker's first word (+21 to +34 dB rises); 0.65 s drop-out at 91.7 s right before the last line, then 3.1 s of silence under the logo.
- Cut-to-onset sync 12 % vs chance 42 %: cuts sit on speech, deliberately off the music beat.

## What makes it premium
- Relay narration: many real employees, one sentence - diverse, credible and fast.
- One word per b-roll shot for the list section; captions make it work with sound off.
- Field people on real sites in full PPE beside office people.

## Recipe (real footage + HTML/GSAP)
- Film 6-8 employees, each says 3-4 lines from one script; lock framing (centred MS, same lens) so the cuts feel like one voice.
- Cut: one line per shot 1.5-3 s; b-roll inserts 1.0-1.5 s; adjective list 1.0-1.3 s per word.
- Captions: `font:400 2.9vh 'Open Sans'; color:#fff; text-shadow:0 0 .6vh rgba(0,0,0,.6); bottom:11vh; text-align:center`, `tl.set` on the cut, no animation.
- Sound: duck music to -24 LUFS under voices; 0.6 s drop before the last line; logo on white with 3 s of silence.
