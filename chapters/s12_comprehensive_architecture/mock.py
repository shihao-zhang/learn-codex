#!/usr/bin/env python3
"""Teaching mock for s12_comprehensive_architecture."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s12_comprehensive_architecture",
    title="End-to-end teaching architecture",
    summary="Shows how the prior chapters connect as a teaching model, not an official diagram.",
    happy_path=[
        event("input", "user submits task through CLI/app surface", surface="teaching"),
        event("runtime", "loop builds model input from instructions and context", chapters="s01-s07"),
        event("tooling", "tools execute under permission boundaries", chapters="s03-s04"),
        event("state", "session/app-server surfaces progress", chapters="s08-s09"),
        event("answer", "runtime returns final response with traceable decisions", status="complete"),
    ],
    failure_path=[
        event("input", "task requires unsafe tool and stale context", risk="combined"),
        event("permissions", "runtime blocks unsafe operation", decision="deny"),
        event("context", "runtime compacts or asks for clarification", action="recover"),
        event("answer", "runtime explains limits instead of overclaiming", status="partial"),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
