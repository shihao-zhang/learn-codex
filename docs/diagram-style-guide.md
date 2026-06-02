# Diagram Style Guide

本规范用于后续“每个章节及必要处提供 SVG 教学辅助图”。它约束的是本教学仓的表达方式，不是 `openai/codex` 官方架构图规范。

## 一句话原则

Mermaid 继续做主机制图；SVG 只做教学辅助图。SVG 可以帮读者看清路径、边界、失败、恢复、对比和 trace，但不能替代源码证据，也不能把教学 mock、桌面端观察或个人推断升级成官方事实。

## 适用范围

适用：

- 章节内的核心教学 SVG。
- failure path、权限边界、事实边界、trace 阅读辅助图。
- 跨章节对比图或总览图。

不适用：

- 替换章节 `diagram.mmd`。
- 作为官方实现事实来源。
- 一次性重画 12 章。
- 用图片生成模型产出的图作为最终机制图或事实图。

## Mermaid 与 SVG 分工

| 类型 | 默认职责 | 适合表达 | 不应承担 |
| --- | --- | --- | --- |
| Mermaid | 章节主机制图 | 模块关系、控制流主干、可快速维护的结构图 | 复杂图例、细粒度 trace、视觉事实边界 |
| SVG | 教学辅助图 | failure path、权限边界、恢复选择、trace 编号、事实/待核实/教学抽象标记 | 替代 Mermaid、制造新官方事实、承诺真实部署拓扑 |

每章 README 的“机制图”仍先指向 `diagram.mmd`。如果新增 SVG，只能作为“可选教学辅助图”入口。

## SVG 最低合同

每张 SVG 必须满足：

- 中文优先：标题、节点、说明、图例和边界说明使用中文；英文只作为路径、字段、命令或 schema 的追溯标签。
- 手写 SVG：源文件是可读文本，可在 git diff 中 review。
- 无外部生成依赖：不依赖外部图片、字体文件、网络服务或导出流水线。
- 不使用图片生成模型作为最终事实图来源；如借鉴构图，必须手写重绘并重新标注事实边界。
- 包含 `<title>` 和 `<desc>`；`<desc>` 必须说明范围和非官方边界。
- 可见图中包含图例或边界说明。
- 如果包含官方事实、mock trace 或待核实语义，应配套 Markdown 说明，记录输入、映射、事实边界和人工 QA。

## 语义标记

颜色不能作为唯一语义，必须同时使用文字 badge、线型或形状。

| 语义 | badge | 用途 | 绘制规则 |
| --- | --- | --- | --- |
| 官方事实 | `FACT` / `官方事实` | 已能追到固定 SHA 源码、OpenAI 官方文档、release note 或 `docs/source-evidence.md` 的机制点 | 实线边框，避免夸大到 UI、默认值或跨平台能力 |
| 待核实 | `待核实` | s08/s10 等未闭环语义，或只有路径证据但行为边界不足的机制 | 虚线边框，不画成稳定官方能力 |
| 教学抽象 | `TEACHING` / `教学抽象` | mock trace、固定预算、教学 checkpoint、跨章解释、示例命令 | 点线边框，明确不等同官方实现 |
| 失败 | `FAIL` / `失败` | 工具缺失、策略冲突、上下文压力导致无法继续 | 红色原因线，写清停止原因 |
| 拒绝 | `DENY` / `拒绝` | 人类或策略拒绝高风险动作 | 红色停止标记，必须说明副作用未执行 |
| 恢复 | `RECOVERY` / `恢复选择` | 低风险替代、请求授权、回到人类确认 | 蓝色回路或出口，写清谁来选择 |

如果一个节点混合多种来源，按更保守的语义标记。例如“session recovery 教学 checkpoint”应标为 `TEACHING`，并给 s08 相关语义加 `待核实` chip。

## 事实边界规则

- `FACT` 节点或边必须能回到当前固定 SHA、OpenAI 官方资料或 `docs/source-evidence.md`。
- 章节状态为 `待核实` 的内容，即使图里只是旁路出现，也必须显式标 `待核实`。
- s12 的综合图、integrated teaching mock 和 pilot trace 都是 `教学抽象`。
- 跨章节图必须说明关键边的来源类型：官方事实、教学抽象或待核实。
- 示例命令、PM 文案、产品指标、恢复建议通常是教学表达；不能画成官方策略。
- Codex Desktop 观察只能用于生成源码阅读问题或教学启发；无法回到公开源码时必须标为 `待核实`、`教学抽象` 或 `推断`。

## 图形规则

建议沿用 s12 pilot 的轻量视觉语义：

| 元素 | 建议 |
| --- | --- |
| 画布 | 浅色背景，给标题、主路径、图例留出稳定空间 |
| 标题 | 写章节和用途，例如 `s04 辅助图：shell 权限边界` |
| 节点层级 | 主路径节点优先，状态 chip 次之，不把字段都画成同级节点 |
| 线条 | 普通路径用灰色，失败/拒绝用红色，恢复用蓝色，待核实用虚线 |
| 字段 chip | 小号 monospace，用于 `permission_decision=deny`、`handler_called=False` 等追溯字段 |
| 图例 | 至少解释 `FACT`、`待核实`、`TEACHING`、`FAIL/DENY`、`RECOVERY` |
| 边界说明 | 明确“本图是教学辅助图，不是 OpenAI 官方架构图” |

