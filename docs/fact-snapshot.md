# Fact Snapshot

本页记录当前骨架引用的公开事实快照。后续内容写作必须以本页为准，除非先更新快照并重新核验。

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

## 易过期点

- release 版本和 npm/Homebrew 分发方式。
- model/provider 名称、reasoning 参数和默认值。
- app-server API、transport、protocol shape。
- permissions、sandbox、network approval 策略。
- extensions、skills、subagents、parallel jobs 的边界和命名。
- `rollout` 与 thread/session 持久化的具体职责。

## 待核实队列

- `codex-rs/skills/src` 与 CLI 一等 skills 能力之间的关系。
- `agent_jobs`、`codex_delegate`、`parallel` 是否构成开源 CLI harness 主线能力。
- `thread-store`、`rollout` 与 app-server/thread 恢复的完整数据流。

