# s01_agent_loop

## 状态标签

状态：已核实官方事实

## 本章回答什么

Step 1 只固定边界：本章将解释 agent loop、turn 与 tool observation 如何构成 Codex CLI harness 的基本执行循环。

## 对产品与平台设计的意义

本章关注“一个 agent 何时继续、何时停下、何时需要工具结果”的产品语义，后续内容会把它翻译成用户可感知的进度、等待、失败和完成状态。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s01_agent_loop/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- agent loop
- turn
- tool observation
- loop termination

## 真实 Codex 映射

- [codex-rs/core/src/agent](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/agent)
- [codex-rs/core/src/tools](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools)

## 教学简化与生产差异

Step 2 的 Python mock 只会解释控制流，不会复刻 Rust async runtime、真实模型非确定性、错误恢复和并发调度。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 逐文件核实 loop 的入口、turn 边界和工具 observation 的真实类型。
- [ ] 避免把 Python mock 的函数名写成官方 Rust 类型名。
