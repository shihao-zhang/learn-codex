from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
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


class ChapterMockTest(unittest.TestCase):
    def run_mock(self, chapter: str, path: str) -> dict:
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "chapters" / chapter / "mock.py"),
                "--demo",
                "--path",
                path,
                "--trace-json",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_all_chapter_mocks_have_happy_and_failure_paths(self) -> None:
        for chapter in CHAPTERS:
            with self.subTest(chapter=chapter, path="happy"):
                payload = self.run_mock(chapter, "happy")
                self.assertEqual(payload["chapter"], chapter)
                self.assertEqual(payload["path"], "happy")
                self.assertGreaterEqual(len(payload["events"]), 3)
            with self.subTest(chapter=chapter, path="failure"):
                payload = self.run_mock(chapter, "failure")
                self.assertEqual(payload["chapter"], chapter)
                self.assertEqual(payload["path"], "failure")
                self.assertGreaterEqual(len(payload["events"]), 3)
