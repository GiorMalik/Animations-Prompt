# G2 Signal Glitch

- Category: A–G Code Samples · G Texture
- What it looks like: The picture slips out of alignment, colors split apart, then a sudden flash.
- Good for: Breaking down, chaos, being cut off mid-sentence
- Keywords: glitch, misalignment, interference

## Style Prompt

Use code (Canvas 2D) to draw a "Signal Glitch" animation: The picture slips out of alignment, colors split apart, then a sudden flash.
Good for: Breaking down, chaos, being cut off mid-sentence
Keywords: glitch, misalignment, interference

Below is our own reference implementation: a draw function S.G2(c, w, h, t, s), where c is the canvas 2D context, w/h are the width and height, t is seconds, and s is an empty object for this function to keep its state in. The shared helper functions live in _shared_functions.js in the same folder.

```js
S.G2 = (c, w, h, t, s) => {
  const tm = t % 5, burst = (tm > 1.2 && tm < 1.7) || (tm > 3.1 && tm < 3.3) || (tm > 3.6 && tm < 4.2), m = Math.min(w, h), fs = Math.min(w / 4.6, h / 3.2);
  c.fillStyle = '#060607'; c.fillRect(0, 0, w, h); const dx = burst ? 4 + Math.random() * 10 : 1.2;
  c.font = `900 ${fs}px ${SANS}`; c.textAlign = 'center'; c.textBaseline = 'middle'; c.globalCompositeOperation = 'lighter';
  c.fillStyle = '#ff2b2b'; c.fillText('I\'m fine.', w / 2 - dx, h / 2); c.fillStyle = '#00e1ff'; c.fillText('I\'m fine.', w / 2 + dx, h / 2);
  c.globalCompositeOperation = 'source-over';
  if (burst) { for (let k = 0; k < 7; k++) { const y = Math.random() * h, sh = 4 + Math.random() * h * .08, off = (Math.random() - .5) * w * .12; c.drawImage(c.canvas, 0, y * (c.canvas.height / h), c.canvas.width, sh * (c.canvas.height / h), off, y, w, sh); } c.fillStyle = 'rgba(230,230,235,.8)'; c.font = `400 ${fs * .22}px ${SANS}`; c.fillText('(Not really)', w / 2 + (Math.random() - .5) * 8, h / 2 + fs * .78); }
  c.fillStyle = 'rgba(0,0,0,.22)'; for (let y = 0; y < h; y += 3) c.fillRect(0, y, w, 1);
};
```
