## ADDED Requirements

### Requirement: 全仓 SVG 视觉一致性 QA

全仓章节 SVG 完成较大范围 rollout 后，仓库 SHALL 把这些教学辅助图作为一组材料做视觉一致性审计，保持可读性和语义边界一致，不改变事实状态。

#### Scenario: 审计全量 SVG 集合

- **WHEN** `audit-svg-visual-consistency` 实施完成
- **THEN** 每个 `chapters/*/diagrams/*.svg` 文件都完成 XML parse
- **AND** 每张章节 SVG 都在验收前完成渲染或预览
- **AND** 审计记录文字遮挡、箭头压字、主路径层级、图例权重和语义标记一致性是否已检查

#### Scenario: 跨章节比较语义标记

- **WHEN** 渲染后的 SVG 集合被 review
- **THEN** 对已出现的 `FACT`、`待核实`、`TEACHING` 或 `教学辅助`、`FAIL`、`DENY` 和 `RECOVERY` 标记检查语义和视觉处理是否一致
- **AND** 不用标记文案新增官方事实或升级未闭环语义

#### Scenario: 高风险章节边界保持显式

- **WHEN** s08 或 s10 SVG 纳入全仓审计
- **THEN** 相关未闭环语义继续可见地标为 `待核实`
- **AND** 审计不改变这两个章节状态

#### Scenario: s12 教学抽象保持显式

- **WHEN** s12 SVG 纳入全仓审计
- **THEN** 图中继续可见地标为 `教学抽象`
- **AND** 跨章节解释不被呈现为 OpenAI 官方架构图

#### Scenario: 修复小型视觉问题

- **WHEN** 审计发现小型可读性或标记一致性问题
- **THEN** 维护者可以修改受影响 SVG 和 companion Markdown
- **AND** 修改不触碰 `docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py` 或章节状态

#### Scenario: 全仓 SVG 审计可验收

- **WHEN** 审计和必要小修完成
- **THEN** `openspec validate audit-svg-visual-consistency --strict`、`openspec validate --all --strict`、全部章节 SVG 的 XML parse、`python3 scripts/check_docs.py`、`python3 scripts/run_all.py`、`python3 -m unittest discover -s tests` 和 `git diff --check` 均通过
