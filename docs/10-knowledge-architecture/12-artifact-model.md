---
document_id: KGAID-KA-002
title: KGAID Artifact Model
status: Accepted
version: 0.1.0
baseline: KGAID-0.1.0
normative: true
maintainer: Krzysztof Olejnik — KGAID Methodology Maintainer
last_reviewed: 2026-07-19
dependencies: [KGAID-KA-001]
supersedes: null
superseded_by: null
verification_status: verified
change_control: docs/50-governance/governance-and-release-model.md
---

# KGAID Artifact Model

## 1. Purpose

This document defines the artifact model of Knowledge-Governed AI-Assisted Development
(KGAID). It specifies the kinds of knowledge artifacts used by the methodology,
their authority, lifecycle states, relationships, minimum metadata and
verification rules.

The model is independent of programming language, framework, architecture
style, repository host and AI provider. A project MAY use a minimal or extended
profile, but it MUST preserve the semantic distinctions defined here.

## 2. Fundamental rules

1. Every normative item of knowledge has exactly one authoritative owner.
2. Downstream artifacts reference upstream knowledge instead of redefining it.
3. Accepted knowledge changes only through an explicit human decision.
4. A changed durable decision supersedes the previous decision; identifiers are
   immutable and never reused.
5. AI output remains a proposal until accepted by an authorized human.
6. Code is a realization of knowledge and cannot silently redefine a
   requirement, contract or decision.
7. Evidence always identifies the exact claim, version, boundary, environment
   and limitations that it verifies.
8. Accepted architecture does not by itself prove implementation.
9. Existing implementation does not by itself prove conformance with accepted
   architecture.
10. Indexes, README files, translations and generated summaries do not create
    competing sources of truth.

These rules establish the **Single Knowledge Ownership Principle**:

> Every definition, rule, decision and status claim has exactly one
> authoritative artifact. Other documents reference that artifact rather than
> copying its normative meaning.

## 3. Artifact and file are different concepts

A knowledge artifact is an identifiable unit of project knowledge. A file is
only a storage container.

One coherent document MAY contain several artifacts. For example, one use-case
catalogue MAY contain `UC-001` through `UC-008`. Each artifact that affects
project decisions MUST nevertheless remain addressable by a stable identifier
or unambiguous anchor.

KGAID does not require one file per artifact and does not assign identifiers to
every paragraph, note, AI conversation or implementation task.

## 4. Artifact catalogue

| Prefix | Artifact | Responsibility |
| --- | --- | --- |
| `PRN` | Principle | A governing and durable project rule. |
| `VIS` | Vision | Product problem, purpose, audience, outcomes and boundaries. |
| `TERM` | Term | One authoritative definition in the project language. |
| `BR` | Business Rule | An independently normative, durable business, domain or regulatory rule. |
| `ASM` | Assumption | A claim that requires confirmation. |
| `RISK` | Risk | Uncertainty, possible impact and treatment. |
| `CAP` | Capability | A product ability that provides value. |
| `UC` | Use Case | Behaviour that achieves an actor's goal. |
| `SCN` | Scenario | A concrete flow and expected outcome. |
| `REQ` | Requirement | A functional requirement. |
| `QR` | Quality Requirement | A quality or non-functional requirement. |
| `CON` | Constraint | A legal, organizational, business or technical restriction. |
| `ARC` | Architecture Specification | System structure, boundaries, ownership and allowed dependencies. |
| `ADR` | Architecture Decision | An accepted durable architecture decision. |
| `CTR` | Contract | Observable behaviour at a component or system boundary. |
| `RFC` | Request for Comments | A proposed solution or technical contract requiring review. |
| `INC` | Increment | A bounded unit selected for realization. |
| `EVD` | Evidence | Evidence supporting one or more explicit claims. |
| `AUD` | Audit | A scoped review of consistency, quality or conformance. |
| `LRN` | Learning | Knowledge obtained from verification or operation. |

A project profile MAY introduce additional artifact types when it defines their
authority and relationships without changing the meanings above.

### 4.1 Business Rule (`BR`)

A Business Rule states a truth, invariant, prohibition, permission or
obligation that governs the represented business domain. It captures a rule
that remains meaningful independently of any particular system, interface or
implementation. A `BR` belongs to Domain Knowledge and is owned by the Domain
Authority.

A `BR` is responsible for the normative business meaning of the rule. It is
not responsible for specifying how a system detects, prevents, stores,
communicates or verifies compliance. Those obligations belong to downstream
requirements, architecture, contracts, implementation and evidence.

