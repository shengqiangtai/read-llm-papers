#!/usr/bin/env python3
"""Validate the public Read LLM Papers plugin without third-party packages."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "read-llm-papers"
SKILL = PLUGIN / "skills" / "read-llm-papers"

REQUIRED = [
    ROOT / ".agents" / "plugins" / "marketplace.json",
    PLUGIN / ".codex-plugin" / "plugin.json",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    SKILL / "references" / "report-contract.md",
    SKILL / "references" / "evidence-rules.md",
    SKILL / "references" / "llm-paper-checklist.md",
]


def fail(message: str) -> None:
    raise SystemExit(f"Validation failed: {message}")


for path in REQUIRED:
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")

plugin = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text())
marketplace = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text())

if plugin.get("name") != "read-llm-papers":
    fail("plugin name must be read-llm-papers")
if plugin.get("skills") != "./skills/":
    fail("plugin skills path must be ./skills/")

entries = marketplace.get("plugins", [])
if len(entries) != 1 or entries[0].get("name") != "read-llm-papers":
    fail("marketplace must contain exactly one read-llm-papers entry")
if entries[0].get("source", {}).get("path") != "./plugins/read-llm-papers":
    fail("marketplace source path is incorrect")

skill_text = (SKILL / "SKILL.md").read_text()
frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill_text, flags=re.DOTALL)
if not frontmatter:
    fail("SKILL.md frontmatter is missing")
if not re.search(r"^name:\s*read-llm-papers\s*$", frontmatter.group(1), re.MULTILINE):
    fail("SKILL.md name is incorrect")
if not re.search(r"^description:\s*\S", frontmatter.group(1), re.MULTILINE):
    fail("SKILL.md description is missing")
if len(skill_text.splitlines()) > 500:
    fail("SKILL.md exceeds 500 lines")

placeholder = "[" + "TODO:"
for path in ROOT.rglob("*"):
    if path.is_file() and ".git" not in path.parts:
        text = path.read_text(errors="ignore")
        if placeholder in text:
            fail(f"unresolved TODO in {path.relative_to(ROOT)}")

print("Read LLM Papers plugin is valid.")
