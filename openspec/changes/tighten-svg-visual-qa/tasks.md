## 1. OpenSpec Setup

- [x] 1.1 Create the `tighten-svg-visual-qa` OpenSpec change.
- [x] 1.2 Record visual QA findings, scope, non-goals, and validation requirements.
- [x] 1.3 Add a spec delta for rendered SVG visual QA.

## 2. Visual Verification

- [x] 2.1 Render s01 and s02 SVGs to PNG.
- [x] 2.2 Confirm s01 information hierarchy is unclear.
- [x] 2.3 Confirm s02 modules overlap.

## 3. SVG Fixes

- [x] 3.1 Revise s01 `turn-loop.svg` to make the FACT main path visually primary.
- [x] 3.2 Revise s02 `event-interface.svg` to eliminate module overlap.
- [x] 3.3 Update s01/s02 companion Manual QA with rendered visual checks.

## 4. Norms

- [x] 4.1 Update `docs/diagram-style-guide.md` with rendered visual QA rules.
- [x] 4.2 Keep the new rules focused on durable agent decisions, not one-off postmortem detail.

## 5. Validation

- [x] 5.1 Run `openspec validate tighten-svg-visual-qa --strict`.
- [x] 5.2 Run XML parse checks for affected SVGs.
- [x] 5.3 Render affected SVGs again and visually verify layout.
- [x] 5.4 Run `python3 scripts/check_docs.py`.
- [x] 5.5 Run `python3 scripts/run_all.py`.
- [x] 5.6 Run `python3 -m unittest discover -s tests`.
- [x] 5.7 Run `git diff --check`.
- [x] 5.8 Commit without pushing.
