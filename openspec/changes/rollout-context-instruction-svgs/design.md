## Context

本仓的读者是 AI 产品经理和 agent 平台设计者。s05 与 s06 处理的是 agent 长任务体验中最容易“看起来像模型问题、实际是 harness 与治理问题”的两组机制：

- s05：长任务中历史、工具输出、用户约束和当前任务不断挤占 context window，agent 需要选择继续、压缩、截断或请求恢复。
- s06：一次模型调用受到 system、developer、user、`AGENTS.md` 与项目约束共同影响，冲突时需要解释优先级和授权边界。

现有 Mermaid 图继续作为主机制图，但它不适合同时承载 FACT / 教学辅助 / 摘要风险 / 恢复选择 / 指令冲突案例。SVG 作为可选辅助图，可以把这些边界直接画出来。

## Scope

本 change 只覆盖上下文与指令两章：

1. `s05_context_window_compaction`
2. `s06_prompts_instructions`

每章新增 1 张核心教学 SVG 和 1 个 companion Markdown。README 只增加短入口，不改变章节状态、不新增官方事实、不调整主机制图。

## Source Inputs

本轮图形只使用以下输入：

- `AGENTS.md`
- `docs/diagram-style-guide.md`
- `chapters/s04_shell_sandbox_permissions/diagrams/permission-boundary.svg`
- `chapters/s04_shell_sandbox_permissions/diagrams/permission-boundary.md`
- s05/s06 的 README、`diagram.mmd` 和 `mock.py`
- `docs/source-evidence.md` 中已登记的 s05/s06 机制证据

## Fact Boundary

- s05 `FACT` 只标记已在 `docs/source-evidence.md` 登记的机制点：
  - compact 任务入口。
  - compact 后历史替换与 rollout 记录。
  - rollout truncation helper 作为截断边界证据入口，但不等同于完整 compaction 策略。
- s05 `教学辅助` 用于 context pressure 示例、固定 token 数字、阈值、保真字段、摘要质量、用户可见恢复建议和 mock trace。
- s06 `FACT` 只标记已在 `docs/source-evidence.md` 登记的机制点：
  - `AGENTS.md` 发现与组合。
  - 用户指令与 `AGENTS.md` 内容拼接。
  - 初始上下文注入多类指令。
- s06 `教学辅助` 用于冲突案例、授权解释文案、优先级可视化、项目约束示例和 mock trace。
- 本轮不主动引入 s08/s10/s12 语义；如图中需要提到 rollout/resume 或技能/插件，只能作为边界提醒，不能画成新增官方事实。

## Drawing Rules

- 手写 SVG，保持源码可读、可 diff。
- 无外部图片、字体文件、网络或生成依赖。
- 中文优先；英文只作为路径、字段、命令、layer 名称或 mock event 追溯标签。
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
- 渲染预览后确认主路径、侧向路径、文字、chip、箭头和图例可读。
- OpenSpec tasks 全部完成。
- s05/s06 README 仍把 Mermaid 放在“机制图”小节。
- 不修改 `docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py` 或章节状态。
- 运行用户要求的全部命令：
  - `openspec validate rollout-context-instruction-svgs --strict`
  - `openspec validate --all --strict`
  - XML parse 检查所有新增 SVG
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
