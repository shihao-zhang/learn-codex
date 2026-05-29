#!/usr/bin/env python3
"""Check Step 1 documentation contracts for learn-codex."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_COMMIT = "740d942f901a5a63421298c74dafbeb4255e946d"

CHAPTERS = [
    "s01_agent_loop",
    "s02_protocol_events",
    "s03_tool_registry_dispatch",
    "s04_shell_sandbox_permissions",
    "s05_context_window_compaction",
    "s06_prompts_instructions",
    "s07_config_auth_models",
    "s08_sessions_threads_rollout",
    "s09_app_server_transport",
    "s10_extensions_mcp_skills",
    "s11_subagents_parallel_jobs",
    "s12_comprehensive_architecture",
]

REQUIRED_HEADINGS = [
    "## 状态标签",
    "## 本章回答什么",
    "## 对产品与平台设计的意义",
    "## 机制图",
    "## 运行 mock",
    "## 核心机制",
    "## 真实 Codex 映射",
    "## 教学简化与生产差异",
    "## 练习",
    "## 事实核验清单",
]

VALID_STATUSES = {"已核实官方事实", "待核实", "教学抽象"}
PINNED_LINK_RE = re.compile(
    r"https://github\.com/openai/codex/(?:blob|tree)/"
    + re.escape(SOURCE_COMMIT)
    + r"/[^\s)]+"
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        fail(f"missing {path.relative_to(ROOT)}")


def check_root_docs() -> None:
    for rel in [
        "README.md",
        "docs/sourcing.md",
        "docs/fact-snapshot.md",
        "docs/glossary.md",
    ]:
        if not (ROOT / rel).exists():
            fail(f"missing {rel}")

    snapshot = read(ROOT / "docs/fact-snapshot.md")
    if SOURCE_COMMIT not in snapshot:
        fail("docs/fact-snapshot.md does not contain SOURCE_COMMIT")

    sourcing = read(ROOT / "docs/sourcing.md")
    for phrase in ["三选一规则", "固定 commit SHA", "教学抽象"]:
        if phrase not in sourcing:
            fail(f"docs/sourcing.md missing phrase: {phrase}")


def check_chapter(chapter: str) -> None:
    chapter_dir = ROOT / "chapters" / chapter
    if not chapter_dir.is_dir():
        fail(f"missing chapter directory chapters/{chapter}")

    readme = chapter_dir / "README.md"
    diagram = chapter_dir / "diagram.mmd"
    mock = chapter_dir / "mock.py"

    for path in [readme, diagram, mock]:
        if not path.exists():
            fail(f"missing {path.relative_to(ROOT)}")

    text = read(readme)
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            fail(f"{readme.relative_to(ROOT)} missing heading {heading}")

    status_line = next(
        (line for line in text.splitlines() if line.startswith("状态：")),
        None,
    )
    if status_line is None:
        fail(f"{readme.relative_to(ROOT)} missing status line")

    status = status_line.replace("状态：", "", 1).strip()
    if status not in VALID_STATUSES:
        fail(f"{readme.relative_to(ROOT)} has invalid status {status!r}")

    if not PINNED_LINK_RE.search(text):
        fail(f"{readme.relative_to(ROOT)} has no pinned openai/codex permalink")

    mock_text = read(mock)
    if "Step 1 placeholder" not in mock_text:
        fail(f"{mock.relative_to(ROOT)} is not marked as Step 1 placeholder")


def main() -> int:
    check_root_docs()
    for chapter in CHAPTERS:
        check_chapter(chapter)
    print("OK: Step 1 documentation skeleton is complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

