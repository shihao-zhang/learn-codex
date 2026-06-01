## 1. Scope Clarifications

- [x] 1.1 Update README learning map s11 row with mechanism-only scope.
- [x] 1.2 Update s11 README status text to mention v1/v2 experience boundaries.
- [x] 1.3 Update Phase 8 audit permalink count with audit-time wording.

## 2. Validation

- [x] 2.1 Run `openspec validate address-pr-review-scope-clarifications --strict`.
- [x] 2.2 Run `python3 scripts/check_docs.py`.
- [x] 2.3 Run `python3 scripts/run_all.py`.
- [x] 2.4 Run `python3 -m unittest discover -s tests`.
- [x] 2.5 Run `git diff --check`.

Validation result:

- `openspec validate address-pr-review-scope-clarifications --strict`: passed.
- `python3 scripts/check_docs.py`: passed.
- `python3 scripts/run_all.py`: passed, 24 paths / 94 events.
- `python3 -m unittest discover -s tests`: passed, 13 tests.
- `git diff --check`: passed.
