# Patek Philippe - style

Examples (official @PatekPhilippeGeneva uploads):
| Example | Date | Length | Shots | ASL | Median | < 1 s | LUFS | Sub-style |
|---|---|---|---|---|---|---|---|---|
| [generations-legacy](generations-legacy/notes.md) | 2015-02 | 1:56 | 45 | 2.57 s (film part ≈2.19 s) | 2.0 s | 7 % | -12.6 | long B&W film, five cities, 19-s end card |
| [generations-ad](generations-ad/notes.md) | 2016-10 | 1:00 | 37 | 1.62 s | 1.16 s | 19 % | -13.8 | 60-s ad, city captions, colour product end |
| [next-chapter](next-chapter/notes.md) | 2019-11 | 0:37 | 20 | 1.85 s | 1.46 s | 30 % | -16.9 | short chapter, one family, logo first |

## Core idea
The **Generations** campaign has run for decades on one line about looking after a watch for the next generation. The films are photo-book B&W moments between parent and child; the watch is a detail on a wrist, never presented in the film. The line on the end card does the selling.

## Rules that repeat
- **B&W people, colour product** (the product is the only colour shot, if shown at all).
- **Slowest pace in the luxury set:** median 1.16-2.0 s, only 7-30 % of shots under 1 s, 23-37 shots per minute, even pace with no acceleration.
- **No voice, continuous piano/strings,** no drop-outs, -12.6 to -16.9 LUFS.
- **Vignettes:** 8-20 s per family or city, 5-9 shots each, one wrist close-up per vignette.
- **Text:** italic serif city names lower right (≈4.6 % H) in the ad; the campaign line as two serif lines (≈3-3.3 % H) on a silver gradient, or as tracked sans caps (≈2.5 % H) at the left of a product shot (2019 refresh).
- **Long end:** text card 5 s + product 5 s + logo 3 s (60-s ad); 19 s line + logo (long film); 9.8 s product card (37-s spot).
- **Fades only on cards**, hard cuts inside the story.

## Recipe
1. 3-5 vignettes of real-feeling family moments, B&W soft (`grayscale(1) brightness(1.08) contrast(.9)`), shots 1.2-4 s.
2. One wrist close-up per vignette, never a product insert.
3. End: silver gradient card with two serif lines (EB Garamond 3.3vh), line 2 fades in 2-4 s after line 1; then logo; optional colour product turntable 5 s.
