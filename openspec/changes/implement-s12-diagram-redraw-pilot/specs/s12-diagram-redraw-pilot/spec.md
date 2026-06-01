## ADDED Requirements

### Requirement: s12 pilot remains optional

The repository SHALL add the s12 redraw pilot as optional teaching material without replacing existing Mermaid diagrams.

#### Scenario: Pilot files are added

- **WHEN** the s12 pilot is implemented
- **THEN** it adds scoped files under `chapters/s12_comprehensive_architecture/diagrams/`
- **AND** it does not replace `chapters/s12_comprehensive_architecture/diagram.mmd`
- **AND** any Mermaid edits are limited to boundary-label clarifications

#### Scenario: README references the pilot

- **WHEN** s12 README mentions the pilot
- **THEN** it describes the SVG as optional and does not present it as the official or sole mechanism diagram

#### Scenario: Original Mermaid is clarified

- **WHEN** the s12 Mermaid is lightly edited during this pilot
- **THEN** product entry wording is narrowed to a teaching lens or example
- **AND** s08 session/thread/rollout semantics remain visibly marked as pending

### Requirement: Pilot trace maps to s12 mock events

The s12 pilot SVG SHALL map its event numbering to the s12 teaching mock failure trace.

#### Scenario: Failure trace is drawn

- **WHEN** a reviewer reads the SVG and companion notes
- **THEN** F1-F6 correspond to the s12 `--path failure` events in order

#### Scenario: Side effects are blocked

- **WHEN** the pilot depicts denied network or desktop state access
- **THEN** it explicitly marks the real side effect as not invoked or not called

### Requirement: Pilot display is Chinese-first

The s12 pilot SHALL use Chinese as the primary teaching language for its visual display.

#### Scenario: Reader scans the diagram

- **WHEN** a Chinese-speaking product reader scans the title, node titles, explanations, legend, and pilot scope
- **THEN** the primary visible text is Chinese
- **AND** English mock event kinds or trace fields appear only as secondary traceability labels

#### Scenario: Traceability is preserved

- **WHEN** the diagram needs to map back to the Python mock
- **THEN** it may retain English identifiers such as `tool_dispatch`, `permission_decision=deny`, or `needs_human_choice` as small monospace labels

### Requirement: Pilot preserves fact boundaries

The s12 pilot SHALL keep official facts, pending semantics, and teaching abstractions visually distinct.

#### Scenario: Teaching trace is shown

- **WHEN** mock trace events are drawn
- **THEN** the diagram marks them as `TEACHING` and does not claim they are OpenAI Codex official behavior

#### Scenario: Pending semantics are mentioned

- **WHEN** s08/s10, session/thread/rollout, MCP, skills, or extensions are mentioned
- **THEN** they remain marked as `待核实` and are not upgraded to official facts

#### Scenario: Official fact marker is present

- **WHEN** the diagram legend includes `FACT`
- **THEN** it explains that official facts require fixed SHA or official documentation evidence

### Requirement: Pilot is reviewable as text

The pilot SHALL be maintainable through ordinary repository review.

#### Scenario: SVG is reviewed

- **WHEN** the SVG is added
- **THEN** it is hand-written, text-based, includes no external image dependencies, and can be reviewed in git diff

#### Scenario: Companion notes are reviewed

- **WHEN** `pilot-trace.md` is added
- **THEN** it records source trace, event mapping, fact boundary, and manual QA checklist

### Requirement: Pilot validation

The s12 pilot change SHALL pass repository validation before it is marked ready.

#### Scenario: Change is ready

- **WHEN** the pilot files and README update are complete
- **THEN** the maintainer runs `openspec validate implement-s12-diagram-redraw-pilot --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`
