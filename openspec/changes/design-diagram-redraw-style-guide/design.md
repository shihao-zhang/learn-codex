## Context

本轮目标是为“教学插图重绘”先建立轻量规范。读者是 AI 产品经理和 agent 平台设计者，所以图的重点不是画全模块，而是帮助人理解：

- 系统做到哪一步。
- 哪个状态由哪个面负责。
- 失败时为什么停下。
- 是否需要人类授权或改用低风险路径。
- 哪些关系是官方事实、待核实语义或教学抽象。

s12 是合适的 pilot 起点，因为它同时有综合 Mermaid 图、端到端 mock、happy/failure trace、额外 failure scenarios 和测试断言。它能暴露“总图”和“trace 图”之间的差异。

## s12 Inputs Reviewed

本轮阅读和运行的输入包括：

- `AGENTS.md`
- `README.md`
- `docs/roadmap.md`
- `docs/review-checklist.md`
- `chapters/s12_comprehensive_architecture/README.md`
- `chapters/s12_comprehensive_architecture/diagram.mmd`
- `chapters/s12_comprehensive_architecture/mock.py`
- `src/learn_codex_mock/runtime.py`
- `tests/test_chapter_mocks.py`
- `tests/test_run_all.py`
- `scripts/run_all.py`

runner 输出显示 s12 的主线检查覆盖：

- happy path：8 个 events。
- failure path：6 个 events。
- 全仓 runner：24 条 happy/failure paths，共 94 个 events。

s12 额外 scenario 已通过 `--scenario` 暴露，但不是 `scripts/run_all.py` 的默认路径：

- `tool_dispatch_error`
- `permission_denied`
- `context_pressure`
- `instruction_conflict`
- `session_recovery`

## What s12 Needs To Express Visually

### Nodes

s12 现有 Mermaid 图表达了结构总览。未来 pilot 图需要在此基础上区分两类节点。

架构层节点：

- `User`
- `Product surface`
- `App-server + protocol`
- `CLI harness entry`
- `Core runtime`
- `Model + config + auth`
- `Context window / compaction`
- `Tool registry / router / handlers`
- `Sandbox + permissions`
- `Tool observations`
- `Protocol events`
- `Session / thread / rollout state`
- `Extensions / MCP / skills`
- `Subagents / parallel jobs`
- `Teaching abstraction note`

trace 层节点：

- `input`
- `instruction`
- `context`
- `tool_dispatch`
- `permission`
- `tool_result`
- `boundary`
- `answer`
- `failure`
- `recovery`
- `resume`
- `instruction_conflict`

### States

这些状态适合用小标签或状态 chip 表达，而不是画成主节点：

- `teaching_session_id`
- `teaching_checkpoint`
- `fact_boundary=teaching_abstract`
- `network_allowed=False`
- `context_budget_state`
- `permission_decision=allow / deny / allow_after_explanation`
- `handler_called=False`
- `external_state=False`
- `openai_api_called=False`
- `s08_boundary=待核实`
- `s10_boundary=待核实`
- `status=complete / partial / needs_human_choice / blocked_by_boundary / resumed`
- `recovery_choice`
- `decision_reason`

### Failure Paths

s12 真正需要图形化的 failure path 有六类：

1. 综合 failure：请求 live network / desktop state，但 teaching registry 没有 approved offline handler；网络 fallback 被 denied；上下文接近压力线；项目 offline 规则胜出；runtime 返回需要人类选择的 recovery。
2. 工具路由失败：模型请求 `desktop_screen_capture`，router 找不到 deterministic teaching handler，返回 recoverable tool dispatch error，并解释不会调用真实桌面状态。
3. 权限拒绝：任务要求写 workspace 外部，teaching policy 先拒绝，write handler 不被调用，系统提供 workspace-only 替代方案并标注需要人类授权。
4. 上下文压力：固定教学预算接近上限，旧 trace 被替换成 `teaching_summary`，答案带 lossy summary warning。
5. 指令冲突：project offline 规则与 user network lookup 请求冲突，project 层胜出，系统要求离线 fixture 或单独授权路径。
6. session recovery：从 teaching checkpoint 恢复，已完成 fixture read 不重复执行，s08/s10 继续标注 `待核实`，最终恢复控制权。

现有 Mermaid 适合表达第一层架构关系，但不适合单独承载这些 event-level 状态和 recovery 解释。s12 pilot 应优先画 trace，而不是重画完整架构宇宙。

## Method Comparison

