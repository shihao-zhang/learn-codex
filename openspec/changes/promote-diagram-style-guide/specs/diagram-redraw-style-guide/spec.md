## ADDED Requirements

### Requirement: Repository-level SVG style guide

The repository SHALL maintain a long-term SVG teaching diagram guide for future chapter and cross-chapter illustration work.

#### Scenario: Style guide is promoted

- **WHEN** diagram style rules are promoted beyond the s12 pilot
- **THEN** the repository provides `docs/diagram-style-guide.md`
- **AND** the guide defines durable rules rather than one-off implementation notes

#### Scenario: Guide does not create official facts

- **WHEN** the guide describes how to draw official facts, pending semantics, or teaching abstractions
- **THEN** it treats SVG as teaching expression only
- **AND** it does not make SVG itself a source of official implementation facts

### Requirement: Mermaid and SVG have distinct jobs

The repository SHALL keep Mermaid as the chapter mechanism diagram format and use SVG only as optional teaching support.

#### Scenario: Chapter keeps its main mechanism diagram

- **WHEN** a chapter gains an SVG teaching diagram
- **THEN** the chapter keeps `diagram.mmd` as the primary mechanism diagram
- **AND** the SVG is linked as optional teaching material

#### Scenario: SVG purpose is constrained

- **WHEN** an SVG is added
- **THEN** it explains paths, boundaries, failures, recovery choices, comparisons, or trace reading
- **AND** it does not replace the chapter's Mermaid structure map

### Requirement: SVG diagrams are reviewable and Chinese-first

SVG teaching diagrams SHALL be hand-written, text-reviewable, Chinese-first assets without external generation dependency.

#### Scenario: SVG source is reviewed

- **WHEN** an SVG is added or modified
- **THEN** it is hand-written text that can be reviewed in git diff
- **AND** it has no external image, font, network, or generated bitmap dependency

#### Scenario: Image generation is proposed

- **WHEN** a generated image is proposed as the final source for a mechanism or fact diagram
- **THEN** it is rejected for final use
- **AND** any useful idea must be manually redrawn into reviewable SVG with explicit fact boundaries

#### Scenario: Chinese reader scans the diagram

- **WHEN** the visible title, node labels, legend, notes, and boundary explanations are rendered
- **THEN** Chinese is the primary reader-facing language
- **AND** English identifiers remain only as secondary traceability chips where useful

### Requirement: SVG diagrams preserve semantic boundaries

Every SVG teaching diagram SHALL visually distinguish official fact, pending semantics, teaching abstraction, failure/deny, and recovery.

#### Scenario: Official facts appear

- **WHEN** a node or edge is marked `FACT`
- **THEN** it can be traced to fixed SHA OpenAI source evidence, official OpenAI documentation, release note, or `docs/source-evidence.md`

#### Scenario: Pending semantics appear

- **WHEN** a diagram references s08, s10, or another unresolved mechanism
- **THEN** the relevant node or edge is marked `待核实`
- **AND** the diagram does not present it as stable official capability

#### Scenario: Teaching abstractions appear

- **WHEN** a diagram shows mock trace fields, simplified budgets, teaching checkpoints, synthetic examples, or cross-chapter explanation
- **THEN** it is marked `TEACHING` or `教学抽象`
- **AND** it does not claim equivalence to OpenAI Codex official behavior

#### Scenario: Failure or recovery is shown

- **WHEN** a diagram depicts a blocked, denied, skipped, or failed action
- **THEN** it marks the reason with `FAIL` or `DENY`
- **AND** any safe next step is marked `RECOVERY`

### Requirement: SVG diagrams include minimum accessibility and review metadata

Every SVG teaching diagram SHALL include enough metadata and legend text for review and reader orientation.

#### Scenario: SVG file is opened

- **WHEN** the SVG is viewed or reviewed as source
- **THEN** it includes a clear `<title>`
- **AND** it includes a useful `<desc>` explaining scope and non-official boundary
- **AND** the visible diagram includes a legend or boundary note

#### Scenario: Companion notes are needed

- **WHEN** a pilot or cross-chapter SVG includes official fact markers, mock trace mapping, or pending semantics
- **THEN** a companion Markdown note records source inputs, event mapping, fact boundary, and manual QA

### Requirement: Chapter SVG coverage is planned before bulk rollout

The repository SHALL maintain a 12-chapter SVG coverage plan while implementing diagrams in batches.

#### Scenario: Coverage plan is reviewed

- **WHEN** a maintainer reviews `docs/diagram-style-guide.md`
- **THEN** it lists the planned core SVG for all 12 chapters
- **AND** it identifies high-risk chapters whose diagrams require explicit pending or teaching markers

#### Scenario: High-risk chapters are drawn

- **WHEN** s08 or s10 gains SVG teaching material
- **THEN** the SVG visibly marks unresolved semantics as `待核实`
- **AND** it avoids drawing them as official stable capabilities

#### Scenario: s12 is drawn

- **WHEN** s12 gains new or revised SVG material
- **THEN** it remains marked as `教学抽象`
- **AND** any s08/s10-related edge keeps `待核实` chips where relevant

### Requirement: Rollout remains incremental

The repository SHALL promote the style guide through limited pilots before adding SVGs across all chapters.

#### Scenario: Current change is implemented

- **WHEN** `promote-diagram-style-guide` is implemented
- **THEN** it adds the long-term guide and only one to two low-risk pilot SVGs
- **AND** it does not redraw all chapters in a single change

#### Scenario: Future batches are planned

- **WHEN** later changes add SVGs to more chapters
- **THEN** they follow the documented batch rhythm: foundation runtime, tools and permissions, context and instructions, sessions and extensions, then comprehensive architecture

### Requirement: Promotion validation

The promoted style guide change SHALL pass repository validation without modifying fact snapshot or check scripts.

#### Scenario: Change is ready

- **WHEN** the guide, navigation, and pilot are complete
- **THEN** the maintainer runs `openspec validate promote-diagram-style-guide --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`
- **AND** `docs/fact-snapshot.md`, `docs/source-evidence.md`, chapter statuses, and `scripts/check_docs.py` remain unchanged
