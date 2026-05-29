# s08_sessions_threads_rollout

## 状态标签

状态：待核实

## 本章回答什么

本章解释长任务恢复的产品问题：一次 agent 工作如何被识别、历史如何被关联、进程中断后用户如何继续。当前状态仍是待核实：本章已核实 `session_id.rs`、`thread_id.rs`、`ThreadStore` trait、rollout 记录、`InitialHistory::Resumed/Forked` 等局部机制，但从 app-server resume 请求到 thread-store/rollout/reconstruction 的完整数据流尚未闭环。

因此，本章采用“局部官方事实 + 待核实端到端语义”的写法：把 session、thread、rollout、resume 作为理解会话恢复的概念框架，但不把局部源码证据扩写成完整恢复承诺。

## 对产品与平台设计的意义

会话恢复决定长任务是否可靠。用户关心的不是内部叫 session 还是 thread，而是：关闭终端后能不能回来，回来后 agent 知不知道做到哪里，失败时能不能解释丢了什么，多个窗口会不会串线。

平台设计时要把“身份”“历史”“恢复”拆开：身份用于定位一次工作或一条对话，历史用于保存可重放/可摘要的事实，恢复用于决定重新进入任务时应加载哪些内容。三者混在一起，会让产品很难解释失败：到底是找不到会话、历史损坏、上下文太长，还是恢复策略主动丢弃了部分内容。

## 机制图

见 [diagram.mmd](diagram.mmd)。该图只表达待核实章节的阅读框架：局部机制已核实，端到端恢复语义待核实；它不是官方数据流图。

## 运行 mock

```bash
python3 chapters/s08_sessions_threads_rollout/mock.py --demo
```

这个 mock 只演示一种教学上的区分：session 可理解为运行中的交互身份，thread 可理解为对话或任务线索，rollout-style history 可理解为用于恢复的历史记录。以上都是教学抽象，不代表真实 Codex 行为。

## 核心机制

- `session id`：源码显示 `SessionId::new()` 使用 UUID v7，并可与 `ThreadId` 相互转换。生命周期、跨进程语义和产品展示仍需结合调用链核实。
- `thread id`：源码显示 `ThreadId::new()` 使用 UUID v7，并支持字符串解析。它与 session 的关系、是否跨设备或跨进程稳定，仍需端到端核实。
- `rollout`：教学上表示可保存、可回放或可截断的历史轨迹。源码显示 rollout line 会序列化为 JSONL，并带 timestamp；完整生产职责仍需结合 thread-store 与 app-server 核实。
- `resume`：源码显示 `InitialHistory::Resumed/Forked` 会重建历史、处理 token 信息并 flush/persist。真实恢复会加载哪些内容、如何处理缺失或过长历史，仍需完整核实。
- `thread rollout truncation`：路径已在事实快照登记；其职责边界需要继续读源码确认，不能直接等同于 s05 的 compaction。

## 真实 Codex 映射

- [codex-rs/protocol/src/session_id.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/session_id.rs)
- [codex-rs/protocol/src/thread_id.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/thread_id.rs)
- [codex-rs/core/src/thread_rollout_truncation.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/thread_rollout_truncation.rs)
- [codex-rs/thread-store](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/thread-store)
- [codex-rs/rollout](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/rollout)

以上固定 SHA 链接是本章的官方事实入口。由于本章状态仍为待核实，本文不把局部机制证据扩写成完整恢复数据流或产品语义。

机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)。当前证据足以支持 id 生成、thread-store trait、resume/fork 初始历史处理等局部事实；不足以支持完整恢复体验承诺。

## 教学简化与生产差异

教学版把问题拆成四块：创建身份、关联历史、写入记录、恢复继续。这个拆法适合产品理解，但生产实现可能会有不同的边界：历史可能分层存储，恢复可能依赖索引或摘要，过长历史可能需要截断，异常恢复可能需要用户选择。

本章不会先声明 rollout 的完整生产职责，也不会把 `thread_rollout_truncation.rs` 直接解释为 compaction。s05 处理“下一轮模型看什么”的上下文预算问题；s08 关注“历史如何被识别、保存、恢复”的会话连续性问题。二者可能相关，但本章目前只保留待核实边界。

## 练习

1. 运行 mock，区分 happy path 中的 session、thread、persist、resume 四个事件分别回答什么产品问题。
2. 设计一个恢复失败提示：分别说明“找不到 thread”“历史存在但不可用”“历史太长需要截断”时用户该看到什么。
3. 给一个 agent 平台画出你期望的恢复策略：自动恢复、询问恢复、从摘要恢复、重新开始，分别适合什么场景。
4. 阅读本章真实映射链接时，只记录“已核实路径”和“待核实行为”，不要把变量名或目录名直接升级成产品结论。

## 事实核验清单

- [x] 核实 `SessionId` / `ThreadId` 的 UUID v7 生成入口。
- [x] 核实 `ThreadStore` trait 中 create/resume/append/load/read 的存储边界。
- [x] 核实 `InitialHistory::Resumed/Forked` 会触发 rollout reconstruction 和历史替换。
- [ ] 核实 app-server resume 请求、thread-store 读取、rollout reconstruction、history pagination 和 redaction 的端到端数据流。
- [ ] 明确哪些状态由 CLI、app-server 或存储 crate 维护；在完成前保持本章状态为待核实。