A `BR` MUST NOT describe:

- implementation, API, architecture or user-interface design;
- a use-case or scenario flow;
- acceptance criteria or a test procedure; or
- a system-specific mechanism for enforcing the rule.

For example, the following statements have different owners:

```text
BR-001: An invoice with an assigned KSeF number MUST NOT be changed.

REQ-024: The system MUST prevent editing an invoice with an assigned KSeF
number.
```

The `BR` describes the applicable business truth. The `REQ` describes the
observable system obligation that follows from it.

### 4.2 Business Rule qualification

A rule is recorded as a separate `BR` when it is durable, independently
normative within its declared scope, and at least one of the following applies:

- it follows from law, regulation, a binding agreement or a mandatory standard;
- it follows from an applicable external specification or regulatory system;
- it protects business-data integrity or state consistency;
- it defines a security, authorization or entitlement boundary in the domain;
- more than one requirement, capability, contract or decision relies on it; or
- it is a stable domain invariant whose violation changes the meaning or
  validity of a business fact.

A qualifying rule MAY support only one current requirement when its source,
durability or consequence warrants independent ownership. Conversely, repeated
references alone do not turn a local condition into a `BR`.

A condition remains part of a `REQ`, use case, scenario or acceptance criterion
when it is local to that system obligation, has no independent business meaning,
is not expected to constrain other knowledge, and can change together with that
obligation without changing the domain. A formatting detail, workflow step,
error message, API precondition or test expectation is not a `BR` solely
because it uses normative language.

### 4.3 Business Rule relationships

A `BR` uses `TERM` artifacts and a domain model for its vocabulary and scope.
Downstream artifacts reference the `BR` only when the rule materially constrains
their meaning:

- a `CAP` depends on a `BR` when the capability operates under that rule;
- a domain model depends on or is constrained by a `BR` when the rule limits
  valid domain state or transition;
- a `REQ` depends on a `BR` when it expresses a system obligation derived from
  the rule;
- an `ADR` depends on or is constrained by a `BR` when the rule affects the
  accepted architectural decision; and
- `EVD` verifies a `REQ`, contract or other exact claim; it does not make the
  test procedure the owner of the `BR`.

No `REQ` is required to reference a `BR`. The link is used only after the
qualification criteria in Section 4.2 are met.

### 4.4 Business Rule template

Each material `BR` uses the standard artifact metadata from Section 7 and
records the following content. Projects MAY choose Markdown, front matter or a
structured representation, provided that the fields retain these meanings.

```yaml
id: BR-NNN
type: business-rule
title: Concise rule name

knowledge_status: proposed
implementation_status: not-applicable
verification_status: planned

scope: Business context, entities, events and jurisdictions to which the rule applies
owner: domain-owner
decision_authority: domain-authority

normative_statement: The business rule stated without a solution mechanism
rationale: Why the rule exists and the consequence it protects
domain_terms:
  - TERM-NNN
exceptions:
  - Declared exception, or none
sources_of_obligation:
  - kind: law | regulation | external-specification | domain-policy
    reference: Stable source, version or locator
    applicability: Why and where the source applies

depends_on:
  - TERM-NNN
constrained_by: []
supersedes: null

created_at: YYYY-MM-DD
accepted_at: null
last_reviewed_at: YYYY-MM-DD

provenance:
  proposed_by: human-ai-collaboration
  accepted_by: null
```

`normative_statement` is the authoritative rule content. `rationale` explains
the rule but does not narrow or replace it. `exceptions` are part of the rule's
scope and MUST be explicit; an absent exception is recorded as `none`.
`sources_of_obligation` identifies why the rule applies. A business-originated
rule records its authoritative policy or Domain Authority decision there.

## 5. Primary knowledge flow

```mermaid
flowchart TD
    V["VIS: vision"] --> C["CAP: capability"]
    C --> R["REQ / QR"]
    R --> A["ARC / ADR"]
    A --> T["CTR: contract"]
    T --> I["INC: implementation"]
    I --> E["EVD: evidence"]
    E --> L["LRN: learning"]
    L --> V
```

Additional relationships apply throughout this flow:

- `TERM` and `BR` supply the language and rules used by capabilities,
  requirements and architecture;
- `ASM` and `RISK` MAY relate to any artifact;
- `SCN` makes a capability, use case or requirement concrete;
- an `RFC` MAY lead to an `ADR`, `CTR` and `INC`;
- an `AUD` checks a selected part or the whole knowledge chain.

## 6. Independent status dimensions

