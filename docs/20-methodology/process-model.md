# KGAID Process Model

**Status:** Accepted  
**Version:** 0.1  
**Project:** Knowledge-Governed AI-Assisted Development  
**Accepted:** 2026-07-18  
**Accepted by:** Krzysztof Olejnik — KGAID Methodology Owner  
**Depends on:** [KGAID Scope and Boundaries](../00-foundations/scope-and-boundaries.md), [KGAID Principles](../00-foundations/principles.md), [KGAID Knowledge Architecture](../10-knowledge-architecture/README.md), [KGAID Knowledge Lifecycle](../10-knowledge-architecture/knowledge-lifecycle.md), [KGAID Knowledge Authority Model](../10-knowledge-architecture/authority-model.md)  
**Realizes principles:** P1–P12  
**Operationalized by:** [KGAID Delivery Increment Model](delivery-increment-model.md)

## 1. Purpose

This document defines the universal KGAID process from an initial product stimulus to a working, verified, and evolving system.

It explains:

- how product, domain, requirements, architecture, contracts, implementation, verification, and operations relate;
- what must be known before a consequential downstream commitment is made;
- where human decisions are required;
- how AI may support each part of the work;
- how an increment becomes ready for implementation, verification, and release;
- how discoveries and operational evidence return to earlier knowledge.

The process is independent of delivery framework, programming language, architecture style, repository platform, workflow tool, organization size, and AI provider.

## 2. Process Character

KGAID is an iterative, evidence-driven process with ordered dependencies.

It is not a mandatory sequence of project phases. Discovery, design, implementation, and verification may overlap when their scope and uncertainty are explicit. Several capabilities or increments may progress concurrently.

Concurrency does not remove dependency of meaning:

~~~mermaid
flowchart TD
    A["Product purpose"] --> B["Business and domain knowledge"]
    B --> C["Requirements and quality"]
    C --> D["Architecture"]
    D --> E["Contracts"]
    E --> F["Implementation"]
    F --> G["Evidence and operation"]
    G --> A
~~~

A downstream artifact may challenge upstream knowledge, but it MUST NOT silently redefine it. A material discovery returns to the appropriate knowledge owner and decision authority.

The arrows express semantic dependency, not a waterfall schedule.

## 3. Three Nested Cycles

KGAID operates through three nested cycles.

### 3.1 Product learning cycle

The product learning cycle evaluates whether the system produces the intended outcomes in its actual environment.

~~~mermaid
flowchart LR
    A["Vision and outcomes"] --> B["Capabilities"]
    B --> C["Working system"]
    C --> D["Operational evidence"]
    D --> E["Learning"]
    E --> A
~~~

Its unit of change is a product direction, capability, or material change in outcome.

### 3.2 Delivery increment cycle

The delivery increment cycle transforms an accepted, bounded need into a verified realization.

~~~mermaid
flowchart TD
    A["Frame increment"] --> B["Establish upstream knowledge"]
    B --> C["Decide architecture and contracts"]
    C --> D["Realize"]
    D --> E["Verify"]
    E --> F["Baseline or release"]
    F --> G["Observe"]
    G --> A
~~~

Its unit of flow is a **delivery increment**: a coherent, bounded change that can be evaluated against explicit acceptance criteria.

### 3.3 Artifact knowledge cycle

Every material knowledge artifact follows the accepted [KGAID Knowledge Lifecycle](../10-knowledge-architecture/knowledge-lifecycle.md):

~~~text
capture
→ analyze
→ propose
→ review
→ human decision
→ accept
→ realize
→ verify
→ learn
~~~

The process model does not replace the artifact lifecycle. It composes multiple artifact lifecycles into product and delivery work.

## 4. Units of Work

KGAID distinguishes four units that may evolve at different speeds.