不要为了视觉完整而补画未核实的系统、隐藏策略、云端链路、真实桌面端状态或内部服务。

## 文件组织

章节试点使用：

```text
chapters/<chapter>/diagrams/
  <short-name>.svg
  <short-name>.md
```

规则：

- 不替换 `chapters/<chapter>/diagram.mmd`。
- README 只增加短入口。
- companion Markdown 记录输入、event mapping、事实边界和人工 QA。
- 官方机制证据仍统一登记到 `docs/source-evidence.md`；不要为每张图新增分散 sources 文件。

## 12 章覆盖规划

| 章节 | 计划核心 SVG | 边界要求 | 推广批次 |
| --- | --- | --- | --- |
| s01_agent_loop | turn 中用户输入、模型动作、工具 observation、继续/停止的循环 | loop 主干可标 `FACT`；简化时序标 `TEACHING` | 基础运行时 |
| s02_protocol_events | request / response / event 如何被产品界面消费 | 事件协议机制可标 `FACT`；UI 呈现建议标 `TEACHING` | 基础运行时 |
| s03_tool_registry_dispatch | 工具声明、registry、router、handler、结果回写 | 已核实路由机制可标 `FACT`；示例工具名标 `TEACHING` | 基础运行时 |
| s04_shell_sandbox_permissions | shell 请求穿过 approval、sandbox、network policy，拒绝后不执行高风险动作 | 机制点来自 `docs/source-evidence.md` 可标 `FACT`；示例命令和审批文案标 `TEACHING` | 本轮试点 / 工具与权限 |
| s05_context_window_compaction | context pressure 下继续、压缩、截断、摘要风险的选择路径 | compaction 源码入口可标 `FACT`；阈值、保真字段和摘要质量标 `TEACHING` | 上下文与指令 |
| s06_prompts_instructions | system / developer / user / AGENTS.md / 项目约束的冲突处理 | 指令层级来源可标 `FACT`；冲突案例和文案标 `TEACHING` | 上下文与指令 |
| s07_config_auth_models | config、auth、provider/model 选择对成本、能力和合规的影响 | config 类型可标 `FACT`；模型可用性、默认值和产品建议需防漂移 | 工具与权限 |
| s08_sessions_threads_rollout | session、thread、rollout、恢复与持久化的未闭环关系 | 必须显式标 `待核实`；不得画成官方稳定恢复能力 | 会话与扩展 |
| s09_app_server_transport | app-server / protocol / product surface 的状态同步边界 | 已核实入口可标 `FACT`；多端体验和 UI 策略标 `TEACHING` | 工具与权限 |
| s10_extensions_mcp_skills | MCP、extensions、skills、动态工具和治理边界 | 必须显式标 `待核实`；不得把 skills/MCP 画成统一官方产品承诺 | 会话与扩展 |
| s11_subagents_parallel_jobs | delegate、并行子任务、父子事件与审批转发 | 已登记机制可标 `FACT`；默认启用、v1/v2 体验和全部继承策略需保守 | 会话与扩展 |
| s12_comprehensive_architecture | 端到端路径、failure recovery、跨章节边界总览 | 整体标 `教学抽象`；s08/s10 相关边继续标 `待核实` | 综合架构 |

## 推广节奏

本轮只做规范和 s04 试点，不重画全仓。

后续建议批次：

1. 基础运行时：s01、s02、s03。先让读者看懂 agent loop、事件和工具分发。
2. 工具与权限：s04、s07、s09。把 shell 权限、配置认证、app-server 边界放到同一批复核。
3. 上下文与指令：s05、s06。重点讲长任务为什么丢信息、指令冲突如何解释。
4. 会话与扩展：s08、s10、s11。先保守标注 `待核实` 或未闭环边界，再画图。
5. 综合架构：s12 和跨章节图。只在前面章节边界稳定后推进。

每个批次都应先开 OpenSpec change，明确本批新增哪些 SVG、哪些事实边界不变、哪些检查必须通过。

## SVG 人工 QA 清单

提交 SVG 前至少检查：

- [ ] README 是否仍把 `diagram.mmd` 作为主机制图。
- [ ] SVG 是否包含 `<title>`、`<desc>` 和可见图例。
- [ ] 中文是否承担主要解释，英文是否只做追溯标签。
- [ ] `FACT` 是否能回到固定 SHA、官方资料或 `docs/source-evidence.md`。
- [ ] `待核实` 是否覆盖 s08/s10 或其他未闭环语义。
- [ ] `TEACHING` 是否覆盖 mock、示例、固定阈值、跨章解释。
- [ ] 失败/拒绝路径是否说明副作用未执行。
- [ ] 恢复路径是否说明需要人类选择还是系统可自动继续。
- [ ] 没有新增外部图片、生成图、网络依赖或二进制资产。
