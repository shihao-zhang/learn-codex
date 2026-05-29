# s08_sessions_threads_rollout

## 状态标签

状态：待核实

## 本章回答什么

Step 1 只固定边界：本章将解释 session、thread、恢复和 rollout 持久化。当前只确认相关路径存在，具体数据流待核实。

## 对产品与平台设计的意义

会话恢复决定长任务是否可靠、用户能否跨设备/跨进程继续，以及失败后能否解释“做到哪里了”。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s08_sessions_threads_rollout/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- session id
- thread id
- rollout
- resume

## 真实 Codex 映射

- [codex-rs/protocol/src/session_id.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/session_id.rs)
- [codex-rs/protocol/src/thread_id.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/thread_id.rs)
- [codex-rs/core/src/thread_rollout_truncation.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/thread_rollout_truncation.rs)
- [codex-rs/thread-store](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/thread-store)
- [codex-rs/rollout](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/rollout)

## 教学简化与生产差异

本章当前待核实，不会先声明 rollout 的完整生产职责。Step 2 必须先读源码再写数据流。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 核实 session、thread、rollout 的职责边界。
- [ ] 明确哪些状态由 CLI、app-server 或存储 crate 维护。
