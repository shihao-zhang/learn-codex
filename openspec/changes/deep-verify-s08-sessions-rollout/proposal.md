## Why

s08 已完成 Phase 5 核验，但仍保留 `待核实`：主链路已经能追到 app-server、thread-store、rollout 和 `exec resume`，但 TUI、daemon、debug-client、remote store、experimental API 稳定性和状态归属边界还没有完全闭环。

本轮创建一个 focused deep verification change，只处理 `s08_sessions_threads_rollout`。目标不是追新，也不是强行升级章节，而是把“能升级的局部事实”和“必须继续待核实的边界”再压实。

## What Changes

- 使用当前 `docs/fact-snapshot.md` 固定 commit `740d942f901a5a63421298c74dafbeb4255e946d` 作为唯一源码事实基线。
- 复核并补充 s08 相关证据：thread-store、rollout replay、resume/fork、app-server、TUI/daemon/debug-client/remote store 边界。
- 必要时收窄 `chapters/s08_sessions_threads_rollout/README.md`，避免把局部源码路径升级成完整产品承诺。
- 必要时更新 `docs/source-evidence.md`，登记固定 SHA permalink、证据级别、已核实范围和未闭环原因。

## Capabilities

### New Capabilities

- `s08-sessions-rollout-deep-verification`: 定义 s08 deep verification 的官方事实基线、范围边界、升级规则和验证命令。

### Modified Capabilities

- 无。

## Impact

- 影响文档：`docs/source-evidence.md`、`chapters/s08_sessions_threads_rollout/README.md`。
- 影响 OpenSpec：新增本轮 focused change。
- 不更新 `docs/fact-snapshot.md`，不更新 `scripts/check_docs.py`。
- 不处理 s10、diagram redraw、Phase 7 mock 或全仓重构。
