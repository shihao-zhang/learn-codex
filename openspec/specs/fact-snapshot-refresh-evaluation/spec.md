# fact-snapshot-refresh-evaluation Specification

## Purpose
定义 fact snapshot 追新评估的保守流程：先评估候选 commit/release，再决定是否另开迁移工作。
## Requirements
### Requirement: OpenSpec-first snapshot evaluation

仓库 SHALL start target commit or release refresh work with an OpenSpec change before changing `docs/fact-snapshot.md`.

#### Scenario: Snapshot refresh work starts

- **WHEN** a maintainer evaluates whether to update the target commit or release verification value
- **THEN** the repository contains a change with `proposal.md`, `design.md`, `tasks.md`, and `specs/.../spec.md`

### Requirement: Official-source-only refresh evidence

仓库 SHALL use only accepted official sources for target commit, release, and source path verification.

#### Scenario: Commit is evaluated

- **WHEN** the target commit is considered for update
- **THEN** the candidate commit is obtained from the official `openai/codex` GitHub repository and recorded as a full commit SHA

#### Scenario: Release value is evaluated

- **WHEN** the release verification value is considered for update
- **THEN** the candidate release tag and release name come from official `openai/codex` GitHub Releases

#### Scenario: Source paths are checked

- **WHEN** existing snapshot source paths are migrated to a candidate commit
- **THEN** each path is checked using a fixed SHA permalink or GitHub Contents API result, not a moving branch ref

### Requirement: Target commit migration synchronization

仓库 SHALL synchronize all fixed OpenAI source links and the docs checker when the target commit changes.

#### Scenario: Target commit changes

- **WHEN** `docs/fact-snapshot.md` target commit is changed
- **THEN** `scripts/check_docs.py` updates `SOURCE_COMMIT`, all `github.com/openai/codex/(blob|tree)/...` source links use the new commit, and old commit links are removed or explicitly justified outside official-source evidence

#### Scenario: Target commit is preserved

- **WHEN** the evaluation decides not to change the target commit
- **THEN** the change records the reason and does not modify the fixed SHA link set

### Requirement: Conservative high-risk chapter status

仓库 SHALL keep s08 and s10 status changes separate from snapshot refresh.

#### Scenario: s08 path links still resolve

- **WHEN** s08 paths are reachable at a newer target commit
- **THEN** s08 remains `待核实` unless a separate mechanism or behavior verification closes the unresolved session/thread/rollout chain

#### Scenario: s10 path links still resolve

- **WHEN** s10 paths are reachable at a newer target commit
- **THEN** s10 remains `待核实` unless a separate mechanism or behavior verification closes the unresolved extension/MCP/skills chain

### Requirement: No non-official fact contamination

仓库 SHALL NOT mix diagram redraw, teaching mock, Codex Desktop observation, community material, or external review output into target snapshot facts.

#### Scenario: Snapshot facts are updated

- **WHEN** `docs/fact-snapshot.md` is changed
- **THEN** new official facts are limited to fixed SHA OpenAI source permalinks, OpenAI official documentation, or OpenAI release notes

### Requirement: Snapshot refresh validation

仓库 SHALL pass repository validation before the snapshot refresh evaluation is considered ready.

#### Scenario: Change is ready for review

- **WHEN** the evaluation and any necessary snapshot/link/script updates are complete
- **THEN** the maintainer runs `openspec validate evaluate-fact-snapshot-refresh-phase10 --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`
