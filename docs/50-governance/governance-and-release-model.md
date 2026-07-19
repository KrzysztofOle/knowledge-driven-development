---
document_id: KGAID-GOV-001
title: KGAID Governance, Versioning, and Release Model

document_type: governance
status: accepted
version: 0.1.0

owner: Governance

approval_status: pending
approved_by:
approved_at:
---

# KGAID Governance, Versioning, and Release Model

**Status:** Accepted  
**Version:** 0.1.0  
**Baseline:** KGAID-0.1.0  
**Classification:** Normative  
**Maintainer:** Krzysztof Olejnik — KGAID Methodology Maintainer  
**Last reviewed:** 2026-07-19

## 1. Purpose

This document governs changes to the KGAID methodology repository and the preparation of its public baselines. It governs the methodology itself; it does not replace the authority model an adopting project uses for its own knowledge.

## 2. Roles and authority

The KGAID Methodology Maintainer is the durable human maintainer of this repository. The Maintainer MAY delegate review work, but retains responsibility for accepting a methodology change and for authorizing a baseline or release.

Any person MAY submit an issue or pull request. A change that alters a normative requirement, defined status, conformance rule, dependency, or baseline membership is a normative change. A normative change MUST include rationale, affected documents, compatibility assessment, and a proposed version impact. It MUST be reviewed and explicitly accepted by the Maintainer before merge.

Non-normative edits, including typographic corrections and improvements to explanatory material, SHOULD receive review proportionate to their impact. They MUST NOT silently alter a normative interpretation.

## 3. Change lifecycle

Methodology changes follow this lifecycle:

`Draft → Review → Accepted → Baseline`

- **Draft:** a proposed change is visible and has not become authoritative.
- **Review:** scope, dependencies, normative impact, and evidence are examined.
- **Accepted:** the Maintainer has explicitly accepted the change; its document is authoritative in its declared scope.
- **Baseline:** a fixed, verified set of Accepted documents is recorded in a baseline manifest.

An Accepted document MAY change after acceptance, but it MUST re-enter Review before another baseline includes the changed version.

## 4. Versioning and compatibility

KGAID uses semantic versions: `MAJOR.MINOR.PATCH`.

- **MAJOR**: a breaking change to a normative requirement, defined term, conformance expectation, or required artifact.
- **MINOR**: a backwards-compatible normative addition or clarification that adds capability without invalidating a conforming adoption.
- **PATCH**: a non-breaking correction, ambiguity removal, metadata correction, or informative update with no changed normative obligation.

A breaking change MUST identify migration consequences and the baseline it supersedes. A non-breaking normative change SHOULD identify affected dependencies. A baseline is immutable after publication; corrections require a new version and manifest.

## 5. Baselines and releases

A baseline is created when the Maintainer confirms that:

1. every listed normative document is Accepted and has complete metadata;
2. the baseline manifest records membership, dependencies, and verification status;
3. repository controls pass; and
4. known exceptions and residual risks are recorded.

Preparing a manifest does not publish it. Publication requires a separate Maintainer decision, a signed or annotated Git tag named `kgaid-v<version>`, a GitHub release containing the manifest, CHANGELOG entry, and release notes. The first prepared baseline is `KGAID-0.1.0`; it remains unpublished until that separate decision.

## 6. Records

`CONTRIBUTING.md` defines contribution expectations, `CHANGELOG.md` records user-visible changes, `docs/50-governance/baselines/` contains manifests, and `docs/50-governance/audits/` contains evidence and audit records. `AUD-001` and `AUD-002` retain their historical names as evidence of the KDD-to-KGAID identity migration.
