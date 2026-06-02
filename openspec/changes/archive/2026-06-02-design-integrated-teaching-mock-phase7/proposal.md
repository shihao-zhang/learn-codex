## Why

Phase 6 已把 s01~s06 的单章教学密度补强，但读者仍需要一个端到端 mock 来看见这些机制如何组合：agent loop 如何推进，工具如何派发，权限如何改变执行路径，上下文压力如何影响继续执行，指令冲突如何被解释，会话 trace 如何帮助恢复，以及失败后如何把控制权还给人类。

现有 s12 已提供综合架构图和轻量 trace，但它更像总览，不足以承载 Phase 7 的 integrated teaching mock。Phase 7 先做设计，不实现代码，目的是先把边界、事件模型、场景矩阵和验收口径说清楚，防止后续 mock 被误读为 OpenAI Codex 复刻。

## What Changes

- 新增 `design-integrated-teaching-mock-phase7` OpenSpec change。
- 设计一个未来 integrated teaching mock，覆盖：
  - agent loop
  - tool dispatch
  - permission decision
  - context pressure
  - instruction conflict
  - session trace / recovery
  - failure recovery
- 明确未来实现必须保持 deterministic、offline、Python 标准库、Teaching mock only。
- 明确该 mock 不声称复刻 OpenAI Codex，不调用真实 OpenAI API，不调用真实外部服务，不依赖网络。
- 明确 Codex 桌面端体验只能作为教学问题来源，不能写成 `openai/codex` 官方事实。
- 明确引用 s08/s10 时必须标注其仍为 `待核实` 边界，不把恢复、rollout、extensions、MCP 或 skills 写成稳定官方产品承诺。
- 必要时更新 `docs/roadmap.md` 的 Phase 7 状态，只说明设计启动，不实现 mock。

## Capabilities

### New Capabilities

- `integrated-teaching-mock-phase7`: 定义 Phase 7 integrated teaching mock 的设计边界、覆盖面、trace contract、事实边界和验收检查。

### Modified Capabilities

- `next-phase-roadmap`: 可最小更新 Phase 7 状态，说明 integrated mock 已进入设计阶段，但代码实现仍未开始。

## Impact

- 影响 OpenSpec：新增 Phase 7 integrated mock 设计 change。
- 可能影响 `docs/roadmap.md`：只更新阶段状态，不新增官方事实。
- 不影响 Python mock 代码，不新增依赖，不修改 `scripts/run_all.py`，不修改测试。
- 不升级 s08/s10 状态，不修改 `docs/source-evidence.md`，除非后续实现阶段新增官方事实声明。
