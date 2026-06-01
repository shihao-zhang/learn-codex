## Why

Phase 5 和 Phase 6 已经把证据索引、事实边界和前 6 章内容密度推进了一轮。接下来如果继续开放维护，风险不在于“没有内容可写”，而在于贡献者可能把章节状态、桌面端观察、Claude review、教学 mock 或源码 permalink 混成同一种事实。

Phase 9 的目标是把开源维护与 review 规则写成可执行的检查清单：贡献者在改章节、证据、事实快照或 mock 前，能知道什么时候必须走 OpenSpec、什么时候必须更新 `source-evidence.md`，什么时候必须先问人类授权。

## What Changes

- 新增 `docs/review-checklist.md`，集中说明维护与 review 规则。
- 明确章节状态升级、保留和降级标准。
- 明确 `docs/source-evidence.md` 与 `docs/fact-snapshot.md` 的更新触发条件和边界。
- 明确 Claude 等外部 review 的授权边界、默认副作用禁令和云端深度 review 的单独授权要求。
- 明确 Codex Desktop Lens 只能作为观察视角、源码阅读问题和教学启发。
- 明确教学 mock 的非官方、离线、确定性和标准库约束。
- 更新 `README.md` 与 `docs/roadmap.md` 的轻量导航，不改章节正文。

## Capabilities

### New Capabilities

- `maintenance-review-workflow`: 定义 Phase 9 维护、贡献、review、证据更新和提交前检查规则。

### Modified Capabilities

- 无。

## Impact

- 影响 `docs/review-checklist.md`、`README.md`、`docs/roadmap.md` 和本 OpenSpec change。
- 不修改章节正文，不改变任何章节状态。
- 不改变目标 commit、release 核验值或源码证据内容。
- 不调用外部 Claude review，不新增依赖，不调用 OpenAI API。
