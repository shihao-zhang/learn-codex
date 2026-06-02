## Context

P4 closeout 后，PR #1 已创建并调用 Claude 做只读 review。Review 结论是无阻塞项，但建议补强两个低风险表述：

- s11 的学习地图状态需要更靠近读者入口的范围限定。
- Phase 8 audit 的固定链接计数需要避免被理解为未来实时事实。

本 change 只处理这些 review follow-up，不扩大事实边界。

## Goals / Non-Goals

**Goals:**

- 让 README 学习地图直接显示 s11 的已核实范围。
- 让 s11 README 状态段落与 glossary / Phase 8 audit 的待核实点完全对齐。
- 给 Phase 8 audit 的链接数量加上审计时点限定。
- 通过文档和 mock 校验。

**Non-Goals:**

- 不改变 s11 状态。
- 不重新核实 s11 源码。
- 不处理 Phase 7 OpenSpec 归档时的 `ADDED` requirement 收敛。
- 不更新 fact snapshot。
- 不再次调用外部 review。

## Decisions

1. 保持 s11 状态为 `已核实官方事实`。

   因为该章已登记源码机制证据足以支撑机制级状态；review 风险来自读者可能把机制级状态读成产品级承诺。

2. 在 README 学习地图直接加括号说明。

   读者入口比章节正文更早，所以范围说明应出现在状态旁边，而不仅留在 s11 README 内。

3. Phase 8 audit 保留数字，但加“审计当日统计”。

   数字对当时审计有价值；问题不是数字本身，而是缺少时间边界。

## Validation

完成后运行：

- `openspec validate address-pr-review-scope-clarifications --strict`
- `python3 scripts/check_docs.py`
- `python3 scripts/run_all.py`
- `python3 -m unittest discover -s tests`
- `git diff --check`
