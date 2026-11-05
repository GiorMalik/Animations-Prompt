# B3 Particle Convergence

- Category: A–G Code Samples · B Particles
- What it looks like: Particles gather into a heart, a house, a person — then scatter again.
- Good for: Talking about something concrete: home, relationships, a person
- Keywords: gathering into form, shapes, scattering

## Style Prompt

> This prompt is a rewritten, detailed version: the visual rules, colors, and timeline are all pinned down, so DeepSeek and Opus 5.5 can use it directly. {{ }} marks the parts for you to fill in.

You are a front-end motion engineer. Write **one complete index.html file**: only vanilla HTML + JavaScript + Canvas 2D, no external libraries, font files, or images. Make a "Particle Convergence" animation: thousands of tiny glowing particles gather into a shape, hold, scatter, then flow along an arc into the next shape and gather again, on a loop.

## Content

- The four shapes, in order: heart → house → person → a Chinese character ({{default: 家}}).
- Each time a shape comes to rest, a line of subtitles appears at the bottom of the frame. The four lines, in order: {{four lines, separated by |. Default: First, a heart | Then, a house | Someone moves into it | Together they make a home}}.

## Output requirements (follow exactly)

1. Output only one HTML code block, with no explanation. The code must be complete and runnable: no ellipses, no "same as above" or "omitted here".
2. The canvas is fixed at 1920×1080; use CSS to scale it proportionally and center it in the window, with black bars filling the extra space.
3. The picture is a pure function of time t (in seconds), `draw(t)`. Do not use `Math.random`; all randomness comes from seeded mulberry32(2026), generated once at startup. Do not accumulate state inside draw (no "leftovers from the previous frame"). That way the same t always draws exactly the same picture.
4. Loop by default (requestAnimationFrame, t = seconds played); space pauses/resumes; when the URL carries `?t=3.3`, show only the frame at 3.3 seconds (frozen).

## Constants

N = 5000 particles; each shape lasts one period PER = 4.8 seconds, 4 shapes total, a full loop of 19.2 seconds; shape scale SC = 1080 × 0.36; shape center at (960, 520).

## Shapes (coordinates inside the [-1,1] square, y pointing down)

```js
const heart  = (x,y)=>{ y=-y*1.15+.1; x*=1.15; return Math.pow(x*x+y*y-1,3)-x*x*y*y*y<=0; };
const house  = (x,y)=>(Math.abs(x)<=.6&&y>=-.1&&y<=.75&&!(Math.abs(x)<.14&&y>.38))||(y<-.1&&y>-.8&&Math.abs(x)<=.8*(y+.8)/.7);
const person = (x,y)=>(x*x+(y+.55)*(y+.55)<=.05)||(y>=-.28&&y<=.85&&Math.abs(x)<=.25+(y+.28)*.2);
```

- Heart, house, person: inside [-1,1]², use seeded random points for "rejection sampling"; keep the ones that land inside the shape until you have N of them.
- Chinese character: use a 400×400 offscreen canvas to draw the bold white character (`bold 340px "Noto Serif SC","Songti SC","SimSun",serif`, horizontally centered, `textBaseline='middle'`, y=210); after `getImageData`, take one point with alpha > 128 every 2 pixels and convert it into [-1,1]; shuffle with a seed and take N of them (if there are not enough, repeat and add ±0.004 of jitter).
- Shuffle each of the four target-point sets once. Particle i goes to its own i-th target point in each of the four shapes — so it looks like "the same batch of particles changing shape".

## Fixed parameters per particle (generated once at startup)

Angle `a` (0–2π), amplitude `m` (0–1), phase `ph` (0–2π), flicker frequency `f` (0.6–1.6), size `s` (0–1), and whether it has a halo `glow` (true for 20%).

## Position (the core — calculate it exactly like this)

Let k = floor(t / PER) % 4 (the current shape), n = (k+1) % 4 (the next shape), q = t % PER (time within the shape); A = the i-th target point of shape k, B = the i-th target point of shape n.

- Progress e = smoothstep(2.4, 4.2, q). While q is 0–2.4 seconds, e=0 (holding still); 2.4–4.2 seconds is the morph; 4.2–4.8 seconds, e=1 (settled).
- Control point C = (A+B)/2 + (cos a, sin a) × (0.35 + 0.9·m).
- Position P = (1−e)²·A + 2(1−e)e·C + e²·B (a quadratic Bézier, so particles travel along arcs — bursting outward first, then gathering).
- Micro-motion: add (cos(ph + 1.3t), sin(1.7·ph + 1.1t)) × 0.012 × (1 − sin(π·e)) to P.
- Screen coordinates = (960 + P.x × SC, 520 + P.y × SC); then scale the whole frame around the screen center (960, 540) by zoom = 1 + 0.015·sin(0.33t).

## How to draw it

1. **Background**: fill with #07080C; add a radial gradient at the center (radius 800) from `rgba(40,46,66,0.30)` to `rgba(7,8,12,0)`; then draw 220 dim stars at fixed positions (randomized once at startup, opacity 0.15–0.4, twinkling gently with t).
2. **Particles**: draw them additively with `globalCompositeOperation = 'lighter'` so they glow. Colors: heart #F08A8A, house #F1C070, person #A9C6FF, character #F6EBD0; while morphing, blend linearly between "the current shape's color" and "the next shape's color" according to e.
3. Each particle's brightness L = 0.75 + 0.25·sin(f·t + ph); radius r = 1.1 + 1.6·s (pixels); base opacity 0.55·L.
4. **Trails**: draw each particle 3 times, at times t, t−0.045, and t−0.09 (recompute with the same position function; do not store history); opacity ×1, ×0.5, ×0.25 in turn, radius ×1, ×0.8, ×0.6.
5. **Halo**: for particles with glow=true, draw one extra large circle with radius ×3 and opacity 0.05.
6. **Subtitles**: while each shape is at rest (fading in as q goes 0.3 → 1.0, fading out as q goes 2.1 → 2.5), show that shape's line centered at (960, 960), in a 46px serif face, color #EDE6D6, max opacity 0.85.

## Don't

Explosive flashes, lens flares, rainbow colors, a second background, randomness driven by a live timer, or saving the previous frame's state inside `draw`.

## Check your own work when done (don't output this)

- Refresh the same t twice: is the picture exactly the same?
- At t=1.8, do you see a heart made of particles? At t=3.3, is it bursting apart and flowing toward the house?
- One frame draws 5000×3 particles — does it lag? If it does, draw halos only for glow particles.
