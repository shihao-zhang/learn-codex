## 1. OpenSpec Setup

- [x] 1.1 Create a focused Phase 5 s10 OpenSpec proposal, design, spec, and task list.
- [x] 1.2 Validate the change with `openspec validate verify-s10-extensions-mcp-skills-phase5 --strict`.

## 2. Source Reading

- [x] 2.1 Read fixed SHA evidence for MCP handler behavior and registry integration.
- [x] 2.2 Read fixed SHA evidence for extension tool adapter behavior and dynamic tool exposure.
- [x] 2.3 Read fixed SHA evidence for skills crate installation, session skills instructions, and any CLI/config entry points.
- [x] 2.4 Read official README or CLI help evidence for user-visible MCP/extensions/skills entry points where available.

## 3. Documentation Updates

- [x] 3.1 Update `docs/source-evidence.md` s10 entries with refined evidence, scope, and unresolved questions.
- [x] 3.2 Update `chapters/s10_extensions_mcp_skills/README.md` only if boundary language needs to be narrowed.
- [x] 3.3 State whether s10 can upgrade or must remain `待核实`, without forcing an upgrade.

## 4. Validation

- [x] 4.1 Run `python3 scripts/check_docs.py`.
- [x] 4.2 Run `python3 scripts/run_all.py`.
- [x] 4.3 Run `python3 -m unittest discover -s tests`.
- [x] 4.4 Run `git diff --check`.
- [x] 4.5 Capture validation results and remaining s10 open questions for the final summary.
