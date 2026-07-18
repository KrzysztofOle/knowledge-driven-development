---
document_id: KGAID-MTH-003
title: KGAID AI Execution Task Contract
status: Accepted
version: 0.1.0
baseline: KGAID-0.1.0
normative: true
maintainer: Krzysztof Olejnik — KGAID Methodology Maintainer
last_reviewed: 2026-07-19
dependencies: [KGAID-FND-002, KGAID-MTH-001, KGAID-MTH-002, KGAID-KA-004, KGAID-KA-005]
supersedes: null
superseded_by: null
verification_status: verified
change_control: docs/50-governance/governance-and-release-model.md
---

# KGAID AI Execution Task Contract

## 1. Purpose

This document defines the AI Execution Task Contract used to delegate bounded realization work from a Knowledge and Review AI to an Execution AI under human authority.

In the KSeF_2 collaboration pattern:

- the Human and ChatGPT establish what SHOULD be done;
- ChatGPT prepares the task contract;
- the Human authorizes consequential scope;
- ChatGPT sends the contract to Codex;
- Codex implements and tests;
- ChatGPT reviews the actual result and evidence;
- the Human makes the final acceptance decision.

The contract is independent of ChatGPT, Codex, repository platform, programming language, and agent framework.

## 2. Definition

An **AI Execution Task Contract** is a versioned, bounded delegation package that tells an Execution AI:

- why the task exists;
- what result is required;
- which accepted knowledge governs the work;
- what is included and excluded;
- which actions are allowed and forbidden;
- which decisions are already made;
- which decisions remain with humans;
- what acceptance criteria apply;
- what evidence MUST be returned;
- when execution MUST stop and escalate.

The contract converts accepted project knowledge into an executable unit without transferring human decision authority to AI.

It is an operational delegation contract. It is not a system interface contract and MUST NOT override an accepted KGAID Contract artifact, requirement, architecture decision, business rule, or product boundary.

## 3. Three Distinct Decisions

KGAID distinguishes three decisions that MUST NOT be collapsed:

| Decision | Meaning | Authority |
| --- | --- | --- |
| **Task authorization** | The declared work MAY be attempted within the stated delegation. | Human authority or applicable accepted policy. |
| **Result verification** | Evidence supports specified claims about the implementation. | Verification Authority or accepted automatic verification policy. |
| **Result acceptance** | The reviewed result, limitations, and residual risk are accepted for the declared scope. | Properly scoped Human Decision Authority. |

Authorization to begin does not mean that the implementation is correct, verified, accepted, releasable, or deployed.

A successful Execution AI report does not perform the second or third decision automatically.

## 4. Relationship to KGAID Artifacts

The task contract packages and references existing project knowledge. It does not become authoritative merely by copying it.

A task contract typically derives from:

- one delivery Increment artifact;
- accepted product or capability scope;
- applicable business rules;
- requirements and quality requirements;
- architecture specifications and decisions;
- system or component Contracts;
- assumptions and risks;
- acceptance criteria;
- an applicable knowledge baseline.

The task contract SHOULD preserve links to source artifacts rather than duplicating their full content. When a necessary excerpt is included, the authoritative source and version MUST remain identifiable.

A task contract MAY use a project-local identifier. KGAID core does not introduce a new mandatory artifact type in version 0.1. A project MAY associate the contract with its Increment identifier, work-item identifier, or a profile-defined task identifier.

## 5. Contract Parties and Responsibilities

| Party | Responsibility |
| --- | --- |
| **Human Decision Authority** | Accepts consequential objective and scope, authorizes delegation, resolves escalations, and accepts or rejects the final result. |
| **Knowledge and Review AI** | Builds the contract from accepted knowledge, checks completeness, delegates execution, reviews the actual result, and prepares human decisions. |
| **Execution AI** | Performs allowed implementation and verification actions, reports evidence and limitations, and escalates boundary changes. |
| **Knowledge Owners** | Own the meaning of referenced product, domain, requirement, architecture, contract, and risk artifacts. |
| **Verification Authority** | Evaluates whether returned evidence supports the exact claim. |
| **Risk Authority** | Accepts residual risk where the result requires it. |

In the reference realization, ChatGPT performs the Knowledge and Review AI role and Codex performs the Execution AI role.

Authorship of the task contract does not grant ChatGPT human decision authority. Ability to edit the project does not grant Codex authority to change the task contract.

## 6. Required Contract Structure

A material task contract SHOULD contain the following sections.

