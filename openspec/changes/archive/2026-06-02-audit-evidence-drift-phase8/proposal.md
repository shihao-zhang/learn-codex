## Why

Phase 6 已完成 s01~s06 内容加厚，Phase 7 也已进入 integrated teaching mock 的设计阶段。此时最容易出现的风险不是缺少内容，而是证据漂移：固定 SHA 链接、章节状态、roadmap、summary 和章节 README 之间的事实边界可能逐渐不一致。

Phase 8 需要做一次轻量证据抽样复核，重点检查现有内容有没有把教学解释、Codex 桌面端观察、Claude review、mock trace 或其他 agent 产品经验误写成 `openai/codex` 官方事实。

## What Changes

- 新增 `audit-evidence-drift-phase8` OpenSpec change。
- 新增 `docs/phase8-evidence-audit.md`，记录抽样范围、无需修改项、已收窄项、仍待核实项和建议后续另开 change 的项。
- 抽样检查 README、docs、s01~s12 章节 README、`docs/source-evidence.md` 与 `docs/review-checklist.md`。
- 必要时小幅更新 README、roadmap、sourcing、source-evidence 或章节 README 的事实边界措辞。
- 不更新 `docs/fact-snapshot.md` 的目标 commit，不追最新 release，除非人类另行明确授权。
- 不启动或实现 integrated teaching mock。
- 不升级 s08/s10 状态。

## Capabilities

### New Capabilities

- `phase8-evidence-drift-audit`: 定义 Phase 8 证据漂移抽样复核的范围、边界、输出和验收检查。

### Modified Capabilities

- `maintenance-review-workflow`: 如审计发现维护者高频误区未覆盖，可小幅补强 `docs/review-checklist.md`。
- `source-evidence-traceability`: 如审计发现证据级别与章节状态之间容易误读，可小幅补充保守说明。

## Impact

- 影响 OpenSpec：新增 Phase 8 audit change。
- 影响文档：新增 `docs/phase8-evidence-audit.md`，并可能小幅修正边界措辞。
- 不影响 Python mock 代码、不新增依赖、不修改目标 commit、不更新 release 核验值。
- 不使用 Claude 或其他外部 review 服务，除非人类另行授权。
