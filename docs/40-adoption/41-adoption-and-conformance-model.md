---
document_id: KGAID-ADP-001
title: KGAID Adoption and Conformance Model

document_type: governance
status: accepted
version: 0.1.0

owner: Governance

approval_status: pending
approved_by:
approved_at:
---

# KGAID Adoption and Conformance Model

## 1. Purpose

This document defines how a software project adopts Knowledge-Governed AI-Assisted Development and how it MAY make a bounded, evidence-based KGAID conformance claim.

It specifies:

- the invariant KGAID core;
- minimal and extended adoption profiles;
- how a project selects a profile and scope;
- how local roles, artifacts, tools, and workflows map to KGAID;
- what tailoring is permitted;
- how deviations and non-applicable requirements are handled;
- which evidence supports conformance;
- how conformance is assessed, declared, maintained, and invalidated;
- how existing projects such as KSeF_2 and 3ksef MAY adopt KGAID without copying the methodology repository.

This model does not create a certification body or guarantee software quality.

## 2. Foundational Rule

> **KGAID conformance is always scoped, versioned, profiled, and evidenced.**

A valid conformance claim MUST identify:

- KGAID version or immutable methodology baseline;
- adoption profile;
- project, product, increment, capability, or organizational scope;
- implementation and knowledge baseline;
- assessment date;
- assessor and authority;
- permitted tailoring;
- unresolved non-conformities;
- evidence supporting the claim;
- expiry or reassessment trigger where applicable.

A statement such as “this project uses KGAID” is an adoption statement, not a conformance claim.

## 3. Adoption and Conformance

KGAID distinguishes:

| Term | Meaning |
| --- | --- |
| **Adoption** | A project intentionally applies selected KGAID principles, models, and practices. |
| **KGAID-aligned** | A project follows important KGAID ideas but has not demonstrated full conformance for a declared profile and scope. |
| **Conformance candidate** | A declared scope has been mapped and prepared for assessment. |
| **KGAID-conformant** | Evidence demonstrates that all applicable mandatory requirements of the declared KGAID baseline and profile are satisfied. |
| **Non-conformant** | One or more applicable mandatory requirements are not satisfied. |
| **Not assessed** | No evidence-based determination has been made. |
| **Certification** | Formal attestation by an authorized certification scheme, which KGAID version 0.1 does not provide. |

A project MAY adopt KGAID partially and describe itself as KGAID-aligned. It MUST NOT claim conformance when mandatory requirements are missing or unassessed.

Permitted tailoring MAY be part of a conformant realization. A deviation that reverses a mandatory KGAID rule is non-conformity, not tailoring.

## 4. Unit and Scope of Conformance

A conformance scope MAY be:

- an entire product;
- one bounded system;
- a capability;
- a delivery increment;
- a release baseline;
- one team or delivery stream;
- an organizational process;
- a limited pilot.

The scope MUST state:

- included products, components, teams, repositories, environments, and time period;
- excluded areas;
- interfaces with excluded areas;
- applicable external obligations;
- whether the claim concerns knowledge, delivery, verification, operation, or their complete chain.

A narrow scope is valid when it is explicit. It MUST NOT be generalized to excluded parts of the project.

An increment-level conformance claim does not prove organization-wide adoption. A process-level claim does not prove that one particular implementation is correct.

## 5. Methodology Baseline

A project MUST pin its conformance claim to an immutable KGAID baseline.

The preferred baseline is a released KGAID version or repository tag.

Before KGAID has a formal release, a project MAY use:

- an immutable KGAID repository commit;
- a recorded list of accepted normative documents and their revisions;
- a signed or otherwise integrity-protected methodology bundle.

Only documents with lifecycle status **Accepted** are normative for the baseline.

Proposed, experimental, explanatory, and example content MAY guide adoption but MUST NOT create mandatory conformance requirements unless explicitly included by the adopting project.

A newer KGAID version does not retroactively invalidate a valid historical claim. Moving a claim to a newer version requires impact analysis and reassessment.

## 6. Invariant KGAID Core