### 6.1 Identity and lifecycle

- task identifier;
- title;
- contract revision;
- lifecycle status;
- related Increment or change identifier;
- created date and creator;
- authorizing human or role;
- Execution AI;
- Knowledge and Review AI;
- target baseline, repository, branch, environment, or artifact revision;
- expiry or review condition where relevant.

### 6.2 Objective and rationale

- expected outcome;
- product need, obligation, defect, risk reduction, or learning goal;
- relationship to accepted product or capability scope;
- intended completion claim.

The objective describes the result, not only the activity.

### 6.3 Scope

- included behavior, components, artifacts, files, environments, and consumers;
- explicit exclusions and non-goals;
- allowed degree of refactoring or incidental change;
- compatibility and migration boundary;
- external systems or actors affected;
- maximum acceptable expansion without reauthorization.

### 6.4 Authoritative inputs

- accepted knowledge governing the task;
- exact versions, revisions, dates, or baseline;
- applicable source precedence;
- material external obligations;
- working proposals or observations clearly separated from authoritative inputs.

### 6.5 Assumptions and unknowns

- assumptions under which execution MAY proceed;
- consequence if an assumption is false;
- validation or expiry condition;
- unresolved questions;
- decisions already deferred;
- uncertainty that limits the result or evidence claim.

### 6.6 Constraints and invariants

- business rules that MUST remain true;
- architecture boundaries;
- contract obligations;
- quality, security, privacy, legal, and compliance constraints;
- performance, durability, compatibility, and operational expectations;
- project conventions relevant to the change;
- protected behavior and existing state that MUST NOT be altered.

### 6.7 Allowed and forbidden actions

- files, systems, tools, commands, environments, and data the Execution AI MAY access;
- writes and mutations it MAY perform;
- actions requiring preview or read-only inspection first;
- external actions explicitly authorized;
- destructive actions explicitly authorized;
- prohibited actions;
- secrets and sensitive-data rules;
- recovery or rollback expectations.

An omitted external or destructive permission MUST be treated as not granted.

### 6.8 Deliverables

- implementation changes;
- tests and verification assets;
- migrations or configuration;
- documentation and derived artifacts;
- evidence records;
- traceability updates;
- required result report.

### 6.9 Acceptance criteria

Each criterion SHOULD be:

- observable;
- scoped;
- related to accepted upstream knowledge;
- verifiable through a declared method;
- explicit about environment and boundary where material;
- distinguishable from implementation preference.

Criteria MAY reference existing requirement, contract, scenario, or evidence identifiers.

### 6.10 Verification plan

- claims to be verified;
- checks, tests, reviews, or analyses to perform;
- required environment and data;
- success and failure conditions;
- evidence to retain;
- checks that cannot be performed by the Execution AI;
- limitations that prevent broader claims.

### 6.11 Escalation conditions

The contract MUST identify conditions requiring the Execution AI or Knowledge AI to stop affected work and request human direction.

At minimum, escalation applies to a required change in:

- product purpose or scope;
- business meaning;
- normative requirement;
- significant architecture;
- system or component contract;
- security, privacy, legal, or compliance control;
- compatibility or migration obligation;
- evidence scope;
- external effects;
- residual risk.

### 6.12 Result and handoff format

The Execution AI MUST know what to return so the Knowledge AI can perform a substantive review.

The result SHOULD include:

- outcome;
- actual changed scope;
- changed artifacts or diff reference;
- decisions made within delegated discretion;
- commands and checks executed;
- raw or reproducible evidence;
- failed, skipped, or unavailable checks;
- assumptions used;
- discovered conflicts or missing knowledge;
- known limitations;
- remaining risks;
- recommended next action;
- items requiring human decision.

## 7. Lifecycle

The task contract has an execution lifecycle distinct from the knowledge lifecycle.

~~~mermaid
stateDiagram-v2
    [*] --> draft
    draft --> authorized
    draft --> withdrawn
    authorized --> active
    authorized --> revoked
    active --> awaiting_review
    active --> paused
    active --> revoked
    paused --> active
    paused --> revised
    awaiting_review --> correction
    correction --> active
    awaiting_review --> ready_for_human_decision
    ready_for_human_decision --> accepted_result
    ready_for_human_decision --> correction
    ready_for_human_decision --> rejected_result
    revised --> authorized
    accepted_result --> closed
    rejected_result --> closed
    revoked --> [*]
    withdrawn --> [*]
    closed --> [*]
~~~

