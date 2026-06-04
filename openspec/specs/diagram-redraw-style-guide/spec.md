# diagram-redraw-style-guide Specification

## Purpose

定义本仓教学图的长期边界：Mermaid 保持为章节主机制图，SVG 作为可选教学辅助图，用手写、可审查、中文优先的方式解释路径、边界、失败、恢复和 trace，同时不把教学表达升级为 `openai/codex` 官方事实。
## Requirements
### Requirement: Diagram rollout remains OpenSpec-governed and incremental

Diagram redraw and SVG rollout work SHALL use OpenSpec before changing long-term diagram rules or adding batches of chapter SVGs.

#### Scenario: Diagram rules change

- **WHEN** diagram style rules, fact boundaries, validation criteria, or rollout rhythm change
- **THEN** the change defines scope, non-goals, visual rules, fact boundaries, and validation checks in OpenSpec before implementation

#### Scenario: Bulk redraw is proposed

- **WHEN** future diagram work expands beyond a small pilot or batch
- **THEN** it is split into reviewed increments rather than replacing s01-s12 diagrams in one change

#### Scenario: Pilot or batch is selected

- **WHEN** a new SVG batch is planned
- **THEN** it identifies the chapter set, source inputs, expected teaching value, and high-risk fact boundaries before files are added

### Requirement: Mermaid and SVG have distinct jobs

The repository SHALL keep Mermaid as the primary chapter mechanism diagram format and use SVG only as optional teaching support.

#### Scenario: Chapter gains SVG support

- **WHEN** a chapter gains an SVG teaching diagram
- **THEN** the chapter keeps `diagram.mmd` as the main mechanism diagram
- **AND** the README links the SVG only as optional teaching material

#### Scenario: SVG purpose is constrained

- **WHEN** an SVG is added
- **THEN** it explains paths, boundaries, failures, recovery choices, comparisons, or trace reading
- **AND** it does not replace the chapter's Mermaid structure map or become an official architecture diagram

### Requirement: SVG source is reviewable and dependency-light

SVG teaching diagrams SHALL be hand-written, text-reviewable assets without external generation dependency.

#### Scenario: SVG source is reviewed

- **WHEN** an SVG is added or modified
- **THEN** it is readable text that can be reviewed in git diff
- **AND** it has no external image, font, network, generated bitmap, or export-pipeline dependency

#### Scenario: Image generation is proposed

- **WHEN** a generated image is proposed as the final source for a mechanism or fact diagram
- **THEN** it is rejected for final use
- **AND** any useful idea is manually redrawn into reviewable SVG with explicit fact boundaries

#### Scenario: Alternate drawing method is evaluated

- **WHEN** diagrams become numerous or require reusable layout tokens and export automation
- **THEN** a later OpenSpec change may evaluate HTML/CSS source exported to SVG/PNG

### Requirement: SVG diagrams are Chinese-first and accessible

SVG teaching diagrams SHALL use Chinese as the primary reader-facing language and include minimum accessibility metadata.

#### Scenario: Chinese reader scans the diagram

- **WHEN** the visible title, node labels, explanations, legend, notes, and boundary text are rendered
- **THEN** Chinese is the primary reader-facing language
- **AND** English identifiers remain only as secondary traceability chips for commands, paths, schema fields, or mock event kinds

#### Scenario: SVG file is opened

- **WHEN** the SVG is viewed or reviewed as source
- **THEN** it includes a clear `<title>`
- **AND** it includes a useful `<desc>` explaining scope and non-official boundary
- **AND** the visible diagram includes a legend or boundary note

### Requirement: SVG diagrams preserve semantic fact boundaries

Every SVG teaching diagram SHALL visually distinguish official facts, pending semantics, teaching abstractions, failure/deny paths, and recovery choices when those semantics appear.

#### Scenario: Official fact appears

- **WHEN** a node or edge is marked `FACT`
- **THEN** it can be traced to fixed SHA OpenAI source evidence, official OpenAI documentation, a release note, or `docs/source-evidence.md`

#### Scenario: Pending semantics appear

