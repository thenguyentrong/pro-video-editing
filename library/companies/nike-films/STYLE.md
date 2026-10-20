# Nike long-form films - style

Examples (all official uploads):
| Example | Date | Length | Shots | ASL | Median | Sub-style |
|---|---|---|---|---|---|---|
| [so-win](so-win/notes.md) | 2025-02 | 1:00 | 58 | 1.03 s | 0.88 s | mono anthem, VO call-and-response |
| [greatness-nadal](greatness-nadal/notes.md) | 2024-11 | 1:00 | 50 | 1.20 s | 0.94 s | mono tribute, textures + litany |
| [rip-the-script](rip-the-script/notes.md) | 2026-06 | 6:00 | 286 | 1.26 s | 0.96 s | celebrity comedy short, format parody |

## Two sub-styles
1. **Anthem (60 s, mono).** One voice says one rhetorical device, repeated and accelerated. Everything is black and white, the archive too. Still portraits on black vs. real game action. Tiny or huge type only at the end. ASL ~1.0-1.2 s, median ~0.9 s, 54-62 % of shots under 1 s.
2. **Comedy epic (6 min).** A story with real stars, where the edit switches formats (polished ad / handheld BTS / CCTV / TV / flashback / music video). Same fast median (~1 s) but with long comedy holds (17 s).

## Rules that repeat
- **Cut on the voice, not the beat.** Beat-sync is at chance level in all three (6-24 % on onset vs 7-23 % chance). The VO phrase decides the cut.
- **Accelerate, then hold.** Cuts per 10 s climb (Nadal 6 -> 15, So Win 4 -> 12), then the last shot is the longest (Nadal 8.3 s) or a black hold sits before the final act (Rip 2.3 s).
- **Silence before the payoff.** 0.35-0.95 s drop-outs right before "So, win.", before the final litany and before gags.
- **One grade for everything.** Mono (anthems) or a coded two-grade system (Rip: letterboxed teal/orange = fiction, flat full-frame = reality). Archive footage is graded to match.
- **End card = the line, nothing else.** Futura Condensed ExtraBold caps (So Win: 19 % + 40 % of frame height, justified) or a small serif in sentence case (Nadal: ~4 %). Hard on, no animation, swoosh hard on with an audio hit.
- **Loudness:** anthem/comedy masters at about -24 LUFS integrated (broadcast spec), Nadal at -10.7 LUFS. Don't copy the quiet master for social; copy the dynamics (silence -> hit).

## Recipe (real footage + HTML/GSAP)
1. Write the copy as a device ("You can't X / So, X") and record VO first. Lay one shot per phrase.
2. Grade all clips in CSS the same way: `filter: grayscale(1) contrast(1.25) brightness(.92)` + grain overlay at 3 %.
3. Alternate still "portrait to camera" shots (subject on black, one hard light) with real work/action footage.
4. Shot lengths: open 2-4 s, middle 0.8-1.2 s, last third 0.3-0.7 s, then one 6-8 s end shot or a 0.6-2.3 s black.
5. Before the payoff line, kill the music for 0.4-0.9 s, then hit with real ambient sound.
6. End card: hard `gsap.set` on, no easing. Big condensed caps (Anton, 19vh/40vh, line-height .88) or a small serif (EB Garamond 3.2vh). Logo hard on + hit SFX, 2 s hold, end.
