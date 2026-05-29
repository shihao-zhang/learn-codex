# s03_tool_registry_dispatch

## 状态标签

状态：已核实官方事实

## 本章回答什么

本章回答：模型说“我要调用某个工具”之后，运行时如何把这句话变成一次受控执行。

工具系统的核心不是“有一个函数可以调用”，而是四段契约：

- 工具如何声明自己，包括名称、参数 schema、是否对模型可见。
- 工具如何注册到运行时，避免重名、错配和未授权暴露。
- 模型输出如何被解析成工具调用，并路由到正确 handler。
- handler 的结果如何回到模型、UI、trace 和生命周期事件中。

## 对产品与平台设计的意义

对 AI 产品经理来说，工具目录就是 agent 的能力边界。暴露一个工具，相当于给模型增加一种可行动作；隐藏一个工具，可能会降低自动化能力但提升安全性和可控性。

对平台设计者来说，registry/router 是能力治理的入口。它要回答：哪些工具对模型可见？哪些只供内部使用？未知工具如何失败？参数不兼容算用户错误、模型错误还是平台错误？工具执行前后是否要跑 hook、记录 telemetry、支持取消和并行？

## 机制图

见 [diagram.mmd](diagram.mmd)。图里把工具从“可见 spec”到“handler 执行”再到“结构化结果”的路径拆开，方便理解 registry 和 router 的职责差异。

## 运行 mock

```bash
python3 chapters/s03_tool_registry_dispatch/mock.py --demo
```

这个 mock 只展示最小路由链路：注册两个工具、模型请求其中一个、router 找到 handler、handler 返回结果；失败路径展示未知工具如何被结构化拒绝。它不是 Codex 官方工具系统。

## 核心机制

- `tool spec` 是给模型看的能力说明，也是平台控制工具暴露面的第一道门。没有清晰 spec，模型会猜参数；spec 暴露过宽，模型会尝试危险或昂贵动作。
- `registry` 是运行时持有的工具索引。它负责把工具名映射到可执行 runtime，并处理重名、可见性、能力元数据和执行前后需要的辅助逻辑。
- `router` 负责把模型响应里的 tool call 解析成内部调用对象。它要识别函数工具、搜索工具、自定义工具等不同 payload，并把未知或不兼容调用转成稳定错误。
- `handler` 是真正执行工具逻辑的地方。handler 不应该绕开运行时的权限、hook、trace、取消和生命周期通知。
- 工具结果至少有两种读者：模型需要可继续推理的结果，客户端需要可展示的状态。把二者混在一起，会让 UI 或模型任一方被迫消费不适合自己的格式。
- 工具失败也要结构化。未知工具、参数非法、权限拒绝、handler 运行失败、取消和超时，应尽量形成可恢复或可解释的分支。

## 真实 Codex 映射

- [codex-rs/core/src/tools/registry.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/registry.rs)
- [codex-rs/core/src/tools/router.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/router.rs)
- [codex-rs/core/src/tools/handlers](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/handlers)

映射解释：

- `registry.rs` 是理解工具索引和执行分发的主要入口。本章只把它作为官方阅读锚点；工具 runtime、tool output、pre/post tool hook、telemetry、生命周期通知和未知工具错误等细节必须继续按本章核验清单逐文件确认。
- `router.rs` 是理解“模型响应 item 如何变成内部 ToolCall”的入口。它连接模型输出结构、工具名、call id、payload 和 registry dispatch。
- `handlers` 目录是具体工具实现的入口。教学里的 handler 是一个极简函数；真实 handler 会面对权限、环境、参数解析、错误传播和结果格式。
- 本章不把 mock 中的 `ApplyPatchHandler` 当成官方类型名；它只是帮助读者理解“路由到 handler”这件事。
- 机制级证据登记在 [docs/source-evidence.md](../../docs/source-evidence.md)，包括 router 参数、registry 构造、pre/post hook、handler 调用和错误回写。

## 教学简化与生产差异

- mock 把 registry 简化成“工具名 -> 函数”的映射；真实实现还要处理工具可见性、动态工具、扩展工具、hook 输入改写、并行能力、取消语义和 telemetry tag。
- mock 把 router 简化成直接查表；真实实现需要从模型响应结构中提取不同类型的 tool call，并处理不支持的 custom tool 或 payload kind。
- mock 把 handler 结果简化成一条事件；真实实现会把结果转换成模型输入 item、客户端事件、日志预览、trace 和可能的 hook 响应。
- mock 不覆盖权限系统。shell、文件修改、网络访问等能力必须和 s04 的 sandbox/approval 一起理解。

## 练习

1. 运行 mock，画出 `tool name -> router -> handler -> result` 的调用链。
2. 设计一个新工具 `read_config`：写出名称、参数、成功结果、失败结果，以及它是否应该对模型默认可见。
3. 假设模型请求了不存在的工具。你会让 agent 重试、向用户解释，还是直接失败？分别适合什么场景？
4. 为一个危险工具设计三层防线：不对模型默认暴露、执行前权限检查、执行后结果审计。
5. 思考平台演进：当工具 schema 改版时，如何让旧模型提示词、旧客户端和旧 trace 仍然可解释？

## 事实核验清单

- [x] 在固定 SHA 的 `registry.rs` 中核实工具注册、dispatch、hook、telemetry 和错误处理的主要职责。
- [x] 在固定 SHA 的 `router.rs` 中核实模型响应 item 到内部 tool call 的转换边界。
- [ ] 在固定 SHA 的 `handlers` 目录中核实具体工具 handler 的实际分布，不把教学 handler 名称写成官方类型。
- [ ] 区分模型可见工具、隐藏工具、动态工具、扩展工具和外部 MCP/extension 工具。
- [ ] 不把“工具调用成功”简化成“业务动作成功”；handler 运行、权限通过、业务结果符合预期是不同层级。
