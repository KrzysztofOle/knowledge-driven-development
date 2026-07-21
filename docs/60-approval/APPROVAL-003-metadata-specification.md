---
document_id: APPROVAL-003
title: Metadata Specification

document_type: contract
status: proposed
version: 1.0

owner: Architecture

approval_status: pending
approved_by:
approved_at:
---

# APPROVAL-003 — Metadata Specification

- **Status:** Proposed
- **Classification:** Informational requirements specification
- **Scope:** Reusable KGAID capability
- **Depends on:** [APPROVAL-002](APPROVAL-002-approval-process.md)

## 1. Purpose

This document defines the information Approval Center needs to identify,
review, approve, relate and preserve governed documents. It specifies meaning,
cardinality, ownership and validation requirements without prescribing how the
metadata is serialized, embedded, stored or exchanged.

The KGAID Artifact Model remains authoritative for common artifact semantics.
An adopting project may add metadata but must not redefine shared fields.

## 2. Design requirements

Metadata must:

- bind a decision to an exact document revision and content state;
- distinguish knowledge, approval, implementation and verification status;
- identify scoped human ownership and decision authority;
- support comparison with the previous accepted version;
- preserve provenance, review, decision and retirement history;
- express typed upstream relationships without duplicating derived inverses;
- allow indexes and impact views to be rebuilt from authoritative records;
- represent unknown, not applicable and intentionally empty values distinctly;
- remain usable across document types, project sizes and repository layouts;
  and
- avoid dependence on a particular syntax, storage product or user interface.

## 3. Record boundaries

Approval Center requires four logical records. They may be represented together
or separately as long as their identities and authority remain unambiguous.

| Record | Responsibility |
| --- | --- |
| Document record | Stable identity, title, type, scope and ownership. |
| Revision record | Exact content state, version, authoring and change details. |
| Approval case | Submission, review requirements, findings and case status. |
| Decision record | Human decision, authority, rationale, conditions and time. |

Document identity survives renames and moves. Revision identity changes when
decision-relevant content or metadata changes. Approval-case identity prevents
one submission from being confused with a later resubmission. Decision identity
allows an approval, rejection or retirement to be referenced independently.

## 4. Requirement levels

| Level | Meaning |
| --- | --- |
| Required | Needed for every governed document or revision in scope. |
| Conditional | Required when the stated event or condition applies. |
| Recommended | Improves interpretation or governance when proportionate. |
| Extension | Project-specific information that preserves core semantics. |

Absence of a conditional field is valid only when its condition does not apply.
Unknown information is recorded explicitly when it blocks reliable inference.

## 5. Document identity and classification

| Information | Level | Requirement |
| --- | --- | --- |
| `id` | Required | Stable, unique identity that is never reused. |
| `title` | Required | Current human-readable canonical title. |
| Artifact or document type | Required | Declares the governed knowledge kind. |
| Scope | Required | Boundary in which the content and decision apply. |
| Project or knowledge space | Required | Prevents cross-project identity ambiguity. |
| Classification | Recommended | Distinguishes normative, evidential, informative or derived content. |
| Location | Required | Resolves the authoritative content without becoming its identity. |
| Baseline membership | Conditional | Identifies every baseline containing the exact revision. |

Changing a title or location does not change `id`. A document containing
several governed artifacts must make each consequential artifact independently
addressable or declare the document as their coherent approval boundary.

## 6. Revision and version information

| Information | Level | Requirement |
| --- | --- | --- |
| Revision identity | Required | Uniquely identifies the submitted content state. |
| `version` | Required | Human-governed version under the artifact's version policy. |
| Content identity | Required | Detects any change to the submitted decision subject. |
| Created time | Required | Time the revision first became durable. |
| `last_modified` | Required | Time of the latest change included in the revision. |
| Author or contributors | Required | Actors responsible for creating the revision. |
| Change summary | Conditional | Required after the initial revision. |
| Change rationale | Conditional | Required for a proposed change to accepted knowledge. |
| Change classification | Conditional | Clarification, compatible or semantic change. |
| Comparison reference | Conditional | Revision against which the change is reviewed. |
| `previous_approved_version` | Conditional | Exact accepted version preceding this candidate. |

`version`, revision identity and content identity have different meanings. A
version communicates governed evolution. A revision identifies one fixed
candidate. Content identity detects mutation. Approval Center must not infer
one from another.

