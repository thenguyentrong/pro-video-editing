# Bauma 2025 - Hands on the future  (Liebherr, 2025-05-23, 1:42, 16:9 with ≈2.35:1 letterbox, YouTube @Liebherr)
URL: https://www.youtube.com/watch?v=MtHXibXIo2w
Purpose: trade-fair recap / event brand film (world's largest construction-machine fair, Munich)
One-sentence point: At bauma, Liebherr shows that its future technology (hydrogen, electric, digital, autonomy) comes from working hands-on with partners, presented by its leaders on a stand full of giant machines and visitors.

## Structure (music + short soundbites from 5 managers)
- 0.0-8.4 (0-8 %) dawn opener: stand lit purple at night, title card top-right (white box, "Bauma 2025 / Hands on the future", logo, yellow strip), then 7 fast low-angle crane/boom shots against blue-hour sky (0.3-1.4 s), glass atrium.
- 8.4-12.9 (8-13 %) daylight aerial over the fair grounds, cranes towering.
- 12.9-31.9 (13-31 %) board member soundbite (name super) on the stand, cranes behind; b-roll: hydrogen excavator "H2" door, booms, crowds, executives at a machine, cab; product manager soundbite.
- 31.9-43.5 (31-43 %) demo field from above (excavators digging), innovation award on stage (handshake, certificate), visitors, crane lifting a load; claim: the machines combine performance, efficiency, durability.
- 43.5-63.1 (43-62 %) product management soundbite; tablet/configurator, toy-scale models, hydrogen/NH3 concept engine (lens flare), components, a fridge display (Liebherr appliances) - breadth of the group; head of strategy soundbite.
- 63.1-82.7 (62-81 %) energy peak: digital twin/rendered machine on a video wall, people filming with phones, selfies, merchandise, a burst of 0.16-0.4 s flash cuts (74.2-75.9 s) into crowds, career lounge signage (recruiting).
- 82.7-94.3 (81-92 %) e-mobility manager soundbite, wheel loader, components, people at screens, hands on parts.
- 94.3-102.2 (92-100 %) hands-on graphic title "Hands on the future" over a hand on a cube, zoom-blur aerial, end card: isometric cube logo built from photo facets + yellow facet, stacked italic title.

## Cut rhythm
- 80 shots in 102.2 s (73 detected + 6 verified dark dawn cuts from the adaptive detector). ASL 1.28 s, median 0.94 s, 52.5 % under 1 s.
- ASL per quarter 1.34 / 1.28 / 0.91 / 1.60 s. Densest 70-80 s (15 cuts per 10 s, flash burst of 0.16-0.2 s shots); otherwise 5-9 per 10 s.
- Longest 7.89 s (end card), 4.36 s (board member soundbite), 3.68 s (soundbite). Soundbites are cut short (2.5-4.4 s), b-roll between them 0.5-1.5 s.

## Typography
- Corporate grotesk (Liebherr house face; free: Barlow or Archivo, medium). Title card: white box ≈46 % H tall at top-right of the image, two 500-weight lines ≈4.2 % H between two thick black rules, logo below, yellow strip with "The Group" ≈1.5 %. Holds ≈3 s, cuts in.
- Name super: small white box, name 700 ≈2.6 % H + role 400 ≈2.6 % H in black, sentence case, positioned at ≈55 % x / ≈72 % y (next to the speaker's chest, inside the image area, not on the black bar). Roles in German (board member, product management, strategy office). Holds 2.5-4 s, box wipes in from left.
- End card: italic bold stacked "Hands / on the / future" rotated with the cube facet angle, ≈6 % H per line, black on light grey; cube logo made of photo facets + one yellow facet (#FFD000-like).

## Colour/grade
- Letterboxed ≈2.35:1 inside 16:9 (black bars ≈12 % H each). Crisp, punchy daylight grade, deep blue sky, Liebherr yellow and white machines; dawn opener in blue/purple with stand lights. Interviews warm, very shallow focus (cranes as bokeh). Lens flares on purpose (engine shot).

## Camera/shots
- Extreme low angles up booms and lattice cranes (scale), aerial drone over the fairground with demo field, top-down drone on excavators digging, gimbal through crowds, macro hands on components, phone-in-hand POV. Interviews: medium close-up, centre-right, 85 mm, shallow DOF.
- Real event footage; one rendered machine on a video wall (shown as a screen, not composited). No timelapse, no data cards, no speed labels.

## Transitions
- Hard cuts only, plus a radial zoom-blur on the final aerial and graphic wipes for the end card. Flash-cut burst (≈6 shots of 0.16-0.2 s) as the energy peak at ≈73 % of runtime.

## Sound
- Driving cinematic-electronic track, loud and compressed: integrated -10.0 LUFS, LRA 2.7 LU, true peak +0.3 dBTP (clipping risk). Speakers in German with English subtitles available on YouTube; soundbites sit on top of the music without ducking pauses.
- Biggest hits +19.5 dB at 11.0 s (aerial reveal, first soundbite), +18.6 dB at 82.95 s (final section), +17.2 dB at 43.75 s. 5.05 s silence at the end (97.2-102.2 s) under the end card. Cut-to-onset 32 % = chance.

## What makes it premium
- Scale through angles: lens at boom foot, sky behind, letterbox - the machines feel like architecture.
- Fair film that sells the group, not one product: leaders, award, crowds, careers, appliances in 100 s.
- Simple, strict brand frame: white box, black rules, yellow accent, one cube logo.

## Recipe (real footage + HTML/GSAP)
- Letterbox: `.bars{position:absolute;inset:0;box-shadow:inset 0 12vh 0 #000, inset 0 -12vh 0 #000}`.
- Title card: `<div class="tc"><hr><h1>Event 2026<br>Your claim</h1><hr><img logo><div class="strip">The Group</div></div>`; `font:500 4.2vh Barlow`; `hr{height:.6vh;background:#000}` `.strip{background:#FFD000;font:600 1.5vh Barlow}`; hard on, hold 3 s.
- Super: white box `padding:1vh 1.2vw; font:700 2.6vh Barlow` + role 400; `clip-path:inset(0 100% 0 0)` -> `inset(0)` 0.35 s; hold 3 s.
- Cut b-roll at 0.5-1.5 s, soundbites 2.5-4.5 s, one 0.16-0.2 s flash burst before the last soundbite; end on 8 s logo with silence.
- Shot list: 6 low-angle boom shots at dawn, 1 drone reveal, 1 top-down drone of machines working, 5 crowd/handshake shots, 4 macros of hands on parts.
