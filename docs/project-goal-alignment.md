# Project Goal Alignment

本仓的目标是帮助人类 AI 产品经理和 agent 平台设计者建立 agent harness literacy：看懂一个 agent runtime 如何通过 loop、tools、permissions、context、sessions、transport 和 extensions 组合成可控的产品体验。

本仓使用公开 `openai/codex` Rust CLI harness 作为样本，但不是 OpenAI 官方项目，也不复刻官方实现。

## Target Readers

| 读者 | 需要获得的判断力 |
| --- | --- |
| AI 产品经理 | 能把“agent 为什么可信、为什么慢、为什么贵、为什么要问权限、失败后能不能恢复”拆成 runtime 机制问题。 |
| Agent 平台设计者 | 能看见 loop、工具系统、权限、安全边界、上下文、会话、transport 和扩展面之间的架构接口。 |
| 内容贡献者 | 能区分官方事实、教学抽象、桌面端观察和推断，不把灵感误写成事实。 |

## Non Goals

- 不是 OpenAI 官方文档或官方课程。
- 不是 Codex 使用手册。
- 不是链接索引或资料导航站。
- 不是 OpenAI Codex 的 Python 复刻、桌面端复刻或等价实现。
- 不用教学 mock 证明任何官方行为。

## Harness Literacy In Product Terms

| 机制 | 产品经理应该问什么 | 平台设计者应该看什么 |
| --- | --- | --- |
| loop | agent 是如何从“回答”变成“持续执行任务”的？ | turn、tool observation、事件回写和停止条件。 |
| tools | 哪些能力暴露给模型，错误如何回到模型或用户？ | tool registry、dispatch、handler、parallel safety。 |
| permissions | 什么时候必须让人批准，什么时候应该自动拒绝？ | sandbox policy、approval requirement、网络/文件系统边界。 |
| context | 成本、延迟和记忆质量如何被上下文窗口影响？ | compaction、history replacement、trace 与摘要边界。 |
| sessions | 中断、恢复、追责和长任务交接靠什么支撑？ | session/thread id、rollout、thread-store、resume/fork。 |
| transport | UI、CLI 或 app-server 如何同步运行状态？ | protocol event、outgoing message、thread status。 |
| extensions | 新能力如何进入 agent，又如何避免能力边界失控？ | MCP、extension tools、skills instructions 与配置入口。 |

注意：`sessions` 和 `extensions` 对应的 s08、s10 章节当前仍是 `待核实`，具体机制必须回到 README 学习地图和证据索引查看状态。

这些问题最终都落到产品指标上：trust、cost、latency、recoverability、user control 和 permission friction。

## Fact Boundary Recap

- 官方事实：只能来自固定 commit SHA 的 OpenAI 源码 permalink、OpenAI 官方文档或 release note。
- 教学 mock：只用于解释机制，不代表 OpenAI Codex 实现，也不证明等价行为。
- Mermaid 图和综合架构：是教学表达；除非逐项绑定证据，否则不能当官方架构图。
- Codex Desktop Lens：只能作为观察视角、产品设计启发或源码阅读问题，不能作为官方事实来源。
- 推断：必须显式标注推断链路；如果链路不稳，改成 `待核实` 或删掉。

## Reader Path

如果你想先理解项目方向，再读章节：

1. 先读本文，确认本仓要建立的判断力和非目标。
2. 再读 [roadmap.md](roadmap.md)，了解 Phase 5~9 为什么先处理事实边界，再扩写内容。
3. 如果你使用 Codex 桌面端做观察，先读 [codex-desktop-lens.md](codex-desktop-lens.md)，把观察转成源码问题。
4. 最后进入 README 的学习地图逐章阅读。