Every KGAID profile MUST preserve the following invariants.

| ID | Core requirement |
| --- | --- |
| **KGAID-C01** | Product purpose, scope, and intended outcomes precede consequential solution commitment. |
| **KGAID-C02** | Relevant business and domain knowledge informs requirements and architecture. |
| **KGAID-C03** | Significant architecture decisions precede implementation that depends on them. |
| **KGAID-C04** | Material contracts precede acceptance of the code that realizes them. |
| **KGAID-C05** | Authoritative knowledge is distinguishable from proposals, observations, assumptions, derived content, and implementation. |
| **KGAID-C06** | Consequential knowledge decisions and risk acceptance remain with properly scoped humans. |
| **KGAID-C07** | AI operates within explicit context, delegation, and escalation boundaries. |
| **KGAID-C08** | Material work is traceable from intent through knowledge, implementation, and evidence. |
| **KGAID-C09** | Claims are bounded and supported by proportionate evidence. |
| **KGAID-C10** | Knowledge, delivery, verification, baseline, release, and outcome status remain distinct. |
| **KGAID-C11** | Material changes perform impact analysis and preserve relevant history. |
| **KGAID-C12** | Implementation and operational discoveries return to the appropriate knowledge owner and lifecycle. |
| **KGAID-C13** | Rigor is proportional to consequence, uncertainty, reversibility, lifetime, and coordination needs. |
| **KGAID-C14** | Tool choice and artifact form do not silently change project meaning or authority. |
| **KGAID-C15** | Tailoring, exclusions, limitations, and non-conformities remain explicit. |

A profile MAY strengthen these requirements. It cannot reverse them.

## 7. Adoption Profiles

KGAID version 0.1 defines two profiles.

### 7.1 KGAID Minimal Profile

The Minimal Profile is intended for small, low-risk, reversible, short-lived, or exploratory work.

It preserves every core invariant while permitting compact realization.

Typical characteristics:

- one person MAY hold several human authorities;
- one concise artifact MAY represent several knowledge concerns;
- identifiers are required only for materially traceable items;
- review MAY be performed by the same human who authored the work when risk permits;
- one repository or work record MAY contain knowledge, implementation, and evidence;
- AI task contracts MAY use a concise structured message;
- verification MAY use a small evidence set;
- conformance MAY be self-assessed;
- baseline and decision records MAY be lightweight.

The Minimal Profile is not permission to:

- omit product purpose;
- implement through unresolved business meaning;
- allow AI to accept its own proposal;
- hide assumptions or limitations;
- infer contracts solely from code where the boundary is material;
- claim completion without appropriate evidence;
- erase history of consequential decisions.

### 7.2 KGAID Extended Profile

The Extended Profile is intended for regulated, security-sensitive, production-critical, distributed, long-lived, high-impact, difficult-to-reverse, or multi-organization systems.

It strengthens control through:

- explicit and separately governed knowledge artifacts;
- stable identifiers and controlled revisions;
- stronger source provenance and applicability records;
- explicit owners and scoped authorities;
- separation of duties;
- specialist review;
- formal architecture and contract governance;
- versioned compatibility and migration;
- structured AI delegation and retained result records;
- stronger bidirectional traceability;
- independent and diverse verification;
- controlled evidence retention and integrity;
- formal knowledge baselines;
- release, rollback, and operational controls;
- explicit residual-risk acceptance;
- periodic conformance reassessment.

Extended does not mean that every artifact MUST be long or every change requires a meeting. It means the control strength and evidence match the consequence.

## 8. Profile Selection

A project SHOULD select the Minimal Profile only when the affected scope has sufficiently low:

- legal, regulatory, contractual, safety, privacy, and security impact;
- financial and user consequence;
- operational criticality;
- external consumer dependency;
- complexity and coordination cost;
- expected lifetime;
- irreversibility;
- uncertainty;
- need for auditability;
- AI execution autonomy and external effects.

The Extended Profile SHOULD be selected when one or more of the following are material:

- binding regulation or formal audit;
- sensitive or protected data;
- security-critical behavior;
- production service continuity;
- significant financial or legal effect;
- several teams or organizations;
- public or versioned external contracts;
- long-lived data or migrations;
- difficult rollback;
- high AI autonomy;
- deployment, communication, or destructive external action;
- need for independent assurance.

A project MAY use a hybrid application:

- Minimal Profile for the general low-risk project flow;
- Extended controls for selected increments, contracts, data, environments, or quality concerns.

The declared conformance scope MUST identify the profile or overlay applicable to each material area. A lower profile cannot be used to bypass a higher applicable obligation.

## 9. Adoption Lifecycle

~~~mermaid
flowchart TD
    A["Orient and select KGAID baseline"] --> B["Define adoption scope"]
    B --> C["Select profile and overlays"]
    C --> D["Map local project model"]
    D --> E["Close mandatory gaps"]
    E --> F["Operate KGAID process"]
    F --> G["Collect conformance evidence"]
    G --> H["Assess and declare"]
    H --> I["Monitor and reassess"]
    I --> B
~~~

### 9.1 Orient

The project identifies why it is adopting KGAID, expected outcomes, sponsor, constraints, and methodology baseline.

### 9.2 Define scope

The project declares included products, capabilities, teams, repositories, environments, and exclusions.

### 9.3 Select profile

Risk and coordination needs determine Minimal, Extended, or a documented hybrid application.

### 9.4 Map local model

Existing roles, artifacts, tools, workflows, and evidence are mapped to KGAID semantics.

### 9.5 Close gaps

Missing mandatory knowledge, authority, traceability, contracts, task delegation, evidence, or learning loops are addressed.

### 9.6 Operate

The project uses the mapped process on real work. Templates alone do not demonstrate adoption.

### 9.7 Collect evidence

Evidence is gathered from actual decisions, increments, AI task contracts, implementation, reviews, verification, baselines, releases, and learning.

### 9.8 Assess and declare

An authorized assessor determines conformance for the declared scope and baseline.

### 9.9 Monitor and reassess

Material project or methodology changes trigger impact review and possible reassessment.

## 10. Local Mapping

An adopting project MAY use any local terminology or tool when it maps the required meaning.

Example:

| KGAID meaning | Possible local realization |
| --- | --- |
| Product Vision | Product brief, charter, vision page. |
| Business Rule | Domain document, rule catalog, acceptance specification. |
| Architecture Decision | ADR, approved RFC, architecture record. |
| Contract | OpenAPI, schema, state model, invariant specification, contract test. |
| Increment | Epic slice, feature increment, change package, release item. |
| AI Execution Task Contract | Structured Codex prompt, agent task record, workflow object. |
| Evidence | CI report, test result, audit record, measurement, review. |
| Human decision | Approval record, signed commit, issue decision, governed workflow transition. |
| Knowledge baseline | Repository tag, signed manifest, release knowledge bundle. |
| Learning | Incident review, metric analysis, feedback record, lesson artifact. |

A mapping MUST state:

- local representation;
- owner;
- authority;
- lifecycle;
- source of truth;
- trace relationships;
- evidence of use.

Renaming is allowed. Loss of meaning is not.

## 11. Tailoring

Tailoring adapts KGAID realization to project context without reversing its principles or mandatory semantics.

### 11.1 Permitted tailoring

A project MAY:

- rename roles and artifacts;
- combine several knowledge concerns in one artifact;
- split one KGAID concern across several tools or records;
- automate lifecycle transitions under accepted policy;
- choose different review and approval mechanics;
- vary artifact depth;
- use local identifiers;
- omit a condition proven not applicable;
- add stronger organizational, regulatory, security, or quality controls;
- use different AI collaboration topology;
- choose its delivery cadence and planning method.

### 11.2 Tailoring requiring explicit record

A project SHOULD record rationale, scope, authority, risk, and compensating controls when it:

- combines proposal, decision, and evidence in one record;
- assigns several authorities to one person;
- uses self-review for consequential work;
- omits a normally expected artifact or gate;
- reduces evidence independence;
- permits AI external actions;
- uses temporary assumptions to authorize realization;
- cannot maintain a preferred trace relationship;
- applies the Minimal Profile near an Extended trigger.