- **WHEN** a diagram references s08, s10, or another unresolved mechanism
- **THEN** the relevant node or edge is marked `待核实`
- **AND** the diagram does not present it as stable official capability

#### Scenario: Teaching abstraction appears

- **WHEN** a diagram shows mock trace fields, simplified budgets, teaching checkpoints, synthetic examples, UI suggestions, or cross-chapter explanation
- **THEN** it is marked `TEACHING` or `教学辅助`
- **AND** it does not claim equivalence to OpenAI Codex official behavior

#### Scenario: Failure or recovery is shown

- **WHEN** a diagram depicts a blocked, denied, skipped, failed, or recoverable action
- **THEN** it marks the reason with `FAIL` or `DENY` where appropriate
- **AND** any safe next step is marked `RECOVERY` or `恢复选择`

### Requirement: Failure paths are readable and side effects are explicit

SVG diagrams SHALL make failure, denial, and recovery paths understandable to product readers without implying unsafe side effects ran.

#### Scenario: Failure path is drawn

- **WHEN** a diagram depicts missing handler, schema drift, context pressure, instruction conflict, permission denial, or recovery stop
- **THEN** it labels the failure point, decision reason, and user-visible recovery choice

#### Scenario: Side effects are avoided

- **WHEN** a failure or denial path prevents an action from running
- **THEN** the diagram explicitly marks the handler, command, or side effect as not invoked, skipped, denied, or requiring human authorization

### Requirement: SVG companion notes record review inputs

SVG diagrams that use fact markers, mock traces, or pending semantics SHALL have companion Markdown notes.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens a companion Markdown file
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

#### Scenario: File organization is checked

- **WHEN** a chapter SVG is added
- **THEN** it lives under `chapters/<chapter>/diagrams/`
- **AND** its companion Markdown lives in the same directory
- **AND** chapter README navigation remains a short optional entry

### Requirement: Chapter SVG coverage is planned before broad rollout

The repository SHALL maintain chapter SVG coverage planning while keeping high-risk chapters explicitly bounded.

#### Scenario: Coverage plan is reviewed

- **WHEN** a maintainer reviews `docs/diagram-style-guide.md`
- **THEN** it lists the planned core SVG direction for all 12 chapters
- **AND** it identifies high-risk chapters whose diagrams require explicit pending or teaching markers

#### Scenario: Foundation runtime batch is implemented

- **WHEN** the foundation runtime SVG batch is implemented
- **THEN** s01, s02, and s03 each gain one scoped SVG under the chapter `diagrams/` directory
- **AND** each SVG has a companion Markdown note in the same directory
- **AND** each README continues to present `diagram.mmd` as the main mechanism diagram

#### Scenario: Future batches are planned

- **WHEN** later changes add SVGs to more chapters
- **THEN** they follow the documented batch rhythm: foundation runtime, tools and permissions, context and instructions, sessions and extensions, then comprehensive architecture

#### Scenario: High-risk chapters are drawn

- **WHEN** s08 or s10 gains SVG teaching material
- **THEN** the SVG visibly marks unresolved semantics as `待核实`
- **AND** it avoids drawing them as official stable capabilities

#### Scenario: s12 is drawn

- **WHEN** s12 gains new or revised SVG material
- **THEN** it remains marked as `教学抽象`
- **AND** any s08/s10-related edge keeps `待核实` chips where relevant

### Requirement: Foundation SVGs preserve chapter-specific fact boundaries

Foundation runtime SVGs SHALL distinguish registered mechanism facts from teaching simplifications and examples.

#### Scenario: s01 loop diagram marks facts

- **WHEN** the s01 SVG depicts the turn loop, tool call routing, observation 回填, or conversation item recording
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** simplified sequencing, mock events, example tool names, and recovery wording are marked `TEACHING` or `教学辅助`

#### Scenario: s02 protocol diagram marks facts

- **WHEN** the s02 SVG depicts protocol events, response/input items, or trace context
- **THEN** only registered protocol mechanism entries are marked `FACT`
- **AND** UI state, product display suggestions, event names from mock, schema drift examples, and compatibility advice are marked `TEACHING` or `教学辅助`

