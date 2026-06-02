## ADDED Requirements

### Requirement: Foundation runtime SVG rollout

The repository SHALL add optional SVG teaching support for the first foundation runtime batch without replacing existing Mermaid mechanism diagrams.

#### Scenario: Foundation batch is implemented

- **WHEN** `rollout-foundation-runtime-svgs` is implemented
- **THEN** s01, s02, and s03 each gain one scoped SVG under the chapter `diagrams/` directory
- **AND** each SVG has a companion Markdown note in the same directory

#### Scenario: Mermaid remains primary

- **WHEN** s01, s02, or s03 README is updated
- **THEN** the chapter continues to present `diagram.mmd` as the main mechanism diagram
- **AND** the SVG is linked only as optional teaching support

### Requirement: Foundation SVGs preserve fact boundaries

Foundation runtime SVGs SHALL distinguish verified mechanism facts from teaching simplifications and examples.

#### Scenario: s01 loop diagram marks facts

- **WHEN** the s01 SVG depicts the turn loop, tool call routing, observation回填, or conversation item recording
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** simplified sequencing, mock events, and recovery wording are marked `TEACHING` or `教学辅助`

#### Scenario: s02 protocol diagram marks facts

- **WHEN** the s02 SVG depicts protocol events, response/input items, or trace context
- **THEN** only registered protocol mechanism entries are marked `FACT`
- **AND** UI state, product display suggestions, event names from mock, and compatibility advice are marked `TEACHING` or `教学辅助`

#### Scenario: s03 tool dispatch diagram marks facts

- **WHEN** the s03 SVG depicts model-visible specs, registry, router, handler execution, or result回写
- **THEN** only registered router/registry/dispatch mechanism entries are marked `FACT`
- **AND** example tool names, simplified parameters, mock handler names, and product explanations are marked `TEACHING` or `教学辅助`

### Requirement: Foundation SVG companion notes

Each foundation SVG SHALL include a companion Markdown note that records review inputs and human QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens a companion Markdown file for s01, s02, or s03
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

### Requirement: Foundation rollout validation

The foundation runtime SVG rollout SHALL pass repository checks without modifying evidence files, check scripts, or chapter statuses.

#### Scenario: Change is ready

- **WHEN** the foundation SVG rollout is complete
- **THEN** `openspec validate rollout-foundation-runtime-svgs --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, s08/s10/s12 statuses, and s01-s03 statuses remain unchanged
