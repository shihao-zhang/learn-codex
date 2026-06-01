#!/usr/bin/env python3
"""Teaching mock for s12_comprehensive_architecture."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from learn_codex_mock import TeachingScenario, event, run_cli


TEACHING_SESSION_ID = "s12-phase7-integrated-demo"

HAPPY_PATH = [
    event(
        "input",
        "user asks for an offline workspace explanation",
        teaching_session_id=TEACHING_SESSION_ID,
        teaching_checkpoint="turn-1/input",
        fact_boundary="teaching_abstract",
    ),
    event(
        "instruction",
        "runtime keeps project offline rules above the user task",
        decision_reason="higher_priority_project_constraint",
        network_allowed=False,
    ),
    event(
        "context",
        "runtime checks budget before the first tool call",
        context_budget_state={"budget": 100, "used": 48, "state": "comfortable"},
        action="continue_without_summary",
    ),
    event(
        "tool_dispatch",
        "runtime resolves a teaching fixture reader",
        requested_tool="read_workspace_fixture",
        handler="teaching_fixture_reader",
    ),
    event(
        "permission",
        "permission table allows an offline workspace fixture read",
        permission_decision="allow",
        decision_reason="read_workspace_fixture_is_offline",
    ),
    event(
        "tool_result",
        "fixture output is added to the teaching trace",
        external_state=False,
        openai_api_called=False,
    ),
    event(
        "boundary",
        "session and extension concepts remain explicitly pending",
        s08_boundary="待核实",
        s10_boundary="待核实",
    ),
    event(
        "answer",
        "runtime returns a final teaching answer with traceable decisions",
        teaching_checkpoint="turn-1/done",
        status="complete",
    ),
]

FAILURE_PATH = [
    event(
        "input",
        "task asks for live network research and desktop state",
        teaching_session_id=TEACHING_SESSION_ID,
        teaching_checkpoint="turn-2/input",
        fact_boundary="teaching_abstract",
    ),
    event(
        "tool_dispatch",
        "router cannot find an approved offline handler for live lookup",
        requested_tool="web_lookup",
        decision_reason="tool_not_registered_in_teaching_registry",
    ),
    event(
        "permission",
        "network fallback is denied by the teaching policy",
        permission_decision="deny",
        decision_reason="offline_mock_boundary",
    ),
    event(
        "context",
        "runtime records context pressure before deciding whether to continue",
        context_budget_state={"budget": 100, "used": 96, "summary_cost": 18},
        action="teaching_summary_required",
    ),
    event(
        "instruction_conflict",
        "user request conflicts with the project rule to avoid external state",
        winning_layer="project",
        decision_reason="do_not_use_network_or_real_desktop_state",
    ),
    event(
        "recovery",
        "runtime stops and returns safe recovery choices to the human",
        teaching_checkpoint="turn-2/stopped",
        recovery_choice="use_offline_fixture_or_request_authorization",
        status="needs_human_choice",
    ),
]

TOOL_DISPATCH_ERROR = [
    event(
        "input",
        "model requests a tool name from outside the teaching registry",
        teaching_session_id=TEACHING_SESSION_ID,
        requested_tool="desktop_screen_capture",
    ),
    event(
        "tool_dispatch",
        "router compares the request with deterministic teaching handlers",
        known_tools=["read_workspace_fixture", "summarize_context_fixture"],
        decision_reason="no_matching_handler",
    ),
    event(
        "failure",
        "runtime emits a recoverable tool dispatch error",
        recoverable=True,
        recovery_choice="ask_human_or_choose_fixture_tool",
    ),
    event(
        "answer",
        "runtime explains the missing handler instead of calling real desktop state",
        status="partial",
        fact_boundary="teaching_abstract",
    ),
]

PERMISSION_DENIED = [
    event(
        "input",
        "task asks to write outside the workspace",
        teaching_session_id=TEACHING_SESSION_ID,
        requested_action="write_outside_workspace",
    ),
    event(
        "permission",
        "teaching policy denies the action without running it",
        permission_decision="deny",
        decision_reason="outside_workspace_has_side_effect_risk",
    ),
    event(
        "tool_dispatch",
        "router does not invoke the write handler after denial",
        handler_called=False,
    ),
    event(
        "recovery",
        "runtime offers a lower-risk workspace-only alternative",
        recovery_choice="write_teaching_patch_inside_workspace",
        requires_human_authorization=True,
    ),
]

CONTEXT_PRESSURE = [
    event(
        "input",
        "task arrives after a long teaching trace",
        teaching_session_id=TEACHING_SESSION_ID,
        teaching_checkpoint="turn-3/input",
    ),
    event(
        "context",
        "runtime measures pressure with a fixed teaching budget",
        context_budget_state={"budget": 100, "used": 92, "state": "near_limit"},
        tokenization="not_real_tokenization",
    ),
    event(
        "context",
        "older trace details are replaced by a teaching summary",
        action="teaching_summary",
        preserved=["current_task", "latest_decision", "open_risk"],
    ),
    event(
        "answer",
        "runtime continues with an explicit lossy-summary warning",
        status="continue_with_summary",
        fact_boundary="teaching_abstract",
    ),
]

INSTRUCTION_CONFLICT = [
    event(
        "instruction",
        "project rule says the mock must stay offline",
        layer="project",
        rule="offline_no_external_state",
    ),
    event(
        "input",
        "user asks for latest online facts and says to ignore the rule",
        layer="user",
        requested_action="network_lookup",
    ),
    event(
        "instruction_conflict",
        "higher-priority offline constraint wins in this teaching stack",
        winning_layer="project",
        decision_reason="explicit_project_boundary",
    ),
    event(
        "recovery",
        "runtime asks for an offline fixture or separate authorization path",
        recovery_choice="use_offline_fixture_or_pause",
        status="blocked_by_boundary",
    ),
]

SESSION_RECOVERY = [
    event(
        "resume",
        "runtime loads a deterministic teaching checkpoint",
        teaching_session_id=TEACHING_SESSION_ID,
        teaching_checkpoint="turn-4/after_fixture_read",
        s08_boundary="待核实",
    ),
    event(
        "recovery",
        "completed fixture read is not repeated on resume",
        idempotent_resume=True,
        skipped_effects=["read_workspace_fixture"],
    ),
    event(
        "permission",
        "next workspace-only action is explained before it would run",
        permission_decision="allow_after_explanation",
        decision_reason="workspace_only_teaching_action",
    ),
    event(
        "boundary",
        "session/thread recovery and skills/MCP semantics remain pending",
        s08_boundary="待核实",
        s10_boundary="待核实",
    ),
    event(
        "answer",
        "runtime resumes from the checkpoint and returns control to the human",
        teaching_checkpoint="turn-4/resumed",
        status="resumed",
    ),
]

SCENARIO = TeachingScenario(
    chapter="s12_comprehensive_architecture",
    title="End-to-end teaching architecture",
    summary=(
        "Shows how prior chapters connect in a deterministic teaching model, "
        "not an official OpenAI Codex or Codex Desktop implementation."
    ),
    happy_path=HAPPY_PATH,
    failure_path=FAILURE_PATH,
    scenario_paths={
        "context_pressure": CONTEXT_PRESSURE,
        "instruction_conflict": INSTRUCTION_CONFLICT,
        "permission_denied": PERMISSION_DENIED,
        "session_recovery": SESSION_RECOVERY,
        "tool_dispatch_error": TOOL_DISPATCH_ERROR,
    },
)


if __name__ == "__main__":
    raise SystemExit(run_cli(SCENARIO))
