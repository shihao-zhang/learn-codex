# phase8-evidence-drift-audit Specification

## Purpose
定义 Phase 8 证据漂移抽样复核要求，防止固定 SHA、章节状态和教学内容随外部变化被误扩写。
## Requirements
### Requirement: Phase 8 audit change

Phase 8 SHALL start with an OpenSpec change before documentation edits that affect evidence boundaries.

#### Scenario: Audit change is created

- **WHEN** Phase 8 evidence drift work starts
- **THEN** the repository contains `proposal.md`, `design.md`, `tasks.md`, and `specs/.../spec.md` for `audit-evidence-drift-phase8`

### Requirement: Fixed snapshot preservation

The audit SHALL preserve the current fact snapshot unless the human explicitly authorizes a target update.

#### Scenario: Fixed SHA links are checked

- **WHEN** OpenAI source links are sampled
- **THEN** `blob` and `tree` permalinks point to `740d942f901a5a63421298c74dafbeb4255e946d`

#### Scenario: Moving references are found

- **WHEN** a moving reference such as `main`, `master`, `latest`, or a newly discovered release tag is needed for an official fact claim
- **THEN** the change records it as a follow-up or asks for authorization instead of silently updating the fact snapshot

### Requirement: Conservative chapter status

The audit SHALL preserve conservative chapter states unless evidence and review explicitly justify a future status change.

#### Scenario: s08 is reviewed

- **WHEN** s08 sessions/threads/rollout documentation is sampled
- **THEN** README, roadmap, Phase 5 summary, source evidence, and chapter README keep s08 as `待核实`

#### Scenario: s10 is reviewed

- **WHEN** s10 extensions/MCP/skills documentation is sampled
- **THEN** README, roadmap, Phase 5 summary, source evidence, and chapter README keep s10 as `待核实`

#### Scenario: Phase 6 additions are reviewed

- **WHEN** s01~s06 PM questions, failure paths, or mock trace explanations are sampled
- **THEN** they are labeled as teaching explanation, product judgment, `教学抽象`, `推断`, or equivalent conservative wording when they are not official source facts

### Requirement: Audit summary

The repository SHALL record Phase 8 findings in a lightweight audit document.

#### Scenario: Audit summary is created

- **WHEN** the audit completes
- **THEN** `docs/phase8-evidence-audit.md` lists audit scope, no-change items, narrowed items, still-pending items, and suggested follow-up changes

### Requirement: Maintainer-error coverage

The audit SHALL check the review checklist against likely future mistakes.

#### Scenario: Checklist is reviewed

- **WHEN** `docs/review-checklist.md` is sampled
- **THEN** it covers at least moving refs, target commit updates, status upgrades, teaching mock boundaries, desktop-observation boundaries, source evidence updates, and external review authorization

### Requirement: Phase 8 validation

The audit SHALL pass repository validation before being marked complete.

#### Scenario: Change is ready for review

- **WHEN** Phase 8 audit files and necessary wording fixes are complete
- **THEN** the maintainer runs `openspec validate audit-evidence-drift-phase8 --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`