#### Scenario: s03 tool dispatch diagram marks facts

- **WHEN** the s03 SVG depicts model-visible specs, registry, router, handler execution, or result 回写
- **THEN** only registered router/registry/dispatch mechanism entries are marked `FACT`
- **AND** example tool names, simplified parameters, mock handler names, and product explanations are marked `TEACHING` or `教学辅助`

### Requirement: Rendered SVG visual QA is required

The repository SHALL visually verify high-value SVG teaching diagrams after rendering, not only by inspecting source XML.

#### Scenario: SVG is ready for review

- **WHEN** a chapter SVG is added or materially revised
- **THEN** the maintainer renders it to an image or browser preview
- **AND** verifies that the main path, side paths, text, chips, arrows, and legend are readable

#### Scenario: Main path hierarchy is checked

- **WHEN** a diagram contains both verified mechanism facts and teaching failure or recovery paths
- **THEN** the verified mechanism path is visually primary
- **AND** teaching paths, trace examples, and legend content are visually secondary

#### Scenario: Overlap is checked

- **WHEN** a rendered SVG is inspected
- **THEN** cards, labels, chips, arrows, and legend blocks do not overlap or obscure each other
- **AND** connector lines do not pass through reader-facing text

#### Scenario: Dense diagram is simplified

- **WHEN** a diagram becomes visually dense enough that the first reading path is unclear
- **THEN** the diagram is reorganized into separate layers such as main path, side explanation, and legend
- **AND** nonessential chips or copy are reduced before adding more visual elements

### Requirement: Diagram changes pass validation without evidence drift

Diagram style guide and SVG rollout changes SHALL pass repository checks without modifying fact snapshot, source evidence, check scripts, or chapter statuses unless a separate approved change explicitly covers that work.

#### Scenario: Change is ready

- **WHEN** diagram style, SVG rollout, archive, or material SVG revision work is complete
- **THEN** the maintainer runs the relevant `openspec validate ... --strict` command
- **AND** runs `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`

#### Scenario: Fact boundary is protected

