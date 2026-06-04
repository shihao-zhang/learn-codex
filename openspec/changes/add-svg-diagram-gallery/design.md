## 背景

`docs/diagram-style-guide.md` 已规定：Mermaid 是章节主机制图，SVG 只是可选教学辅助图；每张 SVG 都必须通过 companion Markdown 说明输入、映射、事实边界和人工 QA。随着 s01-s12 都已经铺开 SVG，读者需要一个比逐章 README 更高层的入口，用来快速判断“我应该看哪张图”和“图里的事实边界是什么”。

本 change 的核心是导航，不是事实扩写。索引从现有 chapter SVG 与 companion Markdown 汇总信息，不从图形表达中推导新机制，也不修改统一证据索引。

## 范围

本 change 只覆盖：

1. `docs/svg-diagram-gallery.md`
2. `README.md` 的图册入口
3. `openspec/changes/add-svg-diagram-gallery/` 下的 proposal、design、tasks 和 spec delta

不触碰：

- `docs/fact-snapshot.md`
- `docs/source-evidence.md`
- `scripts/check_docs.py`
- `docs/diagram-style-guide.md`
- `chapters/*/README.md`
- `chapters/*/diagram.mmd`
- `chapters/*/diagrams/*.svg`
- `chapters/*/diagrams/*.md`

## 输入来源

本轮索引只使用以下输入：

- `AGENTS.md`
- `docs/diagram-style-guide.md`
- `README.md`
- `chapters/*/README.md`
- `chapters/*/diagrams/*.md`
- `chapters/*/diagrams/*.svg` 的路径与现有文件名

## 图册规则

- 图册按 s01-s12 顺序排列。
- 每行必须包含：章节、SVG 路径、companion Markdown 路径、解决什么理解问题、事实边界。
- 路径使用相对链接，指向现有文件。
- `FACT` 只摘要 companion Markdown 中已经声明的事实机制范围。
- `待核实` 必须显式覆盖 s08、s10，以及 s07/s09/s11 等 companion 中已经标出的漂移或未闭环点。
- `教学抽象` 或 `教学辅助` 必须覆盖 mock trace、示例命令、产品 UI 建议、固定阈值、恢复文案和 s12 整体图。
- 图册不得把 companion Markdown 没有声明的内容升级成新事实。

## 事实边界

- s08 保持 `待核实`：图册只能说它帮助理解 session/thread/rollout/resume/fork 的教学关系，不能称为官方稳定恢复能力。
- s10 保持 `待核实`：图册只能说它帮助并排理解 MCP、dynamic tools、extension tools 和 skills，不能合并成统一官方扩展产品承诺。
- s12 保持 `教学抽象`：图册只能说它基于 s12 mock 解释综合 failure trace，不能呈现为 OpenAI 官方架构图。
- 其他章节的 `FACT` 只限 companion 中已登记机制范围；示例、UI、阈值、恢复建议仍是教学表达。

## 验收

完成前需要检查：

- OpenSpec tasks 全部完成。
- `README.md` 增加图册入口，且不修改学习地图状态列。
- `docs/svg-diagram-gallery.md` 覆盖全部 12 章 SVG。
- 所有 SVG 和 companion Markdown 链接指向现有文件。
- 禁止文件保持未修改：`docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py`。
- 运行用户要求的常规检查：
  - `openspec validate add-svg-diagram-gallery --strict`
  - `openspec validate --all --strict`
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
