## Context

`learn-codex` 当前已经完成 12 章教学初版，并通过 Phase 3~4 建立了统一证据索引、固定 SHA 检查和部分章节状态升级。当前短板不再是“有没有目录和 mock”，而是后续如何持续提高内容密度，同时不把桌面端体验、教学抽象或社区理解误写成 `openai/codex` 官方实现。

本 change 面向两类读者和贡献者：AI 产品经理需要重新理解 agent 产品的 runtime 基础，agent 平台设计者需要看到 loop、tools、permissions、context、sessions、transport、extensions、parallel jobs 如何组合成 harness。Codex 桌面端体验可以提供优秀的问题来源，但它不是公开 Rust CLI 源码的事实依据。

## Goals / Non-Goals

**Goals:**

- 形成 Phase 5 以后的后续计划，明确优先级、产出物和验收口径。
- 把 Codex 桌面端观察纳入项目方法论，但只作为源码阅读问题和产品设计启发。
- 重新对齐项目目标：本仓是 agent harness 教学仓，不是 Codex 使用手册、资料索引或官方实现复刻。
- 为后续实现阶段提供可检查的文档结构、状态边界和 review 标准。

**Non-Goals:**

- 不在本 change 中直接补写各章正文或实现 integrated mock。
- 不升级 s08/s10 状态，不改变当前事实快照目标 commit。
- 不把桌面端、Claude review、社区文章或教学 mock 作为官方事实来源。
- 不引入新依赖、不调用 OpenAI API、不改变 Python mock 标准库约束。

## Decisions

1. 后续计划采用阶段式路线，而不是一次性大改。

   - Phase 5 聚焦 s08/s10 待核实链路，因为它们决定事实可信上限。
   - Phase 6 提升前 6 章内容密度，因为它们是读者理解 harness 的入口。
   - Phase 7 设计端到端 integrated teaching mock，把分散机制串成平台体验。
   - Phase 8 做证据抽样复核，防止源码解释漂移。
   - Phase 9 补开源维护与贡献流程。
   - 备选方案是直接逐章重写；缺点是优先级不清，容易在低风险章节消耗太多精力。

2. 新增 Codex Desktop Lens，但将它定位为“问题生成器”。

   - 可记录桌面端观察，例如沙箱拒绝、外部 review 卡住、GitHub 凭据边界、长任务状态。
   - 每条观察必须转成源码问题或教学场景，不能直接写成官方 Codex 实现。
   - 备选方案是完全不用桌面端经验；缺点是会损失真实 agent 平台里的 failure path 和产品摩擦。

3. 项目目标单独成文，面向人类产品经理重新对齐。

   - README 继续承担学习地图。
   - 新文档负责讲清本仓要帮助读者建立什么判断力、哪些内容不是目标。
   - 备选方案是把目标散落在 README 和章节里；缺点是贡献者容易把仓库写成工具教程或资料索引。

4. 后续计划先以文档合同和 checklist 落地，再进入实现。

   - 本 change 只定义路线和验收口径。
   - 后续 apply 阶段再新增 `docs/roadmap.md`、`docs/codex-desktop-lens.md` 和目标对齐文档。
   - 这样能先稳定“写什么、按什么验收”，再开始填内容。

## Risks / Trade-offs

- [Risk] 桌面端观察被读者误解为官方实现事实 → 在 lens 文档、README 和相关章节中显式标注“观察视角，不是事实来源”。
- [Risk] 路线图过大导致执行发散 → 每个 phase 必须有明确产出物、验收项和停止条件。
- [Risk] s08/s10 深挖后仍不能升级 → 接受保持 `待核实`，并把“不能升级的原因”写成高质量教学内容。
- [Risk] 面向 PM 的表达变得过技术化 → 每份新增计划文档都要先给产品意义，再给源码/检查项。
- [Risk] integrated mock 被误读为 Codex 复刻 → 沿用现有 mock 免责声明，并在测试中保护结构化免责声明。
