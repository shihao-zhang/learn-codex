# s01_agent_loop

## 状态标签

状态：已核实官方事实

## 本章回答什么

本章回答一个最基础但最容易被低估的问题：Codex 这类 agent 不是“一次提问一次回答”的聊天机器人，而是一个会在模型推理、工具调用、工具结果回填之间反复推进的运行循环。

读完本章，你应该能区分三件事：

- `turn`：用户一次输入触发的一段工作，不等于模型只调用一次。
- `tool observation`：工具返回给运行时、再进入模型上下文的结构化结果，不是普通日志。
- `loop termination`：循环何时结束，可能因为模型给出最终答复，也可能因为错误、取消、权限被拒或无法恢复的阻塞。

## 对产品与平台设计的意义

对 AI 产品经理来说，agent loop 决定了用户看到的是“它正在认真工作”，还是“它卡住了但还在转圈”。一次任务可能经历多次模型决策、多次工具调用和多次状态更新，所以产品需要把这些内部阶段翻译成进度、等待、确认、失败和完成。

对平台设计者来说，loop 是调度边界：它决定什么时候组装上下文、什么时候暴露工具、什么时候等待 observation、什么时候允许取消、什么时候把结果持久化或上报给客户端。这里的关键权衡是：循环越自主，越需要清晰的停止条件、权限边界和可观测性；循环越保守，用户摩擦和延迟就会增加。

## PM 真正关心的问题

- 用户不是只问“模型聪不聪明”，而是在问：它现在到底在想、在查、在执行，还是已经卡住了？
- 什么时候应该继续自动推进，什么时候应该停下来问人？例如连续多次工具失败、权限缺失、上下文不足时，继续重试可能只是在消耗用户耐心和预算。
- 一次 turn 的成本和风险上限在哪里？产品需要能限制工具次数、运行时间、审批次数和最终失败呈现，而不是把 loop 当成无限自动驾驶。

## 机制图

见 [diagram.mmd](diagram.mmd)。图里把 agent loop 画成“模型决策 -> 工具执行 -> observation 回填 -> 再决策”的闭环，并显式标出终止出口。

## 运行 mock

```bash
python3 chapters/s01_agent_loop/mock.py --demo
```

这个 mock 只演示教学抽象：一个 happy path 会先读上下文、再把工具结果回填给模型；一个 failure path 会把工具错误转成可解释的最终回复。它不是 Codex 官方实现，也不复刻 Rust 异步运行时或真实模型行为。

## mock trace 怎么读

建议先运行 happy path，再运行：

```bash
python3 chapters/s01_agent_loop/mock.py --demo --path failure --trace-json
```

trace 的价值不是事件名本身，而是因果顺序：`input` 进入 turn，`model` 决定调用工具，`tool_error` 作为 observation 回到运行时，最后模型解释阻塞而不是假装成功。这里的 `recoverable`、`action` 等字段都是教学字段，不是官方 Rust 类型或协议字段。

## 核心机制

- 用户输入进入运行时后，会被放入当前任务/回合的上下文中。平台需要同时携带用户意图、指令、历史、可用工具和权限状态。
- 模型步骤不是天然终点。模型可以选择输出面向用户的最终内容，也可以请求工具。只要请求工具，运行时就要暂停模型侧推进，转入工具执行。
- 工具调用必须被运行时接管：解析工具名和参数、检查是否存在、执行 handler、捕获成功或失败，再把结果整理成模型可消费的 observation。
- observation 回填后，模型才拥有“工具刚刚发生了什么”的上下文。下一步可能继续调用工具，也可能收束成最终答复。
- 终止条件要产品化：正常完成、用户取消、权限拒绝、工具不可用、不可恢复错误、上下文或预算限制，都应该形成不同的用户体验和平台事件。
- 失败不是循环外的异常小尾巴。一个好的 harness 会把可恢复失败交还给模型解释或改路，把不可恢复失败暴露为稳定状态，而不是假装完成。

## 典型 failure path

教学 failure path：用户要求修改一个文件，模型先调用 `read_file`，但工具返回“文件不存在”。此时最重要的产品判断不是“报错了吗”，而是“能不能恢复”：如果用户可能给错路径，agent 应该解释缺口并请求新路径；如果路径来自 agent 自己的假设，agent 应该尝试搜索或缩小范围；如果权限或工作区边界阻止读取，就应转入 s04 的审批/权限路径。

这个 failure path 用来训练读者识别 loop 的安全出口。它不声明官方 Codex 对“文件不存在”一定采用同样文案、事件名或恢复策略；官方事实只限于本章登记的 loop、tool routing 和 item/event 证据。

## 真实 Codex 映射

- [codex-rs/core/src/agent](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/agent)
- [codex-rs/core/src/tools](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools)

映射解释：

- `agent` 目录是理解 agent 控制流、状态和角色组织的入口。教学里的“loop”对应的是一组运行时控制职责，不应被理解成某个单一 Python 函数。
- `tools` 目录是理解工具调用如何进入执行层的入口。教学里的“tool observation”强调结果回填语义；真实实现还要处理工具注册、路由、生命周期、错误、取消和 telemetry。
- 本章只用这两个已登记 permalink 建立阅读入口；具体类型名、字段名和事件名以固定 SHA 下的源码为准。
- 机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)，包括 session loop 启动、tool call 路由和 conversation item 记录。
- 本章的 PM 问题、failure path 和 mock trace 解读是面向产品理解的教学表达；除非能追到固定 SHA 源码证据，否则不要把它们改写成官方行为断言。

## 教学简化与生产差异

- 教学图把 loop 画成串行闭环，是为了让读者先抓住因果关系；生产实现会有异步任务、流式事件、取消信号、并发工具、hook、权限检查和状态持久化。
- mock 里的 `input -> model -> tool -> observation -> model` 是最小心智模型，不代表真实 Codex 的模块边界、函数名或 wire format。
- 教学里把“最终答复”画成单一终点；生产里还要区分用户可见完成、内部清理完成、事件发送完成和持久化完成。
- 教学里把工具结果都称为 observation；生产里可能存在面向模型的输出、面向 UI 的事件、面向日志/trace 的记录，它们不是同一个东西。

## 练习

1. 运行 mock 的 happy path，标出哪一步是模型决策、哪一步是工具执行、哪一步是 observation 回填。
2. 修改用户任务的假想描述：如果工具返回“文件不存在”，产品上应该展示为失败、追问用户，还是让 agent 尝试搜索替代文件？写出你的判断标准。
3. 设计一个最小状态机，至少包含 `running`、`waiting_for_tool`、`waiting_for_approval`、`completed`、`failed`、`cancelled`。说明每个状态由谁触发。
4. 思考一个平台问题：如果模型连续调用 20 次工具但没有接近完成，应该由模型自己停下、运行时限流，还是产品提示用户介入？

## 事实核验清单

- [x] 核实 session loop 启动入口与 `submission_loop` 任务创建。
- [x] 核实 tool call 从模型 response item 进入 router/registry dispatch 的机制路径。
- [x] 核实 conversation items 会写历史、持久化 rollout 并发送 raw response item 事件。
- [ ] 不把 Python mock 的 `TeachingScenario`、事件名或函数名写成官方 Rust 类型名。
- [ ] 区分教学术语“observation”和真实源码中的协议 item、tool output、event、trace 结构。
- [ ] 遇到无法从固定 SHA 源码确认的行为，标注为“教学抽象”或“推断”，不要升级成官方事实。
