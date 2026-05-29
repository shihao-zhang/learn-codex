#!/usr/bin/env python3
"""Teaching mock for s05_context_window_compaction."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s05_context_window_compaction",
    title="Context window pressure and compaction",
    summary="Shows how a runtime can react before model context overflows.",
    happy_path=[
        event("measure", "runtime measures accumulated context", tokens=7200, limit=10000),
        event("decision", "context fits without compaction", action="continue"),
        event("model_input", "full recent turn history is sent", compacted=False),
    ],
    failure_path=[
        event("measure", "runtime detects context pressure", tokens=13200, limit=10000),
        event("compact", "older turns are summarized", risk="lossy"),
        event("truncate", "nonessential details are removed", preserved="current_task"),
        event("model_input", "model receives compacted context", compacted=True),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
