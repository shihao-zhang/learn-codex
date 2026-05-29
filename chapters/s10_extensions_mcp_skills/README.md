# s10_extensions_mcp_skills

## 状态标签

状态：待核实

## 本章回答什么

Step 1 只固定边界：本章将核实 MCP、extensions、skills 目录与动态工具之间的关系。当前禁止先声称“skills 是 CLI 一等能力”。

## 对产品与平台设计的意义

扩展面决定生态策略、第三方工具接入、安全审查和能力发现。这里最容易把其他 agent 产品的概念误套到 Codex。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s10_extensions_mcp_skills/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- MCP
- extension tools
- dynamic tools
- skills directory

## 真实 Codex 映射

- [codex-rs/core/src/tools/handlers/mcp.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/mcp.rs)
- [codex-rs/core/src/tools/handlers/extension_tools.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/extension_tools.rs)
- [codex-rs/skills/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/skills/src)

## 教学简化与生产差异

本章当前待核实。Step 2 必须先确认 `skills` 在 Codex CLI 中的真实角色，再决定是否保留章节名或改成 `extensions_mcp_dynamic_tools`。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 核实 `skills` 是否是 CLI 用户可见能力、内部 crate，还是其他用途。
- [ ] 避免把 Claude Code skills 概念写成 Codex 官方实现。
