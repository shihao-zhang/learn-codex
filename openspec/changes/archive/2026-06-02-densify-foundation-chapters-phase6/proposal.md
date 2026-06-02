## Why

Phase 5 第一轮已经把 s08/s10 的高风险事实边界收住：证据密度提升，但章节继续保持 `待核实`。下一步最有价值的工作不是继续扩张新主题，而是把读者最先进入的 s01~s06 加厚，让 AI 产品经理和 agent 平台设计者更快看懂 agent harness 的核心机制、失败路径和教学 mock 的用途。

当前前 6 章已有机制框架和源码证据入口，但部分章节仍偏“概念说明”：PM 真正会追问的问题、failure path、mock trace 如何帮助理解、以及“不扩大事实边界”的措辞还可以更明确。Phase 6 的目标是提升教学密度，而不是新增未经核验的官方事实。

## What Changes

- 为 s01~s06 每章补强四类内容：
  - 产品经理真正关心的问题。
  - 至少一个 failure path。
  - mock trace 如何帮助理解机制。
  - 不扩大事实边界的措辞。
- 必要时只在 `docs/source-evidence.md` 中补登记已有固定 SHA 证据；不新增无证据的官方事实。
- 更新 `README.md` 或 `docs/roadmap.md` 的 Phase 6 状态，让读者知道本轮正在推进或已完成。
- 不升级 s08/s10 状态，不把 Phase 5 待核实结论写成稳定官方事实。
- 不启动 integrated teaching mock；如发现需要端到端 mock，只记录为后续 Phase 7 问题。

## Capabilities

### New Capabilities

- `foundation-chapter-density`: 定义 s01~s06 的内容加厚要求、事实边界和验收检查。

### Modified Capabilities

- 无。

## Impact

- 影响 s01~s06 的章节 README。
- 影响 `README.md` 或 `docs/roadmap.md` 的 Phase 6 状态说明。
- 可能影响 `docs/source-evidence.md`，但仅限登记已有固定 SHA 证据或澄清证据边界。
- 不影响 Python mock 行为，不新增依赖，不调用 OpenAI API，不改变目标 commit，不改变 s08/s10 状态。
