## Why

Phase 5 需要优先收敛 s10，因为 MCP、extension tools、skills instructions 和 tool registry 很容易被写成同一个“插件体系”，也容易把源码路径存在误写成 CLI 用户可见能力。

本 change 的目标是补强 s10 事实证据，并在无法闭环时继续保持 `待核实`，让读者清楚知道哪些是已核实机制、哪些仍不能升级为官方能力声明。

## What Changes

- 核实 s10 范围内的 MCP handler、extension tool adapter、skills instructions、tool registry 和 CLI 用户可见入口。
- 更新 `docs/source-evidence.md` 的 s10 证据项，补齐固定 SHA permalink、核实范围和未解决问题。
- 必要时收窄 `chapters/s10_extensions_mcp_skills/README.md` 的边界语言，避免把 `skills` 写成已确认 CLI 一等能力。
- 明确不使用 Claude Code skills、Codex 桌面端插件体验或其他 agent 产品经验来证明 `openai/codex` 官方实现。
- 默认不升级章节状态；只有当 CLI 入口、配置、触发规则和官方文档/源码证据都能闭环时，才提出状态升级。

## Capabilities

### New Capabilities

- `s10-extensions-mcp-skills-verification`: 定义 s10 事实核验、证据登记、边界收窄和状态判断规则。

### Modified Capabilities

- 无。

## Impact

- 影响 `docs/source-evidence.md` 的 s10 证据登记。
- 可能影响 `chapters/s10_extensions_mcp_skills/README.md` 的状态说明、核心机制和事实核验清单。
- 可能影响 `docs/fact-snapshot.md` 的待核实队列文字，但不改变目标 commit。
- 不引入 OpenAI API 调用，不调用外部 review 服务，不改变教学 mock 的离线约束。
