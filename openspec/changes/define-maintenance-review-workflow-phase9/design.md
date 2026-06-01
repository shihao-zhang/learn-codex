## Context

本仓已经有三层约束：`AGENTS.md` 定义长期 agent 行为，`docs/sourcing.md` 定义事实来源，`scripts/check_docs.py` 用程序保护固定 SHA、章节状态和证据索引。Phase 9 需要补的是“维护者怎么做 review”：把这些约束整理为日常贡献前后都能执行的规则。

本 change 只补维护流程，不重新核验 `openai/codex` 源码，不更新章节正文，也不改变 `docs/fact-snapshot.md` 的目标 commit。

## Goals / Non-Goals

**Goals:**

- 给章节状态升级、保留和降级提供明确标准。
- 说明什么时候更新 `docs/source-evidence.md`，什么时候更新 `docs/fact-snapshot.md`。
- 把 Claude review、Codex Desktop Lens 和教学 mock 的边界写成 review checklist。
- 给维护者一份提交前检查清单，减少事实边界漂移。
- 保持面向 AI 产品经理的表达：先说明为什么，再给可执行规则。

**Non-Goals:**

- 不改章节正文，不补写 s08/s10 或其他章节内容。
- 不升级或降级任何章节状态。
- 不新增源码证据，不改变目标 commit 或 release 快照。
- 不实际调用 Claude、GitHub 或其他外部 review 服务。
- 不修改检查脚本，除非现有规则无法表达 Phase 9 维护要求。

## Decisions

1. 新增 `docs/review-checklist.md`，而不是把规则塞进 README。

   - README 继续承担学习地图和入口。
   - checklist 承担维护者操作规则，方便后续在 PR 或本地 review 时逐项核对。

2. 保持 `fact-snapshot.md` 和 `source-evidence.md` 的分工。

   - `fact-snapshot.md` 记录目标版本、主路径和易过期点。
   - `source-evidence.md` 记录机制级证据、已核实范围和未解决问题。
   - 行级证据变化优先更新 `source-evidence.md`；目标 commit、release 或主路径变化才更新快照。

3. 章节状态变化必须显式 review。

   - 升级需要机制级或行为级证据支撑，并同步 README、章节 README 和证据索引。
   - 降级同样是正常维护动作：当证据过期、表述过宽或主链路不再闭合时，应主动降级并说明原因。
   - 只证明路径存在不能升级章节状态。

4. 外部 review 默认需要人类授权。

   - Claude 等外部服务可能发送内部文档、diff 或代码，必须先说明范围、调用方式、成本和隐私影响。
   - 默认禁止会修改工作树或发布评论的副作用选项。
   - 云端多 agent / ultra review 需要单独授权。

5. Desktop Lens 和教学 mock 都必须停在“教学”边界内。

   - 桌面端体验只能生成源码问题、failure path 和产品设计启发。
   - mock 可以帮助理解机制，但必须离线、确定性、标准库优先，并且不声称等价于 OpenAI Codex。

## Risks / Trade-offs

- [Risk] checklist 变成又一份复盘文档 → 只保留触发条件、应做/禁做、何时问人。
- [Risk] 规则重复 `docs/sourcing.md` → checklist 只做维护流程入口，事实来源细则继续指向 sourcing 和证据索引。
- [Risk] 过度保守导致贡献者不敢改 → 明确“降级”和“保持待核实”也是合格维护结果。
- [Risk] 外部 review 被误用 → 把授权边界放进提交前 checklist，而不是藏在 AGENTS.md。
