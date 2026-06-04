## Why

全仓 12 章已经各有一张可选 SVG 教学辅助图，但目前读者需要逐章打开 README 才能知道有哪些图、每张图解决什么理解问题，以及哪些内容是 `FACT`、`待核实` 或 `教学抽象`。这会增加 AI 产品经理的阅读成本，也容易让跨章节 SVG 被误读成同一类官方机制图。

本 change 新增一个 SVG 教学图册索引，把现有章节 SVG 作为一组导航材料呈现：列出章节、SVG 路径、companion Markdown 路径、理解问题和事实边界。索引只做导航和边界提示，不新增官方事实，不改变章节状态。

## What Changes

- 新增 `docs/svg-diagram-gallery.md`。
- 图册按 s01-s12 列出现有 SVG：
  - 章节。
  - SVG 路径。
  - companion Markdown 路径。
  - 解决什么理解问题。
  - `FACT` / `待核实` / `教学抽象` 边界。
- README 增加图册入口。
- OpenSpec change `add-svg-diagram-gallery` 记录索引字段、非目标和验收要求。

## Non-Goals

- 不新增、重画或修改任何章节 SVG。
- 不替换或修改任何章节 `diagram.mmd`。
- 不修改任何章节 README 的状态标签或章节状态。
- 不新增官方事实。
- 不修改 `docs/fact-snapshot.md`。
- 不修改 `docs/source-evidence.md`。
- 不修改 `scripts/check_docs.py`。
- 不把 s08、s10 或 s12 的边界升级为官方事实。

## Capabilities

### Modified Capabilities

- `diagram-redraw-style-guide`: 增加全仓 SVG 教学图册索引要求，用一个总入口汇总现有章节 SVG 和事实边界，同时保持 Mermaid/SVG 分工和章节状态不变。

## Impact

- 新增文档：
  - `docs/svg-diagram-gallery.md`
- 更新入口：
  - `README.md`
- 新增 OpenSpec change：
  - `openspec/changes/add-svg-diagram-gallery/`
- 禁止修改：
  - `docs/fact-snapshot.md`
  - `docs/source-evidence.md`
  - `scripts/check_docs.py`
  - 章节状态字段或状态说明
- 验收要求：
  - `openspec validate add-svg-diagram-gallery --strict`
  - `openspec validate --all --strict`
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
