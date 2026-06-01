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

    def run_s12_scenario(self, scenario: str) -> dict:
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "chapters" / "s12_comprehensive_architecture" / "mock.py"),
                "--demo",
                "--scenario",
                scenario,
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
                self.assertIn("Teaching mock only", payload["note"])
                self.assertGreaterEqual(len(payload["events"]), 3)
            with self.subTest(chapter=chapter, path="failure"):
                payload = self.run_mock(chapter, "failure")
                self.assertEqual(payload["chapter"], chapter)
                self.assertEqual(payload["path"], "failure")
                self.assertIn("Teaching mock only", payload["note"])
                self.assertGreaterEqual(len(payload["events"]), 3)

    def test_s12_integrated_mock_happy_path_boundaries(self) -> None:
        payload = self.run_mock("s12_comprehensive_architecture", "happy")
        kinds = {event["kind"] for event in payload["events"]}
        self.assertIn("instruction", kinds)
        self.assertIn("context", kinds)
        self.assertIn("tool_dispatch", kinds)
        self.assertIn("permission", kinds)

        trace_text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        self.assertIn("Teaching mock only", payload["note"])
        self.assertIn("teaching_session_id", trace_text)
        self.assertIn("teaching_checkpoint", trace_text)
        self.assertIn("context_budget_state", trace_text)
        self.assertIn("s08_boundary", trace_text)
        self.assertIn("s10_boundary", trace_text)
        self.assertIn("待核实", trace_text)

    def test_s12_integrated_mock_failure_path_surfaces(self) -> None:
        payload = self.run_mock("s12_comprehensive_architecture", "failure")
        kinds = [event["kind"] for event in payload["events"]]
        for expected in [
            "tool_dispatch",
            "permission",
            "context",
            "instruction_conflict",
            "recovery",
        ]:
            self.assertIn(expected, kinds)

    def test_s12_integrated_mock_additional_scenarios(self) -> None:
        expected_markers = {
            "tool_dispatch_error": ["tool_dispatch", "no_matching_handler"],
            "permission_denied": ["permission_decision", "deny"],
            "context_pressure": ["context_budget_state", "teaching_summary"],
            "instruction_conflict": ["winning_layer", "project"],
            "session_recovery": ["idempotent_resume", "s08_boundary", "s10_boundary"],
        }
        for scenario, markers in expected_markers.items():
            with self.subTest(scenario=scenario):
                payload = self.run_s12_scenario(scenario)
                self.assertEqual(payload["path"], scenario)
                self.assertEqual(payload["scenario"], scenario)
                self.assertIn("Teaching mock only", payload["note"])
                trace_text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
                for marker in markers:
                    self.assertIn(marker, trace_text)

    def test_s12_integrated_mock_trace_is_deterministic(self) -> None:
        first = self.run_s12_scenario("session_recovery")
        second = self.run_s12_scenario("session_recovery")
        self.assertEqual(first, second)