## 7. Status information

| Information | Level | Requirement |
| --- | --- | --- |
| `status` | Required | Uses the KGAID governed document lifecycle taxonomy. |
| `approval_status` | Required | Front-matter projection: `pending` or `approved` for this exact revision. |
| `case_status` | Conditional | Richer workflow state when a complete Approval Center case record exists. |
| Implementation status | Conditional | Recorded when the artifact has a realization claim. |
| Verification status | Conditional | Recorded with exact evidence scope and limitations. |
| Effective period | Conditional | States when accepted knowledge applies, if time-bounded. |
| Supersession or retirement time | Conditional | Required when status changes accordingly. |
| Status rationale | Conditional | Required for rejection, retirement and exceptional transition. |

Each status has one authoritative owner and timestamped history. A dashboard
may combine statuses for display but must not publish a synthetic label that
changes their meaning.

## 8. People, roles and authority

| Information | Level | Requirement |
| --- | --- | --- |
| `author` or contributors | Required | Identifies human, AI or automation contributions accurately. |
| Knowledge Owner | Required | Accountable owner of meaning and lifecycle. |
| Decision Authority | Required | Human role authorized to accept the declared scope. |
| `reviewers` required | Required | Roles or people whose review is needed for the case. |
| `reviewers` participating | Conditional | Actors who performed reviews and their review scopes. |
| Submitter | Conditional | Required after submission. |
| `approved_by` | Conditional | Human actor and authority role for an approval. |
| Rejected by | Conditional | Human actor and authority role for a rejection. |
| Retired by | Conditional | Human actor and authority role for retirement. |
| Delegation reference | Conditional | Evidence of applicable scoped delegation. |

An actor identity alone is insufficient for a consequential decision. The
record also identifies the authority role, scope and applicable delegation.
AI contribution is recorded as provenance and never as human acceptance.

## 9. Approval-case information

| Information | Level | Requirement |
| --- | --- | --- |
| Approval-case identity | Conditional | Required once a revision is submitted. |
| Submitted revision | Conditional | Exact subject of the case. |
| Submitted scope | Conditional | Decision boundary requested by the submitter. |
| Submission time | Conditional | When the fixed revision entered review. |
| Required review disciplines | Conditional | Review coverage needed for decision readiness. |
| Applicable approval rules | Conditional | Rules in effect when the case was submitted. |
| Readiness findings | Conditional | Passed, open, waived or not-applicable conditions. |
| Review findings | Conditional | Comments, questions, conflicts and recommendations. |
| Finding disposition | Conditional | Resolution, response, waiver or continued blocker. |
| `case_status` | Conditional | Current workflow state from the approval-case process taxonomy. |
| Cancellation actor and reason | Conditional | Required when a case is cancelled. |

Approval rules are captured by identity or stable reference so later policy
changes do not rewrite the meaning of an earlier decision.

## 10. Decision information

| Information | Level | Requirement |
| --- | --- | --- |
| Decision identity | Conditional | Required for approval, rejection or retirement. |
| Decision type | Conditional | Approval, rejection, retirement or scoped outcome. |
| Exact revision and content | Conditional | Immutable decision subject. |
| Decision scope | Conditional | What the decision includes and excludes. |
| Decision authority | Conditional | Human role under which the action was taken. |
| Decision actor | Conditional | Human who performed the action. |
| `approved_at` or decision time | Conditional | Effective recorded time of the decision. |
| Rationale | Conditional | Why the decision was made. |
| Conditions | Conditional | Obligations attached to the decision. |
| Limitations | Conditional | Boundaries that the decision does not cross. |
| Accepted risks | Conditional | Exact risks and applicable Risk Authority. |
| Waivers | Conditional | Departures, authority, rationale and expiry. |
| Follow-up obligations | Conditional | Owned actions resulting from the decision. |

`approved_by` and `approved_at` are projections of a complete decision
record, not substitutes for it. A project may use concise rationale for a
low-risk change, but the actor, authority, subject and scope remain mandatory.

## 11. Relationships and traceability

