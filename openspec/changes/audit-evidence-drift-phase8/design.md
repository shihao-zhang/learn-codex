## Context

当前 fact snapshot 的目标 commit 是 `740d942f901a5a63421298c74dafbeb4255e946d`。本 change 不更新该 commit，也不重新追踪最新 release。Phase 8 的重点是审计“现有文档是否仍然忠于这个快照”，而不是扩大事实范围。

已有边界：

- s08 和 s10 在 Phase 5 后仍保持 `待核实`。
- s01~s06 在 Phase 6 新增了 PM 问题、failure path 和 mock trace 解读，但这些新增内容必须保持教学解释或产品判断口径。
- Phase 7 只启动 integrated teaching mock 设计，不在本轮实现。

## Goals / Non-Goals

**Goals:**

- 抽样检查固定 SHA 链接是否统一指向当前 fact snapshot 目标 commit。
- 检查 README、docs、s01~s12 是否存在过强官方事实表述。
- 检查 s08/s10 的待核实边界在 roadmap、Phase 5 summary 和章节 README 中是否一致。
- 检查 s01~s06 的 PM/failure/mock trace 内容是否清楚标为教学解释或产品判断。
- 检查 `docs/source-evidence.md` 的证据级别是否支撑 README 的章节状态。
- 检查 `docs/review-checklist.md` 是否覆盖后续维护者最容易犯错的情况。

**Non-Goals:**

- 不更新目标 commit。
- 不追最新 release。
- 不大改章节正文。
- 不启动或实现 integrated teaching mock。
- 不升级 s08/s10 状态。
- 不把 Codex 桌面端体验、Claude review、教学 mock 或其他 agent 产品经验写成官方事实。

## Audit Method

1. 固定 SHA 抽样：

   - 搜索 OpenAI 源码 permalink。
   - 确认 `blob` / `tree` 链接使用 `740d942f901a5a63421298c74dafbeb4255e946d`。
   - 搜索 moving ref，如 `main`、`master`、`latest` 或 release tag 链接误用。

2. 状态一致性抽样：

   - 对照 README 学习地图、章节 README 状态、`docs/source-evidence.md` 整体行。
   - s08/s10 必须继续显示 `待核实`。
   - s12 必须继续显示 `教学抽象`。

3. 事实边界抽样：

   - 查找 `已核实官方事实`、`待核实`、`教学抽象`、`推断`、`Codex 桌面端`、`Claude`、`mock` 等高风险词。
   - 对过强表述做最小收窄。

4. 审计摘要：

   - 用 `docs/phase8-evidence-audit.md` 记录发现。
   - 明确列出无需修改、已收窄、仍待核实、建议后续另开 change 的项。

## Risks / Trade-offs

- [Risk] 抽样审计被误解为完整重验源码。
  - Mitigation: 审计摘要明确“抽样复核，不更新 fact snapshot，不追 release”。
- [Risk] 为了追求一致性而大改章节正文。
  - Mitigation: 只修事实边界相关措辞，正文结构保持稳定。
- [Risk] 把证据级别当成章节状态自动升级依据。
  - Mitigation: 在审计摘要和必要的维护文档中重申证据级别不会自动升级章节状态。
- [Risk] Phase 7 integrated mock 被提前实现。
  - Mitigation: 本 change 不修改 mock 代码、runner 或测试。
