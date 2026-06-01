## 1. OpenSpec Scope

- [x] 1.1 Create the `verify-s08-sessions-rollout-phase5` OpenSpec change.
- [x] 1.2 Define the s08-only scope, conservative status rule, and validation requirements.

## 2. Source Verification

- [x] 2.1 Read fixed SHA OpenAI source for s08 app-server resume/fork, thread-store, rollout, and CLI resume boundaries.
- [x] 2.2 Update `docs/source-evidence.md` with s08 evidence and unresolved scope notes.
- [x] 2.3 Update `chapters/s08_sessions_threads_rollout/README.md` only where conservative wording or checklist state needs adjustment.
- [x] 2.4 Decide whether s08 can upgrade status; default to `待核实` unless the chain is fully closed.

## 3. Validation

- [x] 3.1 Run `openspec validate verify-s08-sessions-rollout-phase5 --strict`.
- [x] 3.2 Run `python3 scripts/check_docs.py`.
- [x] 3.3 Run `python3 scripts/run_all.py`.
- [x] 3.4 Run `python3 -m unittest discover -s tests`.
- [x] 3.5 Run `git diff --check`.
