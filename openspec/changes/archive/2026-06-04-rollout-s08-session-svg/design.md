## Context

s08 的核心难点是“局部源码路径已能解释很多机制，但产品恢复语义仍不能闭环”。对读者来说，session、thread、rollout、resume 和 fork 很容易被自然脑补成一个稳定恢复产品链路；这正是本图要避免的误读。

因此本轮图形不追求画出完整数据流，而是画出三层关系：

1. 教学概念层：session 是一次运行/交互身份的心智入口，thread 是对话或任务线索，rollout 是可回放历史表面。
2. 局部证据层：固定 SHA 已覆盖 id 生成、local/in-memory store、rollout replay、app-server resume/fork、exec/TUI/debug-client app-server API 路径等局部机制。
3. 未闭环边界层：remote thread-store backend、Codex Cloud/桌面端恢复语义、experimental app-server API 稳定承诺仍为 `待核实`。

## Scope

本 change 只覆盖 `chapters/s08_sessions_threads_rollout`：

- 新增 1 张 SVG。
- 新增 1 个 companion Markdown。
- 更新 s08 README 的短入口。

不调整章节状态、证据文件、风格指南或主 Mermaid 图。

## Source Inputs

本轮图形只使用以下输入：

- `AGENTS.md`
- `docs/diagram-style-guide.md`
- `chapters/s08_sessions_threads_rollout/README.md`
- `chapters/s08_sessions_threads_rollout/diagram.mmd`
- `chapters/s08_sessions_threads_rollout/mock.py`
- `docs/source-evidence.md` 中已登记的 s08 机制证据
- 已有 s01-s06 SVG 与 companion Markdown 的文件组织和标注方式

## Fact Boundary

- s08 README 的状态保持 `待核实`。
- 图中如出现 `FACT`，只能表示“局部固定 SHA 机制证据”，不能表示整章已核实，也不能表示稳定产品能力。
- session/thread id 生成、local/in-memory ThreadStore、rollout replay、app-server resume/fork、exec/TUI/debug-client app-server API 路径可以作为局部证据底座，但要配合 `待核实` 章节边界。
- remote thread-store backend 必须显式标 `待核实`。
- Codex Cloud/桌面端恢复语义必须显式标 `待核实`。
- experimental app-server API 稳定承诺必须显式标 `待核实`。
- resume/fork 只能表达源码路径和教学关系，不得画成官方稳定恢复产品能力。
- Mermaid 仍是 s08 主机制图；SVG 只是可选教学辅助图。

## Drawing Rules

- 手写 SVG，保持源码可读、可 diff。
- 无外部图片、字体文件、网络或生成依赖。
- 中文优先；英文只作为路径、字段、命令、API 名或 traceability chip。
- SVG 包含 `<title>` 和 `<desc>`，并在图中放可见图例或边界说明。
- `待核实` 不只靠颜色表达，还要用 badge、虚线或边界框表达。
- companion Markdown 固定包含：
  - `Source Inputs`
  - `Event / Mechanism Mapping`
  - `Fact Boundary`
  - `Manual QA`

## Validation

完成前需要检查：

- XML 可解析，且 SVG 含 `<title>`、`<desc>` 和可见图例或边界说明。
- 渲染预览后确认主路径、侧向路径、文字、chip、箭头和图例可读。
- OpenSpec tasks 全部完成。
- s08 README 仍把 Mermaid 放在“机制图”小节，SVG 只作为可选入口。
- 不修改仓库根 README、roadmap、`docs/diagram-style-guide.md`、`docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py`。
- s08 状态仍是 `待核实`。
- 运行用户要求的全部命令：
  - `openspec validate rollout-s08-session-svg --strict`
  - `openspec validate --all --strict`
  - XML parse 检查新增 SVG
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
