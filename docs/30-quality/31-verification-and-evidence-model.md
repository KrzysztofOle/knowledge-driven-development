---
document_id: KGAID-QLT-001
title: KGAID Verification and Evidence Model

document_type: verification
status: accepted
version: 0.1.0

owner: Quality

approval_status: pending
approved_by:
approved_at:
---

# KGAID Verification and Evidence Model

## 1. Purpose

This document defines how Knowledge-Governed AI-Assisted Development formulates claims, plans verification, produces evidence, evaluates its strength and limitations, and uses it in human decisions.

It explains:

- what a verifiable claim contains;
- how acceptance criteria relate to claims and evidence;
- which evidence types MAY be used;
- how environment, version, boundary, data, and method limit conclusions;
- how evidence is reviewed, aggregated, invalidated, and retained;
- how much independence is needed;
- how Codex, ChatGPT, and humans participate in verification;
- when automation MAY update verification status;
- how evidence supports increment, baseline, release, and product-outcome decisions.

The model is independent of testing framework, programming language, CI platform, AI provider, and quality standard.

## 2. Foundational Rule

> **A claim MUST NOT exceed its evidence.**

Verification begins with a precise claim, not with an available tool or a list of tests.

A passing check supports only the behavior, subject, version, environment, data, method, and boundary it actually exercised.

Examples:

- a successful build supports syntactic and configured buildability, not functional correctness;
- a unit test supports declared component behavior under its test conditions, not integration or production behavior;
- an integration test supports the exercised integration path, not every consumer or failure mode;
- a simulated restart does not prove process-loss durability unless the real boundary was exercised;
- a security scanner result does not prove absence of vulnerabilities;
- successful deployment does not prove release readiness or product value;
- lack of reported incidents does not prove that no incident occurred.

## 3. Definitions

| Term | Meaning |
| --- | --- |
| **Claim** | A scoped statement asserted to be true about an identified subject. |
| **Subject** | The exact artifact, implementation, system, environment, process, or outcome to which a claim applies. |
| **Criterion** | A condition used to judge whether a claim MAY be supported. |
| **Verification** | Evaluation of whether evidence supports a claim against accepted knowledge. |
| **Validation** | Evaluation of whether a realized and operating result serves the intended product outcome or actual need. |
| **Evidence** | A durable record of an observation, test, analysis, review, measurement, or audit relevant to a claim. |
| **Method** | The procedure used to produce or evaluate evidence. |
| **Boundary** | The component, interaction, system, environment, time, data, or organizational scope covered. |
| **Limitation** | A condition outside the evidence scope or reducing the strength of the conclusion. |
| **Uncertainty** | Relevant knowledge that is incomplete, variable, or not established. |
| **Residual risk** | Risk remaining after applicable controls and verification. |
| **Verification decision** | Human or pre-authorized determination that evidence supports a declared claim. |
| **Acceptance decision** | Human determination to accept a result, limitations, and risk for a declared scope. |

Verification, validation, acceptance, release, and risk acceptance are distinct decisions.

## 4. Claim Model

A material claim SHOULD identify:

- stable claim identifier;
- claim statement;
- subject and exact version;
- owning requirement, contract, acceptance criterion, risk, or product outcome;
- boundary;
- environment;
- applicable conditions and data;
- required confidence or assurance;
- verification method;
- required evidence;
- excluded guarantees;
- decision and authority the claim will support;
- conditions that invalidate the claim.

A claim SHOULD be:

- specific enough to be challenged;
- observable or assessable;
- related to accepted knowledge;
- bounded in time, version, and environment where relevant;
- free of ambiguous words such as complete, safe, robust, scalable, or ready unless those words are defined by criteria.

Example:

~~~yaml
claim:
  id: CLM-042
  statement: >
    CTR-006 idempotency behavior is satisfied by implementation revision abc123
    for duplicate requests processed by component-a in the integration-test
    environment using contract-suite revision 4.
  derives_from:
    - CTR-006
    - REQ-018
  subject:
    type: implementation
    revision: abc123
  boundary:
    component: component-a
    environment: integration-test
    scenarios:
      - duplicate-request-same-key
  excludes:
    - multi-region-concurrency
    - process-restart-durability
    - production-readiness
  verification_method:
    - contract-suite-revision-4
  decision_supported:
    - increment-verification
~~~

The exclusions are part of the claim meaning, not an optional disclaimer.

## 5. Claim Classes

Claim classes help select appropriate evidence. They do not form a simple ladder in which one passing class proves another.

| Class | Question | Examples |
| --- | --- | --- |
| **Knowledge conformance** | Is an artifact consistent with authoritative knowledge? | Requirement review, architecture consistency, contract completeness. |
| **Implementation presence** | Does the declared realization exist at the identified revision? | Code, configuration, migration, generated artifact. |
| **Component behavior** | Does one bounded component satisfy its contract? | Unit, property, component, or contract test. |
| **Integration behavior** | Do interacting elements satisfy shared obligations? | API, message, database, dependency, compatibility test. |
| **System behavior** | Does the integrated system satisfy an end-to-end scenario? | System or end-to-end test. |
| **Quality property** | Does the subject satisfy a declared non-functional property? | Performance, reliability, durability, usability, security analysis. |
| **Migration or recovery** | Can the system move or recover between declared states? | Migration rehearsal, backup restore, failover, rollback. |
| **Compliance** | Does evidence satisfy an applicable external obligation? | Control evidence, legal review, audit, formal attestation. |
| **Operational readiness** | Can the system be operated within declared conditions? | Monitoring, runbooks, support, capacity, recovery evidence. |
| **Release readiness** | Is an identified baseline suitable for a declared release scope? | Aggregate evidence, limitations, risk and authority decision. |
| **Operational behavior** | What occurred in a real environment during a declared period? | Telemetry, incidents, service levels, production observations. |
| **Product outcome** | Did actual use contribute to the intended result? | Adoption, effectiveness, business or user outcome measures. |

Evidence for one class MAY contribute to another decision but MUST NOT be silently generalized.

## 6. Evidence Record

A material Evidence artifact SHOULD contain:

### 6.1 Identity

- stable Evidence identifier;
- title and revision;
- evidence owner;
- author or producing actor;
- creation date and observation period;
- lifecycle and validity status.

### 6.2 Claim relationship

- claim or claims evaluated;
- relationship: supports, contradicts, or informs;
- applicable acceptance criterion, requirement, contract, risk, or outcome;
- subject and exact revision.

### 6.3 Method

- procedure;
- tool, test, model, checklist, or review method and version;
- configuration and parameters;
- input data and relevant provenance;
- preconditions;
- success, failure, and inconclusive conditions.

### 6.4 Boundary

- component, integration, system, or organizational boundary;
- environment;
- infrastructure and dependency versions;
- time and duration;
- exercised scenarios;
- concurrency, scale, load, or fault conditions;
- exclusions.

### 6.5 Result

- raw observation;
- normalized result;
- pass, fail, partial, inconclusive, or not-executed disposition;
- unexpected observations;
- reproducibility;
- links to retained logs, reports, artifacts, or measurements.

### 6.6 Limitations and integrity

- untested conditions;
- known method weaknesses;
- uncertainty;
- data quality;
- independence level;
- tamper protection or integrity mechanism where needed;
- expiry or invalidation conditions.

Evidence SHOULD retain raw or reproducible observations when the decision consequence justifies it. A summary without access to material results provides weaker evidence.

## 7. Evidence Types

