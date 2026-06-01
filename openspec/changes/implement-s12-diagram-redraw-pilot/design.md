## Context

本 change 承接 `design-diagram-redraw-style-guide`，目标是只做一张 s12 pilot 小样，让规范进入可评审状态。由于 s12 已经有 Phase 7 integrated mock，failure trace 能直接映射到稳定事件：

```bash
python3 chapters/s12_comprehensive_architecture/mock.py --demo --path failure --trace-json
```

pilot 的读者仍是 AI 产品经理和 agent 平台设计者。图要先让人看懂“为什么停下”和“下一步如何安全恢复”，而不是展示完整架构宇宙。

## Goals / Non-Goals

**Goals:**

- 用手写 SVG 落地一张 s12 failure trace pilot。
- 保留现有 `diagram.mmd`，把 SVG 放在 `diagrams/` 下作为可选教学插图。
- 允许对 s12 原 Mermaid 做文字级边界修正，避免它被误读成官方多端架构或把 s08 待核实语义画成稳定主线。
- 让每个 F1-F6 节点能追到 mock trace。
- 用图例显式区分 `FACT`、`待核实`、`TEACHING`、`FAIL`、`RECOVERY`。
- 在说明文档中记录输入 trace、边界标记和人工 QA 项。

**Non-Goals:**

- 不全量重绘 s01-s12。
- 不替换 s12 Mermaid 主图。
- 不做 happy trace SVG。
- 不做 HTML/CSS 导出流水线。
- 不用 GPT 生成图。
- 不把教学 mock 或桌面端体验写成 OpenAI 官方实现事实。

## Pilot Shape

第一张 SVG 使用横向 trace 布局：

1. 左侧：F1 用户请求 live network / desktop state。
2. 中段：F2 tool dispatch 找不到 approved offline handler，F3 permission deny，F4 context pressure，F5 instruction conflict。
3. 右侧：F6 recovery / human choice。
4. 下方：not invoked side-effect block 和 legend。

## Mermaid Review Fixes

本 change 可以轻修 s12 原 Mermaid，但只限于边界强化：

- `Product surface` 节点收窄为产品入口示例 / teaching lens，避免读者把 `CLI / app / IDE` 理解成官方多端部署承诺。
- `Session / thread / rollout state` 节点补 `s08 待核实`，避免把 session/thread/rollout 语义画成已核实官方主线。
- 不替换 `diagram.mmd`，不引入 SVG 作为 Mermaid 的替代图。

节点只表达必要状态：

- `requested_tool=web_lookup`
- `decision_reason=tool_not_registered_in_teaching_registry`
- `permission_decision=deny`
- `context_budget_state=96/100`
- `winning_layer=project`
- `status=needs_human_choice`
- `recovery_choice=use_offline_fixture_or_request_authorization`

## Why The First Pilot Was English-heavy

第一版小样虽然符合 trace 可追溯性，但展示层过度沿用了英文，主要原因是：

1. mock 的结构化字段本身是英文：`input`、`tool_dispatch`、`permission`、`instruction_conflict`、`recovery`、`decision_reason` 等直接进入了 SVG 节点标题和 chip。
2. 视觉规范先强调 diff、字段追溯和事实边界，低估了本仓主要读者是中文 AI 产品经理。
3. badge 继承了 `FACT`、`TEACHING`、`RECOVERY` 等英文短词，适合工程 review，但不适合教学首屏阅读。
4. 图题和边界说明用了英文模板，导致读者第一眼看到的是“工程 trace”，不是“中文教学图”。
5. 展示层和追溯层没有分开：本应中文解释概念，英文只保留为 mock 字段或 event kind。

## Chinese-first Rewrite

改写策略：

- 标题、节点标题、节点说明、legend、pilot scope 全部中文优先。
- F1-F6 编号保留，用于和 mock trace index 对齐。
- event kind 作为小号英文标签保留，例如 `tool_dispatch`，服务追溯而不是首屏理解。
- 关键字段保留英文 monospace chip，例如 `permission_decision=deny`、`used=96/100`，避免误写成官方字段。
- badge 改成中文主文案：`教学抽象`、`官方事实`、`待核实`、`失败/拒绝`、`恢复选择`；必要时在说明文档中括注英文原名。
- 不翻译 OpenAI、Codex、Mermaid、mock、trace、README、SVG 等项目约定名。
- 不把中文化改写当作事实升级：图仍然是 s12 teaching mock 的教学抽象。

## Fact Boundary

整张图标记为 `TEACHING`。它基于 s12 mock trace，不是 OpenAI 官方架构图，不代表 Codex Desktop 或真实生产实现。

`FACT` 图例保留，但本 pilot 不把任何 trace 节点标成官方事实。原因是 failure trace 的节点来自教学 mock，而不是固定 SHA 官方源码中的行为断言。

`待核实` 图例保留，用于提醒 s08/s10 相关语义不能被图形表达顺手升级。此 pilot 不把 session/thread/rollout、MCP、skills 或 extensions 画成官方主线能力。

## File Organization

新增文件：

```text
chapters/s12_comprehensive_architecture/diagrams/
  pilot-trace.svg
  pilot-trace.md
```

README 只增加可选入口，不把 pilot 作为唯一机制图。s12 原 Mermaid 只做边界文案轻修，不改变它的综合总览定位。

## Review Notes

评审时重点看：

- 图题是否明确 `not official architecture`。
- failure path 是否能看出动作被拒绝和副作用未执行。
- recovery 是否明确需要人类选择。
- 图例是否足以防止读者把教学 trace 当作官方实现。
- SVG 是否仍然可 diff、可维护，没有外部资源依赖。
