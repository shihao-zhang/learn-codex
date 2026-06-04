## Context

s11 面向 AI 产品经理解释“父任务如何安全拆给多个执行单元”。现有 README 已经把已核实范围收窄到源码机制：multi-agent tool surface、`AgentControl`/delegate、agent jobs CSV worker 和普通工具并行运行时。它也显式保留产品入口、默认启用条件、multi-agent v1/v2 体验差异和完整权限继承策略作为未闭环问题。

Mermaid 图继续承担主机制图职责。新增 SVG 只把 reader 最容易混淆的四件事放在同一张教学图中：

- delegate 会产生父子 thread / event 关系。
- 子 agent 事件需要回到父 session 被观察。
- approval 请求会转发回父 session，而不是在图中暗示子 agent 自行获得无限权限。
- CSV agent jobs 的并行 worker 与 result merge 是特定工具机制，不是通用子代理平台。

## Scope

本 change 只覆盖：

1. `chapters/s11_subagents_parallel_jobs/diagrams/subagents-parallel-jobs.svg`
2. `chapters/s11_subagents_parallel_jobs/diagrams/subagents-parallel-jobs.md`
3. `chapters/s11_subagents_parallel_jobs/README.md` 的可选 SVG 入口
4. `openspec/changes/rollout-subagents-svg/` 下的 proposal、design、tasks 和 spec delta

不触碰全局 README、roadmap、style guide、事实证据文件、检查脚本或章节状态。

## Source Inputs

本轮图形只使用以下输入：

- `AGENTS.md`
- `docs/diagram-style-guide.md`
- `chapters/s11_subagents_parallel_jobs/README.md`
- `chapters/s11_subagents_parallel_jobs/diagram.mmd`
- `chapters/s11_subagents_parallel_jobs/mock.py`
- `docs/source-evidence.md` 中已登记的 s11 机制证据
- `openspec/specs/review-scope-clarifications/spec.md`
- `openspec/specs/pending-chapter-verification/spec.md`

## Fact Boundary

- `FACT` 只用于已登记的 s11 源码机制：
  - multi-agent handler / `spawn_agent` tool surface。
  - `AgentControl` 生成、登记子 agent metadata 并发送初始输入。
  - `codex_delegate.rs` 的子 thread 事件转发与 approval 请求转回父 session。
  - agent jobs CSV item / worker / result 回填与导出。
  - `tools/parallel.rs` 的普通 tool call 并行运行时。
- `待核实` 必须用于默认启用条件、产品入口、multi-agent v1/v2 体验差异，以及完整权限继承策略。
- `TEACHING` / `教学辅助` 用于 result merge 解释、产品 UI 进度表达、mock trace、示例 job、读者侧风险提醒和边界文案。
- 本图不得把 s11 画成“OpenAI 官方通用子代理平台”，不得把 agent jobs 画成通用批处理 API，也不得把 tool parallel runtime 画成子 agent 并行。

## Drawing Rules

- 手写 SVG，保持源码可读、可 diff。
- 无外部图片、字体文件、网络或生成依赖。
- 中文优先；英文只用于路径、函数、schema、字段或源码追溯 chip。
- SVG 包含 `<title>` 与 `<desc>`，并在图内放可见图例和边界说明。
- 主阅读路径应是 `父任务 -> delegate / AgentControl -> 子 agent event -> result merge`。
- 审批转发和 CSV job worker 作为侧向机制解释，不压过主路径。
- 图中必须出现可见 `待核实` 标记，明确默认启用、产品入口和 v1/v2 体验仍需核实。

## Validation

完成前需要检查：

- OpenSpec tasks 全部完成。
- SVG XML 可解析，并包含 `<title>`、`<desc>` 和可见图例或边界说明。
- 渲染预览后确认主路径、侧向路径、文字、chip、箭头和图例可读。
- s11 README 仍把 `diagram.mmd` 放在“机制图”小节，SVG 只作为可选教学辅助入口。
- 不修改仓库 README、roadmap、`docs/diagram-style-guide.md`、`docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py` 或章节状态。
- 运行用户要求的全部命令：
  - `openspec validate rollout-subagents-svg --strict`
  - `openspec validate --all --strict`
  - XML parse 检查新增 SVG
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