| Status | Meaning |
| --- | --- |
| **draft** | Prepared but not authorized for execution. |
| **authorized** | Human authority accepted the declared execution scope and delegation. |
| **active** | Execution is in progress. |
| **paused** | Execution stopped pending information or a non-semantic obstacle. |
| **revised** | Meaningful scope, constraint, or criterion changed and requires reauthorization. |
| **awaiting_review** | Execution result and evidence were returned for Knowledge AI review. |
| **correction** | Review identified defects correctable within the authorized scope. |
| **ready_for_human_decision** | Review is complete and the declared result is ready for human acceptance or rejection. |
| **accepted_result** | Human authority accepted the result for the declared scope. |
| **rejected_result** | Human authority rejected the result or requires a separately revised task. |
| **revoked** | Delegation was withdrawn before completion. |
| **withdrawn** | Draft was abandoned before authorization. |
| **closed** | The task record is complete and retained with its result. |

Only a properly scoped human or accepted policy MAY transition a task to **authorized**.

Only a properly scoped human MAY transition a consequential result to **accepted_result**.

The Knowledge AI MAY manage routine status updates and the correction loop within explicit delegation, but it cannot accept its own contract or result.

## 8. Authorization Readiness

A task is ready for authorization when:

- the objective and intended completion claim are explicit;
- scope and non-goals are bounded;
- authoritative inputs are available and applicable;
- constraints and material invariants are identified;
- assumptions and unknowns are visible;
- allowed and forbidden actions are sufficient to determine execution authority;
- acceptance criteria are testable;
- the verification plan can support the intended claim;
- escalation conditions are explicit;
- the target state and relevant concurrent changes are known;
- no unresolved conflict invalidates the task.

For low-risk work, the record MAY be concise. Missing semantic content MUST NOT be hidden by a longer prompt.

The Knowledge AI SHOULD detect readiness gaps before delegating to the Execution AI.

## 9. Prompt Generation

The prompt sent to the Execution AI is a serialization of the authorized task contract.

The Knowledge AI SHOULD generate the prompt so that it:

- leads with the objective and expected outcome;
- identifies the target repository, baseline, and scope;
- distinguishes authoritative inputs from supporting context;
- states constraints and non-goals;
- lists allowed and forbidden actions;
- defines acceptance criteria and expected evidence;
- states escalation conditions;
- requires a structured result report;
- references durable project artifacts;
- avoids irrelevant context that obscures authority.

The prompt MUST NOT:

- broaden the human-authorized scope;
- silently convert an assumption into a fact;
- grant authority not held by the delegator;
- copy stale knowledge without identifying its version;
- ask the Execution AI to decide matters reserved for humans;
- imply that passing checks equals final acceptance.

A generated prompt MAY include additional tactical guidance when it remains within the contract.

## 10. Reference Contract Template

The following template is a technology-independent reference. Projects MAY change its representation while preserving required semantics.

~~~markdown
# AI Execution Task Contract

## Identity

- Task ID:
- Title:
- Contract revision:
- Status: draft
- Related increment:
- Target repository and baseline:
- Created by:
- Knowledge and Review AI:
- Execution AI:
- Human authorizing authority:
- Decision authority:
- Risk authority:
- Expires or review trigger:

## Objective

### Expected outcome

### Why this work exists

### Intended completion claim

## Scope

### Included

### Excluded and non-goals

### Permitted incidental changes

### Affected consumers and environments

## Authoritative inputs

| ID or source | Version | Authority | Meaning governed |
| --- | --- | --- | --- |

## Working inputs

| Item | Classification | Limitation |
| --- | --- | --- |

## Assumptions and unknowns

| Item | Consequence if false | Validation or escalation |
| --- | --- | --- |

## Constraints and invariants

### Business

### Architecture

### Contracts

### Security, privacy, legal, and compliance

### Compatibility and migration

### Quality and operations

## Delegated actions

### Allowed

### Forbidden

### External effects

### Destructive actions

### Recovery expectations

## Deliverables

## Acceptance criteria

| Criterion | Upstream source | Verification method | Evidence required |
| --- | --- | --- | --- |

## Verification plan

### Checks to execute

### Required environment

### Success and failure conditions

### Evidence to retain

### Checks outside Execution AI authority or capability

## Escalate when

## Execution result

### Outcome

### Actual changes

### Decisions within delegated discretion

### Commands and checks

### Evidence

### Failed, skipped, or unavailable checks

### Assumptions used

