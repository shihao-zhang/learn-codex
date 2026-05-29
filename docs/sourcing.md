# Sourcing Rules

本仓的核心目标不是资料索引，而是把 Codex CLI harness 的机制讲清楚。越是高密度教学，越容易把推断写成事实，所以任何官方事实都必须先过溯源规则。

## 三选一规则

每条官方事实必须满足以下三类之一：

1. 固定 commit SHA 的 OpenAI 源码 permalink。
2. OpenAI 官方文档、release note 或官方 README。
3. 明确标注为“待核实”“教学抽象”或行内“推断”。

不能用社区文章、教学 mock、其他 agent 产品经验来证明 Codex 官方实现。

## Permalink 要求

源码链接必须使用固定 SHA，不使用 `main`、`master` 或 tag 作为事实依据。合格示例：

```text
https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/agents_md.rs
```

目录链接也必须带固定 SHA：

```text
https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools
```

Step 1 骨架阶段，每章必须至少包含一个固定 SHA 的 Codex 源码 permalink。Step 2 如出现只依赖官方文档或 release note 的章节，必须同步放宽 `scripts/check_docs.py` 并在本文件记录新规则。

## 写作标签

- `已核实官方事实`：本章的官方锚点已经进入当前事实快照，且章节主映射已经对照官方源码或官方文档核实。它不表示每个字段、函数名、错误分支或产品解释都已逐行核实；未下钻的细节必须继续放在本章“事实核验清单”中。
- `待核实`：路径可能已核实存在，但章节主映射、行为边界或能力语义仍需继续读源码确认。路径存在不等于行为已核实。
- `教学抽象`：为了帮助理解而设计的简化模型，不声称是官方架构。
- `推断`：基于公开事实的解释性判断，必须说明推断链路；它不是章节级状态，只能用于句子或段落。

## 禁止项

- 禁止把 Python mock 写成 Codex 官方实现。
- 禁止把社区讨论、博客理解或课程比喻写成官方事实。
- 禁止把 Claude Code、其他 agent 平台或内部工具的概念直接套到 Codex 上。
- 禁止引用泄漏材料、私有 prompt 或无法公开核验的内容。

## 更新流程

1. 更新 [fact-snapshot.md](fact-snapshot.md) 的目标 commit、release 和核验日期。
2. 批量检查章节中的 GitHub 链接是否使用新的固定 SHA。
3. 对状态为 `待核实` 的章节重新读源码，再决定是否升级为 `已核实官方事实`。
4. 运行 `python3 scripts/check_docs.py` 和 `python3 -m unittest discover -s tests`。
