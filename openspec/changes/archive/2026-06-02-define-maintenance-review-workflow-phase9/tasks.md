## 1. OpenSpec Change

- [x] 1.1 Create `define-maintenance-review-workflow-phase9` with proposal, design, tasks, and spec.
- [x] 1.2 Define maintenance-review workflow requirements for status changes, evidence updates, external review, desktop lens, mock disclaimers, and checks.

## 2. Maintenance Documentation

- [x] 2.1 Create `docs/review-checklist.md`.
- [x] 2.2 Document chapter status upgrade, retention, and downgrade standards.
- [x] 2.3 Document `source-evidence.md` and `fact-snapshot.md` update triggers.
- [x] 2.4 Document Claude review authorization boundaries.
- [x] 2.5 Document Codex Desktop Lens and teaching mock boundaries.
- [x] 2.6 Document pre-submit checks and review summary requirements.

## 3. Navigation

- [x] 3.1 Add a lightweight README link for maintenance and review rules.
- [x] 3.2 Add a lightweight roadmap note for Phase 9 status.

## 4. Validation

- [x] 4.1 Run `openspec validate define-maintenance-review-workflow-phase9 --strict`.
- [x] 4.2 Run `python3 scripts/check_docs.py`.
- [x] 4.3 Run `python3 scripts/run_all.py`.
- [x] 4.4 Run `python3 -m unittest discover -s tests`.
- [x] 4.5 Run `git diff --check`.
