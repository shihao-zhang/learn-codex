#!/usr/bin/env python3
"""Teaching mock for s11_subagents_parallel_jobs."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s11_subagents_parallel_jobs",
    title="Agent jobs, delegation, and parallel execution",
    summary="Shows a cautious teaching model for concurrent work without claiming final Codex semantics.",
    happy_path=[
        event("plan", "parent task splits independent checks", jobs=2),
        event("dispatch", "runtime starts jobs with separate context", isolation="teaching"),
        event("join", "runtime collects both results", completed=2),
        event("merge", "parent summarizes results for the user", conflicts=False),
    ],
    failure_path=[
        event("dispatch", "one delegated job fails", job="review-docs"),
        event("join", "runtime records partial completion", completed=1),
        event("merge", "parent reports failed job and usable result", degrade=True),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
