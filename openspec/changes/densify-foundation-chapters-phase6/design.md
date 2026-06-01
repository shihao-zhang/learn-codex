## Context

本仓已经完成 12 章教学初版、机制级证据索引和 Phase 5 第一轮高风险章节核验。s01~s06 目前状态均为 `已核实官方事实`，但“已核实”只应理解为章节主机制有固定 SHA 证据支撑；它不意味着章节中的产品解释、教学比喻、mock trace 或所有失败分支都等同于 OpenAI 官方实现。

Phase 6 的工作对象是内容表达密度，而不是事实状态升级。要让前 6 章更适合人类 AI 产品经理阅读：先回答他们真正关心的问题，再解释机制如何影响产品体验、平台治理、失败恢复和边界承诺。

## Goals / Non-Goals

**Goals:**

- s01~s06 每章都新增或强化“PM 真正关心的问题”，用通俗问题把机制和产品决策连起来。
- s01~s06 每章至少补一个 failure path，说明失败触发条件、运行时应如何处理、用户体验风险是什么。
- s01~s06 每章说明 mock trace 的教学价值：它帮助读者看懂哪条控制流，但不能证明官方实现等价。
- 每章都保留或强化事实边界：官方事实只来自固定 SHA OpenAI 源码 permalink、OpenAI 官方文档或 release note；其他内容标为教学抽象、推断或待核实。
- 只在必要时更新统一证据索引，不为每章新增独立 `sources.md`。

**Non-Goals:**

- 不启动、设计或实现 integrated teaching mock。
- 不升级 s08/s10 状态，不把 Phase 5 尚未闭环的结论写成稳定官方事实。
- 不新增 OpenAI API 调用，不调用真实模型，不把 Python mock 写成 Codex 官方实现或等价复刻。
- 不把 Codex 桌面端观察直接写成 `openai/codex` 开源实现事实。
- 不改变目标 commit 或 release 快照。

## Decisions

1. 用“章节内小节”而不是新文档承载加厚内容。

   s01~s06 是读者最先进入的路径，把 PM 问题、failure path 和 mock trace 放在每章 README 内部，能降低跳转成本。统一证据仍放在 `docs/source-evidence.md`，避免 sources 文件漂移。

2. 每章都采用同一组表达模块，但允许篇幅随主题调整。

   推荐模块是：`PM 真正关心的问题`、`典型 failure path`、`mock trace 怎么读`、`边界措辞`。其中 `边界措辞` 可以并入“真实 Codex 映射”或“教学简化与生产差异”，但必须让读者知道哪些句子是教学解释。

3. failure path 优先服务产品理解，不伪装成已核实源码分支。

   如果 failure path 能追到固定 SHA 证据，可以写成机制事实；如果来自产品设计经验或桌面端观察，只能写成教学抽象、推断或源码阅读问题。

4. Phase 6 状态只说明本仓写作进展，不说明 OpenAI Codex 官方能力变化。

   `README.md` 和 `docs/roadmap.md` 可以写“Phase 6 内容加厚已推进/完成”，但不能暗示 s08/s10 已稳定，不能改变章节状态表。

## Risks / Trade-offs

- [Risk] 加厚内容容易把产品建议写成官方实现事实。缓解方式：每章显式保留边界措辞，新增源码断言必须登记到统一证据索引。
- [Risk] 六章同时加厚会让 README 变长。缓解方式：用短小节和列表表达，只补高信号内容。
- [Risk] failure path 可能与真实源码错误分支不完全一致。缓解方式：没有固定 SHA 证据时，称为“教学 failure path”或“平台设计问题”，不要写成官方行为。
- [Risk] mock trace 被误读为官方 trace。缓解方式：每章说明 mock trace 只帮助理解因果和状态，不代表官方 wire format、类型名或执行顺序。
