## Context

Phase 7 的设计 change 已经明确：integrated teaching mock 应承接 s12，而不是新增章节。s12 当前定位为综合架构教学抽象，因此适合把前面章节的核心产品问题串成一条端到端 trace。

实现时最重要的约束不是“像真实 Codex”，而是“让读者看懂 harness 设计问题，并明确知道这不是官方实现”。因此所有新增字段、场景和命令都使用教学命名，避免复用或暗示官方 session、thread-store、MCP、skills、approval UI、protocol schema 或桌面端状态。

## Goals / Non-Goals

**Goals:**

- 实现一个 deterministic、offline、Python 标准库 only 的 s12 integrated teaching mock。
- 覆盖 happy path 和关键 failure path：tool dispatch、permission decision、context pressure、instruction conflict、session recovery。
- 让文本输出和 JSON trace 都包含 `Teaching mock only` 免责声明。
- 让 JSON trace 保持稳定、可断言、无时间戳、无随机数、无机器路径。
- 保持 `scripts/run_all.py` 现有 happy/failure 路径可运行。
- 保持 s08/s10 的 `待核实` 边界，不更新章节状态。

**Non-Goals:**

- 不复刻 OpenAI Codex 官方实现、Codex 桌面端实现或真实 wire format。
- 不调用 OpenAI API、网络、Keychain、外部 CLI、真实桌面端状态或真实审批系统。
- 不新增第三方依赖。
- 不改变 s01~s11 的教学 mock 行为。
- 不把 session/thread/rollout、MCP、skills 或 extensions 写成已核实官方主线能力。

## Decisions

1. 通过共享 runtime 增加可选 `--scenario`，但保留 `--path`。

   现有章节和 runner 都依赖 `--path happy|failure`。实现会在 `TeachingScenario` 中增加可选场景表；只有 s12 使用 `--scenario`。其他章节的 CLI 行为不变。

2. `--path failure` 使用 combined failure summary。

   为了兼容现有 runner，`--path failure` 会展示一个短的综合失败链路：工具派发失败、权限拒绝、上下文压力、指令冲突和恢复停止点。更细解释通过 `--scenario tool_dispatch_error|permission_denied|context_pressure|instruction_conflict|session_recovery` 提供。

3. Trace 字段使用教学命名。

   事件仍保持 `index`、`kind`、`message`、`detail`。`detail` 中允许使用 `teaching_session_id`、`teaching_checkpoint`、`decision_reason`、`context_budget_state`、`recovery_choice`、`s08_boundary`、`s10_boundary` 等字段。这些字段只服务教学，不声称等同于官方 schema。

4. Session recovery 是幂等恢复教学，不是真实会话存储声明。

   `session_recovery` 场景只展示“从教学 checkpoint 继续、避免重复有副作用动作、把下一步选择交还给人类”。它必须标注 s08 为 `待核实`。

5. Skills/MCP 只作为边界提醒。

   如果 integrated mock 提到 tool registry、skills 或 MCP，只能说这是教学问题或待核实扩展面；不得把 s10 升级为稳定官方机制。

## Validation

完成后运行：

- `openspec validate implement-integrated-teaching-mock-phase7 --strict`
- `python3 scripts/check_docs.py`
- `python3 scripts/run_all.py`
- `python3 -m unittest discover -s tests`
- `git diff --check`

## Risks / Trade-offs

- [Risk] 场景字段像官方 trace。缓解：字段使用 `teaching_*` 命名，并在 README 和输出中保留免责声明。
- [Risk] runtime 扩展影响其他章节。缓解：新增能力默认为空，现有 `--path happy|failure` 不变。
- [Risk] failure path 过长。缓解：默认 failure 是短摘要，细节拆到 `--scenario`。
- [Risk] s08/s10 被误解为已实现能力。缓解：输出和 README 显式保留 `待核实`。
