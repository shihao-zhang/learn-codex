# s07_config_auth_models

## 状态标签

状态：已核实官方事实

## 本章回答什么

Step 1 只固定边界：本章将解释 config、auth、model/provider 选择以及 reasoning 参数如何影响运行时。

## 对产品与平台设计的意义

配置和认证决定部署方式、账号边界、成本控制和默认体验。PM 需要理解“选择模型”不是孤立功能，而是权限、计费和能力面的一部分。

## 机制图

见 [diagram.mmd](diagram.mmd)。当前是占位图，Step 2 会补成教学图。

## 运行 mock

```bash
python3 chapters/s07_config_auth_models/mock.py --demo
```

当前 mock 是 Step 1 placeholder，不代表真实 Codex 行为。

## 核心机制

- config
- auth
- model/provider selection
- reasoning effort

## 真实 Codex 映射

- [codex-rs/protocol/src/config_types.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/config_types.rs)
- [codex-rs/protocol/src/models.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/models.rs)
- [codex-rs/protocol/src/openai_models.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/openai_models.rs)
- [codex-rs/protocol/src/auth.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/auth.rs)

## 教学简化与生产差异

本章使用“按 config 选择 model/provider”，不称为复杂模型路由。mock 不会调用真实模型或读取真实凭据。

## 练习

Step 2 补充。

## 事实核验清单

- [ ] 核实 config 字段和默认值。
- [ ] 区分 ChatGPT 登录、API key 和 provider 配置。
