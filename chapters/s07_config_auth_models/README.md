# s07_config_auth_models

## 状态标签

状态：已核实官方事实

## 本章回答什么

本章解释为什么“选模型”不是一个孤立下拉框。agent 在发起模型请求前，需要先确定配置来源、认证方式、provider/model、模型能力参数，以及错误时如何给用户可恢复的提示。任何一个环节不清楚，都会表现为“明明选了模型却跑不起来”“账号可用但权限不对”“某个 reasoning 参数没有生效”。

对平台设计者来说，config 是策略入口，auth 是身份与权限入口，model/provider 是能力与成本入口。三者合起来才构成一次可执行、可审计的模型调用上下文。

## 对产品与平台设计的意义

配置和认证决定部署方式、账号边界、成本控制和默认体验。一个好的模型选择体验至少要回答四个问题：这个 provider 是否存在，当前用户是否有凭据，所选模型是否支持目标能力，失败时用户该改配置、登录还是换模型。

PM 需要把模型选择看成“能力策略”，而不只是偏好设置。比如 reasoning effort 会影响成本、延迟和答案质量预期；provider 选择会影响可用模型、认证路径和企业合规；默认模型会影响新用户的第一印象和平台成本曲线。

## 机制图

见 [diagram.mmd](diagram.mmd)。该图是教学抽象，用来说明配置、认证和模型请求上下文的关系，不表示官方运行时完整流程。

## 可选教学辅助 SVG

见 [model-choice-impact.md](diagrams/model-choice-impact.md)。这张图只辅助理解 config/auth/provider/model 选择对成本、能力、合规和可用性的影响，不替代本章 Mermaid，也不新增官方事实。

## 运行 mock

```bash
python3 chapters/s07_config_auth_models/mock.py --demo
```

这个 mock 只演示“配置选择 provider/model -> 检查凭据 -> 组装请求设置 -> 返回可恢复错误”的产品机制。它不会调用真实模型，也不会读取、打印或验证真实凭据。

## 核心机制

- `config`：把用户偏好、项目配置、profile 和运行参数转成运行时可理解的设置。教学上可理解为“模型请求前的策略表”。
- `auth`：决定当前请求能以什么身份访问 provider。它不只是有没有 token，还包括 token 来源、账号边界、过期状态和错误恢复路径。
- `model/provider selection`：provider 决定访问哪类后端，model 决定具体能力与上下文限制。平台不应假设所有 provider 都支持同一组模型能力。
- `reasoning effort`：影响推理深度、延迟和成本预期的模型参数之一。产品上要避免把它写成“越高越好”的单向按钮，而应表达权衡。
- `actionable errors`：配置错误应该能指导用户下一步：登录、设置 API key、修正 provider、换模型，或关闭不支持的参数。

## 真实 Codex 映射

- [codex-rs/protocol/src/config_types.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/config_types.rs)
- [codex-rs/protocol/src/models.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/models.rs)
- [codex-rs/protocol/src/openai_models.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/openai_models.rs)
- [codex-rs/protocol/src/auth.rs](https://github.com/openai/codex/blob/740d942f901a5a63421298c74dafbeb4255e946d/codex-rs/protocol/src/auth.rs)

以上固定 SHA 链接是本章的官方事实入口：它们说明当前教学对象中存在配置类型、模型定义、OpenAI 模型信息与认证相关源码。本文不新增未经 fact snapshot 登记的链接。

## 教学简化与生产差异

本章使用“按 config 选择 model/provider”的简单模型，不把它讲成复杂模型路由。生产系统可能存在更多输入来源、默认值覆盖、实验开关、企业策略、环境变量和 UI 设置；这些细节必须以源码和官方文档核实后才能写成事实。

本章也不把认证简化成“有 token 就行”。ChatGPT 登录、API key、provider 配置和本地凭据存储属于不同产品语义；它们影响隐私、审计、计费和故障处理。教学 mock 只表达决策点，不处理真实密钥。

## 练习

1. 设计一个模型选择错误页，分别覆盖：provider 不存在、未登录、凭据过期、模型不支持某参数。
2. 给 `reasoning effort` 写三档产品文案，要求同时说明质量、延迟和成本权衡。
3. 画出你自己平台的配置优先级：全局默认、项目配置、命令行覆盖、临时用户选择，冲突时谁赢。
4. 运行 mock，观察 failure path 为什么应该返回可恢复配置错误，而不是让 agent 在后续轮次里猜。

## 事实核验清单

- [ ] 核实 config 字段、默认值、覆盖顺序和 profile 行为。
- [ ] 区分 ChatGPT 登录、API key、provider 配置与本地凭据存储。
- [ ] 核实模型能力参数与 reasoning effort 的真实支持范围，避免把教学文案写成官方承诺。
