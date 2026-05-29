#!/usr/bin/env python3
"""Teaching mock for s10_extensions_mcp_skills."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


SCENARIO = TeachingScenario(
    chapter="s10_extensions_mcp_skills",
    title="Extensions, MCP, skills directory, and dynamic tools",
    summary="Shows the boundary between verified paths and still-unverified capability semantics.",
    happy_path=[
        event("config", "runtime discovers configured MCP server", source="config"),
        event("list_tools", "server advertises tool metadata", count=2),
        event("register", "runtime exposes dynamic tools to model", mode="teaching"),
        event("call", "tool call is routed through extension/MCP boundary", status="ok"),
    ],
    failure_path=[
        event("config", "extension claims unsupported tool schema", schema="invalid"),
        event("validate", "runtime refuses to register unsafe dynamic tool", registered=False),
        event("error", "user sees extension/tool setup failure", recoverable=True),
    ],
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
