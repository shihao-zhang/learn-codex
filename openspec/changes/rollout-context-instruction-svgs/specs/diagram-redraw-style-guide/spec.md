## ADDED Requirements

### Requirement: Context and instruction SVG rollout

The repository SHALL add optional SVG teaching support for the context and instruction batch without replacing existing Mermaid mechanism diagrams.

#### Scenario: Context and instruction batch is implemented

- **WHEN** `rollout-context-instruction-svgs` is implemented
- **THEN** s05 and s06 each gain one scoped SVG under the chapter `diagrams/` directory
- **AND** each SVG has a companion Markdown note in the same directory

#### Scenario: Mermaid remains primary

- **WHEN** s05 or s06 README is updated
- **THEN** the chapter continues to present `diagram.mmd` as the main mechanism diagram
- **AND** the SVG is linked only as optional teaching support

### Requirement: Context SVG preserves compaction fact boundaries

The s05 SVG SHALL distinguish verified compaction entry points from teaching simplifications about pressure, thresholds, preservation, summary quality, and recovery.

#### Scenario: s05 diagram marks facts

- **WHEN** the s05 SVG depicts compact entry points, compacted history replacement, rollout recording, or truncation helper evidence
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** fixed token thresholds, context pressure examples, preserved field lists, summary quality risks, mock trace events, and recovery wording are marked `TEACHING` or `教学辅助`

#### Scenario: s05 diagram shows loss or recovery

- **WHEN** the s05 SVG depicts summary loss, truncation, or missing constraints
- **THEN** the loss point is visually marked as `FAIL` or risk
- **AND** the safe next step is marked `RECOVERY` or `恢复选择`
- **AND** the diagram does not claim compaction is lossless memory

### Requirement: Instruction SVG preserves hierarchy fact boundaries

The s06 SVG SHALL distinguish verified instruction source and injection paths from teaching examples about priority, conflict handling, authorization, and product copy.

#### Scenario: s06 diagram marks facts

- **WHEN** the s06 SVG depicts `AGENTS.md` discovery, project/user instruction composition, or initial context instruction injection
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** conflict examples, priority visualization, authorization copy, project constraint examples, and mock trace events are marked `TEACHING` or `教学辅助`

#### Scenario: s06 diagram shows conflict

- **WHEN** the s06 SVG depicts a user request conflicting with higher-priority or project-scoped rules
- **THEN** the conflict point is visually marked as `FAIL`, `DENY`, or conflict
- **AND** the safe next step is marked `RECOVERY` or `恢复选择`
- **AND** the diagram does not reveal or invent private prompt text or an unverified priority algorithm

### Requirement: Context and instruction companion notes

Each context and instruction SVG SHALL include a companion Markdown note that records review inputs and human QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens a companion Markdown file for s05 or s06
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

### Requirement: Context and instruction rollout validation

The context and instruction SVG rollout SHALL pass repository checks without modifying evidence files, check scripts, or chapter statuses.

#### Scenario: Change is ready

- **WHEN** the context and instruction SVG rollout is complete
- **THEN** `openspec validate rollout-context-instruction-svgs --strict`, `openspec validate --all --strict`, XML parse checks for newly added SVGs, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, s08/s10/s12 statuses, and s05/s06 statuses remain unchanged
