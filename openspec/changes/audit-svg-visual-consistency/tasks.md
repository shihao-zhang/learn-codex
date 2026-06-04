## 1. OpenSpec 准备

- [x] 1.1 创建 `audit-svg-visual-consistency` OpenSpec change。
- [x] 1.2 记录范围、非目标、审计方法、修复策略和验收要求。
- [x] 1.3 为全仓 SVG 视觉一致性 QA 增加 spec delta。

## 2. 清单与渲染

- [x] 2.1 盘点全部 `chapters/*/diagrams/*.svg` 文件。
- [x] 2.2 XML parse 全部章节 SVG。
- [x] 2.3 渲染或预览全部章节 SVG。

## 3. 逐章视觉 QA

- [x] 3.1 QA s01 `turn-loop.svg`。
- [x] 3.2 QA s02 `event-interface.svg`。
- [x] 3.3 QA s03 `tool-dispatch.svg`。
- [x] 3.4 QA s04 `permission-boundary.svg`。
- [x] 3.5 QA s05 `context-pressure.svg`。
- [x] 3.6 QA s06 `instruction-conflict.svg`。
- [x] 3.7 QA s07 `model-choice-impact.svg`。
- [x] 3.8 QA s08 `session-thread-rollout.svg`，保持 `待核实` 显式。
- [x] 3.9 QA s09 `state-sync-boundary.svg`。
- [x] 3.10 QA s10 `extension-capability-lines.svg`，保持 `待核实` 显式。
- [x] 3.11 QA s11 `subagents-parallel-jobs.svg`。
- [x] 3.12 QA s12 `pilot-trace.svg`，保持 `教学抽象` 显式。

## 4. 修复与记录

- [x] 4.1 修复 QA 中发现的小型 SVG 视觉或语义标记一致性问题。
- [x] 4.2 更新受影响 companion Markdown 的 `Manual QA` 记录。
- [x] 4.3 确认没有新增官方事实、没有修改证据文件、检查脚本或章节状态。

## 5. 验收

- [x] 5.1 运行 `openspec validate audit-svg-visual-consistency --strict`。
- [x] 5.2 运行 `openspec validate --all --strict`。
- [x] 5.3 对全部章节 SVG 运行 XML parse 检查。
- [x] 5.4 运行 `python3 scripts/check_docs.py`。
- [x] 5.5 运行 `python3 scripts/run_all.py`。
- [x] 5.6 运行 `python3 -m unittest discover -s tests`。
- [x] 5.7 运行 `git diff --check`。
- [x] 5.8 本地 commit，不 push。
