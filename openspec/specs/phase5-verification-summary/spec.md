# phase5-verification-summary Specification

## Purpose
定义 Phase 5 核验总结要求，确保 s08/s10 的新增证据、保守结论、章节状态决策和剩余缺口都能被后续维护者追踪，并防止核验进展被误写成官方事实升级。
## Requirements
### Requirement: Phase 5 summary document
The repository SHALL provide a short Phase 5 summary after the s08 and s10 verification sessions complete.

#### Scenario: Summary is created
- **WHEN** Phase 5 first-pass verification is closed
- **THEN** the repository contains a summary document that lists s08 and s10 verified scope, remaining open questions, status decision, and next-phase recommendation

### Requirement: Conservative status preservation
The summary SHALL distinguish verification progress from chapter status upgrades.

#### Scenario: s08 remains pending
- **WHEN** s08 has stronger app-server, thread-store, rollout, and exec resume evidence but product/client boundaries remain open
- **THEN** the summary keeps s08 as `待核实` and explains why this is a conservative quality decision

#### Scenario: s10 remains pending
- **WHEN** s10 has stronger MCP, dynamic tools, extension adapter, and skills evidence but extension entry or unified governance remains open
- **THEN** the summary keeps s10 as `待核实` and explains why this is a conservative quality decision

### Requirement: Phase 6 entry
The summary SHALL identify Phase 6 as the next recommended work only after preserving Phase 5 boundaries.

#### Scenario: Next work is selected
- **WHEN** a reader asks what to do after Phase 5 first-pass verification
- **THEN** the repository points to Phase 6 content-density work for s01~s06 and warns not to reuse s08/s10 as stable product claims
