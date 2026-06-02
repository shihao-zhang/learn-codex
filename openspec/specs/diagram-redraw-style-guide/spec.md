# diagram-redraw-style-guide Specification

## Purpose

定义本仓教学图的长期边界：Mermaid 保持为章节主机制图，SVG 作为可选教学辅助图，用手写、可审查、中文优先的方式解释路径、边界、失败、恢复和 trace，同时不把教学表达升级为 `openai/codex` 官方事实。

## Requirements

### Requirement: Diagram rollout remains OpenSpec-governed and incremental

Diagram redraw and SVG rollout work SHALL use OpenSpec before changing long-term diagram rules or adding batches of chapter SVGs.

#### Scenario: Diagram rules change

- **WHEN** diagram style rules, fact boundaries, validation criteria, or rollout rhythm change
- **THEN** the change defines scope, non-goals, visual rules, fact boundaries, and validation checks in OpenSpec before implementation

#### Scenario: Bulk redraw is proposed

- **WHEN** future diagram work expands beyond a small pilot or batch
- **THEN** it is split into reviewed increments rather than replacing s01-s12 diagrams in one change

#### Scenario: Pilot or batch is selected

- **WHEN** a new SVG batch is planned
- **THEN** it identifies the chapter set, source inputs, expected teaching value, and high-risk fact boundaries before files are added

### Requirement: Mermaid and SVG have distinct jobs

The repository SHALL keep Mermaid as the primary chapter mechanism diagram format and use SVG only as optional teaching support.

#### Scenario: Chapter gains SVG support

- **WHEN** a chapter gains an SVG teaching diagram
- **THEN** the chapter keeps `diagram.mmd` as the main mechanism diagram
- **AND** the README links the SVG only as optional teaching material

#### Scenario: SVG purpose is constrained

- **WHEN** an SVG is added
- **THEN** it explains paths, boundaries, failures, recovery choices, comparisons, or trace reading
- **AND** it does not replace the chapter's Mermaid structure map or become an official architecture diagram

### Requirement: SVG source is reviewable and dependency-light

SVG teaching diagrams SHALL be hand-written, text-reviewable assets without external generation dependency.

#### Scenario: SVG source is reviewed

- **WHEN** an SVG is added or modified
- **THEN** it is readable text that can be reviewed in git diff
- **AND** it has no external image, font, network, generated bitmap, or export-pipeline dependency

#### Scenario: Image generation is proposed

- **WHEN** a generated image is proposed as the final source for a mechanism or fact diagram
- **THEN** it is rejected for final use
- **AND** any useful idea is manually redrawn into reviewable SVG with explicit fact boundaries

#### Scenario: Alternate drawing method is evaluated

- **WHEN** diagrams become numerous or require reusable layout tokens and export automation
- **THEN** a later OpenSpec change may evaluate HTML/CSS source exported to SVG/PNG

### Requirement: SVG diagrams are Chinese-first and accessible

SVG teaching diagrams SHALL use Chinese as the primary reader-facing language and include minimum accessibility metadata.

#### Scenario: Chinese reader scans the diagram

- **WHEN** the visible title, node labels, explanations, legend, notes, and boundary text are rendered
- **THEN** Chinese is the primary reader-facing language
- **AND** English identifiers remain only as secondary traceability chips for commands, paths, schema fields, or mock event kinds

#### Scenario: SVG file is opened

- **WHEN** the SVG is viewed or reviewed as source
- **THEN** it includes a clear `<title>`
- **AND** it includes a useful `<desc>` explaining scope and non-official boundary
- **AND** the visible diagram includes a legend or boundary note

### Requirement: SVG diagrams preserve semantic fact boundaries

Every SVG teaching diagram SHALL visually distinguish official facts, pending semantics, teaching abstractions, failure/deny paths, and recovery choices when those semantics appear.

#### Scenario: Official fact appears

- **WHEN** a node or edge is marked `FACT`
- **THEN** it can be traced to fixed SHA OpenAI source evidence, official OpenAI documentation, a release note, or `docs/source-evidence.md`

#### Scenario: Pending semantics appear

- **WHEN** a diagram references s08, s10, or another unresolved mechanism
- **THEN** the relevant node or edge is marked `待核实`
- **AND** the diagram does not present it as stable official capability

#### Scenario: Teaching abstraction appears

- **WHEN** a diagram shows mock trace fields, simplified budgets, teaching checkpoints, synthetic examples, UI suggestions, or cross-chapter explanation
- **THEN** it is marked `TEACHING` or `教学辅助`
- **AND** it does not claim equivalence to OpenAI Codex official behavior

#### Scenario: Failure or recovery is shown

- **WHEN** a diagram depicts a blocked, denied, skipped, failed, or recoverable action
- **THEN** it marks the reason with `FAIL` or `DENY` where appropriate
- **AND** any safe next step is marked `RECOVERY` or `恢复选择`

### Requirement: Failure paths are readable and side effects are explicit

SVG diagrams SHALL make failure, denial, and recovery paths understandable to product readers without implying unsafe side effects ran.

#### Scenario: Failure path is drawn

- **WHEN** a diagram depicts missing handler, schema drift, context pressure, instruction conflict, permission denial, or recovery stop
- **THEN** it labels the failure point, decision reason, and user-visible recovery choice

