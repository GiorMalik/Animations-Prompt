# V10 Aurora & Glassmorphism
- Category: V mg-styles-15 · mg-styles-15
- Fit: Soft glow, quiet passages

## Style Prompt

# Gradient Blur (Aurora) & Glassmorphism

**Original film**: Aurora — think in light ('Think, and there is light') · 1920×1080 · 30 fps · 10 s · final AI review score 8.07 / 10

**Source code**: [demos/12-aurora-glass/](../demos/12-aurora-glass/)

## How to use

1. Create a new empty folder, and open an AI assistant in it that can write code and run commands (e.g. Claude Code). This machine needs to be able to render web pages (Node + Chrome) and run ffmpeg.
2. Copy the whole "Prompt" section below and send it.
3. To make it your own content: change the story, brand name, copy and colours in `Creative seed`, or change the dimensions in `Output` (e.g. vertical 1080×1920). Don't delete the `Signature features` section — it's what makes this style recognisable at a glance.
4. To push it further: once the film is out, open a separate AI to review it with [rubric.md](../rubric.md), then paste the review back to the making AI for another round. That's how the original film was revised twice.

## Prompt

```text
You are the director, motion designer, engineer and sound designer of ONE 10-second motion-design film.
The goal is the most classic, yet most stunning form of this style — award-shortlist / high-end commercial quality. A clean,
template-looking result is a fail. Benchmarks: Buck, ManvsMachine, Ordinary Folk, Giant Ant, Territory Studio, Apple keynote
motion, Pentagram motion identities, top Behance/Motionographer features, top Douyin/Bilibili designer accounts.

# Style
Gradient Blur (Aurora) & Glassmorphism

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML WebGL: aurora mesh-gradient shader + glass refraction (SDF lens, chromatic dispersion) + DOM/CSS backdrop-filter glass cards
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
"Liquid Glass"2025–26 AI-product-launch aesthetic: slow, translucent, expensive.
- Deep indigo-black base; 4–5 aurora blobs (violet/blue/cyan/magenta, adjacent hues only) drifting on bezier paths, blending into a mesh gradient, 3–5% noise dithering (no banding).
- Frosted glass cards (backdrop blur ~30px, 5–10% white fill, 1px 30% white inner highlight, large radius) float in with parallax depth and slight 3D tilt; micro-UI inside (chat bubble, voice waveform, toggles) animates with opacity + 8px rise.
- WOW: a Liquid-Glass lens (true refraction, chromatic dispersion on the rim, specular edge) glides across and magnifies the aurora and the cards.
- Title (invented product, e.g. "Aurora — think in light") in a light elegant sans; sine/breathing easing everywhere; nothing fast.
Sound: ambient cinematic pad, soft shimmer, very subtle UI ticks.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
Large Gaussian-blurred colour blobs (aurora/mesh gradient) drift slowly as the ground, with frosted translucent glass cards floating above. Apple's iOS 26 Liquid Glass and the AI product launches made this the default look for 2024–2026 tech brand films — its character is 'slow, translucent, premium'.
Visual traits: large blurred colour blobs drifting, frosted glass cards, 1px highlight outlines, low-contrast adjacent-hue palettes, slow breathing rhythm
Key technique — the aurora base: 3–5 large solid-colour circles, blur 80–150px, each drifting on a bezier path in a 20–40 s loop, blending into a mesh gradient feel
Glass card recipe: backdrop-filter blur(20–40px) + 5–10% white fill + 1px 30% white inner stroke + large corner radius
Use 2–3 adjacent hues (violet-blue-cyan / orange-pink); clashing colours look dirty; bright blobs on a dark ground work better than on a light one
3–5% noise over everything to prevent banding (crosses over with the grain-texture technique)
Easing close to linear or a sine breathing curve — everything is slow; fast movement instantly breaks the mood; text also enters with only opacity + 8px of movement

# How to work
1. Treatment. Write down one clear idea: a hook in the first 0.5 s (never open on more than 0.3 s of empty or black), an
   escalation, one unmistakable hero moment at ~60–75 % of the runtime, and a composed end frame held ~0.8–1.2 s with living
   micro-motion. Map every signature feature above to a moment. Keep one cue sheet (beats and hit times) that both the
   picture and the sound read from.
2. Key frames before motion. Build the look, render stills at 6–10 key times and actually look at them. Each still should be
   poster-worthy: composition, hierarchy, negative space, type set properly (kerning, line-height, weight contrast, CJK
   punctuation, ~5 % safe margins). Iterate until nothing looks default, generic, cramped or "AI-template".
3. Motion. Build the choreography and preview at low resolution. Step through the fastest moves frame by frame: spacing,
   easing, arcs, overlap, anticipation and follow-through, motion blur. No unintended dead spans; the energy follows the music.
4. Sound. Write genre-correct music and sound design locked to the cue sheet. Check that visual hits land on audio onsets.
   Master to the output spec.
5. Final. Render at full resolution (motion blur where apt), then check: exactly 10.00 s, resolution, fps, audio present and at
   the right loudness, no black frames, no fallback fonts or tofu, no clipped elements at the frame edges, no shimmer on thin
   lines, no gradient banding. Fix and repeat until you would submit it to a festival.
6. Write an honest self-critique: what is strongest, what is weakest, what you would do with more time.

# Rules
- Rendering must be deterministic: every frame is a pure function of time t. Seeded randomness only; physics and particles
  precomputed or closed-form; no real-time clocks; no state-triggered CSS transitions. A reliable route: a web page that can
  draw any time t on request, captured frame by frame with a headless browser and encoded with ffmpeg (or a Blender script
  that renders a PNG sequence).
- Assets: only CC0 / public domain / OFL / Apache / free-for-commercial-use. Record each source and licence in CREDITS.md.
  No real brand trademarks; invent brand names.
- On-screen text must be correct and natural: idiomatic Chinese, proper CJK punctuation, no typos.

# Craft checklist (what a jury looks for)
- Style authenticity: an expert names the style in one second; every signature technique is present and executed correctly.
- Motion craft: purposeful easing (no linear unless mechanical by design), overlap and stagger, anticipation and
  follow-through, arcs, squash and stretch where the style allows, consistent physics, motion blur where apt; transitions
  carried by elements, not crossfades.
- Rhythm: hits locked to the music; contrast between busy and calm; no monotony.
- Design: strong composition, grid, typographic hierarchy, controlled palette; texture and finishing (grain, glow, vignette)
  only where the style wants it; nothing looks accidental.
- Technical polish: no jitter (unless intended), no popping, no aliasing, no banding, no fallback fonts, no half-loaded images.
- Sound: genre-correct, musical, synced, mastered.

# Before you deliver, score yourself honestly
1–10 on style fidelity, concept wow, motion craft, design & typography, finish & texture, sound & sync, technical
(6 = template-level, 8 = high-end agency, 9 = award shortlist). Aim for 9; fix whatever scores lowest first.

# Deliver
video.mp4, plus a short report: the concept in two sentences; a beat sheet with timecodes; how each signature feature is
realised; the tech route; check numbers (duration, resolution, fps, loudness, true peak); your honest top-3 weaknesses.
```
