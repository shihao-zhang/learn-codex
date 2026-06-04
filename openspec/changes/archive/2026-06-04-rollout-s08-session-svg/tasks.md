## 1. OpenSpec Setup

- [x] 1.1 Create the `rollout-s08-session-svg` OpenSpec change.
- [x] 1.2 Define scope, non-goals, fact boundaries, source inputs, and validation requirements.
- [x] 1.3 Add a spec delta for s08 SVG rollout rules.

## 2. Source Review

- [x] 2.1 Re-read `AGENTS.md`.
- [x] 2.2 Review `docs/diagram-style-guide.md`.
- [x] 2.3 Review s08 README, Mermaid diagram, mock, and existing source evidence entries.
- [x] 2.4 Review previous SVG rollout structure for file organization and companion notes.

## 3. s08 Session SVG

- [x] 3.1 Add `s08_sessions_threads_rollout` optional SVG and companion Markdown.
- [x] 3.2 Explicitly mark remote thread-store backend as `待核实`.
- [x] 3.3 Explicitly mark Codex Cloud/desktop recovery semantics as `待核实`.
- [x] 3.4 Explicitly mark experimental app-server API stability as `待核实`.
- [x] 3.5 Confirm resume/fork are not drawn as official stable product capabilities.
- [x] 3.6 Confirm SVG is hand-written, XML-parseable, Chinese-first, diffable, and includes `<title>`, `<desc>`, and visible legend or boundary note.
- [x] 3.7 Render or preview the SVG and fix visual readability issues before finalizing.

## 4. Chapter Navigation

- [x] 4.1 Update s08 README with a short optional SVG entry without replacing `diagram.mmd`.
- [x] 4.2 Confirm s08 status remains `待核实`.
- [x] 4.3 Confirm no root README, roadmap, diagram style guide, fact snapshot, source evidence, or check script changed.

## 5. Validation

- [x] 5.1 Run `openspec validate rollout-s08-session-svg --strict`.
- [x] 5.2 Run `openspec validate --all --strict`.
- [x] 5.3 Run XML parse checks for the newly added SVG file.
- [x] 5.4 Run `python3 scripts/check_docs.py`.
- [x] 5.5 Run `python3 scripts/run_all.py`.
- [x] 5.6 Run `python3 -m unittest discover -s tests`.
- [x] 5.7 Run `git diff --check`.
- [x] 5.8 Review final diff and commit without pushing.