### 11.3 Prohibited tailoring

A project MUST NOT claim KGAID conformance while tailoring that:

- gives AI final human decision or risk authority;
- treats implementation as automatically authoritative;
- removes the business-before-architecture dependency;
- allows significant architecture to emerge without governed decision;
- accepts material code without an applicable contract;
- treats task completion as verification or release;
- permits claims broader than evidence;
- hides negative or missing evidence;
- erases consequential decision history;
- makes unresolved deviations invisible;
- labels non-applicable a requirement that is merely inconvenient.

## 12. Applicability and Non-Applicable Requirements

A mandatory conditional requirement MAY be marked **not applicable** only when:

- the triggering condition is absent from the declared scope;
- the rationale is explicit;
- the responsible authority accepts the determination;
- related risks and interfaces are considered;
- the conclusion has a reassessment trigger.

Example:

A migration plan MAY be not applicable when the increment introduces no persistent data, existing consumers, or state transition. It is not non-applicable merely because migration has not yet been designed.

When applicability is uncertain, the requirement remains open or a human Risk Authority accepts a bounded temporary assumption.

## 13. Deviations and Non-Conformities

| Classification | Meaning | Effect on claim |
| --- | --- | --- |
| **Equivalent realization** | Different form preserves required semantics. | Conformant. |
| **Permitted tailoring** | Explicit adaptation allowed by KGAID. | Conformant when evidenced. |
| **Accepted temporary deviation** | Mandatory requirement is not currently satisfied, with owner, risk, remediation, and expiry. | Scope is not fully conformant until resolved unless the declared claim explicitly excludes the affected scope. |
| **Non-conformity** | Applicable mandatory requirement is not satisfied. | Conformance claim is false for affected scope. |
| **Observation** | Improvement opportunity that does not violate a requirement. | Does not block conformance. |
| **Unknown** | Assessment lacks sufficient evidence. | Cannot be treated as conformant. |

Risk acceptance does not convert non-conformity into conformance. It MAY authorize operation while the conformance status remains accurate.

A deviation record SHOULD identify:

- requirement;
- affected scope;
- reason;
- consequence and risk;
- authority;
- compensating control;
- remediation;
- expiry or review trigger;
- evidence;
- status.

## 14. Conformance Requirements

The following requirements specialize the invariant core for assessment.

| ID | Requirement | Minimum evidence |
| --- | --- | --- |
| **KGAID-R01 Baseline** | KGAID version or immutable methodology baseline is declared. | Tag, commit, or accepted-document manifest. |
| **KGAID-R02 Scope** | Conformance scope, exclusions, interfaces, profile, and assessment period are declared. | Adoption declaration. |
| **KGAID-R03 Principles** | Local process does not reverse accepted KGAID principles. | Mapping and assessment review. |
| **KGAID-R04 Knowledge** | Material knowledge has identifiable status, owner, provenance, and authority. | Representative accepted artifacts. |
| **KGAID-R05 Product and domain** | Product intent and relevant business meaning precede solution commitment. | Vision, rules, requirements, decision chronology. |
| **KGAID-R06 Architecture and contracts** | Significant architecture and material contracts precede dependent implementation acceptance. | ADRs, architecture records, contracts, revisions. |
| **KGAID-R07 Human authority** | Consequential decisions and risk acceptance are made by scoped humans. | Decision and authority records. |
| **KGAID-R08 AI collaboration** | Material AI work has context, delegation, boundaries, review, and escalation. | Collaboration or task contract records. |
| **KGAID-R09 Increment** | Material delivery uses a bounded increment with readiness, scope, criteria, and state separation. | Increment artifact and status evidence. |
| **KGAID-R10 Traceability** | Critical paths connect intent, knowledge, implementation, evidence, and decision. | Trace matrix or navigable links. |
| **KGAID-R11 Verification** | Claims are explicit and supported by bounded evidence. | Claim and Evidence artifacts. |
| **KGAID-R12 State semantics** | Knowledge, implementation, verification, baseline, release, and outcome states are not conflated. | Status model and representative records. |
| **KGAID-R13 Change** | Material changes perform impact analysis and preserve history. | Change, supersession, and impact records. |
| **KGAID-R14 Learning** | Verification and operational learning return to knowledge owners. | Learning, incident, feedback, or updated artifact chain. |
| **KGAID-R15 Tailoring** | Tailoring, applicability, deviations, and non-conformities are explicit. | Tailoring and assessment records. |
| **KGAID-R16 Conformance evidence** | The assessment conclusion is supported by retained evidence and limitations. | Assessment report and evidence index. |

