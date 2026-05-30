## Why

Phase 3~4 已经把 `learn-codex` 从路径级骨架推进到机制级证据索引，但项目还需要一份清晰的后续路线，避免后续写作在内容密度、事实边界和教学体验之间失衡。

同时，Codex 桌面端的真实使用体验可以帮助提出更好的源码阅读问题，但必须被严格限制为“观察视角”，不能被写成 `openai/codex` 开源实现事实。

## What Changes

- 新增后续阶段路线：优先打穿 s08/s10，提升前 6 章内容密度，设计端到端 integrated teaching mock，完善维护与 review 流程。
- 新增 Codex Desktop Lens 视角：把桌面端使用体验转化为源码问题、产品设计启发和 mock 场景，不作为官方事实来源。
- 明确项目目标对齐口径：本仓面向 AI 产品经理和 agent 平台设计者，核心是理解 agent harness，而不是使用教程、资料索引或官方实现复刻。
- 建立下一阶段验收口径：每个阶段都要有事实边界、产出物、检查项和继续保守标注的条件。
- 保持现有章节结构和 Python mock 约束，不引入 OpenAI API 调用，不改变非官方声明。

## Capabilities

### New Capabilities

- `next-phase-roadmap`: 定义 Phase 5 以后如何排序、验收和收敛后续工作。
- `codex-desktop-lens`: 定义如何使用 Codex 桌面端观察来生成源码阅读问题和教学场景，同时防止其污染官方事实边界。
- `project-goal-alignment`: 定义面向人类产品经理的项目目标、非目标、读者收益和沟通口径。

### Modified Capabilities

- 无。

## Impact

- 影响后续文档规划：`README.md`、`docs/` 下的 roadmap/lens/goal 文档，以及部分章节 README 的问题入口。
- 影响后续 mock 设计：未来可能新增跨章节 integrated mock，但本 change 只规划，不实现。
- 影响 review 流程：后续阶段需要继续区分官方源码事实、桌面端观察、教学抽象和推断。
- 不影响当前公开事实快照、不改变章节状态、不引入新依赖。
