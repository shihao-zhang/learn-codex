# s09_app_server_transport

## 状态标签

状态：已核实官方事实

## 本章回答什么

Step 1 只固定边界：本章将解释 app-server、transport、protocol package 和状态同步的公开源码范围。

## 对产品与平台设计的意义

app-server 决定多端 UI、远程控制、状态同步和工具事件如何被产品化。它是“agent runtime”与“用户界面”之间的接口层。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s09_app_server_transport/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- app-server
- transport
- app-server protocol
- status sync

## 真实 Codex 映射

- [codex-rs/app-server/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server/src)
- [codex-rs/app-server-protocol/src](https://github.com/openai/codex/tree/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/app-server-protocol/src)

## 教学简化与生产差异

Python mock 只能演示消息流，不会复刻真实 transport、并发、连接恢复和 schema 导出。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 核实 request/response 与 outgoing message 的边界。
- [ ] 区分 app-server 开源协议和任何非公开 Codex Cloud 行为。
