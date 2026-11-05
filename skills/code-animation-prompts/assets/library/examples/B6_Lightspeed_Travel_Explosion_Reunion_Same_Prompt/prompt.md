# B6 Lightspeed Travel · Explosion · Reunion

> The same prompt, given to Opus 5.5 (High) and DeepSeek-V4.1-Flash (1017, High) — the results are in this folder. Fill in the {{ }} parts yourself.

You are a front-end motion engineer. Write **one complete index.html file**: only native HTML + JavaScript + Canvas 2D, no external libraries, font files or images. Make a 12-second, **single continuous shot** animation: lightspeed travel → bursting through 5 light rings → braking, particles sucked toward the centre → explosion → fragments spinning back together into the title. The whole thing is one camera flying forward through 3D space, **never cutting once**; the same 4000 particles start as streaks of starlight, then become the explosion's fragments, and finally assemble into the title.

## Content

- Title: {{default: "Looking Up and Down"}}
- Subtitle: {{default: "In the river's flow, see the moment; in the trees, see eternity"}}

## Output requirements (must follow)

1. Output only one HTML code block, no explanation. The code must be complete and runnable: no ellipses, never write "same as above" or "omitted here".
2. Canvas fixed at 1920×1080; use CSS to scale it proportionally and centre it in the window, with black bars in the extra space.
3. The picture is a pure function of time t (seconds), `draw(t)`. Do not use `Math.random`; all randomness uses seeded mulberry32(7), generated only once at startup. Do not keep the previous frame's state inside draw. The same t must always draw exactly the same thing.
4. Loops by default (requestAnimationFrame, t = seconds played, modulo 12); space pauses/resumes; a URL with `?t=5.7` shows only the frame at second 5.7 (still).

## Constants

W=1920, H=1080, screen centre (960,540); N=4000 particles; total length 12 seconds; tunnel length L=6000; base focal length F0=900.

## Camera (the camera travels along the z axis. Get these functions right first)

```js
const V0 = 80, V1 = 2600;
const z1 = t => V0*t + (V1-V0)*(3/3.2)*Math.pow(Math.min(t,3)/3, 3.2) + V1*Math.max(0, t-3);
const Z5 = z1(5.0), zB = Z5 + 780, ZC = zB + 900, Z3 = z1(3), ZT = zB - 700;
function camZ(t) {
  if (t <= 5.0) return z1(t);                                              // accelerate to lightspeed
  if (t <= 5.6) { const u = (t-5.0)/0.6; return Z5 + 2600*0.6*(u - u*u/2); } // hard brake
  if (t <= 8.0) { const v = (t-5.6)/2.4; return zB - 2200*(1-(1-v)*(1-v)); } // pull back hard after the explosion
  return zB - 2200 - 120*(t-8.0);                                          // then pull back slowly
}
```

- **5 rings**: the k-th ring (k=0..4) sits at world z = Z3 + 2600·(0.3 + 0.42k), and the camera passes through it at time tk = 3.3 + 0.42k; when k is even its colour is (125,249,255), when odd (255,213,154); radius R=260.
- **Focal length** f(t) = 900 + for each tk≤t, add 260·exp(−9(t−tk)) + (when t≥5.6, add 520·exp(−6(t−5.6))) — every time the camera passes a ring, and at the instant of the explosion, the picture "punches" in.
- **Roll** roll(t) = 0.02·sin(1.7t) + (when t≥5.6, add 0.12·sin(2π·0.9·(t−5.6))·exp(−2.2(t−5.6))).
- **Shake**: amp = (t≥5.6 ? 22·exp(−3.2(t−5.6)) : 0), offset = (sin(53t)·amp, cos(47t)·amp).
- Before drawing particles, rings, core and shockwave: `ctx.translate(960+shakeX, 540+shakeY); ctx.rotate(roll); ctx.translate(-960, -540)`; after drawing them, `restore`, so the white flash, titles and so on are unaffected by roll and shake.

## Projection

A point at camera-space coordinates (X, Y, d) (d is its distance from the camera) is drawn on screen at: `sx = 960 + f·X/d`, `sy = 540 + f·Y/d`.

## Each particle's fixed parameters (generated once at startup)

- `a` (0–2π); `rho` = 220 + 1280·rand^0.8; `zw` = rand·L (world depth inside the tunnel); `s` (0–1); `cls` (15% are 1, the rest 0); `ph` (0–2π); `fq` (0.6–1.6);
- Explosion direction `dir`: zz = −0.55 + 1.55·rand, φ = rand·2π, rxy = √(1−zz²), dir = (rxy·cosφ, rxy·sinφ, zz);
- Explosion strength `mag` = 300 + 2600·rand^1.6;
- Spin `sw` = (1.2 + 2·rand)·(random sign);
- Title target point `(tx, ty)`: see below.

## The title's target points

