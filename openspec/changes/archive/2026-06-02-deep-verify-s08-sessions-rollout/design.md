## Context

P2 `evaluate-fact-snapshot-refresh-phase10` 已完成，结论是不更新 `docs/fact-snapshot.md` 的目标 commit，也不更新 `scripts/check_docs.py`。因此本轮继续使用当前 fact snapshot 固定 SHA 作为官方事实基线。

新候选 commit 只能说明追新风险，不能作为本轮官方证据来源。官方事实只能来自当前固定 SHA 的 OpenAI 源码 permalink、OpenAI 官方文档或 release note。

## Goals / Non-Goals

**Goals:**

- 深核 `thread-store`、rollout replay、resume/fork、app-server 的 s08 主链路证据。
- 明确 TUI、daemon、debug-client、remote store 和 experimental app-server API 的边界是否能闭环。
- 能升级的局部事实才升级；不能闭环的内容保持 `待核实`，并写明原因。
- 运行 OpenSpec 与仓库既有检查命令。

**Non-Goals:**

- 不处理 s10。
- 不做 diagram redraw。
- 不修改 Phase 7 mock。
- 不做全仓重构。
- 不把 Codex Desktop 体验写成 `openai/codex` 官方实现事实。
- 不用新候选 commit 作为官方事实来源。

## Verification Strategy

1. 先读当前 s08 README、`docs/source-evidence.md` 和当前 fact snapshot，确认已有证据与缺口。
2. 只读取固定 SHA 的 OpenAI 源码链接，围绕用户指定主题补证或收窄。
3. 对每个机制点给出三种结果之一：

   - `可升级局部事实`：能追到入口、类型或控制流，并能说明已核实范围。
   - `保持待核实`：只能证明路径存在，或缺少端到端调用/产品边界证据。
   - `缩窄表述`：已有文字容易把局部机制写成完整承诺，需要降级或加边界。

4. README 面向产品经理保留简洁结论；源码细节集中登记到 `docs/source-evidence.md`。

## Risks / Trade-offs

- [Risk] 把 experimental app-server 字段写成稳定产品能力。缓解：所有相关结论必须带稳定性边界。
- [Risk] 因为 TUI/daemon/debug-client 有路径或入口就推断完整恢复体验。缓解：路径存在只作为路径证据；缺少端到端链路时保持 `待核实`。
- [Risk] 证据表过密影响可读性。缓解：README 只写产品经理能读懂的边界和结论。
