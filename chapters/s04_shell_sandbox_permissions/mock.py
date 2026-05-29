#!/usr/bin/env python3
"""Teaching mock for s04_shell_sandbox_permissions."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s04_shell_sandbox_permissions",
    title="Shell sandbox and approval boundary",
    summary="Shows how a command crosses policy, sandbox, and approval checks.",
    happy_path=[
        event("tool", "shell command requested", command="python3 -m unittest"),
        event("policy", "command allowed in workspace-write sandbox", network=False),
        event("sandbox", "command runs with workspace write scope", os_boundary="teaching"),
        event("result", "runtime captures exit code and output", exit_code=0),
    ],
    failure_path=[
        event("tool", "shell command requests network and root write", command="curl | sudo sh"),
        event("policy", "runtime requires escalation", reason="network_and_privilege"),
        event("approval", "human rejects request", decision="denied"),
        event("result", "runtime reports denial instead of executing", exit_code=None),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
