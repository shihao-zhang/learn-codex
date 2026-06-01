## 1. OpenSpec Setup

- [x] 1.1 Create the `audit-evidence-drift-phase8` OpenSpec change.
- [x] 1.2 Define audit scope, non-goals, source boundaries, and validation requirements.

## 2. Evidence Audit

- [x] 2.1 Check fixed SHA links against the current fact snapshot target commit.
- [x] 2.2 Check README, docs, and s01~s12 README files for over-strong official-fact wording.
- [x] 2.3 Check s08/s10 pending boundaries across roadmap, Phase 5 summary, and chapter README files.
- [x] 2.4 Check s01~s06 Phase 6 additions for teaching/product-boundary labels.
- [x] 2.5 Check whether `docs/source-evidence.md` supports README chapter statuses.
- [x] 2.6 Check whether `docs/review-checklist.md` covers likely maintainer mistakes.

## 3. Documentation

- [x] 3.1 Create `docs/phase8-evidence-audit.md`.
- [x] 3.2 Apply only necessary boundary wording fixes.
- [x] 3.3 Explicitly list no-change, narrowed, still-pending, and follow-up change items.

## 4. Validation

- [x] 4.1 Run `openspec validate audit-evidence-drift-phase8 --strict`.
- [x] 4.2 Run `python3 scripts/check_docs.py`.
- [x] 4.3 Run `python3 scripts/run_all.py`.
- [x] 4.4 Run `python3 -m unittest discover -s tests`.
- [x] 4.5 Run `git diff --check`.
