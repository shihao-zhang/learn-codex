#!/usr/bin/env python3
"""Run every learn-codex chapter mock on happy and failure paths."""

from __future__ import annotations

import json
import subprocess
import sys
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


def run_mock(chapter: str, path_name: str) -> dict:
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "chapters" / chapter / "mock.py"),
            "--demo",
            "--path",
            path_name,
            "--trace-json",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"{chapter} {path_name} failed:\n{result.stderr}")
    return json.loads(result.stdout)


def main() -> int:
    total_events = 0
    for chapter in CHAPTERS:
        for path_name in ["happy", "failure"]:
            payload = run_mock(chapter, path_name)
            total_events += len(payload["events"])
            print(f"OK {chapter} {path_name}: {len(payload['events'])} events")
    print(f"OK all mocks: {len(CHAPTERS) * 2} paths, {total_events} events")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
