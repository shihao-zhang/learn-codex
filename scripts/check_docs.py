#!/usr/bin/env python3
"""Check documentation and teaching mock contracts for learn-codex."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
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
VERIFIED_EVIDENCE_LEVELS = {"mechanism-verified", "behavior-verified"}
PENDING_EVIDENCE_LEVELS = {"pending"}
TEACHING_EVIDENCE_LEVELS = {"teaching-abstract"}
VALID_EVIDENCE_LEVELS = (
    {"path-exists"}
    | VERIFIED_EVIDENCE_LEVELS
    | PENDING_EVIDENCE_LEVELS
    | TEACHING_EVIDENCE_LEVELS
)
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
OPENAI_CODE_LINK_RE = re.compile(
    r"https://github\.com/openai/codex/(?:blob|tree)/"
    r"(?P<ref>[^/\s)]+)/[^\s)]+"
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
CHAPTER_NAME_RE = re.compile(r"^s\d{2}_[a-z0-9_]+$")


@dataclass(frozen=True)
class EvidenceRow:
    chapter: str
    mechanism: str
    level: str
    source: str
    verified_scope: str
    open_questions: str
    links: frozenset[str]


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
        "docs/source-evidence.md",
        "docs/glossary.md",
    ]:
        if not (ROOT / rel).exists():
            fail(f"missing {rel}")

    snapshot = read(ROOT / "docs/fact-snapshot.md")
    if SOURCE_COMMIT not in snapshot:
        fail("docs/fact-snapshot.md does not contain SOURCE_COMMIT")

    sourcing = read(ROOT / "docs/sourcing.md")
    for phrase in ["三选一规则", "固定 commit SHA", "教学抽象", "证据索引"]:
        if phrase not in sourcing:
            fail(f"docs/sourcing.md missing phrase: {phrase}")
    check_openai_code_link_shas()
    check_source_evidence()


def check_openai_code_link_shas() -> None:
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix not in {".md", ".mmd", ".py"}:
            continue
        text = read(path)
        for ref, link in unfixed_openai_code_links(text):
            fail(
                f"{path.relative_to(ROOT)} has openai/codex link with "
                f"unexpected ref {ref}: {link}"
            )


def unfixed_openai_code_links(text: str) -> list[tuple[str, str]]:
    return [
        (match.group("ref"), match.group(0))
        for match in OPENAI_CODE_LINK_RE.finditer(text)
        if match.group("ref") != SOURCE_COMMIT
    ]


def pinned_links(text: str) -> set[str]:
    return set(PINNED_LINK_RE.findall(text))


def parse_evidence_rows(text: str) -> list[EvidenceRow]:
    rows: list[EvidenceRow] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) != 6:
            continue
        chapter, mechanism, level, source, verified_scope, open_questions = cells
        if chapter == "章节" or set(chapter) <= {"-", " "}:
            continue
        if not CHAPTER_NAME_RE.fullmatch(chapter):
            continue
        rows.append(
            EvidenceRow(
                chapter=chapter,
                mechanism=mechanism,
                level=level,
                source=source,
                verified_scope=verified_scope,
                open_questions=open_questions,
                links=frozenset(PINNED_LINK_RE.findall(line)),
            )
        )
    return rows


def evidence_rows_by_chapter() -> dict[str, list[EvidenceRow]]:
    evidence = read(ROOT / "docs/source-evidence.md")
    rows = parse_evidence_rows(evidence)
    if not rows:
        fail("docs/source-evidence.md has no evidence rows")

    by_chapter: dict[str, list[EvidenceRow]] = {}
    for row in rows:
        if row.chapter not in CHAPTERS:
            fail(f"docs/source-evidence.md has unknown chapter {row.chapter}")
        if row.level not in VALID_EVIDENCE_LEVELS:
            fail(
                "docs/source-evidence.md has invalid evidence level "
                f"{row.level!r} for {row.chapter}"
            )
        if row.level != "teaching-abstract" and not row.links:
            fail(
                "docs/source-evidence.md evidence row lacks fixed SHA source "
                f"for {row.chapter}: {row.mechanism}"
            )
        by_chapter.setdefault(row.chapter, []).append(row)
    return by_chapter


def check_source_evidence() -> None:
    evidence = read(ROOT / "docs/source-evidence.md")
    for phrase in ["Evidence Levels", "mechanism-verified", "behavior-verified", "pending"]:
        if phrase not in evidence:
            fail(f"docs/source-evidence.md missing phrase: {phrase}")

    rows_by_chapter = evidence_rows_by_chapter()
    statuses = root_statuses()
    for error in evidence_status_errors(rows_by_chapter, statuses):
        fail(error)


def evidence_status_errors(
    rows_by_chapter: dict[str, list[EvidenceRow]],
    statuses: dict[str, str],
    chapters: list[str] | None = None,
) -> list[str]:
    errors: list[str] = []
    for chapter in chapters or CHAPTERS:
        rows = rows_by_chapter.get(chapter, [])
        if not rows:
            errors.append(f"docs/source-evidence.md missing evidence for {chapter}")
            continue
        status = statuses.get(chapter)
        if status == "已核实官方事实" and not any(
            row.level in VERIFIED_EVIDENCE_LEVELS for row in rows
        ):
            errors.append(
                f"{chapter} is verified but has no mechanism/behavior evidence "
                "in docs/source-evidence.md"
            )
        if status == "待核实" and not any(row.level in PENDING_EVIDENCE_LEVELS for row in rows):
            errors.append(
                f"{chapter} is pending but has no pending evidence row "
                "in docs/source-evidence.md"
            )
        if status == "教学抽象" and not any(
            row.level in TEACHING_EVIDENCE_LEVELS for row in rows
        ):
            errors.append(
                f"{chapter} is teaching abstraction but has no teaching-abstract "
                "evidence row in docs/source-evidence.md"
            )
    return errors


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


def chapter_link_errors(
    chapter: str,
    status: str,
    links: set[str],
    snapshot_by_chapter: dict[str, set[str]],
    rows_by_chapter: dict[str, list[EvidenceRow]],
    readme_rel: str,
) -> list[str]:
    errors: list[str] = []
    all_snapshot_links = (
        set().union(*snapshot_by_chapter.values()) if snapshot_by_chapter else set()
    )
    missing_from_snapshot = sorted(links - all_snapshot_links)
    if missing_from_snapshot:
        missing_list = "\n".join(f"  - {link}" for link in missing_from_snapshot)
        errors.append(
            f"{readme_rel} has links missing from docs/fact-snapshot.md:\n{missing_list}"
        )

    if status == "已核实官方事实":
        chapter_snapshot_links = snapshot_by_chapter.get(chapter, set())
        chapter_evidence_links = set().union(
            *(row.links for row in rows_by_chapter.get(chapter, []))
        )
        registered_links = chapter_snapshot_links | chapter_evidence_links
        missing_for_chapter = sorted(links - registered_links)
        if missing_for_chapter:
            missing_list = "\n".join(f"  - {link}" for link in missing_for_chapter)
            errors.append(
                f"{readme_rel} has verified-status links not registered under "
                f"{chapter} in docs/fact-snapshot.md or docs/source-evidence.md:\n"
                f"{missing_list}"
            )
    return errors


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
    if status == "待核实" and not any(
        marker in diagram_text for marker in ["待核实", "to be verified", "pending"]
    ):
        fail(f"{diagram.relative_to(ROOT)} for pending chapter must mark pending semantics")
    if status == "教学抽象" and not any(
        marker in diagram_text for marker in ["教学抽象", "Teaching abstraction", "not official"]
    ):
        fail(f"{diagram.relative_to(ROOT)} for teaching abstraction must say it is not official")

    links = pinned_links(text)
    if not links:
        fail(f"{readme.relative_to(ROOT)} has no pinned openai/codex permalink")

    snapshot_by_chapter = snapshot_links_by_chapter()
    rows_by_chapter = evidence_rows_by_chapter()
    for error in chapter_link_errors(
        chapter,
        status,
        links,
        snapshot_by_chapter,
        rows_by_chapter,
        str(readme.relative_to(ROOT)),
    ):
        fail(error)

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
