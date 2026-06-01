## ADDED Requirements

### Requirement: Review closeout document

The repository SHALL provide a review closeout document before treating P4 as complete.

#### Scenario: Closeout is prepared

- **WHEN** P4 is complete
- **THEN** the repository contains `docs/maintenance-closeout.md`
- **AND** it summarizes completed work, fact boundaries, validation results, and remaining risks

### Requirement: No new official fact claims

The P4 closeout SHALL NOT introduce new `openai/codex` implementation facts.

#### Scenario: Closeout text is written

- **WHEN** the closeout describes completed work
- **THEN** it describes this teaching repository's changes and does not claim OpenAI Codex official behavior changed

#### Scenario: Fact snapshot is mentioned

- **WHEN** the closeout mentions fact snapshot status
- **THEN** it states that the target commit and release verification value remain unchanged unless a separate change migrates them

### Requirement: Active change review strategy

The P4 closeout SHALL state how active OpenSpec changes should be handled for review.

#### Scenario: Active changes are listed

- **WHEN** a reviewer reads the closeout
- **THEN** completed OpenSpec changes are grouped by purpose
- **AND** the document recommends keeping them active through review unless a separate archive step is requested

### Requirement: PR and review hygiene

The repository SHALL define minimum PR/review hygiene for this branch.

#### Scenario: PR summary is drafted

- **WHEN** the branch is prepared for review
- **THEN** the summary includes changed areas, unchanged fact boundaries, checks run, and follow-up risks

### Requirement: P4 validation

The P4 closeout SHALL pass repository validation before completion.

#### Scenario: Change is ready

- **WHEN** closeout docs and checklist updates are complete
- **THEN** the maintainer runs `openspec validate prepare-open-source-review-closeout-p4 --strict`, `python3 scripts/check_docs.py`, `python3 scripts/run_all.py`, `python3 -m unittest discover -s tests`, and `git diff --check`
