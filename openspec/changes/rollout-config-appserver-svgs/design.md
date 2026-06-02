## Context

本仓面向 AI 产品经理和 agent 平台设计者。s07 与 s09 都属于“产品接口看起来简单，背后机制边界很容易被误读”的章节：

- s07：模型选择不是单个下拉框，而是 config、auth、provider/model、能力参数和错误恢复共同组成的请求上下文。
- s09：app-server 不是模型服务或 Codex Cloud，而是把 runtime 请求、事件和状态投影整理给客户端消费的接口边界。

现有 Mermaid 图继续作为主机制图。SVG 的任务是把影响面和边界画清楚：s07 画成本、能力、合规、可用性的取舍；s09 画 transport、protocol、product surface 之间哪些状态可以同步、哪些不应外推。

## Scope

本 change 只覆盖两章：

1. `s07_config_auth_models`
2. `s09_app_server_transport`

每章新增 1 张核心教学 SVG 和 1 个 companion Markdown。README 只增加短入口，不改变章节状态、不新增官方事实、不调整主机制图。

## Source Inputs

本轮图形只使用以下输入：

- `AGENTS.md`
- `docs/diagram-style-guide.md`
- s07/s09 的 README、`diagram.mmd` 和 `mock.py`
- 已有 SVG 试点和批次 companion note 的组织方式
- `docs/source-evidence.md` 中已登记的 s07/s09 机制证据

## Fact Boundary

- s07 `FACT` 只标记已在 `docs/source-evidence.md` 登记的机制点：
  - config 类型入口。
  - model preset 与 model info。
  - session 初始化时选择模型与 base instructions。
- s07 `教学辅助` 用于：
  - 成本、能力、合规、可用性的产品影响面。
  - provider/model 选择的 PM 文案。
  - auth 来源、账号边界、凭据失败恢复的教学解释。
  - 最新模型可用性、默认值、真实价格、企业策略和 UI 推荐。
- s09 `FACT` 只标记已在 `docs/source-evidence.md` 登记的机制点：
  - transport 连接状态与 outbound 队列。
  - outgoing envelope 路由与慢连接处理。
  - server request/response/callback 管理。
  - thread status 投影。
  - protocol schema export。
- s09 `教学辅助` 用于：
  - product surface、UI 状态命名、多端体验、断线重连策略和用户可见文案。
  - 把 protocol 理解成“产品状态同步合同”的解释。
  - 任何 Codex Cloud、远端服务或非公开客户端行为的边界提醒。
- 本轮不主动引入 s08/s10/s12 语义；如图中需要提醒 resume、extension 或综合架构，只能作为边界提醒，不能画成新增官方事实。

## Drawing Rules

- 手写 SVG，保持源码可读、可 diff。
- 无外部图片、字体文件、网络或生成依赖。
- 中文优先；英文只作为路径、字段、命令、schema 或 mock event 追溯标签。
- 每张 SVG 包含 `<title>` 和 `<desc>`，并在图中放可见图例或边界说明。
- Mermaid 继续是 README 的主机制图入口；SVG 标为“可选教学辅助 SVG”。
- companion Markdown 固定包含：
  - `Source Inputs`
  - `Event / Mechanism Mapping`
  - `Fact Boundary`
  - `Manual QA`

## Validation

完成前需要检查：

- XML 可解析，且每张 SVG 含 `<title>`、`<desc>` 和可见图例或边界说明。
- 渲染预览后确认主路径、侧向路径、文字、chip、箭头和图例可读。
- OpenSpec tasks 全部完成。
- s07/s09 README 仍把 Mermaid 放在“机制图”小节。
- 不修改仓库根 README、`docs/roadmap.md`、`docs/diagram-style-guide.md`、`docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py` 或章节状态。
- 运行用户要求的全部命令：
  - `openspec validate rollout-config-appserver-svgs --strict`
  - `openspec validate --all --strict`
  - XML parse 检查所有新增 SVG
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