| Unit | Meaning | Typical result |
| --- | --- | --- |
| **Product** | The enduring value proposition and system boundary. | Vision, outcomes, product boundaries, operational learning. |
| **Capability** | A coherent ability the product must provide. | Capability definition, use cases, quality expectations. |
| **Delivery increment** | A bounded change selected for realization and verification. | Implemented and evidenced change. |
| **Knowledge artifact** | One governed unit of meaning. | Requirement, decision, contract, evidence, learning, or another KGAID artifact. |

A project MUST NOT use completion of one unit as an unsupported completion claim for another. For example:

- an accepted requirement does not mean the capability is implemented;
- implemented code does not mean the increment is verified;
- a verified increment does not mean the product outcome has been achieved;
- one successful experiment does not establish general production readiness.

## 5. End-to-End Process

The default process contains nine concerns. They may overlap and repeat, but their exit conditions constrain downstream commitment.

| ID | Concern | Primary question | Principal result |
| --- | --- | --- | --- |
| **PM-1** | Orient | What triggered work, and why might it matter? | Classified trigger and investigation scope. |
| **PM-2** | Frame product or change | What outcome and boundary should guide decisions? | Accepted intent, scope, constraints, and success measures. |
| **PM-3** | Discover business and domain | What business meaning and rules govern the problem? | Shared terminology, rules, actors, scenarios, and unknowns. |
| **PM-4** | Define requirements and quality | What must be true of the system and result? | Accepted requirements, quality expectations, and acceptance criteria. |
| **PM-5** | Shape architecture | Which significant structural decisions enable the requirements? | Accepted boundaries, responsibilities, strategies, and decisions. |
| **PM-6** | Establish contracts | What observable obligations must implementations satisfy? | Accepted contracts and compatibility expectations. |
| **PM-7** | Realize increment | How will accepted knowledge become a working change? | Integrated implementation and implementation record. |
| **PM-8** | Verify and baseline | What exact claims does evidence support? | Evidence, limitations, residual risk, and coherent baseline. |
| **PM-9** | Operate and learn | What does actual use teach us? | Observations, incidents, measurements, and proposed learning. |

## 6. Process Concerns

### 6.1 PM-1 — Orient

**Purpose:** Turn a stimulus into a visible and correctly routed knowledge item.

A trigger may originate from product vision, an external obligation, user feedback, an opportunity, a defect, an incident, a risk, a dependency change, a verification failure, or a human or AI proposal.

**Required work:**

1. capture the trigger and provenance;
2. distinguish observation, claim, inference, assumption, and recommendation;
3. identify potentially affected scope;
4. identify an initial owner;
5. decide whether to reject, investigate, defer, or frame work.

**Exit condition:** The trigger has an owner, classification, provenance, initial scope, and explicit next action.

AI MAY classify and correlate triggers. A human authority MUST decide whether a trigger changes product direction, priority, obligation, or accepted risk.

### 6.2 PM-2 — Frame product or change

**Purpose:** Establish why the work should exist and what outcome bounds it.

For a new product, framing SHOULD establish:

- vision and problem statement;
- stakeholders and users;
- desired outcomes and success measures;
- product boundary and non-goals;
- material constraints;
- assumptions, unknowns, and risks.

For an increment, framing SHOULD establish:

- relationship to an accepted outcome or obligation;
- included and excluded behavior;
- affected capabilities and stakeholders;
- intended value or learning;
- urgency and priority;
- preliminary acceptance boundary.

**Exit condition:** The Product Authority has accepted the purpose, scope, outcome, and known material constraints at a depth proportionate to commitment.

Exploratory work MAY proceed without a fully accepted solution scope when it is explicitly labeled as learning, remains reversible, and cannot create an unauthorized product or release claim.

### 6.3 PM-3 — Discover business and domain

**Purpose:** Build the business knowledge from which requirements and architecture derive.

Discovery SHOULD identify:

- authoritative terminology;
- actors, responsibilities, and external parties;
- business rules and invariants;
- processes, events, and state;
- capabilities, use cases, and scenarios;
- exceptions and failure cases;
- external obligations and sources;
- disputed meanings, assumptions, and unknowns.

**Exit condition:** The business meaning necessary for the increment is accepted or explicitly bounded by recorded assumptions, and unresolved conflicts do not invalidate downstream work.

