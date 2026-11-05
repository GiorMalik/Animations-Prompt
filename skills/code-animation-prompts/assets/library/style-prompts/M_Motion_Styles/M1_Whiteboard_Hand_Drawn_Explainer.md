# M1 Whiteboard Hand-Drawn Explainer

- Category: M Motion Styles · Explainer
- What it looks like: A white background, a hand (or a pen) drawing as it talks, lines drawn first, then colored in.
- Good for: Passages that explain a concept or a principle. For example: "A large language model is the brain, Harness is the hands and feet."

## Style Prompt

> This prompt is a rewritten, detailed version: the visual rules, colors, and timeline are all pinned down, so DeepSeek and Opus 5.5 can use it directly. {{ }} marks the parts for you to fill in.

You are a front-end motion engineer. Write **one complete index.html file**: only vanilla HTML + JavaScript + Canvas, no external libraries, font files, or images. Make a whiteboard hand-drawn explainer animation.

## What it explains

- Topic: {{topic, e.g. A large language model is the brain, Harness is the hands and feet}}
- Total length: {{seconds, default 20}}
- Words on screen: {{3–6 short words. E.g. title "How AI does its work"; left "Large language model", sub-label "It thinks, it speaks"; right "Harness", sub-label "Hands and feet: it actually does things"; on the arrow, "Instruction"}}

## Output requirements (follow exactly)

1. Output only one HTML code block, with no explanation. The code must be complete and runnable: no ellipses, no "same as above" or "omitted here".
2. The canvas is fixed at 1920×1080; use CSS to scale it proportionally and center it in the window, with black bars filling the extra space.
3. Every frame is decided by the function `draw(t)`, where `t` is seconds. Do not use `Math.random`; when you need randomness, use seeded mulberry32(seed), so the same `t` always draws exactly the same picture.
4. Loop by default; space pauses/resumes; when the URL carries `?t=8.5`, show only the frame at 8.5 seconds (frozen), for easy screenshots.

## How to draw the picture

- Base color #FBFAF7; layer a few very faint gray eraser smudges on top (40–90px wide, opacity 0.03–0.06).
- Lines are a black marker #1B1B1B, 10px wide, with `lineCap` and `lineJoin` both round. Draw every stroke twice: first pass at opacity 0.93; second pass 5.5px wide, opacity 0.55, offset by ±1.5px.
- Only black and **one** accent color #E5432B (used for the title underline, the arrow, sub-labels, and the pen cap). No third color.
- Type: `font-family: KaiTi, STKaiti, "Kaiti SC", "Microsoft YaHei", sans-serif`, bold; title 110px, labels 90px, sub-labels 56px. Draw words with `strokeText` plus `fillText`, with a stroke about 3.5% of the font size.
- Hand-drawn feel: add ±2.5px of jitter to each point, taking the jitter from seeded randomness keyed to "the point's index" — never re-randomize per frame.
- What to draw:
  - A cloud-shaped "brain": polar coordinates r = R·(1 + 0.11·|sin(3.5θ)|), with a few wavy lines inside;
  - A stick figure: round head, a single-line body, two arms (a circle at the end of each for a hand), two legs;
  - A curved accent-color arrow, its head following the direction of the line's tail;
  - A marker pen: black barrel, red cap, about 330px long, tilted 55°, its tip always resting at the end of "the stroke currently being drawn"; once everything is drawn, it slides out of frame.

## How it moves

- Each stroke is a list of points. Use progress (0→1) to decide how many points are drawn, eased in-out; one stroke takes 0.4–1.2 seconds.
- Order: title → title underline (red) → the brain on the left → the little figure on the right → the red arrow → the word "Instruction" → the two label texts. Only one stroke is drawn at a time.
- Once everything is drawn, hold still for 1.5 seconds, then loop.

## Don't

Gradients, shadows, glow, 3D, particles, complicated color schemes, screens full of text, camera shake.

## Check your own work when done (don't output this)

- At `t=0`, is the whiteboard almost blank?
- At `t=total length−0.1`, are all the elements there?
- Is any text covered by a line or the pen?
- Refresh the same `t` twice: is the picture exactly the same?
