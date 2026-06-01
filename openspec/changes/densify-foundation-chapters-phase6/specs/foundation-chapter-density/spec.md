## ADDED Requirements

### Requirement: 前 6 章内容加厚

仓库 SHALL 在 s01~s06 的章节 README 中补强产品问题、失败路径、mock trace 解读和事实边界说明。

#### Scenario: 章节被纳入 Phase 6

- **WHEN** 章节属于 s01~s06
- **THEN** 该章节 README 包含面向 AI 产品经理的真实问题、至少一个 failure path、mock trace 如何帮助理解机制、以及不扩大官方事实边界的说明

### Requirement: 官方事实边界保守

Phase 6 SHALL NOT 将无固定 SHA 证据、OpenAI 官方文档或 release note 支撑的解释写成官方事实。

#### Scenario: 新增机制解释没有证据

- **WHEN** 新增内容来自教学抽象、产品经验、Codex 桌面端观察或推断
- **THEN** 文档使用 `教学抽象`、`推断`、`待核实` 或等价保守措辞，而不是声明为 `已核实官方事实`

#### Scenario: 新增官方机制事实

- **WHEN** 新增内容声称为 `openai/codex` 官方机制事实
- **THEN** 该内容能追到固定 SHA OpenAI 源码 permalink、OpenAI 官方文档或 release note，并按统一证据索引规则登记

### Requirement: Phase 5 边界继承

Phase 6 SHALL 继承 Phase 5 对 s08/s10 的保守状态判断。

#### Scenario: 更新阶段状态

- **WHEN** `README.md` 或 `docs/roadmap.md` 说明 Phase 6 进展
- **THEN** 文档不升级 s08/s10 状态，不把 Phase 5 待核实结论写成稳定官方事实

### Requirement: Integrated mock 不在本轮启动

Phase 6 SHALL NOT 启动、设计或实现 integrated teaching mock。

#### Scenario: 发现端到端 mock 需求

- **WHEN** 加厚 s01~s06 时发现需要跨章端到端教学 mock
- **THEN** 只把它记录为 Phase 7 后续问题，不在本 change 中实现

### Requirement: 验收检查

Phase 6 SHALL run the repository validation commands before being marked complete.

#### Scenario: Change is ready for review

- **WHEN** Phase 6 content updates are complete
- **THEN** the maintainer runs `openspec validate densify-foundation-chapters-phase6 --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`