A single status field is insufficient. KGAID separates knowledge approval,
implementation maturity and verification.

### 6.1 Knowledge status

```text
captured
→ proposed
→ reviewed
→ accepted
→ superseded
→ retired
```

`rejected` is an additional terminal state for a proposal that was considered
and not accepted.

- `captured`: an observation, need or idea has been recorded;
- `proposed`: a coherent candidate artifact exists;
- `reviewed`: review is complete, but acceptance has not yet been granted;
- `accepted`: an authorized human has made the artifact normative;
- `superseded`: another accepted artifact replaced it;
- `retired`: it is no longer applicable and has no direct replacement;
- `rejected`: it was considered and deliberately not adopted.

### 6.2 Implementation status

```text
not-applicable
not-started
planned
in-progress
experimental
partial
implemented
deprecated
removed
```

Implementation status is always interpreted within the artifact's declared
scope. `experimental` or `partial` MUST identify the missing boundary or
guarantee. `implemented` requires realization at the intended boundary, not
merely the existence of related code.

### 6.3 Verification status

```text
not-planned
planned
in-progress
partially-supported
failed
verified
verified-with-limitations
inconclusive
invalidated
expired
```

These are the canonical claim verification statuses defined by the Verification
and Evidence Model. Verification status never stands alone. It MUST reference evidence and its
scope. Evidence from a unit test, controlled substitute or DEMO environment
MUST NOT be generalized to production behaviour.

Example:

```yaml
knowledge_status: accepted
implementation_status: experimental
verification_status: partially-supported

verification_scope:
  environment: demo
  boundary: in-memory-storage
  limitations:
    - no process-restart durability
    - no production database
```

## 7. Minimum metadata

Every normative artifact MUST provide at least:

```yaml
id: ADR-001
type: architecture-decision
title: Decision title

knowledge_status: accepted
implementation_status: planned
verification_status: planned

scope: Scope in which the artifact applies
owner: architecture-owner
decision_authority: product-owner

depends_on:
  - REQ-004
  - QR-002

supersedes: null

created_at: YYYY-MM-DD
accepted_at: YYYY-MM-DD
last_reviewed_at: YYYY-MM-DD

provenance:
  proposed_by: human-ai-collaboration
  accepted_by: human
```

Projects MAY use Markdown front matter, tables, structured files or another
machine-readable representation. The semantics are normative; the serialization
format is replaceable.

The inverse relation `downstream` SHOULD NOT be maintained manually. It SHOULD
be derived from authoritative upstream links such as `depends_on`, because
duplicated bidirectional links easily become inconsistent.

## 8. Relationship vocabulary

| Relationship | Meaning |
| --- | --- |
| `depends_on` | The artifact requires upstream knowledge. |
| `defines` | The artifact owns a definition. |
| `satisfies` | An element satisfies a requirement or constraint. |
| `realizes` | An implementation or increment realizes a contract or architecture element. |
| `constrained_by` | The artifact is limited by another artifact or external obligation. |
| `verified_by` | The claim is supported by referenced evidence. |
| `derived_from` | The artifact is a non-authoritative derivative. |
| `supersedes` | The artifact replaces an earlier artifact. |
| `conflicts_with` | An unresolved contradiction has been detected. |

An accepted release of project knowledge SHOULD NOT contain an unresolved
`conflicts_with` relation without an explicit exception owner, scope and
resolution plan.

## 9. Authority hierarchy

| Level | Knowledge |
| --- | --- |
| 0 | Binding law, standards and external obligations. |
| 1 | Project principles, vision, product boundaries and governance. |
| 2 | Domain model, terminology and business rules. |
| 3 | Capabilities, use cases, requirements and acceptance criteria. |
| 4 | Architecture specifications and accepted decisions. |
| 5 | Contracts. |
| 6 | Delivery increments and implementation. |
| 7 | Evidence, reports, observations and operational learning. |

A downstream artifact cannot silently override upstream knowledge.

If implementation reveals that a requirement MUST change, the requirement is
changed first through its own authority and lifecycle. The affected
architecture, contracts, implementation and verification are then reviewed and
updated. Existing code does not automatically become the specification.

An ADR MAY clarify or choose within accepted upstream constraints. It cannot
override a principle, business rule or requirement unless the owning upstream
artifact is explicitly changed or superseded.

## 10. Common document roles

