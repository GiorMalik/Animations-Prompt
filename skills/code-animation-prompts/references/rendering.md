# Exporting Browser Animation

## Time interface

The bundled renderer serves HTML that provides this interface (it does not render arbitrary web pages):

```js
window.renderAt = async function (t) {
  // t is in seconds; position all animation, particles, camera, and subtitles at this moment.
  draw(t);
};
```

Once the page receives `?export=1`, it does not start a requestAnimationFrame/timer loop and stops CSS self-playing animations; `renderAt(t)` alone advances the picture. Random particles are generated at startup with a fixed seed, or computed directly from index and time. Async resources should be ready before `renderAt` returns. The Canvas pixel size, CSS viewport, and output size match, with no player controls included.

`../assets/starter/index.html` is a minimal example you can copy. HTML in the original material is not guaranteed to provide this interface; when adapting it, save a copy and do not modify the original library. Existing projects such as Remotion use their own export tools.

## Dependencies

Search and install need only the Python 3.10+ standard library. Only browser rendering needs extra installs:

```bash
python -m pip install playwright
python -m playwright install chromium
ffmpeg -version
```

FFmpeg must be installed and on PATH; see the [official FFmpeg downloads](https://ffmpeg.org/download.html) for how to install it.

## Export

```bash
python "<skill directory>/scripts/render_video.py" ./index.html \
  --output ./output/video.mp4 --duration 12 --fps 30 --width 1920 --height 1080
```

With prepared music/narration, add `--audio ./narration.wav`. The script does not generate sound and does not automatically loop short audio; it pads silence or trims to the video length. Silent by default. If the output file already exists, the script stops — pick another filename.

The script loads the HTML through a local HTTP server bound to a random port on `127.0.0.1`; dependency assets should sit in the HTML's directory or its subdirectories. It captures frames one by one at `t = frame / fps` and encodes them with FFmpeg as H.264 / yuv420p. Dimensions must be positive even numbers; the frame count is `ceil(duration × fps)`, so the actual duration may round up to one frame. By default it captures the whole output viewport.

Long or high-resolution pieces render slowly frame by frame. Export a short segment first to check the visuals and dependencies, then render the full piece. If output fails, report the specific missing item or interface error — do not claim it finished.
