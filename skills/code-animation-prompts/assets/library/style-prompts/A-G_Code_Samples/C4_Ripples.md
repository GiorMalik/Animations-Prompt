# C4 Ripples

- Category: A–G Code Samples · C Lines & Ink
- What it looks like: A drop falls, and ripples spread outward ring by ring.
- Good for: The impact of a single sentence, its aftershocks
- Keywords: ripples, water drops, spreading

## Style Prompt

Use code (Canvas 2D) to draw a "Ripples" animation: A drop falls, and ripples spread outward ring by ring.
Good for: The impact of a single sentence, its aftershocks
Keywords: ripples, water drops, spreading

Below is our own reference implementation: a draw function S.C4(c, w, h, t, s), where c is the canvas 2D context, w/h are the width and height, t is seconds, and s is an empty object for this function to keep its state in. The shared helper functions live in _shared_functions.js in the same folder.

```js
S.C4 = (c, w, h, t, s) => {
  c.fillStyle = vgrad(c, h, '#082027', '#020708'); c.fillRect(0, 0, w, h);
  const r = rng(29), per = 1.15, k = Math.floor(t / per), m = Math.min(w, h); c.lineWidth = 1;
  for (let i = k - 4; i <= k; i++) {
    if (i < 0) continue; const rr = rng(i * 7 + 1), x = (.12 + rr() * .76) * w, y = (.25 + rr() * .6) * h, age = t - i * per;
    for (let j = 0; j < 4; j++) { const a = age - j * .2; if (a <= 0) continue; const R = a * m * .17, al = Math.max(0, 1 - age / 4.4) * (1 - j * .2) * .75; c.strokeStyle = `rgba(170,225,230,${al})`; c.beginPath(); c.ellipse(x, y, R, R * .42, 0, 0, TAU); c.stroke(); }
    if (age < .25) glowDot(c, x, y, 10, '#cdf3f5', (1 - age / .25) * .8);
  }
};
```
