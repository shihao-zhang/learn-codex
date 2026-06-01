## Why

P0-P3 已完成图形规范试点、fact snapshot 刷新评估、s08/s10 深核验和多轮提交。现在的风险不在于缺少内容，而在于 review 面太散：维护者需要同时理解哪些 change 已完成、哪些事实边界没有变化、哪些后续任务必须单独开 change。

P4 的目标是把当前分支整理成可 review 的开源维护状态：给出 PR/review summary、active OpenSpec change 清点、后续归档策略和下一步风险，不新增官方事实，不继续扩写章节。

## What Changes

- 新增 `prepare-open-source-review-closeout-p4` OpenSpec change。
- 新增 `docs/maintenance-closeout.md`，作为 P4 开源维护收口页。
- 更新 `docs/roadmap.md`，标记 P4 已完成并说明下一步只剩 review/归档/后续独立 change。
- 更新 `docs/review-checklist.md`，补充 PR / release closeout 的最小检查项。

## Capabilities

### New Capabilities

- `open-source-review-closeout`: 定义开源维护收口、PR summary、active OpenSpec change 清点和后续风险分流规则。

### Modified Capabilities

- `next-phase-roadmap`: 标记 P4 收口完成。
- `maintenance-review-workflow`: 增加 PR / release closeout 检查项。

## Impact

- 影响 `docs/maintenance-closeout.md`、`docs/roadmap.md`、`docs/review-checklist.md` 和本 OpenSpec change。
- 不新增 OpenAI 官方事实。
- 不修改 `docs/fact-snapshot.md` 的 target commit 或 release 核验值。
- 不修改 s08/s10 章节状态。
- 不归档 OpenSpec changes，不推送、不创建 PR、不调用外部 review。
