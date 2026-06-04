## Why

s08 已经补过 session、thread、rollout、resume/fork、thread-store 和 app-server 主链路的固定 SHA 证据，但章节状态仍然是 `待核实`。原因不是“没有任何证据”，而是产品语义未闭环：真实 remote thread-store backend、Codex Cloud/桌面端恢复语义，以及 experimental app-server API 的稳定承诺都不能从当前证据直接推出。

本 change 的目标是推进 SVG rollout C：为 `s08_sessions_threads_rollout` 新增 1 张可选教学辅助 SVG 和 companion Markdown。图的价值是帮助 AI 产品经理把 session、thread、rollout、resume、fork 的教学关系看清楚，同时更醒目地看到未闭环边界，避免把恢复链路误读成官方稳定产品能力。

## What Changes

- 新增 s08 可选 SVG：展示 session / thread / rollout / resume / fork 的教学关系。
- SVG 中显式标出 `待核实` 边界，尤其是：
  - remote thread-store backend。
  - Codex Cloud/桌面端恢复语义。
  - experimental app-server API 稳定承诺。
- SVG 保持手写、可 diff、无外部依赖，并包含 `<title>`、`<desc>`、可见图例或边界说明。
- 新增 companion Markdown，记录 `Source Inputs`、`Event / Mechanism Mapping`、`Fact Boundary` 和 `Manual QA`。
- 只更新 s08 README 的“可选教学辅助 SVG”入口，继续保留 Mermaid 作为主机制图。

## Non-Goals

- 不替换或修改 `chapters/s08_sessions_threads_rollout/diagram.mmd`。
- 不修改仓库根 README、roadmap 或 `docs/diagram-style-guide.md`。
- 不修改 `docs/fact-snapshot.md`、`docs/source-evidence.md` 或 `scripts/check_docs.py`。
- 不改变 s08 章节状态，状态必须保持 `待核实`。
- 不把 resume/fork、Codex Cloud、桌面端恢复、daemon/remote transport 或 remote thread-store 画成官方稳定产品能力。
- 不把 experimental app-server API 画成稳定公开接口承诺。
- 不使用图片生成模型、外部图片、字体文件、网络服务或导出流水线作为最终图来源。

## Capabilities

### Modified Capabilities

- `diagram-redraw-style-guide`: 按已规划的“会话与扩展”批次，为 s08 增加可选 SVG 教学辅助图，并保持 Mermaid/SVG 分工和待核实事实边界。

## Impact

- 新增图形资产：
  - `chapters/s08_sessions_threads_rollout/diagrams/session-thread-rollout.svg`
- 新增 companion Markdown：
  - `chapters/s08_sessions_threads_rollout/diagrams/session-thread-rollout.md`
- 更新 s08 README 的可选 SVG 入口。
- OpenSpec 与仓库验证要求：
  - `openspec validate rollout-s08-session-svg --strict`
  - `openspec validate --all --strict`
  - XML parse 检查新增 SVG
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
