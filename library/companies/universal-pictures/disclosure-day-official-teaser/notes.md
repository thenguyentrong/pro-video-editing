# Disclosure Day | Official Teaser  (Universal Pictures, 16 Dec 2025, 126.0 s, 16:9 file / 2.39:1 picture, cards full frame, YouTube)
URL: https://www.youtube.com/watch?v=UFe6NRgoXCM
Purpose: teaser (first footage, about 6 months before release)
One-sentence point: someone is about to prove to the world that we are not alone, and ordinary people start to feel it.

## Structure (beats with timestamps; % of 126 s)
- **No studio logo at the start.** 0.0–0.17 black, then straight into the story.
- 0.17–17.3 **quiet cold open (14 %)**: a man in a doorway (4.0 s), a dark window with deer outside (4.6 s), a macro hand holding a small object, a child in bed under a lamp, a man at a desk, the lead's close-up. Dialogue at −25…−33 dBFS RMS asks the question of the film.
- 17.3–43.3 **the broadcast scene**: a TV weather presenter in a studio, held 7.8 s (longest shot), cut with the control room; her speech breaks apart. **Drop-out** 30.15–30.6 s to −54 dBFS, then a +38.5 dB hit at 30.65 (biggest rise). Reactions: a phone in a field, crowds, nuns.
- 43.3–49.0 black, a 0.4 s drop-out at 43.55, then the **card "FROM DIRECTOR / STEVEN SPIELBERG"** builds (44.3–47.0) and holds to 49.0 (at 35 %).
- 49.0–77.2 **escalation**: a crowd of phone lights, a man awake at night, a huge control room (loudest 0.5 s at 56.2, −8.8 dBFS), a lab, a man shouting, two extreme eye close-ups (1.8 + 2.3 s).
- 77.2–79.7 **card "THIS SUMMER"** (2.5 s, 61 %).
- 79.7–84.1 **scale shot**: aerial of a crop-circle pattern with one tiny figure (4.4 s).
- 84.1–111.8 montage: three shots of 0.42–0.71 s, then ASL ≈1.5 s: people looking up, a flashlight, a car chase on a farm, two hands reaching toward each other on white.
- 111.8–116.5 black dip, then a night house in the woods with lights coming down (4.7 s).
- 116.5–121.5 **title** "DISCLOSURE DAY" (5.0 s, at 92 %), on the loud music (−10…−12 dBFS).
- 121.5–124.5 three credit cards, **exactly 1.0 s each** (story by / screenplay by / directed by), the music falls to −40 dBFS under them.
- 124.5–126.0 **"SUMMER 2026"** + format logos, on a last hit (+27 dB at 124.6).

## Cut rhythm
- 56 shots (adaptive detector; 3 credit-card changes added by eye). **ASL 2.25 s**, median 1.71 s.
- ASL per quarter **2.86 · 2.63 · 1.85 · 1.66 s** (speeds up steadily). 18 % of shots under 1 s, 29 % over 3 s. 26.7 shots per minute.
- Cuts per 10 s: 3 5 2 5 3 2 4 5 5 7 6 4 1 (densest 90–100 s = 71–79 %).
- Cuts on audio onsets 24 % vs 33 % chance: cuts follow the dialogue, not the music.
- Speech in ≈99 s of 126 s (78 %): a dialogue-driven teaser.

## Typography
- One face: condensed, slightly rounded caps (closest free fonts: Oswald 500 or Antonio 600), silver-white #f0f9f6 with a soft white glow, on full-frame black (cards drop the letterbox).
- Sizes (≈, glow excluded): "THIS SUMMER" ≈21 % H, title ≈23 % H spanning 17–82 % W; "FROM DIRECTOR" ≈8 % H over a ≈14 % H name; credit cards the same two-line layout; date "SUMMER 2026" ≈15 % H with format logos ≈3.5 % H at 67 % and 74 % H.
- **Animation = "declassified" reveal**: the letters appear as thin vertical slices that fill in over 1.8–2.7 s, then the glow blooms. Out: hard cut. Holds: director card 4.7 s, month card 2.5 s, title 5.0 s, credits 1.0 s.

## Colour / grade
2.39:1 picture (61 px bars at 480p). Cool, low-key night interiors with warm practical lamps; broadcast blues and reds; one golden field (crop circle); one white, high-key insert (hands). Cards are neutral silver.

## Camera / shots
Medium dialogue shots, extreme eye close-ups, a macro hand, crowds looking up, a locked aerial of scale, one car-chase burst. Long takes in the newsroom (4–8 s).

## Transitions
Hard cuts; two black dips (43.3, 111.8); cards resolve out of black. No dissolves between shots.

## Sound
- Integrated **−14.0 LUFS**, LRA 11.8 LU, true peak +0.9 dBTP.
- Open at −25…−33 dBFS with dialogue; from 49 s the music and hits sit at −10…−15 dBFS.
- Two short **drop-outs** (0.45 s at 30.15 and 0.4 s at 43.55, floor −51…−54 dBFS), each followed by a hit of +37…+39 dB.
- No pre-title silence: the title rides the loudest bed, then the end block drops to −40 dBFS and closes on one last hit under the date.

## What makes it premium
- No logo, no music for the first seconds: the film's question and a dark window start the piece.
- One long, uncomfortable scene (the broken broadcast) instead of a montage of events.
- A card animation that tells the story (classified text being revealed).
- Scale held once: a 4.4 s aerial of a tiny figure in a crop pattern.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Bars 138 px (2.39:1) on footage; cards full-frame `#000`.
2. 0–17 s: five or six 1.5–4.5 s shots under quiet dialogue (−28 dBFS).
3. One 20–25 s scene that breaks down, with a 0.4 s mute and a +35 dB hit in the middle.
4. Card: two lines, `font-family:Oswald; font-weight:500; color:#f0f8f6; text-shadow:0 0 18px rgba(220,255,250,.45)`; small line 90 px, main 150 px (title 250 px). Reveal: put the text behind 40 vertical slit masks (`clip-path: inset(0 x% 0 y%)` per slice) and open them with `stagger:{each:.04, from:"random"}` over 1.8 s, then glow `text-shadow` 0→18 px in 0.8 s. Hard cut out.
5. Last third: ASL 1.5 s, three shots of 0.4–0.7 s, a black dip, one held image of 4–5 s, title 5 s on full music, credits 1.0 s each with the music down to −40 dBFS, then the date on a final hit.
6. Master −14 LUFS, true peak −1 dBTP.
