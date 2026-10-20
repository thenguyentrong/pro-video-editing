# Helsing HX-2 Field Testing  (Helsing, 2025-11-10, 1:01, 16:9, YouTube @HelsingAI)
URL: https://www.youtube.com/watch?v=BZC8XuRqDHQ
Purpose: field-proof demo (capability reel from a test range)
One-sentence point: the strike drone is shown launched, guided and hitting targets on a real test range, with one capability label per shot and the operator kept in the loop.

## Structure (no voice, music + field sound)
- 0.0-2.1 hook: onboard-camera view diving onto an armoured target vehicle; 0.7 s drop-out (2.1-2.8).
- 2.1-4.3 title card: monospaced caps product name + "field testing", typed on, brand mark under it, on black (+26.3 dB hit at 3.05).
- 4.3-14.5 setup: launch from a tripod rail, target vehicles in savannah, a partner's ground robot and sensor turret with a label and the partner's logo, two operators at a laptop in a tent (faces blurred), a tablet.
- 14.5-23.4 machine view: the drone's real camera feed with reticle, compass tape and a coloured status bar with monospaced status text; a 2-line capability label bottom-left.
- 23.4-33.3 human in the loop: hand on a tablet with a label saying so, then manual acquisition UI, then automated terminal guidance UI, then the target seen from the ground.
- 33.3-52.0 capability montage (densest: 15 cuts in 40-50 s): launches, flights, moving targets, high wind, different warheads, a map briefing, soldiers carrying cases; one label per claim.
- 52.0-54.1 brand mark on black.
- 54.1-60.3 after the logo: one letterboxed wide shot (6.2 s, the longest) of a target vehicle being hit.

## Cut rhythm
- 51 shots in 61.3 s (adaptive detector + 3 fast cuts added by eye, 1 removed). ASL 1.20 s, median 0.90 s. ASL per quarter 1.09 / 1.70 / 0.90 / 1.09 s.
- 57 % of shots under 1 s, 6 % over 3 s. Cuts per 10 s: 8, 6, 6, 10, 15, 4.
- Longest 6.24 s (post-logo strike), 4.87 s (UI feed), 4.0 s (UI feed). The UI shots are the long ones; the field montage is fast.

## Typography
- Title: monospaced caps, ≈10 % of frame height, centred, typed on character by character; brand mark ≈8 % under it. Closest free: JetBrains Mono 700 / Space Mono.
- Capability labels: grotesk 700 caps, 2 lines ≈5 % each, bottom-left (x ≈3 %, y ≈88 %), white, no box, slight shadow; one label held across 2-6 shots of the same claim; some reveal letter by letter. Closest free: Inter 700.
- Partner credit: same label style + the partner's logo bug under it (≈4 %).
- Real UI text kept as-is: monospaced status line in a red or blue bar along the bottom (system words + clock time).

## Colour/grade
- Natural daylight, overcast, greens and ochres; UI shots keep their own white/red/blue. No stylised grade. The post-logo strike is letterboxed.

## Camera/shots
- Handheld and tripod on the range, action cameras on vehicles and the airframe (fish-eye), long lens on targets, aerial views. Faces of personnel are blurred.

## Transitions
- Hard cuts; black title and logo cards.

## Sound
- No narrator. Integrated -11.9 LUFS, LRA 8.5 LU, true peak +1.9 dBTP (hot). Hits: 3.05 s (+26.3 dB, title), 19.65 s (+23 dB), 38.35 s (+22.2 dB). Drop-outs 0.0-0.5 and 2.1-2.8. Ending: fade.

## What makes it premium (and credible)
- The machine's real view (UI with status text and clock) is on screen longer than any field shot.
- Human control is labelled, not implied; manual and automatic modes are shown as two separate UI states.
- A partner is named on screen with its logo.
- Blurred faces read as operational reality.

## Recipe (real footage + HTML/GSAP)
- Open on the most dramatic real POV for 2 s, then 0.7 s silence and a mono title typed at 0.04 s/char.
- One label per claim: `font:700 5vh/1.05 Inter; text-transform:uppercase; left:3vw; bottom:6vh; text-shadow:0 0 6px rgba(0,0,0,.5)`, 2 lines max; hold it while 2-6 shots prove the claim.
- Use the real UI recording for 4-5 s per state (manual, then automatic); never redraw it.
- Partner shot: label + partner logo PNG 4vh under it.
- Blur faces with a tracked mask (`filter:blur(14px)` on an ellipse) when people cannot be shown.
- Optional: one letterboxed 6 s proof shot after the logo.
