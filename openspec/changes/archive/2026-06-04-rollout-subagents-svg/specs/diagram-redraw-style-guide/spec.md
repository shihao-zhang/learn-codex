## ADDED Requirements

### Requirement: s11 subagents SVG rollout

The repository SHALL add optional SVG teaching support for s11 without replacing the existing Mermaid mechanism diagram or changing chapter status.

#### Scenario: s11 SVG is implemented

- **WHEN** `rollout-subagents-svg` is implemented
- **THEN** s11 gains one scoped SVG under the chapter `diagrams/` directory
- **AND** the SVG has a companion Markdown note in the same directory

#### Scenario: Mermaid remains primary

- **WHEN** s11 README is updated
- **THEN** the chapter continues to present `diagram.mmd` as the main mechanism diagram
- **AND** the SVG is linked only as optional teaching support

### Requirement: s11 SVG preserves subagent fact boundaries

The s11 SVG SHALL distinguish registered source mechanisms from unresolved product semantics and teaching simplifications.

#### Scenario: s11 diagram marks facts

- **WHEN** the s11 SVG depicts multi-agent tool surface, `spawn_agent`, `AgentControl`, delegate event forwarding, delegate approval forwarding, agent jobs CSV worker behavior, or ordinary tool-call parallel runtime
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** result-merge explanations, UI progress suggestions, mock trace events, synthetic examples, and reader guidance are marked `TEACHING` or `教学辅助`

#### Scenario: s11 diagram shows unresolved product semantics

- **WHEN** the s11 SVG mentions default enablement, product entry, multi-agent v1/v2 experience, or complete permission inheritance strategy
- **THEN** those nodes or notes are visibly marked `待核实`
- **AND** the diagram does not present them as stable official capability

#### Scenario: s11 diagram avoids over-generalization

- **WHEN** the s11 SVG shows delegation or parallel job execution
- **THEN** it does not draw s11 as a general official subagent platform
- **AND** it does not present agent jobs as a generic batch-processing API
- **AND** it does not present `tools/parallel.rs` as child-agent parallelism

### Requirement: s11 SVG companion note records boundaries

The s11 SVG SHALL include a companion Markdown note that records review inputs, mapping, fact boundaries, and manual QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens the s11 companion Markdown file
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`
- **AND** it explicitly states that default enablement, product entry, and multi-agent v1/v2 experience remain to be verified

### Requirement: s11 rollout validation

The s11 SVG rollout SHALL pass repository checks without modifying global guide, evidence files, check scripts, or chapter statuses.

#### Scenario: Change is ready

- **WHEN** the s11 SVG rollout is complete
- **THEN** `openspec validate rollout-subagents-svg --strict`, `openspec validate --all --strict`, XML parse checks for the newly added SVG, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** repository README, roadmap, `docs/diagram-style-guide.md`, `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and chapter statuses remain unchanged
