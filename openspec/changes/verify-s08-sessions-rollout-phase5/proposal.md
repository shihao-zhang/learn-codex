## Why

Phase 5 要先收敛 s08 的 session/thread/rollout 恢复链路，因为这一章最容易把局部源码路径误写成完整产品承诺。当前已有局部证据，但 app-server resume/fork、thread-store、rollout、CLI resume 之间的边界还需要更细证据登记。

## What Changes

- 只推进 `s08_sessions_threads_rollout` 的事实核验，不改 s10，不扩写其他章节正文。
- 补登记固定 SHA OpenAI 源码证据，覆盖 app-server `thread/resume` / `thread/fork`、thread-store 读写边界、rollout 持久化策略、resume response 的分页与 redaction。
- 必要时收窄 s08 README 的表述：能核实的写成局部官方事实，未闭环或不稳定字段继续标为 `待核实`。
- 给出状态判断；除非主链路、入口、关键类型和产品边界都闭环，否则不升级 s08。

## Capabilities

### New Capabilities

- `phase5-s08-verification`: 定义 Phase 5 中 s08 恢复链路核验、证据登记、保守状态判断和验证命令的要求。

### Modified Capabilities

- 无。

## Impact

- 影响文档：`docs/source-evidence.md` 与 `chapters/s08_sessions_threads_rollout/README.md`。
- 影响 OpenSpec：新增本轮 Phase 5 s08 核验 change。
- 不改代码、不引入依赖、不调用外部 review 服务、不改变 s10 或其他章节正文。