All requirements apply to both profiles. Profile selection changes required depth, independence, and formality.

## 15. Profile Evidence Expectations

| Concern | Minimal Profile | Extended Profile |
| --- | --- | --- |
| Baseline | Commit, tag, or document list. | Controlled, integrity-protected methodology and project baseline. |
| Scope | Concise declared boundary. | Formal boundary including interfaces, environments, teams, and period. |
| Roles | Combined roles allowed and named. | Explicit scoped authorities and separation of duties. |
| Artifacts | Concise or combined records. | Stable identifiers, controlled revisions, stronger provenance. |
| Decisions | Human decision visible. | Formal authority, review, alternatives, risk, and acceptance record. |
| Architecture and contracts | Material decisions and obligations explicit. | Versioned governance, compatibility, migration, specialist review. |
| AI delegation | Bounded structured message MAY suffice. | Controlled task contract, permissions, retained evidence, external-action policy. |
| Traceability | Navigable critical path. | Strong bidirectional traceability and impact analysis. |
| Verification | Proportionate evidence with limitations. | Independent, diverse, reproducible evidence with controlled retention. |
| Baseline and release | Lightweight binding and human decision. | Formal baseline, release authority, rollback, operations, residual risk. |
| Assessment | Self-assessment permitted. | Independent internal or external assessment recommended or required by obligation. |
| Reassessment | On material change. | Periodic and event-driven reassessment. |

## 16. Conformance Evidence Package

A conformance evidence package SHOULD contain:

1. adoption and conformance declaration;
2. KGAID methodology baseline;
3. scope and profile;
4. local terminology and artifact mapping;
5. role and authority mapping;
6. tailoring and applicability record;
7. deviations and non-conformities;
8. requirement-to-evidence matrix;
9. representative critical trace paths;
10. representative increments and AI task contracts;
11. verification and evidence examples;
12. baseline, release, and learning examples where applicable;
13. assessment method and sampling;
14. assessment findings;
15. decision, limitations, validity period, and reassessment triggers.

The package SHOULD prefer links to authoritative project evidence rather than copied snapshots when links remain durable and access is controlled.

One successful increment MAY demonstrate an increment-level claim. It does not automatically demonstrate project-wide conformance.

## 17. Assessment Methods

A project MAY use:

| Method | Description |
| --- | --- |
| **Self-assessment** | Project members evaluate their own scope. |
| **Independent internal assessment** | A person or team outside the assessed delivery context evaluates evidence. |
| **Peer assessment** | Another KGAID-adopting project or practitioner evaluates the scope. |
| **External assessment** | An independent external party evaluates conformance. |
| **Continuous assessment** | Accepted automation and periodic human review monitor selected requirements. |

The assessment method MUST be declared.

Independence SHOULD be proportional to the consequence of the conformance claim. A public, regulatory, contractual, or high-risk claim SHOULD NOT rely only on undocumented self-assessment.

KGAID version 0.1 defines no accredited certifier, conformity mark, or certification authority.

## 18. Assessment Process

~~~mermaid
flowchart TD
    A["Confirm baseline, profile, and scope"] --> B["Review local mapping"]
    B --> C["Evaluate each requirement"]
    C --> D["Inspect representative evidence"]
    D --> E["Record findings and gaps"]
    E --> F["Resolve or classify gaps"]
    F --> G["Human conformance decision"]
    G --> H["Publish bounded declaration"]
    H --> I["Monitor validity"]
