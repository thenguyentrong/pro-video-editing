# Dusty Robotics FieldPrinter System: How It Works  (Dusty Robotics, 2023-02-14, 1:25, 16:9, YouTube @DustyRobotics)
URL: https://www.youtube.com/watch?v=6vu8yvCUNPE
Purpose: animated explainer / onboarding (workflow from BIM model to printed floor)
One-sentence point: Bring a model, three survey control points and a swept floor; the robot localises with a laser tracker, you pick what to print on a tablet, and you get a report with productivity stats.

## Structure (narrated, 100 % flat 2D/2.5D illustration, no live footage)
- 0.0-3.1 (0-4 %) title: logo + "How It All Works" in a thin-bordered box, diagonal line pattern draws in on white.
- 3.1-15.5 (4-18 %) promise: isometric robot close-up with a dashed print line, zoom-out to a robot and a worker with a tablet; front view of the robot (cartoon "eyes" blink). VO: fastest, most accurate way to bring BIM models to the field; simple to use.
- 15.5-23.8 (18-28 %) requirements as a 3-icon checklist that builds one by one: monitor "CAD", control point "Control", broom "Clean floor".
- 23.8-40.0 (28-47 %) step 1-2: monitor with a plan; robot badge "ROBOT READY DRAWINGS"; CAD and REVIT labels; then robot card with a 3-item checklist card (control points, clean floor).
- 40.0-53.4 (47-63 %) step 3: control point pin drops, worker scans with a laser tracker on a tripod (dashed beam), zoom into a tablet, dark plan pans to a floor plan, a hand taps the tablet UI to choose the area.
- 53.4-62.5 (63-74 %) robot prints; extra: "If you want to print in DIFFERENT COLORS" banner, ink cartridge swap card "REPLACE INK CARTRIDGE".
- 62.5-75.1 (74-88 %) result: "QA REPORT" sheet of the printed plan, then a stats sheet (zone name, linear feet, points, text count, per-hour rates, bar chart "Total Linear Feet per Hour").
- 75.1-84.5 (88-100 %) tagline over isometric robot, end card: logo + one line CTA + orange URL button, held ≈8 s.

## Cut rhythm
- 17 scenes in 84.5 s (2 hard cuts detected; 14 scene changes added by eye - they are animated pushes/wipes, so the scene detector misses them). ASL 4.97 s, median 4.38 s, 0 % under 1 s.
- ASL per quarter 5.28 / 4.22 / 2.64 / 7.04 s: busiest in the workflow middle (tracker -> tablet -> plan, 1.9 s scenes), long holds on the report and end card. Longest 9.39 s (end card), 9.10 s (report), 8.30 s (checklist).
- Inside scenes, elements keep moving every 1-2 s (pop-in icons, label boxes), so the felt pace is faster than the scene ASL.

## Typography
- Geometric/neo-grotesk sans (free: Inter or Manrope). Title "How It All Works" 600 sentence case ≈5.5 % H in a white box with 1 px grey border. Section banner: kicker in white on an orange box (≈4.5 % H, 300-400) + headline 800 caps ≈7 % H navy, on a pale-aqua band, left-aligned, slides in from the left. Small labels ("CLEAN FLOOR", "CONTROL POINTS") 500 caps ≈3 % H on white cards with soft shadow. UI and report text tiny (≈2 %), not meant to be read, only to show "real data".
- Colour palette: pale aqua background #C6E4E6, brand orange #E8792B, navy #0E3A55, white, light grey lines.

## Colour/grade
- Flat vector, no gradients except soft drop shadows; isometric 30 deg robot with flat shading; consistent palette across all scenes.

## Camera/shots
- Virtual camera: slow zoom-outs and pans across a 2.5D isometric world; push into the tablet screen; a cartoon hand taps the UI.
- No live footage, no drone, no timelapse. Data card = the productivity report (linear feet, points, text, per-hour).

## Transitions
- Animated: pushes, zoom-throughs into a screen, wipes with orange shape, elements building on (scale-in with overshoot, 0.3-0.5 s). Line pattern draw-on for title and end.

## Sound
- Calm female VO (US), corporate light-electronic bed, soft UI blips on pop-ins. Integrated -20.1 LUFS, LRA 2.9 LU (flat), true peak -4.0 dBTP. No drop-outs; silence only in the last 0.9 s. VO pace ≈2.6 words/s.

## What makes it work
- It answers the buyer's practical question ("what do I need on site?") as a checklist before any feature.
- The full workflow in 5 steps with the real tool names (AutoCAD, Revit, laser tracker, tablet, report).
- One palette and one isometric robot drawing make it look like the product, not like stock icons.
- Ends with the output a manager cares about: a report with numbers.

## Recipe (HTML/GSAP, no footage needed)
- Background `#C6E4E6`; cards white `border-radius:2px; box-shadow:0 6px 20px rgba(14,58,85,.12)`; accent `#E8792B`; text `#0E3A55`.
- Banner: kicker `font:400 4.5vh Inter; background:#E8792B; color:#fff; padding:.4vh 1vw` + headline `font:800 7vh Inter; text-transform:uppercase`; `gsap.from(band,{xPercent:-100,duration:.5,ease:'power3.out'})`.
- Checklist: 3 icon cards, `gsap.from(card,{scale:.6,opacity:0,duration:.35,ease:'back.out(1.6)',stagger:.9})` on each VO noun.
- Scenes 2-8 s, one VO sentence each (≈2.6 words/s); push transitions `x:-100vw` 0.6 s `power2.inOut`.
- End on the report card with 2-4 real numbers, then logo + CTA button held 8 s.
