## ADDED Requirements

### Requirement: Phase 7 design-only boundary

Phase 7 SHALL begin with an OpenSpec design change before any integrated teaching mock implementation.

#### Scenario: Design change is created

- **WHEN** Phase 7 integrated teaching mock work starts
- **THEN** the repository contains `proposal.md`, `design.md`, `tasks.md`, and `specs/.../spec.md` for `design-integrated-teaching-mock-phase7`

#### Scenario: Current round remains design-only

- **WHEN** this change is applied
- **THEN** it does not modify Python mock code, does not add dependencies, and does not update mock runners or tests for a new implementation

### Requirement: Integrated teaching surfaces

The Phase 7 design SHALL cover the main runtime surfaces that a product manager needs to see in one trace.

#### Scenario: Coverage is reviewed

- **WHEN** a reviewer reads the design
- **THEN** it covers agent loop, tool dispatch, permission decision, context pressure, instruction conflict, session trace / recovery, and failure recovery

### Requirement: Teaching mock constraints

The future integrated mock SHALL remain deterministic, offline, Python standard-library only, and clearly labeled as teaching material.

#### Scenario: Future implementation is proposed

- **WHEN** a later change implements the integrated mock
- **THEN** it uses no network calls, no real OpenAI API calls, no external services, no non-standard-library dependencies, no randomness, and no wall-clock-dependent output

#### Scenario: Output is rendered

- **WHEN** the future mock emits text or JSON
- **THEN** it includes a `Teaching mock only` style disclaimer and does not claim to reproduce OpenAI Codex

### Requirement: Fact boundary preservation

The Phase 7 design SHALL preserve this repository's official-fact boundary.

#### Scenario: Design references official facts

- **WHEN** the design or future implementation states an `openai/codex` official mechanism fact
- **THEN** the claim is backed by a fixed SHA OpenAI source permalink, OpenAI official documentation, or release note, and is registered according to the repository evidence workflow

#### Scenario: Design uses Codex Desktop experience

- **WHEN** Codex Desktop experience informs a teaching question, scenario, or failure path
- **THEN** it is labeled as a teaching prompt, product-design inspiration, `推断`, or `待核实`, not as an `openai/codex` official fact

#### Scenario: Design references s08 or s10

- **WHEN** the design discusses session trace / recovery, rollout, thread-store, MCP, extensions, or skills
- **THEN** it explicitly preserves the current `待核实` boundary for s08/s10 and does not upgrade those chapters to stable official product claims

### Requirement: Trace contract for recovery

The Phase 7 design SHALL describe a stable teaching trace that can explain recovery without implying official schema.

#### Scenario: Recovery path is designed

- **WHEN** the future mock demonstrates session trace / recovery
- **THEN** the trace uses teaching-named fields such as checkpoint, decision reason, and recovery choice, and avoids claiming equivalence to official session, rollout, thread-store, or protocol fields

### Requirement: Phase 7 validation

The Phase 7 design change SHALL pass the requested documentation and diff checks before being marked ready.

#### Scenario: Change is ready for review

- **WHEN** the design files and optional roadmap update are complete
- **THEN** the maintainer runs `openspec validate design-integrated-teaching-mock-phase7 --strict`, `python3 scripts/check_docs.py`, and `git diff --check`
