## ADDED Requirements

### Requirement: Rendered SVG visual QA

The repository SHALL visually verify high-value SVG teaching diagrams after rendering, not only by inspecting source XML.

#### Scenario: SVG is ready for review

- **WHEN** a chapter SVG is added or materially revised
- **THEN** the maintainer renders it to an image or browser preview
- **AND** verifies that the main path, side paths, text, chips, arrows, and legend are readable

#### Scenario: Main path hierarchy is checked

- **WHEN** a diagram contains both verified mechanism facts and teaching failure or recovery paths
- **THEN** the verified mechanism path is visually primary
- **AND** teaching paths, trace examples, and legend content are visually secondary

#### Scenario: Overlap is checked

- **WHEN** a rendered SVG is inspected
- **THEN** cards, labels, chips, arrows, and legend blocks do not overlap or obscure each other
- **AND** connector lines do not pass through reader-facing text

#### Scenario: Dense diagram is simplified

- **WHEN** a diagram becomes visually dense enough that the first reading path is unclear
- **THEN** the diagram is reorganized into separate layers such as main path, side explanation, and legend
- **AND** nonessential chips or copy are reduced before adding more visual elements
