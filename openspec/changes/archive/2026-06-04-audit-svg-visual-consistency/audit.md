# SVG 视觉一致性审计记录

## 渲染输入

- 目标集合：`chapters/*/diagrams/*.svg`
- 数量：12 张 SVG。
- XML parse：视觉 QA 前，全部目标 SVG 均可成功解析。
- 预览方式：使用 macOS Quick Look 渲染预览。直接渲染非正方形 SVG 缩略图时会横向裁切，因此最终人工 QA 使用 `/tmp` 中的临时方形 viewBox 预览副本；仓库内 SVG 源文件没有为渲染方式做临时改动。

## 审计口径

- 文字和卡片不重叠。
- 连线和箭头不压住读者需要阅读的正文。
- 主阅读路径先于侧向解释被看到。
- 图例存在、可读，且不比图主体更抢眼。
- 语义标记保持一致：`FACT`、`待核实`、`教学辅助`、`FAIL` / `失败`、`DENY` / `拒绝`、`RECOVERY` / `恢复选择`。
- s08 和 s10 的未闭环语义继续显式标 `待核实`。
- s12 继续显式标 `教学抽象`。

## 逐图结论

| 章节 | SVG | 结论 | 记录 |
| --- | --- | --- | --- |
| s01 | `turn-loop.svg` | 通过 | `FACT` 主路径视觉优先；failure/recovery 路径处于次级区域；未发现文字或箭头遮挡。 |
| s02 | `event-interface.svg` | 通过 | event 主路径、trace context、schema drift failure path 和图例均可读；未发现遮挡。 |
| s03 | `tool-dispatch.svg` | 通过 | registry / route / dispatch 主路径清楚；failure 和 recovery 路径保持次级。 |
| s04 | `permission-boundary.svg` | 已修复 | `exit_code=null` chip 偏窄；已加宽 chip，并更新 companion QA。 |
| s05 | `context-pressure.svg` | 通过 | context pressure、compact/truncation、failure 和 recovery 路径均可读；相邻连线未压住正文。 |
| s06 | `instruction-conflict.svg` | 通过 | 指令来源、冲突、未执行和恢复选择视觉区分清楚。 |
| s07 | `model-choice-impact.svg` | 通过 | config/auth/model 主路径优先；`待核实` 漂移风险显式；图例可读。 |
| s08 | `session-thread-rollout.svg` | 通过 | `FACT(局部)` 与 `待核实` 同时显式；remote backend、Cloud/desktop 恢复语义和 experimental API 继续保持 pending。 |
| s09 | `state-sync-boundary.svg` | 通过 | runtime / app-server / protocol / product surface 分栏清楚；failure/recovery path 可读。 |
| s10 | `extension-capability-lines.svg` | 已修复 | 小卡片和底部边界说明垂直留白偏紧；已增加卡片空间，四条能力线和 `待核实` 标记不变。 |
| s11 | `subagents-parallel-jobs.svg` | 已修复 | `待核实` 虚线靠近 `spawn_agent` chip；已重排连线，并更新 companion QA。 |
| s12 | `pilot-trace.svg` | 通过 | 整图保持 `教学抽象`；s08/s10 `待核实` 提醒可见；companion 标题已标准化。 |

## 边界确认

- 没有新增官方事实。
- 未修改 `docs/fact-snapshot.md`。
- 未修改 `docs/source-evidence.md`。
- 未修改 `scripts/check_docs.py`。
- 未改变章节状态。
