# AGENTS.md

## Project Scope

- 本仓研究对象限定为 `openai/codex` 公开开源仓库中的 Rust CLI harness，重点是 `codex-rs`。
- 本仓面向 AI 产品经理和 agent 平台设计者，目标是讲清 agent harness 的机制，而不是做资料索引、产品宣传或官方实现复刻。
- Python mock 只用于教学，不得写成 Codex 官方实现或等价复刻。
- 桌面端 Codex 使用体验可以作为“问题生成视角”和“产品设计启发”，但不得作为 `openai/codex` 官方实现事实。

## Fact Boundary

- 官方事实只能来自固定 commit SHA 的 OpenAI 源码 permalink、OpenAI 官方文档或 release note。
- 社区文章、Claude review、桌面端观察、教学 mock 只能作为理解材料、审稿材料或教学启发，不能作为官方事实来源。
- 如果一个机制只有路径存在证据，不能升级为 `已核实官方事实`；必须标注为 `待核实` 或缩窄表述。
- 不要把其他 agent 产品、Claude Code、Codex 桌面端体验或个人推断直接套到 `openai/codex` 开源实现上。

## Codex Desktop Lens

- 当阅读本 `AGENTS.md` 的 agent 是 Codex 桌面端时，应主动使用自身桌面端执行体验来生成更好的源码阅读问题。
- 推荐链路是：`桌面端观察 -> 源码问题 -> 固定 SHA 证据 -> 教学表达`。
- 禁止链路是：`桌面端观察 -> 直接断言 openai/codex 官方实现`。
- Codex 桌面端应主动把自身经历到的工具调用、权限审批、沙箱限制、上下文压缩、session 恢复、GitHub 凭据、外部 review 卡住等体验，转化为章节中的阅读问题、failure path 和产品设计启发。
- 所有由桌面端体验引出的内容，必须回到公开源码或官方文档核验；无法核验时标注为 `待核实`、`教学抽象` 或 `推断`。

## Evidence Workflow

- 机制级证据统一登记到 `docs/source-evidence.md`，不要为每章新增独立 `sources.md`。
- 修改章节状态、事实边界、证据规则或验收口径时，必须同步更新相关文档；涉及长期规则变化时，应使用 OpenSpec 记录 proposal、design、tasks 或 specs。
- 章节 README 中出现的主引用必须能在 `docs/fact-snapshot.md` 或 `docs/source-evidence.md` 中追到。
- 提交前至少运行：
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