### Discoveries and conflicts

### Limitations and residual risk

### Decisions required

## Knowledge AI review

### Contract conformance

### Evidence assessment

### Defects and correction requests

### Unresolved questions

### Recommendation to Human

## Human decision

- Decision:
- Decided by:
- Date:
- Accepted scope:
- Accepted limitations:
- Accepted risks:
- Follow-up:
~~~

Empty headings SHOULD be removed or marked not applicable with rationale. They SHOULD NOT be left ambiguous when they affect authority or completion.

## 11. Execution Rules for Codex or Another Execution AI

The Execution AI MUST:

1. inspect the target state before changing it;
2. read applicable authoritative knowledge;
3. confirm that the task is executable within delegated permissions;
4. preserve unrelated human and system changes;
5. implement only within accepted boundaries;
6. run checks required by the verification plan;
7. capture material discoveries and conflicts;
8. stop the affected work when an escalation condition occurs;
9. report actual changes and evidence accurately;
10. avoid claiming final acceptance.

The Execution AI MAY:

- choose routine, reversible implementation details;
- refine its local plan;
- add tests or derived documentation necessary to meet accepted criteria;
- request clarification;
- recommend a contract revision;
- return partial work when limitations are explicit.

The Execution AI MUST NOT edit the authorized task contract to make its result appear compliant.

## 12. Knowledge AI Review Protocol

The Knowledge AI reviews the Execution AI result against the authorized contract.

It MUST inspect, as applicable:

- actual changed artifacts or diff;
- target baseline and final revision;
- accepted requirements, architecture, and contracts;
- each acceptance criterion;
- test and tool output;
- failed, skipped, or unavailable checks;
- unintended changes and scope expansion;
- security, compatibility, and operational impact;
- assumptions and discoveries;
- evidence boundary and limitations;
- traceability updates.

The review SHOULD produce:

| Result | Meaning |
| --- | --- |
| **conforms** | Result satisfies the contract and evidence supports the stated claim. |
| **conforms with limitations** | Result satisfies a narrower claim with explicit limitations. |
| **correction required** | Defects can be corrected within authorized scope. |
| **human decision required** | Upstream meaning, scope, authority, or risk MUST change. |
| **rejected** | Result cannot be accepted under the current contract. |
| **review limited** | The Knowledge AI lacks access or evidence necessary for a complete review. |

The Knowledge AI MAY request corrections directly from the Execution AI only within the original authorized boundary.

It MUST NOT rewrite criteria after execution to match the implementation.

## 13. Correction Request

A correction request SHOULD contain:

- task identifier and authorized contract revision;
- defect or non-conformance;
- violated criterion or authoritative source;
- observed evidence;
- required result;
- scope that MUST remain unchanged;
- checks to repeat;
- any new limitation;
- escalation condition.

A correction is part of the existing contract only when it restores conformance without changing accepted meaning, scope, compatibility, security, evidence claim, or risk.

Otherwise the task becomes **revised** and requires human reauthorization.

## 14. Contract Change Rules

### 14.1 Clarification

A clarification MAY be made without reauthorization when it does not change observable meaning, permissions, scope, constraints, criteria, evidence claim, or risk.

The clarification SHOULD be recorded with its author and date.

### 14.2 Execution-level adjustment

The Knowledge AI or Execution AI MAY adjust tactics when the change:

- remains reversible;
- stays inside accepted architecture and contracts;
- does not affect consumers or external systems beyond scope;
- preserves acceptance criteria;
- introduces no new residual risk.

### 14.3 Material revision

Human reauthorization is required when the contract changes:

- objective or intended completion claim;
- included or excluded scope;
- authoritative interpretation;
- business rule or requirement;
- architecture or contract semantics;
- compatibility or migration;
- security, privacy, legal, or compliance control;
- allowed external or destructive action;
- acceptance criterion or evidence scope;
- residual risk.

A material revision MUST create a new contract revision and preserve the previous authorized revision.

## 15. Evidence Package

The Execution AI result SHOULD provide evidence sufficient for the Knowledge AI and Human to evaluate the declared claim.

An evidence package MAY include:

- implementation revision or diff;
- test commands and raw results;
- test, static-analysis, security, compatibility, and quality reports;
- environment and dependency versions;
- screenshots or recordings where relevant;
- reproduction steps;
- migration or rollback results;
- known skipped checks;
- failure logs;
- manual-verification requirements.

Evidence MUST state its boundary. A unit test does not prove integration, a simulated environment does not prove production behavior, and a successful build does not prove product acceptance.

