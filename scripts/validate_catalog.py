#!/usr/bin/env python3
"""Deterministic checks for the public skills catalogue draft.

Validates:
  - manifest counts against JSON catalogue lengths / uniqueness
  - Vercel overlapping skill names
  - recommendations.json counts and brief file paths
  - relative Markdown links that target paths inside this repository

Exit code 0 on success, 1 on failure.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOGS = ROOT / "catalogs"

MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def load_json(name: str):
    path = CATALOGS / name
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def fail(messages: list[str]) -> None:
    for msg in messages:
        print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def check_counts(manifest: dict, managed: list, plugins: list, installed: list, unregistered: list) -> list[str]:
    errors: list[str] = []
    counts = manifest["counts"]

    expected = {
        "custom_skills": 0,
        "managed_platform_skills": len(managed),
        "plugin_skill_entries": len(plugins),
        "plugin_skill_unique_names": len({p["name"] for p in plugins}),
        "installed_plugins": len(installed),
        "unregistered_skill_md_inside_plugin_installs": len(unregistered),
        "custom_skill_files_shipped": 0,
    }

    for key, value in expected.items():
        if counts.get(key) != value:
            errors.append(f"counts.{key}: manifest={counts.get(key)!r} computed={value!r}")

    plugin_names = [p["name"] for p in plugins]
    name_counts = Counter(plugin_names)
    overlapping = sorted(name for name, n in name_counts.items() if n > 1)
    overlap_extra = sum(n - 1 for n in name_counts.values() if n > 1)

    if counts.get("vercel_overlapping_skill_names") != overlap_extra:
        errors.append(
            "counts.vercel_overlapping_skill_names: "
            f"manifest={counts.get('vercel_overlapping_skill_names')!r} computed_extra_entries={overlap_extra!r}"
        )

    manifest_overlap = sorted(manifest.get("vercel_overlapping_names", []))
    if manifest_overlap != overlapping:
        errors.append(
            "vercel_overlapping_names mismatch: "
            f"manifest={manifest_overlap!r} computed={overlapping!r}"
        )

    with_skills = sum(1 for p in installed if p.get("registered_skill_count", 0) > 0)
    without_skills = sum(1 for p in installed if p.get("registered_skill_count", 0) == 0)
    if counts.get("installed_plugins_with_skills") != with_skills:
        errors.append(
            "counts.installed_plugins_with_skills: "
            f"manifest={counts.get('installed_plugins_with_skills')!r} computed={with_skills!r}"
        )
    if counts.get("installed_plugins_without_skills") != without_skills:
        errors.append(
            "counts.installed_plugins_without_skills: "
            f"manifest={counts.get('installed_plugins_without_skills')!r} computed={without_skills!r}"
        )

    managed_names = [m["name"] for m in managed]
    if len(managed_names) != len(set(managed_names)):
        errors.append("managed-skills.json contains duplicate names")

    skill_sum = sum(int(p.get("registered_skill_count", 0)) for p in installed)
    if skill_sum != len(plugins):
        errors.append(
            f"sum of installed plugin registered_skill_count ({skill_sum}) "
            f"!= plugin-skills.json length ({len(plugins)})"
        )

    return errors


def check_markdown_tables() -> list[str]:
    """Ensure human-readable catalogues list the same number of skill rows as JSON."""
    errors: list[str] = []

    managed_md = (CATALOGS / "managed-skills.md").read_text(encoding="utf-8")
    managed_rows = len(re.findall(r"^\| `[a-z0-9][^`]*` \|", managed_md, flags=re.MULTILINE))
    managed_json = load_json("managed-skills.json")
    if managed_rows != len(managed_json):
        errors.append(
            f"managed-skills.md table rows ({managed_rows}) != managed-skills.json ({len(managed_json)})"
        )

    plugin_md = (CATALOGS / "plugin-skills.md").read_text(encoding="utf-8")
    plugin_rows = len(re.findall(r"^\| `[a-z0-9][^`]*` \|", plugin_md, flags=re.MULTILINE))
    plugin_json = load_json("plugin-skills.json")
    if plugin_rows != len(plugin_json):
        errors.append(
            f"plugin-skills.md table rows ({plugin_rows}) != plugin-skills.json ({len(plugin_json)})"
        )

    installed_md = (CATALOGS / "installed-plugins.md").read_text(encoding="utf-8")
    installed_rows = len(re.findall(r"^\| [^|]+ \| [^|]+ \| \d+ \|", installed_md, flags=re.MULTILINE))
    installed_json = load_json("installed-plugins.json")
    if installed_rows != len(installed_json):
        errors.append(
            f"installed-plugins.md table rows ({installed_rows}) != installed-plugins.json ({len(installed_json)})"
        )

    return errors


def iter_repo_markdown() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        paths.append(path)
    return sorted(paths)


def check_recommendations() -> list[str]:
    errors: list[str] = []
    path = CATALOGS / "recommendations.json"
    if not path.exists():
        return errors

    data = load_json("recommendations.json")
    recs = data.get("recommendations", [])
    counts = data.get("counts", {})

    if counts.get("shortlisted") != len(recs):
        errors.append(
            f"recommendations counts.shortlisted ({counts.get('shortlisted')!r}) "
            f"!= recommendations length ({len(recs)})"
        )

    original = sum(1 for r in recs if r.get("kind") == "original-to-author")
    if counts.get("original_to_author") != original:
        errors.append(
            f"recommendations counts.original_to_author ({counts.get('original_to_author')!r}) "
            f"!= computed ({original})"
        )

    install_reuse = sum(1 for r in recs if r.get("kind") == "install-or-reuse")
    if counts.get("install_or_reuse_external_skill") != install_reuse:
        errors.append(
            "recommendations counts.install_or_reuse_external_skill: "
            f"manifest={counts.get('install_or_reuse_external_skill')!r} computed={install_reuse!r}"
        )

    for rec in recs:
        status = rec.get("status")
        install_state = rec.get("install_state")
        if status != "PROPOSED":
            errors.append(f"recommendation {rec.get('id')!r}: status must be PROPOSED, got {status!r}")
        if install_state != "NOT_INSTALLED":
            errors.append(
                f"recommendation {rec.get('id')!r}: install_state must be NOT_INSTALLED, "
                f"got {install_state!r}"
            )
        rel = rec.get("file")
        if not rel:
            errors.append(f"recommendation {rec.get('id')!r}: missing file")
            continue
        brief = ROOT / rel
        if not brief.is_file():
            errors.append(f"recommendation {rec.get('id')!r}: missing brief {rel}")

    return errors


def check_relative_links() -> list[str]:
    errors: list[str] = []
    for md_path in iter_repo_markdown():
        text = CODE_FENCE_RE.sub("", md_path.read_text(encoding="utf-8"))
        for match in MD_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith("#"):
                continue
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                # http(s), mailto, etc.
                continue
            if target.startswith("//"):
                continue
            path_part = target.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            resolved = (md_path.parent / path_part).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{md_path.relative_to(ROOT)}: link escapes repo: {target}")
                continue
            if not resolved.exists():
                errors.append(f"{md_path.relative_to(ROOT)}: broken relative link: {target}")
    return errors


def main() -> None:
    manifest = load_json("manifest.json")
    managed = load_json("managed-skills.json")
    plugins = load_json("plugin-skills.json")
    installed = load_json("installed-plugins.json")
    unregistered = load_json("unregistered-plugin-skill-files.json")

    errors: list[str] = []
    errors.extend(check_counts(manifest, managed, plugins, installed, unregistered))
    errors.extend(check_markdown_tables())
    errors.extend(check_recommendations())
    errors.extend(check_relative_links())

    if errors:
        fail(errors)

    recommendations = load_json("recommendations.json") if (CATALOGS / "recommendations.json").exists() else {}
    print("OK: catalogue counts, recommendations, duplicates/overlaps, and relative links validated")
    print(
        "counts:",
        json.dumps(
            {
                "managed": len(managed),
                "plugin_entries": len(plugins),
                "plugin_unique_names": len({p["name"] for p in plugins}),
                "vercel_overlap_extra": sum(
                    n - 1 for n in Counter(p["name"] for p in plugins).values() if n > 1
                ),
                "installed_plugins": len(installed),
                "unregistered_skill_md": len(unregistered),
                "recommendations_shortlisted": len(recommendations.get("recommendations", [])),
            },
            sort_keys=True,
        ),
    )


if __name__ == "__main__":
    main()
