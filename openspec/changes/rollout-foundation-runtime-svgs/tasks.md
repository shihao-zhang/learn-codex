## 1. OpenSpec Setup

- [x] 1.1 Create the `rollout-foundation-runtime-svgs` OpenSpec change.
- [x] 1.2 Define scope, non-goals, fact boundaries, source inputs, and validation requirements.
- [x] 1.3 Add a spec delta for foundation runtime SVG rollout rules.

## 2. Source Review

- [x] 2.1 Re-read `AGENTS.md`.
- [x] 2.2 Review `docs/diagram-style-guide.md`.
- [x] 2.3 Review the s04 SVG pilot and companion note.
- [x] 2.4 Review s01-s03 README, Mermaid diagrams, mocks, and existing source evidence entries.

## 3. Foundation Runtime SVGs

- [x] 3.1 Add `s01_agent_loop` optional SVG and companion Markdown.
- [x] 3.2 Add `s02_protocol_events` optional SVG and companion Markdown.
- [x] 3.3 Add `s03_tool_registry_dispatch` optional SVG and companion Markdown.
- [x] 3.4 Confirm every SVG is hand-written, XML-parseable, Chinese-first, diffable, and includes `<title>`, `<desc>`, and visible legend or boundary note.

## 4. Chapter Navigation

- [x] 4.1 Update s01 README with a short optional SVG entry without replacing `diagram.mmd`.
- [x] 4.2 Update s02 README with a short optional SVG entry without replacing `diagram.mmd`.
- [x] 4.3 Update s03 README with a short optional SVG entry without replacing `diagram.mmd`.
- [x] 4.4 Confirm no official facts, chapter statuses, fact snapshot entries, source evidence entries, or check scripts changed.

## 5. Validation

- [x] 5.1 Run `openspec validate rollout-foundation-runtime-svgs --strict`.
- [x] 5.2 Run `python3 scripts/check_docs.py`.
- [x] 5.3 Run `python3 scripts/run_all.py`.
- [x] 5.4 Run `python3 -m unittest discover -s tests`.
- [x] 5.5 Run `git diff --check`.
- [x] 5.6 Review final diff and commit without pushing.
