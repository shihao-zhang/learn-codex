# s06_prompts_instructions

## 状态标签

状态：已核实官方事实

## 本章回答什么

Step 1 只固定边界：本章将解释 system prompt、AGENTS.md 和多层指令如何进入 agent harness。

## 对产品与平台设计的意义

指令层级决定平台如何表达长期规则、项目规则和用户即时意图。它直接影响可控性、冲突处理和团队协作体验。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s06_prompts_instructions/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- system prompt
- AGENTS.md discovery
- instruction hierarchy
- conflict handling

## 真实 Codex 映射

- [codex-rs/protocol/src/prompts](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/prompts)
- [codex-rs/core/src/agents_md.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/agents_md.rs)

## 教学简化与生产差异

Python mock 只能展示指令优先级，不会包含官方 prompt 文本或任何私有 prompt。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 核实 AGENTS.md 搜索、合并和冲突规则。
- [ ] 禁止引用不可公开核验的 prompt 内容。
