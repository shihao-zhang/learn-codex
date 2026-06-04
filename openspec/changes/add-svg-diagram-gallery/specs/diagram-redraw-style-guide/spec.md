## ADDED Requirements

### Requirement: 全仓 SVG 教学图册索引

全仓章节 SVG 完成覆盖后，仓库 SHALL 提供一个面向读者的 SVG 教学图册索引，帮助读者按章节找到图形资产、companion Markdown 和事实边界说明。

#### Scenario: 图册覆盖全部章节 SVG

- **WHEN** `add-svg-diagram-gallery` 实施完成
- **THEN** `docs/svg-diagram-gallery.md` 列出 s01-s12 每章现有 SVG
- **AND** 每行包含章节、SVG 路径、companion Markdown 路径、解决什么理解问题、`FACT` / `待核实` / `教学抽象` 边界

#### Scenario: README 提供总入口

- **WHEN** 读者从仓库 README 进入文档
- **THEN** README 提供 `docs/svg-diagram-gallery.md` 的入口
- **AND** 学习地图的章节状态不因新增入口而改变

### Requirement: 图册索引保持事实边界

SVG 教学图册 SHALL 只作为导航和边界提示，不新增官方事实、不升级未闭环语义、不改变章节状态。

#### Scenario: 索引摘要 FACT 机制

- **WHEN** 图册摘要某章 `FACT` 边界
- **THEN** 摘要只来自该章 companion Markdown 已声明的机制范围
- **AND** 仍以 `docs/source-evidence.md` 作为机制级证据入口

#### Scenario: 索引包含高风险章节

- **WHEN** 图册列出 s08 或 s10
- **THEN** 对应行显式保留 `待核实` 边界
- **AND** 不把局部源码路径或能力线画成官方稳定产品承诺

#### Scenario: 索引包含综合图

- **WHEN** 图册列出 s12
- **THEN** 对应行显式标出整体为 `教学抽象`
- **AND** 不把 s12 pilot trace 说成 OpenAI 官方架构图

#### Scenario: 索引表达教学内容

- **WHEN** 图册摘要 mock trace、示例命令、固定阈值、UI 建议、恢复文案或跨章解释
- **THEN** 这些内容标为 `教学抽象` 或 `教学辅助`
- **AND** 不被写成官方实现事实

### Requirement: 图册变更验收

SVG 教学图册变更 SHALL 通过 OpenSpec 与常规仓库检查，并保持用户点名禁止的文件不变。

#### Scenario: 图册变更完成

- **WHEN** 图册、README 入口和 OpenSpec change 完成
- **THEN** `openspec validate add-svg-diagram-gallery --strict`、`openspec validate --all --strict`、`python3 scripts/check_docs.py`、`python3 scripts/run_all.py`、`python3 -m unittest discover -s tests` 和 `git diff --check` 均通过
- **AND** `docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py` 和章节状态保持不变
