# Changelog

All notable changes to KGAID are recorded here. The format follows Keep a Changelog and versions follow the governance model.

## [Unreleased]

### Added

- The governed-document approval vocabulary now includes `draft` for work that
  has not yet been submitted for approval. Documents move explicitly from
  `draft` to `pending`; only `pending` documents enter the Human Authority
  queue.

Changes accepted after the prepared baseline and before a release are recorded
here.

## [0.2.3] — 2026-07-20

### Fixed

- Resolve local Markdown document links relative to their source document through the named Flask preview route, preserving fragments and `SCRIPT_NAME` while rejecting targets outside the configured documentation directory.

## [0.2.2] — 2026-07-20

### Fixed

- Rebuilt KGAID Documentation Approval interface routing on Flask named endpoints and `url_for()`, so queue, document preview, approval actions, redirects, and `SCRIPT_NAME` prefixes remain consistent.

## [0.1.0] — 2026-07-19

### Added

- First prepared, unpublished KGAID baseline manifest.
- Governance, versioning, contribution, security, conduct, citation, and repository validation controls.
- Uniform metadata profile for the fourteen normative documents.
- Knowledge Architecture principle-realization mapping.

### Changed

- Verification status vocabulary is aligned to the Verification and Evidence Model.
- The post-audit maintainer title in AUD-001 now uses KGAID terminology; historical KDD audit evidence is retained.