Completeness is scoped. A project does not need a complete model of the entire domain before delivering one capability.

AI MAY extract terms, compare sources, generate scenarios, and find contradictions. Domain meaning and applicable business rules require the proper human authority.

### 6.4 PM-4 — Define requirements and quality

**Purpose:** Translate product and domain knowledge into testable obligations.

Required knowledge MAY include:

- functional requirements;
- quality requirements;
- security, privacy, legal, and compliance constraints;
- data and retention obligations;
- compatibility and migration expectations;
- operational and observability expectations;
- acceptance criteria;
- explicit exclusions and limitations.

Requirements MUST:

- relate to accepted upstream purpose or obligation;
- identify their scope and owner;
- distinguish mandatory behavior from preference;
- be verifiable at a declared boundary;
- avoid embedding unnecessary implementation choices.

**Exit condition:** Requirements and acceptance criteria are accepted for the intended increment, material conflicts are resolved, and a viable verification approach exists.

### 6.5 PM-5 — Shape architecture

**Purpose:** Make the significant decisions required to satisfy accepted business and quality needs.

Architecture work SHOULD address, as relevant:

- system and context boundaries;
- ownership and responsibilities;
- component or service boundaries;
- data ownership and lifecycle;
- interactions and dependencies;
- security and trust boundaries;
- failure, recovery, and consistency strategies;
- deployment and operational constraints;
- significant alternatives and trade-offs;
- compatibility and evolution.

An architectural decision is required when a choice materially affects product capability, business meaning, system ownership, quality attributes, security, compatibility, long-term cost, reversibility, or several independent implementations.

**Exit condition:** The significant architectural decisions needed by the increment are accepted, their rationale and consequences are visible, and no unresolved architecture conflict invalidates the intended contracts or realization.

Implementation MAY inform architecture through prototypes or experiments. Experimental code MUST be labeled and MUST NOT silently establish normative architecture.

### 6.6 PM-6 — Establish contracts

**Purpose:** Define observable obligations that allow work to be implemented and verified independently.

A contract MAY govern:

- API or message interaction;
- data structure and semantics;
- component or module behavior;
- workflow and state transition;
- error and failure behavior;
- performance, availability, durability, or security;
- compatibility and versioning;
- human interaction or operational procedure.

A material contract SHOULD specify:

- owner and consumers;
- scope and version;
- inputs, outputs, preconditions, and postconditions;
- invariants and failure semantics;
- quality guarantees;
- compatibility and evolution rules;
- verification criteria;
- known limitations.

**Exit condition:** Material contracts are accepted by the relevant authorities, consumers can interpret them consistently, and the verification method is defined.

Schemas, examples, tests, and generated clients MAY represent a contract. The project MUST identify which representation owns meaning and how derived representations remain synchronized.

### 6.7 PM-7 — Realize increment

**Purpose:** Convert accepted knowledge into an integrated, reviewable system change.

Before implementation commitment, the affected scope MUST satisfy the realization readiness conditions in Section 7.

Realization may include code, configuration, infrastructure, data migration, generated artifacts, operational procedures, documentation, and test assets.

During realization:

- local, reversible decisions MAY be delegated to humans or AI;
- implementation MUST remain within accepted requirements, architecture, contracts, and risk boundaries;
- material discoveries MUST be captured and routed upstream;
- scope-changing decisions MUST NOT be concealed as implementation details;
- derived knowledge SHOULD be updated from its authoritative source;
- traceability and evidence hooks SHOULD be created with the change.

**Exit condition:** The declared increment is integrated and reviewable, required implementation work is complete, discovered scope conflicts are resolved or removed from the increment, and verification can execute against the intended subject.

### 6.8 PM-8 — Verify and baseline

**Purpose:** Determine what claims the realized increment can support and bind them to reproducible evidence.

Verification MUST compare the realization with accepted requirements, architecture constraints, contracts, acceptance criteria, security and quality expectations, and operational readiness criteria.

