# Phase 8 Evidence Audit

本页记录 `audit-evidence-drift-phase8` 的轻量抽样复核。它不是一次完整源码重验，也不更新 fact snapshot 的目标 commit 或 release 核验值。

## 审计范围

- 固定 SHA：抽样检查 README、docs、chapters、openspec 中的 OpenAI 源码 permalink。
- 章节状态：对照 README 学习地图、章节 README、`docs/source-evidence.md`。
- 高风险章节：重点复核 s08 sessions/threads/rollout 与 s10 extensions/MCP/skills。
- Phase 6 新增内容：抽样复核 s01~s06 的 PM 问题、failure path 和 mock trace 是否保持教学/产品判断口径。
- 维护规则：复核 `docs/review-checklist.md` 是否覆盖后续维护者常见误区。

本轮明确不做：

- 不更新目标 commit `740d942f901a5a63421298c74dafbeb4255e946d`。
- 不追最新 release。
- 不启动或实现 integrated teaching mock。
- 不升级 s08/s10 状态。
- 不调用 Claude 或其他外部 review 服务。

## 无需修改

- 固定 SHA 链接抽样结果：190 个 `github.com/openai/codex/blob|tree/<sha>` 链接均指向当前目标 commit。
- 未发现 `openai/codex` 源码链接使用 `main`、`master` 或 `latest` moving ref。
- README 学习地图仍保持 s08、s10 为 `待核实`，s12 为 `教学抽象`。
- s08 在 roadmap、Phase 5 summary、章节 README 和 source evidence 中一致保留 `待核实`；原因仍是 TUI、daemon、remote store、experimental API 和用户可见恢复体验未闭环。
- s01~s06 的新增 PM 问题、failure path 和 mock trace 基本都已用“教学抽象”“产品判断”“不声明官方行为”等口径隔离，没有发现需要大改正文的漂移。
- `docs/source-evidence.md` 对 README 章节状态仍有支撑：已核实章节有 `mechanism-verified` 或 `behavior-verified`，待核实章节有 `pending`，s12 有 `teaching-abstract`。

## 已收窄

- s10：把 `skills CLI/TUI 可见性` 收窄为“目标 commit 下 TUI 可见入口和配置路径已有固定 SHA 证据”；不再暗示所有客户端或完整 CLI 一等能力都已闭环。
- s10：移除 source evidence 中未单独登记链接的“OpenAI 官方文档也明确 skills 可用于 CLI/IDE/App”表述，避免把未固定在本索引里的外部文档当作证据。
- glossary：更新 `skills` 和 `subagents` 的术语边界，避免继续使用 Phase 1 骨架阶段的旧待核实口径。
- roadmap：把 Phase 7 验收从“mock 必须测试覆盖”收窄为“设计必须声明未来 mock 约束，本阶段不要求实现代码或测试”。
- roadmap/README：标注 Phase 8 本轮只做抽样复核，不更新目标 commit、不追 release、不实现 integrated mock。
- review checklist：新增“高频误区”，覆盖 moving ref、状态自动升级、Phase 6 教学内容、Phase 7 mock 设计与实现边界、skills/extensions/MCP/subagents 混写等风险。

## 仍待核实

- s08：TUI、daemon、debug-client、remote store、experimental app-server API 稳定性边界，以及所有用户可见恢复体验。
- s10：extension tools 的用户安装/发现入口、dynamic tools 的 CLI/app-server client 边界，以及 MCP、dynamic tools、extension tools、skills 是否能被概括为同一治理路径。
- s11：默认启用条件、产品入口和 multi-agent v1/v2 体验差异仍是局部待核实点；当前章节状态只覆盖已登记源码机制，不代表官方产品承诺。
- release、model/provider 默认值、权限策略和 app-server 协议仍是易过期点；本轮没有追新。

## 建议后续另开 Change

- 如果要更新目标 commit 或最新 release 核验值，单独开 fact snapshot update change，并同步 `scripts/check_docs.py` 的固定 commit 常量。
- 如果要推进 s08 状态，单独开 resume/thread-store/remote-store 端到端核验 change。
- 如果要推进 s10 状态，单独开 extension tools 用户入口与统一扩展治理核验 change。
- 如果要实现 Phase 7 integrated teaching mock，单独开 implementation change；继续保持 deterministic、offline、Python 标准库和非官方教学抽象。
