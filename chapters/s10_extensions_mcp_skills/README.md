# s10_extensions_mcp_skills

## 状态标签

状态：待核实

## 本章回答什么

本章回答“能力如何进入 agent 平台”的设计问题。当前已核实四条不同能力线：MCP、dynamic tools、extension tools 和 skills directory。它们在源码里有不同入口、配置、暴露和治理路径，不能因为名字都像“扩展能力”就合并成一个官方产品概念。

章节状态仍保持待核实，不是因为所有机制都缺证据，而是因为通用 extension tools 的用户安装/发现入口未闭环，dynamic tools 目前定位为 app-server experimental API，且四条能力线没有被证明共享同一条治理路径。因此本章仍不会把源码路径存在直接写成完整扩展产品能力，也不会把 Claude Code、Codex 桌面端插件体验或其他 agent 产品的 skills 概念套到 `openai/codex`。

## 对产品与平台设计的意义

扩展面决定一个 agent 平台能否从“内置工具集合”成长为“可治理的能力生态”。产品上要同时解决四件事：

- 发现：agent 怎么知道有哪些外部能力可用，能力描述是否足够让模型正确选择。
- 暴露：哪些能力进入当前 turn，哪些延迟加载，哪些只在特定上下文出现。
- 治理：外部能力如何经过权限、审批、审计、速率限制和数据边界。
- 体验：用户看到的是一个稳定工具，还是一个来源复杂、失败方式各异的插件集合。

本章的关键权衡是：能力越开放，生态越强；能力越动态，安全审查、可解释性和调试成本越高。

## 机制图

见 [diagram.mmd](diagram.mmd)。图把 MCP、dynamic tools、extension tools、skills 先画成不同能力来源，再进入发现、工具规范、治理和运行时；其中多条 runtime adapter 已有机制证据，但跨客户端语义、通用 extension 用户入口和统一治理边界仍待核实。

## 运行 mock

```bash
python3 chapters/s10_extensions_mcp_skills/mock.py --demo
```

教学 mock 只演示“能力来源 -> 工具描述 -> 策略检查 -> 调用结果”的产品化流程，不代表 Codex 官方扩展机制、MCP wire format、skills 语义或真实权限实现。

## 核心机制

- `MCP`：已核实 Codex CLI 有 `codex mcp` / `codex mcp-server` 用户入口；`mcp add/remove` 会改全局配置；配置结构覆盖 stdio/http transport、enabled/required、tool allow/deny、per-tool approval 和 OAuth 相关字段。runtime 会刷新 MCP manager、读取 tools、按直接/延迟暴露策略加入 tool router；MCP handler 实现 `ToolExecutor`，并根据 read-only hint 或 server opt-in 决定是否支持并行。审批侧能看到 elicitation、guardian review 和自动批准条件，但这不等于每个 MCP server 的失败恢复都已核完。
- `dynamic tools`：源码显示 app-server 的 `thread/start.dynamicTools` 是 experimental API；thread start 会校验 namespace/name，传入 core session，handler 把 `DynamicToolSpec` 转为 tool spec，调用时通过 dynamic tool request/response event 与外部客户端闭环。它不是已核实的 CLI 用户可手动创建工具入口。
- `extension tools`：源码显示 extension registry 可注册 tool contributors，app-server 会安装一组内置 extensions，core 会收集 contributors 并通过 adapter 放入 tool runtime。已闭环的是“内置 extension tool contributor 到 runtime”的路径；未闭环的是通用 extension 的用户安装、发现、授权和市场/插件式入口。
- `skills directory`：当前目标 commit 的 TUI 源码显示 skills 有 `/skills` 菜单、`$`/`@` 技能列表入口、启停技能 UI；loader/config 源码显示 repo/user/admin/system/plugin roots、配置启停规则、system skills cache、available skills instructions、显式 mention 注入和 MCP dependency 提示。该证据不等于所有客户端都有同样入口。
- `tool surface governance`：产品层可以用同一组问题审视这些能力：谁声明、谁授权、谁执行、谁记录、失败时谁负责。但源码证据显示四条能力线的治理实现不同，不能直接合并成一条“插件生态”官方事实。

