## Why

`promote-diagram-style-guide` 已经把 SVG 教学辅助图规范沉淀到 `docs/diagram-style-guide.md`，并用 s04 的 shell 权限边界图验证了低风险试点方式。基础运行时三章 s01-s03 是读者理解 agent harness 的入口，但目前只有 Mermaid 主机制图，缺少能把 loop、protocol event 和 tool dispatch 的事实边界、教学简化和产品理解问题同时讲清的辅助图。

本 change 的目标是推进第一批 SVG rollout：只给 s01-s03 各新增 1 张可选教学辅助 SVG 和 companion Markdown，让读者在不替换 Mermaid、不新增官方事实的前提下，更快理解基础运行时路径。

## What Changes

- 新增 s01 可选 SVG：解释一个 turn 中“用户输入 -> 模型动作 -> 工具调用 -> observation -> 继续/停止”的循环。
- 新增 s02 可选 SVG：解释 request / response / event / trace item 如何帮助产品界面理解 agent 行为。
- 新增 s03 可选 SVG：解释工具声明、registry、router、handler 和结果回写的受控分发链路。
- 每张 SVG 使用手写、可 diff、无外部依赖的 SVG，并包含 `<title>`、`<desc>`、可见图例或边界说明。
- 每张图配套 Markdown，记录 `Source Inputs`、`Event / Mechanism Mapping`、`Fact Boundary` 和 `Manual QA`。
- 更新 s01-s03 README，只增加“可选教学辅助 SVG”入口，继续保留 Mermaid 作为主机制图。

## Non-Goals

- 不替换或修改 s01-s03 的 `diagram.mmd`。
- 不更新 `docs/fact-snapshot.md`。
- 不修改 `docs/source-evidence.md`。
- 不修改 `scripts/check_docs.py`。
- 不改变章节状态。
- 不触碰 s08、s10、s12 的状态或语义边界。
- 不把 Codex Desktop 观察、Python mock、示例工具名、UI 呈现建议或 SVG 表达写成 `openai/codex` 官方事实。
- 不使用图片生成模型、外部图片、字体文件、网络服务或导出流水线作为最终图来源。

## Capabilities

### Modified Capabilities

- `diagram-redraw-style-guide`: 按已推广的第一批节奏，为基础运行时 s01-s03 增加可选 SVG 教学辅助图，并保持 Mermaid/SVG 分工。

## Impact

- 新增图形资产：
  - `chapters/s01_agent_loop/diagrams/turn-loop.svg`
  - `chapters/s02_protocol_events/diagrams/event-interface.svg`
  - `chapters/s03_tool_registry_dispatch/diagrams/tool-dispatch.svg`
- 新增 companion Markdown：
  - `chapters/s01_agent_loop/diagrams/turn-loop.md`
  - `chapters/s02_protocol_events/diagrams/event-interface.md`
  - `chapters/s03_tool_registry_dispatch/diagrams/tool-dispatch.md`
- 更新 s01-s03 README 的导航入口。
- OpenSpec 验证要求：
  - `openspec validate rollout-foundation-runtime-svgs --strict`
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
