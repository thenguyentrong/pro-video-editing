# Skateboarding this NYC Tunnel is Legal Once a Year  (Casey Neistat, 2026-08-20, 9:34 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=s-ZSuar3ihs
Purpose: event / adventure vlog with a sponsor integration (a 360 camera)
One-sentence point: On the yearly car-free streets day Casey and a friend skate through a road tunnel that is open to people only once a year, filmed mostly on the sponsor's 360 camera.

Data note: first 300 s analysed (trimmed with ffmpeg). The default scene detector missed 8 cuts in handheld/fisheye footage; cuts are from the adaptive detector plus one verified scene-only whip cut (287.2 s). No hidden jump cuts were found inside the 34.7 s desk take with a more sensitive pass. Speech timings from a local speech-to-text pass (±0.5 s).

## First 30 s (hook)
- 0.0–3.9: locked-off wide of a building entrance; Casey walks out with his board.
- 3.9–6.9: fisheye low angle, he looks up and calls to a friend; first spoken line at ≈5.3 s.
- 6.9–10.7: extreme low angle (360 camera) of the facade, the friend leans out of a window.
- 10.7–12.1: Casey gestures "come down" (the invitation, ≈9–12.5 s of talk).
- 12.1–24.2: one 12.1 s 360 reframe: facade tilt-down to the door, the friend comes out, both skate off along the sidewalk. No speech from ≈13 s to 44.5 s: music carries it.
- 24.2–28.9: overhead "third-person" 360 follow shot of both skating down a pink bike lane.
- 28.9–33.5: sponsor reveal as a physical title: a handwritten sticky note on the product box, fingers tapping it.
- (after the hook) 33.5–42.5 product shots on black, a tiny-planet selfie; 42.5 street selfie; the event and its rules are explained to camera from ≈44.5 s; the real street sign of the event at 51.4 s acts as the title.
- Cuts in 0–30 s: 6.

## Structure (first 300 s)
- 0–42.5 hook + sponsor card + product shots.
- 42.5–80 the event explained in fisheye selfies on the closed avenue, the event sign (51.4–53.3 s), a runner, a top-down 360 shot, spectators.
- 80.2–111.3 sit-down at his studio desk (two takes, 15.6 s longest): the sponsor's camera explained with three cameras on the desk; dry voice, no music.
- 111–127 back on the avenue, selfies on a ramp.
- 127–206 the tunnel: entrance, riding inside under sodium light, a maintenance staircase and grates explored with the friend (fisheye, POV arm, 360 overhead), cyclists with lights.
- 206.0–240.7 a 34.7 s desk take (longest shot): more on the sponsor's camera, dry voice with 0.3–1.25 s pauses to −48…−50 dBFS.
- 240.7–287 avenue again: viaduct, aerial-looking 360 shots over Park Avenue, event signage, park selfies.
- 287.2 whip cut to a stage with a band; 295.5 the event banner.

## Cut rhythm
46 shots in 300 s, ASL 6.52 s, median 4.51 s, 2.2 % under 1 s, 73.9 % over 3 s, 9.2 shots/min — the slowest of the three because the 360 camera is reframed inside long takes (moves replace cuts). ASL by quarter 5.0 / 6.8 / 6.8 / 6.3 s. Longest 34.7 s (206.0 s desk), 15.6 s (95.8 s desk), 14.6 s (53.3 s selfie). Shortest 0.96 s, 1.08 s, 1.42 s. Cuts per 10 s mostly 1–2, max 4 (190–200 s, tunnel stairs). Cuts on onsets 47 % vs 38 % chance.

## Typography
- No added type in the first 300 s. Titles are physical: a handwritten sticky note on the product box (sponsor), the real event street sign (title), event banners and wayfinding signs (place).

## Colour/grade
Bright, saturated summer daylight; tunnel left in its sodium yellow/orange; desk set warm with practical lights and colourful shelves. Strong fisheye/360 distortion is kept as a look. No letterbox, no grain.

## Camera/shots
360 camera everywhere: invisible-stick third-person follow shots from above, tiny-planet selfies, extreme low angles, reframed tilt moves inside one take. Fisheye selfies at arm's length. Locked-off wide for the very first shot. Desk sit-down with a wide lens at table height, product in the foreground.

## Transitions
Hard cuts; one whip-blur cut (287.2 s); camera moves inside 360 footage replace many cuts.

## Sound
−14.0 LUFS integrated, LRA 6.1 LU, true peak +0.7 dBTP (480p re-encode). RMS median −18.9 dBFS. Music under the outdoor sections (p10 within 2–8 dB of the median); desk takes dry (p10 −44…−46 dBFS, 11 drop-outs of 0.3–1.25 s). Biggest rises +36…+40 dB inside the desk take (speech after pauses). No designed full silence.

## What makes it premium
- A rare, time-limited event = a natural hook (only once a year).
- The sponsor's product is the camera that makes the film's best shots, so the integration earns its place.
- Physical titles (sticky note, real signs) instead of graphics keep it hand-made.
- Long 360 takes with reframed moves feel like crane/drone work from one person.

## Recipe (real footage + HTML/GSAP)
- 0–12 s: 4 quick set-up shots (locked wide, fisheye, low angle) with a short invitation line at ≈5 s.
- 12–29 s: one long move shot (12 s) + one overhead follow (4.7 s) on music, no talk.
- Sponsor card at ≈29 s: a real handwritten note on the product, 4.6 s, then product shots on black.
- Premise to camera at ≈44 s; a real sign as the title.
- Sponsor explanation as separate dry desk takes (15–35 s) placed at ≈27 % and ≈69 % of the runtime, music off.
- If building in code, use no type layer at all; let `<video>` sources carry signs and notes.
</content>
</invoke>
