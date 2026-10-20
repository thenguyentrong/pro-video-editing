# Electromechanical Actuators - powerful, flexible, efficient  (Bosch Rexroth, 2026-10-15, 2:21, 16:9, YouTube @BoschRexroth, [EN] version)
URL: https://www.youtube.com/watch?v=cjPNGx2JBM4
Purpose: product / application-catalogue film, 100 % CGI, silent (made for trade-fair screens and muted autoplay)
One-sentence point: Rexroth electromechanical cylinders replace hydraulics and pneumatics in pressing, forming, transport, mobile, packaging, pumping, woodworking and simulators.

## Structure
- 0-10 intro: white stylised worker holding a cylinder on a cyan panel (right half); left half dark teal with "ELECTROMECHANICAL CYLINDERS" + "POWERFUL / FLEXIBLE / EFFICIENT" stepping in.
- 10-96 eight application blocks of ≈10-12 s each, same layout: a short macro/fly-in on the render (2-3 s), then the split screen - left dark teal panel with the category title in a navy bar ("PRESSING", "FORMING", "TRANSPORT", "MOBILE", "PACKAGING", "VOLUMETRIC PUMPING", "WOODWORKING", "SIMULATORS") and three sub-uses as staggered navy tags (e.g. press fitting / punching / clinching); right panel a white-grey render of the machine with the actuators glowing cyan.
- 96-120 "ELECTROMECHANICAL CYLINDERS ADVANTAGES": blurred render background, a grid of six cards builds pair by pair (Dynamic, Economic, Precise, Flexible, Robust, Compact), each with a one-line benefit.
- 120-137 "KEY TECHNICAL DATA": two tilted teal cards side by side with 4 bullet specs each (sizes, axial force up to 250 kN / 72 kN, travel speed up to 2.5 m/s / 0.55 m/s, max. stroke up to 1,500 mm / 400 mm) and a product render.
- 137-141 Rexroth logo build from coloured stripes on white.

## Cut rhythm
- The default detector finds 1 cut; the adaptive detector 6 (7 shots, ASL 20.1 s, median 12.0 s, longest 60.5 s from 76 s). Most changes are camera moves and panel wipes inside continuous renders, so the "cuts" do not describe the rhythm.
- By eye (≈): 8 application blocks at 10-12 s each, inside each ≈2-3 s fly-in + ≈8 s held layout; label tags step in every ≈0.5 s.

## Typography
- Bosch Sans-like grotesk (closest free: Inter Bold / Arial-like neutral sans), caps, white on navy (#0f3a52-ish) bars.
- Category bar: ≈7 % H tall, text ≈3.5 % H bold caps, x ≈6-39 %, y ≈11-19 %.
- Sub-use tags: navy boxes ≈6 % H with ≈3 % H caps text, stepped diagonally (each one ≈10 % W further right and ≈9 % H lower).
- Advantage cards: navy/cyan boxes with title ≈2.5 % + one line ≈1.8 %.
- Data cards: header bar caps ≈5 % H; card title bold caps ≈3.5 %; bullets with bold label + regular value ≈3 % H, metric units with "up to".

## Colour/grade
- Dark teal-to-navy gradient panel + white/light-grey clay renders; actuators in glowing cyan as the only colour; Rexroth red only in the logo stripes.

## Camera/shots
- 100 % CGI: macros on rods and bearings, fly-ins, slow rotations of each machine; a stylised clay worker for scale.

## Transitions
- Panel wipes (the teal half slides in), camera moves out of macros, blur-backgrounds for card sections; stripe animation into the logo.

## Sound
- None. The audio track is digital silence (-91 dB mean) for the whole film. Built to work without sound: every message is text.

## What makes it useful
- One fixed layout for 8 applications: the viewer learns where to look once.
- Product highlighted by colour (cyan) inside a neutral machine.
- Real numbers with units on a dedicated data card.
- Weak: no real footage at all; very small text in the advantage grid; no sound for web viewers.

## Recipe (HTML/GSAP)
- Split layout: `.panel{position:absolute;left:0;width:45vw;height:100vh;background:linear-gradient(180deg,#4f7d8f,#0b3550)}`, render video in the right 55 %.
- Category: `.cat{background:#123f57;color:#fff;font:700 3.5vh Inter;text-transform:uppercase;padding:1.8vh 2vw;left:6vw;top:11vh}`.
- Tags: three `.tag` (`font:700 3vh Inter`, navy box), positions stepping `left:6vw/16vw/26vw; top:42vh/51vh/60vh`; `gsap.from(tags,{x:-30,autoAlpha:0,stagger:.5,duration:.3})`.
- Data card: `transform:perspective(1200px) rotateY(8deg)`, bullets `<b>Axial force:</b> up to 250 kN`.
- Add music and a VO track for web use; keep the silent master for trade-fair screens.