| Evidence type | Typical strength | Typical limitation |
| --- | --- | --- |
| **Source inspection** | Establishes content of an identified artifact or specification. | Does not show implementation behavior. |
| **Human review** | Applies expertise, context, and judgment. | May be subjective or incomplete. |
| **AI review** | Scales comparison, pattern detection, and contradiction analysis. | May share assumptions or hallucinate without grounded inputs. |
| **Static analysis** | Evaluates code or artifacts without execution. | Cannot establish all runtime behavior. |
| **Example-based test** | Demonstrates behavior for selected cases. | Coverage limited to chosen examples. |
| **Property-based test** | Explores a declared property over generated cases. | Generator and oracle MAY omit important states. |
| **Contract test** | Evaluates consumer or provider obligations. | Limited to contract representation and environment. |
| **Integration test** | Exercises interactions and dependencies. | May not reproduce full production conditions. |
| **System or end-to-end test** | Exercises an integrated scenario. | Expensive and MAY localize defects poorly. |
| **Performance or reliability test** | Measures a quality property under declared load and conditions. | Results depend strongly on environment and workload. |
| **Security analysis or test** | Identifies declared classes of weakness or attack behavior. | No finite assessment proves absence of all vulnerabilities. |
| **Formal analysis** | Provides strong conclusions under explicit model assumptions. | Model MAY not represent implementation or environment fully. |
| **Simulation or fault injection** | Evaluates selected failures or conditions. | Simulated boundary MAY differ from actual failure. |
| **Migration or recovery rehearsal** | Exercises transition, restore, rollback, or recovery. | Evidence applies to exercised data and environment. |
| **Operational measurement** | Observes actual behavior. | Observation MAY be incomplete and causality uncertain. |
| **Audit** | Independently evaluates conformance and controls. | Scope and sampling limit conclusions. |
| **User or stakeholder validation** | Evaluates fitness for actual need. | May be qualitative or affected by selection bias. |

No evidence type is universally superior. Selection depends on the exact claim.

## 8. Evidence Strength Dimensions

KGAID evaluates evidence across dimensions rather than assigning one universal confidence score.

| Dimension | Question |
| --- | --- |
| **Relevance** | Does the evidence address the exact claim? |
| **Directness** | Does it observe the subject directly or rely on several inferences? |
| **Coverage** | Which scenarios, states, inputs, and failure modes were exercised? |
| **Realism** | How closely do environment and conditions represent the target boundary? |
| **Independence** | How separate are the author, implementer, reviewer, method, and environment? |
| **Reproducibility** | Can an authorized party obtain the same observation? |
| **Currency** | Does evidence apply to the current subject, dependencies, and environment? |
| **Integrity** | Can the evidence and its provenance be trusted as unaltered? |
| **Specificity** | Are subject, version, method, and limitations explicit? |
| **Diversity** | Do materially different methods address correlated failure modes? |

More evidence does not automatically mean stronger evidence. Many duplicated checks MAY share one blind spot.

A verification decision SHOULD explain material weakness in any dimension when the claim is consequential.

## 9. Verification Planning

Verification SHOULD be planned with requirements, contracts, and increment shaping rather than postponed until implementation is complete.

A verification plan SHOULD identify:

- claims;
- applicable criteria;
- subject and target revision;
- evidence methods;
- required environments and data;
- responsibility and authority;
- independence requirements;
- automation policy;
- evidence retention;
- failure and escalation behavior;
- limitations that will remain;
- invalidation triggers;
- decision or gate supported.

A criterion-to-evidence matrix makes missing coverage visible:

| Claim or criterion | Method | Boundary | Required evidence | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| CLM-001 | Contract test | Component | EVD planned | Verification owner | planned |
| CLM-002 | Integration scenario | Integration | EVD planned | Verification owner | blocked |
| CLM-003 | Production measurement | Operational | EVD after release | Operations owner | not available |

A plan MUST NOT mark unavailable future evidence as currently satisfied.

## 10. Verification Lifecycle

The typical lifecycle is:

~~~mermaid
flowchart TD
    A["Define claim"] --> B["Plan verification"]
    B --> C["Prepare subject and environment"]
    C --> D["Collect evidence"]
    D --> E["Evaluate evidence"]
    E --> F{"Claim supported?"}
    F -->|Yes| G["Verification decision"]
    F -->|No| H["Fail, limit, or revise"]
    G --> I["Baseline or acceptance input"]
    H --> A
    I --> J["Monitor invalidation"]
    J --> A
~~~

The lifecycle MAY return upstream when:

- the claim is ambiguous;
- the method cannot evaluate it;
- the environment is unrepresentative;
- evidence reveals an implementation defect;
- evidence challenges an accepted requirement or contract;
- the intended claim requires broader authority or risk acceptance.

A failed verification does not automatically change normative knowledge. It creates a trigger for analysis and the appropriate owner decision.

## 11. Evidence Results and Claim Status

Evidence result and claim status are distinct.

### 11.1 Evidence result

| Result | Meaning |
| --- | --- |
| **supports** | Observation is consistent with the claim within the evidence boundary. |
| **contradicts** | Observation is inconsistent with the claim. |
| **partial** | Evidence addresses only part of the declared claim. |
| **inconclusive** | Method or result cannot determine support or contradiction. |
| **not-executed** | Planned evidence was not produced. |
| **invalid** | Evidence procedure or integrity is not usable. |

### 11.2 Claim verification status

This is the canonical KGAID verification-status taxonomy. Artifact, increment,
and other model documents MUST use these names for a verification claim.

| Status | Meaning |
| --- | --- |
| **not-planned** | No verification approach exists. |
| **planned** | Claim and evidence method are defined. |
| **in-progress** | Evidence collection or evaluation is active. |
| **partially-supported** | Some required evidence supports a narrower portion. |
| **failed** | Applicable credible evidence contradicts the claim or a mandatory criterion failed. |
| **verified** | Required evidence supports the exact claim within declared limitations. |
| **verified-with-limitations** | Human authority accepted an explicitly narrowed verification claim. |
| **inconclusive** | Available evidence cannot resolve the claim. |
| **invalidated** | Previously applicable evidence no longer supports the current claim. |
| **expired** | Time or policy boundary requires reverification. |

A claim MUST NOT be marked verified solely because no contradicting evidence was found.

## 12. Boundaries and Environments

Verification MUST declare the boundary at which evidence was produced.

Common boundaries include:

- artifact or document;
- function or module;
- component;
- process;
- service;
- service integration;
- system;
- multi-system ecosystem;
- deployment environment;
- operational period;
- organization or control system;
- user or product outcome.

Environments MAY include local, simulated, CI, integration, staging, production-like, limited production, and production.

Environment labels alone are insufficient. Relevant differences SHOULD be identified, including:

- configuration;
- dependency versions;
- infrastructure;
- data;
- scale;
- concurrency;
- network and failure behavior;
- credentials and permissions;
- observability;
- external services;
- time-dependent state.

Evidence MAY be promoted to a broader decision only through explicit reasoning about equivalence and remaining differences.

## 13. Positive, Negative, and Missing Evidence

Positive evidence shows that an observed result supports a claim under declared conditions.

Negative evidence shows a contradiction, failed criterion, defect, control weakness, or adverse observation.

Missing evidence means a required claim has not been evaluated sufficiently.

KGAID rules:

- negative evidence MUST remain visible until resolved, scoped out by proper authority, or invalidated with rationale;
- one positive observation MUST NOT silently cancel credible negative evidence;
- missing evidence MUST NOT be represented as a pass;
- a skipped check MUST identify why it was skipped and which claim remains unsupported;
- “not reproduced” MUST NOT be treated as “fixed” without appropriate evidence;
- “no findings” means only that the method produced no findings within its scope.

## 14. Aggregating Evidence

Evidence MAY be combined when each item has compatible:

- claim meaning;
- subject and revision;
- environment or justified equivalence;
- boundary;
- method interpretation;
- time validity.

Aggregation SHOULD identify:

- which criteria each item supports;
- overlaps and duplicated methods;
- uncovered conditions;
- contradictions;
- correlated sources of error;
- limitations of the combined conclusion.

A large test count, coverage percentage, or number of AI reviews is not a completion claim by itself.

Evidence from different revisions MUST NOT be combined as if it applied to one revision unless the relevant subject is proven unchanged.

Contradictory evidence requires explicit analysis. It MUST NOT be averaged into a neutral status.

## 15. Independence Model

Verification independence SHOULD increase with consequence, uncertainty, irreversibility, and potential correlated failure.

| Level | Description | Example |
| --- | --- | --- |
| **V0 — Self-check** | Same actor and context create and check the work. | Codex implements and runs its own tests. |
| **V1 — Context separation** | Review uses a separate context, method, or tool. | ChatGPT reviews Codex diff and raw evidence against accepted knowledge. |
| **V2 — Independent review** | A separate accountable person, team, model context, or verification owner evaluates the result. | Human reviewer or separately prepared contract suite. |
| **V3 — Specialist or external assurance** | Qualified specialist or independent body evaluates a high-consequence concern. | Security assessment, compliance audit, safety review. |

Higher levels complement rather than automatically replace lower levels.

The Human–ChatGPT–Codex pattern normally provides:

- V0 through Codex implementation checks;
- V1 through ChatGPT review of actual changes and evidence;
- human acceptance and possible V2 when the human performs substantive review.

If ChatGPT and Codex share the same unsupported assumption, V1 MAY not detect it. High-risk claims SHOULD use independent sources, methods, environments, specialists, or separately designed tests.

## 16. Human–ChatGPT–Codex Verification Flow

~~~mermaid
sequenceDiagram
    participant H as Human
    participant K as ChatGPT
    participant E as Codex

    H->>K: Accept claim scope and risk boundary
    K->>E: Send task and verification plan
    E->>E: Implement, test, collect raw evidence
    E->>K: Return changes, results, limitations
    K->>K: Compare claims, criteria, diff, and evidence
    alt Defect within accepted scope
        K->>E: Request correction and reverification
        E->>K: Return corrected evidence
    else Unsupported claim or new risk
        K->>H: Present decision packet
    end
    K->>H: Report supported claim and limitations
    H->>H: Accept, reject, limit, or require more evidence
~~~

### 16.1 Codex responsibility

Codex SHOULD:

- implement verification hooks and tests required by its task contract;
- execute applicable checks;
- retain raw or reproducible results;
- report failures and skipped checks;
- identify the exact revision and environment;
- avoid broadening the claim;
- return discoveries that challenge accepted knowledge.

Codex MUST NOT mark its own consequential result finally accepted.

### 16.2 ChatGPT responsibility

ChatGPT SHOULD:

- compare the intended claim with accepted requirements and contracts;
- inspect actual changes rather than only the Codex summary;
- inspect raw or reproducible evidence;
- map evidence to each criterion;
- detect missing coverage, inconsistent revisions, weak environments, and unsupported generalization;
- request corrections inside accepted scope;
- escalate changed meaning, risk, or claim scope;
- present the Human with supported claims, contradictions, limitations, and recommendation.

ChatGPT review is evidence of review, not automatic proof of implementation correctness.

### 16.3 Human responsibility

The Human or applicable authority SHOULD:

- confirm that the claim matters and is correctly scoped;
- decide whether evidence depth and independence match the consequence;
- resolve product, contract, architecture, compliance, and risk questions;
- accept or reject the verification decision;
- accept residual limitations and risk where authorized;
- decide baseline, release, or additional assurance.

## 17. AI-Generated Evidence

AI MAY:

- generate tests and verification procedures;
- execute tools;
- collect and structure evidence;
- analyze failures;
- compare implementation with contracts;
- identify gaps and contradictions;
- draft verification reports.

