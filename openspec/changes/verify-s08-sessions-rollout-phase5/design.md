## Context

s08 当前状态是 `待核实`。已有证据覆盖 `SessionId` / `ThreadId`、`ThreadStore` trait、`InitialHistory::Resumed/Forked` 等局部机制，但读者仍需要知道 app-server 请求、CLI resume、thread-store 与 rollout 在恢复链路中各自承担什么。

本轮事实只能来自固定 commit `740d942f901a5a63421298c74dafbeb4255e946d` 的 OpenAI 源码 permalink、OpenAI 官方文档或 release note。本轮已读取该固定 commit 的公开源码快照；不使用 Codex 桌面端体验、社区文章或 Claude review 作为官方事实来源。

## Goals / Non-Goals

**Goals:**

- 补齐 s08 的机制级证据登记，尤其是 `thread/resume`、`thread/fork`、`thread/turns/list`、thread-store local read/resume、rollout persistence policy。
- 明确哪些语义可以升级为局部官方事实，哪些仍要保持 `待核实`。
- 保持 README 面向产品经理的保守表达：讲清身份、历史、恢复边界，不承诺未核实体验。
- 运行 OpenSpec 与仓库既有检查命令。

**Non-Goals:**

- 不升级 s08，除非证据足够闭合。
- 不研究或修改 s10。
- 不把 app-server 实验字段写成稳定公开产品能力。
- 不把桌面端观察写成 `openai/codex` 官方实现事实。

## Decisions

1. 证据更新优先于正文扩写。

   - 先在 `docs/source-evidence.md` 登记行级 permalink 和证据级别。
   - README 只做必要收窄，避免把证据表内容搬成低可读性源码索引。
   - 备选方案是直接重写章节；风险是把仍不稳定的 app-server 字段写成产品承诺。

2. s08 默认保持 `待核实`。

   - 即使 app-server 主链路进一步清楚，只要 CLI/TUI/daemon/remote store 或不稳定字段边界没有完全闭合，就不强行升级。
   - 合格结果可以是“缺口更清楚”，而不是“状态升级”。

3. 区分三类恢复链路。

   - CLI `exec resume`：从源码看通过 in-process app-server 的 `thread/list` + `thread/resume`。
   - app-server cold resume/fork：从 store/rollout 读取历史并交给 core `InitialHistory`。
   - running thread rejoin：已有运行中 thread 时通过 listener 命令发送恢复响应并订阅后续更新。

## Risks / Trade-offs

- [Risk] 误把 experimental app-server 字段当稳定接口 -> 在证据 notes 和 README 中保留不稳定/待核实边界。
- [Risk] 行级证据过多降低章节可读性 -> 详细证据集中在 `source-evidence.md`，README 只保留结论与缺口。
- [Risk] 端到端链路看起来足够完整但仍有产品边界未知 -> 状态不升级，并写明缺口。
