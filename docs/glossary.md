# Glossary

本术语表维护跨章节术语边界。每个术语都必须回到章节内容、固定 SHA 证据或明确的教学抽象标签，不能只靠产品经验扩写成官方事实。

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
| skills | 目标 commit 下有 TUI 用户入口、配置启停、loader、instructions 和 system cache 证据 | extension tools 入口和统一扩展治理仍待核实；容易和 Claude Code skills 混淆 |
| subagents | 目标 commit 下有 multi-agent tool surface、delegate、agent jobs 和并行运行时证据 | 默认启用条件、产品入口和 v1/v2 体验差异仍需核实；容易和其他 agent 产品混淆 |
| app-server | Codex app/server 侧协议、状态同步和 transport 相关 crate | 不等同于 Codex Cloud 私有实现 |
