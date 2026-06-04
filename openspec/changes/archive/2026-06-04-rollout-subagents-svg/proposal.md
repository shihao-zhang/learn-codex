## Why

s11 已经把 subagents、delegate、agent jobs 与 tool parallel runtime 的源码机制核实到固定 SHA，并在章节开头明确这些只是机制级事实，不等于默认启用、产品入口或 multi-agent v1/v2 体验已经闭环。读者需要一张辅助图，把“父任务如何 delegate、父子事件如何回传、审批如何转发、并行 job 如何汇总结果”放在同一张图里看清楚，同时继续避免把 s11 画成通用官方子代理平台。

本 change 推进 SVG rollout B 的 s11 单章切片：为 `s11_subagents_parallel_jobs` 新增 1 张可选教学 SVG 和 companion Markdown。Mermaid 仍是主机制图，SVG 只作为教学辅助入口。

## What Changes

- 新增 s11 可选 SVG：展示 delegate、父子事件、审批转发、并行 job / result merge 的关系。
- 新增 s11 companion Markdown：记录 `Source Inputs`、`Event / Mechanism Mapping`、`Fact Boundary` 和 `Manual QA`。
- SVG 使用手写、可 diff、无外部依赖的 SVG，并包含 `<title>`、`<desc>`、可见图例和边界说明。
- s11 README 只增加短的可选 SVG 入口，继续保留 `diagram.mmd` 作为主机制图。
- 图中可把已登记源码机制标为 `FACT`，但必须显式写清：默认启用、产品入口、multi-agent v1/v2 体验仍需核实。

## Non-Goals

- 不替换或修改 s11 的 `diagram.mmd`。
- 不把 s11 画成通用官方子代理平台。
- 不声称 agent jobs 是通用批处理 API。
- 不声称 tool parallel runtime 等同于子 agent 并行。
- 不核实或新增默认启用条件、用户可见产品入口、multi-agent v1/v2 体验差异或完整权限继承策略。
- 不修改仓库 README、roadmap 或 `docs/diagram-style-guide.md`。
- 不修改 `docs/fact-snapshot.md`、`docs/source-evidence.md` 或 `scripts/check_docs.py`。
- 不改变任何章节状态。
- 不使用图片生成模型、外部图片、字体文件、网络服务或导出流水线作为最终图来源。

## Capabilities

### Modified Capabilities

- `diagram-redraw-style-guide`: 按会话与扩展批次中的 s11 单章 rollout，为 subagents / parallel jobs 增加可选 SVG 教学辅助图，并保持 Mermaid/SVG 分工和 s11 事实边界。

## Impact

- 新增图形资产：
  - `chapters/s11_subagents_parallel_jobs/diagrams/subagents-parallel-jobs.svg`
- 新增 companion Markdown：
  - `chapters/s11_subagents_parallel_jobs/diagrams/subagents-parallel-jobs.md`
- 更新 s11 README 的可选 SVG 导航入口。
- OpenSpec 与仓库验证要求：
  - `openspec validate rollout-subagents-svg --strict`
  - `openspec validate --all --strict`
  - XML parse 检查新增 SVG
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
