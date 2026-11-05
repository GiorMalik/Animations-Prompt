# V6 Shape Morph
- Category: V mg-styles-15 · mg-styles-15
- Fit: One shape becoming 6–8 meaningful icons in a row, e.g. coffee cup → sun → sunset over the sea → seagull → paper plane → location pin → heart; see also M38

## Style Prompt

# Morphing / Shape Morph

**Original film**: One Shape, Every Story · 1920×1080 · 30 fps · 10 s · final AI review score 7.64 / 10

**Source code**: [demos/08-morph/](../demos/08-morph/)

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
Morphing / Shape Morph

# Output (fixed)
- 1920×1080, 30 fps, exactly 10.000 s (300 frames), H.264 MP4 with stereo AAC audio (48 kHz), mastered to −14 LUFS
  integrated, true peak ≤ −1 dBTP. Final file: video.mp4.

# Suggested technical route
HTML: SVG + flubber or GSAP MorphSVGPlugin (tune shapeIndex), color-field wipes
(You may choose a better route if it clearly raises quality; say why.)

# Creative seed
"Everything Connected" — Apple-keynote-grade morph chain: one hero shape continuously becomes 6–8 meaningful icons, on the beat.
- Chain example: coffee cup → (circle) → sun → sunset over sea → gull → paper plane → location pin → heart → invented brand logo "morphe" with wordmark.
- Every A→B goes through a simple intermediate (circle/capsule) with rotation and 10–15% squash&stretch; sub-parts morph in sync (steam → sun rays → waves).
- Background color fields change with each morph (clean color-block wipes); ease cubic-bezier(0.7,0,0.3,1), 3-frame cushions at start/end; no knotting/tangling ever (check every morph mid-point stills).
Sound: rhythmic plucky arpeggio; a pitched whoosh per morph landing on the beat.

You are the director: you may change the concept, copy, story beats and brand names if you find a stronger idea, but the result must remain the CANONICAL, instantly-recognisable form of this style and must hit its signature features below.

# Signature features and key techniques (the result is judged against these)
One shape slides continuously into another: a phone becomes a map pin, a coffee cup becomes a sunset. It is the core grammar of visual storytelling, and the part that shows the most craft in Apple keynote motion and high-end explainers.
Visual traits: outlines transitioning continuously with no jumps, intermediate shapes bridging, morphs accompanied by movement and rotation, squash & stretch at the moment of change
Key technique — path alignment comes first: both shapes need the same vertex count, with first vertices in matching positions (reset first vertex in AE), or the morph tangles
Don't morph a complex A straight into B: converge first into a simple intermediate shape (circle/capsule), then expand — 'A → circle → B', 8–12 frames per leg
Layer 10–15% squash & stretch and a slight rotation over the whole morph to hide the mechanical feel of the interpolation
The speed curve peaks mid-way, cubic-bezier(0.7,0,0.3,1): leave 3 frames of buffer at each end
On the web, use the flubber/polymorph libraries for optimal vertex-matched interpolation — far better than naive SMIL

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
