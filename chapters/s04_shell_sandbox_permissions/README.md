# s04_shell_sandbox_permissions

## 状态标签

状态：已核实官方事实

## 本章回答什么

Step 1 只固定边界：本章将解释 shell tool、sandbox policy、approval 与网络权限如何一起形成安全边界。

## 对产品与平台设计的意义

权限系统是在“让 agent 有用”和“防止 agent 越界”之间做产品权衡。它影响用户信任、企业合规、默认权限和中断体验。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s04_shell_sandbox_permissions/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- shell execution
- sandbox policy
- approval request
- network approval

## 真实 Codex 映射

- [codex-rs/core/src/tools/sandboxing.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/sandboxing.rs)
- [codex-rs/core/src/tools/network_approval.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/core/src/tools/network_approval.rs)
- [codex-rs/protocol/src/permissions.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/permissions.rs)

## 教学简化与生产差异

Python mock 不能复刻 macOS Seatbelt、Linux sandbox 或 Windows restricted token，只能表达“决策点”和“用户确认点”。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 分 OS 核实 sandbox 行为。
- [ ] 区分 approval policy、sandbox policy 和 network policy。
