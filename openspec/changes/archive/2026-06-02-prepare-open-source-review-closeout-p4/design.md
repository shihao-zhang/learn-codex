## Context

当前分支 `codex/phase5-9-roadmap-closure` 已从 roadmap 设计推进到 P3 深核验。工作重点已经从“继续加内容”转为“让 reviewer 能判断这批内容能否进入主线”。

P4 不应再引入新的机制事实。它只做维护收口：

- 汇总当前已完成内容。
- 标注 s08/s10、fact snapshot、diagram pilot 和 teaching mock 的边界。
- 说明 active OpenSpec changes 如何处理。
- 给出 PR/review summary 草案。
- 明确后续风险分流。

## Goals / Non-Goals

**Goals:**

- 建立一页面向 reviewer 的维护收口文档。
- 将 P0-P4 的完成状态和后续风险写进 roadmap。
- 在 review checklist 中加入 PR / release closeout 操作项。
- 保持 OpenSpec changes 处于可 review 状态，不提前归档。
- 运行全仓文档、mock、单测和 diff 检查。

**Non-Goals:**

- 不新增或更新 OpenAI 官方机制事实。
- 不迁移 fact snapshot target commit。
- 不修改 `scripts/check_docs.py`。
- 不升级 s08/s10。
- 不重绘更多图，不扩写 Phase 7 mock。
- 不执行 push、PR 创建、OpenSpec archive 或外部 review。

## Decisions

1. 新增 `docs/maintenance-closeout.md`，而不是把 PR summary 塞进 README。

   README 继续做读者入口；closeout 文档服务 reviewer 和维护者。

2. Active OpenSpec changes 暂不归档。

   这些 changes 是本轮 review 的主要证据。归档会改变仓库结构，适合在 review 通过后另开归档/merge hygiene change 或按人类明确指令执行。

3. PR summary 只写本仓事实，不写成 OpenAI 官方实现说明。

   Summary 只能说“本教学仓新增了什么、如何处理事实边界、哪些检查通过”，不能说 OpenAI Codex 官方能力发生变化。

4. 后续任务按风险分流。

   - fact snapshot 迁移：独立 implementation change。
   - s08/s10 状态升级：独立 focused verification。
   - diagram style guide 推广：先抽象文档，再试点，不全仓重绘。
   - OpenSpec 归档：review 后再做。

## Risks / Trade-offs

- [Risk] 收口文档变成冗长复盘。
  Mitigation: 只保留 review 所需的 scope、status、checks、risks 和 next steps。

- [Risk] active changes 太多影响 reviewer。
  Mitigation: 按 phase 分组列出，说明全部 artifact complete，并建议 review 后再归档。

- [Risk] P4 被误认为 release 发布。
  Mitigation: 文档明确 P4 只准备 review，不推送、不发布、不归档。

## Validation

完成后运行：

- `openspec validate prepare-open-source-review-closeout-p4 --strict`
- `python3 scripts/check_docs.py`
- `python3 scripts/run_all.py`
- `python3 -m unittest discover -s tests`
- `git diff --check`
