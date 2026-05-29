# Fact Snapshot

本页记录当前教学内容引用的公开事实快照。后续内容写作必须以本页为准，除非先更新快照并重新核验。

## Snapshot

- 核验日期：2026-05-29
- OpenAI Codex 仓库：[openai/codex](https://github.com/openai/codex)
- 目标 commit：[`740d942f901a5a63421298c74dafbeb4255e946d`](https://github.com/openai/codex/commit/740d942f901a5a63421298c74dafbeb4255e946d)
- 最新 GitHub release 核验值：[`rust-v0.135.0`](https://github.com/openai/codex/releases/tag/rust-v0.135.0)，发布名 `0.135.0`
- Rust CLI README：[codex-rs/README.md](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/README.md)
- Cargo workspace：[codex-rs/Cargo.toml](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/Cargo.toml)

## 已核实边界

- `codex-rs` 是当前教学对象，且官方 README 称 Rust implementation 是 maintained Codex CLI。
- `codex-rs` 是 Cargo workspace。
- 官方 README 描述了 npm、Homebrew、GitHub Releases 安装路径。
- 官方 README 描述了 MCP client、experimental MCP server、sandbox policy、`codex exec` 和 `codex sandbox` 等能力。

## 证据分级

本快照中的“源码路径”只证明路径存在。机制级和行为级核验统一登记在 [source-evidence.md](source-evidence.md)：

- 路径存在证据：GitHub Contents API 或固定 SHA permalink 能打开对应文件/目录。
- 机制级证据：已读到机制入口、类型、trait、handler、控制流或状态投影，可以支撑章节主映射。
- 行为级证据：已读到关键分支、错误路径、状态转换、持久化或重试逻辑，可以支撑更具体的行为描述。

章节不得仅凭本页路径存在表升级为 `已核实官方事实`。升级必须同时满足章节 README 状态、`docs/source-evidence.md` 证据级别和 `scripts/check_docs.py` 检查。

## 已核实源码路径

以下路径已在 2026-05-29 通过 GitHub Contents API 对目标 commit 验证存在，返回 HTTP 200。该表只证明路径存在，不证明章节对行为的解释已经完整。

| 章节 | 已核实路径 |
| --- | --- |
| s01_agent_loop | [codex-rs/core/src/agent](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/agent) |
| s01_agent_loop | [codex-rs/core/src/tools](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools) |
| s02_protocol_events | [codex-rs/protocol/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src) |
| s03_tool_registry_dispatch | [codex-rs/core/src/tools/registry.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/registry.rs) |
| s03_tool_registry_dispatch | [codex-rs/core/src/tools/router.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/router.rs) |
| s03_tool_registry_dispatch | [codex-rs/core/src/tools/handlers](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers) |
| s04_shell_sandbox_permissions | [codex-rs/core/src/tools/sandboxing.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/sandboxing.rs) |
| s04_shell_sandbox_permissions | [codex-rs/core/src/tools/network_approval.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/network_approval.rs) |
| s04_shell_sandbox_permissions | [codex-rs/protocol/src/permissions.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/permissions.rs) |
| s05_context_window_compaction | [codex-rs/core/src/compact.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact.rs) |
| s05_context_window_compaction | [codex-rs/core/src/compact_remote.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact_remote.rs) |
| s05_context_window_compaction | [codex-rs/core/src/compact_remote_v2.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact_remote_v2.rs) |
| s06_prompts_instructions | [codex-rs/protocol/src/prompts](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/prompts) |
| s06_prompts_instructions | [codex-rs/core/src/agents_md.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/agents_md.rs) |
| s07_config_auth_models | [codex-rs/protocol/src/config_types.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/config_types.rs) |
| s07_config_auth_models | [codex-rs/protocol/src/models.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/models.rs) |
| s07_config_auth_models | [codex-rs/protocol/src/openai_models.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/openai_models.rs) |
| s07_config_auth_models | [codex-rs/protocol/src/auth.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/auth.rs) |
| s09_app_server_transport | [codex-rs/app-server/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server/src) |
| s09_app_server_transport | [codex-rs/app-server-protocol/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server-protocol/src) |
| s11_subagents_parallel_jobs | [codex-rs/core/src/tools/handlers/agent_jobs.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/agent_jobs.rs) |
| s11_subagents_parallel_jobs | [codex-rs/core/src/codex_delegate.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/codex_delegate.rs) |
| s11_subagents_parallel_jobs | [codex-rs/core/src/tools/parallel.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/parallel.rs) |

## 已引用但行为待核实的源码路径

以下路径同样已在 2026-05-29 通过 GitHub Contents API 对目标 commit 验证存在，返回 HTTP 200。但对应章节仍标为 `待核实` 或 `教学抽象`，因为路径存在不等于行为解释已经核实。

| 章节 | 已核实存在的路径 |
| --- | --- |
| s08_sessions_threads_rollout | [codex-rs/protocol/src/session_id.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/session_id.rs) |
| s08_sessions_threads_rollout | [codex-rs/protocol/src/thread_id.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/thread_id.rs) |
| s08_sessions_threads_rollout | [codex-rs/core/src/thread_rollout_truncation.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/thread_rollout_truncation.rs) |
| s08_sessions_threads_rollout | [codex-rs/thread-store](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/thread-store) |
| s08_sessions_threads_rollout | [codex-rs/rollout](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/rollout) |
| s10_extensions_mcp_skills | [codex-rs/core/src/tools/handlers/mcp.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/mcp.rs) |
| s10_extensions_mcp_skills | [codex-rs/core/src/tools/handlers/extension_tools.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/extension_tools.rs) |
| s10_extensions_mcp_skills | [codex-rs/skills/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/skills/src) |
| s12_comprehensive_architecture | [codex-rs/core](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core) |
| s12_comprehensive_architecture | [codex-rs/protocol](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol) |
| s12_comprehensive_architecture | [codex-rs/app-server](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server) |
| s12_comprehensive_architecture | [codex-rs/Cargo.toml](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/Cargo.toml) |

## 易过期点

- release 版本和 npm/Homebrew 分发方式。
- model/provider 名称、reasoning 参数和默认值。
- app-server API、transport、protocol shape。
- permissions、sandbox、network approval 策略。
- extensions、skills、subagents、parallel jobs 的边界和命名。
- `rollout` 与 thread/session 持久化的具体职责。

## 待核实队列

- `codex-rs/skills/src`、session available skills instructions 与 CLI 用户可见 skills 能力之间的关系。
- `thread-store`、`rollout`、`thread_rollout_truncation.rs` 与 app-server/thread 恢复的完整数据流。
- `app-server`、`app-server-protocol` 中 request、outgoing message、thread state/status、protocol export 的字段级兼容性。
- 多 agent v1/v2、agent jobs 与普通工具并行的产品入口、默认启用条件和体验边界。
