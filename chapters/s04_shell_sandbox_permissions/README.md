# s04_shell_sandbox_permissions

## 状态标签

状态：已核实官方事实

## 本章回答什么

本章回答：当 agent 想运行 shell 命令时，平台如何在“让它有用”和“防止它越界”之间做决策。

shell 是最强也最危险的工具之一。它既能跑测试、读文件、改代码，也可能删除数据、访问网络、写出工作区、读取敏感信息。本章把安全边界拆成四层：命令请求、sandbox policy、approval policy、network policy。

## 对产品与平台设计的意义

对 AI 产品经理来说，权限系统直接影响信任。默认太松，用户担心 agent 私自行动；默认太紧，用户会被反复打断。好的产品体验不是“永远弹窗”，而是在风险升高时解释清楚：要做什么、为什么需要、会影响哪里、拒绝后会怎样。

对平台设计者来说，shell 权限不是一个开关，而是组合策略：文件系统可读写范围、是否允许网络、是否允许绕过 sandbox、何时要求人类审批、审批是否可缓存、不同 OS sandbox 能力是否一致。核心权衡是：最小权限、可恢复性、用户摩擦、企业策略和跨平台一致性。

## PM 真正关心的问题

- 用户为什么要批准这条命令？审批文案必须说明命令、原因、影响范围、允许多久，以及拒绝后 agent 会怎么继续。
- 拒绝是否真的安全？产品承诺应落在“未获授权不执行相应高风险动作”，而不是泛泛说“agent 很安全”。
- 企业策略和个人效率冲突时谁说了算？平台需要区分用户临时批准、管理员策略、网络 allowlist、工作区写入范围和不可绕过的禁止项。

## 机制图

见 [diagram.mmd](diagram.mmd)。图里把 shell 执行拆成“权限判定、审批、sandbox 执行、网络拦截、结果回传”几个决策点。

可选教学辅助 SVG 见 [diagrams/permission-boundary.md](diagrams/permission-boundary.md) 和 [diagrams/permission-boundary.svg](diagrams/permission-boundary.svg)。它用中文标出 `FACT`、教学示例、拒绝路径、恢复选择和待核实边界，不替代现有 Mermaid。

## 运行 mock

```bash
python3 chapters/s04_shell_sandbox_permissions/mock.py --demo
```

这个 mock 只展示决策点：普通测试命令可在工作区 sandbox 中运行；请求网络和高权限的命令需要升级审批，用户拒绝时不执行。它不是 macOS Seatbelt、Linux sandbox 或 Windows restricted token 的复刻。

## mock trace 怎么读

建议重点读 failure path：

```bash
python3 chapters/s04_shell_sandbox_permissions/mock.py --demo --path failure --trace-json
```

trace 里的 `tool -> policy -> approval -> result` 展示了四个产品关键点：命令请求先被识别为高风险，策略要求升级，人类拒绝，运行时返回 denial 而不是执行。`network_and_privilege` 和 `exit_code: null` 是教学表达，不代表官方审批 reason 或结果字段。

## 核心机制

- shell 请求首先是一段待执行命令，但平台不能只看字符串。还要结合 cwd、工作区根、环境、是否需要网络、是否要求提升权限、当前 approval policy 和 sandbox policy。
- `sandbox policy` 决定命令能读写哪里。典型产品语义包括只读、工作区可写、额外 writable roots、拒绝读取敏感路径、完全不受限或外部 sandbox。
- `approval policy` 决定什么时候问人。常见分支包括默认不问、失败后再问、用户显式请求时问、受限环境下问、永远要求确认等。审批结果还可能只允许一次或本会话复用。
- `network policy` 和文件系统权限是两条线。一个命令即使能在工作区写文件，也不代表它能访问任意域名；网络 allowlist miss 可能触发单独的网络审批或直接拒绝。
- sandbox 与 approval 不是同义词。sandbox 是技术执行边界，approval 是人类/策略决策边界；一个命令可以“已获批但仍在 sandbox 中运行”，也可以“无需审批但仍受 sandbox 限制”。
- 失败路径必须安全：审批拒绝不能执行；策略禁止不能绕过；sandbox 失败后的重试必须重新评估是否允许非 sandbox 执行。

