# Next Phase Roadmap

本路线图是后续写作和 review 的执行合同，不是 `openai/codex` 官方计划。它只约束本教学仓如何继续把 agent harness 讲清楚，并继续遵守 [fact-snapshot.md](fact-snapshot.md) 与 [source-evidence.md](source-evidence.md) 的事实边界。

## Phase Sequence

| Phase | 目的 | 主要产出 | 验收检查 | 停止条件 |
| --- | --- | --- | --- | --- |
| Phase 5：s08/s10 验证优先 | 先收敛最容易误写成官方能力的 session/thread/rollout 与 skills/MCP/extension 语义。 | s08、s10 的源码阅读问题、证据补登记、章节保守表述；必要时保留 `待核实`。 | 每个新增官方事实都有固定 SHA 或官方文档依据；`source-evidence.md` 有对应证据级别；章节状态不被强行升级。 | 如果端到端链路仍无法闭环，停止在 `待核实`，把缺口写清楚，不用推断补事实。 |
| Phase 6：前 6 章内容加厚 | 提高读者进入 agent harness 的第一屏密度。 | s01~s06 的产品问题、机制解释、failure path、mock trace 说明更完整。 | 文档检查、mock 检查、单测通过；新增源码映射进入统一证据索引；review summary 逐章说明产品问题、failure path 或 mock trace 的具体改进。 | 如果某段解释只能靠类比或经验支撑，先标为 `推断` 或删减。 |
| Phase 7：integrated teaching mock | 把分散机制串成一个端到端教学体验，帮助读者看见 runtime 组合关系。 | s12 integrated teaching mock，覆盖 loop、tool dispatch、permission decision、context pressure、instruction conflict、session trace、failure recovery。 | mock 必须离线、确定性、仅标准库，并保留 “Teaching mock only” 类免责声明；s08/s10 继续保持 `待核实`。 | 如果 mock 看起来像 OpenAI Codex 复刻，或需要调用真实 API，停止并降级为教学抽象。 |
| Phase 8：证据抽样复核 | 防止章节解释随 release、模型名、权限策略或 app-server 协议漂移。 | 抽样复核记录、过期风险清单；如需更新事实快照，另开 proposal。 | 固定 SHA 链接不使用 moving ref；变更事实快照前走 OpenSpec；review summary 说明哪些内容保持保守。 | 如果新 release 改动较大，先开新 change，不在原章节里直接混写新旧事实。 |
| Phase 9：维护与贡献流程 | 让后续贡献者知道如何改文档、证据和 mock。 | 贡献流程、review checklist、常见误区和回滚方式。 | 文档、mock、单测、diff whitespace 检查通过；人工 summary 能说明事实边界。 | 如果流程文档变成复盘或命令日志，停止并删减为可执行规则。 |

## Phase 5 Priority

Phase 5 必须先处理 s08 和 s10，因为它们决定本仓事实可信度上限：

- s08：继续核实 `thread-store`、`rollout`、`thread_rollout_truncation.rs` 与 app-server/thread 恢复之间的数据流。目标不是把章节升为 `已核实官方事实`，而是弄清哪些语义能核实、哪些必须继续保守。
- s10：继续核实 MCP CLI 入口、extension tools、skills TUI/配置入口和统一扩展治理之间的边界。不能只因为源码存在 `skills` crate 就写成完整扩展产品能力。

如果 s08 或 s10 读完仍不能闭环，合格结果是：章节继续 `待核实`，但读者能看懂为什么不能升级。

Phase 5 第一轮核验已完成，阶段收口见 [phase5-summary.md](phase5-summary.md)。结论是：s08/s10 的证据密度显著提升，但仍保留 `待核实`，后续写作必须继承这个边界。

## Phase 5~9 Completion Checkpoint

Phase 5~9 本轮已经收拢到可 review 状态：

- Phase 5：s08/s10 完成第一轮核验和阶段总结，状态继续 `待核实`。
- Phase 6：s01~s06 完成内容加厚，新增内容保持产品判断、教学解释和官方事实边界分离。
- Phase 7：完成 integrated teaching mock 设计与实现；实现承接 s12，不新增章节，不升级 s08/s10 状态。
- Phase 8：完成证据抽样复核，不更新目标 commit、不追最新 release、不升级章节状态。
- Phase 9：完成维护与 review checklist，作为后续贡献和提交前自查入口。

如果后续继续扩展 Phase 7 场景，必须另开 change 并继续保持 deterministic、offline、Python 标准库和非官方教学抽象；如果更新目标 commit 或追新 release，也必须另开 fact snapshot update change。

PR #1 merge 后，本轮 completed OpenSpec changes 已归档到 `openspec/changes/archive/`，长期规格位于 `openspec/specs/`。

## Phase 6 Status

Phase 6 本轮内容加厚已覆盖 s01~s06：每章补强了 PM 真正关心的问题、至少一个教学 failure path、mock trace 解读方式，以及不扩大官方事实边界的措辞。此进展只说明本教学仓的写作密度提升，不改变 `openai/codex` 官方事实快照，也不升级 s08/s10 状态。

Phase 6 当轮没有启动 integrated teaching mock。跨章端到端 trace 保留为 Phase 7 的后续问题：如果后续要把 loop、tool dispatch、permission decision、context pressure 和 instruction conflict 串成一个 mock，必须先走新的 OpenSpec proposal，并继续保持离线、确定性、非官方教学抽象。

## Phase 7 Status

Phase 7 integrated teaching mock 已通过 OpenSpec changes `design-integrated-teaching-mock-phase7` 和 `implement-integrated-teaching-mock-phase7` 完成设计与实现，并已归档为 `openspec/specs/integrated-teaching-mock-phase7/spec.md`。实现承接 s12：保留既有 `--path happy|failure` 兼容性，并新增 `--scenario` 教学场景覆盖 tool dispatch、permission denied、context pressure、instruction conflict 和 session recovery。

