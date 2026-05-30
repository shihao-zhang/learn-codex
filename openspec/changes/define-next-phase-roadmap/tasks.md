## 1. Roadmap Document

- [ ] 1.1 Create `docs/roadmap.md` with Phase 5~9 sequence, purpose, deliverables, acceptance checks, and stop conditions.
- [ ] 1.2 Mark Phase 5 as s08/s10 verification-first work, without forcing status upgrades.
- [ ] 1.3 Add integrated teaching mock planning for loop, tool dispatch, permission decision, context pressure, session trace, and failure recovery.
- [ ] 1.4 Add release-readiness checkpoints for documentation checks, mock checks, unit tests, and review summary.

## 2. Codex Desktop Lens

- [ ] 2.1 Create `docs/codex-desktop-lens.md` that defines desktop experience as an observation lens, not an official source of truth.
- [ ] 2.2 Add an observation-to-question table mapping desktop runtime experiences to source-reading questions and target chapters.
- [ ] 2.3 Add rules for using lens material in chapters and mocks without implying Codex desktop or `openai/codex` equivalence.
- [ ] 2.4 Include failure-path examples such as sandbox denial, external review latency, credential boundary, long-task recovery, and trace readability.

## 3. Project Goal Alignment

- [ ] 3.1 Create a concise project goal document for AI product managers and agent platform designers.
- [ ] 3.2 State non-goals: not official, not a usage manual, not a link index, not a clone of OpenAI implementation.
- [ ] 3.3 Explain harness literacy in product-manager terms: trust, cost, latency, recoverability, user control, and permission friction.
- [ ] 3.4 Recap fact boundaries for official facts, teaching mocks, diagrams, desktop-lens material, and inference.

## 4. README and Navigation

- [ ] 4.1 Link the roadmap, desktop lens, and goal alignment documents from `README.md`.
- [ ] 4.2 Update the README current-stage summary so Phase 3/4 is no longer described as in progress.
- [ ] 4.3 Add a short reader path for people who want to understand the project direction before reading chapters.

## 5. Validation and Review

- [ ] 5.1 Run `python3 scripts/check_docs.py`.
- [ ] 5.2 Run `python3 scripts/run_all.py`.
- [ ] 5.3 Run `python3 -m unittest discover -s tests`.
- [ ] 5.4 Prepare a short human-readable summary listing the new roadmap, the desktop-lens boundary, and the project-goal alignment.
