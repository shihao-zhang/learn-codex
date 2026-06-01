# s12_comprehensive_architecture

## 状态标签

状态：教学抽象

## 本章回答什么

本章把前 11 章串成一张端到端教学架构图，帮助读者理解 Codex CLI harness 可以怎样被拆成产品面、接口面、运行时、安全面、记忆面和扩展面。

重要边界：本章是教学抽象，不是 OpenAI 官方架构图，不代表真实部署拓扑，不覆盖 Codex Cloud 或任何非公开内部系统。图中的实线表示前面章节已经建立过的公开源码锚点或教学关系；待核实章节会显式标为待核实。

## 对产品与平台设计的意义

综合架构的价值是把零散机制翻译成产品决策：

- 用户看到的是“对话、进度、权限、文件变化、错误和结果”，不是 loop、router、protocol crate。
- 平台要把模型调用、工具执行、上下文压缩、会话恢复、权限审批和 app-server 状态同步组织成一条可解释链路。
- 每个边界都对应一个产品风险：协议漂移会破坏 UI，权限继承会影响安全，扩展面会影响生态治理，并行会影响成本和可控性。
- PM 读总图时，不应追求“画全”，而应追问“哪个状态由谁负责、失败时用户能不能理解、恢复时系统知道做到哪里了吗”。

## 机制图

见 [diagram.mmd](diagram.mmd)。图是教学总览：把产品界面、app-server/protocol、core runtime、工具/权限/上下文/模型/会话，以及待核实扩展与并行线索放在一张图里。

## 运行 mock

```bash
python3 chapters/s12_comprehensive_architecture/mock.py --demo
python3 chapters/s12_comprehensive_architecture/mock.py --demo --path failure
python3 chapters/s12_comprehensive_architecture/mock.py --demo --scenario session_recovery --trace-json
```

教学 mock 只演示端到端控制流，不代表真实 Codex 架构、Codex 桌面端实现、进程边界、网络边界、存储边界或官方模块划分。它是 deterministic、offline、Python 标准库教学抽象；不会调用 OpenAI API、网络、Keychain、外部 CLI、真实审批系统或真实桌面端状态。

可选场景：

- `--path happy`：agent loop、tool dispatch、permission allow、context budget 和 final answer 的主线。
- `--path failure`：综合失败摘要，串起 tool dispatch、permission、context pressure、instruction conflict 和 recovery stop。
- `--scenario tool_dispatch_error`：工具名无法路由时如何返回 recoverable error。
- `--scenario permission_denied`：权限拒绝后如何避免执行并给出低风险选项。
- `--scenario context_pressure`：固定教学预算下如何触发 `teaching_summary`，不模拟真实 tokenization。
- `--scenario instruction_conflict`：项目 offline 约束与用户联网请求冲突时如何解释优先级。
- `--scenario session_recovery`：从教学 checkpoint 恢复，避免重复有副作用动作；s08 session/thread/rollout 语义继续标为 `待核实`。

## 核心机制

- `product surface`：用户提交任务、查看进度、批准权限、接收结果。它关心状态和解释，不直接关心内部实现。
- `app-server / protocol boundary`：把产品动作转成请求，把 runtime 事件转成 UI 可消费消息；适合承载多端和远程界面。
- `core runtime`：负责 agent loop、turn、工具路由、模型交互和终止条件，是 harness 的执行中心。
- `tool and permission plane`：工具让 agent 能行动，权限让行动可治理。两者必须一起设计。
- `context and memory plane`：上下文窗口、压缩、session/thread/rollout 决定长任务能否连续、可恢复、可解释。
- `model/config/auth plane`：模型选择、provider、认证和配置决定成本、能力、合规和默认体验。
- `extensions and parallelism`：s10/s11 仍是待核实语义；总图只能把它们标成“待核实扩展面/并行面”，不能写成官方主线架构。
- `integrated teaching trace`：Phase 7 mock 用 `teaching_session_id`、`teaching_checkpoint`、`decision_reason`、`context_budget_state` 等教学字段解释状态，不代表官方 session、protocol、thread-store、MCP 或 skills schema。
- `fact vs abstraction`：真实 Codex 映射只用固定 SHA permalink；任何跨章节总图都是教学抽象。

## 真实 Codex 映射

- [codex-rs/core](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core)
- [codex-rs/protocol](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol)
- [codex-rs/app-server](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server)
- [codex-rs/Cargo.toml](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/Cargo.toml)

这些链接锚定公开源码中的大模块和 workspace 入口，不等于官方架构图。总图中的跨模块关系是教学组织方式，必须回到前面章节逐条核验。

## 教学简化与生产差异

为了让读者形成整体心智，本章刻意牺牲了一些真实复杂度：

- 图把多种异步、并发、错误恢复和状态投影压成少数节点。
- 图不表达真实部署、进程、线程、网络、存储或云端边界。
- mock 的 context budget 是固定整数教学预算，不是 OpenAI Codex 的真实 tokenization 或 compaction 实现。
- mock 的 permission table 是策略演示，不代表真实沙箱、审批 UI 或 Codex 桌面端权限模型。
- mock 的 session recovery 是 checkpoint 教学，不代表 s08 已完成官方核验。
- 图不补画未经公开核验的 Codex Cloud、内部服务、私有 prompt 或隐藏策略。
- s10/s11 的扩展与并行语义仍待核实，所以在总图中只能作为虚线能力面。
- 总图适合教学和产品讨论，不适合拿去当实现设计评审的唯一依据。

## 练习

1. 从用户点击“开始任务”开始，沿总图写出 8 步端到端链路：输入、配置、模型、工具、权限、事件、状态、结果。
2. 选一个失败场景，例如 shell 权限被拒、上下文超限、客户端断线或工具超时，标出它穿过了哪些节点。
3. 给每个节点写一个产品指标：例如工具成功率、审批等待时长、重连恢复率、上下文压缩后任务完成率。
4. 把 s10/s11 的虚线节点拿掉，再看总图是否仍能解释单 agent 主流程；这能帮助你区分“主线机制”和“增强能力”。

## 事实核验清单

- [x] 明确本章是教学抽象，不是 OpenAI 官方架构图。
- [x] Phase 7 integrated teaching mock 保持 deterministic、offline、Python 标准库。
- [x] 文本输出和 JSON trace 保留 `Teaching mock only` 免责声明。
- [x] 真实 Codex 映射只使用 fact-snapshot 中登记的固定 SHA permalink。
- [x] 不绘制无法公开核验的 Codex Cloud 或内部系统。
- [x] s10/s11 在总图中保持待核实语义，不升级为官方主线能力。
- [x] s08 session/thread/rollout 和 s10 MCP/skills/extension 相关语义在 mock 中继续保持 `待核实` 边界。
- [ ] 后续每新增一条跨模块边，都必须回到对应章节事实，或在图中显式标为教学抽象。
