## ADDED Requirements

### Requirement: Mechanism evidence entries
The documentation system SHALL provide a traceable evidence entry for every chapter mechanism point that is presented as an official Codex fact.

#### Scenario: Official mechanism point is documented
- **WHEN** a chapter states a mechanism point as an official Codex fact
- **THEN** the chapter or its evidence file records a fixed SHA OpenAI Codex permalink, the verified scope, the verification date, and the verification status

#### Scenario: Mechanism point is not fully verified
- **WHEN** a mechanism point is based on interpretation, teaching simplification, or incomplete source review
- **THEN** the documentation labels it as `推断`, `待核实`, or `教学抽象` instead of presenting it as an official fact

### Requirement: Status upgrade gate
The documentation system SHALL prevent a chapter from being treated as `已核实官方事实` unless its primary mechanism mapping has evidence beyond path existence.

#### Scenario: Chapter has only path existence evidence
- **WHEN** a chapter only proves that referenced files or directories exist at the target commit
- **THEN** the chapter remains `待核实` unless the main mechanism behavior is separately documented with evidence

#### Scenario: Chapter is upgraded to verified
- **WHEN** a chapter status is changed to `已核实官方事实`
- **THEN** its evidence entries include source-backed support for the chapter's main mechanism claims

### Requirement: Evidence checks
The repository checks SHALL detect missing, stale, or unregistered OpenAI Codex source links in documentation artifacts.

#### Scenario: Link uses the wrong commit
- **WHEN** a documentation file contains an `openai/codex` source link with a commit SHA different from the fact snapshot target commit
- **THEN** the documentation check fails and reports the offending file and SHA

#### Scenario: Link is not registered
- **WHEN** a chapter uses a fixed SHA OpenAI Codex source link that is not present in the fact snapshot or chapter evidence registry
- **THEN** the documentation check fails and reports the missing registration

### Requirement: Mock boundary preservation
The teaching mocks SHALL remain clearly marked as deterministic teaching models and SHALL NOT imply equivalence with OpenAI Codex.

#### Scenario: Human-readable mock output is shown
- **WHEN** a user runs a chapter mock without `--trace-json`
- **THEN** the output includes a non-official teaching mock disclaimer

#### Scenario: Structured mock output is shown
- **WHEN** a user runs a chapter mock with `--trace-json`
- **THEN** the JSON trace includes a non-official teaching mock disclaimer
