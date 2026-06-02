# review-scope-clarifications Specification

## Purpose
记录 PR review 后的 scope 澄清，确保合并前修正只收窄审稿歧义，不新增官方事实或改变章节状态。
## Requirements
### Requirement: S11 status scope is visible at reader entry

The repository SHALL keep s11's mechanism-level status visible without implying product-level guarantees.

#### Scenario: Reader sees README learning map

- **WHEN** the README learning map lists s11 as `已核实官方事实`
- **THEN** the same row also states that this status is limited to registered source mechanisms
- **AND** it states that product entry, default enablement, and v1/v2 experience boundaries remain to be verified

### Requirement: S11 chapter boundary remains explicit

The s11 chapter SHALL distinguish verified source mechanisms from unresolved product semantics.

#### Scenario: Reader opens s11 README

- **WHEN** the status label is explained
- **THEN** the explanation includes source mechanisms as the verified scope
- **AND** it excludes default availability, product commitments, and multi-agent v1/v2 experience semantics

### Requirement: Audit counts are time-bounded

Evidence audit documents SHALL avoid presenting point-in-time counts as permanent current facts.

#### Scenario: Phase 8 audit mentions permalink count

- **WHEN** the audit states the number of fixed SHA links inspected
- **THEN** the wording marks that number as an audit-time count
