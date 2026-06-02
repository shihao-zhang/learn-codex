# phase5-s08-verification Specification

## Purpose
定义 Phase 5 对 s08 session、thread 和 rollout 语义的第一轮核验要求，保持未闭环部分为 `待核实`。
## Requirements
### Requirement: s08 evidence-first verification
Phase 5 s08 verification SHALL update mechanism-level evidence before changing chapter status or expanding chapter claims.

#### Scenario: official fact is added
- **WHEN** s08 adds or strengthens an official implementation claim
- **THEN** `docs/source-evidence.md` records a fixed SHA OpenAI source permalink for that exact mechanism and labels unresolved scope in notes

#### Scenario: evidence remains incomplete
- **WHEN** the resume/thread/rollout chain still has unknown product or implementation boundaries
- **THEN** s08 remains `待核实` and the README states the remaining gap instead of inferring behavior

### Requirement: s08 scope guard
Phase 5 s08 verification SHALL stay within session/thread/rollout/thread-store/resume/fork/app-server recovery behavior.

#### Scenario: unrelated chapter would be changed
- **WHEN** a finding concerns s10 or another chapter body
- **THEN** the change is deferred unless it is required shared evidence or status wording for s08 verification

### Requirement: s08 validation
Phase 5 s08 verification SHALL pass the repository checks used for documentation and teaching mocks.

#### Scenario: verification is completed
- **WHEN** the s08 evidence and wording updates are ready for review
- **THEN** the run records `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, `git diff --check`, and OpenSpec validation for this change