| Document | Authority |
| --- | --- |
| README | Informative entry point; not a substitute for normative artifacts. |
| Manifest | Normative values and principles. |
| Vision | Normative product purpose and boundaries. |
| Glossary | Index of terms and their authoritative definitions. |
| ADR | Normative durable decision. |
| RFC | Proposal or accepted technical contract; does not by itself prove implementation. |
| Roadmap | Current order and maturity assessment; not a source of requirements. |
| Release notes | Historical description of a particular release. |
| Audit | Scoped conformance assessment at a declared point in time. |
| Test report | Evidence with an explicit boundary and limitations. |
| Translation | Derived artifact that cannot introduce normative meaning. |
| Code | Realization of accepted knowledge, not the owner of product decisions. |

A status MUST have one authoritative location. README files and registries
SHOULD link to it rather than maintain independent copies. When tooling is
available, indexes SHOULD be generated from artifact metadata.

## 11. Evidence model

Every `EVD` MUST state:

1. the claims it verifies;
2. the subject and exact version;
3. the environment in which it was obtained;
4. the boundary that was actually exercised;
5. the guarantees it does not establish;
6. the date and responsible actor;
7. whether and how the evidence can be reproduced.

Example:

```yaml
id: EVD-014
type: test-result

verified_claims:
  - CTR-006
  - REQ-021

subject_version: 0.10.1
environment: controlled-demo
verification_status: verified

limitations:
  - in-memory storage only
  - no restart durability
  - no production deployment
```

Evidence can invalidate an assumption or reveal a conflict. It does not
silently edit the affected knowledge. It creates a proposed change or
`LRN` artifact for human review.

## 12. KGAID profiles

### 12.1 Minimal profile

A small project MUST maintain at least:

1. product vision and boundaries;
2. essential terms and business rules;
3. capabilities or use cases;
4. requirements and acceptance criteria;
5. a basic architecture description;
6. ADRs for consequential decisions;
7. contracts for material boundaries; and
8. evidence supporting completion claims.

The artifacts MAY be grouped into a small number of files.

### 12.2 Extended profile

A larger, regulated, long-lived or multi-team project SHOULD additionally
maintain:

- separate assumption and risk registers;
- formal RFC and ADR registries;
- quality requirements and constraints;
- architecture views and component ownership;
- contract compatibility rules;
- implementation increments;
- an evidence registry;
- architecture and conformance audits;
- operational learning and supersession history.

The selected profile SHOULD be recorded in project governance and MAY evolve
as the project grows.

## 13. Identifier rules

Stable identifiers are required for items with meaningful project impact,
including:

- principles;
- business and domain rules;
- capabilities and use cases;
- requirements and quality requirements;
- assumptions and risks;
- durable decisions;
- contracts;
- evidence;
- learning that changes the project.

Identifiers are not required for:

- every paragraph;
- transient working notes;
- unreviewed AI conversation;
- routine implementation activity;
- mechanical or cosmetic changes.

Identifiers are immutable and never reused. A renamed artifact retains its
identifier. A changed decision is represented by a new artifact that
`supersedes` the previous one.

## 14. Human and AI authority

AI MAY gather sources, identify gaps, detect contradictions, propose models,
draft artifacts, implement accepted contracts, generate verification and
perform an additional review.

AI MUST NOT:

- accept its own proposal;
- change product goals or business rules without human authorization;
- silently broaden evidence;
- treat generated code as an accepted requirement;
- waive a quality gate;
- accept project risk on behalf of a human.

A material AI-created or AI-modified artifact starts no higher than
`proposed`. Human acceptance records the decision authority independently
from authorship.

## 15. Evolution rules

1. A clarification MAY update an accepted artifact only when it does not change
   its observable meaning.
2. A semantic change creates a new revision or artifact according to that
   artifact type's governance.
3. A changed durable decision requires a new decision that supersedes the old
   one.
4. A change to upstream knowledge triggers an impact review of dependent
   artifacts.
5. Previously valid evidence is marked `invalidated` when its subject,
   boundary or prerequisite changes materially.
6. Historical artifacts remain available to explain why the current state
   exists.
7. Knowledge cleanup removes duplication but does not erase decision history.

## 16. Origin and applicability

This model was extracted from practical experience developing KSeF_2 and then
generalized for projects independent of domain, language and framework.

KSeF_2 demonstrates the value of ordered normative documentation, explicit
domain boundaries, use cases, contract-first design, ADR and RFC registries,
bounded implementation claims, automated verification and architecture audits.
KGAID adopts those general lessons without requiring KSeF_2-specific choices
such as Hexagonal Architecture, Python, pytest, a particular coverage target,
English as the normative language, or a particular AI product.
