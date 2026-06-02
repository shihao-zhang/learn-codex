## ADDED Requirements

### Requirement: Desktop lens boundary
The repository SHALL define Codex desktop experience as an observation lens, not as an official source of truth for `openai/codex`.

#### Scenario: Desktop observation is recorded
- **WHEN** a document uses Codex desktop experience to explain a question or teaching scenario
- **THEN** it labels the material as observation, product-design inspiration, or teaching prompt rather than official implementation fact

#### Scenario: Official fact is claimed
- **WHEN** a document claims a Codex implementation fact
- **THEN** the claim is sourced to fixed-SHA OpenAI code, OpenAI official documentation, or explicitly marked as pending/teaching abstraction

### Requirement: Observation-to-question mapping
The repository SHALL translate desktop experience into source-reading questions before using it in chapter work.

#### Scenario: Tool permission friction is observed
- **WHEN** a desktop experience reveals permission, sandbox, approval, or credential friction
- **THEN** the lens document maps that observation to specific source-reading questions for the relevant chapter

#### Scenario: Long-running agent behavior is observed
- **WHEN** a desktop experience reveals waiting, retry, interruption, review, or recovery behavior
- **THEN** the lens document maps that observation to harness topics such as sessions, trace, jobs, or failure recovery

### Requirement: Teaching use of desktop lens
The repository SHALL use desktop-lens material to improve reader questions, failure paths, and mock scenarios.

#### Scenario: Chapter is expanded using the lens
- **WHEN** a chapter uses desktop-lens material
- **THEN** it separates the product question from the official Codex source mapping

#### Scenario: Mock scenario is inspired by the lens
- **WHEN** a mock scenario is inspired by desktop experience
- **THEN** the mock keeps the existing non-official teaching disclaimer and does not imply equivalence with Codex desktop behavior
