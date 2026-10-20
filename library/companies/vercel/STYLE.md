# Vercel — launch film style

Three official Vercel films measured at 480p/360p (adaptive and scene cut detection + eye check on before/after pairs, EBU loudness, 50 ms RMS, speech detection for voice timing; text in % of frame height H). Analysed Oct 2026.

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice | Aspect |
|---|---|---|---|---|---|---|---|---|
| [Introducing v0: Generative UI (2023)](introducing-v0/notes.md) | 47.5 s | 1 (≈12 beats by eye, ≈3.8 s) | — | — | — | −16.6 | none | 16:9 |
| [Develop. Preview. Ship. (2021)](develop-preview-ship/notes.md) | 41.8 s | 1 (≈10 beats by eye, ≈4.2 s) | — | — | — | −27.8 | narrator, ≈2.9 w/s | 16:9 |
| [Ship Week 2026 London (2026)](ship-week-2026-london/notes.md) | 61.1 s | 53 | 1.15 / 0.92 | 1.27 · 0.90 · 1.17 · 1.09 | 59 % / 2 % | −13.5 | sound bites, ≈2.5 w/s | 16:9 |

Method note: the two product films are single continuous motion-graphics takes (no hard cuts by either detector). Their "beats" are counted by eye from the contact sheet and are approximate.

## The core idea
Vercel speaks in two registers. **Product films** are pure interface graphics with zero cuts: one virtual camera glides, zooms and scales between prompt, result and code on a flat white or pure black field, with the product's own UI as the only picture and a bold question or the product's verbs as the only headline. **Event films** are the opposite: a fast, dark, real-people sizzle (≈1 s cutting) held together by a voice spine of keynote sound bites and one graphic language of typed mono words with a block cursor. The brand stays monochrome (black, white, the triangle); colour comes only from the UI or from one gradient per chapter.

## Rules with numbers
1. **Monochrome field.** White (#fff, mean luma 0.95) or black (#000, mean luma 0.01-0.14). Ink is the opposite colour; no textures.
2. **No cuts in product films.** Move a virtual camera instead: zoom 1.5-3× into a detail, hold 3-5 s, zoom out; 10-12 beats in 42-48 s (≈4 s each).
3. **The headline is the UI.** A bold question inside a huge prompt pill (pill ≈75 % W × 13 % H, cap ≈7 % H) that shrinks into the real input; or the product's verbs as numbered chapters (cap ≈6-7 % H, one gradient per chapter).
4. **Small, exact type elsewhere.** Social proof in tiny tracked caps (≈1 % H); URL ≈3.5-4 % H; end lockup ≈7 % H; corner bug ≈3.5 % H.
5. **End in three steps.** URL (≈1-2.5 s) → product logo (≈1 s) → company mark + wordmark (≈2-4 s) → 0.85-1.35 s silence.
6. **Event sizzle numbers.** ASL ≈1.15 s, median ≈0.9 s, 52 shots/min, flat across quarters (0.9-1.3 s); one longer keynote shot (≈5 s) at 5-12 %; densest 10 s window (13 cuts) at ≈35-50 %; big hall wide at ≈90 %.
7. **Typed mono words** over picture in event films: lowercase, line box ≈17 % H, block cursor, 1-3 words, 0.6-1.5 s, pixel-noise exit.
8. **Sound.** Product demo: music only, steady growth (≈+11 dB from start to the 60 % peak), −16.6 LUFS. Explainer: narrator ≈2.9 words/s, pops on element entrances. Event: sound-bite VO ≈2.5 words/s over a pulsing bed, −13.5 LUFS; cuts not beat-locked (54 % vs 53 % chance).

## Recipe (Hyperframes, 1920×1080)
**Product demo (≈45 s, no cuts)**
1. `background:#fff`; logo build 2-3 s.
2. Hero prompt pill (`#111`, radius = half height, `700 76px Geist` white) with the hook question, 1.5 s; tween into the real input size (0.8 s `power3.inOut`); cycle 3-5 example prompts (1.2 s each).
3. Fade up the generated UI; camera wrapper zooms into one element (1.2 s `power3.inOut`), cursor click, typed edit, the element updates; zoom out.
4. Code panel swing (`rotateY -25° → 0`, 0.8 s); one more zoom detail; a grid of many outputs panning (2.5 s).
5. URL → product logo → company lockup; music bed growing to the 60 % peak, 1.3 s silence at the end; master −16 LUFS.

**Chapter explainer (≈40 s)**: black field, 4 numbered chapters (5-8 s), a 1 px line drawing down between chapters, one gradient per chapter, narrator ≈2.9 words/s.

**Event sizzle (≈60 s)**: 50-60 real clips of 0.5-2 s, sound-bite VO spine, typed mono words, corner bug top-left, name supers bottom-left in caps, lockup on black at the end, master −14 LUFS.
