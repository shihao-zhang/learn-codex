## Why

当前 `docs/fact-snapshot.md` 固定在 2026-05-29 的 `openai/codex` 快照，并记录了当时的 GitHub release 核验值。这个快照是全仓官方事实的锚点：章节 README、`docs/source-evidence.md` 和 `scripts/check_docs.py` 都依赖同一个固定 commit。

Phase 10 的目标不是“自动追新”，而是做一次受控评估：确认是否需要刷新目标 commit 和 release 核验值；如果刷新，则同步迁移所有 OpenAI 源码 permalink 和校验脚本；如果不刷新，则记录保守理由。

## What Changes

- 新增 OpenSpec change，定义 fact snapshot 刷新评估的决策边界。
- 使用官方来源核验 `openai/codex` 默认分支 commit、GitHub release 核验值和目标路径可访问性。
- 如决定更新目标 commit：
  - 更新 `docs/fact-snapshot.md` 的核验日期、目标 commit、release 核验值和所有固定 SHA 源码链接。
  - 更新 `scripts/check_docs.py` 中的 `SOURCE_COMMIT`。
  - 检查仓库内所有 `github.com/openai/codex/(blob|tree)/...` 链接，确保没有旧 SHA 或 moving ref。
- 明确 s08 和 s10 不因 commit 刷新自动升级；只有单独完成机制级或行为级核验后才可调整状态。
- 不引入 diagram redraw、教学 mock 或 Codex Desktop 观察作为官方事实。

## Capabilities

### New Capabilities

- `fact-snapshot-refresh-evaluation`: 定义目标 commit / release 核验值的刷新评估、同步迁移和验证规则。

### Modified Capabilities

- 无。是否修改 `docs/fact-snapshot.md` 取决于本 change 的官方来源核验结果。

## Impact

- 影响本 OpenSpec change。
- 可能影响 `docs/fact-snapshot.md`、`scripts/check_docs.py` 以及包含固定 SHA OpenAI 源码 permalink 的 Markdown / Mermaid / Python 文件。
- 不修改章节状态。
- 不调用 Claude 或其他外部 review 服务。
- 不混入 diagram redraw、教学 mock 或 Codex Desktop 观察。
