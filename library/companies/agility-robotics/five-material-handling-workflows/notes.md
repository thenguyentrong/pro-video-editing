# Precision in Motion: Five Humanoid Material Handling Workflows  (Agility Robotics, 2024-12-17, 1:28, 16:9, YouTube @AgilityRobotics)
URL: https://www.youtube.com/watch?v=3xQVCQ7_zZk
Purpose: capability demo (skills catalogue)
One-sentence point: one Digit fleet does five different tote workflows in one test cell.

## Structure
- 0-2.4 hook: high angle of the test cell, several Digits working at once.
- 2.4-24.6 quick tour (11 shots, 1.5-3.7 s): totes on a curved conveyor, gripper close-up, overheads, Digits walking with totes; title "AMR UNLOAD" over a Digit at an AMR (≈15.5-18 s).
- 24.6-35.3 "TOTE STACKING & DESTACKING" over one 10.8 s medium take.
- 35.3-54.3 two long takes (7.5 s, 11.4 s) of Digit walking totes between conveyors; "TOTE NESTING" title (≈44-47 s).
- 54.3-73.0 overhead, two-robot close, "DEPALLETIZATION" over a high-angle take (≈60-64 s), a front medium, a 1.0 s music drop-out at 67.8 s, then two wides.
- 73.0-83.6 summary: one 10.6 s overhead of the whole cell with all five workflow tags pinned to their stations.
- 83.6-87.6 end card on black "AGILITY ROBOTICS / MADE FOR WORK" (after a short dip to black).

## Cut rhythm
- 22 shots, ASL 3.98 s, median 3.07 s, 4.5 % < 1 s, 55 % > 3 s, 15.1 shots/min. ASL per quarter 2.2 / 5.5 / 4.4 / 3.7 s.
- Fast tour (4 cuts per 10 s) then 1-3 cuts per 10 s; longest takes 11.4, 10.8, 10.6 s.
- 67 % of cuts on audio onsets vs 63 % chance (dense beat, so no clear sync).

## Typography
- Workflow title: geometric sans extra-bold caps (closest free: Poppins 800), ≈9 % H, mint-to-white vertical gradient (#9FF0D5 → #FFFFFF), centred low in frame (y ≈70-78 %); subline "& DESTACKING" ≈5 % H right-aligned under it. Hold 3-10 s, fade in/out.
- Tracked station tags in the summary overhead: white caps ≈3 % H with a thin dashed underline that runs to a dot on the station (callout pinned to the real place).
- End card: "AGILITY ROBOTICS" ≈3 % + "MADE FOR WORK" ≈1.8 %, centred, white on black.
- No speed or autonomy label.

## Colour/grade
- Bright, punchy commercial grade: teal robots, saturated red and yellow totes, black floor mats with AprilTag-style markers, white walls. Real test lab.

## Camera/shots
- Overheads, high angles, locked mediums, a few low angles; one close-up at the gripper. Several robots in frame (fleet).

## Transitions
- Hard cuts; dip to black before the end card.

## Sound
- Music only (no speech detected): upbeat electronic, loud. Integrated -11.6 LUFS, true peak +3.1 dBTP (clipping risk in the upload). One 1.0 s drop-out at 67.75-68.75 s (floor -57 dB), then the biggest rise of the film (+45.7 dB at 68.9 s) on the cut to the next workflow.

## What makes it credible
- Real lab with fiducial markers, cables and many robots at once; workflows shown in 7-11 s takes.
- The final overhead maps every skill to its station in one real frame.
- Weak: no speed label, no autonomy statement, lab not customer site.

## Recipe
- One title per skill: `font:800 9vh Poppins;text-transform:uppercase;background:linear-gradient(#9FF0D5,#fff);-webkit-background-clip:text;color:transparent`, `autoAlpha 0→1, y 20→0, .4 s power3.out`, hold over one 7-11 s take.
- Summary shot: overhead of the whole cell, pinned callouts (`<line stroke-dasharray="3 3">` + 3vh caps) drawn with `stroke-dashoffset` 0.4 s, stagger 0.15 s.
- Music-only, master to -14 LUFS / -1 dBTP (not hotter); a 1 s drop-out before the last workflow.
