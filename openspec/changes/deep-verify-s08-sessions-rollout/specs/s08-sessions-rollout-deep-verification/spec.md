## ADDED Requirements

### Requirement: Fixed-SHA s08 official evidence

s08 deep verification SHALL use the current fact snapshot target commit as its official source baseline.

#### Scenario: Source evidence is added

- **WHEN** a s08 mechanism claim is added or strengthened
- **THEN** `docs/source-evidence.md` records a fixed SHA OpenAI source permalink, evidence level, verified scope, and unresolved scope

#### Scenario: Newer upstream code is mentioned

- **WHEN** a newer candidate commit appears relevant
- **THEN** the change may mention it only as freshness risk and SHALL NOT use it as official evidence for this round

### Requirement: s08-only focused scope

s08 deep verification SHALL limit documentation and evidence changes to sessions, threads, rollout, resume/fork, app-server recovery, thread-store, and explicit client/storage boundaries.

#### Scenario: Unrelated chapter finding appears

- **WHEN** a finding concerns s10, diagram redraw, Phase 7 mock, or whole-repository restructuring
- **THEN** the finding is deferred and no implementation change is made under this change

### Requirement: Conservative status upgrade

s08 deep verification SHALL upgrade only claims that are supported by mechanism-level or behavior-level fixed-SHA evidence.

#### Scenario: Path exists but mechanism is unclear

- **WHEN** a source path exists but the control flow, state transition, or product boundary is not closed
- **THEN** the corresponding README wording remains `待核实`, `教学抽象`, or narrower than a complete product claim

#### Scenario: Client or storage boundary is incomplete

- **WHEN** TUI, daemon, debug-client, remote store, or experimental app-server API behavior is not fully closed
- **THEN** the chapter remains `待核实` and the unresolved reason is stated plainly

### Requirement: s08 validation

s08 deep verification SHALL pass OpenSpec and repository checks before completion.

#### Scenario: Change is ready for review

- **WHEN** evidence and wording updates are complete
- **THEN** the maintainer runs `openspec validate deep-verify-s08-sessions-rollout --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`
