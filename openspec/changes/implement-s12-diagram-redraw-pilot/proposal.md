## Why

`design-diagram-redraw-style-guide` 已经给出结论：保留 Mermaid 作为机制图主入口，先用 s12 做一张手写 SVG pilot，验证 trace、failure path、fact boundary 和图例规则是否真的适合本仓读者。

Phase 7 implementation 已完成，s12 integrated teaching mock 现在有稳定的 happy/failure path 和额外 scenario。可以把第一张小样落到 s12，但仍然保持轻量：不替换 `diagram.mmd`，仅允许对原 Mermaid 做边界文案轻修，不重绘其他章节，不新增图片生成或导出流水线。

## What Changes

- 新增 `implement-s12-diagram-redraw-pilot` OpenSpec change。
- 新增 s12 failure trace pilot：
  - `chapters/s12_comprehensive_architecture/diagrams/pilot-trace.svg`
  - `chapters/s12_comprehensive_architecture/diagrams/pilot-trace.md`
- 在 s12 README 中增加可选 pilot 插图入口，明确它不替代现有 Mermaid。
- 对 s12 原 Mermaid 做轻量边界修正：收窄产品入口表述，并显式标出 s08 待核实。
- 使用手写 SVG 表达：
  - F1-F6 failure trace 编号。
  - tool dispatch missing handler。
  - permission deny。
  - context pressure。
  - instruction conflict。
  - recovery / human choice。
  - `TEACHING`、`待核实`、`FACT`、`FAIL`、`RECOVERY` 图例。

## Capabilities

### New Capabilities

- `s12-diagram-redraw-pilot`: 将 s12 failure trace 小样落为 reviewable SVG 和说明文档。

### Modified Capabilities

- `diagram-redraw-style-guide`: 从设计建议推进到一张 s12 pilot 小样，但不改变全仓默认画图方式。

## Impact

- 影响 `chapters/s12_comprehensive_architecture` 的可选插图资料。
- 不修改 Python mock、runner 或测试。
- 不替换任何 Mermaid 图；只允许 s12 原 Mermaid 的边界文案轻修。
- 不升级 s08/s10/s12 状态。
- 不新增官方事实，不修改 `docs/source-evidence.md` 或 `docs/fact-snapshot.md`。
- 不调用 OpenAI API、GPT 图片生成、外部 review、网络服务或真实桌面端状态。
