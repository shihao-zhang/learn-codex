## Why

`docs/diagram-style-guide.md` 已经把 SVG 教学辅助图规范沉淀为长期规则，s04 试点与 s01-s03 基础运行时 rollout 也验证了“Mermaid 主机制图 + SVG 可选辅助图”的方式。下一批应覆盖上下文与指令两章，因为这两类问题最容易被读者误解为“模型记忆差”或“agent 不听话”，实际需要区分上下文压力、摘要风险、指令来源和冲突处理。

本 change 的目标是推进第二批 SVG rollout：只给 s05 与 s06 各新增 1 张可选教学辅助 SVG 和 companion Markdown，让 AI 产品经理能更快看懂长任务继续/压缩/截断的取舍，以及 system / developer / user / `AGENTS.md` / 项目约束之间的冲突处理边界。

## What Changes

- 新增 s05 可选 SVG：展示 context pressure 下继续、压缩、截断、摘要风险与恢复选择。
- 新增 s06 可选 SVG：展示 system / developer / user / `AGENTS.md` / 项目约束之间的冲突处理。
- 每张 SVG 使用手写、可 diff、无外部依赖的 SVG，并包含 `<title>`、`<desc>`、可见图例或边界说明。
- 每张图配套 Markdown，记录 `Source Inputs`、`Event / Mechanism Mapping`、`Fact Boundary` 和 `Manual QA`。
- 更新 s05/s06 README，只增加“可选教学辅助 SVG”入口，继续保留 Mermaid 作为主机制图。

## Non-Goals

- 不替换或修改 s05/s06 的 `diagram.mmd`。
- 不更新 `docs/fact-snapshot.md`。
- 不修改 `docs/source-evidence.md`。
- 不修改 `scripts/check_docs.py`。
- 不改变章节状态。
- 不触碰 s08、s10、s12 的状态或语义边界。
- 不把 token 阈值、摘要保真字段、摘要质量、冲突案例、产品解释文案或 Python mock 写成 `openai/codex` 官方事实。
- 不使用图片生成模型、外部图片、字体文件、网络服务或导出流水线作为最终图来源。

## Capabilities

### Modified Capabilities

- `diagram-redraw-style-guide`: 按已规划的“上下文与指令”批次，为 s05-s06 增加可选 SVG 教学辅助图，并保持 Mermaid/SVG 分工和事实边界。

## Impact

- 新增图形资产：
  - `chapters/s05_context_window_compaction/diagrams/context-pressure.svg`
  - `chapters/s06_prompts_instructions/diagrams/instruction-conflict.svg`
- 新增 companion Markdown：
  - `chapters/s05_context_window_compaction/diagrams/context-pressure.md`
  - `chapters/s06_prompts_instructions/diagrams/instruction-conflict.md`
- 更新 s05/s06 README 的导航入口。
- OpenSpec 与仓库验证要求：
  - `openspec validate rollout-context-instruction-svgs --strict`
  - `openspec validate --all --strict`
  - XML parse 检查所有新增 SVG
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
