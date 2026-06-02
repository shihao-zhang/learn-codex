# s10-extensions-mcp-skills-verification Specification

## Purpose
定义 Phase 5 对 s10 MCP、extensions 和 skills 语义的第一轮核验要求，防止把源码路径误写成完整产品能力。
## Requirements
### Requirement: s10 evidence remains source-bound
The repository SHALL record s10 official facts only when they are supported by fixed SHA OpenAI source permalinks, OpenAI official documentation, or OpenAI release notes.

#### Scenario: New s10 mechanism evidence is added
- **WHEN** `docs/source-evidence.md` adds or changes an s10 mechanism claim
- **THEN** the evidence entry cites a fixed SHA source link and states the verified scope and unresolved questions

### Requirement: s10 distinguishes mechanism evidence from user-visible capability
The repository SHALL distinguish path existence, internal mechanism evidence, and CLI user-visible capability semantics for MCP, extension tools, skills instructions, tool registry, and CLI entry points.

#### Scenario: Skills are described
- **WHEN** s10 describes `skills`, system skills, skill instructions, or skill discovery
- **THEN** it states whether the evidence proves an internal mechanism, a user-visible CLI capability, or a still-pending boundary

### Requirement: s10 avoids cross-product inference
The repository SHALL NOT use Claude Code skills, Codex desktop plugin experience, or other agent product behavior as proof of `openai/codex` CLI implementation facts.

#### Scenario: Similar product concepts are tempting
- **WHEN** s10 discusses skills, plugins, extensions, or MCP in product terms
- **THEN** it either ties the statement to registered official evidence or labels it as product framing, teaching abstraction, or pending

### Requirement: s10 status upgrade requires closed user-entry evidence
The repository SHALL keep s10 as `待核实` unless CLI entry, configuration, trigger rules, and runtime exposure are all verified against accepted official sources.

#### Scenario: Evidence remains partial
- **WHEN** the verified evidence only covers handlers, adapters, crate behavior, or session instruction construction
- **THEN** the chapter status remains `待核实` and the unresolved user-visible capability question stays explicit
