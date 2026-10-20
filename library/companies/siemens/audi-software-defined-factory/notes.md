# Siemens and Audi: Redefining Manufacturing with a Software-Defined Factory  (Siemens, 2026-05-20, 2:55, 16:9, YouTube @Siemens)
URL: https://www.youtube.com/watch?v=tWHNBqH-Vh8
Purpose: customer testimonial / trade-show interview (Hannover Messe 2026)
One-sentence point: Audi's VP explains how the platform built with Siemens moves Audi's plants from hardware-heavy to software-defined - "a game changer in flexibility".

## Structure (cut list + English captions)
- 0.0-12.5 host intro: handheld two-shot on the busy Siemens booth (host in a blue polo with a handheld mic, Audi VP next to him): "We are back at Hannover Messe... our collaboration with Audi... from hardware-heavy to software-defined."
- 12.5-14.2 name card: hard cut to the guest cut out (rotoscoped) on Siemens navy, then he turns black-and-white and his name types in big mint caps: "PETER STECHEL / Vice President, Data- and Technology Driven Production and Supply Chain, Audi AG" (white, bold) - 1.7 s.
- 14.2-19: back to the two-shot; the guest's single with a lower third (navy box, white text, 16-19 s).
- 19-171: testimonial single (handheld, the trade-show crowd moving behind him) intercut every 5-15 s with Audi plant b-roll: body-shop robots (orange KUKA), engineers at a laptop, the software UI on a screen (24-25 s, node graph), workers at the line, Siemens drives/controllers macro (72-74 s), door assemblies, HMI touch panels, an Audi A6 body on a hanger, a CGI wireframe of a car body (132 s, blue x-ray look), clean-room installation. 0.15-0.9 s audio gaps around many b-roll entries (music edits).
- 167-171: wide two-shot again, handshake ("We'll keep you posted on the next steps").
- 171.8-175: SIEMENS wordmark on navy with a sting (loudest, +36.8 dB at 172.1 s).

## Cut rhythm
- 82 shots in 175 s. ASL 2.13 s, median 1.48 s. ASL per quarter 2.19 / 1.99 / 1.68 / 2.57 s.
- Longest 12.48 s (opening two-shot), 8.64 s, 7.6 s, 7.24 s (testimonial singles). Shortest 0.36-0.52 s (b-roll).
- 15 % under 1 s, 13 % over 3 s. Talk shots 4-12 s; b-roll bursts of 3-6 shots at 0.5-2 s.

## Typography
- Name card: guest cut-out (B&W) left, name in Siemens Sans Black caps, mint-to-cyan gradient (~9 % frame height per line, 2 lines), role in white bold sentence case (~3 %, 3 lines), on navy #000028 - a "trading card" moment.
- Lower third: navy box with white name (bold) + role (regular), ~2.2 % height, left-centre over the speaker's chest.
- End: white SIEMENS wordmark on navy.
- No spec/number overlays; the software is shown as real screen footage.

## Colour/grade
- Trade show: bright, busy, mixed light, Siemens navy/teal booth graphics. Plant b-roll: clean white/grey Audi factory, orange robots, cool screens. Lightly graded, contrasty, sharp.

## Camera/shots
- Handheld gimbal at the booth (with real crowd and noise), testimonial framed medium-close with lots of booth behind.
- B-roll is real Audi plant footage (shot separately, likely Audi/Siemens archive): robots welding, workers at HMIs, macro of Siemens hardware, screen UI; one CGI wireframe.

## Transitions
- Hard cuts only. Music edits (short gaps) mark b-roll entries.

## Sound
- Interview audio (lav + handheld mic) with booth ambience; corporate electronic music bed with frequent micro-cuts (36 gaps of 0.15-0.9 s). Integrated -13.8 LUFS.

## What makes it credible
- The customer (not Siemens) says the claim, with full name, title and company on screen.
- Real plant footage of the customer's production and of Siemens hardware in it.
- Live event setting (crowd behind) - it was really said there.
- Weak spot: no numbers ("game changer" stays vague); the b-roll is generic factory footage.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Format: host + customer at your stand or on the customer's site; 2-3 min; b-roll every 10-20 s of talk (3-6 shots, 0.5-2 s each).
- Trading-card name intro: cut-out PNG/WebM of the guest (`remove-background`), `filter: grayscale(1)`, on `#000028`; name `font: 900 9vh Inter; background: linear-gradient(90deg,#00ffb9,#00e6dc); -webkit-background-clip:text; color:transparent; text-transform: uppercase; line-height:.95`; role `font: 700 3vh Inter; color:#fff`. Timeline: `tl.from(cutout,{x:-40,autoAlpha:0,duration:.3}).to(cutout,{filter:'grayscale(1)',duration:.2}).from(nameChars,{autoAlpha:0,duration:.001,stagger:.03})`, hold 1.7 s, hard cut back.
- Lower third: navy box, 2.2vh white text, left-centre, 3-4 s.
- For a construction robot: interview the site manager/customer on site; b-roll of your machine on that same site; one real screen recording of your software.