- **WHEN** SVG or diagram style work is committed
- **THEN** `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and s08/s10/s12 statuses remain unchanged unless the OpenSpec change explicitly requires those files or statuses to change

### Requirement: Context and instruction SVG rollout

The repository SHALL add optional SVG teaching support for the context and instruction batch without replacing existing Mermaid mechanism diagrams.

#### Scenario: Context and instruction batch is implemented

- **WHEN** `rollout-context-instruction-svgs` is implemented
- **THEN** s05 and s06 each gain one scoped SVG under the chapter `diagrams/` directory
- **AND** each SVG has a companion Markdown note in the same directory

#### Scenario: Mermaid remains primary

- **WHEN** s05 or s06 README is updated
- **THEN** the chapter continues to present `diagram.mmd` as the main mechanism diagram
- **AND** the SVG is linked only as optional teaching support

### Requirement: Context SVG preserves compaction fact boundaries

The s05 SVG SHALL distinguish verified compaction entry points from teaching simplifications about pressure, thresholds, preservation, summary quality, and recovery.

#### Scenario: s05 diagram marks facts

- **WHEN** the s05 SVG depicts compact entry points, compacted history replacement, rollout recording, or truncation helper evidence
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** fixed token thresholds, context pressure examples, preserved field lists, summary quality risks, mock trace events, and recovery wording are marked `TEACHING` or `教学辅助`

#### Scenario: s05 diagram shows loss or recovery

- **WHEN** the s05 SVG depicts summary loss, truncation, or missing constraints
- **THEN** the loss point is visually marked as `FAIL` or risk
- **AND** the safe next step is marked `RECOVERY` or `恢复选择`
- **AND** the diagram does not claim compaction is lossless memory

### Requirement: Instruction SVG preserves hierarchy fact boundaries

The s06 SVG SHALL distinguish verified instruction source and injection paths from teaching examples about priority, conflict handling, authorization, and product copy.

#### Scenario: s06 diagram marks facts

- **WHEN** the s06 SVG depicts `AGENTS.md` discovery, project/user instruction composition, or initial context instruction injection
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** conflict examples, priority visualization, authorization copy, project constraint examples, and mock trace events are marked `TEACHING` or `教学辅助`

#### Scenario: s06 diagram shows conflict

- **WHEN** the s06 SVG depicts a user request conflicting with higher-priority or project-scoped rules
- **THEN** the conflict point is visually marked as `FAIL`, `DENY`, or conflict
- **AND** the safe next step is marked `RECOVERY` or `恢复选择`
- **AND** the diagram does not reveal or invent private prompt text or an unverified priority algorithm

### Requirement: Context and instruction companion notes

Each context and instruction SVG SHALL include a companion Markdown note that records review inputs and human QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens a companion Markdown file for s05 or s06
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

### Requirement: Context and instruction rollout validation

The context and instruction SVG rollout SHALL pass repository checks without modifying evidence files, check scripts, or chapter statuses.

#### Scenario: Change is ready

- **WHEN** the context and instruction SVG rollout is complete
- **THEN** `openspec validate rollout-context-instruction-svgs --strict`, `openspec validate --all --strict`, XML parse checks for newly added SVGs, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, s08/s10/s12 statuses, and s05/s06 statuses remain unchanged

### Requirement: Config and app-server SVG rollout

The repository SHALL add optional SVG teaching support for the s07/s09 rollout without replacing existing Mermaid mechanism diagrams.

#### Scenario: Config and app-server batch is implemented

- **WHEN** `rollout-config-appserver-svgs` is implemented
- **THEN** s07 and s09 each gain one scoped SVG under the chapter `diagrams/` directory
- **AND** each SVG has a companion Markdown note in the same directory

#### Scenario: Mermaid remains primary

- **WHEN** s07 or s09 README is updated
- **THEN** the chapter continues to present `diagram.mmd` as the main mechanism diagram
- **AND** the SVG is linked only as optional teaching support

### Requirement: Config SVG preserves model-choice fact boundaries

The s07 SVG SHALL explain how config, auth, provider, and model choices affect cost, capability, compliance, and availability without turning product guidance into official implementation fact.

#### Scenario: s07 diagram marks facts

- **WHEN** the s07 SVG depicts config type entry points, model preset/model info, or session initialization model selection
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** auth product meaning, account boundaries, provider availability, latest model list, default choices, price/cost interpretation, compliance posture, UI recommendations, and recovery wording are marked `TEACHING` or `教学辅助`

#### Scenario: s07 diagram shows configuration failure

- **WHEN** the s07 SVG depicts missing provider, missing credential, unsupported capability, or unavailable model
- **THEN** the blocked point is visually marked as `FAIL` or risk
- **AND** the safe next step is marked `RECOVERY` or `恢复选择`
- **AND** the diagram does not print, inspect, or imply validation of real credentials

### Requirement: App-server SVG preserves state-sync boundaries

The s09 SVG SHALL distinguish verified app-server/protocol mechanisms from product-surface state synchronization advice.

#### Scenario: s09 diagram marks facts

- **WHEN** the s09 SVG depicts transport connection state, outbound routing, server request callbacks, thread status projection, or schema export
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** product UI surfaces, multi-client behavior, reconnect policy, user-visible status names, Codex Cloud interpretation, and client implementation details are marked `TEACHING` or boundary notes

#### Scenario: s09 diagram shows synchronization boundary

- **WHEN** the s09 SVG depicts runtime events becoming product-visible state
- **THEN** protocol/schema and transport boundaries are visually separated from product-surface interpretation
- **AND** incomplete field-level compatibility or private service behavior is not drawn as stable official capability
- **AND** disconnect or slow-connection examples are marked as risk or recovery teaching paths

### Requirement: Config and app-server companion notes

Each s07/s09 SVG SHALL include a companion Markdown note that records review inputs and human QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens a companion Markdown file for s07 or s09
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

### Requirement: Config and app-server rollout validation

The s07/s09 SVG rollout SHALL pass repository checks without modifying evidence files, check scripts, chapter statuses, root README, roadmap, or the diagram style guide.

#### Scenario: Change is ready

- **WHEN** the config and app-server SVG rollout is complete
- **THEN** `openspec validate rollout-config-appserver-svgs --strict`, `openspec validate --all --strict`, XML parse checks for newly added SVGs, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** `README.md`, `docs/roadmap.md`, `docs/diagram-style-guide.md`, `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and all chapter statuses remain unchanged

