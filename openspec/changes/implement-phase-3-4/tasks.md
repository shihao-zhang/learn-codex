## 1. Evidence Model

- [x] 1.1 Define the evidence entry shape in `docs/sourcing.md`, including mechanism point, source link, verified scope, status, verification date, and open questions.
- [x] 1.2 Decide whether chapter evidence lives in per-chapter `sources.md` files or a unified evidence index, then document that convention.
- [x] 1.3 Update `docs/fact-snapshot.md` to distinguish path existence, mechanism-level evidence, and behavior-level evidence.
- [x] 1.4 Add example evidence entries for one verified chapter and one pending chapter.

## 2. Documentation Checks

- [x] 2.1 Extend `scripts/check_docs.py` to validate registered evidence entries for chapter source links.
- [x] 2.2 Add checks that prevent `已核实官方事实` chapters from relying only on path-existence evidence.
- [x] 2.3 Add tests that fail on unregistered source links, wrong SHA links, and pending chapters without pending semantics.
- [x] 2.4 Run `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, and `python3 -m unittest discover -s tests`.

## 3. Phase 3 Verified Chapter Upgrade

- [x] 3.1 Add mechanism-level evidence for s01 agent loop and tool observation boundaries.
- [x] 3.2 Add mechanism-level evidence for s03 tool registry, router, handlers, and error paths.
- [x] 3.3 Add mechanism-level evidence for s04 sandbox, approval, network permission, and shell execution boundaries.
- [x] 3.4 Add mechanism-level evidence for s05 context compaction and rollout truncation boundaries.
- [x] 3.5 Review s02, s06, and s07 for over-strong claims and either add evidence or downgrade wording.

## 4. Phase 4 Pending Chapter Verification

- [x] 4.1 Verify s08 session/thread/rollout/thread-store data flow and update its status rationale.
- [x] 4.2 Verify s09 app-server/app-server-protocol transport, request, outgoing message, and thread status boundaries.
- [x] 4.3 Verify s10 MCP, extension tools, and skills crate semantics without assuming CLI first-class skills behavior.
- [x] 4.4 Verify s11 agent jobs, delegation, and parallel execution paths, including whether they belong to the open-source CLI harness mainline.
- [x] 4.5 For each s08~s11 chapter, decide whether to keep `待核实`, upgrade to `已核实官方事实`, or narrow the chapter language.

## 5. Review and Release Readiness

- [x] 5.1 Update README learning map if any chapter statuses change.
- [x] 5.2 Re-run local checks and capture the exact commands in the final implementation summary.
- [x] 5.3 Request authorized Claude review only after stating scope, call mode, cost/side effects, and receiving explicit approval.
- [x] 5.4 Fix review findings that affect fact boundaries, status labels, or source traceability.
- [x] 5.5 Prepare a human-review summary that lists upgraded chapters, remaining pending questions, and evidence coverage.