Evidence MUST identify:

- the exact claim;
- subject and version;
- environment and boundary;
- method and result;
- limitations and exclusions;
- responsible actor and date;
- reproducibility where relevant.

A failure MAY require implementation correction, upstream clarification, architecture revision, risk treatment, limitation of the claim, or removal of scope from the increment.

A knowledge baseline binds:

- accepted knowledge revisions;
- implementation revision;
- applicable contracts;
- verification evidence;
- known limitations;
- unresolved and accepted residual risks.

**Exit condition:** Every completion or release claim is supported by proportionate evidence, the baseline is internally consistent, and authorized humans have accepted the claim and residual risk within their scope.

A baseline does not imply that the product is complete or that all possible qualities have been proven.

### 6.9 PM-9 — Operate and learn

**Purpose:** Evaluate the system in actual use and convert observations into governed learning.

Operations may supply product outcome measures, usage data, service-level results, incidents, security events, user feedback, support patterns, performance and cost observations, dependency changes, and disproven assumptions.

Operational evidence MUST retain its environment, time range, version, and limitations.

Learning MAY validate the current direction, create an opportunity, reveal a missing requirement, challenge an assumption, require architecture or contract change, invalidate evidence, create corrective work, or retire obsolete knowledge.

**Exit condition:** Material learning has been routed to the owner of affected knowledge and either rejected with rationale, retained for monitoring, or entered into a new proposal cycle.

Learning does not update normative knowledge automatically.

## 7. Realization Readiness

An increment is realization-ready when, proportionate to its risk:

- purpose and bounded scope are accepted;
- relevant business rules and terminology are stable enough for the commitment;
- applicable requirements and acceptance criteria are accepted;
- significant architectural decisions are accepted;
- material contracts are accepted;
- dependencies and affected consumers are identified;
- assumptions, risks, and unresolved questions are visible;
- compatibility and migration needs are addressed;
- the verification approach is feasible;
- required authorities are identified;
- no unresolved conflict invalidates the planned realization.

This corresponds to knowledge gate **KG-4 Realization Ready**.

Readiness applies to the affected scope, not necessarily the whole product. A project MAY begin one ready increment while another remains in discovery.

When an authorized human accepts reduced readiness, the decision MUST record:

- the missing knowledge;
- why proceeding is justified;
- the limited scope;
- compensating controls;
- accepted risk;
- the trigger for reevaluation.

AI cannot accept reduced readiness or its associated risk.

## 8. Process Checkpoints

KGAID checkpoints are semantic conditions, not mandatory meetings or ceremonies.

| Checkpoint | Required result | Primary human authority |
| --- | --- | --- |
| **PC-1 Direction** | Purpose, outcome, boundary, and material constraints accepted. | Product Authority. |
| **PC-2 Business Meaning** | Relevant domain meaning and rules accepted or explicitly bounded. | Domain Authority. |
| **PC-3 Obligation** | Requirements, quality expectations, and acceptance criteria accepted. | Product, Requirements, and applicable specialist authorities. |
| **PC-4 Design** | Significant architectural decisions and material contracts accepted. | Architecture, Contract, Domain, Security, and Compliance authorities as applicable. |
| **PC-5 Realization Ready** | The affected increment satisfies Section 7. | Applicable upstream authorities and Delivery Authority. |
| **PC-6 Implementation Complete** | Declared realization is integrated without unresolved scope-changing conflict. | Delivery Authority. |
| **PC-7 Claim Verified** | Evidence supports the exact declared claim. | Verification Authority. |
| **PC-8 Baseline or Release** | Knowledge, system, evidence, limitations, and residual risk form an accepted baseline. | Baseline, Product, Operations, and Risk authorities as applicable. |
| **PC-9 Learning Routed** | Material operational learning has an owner and explicit disposition. | Owner of affected normative knowledge. |

A checkpoint:

- MAY be automated when its policy and evidence interpretation were accepted by humans;
- MAY be concise for low-risk work;
- MAY require independent review for high-risk work;
- blocks only the affected claim or scope;
- MUST NOT be passed by renaming missing knowledge or lowering a claim without authority.

