## 1. OpenSpec Setup

- [x] 1.1 Create the `rollout-context-instruction-svgs` OpenSpec change.
- [x] 1.2 Define scope, non-goals, fact boundaries, source inputs, and validation requirements.
- [x] 1.3 Add a spec delta for context and instruction SVG rollout rules.

## 2. Source Review

- [x] 2.1 Re-read `AGENTS.md`.
- [x] 2.2 Review `docs/diagram-style-guide.md`.
- [x] 2.3 Review the s04 SVG pilot and companion note.
- [x] 2.4 Review s05/s06 README, Mermaid diagrams, mocks, and existing source evidence entries.

## 3. Context and Instruction SVGs

- [x] 3.1 Add `s05_context_window_compaction` optional SVG and companion Markdown.
- [x] 3.2 Add `s06_prompts_instructions` optional SVG and companion Markdown.
- [x] 3.3 Confirm every SVG is hand-written, XML-parseable, Chinese-first, diffable, and includes `<title>`, `<desc>`, and visible legend or boundary note.
- [x] 3.4 Render or preview both SVGs and fix visual readability issues before finalizing.

## 4. Chapter Navigation

- [x] 4.1 Update s05 README with a short optional SVG entry without replacing `diagram.mmd`.
- [x] 4.2 Update s06 README with a short optional SVG entry without replacing `diagram.mmd`.
- [x] 4.3 Confirm no official facts, chapter statuses, fact snapshot entries, source evidence entries, or check scripts changed.

## 5. Validation

- [x] 5.1 Run `openspec validate rollout-context-instruction-svgs --strict`.
- [x] 5.2 Run `openspec validate --all --strict`.
- [x] 5.3 Run XML parse checks for all newly added SVG files.
- [x] 5.4 Run `python3 scripts/check_docs.py`.
- [x] 5.5 Run `python3 scripts/run_all.py`.
- [x] 5.6 Run `python3 -m unittest discover -s tests`.
- [x] 5.7 Run `git diff --check`.
- [x] 5.8 Review final diff and commit without pushing.
