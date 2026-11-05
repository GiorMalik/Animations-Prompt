# H1 Biennale Yellow

- Category: H Ready Layouts · Ready Layouts
- What it looks like: Warm parchment background, a sun-yellow halo, a big serif headline, indigo ink, fine lines

## Style Prompt

> This prompt is a rewritten, detailed version: the visual rules, colors, and timeline are all pinned down, so DeepSeek and Opus 5.5 can use it directly. {{ }} marks the parts for you to fill in.

You are a front-end motion engineer. Write **one complete index.html file**: only vanilla HTML + JavaScript + Canvas, no external libraries, font files, or images. Make an animated title card in the style of an "art biennale magazine cover".

## Content

- Main headline (two lines): {{first line, e.g. Biennale}} / {{second line, e.g. Yellow}} (second line in italics)
- Header left: {{e.g. THE TWELFTH BIENNALE · EDITORIAL SERIES}}; header right: {{e.g. N° 01}}
- Footer left: {{a one-line description}}; footer right: {{number}}
- Total length: {{seconds, default 6}}

## Output requirements (follow exactly)

1. Output only one HTML code block, with no explanation. The code must be complete and runnable: no ellipses, no "same as above" or "omitted here".
2. The canvas is fixed at 1920×1080; use CSS to scale it proportionally and center it, with black bars filling the extra space.
3. Every frame is decided by the function `draw(t)` (`t` in seconds). Do not use `Math.random`; generate the paper texture with seeded mulberry32(seed).
4. Loop by default; space pauses/resumes; when the URL carries `?t=3`, show only the frame at 3 seconds.

## Colors and lines (use only these)

- Base color paper = #F2E9D2; add paper texture: 5000 tiny 1–3px squares, half #8C7A55 and half #FFFAF0, opacity 0.045–0.095. Draw the texture once and cache it on an offscreen canvas.
- The only accent color, sun = #F6C23E.
- All text and lines use ink = #1D2A68, line width 1.6–1.8px.

## Type

`font-family: Georgia, "Times New Roman", "Noto Serif SC", "Songti SC", serif`. Serif only, throughout. Main headline about 214px, `letterSpacing = '-4px'`; header 26px, uppercase, `letterSpacing = '6px'`; footer text 34px. (Canvas `ctx.letterSpacing` works in newer browsers; where it is not supported, draw character by character.)

## Layout (coordinates for 1920×1080)

1. Outer frame: `strokeRect(64, 64, 1792, 952)`; then two horizontal rules: y=148 and y=932, from x=64 to x=1856.
2. The sun, center (1380, 470):
   - Halo: a radial gradient, radius 20→560, from `rgba(246,194,62,1)` to `rgba(246,194,62,0.92)` (at 38%), then to `rgba(246,214,120,0.35)` (at 70%), to `rgba(246,214,120,0)` (at 100%);
   - Solid disc: radius 250, color sun;
   - Three thin concentric rings: radii 250, 330, 410 (ink, opacity 0.9, 0.45, 0.45);
   - Tick ring: radius 410 to 421 (every 5th tick longer, reaching 432), 120 ticks total, ink, opacity 0.85.
3. Main headline: left edge x=100, first-line baseline y=560, second line (italics) baseline y=770. Make sure the right end of the headline does not touch the tick ring (its leftmost point is about x=948).
4. Header small-text baselines y=118 (left x=104, right x=1650); footer text baseline y=980 (left x=104), number right-aligned to x=1816.

## How it moves

- 0–0.8 s: the outer frame and the two rules "draw themselves" from the corners toward the middle (use `setLineDash` or clip by progress);
- 0.4–1.8 s: the sun rises into place from 300px below (ease-out), halo opacity 0→1;
- 1.0–2.4 s: the two headline lines fade in one after the other from 24px below, letter spacing tightening from +20px to −4px;
- 2.0–2.8 s: header and footer fade in; the tick ring turns slowly clockwise at 1° per second;
- Final 0.5 s: fade everything out to the paper color, then loop.

## Don't

Gradient blocks, shadows, rounded cards, a second accent color, a sans-serif headline, glow, particles.

## Check your own work when done (don't output this)

- Does the whole film use sun as its only accent color?
- Does the headline touch the tick ring?
- Refresh the same `t` twice: is the picture exactly the same?