AI-generated evidence SHOULD be treated according to method, provenance, reproducibility, independence, and boundary—not according to fluency.

When AI creates both implementation and test oracle, the risk of a shared misunderstanding increases. Proportionate controls MAY include:

- human review of criteria;
- tests derived independently from contracts;
- separate AI context or model;
- mutation or fault-injection testing;
- external or consumer-driven contract tests;
- production-like observation;
- specialist assessment.

Hidden model reasoning is not required as evidence. Sources, inputs, procedure, observable outputs, limitations, and decision record are.

## 18. Automatic Verification Policy

Automation MAY update claim status only under a human-accepted policy that defines:

- exact claim;
- subject resolution;
- accepted verification procedure and version;
- environment and boundary;
- success, failure, inconclusive, and not-executed interpretation;
- evidence retention;
- policy owner;
- independence requirement;
- expiry and invalidation conditions;
- exception and escalation behavior.

Example:

~~~yaml
automatic_verification:
  policy_id: AVP-004
  claim: CLM-042
  subject_resolution: current-increment-candidate
  method: contract-suite-revision-4
  environment: declared-integration-environment
  on_success: verified
  on_failure: failed
  on_missing_result: inconclusive
  retain:
    - subject-revision
    - suite-revision
    - environment
    - raw-results
  invalidate_when:
    - contract-suite-changes
    - contract-semantics-change
    - implementation-revision-changes
    - environment-boundary-changes
~~~

Automation executes accepted interpretation. It cannot broaden the claim, waive failures, or accept risk.

## 19. Evidence Invalidation

Evidence MUST be reviewed or invalidated when a relevant change affects:

- claim meaning;
- requirement or contract;
- subject implementation;
- dependency or configuration;
- environment or infrastructure;
- data, workload, scale, or time boundary;
- verification method or oracle;
- security threat model;
- applicable external obligation;
- discovered defect;
- evidence integrity;
- accepted limitation.

Invalidation MAY be:

- complete;
- limited to one claim;
- limited to one environment;
- limited to one criterion;
- time-based expiry.

Invalidated evidence remains part of project history but MUST NOT support the current claim.

Impact analysis SHOULD follow traceability from changed knowledge or implementation to claims and evidence.

## 20. Verification Decision Packet

A material verification decision packet SHOULD contain:

- exact claim;
- subject and version;
- governing requirements, contracts, criteria, and risks;
- evidence matrix;
- evidence strength and independence;
- contradictions and failures;
- skipped or unavailable checks;
- limitations and excluded guarantees;
- residual uncertainty and risk;
- verification recommendation;
- decision authority required;
- effect on increment, baseline, release, or operation;
- reverification and monitoring needs.

The packet SHOULD distinguish:

- what was observed;
- what is inferred;
- what remains assumed;
- what requires human acceptance.

## 21. Evidence Package Template

~~~markdown
# EVD-NNN — Evidence title

## Metadata

- Evidence status:
- Validity status:
- Owner:
- Produced by:
- Reviewed by:
- Independence level:
- Created:
- Observation period:

## Claim

- Claim ID:
- Statement:
- Subject:
- Subject revision:
- Governing artifacts:
- Decision supported:

## Method

- Procedure:
- Tool, test, model, or checklist:
- Method version:
- Configuration:
- Inputs and data:
- Preconditions:
- Success condition:
- Failure condition:
- Inconclusive condition:

## Boundary

- Component or system boundary:
- Environment:
- Infrastructure and dependencies:
- Scenarios:
- Scale and concurrency:
- Time:
- Exclusions:

## Result

- Disposition:
- Raw observation:
- Normalized result:
- Unexpected observations:
- Reproduction:
- Retained artifacts:

## Strength

- Relevance:
- Directness:
- Coverage:
- Realism:
- Independence:
- Reproducibility:
- Currency:
- Integrity:
- Diversity:

