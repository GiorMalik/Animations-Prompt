"""Validate the translated library baseline, documented library changes, counts and local links."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/code-animation-prompts"
LIBRARY = SKILL / "assets/library"


def validate_library(library, manifest, changes):
    original = manifest["files"]
    modified, added = changes["modified"], changes["added"]
    assert manifest["file_count"] == len(original), "Original manifest count differs"
    assert set(modified) <= set(original), "Modified file is not in the original baseline"
    assert not set(added) & set(original), "Added file overlaps the original baseline"
    files = {p.relative_to(library).as_posix(): p for p in library.rglob("*") if p.is_file()}
    assert set(files) == set(original) | set(added), "Library file set differs from baseline plus additions"
    for name, record in {**modified, **added}.items():
        assert record["contribution"] in changes["contributions"], f"Missing contribution source: {name}"
        assert record["reason"].strip(), f"Missing change reason: {name}"
    for name, digest in original.items():
        if name in modified:
            record = modified[name]
            assert record["original_sha256"] == digest, f"Original hash mismatch: {name}"
            digest = record["sha256"]
        assert hashlib.sha256(files[name].read_bytes()).hexdigest() == digest, f"Unexpected library change: {name}"
    for name, record in added.items():
        assert hashlib.sha256(files[name].read_bytes()).hexdigest() == record["sha256"], f"Added asset changed: {name}"
    return len(original) - len(modified), len(modified), len(added)


def main():
    manifest = json.loads((ROOT / "docs/source-manifest.json").read_text(encoding="utf-8"))
    changes = json.loads((SKILL / "references/library-changes.json").read_text(encoding="utf-8"))
    unchanged, modified, added = validate_library(LIBRARY, manifest, changes)
    data = json.loads((SKILL / "references/catalog.json").read_text(encoding="utf-8"))
    assert data["total"] == len(data["entries"]) == 341
    assert len({e["id"] for e in data["entries"]}) == 341
    stills = sum(bool(e["image"]) for e in data["entries"])
    assert stills == data["with_still"]
    stats = json.loads((LIBRARY / "_stats.json").read_text(encoding="utf-8"))
    assert (stats["total"], stats["withStill"]) == (data["total"], stills)
    picker = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>',
                                 (LIBRARY / "style-picker.html").read_text(encoding="utf-8"), re.S).group(1))
    picker_entries = {e["id"]: e for e in picker["entries"]}
    assert len(picker_entries) == len(picker["entries"]) == data["total"]
    for entry in data["entries"]:
        source = picker_entries[entry["id"]]
        assert entry["file"] == "assets/library/" + source["file"]
        assert entry["image"] == ("assets/library/" + source["img"] if source.get("img") else "")
        for key in ["file", "image"]:
            if entry[key]:
                assert (SKILL / entry[key]).is_file(), entry[key]
    checked = 0
    for doc in ROOT.rglob("*.md"):
        if any(part in {".git", ".build", ".agents", ".claude"} for part in doc.relative_to(ROOT).parts):
            continue
        if LIBRARY in doc.parents:
            continue  # Original documents are retained verbatim.
        for target in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "mailto:", "#")):
                continue
            path = unquote(target.split("#")[0])
            assert (doc.parent / path).exists(), f"Broken link: {doc.relative_to(ROOT)} -> {target}"
            checked += 1
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    text_only = data["total"] - stills
    assert f'{data["total"]} style prompts · {stills} reference stills' in readme, "README headline counts are stale"
    assert f'reference_stills-{stills}-' in readme, "README badge count is stale"
    assert f'**{stills} styles have stills, {text_only} are text references**' in readme, "README summary counts are stale"
    assert f'**{stills} still frames + {text_only} text references**' in readme, "README table counts are stale"
    skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert f'{stills} reference stills' in skill and f'{text_only} entries have no still frame' in skill, "Skill counts are stale"
    assert f'{stills} entries include a still frame' in (ROOT / "docs/STYLES.md").read_text(encoding="utf-8"), "Style index count is stale"
    prompt = re.search(r'```text\n(Please install https://github.com/GiorMalik/Animations-Prompt.*?)(?:\n```)', readme, re.S).group(1)
    assert prompt in (ROOT / "prompts/one-click-import.md").read_text(encoding="utf-8")
    print(f"PASS: {unchanged} original files unchanged; {modified} documented modifications; "
          f"{added} contributed assets; {data['total']} styles; {stills} stills; "
          f"{checked} local links; counts and import prompt consistent.")


if __name__ == "__main__":
    main()
