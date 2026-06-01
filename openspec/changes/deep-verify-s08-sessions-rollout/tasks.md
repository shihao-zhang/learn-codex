## 1. OpenSpec Scope

- [x] 1.1 Create the `deep-verify-s08-sessions-rollout` OpenSpec change.
- [x] 1.2 Define the s08-only scope, fixed-SHA fact baseline, status upgrade rule, and validation requirements.

## 2. Source Verification

- [x] 2.1 Re-read current s08 README, fact snapshot, and source evidence.
- [x] 2.2 Verify fixed-SHA sources for thread-store and rollout replay.
- [x] 2.3 Verify fixed-SHA sources for app-server resume/fork and core reconstruction boundaries.
- [x] 2.4 Verify fixed-SHA sources for TUI, daemon, debug-client, and remote store boundaries.
- [x] 2.5 Decide which s08 claims can upgrade and which must remain `待核实`.

## 3. Documentation Updates

- [x] 3.1 Update `docs/source-evidence.md` only for s08 mechanisms and unresolved boundaries.
- [x] 3.2 Update `chapters/s08_sessions_threads_rollout/README.md` with conservative wording if needed.
- [x] 3.3 Do not modify `docs/fact-snapshot.md` or `scripts/check_docs.py`.

## 4. Validation

- [x] 4.1 Run `openspec validate deep-verify-s08-sessions-rollout --strict`.
- [x] 4.2 Run `python3 scripts/check_docs.py`.
- [x] 4.3 Run `python3 scripts/run_all.py`.
- [x] 4.4 Run `python3 -m unittest discover -s tests`.
- [x] 4.5 Run `git diff --check`.

Validation result:

- `openspec validate deep-verify-s08-sessions-rollout --strict`: passed.
- `python3 scripts/check_docs.py`: passed after the paired s10 deep verification and fact snapshot path registration were reconciled.
- `python3 scripts/run_all.py`: passed.
- `python3 -m unittest discover -s tests`: passed after the paired s10 deep verification and fact snapshot path registration were reconciled.
- `git diff --check`: passed.
