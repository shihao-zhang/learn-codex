#!/usr/bin/env python3
"""Teaching mock for s08_sessions_threads_rollout."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s08_sessions_threads_rollout",
    title="Sessions, threads, and rollout persistence",
    summary="Shows the teaching distinction between identity, history, and resume.",
    happy_path=[
        event("session", "runtime creates session id", stable_for="process"),
        event("thread", "runtime associates turns with thread id", stable_for="conversation"),
        event("persist", "runtime writes rollout-style history", purpose="resume"),
        event("resume", "runtime reloads prior turn state", recovered=True),
    ],
    failure_path=[
        event("session", "resume requested for unknown thread", thread_id="missing"),
        event("lookup", "store cannot find rollout history", found=False),
        event("error", "runtime starts fresh or reports missing resume target", recoverable=True),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
