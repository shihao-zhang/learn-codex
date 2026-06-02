## Context

s10 的风险不在于没有源码线索，而在于线索来自多个层次：MCP handler、extension tool adapter、skills crate、session skills instructions、tool registry 和 CLI 文档/入口。它们可能共同进入模型可见工具面，也可能只是内部机制或实验能力。

本轮核验必须把“代码能打开”“机制存在”“CLI 用户可见能力”“官方文档承诺”分开记录。

## Verification Approach

1. 固定证据边界：继续使用 `docs/fact-snapshot.md` 中的目标 commit `740d942f901a5a63421298c74dafbeb4255e946d`，新增链接必须是固定 SHA permalink。
2. 源码优先级：
   - 先读 tool registry 和 session 初始上下文中如何组装 MCP、extension tools、dynamic tools、available skills instructions。
   - 再读 CLI README、CLI 参数/配置入口和相关 protocol/config 类型，确认是否存在用户可见入口。
   - 最后只把能被源码或官方 README/release note 支撑的机制写入证据。
3. 状态判断：
   - 如果只能证明 `skills` crate 写入 system skills 或 session 构造 instructions，则保持 `待核实`。
   - 如果能证明 CLI 用户如何配置、触发并观察 skills，且证据来自固定 SHA 源码或官方文档，才考虑升级。
4. 文档收敛：
   - `docs/source-evidence.md` 记录机制点、证据级别、已核实范围和未解决问题。
   - 章节 README 只写读者需要的边界语言，不堆源码路径。

## Non-Goals

- 不研究 s08、s09、s11 的新事实。
- 不把 Claude Code skills、Codex 桌面端插件体验、Browser/Chrome 插件或本 session tools 写成 `openai/codex` 事实。
- 不因为 `skills`、`extensions` 或 `mcp` 字样出现在路径中就断言产品能力。
- 不更新目标 commit，不追踪最新 release 变化，除非发现现有官方文档引用已经阻塞本轮核验。

## Review and Validation

完成后运行：

```bash
python3 scripts/check_docs.py
python3 scripts/run_all.py
python3 -m unittest discover -s tests
git diff --check
openspec validate verify-s10-extensions-mcp-skills-phase5 --strict
```

最终说明必须包含：新增/修改的 s10 证据、是否修改章节 README、是否能升级状态，以及仍然待核实的问题。
