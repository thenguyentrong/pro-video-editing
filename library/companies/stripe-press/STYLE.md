# Stripe Press – founder / tech-history documentaries (2021–2022)

Examples: `we-are-as-gods` (documentary trailer, 141.2 s), `street-network` (short documentary, first 300 s of 21:29 measured), `big-score` (60 s book micro-doc). All on the Stripe YouTube channel, 16:9. Analysed Oct 2026. Stripe's product launch films are in `companies/stripe` (a different style).

## The style in one line
A company's publishing imprint tells other people's stories about technology and progress: archive and observational footage, a small publisher mark, editorial typography (serif cards, mono credits), and patience.

## Measured overview
| film | length | shots | ASL | median | <1 s | >3 s | LUFS | look |
|---|---|---|---|---|---|---|---|---|
| We Are As Gods | 141.2 s | 71 | 1.99 s | 1.58 s | 30 % | 15.5 % | -21.4 | archive collage on aged paper |
| The Street Network (0–300 s) | 300 s | 77 | 3.90 s | 2.59 s | 17 % | 42 % | -22.2 | observational doc, ribbon tags, serif cards |
| The Big Score | 60.3 s | 10 | 6.03 s | 5.23 s | 10 % | — | -17.6 | remote interview + inserts, flat brand colour |

## Core idea
The company never sells. Its name appears once, small ("A Stripe Press short film", a monogram on paper or orange). The film is about a person or a community that shows the values the company wants to be linked with (building, tools, curiosity). Credibility comes from archive, real places and real voices.

## Rules (with numbers)
1. **Quiet start.** 1.75–4 s of silence (-50 dBFS) with the publisher mark or a "presents" line; the first voice comes after.
2. **Mark small and once.** Monogram ≈6 % H or a mono caps line ≈1.6 % H; repeated only at the end.
3. **Title late.** Street Network titles at 43 s, We Are As Gods at 132 s (end), both over a symbolic image (antenna, the subject from behind).
4. **Editorial type.** Book serif for context and definitions (≈3.2 % H, 2–3 lines, 8 s on black); condensed caps for place/name tags (4.5–5.5 % H) on coloured ribbons; small serif title with an underline (≈2.5 % H).
5. **Archive is treated as objects.** Photos with rounded borders and shadows on paper, a magnifier moving across catalogue pages, a webcam feed revealed on a monitor in a room.
6. **Let people pause.** Interviews 8–18 s with real pauses (0.3–1 s drop-outs left in); 21 s explainer holds.
7. **Loudness** -17.6 to -22.2 LUFS: quieter than ads; music peaks only under context cards.

## Recipe (real footage + HTML/GSAP, 1920x1080)
- Trailer version (≈140 s): paper ground `#efe3cc` + vignette; 70 shots, ASL ≈2 s, 13 cuts per 10 s in the last fifth; title on paper 8 s at the end.
- Short doc version: ASL 3.5–4 s (first quarter 10+ s), first interview 15–18 s, title at ≈40 s, two serif cards on black (8 s each), explainer graphic ≈20 s.
- Promo version (60 s): 5–6 shots of 5–14 s, one remote interview, two inserts, a flat brand-colour packshot card.
- CSS: `.credit{font:400 1.6vh "IBM Plex Mono";letter-spacing:.1em}` `.card{font:400 3.2vh "Source Serif 4";line-height:1.35}` `.tag{font:600 4.5vh Oswald;text-transform:uppercase}` ribbons `skewX(-25deg)`.
