# A3 Big Words Hit Hard

- Category: A–G Code Samples · A Words
- What it looks like: Words slam into the frame one by one, on the beat.
- Good for: Emotional outbursts, pull-quotes, an MV chorus
- Keywords: big words, slamming down, on the beat

## Style Prompt

Use code (Canvas 2D) to draw a "Big Words Hit Hard" animation: Words slam into the frame one by one, on the beat.
Good for: Emotional outbursts, pull-quotes, an MV chorus
Keywords: big words, slamming down, on the beat

Below is our own reference implementation: a draw function S.A3(c, w, h, t, s), where c is the canvas 2D context, w/h are the width and height, t is seconds, and s is an empty object for this function to keep its state in. The shared helper functions live in _shared_functions.js in the same folder.

```js
S.A3 = (c, w, h, t, s) => {
  const L = [["You", .17, .33, .30, 0], ["Know", .40, .30, .22, 0], ["What", .70, .33, .17, 0], ["I", .19, .64, .20, 0], ["It's all", .43, .62, .14, 0], ["For your own good", .63, .84, .16, 1], ["Obey", .80, .60, .13, 0], ["!", .90, .84, .22, 1]];
  const beat = .4, len = L.length * beat + 1.4, tm = t % len, k = Math.floor(tm / beat), age = tm - k * beat;
  const m = Math.min(w, h), hit = k < L.length ? Math.exp(-age * 9) : 0;
  c.fillStyle = mixHex('#08080a', '#2a2a2e', hit * .5); c.fillRect(0, 0, w, h);
  const sx = (Math.sin(t * 91) * 6) * hit, sy = (Math.cos(t * 77) * 6) * hit;
  c.save(); c.translate(sx, sy); c.textAlign = 'center'; c.textBaseline = 'middle';
  for (let i = 0; i <= Math.min(k, L.length - 1); i++) {
    const [txt, fx0, fy, fz, red] = L[i], newest = i === k, port = h > w, fx = port ? .5 + (fx0 - .5) * .85 : fx0;
    const sc = newest ? 1 + .9 * Math.exp(-age * 16) : 1;
    c.font = `900 ${fz * m * (port ? .95 : 1.45) * sc}px ${SANS}`;
    c.fillStyle = red ? (newest ? '#ff4a32' : '#a3392a') : (newest ? '#ffffff' : '#55565c');
    c.fillText(txt, fx * w, fy * h);
  }
  c.restore();
};
```
