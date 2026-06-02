## ADDED Requirements

### Requirement: Design-only diagram redraw change

The repository SHALL start diagram redraw work with a design-only OpenSpec change before replacing chapter diagrams.

#### Scenario: Lightweight research is proposed

- **WHEN** teaching diagram redraw work begins
- **THEN** the change defines scope, non-goals, visual rules, and validation checks before any full chapter image replacement

#### Scenario: Current session stays lightweight

- **WHEN** this change is applied
- **THEN** it does not replace s01-s12 Mermaid diagrams, does not add generated images, and does not modify Python mock code or tests

### Requirement: s12 pilot-first approach

Diagram redraw work SHALL use s12 as the first pilot because it contains the broadest end-to-end teaching trace.

#### Scenario: Pilot input is selected

- **WHEN** a pilot illustration is designed
- **THEN** it is based on s12 mock/test trace, current Mermaid structure, and documented teaching boundaries

#### Scenario: Pilot scope is reviewed

- **WHEN** a reviewer checks the pilot plan
- **THEN** it covers nodes, states, and failure paths without claiming to be an OpenAI official architecture diagram

### Requirement: Recommended drawing method

The repository SHALL prefer hand-written SVG for high-value teaching redraw pilots while keeping Mermaid as the existing mechanism diagram source.

#### Scenario: Main method is chosen

- **WHEN** a small number of high-value teaching diagrams need clearer visual hierarchy than Mermaid can provide
- **THEN** the diagram source is hand-written SVG with reviewable text, explicit legend, and no external generation dependency

#### Scenario: Backup method is chosen

- **WHEN** diagrams become numerous or need reusable layout tokens and export automation
- **THEN** a later change may evaluate HTML/CSS source files exported to SVG/PNG

#### Scenario: GPT image generation is considered

- **WHEN** generated images are proposed for mechanism or fact diagrams
- **THEN** they are rejected as source-of-truth diagrams because they are difficult to diff, verify, and keep inside fact boundaries

### Requirement: Visual fact boundary markers

Every redesigned teaching diagram SHALL distinguish official fact, pending semantics, and teaching abstraction.

#### Scenario: Official fact appears

- **WHEN** a node or edge is marked as official fact
- **THEN** it uses a `FACT` marker and is backed by the repository evidence workflow

#### Scenario: Pending semantics appear

- **WHEN** a node or edge references s08/s10 or another unresolved mechanism
- **THEN** it uses a `待核实` marker and does not upgrade the claim to official fact

#### Scenario: Teaching abstraction appears

- **WHEN** a diagram combines mechanisms for explanation, shows mock trace fields, uses fixed teaching budgets, or depicts teaching checkpoints
- **THEN** it uses a `TEACHING` marker and does not claim equivalence to OpenAI Codex, Codex Desktop, or production behavior

### Requirement: Chinese-first display language

Redesigned teaching diagrams SHALL use Chinese as the primary reader-facing language.

#### Scenario: Teaching diagram is displayed

- **WHEN** a Chinese-speaking product reader scans the title, node titles, explanations, legend, and boundary notes
- **THEN** those primary display elements are written in Chinese

#### Scenario: Technical traceability is needed

- **WHEN** a diagram needs to preserve traceability to commands, paths, schema fields, or mock event kinds
- **THEN** English identifiers may remain as secondary monospace chips or inline technical labels

### Requirement: Failure path readability

Redesigned diagrams SHALL make failure and recovery paths understandable to product readers.

#### Scenario: Failure path is drawn

- **WHEN** a diagram depicts deny, missing handler, context pressure, instruction conflict, or recovery stop
- **THEN** it labels the failure point, decision reason, and user-visible recovery choice

#### Scenario: Side effects are avoided

- **WHEN** a failure path prevents an action from running
- **THEN** the diagram explicitly marks the handler or side effect as not invoked, skipped, or requiring human authorization

### Requirement: Legend, numbering, and file organization

Redesigned diagrams SHALL be traceable back to their teaching inputs.

#### Scenario: Trace events are numbered

- **WHEN** a diagram is based on s12 trace events
- **THEN** event numbering follows the mock trace index with prefixes such as `H`, `F`, `TD`, `P`, `C`, `I`, or `R`

#### Scenario: Pilot files are added later

- **WHEN** a future change adds s12 pilot image files
- **THEN** they live under `chapters/s12_comprehensive_architecture/diagrams/` or a similarly scoped pilot directory and do not replace `diagram.mmd` without a separate review

### Requirement: Validation before review

The diagram redraw style guide change SHALL pass requested checks before being marked ready.

#### Scenario: Change is ready for review

- **WHEN** the design files are complete
- **THEN** the maintainer runs `openspec validate design-diagram-redraw-style-guide --strict`, `python3 scripts/check_docs.py`, and `git diff --check`
