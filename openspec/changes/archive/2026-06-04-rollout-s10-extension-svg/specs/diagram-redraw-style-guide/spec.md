## ADDED Requirements

### Requirement: s10 extension SVG rollout

The repository SHALL add optional SVG teaching support for s10 without replacing the existing Mermaid mechanism diagram or changing the chapter status.

#### Scenario: s10 diagram is implemented

- **WHEN** `rollout-s10-extension-svg` is implemented
- **THEN** `s10_extensions_mcp_skills` gains one scoped SVG under the chapter `diagrams/` directory
- **AND** the SVG has a companion Markdown note in the same directory
- **AND** the chapter status remains `待核实`

#### Scenario: Mermaid remains primary

- **WHEN** s10 README is updated
- **THEN** the chapter continues to present `diagram.mmd` as the main mechanism diagram
- **AND** the SVG is linked only as optional teaching support

### Requirement: s10 SVG preserves separate capability paths

The s10 SVG SHALL keep MCP, dynamic tools, extension tools, and skills as separate capability lines unless a fixed SHA official source proves a shared official mechanism.

#### Scenario: Four lines are drawn

- **WHEN** the s10 SVG depicts extension-like capabilities
- **THEN** it shows MCP, dynamic tools, extension tools, and skills as separate paths
- **AND** it does not merge them into one official extension product promise

#### Scenario: Facts are marked

- **WHEN** the s10 SVG marks a node or edge as `FACT`
- **THEN** that claim is limited to mechanisms already registered in `docs/source-evidence.md`
- **AND** the diagram does not use `FACT` to prove cross-client semantics, marketplace behavior, or unified governance

### Requirement: s10 SVG marks unresolved boundaries

The s10 SVG SHALL explicitly mark high-risk unresolved boundaries as `待核实`.

#### Scenario: dynamic tools are shown

- **WHEN** dynamic tools appear in the s10 SVG
- **THEN** the diagram labels `thread/start.dynamicTools` as experimental or pending
- **AND** it does not present dynamic tools as a stable CLI user-created tool entry

#### Scenario: extension tools are shown

- **WHEN** extension tools appear in the s10 SVG
- **THEN** the diagram labels the generic extension user install, discovery, authorization, or marketplace-style entry as `待核实`
- **AND** it only marks built-in app-server extension and runtime adapter evidence as verified when supported by registered evidence

#### Scenario: governance is shown

- **WHEN** the s10 SVG depicts governance across MCP, dynamic tools, extension tools, and skills
- **THEN** it labels any shared or unified governance path as `待核实`
- **AND** it preserves separate per-path governance notes instead of drawing one proven common policy pipeline

### Requirement: s10 SVG companion note records review inputs

The s10 SVG SHALL include a companion Markdown note that records source inputs, mapping, fact boundaries, and manual QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens the s10 companion Markdown file
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

### Requirement: s10 SVG rollout validation

The s10 SVG rollout SHALL pass repository checks without modifying evidence files, check scripts, root navigation, roadmap, style guide, or chapter statuses.

#### Scenario: Change is ready

- **WHEN** the s10 SVG rollout is complete
- **THEN** `openspec validate rollout-s10-extension-svg --strict`, `openspec validate --all --strict`, XML parse checks for the newly added SVG, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** root `README.md`, `docs/roadmap.md`, `docs/diagram-style-guide.md`, `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and chapter statuses remain unchanged