| 方式 | 优点 | 风险 | 本仓定位 |
| --- | --- | --- | --- |
| Mermaid | 可维护、可 diff、与现有章节一致，适合机制草图。 | 复杂状态、图例、分层视觉、failure path 表达能力有限。 | 继续作为章节机制图主入口，不在本轮替换。 |
| 手写 SVG | 可精确控制视觉层级、颜色、badge、编号和线型；纯文本、可 diff、无外部生成依赖。 | 复杂图会冗长，人工维护成本高。 | 推荐作为 s12 pilot 和少量高价值教学插图的主方案。 |
| HTML/CSS 导出 SVG/PNG | 样式系统强，适合统一 tokens、复杂排版和后续自动化导出。 | 引入渲染链路和二进制导出物，review 成本变高；需要另开工具链决策。 | 作为备选方案，等 pilot 稳定或图量变多后再评估。 |
| GPT 图片生成 | 快速产生氛围图或封面感视觉。 | 文本不稳定、难 diff、难保证事实边界，容易把教学抽象画成事实。 | 不用于机制图或事实图；最多作为非事实装饰图，且需人工重绘和标注。 |

## Recommendation

主方案：手写 SVG，保留 Mermaid。

理由：

- 符合本仓“事实边界可审查”的要求：SVG 是文本，review 能看到标签、编号和 disclaimer。
- 不新增依赖，不需要网络，不使用 GPT 图片生成。
- 能清楚表达 `官方事实 / 待核实 / 教学抽象` 三种边界。
- 适合 s12 这种端到端 trace 小样：少量节点、强编号、强图例，比完整重画所有章节更稳。
- 不破坏现有 Mermaid 图；Mermaid 继续承载机制总览，SVG 只作为教学插图 pilot。

备选方案：HTML/CSS 源文件导出 SVG/PNG。

适用条件：

- 后续确认需要多张同风格插图。
- 需要更复杂的响应式布局、自动编号或统一设计 tokens。
- 愿意新增并维护渲染检查流程。

不建议把 GPT 图片生成作为本仓机制图方案。它可以启发构图，但不能作为事实图源文件。

## Lightweight Visual Spec

### Graphic Hierarchy

图分四层：

1. 读者任务层：用户目标、产品问题、当前 trace 名称。
2. 责任面层：product surface、protocol boundary、core runtime、tool/permission、context/session、extension/parallel pending。
3. 事件层：按 mock trace 编号的 event cards，例如 H1-H8 或 F1-F6。
4. 状态层：小型 chips 展示 `decision_reason`、`permission_decision`、`context_budget_state`、`recovery_choice` 等。

不要把所有 detail 都画成同级节点。PM 第一眼应先看到路径，第二眼再读状态。

### Display Language

面向读者的展示层必须中文优先：

- 图题、节点标题、节点说明、图例和边界说明使用中文。
- 英文保留给路径、命令、schema 字段、mock event kind、OpenSpec/README/SVG/Mermaid 等项目约定名。
- 需要追溯到 mock trace 时，用小号 monospace chip 保留英文原字段，例如 `tool_dispatch`、`permission_decision=deny`、`needs_human_choice`。
- 不要把英文 event kind 直接当作主视觉标题；主标题应翻译成读者能立即理解的机制名，例如 `工具路由`、`权限判断`、`恢复选择`。
- 中英文混排时，中文承担解释，英文承担定位；不要反过来。

### Color Semantics

颜色不能作为唯一语义，必须同时配合文字 badge、线型或形状。

| 语义 | 建议颜色 | 线型 / 标记 |
| --- | --- | --- |
| 官方事实 | `#176B87` | 实线边框，badge：`FACT` |
| 待核实 | `#B7791F` | 虚线边框，badge：`待核实` |
| 教学抽象 | `#6B5B95` | 点线边框，badge：`TEACHING` |
| failure / deny | `#C2410C` | 粗实线或 stop marker，badge：`DENY` / `FAIL` |
| recovery / human choice | `#2563EB` | 回环箭头，badge：`RECOVERY` |
| 普通状态 | `#475569` | 细边框，chip 文本 |
| 背景 | `#F8FAFC` | 仅用于画布底色 |
| 主文本 | `#111827` | 高对比正文 |

### Fact Boundary Markers

每张重绘图必须出现边界图例。节点和边的标记规则：

