# learn-codex

`learn-codex` 是一个面向 AI 产品经理和 agent 平台设计者的中文教学仓库。它用公开源码拆解 Codex CLI 的 agent harness：loop、tools、context、permissions、sessions、models、extensions、app-server 与综合架构。

## 当前阶段

Step 1 已完成：目录、章节边界、状态标签、事实快照和溯源规则已经固定。

Step 2 初版已完成：12 章均包含 README、Mermaid 图、Python mock、真实映射、生产差异、练习和事实核验清单。Python mock 只用于教学，不调用 OpenAI API，不代表官方实现，也不证明与官方 Codex 实现等价。

## 事实边界

- 本仓研究对象是 [OpenAI Codex 开源仓库](https://github.com/openai/codex) 中的 Rust CLI harness，也就是 `codex-rs`。
- Python 代码只用于教学 mock，不代表 OpenAI 官方实现。
- Codex Web、Codex Cloud、IDE 体验和 GitHub 集成只在公开资料范围内作为旁支说明。
- 所有“官方事实”必须能追到固定 commit 的 OpenAI 源码 permalink、OpenAI 官方文档或 release note；否则章节必须标注为“待核实”或“教学抽象”，句子层面的解释可以标注为“推断”。

当前事实快照见 [docs/fact-snapshot.md](docs/fact-snapshot.md)。

## 学习地图

| 阶段 | 章节 | 主题 | 状态 |
| --- | --- | --- | --- |
| 基础运行时 | [s01_agent_loop](chapters/s01_agent_loop/README.md) | agent loop、turn、tool observation | 已核实官方事实 |
| 基础运行时 | [s02_protocol_events](chapters/s02_protocol_events/README.md) | 事件协议、输入输出项、trace | 已核实官方事实 |
| 工具系统 | [s03_tool_registry_dispatch](chapters/s03_tool_registry_dispatch/README.md) | 工具声明、注册、路由、执行 | 已核实官方事实 |
| 安全边界 | [s04_shell_sandbox_permissions](chapters/s04_shell_sandbox_permissions/README.md) | shell、sandbox、approval、网络权限 | 已核实官方事实 |
| 上下文管理 | [s05_context_window_compaction](chapters/s05_context_window_compaction/README.md) | 上下文窗口、压缩、截断 | 已核实官方事实 |
| 指令系统 | [s06_prompts_instructions](chapters/s06_prompts_instructions/README.md) | system prompt、AGENTS.md、指令层级 | 已核实官方事实 |
| 配置与模型 | [s07_config_auth_models](chapters/s07_config_auth_models/README.md) | config、认证、model/provider 选择 | 已核实官方事实 |
| 会话状态 | [s08_sessions_threads_rollout](chapters/s08_sessions_threads_rollout/README.md) | session、thread、恢复、rollout 持久化 | 待核实 |
| App Server | [s09_app_server_transport](chapters/s09_app_server_transport/README.md) | app-server、transport、状态同步 | 已核实官方事实 |
| 扩展面 | [s10_extensions_mcp_skills](chapters/s10_extensions_mcp_skills/README.md) | MCP、extensions、skills 目录与动态工具 | 待核实 |
| 并行与委派 | [s11_subagents_parallel_jobs](chapters/s11_subagents_parallel_jobs/README.md) | 子任务、并行、委派 | 待核实 |
| 综合架构 | [s12_comprehensive_architecture](chapters/s12_comprehensive_architecture/README.md) | 端到端架构整合 | 教学抽象 |

## 读者路径

- AI 产品经理：先读每章的“本章回答什么”和“对产品与平台设计的意义”，重点看安全、成本、延迟、信任与用户摩擦。
- Agent 平台设计者：从源码映射和机制图进入，再看后续 Step 2 的 mock、trace 与 failure path。
- 内容贡献者：先读 [docs/sourcing.md](docs/sourcing.md) 和 [docs/glossary.md](docs/glossary.md)，再动任何“官方事实”相关文字。

## 本地检查

```bash
python3 scripts/check_docs.py
python3 scripts/run_all.py
python3 -m unittest discover -s tests
```

## 非官方声明

本仓是非官方教学项目，与 OpenAI 无隶属关系。`Codex` 是 OpenAI 相关名称。引用 OpenAI Codex 源码或文档时，必须遵守其原仓库 license 和官方使用条款；本仓自身采用 [MIT License](LICENSE)。
