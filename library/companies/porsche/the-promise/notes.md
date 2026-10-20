# The Promise | Porsche. There is no substitute.  (Porsche, 2025-07-15, 1:34, 16:9, YouTube @Porsche)
URL: https://www.youtube.com/watch?v=wSnZ5F83gro
Purpose: brand film (community / heritage anthem)
One-sentence point: Porsche is made by its fans - the rebels, restorers, artists and racers - and the brand promises them "there is no substitute".

## Structure (cut list + English captions)
- 0.0-5.8 hook: fast landscape plates at golden hour - mountain road, car passing, a tilted ocean wave (4-5 s, camera rolled ~40 degrees). No product hero yet.
- 5.8-22 "This is a promise to you, the rebels and leaders, the restorers and the avant-garde": archive (1950s design clay model, engineers - pillarboxed archive photos at 6-7 s), sunset silhouettes, cars on coast roads, a paint gun on an art car.
- 22-34 "Our word of honor to those who cheer us...": key ring, crest macro (23 s), cowboy fan, racing driver in helmet, crowd with phones at night, podium champagne. 0.65 s silence at 32.5 s, then "challenge us" / "The greatest of all compliments" (34.3 s).
- 34-66 the community montage: restorers, street, art cars, carpets ("because wow, that's pretty cool" - a casual laugh line at 52 s), surfers, Santa Monica, mountain peak.
- 66-85 heroes: drivers, kids at the window, Super-8 archive (72-74 s, in a film-gate frame), Le Mans 917 blur (75 s), Dua Lipa close-up (81 s), a man on a cliff at dusk (83-85 s). VO "It's been said before and it remains our promise to you."
- 85.12 end: cut to black, "PORSCHE" wordmark blurs in (85.1-86 s), sharp 86-90 s, then fades. VO "Porsche. There is no substitute." (81.3 s, finishes over the logo).
- 91.12-94.1: legal WLTP consumption/CO2 text, top-left, small (EU requirement).

## Cut rhythm
- 117 shots in 94 s. ASL 0.80 s, median 0.68 s. ASL per quarter 0.78 / 0.71 / 0.71 / 0.98 s.
- Longest 6.0 s (logo card), 3.0 s (legal card), 1.96 s (83.16, the cliff man). Shortest 0.16 s (76.48), 0.20 s, 0.24 s.
- 75 % of shots under 1 s, 1 % over 3 s. 14-16 cuts per 10 s for the whole middle.
- Cuts do not follow music onsets (20 % vs 16 % chance) - steady montage pulse instead.

## Typography
- No titles in the film. Only the end card: Porsche wordmark (wide extended caps, Porsche Next / custom wordmark; closest free: Michroma or Syncopate), white on black, 42 % of frame width, 5 % frame height, dead centre.
- In: Gaussian blur to sharp in ~0.9 s. Out: fade to black around 90 s.
- Legal card: small sans (looks like Porsche Next), ~1.5 % line height, left-aligned at x 10 %, top 20-78 %.

## Colour/grade
- Warm golden-hour film look: lifted blacks, soft contrast, orange/teal, lens flares (9-10 s), slight film grain and halation. Archive shots keep their own colour (faded 60s/70s colour, Super-8 gate with rounded corners).
- No letterbox; archive photos pillarboxed inside 16:9.

## Camera/shots
- Mostly real footage of real people and events (fans, races, meets, Le Mans, kids) mixed with staged golden-hour car drives.
- Many camera rolls/dutch angles on the road plates (4-5 s, 14 s: horizon tilted 30-45 degrees), close-ups of hands, keys, crests.
- Celebrity cameo (Dua Lipa) for 1 s only, no name super.

## Transitions
- Hard cuts only. One blur-in on the logo. Archive formats used as texture, not as transitions.

## Sound
- VO (English, relaxed) over an orchestral/indie build. Integrated -13.0 LUFS.
- Drop-out 32.5 s (0.65 s, to -50 dBFS) before "The greatest of all compliments".
- Loudest 0.5 s at 86.85 s (-12.3 dBFS) - the logo sting; hit at 86.7 s (+15 dB).

## What makes it premium
- Real community footage instead of models: credibility through variety (75 % of shots < 1 s).
- Warm, filmic grade on everything new; archive left honest.
- No supers, no product specs, no names - only the VO line and the wordmark.
- Logo blur-in on black with a sting, then a long 4 s hold - calm after 85 s of speed.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Collect 100+ short real clips (customers, crews, sites, archive). Trim to 0.5-0.9 s each; keep 2 s for the last human shot.
- Warm grade in CSS: `filter: sepia(.15) saturate(1.1) contrast(.95) brightness(1.03)` + grain + an orange `radial-gradient` flare layer at `mix-blend-mode: screen`, opacity .25, on 3-4 shots.
- Archive: put old photos in a `<div>` with `border-radius: 6%` and a black pillarbox to mimic a film gate.
- End card: black, wordmark `font-family: Michroma; letter-spacing: .35em; font-size: 5vh; width: 42vw`. `gsap.fromTo(logo, {filter:'blur(18px)', autoAlpha:0}, {filter:'blur(0px)', autoAlpha:1, duration:.9, ease:'power2.out'})`, hold 4 s, `autoAlpha:0` over 0.8 s. Sting SFX at +0.6 s.
- Silence 0.6 s in the music before the key line of the VO.
