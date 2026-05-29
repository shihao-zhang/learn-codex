#!/usr/bin/env python3
"""Teaching mock for s06_prompts_instructions."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s06_prompts_instructions",
    title="Prompt and instruction layering",
    summary="Shows how long-lived project instructions shape a turn.",
    happy_path=[
        event("load", "runtime reads system/developer instructions", layer="system"),
        event("load", "runtime reads AGENTS.md rules", layer="project"),
        event("merge", "runtime builds ordered instruction stack", conflict=False),
        event("model_input", "user task is sent with scoped guidance", source="public"),
    ],
    failure_path=[
        event("load", "AGENTS.md says avoid external review without authorization", layer="project"),
        event("user", "user asks to send private diff externally", authorization=False),
        event("decision", "runtime should surface authorization need", action="ask_first"),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