The Knowledge AI SHOULD link each acceptance criterion to supporting evidence or mark it unsupported.

## 16. Traceability

A consequential task SHOULD preserve:

~~~text
product need or obligation
→ accepted increment
→ requirements and quality criteria
→ architecture decisions
→ system or component contracts
→ authorized AI Execution Task Contract revision
→ implementation revision
→ execution evidence
→ Knowledge AI review
→ human result decision
~~~

Minimum useful relationships include:

- task **realizes** Increment;
- task **depends_on** authoritative knowledge;
- implementation **realizes** task and contracts;
- evidence **verifies** criteria or implementation claims;
- review **evaluates** result and evidence;
- human decision **accepts**, **rejects**, or **limits** the result;
- material revision **supersedes** the previous contract revision.

Traceability MUST NOT imply acceptance merely because links exist.

## 17. Safety and External Effects

The task contract MUST explicitly address actions that:

- modify external repositories, services, tickets, or communications;
- deploy or publish;
- change cloud or infrastructure state;
- access protected data;
- create financial or legal effects;
- delete or irreversibly overwrite meaningful state;
- change access, credentials, or security controls.

The exact target SHOULD be resolved with read-only inspection before a consequential action.

Broad paths, unresolved variables, implicit recipients, inferred environments, or unspecified production targets MUST NOT be used as authorization.

When recovery is possible, the contract SHOULD define backup, checkpoint, rollback, or containment expectations.

## 18. Concurrent Work

Before execution, the contract SHOULD identify whether other humans, AI agents, branches, or systems MAY change the same scope.

The Execution AI MUST:

- inspect current state;
- avoid overwriting unrelated work;
- report unexpected changes;
- rebase, merge, or resolve conflicts only within delegated authority;
- stop when concurrent changes invalidate authoritative context or acceptance criteria.

A contract bound to a stale baseline SHOULD be reviewed before continuing.

## 19. Minimal and Extended Profiles

### 19.1 Minimal profile

For low-risk, reversible work, a compact contract MAY contain:

- objective and scope;
- authoritative references;
- constraints and non-goals;
- allowed change;
- acceptance criteria;
- checks to run;
- escalation conditions;
- expected result report;
- human authorization.

A well-structured short message MAY satisfy the minimal profile.

### 19.2 Extended profile

For high-risk, regulated, security-sensitive, production-critical, or multi-agent work, the contract SHOULD additionally include:

- stable identifier and controlled revision;
- explicit authority assignments;
- fixed knowledge baseline;
- data classification;
- external and destructive-action authorization;
- independent review requirements;
- separation of duties;
- detailed evidence retention;
- compatibility and migration plan;
- rollback or containment;
- expiry and reevaluation;
- formal human decision record.

## 20. Failure Signals

The following indicate likely contract failure:

- Codex receives only a broad goal without accepted scope;
- the prompt does not identify authoritative knowledge;
- ChatGPT copies assumptions into the prompt as facts;
- allowed implementation is confused with authority to change architecture or contracts;
- acceptance criteria describe activities rather than observable results;
- tests are requested without stating the claim they support;
- external actions are implied rather than explicitly authorized;
- the Execution AI changes the task contract to match its output;
- ChatGPT reviews only the Codex summary instead of actual changes and evidence;
- corrections silently broaden the original task;
- a stale task continues after upstream knowledge changes;
- successful execution is reported as final human acceptance;
- the Human cannot identify what was authorized, changed, verified, and accepted.

## 21. Conformance

A project conforms to this contract specification when, for a declared scope and KGAID version:

- consequential AI execution begins from a human-authorized, bounded task contract;
- the contract identifies objective, scope, authoritative inputs, constraints, permissions, criteria, evidence, and escalation;
- the generated Execution AI prompt preserves the authorized contract;
- task authorization, verification, and result acceptance remain distinct;
- the Execution AI stays within delegated actions and exposes discoveries;
- material changes create a revised contract and return to human authorization;
- the Knowledge AI inspects actual results and evidence against the authorized revision;
- correction loops do not expand scope or authority;
- evidence is mapped to exact criteria and limitations;
- external and destructive actions require exact authorization;
- traceability connects human intent, delegation, implementation, evidence, review, and human decision;
- final acceptance and risk remain with properly scoped humans.

Conformance does not require ChatGPT, Codex, a particular template format, repository platform, work-item system, prompt syntax, or AI provider.
