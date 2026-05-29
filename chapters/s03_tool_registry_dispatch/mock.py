#!/usr/bin/env python3
"""Teaching mock for s03_tool_registry_dispatch."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s03_tool_registry_dispatch",
    title="Tool registry, router, and handler dispatch",
    summary="Shows how a tool name is resolved to a checked handler call.",
    happy_path=[
        event("register", "runtime registers shell and apply_patch tools", count=2),
        event("model", "model requests apply_patch", tool="apply_patch"),
        event("router", "router finds matching handler", handler="ApplyPatchHandler"),
        event("handler", "handler validates args and returns result", status="ok"),
    ],
    failure_path=[
        event("model", "model requests unknown tool", tool="delete_world"),
        event("router", "router cannot resolve tool name", known_tools=["shell", "apply_patch"]),
        event("event", "runtime returns structured tool error", recoverable=True),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
