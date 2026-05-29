from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECK_DOCS = ROOT / "scripts" / "check_docs.py"


def load_check_docs_module():
    spec = importlib.util.spec_from_file_location("check_docs", CHECK_DOCS)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class SourceEvidenceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.check_docs = load_check_docs_module()

    def test_parse_evidence_rows_extracts_level_and_links(self) -> None:
        text = """
| 章节 | 机制点 | 证据级别 | 源码证据 | 已核实范围 | 未解决问题 |
| --- | --- | --- | --- | --- | --- |
| s01_agent_loop | loop | mechanism-verified | [source](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/session/mod.rs#L638-L644) | scope | none |
"""
        rows = self.check_docs.parse_evidence_rows(text)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0].chapter, "s01_agent_loop")
        self.assertEqual(rows[0].level, "mechanism-verified")
        self.assertEqual(len(rows[0].links), 1)

    def test_verified_chapters_have_non_path_evidence(self) -> None:
        rows_by_chapter = self.check_docs.evidence_rows_by_chapter()
        root_statuses = self.check_docs.root_statuses()
        for chapter, status in root_statuses.items():
            if status == "已核实官方事实":
                self.assertTrue(
                    any(
                        row.level in self.check_docs.VERIFIED_EVIDENCE_LEVELS
                        for row in rows_by_chapter[chapter]
                    ),
                    chapter,
                )

    def test_pending_chapters_have_pending_semantics(self) -> None:
        rows_by_chapter = self.check_docs.evidence_rows_by_chapter()
        root_statuses = self.check_docs.root_statuses()
        for chapter, status in root_statuses.items():
            if status == "待核实":
                self.assertTrue(
                    any(
                        row.level in self.check_docs.PENDING_EVIDENCE_LEVELS
                        for row in rows_by_chapter[chapter]
                    ),
                    chapter,
                )

    def test_wrong_sha_or_moving_ref_is_rejected(self) -> None:
        base = "https://github.com/" + "openai/codex/blob/"
        moving_ref = (
            f"{base}main/"
            "codex-rs/core/src/session/mod.rs"
        )
        short_sha = (
            f"{base}740d942/"
            "codex-rs/core/src/session/mod.rs"
        )
        pinned = (
            f"{base}{self.check_docs.SOURCE_COMMIT}/"
            "codex-rs/core/src/session/mod.rs"
        )

        errors = self.check_docs.unfixed_openai_code_links(
            f"{moving_ref}\n{short_sha}\n{pinned}"
        )

        self.assertEqual([ref for ref, _ in errors], ["main", "740d942"])

    def test_unregistered_source_link_is_rejected(self) -> None:
        base = "https://github.com/" + "openai/codex/blob/"
        link = (
            f"{base}{self.check_docs.SOURCE_COMMIT}/"
            "codex-rs/core/src/session/mod.rs"
        )

        errors = self.check_docs.chapter_link_errors(
            chapter="s01_agent_loop",
            status="已核实官方事实",
            links={link},
            snapshot_by_chapter={},
            rows_by_chapter={},
            readme_rel="chapters/s01_agent_loop/README.md",
        )

        self.assertTrue(any("missing from docs/fact-snapshot.md" in item for item in errors))
        self.assertTrue(any("not registered under s01_agent_loop" in item for item in errors))

    def test_pending_status_without_pending_evidence_is_rejected(self) -> None:
        row = self.check_docs.EvidenceRow(
            chapter="s08_sessions_threads_rollout",
            mechanism="ids",
            level="mechanism-verified",
            source="source",
            verified_scope="scope",
            open_questions="none",
            links=frozenset(),
        )

        errors = self.check_docs.evidence_status_errors(
            rows_by_chapter={"s08_sessions_threads_rollout": [row]},
            statuses={"s08_sessions_threads_rollout": "待核实"},
            chapters=["s08_sessions_threads_rollout"],
        )

        self.assertTrue(any("has no pending evidence row" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
