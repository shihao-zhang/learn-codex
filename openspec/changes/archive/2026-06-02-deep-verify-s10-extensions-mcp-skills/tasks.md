## 1. OpenSpec Setup

- [x] 1.1 Create focused proposal, design, tasks, and spec for s10 deep verification.
- [x] 1.2 Validate the new change with `openspec validate deep-verify-s10-extensions-mcp-skills --strict`.

## 2. Source Reading

- [x] 2.1 Re-read fixed SHA evidence for MCP entry, config, discovery, exposure, handler, and governance signals.
- [x] 2.2 Re-read fixed SHA evidence for dynamic tools entry/config source, exposure, request/response, and governance signals.
- [x] 2.3 Re-read fixed SHA evidence for extension tools registry, contributors, adapter, exposure, and missing user entry.
- [x] 2.4 Re-read fixed SHA evidence for skills TUI entry, discovery roots, config, instruction injection, and dependency prompts.

## 3. Documentation Updates

- [x] 3.1 Update `docs/source-evidence.md` s10 entries to split MCP, dynamic tools, extension tools, and skills by verified scope.
- [x] 3.2 Update `chapters/s10_extensions_mcp_skills/README.md` to reflect the deep verification result and unresolved questions.
- [x] 3.3 Decide whether s10 can upgrade; if not, keep `待核实` and write the exact non-closed loops.

## 4. Validation

- [x] 4.1 Run `openspec validate deep-verify-s10-extensions-mcp-skills --strict`.
- [x] 4.2 Run `python3 scripts/check_docs.py`.
- [x] 4.3 Run `python3 scripts/run_all.py`.
- [x] 4.4 Run `python3 -m unittest discover -s tests`.
- [x] 4.5 Run `git diff --check`.

Validation result:

- `openspec validate deep-verify-s10-extensions-mcp-skills --strict`: passed.
- `python3 scripts/check_docs.py`: passed after s10 README source links were registered in `docs/fact-snapshot.md`.
- `python3 scripts/run_all.py`: passed.
- `python3 -m unittest discover -s tests`: passed.
- `git diff --check`: passed.
