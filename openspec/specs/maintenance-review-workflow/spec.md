# maintenance-review-workflow Specification

## Purpose
定义长期维护 review 工作流，覆盖章节状态、证据、fact snapshot、外部 review 授权、Codex Desktop Lens 和提交前检查。
## Requirements
### Requirement: 章节状态维护标准

仓库 SHALL define review standards for upgrading, retaining, and downgrading chapter status labels.

#### Scenario: 章节升级为已核实官方事实

- **WHEN** a maintainer upgrades a chapter to `已核实官方事实`
- **THEN** the chapter has at least one `mechanism-verified` or `behavior-verified` row in `docs/source-evidence.md`, every primary fixed-SHA source link in the chapter is traceable through `docs/fact-snapshot.md` or `docs/source-evidence.md`, and `README.md` status matches the chapter README status

#### Scenario: 章节保持待核实

- **WHEN** only path existence is known, an API is experimental, a product entry point is unclear, or an end-to-end mechanism chain is not closed
- **THEN** the chapter remains `待核实`, and the unresolved chain is recorded in `docs/source-evidence.md` or the chapter fact checklist

#### Scenario: 章节降级

- **WHEN** existing wording becomes broader than the evidence, the fixed snapshot becomes stale, or a previously assumed mechanism boundary is no longer supported
- **THEN** the maintainer downgrades the chapter status or narrows the wording, updates the evidence record, and explains the reason in the review summary

### Requirement: Source evidence maintenance

仓库 SHALL keep mechanism-level official facts in the unified `docs/source-evidence.md` index.

#### Scenario: 新增或修改官方机制事实

- **WHEN** a change adds, removes, or changes an official `openai/codex` mechanism claim
- **THEN** `docs/source-evidence.md` is updated with chapter, mechanism point, evidence level, fixed-SHA source link, verified scope, and unresolved question

#### Scenario: 纯导航或措辞修改

- **WHEN** a change only updates navigation, wording, typo fixes, or other text that does not alter official fact claims
- **THEN** `docs/source-evidence.md` does not need a new evidence row, and the review summary states that no evidence boundary changed when relevant

#### Scenario: 证据级别不等于章节状态

- **WHEN** an evidence row is upgraded from `path-exists` to `mechanism-verified` or `behavior-verified`
- **THEN** the chapter status is reviewed separately and is not automatically upgraded

### Requirement: Fact snapshot maintenance

仓库 SHALL update `docs/fact-snapshot.md` only when the target fact snapshot changes.

#### Scenario: 目标快照变化

- **WHEN** the target commit, release value, verification date, main source path list, or easy-expiring boundary changes
- **THEN** `docs/fact-snapshot.md` is updated, affected links and evidence are reviewed, and `scripts/check_docs.py` is updated if the pinned commit changes

#### Scenario: 行级机制证据补充

- **WHEN** a maintainer only adds row-level mechanism evidence against the existing snapshot
- **THEN** the maintainer updates `docs/source-evidence.md` instead of changing `docs/fact-snapshot.md`

### Requirement: Claude review authorization boundary

仓库 SHALL require explicit human authorization before sending private or unpublished materials to Claude or another external review service.

#### Scenario: External review is requested

- **WHEN** a maintainer wants to call Claude or another external service to review internal docs, code, diffs, or plans
- **THEN** the maintainer pauses, explains the sending scope, call method, likely cost, privacy impact, and side effects, then waits for explicit human authorization

#### Scenario: Side-effectful review options

- **WHEN** a review tool can modify the worktree, publish comments, push commits, or call cloud multi-agent / ultra review
- **THEN** the maintainer obtains separate explicit authorization before using those options

#### Scenario: Authorized review defaults

- **WHEN** human authorization is granted for external review
- **THEN** code review uses the approved local Claude Code review profile, and documentation, planning, or strategy review uses a document-specific prompt rather than code-review-only commands

### Requirement: Codex Desktop Lens boundary

仓库 SHALL use Codex Desktop Lens as an observation-to-question method, not as an official source of truth.

#### Scenario: Desktop observation informs writing

- **WHEN** a desktop experience informs a chapter, checklist, or mock scenario
- **THEN** the material is labeled as observation, product-design inspiration, source-reading question, teaching abstraction, or inference rather than official `openai/codex` fact

#### Scenario: Official implementation fact is claimed

- **WHEN** the text claims an official `openai/codex` implementation fact
- **THEN** the claim is supported by fixed-SHA OpenAI source, OpenAI official documentation, or release note; otherwise it is narrowed or marked `待核实`, `教学抽象`, or `推断`

### Requirement: Teaching mock disclaimer

仓库 SHALL keep Python mocks as non-official teaching tools.

#### Scenario: Mock is created or updated

- **WHEN** a teaching mock is added or changed
- **THEN** it remains deterministic, offline, standard-library first, and does not claim to reproduce OpenAI Codex, Codex Desktop, or production behavior

#### Scenario: Mock borrows a failure path

- **WHEN** a mock scenario is inspired by desktop observation, external review friction, permission denial, or credential boundaries
- **THEN** the mock labels the scenario as teaching material and does not use it as evidence for official implementation behavior

### Requirement: Pre-submit review checklist

仓库 SHALL require validation commands and a human-readable review summary before a maintenance change is considered ready.

#### Scenario: Change is ready for review

- **WHEN** Phase 9 or a later maintenance change is ready for review
- **THEN** the maintainer runs the relevant `openspec validate <change> --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`, or explicitly reports any skipped check and reason

#### Scenario: Review summary is written

- **WHEN** the maintainer summarizes the change
- **THEN** the summary states changed files, fact-boundary impact, chapter status impact, evidence/snapshot impact, external review usage, and validation results