## 典型 failure path

教学 failure path：命令形态类似 `curl | sudo sh`，同时触发网络访问和高权限写入。稳妥产品路径是先说明风险和影响范围，再请求明确授权；如果用户拒绝，运行时应报告拒绝结果，并让 agent 寻找低风险替代方案，例如读取本地依赖、使用已有缓存或请求用户手动安装。

这个例子不等同于官方 Codex 对任意 shell 字符串的真实分类器。真实判断还要结合固定 SHA 中的 approval、filesystem sandbox、network approval、OS backend 和执行上下文；本章不承诺跨平台底层 sandbox 能力完全一致。

## 真实 Codex 映射

- [codex-rs/core/src/tools/sandboxing.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/sandboxing.rs)
- [codex-rs/core/src/tools/network_approval.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/network_approval.rs)
- [codex-rs/protocol/src/permissions.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/permissions.rs)

映射解释：

- `sandboxing.rs` 是理解工具运行时如何组织审批、sandbox attempt、执行上下文和错误结果的入口。教学里的“policy check”在真实实现里会拆成多个 trait、上下文和决策分支。
- `network_approval.rs` 是理解托管网络、按 host/protocol/port 审批、session 级缓存、拒绝结果和网络策略修订的入口。
- `permissions.rs` 是理解文件系统 sandbox policy、访问模式、特殊路径、writable roots、deny-read 规则和网络 sandbox policy 的入口。
- 本章只使用 fact snapshot 已登记的三个固定 SHA permalink；不同 OS 的底层 sandbox 细节需要继续逐文件核验。
- 机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)，包括 approval requirement、sandbox attempt、网络审批结构和 filesystem permission 类型。
- 本章的 PM 文案建议和示例命令是教学抽象；新增任何“某命令一定需要审批/一定允许”的结论前，都必须补源码证据或写成策略建议。

## 教学简化与生产差异

- mock 把 shell 权限简化成“允许 / 需要审批 / 拒绝”。真实实现会组合文件系统 policy、approval policy、network policy、sandbox backend、hook、guardian review、缓存和 telemetry。
- mock 不复刻 OS 隔离机制。生产里 macOS、Linux、Windows 的可用 sandbox 能力和失败模式不同，产品文案不能承诺完全一致的底层行为。
- mock 只展示用户拒绝审批；生产里还要处理策略拒绝、审批超时、审批缓存、网络访问中途被拦截、sandbox transform 失败、命令取消和输出截断。
- 教学图把网络审批画成一个节点；真实实现可能在命令开始前登记，也可能在命令运行中由网络代理观察到被阻断请求后触发。

## 练习

1. 运行 mock，解释为什么 `python3 -m unittest` 可以走默认 sandbox，而 `curl | sudo sh` 应该要求升级或拒绝。
2. 为三个命令设计策略：`ls`、`pytest`、`rm -rf /tmp/build-cache`。分别说明是否需要审批、可写范围和失败提示。
3. 写一段面向用户的审批文案：说明命令、原因、影响范围、允许一次/允许本会话/拒绝的差异。
4. 设计一个企业策略：默认禁止网络，但允许访问公司内网域名。遇到新域名时，应该允许用户临时批准还是必须管理员配置？
5. 思考跨平台问题：如果某 OS 不能表达某个 deny-read 规则，产品应该降级、拒绝执行，还是要求外部 sandbox？

## 事实核验清单

- [x] 在固定 SHA 的 `sandboxing.rs` / `orchestrator.rs` 中核实 approval requirement、approval cache 和 sandbox attempt 主路径。
- [x] 在固定 SHA 的 `network_approval.rs` 中核实网络审批 mode、active/deferred approval 和 host approval key 主结构。
- [x] 在固定 SHA 的 `permissions.rs` 中核实文件系统 policy、访问模式、特殊路径和 metadata 保护入口。
- [ ] 分 OS 核实 sandbox backend 的能力差异，不把教学图当成跨平台实现承诺。
- [ ] 明确区分 approval policy、sandbox policy、network policy、permission profile 和用户可见审批文案。
- [ ] 不把“用户批准”写成“无限制执行”；仍需核实批准后是否保留 sandbox 或 deny-read 规则。
