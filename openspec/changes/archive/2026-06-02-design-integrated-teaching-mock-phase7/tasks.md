## 1. OpenSpec Setup

- [x] 1.1 Create the `design-integrated-teaching-mock-phase7` OpenSpec change.
- [x] 1.2 Define the design-only scope, non-goals, and future implementation boundaries.
- [x] 1.3 Add a spec for integrated mock coverage, fact boundaries, and validation requirements.

## 2. Integrated Mock Design

- [x] 2.1 Define the required teaching surfaces: agent loop, tool dispatch, permission decision, context pressure, instruction conflict, session trace / recovery, and failure recovery.
- [x] 2.2 Define deterministic/offline/Python-standard-library constraints for future implementation.
- [x] 2.3 Define the trace contract and scenario matrix without claiming to reproduce OpenAI Codex.
- [x] 2.4 Define how s08/s10 can be referenced only as `待核实` boundaries.

## 3. Roadmap

- [x] 3.1 Update `docs/roadmap.md` if needed to show Phase 7 design has started, without implying code implementation.

## 4. Validation

- [x] 4.1 Run `openspec validate design-integrated-teaching-mock-phase7 --strict`.
- [x] 4.2 Run `python3 scripts/check_docs.py`.
- [x] 4.3 Run `git diff --check`.
