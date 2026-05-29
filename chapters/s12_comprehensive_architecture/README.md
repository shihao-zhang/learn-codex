# s12_comprehensive_architecture

## 状态标签

状态：教学抽象

## 本章回答什么

Step 1 只固定边界：本章会把前 11 章串成端到端教学架构，但不会声称这是 OpenAI 官方架构图。

## 对产品与平台设计的意义

综合架构帮助读者把 loop、tools、context、permissions、sessions、models、extensions 和 app-server 放到同一张产品系统图里。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s12_comprehensive_architecture/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- end-to-end harness
- runtime boundaries
- product-facing states
- fact vs abstraction

## 真实 Codex 映射

- [codex-rs/core](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core)
- [codex-rs/protocol](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol)
- [codex-rs/app-server](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server)
- [codex-rs/Cargo.toml](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/Cargo.toml)

## 教学简化与生产差异

本章是教学抽象。任何总图都必须标注“不是官方架构图”，并链接回前 11 章的已核实事实。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 总图中的每条边必须能回到某章事实或显式标为教学抽象。
- [ ] 不绘制无法公开核验的 Codex Cloud 或内部系统。
