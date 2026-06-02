## Why

`docs/diagram-style-guide.md` 已经把 s10 放在“会话与扩展”批次，并明确要求 s10 的 MCP、extensions、skills、dynamic tools 必须显式标 `待核实`，不能被画成统一官方产品承诺。s10 README 已完成深核验后的保守文字，但读者仍需要一张能把四条能力线的来源、入口、治理和待核实边界并排看清的教学辅助图。

本 change 的目标是推进 SVG rollout D：只给 `s10_extensions_mcp_skills` 新增 1 张可选教学辅助 SVG 和 companion Markdown。图的重点不是补新事实，而是帮助 AI 产品经理区分“源码中已能追到的路径”和“还不能升级成稳定产品语义的边界”。

## What Changes

- 新增 s10 可选 SVG：并排展示 MCP、dynamic tools、extension tools、skills 四条能力线的来源、入口、治理与待核实边界。
- 新增 companion Markdown：记录 `Source Inputs`、`Event / Mechanism Mapping`、`Fact Boundary` 和 `Manual QA`。
- 更新 s10 README，只增加“可选教学辅助 SVG”入口，继续保留 Mermaid 作为主机制图。
- SVG 使用手写、可 diff、无外部依赖的 XML，并包含 `<title>`、`<desc>`、可见图例和边界说明。

## Non-Goals

- 不替换或修改 s10 的 `diagram.mmd`。
- 不修改根 `README.md`、`docs/roadmap.md` 或 `docs/diagram-style-guide.md`。
- 不修改 `docs/fact-snapshot.md`、`docs/source-evidence.md` 或 `scripts/check_docs.py`。
- 不改变任何章节状态；s10 必须保持 `待核实`。
- 不把 MCP、dynamic tools、extension tools 和 skills 画成统一官方扩展产品承诺。
- 不把 dynamic tools 画成稳定 CLI 用户入口。
- 不把通用 extension 用户安装/发现/授权入口画成已闭环能力。
- 不把四条能力线画成已验证共享同一治理路径。
- 不使用图片生成模型、外部图片、字体文件、网络服务或导出流水线作为最终图来源。

## Capabilities

### Modified Capabilities

- `diagram-redraw-style-guide`: 按已规划的“会话与扩展”批次，为 s10 增加一张保守边界的可选 SVG 教学辅助图，并保持 Mermaid/SVG 分工与 s10 待核实状态。

## Impact

- 新增图形资产：
  - `chapters/s10_extensions_mcp_skills/diagrams/extension-capability-lines.svg`
- 新增 companion Markdown：
  - `chapters/s10_extensions_mcp_skills/diagrams/extension-capability-lines.md`
- 更新 s10 README 的导航入口。
- OpenSpec 与仓库验证要求：
  - `openspec validate rollout-s10-extension-svg --strict`
  - `openspec validate --all --strict`
  - XML parse 检查新增 SVG
  - 渲染或浏览器预览新增 SVG
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
