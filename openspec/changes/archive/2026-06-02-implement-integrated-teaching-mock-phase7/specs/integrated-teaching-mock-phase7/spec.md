## ADDED Requirements

### Requirement: Integrated mock implementation

The repository SHALL provide a runnable Phase 7 integrated teaching mock through s12.

#### Scenario: Existing happy path remains compatible

- **WHEN** a maintainer runs `python3 chapters/s12_comprehensive_architecture/mock.py --demo --path happy`
- **THEN** the command succeeds, emits a deterministic teaching trace, and includes a `Teaching mock only` disclaimer

#### Scenario: Existing failure path remains compatible

- **WHEN** a maintainer runs `python3 chapters/s12_comprehensive_architecture/mock.py --demo --path failure`
- **THEN** the command succeeds, emits a deterministic combined failure trace, and includes a `Teaching mock only` disclaimer

### Requirement: Key teaching surfaces

The integrated mock SHALL cover the main harness surfaces in one readable trace.

#### Scenario: Happy path is reviewed

- **WHEN** a reviewer reads or runs the happy path
- **THEN** it covers agent loop, tool dispatch, permission allow, context budget, trace checkpoint, and final answer

#### Scenario: Failure scenarios are reviewed

- **WHEN** a reviewer runs the additional integrated scenarios
- **THEN** they cover tool dispatch failure, permission denied, context pressure, instruction conflict, and session recovery

### Requirement: Offline deterministic boundary

The integrated mock SHALL remain deterministic, offline, and Python standard-library only.

#### Scenario: Mock runs

- **WHEN** the mock is executed
- **THEN** it does not call OpenAI APIs, network resources, Keychain, external CLIs, true desktop state, or real approval systems

#### Scenario: Trace is emitted

- **WHEN** `--trace-json` is used
- **THEN** the JSON contains no timestamps, randomness, machine-specific paths, or external state

### Requirement: Teaching fact boundary

The integrated mock SHALL preserve this repository's fact boundary.

#### Scenario: Output is rendered

- **WHEN** the mock emits text or JSON
- **THEN** it states that the trace is a teaching mock and does not claim to reproduce OpenAI Codex or Codex Desktop

#### Scenario: s08 and s10 are referenced

- **WHEN** the mock discusses session recovery, thread/rollout concepts, MCP, extensions, or skills
- **THEN** it preserves the current `待核实` boundary and does not upgrade s08/s10 chapter status

### Requirement: Validation coverage

The implementation SHALL be covered by repository checks before it is marked ready.

#### Scenario: Change is ready for review

- **WHEN** implementation and docs are complete
- **THEN** the maintainer runs `openspec validate implement-integrated-teaching-mock-phase7 --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`