- `FACT`：只用于能追到固定 SHA OpenAI 源码、OpenAI 官方文档或 release note 的机制点。
- `待核实`：用于 s08/s10 等现有章节状态未升级的语义，或只有路径证据但未形成行为闭环的机制。
- `TEACHING`：用于跨章总图、mock trace、固定预算、教学 checkpoint、教学 permission table、个人推断形成的解释图。

如果一个节点混合多种来源，默认降级到更保守标记。例如 “session recovery 教学 checkpoint” 应标 `TEACHING`，并对 s08 相关语义加 `待核实` chip。

### Failure Path

failure path 使用“红色原因线 + 蓝色恢复线”：

- 失败边只标事实发生点和停止原因，例如 `tool_not_registered`、`permission_decision=deny`。
- recovery 边必须指向人类可理解的下一步，例如 `use_offline_fixture`、`request_authorization`、`workspace_only_alternative`。
- 不画会误导读者的自动成功路径。若需要授权，必须显式标 `human choice`。
- 对有副作用风险的动作，画出 “not invoked” 或 “skipped effect”，避免读者以为动作已执行。

### Legend And Numbering

编号必须服务 trace 可追责：

- happy path 使用 `H1` 到 `H8`，对应 s12 happy trace index。
- failure path 使用 `F1` 到 `F6`，对应 s12 failure trace index。
- 额外场景使用短前缀：
  - `TD`：tool dispatch error
  - `P`：permission denied
  - `C`：context pressure
  - `I`：instruction conflict
  - `R`：session recovery
- 每张图底部保留 legend，至少解释“官方事实 / FACT”、“待核实”、“教学抽象 / TEACHING”、“失败/拒绝”、“恢复选择”。
- 图题应包含章节和用途，例如 `s12 小样：失败路径 trace`，不要写成官方架构图。

### File Organization

本 change 不落地 SVG 文件。后续如果进入 pilot，建议使用：

```text
chapters/s12_comprehensive_architecture/diagrams/
  pilot-trace.svg
  pilot-trace.md
```

规则：

- 不替换 `chapters/s12_comprehensive_architecture/diagram.mmd`。
- `pilot-trace.md` 记录图的输入 trace、边界标记和人工检查项。
- 如果后续采用 HTML/CSS 导出方案，再另开 change 增加 `source.html` 和导出脚本。
- 全仓通用规范稳定后，再考虑抽到 `docs/diagram-style-guide.md`。
- 官方机制证据仍统一登记到 `docs/source-evidence.md`，不要为插图新建分散 sources 文件。

## s12 Pilot Draft

建议第一张小样不是完整架构图，而是 `s12 pilot: failure trace`：

- 左侧：用户请求 live network / desktop state。
- 中段：tool dispatch 找不到 offline handler，permission deny，context pressure，instruction conflict。
- 右侧：recovery choices，明确 `needs_human_choice`。
- 底部：边界图例，标明本图是 `TEACHING`，s08/s10 相关语义保持 `待核实`。

第二张小样可以是 `s12 pilot: happy trace`：

- 展示 H1-H8 的主线，突出 offline fixture read、permission allow、boundary chips、final answer。
- 用较少节点帮助读者对照 failure trace。

本轮不生成这两张图，只完成规范和草案。

## Parallel Work And Blockers

适合并行推进：

- 梳理每章 Mermaid 图里哪些节点是官方事实、待核实或教学抽象。
- 为 s12 pilot 准备 trace storyboard，不动正式图。
- 定义 SVG badge、颜色 token、legend 文案和人工 QA 清单。
- 检查现有 README 是否已清楚标注 mock/diagram 的非官方边界。

必须等 Phase 7 implementation 完成并被 review 后再做：

- 用 integrated trace 自动生成或半自动生成插图。
- 把 s12 pilot 图写入章节 README 主路径。
- 推广到 s01-s12 的全量重绘。
- 新增渲染脚本、截图测试或图片导出流水线。
- 把 mock 的额外 scenario 当作全仓稳定验收入口。

## Risks / Trade-offs

- [Risk] SVG 画得太精致，读者误以为是官方架构图。缓解：图题、legend 和 badge 都标注 `TEACHING`。
- [Risk] 颜色语义被单独依赖，色弱读者不易分辨。缓解：颜色必须配合文字和线型。
- [Risk] pilot 过早扩散为全仓重绘。缓解：只从 s12 trace 小样开始，保留 Mermaid。
- [Risk] 把 Codex 桌面端体验或 GPT 生成图写成官方事实。缓解：只作为问题启发，不能作为图中 `FACT`。
