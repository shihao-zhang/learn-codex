## Context

s10 讨论“能力如何进入 agent 平台”，但它不是一个统一扩展产品的说明书。当前章节已经把 MCP、dynamic tools、extension tools、skills directory 拆成四条能力线：有些路径已能追到 CLI、配置、runtime adapter 或 TUI 入口，有些只证明内部机制存在，有些仍停在 experimental 或待核实边界。

读者最容易误解的点有三个：

- 看到 MCP、extension、skills 这些词，就以为它们是同一套官方插件生态。
- 看到 dynamic tools 的 runtime handler，就以为 CLI 用户可以稳定创建动态工具。
- 看到 extension registry 和内置 app-server extensions，就以为存在通用用户安装、发现、授权入口。

因此，本轮 SVG 应把四条线并排展示，并把治理问题拆成“各自已有线索”和“统一治理路径待核实”，而不是画成一个单一平台漏斗。

## Scope

本 change 只覆盖：

1. `chapters/s10_extensions_mcp_skills/diagrams/extension-capability-lines.svg`
2. `chapters/s10_extensions_mcp_skills/diagrams/extension-capability-lines.md`
3. `chapters/s10_extensions_mcp_skills/README.md` 的可选 SVG 入口

## Source Inputs

本轮图形只使用以下输入：

- `AGENTS.md`
- `docs/diagram-style-guide.md`
- `chapters/s10_extensions_mcp_skills/README.md`
- `chapters/s10_extensions_mcp_skills/diagram.mmd`
- `chapters/s10_extensions_mcp_skills/mock.py`
- `docs/source-evidence.md` 中已登记的 s10 机制证据
- `openspec/specs/s10-extensions-mcp-skills-verification/spec.md`
- `openspec/specs/s10-extensions-mcp-skills-deep-verification/spec.md`

## Fact Boundary

- s10 章节状态保持 `待核实`。
- `FACT` 只标记 `docs/source-evidence.md` 已登记的 s10 局部机制点：
  - MCP CLI/config/tool discovery/exposure/handler/approval 相关路径。
  - dynamic tools 的 app-server experimental entry、命名校验、runtime request/response flow。
  - extension API registry、tool contributor contract、app-server 内置 extensions、adapter 进入 runtime。
  - skills TUI 入口、roots/config、system cache、available skills instructions、explicit mention injection、MCP dependency 提示。
- `待核实` 必须显式覆盖：
  - dynamic tools experimental API 稳定性与客户端产品边界。
  - 通用 extension 用户安装、发现、授权或市场式入口。
  - MCP、dynamic tools、extension tools、skills 是否共享统一治理路径。
- `教学辅助` 用于四条能力线的并列表达、产品治理问题、mock trace、读者建议和图形布局。
- 图中不得出现“统一官方扩展产品”“官方插件生态已闭环”“统一治理已验证”等暗示。

## Drawing Rules

- Mermaid 继续是 s10 README 的主机制图入口；SVG 只能作为“可选教学辅助 SVG”。
- 手写 SVG，保持源码可读、可 diff。
- 无外部图片、字体文件、网络或生成依赖。
- 中文优先；英文只作为路径、字段、命令、API 或 trace chip。
- SVG 必须包含 `<title>`、`<desc>` 和可见图例或边界说明。
- 四条能力线必须保持视觉分离，不能汇成“统一官方产品承诺”。
- 待核实节点使用虚线边框、`待核实` badge 和文字说明，颜色不得作为唯一语义。

## Validation

完成前需要检查：

- OpenSpec tasks 全部完成。
- 新增 SVG XML 可解析，并含 `<title>`、`<desc>` 和可见图例或边界说明。
- 渲染预览后确认主路径、四条能力线、待核实边界、箭头、文字和图例可读。
- s10 README 仍把 Mermaid 放在“机制图”小节，并且状态仍为 `待核实`。
- 不修改根 `README.md`、`docs/roadmap.md`、`docs/diagram-style-guide.md`、`docs/fact-snapshot.md`、`docs/source-evidence.md` 或 `scripts/check_docs.py`。
- 运行用户要求的全部命令：
  - `openspec validate rollout-s10-extension-svg --strict`
  - `openspec validate --all --strict`
  - `python3 scripts/check_docs.py`
  - `python3 scripts/run_all.py`
  - `python3 -m unittest discover -s tests`
  - `git diff --check`
