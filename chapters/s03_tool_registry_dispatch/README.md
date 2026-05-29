# s03_tool_registry_dispatch

## 状态标签

状态：已核实官方事实

## 本章回答什么

Step 1 只固定边界：本章将解释工具如何声明、注册、路由到 handler，并把结果送回运行时。

## 对产品与平台设计的意义

工具系统决定 agent 能做什么、何时暴露能力、失败后如何解释。它直接影响平台的能力边界、权限边界和可观测性。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s03_tool_registry_dispatch/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- tool spec
- registry
- router
- handler

## 真实 Codex 映射

- [codex-rs/core/src/tools/registry.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/registry.rs)
- [codex-rs/core/src/tools/router.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/router.rs)
- [codex-rs/core/src/tools/handlers](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers)

## 教学简化与生产差异

Python mock 会把工具注册压成极小接口；真实实现涉及 schema、handler 生命周期、权限和错误传播。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 核实 registry 与 router 的职责边界。
- [ ] 区分内置工具、动态工具和外部工具。
