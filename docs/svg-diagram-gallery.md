# SVG 教学图册索引

本页是全仓 SVG 教学辅助图的导航索引，面向 AI 产品经理和 agent 平台设计者。它只汇总现有图和 companion Markdown 的边界说明，不新增官方事实，不替代每章 `diagram.mmd`，也不改变章节状态。

读图顺序建议：

1. 先看本页判断哪张图能回答当前问题。
2. 再打开 companion Markdown，看 `Source Inputs`、`Event / Mechanism Mapping`、`Fact Boundary` 和 `Manual QA`。
3. 如果要引用官方事实，回到 [source-evidence.md](source-evidence.md) 和固定 SHA 源码；不要把 SVG 当成事实来源。

## 图册总览

| 章节 | SVG 路径 | companion Markdown 路径 | 解决什么理解问题 | FACT / 待核实 / 教学抽象边界 |
| --- | --- | --- | --- | --- |
| s01_agent_loop | [turn-loop.svg](../chapters/s01_agent_loop/diagrams/turn-loop.svg) | [turn-loop.md](../chapters/s01_agent_loop/diagrams/turn-loop.md) | 一个 turn 如何在模型动作、工具执行、observation 回填、继续/停止之间循环。 | `FACT` 只覆盖 loop 入口、tool call 路由、observation 回填和历史记录；mock event、示例工具名、失败恢复话术是 `教学抽象`；本图不引入 s08/s10 `待核实` 语义。 |
| s02_protocol_events | [event-interface.svg](../chapters/s02_protocol_events/diagrams/event-interface.svg) | [event-interface.md](../chapters/s02_protocol_events/diagrams/event-interface.md) | request、input/output item、protocol event 和 trace context 如何变成客户端可理解的状态。 | `FACT` 只覆盖已登记的 Event/EventMsg、模型输入输出 item 和 trace context 入口；UI 状态、mock event 名称、schema drift 和兼容降级是 `教学抽象`；本图不引入 s08/s10 `待核实` 语义。 |
| s03_tool_registry_dispatch | [tool-dispatch.svg](../chapters/s03_tool_registry_dispatch/diagrams/tool-dispatch.svg) | [tool-dispatch.md](../chapters/s03_tool_registry_dispatch/diagrams/tool-dispatch.md) | 工具声明、registry、router、handler 和结果回写如何形成受控执行链。 | `FACT` 只覆盖 model-visible specs、registry、router、dispatch、handler 调用和结果回写；示例工具名、mock handler、未知工具恢复是 `教学抽象`；dynamic tools、MCP、extensions、skills 仍按 s10 `待核实` 边界处理。 |
| s04_shell_sandbox_permissions | [permission-boundary.svg](../chapters/s04_shell_sandbox_permissions/diagrams/permission-boundary.svg) | [permission-boundary.md](../chapters/s04_shell_sandbox_permissions/diagrams/permission-boundary.md) | shell 请求如何穿过 approval、sandbox、network policy；拒绝后为什么不执行高风险副作用。 | `FACT` 只覆盖 approval requirement、approval primitive/cache、sandbox attempt、网络审批状态与 deferred flow；示例命令、审批文案和恢复建议是 `教学抽象`；OS sandbox backend、具体 UI 和跨平台细节为 `待核实`。 |
| s05_context_window_compaction | [context-pressure.svg](../chapters/s05_context_window_compaction/diagrams/context-pressure.svg) | [context-pressure.md](../chapters/s05_context_window_compaction/diagrams/context-pressure.md) | context pressure 下 compact、历史替换、truncation helper、摘要风险和恢复选择如何区分。 | `FACT` 只覆盖 compact task 入口、compact 后历史替换与 rollout 记录、thread rollout truncation helper；token 数字、阈值、保真字段、摘要质量和恢复文案是 `教学抽象`；rollout/resume 端到端承诺仍按 s08 边界，不在本图升级。 |
| s06_prompts_instructions | [instruction-conflict.svg](../chapters/s06_prompts_instructions/diagrams/instruction-conflict.svg) | [instruction-conflict.md](../chapters/s06_prompts_instructions/diagrams/instruction-conflict.md) | system/developer/user 指令与 AGENTS.md 项目规则冲突时，如何解释优先级、授权和未执行副作用。 | `FACT` 只覆盖 AGENTS.md 发现与组合、用户指令与项目说明拼接、初始上下文注入多类指令；冲突案例、优先级可视化、授权文案和项目规则示例是 `教学抽象`；不声明真实优先级算法或所有客户端裁决规则。 |
| s07_config_auth_models | [model-choice-impact.svg](../chapters/s07_config_auth_models/diagrams/model-choice-impact.svg) | [model-choice-impact.md](../chapters/s07_config_auth_models/diagrams/model-choice-impact.md) | config、auth、provider/model 选择如何影响成本、能力、合规和可用性。 | `FACT` 只覆盖 config 类型入口、model preset/model info、session 初始化时模型与 base instructions 选择；成本、能力、合规、可用性、auth 产品解释和恢复建议是 `教学抽象`；最新模型列表、价格、默认值和企业策略为 `待核实` 或易漂移点。 |
| s08_sessions_threads_rollout | [session-thread-rollout.svg](../chapters/s08_sessions_threads_rollout/diagrams/session-thread-rollout.svg) | [session-thread-rollout.md](../chapters/s08_sessions_threads_rollout/diagrams/session-thread-rollout.md) | session、thread、rollout、resume、fork 的关系哪些只是局部源码证据，哪些不能升级成稳定恢复语义。 | 章节状态保持 `待核实`；`FACT(局部)` 只覆盖 session/thread id、local/in-memory ThreadStore、rollout replay、app-server resume/fork 等已登记路径；remote thread-store、Codex Cloud/桌面端恢复语义、experimental API 稳定承诺均为 `待核实`；恢复链路表达是 `教学抽象`。 |
| s09_app_server_transport | [state-sync-boundary.svg](../chapters/s09_app_server_transport/diagrams/state-sync-boundary.svg) | [state-sync-boundary.md](../chapters/s09_app_server_transport/diagrams/state-sync-boundary.md) | runtime event、app-server、protocol/transport 和 product surface 的状态同步边界在哪里。 | `FACT` 只覆盖 transport 连接状态与 outbound 队列、outgoing envelope 路由、server request callback、thread status 投影和 schema export；UI 命名、多端体验、重连建议和 mock trace 是 `教学抽象`；字段级兼容性、具体客户端、完整事件重放、Codex Cloud 和私有服务行为为 `待核实`。 |
| s10_extensions_mcp_skills | [extension-capability-lines.svg](../chapters/s10_extensions_mcp_skills/diagrams/extension-capability-lines.svg) | [extension-capability-lines.md](../chapters/s10_extensions_mcp_skills/diagrams/extension-capability-lines.md) | MCP、dynamic tools、extension tools、skills 四条能力线如何并排理解，而不是合并成一个插件承诺。 | 章节状态保持 `待核实`；`FACT` 只覆盖已登记的 s10 局部机制点；dynamic tools experimental API、通用 extension 用户入口、统一治理路径和 skills 跨客户端语义为 `待核实`；四条能力线并列表达、产品治理框架和 mock trace 是 `教学抽象`。 |
| s11_subagents_parallel_jobs | [subagents-parallel-jobs.svg](../chapters/s11_subagents_parallel_jobs/diagrams/subagents-parallel-jobs.svg) | [subagents-parallel-jobs.md](../chapters/s11_subagents_parallel_jobs/diagrams/subagents-parallel-jobs.md) | 父任务如何 delegate，父子事件和审批如何回传，并行 job 如何执行和汇总结果。 | `FACT` 只覆盖 multi-agent/spawn_agent surface、AgentControl、delegate 事件与审批转发、CSV agent job worker/result、普通 tool call 并行运行时；默认启用、产品入口、multi-agent v1/v2 体验和完整权限继承策略为 `待核实`；result merge、进度 UI、冲突处理和 mock trace 是 `教学抽象`。 |
| s12_comprehensive_architecture | [pilot-trace.svg](../chapters/s12_comprehensive_architecture/diagrams/pilot-trace.svg) | [pilot-trace.md](../chapters/s12_comprehensive_architecture/diagrams/pilot-trace.md) | 端到端 failure trace 中，工具缺失、权限拒绝、上下文压力、指令冲突和恢复选择如何串起来。 | 整张图是 `教学抽象`，来自 s12 Python mock；不代表 OpenAI Codex 官方实现、Codex 桌面端实现、真实权限 UI 或生产拓扑；图例保留 `FACT` 和 `待核实` 是边界提醒，不把任何 trace 节点升级成官方事实。 |

## 维护规则

- 新增或改名章节 SVG 时，同步更新本索引。
- 本索引只链接 `chapters/<chapter>/diagrams/` 下的手写 SVG 和 companion Markdown。
- 如果某张图包含 `FACT`，事实来源仍必须回到 [source-evidence.md](source-evidence.md)；图册不承担证据登记职责。
- s08、s10、s12 的状态边界不得通过图册措辞被弱化。
- 图册入口可以帮助读者选图，但不能替代每章 README、companion Markdown 和事实核验清单。