## 9. Human and AI Collaboration

| Process concern | AI may contribute | Humans remain accountable for |
| --- | --- | --- |
| Orient | Classify triggers, find related knowledge, identify gaps. | Relevance, ownership, priority, and obligation. |
| Frame | Draft problem statements, outcomes, assumptions, and alternatives. | Product intent, scope, priority, and accepted constraints. |
| Discover | Extract terminology and rules, compare sources, generate scenarios. | Domain correctness and source applicability. |
| Requirements | Draft requirements, criteria, edge cases, and quality concerns. | Accepted obligations and trade-offs. |
| Architecture | Generate options, evaluate consequences, model risks. | Significant decisions and accepted architecture risk. |
| Contracts | Draft schemas, examples, invariants, and compatibility analysis. | Contract meaning and consumer obligations. |
| Realize | Implement, refactor, review, generate tests, run tools. | Scope-changing decisions and delegated boundaries. |
| Verify | Execute checks, collect evidence, detect unsupported claims. | Adequacy of evidence, residual risk, and release claim. |
| Operate | Analyze telemetry, incidents, feedback, and patterns. | Interpretation, response, and changes to normative knowledge. |

AI MUST stop and request human direction when it would otherwise:

- define or change product intent;
- choose between materially different business meanings;
- accept a requirement or contract;
- make or supersede a significant architecture decision;
- weaken security, privacy, compliance, compatibility, or evidence scope;
- accept residual risk;
- establish a normative baseline or release claim;
- treat its own proposal as accepted.

AI need not interrupt for routine, reversible, local choices already constrained by accepted knowledge and explicit delegation.

## 10. Feedback and Return Rules

Returning to earlier work is normal when knowledge changes.

| Discovery | Required return |
| --- | --- |
| Product outcome or boundary is unclear or changed. | PM-2 Frame. |
| Business term, rule, actor, or scenario is disputed. | PM-3 Discover. |
| Requirement is missing, contradictory, or unverifiable. | PM-4 Requirements. |
| Boundary, responsibility, dependency, or quality strategy must change. | PM-5 Architecture. |
| Observable obligation or compatibility semantics must change. | PM-6 Contracts. |
| Realization does not satisfy accepted knowledge. | PM-7 Realize, unless upstream knowledge is challenged. |
| Evidence cannot support the intended claim. | PM-4 through PM-8 according to cause. |
| Operation disproves an assumption or reveals a new need. | PM-1 Orient and the affected upstream concern. |

The actor discovering the issue MUST:

1. record the discovery and affected scope;
2. stop relying on the disputed claim within that scope;
3. link the affected artifacts and implementation;
4. identify the appropriate owner and decision authority;
5. continue only work that remains valid and cannot conceal the conflict.

A return loop is a correction mechanism, not process failure.

## 11. Concurrency and Exploration

Several increments MAY proceed concurrently when:

- each has a bounded scope;
- shared authoritative knowledge is identifiable;
- dependencies and contract versions are explicit;
- changes to shared upstream knowledge trigger impact analysis;
- evidence and completion claims remain increment-specific;
- unresolved conflicts are not hidden by branch or team boundaries.

A project MAY use spikes, prototypes, simulations, or temporary adapters to reduce uncertainty. Such work MUST identify:

- its learning question;
- time or scope limit;
- assumptions;
- whether its output is disposable;
- evidence required to retain any conclusion;
- the human decision needed before production use.

Exploration is not realization unless it passes the applicable knowledge, contract, verification, and authority conditions.

## 12. Completion Semantics

KGAID distinguishes the following claims:

| Claim | Meaning |
| --- | --- |
| **Knowledge accepted** | An authorized human accepted the declared artifact and scope. |
| **Realization ready** | Accepted upstream knowledge is sufficient for implementation commitment. |
| **Implemented** | The declared change exists in the identified implementation revision. |
| **Verified** | Evidence supports a specific claim within a declared boundary. |
| **Baselined** | Accepted knowledge, implementation, evidence, limitations, and risk form a coherent reference. |
| **Released** | An authorized release decision applied to an identified baseline and environment. |
| **Outcome achieved** | Operational evidence supports an accepted product success measure. |

