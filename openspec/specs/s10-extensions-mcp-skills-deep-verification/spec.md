# s10-extensions-mcp-skills-deep-verification Specification

## Purpose
定义 s10 skills/MCP/extensions 的深核验要求，继续区分源码存在、机制证据和用户可见产品能力边界。
## Requirements
### Requirement: s10 separates four capability paths
The repository SHALL describe MCP, dynamic tools, extension tools, and skills as separate capability paths unless a fixed SHA official source proves a shared official mechanism.

#### Scenario: s10 discusses extension-like capabilities
- **WHEN** `chapters/s10_extensions_mcp_skills/README.md` or `docs/source-evidence.md` describes s10 capabilities
- **THEN** it states which path is being described and avoids merging similarly named features into one official product concept

### Requirement: s10 records entry, discovery, configuration, exposure, and governance status
The repository SHALL record for each s10 capability path whether user entry, discovery, configuration, runtime exposure, and governance behavior are verified, partial, or pending.

#### Scenario: A mechanism is upgraded or kept pending
- **WHEN** an s10 evidence entry changes level or wording
- **THEN** the entry states the verified scope and the exact non-closed loop that prevents overclaiming

### Requirement: s10 official facts remain pinned to the current fact snapshot
The repository SHALL use the current fact snapshot target commit as the official source baseline for this change.

#### Scenario: New source evidence is added
- **WHEN** `docs/source-evidence.md` adds or changes s10 OpenAI source evidence
- **THEN** every source permalink uses commit `740d942f901a5a63421298c74dafbeb4255e946d`

### Requirement: s10 status upgrade requires closed capability boundaries
The repository SHALL keep s10 as `待核实` unless all four capability paths have separately verified entry, discovery/configuration, runtime exposure, and governance semantics.

#### Scenario: A path remains partial
- **WHEN** extension tools user entry, dynamic tool client-side origin, MCP lifecycle/governance, or skills cross-client semantics remain partial
- **THEN** the chapter status stays `待核实` and the unresolved reason is visible to readers
