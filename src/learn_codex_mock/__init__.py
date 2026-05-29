"""Shared deterministic runtime for learn-codex teaching mocks."""

from .runtime import TeachingScenario
from .runtime import TraceEvent
from .runtime import event
from .runtime import run_cli

__all__ = ["TeachingScenario", "TraceEvent", "__version__", "event", "run_cli"]

__version__ = "0.2.0-step2"