### Requirement: s11 subagents SVG rollout

The repository SHALL add optional SVG teaching support for s11 without replacing the existing Mermaid mechanism diagram or changing chapter status.

#### Scenario: s11 SVG is implemented

- **WHEN** `rollout-subagents-svg` is implemented
- **THEN** s11 gains one scoped SVG under the chapter `diagrams/` directory
- **AND** the SVG has a companion Markdown note in the same directory

#### Scenario: Mermaid remains primary

- **WHEN** s11 README is updated
- **THEN** the chapter continues to present `diagram.mmd` as the main mechanism diagram
- **AND** the SVG is linked only as optional teaching support

### Requirement: s11 SVG preserves subagent fact boundaries

The s11 SVG SHALL distinguish registered source mechanisms from unresolved product semantics and teaching simplifications.

#### Scenario: s11 diagram marks facts

- **WHEN** the s11 SVG depicts multi-agent tool surface, `spawn_agent`, `AgentControl`, delegate event forwarding, delegate approval forwarding, agent jobs CSV worker behavior, or ordinary tool-call parallel runtime
- **THEN** only mechanisms already registered in `docs/source-evidence.md` are marked `FACT`
- **AND** result-merge explanations, UI progress suggestions, mock trace events, synthetic examples, and reader guidance are marked `TEACHING` or `教学辅助`

#### Scenario: s11 diagram shows unresolved product semantics

- **WHEN** the s11 SVG mentions default enablement, product entry, multi-agent v1/v2 experience, or complete permission inheritance strategy
- **THEN** those nodes or notes are visibly marked `待核实`
- **AND** the diagram does not present them as stable official capability

#### Scenario: s11 diagram avoids over-generalization

- **WHEN** the s11 SVG shows delegation or parallel job execution
- **THEN** it does not draw s11 as a general official subagent platform
- **AND** it does not present agent jobs as a generic batch-processing API
- **AND** it does not present `tools/parallel.rs` as child-agent parallelism

### Requirement: s11 SVG companion note records boundaries

The s11 SVG SHALL include a companion Markdown note that records review inputs, mapping, fact boundaries, and manual QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens the s11 companion Markdown file
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`
- **AND** it explicitly states that default enablement, product entry, and multi-agent v1/v2 experience remain to be verified

### Requirement: s11 rollout validation

The s11 SVG rollout SHALL pass repository checks without modifying global guide, evidence files, check scripts, or chapter statuses.

#### Scenario: Change is ready

- **WHEN** the s11 SVG rollout is complete
- **THEN** `openspec validate rollout-subagents-svg --strict`, `openspec validate --all --strict`, XML parse checks for the newly added SVG, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** repository README, roadmap, `docs/diagram-style-guide.md`, `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and chapter statuses remain unchanged

### Requirement: s08 session SVG rollout preserves pending boundaries

The repository SHALL add optional SVG teaching support for s08 without replacing the existing Mermaid mechanism diagram or changing the chapter status.

#### Scenario: s08 optional SVG is implemented

- **WHEN** `rollout-s08-session-svg` is implemented
- **THEN** `s08_sessions_threads_rollout` gains one scoped SVG under the chapter `diagrams/` directory
- **AND** the SVG has a companion Markdown note in the same directory
- **AND** the chapter README links the SVG only as optional teaching support
- **AND** `diagram.mmd` remains the main mechanism diagram
- **AND** the s08 status remains `待核实`

### Requirement: s08 SVG marks unresolved recovery and storage semantics

The s08 SVG SHALL visibly mark unresolved recovery, storage, and API stability semantics as `待核实`.

#### Scenario: Remote thread-store backend appears

