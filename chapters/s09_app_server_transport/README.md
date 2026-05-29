# s09_app_server_transport

## 状态标签

状态：已核实官方事实

## 本章回答什么

本章回答一个产品层问题：当 Codex 不只运行在终端里，而要被 App、IDE、远程界面或其他客户端驱动时，运行时如何把“请求、事件、状态、工具进度”整理成可消费的接口层。

公开事实边界仍要收窄：本章只讨论固定 commit 中的 `codex-rs/app-server/src` 与 `codex-rs/app-server-protocol/src`。目前已核实 transport 连接状态、outgoing message 路由、server request 回调、thread status 投影和 schema export 入口；字段级兼容性和客户端实现细节仍放在事实核验清单里。本章不会把这些路径扩展成 Codex Cloud 或任何非公开服务架构。

## 对产品与平台设计的意义

对 AI 产品经理来说，app-server 的价值不是“又多了一层后端”，而是把 agent runtime 变成可产品化的状态机：

- 客户端不应直接理解内部 loop，而应消费稳定的请求、响应、事件和状态。
- UI 需要知道任务是否在思考、等待工具、申请权限、被中断、完成或失败；这些都要通过接口层同步，而不是靠猜日志。
- 多端体验依赖状态再现：同一个 thread 在不同界面里看到的进度、文件变化、审批请求和错误含义要一致。
- 平台设计要区分 transport、protocol、runtime 三层：transport 解决“怎么连”，protocol 解决“说什么”，runtime 解决“怎么做”。

## 机制图

见 [diagram.mmd](diagram.mmd)。图是教学拆解：把客户端请求、transport、app-server 协调层、核心运行时、状态投影和 outgoing message 分开看，帮助读者理解接口边界；它不是官方部署图。

## 运行 mock

```bash
python3 chapters/s09_app_server_transport/mock.py --demo
```

教学 mock 只演示“客户端请求进入、运行时产生事件、服务端投影状态、客户端接收更新”的消息流，不代表真实 Codex transport、JSON-RPC 细节、线程模型或错误恢复策略。

## 核心机制

- `app-server`：面向客户端的协调层。它把用户界面需要的动作封装成请求，把 runtime 产生的变化整理成客户端可消费的消息。
- `transport`：连接与传输边界。产品上要把它看成“会断、会重连、会乱序感知”的基础设施，而不是业务逻辑本身。
- `app-server protocol`：客户端和 app-server 之间的消息契约。协议层一旦稳定，UI、自动化和远程控制才能独立演进。
- `request processing`：把客户端动作转成运行时可执行的操作，例如开始任务、中断、审批、配置变更或状态查询。
- `outgoing message`：把运行时事件、工具状态、错误和完成信号转成 UI 侧可以渲染的更新。
- `thread state/status`：把长任务压缩成产品状态。它不是完整日志，而是“当前应该让用户看到什么、允许做什么”的状态投影。

## 真实 Codex 映射

- [codex-rs/app-server/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server/src)
- [codex-rs/app-server-protocol/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server-protocol/src)

机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)：transport/outgoing/status/schema export 已核实到具体源码行。章节状态因此升级为“已核实官方事实”，但这个标签只覆盖本章明确列出的公开源码机制；字段级兼容性、客户端实现和非公开服务架构仍不能外推。

## 教学简化与生产差异

本章把接口层简化成“request -> runtime -> state/outgoing message”。真实生产实现会复杂得多：

- transport 需要处理连接生命周期、背压、取消、重放、超时和客户端版本差异；本章只核实了连接状态、消息路由和慢连接队列处理的一部分源码路径。
- protocol 需要兼顾类型稳定、schema 导出、兼容性和错误码，而不是随便传 JSON。
- 状态同步通常不是完整事件日志的逐字转发，而是面向产品视图的投影与压缩。
- app-server 不等于模型服务，也不等于 Codex Cloud；它位于客户端体验和本地/核心运行时之间。
- 教学图和 Python mock 都不是官方实现，只是帮助理解“接口层为什么存在”。

## 练习

1. 画出你自己的 agent 产品状态表：至少包含 `idle`、`running`、`waiting_for_tool`、`waiting_for_approval`、`interrupted`、`completed`、`failed`，并写出每个状态允许的用户操作。
2. 设计一个“断线重连”场景：客户端断开 30 秒后回来，应该请求哪些状态，哪些事件可以丢，哪些必须恢复。
3. 把一次 shell 工具调用拆成三条 UI 更新：开始、输出增量、结束。说明哪些字段属于 protocol，哪些只是界面展示。
4. 找一个你熟悉的 agent App，判断它的问题是在 transport 层、protocol 层、runtime 层，还是状态投影层。

## 事实核验清单

- [x] 仅使用 fact-snapshot 中登记的固定 SHA permalink。
- [x] 明确区分公开 app-server/app-server-protocol 源码与任何非公开 Codex Cloud 行为。
- [x] 明确 Python mock 和 Mermaid 图都是教学材料，不是官方实现。
- [x] 已把 transport、outgoing message、thread status 和 schema export 的机制级证据登记到 `docs/source-evidence.md`。
- [ ] 继续逐字段核实 request、notification、response、thread history pagination 和 experimental API 兼容性。
