# Sonos Amp Multi | World-class audio, amplified  (Sonos, 2026-01-27, 2:10, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=JaFa0xiEOvQ
Purpose: launch film for a pro / installer product (spec film)
One-sentence point: A rack amplifier for installers, shown feature by feature in a dark studio with one calm label per feature.

Structure:
- 0.0-6 darkness; a light slowly finds the perforated top of the product (two shots, 3 s each).
- 6-11.5 title "Sonos Amp Multi" above the product, centred (frames/t008.0s.jpg).
- 12-21.5 rear panel macros with labels at the bottom: zones/outputs, efficiency, amplifier class (t013.0s).
- 22-35 software: a phone with the setup app over the product, then a floor-plan line drawing that lights up zone by zone (t024.0s).
- 36-43.5 laptop with a tuning EQ curve that moves (t040.0s).
- 44-58 rack mount and installation shots in near-black.
- 59-77 design: "Innovative design", then dimension call-outs "2U" and "0.5U" drawn as a bracket line next to stacked units (t064.0s), "Takes up less space".
- 78-107 setup on the phone; indicator lights; connector labels change one by one on a locked shot of the rear panel (t097.0s, 95-106 s).
- 107-118 partner logos card, then "Engineered responsibly" over a perforated macro.
- 118-123 end line "World-class audio, / amplified" (second line grey) above the product (t120.5s).
- 123-130 SONOS + sonos.com on black, 5.9 s of silence (t126.0s).

Cut rhythm: 26 shots (adaptive detector + 2 dissolves added; ffmpeg scene found 0 because the film is near-black), ASL 5.0 s, median 4.5 s, 0 % under 1 s, 81 % over 3 s, 12 shots/min. Quarters 4.06 / 3.25 / 4.64 / 8.12 s. Longest 12 s (end line + logo, and the locked rear panel with changing labels). By eye there are ≈ 28 set-ups ≈ 4.6 s each. Many changes are fades through black.

Typography: neo-grotesk sans (closest free: Inter), sentence case, white, no box. Feature labels: cap ≈ 4.6 % H main line + ≈ 3.5 % sub-line (spec number), centred at y ≈ 85 % (bottom), 1 label per shot, held for the whole shot (3-6 s). Title and end line: cap ≈ 5.8 % H, centred in the upper third (y ≈ 27-37 %), product below. Grey second line (≈ #9a9a9a) for the payoff word. Dimension call-outs: big numerals "2U" ≈ 9 % H with a thin vertical bracket line.

Colour/grade: almost black (median luma 16, 100 % of frames dark), zero saturation except tiny red/white LEDs and the phone UI; contrast is low (p95-p5 33) because most of the frame is black. Soft top light that rakes across the perforation.

Camera/shots: photoreal CG, slow dollies and slides along the panel, top-down floor-plan graphic, UI on phone and laptop composited into the dark set. No people.

Transitions: fades through black between sections, cross-dissolves inside sections; labels change on a locked shot instead of cutting.

Sound: music only (no VO), steady electronic pulse; −15.1 LUFS, LRA 2.9 LU, true peak +0.1 dBTP. The music stops for 0.3-0.45 s six times (1.7, 30.1, 35.2, 38.3, 45.6, 66.3, 78.6, 83.8 s): each stop marks a new section. Logo in 5.9 s of silence.

What makes it premium:
- Restraint for a technical product: one label per shot, low on the frame, never more than two lines.
- Light reveals the product slowly; darkness hides everything that is not the point.
- Section stops in the music (0.3-0.45 s) give a "chapter" rhythm without titles.
- Grey second line on the payoff = soft emphasis without bold or colour.

Recipe (HTML/GSAP):
1. Background `#050505`; product renders or photos lit from the top; a moving light via a radial-gradient mask (`mask-image: radial-gradient(40% 60% at var(--x) 30%, #000 0%, transparent 70%)`, animate `--x` 20 % → 80 % over 4 s).
2. Label component: `bottom:12%; text-align:center; font: 500 6.3vh 'Inter'` + sub-line `font-size:4.8vh; opacity:.85`; `opacity 0→1` 0.5 s; hold for the whole shot.
3. Section rhythm: shots 4-6 s, fade through black 0.4 s between sections; cut the music for 0.35 s at each section start.
4. Dimension call-out: SVG line `strokeDashoffset` 0.6 s, then the numeral fades in at `font-size:12vh`.
5. End line two lines, second line `color:#9a9a9a`; logo on black 4-6 s in silence. Master −15 LUFS.
