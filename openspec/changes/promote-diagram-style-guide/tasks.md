## 1. OpenSpec Setup

- [x] 1.1 Create the `promote-diagram-style-guide` OpenSpec change.
- [x] 1.2 Define scope, non-goals, fact boundaries, rollout rhythm, and validation requirements.
- [x] 1.3 Add a spec delta for promoted SVG teaching diagram rules.

## 2. Long-Term Style Guide

- [x] 2.1 Add `docs/diagram-style-guide.md`.
- [x] 2.2 Define Mermaid vs SVG division of labor.
- [x] 2.3 Record SVG source rules: Chinese-first, hand-written, diffable, no external generation dependency, no image-generation model as final fact diagram source.
- [x] 2.4 Define required title, legend, description / `<desc>`, and semantic markers.
- [x] 2.5 Define 12-chapter SVG coverage planning.
- [x] 2.6 Define rollout batches and high-risk chapter boundaries.

## 3. Low-Risk Pilot

- [x] 3.1 Add a scoped s04 SVG under `chapters/s04_shell_sandbox_permissions/diagrams/`.
- [x] 3.2 Add a companion note that records source inputs, event mapping, fact boundary, and manual QA.
- [x] 3.3 Update s04 README with a short optional SVG entry without replacing `diagram.mmd`.

## 4. Navigation

- [x] 4.1 Update root README navigation to point to `docs/diagram-style-guide.md`.
- [x] 4.2 Update roadmap navigation to point to the style guide and current s04 pilot.

## 5. Validation

- [x] 5.1 Run `openspec validate promote-diagram-style-guide --strict`.
- [x] 5.2 Run `python3 scripts/check_docs.py`.
- [x] 5.3 Run `python3 scripts/run_all.py`.
- [x] 5.4 Run `python3 -m unittest discover -s tests`.
- [x] 5.5 Run `git diff --check`.
- [x] 5.6 Confirm `docs/fact-snapshot.md`, `docs/source-evidence.md`, chapter statuses, and `scripts/check_docs.py` were not modified.
