# iOS 26: Introducing Liquid Glass  (Apple, 2025-06-09, 4:34 file / 4:28.8 content, 16:9, YouTube — WWDC25 keynote segment)
URL: https://www.youtube.com/watch?v=jGztGfRujSE
Purpose: keynote feature segment (presenter + demo film)
One-sentence point: Apple's design chief introduces "Liquid Glass", a new universal design material, and shows it on every device.

## Structure
- 0-12 s **Cold open**: Apple Park architecture — curved glass roof, spiral stair, white curved surfaces (music only, ASL ~3 s, slow moves).
- 12-51 s **Presenter intro**: Alan Dye in the Apple Park design studio, wide shot with lower third (14-19 s) → medium shot; B-roll of iPad/Mac/iPhone in use (25-30 s). Story: "Software is the heart and soul… iOS 7… next chapter".
- 52-70 s **Material teaser**: abstract blue glass waves and glass "9:41" numerals (renders), glass app-icon layers, the new Home Screen on a floating phone.
- 70-104 s **Universal design**: presenter, then all platforms (Mac dock, Watch, TV, Vision Pro, iPad), physical glass objects on studio desks, magnifier lens over text (92-96 s).
- 104-112 s **Name reveal**: glass lens forming in the dark (104-109 s) → "Liquid Glass" title in glass letters on white (110-112 s).
- 113-268 s **Demo run**: UI controls in glass (slider, toggle, tab bar), Lock Screen clock, media players, Safari, Photos, tilted-phone renders on white (150-166 s), designers' hands with glass prototypes ("hello" in glass, 236-244 s), Mac, Control Center, presenter returns 5× as anchor (145, 186, 205, 255 s).
- 264-268 s **End**: soft Apple logo with an iridescent tint on white.

## Cut rhythm
- 70 shots in 268.8 s → **ASL 3.84 s**, median 2.74 s; quarters 4.20 / 2.92 / 4.80 / 3.36.
- No shot < 1 s; 46 % > 3 s. Longest: presenter 20.7 s (31-52 s), tilted-phone render 16.6 s (150-167 s), name reveal 10.6 s.
- Felt pace is faster: inside many shots the UI animates or morphs every 1-3 s.
- Cuts on audio onsets 42 % vs chance 49 % → edited to speech, not to the beat.

## Typography
- Lower third: 2 lines right-aligned at x ≈ 95 %, y 81-91 %, white SF Pro; name semibold, title regular ("VP, Human Interface"); cap ≈ 3 % H; on 14-19 s only, no box, no bar.
- Title card: "Liquid Glass" as glass-material letters (white, embossed, faint rainbow refraction) on white, centred, cap ≈ 13 % H.
- Everything else is real UI text inside the demos.

## Colour / grade
- Natural, bright, airy: white studio, daylight through glass, green trees outside, beige wood desks.
- Demo renders on white/light-grey sweeps; blue/teal glass waves as the "material" colour.
- Only 7 % of frames mostly empty — busier than the product films.

## Camera / shots
Presenter on a slow dolly in two framings (wide, medium-close), clean 3D UI renders on floating/tilted devices, macro of real glass prototypes, hands using devices (top-down and over-shoulder), architecture B-roll.

## Transitions
Hard cuts to and from the presenter; morphs and dissolves inside renders (glass shapes morph into UI); light-leak/flare into the name reveal.

## Sound
- Opens with "uplifting electronic music" (captions), then presenter speech carries everything; music bed low under speech.
- Integrated **−19.2 LUFS** (quieter than the ads; speech-led). Short silences 17-19 s are speech pauses.
- Hits 236.2 s (+31 dB) and 256-265 s on the glass-prototype and finale shots.

## What makes it premium
- The presenter is filmed like a documentary (natural light, real workspace, no podium), not like a stage talk.
- The abstract idea (a material) is shown first as an art object, then as real UI.
- Each demo shot shows one control, isolated on white, moving smoothly.
- Physical glass prototypes make software feel crafted.

## Recipe (real footage + HTML/GSAP)
- Presenter: two-camera interview (wide 24 mm + 50 mm), natural window light, ASL 6-20 s while talking; cut to B-roll every time a new noun is named.
- Lower third: Inter/SF Pro, name 600 / title 400, `font-size: 3.9vh` (cap ≈ 3 % H), white, right-aligned at `right: 5vw; bottom: 9vh`, no background; `gsap.from(lt,{opacity:0,duration:.5})`, hold 5 s.
- Glass UI in HTML: `backdrop-filter: blur(18px) saturate(1.8); background: rgba(255,255,255,.18); border: 1px solid rgba(255,255,255,.5); box-shadow: inset 0 1px 0 rgba(255,255,255,.6), 0 8px 24px rgba(0,0,0,.12)`; animate scale/position with `ease:"elastic.out(1,.6)"` for the "liquid" feel.
- Glass title: white text with `text-shadow: 0 2px 4px rgba(0,0,0,.15), 0 -1px 0 #fff` and a faint rainbow `background-clip:text` gradient at 20 % opacity.
- Mix speech at −19 to −16 LUFS, music bed −30 LUFS under speech.
