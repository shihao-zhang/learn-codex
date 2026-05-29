#!/usr/bin/env python3
"""Teaching mock for s09_app_server_transport."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s09_app_server_transport",
    title="App-server transport and state synchronization",
    summary="Shows how UI-facing requests can bridge into runtime state.",
    happy_path=[
        event("client", "client sends request over transport", method="start_turn"),
        event("server", "app-server validates and forwards request", target="core"),
        event("runtime", "core emits state update", update="turn_started"),
        event("client", "client renders synchronized status", status="running"),
    ],
    failure_path=[
        event("client", "transport connection drops mid-turn", connected=False),
        event("server", "app-server keeps thread state", state="running"),
        event("client", "client reconnects and requests snapshot", recovery="sync_state"),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
