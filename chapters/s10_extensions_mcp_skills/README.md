# s10_extensions_mcp_skills

## 状态标签

状态：待核实

## 本章回答什么

本章回答“能力如何进入 agent 平台”的设计问题。当前已核实 MCP 的 CLI 用户入口与 runtime exposure、extension tool adapter、dynamic tools、system skills 缓存安装、skills discovery/config、TUI `/skills`/`$` 入口、配置层启停路径、available skills instructions 和显式 skill mention 注入。

章节状态仍保持待核实，不是因为 skills TUI 可见入口完全无法证明，而是因为 extension tools 的安装/发现/用户入口仍未闭环，且 MCP、dynamic tools、extension tools、skills 是否能被概括为同一条“扩展治理路径”还需要继续核实。因此本章仍不会把源码路径存在直接写成完整扩展产品能力，也不会把 Claude Code、Codex 桌面端插件体验或其他 agent 产品的 skills 概念套到 `openai/codex`。

## 对产品与平台设计的意义

扩展面决定一个 agent 平台能否从“内置工具集合”成长为“可治理的能力生态”。产品上要同时解决四件事：

- 发现：agent 怎么知道有哪些外部能力可用，能力描述是否足够让模型正确选择。
- 暴露：哪些能力进入当前 turn，哪些延迟加载，哪些只在特定上下文出现。
- 治理：外部能力如何经过权限、审批、审计、速率限制和数据边界。
- 体验：用户看到的是一个稳定工具，还是一个来源复杂、失败方式各异的插件集合。

本章的关键权衡是：能力越开放，生态越强；能力越动态，安全审查、可解释性和调试成本越高。

## 机制图

见 [diagram.mmd](diagram.mmd)。图把 MCP、extension tools、skills 先画成不同能力来源，再进入发现、工具规范、治理和运行时；其中 MCP/extension adapter 已有机制证据，skills 的 TUI 可见入口和配置路径已有证据，但跨客户端语义和统一治理边界仍待核实。

## 运行 mock

```bash
python3 chapters/s10_extensions_mcp_skills/mock.py --demo
```

教学 mock 只演示“能力来源 -> 工具描述 -> 策略检查 -> 调用结果”的产品化流程，不代表 Codex 官方扩展机制、MCP wire format、skills 语义或真实权限实现。

## 核心机制

- `MCP`：已核实 Codex CLI 有 `codex mcp` / `codex mcp-server` 用户入口；runtime 会读取 MCP tools，按直接/延迟暴露策略加入 tool router；MCP handler 实现 `ToolExecutor`，并根据 read-only hint 或 server opt-in 决定是否支持并行。仍需继续核实具体 server 生命周期、认证、审批和失败恢复。
- `extension tools`：源码显示 extension registry 的 tool contributors 会产出 executors，planning 阶段会把它们适配成 core tool runtime。仍需核实 extension 的安装、发现、授权和用户可见入口。
- `dynamic tools`：源码显示 thread-scoped `DynamicToolSpec` 可转为 tool spec，调用时通过 dynamic tool request/response event 与外部客户端闭环。仍需核实 CLI 用户能否直接创建 dynamic tools，以及 app-server client 侧实现边界。
- `skills directory`：当前目标 commit 的 TUI 源码显示 skills 有 `/skills` 菜单、`$`/`@` 技能列表入口、启停技能 UI；配置和 loader 源码显示 repo/user/admin/system/plugin roots、配置启停路径、available skills instructions 和显式 mention 注入。该证据不等于所有客户端都有同样入口。
- `tool surface governance`：无论能力来自哪里，平台都要回答同一组问题：谁声明、谁授权、谁执行、谁记录、失败时谁负责。

## 真实 Codex 映射

- [codex-rs/core/src/tools/handlers/mcp.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/mcp.rs)
- [codex-rs/core/src/tools/handlers/extension_tools.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/extension_tools.rs)
- [codex-rs/skills/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/skills/src)

这些 permalink 是本章入口锚点，不自动证明三者属于同一个产品语义或治理体系。更细的机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)。

当前可核实的事实包括 MCP CLI 入口、MCP tool exposure、dynamic tool event flow、extension adapter、skills discovery/config、skills instructions 和显式 skill 注入。章节待核实点集中在 extension tools 的用户入口，以及这些能力是否能统一称为同一扩展体系。

## 教学简化与生产差异

本章故意采用保守写法：先讲平台设计中的扩展面问题，再把 Codex 映射限制在已登记路径。

- 教学 mock 会把所有扩展统一成同一种 `ToolSpec`，真实实现已经能看到不同 adapter、事件、权限和生命周期线索，不能用 mock 抹平差异。
- 图中的 `skills` 现在可以写成目标 commit 下 TUI 可见、配置可管理的 skills 能力，但不能借此套用 Claude Code skills、Codex 桌面端插件体验或其他平台语义。
- 如果后续更换目标 commit 后发现 `skills` 用户入口发生重大变化，本章需要重新走事实快照和 OpenSpec 核验。
- 如果后续核实发现 MCP、extension tools、skills 的治理路径不同，应拆成独立小节，避免用“插件生态”一词抹平差异。

## 练习

1. 做一张能力来源表：列出 MCP、extension tools、skills 三行，分别填“已核实事实”“待核实语义”“产品风险”。
2. 设计一个动态工具的上架流程：从发现、schema 校验、权限提示、试运行到审计记录，每步写清谁负责。
3. 比较“默认暴露所有工具”和“按需搜索工具”的成本：前者上下文重，后者发现慢；给出你的产品默认值。
4. 写一个反例：为什么不能把其他 agent 产品里的 skills 体验直接写成 Codex 官方能力。

## 事实核验清单

- [x] 已登记 MCP CLI 入口、MCP handler/exposure、dynamic tools、extension adapter、skills discovery/config、system skills 安装、skills instructions 和显式 skill 注入的机制级证据。
- [x] 已核实 skills 在目标 commit 的 TUI 中有用户可见入口，并有配置启停路径；但不把它和其他 agent 产品的 skills 概念混同。
- [x] 明确 extension tools 的用户入口、能力生命周期和统一治理语义仍待核实。
- [x] 明确不把 Claude Code skills 或其他平台概念写成 Codex 官方实现。
- [x] 核实 `skills` 有目标 commit 下的 TUI 用户入口、配置启停路径、内部 loader、config、instructions 和 system cache 机制。
- [ ] 核实 MCP 与 extension tools 是否共享同一工具治理路径。
