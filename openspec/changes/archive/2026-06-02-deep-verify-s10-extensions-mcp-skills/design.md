## Context

当前事实基线固定在 `docs/fact-snapshot.md` 的目标 commit `740d942f901a5a63421298c74dafbeb4255e946d`。Phase 10 已决定暂不刷新目标 commit 和 `scripts/check_docs.py`，因此本 change 不能用新候选 commit 改写官方事实。

s10 的难点是四类能力位于不同层级：

- MCP 有 CLI 命令、配置和 runtime tool exposure。
- dynamic tools 更像由 thread/session 外部客户端声明和响应的动态工具面。
- extension tools 有 registry、contributors 和 adapter，但用户安装/发现入口仍需核实。
- skills 有 discovery/config/instruction 注入和 TUI 入口，但不等于 MCP 或 extension tool。

## Verification Approach

1. 固定证据来源
   - 只使用当前目标 commit 的 OpenAI source permalink、OpenAI 官方 README 或 release note。
   - 不使用候选新 commit 作为证据；如需提及，只作为追新风险。

2. 分线核验
   - MCP：从 CLI/subcommand、config 类型、MCP connection manager、tool listing/exposure、handler 和 approval/notify 线索读起。
   - dynamic tools：从 protocol 类型、session/thread runtime、handler request/response、client event 边界读起。
   - extension tools：从 extension registry、tool contributors、router/spec planning、adapter executor 读起。
   - skills：从 TUI entry、loader roots、config edit、render/injection、MCP dependency helper 读起。

3. 证据分级
   - `behavior-verified` 只用于已读到关键分支、状态转换、调用闭环或错误/治理路径的机制。
   - `mechanism-verified` 用于入口、类型、adapter 或控制流存在，但行为链未完全闭合的机制。
   - `pending` 用于仍缺用户入口、配置来源、运行时闭环或治理语义的判断。

4. 状态判断
   - 只有当四类能力的入口、发现、配置、暴露和治理路径都能分别闭环，且章节不再依赖统一概念假设时，才考虑把 s10 升级。
   - 如果 extension tools 用户入口、dynamic tools 客户端实现、或四类能力的统一治理语义仍未闭环，则 s10 保持 `待核实`。

## Risks

- Risk: 行号锚点在候选新 commit 可打开，但旧 commit 证据没有重新读。
  Mitigation: 本轮只引用 `740d942f901a5a63421298c74dafbeb4255e946d` permalink。

- Risk: 把 “都进入工具面” 写成 “同一官方扩展体系”。
  Mitigation: 文档使用分线表述，只在教学层说明共同产品问题，不声明统一官方概念。

- Risk: skills 的 TUI 入口被误读为所有客户端一致。
  Mitigation: 明确只证明目标 commit 下的 TUI/protocol/config 线索，不外推到 Desktop 或其他客户端。

## Validation

完成后运行：

```bash
openspec validate deep-verify-s10-extensions-mcp-skills --strict
python3 scripts/check_docs.py
python3 scripts/run_all.py
python3 -m unittest discover -s tests
git diff --check
```

最终说明必须包含：哪些证据升级或收窄、s10 是否升级、仍待核实的入口/治理问题，以及验证命令结果。
