## 1. OpenSpec Setup

- [x] 1.1 Create the `densify-foundation-chapters-phase6` OpenSpec change.
- [x] 1.2 Define scope, non-goals, evidence boundaries, and validation requirements.
- [x] 1.3 Validate the change with `openspec validate densify-foundation-chapters-phase6 --strict`.

## 2. Chapter Densification

- [x] 2.1 Update `chapters/s01_agent_loop/README.md` with PM questions, failure path, mock trace reading guidance, and boundary wording.
- [x] 2.2 Update `chapters/s02_protocol_events/README.md` with PM questions, failure path, mock trace reading guidance, and boundary wording.
- [x] 2.3 Update `chapters/s03_tool_registry_dispatch/README.md` with PM questions, failure path, mock trace reading guidance, and boundary wording.
- [x] 2.4 Update `chapters/s04_shell_sandbox_permissions/README.md` with PM questions, failure path, mock trace reading guidance, and boundary wording.
- [x] 2.5 Update `chapters/s05_context_window_compaction/README.md` with PM questions, failure path, mock trace reading guidance, and boundary wording.
- [x] 2.6 Update `chapters/s06_prompts_instructions/README.md` with PM questions, failure path, mock trace reading guidance, and boundary wording.

## 3. Phase Status And Evidence

- [x] 3.1 Update `README.md` or `docs/roadmap.md` to show Phase 6 progress without changing s08/s10 status.
- [x] 3.2 Update `docs/source-evidence.md` only if new official mechanism claims need registered fixed SHA evidence. No update needed because this change adds teaching/product explanations, not new official mechanism claims.
- [x] 3.3 Record any integrated teaching mock ideas as Phase 7 follow-up questions instead of implementing them.

## 4. Validation

- [x] 4.1 Run `openspec validate densify-foundation-chapters-phase6 --strict`.
- [x] 4.2 Run `python3 scripts/check_docs.py`.
- [x] 4.3 Run `python3 scripts/run_all.py`.
- [x] 4.4 Run `python3 -m unittest discover -s tests`.
- [x] 4.5 Run `git diff --check`.
