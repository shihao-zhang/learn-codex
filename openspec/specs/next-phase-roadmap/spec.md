# next-phase-roadmap Specification

## Purpose
定义后续 phase roadmap 的长期要求，把未闭环事实、教学 mock 和 release readiness 拆成可 review 的工作。
## Requirements
### Requirement: Phase roadmap document
The repository SHALL provide a next-phase roadmap that converts the current reflection into ordered, reviewable work.

#### Scenario: Roadmap is created
- **WHEN** the next-phase planning change is applied
- **THEN** the repository contains a roadmap document that lists the next phases, their purpose, deliverables, acceptance checks, and stop conditions

#### Scenario: Phase order is explicit
- **WHEN** a contributor reads the roadmap
- **THEN** Phase 5 prioritizes s08 and s10 verification before broad content expansion

### Requirement: Pending chapter priority
The roadmap SHALL treat unresolved official-fact boundaries as higher priority than adding more teaching content.

#### Scenario: s08 remains unresolved
- **WHEN** s08 resume/thread/rollout semantics are not end-to-end verified
- **THEN** the roadmap keeps s08 work focused on verification or conservative wording rather than forced status upgrade

#### Scenario: s10 remains unresolved
- **WHEN** skills, MCP, or extension semantics cannot be tied to user-facing CLI behavior
- **THEN** the roadmap keeps s10 work focused on evidence, caveats, and boundary language

### Requirement: Integrated teaching mock planning
The roadmap SHALL define a future integrated mock that connects multiple harness mechanisms without claiming to reproduce Codex.

#### Scenario: Integrated mock is planned
- **WHEN** the roadmap describes the integrated mock
- **THEN** it states that the mock is deterministic, standard-library only, offline, and not equivalent to OpenAI Codex

#### Scenario: Integrated mock scope is defined
- **WHEN** the roadmap lists integrated mock behavior
- **THEN** it includes loop, tool dispatch, permission decision, context pressure, session trace, and failure recovery as planned teaching surfaces

### Requirement: Release-readiness checkpoints
The roadmap SHALL define checks that future phases must pass before they are considered ready.

#### Scenario: Phase is completed
- **WHEN** a future phase claims completion
- **THEN** it has run documentation checks, mock checks, unit tests, and a human-readable review summary
