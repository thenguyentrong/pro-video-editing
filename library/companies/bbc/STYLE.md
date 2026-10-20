# BBC – video style

Examples studied (Oct 2026):

| Example | Type | Content length | Shots | ASL | Median | Integrated / LRA |
|---|---|---|---|---|---|---|
| [bbc-one-lens-ident-trampoline](bbc-one-lens-ident-trampoline/notes.md) | BBC One channel ident ("Lens", 2022), fan-archive upload | 40.0 s | 1 | 40.0 s | 40.0 s | −11.9 LUFS / 3.8 LU |
| [night-manager-s2-trailer](night-manager-s2-trailer/notes.md) | drama trailer (BBC One / iPlayer) | 89.0 s | 91 | 0.98 s | 0.88 s | −22.9 LUFS / 4.9 LU |
| [planet-earth-iii-trailer](planet-earth-iii-trailer/notes.md) | landmark natural-history trailer (BBC Earth) | 59.0 s | 50 | 1.18 s | 0.92 s | −14.1 LUFS / 7.6 LU |

## The look in one paragraph
The BBC's constant is its brand frame, not a cutting style: the three-block BBC logo is on every frame (top-left bug at ~3–4 % of frame height on trailers, top-centre lockup on idents and end cards), the type is a clean humanist/geometric sans, and every promo ends on a branded card with a "Watch on iPlayer" call to action. Inside that frame the style follows the genre. Channel idents show real people in real British shared spaces in one locked-off long take, and one circular brand device (the "Lens", heir to the BBC One globe/circle) passes through for ~7 s, then the shot simply continues so continuity can talk over it. Trailers cut fast (ASL ~1.0–1.2 s, median ~0.9 s) and only slow down for the last two shots or the end title. Drama trailers carry the message in giant, very wide one-word cards on black (cap height ~23 % of frame); natural-history trailers carry it in thin, widely tracked caption lines (cap ~2.5 %) placed only on calm aerial plates, written as one short poem. Sound is a steady bed with no mid-trailer hits; the end gets a short silence and a sting.

## Sub-styles
1. **Channel ident** (BBC One "Lens"). One locked-off real location with real people, logo blocks top-centre + "ONE" bottom-centre static from the first frame, a circular lens rotates in (1.6 s), turns face-on to show a second community space inside it (3.2–6.4 s), turns copper and exits (by 9 s), then a 31 s tail of the same shot. Loud, flat music bed.
2. **Drama trailer** (The Night Manager S2). 2:1 letterbox, BBC bug top-left + show-title bug top-right, iPlayer pill in the first seconds, drone aerials as location chapters, 58 % of shots under 1 s, tagline as five one-word cards alternating with action (THE / HEAT / IS / BACK / ON), two slower closing shots, end card with BBC blocks + a single brand image (orchid) + title + "Watch on iPLAYER".
3. **Landmark nature trailer** (Planet Earth III). Opening numeral "III" as frosted bars over an aerial, 10 caption lines forming one poem ("17 years ago our eyes were opened… This is our future"), each on a calm graphic aerial followed by 2–5 action shots of 0.5–1 s, a turn to humans and fire in the last third, symbolic end title (eclipse ring + one tree silhouette + stacked tracked title).

## Rules (most important first)
1. **Brand frame on every frame.** BBC blocks bug top-left at 3–4 % of frame height with ~2.5 % margins on trailers; top-centre lockup on idents and end cards. Programme title bug top-right in small tracked caps on drama trailers.
2. **Real people, real places, long takes for idents.** One locked-off wide shot, documentary casting, no actors posing; the brand device is the only VFX.
3. **One circular device, used once.** The lens/circle enters, reveals a second space, leaves within ~8 s; after that the ident is a plain continuity bed.
4. **Trailers are fast and flat.** ASL 1.0–1.2 s, median ~0.9 s, 54–58 % of shots under 1 s, densest in the third quarter (13–14 cuts per 10 s); only the final 2 shots or the end title last 2–4 s.
5. **Text by genre.** Drama: one giant word per card (wide heavy sans, cap ~23 % H, white on black, hard in/out, ~0.45 s). Factual/nature: thin wide-tracked caps (cap ~2.5 % H, ~0.2 em tracking), centred one line, fades, never on a busy shot.
6. **Copy as one chain across the trailer.** Five word cards = one tagline; ten captions = one poem. No standalone slogans.
7. **Aerials as chapter markers.** Each new location or chapter opens on a drone/helicopter aerial (London, port, jungle, hillside city; dunes, braided river, sea).
8. **iPlayer CTA + branded end card.** 2.5–4 s end card: black or dark field, one symbolic brand image, title in wide-tracked caps, BBC blocks above, "Watch on iPLAYER" pill (magenta accent); a 0.2 s silence before the final sting.

## Recipe: a BBC-style promo in Hyperframes (real footage + HTML/GSAP)
- Frame: 16:9; for drama add a 2:1 letterbox (bars 5 %). Logo layer always on: three white squares (each 3.5 % of frame height, gap 0.4 %) with dark letters, top-left at 2.5 % margins; title bug top-right Oswald 500, letter-spacing 0.2em, 2 % height.
- Ident (40 s): one locked-off real plate; circle div 80 % of frame height showing a second plate with mix-blend-mode: screen; GSAP rotateY 85° → 0° (1.6–4.4 s, power2.out) and 0° → −80° with x → +45 % (6.4–9 s, power2.in), perspective 1400 px; copper ring via conic-gradient; logo top-centre (8 % H) and channel name bottom-centre (Inter 700, 5.5 % cap) static.
- Drama trailer (85–90 s): 85–90 shots of 0.5–1.4 s; aerial at each location change; word cards in Archivo Expanded 800, cap 23 % of frame height, #fff on #000, hard cuts 0.45 s, alternating with 0.4–0.6 s shots; last two shots 2–2.5 s; end card 2.5 s.
- Nature trailer (60 s): 8–10 captions in Montserrat 400 uppercase, letter-spacing 0.2em, cap 2.5 % H, centred at 49 % height, opacity 0→1 in 0.4 s; each caption on a calm aerial of 1.3–2.2 s followed by 2–5 action shots of 0.5–1 s; end title on a dark star plate with an SVG ring drawn in 1.2 s.
- End card: black, one brand image, title letter-spacing 0.3–0.5em, BBC blocks above, "Watch on iPLAYER" pill (border-radius 6 px, #000, white text, #f54997 accent).
- Sound: steady music bed (drama ~−20 LUFS momentary with dialogue on top; nature builds over 25 s to a −10 to −12 plateau); no SFX hits mid-trailer; 0.2 s silence then sting on the end card.
