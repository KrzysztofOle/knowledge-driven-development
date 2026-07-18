# Knowledge-Driven Development

Knowledge-Driven Development (KDD) is an open, technology-independent methodology for developing software systems through collaboration between people and AI.

KDD treats knowledge as the primary project asset. Code is a realization of accepted knowledge rather than its sole source. Product and business understanding guide architecture, architecture guides implementation, explicit contracts precede the code that realizes them, and verification evidence limits completion claims. AI supports the work; humans retain decision authority and accountability.

## Methodology structure

~~~mermaid
flowchart TD
    A["00 Foundations"] --> B["10 Knowledge Architecture"]
    B --> C["20 Methodology"]
    C --> D["30 Quality"]
    D --> E["40 Adoption"]
    E --> F["Adopting projects"]
    F --> G["Operational evidence and learning"]
    G --> D
    G --> C
~~~

The numbered directories express dependency of meaning, not a mandatory waterfall schedule.

### 00 — Foundations

Foundations define the identity and constitutional rules of KDD.

- [KDD Scope and Boundaries](docs/00-foundations/scope-and-boundaries.md) — what KDD covers and deliberately does not prescribe.
- [KDD Principles](docs/00-foundations/principles.md) — the normative principles governing the methodology and its adoption.

### 10 — Knowledge Architecture

Knowledge Architecture defines the units, lifecycle, authority, relationships, and semantic ownership of project knowledge.

- [Knowledge Architecture Overview](docs/10-knowledge-architecture/README.md) — normative entry point and relationship between the models.
- [Artifact Model](docs/10-knowledge-architecture/artifact-model.md) — governed units and types of knowledge.
- [Knowledge Lifecycle](docs/10-knowledge-architecture/knowledge-lifecycle.md) — creation, proposal, review, acceptance, realization, verification, and evolution.
- [Authority Model](docs/10-knowledge-architecture/authority-model.md) — human authority, AI boundaries, delegation, and conflict resolution.
- [Traceability Model](docs/10-knowledge-architecture/traceability-model.md) — relationships from intent to evidence and impact analysis.
- [Knowledge Domains](docs/10-knowledge-architecture/knowledge-domains.md) — semantic ownership and boundaries between knowledge areas.

### 20 — Methodology

The methodology composes accepted knowledge models into an end-to-end way of working.

- [KDD Process Model](docs/20-methodology/process-model.md) — the iterative process from product stimulus through business knowledge, requirements, architecture, contracts, implementation, verification, operation, and learning.
- [KDD Human–AI Collaboration Model](docs/20-methodology/human-ai-collaboration.md) — context, delegation, execution, review, escalation, evidence, and the Human–Knowledge AI–Execution AI control pattern.
- [KDD AI Execution Task Contract](docs/20-methodology/ai-execution-task-contract.md) — the bounded, human-authorized task passed from a Knowledge and Review AI to an Execution AI.
- [KDD Delivery Increment Model](docs/20-methodology/delivery-increment-model.md) — the governed unit that connects accepted product knowledge, execution tasks, integration, evidence, baseline, and human acceptance.

### 30 — Quality

Quality models define how claims are verified, how evidence is interpreted, and how limitations constrain completion, baseline, release, and outcome decisions.

- [KDD Verification and Evidence Model](docs/30-quality/verification-and-evidence-model.md) — claim-first verification, evidence strength and boundaries, independence, invalidation, and the Human–ChatGPT–Codex verification flow.

### 40 — Adoption

Adoption models define how projects select a KDD baseline and profile, tailor local realization, demonstrate conformance, and maintain an evidence-based declaration.

- [KDD Adoption and Conformance Model](docs/40-adoption/adoption-and-conformance-model.md) — invariant core, Minimal and Extended profiles, tailoring, assessment requirements, evidence package, declaration, and adoption paths for KSeF_2, 3ksef, and future projects.

## Core dependency

~~~text
product purpose
→ business and domain knowledge
→ requirements and quality
→ architecture
→ contracts
→ implementation
→ evidence and operation
→ learning
~~~

The sequence is a dependency of meaning. Work may overlap, iterate, and proceed concurrently in bounded increments when uncertainty, authority, contracts, and evidence remain explicit.

## Human and AI

AI may analyze, propose, compare, implement, verify, and review within accepted context and delegated boundaries.

Humans remain accountable for:

- product purpose and priorities;
- authoritative business meaning;
- acceptance of requirements, architecture, and contracts;
- security, compliance, compatibility, and risk decisions;
- baselines, releases, and consequential completion claims.

AI cannot accept its own proposal or project risk.

## Adoption

KDD is independent of:

- programming language and framework;
- architectural style;
- project-management and repository tools;
- AI model or provider;
- deployment model;
- organization size.

An adopting project owns its product-specific knowledge and selects a level of rigor proportionate to uncertainty, consequence, reversibility, lifetime, and coordination needs.

## Origin

KDD is being extracted and generalized from practical project experience, including [KSeF_2](https://github.com/KrzysztofOle/KSeF_2). KSeF_2 is an empirical source and reference application, not a normative source for the methodology.

## Status

The methodology is under active development. Each normative document declares its own lifecycle status and version. Only content marked **Accepted** is authoritative within its declared scope.
