# Code Animation Style Prompts

A total of **341** styles, one prompt each — usable with Opus 5.5 and with DeepSeek. 193 of them include a still frame.

Some were collected from the web; most I organized, made, and summarized myself.

## What's inside

| Folder / file | What it is |
|---|---|
| `style-picker.html` | The picker web page. Open it directly in Chrome or Edge by double-clicking; no internet needed. Filter by category, search, zoom into stills, read prompts, tick selections, and export a list. Keep it next to the `style-prompts` folder — don't separate them. |
| `style-prompts/` | 341 styles, one `.md` prompt each; styles with a still have a same-named `.jpg` next to them |
| `examples/` | Two real-world tests: the same detailed prompt given to Opus 5.5 and DeepSeek, compared; and a single sentence given to DeepSeek |
| `license-and-sources.md`, `third-party-licenses/` | Where each style group came from, and under what license |

### How the 341 break down

| Category | Count | What it is |
|---|---|---|
| A–G Code Samples | 26 | Words, particles, lines and ink, light and weather, shapes and paper, explainers, texture; each with reference implementation code |
| M Motion Styles | 40 | How a whole video moves, cuts, and tells its story |
| K Cartoon Styles | 38 | What the characters and the picture look like |
| Z Chinese Style | 15 | Ink wash, fine-line painting, paper cutting, shadow puppetry, Dunhuang… |
| H Ready Layouts | 12 | Complete color-plus-type pairings |
| L Lemo-Opuscar | 59 | Styles from the open-source Lemo-Opuscar project, each with a full how-to |
| V mg-styles-15 | 15 | Motion styles from the open-source mg-styles-15 project |
| X code-video | 31 | Styles from the open-source code-video project |
| R Learned from References | 7 | Cyberpunk drawn in code by studying references |
| O 98 Oscar Best Pictures | 98 | One visual style per Oscar Best Picture winner, 98 films |

## How to use

**With DeepSeek Harness (or Claude Code):**

1. Put this folder somewhere it can read, and tell it: "Read this folder — I want to use these styles to make code animations."
2. Pick your styles on the picker page, click "My Picks", copy it, and send it to the model.
3. Explain clearly what you want to express: what it's about, how long, landscape or vertical, how the camera moves, how the styles connect.
4. **Remember to say whether you want music and sound effects.** If you don't, it will most likely come back silent.
5. Have it output an HTML file you can open in a browser, then have it rendered into a video.

**Using a single style directly:** Open that style's `.md`, copy the "Style Prompt" section to the model, and add your content. Some prompts contain `{{ }}` — those are placeholders for you to fill in.

**A tip:** The more specific the prompt (colors, timing, camera moves all pinned down), the closer different models' results will be. A single sentence works too, but the result varies every time and takes longer. The examples folder shows both.

## Ground rules

- All free — no DMs, no paid courses.
- Free to use and free to pass on; when you share, please share for free too.
- **Do not repackage any of this as a course, a paid skill, or anything else you sell.**
- The parts from open-source projects keep their original licenses and attribution — see `license-and-sources.md`.

If you found this useful, a like, a coin, and a favorite would mean a lot. Thanks, everyone — I'll keep sharing more practical open-source work.