| Information | Level | Requirement |
| --- | --- | --- |
| `depends_on` | Conditional | Direct upstream knowledge required by the artifact. |
| `supersedes` | Conditional | Exact earlier artifact or version replaced on acceptance. |
| `derived_from` | Conditional | Authoritative source of a non-authoritative derivative. |
| `constrained_by` | Conditional | Applicable constraint or obligation. |
| `satisfies` | Conditional | Need or requirement satisfied by this artifact. |
| `realizes` | Conditional | Specification realized by this artifact. |
| `verified_claims` | Conditional | Exact claims addressed by evidence. |
| `conflicts_with` | Conditional | Unresolved contradiction and affected scope. |
| Related items | Recommended | Non-dependency context with a declared relation type. |

Relationships use stable identifiers and, where meaning depends on it, exact
versions or revisions. Inverse relationships such as downstream dependants are
derived from authoritative forward links rather than maintained twice.

`previous_approved_version` is a revision-history reference. `supersedes` is a
semantic lifecycle relationship. They may identify the same version, but one
must not be inferred automatically from the other.

## 12. Provenance and time

| Information | Level | Requirement |
| --- | --- | --- |
| Sources | Conditional | Origins, versions, dates and applicability of material claims. |
| Proposed by | Required | Actor or collaboration that originated the candidate. |
| Created time | Required | Durable creation event. |
| `last_modified` | Required | Latest included modification. |
| Submitted time | Conditional | Approval submission event. |
| Review times | Conditional | When each review outcome was recorded. |
| Decision time | Conditional | Approval, rejection or retirement event. |
| Event history | Required | Ordered changes to status, ownership and decision state. |

Times include sufficient context for unambiguous ordering. A displayed local
time may be adapted to the user, but the underlying record remains comparable
across projects and locations.

## 13. Validation requirements

Validation must detect at least:

- missing or duplicate stable identities;
- a revision or decision that cannot resolve its exact content;
- invalid status values or impossible transitions;
- approval without a human actor and applicable authority;
- approval metadata inherited by changed content;
- missing required reviewer or unresolved blocking finding;
- dependency on missing, rejected, retired or incompatible knowledge;
- supersession cycles and inconsistent version lineage;
- a decision time earlier than its submitted revision;
- conflicting active accepted versions in the same scope; and
- a derived inverse relationship that disagrees with its authoritative source.

Validation results distinguish error, warning and information. Severity is
governed by the applicable project profile and risk, not by the presentation
layer. No validator may invent missing authority, relationships or approvals.

## 14. Minimum and extended profiles

### 14.1 Minimum profile

Every governed approval requires at least:

- document and project identity, title, type and scope;
- exact revision, version and content identity;
- knowledge and approval status;
- author or contributors, Knowledge Owner and Decision Authority;
- direct dependencies;
- creation and last-modified times;
- approval case and required reviewers after submission; and
- a complete human decision record after decision.

### 14.2 Extended profile

Projects with greater consequence, lifetime or coordination needs should also
capture:

- multiple review disciplines and delegations;
- evidence and risk relationships;
- compatibility and migration classification;
- effective and expiry periods;
- policy versions and waivers;
- grouped-decision membership;
- cross-project relationship scope; and
- follow-up obligations with owners and due conditions.

The extended profile adds rigor without changing the meaning of the minimum
fields.

## 15. Privacy and integrity requirements

Metadata contains personal and potentially sensitive decision information.
Approval Center must:

- collect only identity detail required for accountability;
- apply visibility appropriate to project and decision scope;
- protect decision records from undetected alteration;
- preserve attribution when a person's display name changes;
- support retention obligations without exposing unrelated private data; and
- distinguish correction of personal display data from alteration of history.

## 16. Open design decisions

The following remain intentionally undecided until prototype and pilot
evidence exists:

- physical placement of metadata relative to Markdown content;
- serialization and schema notation;
- content-identity mechanism;
- representation of actors and delegations;
- storage boundary for decision and event history;
- project-specific extension mechanism; and
- synchronization strategy across knowledge locations.

These are implementation or adoption decisions. They do not alter the semantic
requirements in this document.

## 17. Related documents

- [Vision](APPROVAL-001-vision.md)
- [Approval Process](APPROVAL-002-approval-process.md)
- [Approval Center UI](APPROVAL-004-approval-center-ui.md)
- [Architecture](APPROVAL-005-architecture.md)
- [Roadmap](APPROVAL-006-roadmap.md)
- [Approval Center index](README.md)
