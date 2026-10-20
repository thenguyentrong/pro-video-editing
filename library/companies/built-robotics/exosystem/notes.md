# Building New Tools: the Exosystem - Built Robotics  (Built Robotics, 2021-12-07, 1:43, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=drB3-KtpbO4
Purpose: product launch film (retrofit kit that makes an excavator autonomous)
One-sentence point: The Exosystem turns any excavator into an autonomous digging robot, with an eight-layer safety system, and it continues the tradition of builders inventing their own tools.

## Structure
- 0.0-10.9 (0-11 %) heritage hook: an operator pulls on leather gloves, a hand picks a wrench from a tool drawer, a hammer, the man puts on a white hard hat and hi-vis vest, low close-up of excavator tracks in dust. VO: we still build like our grandparents, only the tools change.
- 10.9-24.5 (11-24 %) the product: the black-and-yellow Exosystem box (logo), top-down drone of a yellow excavator, the cab with the kit mounted, excavator digging a trench, a service truck crane lifting the box onto the excavator roof (installed on site).
- 24.5-36.8 (24-36 %) spec block (dark): the box in a dark workshop, macro of the GPS antenna, light flares, the giant "BUILT" letters on the wall; VO lists computer, RTK GPS, solar panels, all-weather design; operator flips a switch from manual to AI mode.
- 36.8-57.5 (36-56 %) "it can dig": operator in the cab flips the switch and climbs out, empty trench line, low trench POV of the bucket, dust, a wide of the lone excavator digging on a huge empty field (3.8 s), more bucket close-ups, rear view of the kit with the CAT logo.
- 57.5-78.6 (56-76 %) safety block: VO admits the 80,000 lb robot is scary; cameras, radar, blue LEDs at night, trench with a safety cone line, the real planning UI on a laptop in a truck (trench path in blue, coordinates table, yellow "save" button), a red "STOP ROBOT" button on a post and a hand slamming it, excavator working, a boy in a field, hands putting a seed/ball in soil.
- 78.6-94.6 (76-92 %) legacy: the boy and the excavator at dusk, a worker walking the field, the operator standing (portrait, 4 shots), top-down drone of a bridge, a city, a house frame, the excavator trench top-down. VO: builders before us invented tools; now it is our turn.
- 94.6-103.1 (92-100 %) dirt top-down, fade to black, "BUILT ROBOTICS" logo fades in and out on black (≈6 s).

## Cut rhythm (adaptive detector; scene missed 10 cuts in the dark workshop and dust shots)
- 56 shots in 103.1 s. ASL 1.84 s, median 1.60 s, 14 % under 1 s, 9 % over 3 s, 32.6 shots/min.
- ASL per quarter 1.72 / 1.43 / 1.72 / 2.34 s. 5-8 cuts per 10 s throughout, 2 in the end.
- Longest: logo tail 8.5 s, lone excavator wide 3.8 s, crane install 3.4 s. Shortest 0.52-0.76 s (bucket and dust inserts).

## Typography
- No supers or captions. All words are VO. Branding is physical: "BUILT ROBOTICS" printed on the kit, huge 3D "BUILT" letters on a workshop wall, the CAT logo on the machine.
- End logo: white condensed bold wordmark "BUILT" (≈10 % H) over spaced "ROBOTICS" (≈3 %), centred on black, slow fade in / out. Closest free font: Oswald Bold / Barlow Condensed Bold.

## Colour/grade
- Warm, hazy, dusty desert grade (beige sky, golden hour), slightly lifted blacks; the yellow of the machine is the strongest colour. Spec block in a dark workshop with blue light and lens flares. Night shot with blue LEDs.

## Camera/shots
- Cinema look: shallow depth of field, low angles at track and bucket level, a camera inside the trench, slow dolly moves, top-down drone (excavator, bridge, city, house frame).
- Real machine, real site (open field), real install by a crane truck. Autonomy shown by the operator stepping out and the empty cab, not by labels.
- One real software UI shot (laptop in a truck), one physical E-stop shot. No speed labels; speed looks real time.
- Persons in PPE (white hard hat, hi-vis).

## Transitions
- Hard cuts; fade to black and logo fade at the end.

## Sound
- Male VO (warm, plain-spoken), cinematic piano/strings building to drums. Integrated -18.8 LUFS, range 4.6 LU, true peak -0.8 dBTP. No drop-outs; hits at 4.7 s and 11.1 s (product reveal), 27 s (spec block). 1.4 s silence on the logo end.

## What makes it premium
- Heritage framing (hands, gloves, tools) before any technology.
- Facing the fear head-on: one block admits the danger, then lists every safety layer with a physical shot for each (camera, radar, LEDs, barrier, geofence UI, E-stop).
- Physical branding on the machine instead of on-screen text.
- Real install on site (crane truck) proves "retrofit any excavator".

## Recipe (real footage + HTML/GSAP, Hyperframes)
- 50-60 shots of 1.2-2.5 s, one 3-4 s lone-machine wide per act, logo 5-6 s.
- Acts: heritage hands (10 %) -> product reveal + install (14 %) -> spec list over macros (12 %) -> it works (20 %) -> safety list, one shot per layer (20 %) -> legacy aerials (16 %) -> logo.
- Spec list without text: one macro per spoken spec, 1.0-1.5 s each. If you add labels, use Barlow Condensed 600 caps 3vh, bottom-left, letter-spacing .08em, cut in/out with the shot.
- Logo: `gsap.fromTo(logo,{opacity:0},{opacity:1,duration:1.2})`, hold 3 s, fade out 1 s on black with music tail.
- Shots to film: gloves on, tool drawer, hard hat on, track macro in dust, crane install, operator flips switch and leaves cab, trench-level bucket, lone machine wide on empty field (drone), UI on laptop in truck, E-stop press, operator portrait.
