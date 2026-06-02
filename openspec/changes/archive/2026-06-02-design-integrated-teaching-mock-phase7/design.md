## Context

本仓已有 12 个章节 mock，其中 s01~s06 解释核心机制，s08/s10 仍保持 `待核实`，s12 提供综合架构教学抽象。Phase 7 的价值不是新增官方事实，而是把已有教学面组织成一个可运行、可读 trace 的端到端体验，让 AI 产品经理看到 harness 组合关系。

这个 mock 的设计必须比单章 mock 更谨慎：它会跨越 loop、工具、权限、上下文、指令、session 和 failure recovery。任何跨章串联都容易被读者误解为真实 Codex 调用链，因此设计层必须先把“教学抽象”和“官方事实”切开。

## Goals / Non-Goals

**Goals:**

- 设计一个未来可实现的 integrated teaching mock，而不是本轮实现 mock。
- 覆盖 agent loop、tool dispatch、permission decision、context pressure、instruction conflict、session trace / recovery、failure recovery。
- 保持 deterministic、offline、Python 标准库、Teaching mock only。
- 复用本仓现有 mock 交互习惯：命令行可读文本和 `--trace-json` 结构化 trace。
- 让 trace 能回答产品问题：系统做到哪一步、为什么停下、是否需要人类授权、恢复时从哪里继续。
- 引用 s08/s10 时只作为 `待核实` 边界或产品风险提示，不升级为官方事实。

**Non-Goals:**

- 不实现 Phase 7 mock 代码。
- 不调用 OpenAI API、GitHub、网络、系统 Keychain、外部 CLI 或真实审批系统。
- 不模拟完整 OpenAI Codex 内部实现、wire format、事件类型、存储 schema 或权限 UI。
- 不把 Codex 桌面端体验写成 `openai/codex` 官方事实。
- 不修改 s08/s10 的章节状态，不新增未经证据登记的官方机制 claim。

## Decisions

1. Phase 7 integrated mock 应优先承接 s12，而不是新建 s13。

   s12 已经是综合架构教学抽象。未来实现宜增强 `chapters/s12_comprehensive_architecture/mock.py`，或让它委托到一个小型 integrated runtime；这样能避免新增章节编号、状态表和脚本清单的额外 churn。若后续发现 s12 过载，再另开 OpenSpec change 讨论拆分。

2. Trace contract 使用教学字段，不复用官方字段名作承诺。

   未来 JSON trace 可以包含 `index`、`kind`、`message`、`detail`，并在 `detail` 中使用 `teaching_session_id`、`teaching_checkpoint`、`decision_reason`、`context_budget_state` 等教学字段。字段名必须避免暗示它们等同于官方 session、rollout、thread-store 或 protocol schema。

3. 场景矩阵至少覆盖四类路径，但 CLI 兼容现有 happy/failure 习惯。

   推荐设计：

   | 场景 | 覆盖重点 | 读者看到什么 |
   | --- | --- | --- |
   | `happy` | loop、tool dispatch、permission allow、trace close | 一个任务如何从输入推进到答案 |
   | `permission_denied` | permission decision、failure recovery | 被拒绝的动作如何转为解释、降级或请人类选择 |
   | `context_conflict` | context pressure、instruction conflict | 上下文压力和指令冲突如何改变下一步 |
   | `session_recovery` | session trace / recovery、idempotent resume | 中断后如何从教学 checkpoint 继续，而不是重复危险动作 |

   为兼容现有脚本，未来可以让 `--path happy` 和 `--path failure` 继续可用；更细场景可通过 `--scenario` 增加。若增加新参数，测试必须保证默认用法仍稳定。

4. Permission model 只做策略演示。

   未来 mock 可以定义小型策略表，例如 `read_workspace=allow`、`write_workspace=allow_after_explanation`、`write_outside_workspace=deny`、`network=deny`。这只解释产品治理问题，不代表 OpenAI Codex 的真实审批策略、沙箱实现或桌面端 UI。

5. Context pressure 只做可解释阈值，不模拟真实 tokenization。

   未来 mock 可以使用固定整数预算，例如 `budget=100`、`used=92`、`summary_cost=20`。压缩动作应叫 `teaching_summary` 或等价名称，避免把它写成官方 compaction、rollout 或 context window 实现。

6. Instruction conflict 应展示优先级和可解释性，而不是发明隐藏规则。

   未来 mock 可用固定指令栈演示冲突：system/developer 要求 offline，user 要求联网。结果应是拒绝联网、改用离线 fixture 或询问人类。设计必须明确这是教学抽象，不是官方 prompt hierarchy 的完整复刻。

7. Failure recovery 的核心是“保留人类控制权”。

   失败路径不应只输出错误；它要记录 failure point、可恢复状态、下一步选项和停止原因。对 PM 来说，关键是用户能否理解系统为什么停、能否安全继续、是否会重复有副作用动作。

## Future Implementation Shape

本轮不实现，但为了后续评审可落地，建议未来实现保持以下形状：

- 入口：继续使用 `python3 chapters/s12_comprehensive_architecture/mock.py --demo`。
- 输出：文本输出必须包含 `Teaching mock only; not an OpenAI Codex implementation.` 或等价免责声明。
- JSON：`--trace-json` 输出稳定、可断言、无时间戳、无随机数、无机器路径。
- 代码：只使用 Python 标准库；不新增 `requirements.txt`、网络调用或外部进程。
- 测试：覆盖 happy、permission denial、context conflict、session recovery；断言输出稳定、免责声明存在、s08/s10 待核实边界存在。

## Risks / Trade-offs

- [Risk] integrated trace 看起来像官方实现。缓解方式：所有跨章字段使用教学命名，文本和 JSON 都保留免责声明。
- [Risk] s08/s10 被顺手写成稳定能力。缓解方式：session recovery 和 extension/tool 相关说明必须显式标注 `待核实`，不能升级章节状态。
- [Risk] 场景太多导致 PM 难读。缓解方式：默认 `happy` 展示主线，其他场景服务 failure path。
- [Risk] 为了像真实系统而引入复杂状态机。缓解方式：只保留教学需要的状态：turn、tool call、permission decision、context budget、checkpoint、recovery choice。
- [Risk] 未来实现改动 s12 后影响现有脚本。缓解方式：保留现有 CLI contract，并在 `scripts/run_all.py` 和单测中验证默认 happy/failure 路径。