These claims MUST NOT be used interchangeably.

An increment is complete only relative to its declared completion claim. “Done” without scope, baseline, and evidence is not a KGAID completion statement.

## 13. Minimal and Extended Application

### 13.1 Minimal application

For small, reversible, low-risk work, one concise artifact or change record MAY cover several process concerns.

At minimum it SHOULD identify:

- purpose and scope;
- relevant business rule or assumption;
- acceptance criteria;
- significant decision or explicit statement that none is required;
- material contract or boundary;
- implementation change;
- verification result and limitation;
- human acceptance where consequential.

One person MAY hold several authorities, but the capacity in which each consequential decision is made should remain clear.

### 13.2 Extended application

For high-risk, regulated, security-sensitive, distributed, or long-lived systems, application SHOULD include:

- separate authoritative artifacts for major concerns;
- formal source and applicability records;
- independent specialist review;
- explicit decision and risk authority;
- controlled contract versioning and migration;
- stronger bidirectional traceability;
- reproducible evidence retention;
- separation of duties;
- formal baseline and release approval;
- operational controls and incident learning.

The process meaning remains the same across profiles. Only necessary depth, formality, and separation change.

## 14. Process Health Signals

A healthy KGAID process shows that:

- people can explain current work in terms of product outcome;
- domain meaning is stable where downstream commitment depends on it;
- decisions and contracts are discoverable before implementation relies on them;
- implementation discoveries return to knowledge owners;
- critical trace paths remain navigable;
- evidence descriptions match the claims they support;
- AI contributions expose assumptions and remain within delegated authority;
- blocked scope is visible without unnecessarily stopping unrelated work;
- operational feedback changes knowledge through explicit decisions;
- process cost remains proportionate to risk.

Warning signals include:

- process concerns treated as document-production quotas;
- implementation used to force acceptance of a design;
- architecture created without business drivers;
- contracts reconstructed only after integration failure;
- status reported from intention rather than repository and evidence;
- AI output accepted because it is detailed or confident;
- a passing check generalized to release or product success;
- unresolved questions hidden to pass a checkpoint;
- operational learning recorded but never routed to knowledge owners.

## 15. Tailoring Rules

An adopting project MAY tailor:

- role names;
- artifact formats;
- tool workflows;
- checkpoint mechanics;
- level of detail;
- review depth;
- whether concerns are represented in one or several artifacts;
- delivery cadence and planning method.

Tailoring MUST preserve:

- dependency of downstream work on adequate upstream knowledge;
- human authority over consequential decisions and risk;
- explicit contracts for material boundaries;
- traceability proportionate to impact;
- evidence bounded to exact claims;
- distinction between knowledge, implementation, and verification status;
- preservation of material history;
- learning as input to new knowledge decisions.

A tailoring decision that omits a normally required control SHOULD state its rationale, affected scope, compensating control, and accepted risk.

## 16. Conformance

A project conforms to this process model when it can demonstrate, for a declared scope and KGAID version, that:

- work begins from an owned and classified trigger;
- product or change intent is accepted before solution commitment;
- relevant business knowledge informs requirements and architecture;
- significant architecture decisions precede dependent implementation;
- material contracts precede acceptance of their realization;
- increments meet proportionate realization readiness;
- implementation discoveries are routed back to affected knowledge;
- human authorities make consequential decisions and accept risk;
- AI operates within explicit authority boundaries;
- completion claims identify their scope and supporting evidence;
- knowledge, implementation, and verification status remain distinct;
- accepted change performs downstream impact analysis;
- operational learning re-enters the knowledge process;
- tailoring does not reverse the KGAID principles.

Conformance does not require a waterfall lifecycle, particular ceremony, fixed team structure, document count, delivery framework, programming language, repository platform, or AI product.
