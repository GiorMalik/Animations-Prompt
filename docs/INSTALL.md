# Installing in Claude Code / Codex

This repository targets Claude Code and Codex, which have local file and terminal access. Download the full repository first (the original videos are about 75 MiB, plus README images); what gets installed is the entire `skills/code-animation-prompts/` directory.

## One line to hand your assistant

[Copy the one-click import prompt](../prompts/one-click-import.md). Your assistant will download the repository, read the instructions, pick the install location for your current tool, and verify style lookup.

## Python install script

Requires Python 3.10+, no third-party packages. Run from the repository root:

```bash
python scripts/install_skill.py --target codex
python scripts/install_skill.py --target claude
```

Pick one of the two. `--target both` installs to both locations. `--dry-run` only shows the paths without writing files.

| Tool | User-level directory | Project-level directory |
|---|---|---|
| Codex | `~/.agents/skills/code-animation-prompts/` | `<project>/.agents/skills/code-animation-prompts/` |
| Claude Code | `~/.claude/skills/code-animation-prompts/` | `<project>/.claude/skills/code-animation-prompts/` |

`~` means your home directory; on Windows it is usually `C:\Users\<username>`. Paths follow the [OpenAI official skills docs](https://learn.chatgpt.com/docs/build-skills) and [Claude Code official skills docs](https://code.claude.com/docs/en/skills).

To install into a specific project:

```bash
python scripts/install_skill.py --target codex --scope project --project-dir "your project path"
python scripts/install_skill.py --target claude --scope project --project-dir "your project path"
```

Do not install the same-named skill at both the user level and the project level in the same assistant — that creates duplicate entries.

## Without Python

Manually copy the repository's entire `skills/code-animation-prompts/` directory to one of the locations in the table. You should end up with:

```text
<install location>/code-animation-prompts/SKILL.md
<install location>/code-animation-prompts/assets/library/style-picker.html
<install location>/code-animation-prompts/references/catalog.json
```

Copying only `SKILL.md` loses the style library. Do not change the relative positions of files inside `assets/library/`.

## Verify the installation

Replace `<skill directory>` with the real install path:

```bash
python "<skill directory>/scripts/styles.py" search ink
python "<skill directory>/scripts/styles.py" show B3
```

After starting a new session, Codex users can type `$code-animation-prompts`; Claude Code users can type `/code-animation-prompts`. You can also just say "Use code-animation-prompts to make an animation". If the new skill does not show up in the current session, restart the session; account or admin settings can affect skill discovery.

## Updating

The install script does not overwrite an existing directory. Before updating, save your own changes and back up the old skill directory outside the skill scan directories; then pull the repository and re-run the install command. Do not leave a backup containing `SKILL.md` under `.agents/skills/` or `.claude/skills/`, or it may still be scanned.

Update the repository's material index and check integrity:

```bash
python scripts/build_catalog.py
python scripts/validate_repo.py
```

## Optional: video export

Installing the skill does not automatically install a browser or FFmpeg. When you actually need to export video, set up the dependencies as described in the [rendering notes](../skills/code-animation-prompts/references/rendering.md).

[Back to README](../README.md)
