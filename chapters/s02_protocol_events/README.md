# s02_protocol_events

## 状态标签

状态：已核实官方事实

## 本章回答什么

Step 1 只固定边界：本章将解释 Codex 的 protocol、事件、输入输出项和 trace 如何让运行时与界面同步。

## 对产品与平台设计的意义

事件协议决定用户看到的进度、错误、工具状态和恢复体验。PM 需要理解事件不是日志，而是产品状态的契约。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s02_protocol_events/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- protocol event
- input/output item
- trace
- schema drift

## 真实 Codex 映射

- [codex-rs/protocol/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src)

## 教学简化与生产差异

Step 2 的 mock 会使用少量简化事件名；正式内容必须把简化事件映射回真实 protocol crate 类型，或明确标注为教学抽象。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 核实真实事件类型和字段命名。
- [ ] 不把 mock trace 当成官方 wire format。
