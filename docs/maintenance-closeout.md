# Maintenance Closeout

本页是 P4 开源维护收口记录。它服务 reviewer 和后续维护者：说明当前分支做了什么、没有做什么、事实边界如何保持、以及下一步风险应该怎样拆开。

本页不新增 `openai/codex` 官方事实。官方事实仍只来自 [fact-snapshot.md](fact-snapshot.md)、[source-evidence.md](source-evidence.md) 和各章节固定 SHA 引用。

## Review Status

当前分支：`main`（PR #1 已合并）

PR #1 中的主要提交：

| Commit | 主题 |
| --- | --- |
| `9695f9d` | Phase 5~9 roadmap/documentation closure |
| `39162ff` | Phase 7 integrated teaching mock |
| `aea8608` | Diagram redraw backlog |
| `df30904` | s12 diagram redraw pilot |
| `540a5a3` | Phase 10 fact snapshot refresh evaluation |
| `69d3191` | s08/s10 deep verification |

P4 收口已完成 review 并合入 `main`。本次 archive cleanup 只处理 merge 后 OpenSpec 维护状态，不推送、不创建 PR。

## What Changed

- 项目目标和路线：新增 roadmap、goal alignment、Codex Desktop Lens 边界、Phase 5 / Phase 8 summary。
- 前 6 章内容密度：s01~s06 补强 PM 问题、failure path 和 mock trace 读法。
- 高风险章节：s08 和 s10 经过 Phase 5 与 P3 两轮核验，局部机制证据更细，但章节状态继续 `待核实`。
- 教学 mock：s12 落地 integrated teaching mock，保持 deterministic、offline、Python 标准库和 `Teaching mock only`。
- 图形表达：新增 diagram redraw style guide 和 s12 failure trace SVG pilot；Mermaid 仍是主机制图。
- 维护规则：新增 review checklist、P4 closeout，并在 merge 后完成 OpenSpec change 归档清点。

## Fact Boundaries

- `docs/fact-snapshot.md` 的 target commit 未迁移，仍为当前固定 SHA。
- `scripts/check_docs.py` 的 `SOURCE_COMMIT` 未改变。
- P2 评估过更新候选 commit，但结论是路径可访问不等于行号锚点和机制解释已复核，因此不迁移。
- s08 继续 `待核实`：真实 remote thread-store backend、Codex Cloud / 桌面端产品恢复语义、experimental app-server API 稳定承诺仍未闭环。
- s10 继续 `待核实`：通用 extension tools 用户安装/发现/授权入口、dynamic tools 产品边界、四类能力统一治理语义仍未闭环。
- s12 继续 `教学抽象`：integrated mock 和 SVG pilot 只帮助读者理解 trace，不代表 OpenAI 官方架构。
- Codex Desktop Lens 只能作为观察视角、源码阅读问题和产品设计启发，不能作为官方事实。

## Archived OpenSpec Changes

这些 changes 已随 PR #1 merge 后的 archive cleanup 归档到 `openspec/changes/archive/`；`openspec list` 当前显示无 active changes。主规格已生成在 `openspec/specs/`。

Phase 7 的 `design-integrated-teaching-mock-phase7` 与 `implement-integrated-teaching-mock-phase7` 原本都对 `integrated-teaching-mock-phase7` 使用 `ADDED Requirements`。归档后已在主规格中合并为长期要求，去掉 design-only 与 future implementation 的临时重复语义。

| 分组 | Archived changes |
| --- | --- |
| 基础证据与路线 | `implement-phase-3-4`, `define-next-phase-roadmap` |
| Phase 5 | `verify-s08-sessions-rollout-phase5`, `verify-s10-extensions-mcp-skills-phase5`, `summarize-phase5-verification` |
| Phase 6~9 | `densify-foundation-chapters-phase6`, `design-integrated-teaching-mock-phase7`, `audit-evidence-drift-phase8`, `define-maintenance-review-workflow-phase9` |
| Phase 7 implementation | `implement-integrated-teaching-mock-phase7` |
| Diagram line | `design-diagram-redraw-style-guide`, `implement-s12-diagram-redraw-pilot` |
| Fact line | `evaluate-fact-snapshot-refresh-phase10` |
| P3 deep verification | `deep-verify-s08-sessions-rollout`, `deep-verify-s10-extensions-mcp-skills` |
| P4 closeout | `prepare-open-source-review-closeout-p4` |

## PR Summary Draft

本 PR 把 `learn-codex` 从初版章节仓推进到可维护的中文教学仓：

- 建立后续路线、项目目标对齐、Codex Desktop Lens 边界和维护 review checklist。
- 对 s08/s10 做两轮高风险核验；两章局部机制证据增强，但状态继续 `待核实`。
- 加厚 s01~s06 的产品问题、failure path 和 mock trace 解释。
- 在 s12 实现 integrated teaching mock，并新增一张中文优先的 failure trace SVG pilot。
- 评估 fact snapshot 是否追新；本轮保守不迁移 target commit 或 release 核验值。
- 补充 P4 maintenance closeout，说明 OpenSpec changes、事实边界、检查结果和后续风险。

未改变：

- 未更新 fact snapshot target commit。
- 未把 s08/s10 升级为已核实官方事实。
- 未把教学 mock、diagram pilot 或 Codex Desktop 观察写成 OpenAI 官方实现。
- 未调用外部 review、未推送、未创建 PR。

## Review Checklist

- README 学习地图仍显示 s08/s10 为 `待核实`，s12 为 `教学抽象`。
- s08/s10 新增主引用能在 `docs/fact-snapshot.md` 或 `docs/source-evidence.md` 追到。
- SVG pilot 是可选教学图，不替换 `diagram.mmd`。
- Phase 7 mock 输出保留 `Teaching mock only`，且不调用外部 API。
- P2 的候选 commit 只作为追新风险，不作为当前证据基线。

## Remaining Risks

- 真正迁移到 P2 候选 commit 需要单独 implementation change，逐章复核行号锚点和机制解释。
- s08 若要升级，需要闭合真实 remote thread-store backend、产品恢复语义和 experimental API 稳定性。
- s10 若要升级，需要闭合通用 extension 用户入口、dynamic tools 客户端边界和统一治理路径。
- diagram style guide 若要推广，需要先抽成 `docs/diagram-style-guide.md`，再做少量章节试点。
- 已归档 specs 若继续演进，应另开 OpenSpec change；本次归档不改变 fact snapshot、s08/s10 状态或 s12 教学抽象边界。

## Validation

P4 收口检查结果：

- `openspec validate prepare-open-source-review-closeout-p4 --strict`: passed.
- `python3 scripts/check_docs.py`: passed.
- `python3 scripts/run_all.py`: passed, 24 paths / 94 events.
- `python3 -m unittest discover -s tests`: passed, 13 tests.
- `git diff --check`: passed.
