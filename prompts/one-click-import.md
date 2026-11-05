# One-Click Import Prompt

Copy the whole block below into Claude Code or Codex with local file and terminal access.

```text
Please install https://github.com/GiorMalik/Animations-Prompt as a skill for my current coding assistant.

1. Download the repository to a suitable local directory; if a directory with the same name already exists, check its contents first and do not overwrite existing changes.
2. Read README.md, docs/INSTALL.md, and skills/code-animation-prompts/SKILL.md.
3. Choose the install target for the current assistant: Codex uses ~/.agents/skills/code-animation-prompts,
   Claude Code uses ~/.claude/skills/code-animation-prompts.
   From the repository root, run python scripts/install_skill.py --target codex or --target claude.
   If the current assistant cannot be determined, ask me to confirm the target; do not install to both locations on your own.
4. Keep the complete skill folder when installing, including all prompts, still frames, HTML,
   example videos, and license files in assets/library. If the target already exists, keep the existing directory and report it; do not delete or overwrite it automatically.
5. Run scripts/styles.py search ink in the installed directory to confirm styles can be found;
   then run scripts/styles.py show B3 to confirm the full prompt can be read.
6. Tell me the actual install path, how to invoke it, and whether I need a new session.
   Finally, give me one ready-to-use example request: a "12-second particle-gathering animation".

This installs only the style skill — it does not install video-rendering dependencies or change other assistant settings.
```

[Back to README](../README.md)
