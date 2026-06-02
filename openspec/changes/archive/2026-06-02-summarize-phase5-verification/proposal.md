## Why

Phase 5 的两条事实核验 session 已经完成第一轮：s08 和 s10 都补强了机制级证据，但都选择继续保持 `待核实`。项目需要一个短的收口文档，把“已经核实了什么、为什么仍不升级、下一步为什么进入 Phase 6”说清楚，避免后续读者误以为 Phase 5 未执行，或误以为证据增加就等于状态升级。

## What Changes

- 新增 `docs/phase5-summary.md`，汇总 s08/s10 第一轮事实核验结果、仍未闭环的问题、保守状态判断和下一阶段建议。
- 更新 `README.md` 当前阶段：从“进入 Phase 5”调整为“Phase 5 第一轮核验已完成，下一步 Phase 6”。
- 更新 `docs/roadmap.md`：在 Phase 5 段落补充第一轮核验结论和进入 Phase 6 的前置条件。
- 不新增 OpenAI 源码事实，不改章节状态，不把 Codex 桌面端观察写成官方实现事实。

## Capabilities

### New Capabilities

- `phase5-verification-summary`: 定义 Phase 5 第一轮事实核验收口、保守状态判断和 Phase 6 入口说明。

### Modified Capabilities

- 无。

## Impact

- 影响 `README.md`、`docs/roadmap.md` 和新增 `docs/phase5-summary.md`。
- 影响 OpenSpec：新增本轮汇总 change。
- 不影响代码、不引入依赖、不改变事实快照目标 commit、不升级 s08/s10 状态。
