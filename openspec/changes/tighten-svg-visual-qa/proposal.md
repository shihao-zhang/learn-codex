## Why

第一批基础运行时 SVG rollout 后，人工视觉检查发现两个问题：

- s01 `turn-loop.svg` 信息权重混乱，主路径、教学 failure path 和图例之间缺少清晰层级。
- s02 `event-interface.svg` 存在模块重叠，影响阅读和 review。

这说明当前 SVG 规范虽然约束了事实边界、语义 badge 和 companion note，但对“渲染后视觉 QA”要求不够具体。仅凭 SVG XML 可解析和源码可 diff，不能保证图真正可读。

## What Changes

- 修正 s01 SVG，让 FACT 主路径成为第一阅读路径，教学 failure path 和恢复路径降为次级解释。
- 修正 s02 SVG，消除模块重叠，并让 trace context 作为侧向关联而不是被遮挡的模块。
- 更新 companion Markdown 的 Manual QA，记录已做视觉核实。
- 更新 `docs/diagram-style-guide.md`，沉淀渲染后视觉 QA 规则：
  - 提交前必须渲染并目视检查关键 SVG。
  - 主路径应有明确视觉层级，不让图例、failure path 或教学 chip 抢占第一阅读路径。
  - 模块、文字、箭头和 chip 不得相互遮挡。
  - 高密度图应拆成主路径、侧向解释、图例三层。

## Non-Goals

- 不新增官方事实。
- 不替换 Mermaid 主机制图。
- 不修改 `docs/fact-snapshot.md`。
- 不修改 `docs/source-evidence.md`。
- 不修改 `scripts/check_docs.py`。
- 不改变章节状态。
- 不触碰 s08、s10、s12 状态。

## Impact

- 修改 s01/s02 SVG 与 companion Markdown。
- 修改 `docs/diagram-style-guide.md` 的视觉 QA 规范。
- 新增 OpenSpec change `tighten-svg-visual-qa`。
