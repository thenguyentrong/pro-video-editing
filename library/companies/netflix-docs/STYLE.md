# Netflix – documentary trailers (2023–2026)

Examples: `our-planet-ii-trailer` (nature series, 83.5 s), `drive-to-survive-s8-trailer` (sports series, 113.8 s), `rafa-trailer` (athlete series, 147.3 s). All official uploads on the Netflix YouTube channel, 16:9, YouTube end screens excluded from all numbers. Analysed Oct 2026. The scripted Netflix trailers are in `companies/netflix`.

## The style in one line
Real footage cut like a drama trailer: a quiet intimate or natural open, a fast flash-burst of highlights, a confession or hero shot, two short cards, one final image held long, then the show's own title and Netflix's light-bar date card.

## Measured overview
| film | length | shots | ASL | median | <1 s | per quarter | LUFS | cards |
|---|---|---|---|---|---|---|---|---|
| Our Planet II | 83.5 s | 46 | 1.82 s (footage 1.47) | 1.15 s | 6.5 % | 1.90 / 1.39 / 1.16 / 4.17 | -14.4 | 2 on footage |
| Drive to Survive S8 | 113.8 s | 102 | 1.12 s | 1.00 s | 46 % | 1.05 / 1.05 / 1.19 / 1.05 | -15.1 | none (title only) |
| Rafa | 147.3 s | 103 | 1.43 s | 1.13 s | 42 % | 1.15 / 1.84 / 1.05 / 1.94 | -14.7 | 2 on black |

Cut-on-onset: 24 % (chance 11 %) nature, 36 % (31 %) sports, 31 % (29 %) athlete: only the nature trailer is cut strictly on the beat; the people trailers cut on speech.

## Core idea
Netflix sells a documentary like a series: characters, conflict, a climax. The footage is real (archive, observational, interviews), but the editing grammar is the trailer grammar from `movie-trailer.md`, softened by intimacy: home video, low-key confessions, silences.

## Rules (with numbers)
1. **Open small.** Home video (Rafa, 8 s), a club-lit garage (DTS, 8 s) or calm ocean fins (Our Planet, 2.4 s shots). No title, no music hit.
2. **Bug system.** First ≈5 s: series name top-left with a thin red rule (cap ≈1.8 % H) + N monogram top-right; afterwards the grey "NETFLIX" wordmark top-right (≈3 % H) on all footage, hidden on cards.
3. **One flash burst.** 7–10 shots of 4–5 frames (0.16–0.25 s): trophies and camera flashes (Rafa 23–27 s), rookies with slates (DTS 17 s). Nature trailers skip this and never go under 0.8 s.
4. **Confession or hero hold.** One 7 s low-key interview close-up with a ≈1 s drop to -50 dB before the key line (Rafa), or one 2.8 s macro (DTS sunglasses reflection).
5. **Cards are few and quiet.** 2 cards per trailer, 2–4 words, wide-tracked thin caps: on footage (Our Planet, Montserrat 300-like, 6 % H, 1–1.3 s) or on black with a small line over a big spaced word (Rafa, classical caps 1.5 % + 4 % H, 2 s). DTS uses none.
6. **Act breaks** = 0.3–0.5 s dips to black or a mid-trailer N sting (Rafa 43 s).
7. **Final image before the title** is held: overhead of the athlete on clay 6 s (Rafa), a predator chase into a 3D ring wipe (Our Planet), a man alone in a dark studio (DTS).
8. **Title in the show's world, date in Netflix's world.** Show logo (thin spaced caps / geometric caps / 3D letters) 2–10 s, then "ONLY ON NETFLIX" (≈3 % H) over a bold date (≈7 % H) on vertical light bars 2–3 s, then the N sting 2–3 s.
9. **Subtitles are design** in non-English docs: white sans ≈3.5 % H, bottom centre, every story line.
10. **Loudness** -14.4 to -15.1 LUFS; drop-outs only before key lines and the date card (0.75–0.95 s to -50…-54 dB).

## Recipe (real footage + HTML/GSAP, 1920x1080)
- Runtime 85–150 s. ASL 1.1–1.5 s (people) or 1.5–1.9 s (nature, cut every 2 beats). Last quarter slower (1.9–4.2 s) because of the final image and title.
- Order: intimate open 8 s → world 10–15 s → flash burst 3–4 s → confession 7 s → story → card → glory → card → climax → final image 6 s → title 2–10 s → date 2–3 s → logo 3 s.
- Bug: `.bug{font:600 1.8vh Inter;text-transform:uppercase;border-left:3px solid #e50914;padding-left:.8vh}` first 5 s; wordmark `opacity:.7`.
- Cards: `font:300 6vh Montserrat;letter-spacing:.15em` on footage, or `400 1.5vh/4vh Cinzel; letter-spacing:.5em/.8em` on black.
- Date card: light caps `300 3vh` over bold `700 7vh`, on vertical gradient bars (`linear-gradient(90deg,#0000,#7a00ff,#e50914,#0000)` repeated, blurred 2 px).
