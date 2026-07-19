---
document_id: KGAID-GOV-002
title: KGAID Governed Document Metadata Profile

document_type: governance
status: accepted
version: 0.1.0

owner: Governance

approval_status: pending
approved_by:
approved_at:
---

# KGAID Governed Document Metadata Profile

**Status:** Accepted  
**Version:** 0.1.0  
**Baseline:** KGAID-0.1.0  
**Classification:** Informational governance control  
**Maintainer:** Krzysztof Olejnik — KGAID Methodology Maintainer  
**Last reviewed:** 2026-07-19

## Scope

Every KGAID-governed Markdown document MUST begin with the YAML front matter
defined in this profile. A governed document has a stable `document_id` and is
subject to lifecycle management and human approval. Navigation files such as a
directory `README.md`, repository policies and tool instructions are not
governed documents unless they are explicitly assigned an identifier.

Baseline membership, normative classification, dependencies, supersession and
verification evidence remain in their authoritative manifests or document
content. They are not parallel front-matter fields.

## Required front matter

The header contains each of the following fields exactly once and uses the
lower-case controlled values defined below:

```yaml
---
document_id: XXX-001
title: Canonical document title

document_type: capability
status: proposed
version: 1.0

owner: Product

approval_status: pending
approved_by:
approved_at:
---
```

| Field | Requirement |
| --- | --- |
| `document_id` | Stable, unique identifier. It MUST NOT change when the file is renamed or the document evolves. |
| `title` | Official human-readable document title. |
| `document_type` | Semantic kind from the controlled document-type vocabulary. |
| `status` | Current content lifecycle state; it is independent of approval processing. |
| `version` | Governed document version. Existing version schemes remain valid; new methodology documents use semantic versions. |
| `owner` | Accountable owner category from the project-wide vocabulary. |
| `approval_status` | Technical approval state: `pending` or `approved`. |
| `approved_by` | Human approver identity; empty while approval is pending. |
| `approved_at` | ISO 8601 approval date or timestamp; empty while approval is pending. New approvals SHOULD include time and timezone offset. |

## Document types

The permitted `document_type` values are:

- `vision` — intended outcome and direction;
- `capability` — ability the product, process or organization must provide;
- `business-process` — business or delivery workflow;
- `business-rule` — binding domain or organizational rule;
- `requirement` — verifiable need or constraint;
- `glossary` — controlled terminology;
- `domain-model` — domain concepts and relationships;
- `adr` — architecture decision record;
- `architecture` — structural design and boundaries;
- `contract` — explicit interface, task or metadata contract;
- `verification` — claims, evidence and verification rules;
- `operations` — operation, support and runtime knowledge;
- `governance` — authority, lifecycle, policy or control;
- `knowledge` — governed knowledge not more precisely represented above.

## Content status

The `status` field describes the maturity and authority of document content:

- `draft` — work in progress, not ready for a governance decision;
- `proposed` — coherent candidate submitted or ready for review and decision;
- `accepted` — current authoritative content in its declared scope;
- `deprecated` — still available but discouraged and planned for withdrawal;
- `superseded` — replaced by a newer identified document or version and retained
  only for history and traceability.

Review is an activity performed on a `proposed` document, not a separate
content status. Baseline is a release property recorded in a manifest, not a
document status.

## Owner vocabulary

KGAID uses stable responsibility categories rather than person names in
`owner`. The accountable person or decision authority is resolved by project
governance.

| Owner | Default document types |
| --- | --- |
| `Product` | `vision`, `capability`, `requirement` |
| `Business` | `business-process`, `business-rule`, `glossary` |
| `Architecture` | `domain-model`, `adr`, `architecture`, `contract` |
| `Quality` | `verification` |
| `Operations` | `operations` |
| `Governance` | `governance`, `knowledge` |

A justified project-specific assignment MAY differ, but the owner value MUST
remain one of these six categories.

## Approval process

`approval_status` records only whether the exact current document revision has
been approved through the supported approval mechanism:

- `pending` — no approval is recorded for the current revision;
- `approved` — a human approval is recorded for the current revision, and both
  `approved_by` and `approved_at` are populated.

A new or materially changed governed document starts with `pending` and empty
approval details. The `kgaid-doc-approval` application discovers that value and,
after an explicit human action, changes only `approval_status`, `approved_by`
and `approved_at`. All other front-matter fields and Markdown content are
transparent to the application and MUST remain unchanged.

An approval is bound to the reviewed revision. A later content or governed
metadata change MUST return the document to `pending` and clear `approved_by`
and `approved_at` before renewed approval. Git history preserves the earlier
decision record.

## `status` and `approval_status`

The two fields answer different questions and MUST NOT be derived from one
another:

- `status` answers: *What is the content's lifecycle meaning and authority?*
- `approval_status` answers: *Has this exact revision been approved through the
  approval process?*

For example, an historically accepted document imported before technical
approval tracking can have `status: accepted` and `approval_status: pending`.
A proposed revision can be technically approved as the reviewed proposal while
remaining `status: proposed` until the authorized lifecycle decision changes
its content status.

## Canonical verification taxonomy

The Verification and Evidence Model is the source of truth for verification status. The permitted values are `not-planned`, `planned`, `in-progress`, `partially-supported`, `failed`, `verified`, `verified-with-limitations`, `inconclusive`, `invalidated`, and `expired`.

An evidence result (`supports`, `contradicts`, `partial`, `inconclusive`, `not-executed`, or `invalid`) is not a verification status. Statuses in other models MUST use these canonical values or explicitly map a local label to one of them.

## Normative language

KGAID uses the keywords **MUST**, **SHOULD**, and **MAY** as defined in [KGAID Principles](../00-foundations/02-principles.md#2-normative-language): MUST denotes a requirement, SHOULD a strong recommendation with explicit rationale for departure, and MAY a permitted option. Their negative forms have the corresponding meaning. Lower-case occurrences are avoided in normative rules so the meaning is unambiguous.