## Limitations and uncertainty

## Contradictory or related evidence

## Invalidation conditions

## Verification review

- Claim status recommendation:
- Reviewer:
- Review date:
- Rationale:
- Required follow-up:

## Human decision

- Decision:
- Decided by:
- Date:
- Accepted claim:
- Accepted limitations:
- Accepted residual risk:
~~~

A project MAY combine several related results in one Evidence artifact when individual claim and boundary mappings remain clear.

## 22. Evidence Retention and Integrity

Evidence retention SHOULD be proportional to:

- consequence of the decision;
- regulatory or contractual obligation;
- expected system lifetime;
- cost of reproduction;
- rate of change;
- incident and audit needs;
- privacy and security constraints.

A retained evidence package SHOULD preserve enough information to identify:

- what was evaluated;
- exact revision;
- how it was evaluated;
- result;
- boundary and environment;
- limitations;
- producing and reviewing actors;
- decision based on it.

Sensitive evidence MUST follow data classification, access, minimization, and retention requirements.

Generated summaries SHOULD link to authoritative raw evidence where its retention is required.

## 23. Minimal and Extended Application

### 23.1 Minimal application

For low-risk, reversible work, a concise evidence record MAY contain:

- exact claim;
- subject revision;
- criterion;
- method and environment;
- result;
- limitation;
- reviewer or accepted automation policy;
- human decision when consequential.

### 23.2 Extended application

For high-risk, regulated, security-sensitive, production-critical, or difficult-to-reverse claims, verification SHOULD include:

- stable claim and evidence identifiers;
- controlled methods and environments;
- stronger independence;
- diverse evidence;
- reproducible raw results;
- integrity protection;
- explicit contradiction handling;
- formal limitation and residual-risk review;
- controlled retention;
- independent specialist or external assurance where required;
- reverification and operational monitoring.

## 24. Failure Signals

The following indicate likely verification failure:

- tests exist without an explicit claim;
- acceptance criteria cannot be mapped to evidence;
- a build or unit test is reported as production readiness;
- evidence omits subject revision or environment;
- skipped checks are reported as passing;
- evidence from several revisions is aggregated without qualification;
- ChatGPT reviews only the Codex narrative rather than actual changes and results;
- Codex-generated tests repeat the same misunderstanding as the implementation;
- negative evidence disappears after a rerun without explanation;
- a broad claim relies on one narrow method;
- many similar checks are treated as independent evidence;
- an outdated result continues after contract or implementation change;
- verification, risk acceptance, and release approval are collapsed into one status;
- operational outcome is inferred from successful deployment;
- the Human receives a success summary without limitations and unsupported criteria.

## 25. Conformance

A project conforms to this model when, for a declared KGAID version and profile:

- material verification begins with an explicit, bounded claim;
- claims relate to accepted requirements, contracts, criteria, risks, or outcomes;
- evidence identifies subject, revision, method, environment, result, and limitations;
- evidence is evaluated across relevant strength dimensions;
- missing, negative, inconclusive, and invalid evidence remain visible;
- evidence does not support claims beyond its boundary;
- aggregation preserves claim, revision, environment, and contradiction semantics;
- independence is proportional to consequence and correlated-failure risk;
- Codex returns raw or reproducible evidence and does not accept its own result;
- ChatGPT reviews actual changes, criteria, and evidence and exposes gaps;
- humans retain verification, limitation, risk, baseline, and release authority as applicable;
- automatic status follows a human-accepted verification policy;
- relevant changes invalidate or trigger review of affected evidence;
- traceability connects claims, subjects, criteria, evidence, decisions, and baselines;
- evidence retention and integrity are proportionate to decision needs;
- validation of product outcome remains distinct from implementation verification.

Conformance does not require a particular test framework, coverage metric, CI system, programming language, AI model, certification, or audit standard.
