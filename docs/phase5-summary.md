# Phase 5 Verification Summary

Phase 5 第一轮事实核验已经完成：s08 和 s10 都补强了固定 SHA 证据，也都继续保持 `待核实`。这不是失败，而是本仓的质量边界：证据增加不等于产品语义已经全部闭环。

本页只做阶段收口，不新增 `openai/codex` 官方事实。具体证据仍以 [source-evidence.md](source-evidence.md)、[s08](../chapters/s08_sessions_threads_rollout/README.md) 和 [s10](../chapters/s10_extensions_mcp_skills/README.md) 为准。

## Summary

| 章节 | 第一轮已核实范围 | 仍未闭环 | 状态判断 |
| --- | --- | --- | --- |
| s08 sessions/threads/rollout | `SessionId` / `ThreadId`、`InitialHistory::Resumed/Forked`、thread-store 边界、app-server cold resume/running rejoin/fork、rollout replay、`codex exec resume` 通过 app-server 恢复。 | TUI、daemon、debug-client、remote store、experimental app-server API 和所有用户可见恢复体验仍未逐一闭环。 | 继续 `待核实`。可以讲局部机制，不能承诺稳定恢复产品语义。 |
| s10 extensions/MCP/skills | MCP CLI 入口与 tool exposure、MCP handler、dynamic tools、extension adapter、skills discovery/config、TUI `/skills`/`$` 入口、配置层启停路径、available skills instructions、显式 skill mention 注入。 | extension tools 的安装/发现/用户入口仍未闭环；MCP、dynamic tools、extension tools、skills 是否属于同一治理路径仍需核实。 | 继续 `待核实`。skills TUI 可见入口和配置路径已有证据，但不能抹平不同扩展来源。 |

## What Changed

- s08 从“路径和局部机制存在”推进到“app-server resume/fork 主链路和 `exec resume` 路径更清楚”。
- s10 从“skills 是否用户可见仍高度模糊”推进到“skills TUI 可见入口和配置路径已有固定 SHA 证据，但 extension tools 和统一治理仍待核实”。
- 两章都没有升级状态，避免把局部源码证据写成完整产品承诺。

## Product Meaning

对 AI 产品经理来说，Phase 5 的价值不是“把待核实改成已核实”，而是把风险看清楚：

- s08 告诉我们：恢复体验不能只看有没有 id 和 history，还要看客户端、存储、重放、分页、redaction 和实验接口边界。
- s10 告诉我们：扩展能力不能只看有没有 MCP、skills 或 extension 字样，还要拆开入口、发现、暴露、治理和执行责任。

这会直接影响后续章节的写法：可以讲清产品问题和局部机制，但不能把未闭环体验写成稳定官方能力。

## Later Phases

Phase 5 之后的 Phase 6~9 已完成本轮推进：前 6 章内容加厚、integrated teaching mock 设计、证据抽样复核和维护 review checklist 都已落地。Phase 5 的结论仍然有效：s08/s10 只提升证据密度，不升级章节状态。

后续继续引用 s08/s10 时，只能作为 `待核实` 边界、源码阅读问题或产品风险提示，不能当作稳定官方产品承诺。

如果后续要继续推进，可以从以下方向单独开 change：

- Phase 7 implementation：实现 integrated teaching mock，但继续保持 deterministic、offline、Python 标准库和非官方教学抽象。
- Fact snapshot update：更新目标 commit 或追新 release，并同步固定 SHA 链接和检查脚本。
- s08/s10 deep verification：继续端到端核验 session/thread/rollout 或 extensions/MCP/skills 的用户可见边界。
