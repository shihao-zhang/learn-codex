## Why

PR #1 的只读 Claude review 没有发现阻塞项，但指出两个值得合并前收窄的表达风险：

- README 学习地图把 s11 标为 `已核实官方事实`，读者可能忽略该章只核实到已登记源码机制。
- Phase 8 audit 写死固定 SHA 链接数量，未来链接数量变化时容易被误读为当前实时统计。

这两个问题不需要改变章节状态，也不新增官方事实；目标是把范围说明前置，让 reviewer 和读者更难误读。

## What Changes

- 在 README 学习地图的 s11 行补充“限已登记源码机制；入口/默认启用/v1-v2 待核实”。
- 在 s11 README 状态段落中显式加入 multi-agent v1/v2 体验差异仍需核实。
- 在 Phase 8 audit 中把 “190 个 permalink” 改成 “Phase 8 审计当日统计为 190 个”。

## Capabilities

### New Capabilities

- `review-scope-clarifications`: 定义 PR review follow-up 中的范围澄清规则。

## Impact

- 影响 `README.md`、`chapters/s11_subagents_parallel_jobs/README.md`、`docs/phase8-evidence-audit.md` 和本 OpenSpec change。
- 不新增 `openai/codex` 官方事实。
- 不改变 s11 状态，不升级或降级任何章节。
- 不修改 fact snapshot target commit、release 核验值或 `scripts/check_docs.py`。
