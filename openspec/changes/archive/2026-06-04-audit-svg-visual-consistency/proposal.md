## Why

全仓 12 章已经各有一张可选 SVG 教学辅助图。此前每个批次都做过局部渲染 QA，但读者最终看到的是一组连续章节图：如果不同章节的标记、图例、主路径层级或待核实边界不一致，会让 AI 产品经理误读哪些是官方事实、哪些只是教学表达。

本 change 的目标是推进一次全仓 SVG 视觉一致性审计：逐张渲染/预览 `chapters/*/diagrams/*.svg`，检查文字遮挡、箭头压字、主路径可见性、图例权重，以及 `FACT` / `待核实` / `教学辅助` / `FAIL` / `DENY` / `RECOVERY` 标记的一致性。

## What Changes

- 新增 OpenSpec change `audit-svg-visual-consistency`，把全仓 SVG 视觉一致性 QA 的范围、边界和验收记录下来。
- 渲染/预览全部章节 SVG：
  - `chapters/*/diagrams/*.svg`
- 对每张图检查并记录：
  - 是否有文字遮挡或模块重叠。
  - 箭头是否压字或穿过读者需要阅读的文本。
  - 主路径是否一眼可见。
  - 图例是否过重、缺失或与图中语义不一致。
  - `FACT` / `待核实` / `教学辅助` / `FAIL` / `DENY` / `RECOVERY` 标记是否一致。
  - s08/s10 是否显式保持 `待核实`。
  - s12 是否显式保持 `教学抽象`。
- 如发现小问题，直接修复 SVG 和同目录 companion Markdown 的 `Manual QA` 记录。

## Non-Goals

- 不新增官方事实。
- 不新增或替换章节 Mermaid 主机制图。
- 不修改 `docs/fact-snapshot.md`。
- 不修改 `docs/source-evidence.md`。
- 不修改 `scripts/check_docs.py`。
- 不改变任何章节状态，尤其不升级 s08、s10、s12。
- 不修改 `docs/diagram-style-guide.md` 的长期规则，除非审计发现必须沉淀的新长期决策；本次默认只执行既有规则。
- 不使用图片生成模型、外部图片、外部字体、网络服务或二进制导出物作为最终图源。

## Capabilities

### Modified Capabilities

- `diagram-redraw-style-guide`: 增加一次全仓 SVG 视觉一致性审计的验收约束，确保已铺开的章节 SVG 在渲染后保持可读、语义标记一致，并继续保护 s08/s10/s12 的事实边界。

## Impact

- 新增 OpenSpec change：
  - `openspec/changes/audit-svg-visual-consistency/`
- 可能修改：
  - `chapters/*/diagrams/*.svg`
  - `chapters/*/diagrams/*.md`
- 禁止修改：
  - `docs/fact-snapshot.md`
  - `docs/source-evidence.md`
  - `scripts/check_docs.py`
  - 章节状态字段或状态说明
- 验收要求：
  - `openspec validate audit-svg-visual-consistency --strict`
  - `openspec validate --all --strict`
  - XML parse 全部 SVG
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
