## Why

`design-integrated-teaching-mock-phase7` 已经定义了 Phase 7 integrated teaching mock 的边界：它应把 agent loop、tool dispatch、permission decision、context pressure、instruction conflict、session trace / recovery 和 failure recovery 串成一个可运行、可读 trace 的教学体验。

当前 s12 只有轻量 happy/failure 总览，不能让 AI 产品经理看到这些机制在同一条链路中如何互相影响。实现阶段需要把设计落到 deterministic、offline、Python 标准库 mock，同时继续保留“教学抽象，不代表 OpenAI Codex 官方实现或 Codex 桌面端实现”的事实边界。

## What Changes

- 新增 `implement-integrated-teaching-mock-phase7` OpenSpec change。
- 增强 `chapters/s12_comprehensive_architecture/mock.py`，让它承载 Phase 7 integrated teaching mock。
- 保留现有 CLI 兼容性：
  - `--demo --path happy`
  - `--demo --path failure`
  - `--trace-json`
- 新增更细的教学场景，覆盖：
  - happy path
  - tool dispatch failure
  - permission denied
  - context pressure
  - instruction conflict
  - session recovery
- 扩展共享 mock runtime 时，只增加向后兼容能力，不破坏其他章节。
- 更新 s12 README，说明新增场景、教学边界和 s08/s10 `待核实` 限制。
- 增加测试，断言输出稳定、免责声明存在、关键场景可运行、s08/s10 待核实边界未被升级。

## Capabilities

### New Capabilities

- 无。

### Modified Capabilities

- `integrated-teaching-mock-phase7`: 从设计约束推进到可运行的 integrated teaching mock 和测试验收。

## Impact

- 影响 `chapters/s12_comprehensive_architecture/mock.py` 和 README。
- 可能影响 `src/learn_codex_mock/runtime.py`，仅用于向后兼容地支持额外教学场景。
- 影响测试文件，增加 s12 integrated mock 场景覆盖。
- 不调用 OpenAI API，不依赖网络、Keychain、外部 CLI 或真实桌面端状态。
- 不升级 s08/s10 的章节状态；session/thread/skills/MCP 相关内容继续标注为 `待核实` 或 `教学抽象`。
- 不新增第三方依赖，不改变其他章节默认 happy/failure contract。
