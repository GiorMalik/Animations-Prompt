# Material & Licensing

This skill packages the "Code Animation — 341 Style Prompts — Free" material pack supplied with the project. The original author's notes, prompts, examples, and licenses stay in `../assets/library/`. XiaoyeCodes maintains this repository's skill packaging, search/install/render scripts, and showcase docs, and does not claim all works in the material pack as their own originals.

- [Original notes](../assets/library/about.md): free to use, free to share; do not package this content as a course, a paid skill, or other paid content to sell.
- [Original source notes](../assets/library/license-and-sources.md): the original curator's notes on the self-made/rewritten parts.
- [Lemo-Opuscar](../assets/library/third-party-licenses/Lemo-Opuscar_LICENSE.txt): MIT, Copyright (c) 2026 LemoLab.
- [mg-styles-15](../assets/library/third-party-licenses/mg-styles-15_LICENSE.txt): MIT, Copyright (c) 2026 Vincentwei1021.
- [code-video](../assets/library/third-party-licenses/code-video_LICENSE.txt): MIT, Copyright (c) 2026 Bae-ChangHyun.

Thanks to the original material curator — Bilibili [**俯仰观照**](https://space.bilibili.com/3690990015613855/?spm_id_from=333.788.upinfo.detail.click) — for sharing the resources.

## Community additions & the original baseline

- **Strange Leo (@strangeyu911-tech)**: contributed three 1920×1080 JPEG reference info cards — K1 Flat Vector, K2 Q-Style, K3 Kawaii — via [PR #1](https://github.com/XiaoyeCodes/code-animation-prompts/pull/1). These are community additions, not images that came with the original package.
- The author says the images were drawn as SVG and rendered, but the PR submitted only the JPEGs, without the SVG source files; this repository does not present the JPEGs as editable vector source.
- The original material contains 193 still frames; with the community additions, the current directory has 196. The 193 in the original package's `about.md` is kept as historical text; the current count follows `catalog.json` and the picker.
- This fork's `docs/source-manifest.json` keeps the hash baseline for the translated file set (558 files under `assets/library/`). [library-changes.json](library-changes.json) records the English translation of the pack from the Chinese upstream (XiaoyeCodes/code-animation-prompts) and ships with the installed skill. Validation checks the files against that translated baseline.

Content from different sources keeps its own license. The free-sharing terms do not rewrite the third-party MIT texts; the collection as a whole cannot simply be labeled all-MIT. Film and art styles and example names are reference descriptions, not official partnerships or endorsements.
