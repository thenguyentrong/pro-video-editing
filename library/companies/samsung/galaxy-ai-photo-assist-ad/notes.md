# Galaxy AI | Photo Assist & Creative Studio | Galaxy S26 Ultra  (Samsung, 11 Mar 2026, 0:35 (30.3 s content + 4.7 s black), 16:9, YouTube @Samsung)
URL: https://www.youtube.com/watch?v=guKQSNsnBfo
Purpose: ad (Galaxy AI feature spot)
One-sentence point: the dog ran out of the party photo - type "Add my dog" and Galaxy AI puts it back, then turns it into a party and stickers.

## Structure
- 0-2.2 s: party at night, man shooting with the phone; super "The new Galaxy S26 Ultra" left (two lines).
- 2.2-3.8 s problem: "Some moments don't sit still" centred (line 5.4% H, cap ~5% H), the corgi runs off.
- 3.8-5.7 s: camera module in hand (product beat).
- 5.7-10.4 s demo: POV phone, prompt pill "Add my dog" -> tap Generate (7.7 s) -> the dog appears in the photo (9.6-10.2 s).
- 10.4-16 s escalation: result full frame; prompt "Change to daytime" -> iridescent glow sweep (12.7-13.3 s) -> daylight; "Birthday party in wonderland" (14 s); "Add birthday sunglasses on dog" (15 s).
- 16-24.8 s Creative Studio: select photo, dog in glasses close-up, sticker sheet UI, share in chat.
- 24.8-27.5 s payoff: animated sticker dogs pop around the real dog; "Simply unleash your creativity" -> "with Photo Assist ✦" (26.3 s).
- 27.5-29.4 s product lockup "The new / Galaxy S26 Ultra / Galaxy AI ✦" on violet product.
- 29.4-30.3 s SAMSUNG on black, then 4.7 s black (upload padding).

## Cut rhythm (cuts2 + 4 soft transitions added after checking by eye)
- 17 shots, ASL 1.78 s, median 1.44 s. Quarters 1.26 / 1.89 / 1.52 / 1.51.
- 18% < 1 s, 6% > 3 s. Longest 4.7 s (5.7 s, the generate demo - one take), shortest 0.54 s (3.8 s).
- 5-6 cuts per 10 s, flat. Cuts on onsets 38% vs 28% chance.

## Typography
- Samsung Sharp Sans Bold, white, centred for statements (cap ~5% H), left-aligned 2-line super for the product name at the start.
- Prompt pill: rounded rectangle ~45% W x 9% H, translucent grey-white glass, prompt text left (regular, ~3% H), image icon right; sits at ~85% H over the photo - the visual "UI language" of the ad.
- End lockup same as the launch film: 3 lines, left third, over the product.

## Colour / grade
- Warm night party (string lights, orange-brown), then bright daylight greens, then candy party colours. AI glow = blue/teal/purple iridescent band.
- 17% of samples >= 70% empty (all on dark, the logo/black end).

## Camera / shots
- Real lifestyle at night, phone-in-hand POV close-ups, product macro (camera bump), cartoon sticker animation composited over the real dog.

## Transitions
- Mostly hard cuts; 4 soft: hand moves into frame, photo expands from phone to full frame (10.4 s), the glow sweep morph (12.9 s), UI dissolve (21.2 s).

## Sound
- Licensed vocal pop track (auto-captions read "Make a move now... you're just my type"; exact song not verified). No narrator.
- Integrated -10.0 LUFS (loud, social-ready). Three tiny 0.15-0.2 s stops (7.9, 11.05, 17.9 s) land on UI taps/generates. Biggest rise +32.9 dB at 14.25 s (wonderland reveal). Loudest 26.75 s (sticker payoff).

## What makes it premium
- One clear problem -> one tap -> escalating results (each one bigger than the last).
- The UI is real and readable; the result fills the screen right after the tap.
- Payoff mixes real footage with cartoon stickers - playful, not cold tech.

## Recipe (real footage + HTML/GSAP)
- Shoot 1 night party scene + POV phone inserts (screen replaced in post or screen recording composited).
- Problem line centred, cap 5% H, 1.6 s hold, fade 0.3 s.
- Prompt pill: `border-radius: 999px; background: rgba(255,255,255,.18); backdrop-filter: blur(16px); height: 9%H; width: 45%W; bottom: 10%`. Type the prompt (35 ms per character), then a 0.15 s music stop + a tap ring, then the result.
- Glow sweep: absolutely positioned div, `linear-gradient(100deg, transparent, #60a5fa 40%, #5eead4 55%, #c084fc 70%, transparent)`, `mix-blend-mode: screen`, `x: -100% -> 100%` over 0.6 s `power2.inOut`, crossfade the after-clip at the band's centre.
- Pace: ASL ~1.5 s, one 4-5 s demo take in the first third.
