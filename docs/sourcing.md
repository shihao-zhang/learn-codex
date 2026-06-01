# Sourcing Rules

本仓的核心目标不是资料索引，而是把 Codex CLI harness 的机制讲清楚。越是高密度教学，越容易把推断写成事实，所以任何官方事实都必须先过溯源规则。

## 三选一规则

每条官方事实必须满足以下三类之一：

1. 固定 commit SHA 的 OpenAI 源码 permalink。
2. OpenAI 官方文档、release note 或官方 README。
3. 明确标注为“待核实”“教学抽象”或行内“推断”。

不能用社区文章、教学 mock、其他 agent 产品经验来证明 Codex 官方实现。Codex 桌面端体验也只能作为观察视角、产品设计启发或源码阅读问题，不能作为 `openai/codex` 官方事实来源。

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

## 证据索引

本仓使用统一证据索引：[source-evidence.md](source-evidence.md)。每条机制级证据必须包含：

- 章节：对应 `s01_*` 到 `s12_*`。
- 机制点：这条证据回答的具体机制问题。
- 证据级别：`path-exists`、`mechanism-verified`、`behavior-verified`、`pending` 或 `teaching-abstract`。
- 源码证据：固定 commit SHA 的 OpenAI 源码 permalink；教学抽象也要尽量指向被组合的官方源码范围。
- 已核实范围：只能写已经读到的源码事实。
- 核验日期：默认继承 [fact-snapshot.md](fact-snapshot.md)；如果单条证据来自不同日期，必须在已核实范围中说明。
- 未解决问题：说明哪些语义仍不能下结论。

章节状态的升级门槛：

- `已核实官方事实` 章节至少要有一条 `mechanism-verified` 或 `behavior-verified` 证据。只登记路径存在不能升级。
- `待核实` 章节必须至少有一条 `pending` 证据，说明还缺哪段源码链路或语义判断。
- `教学抽象` 章节必须有 `teaching-abstract` 证据，并明确不是官方架构图。

不要在每章新建独立 `sources.md`。统一索引让检查脚本能一次性验证章节状态、证据级别和固定 SHA。

`fact-snapshot.md` 记录目标版本、章节主路径和易过期点；`source-evidence.md` 是行级证据登记表。因此某些行级 permalink 只出现在 `source-evidence.md` 是允许的，但章节 README 中出现的主引用必须能在快照或证据索引中追到。

## 写作标签

- `已核实官方事实`：本章的官方锚点已经进入当前事实快照，且章节主映射已经对照官方源码或官方文档核实。它不表示每个字段、函数名、错误分支、默认入口或产品解释都已逐行核实；未下钻的细节必须继续放在本章“事实核验清单”中。
- `待核实`：路径可能已核实存在，但章节主映射、行为边界或能力语义仍需继续读源码确认。路径存在不等于行为已核实。
- `教学抽象`：为了帮助理解而设计的简化模型，不声称是官方架构。
- `推断`：基于公开事实的解释性判断，必须说明推断链路；它不是章节级状态，只能用于句子或段落。

边界判据要可复用：如果一个章节的主线问题依赖尚未闭环的端到端数据流或产品语义，应保持 `待核实`；如果已经能逐条核实源码机制，但默认暴露条件或产品入口仍未知，可以标为 `已核实官方事实`，同时在章首明确“已核实”只限源码机制，不代表默认产品能力。

## 禁止项

- 禁止把 Python mock 写成 Codex 官方实现。
- 禁止把社区讨论、博客理解或课程比喻写成官方事实。
- 禁止把 Claude Code、其他 agent 平台或内部工具的概念直接套到 Codex 上。
- 禁止引用泄漏材料、私有 prompt 或无法公开核验的内容。

## 更新流程

1. 更新 [fact-snapshot.md](fact-snapshot.md) 的目标 commit、release 和核验日期。
2. 批量检查章节中的 GitHub 链接是否使用新的固定 SHA。
3. 更新 [source-evidence.md](source-evidence.md)，把新增或变化的机制证据登记到对应章节。
4. 对状态为 `待核实` 的章节重新读源码，再决定是否升级为 `已核实官方事实`。
5. 运行 `python3 scripts/check_docs.py` 和 `python3 -m unittest discover -s tests`。
