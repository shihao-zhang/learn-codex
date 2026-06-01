## 1. OpenSpec Setup

- [x] 1.1 Create `prepare-open-source-review-closeout-p4`.
- [x] 1.2 Define P4 scope, non-goals, active change strategy, and validation requirements.
- [x] 1.3 Add a spec for open-source review closeout.

## 2. Maintenance Closeout

- [x] 2.1 Create `docs/maintenance-closeout.md`.
- [x] 2.2 Summarize completed work since the roadmap change.
- [x] 2.3 List active OpenSpec changes and review/archival strategy.
- [x] 2.4 Record fact boundaries, unchanged chapter statuses, and remaining risks.
- [x] 2.5 Provide a PR/review summary draft.

## 3. Navigation And Checklist

- [x] 3.1 Update `docs/roadmap.md` to mark P4 complete.
- [x] 3.2 Update `docs/review-checklist.md` with PR / release closeout checks.

## 4. Validation

- [x] 4.1 Run `openspec validate prepare-open-source-review-closeout-p4 --strict`.
- [x] 4.2 Run `python3 scripts/check_docs.py`.
- [x] 4.3 Run `python3 scripts/run_all.py`.
- [x] 4.4 Run `python3 -m unittest discover -s tests`.
- [x] 4.5 Run `git diff --check`.

Validation result:

- `openspec validate prepare-open-source-review-closeout-p4 --strict`: passed.
- `python3 scripts/check_docs.py`: passed.
- `python3 scripts/run_all.py`: passed, 24 paths / 94 events.
- `python3 -m unittest discover -s tests`: passed, 13 tests.
- `git diff --check`: passed.
