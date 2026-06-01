# Maintenance Review Checklist

本页是 Phase 9 的维护与 review 规则。它面向后续贡献者：改章节、证据、快照、mock 或维护流程前，先用这份清单判断“要不要更新证据、要不要问人、要不要走 OpenSpec”。

## 适用范围

- 章节 README、Mermaid 图、Python mock、README 导航、roadmap、sourcing、fact snapshot、source evidence 和 OpenSpec 文档。
- 任何会改变 agent 决策规则、事实边界、章节状态、验收口径或长期协作规则的修改。
- 纯错别字、链接文字、轻量导航可以直接改；只要改变事实判断或维护规则，就先走 OpenSpec。

## 章节状态

### 升级为 `已核实官方事实`

只有同时满足以下条件，才能升级：

- 章节主张能追到固定 commit SHA 的 OpenAI 源码 permalink、OpenAI 官方文档或 release note。
- `docs/source-evidence.md` 至少有一条对应章节的 `mechanism-verified` 或 `behavior-verified` 证据。
- 章节 README 的主引用能在 `docs/fact-snapshot.md` 或 `docs/source-evidence.md` 追到。
- README 学习地图状态和章节 README 状态同步。
- 未解决问题不会影响章节主映射；如果只影响细节，必须写清“已核实范围”。

### 保持 `待核实`

出现以下任一情况，就保持 `待核实`：

- 只有路径存在证据，没有机制或行为证据。
- 端到端数据流、默认入口、用户可见语义或产品能力边界没有闭环。
- 源码注释或协议字段标为 experimental，不能当成稳定能力。
- 解释主要来自桌面端观察、社区文章、其他 agent 产品或教学推断。

保持 `待核实` 是合格结果。要把缺口写在 `docs/source-evidence.md` 的“未解决问题”或章节“事实核验清单”里。

### 降级或缩窄

当证据过期、表述过宽、固定快照变化、或旧结论不能继续支撑章节主张时，必须降级或缩窄措辞。降级时同步更新 README、章节 README、`docs/source-evidence.md`，并在 review summary 中说明原因。

`教学抽象` 只用于帮助读者理解的组合模型、图或 mock。它不是官方架构，也不能因为讲得顺就升级成官方事实。

## Source Evidence

更新 `docs/source-evidence.md` 的触发条件：

- 新增、删除或修改 `openai/codex` 官方机制事实。
- 新增章节主引用或重要固定 SHA 源码链接。
- 改变证据级别，例如从 `path-exists` 升到 `mechanism-verified`。
- 状态升级、降级或继续保守时，需要记录支撑理由。
- 发现旧证据不能支撑现有表述。

不需要更新 `docs/source-evidence.md` 的情况：

- 纯导航、错别字、排版或不改变事实边界的措辞。
- 只补充读者路径、维护清单或 OpenSpec 流程，且不新增官方机制事实。

每条证据必须写清：章节、机制点、证据级别、固定 SHA 源码链接、已核实范围、未解决问题。证据级别不会自动升级章节状态，状态变化必须单独 review。

## Fact Snapshot

`docs/fact-snapshot.md` 只记录当前目标版本和主路径边界。以下情况才更新：

- 目标 commit 改变。
- release 核验值、核验日期或官方主入口改变。
- 章节主路径清单发生变化。
- 易过期点列表需要调整。

如果只是在现有目标 commit 下补行级机制证据，更新 `docs/source-evidence.md`，不要改 fact snapshot。目标 commit 改变时，还要同步检查所有 OpenAI 源码链接，并更新 `scripts/check_docs.py` 中的固定 commit 常量。

## 高频误区

- 不要把 `main`、`master`、tag 或最新 release 链接当成固定事实依据；需要追新版本时先开新 OpenSpec change。
- 不要因为 `docs/source-evidence.md` 出现多条 `behavior-verified` 就自动升级章节状态；端到端产品语义或默认入口没闭环时，继续保持 `待核实`。
- 不要把 Phase 6 的 PM 问题、failure path 或 mock trace 改写成官方实现行为；它们默认是教学解释或产品判断。
- 不要把 Phase 7 integrated mock 的设计文档理解成已经允许实现；实现必须另开 change，并继续保持离线、确定性、非官方教学抽象。
- 不要把 skills、extensions、MCP、subagents 等名字相似的能力抹平成一个产品概念；每个入口、治理路径和默认暴露条件都要单独核实。

## Claude Review 授权

凡是把内部文档、代码、diff 或计划发送给 Claude 等外部服务 review，必须先暂停并向人类请求明确授权。请求时说明：

- 发送范围。
- 调用方式和模型或命令。
- 可能的成本、耗时和隐私影响。
- 是否有副作用。

未获授权时，只做本地自审并说明原因。默认禁止 `--fix`、`--comment`、自动发 PR 评论、自动修改工作树等副作用选项。云端多 agent、`ultra`、深度云端 review 必须单独授权。

授权后，代码 review 默认使用本机 Claude Code 的 `claude-opus-4-8 + xhigh`；文档、规划和策略 review 默认使用 `claude-opus-4-6 + max`，并按审稿目标自定义 prompt，不使用代码 review 专用命令。

## Codex Desktop Lens

桌面端体验可以帮助提出问题，但不能证明 `openai/codex` 开源实现。

允许链路：

```text
桌面端观察 -> 源码阅读问题 -> 固定 SHA 证据或官方文档 -> 教学表达
```

禁止链路：

```text
桌面端观察 -> 直接断言 openai/codex 官方实现
```

写入文档时必须标注为“观察视角”“产品设计启发”“源码阅读问题”“教学抽象”或“推断”。无法回到公开源码或官方文档核验时，不要写成官方事实。

## 教学 Mock

Python mock 只用于教学：

- 离线、确定性、优先只用标准库。
- 不调用 OpenAI API，不依赖真实 Codex 服务。
- 不声称复刻 OpenAI Codex、Codex 桌面端或生产行为。
- 可以借用权限失败、凭据边界、外部 review 等 failure path，但必须写成教学场景，不能当作官方事实证据。

## 提交前检查

维护 change 准备进入 review 前，至少运行：

```bash
openspec validate <change-name> --strict
python3 scripts/check_docs.py
python3 scripts/run_all.py
python3 -m unittest discover -s tests
git diff --check
```

如果某项没有运行或失败，必须在 summary 中说明原因和风险。

Review summary 至少说明：

- 改了哪些文件。
- 是否改变章节状态。
- 是否改变官方事实、`source-evidence.md` 或 `fact-snapshot.md`。
- 是否使用 Claude 或其他外部 review；如果没有，也明确说明。
- 运行了哪些检查，结果如何。

## PR / Release Closeout

准备把一批完成的 changes 送 review 或 PR 前，先做一次 closeout：

- 列出本批新增/修改的文档、章节、mock、diagram 和 OpenSpec changes。
- 明确哪些章节状态没有变化；尤其是 s08/s10 是否仍为 `待核实`，s12 是否仍为 `教学抽象`。
- 明确是否改变 `docs/fact-snapshot.md` target commit、release 核验值或 `scripts/check_docs.py`。
- 给出 active OpenSpec changes 的处理策略：review 前默认保留 active，归档应在 review 后按人类指令或单独 change 执行。
- 写出 PR summary 草案，包括事实边界、检查结果和剩余风险。
- 不在 closeout 中新增官方事实；如果发现必须新增事实，先回到对应 evidence / OpenSpec change。