- **WHEN** the SVG references a remote thread-store backend, non-local persistence, daemon transport, or remote app-server transport as a recovery/storage boundary
- **THEN** the relevant node or edge is marked `待核实`
- **AND** the SVG does not present it as an implemented official backend or stable product capability

#### Scenario: Cloud or desktop recovery semantics appear

- **WHEN** the SVG references Codex Cloud, Codex desktop, cross-client recovery, or desktop resume semantics
- **THEN** the relevant node or edge is marked `待核实`
- **AND** the SVG does not infer official product behavior from desktop observations or teaching mocks

#### Scenario: Experimental API stability appears

- **WHEN** the SVG references `thread/resume`, `thread/fork`, app-server v2, or experimental app-server API stability
- **THEN** the relevant node or edge is marked `待核实`
- **AND** the SVG does not claim a stable public API commitment

### Requirement: s08 SVG distinguishes teaching relationships from product promises

The s08 SVG SHALL explain session/thread/rollout/resume/fork as a teaching relationship while avoiding official recovery-product claims.

#### Scenario: Teaching relationship is drawn

- **WHEN** the SVG depicts session, thread, rollout, resume, or fork
- **THEN** the diagram labels the relationship as teaching support or `局部源码证据` with pending chapter boundary
- **AND** it avoids drawing resume/fork as a guaranteed official recovery path

#### Scenario: Local facts are shown

- **WHEN** the SVG marks a node or edge as `FACT`
- **THEN** the label is scoped as local or `局部` evidence only
- **AND** it can be traced to fixed SHA evidence already registered in `docs/source-evidence.md`
- **AND** it does not upgrade the s08 chapter status

### Requirement: s08 companion note records review inputs and boundaries

The s08 SVG SHALL include a companion Markdown note that records review inputs, mechanism mapping, fact boundaries, and human QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens `chapters/s08_sessions_threads_rollout/diagrams/session-thread-rollout.md`
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

### Requirement: s08 SVG rollout validation

The s08 SVG rollout SHALL pass repository checks without modifying evidence files, check scripts, root navigation, or chapter status.

#### Scenario: Change is ready

- **WHEN** the s08 SVG rollout is complete
- **THEN** `openspec validate rollout-s08-session-svg --strict`, `openspec validate --all --strict`, XML parse checks for the new SVG, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** root README, roadmap, `docs/diagram-style-guide.md`, `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and the s08 status remain unchanged

### Requirement: s10 extension SVG rollout

The repository SHALL add optional SVG teaching support for s10 without replacing the existing Mermaid mechanism diagram or changing the chapter status.

#### Scenario: s10 diagram is implemented

- **WHEN** `rollout-s10-extension-svg` is implemented
- **THEN** `s10_extensions_mcp_skills` gains one scoped SVG under the chapter `diagrams/` directory
- **AND** the SVG has a companion Markdown note in the same directory
- **AND** the chapter status remains `待核实`

#### Scenario: Mermaid remains primary

- **WHEN** s10 README is updated
- **THEN** the chapter continues to present `diagram.mmd` as the main mechanism diagram
- **AND** the SVG is linked only as optional teaching support

### Requirement: s10 SVG preserves separate capability paths

The s10 SVG SHALL keep MCP, dynamic tools, extension tools, and skills as separate capability lines unless a fixed SHA official source proves a shared official mechanism.

#### Scenario: Four lines are drawn

- **WHEN** the s10 SVG depicts extension-like capabilities
- **THEN** it shows MCP, dynamic tools, extension tools, and skills as separate paths
- **AND** it does not merge them into one official extension product promise

#### Scenario: Facts are marked

- **WHEN** the s10 SVG marks a node or edge as `FACT`
- **THEN** that claim is limited to mechanisms already registered in `docs/source-evidence.md`
- **AND** the diagram does not use `FACT` to prove cross-client semantics, marketplace behavior, or unified governance

### Requirement: s10 SVG marks unresolved boundaries

The s10 SVG SHALL explicitly mark high-risk unresolved boundaries as `待核实`.

#### Scenario: dynamic tools are shown

- **WHEN** dynamic tools appear in the s10 SVG
- **THEN** the diagram labels `thread/start.dynamicTools` as experimental or pending
- **AND** it does not present dynamic tools as a stable CLI user-created tool entry

#### Scenario: extension tools are shown

- **WHEN** extension tools appear in the s10 SVG
- **THEN** the diagram labels the generic extension user install, discovery, authorization, or marketplace-style entry as `待核实`
- **AND** it only marks built-in app-server extension and runtime adapter evidence as verified when supported by registered evidence

#### Scenario: governance is shown

- **WHEN** the s10 SVG depicts governance across MCP, dynamic tools, extension tools, and skills
- **THEN** it labels any shared or unified governance path as `待核实`
- **AND** it preserves separate per-path governance notes instead of drawing one proven common policy pipeline

### Requirement: s10 SVG companion note records review inputs

The s10 SVG SHALL include a companion Markdown note that records source inputs, mapping, fact boundaries, and manual QA.

#### Scenario: Companion note is reviewed

- **WHEN** a reviewer opens the s10 companion Markdown file
- **THEN** it includes `Source Inputs`
- **AND** it includes `Event / Mechanism Mapping`
- **AND** it includes `Fact Boundary`
- **AND** it includes `Manual QA`

### Requirement: s10 SVG rollout validation

The s10 SVG rollout SHALL pass repository checks without modifying evidence files, check scripts, root navigation, roadmap, style guide, or chapter statuses.

#### Scenario: Change is ready

- **WHEN** the s10 SVG rollout is complete
- **THEN** `openspec validate rollout-s10-extension-svg --strict`, `openspec validate --all --strict`, XML parse checks for the newly added SVG, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check` pass
- **AND** root `README.md`, `docs/roadmap.md`, `docs/diagram-style-guide.md`, `docs/fact-snapshot.md`, `docs/source-evidence.md`, `scripts/check_docs.py`, and chapter statuses remain unchanged

