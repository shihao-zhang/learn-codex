# s08_sessions_threads_rollout

## 状态标签

状态：待核实

## 本章回答什么

本章解释长任务恢复的产品问题：一次 agent 工作如何被识别、历史如何被关联、进程中断后用户如何继续。当前状态仍是待核实：本章已核实 `session_id.rs`、`thread_id.rs`、`ThreadStore` trait、rollout 记录、`InitialHistory::Resumed/Forked`、`thread/resume` / `thread/fork` 的 app-server 主链路，以及 `codex exec resume` 通过 app-server API 恢复的路径。

但这还不足以升级整章：app-server 协议里有 experimental 字段，TUI/daemon/remote store 与所有用户可见恢复体验尚未逐一闭环。因此，本章采用“局部官方事实 + 待核实产品边界”的写法：把 session、thread、rollout、resume 作为理解会话恢复的概念框架，但不把局部源码证据扩写成稳定产品承诺。

## 对产品与平台设计的意义

会话恢复决定长任务是否可靠。用户关心的不是内部叫 session 还是 thread，而是：关闭终端后能不能回来，回来后 agent 知不知道做到哪里，失败时能不能解释丢了什么，多个窗口会不会串线。

平台设计时要把“身份”“历史”“恢复”拆开：身份用于定位一次工作或一条对话，历史用于保存可重放/可摘要的事实，恢复用于决定重新进入任务时应加载哪些内容。三者混在一起，会让产品很难解释失败：到底是找不到会话、历史损坏、上下文太长，还是恢复策略主动丢弃了部分内容。

## 机制图

见 [diagram.mmd](diagram.mmd)。该图只表达待核实章节的阅读框架：app-server 主链路已有更多源码证据，但完整产品边界仍待核实；它不是官方数据流图。

## 运行 mock

```bash
python3 chapters/s08_sessions_threads_rollout/mock.py --demo
```

这个 mock 只演示一种教学上的区分：session 可理解为运行中的交互身份，thread 可理解为对话或任务线索，rollout-style history 可理解为用于恢复的历史记录。以上都是教学抽象，不代表真实 Codex 行为。

## 核心机制

- `session id`：源码显示 `SessionId::new()` 使用 UUID v7，并可与 `ThreadId` 按 UUID 相互转换。生命周期、跨进程语义和产品展示仍需结合调用链核实。
- `thread id`：源码显示 `ThreadId::new()` 使用 UUID v7，并支持字符串解析。它与 session 的关系、是否跨设备或跨进程稳定，仍需端到端核实。
- `rollout`：教学上表示可保存、可回放或可截断的历史轨迹。源码显示 rollout writer 会把 canonical items 写入 JSONL；读取时可解析为 `InitialHistory::Resumed`。但 limited/extended 持久化策略会过滤事件，不能假设所有运行时事件都会完整保留。
- `resume`：源码显示 app-server 的 cold resume 可从显式 history、thread id 或 rollout path 构造初始历史；running thread rejoin 会复用 live thread 并发送 resume response；core 会对 `InitialHistory::Resumed/Forked` 做 rollout reconstruction、token 信息恢复和 persist/flush。真实产品体验与所有客户端边界仍需继续核实。
- `fork`：源码显示 app-server fork 会读取源 thread history，并用 `ForkSnapshot::Interrupted` 创建新 thread；持久 fork 和 ephemeral fork 的可见历史来源不同。该结论只覆盖 app-server 代码路径。
- `exec resume`：源码显示 `codex exec resume` 通过 in-process app-server 的 `thread/list` + `thread/resume` 恢复，而不是直接读取 rollout 存储。该结论不覆盖 TUI、debug-client、daemon 或桌面端。
- `thread rollout truncation`：路径已在事实快照登记；其职责边界需要继续读源码确认，不能直接等同于 s05 的 compaction。

## 真实 Codex 映射

- [codex-rs/protocol/src/session_id.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/session_id.rs)
- [codex-rs/protocol/src/thread_id.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/thread_id.rs)
- [codex-rs/app-server-protocol/src/protocol/v2/thread.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server-protocol/src/protocol/v2/thread.rs)
- [codex-rs/app-server/src/request_processors/thread_processor.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server/src/request_processors/thread_processor.rs)
- [codex-rs/core/src/thread_rollout_truncation.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/thread_rollout_truncation.rs)
- [codex-rs/thread-store](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/thread-store)
- [codex-rs/rollout](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/rollout)
- [codex-rs/exec/src/lib.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/exec/src/lib.rs)

以上固定 SHA 链接是本章的官方事实入口。由于本章状态仍为待核实，本文不把局部机制证据扩写成完整产品语义或稳定恢复承诺。

机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)。当前证据足以支持 id 生成、thread-store trait/local store、app-server cold resume/running rejoin/fork、rollout replay、initial turns pagination、response-only redaction、exec resume API 路径等局部事实；不足以支持所有客户端和稳定产品语义的完整恢复承诺。

## 教学简化与生产差异

教学版把问题拆成四块：创建身份、关联历史、写入记录、恢复继续。这个拆法适合产品理解，但生产实现可能会有不同的边界：历史可能分层存储，恢复可能依赖索引或摘要，过长历史可能需要截断，异常恢复可能需要用户选择。

本章不会先声明 rollout 的完整生产职责，也不会把 `thread_rollout_truncation.rs` 直接解释为 compaction。s05 处理“下一轮模型看什么”的上下文预算问题；s08 关注“历史如何被识别、保存、恢复”的会话连续性问题。二者可能相关，但本章目前仍保留待核实边界。

另一个边界是 redaction：源码注释明确 app-server resume 的 redaction 是 response-only，用于特定 remote client 的返回 payload；它不改变 persisted rollout history、model resume history 或其他 API。因此不能把它写成完整隐私策略。

## 练习

1. 运行 mock，区分 happy path 中的 session、thread、persist、resume 四个事件分别回答什么产品问题。
2. 设计一个恢复失败提示：分别说明“找不到 thread”“历史存在但不可用”“历史太长需要截断”时用户该看到什么。
3. 给一个 agent 平台画出你期望的恢复策略：自动恢复、询问恢复、从摘要恢复、重新开始，分别适合什么场景。
4. 阅读本章真实映射链接时，只记录“已核实路径”和“待核实行为”，不要把变量名或目录名直接升级成产品结论。

## 事实核验清单

- [x] 核实 `SessionId` / `ThreadId` 的 UUID v7 生成入口。
- [x] 核实 `ThreadStore` trait 中 create/resume/append/load/read 的存储边界。
- [x] 核实 `InitialHistory::Resumed/Forked` 会触发 rollout reconstruction 和历史替换。
- [x] 核实 app-server resume 请求、thread-store 读取、rollout reconstruction、running rejoin、history pagination 和 response redaction 的主源码路径。
- [x] 核实 `codex exec resume` 通过 app-server `thread/list` + `thread/resume` 恢复。
- [ ] 明确 TUI、daemon、debug-client、remote store 与 experimental app-server API 的稳定边界；在完成前保持本章状态为待核实。
- [ ] 明确哪些状态由 CLI、app-server 或存储 crate 维护；在完成前保持本章状态为待核实。
