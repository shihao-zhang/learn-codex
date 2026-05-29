## ADDED Requirements

### Requirement: Pending chapter verification plan
The repository SHALL define a verification plan for s08, s09, s10, and s11 before upgrading any of them from `待核实`.

#### Scenario: Pending chapter remains unresolved
- **WHEN** a pending chapter still has unresolved questions about behavior, capability semantics, or mainline CLI relevance
- **THEN** the chapter keeps the `待核实` status and lists the unresolved questions in its fact verification checklist

#### Scenario: Pending chapter is ready to upgrade
- **WHEN** the chapter's entry points, key types or functions, data flow, and production boundary are verified against fixed SHA source links
- **THEN** the chapter may be proposed for upgrade with evidence entries and a short rationale

### Requirement: s08 session thread rollout verification
The repository SHALL verify the relationship between session IDs, thread IDs, thread-store, rollout, and rollout truncation before treating s08 as an official mechanism chapter.

#### Scenario: Resume behavior is described
- **WHEN** s08 describes resume or persistence behavior
- **THEN** it cites fixed SHA evidence for the relevant session/thread identifiers, storage path, rollout path, and truncation behavior or labels the description as pending

### Requirement: s09 app-server transport verification
The repository SHALL verify app-server request, outgoing message, transport, and thread status boundaries before treating s09 as an official mechanism chapter.

#### Scenario: Protocol field behavior is described
- **WHEN** s09 describes protocol fields, request types, outgoing messages, or thread status semantics
- **THEN** it cites fixed SHA evidence for those exact constructs or keeps the claim marked as `待核实`

### Requirement: s10 extensions MCP skills verification
The repository SHALL verify MCP, extension tools, and skills boundaries without assuming that `skills` is a user-facing CLI first-class capability.

#### Scenario: Skills behavior is described
- **WHEN** s10 describes `skills` behavior
- **THEN** it distinguishes path existence from CLI capability semantics and cites fixed SHA evidence before making an official claim

### Requirement: s11 subagents parallel jobs verification
The repository SHALL verify whether agent jobs, delegation, and parallel execution are part of the open-source CLI harness mainline before presenting them as such.

#### Scenario: Parallel or delegated work is described
- **WHEN** s11 describes subagents, parallel jobs, or delegation as a Codex mechanism
- **THEN** it cites fixed SHA evidence for the calling path and runtime role or marks the description as pending/teaching abstraction
