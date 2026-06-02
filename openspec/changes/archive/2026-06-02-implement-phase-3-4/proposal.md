## Why

`learn-codex` Step 2 已经形成可公开 review 的 12 章教学初版，但事实依据仍以路径级核验为主，距离“高密度源码导读”还有差距。Phase 3~4 的目标是在不突破公开事实边界的前提下，把关键章节推进到机制点级核验，并优先打穿 s08~s11 这些最容易误读的待核实区域。

## What Changes

- 为章节新增源码证据能力：每个关键机制点都要能追到固定 SHA permalink、核验状态、核验日期和未决问题。
- 优先升级 s01~s07 的事实颗粒度，从“目录/文件存在”推进到“机制点与源码位置对应”。
- 集中核验 s08~s11：session/thread/rollout、app-server transport、MCP/extensions/skills、subagents/parallel jobs。
- 强化文档检查：防止无证据的机制断言、待核实章节被误升为已核实、以及新增源码链接未登记。
- 保持教学 mock 的边界：mock 继续只证明教学模型自洽，不证明与官方 Codex 等价。

## Capabilities

### New Capabilities
- `source-evidence-traceability`: 为章节机制点建立源码证据登记、状态升级规则和检查约束。
- `pending-chapter-verification`: 为 s08~s11 的待核实章节建立逐章核验、降级/升级、未决问题收敛流程。

### Modified Capabilities
- 无。

## Impact

- 影响 `README.md`、`docs/sourcing.md`、`docs/fact-snapshot.md`、`docs/glossary.md` 和各章节 README。
- 新增统一证据索引文件，章节 README 只链接到统一索引。
- 影响 `scripts/check_docs.py`、测试用例和 CI 检查策略。
- 不引入 OpenAI API 调用，不改变 Python mock 的“标准库、离线、教学用途”约束。
