## ADDED Requirements

### Requirement: Config and app-server SVG rollout

The repository SHALL add optional SVG teaching support for the s07/s09 rollout without replacing existing Mermaid mechanism diagrams.

#### Scenario: Config and app-server batch is implemented

- **WHEN** `rollout-config-appserver-svgs` is implemented
- **THEN** s07 and s09 each gain one scoped SVG under the chapter `diagrams/` directory
- **AND** each SVG has a companion Markdown note in the same directory

#### Scenario: Mermaid remains primary

- **WHEN** s07 or s09 README is updated
- **THEN** the chapter continues to present `diagram.mmd` as the main mechanism diagram
- **AND** the SVG is linked only as optional teaching support

### Requirement: Config SVG preserves model-choice fact boundaries

The s07 SVG SHALL explain how config, auth, provider, and model choices affect cost, capability, compliance, and availability without turning product guidance into official implementation fact.

#### Scenario: s07 diagram marks facts

- **WHEN** the s07 SVG depicts config type entry points, model preset/model info, or session initialization model selection
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** auth product meaning, account boundaries, provider availability, latest model list, default choices, price/cost interpretation, compliance posture, UI recommendations, and recovery wording are marked `TEACHING` or `教学辅助`

#### Scenario: s07 diagram shows configuration failure

- **WHEN** the s07 SVG depicts missing provider, missing credential, unsupported capability, or unavailable model
- **THEN** the blocked point is visually marked as `FAIL` or risk
- **AND** the safe next step is marked `RECOVERY` or `恢复选择`
- **AND** the diagram does not print, inspect, or imply validation of real credentials

### Requirement: App-server SVG preserves state-sync boundaries

The s09 SVG SHALL distinguish verified app-server/protocol mechanisms from product-surface state synchronization advice.

#### Scenario: s09 diagram marks facts

- **WHEN** the s09 SVG depicts transport connection state, outbound routing, server request callbacks, thread status projection, or schema export
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** product UI surfaces, multi-client behavior, reconnect policy, user-visible status names, Codex Cloud interpretation, and client implementation details are marked `TEACHING` or boundary notes

#### Scenario: s09 diagram shows synchronization boundary

- **WHEN** the s09 SVG depicts runtime events becoming product-visible state
- **THEN** protocol/schema and transport boundaries are visually separated from product-surface interpretation
- **AND** incomplete field-level compatibility or private service behavior is not drawn as stable official capability
- **AND** disconnect or slow-connection examples are marked as risk or recovery teaching paths

### Requirement: Config and app-server companion notes

Each s07/s09 SVG SHALL include a companion Markdown note that records review inputs and human QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens a companion Markdown file for s07 or s09
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

### Requirement: Config and app-server rollout validation

The s07/s09 SVG rollout SHALL pass repository checks without modifying evidence files, check scripts, chapter statuses, root README, roadmap, or the diagram style guide.

#### Scenario: Change is ready

- **WHEN** the config and app-server SVG rollout is complete
- **THEN** `openspec validate rollout-config-appserver-svgs --strict`, `openspec validate --all --strict`, XML parse checks for newly added SVGs, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** `README.md`, `docs/roadmap.md`, `docs/diagram-style-guide.md`, `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and all chapter statuses remain unchanged
