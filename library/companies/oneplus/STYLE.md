# OnePlus - video style (2025, OnePlus 15 campaign)

Built from 3 official examples, analysed 20 Oct 2026 (480p, adaptive cut detector, cuts checked by eye, EBU loudness, text measured in % of frame height H). All three are pre-launch pieces of one campaign ("Power On. Limits Off."), so this describes a campaign more than a long-term house style.

| Example | Type | Length | Shots | ASL / median | % < 1 s | % > 3 s | Loudness | Voice |
|---|---|---|---|---|---|---|---|---|
| [oneplus-15-power-reimagined](oneplus-15-power-reimagined/notes.md) | performance manifesto | 60.0 s | 76 | 0.79 / 0.64 s | 74 | 0 | -9.2 LUFS | narrator, subtitled |
| [oneplus-15-design-reimagined](oneplus-15-design-reimagined/notes.md) | design film (split screens) | 52.1 s | 21 | 2.48 / 2.37 s | 14 | 38 | -9.6 LUFS | none |
| [oneplus-15-sand-storm](oneplus-15-sand-storm/notes.md) | colour / material film | 69.8 s | 28 | 2.49 / 2.50 s | 4 | 25 | -18.5 LUFS | narrator, subtitled |

## In one sentence
OnePlus splits one launch into three moods - a loud 0.8 s-per-shot athlete manifesto, a split-screen design film where every panel has a two-word label, and a slow poetic CGI material story - all with small, plain sentence-case type and a black "Coming Soon" end.

## Sub-styles

### 1. Performance manifesto
- Athletes and motion (sprinter in blocks, motocross, skaters, swimmers), 0.12-0.8 s shots, a studio set with a dolly track and plinth as bookends; the phone appears only in the last 3 s.
- VO manifesto subtitled at ≈86 % H (cap ≈2.5 % H); compressed, very loud master (−9.2 LUFS, LRA 2.1 LU).

### 2. Split-screen design film
- Every shot is two panels with one two-word label each (cap ≈3 % H, centred in the panel): opposites as a system ("outside | inside", "dust | deep", "Power On | Limits Off").
- Panels change at different times, so it feels twice as fast as the measured ASL (2.5 s).
- Music + SFX, loud (−9.6 LUFS).

### 3. Colour / material myth
- Desert → electric-arc factory → finished shell, ≈85 % CGI, very even pace (ASL 2.5 s, quarters 1.9-2.5 s).
- Narration subtitled (≈2.6 % H at 93 % H), one claim line on top (≈4.2 % H). Quiet master (−18.5 LUFS).

## Measured ranges
- ASL 0.79-2.49 s; loudness −9.2 to −18.5 LUFS - the widest spread in this set, chosen per mood.
- Two of three masters peak at +0.9 dBTP (clip after encoding).

## Typography
- OnePlus Sans (proprietary). Free stand-in: **Inter** or **Manrope** Regular.
- Always sentence case, small (2.5-4.2 % H), white, centred; no bold headlines, no big numbers.
- End: product name ≈2.5 % H + "Coming Soon" / date ≈1.3-1.8 % H, then the wordmark, on black.

## Colour
- Manifesto: dark high-contrast with red accents. Design: one colour world per finish (sand/champagne, lilac, black + red laser). Material film: beige desert + teal-black/orange embers.

## Recipe
- Decide the mood first (manifesto / design pairs / material myth) and set pace and loudness to match: 0.8 s and −9 LUFS, 2.5 s and −10 LUFS, or 2.5 s and −18 LUFS.
- Split-screen pairs: `grid-template-columns:1fr 1fr`, label per panel `3vh Inter`, offset panel cuts 0.4-1 s.
- Subtitle-style VO lines at the bottom, one per shot.
- Keep true peak ≤ −1 dBTP (the originals clip).
