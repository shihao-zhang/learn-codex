#!/usr/bin/env python3
"""Teaching mock for s07_config_auth_models."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s07_config_auth_models",
    title="Config, auth, and model/provider selection",
    summary="Shows why model selection belongs with config and auth, not only UX.",
    happy_path=[
        event("config", "profile selects provider and model", provider="openai", model="example-model"),
        event("auth", "credential source is available", source="api_key_or_login"),
        event("request", "runtime attaches model settings", reasoning_effort="medium"),
        event("result", "model client is constructed", status="ready"),
    ],
    failure_path=[
        event("config", "profile references missing provider", provider="missing"),
        event("auth", "no usable credential found", source=None),
        event("error", "runtime returns actionable configuration error", recoverable=True),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
