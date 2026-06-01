# s05_context_window_compaction

## 状态标签

状态：已核实官方事实

## 本章回答什么

本章解释一个长任务为什么会“越聊越难”：模型每次只能看到有限的输入窗口，agent harness 必须在历史记录、工具输出、用户约束和当前任务之间做取舍。核心问题不是“能不能无限记忆”，而是“在预算有限时，哪些信息必须保真，哪些信息可以摘要，哪些信息可以丢弃”。

对产品经理来说，上下文窗口是长任务体验的底层约束；对平台设计者来说，compaction 是把历史压成可继续工作的状态，truncation 是在必要时直接减少可见信息。两者都能让任务继续，但代价不同：压缩可能损失细节，截断可能直接让模型看不到某些事实。

## 对产品与平台设计的意义

上下文管理同时影响成本、延迟、可靠性和用户信任。窗口越大，单轮请求通常越贵、越慢；窗口越紧，越容易发生“忘了刚才的约束”“重复问已经回答过的问题”“误用旧工具输出”等体验问题。

好的 agent 产品不应把 compaction 包装成无损记忆。更稳妥的设计是把长任务拆成可恢复的工作单元，并在摘要中优先保留：用户目标、不可违反的约束、已经做过的关键决策、当前文件/分支/环境状态、失败原因、待确认问题和下一步计划。平台侧则需要给摘要质量、触发时机和失败恢复留出观测点，否则用户只会看到“agent 突然变笨了”。

## PM 真正关心的问题

- 用户为什么觉得 agent “忘了”？很多时候不是模型态度问题，而是上下文预算迫使系统摘要、截断或重新取证。
- 哪些信息绝对不能丢？安全约束、用户明确偏好、当前任务目标、已做决策和失败原因，通常比早期寒暄或完整日志更重要。
- 要不要告诉用户正在整理上下文？透明能建立信任，但不能暗示“我们有无损长期记忆”；更好的文案是说明为了继续任务正在压缩历史，并保留关键约束。

## 机制图

见 [diagram.mmd](diagram.mmd)。该图是教学抽象，用来说明上下文压力下的选择路径，不是 OpenAI 官方架构图。

## 运行 mock

```bash
python3 chapters/s05_context_window_compaction/mock.py --demo
```

这个 mock 只演示“测量预算 -> 决定继续/压缩/截断 -> 形成下一轮输入”的控制流。它不是真实 Codex 实现，也不代表真实摘要策略、token 计数方式或模型输入格式。

## mock trace 怎么读

运行 failure trace：

```bash
python3 chapters/s05_context_window_compaction/mock.py --demo --path failure --trace-json
```

trace 展示 `measure -> compact -> truncate -> model_input` 的教学链路。重点不是 `10000` 这个阈值，而是决策含义：系统先发现 context pressure，再把旧 turns 摘要，必要时移除非关键细节，最后把 compacted context 交给模型。所有 token 数字、阈值和保留字段都只是教学参数。

## 核心机制

- `context window`：模型单轮可见的信息上限。它不是长期记忆，只是下一次推理时能被放进输入里的工作台。
- `context pressure`：历史消息、工具观察、文件片段和指令逐渐挤占窗口时产生的压力。压力不是等到溢出才出现，接近预算时就会影响选择。
- `compaction`：把较早的交互压成摘要，让后续轮次仍能保留任务脉络。它适合保留“为什么这么做”和“现在做到哪里”，但不适合承诺逐字保真。
- `truncation`：直接移除部分低价值或过旧内容。它更简单，也更危险；一旦被截掉的信息后来变重要，agent 只能依赖用户、文件系统或工具重新取证。
- `working set`：当前轮最该保真的信息集合，通常包括最新用户意图、当前错误、最近工具输出、待编辑文件和明确约束。

## 典型 failure path

教学 failure path：长任务中历史超过预算，系统进行 compaction，但摘要漏掉了“未经授权不得调用外部 review”。后续 agent 可能错误地把外部 review 当成可用动作。这个失败不是单纯的 token 问题，而是治理约束丢失问题。

产品上应把安全约束、授权状态和当前阻塞点列为高保真信息；平台上应保留摘要生成、历史替换和后续恢复的可观测线索。这个例子是教学抽象，不声明官方 compact prompt 一定以同样字段保留信息。

## 真实 Codex 映射

- [codex-rs/core/src/compact.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact.rs)
- [codex-rs/core/src/compact_remote.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact_remote.rs)
- [codex-rs/core/src/compact_remote_v2.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact_remote_v2.rs)

以上固定 SHA 链接是本章的官方事实入口：它们说明当前教学对象中存在 compaction 相关源码。README 中的机制解释用于教学，不把 Python mock 或 Mermaid 图声明为官方实现。

机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)，包括 compact task 入口、compact 后历史替换与 rollout 记录、以及 thread rollout truncation helper。

本章新增的 PM 问题、failure path 和 mock trace 解读只说明上下文管理的产品风险；真实 compact 触发条件、摘要提示词、remote/v2 字段职责和 token 策略仍以固定 SHA 证据为准。

## 教学简化与生产差异

教学版把上下文管理压成三步：测量、压缩、截断。生产系统通常还要处理更多问题：不同模型的窗口上限不同，工具输出可能很长，文件内容可能需要重新读取，摘要本身也会占用 token，且摘要质量会受模型、提示词和历史结构影响。

本章刻意不把 rollout 解释为 compaction；rollout、thread store 和 resume 归入 s08。二者容易混淆：compaction 解决“下一轮模型看什么”，rollout/resume 更接近“历史如何保存与恢复”。这个边界在产品设计上很重要，因为“省 token”和“可恢复”不是同一个承诺。

## 练习

1. 运行 mock，比较 happy path 和 failure path 中哪些信息被保留、哪些信息被压缩。
2. 设计一个 30 分钟长任务的“必须保真字段”清单，例如目标、约束、已改文件、失败命令和下一步。
3. 写一条用户可见的状态文案，提示“正在整理上下文以继续任务”，要求既不吓人，也不暗示无损记忆。
4. 反向思考一个失败案例：如果摘要漏掉“未经授权不得调用外部 review”，后续 agent 可能做出什么错误动作？

## 事实核验清单

- [x] 核实 `compact.rs` 中 compact task 的主入口和 inline/remote 选择入口。
- [x] 核实 compact 后会替换历史、写入 `Compacted` / `TurnContext` rollout item，并推进窗口 generation。
- [x] 核实 `thread_rollout_truncation.rs` 中按 user turn / fork turn 截断 rollout 的 helper。
- [ ] 继续核实 remote compact 与 v2 compact 的字段级职责边界。
- [ ] 核实 compaction 与 truncation 的真实触发条件，避免把教学 mock 的阈值写成官方行为。
- [ ] 明确 compaction 与 rollout 的边界；rollout 相关端到端路径在 s08 仍按待核实处理。
