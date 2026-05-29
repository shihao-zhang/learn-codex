#!/usr/bin/env python3
"""Check documentation and teaching mock contracts for learn-codex."""

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
PLACEHOLDER_PHRASES = [
    "Step 1 placeholder",
    "Step 2 补充",
    "当前是占位图",
    "placeholder",
]
PINNED_LINK_RE = re.compile(
    r"https://github\.com/openai/codex/(?:blob|tree)/"
    + re.escape(SOURCE_COMMIT)
    + r"/[^\s)]+"
)
SNAPSHOT_ROW_RE = re.compile(
    r"\|\s*(?P<chapter>s\d{2}_[^|]+?)\s*\|\s*\[[^\]]+\]\((?P<link>https://github\.com/openai/codex/(?:blob|tree)/"
    + re.escape(SOURCE_COMMIT)
    + r"/[^\s)]+)\)\s*\|"
)
STATUS_ROW_RE = re.compile(
    r"\|\s*[^|]+\s*\|\s*\[(?P<chapter>s\d{2}_[^\]]+)\]\([^)]+\)\s*"
    r"\|\s*[^|]+\s*\|\s*(?P<status>[^|]+?)\s*\|"
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


def pinned_links(text: str) -> set[str]:
    return set(PINNED_LINK_RE.findall(text))


def chapter_status(text: str, readme: Path) -> str:
    status_line = next(
        (line for line in text.splitlines() if line.startswith("状态：")),
        None,
    )
    if status_line is None:
        fail(f"{readme.relative_to(ROOT)} missing status line")

    status = status_line.replace("状态：", "", 1).strip()
    if status not in VALID_STATUSES:
        fail(f"{readme.relative_to(ROOT)} has invalid status {status!r}")
    return status


def root_statuses() -> dict[str, str]:
    readme = read(ROOT / "README.md")
    statuses: dict[str, str] = {}
    for match in STATUS_ROW_RE.finditer(readme):
        statuses[match.group("chapter")] = match.group("status").strip()
    return statuses


def snapshot_links_by_chapter() -> dict[str, set[str]]:
    snapshot = read(ROOT / "docs/fact-snapshot.md")
    links: dict[str, set[str]] = {}
    for match in SNAPSHOT_ROW_RE.finditer(snapshot):
        chapter = match.group("chapter").strip()
        links.setdefault(chapter, set()).add(match.group("link"))
    return links


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
    for phrase in PLACEHOLDER_PHRASES:
        if phrase in text:
            fail(f"{readme.relative_to(ROOT)} still contains placeholder phrase {phrase!r}")

    diagram_text = read(diagram)
    for phrase in PLACEHOLDER_PHRASES:
        if phrase in diagram_text:
            fail(f"{diagram.relative_to(ROOT)} still contains placeholder phrase {phrase!r}")

    status = chapter_status(text, readme)

    links = pinned_links(text)
    if not links:
        fail(f"{readme.relative_to(ROOT)} has no pinned openai/codex permalink")

    snapshot_by_chapter = snapshot_links_by_chapter()
    all_snapshot_links = set().union(*snapshot_by_chapter.values())
    missing_from_snapshot = sorted(links - all_snapshot_links)
    if missing_from_snapshot:
        missing_list = "\n".join(f"  - {link}" for link in missing_from_snapshot)
        fail(
            f"{readme.relative_to(ROOT)} has links missing from "
            f"docs/fact-snapshot.md:\n{missing_list}"
        )

    if status == "已核实官方事实":
        chapter_snapshot_links = snapshot_by_chapter.get(chapter, set())
        missing_for_chapter = sorted(links - chapter_snapshot_links)
        if missing_for_chapter:
            missing_list = "\n".join(f"  - {link}" for link in missing_for_chapter)
            fail(
                f"{readme.relative_to(ROOT)} has verified-status links not "
                f"registered under {chapter} in docs/fact-snapshot.md:\n{missing_list}"
            )

    mock_text = read(mock)
    for phrase in PLACEHOLDER_PHRASES:
        if phrase in mock_text:
            fail(f"{mock.relative_to(ROOT)} still contains placeholder phrase {phrase!r}")
    for token in ["TeachingScenario", "happy_path", "failure_path", "run_cli"]:
        if token not in mock_text:
            fail(f"{mock.relative_to(ROOT)} missing teaching mock token {token}")


def check_status_map() -> None:
    statuses = root_statuses()
    for chapter in CHAPTERS:
        if chapter not in statuses:
            fail(f"README.md learning map missing {chapter}")
        readme = ROOT / "chapters" / chapter / "README.md"
        status = chapter_status(read(readme), readme)
        if statuses[chapter] != status:
            fail(
                f"README.md status for {chapter} is {statuses[chapter]!r}, "
                f"but chapter README says {status!r}"
            )


def main() -> int:
    check_root_docs()
    for chapter in CHAPTERS:
        check_chapter(chapter)
    check_status_map()
    print("OK: documentation and teaching mock contracts are complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
