## 1. OpenSpec Setup

- [x] 1.1 Create the `rollout-subagents-svg` OpenSpec change.
- [x] 1.2 Define scope, non-goals, source inputs, fact boundaries, drawing rules, and validation requirements.
- [x] 1.3 Add a spec delta for the s11 subagents SVG rollout rules.

## 2. Source Review

- [x] 2.1 Re-read `AGENTS.md`.
- [x] 2.2 Review `docs/diagram-style-guide.md`.
- [x] 2.3 Review s11 README, Mermaid diagram, mock, and existing source evidence entries.
- [x] 2.4 Review relevant OpenSpec boundary specs for pending chapters and s11 scope clarification.

## 3. s11 SVG

- [x] 3.1 Add `s11_subagents_parallel_jobs` optional SVG covering delegate, parent/child events, approval forwarding, parallel job, and result merge.
- [x] 3.2 Add companion Markdown with `Source Inputs`, `Event / Mechanism Mapping`, `Fact Boundary`, and `Manual QA`.
- [x] 3.3 Confirm the SVG is hand-written, XML-parseable, Chinese-first, diffable, and includes `<title>`, `<desc>`, and visible legend or boundary note.
- [x] 3.4 Render or preview the SVG and fix visual readability issues before finalizing.

## 4. Chapter Navigation

- [x] 4.1 Update s11 README with a short optional SVG entry without replacing `diagram.mmd`.
- [x] 4.2 Confirm no repository README, roadmap, style guide, evidence files, check scripts, or chapter statuses changed.

## 5. Validation

- [x] 5.1 Run `openspec validate rollout-subagents-svg --strict`.
- [x] 5.2 Run `openspec validate --all --strict`.
- [x] 5.3 Run XML parse checks for the newly added SVG file.
- [x] 5.4 Run `python3 scripts/check_docs.py`.
- [x] 5.5 Run `python3 scripts/run_all.py`.
- [x] 5.6 Run `python3 -m unittest discover -s tests`.
- [x] 5.7 Run `git diff --check`.
- [x] 5.8 Review final diff and commit without pushing.
