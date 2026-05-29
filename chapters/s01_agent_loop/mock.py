#!/usr/bin/env python3
"""Teaching mock for s01_agent_loop."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s01_agent_loop",
    title="Agent loop, turn, and observation",
    summary="Shows how a turn can alternate between model steps and tool observations.",
    happy_path=[
        event("input", "user asks for a small repository change", turn="t1"),
        event("model", "model decides it needs filesystem context", action="call_tool"),
        event("tool", "read_file returns relevant content", tool="read_file"),
        event("observation", "runtime appends tool result to the turn", visible_to_model=True),
        event("model", "model produces final answer after observation", action="final"),
    ],
    failure_path=[
        event("input", "user asks for a change that needs a missing file", turn="t1"),
        event("model", "model calls read_file", path="missing.py"),
        event("tool_error", "tool reports file not found", recoverable=True),
        event("model", "model explains blocker instead of pretending success", action="final"),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
