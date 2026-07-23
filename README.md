# Knowledge-Governed AI-Assisted Development

Knowledge-Governed AI-Assisted Development (KGAID) is an open, technology-independent methodology for developing software systems through collaboration between people and AI.

KGAID treats knowledge as the primary project asset. Code is a realization of accepted knowledge rather than its sole source. Product and business understanding guide architecture, architecture guides implementation, explicit contracts precede the code that realizes them, and verification evidence limits completion claims. AI supports the work; humans retain decision authority and accountability.

> [KGAID overview website — English and Polish](https://krzysztofole.github.io/kgaid-methodology/)
>
> **Early-stage notice:** KGAID is at the beginning of its development. The current repository is a first structured draft of the concept, developed in parallel with real projects that use it. Accepted documents are authoritative only within the current experimental baseline and do not imply an established industry standard or certification scheme.

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

Foundations define the identity and constitutional rules of KGAID.

- [KGAID Scope and Boundaries](docs/00-foundations/01-scope-and-boundaries.md) — what KGAID covers and deliberately does not prescribe.
- [KGAID Principles](docs/00-foundations/02-principles.md) — the normative principles governing the methodology and its adoption.

### 10 — Knowledge Architecture

Knowledge Architecture defines the units, lifecycle, authority, relationships, and semantic ownership of project knowledge.

- [Knowledge Architecture Overview](docs/10-knowledge-architecture/11-knowledge-architecture.md) — normative entry point and relationship between the models.
- [Artifact Model](docs/10-knowledge-architecture/12-artifact-model.md) — governed units and types of knowledge.
- [Knowledge Lifecycle](docs/10-knowledge-architecture/13-knowledge-lifecycle.md) — creation, proposal, review, acceptance, realization, verification, and evolution.
- [Authority Model](docs/10-knowledge-architecture/14-authority-model.md) — human authority, AI boundaries, delegation, and conflict resolution.
- [Traceability Model](docs/10-knowledge-architecture/15-traceability-model.md) — relationships from intent to evidence and impact analysis.
- [Knowledge Domains](docs/10-knowledge-architecture/16-knowledge-domains.md) — semantic ownership and boundaries between knowledge areas.

### 20 — Methodology

The methodology composes accepted knowledge models into an end-to-end way of working.

- [KGAID Process Model](docs/20-methodology/21-process-model.md) — the iterative process from product stimulus through business knowledge, requirements, architecture, contracts, implementation, verification, operation, and learning.
- [KGAID Human–AI Collaboration Model](docs/20-methodology/22-human-ai-collaboration.md) — context, delegation, execution, review, escalation, evidence, and the Human–Knowledge AI–Execution AI control pattern.
- [KGAID AI Execution Task Contract](docs/20-methodology/23-ai-execution-task-contract.md) — the bounded, human-authorized task passed from a Knowledge and Review AI to an Execution AI.
- [KGAID Delivery Increment Model](docs/20-methodology/24-delivery-increment-model.md) — the governed unit that connects accepted product knowledge, execution tasks, integration, evidence, baseline, and human acceptance.
- [KGAID Knowledge Base Curation Workflow](docs/20-methodology/25-knowledge-base-curation-workflow.md) — proposed operational workflow for turning staged source materials into governed expert knowledge, maintaining traceability, and preserving human approval authority; it is not part of the current baseline.

### 30 — Quality

Quality models define how claims are verified, how evidence is interpreted, and how limitations constrain completion, baseline, release, and outcome decisions.

- [KGAID Verification and Evidence Model](docs/30-quality/31-verification-and-evidence-model.md) — claim-first verification, evidence strength and boundaries, independence, invalidation, and the Human–ChatGPT–Codex verification flow.

### 40 — Adoption

Adoption models define how projects select a KGAID baseline and profile, tailor local realization, demonstrate conformance, and maintain an evidence-based declaration.

- [KGAID Adoption and Conformance Model](docs/40-adoption/41-adoption-and-conformance-model.md) — invariant core, Minimal and Extended profiles, tailoring, assessment requirements, evidence package, declaration, and adoption paths for KSeF_2, 3ksef, and future projects.

### 45 — Experience

Experience records preserve evidence and observations from real KGAID use
without automatically changing the methodology or granting reference-project
status.

- [KGAID experience index](docs/45-experience/README.md) — draft Experience
  Record model, pilot register, observation-response matrix, feedback lifecycle
  proposal, and the first record from `3ksef`.
- [EXP-3KSEF-001](docs/45-experience/reference-projects/3ksef/EXP-3KSEF-001.md)
  — draft record tied to immutable project and methodology commits.

### 50 — Governance evidence

Governance evidence records reviews and decisions about the methodology itself. It is informative or evidential unless an artifact explicitly declares normative status.

- [AUD-001 — KDD 0.1 Cross-Document Consistency Review](docs/50-governance/audits/AUD-001-kdd-0.1-consistency-review.md) — completed self-review of structure, terminology, authority, metadata, and baseline readiness.
- [AUD-002 — Knowledge-Driven Development Name and Prior-Use Landscape Review](docs/50-governance/audits/AUD-002-knowledge-driven-development-landscape-review.md) — external-source review of earlier terminology, conceptual overlap, distinct Human–AI features, and naming options.
- [Methodology Identity Proposal](docs/50-governance/proposals/methodology-identity-proposal.md) — accepted naming decision and migration basis for Knowledge-Governed AI-Assisted Development (KGAID).
- [Governance, Versioning, and Release Model](docs/50-governance/governance-and-release-model.md) — methodology change authority, versioning, baseline, and release rules.
- [Prepared KGAID-0.1.0 manifest](docs/50-governance/baselines/KGAID-0.1.0.yaml) — first baseline membership and dependencies; publication remains pending.
- [Draft Change Proposals](docs/50-governance/change-proposals/README.md) —
  lifecycle vocabulary, revision-bound Human Decision, Baseline Manifest v2,
  and evidence-based methodology evolution.
- [Open Human Authority decisions](docs/50-governance/decisions/README.md) —
  unresolved choices recorded without deciding them.

### 60 — Approval Center

Approval Center is a proposed, technology-neutral KGAID capability for
reviewing exact document revisions, recording human decisions, and exposing
change history and traceability. Its design is informative and is not part of
the current normative baseline.

- [Approval Center design](docs/60-approval/README.md) — index of the vision,
  approval process, metadata requirements, future user interface, conceptual
  architecture, and staged roadmap.

### KGAID tools

- [KGAID tools](tools/README.md) — reusable developer tools maintained in this
  repository and installed by adopting projects without copying their code.
- [KGAID Project Review](tools/kgaid_project_review/README.md) — a read-only,
  repeatable documentation health report for an adopting project's explicitly
  selected documentation directory; it does not make Human Authority decisions.

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

KGAID is independent of:

- programming language and framework;
- architectural style;
- project-management and repository tools;
- AI model or provider;
- deployment model;
- organization size.

An adopting project owns its product-specific knowledge and selects a level of rigor proportionate to uncertainty, consequence, reversibility, lifetime, and coordination needs.

## Origin

KGAID is being extracted and generalized from practical project experience, including [KSeF_2](https://github.com/KrzysztofOle/KSeF_2). KSeF_2 is an empirical source and reference application, not a normative source for the methodology.

The methodology was developed under the working name Knowledge-Driven Development (KDD). The identity changed to KGAID after [AUD-002](docs/50-governance/audits/AUD-002-knowledge-driven-development-landscape-review.md) confirmed prior use of the former name and the KGAID Methodology Maintainer accepted a distinct identity.

## Status

The methodology is under active development. Each normative document declares its own lifecycle status and version. Only content marked **Accepted** is authoritative within its declared scope.
