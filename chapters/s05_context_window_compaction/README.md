# s05_context_window_compaction

## 状态标签

状态：已核实官方事实

## 本章回答什么

Step 1 只固定边界：本章将解释上下文窗口、压缩、截断和上下文压力如何影响 agent 行为。

## 对产品与平台设计的意义

上下文管理决定成本、延迟、记忆可靠性和长任务体验。PM 需要知道“压缩”不是免费魔法，它会改变信息可见性。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s05_context_window_compaction/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- context window
- compaction
- truncation
- context pressure

## 真实 Codex 映射

- [codex-rs/core/src/compact.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact.rs)
- [codex-rs/core/src/compact_remote.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact_remote.rs)
- [codex-rs/core/src/compact_remote_v2.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/compact_remote_v2.rs)
- [codex-rs/core/src/thread_rollout_truncation.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/thread_rollout_truncation.rs)

## 教学简化与生产差异

本章不把 rollout 解释为 compaction；rollout 归入 s08。Python mock 只会展示上下文预算与压缩触发，不代表真实摘要质量。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 核实 compact 与 truncation 的触发条件。
- [ ] 明确 compaction 与 rollout 的边界。
