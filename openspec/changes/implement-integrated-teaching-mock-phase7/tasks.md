## 1. OpenSpec Setup

- [x] 1.1 Create the `implement-integrated-teaching-mock-phase7` OpenSpec change.
- [x] 1.2 Define implementation scope, non-goals, fact boundaries, and validation requirements.
- [x] 1.3 Add a spec for the integrated mock implementation contract.

## 2. Integrated Mock Implementation

- [x] 2.1 Extend the shared teaching mock runtime with backward-compatible scenario support.
- [x] 2.2 Implement the s12 happy path as an integrated loop/tool/permission/context trace.
- [x] 2.3 Implement key failure scenarios: tool dispatch, permission decision, context pressure, instruction conflict, and session recovery.
- [x] 2.4 Keep text and JSON outputs deterministic, offline, and clearly labeled as teaching mock only.

## 3. Documentation And Tests

- [x] 3.1 Update s12 README with the new scenario commands and boundaries.
- [x] 3.2 Add tests for s12 integrated scenarios, disclaimer, deterministic trace, and s08/s10 `待核实` boundaries.
- [x] 3.3 Preserve existing `scripts/run_all.py` and chapter happy/failure compatibility.

## 4. Validation

- [x] 4.1 Run `openspec validate implement-integrated-teaching-mock-phase7 --strict`.
- [x] 4.2 Run `python3 scripts/check_docs.py`.
- [x] 4.3 Run `python3 scripts/run_all.py`.
- [x] 4.4 Run `python3 -m unittest discover -s tests`.
- [x] 4.5 Run `git diff --check`.
