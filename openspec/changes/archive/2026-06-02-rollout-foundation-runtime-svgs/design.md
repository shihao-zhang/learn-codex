## Context

本仓的读者是 AI 产品经理和 agent 平台设计者。s01-s03 是他们进入 agent harness 的第一组心智模型：

- s01：agent loop 不是一次性聊天，而是模型动作、工具调用和 observation 回填的循环。
- s02：protocol event 不是日志，而是客户端理解运行时状态的契约。
- s03：tool registry/dispatch 不是任意函数调用，而是工具声明、路由、handler 和结果回写的受控链路。

现有 Mermaid 图继续作为主机制图，但它不适合同时承载事实边界、教学简化、UI 建议和 mock trace 字段。SVG 作为可选辅助图，可以把这些边界直接画出来。

## Scope

本 change 只覆盖基础运行时三章：

1. `s01_agent_loop`
2. `s02_protocol_events`
3. `s03_tool_registry_dispatch`

每章新增 1 张核心教学 SVG 和 1 个 companion Markdown。README 只增加短入口，不改变章节状态、不新增官方事实、不调整主机制图。

## Source Inputs

本轮图形只使用以下输入：

- `docs/diagram-style-guide.md`
- `chapters/s04_shell_sandbox_permissions/diagrams/permission-boundary.svg`
- `chapters/s04_shell_sandbox_permissions/diagrams/permission-boundary.md`
- s01-s03 的 README、`diagram.mmd` 和 `mock.py`
- `docs/source-evidence.md` 中已登记的 s01-s03 机制证据

## Fact Boundary

- `FACT` 只标记已在 `docs/source-evidence.md` 登记的机制点：
  - s01：submission loop 入口、tool call 路由/observation 回写、conversation item 记录。
  - s02：`Event` / `EventMsg` 协议边界、模型输入输出项、trace context 字段入口。
  - s03：router 参数与模型可见工具规格、registry 构造、pre/post hook、handler 调用和结果回写。
- `TEACHING` / `教学辅助` 用于 mock event、简化时序、示例工具名、示例参数、UI 呈现建议和产品解释。
- 本轮 s01-s03 不主动引入 s08/s10/s12 语义，因此不为了图例完整硬塞 `待核实`。
- 如果图中出现失败或拒绝，只限于教学 failure path；不声明官方错误码、真实文案或任意输入的真实分类规则。

## Drawing Rules

- 手写 SVG，保持源码可读、可 diff。
- 无外部图片、字体文件、网络或生成依赖。
- 中文优先；英文只作为路径、字段、mock event 或 schema 追溯标签。
- 每张 SVG 包含 `<title>` 和 `<desc>`，并在图中放可见图例或边界说明。
- Mermaid 继续是 README 的主机制图入口；SVG 标为“可选教学辅助 SVG”。
- companion Markdown 固定包含：
  - `Source Inputs`
  - `Event / Mechanism Mapping`
  - `Fact Boundary`
  - `Manual QA`

## Validation

完成前需要检查：

- XML 可解析，且每张 SVG 含 `<title>`、`<desc>` 和可见图例或边界说明。
- OpenSpec tasks 全部完成。
- s01-s03 README 仍把 Mermaid 放在“机制图”小节。
- 不修改 `docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py` 或章节状态。
- 运行用户要求的全部命令：
  - `openspec validate rollout-foundation-runtime-svgs --strict`
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
