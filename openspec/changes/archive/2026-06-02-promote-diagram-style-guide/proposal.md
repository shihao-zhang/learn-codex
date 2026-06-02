## Why

`design-diagram-redraw-style-guide` 和 `implement-s12-diagram-redraw-pilot` 已经证明：手写 SVG 能把 trace、failure path、恢复选择和事实边界讲得比 Mermaid 更清楚；但当前仓库还缺一个长期规范，后续 agent 容易把 SVG 当成“重画机制图”或“补官方架构图”。

本 change 的目的不是一次性重画全仓，而是把规范正式沉淀到 `docs/diagram-style-guide.md`，并用 1 个低风险章节试点验证推广方式。

## What Changes

- 新增 `docs/diagram-style-guide.md`，作为后续 SVG 教学辅助图的长期规范。
- 明确 Mermaid 与 SVG 分工：
  - Mermaid 保留为章节主机制图和可快速维护结构图。
  - SVG 只作为教学辅助图，用于解释路径、边界、失败、恢复、对比和 trace。
- 固化 s12 pilot 得到的图形规则：
  - 中文优先。
  - 手写 SVG，代码可 diff。
  - 无外部生成依赖。
  - 不使用图片生成模型作为最终事实图来源。
  - 必须包含清晰标题、图例、说明或 `<desc>`。
  - 必须区分 `FACT`、`待核实`、`TEACHING`、`FAIL`、`DENY`、`RECOVERY` 等语义。
- 建立 12 章 SVG 覆盖规划和分批推广节奏。
- 本轮只新增 1 个低风险试点：`s04_shell_sandbox_permissions` 的可选 SVG 教学辅助图。
- README / roadmap 只增加指向规范和本轮试点的导航入口。

## Capabilities

### New Capabilities

- `promoted-diagram-style-guide`: 提供长期 SVG 教学辅助图规范、章节覆盖规划、推广节奏和试点验收规则。

### Modified Capabilities

- `diagram-redraw-style-guide`: 从轻量设计建议升级为仓库长期规范，但不改变 Mermaid 作为主机制图的地位。
- `s12-diagram-redraw-pilot`: 将 s12 pilot 的经验抽象成通用规则；s12 继续保持教学抽象。

## Impact

- 影响文档：新增 `docs/diagram-style-guide.md`，更新 README、roadmap 和 s04 README。
- 影响图形资产：新增 s04 可选 SVG 试点，放在章节 `diagrams/` 目录。
- 不替换任何 `diagram.mmd`。
- 不一次性重画 12 章。
- 不修改 `docs/fact-snapshot.md`、`docs/source-evidence.md` 或 `scripts/check_docs.py`。
- 不改变任何章节状态。
- 不新增官方事实；SVG 中的官方事实必须回到已有固定 SHA 证据或 `docs/source-evidence.md`。
- 不调用 OpenAI API、GPT 图片生成、外部 review、网络服务或真实桌面端状态。
