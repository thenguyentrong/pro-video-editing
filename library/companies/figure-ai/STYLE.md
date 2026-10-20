# Figure AI - style

Examples (official @figureai uploads):
| Example | Date | Length | Shots | ASL | Median | Sub-style |
|---|---|---|---|---|---|---|
| [figure-03-trailer](figure-03-trailer/notes.md) | 2025-10 | 0:48 | 23 | 2.09 s | 2.00 s | industrial-design macro teaser |
| [introducing-figure-02](introducing-figure-02/notes.md) | 2024-08 | 2:03 | 11 | 11.15 s | 4.96 s | long-take spec reveal -> real customer plant |
| [f03-at-bmw](f03-at-bmw/notes.md) | 2026-06 | 1:00 | 33 | 1.81 s | 1.38 s | real-site fleet montage on a beat grid |

## Sub-styles
1. **Design teaser:** macro materials on a warm-grey sweep, whole product only in the last third, loud electronic track, pixel-logo bookends.
2. **Spec reveal with long takes:** 27-43 s continuous camera moves around the real robot, typewriter spec labels (category caps + 2 lines), then named customer site.
3. **Deployment montage:** real plant, fleet shots, desaturated grade, cuts every 2 beats at ~100 BPM, typewriter title "F.03 AT BMW".

## House rules
- **Monochrome world:** black robot, grey/white environment, desaturated; colour only from the site (green bins, yellow rails) or one blue accent light.
- **Typewriter text:** every title and label types on letter by letter and deletes letter by letter - the brand's "machine voice". Monospaced grotesk for titles, grotesk for labels; no boxes.
- **Spec label = category + value + meaning:** "BATTERY / 2.25 KWh / +50% Runtime". Placement rotates between corners per shot; colour flips black/white with the background.
- **Pixel logo** built from squares at the end (and on the robot's face display).
- **No VO**; music carries the film.

## How they show a real machine working / keep it credible
- Long continuous takes (42.7 s orbit, 27.2 s walk) in the spec film; named customer location as a label ("BMW Production Line, Plant Spartanburg - SC"); "100% Autonomous" + "Self-correcting" shown on a real correction.
- Deployment montage shows several robots in one frame (scale) with real workers and cars behind.
- Weak spot: fast montages don't show task duration or autonomy labels; the design teaser may be CGI (not stated).

## Recipe (real footage + HTML/GSAP)
1. One long take per idea: rising orbit around the machine (30-45 s), tracking walk on site (20-30 s), a correction close-up (8-10 s).
2. Labels: Inter 600 caps 1.5vh (letter-spacing .12em) + Inter 500 3.2vh x 2 lines; typewriter in at 0.035 s/char, out at 0.025 s/char; 4-6 s hold; corner rotates per shot.
3. Grade everything to near-monochrome (`saturate(.3-.4)`) and keep your one brand colour.
4. Montage cuts on a 2-beat grid (1.2 s at 100 BPM), section changes on bar hits.
5. End on a pixel/grid logo build (CSS grid of squares, random stagger 0.02 s).
