## ADDED Requirements

### Requirement: s08 session SVG rollout preserves pending boundaries

The repository SHALL add optional SVG teaching support for s08 without replacing the existing Mermaid mechanism diagram or changing the chapter status.

#### Scenario: s08 optional SVG is implemented

- **WHEN** `rollout-s08-session-svg` is implemented
- **THEN** `s08_sessions_threads_rollout` gains one scoped SVG under the chapter `diagrams/` directory
- **AND** the SVG has a companion Markdown note in the same directory
- **AND** the chapter README links the SVG only as optional teaching support
- **AND** `diagram.mmd` remains the main mechanism diagram
- **AND** the s08 status remains `待核实`

### Requirement: s08 SVG marks unresolved recovery and storage semantics

The s08 SVG SHALL visibly mark unresolved recovery, storage, and API stability semantics as `待核实`.

#### Scenario: Remote thread-store backend appears

- **WHEN** the SVG references a remote thread-store backend, non-local persistence, daemon transport, or remote app-server transport as a recovery/storage boundary
- **THEN** the relevant node or edge is marked `待核实`
- **AND** the SVG does not present it as an implemented official backend or stable product capability

#### Scenario: Cloud or desktop recovery semantics appear

- **WHEN** the SVG references Codex Cloud, Codex desktop, cross-client recovery, or desktop resume semantics
- **THEN** the relevant node or edge is marked `待核实`
- **AND** the SVG does not infer official product behavior from desktop observations or teaching mocks

#### Scenario: Experimental API stability appears

- **WHEN** the SVG references `thread/resume`, `thread/fork`, app-server v2, or experimental app-server API stability
- **THEN** the relevant node or edge is marked `待核实`
- **AND** the SVG does not claim a stable public API commitment

### Requirement: s08 SVG distinguishes teaching relationships from product promises

The s08 SVG SHALL explain session/thread/rollout/resume/fork as a teaching relationship while avoiding official recovery-product claims.

#### Scenario: Teaching relationship is drawn

- **WHEN** the SVG depicts session, thread, rollout, resume, or fork
- **THEN** the diagram labels the relationship as teaching support or `局部源码证据` with pending chapter boundary
- **AND** it avoids drawing resume/fork as a guaranteed official recovery path

#### Scenario: Local facts are shown

- **WHEN** the SVG marks a node or edge as `FACT`
- **THEN** the label is scoped as local or `局部` evidence only
- **AND** it can be traced to fixed SHA evidence already registered in `docs/source-evidence.md`
- **AND** it does not upgrade the s08 chapter status

### Requirement: s08 companion note records review inputs and boundaries

The s08 SVG SHALL include a companion Markdown note that records review inputs, mechanism mapping, fact boundaries, and human QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens `chapters/s08_sessions_threads_rollout/diagrams/session-thread-rollout.md`
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

### Requirement: s08 SVG rollout validation

The s08 SVG rollout SHALL pass repository checks without modifying evidence files, check scripts, root navigation, or chapter status.

#### Scenario: Change is ready

- **WHEN** the s08 SVG rollout is complete
- **THEN** `openspec validate rollout-s08-session-svg --strict`, `openspec validate --all --strict`, XML parse checks for the new SVG, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** root README, roadmap, `docs/diagram-style-guide.md`, `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and the s08 status remain unchanged
