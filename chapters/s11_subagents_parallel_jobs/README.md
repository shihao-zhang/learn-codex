# s11_subagents_parallel_jobs

## 状态标签

状态：待核实

## 本章回答什么

本章回答“一个 agent 平台如何安全地把大任务拆给多个执行单元”的设计问题，但当前只确认路径存在已核实，能力语义待核实。

已登记路径包括 agent jobs、delegate、parallel 相关源码线索。它们不能直接证明“Codex CLI 已提供通用子代理并行能力”，也不能证明这些能力属于主线用户体验。因此本章只把它们作为待核实线索和产品设计框架：如何拆任务、如何限流、如何汇总、如何恢复失败、如何把控制权交还给用户。

## 对产品与平台设计的意义

并行不是“让 agent 更快”这么简单。它会同时放大吞吐、成本、权限风险和不可预测性：

- 成本：并行 worker 会消耗更多模型调用、工具调用和上下文预算。
- 权限：子任务是否继承父任务权限，是平台安全边界的核心决策。
- 可解释性：用户要知道哪些工作正在跑、谁失败了、结果是否完整。
- 恢复：长任务需要可追踪的 job/item 状态，否则中断后无法判断是否可续跑。
- 产品控制感：并行度、取消、重试、部分结果导出，都应是显式产品能力，而不是隐藏调度细节。

如果后续核实发现这些路径只服务特定入口，本章必须把它写成“特定能力”而非通用 harness 机制。

## 机制图

见 [diagram.mmd](diagram.mmd)。图用虚线标出待核实源码线索，用实线表达通用产品机制：拆分、调度、执行、汇总、失败恢复。

## 运行 mock

```bash
python3 chapters/s11_subagents_parallel_jobs/mock.py --demo
```

教学 mock 只演示“父任务拆分为多个工作项、有限并发执行、收集结果、处理失败”的产品框架，不代表 Codex 官方子代理、agent jobs 或并行调度实现。

## 核心机制

- `agent jobs`：路径存在已核实，语义待核实。产品上可先把它理解为“把一批工作项作为 job 管理”的待验证线索。
- `delegation`：路径存在已核实，语义待核实。设计上要核实父任务与子任务之间如何传递上下文、权限、审批和结果。
- `parallel dispatch`：路径存在已核实，语义待核实。平台设计上要区分“工具调用并行”“工作项并行”“子代理并行”，三者风险不同。
- `failure recovery`：并行任务必须定义 item 级失败、job 级失败、可重试失败和必须停止失败，否则 UI 只能给出模糊错误。
- `result merge`：汇总不是简单拼接。平台要处理顺序、去重、冲突、置信度、部分完成和最终交付格式。

## 真实 Codex 映射

- [codex-rs/core/src/tools/handlers/agent_jobs.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/agent_jobs.rs)
- [codex-rs/core/src/codex_delegate.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/codex_delegate.rs)
- [codex-rs/core/src/tools/parallel.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/parallel.rs)

这些 permalink 目前只作为“路径存在”的事实锚点。是否构成用户可见的子代理能力、是否属于 CLI harness 主线、生命周期如何，仍待源码级语义核实。

## 教学简化与生产差异

教学上可以先把并行委派拆成五层：任务拆分、并发调度、worker 执行、结果汇总、失败恢复。真实生产系统还需要处理更多问题：

- 父任务和子任务的权限继承、审批路由、审计归属必须清楚。
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

- [x] 当前只说 agent_jobs、delegate、parallel 相关路径存在已核实。
- [x] 明确能力语义、用户入口、生命周期和主线地位仍待核实。
- [x] 明确 Python mock 和 Mermaid 图是教学模型，不代表真实 Codex 行为。
- [ ] 核实 agent_jobs 的用户可见入口、状态存储和生命周期。
- [ ] 核实 parallel.rs 是工具并行、子代理并行，还是内部调度辅助。
- [ ] 核实 delegation 是否继承父任务权限、审批和上下文，或另有隔离边界。
