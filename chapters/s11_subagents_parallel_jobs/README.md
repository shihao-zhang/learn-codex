# s11_subagents_parallel_jobs

## 状态标签

状态：待核实

## 本章回答什么

Step 1 只固定边界：本章将核实子任务、并行和委派相关源码是否属于开源 CLI harness 主线能力。

## 对产品与平台设计的意义

并行和委派会改变任务可预期性、成本、失败恢复和用户控制感。若它只是某个特定产品面的能力，就不应被写成 CLI harness 通用机制。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s11_subagents_parallel_jobs/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- agent jobs
- delegation
- parallel dispatch
- failure recovery

## 真实 Codex 映射

- [codex-rs/core/src/tools/handlers/agent_jobs.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers/agent_jobs.rs)
- [codex-rs/core/src/codex_delegate.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/codex_delegate.rs)
- [codex-rs/core/src/tools/parallel.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/parallel.rs)

## 教学简化与生产差异

本章当前待核实。Step 2 必须确认这些路径的真实职责，再决定是否讲成主线、旁支或删除。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 核实 agent_jobs 的用户可见入口和生命周期。
- [ ] 核实 parallel.rs 是工具并行、子代理并行，还是内部调度辅助。
