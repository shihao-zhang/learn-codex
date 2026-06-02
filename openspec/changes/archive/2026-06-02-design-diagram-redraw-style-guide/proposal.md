## Why

本仓当前主要用 Mermaid 表达机制图。Mermaid 适合维护，但在面向 AI 产品经理解释 agent harness 时，容易把端到端状态、事实边界和 failure path 压成同一种箭头，读者不容易看出“谁负责状态、哪里需要人类选择、哪些只是教学抽象”。

s12 已经承载综合架构和 Phase 7 integrated teaching mock trace，覆盖输入、指令、上下文、工具路由、权限、边界、恢复和答案。因此本轮先围绕 s12 做轻量调研与样式规范，不替换 s01~s12 的 Mermaid，不推进全量重绘。

## What Changes

- 新增 `design-diagram-redraw-style-guide` OpenSpec change。
- 基于 s12 的 Mermaid、Python mock、测试和 runner 输出，整理未来教学插图需要表达的节点、状态和 failure path。
- 对比 Mermaid、手写 SVG、HTML/CSS 导出 SVG/PNG、GPT 图片生成四种画法。
- 推荐主方案和备选方案，并说明适合本仓的理由。
- 定义轻量视觉规范，覆盖：
  - 图形层级
  - 颜色语义
  - 官方事实 / 待核实 / 教学抽象的视觉标记
  - failure path 表达方式
  - 图例和编号规则
  - 文件组织方式
- 给出 s12 pilot 草案边界：只设计，不大规模改图，不替换现有 `diagram.mmd`。

## Capabilities

### New Capabilities

- `diagram-redraw-style-guide`: 定义教学插图重绘的轻量样式规则、事实边界标记和 s12 pilot 入口。

### Modified Capabilities

- 无。本 change 不修改章节正文、mock、runner 或测试。

## Impact

- 影响 OpenSpec：新增一个设计 change。
- 不新增官方事实，不修改 `docs/source-evidence.md` 或 `docs/fact-snapshot.md`。
- 不改变 s08/s10/s12 状态。
- 不调用 OpenAI API、GPT 图片生成、外部 review、网络服务或真实桌面端状态。
- 不替换任何章节 Mermaid 图。
