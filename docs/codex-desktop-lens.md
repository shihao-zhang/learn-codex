# Codex Desktop Lens

Codex 桌面端体验可以帮助本仓提出更好的源码阅读问题，但它不是 `openai/codex` 开源 Rust CLI harness 的官方事实来源。

推荐链路是：

```text
桌面端观察 -> 源码阅读问题 -> 固定 SHA 证据或官方文档 -> 教学表达
```

禁止链路是：

```text
桌面端观察 -> 直接断言 openai/codex 官方实现
```

## Observation To Question

| 桌面端观察 | 可转化的产品问题 | 源码阅读问题 | 目标章节 |
| --- | --- | --- | --- |
| sandbox denial 或命令需要升级权限 | 人类什么时候应该被打断，什么时候应该让 agent 自动收敛？ | Rust CLI 如何计算 sandbox/approval 需求，失败后如何重试或停止？ | s04_shell_sandbox_permissions |
| 联网、全局配置、Keychain 或登录态受限 | agent 如何区分“工具坏了”和“权限边界挡住了”？ | config/auth/permission 边界在哪里，哪些失败不能直接判定为凭据失效？ | s04_shell_sandbox_permissions, s07_config_auth_models |
| 外部 review 或云端服务等待时间长 | 长任务如何让人类知道当前卡在哪里？ | event、trace、job 或 session 状态如何表达等待、取消、恢复？ | s02_protocol_events, s08_sessions_threads_rollout, s11_subagents_parallel_jobs |
| GitHub CLI 凭据在沙箱里不可见 | 产品要如何避免把安全边界误判成账号失效？ | auth/config 是否有明确的 credential source、fallback 和错误表达？ | s07_config_auth_models |
| 上下文变长后需要压缩或恢复任务 | agent 什么时候应该总结，什么时候应该保留原始 trace？ | compact、history、rollout 和 thread 恢复之间如何分工？ | s05_context_window_compaction, s08_sessions_threads_rollout |
| session 中断后继续执行 | 用户如何确认 agent 没有忘记目标和边界？ | session/thread id、history、resume/fork 与 app-server 状态如何串起来？ | s08_sessions_threads_rollout, s09_app_server_transport |
| trace 可读性影响信任 | PM 如何判断一个 agent 是否可追责？ | protocol event、outgoing message、thread status 的边界是什么？ | s02_protocol_events, s09_app_server_transport, s12_comprehensive_architecture |
| 如果观察到 plugins、skills 或动态工具出现 | 平台如何解释“能力是从哪里来的”？ | MCP、extension tool、skills instructions 和 tool registry 的关系是什么？ | s03_tool_registry_dispatch, s10_extensions_mcp_skills |

## Use Rules

- 在章节中使用桌面端材料时，必须标注为“观察视角”“产品设计启发”或“源码阅读问题”。
- 任何 `openai/codex` 官方实现事实仍必须来自固定 SHA 的 OpenAI 源码 permalink、OpenAI 官方文档或 release note。
- 无法核验的内容必须标为 `待核实`、`教学抽象` 或句子级 `推断`。
- mock 可以借用桌面端体验设计 failure path，但必须保留非官方教学免责声明，不能暗示与 Codex 桌面端行为等价。
- 不把 Claude Code、Codex 桌面端、其他 agent 产品或本机工具体验直接套到 `openai/codex` 开源实现上。

## Failure Path Examples

- sandbox denial：适合作为“权限摩擦如何影响用户控制”的产品问题，再回到 s04 查 approval 与 sandbox 控制流。
- external review latency：适合作为“长任务如何报告等待状态”的产品问题，再回到 s02/s08/s11 查事件、session 与 job 表达。
- credential boundary：适合作为“不要把沙箱凭据不可见误判成 token 失效”的产品问题，再回到 s07 查 auth/config 边界。
- long-task recovery：适合作为“恢复后如何保留目标、证据和停止条件”的产品问题，再回到 s05/s08 查 compaction 与 thread 恢复。
- trace readability：适合作为“人类如何审计 agent 做了什么”的产品问题，再回到 s02/s09/s12 查 protocol event、transport 与架构抽象。