~~~

The assessor SHOULD:

1. verify that the declared baseline is immutable;
2. validate scope and exclusions;
3. confirm profile selection;
4. evaluate every applicable KGAID-R requirement;
5. inspect actual project use rather than templates alone;
6. trace representative work from intent to evidence and decision;
7. inspect AI delegation and human authority;
8. inspect negative, missing, and invalidated evidence;
9. record equivalent realizations and tailoring;
10. classify gaps;
11. state sampling and limitations;
12. issue a bounded conclusion.

An unanswered mandatory requirement is not a pass.

## 19. Conformance Status Lifecycle

| Status | Meaning |
| --- | --- |
| **not-assessed** | No assessment exists. |
| **adopting** | Project is mapping KGAID and closing gaps. |
| **candidate** | Evidence package is ready for assessment. |
| **conformant** | All applicable mandatory requirements are satisfied for the declared scope and baseline. |
| **non-conformant** | At least one applicable mandatory requirement is not satisfied. |
| **suspended** | A material event makes the current claim unreliable pending reassessment. |
| **expired** | Validity period or review trigger passed. |
| **superseded** | A newer conformance declaration replaces the current one. |

A conformant status MUST identify its evidence package and decision authority.

A suspended, expired, or superseded declaration remains part of project history but MUST NOT be represented as current.

## 20. Declaration Template

~~~markdown
# KGAID Adoption and Conformance Declaration

## Identity

- Project or product:
- Declaration ID:
- Declaration revision:
- Date:
- Status:

## KGAID baseline

- KGAID version, tag, or commit:
- Accepted normative documents:

## Scope

### Included

### Excluded

### Interfaces with excluded scope

### Assessment period

## Profile

- Base profile:
- Extended overlays:
- Profile rationale:

## Local mapping

| KGAID meaning | Local realization | Owner | Source of truth |
| --- | --- | --- | --- |

## Authorities

| KGAID authority | Person or local role | Scope |
| --- | --- | --- |

## Tailoring and applicability

| Requirement or practice | Realization or N/A | Rationale | Authority |
| --- | --- | --- | --- |

## Deviations and non-conformities

| ID | Requirement | Scope | Classification | Risk | Owner | Due or expiry |
| --- | --- | --- | --- | --- | --- | --- |

## Requirement assessment

| Requirement | Result | Evidence | Limitation |
| --- | --- | --- | --- |

## Assessment

- Method:
- Assessor:
- Independence:
- Sampling:
- Findings:
- Limitations:

## Conformance decision

- Decision:
- Decided by:
- Declared scope:
- KGAID baseline:
- Profile:
- Unresolved exclusions:
- Valid until:
- Reassess when:

## Evidence package

- Evidence index:
- Integrity or baseline reference:
~~~

## 21. Conformance Claim Format

A concise conformance claim SHOULD use this form:

> **Project or scope** conforms to **KGAID baseline**, **profile**, for **declared boundary and period**, based on **assessment and evidence package**, subject to **listed limitations and validity conditions**.

Example:

> Capability X, increments INC-010 through INC-014, conforms to KGAID commit abc123, Minimal Profile with Extended security controls, for repository and integration environment revisions baselined on YYYY-MM-DD, based on assessment AUD-004, excluding production operations and product-outcome validation.

The example is illustrative and does not assert actual conformance.

A project MUST NOT use the KGAID name or badge-like language to imply certification, endorsement, or guarantee that does not exist.

## 22. Continuous Conformance

Conformance is maintained through normal project work rather than reconstructed only before an assessment.

Projects SHOULD:

- create traceability as artifacts are produced;
- retain human decisions;
- version contracts and baselines;
- preserve AI task delegation and results proportionately;
- link evidence to claims;
- record tailoring and deviations when decided;
- monitor invalidation triggers;
- route operational learning;
- assess high-risk increments before release;
- review the declared profile when risk changes.

Automation MAY monitor structural indicators such as:

