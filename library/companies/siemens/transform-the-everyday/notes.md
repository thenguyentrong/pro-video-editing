# Siemens: Transform the everyday  (Siemens, 2023-10-18, 1:31, 16:9 file with ~2.9:1 letterbox, YouTube @Siemens)
URL: https://www.youtube.com/watch?v=uIT02AZs5Is
Purpose: brand film (corporate campaign, "Technology to transform the everyday")
One-sentence point: Ask "can we do something about this?" and Siemens' digital twins, data and AI make it happen - for the climate, factories, cities and trains.

## Structure (cut list + English captions)
- 0.0-11 hook: a young woman photographs a smoggy city street (1-3 s), looks at her camera screen, faces camera: "Can we do something about this?" Overhead walkway (7-10 s): "Oh, there's definitely something that can be done about this."
- 11-18 gag: a professor at blackboards in a lecture hall, "By when?" "Our consensus says by 2030." Big mint-green digits "20 30" grow out of the frame and the colon blinks in -> "20:30" (14-17 s): "Let's make it 20:30 tonight."
- 18-26 transformation: drone over the traffic, the street turns greener; digital HUD tags in the city ("30 %", small icons, 20-21 s); "Let's combine the real and the digital worlds to make big changes for everyone."
- 26-31: the woman again ("Can we do something about the music?" - the score changes).
- 31-47 factory: a woman in a beige suit in a dark street; neon-cyan wireframe of a production line draws itself (36-37 s), she walks through a dark-blue virtual factory with wireframe robots and car bodies (39-43 s), then a real car (44 s) and a real parking lot of new cars (45 s): "First comes a digital twin of the factory, then you optimize it. So you can build the real one that produces batteries in record time."
- 47-69 city: a man on a rooftop at dusk, the city lights up with data tags (56-59 s), drone over towers; "...using data and AI to transform urban life to be smarter and more energy efficient." A cyclist at night (64-69 s).
- 70-83 train: a mother and son on a station platform, a wireframe train draws itself (72-75 s) and becomes a real hydrogen train (76 s), inside the train ("Can you do my homework for me?" "Please don't help him with that.").
- 83-87 tagline: Siemens infinity symbol (mint gradient) on navy (83 s), "Technology to transf∞rm the everyday" with the symbol replacing the "o" (84-86.5 s).
- 87-89 button: the first woman: "Wait, who are you?" (comedy tag).
- 89.4-91: 0.65 s silence, then SIEMENS wordmark on navy with a sting.

## Cut rhythm
- 40 shots in 91 s. ASL 2.27 s, median 1.78 s. ASL per quarter 2.27 / 1.75 / 2.84 / 1.90 s.
- Longest 6.64 s (11.92, lecture hall + "20:30" gag), 4.92 s, 4.80 s (tagline), 4.72 s. Shortest 0.84 s, 0.92 s.
- 5 % under 1 s, 25 % over 3 s: a dialogue pace - each line gets its shot.

## Typography (data on screen)
- "20:30": huge rounded geometric sans digits (Siemens Sans Black; closest free: Nunito Black / Inter Black), mint-to-cyan gradient (#00ffb9 -> #00e6dc, the Siemens "petrol/mint"), ~45 % of the picture height, composited over the live shot; the digits scale up and the colon appears ~1 s later.
- In-world HUD tags: small dark boxes with mint numbers ("30 %") and round icons, tracked to buildings - "data in the city".
- Wireframe line drawings in neon cyan for digital twins (factory line, robots, train) that "become" the real object by a cut or a morph.
- Tagline: white Siemens Sans Bold, sentence case, ~3.5 % frame height, centred on navy (#000028), the infinity symbol inside the word "transform".
- Wordmark: white SIEMENS ~10 % height on navy.

## Colour/grade
- Cinematic ~2.9:1 letterbox (picture 294 of 480 px). Day scenes warm and natural (orange-striped top of the hero as a colour anchor), digital scenes deep navy + neon cyan/mint, dusk scenes blue. Brand colours (navy, mint) carry the "digital" layer.

## Camera/shots
- Live-action with actors (comedy-light dialogue), drones over a real city (Bangkok-like skyline), CGI for twins (wireframes) and city data overlays.
- Real -> digital -> real structure in each chapter: problem in real life, digital twin in wireframe, result in real life.

## Transitions
- Hard cuts; wireframe build-ons; morph from wireframe to real object (train 74-76 s); colour shift of the street from grey to green.

## Sound
- Dialogue + score that changes on cue ("Can we do something about the music?" - the music switches at ~28 s). Integrated -12.7 LUFS. 0.65 s silence before the logo, then sting (+35 dB).

## What makes it premium
- A running dialogue device ("Can we do something about...?") ties 4 industries together.
- Clear visual code: wireframe cyan = digital twin, natural colour = real result.
- Humour (20:30 / homework / "who are you?") makes a B2B tech message human.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Letterbox: bars of 19.4 % top/bottom for a ~2.9:1 picture (or 12.2 % for 2.39:1).
- Wireframe twin: SVG line drawing of your machine/site (export edges from CAD/BIM), `stroke:#00e6dc; stroke-width:1.5; filter: drop-shadow(0 0 6px #00e6dc)`; draw with `stroke-dasharray`/`stroke-dashoffset` over 1.2 s (`ease:'power1.inOut'`, stagger .03 per path), hold, then cross-fade 0.4 s to the real footage of the same view.
- Data tags in the scene: `<div class="tag">` with a navy box and mint number, pinned to tracked points (keyframe x/y every 5 frames).
- Big number gag: `font: 900 45vh Inter; background: linear-gradient(90deg,#00ffb9,#00e6dc); -webkit-background-clip:text; color:transparent`, `gsap.from(digits,{scale:.6,autoAlpha:0,duration:.5,ease:'back.out(1.6)'})`, colon `gsap.set` 1 s later.
- Tagline: navy card, white Inter 700 3.5vh, logo symbol replaces a letter.
