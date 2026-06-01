"""Small deterministic runtime for learn-codex teaching mocks."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from typing import Any, Iterable, List, Mapping, Sequence


@dataclass(frozen=True)
class TraceEvent:
    kind: str
    message: str
    detail: Mapping[str, Any]

    def to_json(self, index: int) -> dict[str, Any]:
        return {
            "index": index,
            "kind": self.kind,
            "message": self.message,
            "detail": dict(self.detail),
        }


@dataclass(frozen=True)
class TeachingScenario:
    chapter: str
    title: str
    summary: str
    happy_path: Sequence[TraceEvent]
    failure_path: Sequence[TraceEvent]
    scenario_paths: Mapping[str, Sequence[TraceEvent]] = field(default_factory=dict)


def event(kind: str, message: str, **detail: Any) -> TraceEvent:
    return TraceEvent(kind=kind, message=message, detail=detail)


def render_text(scenario: TeachingScenario, path_name: str, events: Iterable[TraceEvent]) -> str:
    lines: List[str] = [
        f"{scenario.chapter}: {scenario.title}",
        scenario.summary,
        "note: Teaching mock only; not an OpenAI Codex implementation.",
        f"path: {path_name}",
        "",
    ]
    for index, item in enumerate(events, start=1):
        detail = ", ".join(f"{key}={value!r}" for key, value in sorted(item.detail.items()))
        suffix = f" ({detail})" if detail else ""
        lines.append(f"{index}. [{item.kind}] {item.message}{suffix}")
    return "\n".join(lines)


def render_json(scenario: TeachingScenario, path_name: str, events: Sequence[TraceEvent]) -> str:
    payload = {
        "chapter": scenario.chapter,
        "title": scenario.title,
        "summary": scenario.summary,
        "path": path_name,
        "scenario": path_name,
        "events": [item.to_json(index) for index, item in enumerate(events, start=1)],
        "note": "Teaching mock only; not an OpenAI Codex implementation.",
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def run_cli(scenario: TeachingScenario, argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=scenario.summary)
    parser.add_argument("--demo", action="store_true", help="run the teaching scenario")
    parser.add_argument(
        "--path",
        choices=["happy", "failure"],
        default="happy",
        help="choose the happy path or failure path",
    )
    if scenario.scenario_paths:
        parser.add_argument(
            "--scenario",
            choices=sorted(scenario.scenario_paths),
            help="choose an additional teaching scenario",
        )
    parser.add_argument("--trace-json", action="store_true", help="emit structured JSON trace")
    args = parser.parse_args(argv)

    if not args.demo:
        parser.print_help()
        return 0

    base_paths = {
        "happy": scenario.happy_path,
        "failure": scenario.failure_path,
    }
    path_name = getattr(args, "scenario", None) or args.path
    selected_path = (
        scenario.scenario_paths[path_name]
        if path_name in scenario.scenario_paths
        else base_paths[path_name]
    )
    events = list(selected_path)
    if args.trace_json:
        print(render_json(scenario, path_name, events))
    else:
        print(render_text(scenario, path_name, events))
    return 0