### Requirement: 全仓 SVG 视觉一致性 QA

全仓章节 SVG 完成较大范围 rollout 后，仓库 SHALL 把这些教学辅助图作为一组材料做视觉一致性审计，保持可读性和语义边界一致，不改变事实状态。

#### Scenario: 审计全量 SVG 集合

- **WHEN** `audit-svg-visual-consistency` 实施完成
- **THEN** 每个 `chapters/*/diagrams/*.svg` 文件都完成 XML parse
- **AND** 每张章节 SVG 都在验收前完成渲染或预览
- **AND** 审计记录文字遮挡、箭头压字、主路径层级、图例权重和语义标记一致性是否已检查

#### Scenario: 跨章节比较语义标记

- **WHEN** 渲染后的 SVG 集合被 review
- **THEN** 对已出现的 `FACT`、`待核实`、`TEACHING` 或 `教学辅助`、`FAIL`、`DENY` 和 `RECOVERY` 标记检查语义和视觉处理是否一致
- **AND** 不用标记文案新增官方事实或升级未闭环语义

#### Scenario: 高风险章节边界保持显式

- **WHEN** s08 或 s10 SVG 纳入全仓审计
- **THEN** 相关未闭环语义继续可见地标为 `待核实`
- **AND** 审计不改变这两个章节状态

#### Scenario: s12 教学抽象保持显式

- **WHEN** s12 SVG 纳入全仓审计
- **THEN** 图中继续可见地标为 `教学抽象`
- **AND** 跨章节解释不被呈现为 OpenAI 官方架构图

#### Scenario: 修复小型视觉问题

- **WHEN** 审计发现小型可读性或标记一致性问题
- **THEN** 维护者可以修改受影响 SVG 和 companion Markdown
- **AND** 修改不触碰 `docs/fact-snapshot.md`、`docs/source-evidence.md`、`scripts/check_docs.py` 或章节状态

#### Scenario: 全仓 SVG 审计可验收

- **WHEN** 审计和必要小修完成
- **THEN** `openspec validate audit-svg-visual-consistency --strict`、`openspec validate --all --strict`、全部章节 SVG 的 XML parse、`python3 scripts/check_docs.py`、`python3 scripts/run_all.py`、`python3 -m unittest discover -s tests` 和 `git diff --check` 均通过
