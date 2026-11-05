# V12 80s Synthwave / VHS
- Category: V mg-styles-15 · mg-styles-15
- Fit: Retro neon, videotape

## Style Prompt

# Retro: 80s Synthwave / VHS / Y2K

**Original film**: NEON DRIVE · Midnight ("Neon night drive 1986") · 1920×1080 · 30 fps · 10 s · final AI review score 8.21 / 10

**Source code**: [demos/10-synthwave/](../demos/10-synthwave/)

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
Retro: 80s Synthwave / VHS / Y2K

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML WebGL (perspective grid, sun, mountains shader) + canvas chrome text + CSS/SVG glow; VHS pass
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
"OUTRUN 1986"The quintessential 80s synthwave title sequence.
- Starry night, striped retro sun (horizontal band cut-outs, magenta→orange→yellow), wireframe mountains, palm silhouettes, neon magenta/cyan perspective grid rushing toward the camera.
- 0–1s: VHS tracking noise + 'PLAY ▶' OSD; 1–4s: camera flies low over the grid, sun rises; 4–6s: CHROME title (e.g. "NEON DRIVE", multi-stop metallic gradient, bevel highlight, star glint sweeping across) SLAMS in with a lens flare; 6–7.5s: pink neon script word (e.g. "Midnight") writes on like a neon tube with flicker; 7.5–10s: sustained ride, subtle VHS chroma bleed/scanlines, end on the hero frame.
- Double glow (tight ~4px + wide ~30px), deep purple sky gradient.
Sound: synthwave — gated-reverb snare, arpeggiated saw bass, lush pads, big chord + crash on the title slam.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
A wholesale reference to a specific era's media aesthetic: 80s synthwave is neon grids + sunset gradients + chrome type; VHS is scanlines + colour shift + tape noise; Y2K millennium style is liquid chrome metal, acid green-purple, skeuomorphic system windows and low-fi 3D. Y2K has come back strongly in music videos and trend brand films over the past two years, and the Bilibili template marketplace supplies plenty of 'acid chrome' material.
Visual traits: neon glow, perspective-grid horizon, scanlines and RGB shift, chrome metal type, acid palettes, skeuomorphic window UI
Key technique — the synthwave trio: scrolling perspective grid (one-point-perspective grid + looping vertical displacement), multi-layer gradient sunset orb, double glow (tight 4px bright inner layer + diffuse 30px low-opacity outer layer)
VHS ageing chain: RGB split (red and blue channels offset 1–2px each) → scanlines (2px gaps, 10% black bars) → wavy distortion jitter (1–2 random glitch frame-drops per second) → 4:3 rounded-corner mask
Y2K chrome type: extremely high-contrast multi-band metal gradients + bevel highlights + environment-mapped reflections, plus lens flare
Y2K motion language: pop-up appearances, cursor clicks, window drags — the skeuomorphic interface IS the animation storytelling
Deliberately unstable frame rate: key passages drop to 15fps or play 2 frames backwards to fake a tape jam

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
