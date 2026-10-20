# Rolex - style

Examples (official @ROLEX uploads):
| Example | Date | Length | Shots | ASL | Median | Sub-style |
|---|---|---|---|---|---|---|
| [oyster-100-years](oyster-100-years/notes.md) | 2026-04 | 3:56 | 301 | 0.78 s | 0.56 s | heritage archive collage + macro + manufacture |
| [new-watches-2026](new-watches-2026/notes.md) | 2026-04 | 1:07 | 38 | 1.77 s | 1.46 s | CGI product reveal, tempo-grid cuts |

## Sub-styles
1. **Heritage collage** - newsreel archive in a rounded film gate, archive voices instead of one narrator, product macro and CGI exploded views, a fast manufacture section, a 0.45 s-per-face testimonial run, off-white serif end card.
2. **Novelty reveal** - all CGI: parts float and assemble on a white sweep, watches on water at the horizon, one huge landscape title, logo on white.

## Rules that repeat
- **One object, centred, clean background.** Even at 0.5 s per shot the picture is calm.
- **Engineering shown, not told:** exploded parts that assemble (both films), a test machine, a real watchmaker. Almost no supers; dials carry the text.
- **Tempo grid where it matters:** 0.60 s per shot (intro), 0.88 s (line-up), 0.45-0.5 s (catalogue, testimonials). Free timing for the long assembly shots (4-7 s).
- **No silence, no drop-outs** - continuous score; emphasis comes from new voices or a soft hit.
- **End card:** white/off-white, tiny serif (3-4.6 % height), crown logo, 2-7.6 s hold.
- Speed is high (median 0.56 s heritage) but every frame is a "catalogue" frame - premium comes from cleanliness, not from slowness.

## Recipe (real footage + HTML/GSAP)
1. Shoot the product (or machine part) macro on a white sweep and on a reflective surface; keep the camera centred and slow.
2. Exploded view: PNG layers of parts, assemble with `power3.out`, 0.25 s stagger, 1-2 % landing bounce.
3. Archive (old project photos/film): rounded gate on black, grayscale, light flicker, 0.2-0.6 s per image.
4. Cut to a tempo: `beat = 60/BPM`; intros and line-ups on 1 or 1.5 beats.
5. End card: off-white radial gradient, serif italic + caps (EB Garamond 3vh / 4.6vh), logo cross-fade.
