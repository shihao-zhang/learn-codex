## Context

本仓面向 AI 产品经理和 agent 平台设计者。读者需要的不只是“模块之间有箭头”，还需要看懂：

- 哪条线是官方事实，哪条线只是教学抽象。
- 高风险动作为什么停下。
- 人类授权、拒绝、恢复选择分别发生在哪里。
- 哪些章节仍是 `待核实`，不能因为图画得顺滑就升级成官方稳定能力。

Mermaid 已经足够承担章节主机制图，但它不适合承载所有 trace 细节、状态 chip、failure path 和事实边界图例。s12 pilot 说明手写 SVG 可以补上这部分教学表达，但也暴露出一个风险：如果没有长期规范，后续 SVG 很容易变成无法 review 的“漂亮图”。

## Scope

本 change 只做三类落地：

1. 建立长期规范：`docs/diagram-style-guide.md`。
2. 建立 12 章覆盖规划和分批推广节奏。
3. 做 1 个低风险章节试点：s04 shell / sandbox / approval。

## Non-Goals

- 不替换任何章节的 `diagram.mmd`。
- 不一次性给 12 章都新增 SVG。
- 不更新 fact snapshot target commit。
- 不修改 `scripts/check_docs.py`。
- 不把 Codex Desktop 观察、教学 mock、s12 pilot 或个人推断写成 `openai/codex` 官方实现事实。
- 不使用图片生成模型作为最终机制图或事实图来源。

## Mermaid And SVG Roles

Mermaid 继续承担主机制图：

- 每章结构总览。
- 低成本维护的机制关系。
- 与章节 README 一起构成默认阅读入口。

SVG 承担教学辅助图：

- failure path、权限边界、恢复选择。
- trace 编号和字段 chip。
- 官方事实、待核实、教学抽象的视觉区分。
- 跨章节边界和高风险误读点。

SVG 不替代 Mermaid，也不作为新增官方事实的证据来源。

## Pilot Choice

本轮选择 `s04_shell_sandbox_permissions` 做试点，理由：

- 章节状态是 `已核实官方事实`，已有 `docs/source-evidence.md` 机制级证据。
- 读者最容易被 shell、sandbox、approval、network policy 混淆，适合用 SVG 拆清边界。
- mock failure path 已经稳定：高风险命令触发升级，人类拒绝后不执行。
- 试点可以同时展示 `FACT` 和 `TEACHING`，但不需要触碰 s08/s10 高风险未闭环语义。

## Coverage Planning

长期目标是每个章节至少规划 1 张核心教学 SVG，但推广必须分批：

1. 本轮：规范 + s04 试点。
2. 基础运行时：s01、s02、s03。
3. 工具与权限：s04、s07、s09。
4. 上下文与指令：s05、s06。
5. 会话与扩展：s08、s10、s11。
6. 综合架构：s12 和必要跨章节图。

s08/s10 的 SVG 必须显式标注 `待核实`；s12 必须继续标为 `教学抽象`。跨章节图必须说明每条关键边是官方事实、教学抽象还是待核实。

## Review And Validation

本 change 完成前需要通过：

- `openspec validate promote-diagram-style-guide --strict`
- `python3 scripts/check_docs.py`
- `python3 scripts/run_all.py`
- `python3 -m unittest discover -s tests`
- `git diff --check`

提交前还要人工确认：未修改 fact snapshot、source evidence、章节状态和 `scripts/check_docs.py`。
