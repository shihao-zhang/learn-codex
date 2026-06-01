## 1. OpenSpec Setup

- [x] 1.1 Create the `implement-s12-diagram-redraw-pilot` OpenSpec change.
- [x] 1.2 Define pilot scope, non-goals, fact boundaries, and validation requirements.
- [x] 1.3 Add a spec for the s12 pilot diagram contract.

## 2. s12 Pilot Files

- [x] 2.1 Add `chapters/s12_comprehensive_architecture/diagrams/pilot-trace.svg`.
- [x] 2.2 Add `chapters/s12_comprehensive_architecture/diagrams/pilot-trace.md`.
- [x] 2.3 Update s12 README with an optional pilot entry, without replacing `diagram.mmd`.
- [x] 2.4 Rewrite the pilot display layer to be Chinese-first while keeping English trace fields as secondary labels.
- [x] 2.5 Apply review fixes to README wording and s12 Mermaid boundary labels without replacing the Mermaid diagram.

## 3. Validation

- [x] 3.1 Run `openspec validate implement-s12-diagram-redraw-pilot --strict`.
- [x] 3.2 Run `python3 scripts/check_docs.py`.
- [x] 3.3 Run `python3 scripts/run_all.py`.
- [x] 3.4 Run `python3 -m unittest discover -s tests`.
- [x] 3.5 Run `git diff --check`.
