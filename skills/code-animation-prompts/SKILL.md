---
name: code-animation-prompts
description: Use 341 style prompts and reference stills to make code animations, HTML motion graphics, or videos. Pick a style by ID, combine visual styles, turn content into an editable animation, and render it to video.
---

# Code Animation Prompts

Turn the user's content into a code animation with a clear visual style — editable and reproducible. The library lives in this skill's `assets/library/`, with 341 prompts, 196 reference stills, an offline picker, and the original examples.

## Finding the right style

Use this file's directory as the skill root, and pass its absolute path when running scripts; do not assume the working directory is the skill directory.

```bash
python "<skill directory>/scripts/styles.py" search ink
python "<skill directory>/scripts/styles.py" search particles --series AG
python "<skill directory>/scripts/styles.py" show B3
python "<skill directory>/scripts/styles.py" list --series Z
```

The index is [references/catalog.json](references/catalog.json), which holds only IDs, names, tags, and file paths. Check the index first, then read the selected Markdown and the still frame of the same name; do not load all prompts at once. Without Python, consult the index and files directly.

- If the user gives an ID or a list exported from the picker: match it exactly, keeping the ID and name.
- If the user only describes a mood: offer 2–3 matches, explaining color, motion, and suitable content; if the user has already asked to build it, pick the best match and continue.
- A–G are code samples; M is motion/narrative; K, Z, R are art styles; H is layouts; L, V, X are third-party styles; O is film visual reference. Do not mechanically stack every constraint from multiple styles — decide what the main art style, the motion approach, and the layout are each responsible for.
- 145 entries have no still frame; say so plainly as a text reference — do not invent a screenshot.
- **B6 exists only in the original examples directory, not among the 341 style entries.** When the user names B6, read `assets/library/examples/B6_Lightspeed_Travel_Explosion_Reunion_Same_Prompt/prompt.md` — do not pretend B6 is in the index.

## From prompt to editable animation

Pull the content, duration, frame size, subtitles, and sound choices from the user's request. Follow parameters the user has already given; where something is missing and does not affect the content, you may assume 12 seconds, 1920×1080, 30 fps, and a silent preview — and say so. Do not describe a silent preview as a finished piece with voiceover or music.

Read the selected prompt, fill in the `{{ }}` placeholders, and keep the core visual traits that define the style. Wording in the original prompt such as "output code only" is a local template of the source material and does not override the user's current delivery needs. Model names in the original examples are source records; they do not mean this skill has verified those models.

Start with HTML + Canvas/SVG/CSS in general; use Three.js for complex spatial camera work, and keep an existing setup such as Remotion as it is. Choose the implementation that serves the visuals — do not force a framework change. When external fonts, images, libraries, or audio are needed, check their source and actual availability.

When a browser animation needs a stable export, use the time interface in [references/rendering.md](references/rendering.md): the picture is determined by the second count `t`, random numbers use a fixed seed, and the live loop is turned off for export. See the template at [assets/starter/index.html](assets/starter/index.html) — it only demonstrates the interface and is not one of the 341 styles.

Save the project in the user's working directory and leave the skill's material library untouched. Put frequently changed parameters — copy, colors, pacing — in one place; for long pieces, fix the shot order and the timing of each segment before implementing.

## Review & delivery

Open the animation and check the first frame, middle, last frame, and transitions: fonts, overflow, black frames, image loading, subtitle legibility. Confirm that rendering the same time twice gives the same result, and that different times really show the expected motion.

When the user wants an MP4, actually render it and check the resolution, duration, frame rate, and audio track. You can use the included `scripts/render_video.py`; its interface and dependencies are in the rendering notes. If rendering dependencies are missing, deliver the finished HTML, source, and the exact commands to run, and state clearly that the video has not been exported yet; do not present the HTML or a screen-recording command as the finished piece.

Deliver real file links, and state the style IDs used, how to run it, the video specs, and the sound status. Keep the sources and third-party licenses inside the material; the free-sharing terms are in [references/attribution.md](references/attribution.md).