#### Scenario: Side effects are avoided

- **WHEN** a failure or denial path prevents an action from running
- **THEN** the diagram explicitly marks the handler, command, or side effect as not invoked, skipped, denied, or requiring human authorization

### Requirement: SVG companion notes record review inputs

SVG diagrams that use fact markers, mock traces, or pending semantics SHALL have companion Markdown notes.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens a companion Markdown file
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

#### Scenario: File organization is checked

- **WHEN** a chapter SVG is added
- **THEN** it lives under `chapters/<chapter>/diagrams/`
- **AND** its companion Markdown lives in the same directory
- **AND** chapter README navigation remains a short optional entry

### Requirement: Chapter SVG coverage is planned before broad rollout

The repository SHALL maintain chapter SVG coverage planning while keeping high-risk chapters explicitly bounded.

#### Scenario: Coverage plan is reviewed

- **WHEN** a maintainer reviews `docs/diagram-style-guide.md`
- **THEN** it lists the planned core SVG direction for all 12 chapters
- **AND** it identifies high-risk chapters whose diagrams require explicit pending or teaching markers

#### Scenario: Foundation runtime batch is implemented

- **WHEN** the foundation runtime SVG batch is implemented
- **THEN** s01, s02, and s03 each gain one scoped SVG under the chapter `diagrams/` directory
- **AND** each SVG has a companion Markdown note in the same directory
- **AND** each README continues to present `diagram.mmd` as the main mechanism diagram

#### Scenario: Future batches are planned

- **WHEN** later changes add SVGs to more chapters
- **THEN** they follow the documented batch rhythm: foundation runtime, tools and permissions, context and instructions, sessions and extensions, then comprehensive architecture

#### Scenario: High-risk chapters are drawn

- **WHEN** s08 or s10 gains SVG teaching material
- **THEN** the SVG visibly marks unresolved semantics as `待核实`
- **AND** it avoids drawing them as official stable capabilities

#### Scenario: s12 is drawn

- **WHEN** s12 gains new or revised SVG material
- **THEN** it remains marked as `教学抽象`
- **AND** any s08/s10-related edge keeps `待核实` chips where relevant

### Requirement: Foundation SVGs preserve chapter-specific fact boundaries

Foundation runtime SVGs SHALL distinguish registered mechanism facts from teaching simplifications and examples.

#### Scenario: s01 loop diagram marks facts

- **WHEN** the s01 SVG depicts the turn loop, tool call routing, observation 回填, or conversation item recording
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** simplified sequencing, mock events, example tool names, and recovery wording are marked `TEACHING` or `教学辅助`

#### Scenario: s02 protocol diagram marks facts

- **WHEN** the s02 SVG depicts protocol events, response/input items, or trace context
- **THEN** only registered protocol mechanism entries are marked `FACT`
- **AND** UI state, product display suggestions, event names from mock, schema drift examples, and compatibility advice are marked `TEACHING` or `教学辅助`

#### Scenario: s03 tool dispatch diagram marks facts

- **WHEN** the s03 SVG depicts model-visible specs, registry, router, handler execution, or result 回写
- **THEN** only registered router/registry/dispatch mechanism entries are marked `FACT`
- **AND** example tool names, simplified parameters, mock handler names, and product explanations are marked `TEACHING` or `教学辅助`

### Requirement: Rendered SVG visual QA is required

The repository SHALL visually verify high-value SVG teaching diagrams after rendering, not only by inspecting source XML.

#### Scenario: SVG is ready for review

- **WHEN** a chapter SVG is added or materially revised
- **THEN** the maintainer renders it to an image or browser preview
- **AND** verifies that the main path, side paths, text, chips, arrows, and legend are readable

#### Scenario: Main path hierarchy is checked

- **WHEN** a diagram contains both verified mechanism facts and teaching failure or recovery paths
- **THEN** the verified mechanism path is visually primary
- **AND** teaching paths, trace examples, and legend content are visually secondary

#### Scenario: Overlap is checked

- **WHEN** a rendered SVG is inspected
- **THEN** cards, labels, chips, arrows, and legend blocks do not overlap or obscure each other
- **AND** connector lines do not pass through reader-facing text

#### Scenario: Dense diagram is simplified

- **WHEN** a diagram becomes visually dense enough that the first reading path is unclear
- **THEN** the diagram is reorganized into separate layers such as main path, side explanation, and legend
- **AND** nonessential chips or copy are reduced before adding more visual elements

### Requirement: Diagram changes pass validation without evidence drift

Diagram style guide and SVG rollout changes SHALL pass repository checks without modifying fact snapshot, source evidence, check scripts, or chapter statuses unless a separate approved change explicitly covers that work.

#### Scenario: Change is ready

- **WHEN** diagram style, SVG rollout, archive, or material SVG revision work is complete
- **THEN** the maintainer runs the relevant `openspec validate ... --strict` command
- **AND** runs `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`

#### Scenario: Fact boundary is protected

- **WHEN** SVG or diagram style work is committed
- **THEN** `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and s08/s10/s12 statuses remain unchanged unless the OpenSpec change explicitly requires those files or statuses to change
