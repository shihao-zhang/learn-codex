## ADDED Requirements

### Requirement: Project goal statement
The repository SHALL provide a concise project goal statement for AI product managers and agent platform designers.

#### Scenario: Reader opens the goal statement
- **WHEN** a reader opens the project goal document
- **THEN** it explains that the repository teaches agent harness mechanisms using public `openai/codex` Rust CLI source as a sample

#### Scenario: Reader checks non-goals
- **WHEN** a reader checks what the repository is not
- **THEN** it states that the repository is not an official OpenAI project, not a Codex usage manual, not a link index, and not an implementation clone

### Requirement: Product-manager alignment
The repository SHALL explain the value of harness literacy in product-manager language.

#### Scenario: Product manager reads the document
- **WHEN** the target reader is an AI product manager
- **THEN** the document explains how loop, tools, permissions, context, sessions, and transport shape product trust, cost, latency, recoverability, and user control

#### Scenario: Platform designer reads the document
- **WHEN** the target reader is an agent platform designer
- **THEN** the document points to the mechanism layers and evidence boundaries needed for platform architecture decisions

### Requirement: Fact boundary recap
The repository SHALL recap fact boundaries wherever the project goal is summarized.

#### Scenario: Official source boundary is described
- **WHEN** the project goal document describes official facts
- **THEN** it repeats that official facts require fixed-SHA OpenAI source links, OpenAI official documentation, or explicit pending/teaching labels

#### Scenario: Teaching abstraction is described
- **WHEN** the project goal document describes mocks, diagrams, or desktop-lens material
- **THEN** it states that those artifacts are teaching aids and cannot prove OpenAI Codex implementation behavior
