# Boston Dynamics - style

Examples (official @BostonDynamics uploads):
| Example | Date | Length | Shots | ASL | Median | Sub-style |
|---|---|---|---|---|---|---|
| [atlas-product-features](atlas-product-features/notes.md) | 2026-01 | 1:43 | 27 | 3.83 s | 2.59 s | CGI spec film with datasheet overlays |
| [atlas-goes-hands-on](atlas-goes-hands-on/notes.md) | 2024-10 | 2:53 | 2 | 86.3 s | - | one-take autonomy demo, robot-view PiP |
| [beginning-of-your-tomorrow](beginning-of-your-tomorrow/notes.md) | 2026-01 | 2:04 | 102 | 1.22 s | 0.92 s | brand story: archive -> deployments -> vision |

## Three sub-styles, three jobs
1. **Proof (demo):** one uncut take, real lab, real sound, small "Fully Autonomous" label, PiP of the robot's camera with a segmentation mask. No music, no cuts, no claims. Credibility = nothing hidden.
2. **Specs (product features):** clean CGI, one spec per shot, datasheet typography, yellow tracked graphics, staccato sound with a hit per number.
3. **Story (brand film):** VO, fast montage (median 0.92 s), archive with original watermarks, real customer deployments, a short clearly-stylised CGI vision, then a real hero shot.

## How they show a real machine working
- Medium-wide, eye-level, full body + workpiece + target in frame (hands-on: always the whole cell). Close-ups only as inserts (grippers, hands).
- No slow motion and no speed ramps on demo footage; slow push-in only for the brand hero shot.
- Sound of the machine is left raw in demos (room tone, contact transients, faint motor whine); brand films cover it with music.

## How they show data/specs
- `[label]` small in brackets + big metric value + thin divider + small imperial value; white Montserrat-like sans; brand-yellow leader lines, dimension lines and floor rings that touch the real object; 3-5 s per spec; a sound "click" after a micro-silence.
- In demos the "data" is perception, not numbers: robot camera inset + mask.

## How they keep it credible
- Real vs. render is separated by sub-style, never mixed inside one shot: demo = 100 % real one-take; spec film = 100 % CGI; brand film = real first, CGI vision last (~9 % of runtime) and visibly stylised.
- Archive keeps its original watermarks and low resolution.
- Label autonomy explicitly ("Fully Autonomous").

## Recipe (real footage + HTML/GSAP) for a construction-robot startup
1. Demo cut: one gimbal take of 60-150 s on the real site, whole machine in frame, raw sound, label `Fully autonomous` (Inter 600, 2vh, bottom-right), optional PiP of your sensor view (33vw, left) with a mask colour.
2. Spec cut: 5-7 locked shots of 3-5 s; one spec per shot using the bracket/value/divider/alt block; SVG leader line in one brand colour to the tool tip; click SFX after 0.2-0.4 s of silence.
3. Story cut: VO script "We asked... we built... now", archive photos in windows on black, real customer site footage, max 10 % render vision at the end, real hero push-in 8-10 s, logo 3 s on black.