## 真实 Codex 映射

- [codex-rs/core/src/tools/handlers/mcp.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/mcp.rs)
- [codex-rs/core/src/mcp_tool_exposure.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/mcp_tool_exposure.rs)
- [codex-rs/core/src/tools/handlers/extension_tools.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/extension_tools.rs)
- [codex-rs/core/src/tools/handlers/dynamic.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/dynamic.rs)
- [codex-rs/skills/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/skills/src)

这些 permalink 是本章入口锚点，不自动证明四者属于同一个产品语义或治理体系。更细的机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)。

当前可核实的事实包括 MCP CLI/config/exposure/handler/elicitation 路径、dynamic tools experimental app-server thread flow、内置 extension tool contributor 到 runtime 的 adapter 路径、skills discovery/config/instructions/explicit injection。章节待核实点集中在通用 extension 用户入口、dynamic tools 的客户端产品边界，以及这些能力是否能统一称为同一扩展体系。

## 教学简化与生产差异

本章故意采用保守写法：先讲平台设计中的扩展面问题，再把 Codex 映射限制在已登记路径。

- 教学 mock 会把所有扩展统一成同一种 `ToolSpec`，真实实现已经能看到不同 adapter、事件、权限和生命周期线索，不能用 mock 抹平差异。
- 图中的 `skills` 现在可以写成目标 commit 下 TUI 可见、配置可管理的 skills 能力，但不能借此套用 Claude Code skills、Codex 桌面端插件体验或其他平台语义。
- 如果后续更换目标 commit 后发现 `skills` 用户入口发生重大变化，本章需要重新走事实快照和 OpenSpec 核验。
- 如果后续核实发现 MCP、dynamic tools、extension tools、skills 的治理路径可以被稳定归纳，才能再考虑状态升级；否则应继续拆成独立小节，避免用“插件生态”一词抹平差异。

## 练习

1. 做一张能力来源表：列出 MCP、dynamic tools、extension tools、skills 四行，分别填“已核实事实”“待核实语义”“产品风险”。
2. 设计一个动态工具的上架流程：从发现、schema 校验、权限提示、试运行到审计记录，每步写清谁负责。
3. 比较“默认暴露所有工具”和“按需搜索工具”的成本：前者上下文重，后者发现慢；给出你的产品默认值。
4. 写一个反例：为什么不能把其他 agent 产品里的 skills 体验直接写成 Codex 官方能力。

## 事实核验清单

- [x] 已拆开 MCP、dynamic tools、extension tools、skills 四条路径，分别登记入口、配置、暴露、运行时和治理证据。
- [x] 已核实 MCP CLI/config/exposure/handler/elicitation 的主要路径，但不把它扩写成所有 server 的稳定产品体验。
- [x] 已核实 dynamic tools 的 app-server experimental thread flow，但不把它写成 CLI 用户创建工具入口。
- [x] 已核实 extension registry、内置 app-server extensions 和 adapter 进入 runtime 的路径，但不把它写成通用用户插件市场能力。
- [x] 已核实 skills 在目标 commit 的 TUI 中有用户可见入口，并有配置启停、loader、instructions、system cache、显式注入和 MCP dependency 提示路径。
- [x] 明确不把 Claude Code skills 或其他平台概念写成 Codex 官方实现。
- [ ] 核实通用 extension tools 是否存在用户安装/发现/授权入口。
- [ ] 核实 dynamic tools 的 app-server client 产品边界和 experimental API 稳定性。
- [ ] 核实 MCP、dynamic tools、extension tools、skills 是否能共享同一治理路径；当前证据不支持合并表述。
