# s05_context_window_compaction

## 状态标签

状态：已核实官方事实

## 本章回答什么

本章解释一个长任务为什么会“越聊越难”：模型每次只能看到有限的输入窗口，agent harness 必须在历史记录、工具输出、用户约束和当前任务之间做取舍。核心问题不是“能不能无限记忆”，而是“在预算有限时，哪些信息必须保真，哪些信息可以摘要，哪些信息可以丢弃”。

对产品经理来说，上下文窗口是长任务体验的底层约束；对平台设计者来说，compaction 是把历史压成可继续工作的状态，truncation 是在必要时直接减少可见信息。两者都能让任务继续，但代价不同：压缩可能损失细节，截断可能直接让模型看不到某些事实。

## 对产品与平台设计的意义

上下文管理同时影响成本、延迟、可靠性和用户信任。窗口越大，单轮请求通常越贵、越慢；窗口越紧，越容易发生“忘了刚才的约束”“重复问已经回答过的问题”“误用旧工具输出”等体验问题。

好的 agent 产品不应把 compaction 包装成无损记忆。更稳妥的设计是把长任务拆成可恢复的工作单元，并在摘要中优先保留：用户目标、不可违反的约束、已经做过的关键决策、当前文件/分支/环境状态、失败原因、待确认问题和下一步计划。平台侧则需要给摘要质量、触发时机和失败恢复留出观测点，否则用户只会看到“agent 突然变笨了”。

## 机制图

见 [diagram.mmd](diagram.mmd)。该图是教学抽象，用来说明上下文压力下的选择路径，不是 OpenAI 官方架构图。

## 运行 mock

```bash
python3 chapters/s05_context_window_compaction/mock.py --demo
```

这个 mock 只演示“测量预算 -> 决定继续/压缩/截断 -> 形成下一轮输入”的控制流。它不是真实 Codex 实现，也不代表真实摘要策略、token 计数方式或模型输入格式。

## 核心机制

- `context window`：模型单轮可见的信息上限。它不是长期记忆，只是下一次推理时能被放进输入里的工作台。
- `context pressure`：历史消息、工具观察、文件片段和指令逐渐挤占窗口时产生的压力。压力不是等到溢出才出现，接近预算时就会影响选择。
- `compaction`：把较早的交互压成摘要，让后续轮次仍能保留任务脉络。它适合保留“为什么这么做”和“现在做到哪里”，但不适合承诺逐字保真。
- `truncation`：直接移除部分低价值或过旧内容。它更简单，也更危险；一旦被截掉的信息后来变重要，agent 只能依赖用户、文件系统或工具重新取证。
- `working set`：当前轮最该保真的信息集合，通常包括最新用户意图、当前错误、最近工具输出、待编辑文件和明确约束。

## 真实 Codex 映射

- [codex-rs/core/src/compact.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact.rs)
- [codex-rs/core/src/compact_remote.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact_remote.rs)
- [codex-rs/core/src/compact_remote_v2.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact_remote_v2.rs)

以上固定 SHA 链接是本章的官方事实入口：它们说明当前教学对象中存在 compaction 相关源码。README 中的机制解释用于教学，不把 Python mock 或 Mermaid 图声明为官方实现。

## 教学简化与生产差异

教学版把上下文管理压成三步：测量、压缩、截断。生产系统通常还要处理更多问题：不同模型的窗口上限不同，工具输出可能很长，文件内容可能需要重新读取，摘要本身也会占用 token，且摘要质量会受模型、提示词和历史结构影响。

本章刻意不把 rollout 解释为 compaction；rollout、thread store 和 resume 归入 s08。二者容易混淆：compaction 解决“下一轮模型看什么”，rollout/resume 更接近“历史如何保存与恢复”。这个边界在产品设计上很重要，因为“省 token”和“可恢复”不是同一个承诺。

## 练习

1. 运行 mock，比较 happy path 和 failure path 中哪些信息被保留、哪些信息被压缩。
2. 设计一个 30 分钟长任务的“必须保真字段”清单，例如目标、约束、已改文件、失败命令和下一步。
3. 写一条用户可见的状态文案，提示“正在整理上下文以继续任务”，要求既不吓人，也不暗示无损记忆。
4. 反向思考一个失败案例：如果摘要漏掉“未经授权不得调用外部 review”，后续 agent 可能做出什么错误动作？

## 事实核验清单

- [ ] 逐文件核实 compact、remote compact 与 v2 compact 的职责边界。
- [ ] 核实 compaction 与 truncation 的真实触发条件，避免把教学 mock 的阈值写成官方行为。
- [ ] 明确 compaction 与 rollout 的边界；rollout 相关路径在 s08 仍按待核实处理。
