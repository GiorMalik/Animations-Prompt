# B1 Flowing Threads

- Category: A–G Code Samples · B Particles
- What it looks like: Countless fine threads drift on an invisible wind.
- Good for: Thoughts, feelings in flow, calming down
- Keywords: flowing, threads, wind

## Style Prompt

Use code (Canvas 2D) to draw a "Flowing Threads" animation: Countless fine threads drift on an invisible wind.
Good for: Thoughts, feelings in flow, calming down
Keywords: flowing, threads, wind

Below is our own reference implementation: a draw function S.B1(c, w, h, t, s), where c is the canvas 2D context, w/h are the width and height, t is seconds, and s is an empty object for this function to keep its state in. The shared helper functions live in _shared_functions.js in the same folder.

```js
S.B1 = (c, w, h, t, s, dpr) => {
  if (!s.init) { s.init = 1; [s.bc, s.bx] = offscreen(w, h, dpr); s.bx.fillStyle = '#05080d'; s.bx.fillRect(0, 0, w, h); const r = rng(5); s.r = r; s.p = []; for (let i = 0; i < 800; i++) s.p.push([r() * w, r() * h, r() * 200, r()]); }
  const b = s.bx, sc = 3.2 / Math.min(w, h); b.fillStyle = 'rgba(5,8,13,.07)'; b.fillRect(0, 0, w, h); b.lineWidth = .8;
  for (const p of s.p) {
    const a = nz(p[0] * sc, p[1] * sc, t * .12) * Math.PI, sp = Math.min(w, h) / 260;
    const nx = p[0] + Math.cos(a) * sp, ny = p[1] + Math.sin(a) * sp;
    b.strokeStyle = `hsla(${195 + p[3] * 40},60%,${62 + p[3] * 25}%,.4)`; b.beginPath(); b.moveTo(p[0], p[1]); b.lineTo(nx, ny); b.stroke();
    p[0] = nx; p[1] = ny; p[2]--;
    if (p[2] < 0 || nx < 0 || nx > w || ny < 0 || ny > h) { p[0] = s.r() * w; p[1] = s.r() * h; p[2] = 80 + s.r() * 200; }
  }
  c.drawImage(s.bc, 0, 0, w, h);
};
```