- missing ownership or status;
- broken trace links;
- absent task authorization;
- evidence referring to stale revisions;
- expired deviations;
- missing human decisions;
- conformance baseline drift.

Automation MAY identify or update pre-authorized findings. It cannot make the final human conformance decision or hide semantic gaps behind structural completeness.

## 23. Reassessment Triggers

A conformance declaration SHOULD be reassessed when:

- KGAID baseline changes;
- product or conformance scope changes materially;
- selected profile is no longer proportionate;
- organization or authority model changes;
- significant architecture or contract changes;
- AI collaboration or autonomy changes materially;
- new external, destructive, or production actions are delegated;
- verification strategy changes;
- a critical incident or audit finding challenges conformance;
- evidence is invalidated;
- a temporary deviation expires;
- a new legal, regulatory, contractual, security, or privacy obligation applies;
- validity period ends.

Reassessment MAY be limited to the affected requirements and scope when impact analysis supports that boundary.

## 24. Existing Project Adoption

### 24.1 KSeF_2

KSeF_2 is an empirical source from which KGAID was generalized. It is not automatically KGAID-conformant.

To make a claim, KSeF_2 SHOULD:

1. select an immutable KGAID baseline;
2. declare the assessed system, increments, repositories, and environments;
3. select a profile;
4. map existing KSeF_2 artifacts and roles to KGAID;
5. identify gaps created before KGAID terminology existed;
6. assess representative critical trace paths;
7. record tailoring and non-conformities;
8. produce an evidence-backed declaration.

Existing ADRs, RFCs, use cases, contracts, tests, and execution patterns MAY provide evidence. Historical influence alone is not conformance.

### 24.2 3ksef and future projects

A new project SHOULD adopt KGAID prospectively:

1. pin the methodology baseline at project start;
2. create its local mapping and authority model;
3. select profile by risk;
4. use KGAID identifiers and relationships where valuable;
5. shape increments and AI task contracts from accepted knowledge;
6. collect evidence during delivery;
7. baseline and assess the first representative increment;
8. expand the claim only after evidence supports broader scope.

An adopting project SHOULD reference KGAID rather than copy normative files into its repository unless offline, regulatory, or integrity needs require a controlled copy.

Project-specific extensions remain owned by the adopting project. They do not change KGAID core unless separately proposed and accepted in the KGAID repository.

## 25. Failure Signals

The following indicate likely adoption or conformance failure:

- the project claims KGAID without a version, profile, scope, or evidence;
- templates exist but are not used in real delivery;
- local names are mapped without preserving authority or lifecycle meaning;
- the Minimal Profile is selected only to avoid controls required by risk;
- AI is listed as a decision authority;
- code or tests are treated as the sole authoritative knowledge;
- all work is marked done with one status;
- missing evidence is treated as not applicable;
- risk acceptance is used to label non-conformity as conformant;
- one successful increment is generalized to the whole project;
- an assessor inspects file presence but not actual trace paths and decisions;
- deviations have no owner, expiry, or reassessment trigger;
- a stale declaration remains current after major project change;
- KSeF_2 is called conformant merely because it inspired KGAID;
- a project implies external certification or endorsement that KGAID does not provide.

## 26. Conformance

This adoption model is satisfied when an adopting project:

- pins an immutable KGAID baseline;
- declares profile and bounded scope;
- preserves every invariant core requirement;
- maps local roles, artifacts, tools, and workflows to KGAID semantics;
- applies rigor proportionate to risk;
- records tailoring and applicability;
- identifies deviations, non-conformities, owners, risk, and expiry;
- evaluates every applicable KGAID-R requirement;
- provides evidence from actual project work;
- keeps AI execution and human authority distinct;
- preserves traceability from intent to evidence and decision;
- uses an assessment method appropriate to the claim;
- issues a bounded declaration without implying certification;
- monitors invalidation and reassessment triggers;
- keeps historical declarations and supersession;
- expands conformance claims only when broader evidence exists.

Conformance does not require a particular repository layout, tool, document format, organization chart, delivery framework, programming language, AI provider, or certification scheme.
