# Glossary

本术语表只做 Step 1 骨架约束。后续每个术语必须在章节内容中补齐官方映射或明确标注为教学抽象。

| 术语 | 本仓暂定含义 | 风险提示 |
| --- | --- | --- |
| agent harness | 支撑 agent 循环、工具调用、权限、上下文和会话状态的运行时脚手架 | 教学抽象，不等同于官方模块名 |
| loop | agent 在一次或多次 turn 中接收输入、调用模型、执行工具、观察结果并继续的控制流 | 需对齐真实 Rust 实现 |
| turn | 一轮用户输入和 agent 响应/工具调用相关的执行单元 | 需对齐 `protocol` 与 core 中的类型 |
| tool observation | 工具执行后的结构化结果，返回给模型或运行时继续处理 | mock 命名可能简化 |
| protocol event | CLI、core、app-server 或前端之间流转的结构化事件 | 需尽量使用真实类型名 |
| sandbox | 限制命令执行能力的系统边界 | 不同 OS 实现不同，不能只用 Python mock 推断 |
| approval | 对高风险操作请求人类确认的机制 | 策略和 UI 可能随版本变化 |
| compaction | 上下文窗口压力下对历史信息进行压缩或截断 | 不等同于 rollout |
| rollout | 会话历史或执行轨迹的持久化/恢复相关概念 | 容易和 context compaction 混淆，当前待核实 |
| AGENTS.md | 仓库内给 agent 的长期行为规则 | 与 prompt、memory、system instruction 不要混写 |
| model/provider | 通过配置选择模型和服务提供方 | 不称为复杂“模型路由”，除非源码证明 |
| MCP | Model Context Protocol 相关 client/server/tool 集成 | 官方 README 已说明，但具体实现仍需逐章核实 |
| skills | Codex 仓库中存在相关目录/包名，但它是否是 CLI 一等用户能力待核实 | 容易和 Claude Code skills 混淆 |
| subagents | 子任务、委派或后台 agent 相关能力的泛称 | 容易和其他 agent 产品混淆，当前待核实 |
| app-server | Codex app/server 侧协议、状态同步和 transport 相关 crate | 不等同于 Codex Cloud 私有实现 |

