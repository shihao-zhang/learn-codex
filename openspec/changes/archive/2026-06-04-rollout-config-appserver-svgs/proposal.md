## Why

`docs/diagram-style-guide.md` 已规划“工具与权限”批次：s04、s07、s09。s04 已完成 SVG 试点，s07 与 s09 是同一批里最容易被产品读者误解的两章：一个把“选模型”误看成 UI 偏好，另一个把 app-server 误看成完整云端产品架构。

本 change 的目标是推进 SVG rollout A：为 s07 和 s09 各新增 1 张可选教学辅助 SVG 和 companion Markdown。Mermaid 继续作为主机制图；SVG 只帮助读者看清配置/认证/模型选择的影响面，以及 app-server/protocol/product surface 之间的状态同步边界。

## What Changes

- 新增 s07 可选 SVG：展示 config、auth、provider/model 选择如何影响成本、能力、合规和可用性。
- 新增 s09 可选 SVG：展示 app-server、protocol、product surface 的状态同步边界。
- 每张 SVG 使用手写、可 diff、无外部依赖的 SVG，并包含 `<title>`、`<desc>`、可见图例或边界说明。
- 每张图配套 Markdown，记录 `Source Inputs`、`Event / Mechanism Mapping`、`Fact Boundary` 和 `Manual QA`。
- 更新 s07/s09 README，只增加“可选教学辅助 SVG”入口，继续保留 Mermaid 作为主机制图。

## Non-Goals

- 不替换或修改 s07/s09 的 `diagram.mmd`。
- 不修改仓库根 README、`docs/roadmap.md` 或 `docs/diagram-style-guide.md`。
- 不更新 `docs/fact-snapshot.md`。
- 不修改 `docs/source-evidence.md`。
- 不修改 `scripts/check_docs.py`。
- 不改变任何章节状态。
- 不把最新模型可用性、默认模型、真实计费、企业合规策略、客户端 UI 命名、多端体验或 Codex Cloud 行为写成 `openai/codex` 官方事实。
- 不使用图片生成模型、外部图片、字体文件、网络服务或导出流水线作为最终图来源。

## Capabilities

### Modified Capabilities

- `diagram-redraw-style-guide`: 按已规划的“工具与权限”批次，为 s07/s09 增加可选 SVG 教学辅助图，并保持 Mermaid/SVG 分工和事实边界。

## Impact

- 新增图形资产：
  - `chapters/s07_config_auth_models/diagrams/model-choice-impact.svg`
  - `chapters/s09_app_server_transport/diagrams/state-sync-boundary.svg`
- 新增 companion Markdown：
  - `chapters/s07_config_auth_models/diagrams/model-choice-impact.md`
  - `chapters/s09_app_server_transport/diagrams/state-sync-boundary.md`
- 更新 s07/s09 README 的导航入口。
- OpenSpec 与仓库验证要求：
  - `openspec validate rollout-config-appserver-svgs --strict`
  - `openspec validate --all --strict`
  - XML parse 检查所有新增 SVG
  - 渲染预览新增 SVG，确认主路径、侧向路径、文字、chip、箭头和图例可读
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