实现继续保持 deterministic、offline、Python 标准库和 “Teaching mock only” 免责声明；引用 s08/s10 时仍只能作为 `待核实` 边界，不得写成 OpenAI Codex 官方稳定产品承诺。

## Phase 8 Status

Phase 8 已通过 OpenSpec change `audit-evidence-drift-phase8` 完成证据抽样复核。本轮只检查固定 SHA、章节状态、s08/s10 边界、Phase 6 新增教学内容和维护清单，不更新目标 commit、不追最新 release、不实现 integrated teaching mock。

## Phase 9 Status

Phase 9 已完成本轮维护与 review 规则建设，入口见 [review-checklist.md](review-checklist.md)。本阶段只补开源维护、证据更新、外部 review 授权、Codex Desktop Lens 边界、教学 mock 免责声明和提交前检查清单，不改章节正文，不改变章节状态。

## Post-Phase 7 Backlog

Phase 7 implementation 已让 s12 具备可运行 integrated teaching trace。后续计划应从“更多机制事实”转向“让读者更快看懂 trace、边界和 failure path”，但仍不能放松事实边界。

| 优先级 | 待办 | 建议 change | 推进方式 | 验收口径 |
| --- | --- | --- | --- | --- |
| P0 | 收口 `design-diagram-redraw-style-guide` 轻量调研 | `design-diagram-redraw-style-guide` | 已完成并归档；不替换现有 Mermaid，不生成事实图。 | OpenSpec valid；确认主方案是手写 SVG、Mermaid 保留；FACT/待核实/TEACHING 标记规则清楚。 |
| P1 | s12 pilot trace 插图 | `implement-s12-diagram-redraw-pilot` | 已完成并归档；只做 s12 小样，优先 failure trace；不推广到全章全仓。 | 插图中文优先、可 diff、无外部生成依赖；不替换 `diagram.mmd`；s08/s10 保持 `待核实`。 |
| P2 | 事实快照更新评估 | `evaluate-fact-snapshot-refresh-phase10` | 已完成并归档；本轮保守不更新 target commit 或 release 核验值。 | 候选 commit 路径可访问不等于行号锚点和机制解释已复核；真正迁移需另开 implementation change。 |
| P3 | s08/s10 深核验 | `deep-verify-s08-sessions-rollout` / `deep-verify-s10-extensions-mcp-skills` | 已完成并归档；s08/s10 都继续保持 `待核实`，但局部机制证据更细。 | s08 真实 remote thread-store/产品恢复语义未闭环；s10 通用 extension 入口、dynamic tools 产品边界和统一治理未闭环。 |
| P4 | 开源维护收口 | `prepare-open-source-review-closeout-p4` | 已完成并归档；active OpenSpec changes 已清空。 | 工作树检查和 archive 校验通过后，summary 说明事实边界、未处理风险和归档结果。 |

`design-diagram-redraw-style-guide` 是已归档规格入口，不是全仓重绘许可。只有 s12 pilot 被 review 证明有教学价值后，才考虑是否抽象成 `docs/diagram-style-guide.md` 或推广到其他章节。

当前状态：P0 `design-diagram-redraw-style-guide`、P1 `implement-s12-diagram-redraw-pilot`、P2 `evaluate-fact-snapshot-refresh-phase10`、P3 `deep-verify-s08-sessions-rollout` / `deep-verify-s10-extensions-mcp-skills` 与 P4 `prepare-open-source-review-closeout-p4` 已完成本轮收口并归档。后续如果要迁移 target commit、继续升级 s08/s10 或推广 diagram style guide，仍需单独 change 或明确人类指令。

## Integrated Teaching Mock Planning

Phase 7 的 integrated mock 只做教学，不复刻 OpenAI Codex。它必须是确定性的、离线的、只依赖 Python 标准库，并明确声明不等同于 OpenAI Codex 或 Codex 桌面端。

计划覆盖的教学面如下：

| 教学面 | 要展示的问题 | 边界 |
| --- | --- | --- |
| loop | agent 如何在 turn 中接收输入、产出动作、读取 observation 并继续。 | 只展示控制流，不声明真实调度实现。 |
| tool dispatch | 工具名、参数、handler、结果回写如何形成闭环。 | 只使用本仓简化工具，不模拟所有官方 handler。 |
| permission decision | sandbox、approval、拒绝、重试如何影响体验。 | 不能从桌面端审批 UI 推断 CLI 实现。 |
| context pressure | 长任务中压缩、截断或摘要如何影响继续执行。 | 摘要策略只做教学抽象。 |
| instruction conflict | system/developer/user/project 指令冲突时如何解释下一步。 | 只展示教学优先级和解释方式，不复刻官方 prompt 策略。 |
| session trace | 事件、状态、history 与恢复线索如何帮助追责。 | 不声明官方持久化字段，除非有固定 SHA 证据。 |
| failure recovery | 外部服务延迟、凭据边界、工具失败后如何保留人类控制。 | failure path 来自产品问题，不来自官方事实断言。 |

## Release Readiness

未来任何 phase 声称完成前，至少要完成：

```bash
python3 scripts/check_docs.py
python3 scripts/run_all.py
python3 -m unittest discover -s tests
git diff --check
```

同时提交一段人工可读 review summary，说明：

- 新增或修改了哪些文档、章节或 mock。
- 哪些内容是官方事实，哪些是待核实、教学抽象或推断。
- 是否有章节状态变化，以及变化依据。
- 是否有未运行、失败或被跳过的检查。
