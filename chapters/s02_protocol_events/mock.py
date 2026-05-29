#!/usr/bin/env python3
"""Teaching mock for s02_protocol_events."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s02_protocol_events",
    title="Protocol events and client-visible state",
    summary="Shows how runtime state becomes client-consumable events.",
    happy_path=[
        event("request", "client submits user input", item="UserInput"),
        event("event", "runtime emits turn_started", audience="client"),
        event("event", "runtime streams model_message_delta", partial=True),
        event("event", "runtime emits turn_completed", terminal=True),
    ],
    failure_path=[
        event("request", "client submits malformed tool result", item="ToolOutput"),
        event("validate", "protocol validation rejects unknown field", field="toolz"),
        event("event", "runtime emits error event with stable code", recoverable=False),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
