# V11 Geometric Bauhaus
- Category: V mg-styles-15 · mg-styles-15
- Fit: Geometry, design feel

## Style Prompt

# Geometric / Bauhaus Motion

**Original film**: KONSTRUKTION · 20 SCHLÄGE ("Twenty-beat construction") · 1920×1080 · 30 fps · 10 s · final AI review score 7.71 / 10

**Source code**: [demos/09-bauhaus/](../demos/09-bauhaus/)

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
Geometric / Bauhaus Motion

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: SVG/Canvas + GSAP on a strict modular grid, beat grid at 120 BPM
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
"Bauhaus Kinetic Poster" — Bauhaus 1919 kinetic poster — mechanical, rational, musical.
- Cream paper (#F1E9DA), primaries red #E03C31, yellow #F2B705, blue #1E4FA3, black #111; strict modular grid (e.g. 240px modules); every move is an integer number of modules; every landing on a grid line.
- 120 BPM (0.5 s/beat): each beat a module acts — quarter circles rotate 90° about a corner pivot, semicircles slide one module, triangles flip, squares split; rotation pivots alternate (own centre / corner / frame centre).
- 0–2s grid lines draw & the first red circle lands; 2–6s the composition assembles into a Kandinsky/Bauhaus poster; 6–8s phase-shifted cascade wave across the grid on the drop; 8–10s freeze into a perfect poster with Swiss typography: "BAUHAUS" set vertically in heavy geometric sans + small caps "FORM · FARBE · FUNKTION".
- Easing: power2.inOut or linear — NO overshoot; subtle paper tooth + slight print misregistration allowed.
Sound: minimal techno/click — each flip = a pitched click/blip, kick on quarters.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
Circles, triangles and rectangles translate, rotate and scale precisely on a strict grid, in a limited palette of the three primaries plus black and white — the orderly beauty of mechanical rationality. It comes from the Bauhaus and Swiss International graphic tradition (Adobe once worked with the Bauhaus archive on the Hidden Treasures project), and is the mainstream language of the kinetic poster, naturally in step with a music beat.
Visual traits: basic geometric shapes, limited red-yellow-blue-black palette, strict grid alignment, rotation around the geometric centre, beat-driven modular movement
Key technique — every movement is anchored to the grid: displacement = a whole multiple of the grid module, landing points always on grid lines
Restrained easing: easeInOutQuad or simply constant speed; overshoot is banned — the mechanical feel is a feature, not a flaw
Beat-driven: each geometric element appears/flips instantly on a beat point, one action per beat — like the beat-sync logic already used elsewhere
Rotation pivot play: alternating between rotating around the shape's own centre, an edge vertex, and the frame centre to make rhythm
Generative variant: Processing/p5.js driving arrays of geometry in bulk with trigonometric phase differences (the mainstream approach in the Chinese kinetic-poster scene)

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