On a 1200×400 offscreen canvas, write the title in white bold type (`bold 280px "Noto Serif SC","Songti SC","SimSun",serif`, horizontally centred, `textBaseline='middle'`, at (600, 205)); sample a point every 3 pixels where alpha>128, convert its coordinates to ((x−600)·2.093, (y−200)·2.093); shuffle with a seed and take N of them (if there aren't enough, repeat, adding ±3 jitter). Particle i uses point i.

## Each particle's camera-space position at time t (write it as a function `place(p, t)` returning X, Y, d)

- **t < 5.6 (tunnel)**: k = 1 − 0.92·smoothstep(5.0, 5.6, t) (from 5.0–5.6 s the particles converge toward the centre of the frame); X = rho·cos(a)·k, Y = rho·sin(a)·k; d = ((zw − camZ(t)) mod L + L) mod L + 60.
- **5.6 ≤ t ≤ 8 (explosion)**: τ = min(1, (t−5.6)/2.4), g = 1 − (1−τ)³; world coordinates X = dir.x·mag·g, Y = dir.y·mag·g, Z = ZC + dir.z·mag·g; d = Z − camZ(t).
- **t > 8 (reunion)**: e = smoothstep(8, 10, t); start E = (dir.x·mag, dir.y·mag, ZC + dir.z·mag), end Tg = (tx, ty, ZT); Q = E + (Tg − E)·e; then rotate (Q.x, Q.y) around the origin by θ = sin(π·e)·sw; X, Y = the rotated result, Z = Q.z; d = Z − camZ(t).

## How to draw each frame

1. **Background** #05060A; then a radial gradient centred on (960,540), radius 700: from `rgba(30,60,90, 0.28·sf·(t<5.6 ? 1 : 0.4))` to `rgba(5,6,10,0)`. sf = 0.45 + 0.55·clamp(speed/2600, 0, 1), where speed is the camera's current speed: t<3 → 80+2520·(t/3)^2.2; 3–5 s → 2600; 5–5.6 s → 2600·(1−(t−5)/0.6); otherwise 0.
2. Everything below uses `globalCompositeOperation='lighter'`, `lineCap='round'`.
3. **Particles**: draw each one as a line segment from "the screen position at time tp" to "the screen position at time t". tp = max(t − DT, t≥5.6 ? 5.6 : 0), DT = (t<5.6 ? 0.03 : 0.06 − 0.03·smoothstep(8, 9, t)); use tp's focal length for the tp end. If either end has d<30, or the two ends' d differ by more than 500 (just wrapped back to the start of the tunnel), don't draw this line.
   - **Colour**: t<5.0: cls=1 → (255,213,154), otherwise (191,232,255); 5.0–5.6: blend toward white by smoothstep(5.0, 5.6, t); 5.6–8: while τ<0.4 blend from white to orange (255,176,74), then from orange to magenta (255,61,110); 8–10: blend from magenta to warm white (246,235,208) (by smoothstep(8,10,t)); t≥10: warm white.
   - **Opacity**: t<5.6: (1 − d/L)^1.4·(0.25 + 0.55·s)·sf·1.6, clamped to 0–1; t≥5.6: 0.9·(0.7 + 0.3·sin(fq·t + ph))·(t<8 ? 1−0.4τ : 0.9).
   - **Line width**: t<5.6: (0.9 + 1.8·s)·clamp(√(900/d), 0.5, 2.2); t≥5.6: (2 + 3·s)·clamp(√(900/d), 0.6, 2.2).
4. **Rings (only draw while t<5.6!)**: for each ring, d = the ring's z − camZ(t); don't draw if d<40 or d>5200; otherwise draw a 96-segment circle of radius R=260: point = (960 + f·R·cosθ/d, 540 + f·R·sinθ/d); line width clamp(6·900/d, 1.5, 16), opacity 0.6·clamp(1 − d/5200, 0, 1); after drawing it once, draw it again with 3× the line width and 1/4 opacity as a glow.
5. **The core's light**: when t≥4.4 and dc = ZC − camZ(t) > 40, draw a white radial-gradient circle (centre (960,540), from `rgba(255,255,255,0.9)` to transparent), radius = 140000/dc·(0.4 + 0.6·smoothstep(4.4, 5.6, t))·(f/900), multiplied by exp(−3(t−5.6)) when t≥5.6.
6. **Shockwave**: when t≥5.6, ts = clamp((t−5.6)/1.2, 0, 1), world radius Rw = 3600·(1 − (1−ts)³); if ts<1 and dd = ZC − camZ(t) > 40: draw a white stroked circle, centre (960,540), radius f·Rw/dd, opacity 0.8·(1−ts), line width 1 + 8·(1−ts).
7. Undo the translation/rotation (`restore`), then draw in order:
   - **White flash**: a full-screen white rectangle (lighter), opacity = (t≥5.6 ? 0.95·exp(−9(t−5.6)) : 0.7·smoothstep(5.4, 5.6, t)) + 0.3·exp(−14(t−tk)) for each tk≤t + (t≥10 ? 0.35·exp(−8(t−10)) : 0), total clamped to 1;
   - **Title solidifying** (source-over): opacity 0.9·smoothstep(9.7, 10.3, t)·(1 − smoothstep(11.4, 12, t)), draw the title centred at (960, 545), `bold 300px` in the same fonts, colour #F6EBD0;
   - **Subtitle**: opacity 0.85·smoothstep(9.6, 10.4, t)·(1 − smoothstep(11.4, 12, t)), centred at (960, 790), serif 40px, colour #EDE6D6;
   - **Vignette**: a radial gradient, radius 400→1150, from `rgba(0,0,0,0)` to `rgba(0,0,0,0.55)`;
   - **Fade in/out at the ends**: a full-screen black rectangle, opacity (1 − smoothstep(0, 0.35, t)) + smoothstep(11.4, 12, t).

smoothstep(a, b, x): t = clamp((x−a)/(b−a), 0, 1), returns t·t·(3 − 2t).

## Don't

`Math.random`; keeping the previous frame's state inside `draw`; animating with DOM elements; extra colours; drawing the rings after the explosion (they would "come at" the camera as it pulls back — they must not be drawn).

## Check it yourself when done (don't output this)

- Does refreshing at the same t twice draw exactly the same picture?
- At t=2.8, do you see starlight streaks stretched outward, with a few cyan/amber rings in the middle?
- At t=5.3, are the particles being sucked toward the centre with a ball of white light there? At t=5.7, is it a white radial explosion?
- At t=9.5, are the particles spiralling back together? At t=10.8, is the title clearly readable?
- Will one frame with 4000 lines plus 5 rings lag?
