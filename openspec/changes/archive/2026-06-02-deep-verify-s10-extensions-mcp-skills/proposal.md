## Why

s10 已经登记了一批 MCP、dynamic tools、extension tools 和 skills 证据，但章节仍有一个关键风险：读者可能把名字相近的能力误读成同一个官方“扩展体系”，也可能把 adapter、handler 或路径存在误读成完整用户入口。

本 change 的目标是围绕 s10 做一次 focused deep verification：只用当前 fact snapshot 固定 SHA 的官方源码和 OpenAI 官方资料，拆开四类能力的入口、发现、配置、暴露和治理路径；能升级才升级，不能闭环则继续标注 `待核实` 并说明原因。

## What Changes

- 复核 s10 相关官方证据，但不更新 `docs/fact-snapshot.md` 的目标 commit，也不更新 `scripts/check_docs.py`。
- 分别核实并记录：
  - MCP：用户入口、server 配置、工具发现、runtime 暴露、handler 调用和治理线索。
  - dynamic tools：配置/来源、thread-scoped 暴露、请求/响应闭环和治理线索。
  - extension tools：extension registry、tool contributors、adapter 暴露和仍未闭环的安装/发现入口。
  - skills：用户入口、discovery roots、配置启停、instructions 注入、MCP dependency 提示和治理边界。
- 更新 `docs/source-evidence.md` 的 s10 证据项，使每条证据的“已核实范围”和“未解决问题”更细。
- 必要时更新 `chapters/s10_extensions_mcp_skills/README.md`，让章节状态和待核实原因与深度核验结果一致。

## Non-Goals

- 不处理 s08、diagram redraw、Phase 7 mock 或全仓重构。
- 不把候选新 commit 写成本轮官方证据来源；新 commit 只可作为后续追新风险说明。
- 不用 Claude Code、Codex Desktop、本 session plugin/skill 体验或其他 agent 产品行为证明 `openai/codex` 官方实现。
- 不把 MCP、dynamic tools、extension tools 和 skills 合并成一个官方产品概念。

## Capabilities

### New Capabilities

- `s10-extensions-mcp-skills-deep-verification`: 定义 s10 四类能力的分线核验、证据登记、状态判断和边界表达规则。

### Modified Capabilities

- 无。

## Impact

- 影响 `docs/source-evidence.md` 的 s10 证据登记。
- 可能影响 `chapters/s10_extensions_mcp_skills/README.md` 的状态说明、核心机制和事实核验清单。
- 不改变固定 SHA、release 核验值、全仓链接校验策略或教学 mock 的离线边界。
