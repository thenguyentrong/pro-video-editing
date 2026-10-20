# ANYbotics - style

Examples (official @anybotics uploads):
| Example | Date | Length | Shots | ASL | Median | <1 s | Shots/min | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|---|
| [superior-robot-mobility](superior-robot-mobility/notes.md) | 2023-10 | 2:01 | 37 | 3.26 s | 2.56 s | 2.7 % | 18.4 | -19.0 | expert-interview tech film: sim → real + point-cloud overlay → field test |
| [rapid-response](rapid-response/notes.md) | 2024-09 | 1:29 | 35 | 2.55 s | 1.68 s | 5.7 % | 23.5 | -16.8 | feature launch: staged emergency, operator + real app, music only |
| [aker-bp-offshore](aker-bp-offshore/notes.md) | 2023-12 | 2:04 | 6 (4 content) | 20.65 s | 5.98 s | 33 % (black lead/tail) | 2.9 | -13.5 | customer log film: one 23 s take + one 88.6 s operator screen |

## Sub-styles
1. **Tech explainer with named experts:** CTO + professor interviews (≈55 % of runtime) cut every 2-5 s against openly synthetic simulation renders, real takes, and real takes with the robot's height-map point cloud on top; ends on the inspection job (gauge + green tick).
2. **Feature launch as a mini-story:** alarm → operator at a desk → robot into fog → real app full screen → firefighters take over. Coral title card at ≈17 % of runtime on the biggest hit (+24.7 dB). No voice, no supers.
3. **Customer deployment log:** "PROJECT / DAY 3" title over a locked-off real take, then an uncut screen recording of the remote app beside the partner's digital twin; co-branded white end card.

## House rules
- **Coral brand frame:** full-frame coral red (≈#EE5A5A) for logo stings, title cards and end cards; white wordmark/symbol; city line "Zurich | San Francisco".
- **Robot is red (or blue for the ATEX X model)** - the only saturated colour in grey plants.
- **Show the robot's data, not graphics:** point clouds, height maps, lidar maps, robot camera, thermal readouts and the real operator UI. Overlays are the robot's own output, tracked to the real picture.
- **Sim is labelled by its look:** grid floors, white void, hundreds of copies - never confused with real.
- **Industrial places, real weather and light:** process plants, offshore platform, refinery at night, gravel, rock, a public lakeside park.
- **Small type, few words:** name supers ≈2 % role caps + ≈3.5 % name on a coral box; title cards ≈7 % cap height; everything else is UI.

## How they show a real machine working / keep it credible
- Long locked-off takes for "first steps" (23 s door exit) and uncut operator screens (88.6 s).
- Teleoperation is shown openly as a feature (Rapid Response): the operator, her screen, the joystick-style app and the stop button are on camera; the app's mode field reads MANUAL in one step and AUTO in another. But no overlay label explains which shots are autonomous.
- No speed labels in any of the three films; long screen recordings are not marked as real time or sped up.
- Customers and partners co-sign (logos, day-stamped PoC title); experts with titles carry the claims.
- Field/inspection film ingredients: ATEX-rated model on a real hazardous site, a door or stair as the first obstacle, robot camera + map + digital twin, one inspection result (gauge tick, thermal min/max), co-branded end card.

## Contrast with other makers in the library
- Closer to Boston Dynamics/Siemens (real site, data views, named people) than to the humanoid launch teasers; less cinematic than Figure or Apptronik, more "engineering record". Music-only feature film, interview-led tech film, raw log film - no hero CGI of the product.

## Recipe (real footage + HTML/GSAP)
1. Pick one job (inspection round, emergency look-in). Shoot one locked-off real take of the first obstacle (door, stairs), 20-30 s.
2. Record the real operator app (OBS) for the whole mission; cut it full frame 2-4 s at each decision, or keep one long uncut capture with a third-person video inset (≈35 % W).
3. Overlay only the robot's real data (point cloud as alpha video, opacity .85, fade in 0.4 s after 1 s of clean picture).
4. Inspection result: 2 px green circle tracked on the gauge + tick badge `back.out(1.7)` 0.25 s, or the thermal frame with min/max.
5. Add what ANYbotics leaves out: a mode label (`MANUAL` / `AUTONOMOUS`) and a speed label (`1X` / `4X`) in the top-right corner, Inter 600 2vh caps on a `rgba(0,0,0,.55)` pill, switched with `tl.set` at the exact frame.
6. Brand frames: full-colour title card (Barlow SemiBold 9vh line, 2 lines) on the biggest hit; end card 3-4 s; co-brand card on white for customer films. Blur personal data in UI captures.
