# s11_subagents_parallel_jobs

## 状态标签

状态：已核实官方事实

这里的“已核实”只指 openai/codex 在目标 commit 中存在并行工具运行时、multi-agent tool surface、delegate 和 agent jobs 等源码机制；它不等于“这些能力在 Codex CLI 中默认对所有用户开放”，也不等于 OpenAI 官方产品承诺。multi-agent v1/v2 的产品体验差异、默认启用条件和用户入口仍需继续核实。

## 本章回答什么

本章回答“一个 agent 平台如何安全地把大任务拆给多个执行单元”的设计问题。当前已核实三类公开源码机制：multi-agent tool surface、`AgentControl`/delegate 子 agent 控制面、agent jobs CSV worker 和普通工具并行运行时。

需要保守的是产品外推：这些源码能证明 Codex 开源 CLI harness 里存在子 agent、agent job 和工具并行相关机制，但不能自动证明所有入口默认启用，也不能把它写成“任意场景通用子代理平台”。因此本章会把已核实机制和仍需核实的用户入口、默认开关、v1/v2 体验边界分开写。

## 对产品与平台设计的意义

并行不是“让 agent 更快”这么简单。它会同时放大吞吐、成本、权限风险和不可预测性：

- 成本：并行 worker 会消耗更多模型调用、工具调用和上下文预算。
- 权限：子任务是否继承父任务权限，是平台安全边界的核心决策。
- 可解释性：用户要知道哪些工作正在跑、谁失败了、结果是否完整。
- 恢复：长任务需要可追踪的 job/item 状态，否则中断后无法判断是否可续跑。
- 产品控制感：并行度、取消、重试、部分结果导出，都应是显式产品能力，而不是隐藏调度细节。

如果后续核实发现这些路径只服务特定入口，本章必须把它写成“特定能力”而非通用 harness 机制。

## 机制图

见 [diagram.mmd](diagram.mmd)。图用实线表达已核实到源码的 agent jobs、AgentControl、delegate 和 parallel runtime，用旁注保留产品入口与默认启用条件的 open questions。

## 可选教学辅助 SVG

见 [subagents-parallel-jobs.md](diagrams/subagents-parallel-jobs.md)。这张图只辅助理解 delegate、父子事件、审批转发、并行 job 和 result merge，不替代本章 Mermaid，也不新增官方事实。

## 运行 mock

```bash
python3 chapters/s11_subagents_parallel_jobs/mock.py --demo
```

教学 mock 只演示“父任务拆分为多个工作项、有限并发执行、收集结果、处理失败”的产品框架，不代表 Codex 官方子代理、agent jobs 或并行调度实现。

## 核心机制

- `agent jobs`：`spawn_agents_on_csv` 会把 CSV 行建成 job item，按并发上限生成 worker sub-agent；worker 必须用 `report_agent_job_result` 回填结果。它是已核实的特定工具机制，不等同于通用批处理 API。
- `delegation`：`codex_delegate.rs` 负责运行子 Codex thread、转发事件，并把审批请求路由回父 session。权限继承策略需要继续按具体分支核实。
- `parallel dispatch`：`tools/parallel.rs` 区分支持并行的工具与不支持并行的工具，分别使用读锁/写锁保护同一 turn 内的工具执行。它是工具并行运行时，不等同于子 agent 并行。
- `failure recovery`：并行任务必须定义 item 级失败、job 级失败、可重试失败和必须停止失败，否则 UI 只能给出模糊错误。
- `result merge`：汇总不是简单拼接。平台要处理顺序、去重、冲突、置信度、部分完成和最终交付格式。

## 真实 Codex 映射

- [codex-rs/core/src/tools/handlers/agent_jobs.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/agent_jobs.rs)
- [codex-rs/core/src/codex_delegate.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/codex_delegate.rs)
- [codex-rs/core/src/tools/parallel.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/parallel.rs)

机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)。当前可核实的官方事实包括：multi-agent handler 的职责注释、`spawn_agent` tool spec、`AgentControl` spawn/metadata/edge 持久化、delegate 事件与审批转发、CSV agent job worker 循环，以及 tool call runtime 的并行/取消处理。仍待核实的是：哪些入口默认暴露给用户、multi-agent v1/v2 的产品差异、以及 agent jobs 是否应作为主线学习路径还是进阶专题。

## 教学简化与生产差异

教学上可以先把并行委派拆成五层：任务拆分、并发调度、worker 执行、结果汇总、失败恢复。真实生产系统还需要处理更多问题：

- 父任务和子任务的权限继承、审批路由、审计归属必须清楚；源码中已读到 delegate 会把审批请求转回父 session，但具体继承策略仍要继续下钻。
- 并行度需要受配置、成本、速率限制和资源隔离约束。
- 子任务之间可能产生冲突，尤其是同时修改文件或共享外部状态时。
- 用户取消父任务时，子任务是否级联取消，需要明确生命周期契约。
- 本章 mock 和图都不是官方实现；它们只是产品架构教学模型。

## 练习

1. 给“批量检查 100 个 issue”设计一个并行 job：定义 item、并发度、输出 schema、失败重试和停止条件。
2. 写出三种失败策略：忽略单项失败、重试单项失败、失败即停止；说明各自适合什么产品场景。
3. 画一张权限继承表：父任务有写文件权限时，子任务是否自动继承？什么时候必须重新问用户？
4. 设计一个进度 UI：同时展示总进度、运行中 item、失败 item、可导出的部分结果。

## 事实核验清单

- [x] 已核实 multi-agent tool surface、AgentControl、delegate、agent jobs 与 tool parallel runtime 的机制级源码证据。
- [x] 明确用户入口、默认启用条件、multi-agent v1/v2 差异和主线地位仍需继续核实。
- [x] 明确 Python mock 和 Mermaid 图是教学模型，不代表真实 Codex 行为。
- [x] 核实 `parallel.rs` 是工具调用并行运行时，不是子 agent 并行本身。
- [ ] 核实 agent jobs 和 multi-agent 工具的默认暴露条件、feature flag、用户可见入口。
- [ ] 继续核实 delegation 的权限继承、审批和上下文隔离分支。
