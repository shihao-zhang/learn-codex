## 1. OpenSpec Setup

- [x] 1.1 Create the `rollout-s10-extension-svg` OpenSpec change.
- [x] 1.2 Define scope, non-goals, fact boundaries, source inputs, drawing rules, and validation requirements.
- [x] 1.3 Add a spec delta for s10 SVG rollout rules.

## 2. Source Review

- [x] 2.1 Re-read `AGENTS.md`.
- [x] 2.2 Review `docs/diagram-style-guide.md`.
- [x] 2.3 Review s10 README, Mermaid diagram, mock, and existing source evidence entries.
- [x] 2.4 Review existing s10 verification OpenSpec specs.

## 3. s10 SVG

- [x] 3.1 Add `s10_extensions_mcp_skills` optional SVG under the chapter `diagrams/` directory.
- [x] 3.2 Add companion Markdown in the same directory.
- [x] 3.3 Confirm the SVG keeps MCP, dynamic tools, extension tools, and skills as separate capability lines.
- [x] 3.4 Confirm dynamic tools experimental, generic extension user entry, and unified governance path are explicitly marked `待核实`.
- [x] 3.5 Confirm the SVG is hand-written, XML-parseable, Chinese-first, diffable, and includes `<title>`, `<desc>`, and visible legend or boundary note.
- [x] 3.6 Render or preview the SVG and fix visual readability issues before finalizing.

## 4. Chapter Navigation

- [x] 4.1 Update s10 README with a short optional SVG entry without replacing `diagram.mmd`.
- [x] 4.2 Confirm s10 status remains `待核实`.
- [x] 4.3 Confirm no official facts, chapter statuses, fact snapshot entries, source evidence entries, check scripts, root README, roadmap, or style guide changed.

## 5. Validation

- [x] 5.1 Run `openspec validate rollout-s10-extension-svg --strict`.
- [x] 5.2 Run `openspec validate --all --strict`.
- [x] 5.3 Run XML parse checks for the newly added SVG file.
- [x] 5.4 Run `python3 scripts/check_docs.py`.
- [x] 5.5 Run `python3 scripts/run_all.py`.
- [x] 5.6 Run `python3 -m unittest discover -s tests`.
- [x] 5.7 Run `git diff --check`.
- [x] 5.8 Review final diff and commit without pushing.
