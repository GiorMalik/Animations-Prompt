# Z5 Paper Cutting

- Category: Z Chinese Style · Chinese Style
- What it looks like: Red paper cut open, folk patterns / Chinese paper cutting

## Style Prompt

> This entry's prompt is a rewritten, detailed version: the picture rules, colours and timeline are all pinned down, so DeepSeek and Opus 5.5 can both use it directly. Fill in the {{ }} parts yourself.

You are a front-end motion engineer. Write **one complete index.html file**: only native HTML + JavaScript + Canvas, no external libraries, font files or images. Make a "Chinese paper cutting" style animation: a round pierced paper-cut window flower, cut from red paper folded in half, layered over window paper, with shadows.

## Content

- Theme: {{theme, e.g. a newlyweds' opening}}
- Total length: {{seconds, default 12}}
- Character to cut out in the centre: {{default "囍" (double happiness)}}

## Output requirements (must follow)

1. Output only one HTML code block, no explanation. The code must be complete and runnable: no ellipses, never write "same as above" or "omitted here".
2. Canvas fixed at 1920×1080, scaled proportionally and centred with CSS; the extra space is black bars.
3. Every frame is decided by the function `draw(t)` (`t` is seconds). Do not use `Math.random`; when you need randomness, use seeded mulberry32(seed), so the same `t` always draws exactly the same thing.
4. Loops by default; space pauses/resumes; a URL with `?t=5` shows only the frame at second 5.

## Colours

Window paper #F1E8D4; main red #C8102E; dark red #8F0B22. No colours besides these three — no gold, gradients or highlights.

## How to draw (follow these steps)

1. **Window paper**: fill with #F1E8D4, then draw 2000 thin short lines 8–34px long with seeded randomness (half #B9A98A, half #FFFAF0, opacity 0.05–0.11) as paper fibres. Draw this layer only once and cache it in an offscreen canvas.
2. **Make two sheets of red paper** (one offscreen canvas each, 1920×1080, origin moved to the centre of the frame):
   - `layerBase`: a dark red #8F0B22 disc, radius 452; use `destination-out` to cut 48 small holes of radius 10 around the outer edge (at radius 428), then cut out the whole circle inside radius 400 (leaving only a dark red rim).
   - `layerTop`: a bright red #C8102E disc, radius 404; use `destination-out` to cut the following, **each ring is "draw 1/N, then rotate-copy it N times"**:
     - 48 small holes around the outer edge: radius 9, at r=378;
     - 24 small drops: from r=342 to r=274, width 22;
     - 12 large petals: from r=244 to r=74, width 50;
     - 12 small diamonds: each rotated π/12 first, centre at r=226, width 32, height 48;
     - 12 small dots: each rotated π/12 first, radius 12, at r=170;
     - 12 inner-ring petals: from r=78 to r=148, width 26;
     - then cut out the centre circle of radius 66; then fill a small bright-red disc of radius 46 back into the centre; finally use `destination-out` to write the centre character on the small disc (bold 66px, centred).
   - Red "bridges" must be left between the petals — do not cut the red paper apart.
3. **Four corner flowers**: use another offscreen canvas to draw a "quarter circle" (radius 250, centre on the corner of the frame) in bright red, cutting: 9 small holes along the arc edge (radius 7), 4 drops, one round window of radius 58. Copy it to all four corners (flipped).
4. **Composite**: draw the window paper first; then draw `layerBase`, `layerTop` and the four corner flowers in order, setting the shadow before each layer: `shadowColor='rgba(70,12,12,0.38)'`, `shadowBlur=16`, `shadowOffsetX=5`, `shadowOffsetY=9`.

The drop shape can be drawn directly with this function (origin at the centre of the window flower, y axis pointing up as negative):

```js
function drop(g, y0, y1, w) {
  const d = y0 - y1;
  g.beginPath(); g.moveTo(0, y0);
  g.bezierCurveTo(w, y0 - d * .25, w * .9, y1 + d * .35, 0, y1);
  g.bezierCurveTo(-w * .9, y1 + d * .35, -w, y0 - d * .25, 0, y0);
  g.fill();
}
function ring(g, n, fn) { for (let i = 0; i < n; i++) { g.save(); g.rotate(i * Math.PI * 2 / n); fn(g, i); g.restore(); } }
```

## Motion

- 0–0.8 s: the dark red base disc expands from radius 0 to full (ease-out); 0.25 s later the bright red main disc expands the same way.
- 1.2–4 s: the pierced holes "open" ring by ring from the outside in (each hole's radius grows from 0 to its target, each ring 0.18 s after the previous, each hole 0.35 s); because the holes are cut out, implement this by passing "hole radius × progress" into the cutting steps above, regenerating `layerTop` every frame (rings already finished may be cached).
- 4–4.4 s: the centre character "stamps" in: scale 1.15 → 1.0.
- After that the whole window flower sways slowly at ±0.6° (6 s period), with the shadow offset following at ±2px.
- Hold still for the last second, then loop.

## Don't

Gold, gradients, plastic highlights, 3D, particles, glow, heavy shadows, or writing the character on the paper (it must be cut out).

## Check it yourself when done (don't output this)

- Are the holes cut with `destination-out`, not covered with the background colour?
- Are the 12 sections fully symmetrical?
- Do all shadows fall to the lower right?
- Does refreshing at the same `t` twice draw exactly the same picture?
