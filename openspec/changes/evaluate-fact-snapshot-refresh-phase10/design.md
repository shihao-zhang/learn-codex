## Context

本仓的事实边界依赖一个全局目标快照：

- `docs/fact-snapshot.md` 记录核验日期、目标 commit、release 核验值和主路径。
- `scripts/check_docs.py` 用 `SOURCE_COMMIT` 防止 OpenAI 源码链接漂移。
- 章节 README 和 `docs/source-evidence.md` 只能引用固定 SHA permalink，不能使用 `main`、`master`、release tag 或其他 moving ref 作为源码证据。

因此，刷新目标 commit 不是单点改值，而是一次全仓证据迁移。迁移必须先确认官方来源，再同步链接和校验脚本。

## Decision Rules

1. 官方来源规则
   - 默认分支 commit 只能来自 `openai/codex` 官方 GitHub 仓库。
   - release 核验值只能来自 `openai/codex` 官方 GitHub Releases。
   - 源码路径可访问性只能用固定 SHA permalink 或 GitHub Contents API 核验。
   - 不使用社区文章、Claude review、桌面端观察、教学 mock 或 diagram redraw 作为官方事实。

2. 是否刷新目标 commit
   - 如果官方默认分支 HEAD 已不同于当前目标 commit，且快照中的路径在新 commit 下仍可核验，则可以刷新目标 commit。
   - 如果关键路径缺失、链接迁移无法闭环、或新 commit 会要求重新解释未核验机制，则保持旧目标 commit，并把追新作为后续 change。
   - release 核验值可以独立刷新，但必须来自官方 release 页面或 API。

3. 同步要求
   - 更新目标 commit 时，必须同步更新 `docs/fact-snapshot.md`、`scripts/check_docs.py` 和仓库内所有固定 SHA OpenAI 源码链接。
   - 更新后必须扫描 `github.com/openai/codex/(blob|tree)/...` 链接，确认没有旧 SHA、`main`、`master` 或 release tag 作为源码证据。
   - 所有迁移后的快照表路径仍只证明“路径存在”，不能自动提高章节证据级别。

4. s08 / s10 保守状态
   - s08 sessions/threads/rollout 和 s10 extensions/MCP/skills 不因新 commit 可访问而自动升级。
   - 若要升级，必须另开或明确扩展 change，逐条核验机制链、产品入口、配置触发、运行时暴露和未决问题。

## Risks

- Risk: 追新 commit 后链接全部可打开，但章节文字仍基于旧机制理解。
  Mitigation: 本 change 只迁移快照与路径存在证据；机制解释仍以 `docs/source-evidence.md` 的证据级别为准。

- Risk: release 值更新后被误读为安装方式或功能边界已全部核实。
  Mitigation: `docs/fact-snapshot.md` 只记录 release 核验值；易过期功能仍需单独核验。

- Risk: 一次性替换 SHA 后漏掉某个文件。
  Mitigation: 使用 `scripts/check_docs.py` 的链接 ref 检查，再运行 `rg` 辅助确认旧 SHA 不残留。

## Validation

完成后运行：

- `openspec validate evaluate-fact-snapshot-refresh-phase10 --strict`
- `python3 scripts/check_docs.py`
- `python3 scripts/run_all.py`
- `python3 -m unittest discover -s tests`
- `git diff --check`

## Evaluation Result

核验日期：2026-06-01。

官方来源核验结果：

- `openai/codex` 默认分支是 `main`。
- `main` 当前 HEAD 是 [`f27bbbd49c0e05e763a96cc7fa677499de32b8d8`](https://github.com/openai/codex/commit/f27bbbd49c0e05e763a96cc7fa677499de32b8d8)，commit 时间为 2026-06-01T09:32:13Z。
- 最新 GitHub release 仍是 [`rust-v0.135.0`](https://github.com/openai/codex/releases/tag/rust-v0.135.0)，发布名 `0.135.0`，发布时间为 2026-05-28T17:31:35Z。
- GitHub Releases 页面同时存在更新的 prerelease，例如 `0.136.0-alpha.2`；本仓本轮只按 GitHub `Latest` 标记的稳定 release 判断 `docs/fact-snapshot.md` 的 release 核验值，不把 prerelease 自动写入快照。
- 候选 commit 的 recursive Git tree 未截断，共 5432 个 path。
- 当前仓内 191 个固定 SHA OpenAI 源码链接对应 81 个唯一路径；这些路径在候选 commit 下全部存在，且 `blob` / `tree` 类型匹配。

本轮决策：

- 暂不更新 `docs/fact-snapshot.md` 的目标 commit。
- 暂不更新 `scripts/check_docs.py` 的 `SOURCE_COMMIT`。
- 暂不批量替换现有 OpenAI 源码 permalink。
- 暂不更新 `docs/fact-snapshot.md` 的 release 核验值，因为最新 release 与现有记录一致。

原因：

- 候选 commit 只能证明路径仍存在，不能证明 `docs/source-evidence.md` 中 191 个行号锚点和机制解释仍逐条成立。
- `docs/source-evidence.md` 当前声明多数证据继承 2026-05-29 的目标快照；直接改快照日期或 commit 会把未逐机制复核的旧证据误标为新快照证据。
- s08 和 s10 的待核实状态不应因路径可访问而自动升级。

后续如果要真正迁移到 `f27bbbd49c0e05e763a96cc7fa677499de32b8d8`，应另开实施型 change，至少逐章复核 `docs/source-evidence.md` 的行号锚点、机制解释和未解决问题，再同步迁移 `docs/fact-snapshot.md`、`scripts/check_docs.py`、章节 README、测试 fixture 和所有 OpenAI 源码链接。
