#!/usr/bin/env python3
"""Check HumVisual's package files without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WORD_BUDGET = 5500
PATTERN_HEADING = re.compile(r"(?m)^### ([0-9]+)\. (.+)$")
PATTERN_INDEX_ROW = re.compile(r"(?m)^\| ([0-9]+) \| ")
README_ROW = re.compile(r"(?m)^\| ([0-9]+) \| \*\*(.+?)\*\*")
SECTION_REFERENCE = re.compile(r"§([0-9]+)")


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"Cannot read {path.relative_to(ROOT)}: {error}")


def read_json(path: Path) -> dict:
    try:
        return json.loads(read(path))
    except json.JSONDecodeError as error:
        raise SystemExit(f"Fix the JSON in {path.relative_to(ROOT)}: {error}")


def require_match(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


def heading_block(text: str, version: str) -> str:
    """Return the CHANGELOG section for one version."""
    match = re.search(
        rf"(?m)^## {re.escape(version)}\n(.*?)(?=^## |\Z)", text, re.DOTALL
    )
    if match is None:
        raise SystemExit(f"CHANGELOG.md has no '## {version}' section")
    return match.group(1)


def main() -> None:
    skill_path = ROOT / "SKILL.md"
    skill = read(skill_path)
    readme = read(ROOT / "README.md")
    changelog = read(ROOT / "CHANGELOG.md")
    patterns = read(ROOT / "references" / "prose-patterns.md")
    license_text = read(ROOT / "LICENSE")

    plugin = read_json(ROOT / ".claude-plugin" / "plugin.json")
    marketplace = read_json(ROOT / ".claude-plugin" / "marketplace.json")
    cursor_plugin = read_json(ROOT / ".cursor-plugin" / "plugin.json")
    package = read_json(ROOT / "package.json")

    metadata = require_match(
        re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL),
        "SKILL.md must begin with YAML metadata",
    ).group(1)

    # One package version in every file that states one.
    skill_version = require_match(
        re.search(r'(?m)^\s+version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$', metadata),
        "Add metadata.version to SKILL.md as a three-part version",
    ).group(1)
    changelog_version = require_match(
        re.search(r"(?m)^## \[?([0-9]+\.[0-9]+\.[0-9]+)\]?", changelog),
        "Add a version heading to CHANGELOG.md",
    ).group(1)
    package_versions = {
        skill_version,
        changelog_version,
        str(plugin.get("version", "")),
        str(cursor_plugin.get("version", "")),
        str(package.get("version", "")),
        *(str(entry.get("version", "")) for entry in marketplace.get("plugins", [])),
    }
    if len(package_versions) != 1:
        raise SystemExit(f"Use one package version in all files: {sorted(package_versions)}")

    # One skill file, at the root, and both loaders point at it.
    skill_files = {path.relative_to(ROOT) for path in ROOT.rglob("SKILL.md")}
    if skill_path.is_symlink() or skill_files != {Path("SKILL.md")}:
        raise SystemExit("Keep one regular SKILL.md at the repo root")
    if plugin.get("skills") != ["./"]:
        raise SystemExit("Point the Claude plugin skill loader at the repo root")
    if cursor_plugin.get("name") != "humvisual":
        raise SystemExit("Set the Cursor plugin name to humvisual")
    if "skills" in cursor_plugin:
        raise SystemExit("Omit skills from the Cursor plugin so it loads the root SKILL.md")

    # Every manifest states the first sentence of the SKILL.md description.
    description = " ".join(
        require_match(
            re.search(r"(?m)^description: \|\n((?:  .*\n)+)", metadata + "\n"),
            "Write the SKILL.md description as an indented block",
        ).group(1).split()
    )
    manifest_descriptions = {
        str(plugin.get("description", "")),
        str(cursor_plugin.get("description", "")),
        str(package.get("description", "")),
        *(str(entry.get("description", "")) for entry in marketplace.get("plugins", [])),
    }
    if len(manifest_descriptions) != 1 or not description.startswith(
        next(iter(manifest_descriptions))
    ):
        raise SystemExit(
            "Use the first sentence of the SKILL.md description in every package manifest: "
            f"{sorted(manifest_descriptions)}"
        )

    # Patterns are numbered from 1 without gaps, and the reference is the only
    # place they are defined.
    defined = {
        int(number): name for number, name in PATTERN_HEADING.findall(patterns)
    }
    numbers = list(defined)
    pattern_count = len(numbers)
    if pattern_count == 0 or numbers != list(range(1, pattern_count + 1)):
        raise SystemExit(
            f"Number references/prose-patterns.md patterns from 1 upward without gaps: {numbers}"
        )

    indexed = {int(number) for number in PATTERN_INDEX_ROW.findall(skill)}
    if indexed != set(numbers):
        raise SystemExit(
            f"List each pattern once in the SKILL.md index table: "
            f"{sorted(set(numbers) - indexed)} missing, {sorted(indexed - set(numbers))} unknown"
        )
    readme_patterns = dict(
        (int(number), name) for number, name in README_ROW.findall(readme)
    )
    if sorted(readme_patterns) != sorted(numbers):
        raise SystemExit(
            f"List patterns 1 through {pattern_count} once each in the README table: "
            f"{sorted(readme_patterns)}"
        )
    renamed = [
        f"{number}: README says {readme_patterns[number]!r}, the reference says {name!r}"
        for number, name in defined.items()
        if readme_patterns.get(number) != name
    ]
    if renamed:
        raise SystemExit("Match the README pattern names to the reference: " + "; ".join(renamed))
    if f"## The {pattern_count} patterns" not in readme:
        raise SystemExit(f"Title the README pattern section 'The {pattern_count} patterns'")

    # Every section reference must point at a pattern that exists. CHANGELOG.md
    # keeps the numbers each upstream release used, so check the prompt files only.
    prompt_files = [skill_path, *(ROOT / "commands").glob("*.md")]
    for path in prompt_files:
        references = {int(number) for number in SECTION_REFERENCE.findall(read(path))}
        dangling = sorted(number for number in references if not 1 <= number <= pattern_count)
        if dangling:
            raise SystemExit(
                f"Point every section reference in {path.relative_to(ROOT)} at a pattern from 1 to "
                f"{pattern_count}: {dangling}"
            )

    # Every word of SKILL.md is read on each use, so the budget is in words.
    skill_words = len(skill.split())
    if skill_words > WORD_BUDGET:
        raise SystemExit(f"Keep SKILL.md at {WORD_BUDGET:,} words or fewer; it has {skill_words:,}")

    # The merged prompt follows its own dash rule, so it carries no em dash.
    for line_number, line in enumerate(skill.splitlines(), start=1):
        if "—" in line or "–" in line:
            raise SystemExit(
                f"SKILL.md line {line_number} uses a dash. Pattern 8 applies to this prompt too; "
                "use a period, comma, colon, or parentheses"
            )

    # The folder the prompt routes to has to exist.
    for pattern in sorted(set(re.findall(r"`\./([^`]+)`", skill))):
        if pattern.endswith((".md", ".html", ".mjs", ".json")) and not (ROOT / pattern).exists():
            raise SystemExit(f"SKILL.md points at a missing file: ./{pattern}")

    for command in sorted((ROOT / "commands").glob("*.md")):
        front = re.match(r"\A---\n(.*?)\n---\n", read(command), re.DOTALL)
        if front is None or not re.search(r"(?m)^name: ", front.group(1)):
            raise SystemExit(f"Give {command.relative_to(ROOT)} YAML metadata with a name")

    for name, target in package.get("bin", {}).items():
        if not (ROOT / target.lstrip("./")).exists():
            raise SystemExit(f"package.json bin {name} points at a missing file: {target}")

    for holder in ("Siqi Chen", "Nico Bailon"):
        if holder not in license_text:
            raise SystemExit(f"LICENSE must keep the upstream copyright: {holder}")

    print(
        f"HumVisual package v{skill_version} is valid: {pattern_count} prose patterns, "
        f"{skill_words:,} words in SKILL.md, {len(list((ROOT / 'commands').glob('*.md')))} commands"
    )


if __name__ == "__main__":
    sys.exit(main())
