# s10_extensions_mcp_skills

## 状态标签

状态：待核实

## 本章回答什么

本章回答“能力如何进入 agent 平台”的设计问题。当前已核实 MCP handler、extension tool adapter、system skills 缓存安装和 session available skills instructions 的源码线索；章节状态仍保持待核实，因为“skills 是否是 CLI 用户可见的一等能力、如何配置和触发”还不能只靠这些局部证据下结论。

已登记的公开源码路径包括 MCP handler、extension tools handler、`skills` crate 目录。它们说明这些代码入口存在，也支持局部机制解释；它们尚不足以证明 MCP、extensions、skills 在 Codex CLI 中分别是什么用户可见能力、生命周期如何、是否属于同一扩展体系。因此本章不会声称“skills 是 CLI 一等能力”，也不会把 Claude Code 或其他 agent 产品的 skills 概念套到 Codex 上。

## 对产品与平台设计的意义

扩展面决定一个 agent 平台能否从“内置工具集合”成长为“可治理的能力生态”。产品上要同时解决四件事：

- 发现：agent 怎么知道有哪些外部能力可用，能力描述是否足够让模型正确选择。
- 暴露：哪些能力进入当前 turn，哪些延迟加载，哪些只在特定上下文出现。
- 治理：外部能力如何经过权限、审批、审计、速率限制和数据边界。
- 体验：用户看到的是一个稳定工具，还是一个来源复杂、失败方式各异的插件集合。

本章的关键权衡是：能力越开放，生态越强；能力越动态，安全审查、可解释性和调试成本越高。

## 机制图

见 [diagram.mmd](diagram.mmd)。图把 MCP、extension tools、skills 先画成不同能力来源，再进入发现、工具规范、治理和运行时；其中 MCP/extension adapter 已有机制证据，skills 的用户可见语义仍待核实。

## 运行 mock

```bash
python3 chapters/s10_extensions_mcp_skills/mock.py --demo
```

教学 mock 只演示“能力来源 -> 工具描述 -> 策略检查 -> 调用结果”的产品化流程，不代表 Codex 官方扩展机制、MCP wire format、skills 语义或真实权限实现。

## 核心机制

- `MCP`：源码显示 MCP handler 实现 `ToolExecutor`，把 MCP tool 转为可调用 tool spec，并根据 read-only hint 或 server opt-in 决定是否支持并行。仍需核实 MCP server 配置、生命周期和用户入口。
- `extension tools`：源码显示 extension executor 会被适配成 core tool runtime，并能拿到 turn id、history、truncation policy 和 turn item emitter。仍需核实 extension 的安装、发现和治理入口。
- `dynamic tools`：概念上指“运行时才发现或暴露的工具”。已定位 app-server thread start 对 dynamic tool identifier、namespace 和 schema 的校验；仍需核实来源、加载时机和可见范围。
- `skills directory`：源码显示 `skills` crate 会把 embedded system skills 安装到 `CODEX_HOME/skills/.system`，session 也会构造 available skills instructions。它仍不能被写成 Codex CLI 已确认的用户级 skills 功能，直到配置、触发和 UI/CLI 入口被完整核实。
- `tool surface governance`：无论能力来自哪里，平台都要回答同一组问题：谁声明、谁授权、谁执行、谁记录、失败时谁负责。

## 真实 Codex 映射

- [codex-rs/core/src/tools/handlers/mcp.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/mcp.rs)
- [codex-rs/core/src/tools/handlers/extension_tools.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/extension_tools.rs)
- [codex-rs/skills/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/skills/src)

这些 permalink 目前只作为“路径存在”的事实锚点。它们不自动证明三者的产品语义、用户入口、配置方式或文档承诺。

机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)。当前可核实的事实包括 MCP handler/extension adapter/system skills 安装路径；章节待核实点集中在用户可见入口、配置生命周期和“skills”术语边界。

## 教学简化与生产差异

本章故意采用保守写法：先讲平台设计中的扩展面问题，再把 Codex 映射限制在已登记路径。

- 教学 mock 会把所有扩展统一成同一种 `ToolSpec`，真实实现已经能看到不同 adapter、事件、权限和生命周期线索，不能用 mock 抹平差异。
- 图中的 `skills` 是待核实线索，不是 Claude Code skills，也不是已确认的 Codex CLI 一等功能。
- 如果后续源码核实发现 `skills` 不是用户可见能力，本章标题应改为更保守的 `extensions_mcp_dynamic_tools`。
- 如果后续核实发现 MCP、extension tools、skills 的治理路径不同，应拆成独立小节，避免用“插件生态”一词抹平差异。

## 练习

1. 做一张能力来源表：列出 MCP、extension tools、skills 三行，分别填“已核实事实”“待核实语义”“产品风险”。
2. 设计一个动态工具的上架流程：从发现、schema 校验、权限提示、试运行到审计记录，每步写清谁负责。
3. 比较“默认暴露所有工具”和“按需搜索工具”的成本：前者上下文重，后者发现慢；给出你的产品默认值。
4. 写一个反例：为什么不能把其他 agent 产品里的 skills 体验直接写成 Codex 官方能力。

## 事实核验清单

- [x] 已登记 MCP handler、extension adapter、system skills 安装和 session skills instructions 的机制级证据。
- [x] 明确能力语义、用户入口和生命周期仍待核实。
- [x] 明确不把 Claude Code skills 或其他平台概念写成 Codex 官方实现。
- [ ] 核实 `skills` 是 CLI 用户可见能力、内部 crate、构建辅助，还是其他用途。
- [ ] 核实 MCP 与 extension tools 是否共享同一工具治理路径。
