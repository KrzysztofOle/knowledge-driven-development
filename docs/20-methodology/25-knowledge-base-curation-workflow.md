---
document_id: KGAID-MTH-005
title: KGAID Knowledge Base Curation Workflow

document_type: business-process
status: proposed
version: 0.1.0

owner: Business

approval_status: pending
approved_by:
approved_at:
---

# KGAID Knowledge Base Curation Workflow

## 1. Purpose

This document describes the end-to-end workflow for turning supplied source
material into durable, governed expert knowledge in an adopting project's
Knowledge Base.

It operationalizes the accepted [Knowledge Lifecycle][knowledge-lifecycle],
[Authority Model][authority-model], [Traceability Model][traceability-model]
and [Human–AI Collaboration Model][collaboration-model] for knowledge
curation. It does not replace those models or change the KGAID 0.1.0 baseline.

The workflow covers:

- acquisition and staging of source material;
- analysis, extraction and classification of knowledge;
- consolidation with existing knowledge and glossary maintenance;
- traceability and downstream impact analysis;
- Human Authority review and approval;
- archival disposition of processed source material; and
- continuing maintenance of accepted knowledge.

This document has `proposed` status and is not a normative member of the
current baseline. An adopting project MAY use it as an operational workflow
within its local authority model. Acceptance into a future KGAID baseline
requires a separate methodology governance decision.

## 2. Empirical basis and limits

The workflow generalizes a knowledge-curation pilot performed in the 3ksef
project. In that pilot, three source materials were retained unchanged and
curated into four topic-oriented knowledge documents and a specialized
glossary. Individual documents used more than one source where the subject
crossed accounting, tax, KSeF and legal boundaries. Time-dependent rules were
isolated from more durable explanations and were given explicit source-review
dates.

The pilot demonstrated that:

- source-file boundaries are not reliable knowledge boundaries;
- staging material and governed knowledge need different authority;
- checking the existing Knowledge Base before writing reduces duplication;
- source claims often require corroboration by applicable primary sources;
- glossary work is part of curation rather than a later editorial task;
- traceability must connect knowledge to its possible product use without
  silently changing product scope; and
- temporal rules need stronger freshness controls than enduring concepts.

The empirical reference is the 3ksef knowledge-curation change at
`KrzysztofOle/3ksef@b3d717bcba891faca2035d91e0ebeed0a7b23afc`. The project is
an experience source, not a normative authority for KGAID. Project-specific
directory names, categories and legal conclusions are not generalized as
methodology requirements.

## 3. Scope and terminology

For this workflow:

- **source material** is supplied input such as a document, note, transcript,
  specification, regulation, export or research result;
- **staging** is the controlled working area that holds source material before
  and during curation;
- **knowledge unit** is one independently meaningful definition, rule,
  process, exception, constraint, dependency or expert conclusion extracted
  for evaluation;
- **knowledge document** is a governed document that owns or groups durable
  knowledge without reproducing the source material;
- **curation** is the analysis, synthesis, classification, reconciliation,
  review and integration of knowledge;
- **source disposition** records whether a staged material was processed,
  rejected, deferred or requires further evidence; and
- **Knowledge Base** is the governed set of accepted and proposed project
  knowledge, not the staging area or an undifferentiated document archive.

`knowledge-staging/incoming` and `knowledge-staging/processed` are logical
locations. An adopting project MAY place them under a project-specific parent
such as `docs/90-knowledge/`, provided that the locations and their authority
are explicit.

## 4. Governing principles

### 4.1 Sources are retained, not copied into knowledge

Source material MUST remain identifiable and unchanged while it is in staging.
The Knowledge Base MUST NOT copy or concatenate source content as if that were
curation. Knowledge documents express the relevant meaning in the project's
own expert language, with provenance back to the source.

The purpose is not to produce a source summary. Curation selects, reconciles
and explains durable meaning that can govern later work. Marketing language,
repetition, transient examples and content outside project scope SHOULD be
excluded, with material omissions recorded when they affect review.

### 4.2 Topics govern document boundaries

There is no required one-to-one relationship between a source material and a
knowledge document:

- one material MAY produce several knowledge documents when it contains
  independently owned topics;
- several materials MAY be synthesized into one document when they support or
  challenge the same topic;
- one material MAY update several existing documents without creating a new
  one; and
- a material MAY produce no knowledge document when it is irrelevant,
  duplicate, unreliable or already represented completely.

Document boundaries SHOULD follow coherent topic, semantic ownership,
authority, lifecycle and maintenance needs. A single file MAY contain several
addressable artifacts, as defined by the [Artifact Model][artifact-model].

### 4.3 One authoritative owner per meaning

Before creating a document, the curator MUST search for an existing owner of
the topic. Existing authoritative knowledge is updated through its lifecycle;
it is not restated in a parallel document. Catalogues, indexes, reports and
glossaries link to owning artifacts rather than becoming competing sources of
truth.

Similar wording is not sufficient evidence of duplication. The curator
compares scope, authority, effective context and intended use. Conversely,
different wording does not justify two artifacts that own the same meaning.

### 4.4 Expert and enduring formulation

Knowledge SHOULD describe stable concepts, rules, processes, exceptions,
constraints and dependencies rather than the incidental form of the supplied
material. It SHOULD remain useful after the original task, conversation or
example is forgotten.

Time-dependent knowledge is not made timeless by omitting dates. It is made
maintainable by separating the enduring concept from the dated rule, recording
applicability and defining a review trigger.

### 4.5 Authority remains visible

Staging material is input, not accepted project knowledge. AI output is a
proposal, not a decision. Moving a file to `processed` records source
disposition; it does not accept the resulting knowledge, prove correctness or
change the authority of the source.

## 5. Roles and responsibilities

The functional role **Knowledge Curator** MAY be performed by one or more
humans or AI tools. Performing curation does not grant decision authority.

| Role | Responsibilities in this workflow | Authority boundary |
| --- | --- | --- |
| **Human Authority** | Authorizes scope; evaluates source applicability and subject-matter correctness; resolves conflicts; owns consequential interpretations; accepts, rejects, limits or requests revision; accepts risk; approves the exact knowledge revision and source disposition. | The only final decision authority. Specialist Domain, Legal, Product, Architecture or other authorities participate when the subject requires their competence. |
| **ChatGPT** | Acts as Knowledge and Review AI in the reference realization; decomposes materials into knowledge units; compares sources and existing knowledge; identifies gaps, conflicts, duplication and temporal claims; proposes document design, glossary changes and trace links; reviews the actual curated change and evidence. | MAY propose and recommend. MUST NOT decide source applicability, legal or business meaning, accept knowledge or approve its own proposal. |
| **CODEX** | Acts as Execution AI in the reference realization; inventories repository state; implements the authorized document changes; updates indexes, glossary and trace links; preserves and moves staged files when the gate is satisfied; runs controls; reports the exact change and evidence. | MUST remain within delegated files and semantics. MUST NOT invent missing knowledge or links, resolve a material conflict, change downstream product artifacts without authority, or record final human acceptance. |
| **Future KGAID tools** | MAY support source inventory, duplicate candidates, metadata and link validation, trace-graph queries, freshness alerts, review queues, approval records and repeatable source disposition. | Automation acts only under a human-accepted policy. It reports candidates and evidence; it does not infer semantic relationships, determine truth, accept risk or replace Human Authority. |

ChatGPT and CODEX are a reference allocation, not required products. Another
toolchain conforms when it preserves the Knowledge and Review AI, Execution AI
and Human Authority semantics defined by the
[Collaboration Model][collaboration-model].

## 6. Inputs and start conditions

A curation run SHOULD begin with a bounded task contract that identifies:

- the source materials in scope;
- why the material may matter;
- the applicable Knowledge Base boundary and baseline;
- source owner, origin, version, acquisition date and available authority;
- allowed and forbidden actions;
- expected knowledge and glossary domains;
- required subject-matter reviewers;
- source licensing, confidentiality and handling constraints;
- acceptance criteria and controls;
- whether source files may be moved; and
- escalation conditions.

Material MUST NOT be processed merely because it is present in the repository.
The run needs explicit scope or a previously accepted automation policy.

For sensitive, licensed, personal or restricted material, the Human Authority
MUST confirm that repository retention and AI processing are permitted before
staging. If they are not permitted, the project uses an approved protected
location and retains only an allowed provenance reference in the Knowledge
Base.

## 7. End-to-end workflow

~~~mermaid
flowchart TD
    A["Acquire and authorize"] --> B["Place unchanged source in incoming"]
    B --> C["Inventory and establish provenance"]
    C --> D["Analyze and extract knowledge units"]
    D --> E["Classify topics and applicability"]
    E --> F["Compare with existing knowledge"]
    F --> G["Design update, creation or consolidation"]
    G --> H["Draft knowledge and glossary changes"]
    H --> I["Create traceability and impact analysis"]
    I --> J["AI review and repository controls"]
    J --> K{"Human Authority decision"}
    K -->|Revise| D
    K -->|Reject or defer| L["Record disposition"]
    K -->|Approve| M["Integrate approved revision"]
    M --> N["Move source to processed"]
    L --> N
    N --> O["Maintain, review and supersede"]
~~~

The steps express semantic gates. Low-risk activities MAY be combined, but no
combination removes provenance, review, authority or disposition requirements.

### 7.1 Acquire and authorize materials

The initiator identifies the material, its origin and the reason for
processing it. The Human Authority or accepted policy confirms scope and
handling permission.

At this step the team SHOULD:

1. identify the supplied files or references exactly;
2. record who supplied them and when;
3. identify known version, publication date and jurisdiction or system scope;
4. distinguish an authoritative source, evidence, commentary and input not yet
   verified;
5. record access, confidentiality and licensing constraints; and
6. name the subject owner and expected decision authority.

Unknown provenance does not automatically make a material useless, but it
MUST remain visible as a limitation and cannot support a stronger claim than
its authority permits.

### 7.2 Place unchanged material in `incoming`

Authorized source files are placed in `knowledge-staging/incoming` without
rewriting, normalization or silent format conversion. If a technical
conversion is required for analysis, the original is retained and the derived
copy is identified as such.

Filename collisions, multiple editions and revised sources MUST be resolved
without overwriting an earlier input. A checksum, immutable revision or other
identity evidence SHOULD be retained when integrity or reproducibility
matters.

The `incoming` location MUST be documented as non-normative. Its contents MUST
NOT be used as accepted knowledge merely because downstream work can link to
them.

### 7.3 Inventory and establish provenance

Before semantic analysis, the curator creates a run inventory containing at
least:

- source identifier or stable locator;
- source title and kind;
- origin, author or publisher when known;
- version or publication date when known;
- acquisition or observation date;
- applicable scope proposed for evaluation;
- authority and reliability observations;
- processing status; and
- known relations to previous versions or other source materials.

The inventory MAY be a task record, table, manifest or report. It does not
need to become a new normative artifact.

### 7.4 Analyze materials

The curator reads every in-scope material completely enough to evaluate its
claims in context. Analysis separates:

- sourced facts and direct observations;
- interpretations and inferences;
- assumptions and recommendations;
- definitions and vocabulary;
- rules, processes, exceptions and constraints;
- dependencies and consequences;
- examples and transient details; and
- contradictions, ambiguities and missing evidence.

Material claims are evaluated against source authority, applicability,
freshness and accepted project knowledge. AI MUST NOT silently repair gaps,
choose between conflicting sources or present an inference as a source fact.

### 7.5 Extract knowledge units

The curator expresses candidate knowledge units in new wording before deciding
their storage form. Each unit SHOULD state:

- the meaning that could remain useful;
- its subject and scope;
- applicable actors, jurisdictions, systems or versions;
- exceptions and limits;
- supporting and conflicting sources;
- whether it is fact, inference, assumption or recommendation;
- intended owner and decision authority; and
- likely downstream relevance.

Extraction excludes source rhetoric, repeated explanations and examples that
do not change the expert meaning. Rejection of content from the Knowledge Base
does not modify or delete the retained source.

### 7.6 Classify knowledge

Each unit is classified along existing KGAID dimensions before file placement:

1. **knowledge domain** — Foundations, Product and Business, Domain,
   Requirements, Architecture, Contracts, Delivery, Verification or
   Operations;
2. **artifact responsibility** — for example `TERM`, `BR`, `CAP`, `REQ`,
   `CON`, `ARC`, `ADR`, `RISK` or another locally defined artifact type;
3. **authority** — owner, decision authority and required reviewers;
4. **maturity** — captured, proposed, reviewed or accepted under the current
   lifecycle; and
5. **applicability and freshness** — stable scope, source version, observation
   date and known change triggers.

Directory categories are a storage mapping, not the semantic classification.
An adopting project defines its own layout consistently with the
[Knowledge Domains Model][knowledge-domains].

The optional timeless/temporal classification and candidate metadata fields
are described separately in Section 11. They are not part of the current
KGAID metadata standard.

### 7.7 Compare with existing knowledge

The curator searches the Knowledge Base, glossary, catalogues and trace graph
for semantic overlap. For each candidate unit, one of the following outcomes
is proposed:

- **already represented** — add no duplicate content; repair provenance or
  traceability only if authorized and meaningful;
- **clarification** — refine wording without changing observable meaning;
- **compatible update** — extend the existing owner and perform proportionate
  impact analysis;
- **semantic change or conflict** — preserve both positions, mark the conflict
  and escalate through the knowledge lifecycle;
- **new knowledge** — create a new owning artifact or document; or
- **out of scope or unsupported** — record the disposition without publishing
  it as knowledge.

When several existing documents partly own the same meaning, curation MAY
propose consolidation. Consolidation preserves stable identifiers,
supersession history and inbound traceability; it is not an unrecorded file
merge.

### 7.8 Design the change set

The proposed change set maps knowledge units to owning artifacts and files.
It makes one-to-many and many-to-one decisions explicit:

| Situation | Preferred design |
| --- | --- |
| One source covers independently owned topics. | Split the knowledge across the applicable existing or new documents. |
| Several sources cover one coherent topic. | Synthesize one owning document and preserve every material source in provenance. |
| A source adds meaning to an existing topic. | Update the existing owner rather than create a source-specific document. |
| Sources disagree. | Preserve the conflict and route it to Human Authority; do not create ambiguous compromise wording. |
| The same meaning appears in several documents. | Select the authoritative owner and replace repeated meaning with references, subject to impact review. |

The design also identifies glossary changes, downstream links, review
authorities, source disposition and controls.

### 7.9 Update or create knowledge documents

The curator updates an existing document whenever it remains the correct
semantic owner. A new document is created only when it has a coherent purpose,
scope, owner and maintenance lifecycle not already provided elsewhere.

Every material knowledge document SHOULD include or reference:

- stable identity and governed metadata;
- purpose, scope and exclusions;
- expert knowledge written in the project's own words;
- explicit exceptions, uncertainty and applicability;
- source provenance, versions and observation dates;
- related knowledge and glossary terms;
- downstream relevance without implying unapproved scope;
- review triggers for unstable dependencies; and
- owner, decision authority and lifecycle status.

Knowledge publication MUST NOT silently create or modify a Capability,
Business Rule, Requirement, Architecture Specification or ADR. When extracted
knowledge implies such a change, the curator records an impact candidate and
routes the affected artifact through its own lifecycle.

### 7.10 Update the glossary

The curator identifies new, changed, ambiguous and synonymous terms. A
glossary entry is added or updated when a stable shared definition is needed.

The glossary:

- owns concise canonical definitions;
- links to the documents that provide fuller context;
- distinguishes domain terms from product, external-system and
  implementation terms;
- avoids repeating rules, processes and architecture; and
- records temporal qualification when the meaning itself changes over time.

The owning knowledge documents use or reference glossary terms consistently.
A glossary update follows the same Human Authority review as other semantic
knowledge.

### 7.11 Establish traceability and impact

The curator creates meaningful relationships described in Section 9 and
checks both direct and transitive impact. Missing relationships are reported;
they are not invented to satisfy a link count.

The impact review determines whether the knowledge may affect Capability,
Business Rules, Requirements, Architecture, ADRs, contracts, implementation,
evidence, operations or an existing baseline. Affected downstream artifacts
retain their own owner and lifecycle.

### 7.12 Perform AI review and repository controls

Before Human Authority review, ChatGPT or another delegated reviewer SHOULD
inspect the actual proposed documents, source mapping and repository diff, not
only the execution summary. CODEX SHOULD provide reproducible control results.

Review covers:

- fidelity to sources without copied source prose;
- separation of fact, inference, assumption and recommendation;
- subject-matter correctness and unresolved conflicts;
- duplicate and ownership analysis;
- glossary consistency;
- traceability and impact completeness;
- temporal applicability and freshness;
- governed metadata and links;
- protection of unrelated project state; and
- whether the completion claim matches the checks performed.

AI review can move a proposal toward decision readiness. It cannot approve the
knowledge.

### 7.13 Human Authority review and decision

The applicable Human Authority reviews the exact proposed revision, sources,
limitations, conflicts, impact and evidence. More than one authority MAY be
required for cross-domain, legal, security, product or architecture meaning.

The Human Authority MAY:

- approve the proposal in its declared scope;
- approve it with explicit limitations or accepted risk;
- request revision;
- reject it with a recorded rationale; or
- defer it pending evidence or specialist review.

Approval records the person or accountable role, exact revision, time, scope
and limitations. Approval processing and content lifecycle status remain
separate as defined by the [Metadata Profile][metadata-profile]. A document
edited after approval returns to review according to project governance.

### 7.14 Integrate and move sources to `processed`

After the knowledge decision and successful required controls, the approved
or otherwise authorized change is integrated. Each completed source material
is moved unchanged from `knowledge-staging/incoming` to
`knowledge-staging/processed`.

The disposition record identifies:

- the source material and its previous location;
- resulting new and updated documents;
- glossary changes;
- rejected or deliberately omitted knowledge units;
- Human Authority decision or other authorized disposition;
- final processing date; and
- the exact integrated revision when available.

`processed` is an archive of handled inputs, not part of accepted knowledge.
Processed sources are not reprocessed by default. A new source version,
explicit re-evaluation request, detected conflict or maintenance trigger starts
a new bounded run without overwriting the earlier material.

If the proposal is deferred and no authorized disposition exists, the source
remains in `incoming` or another explicitly governed holding state. The
workflow MUST NOT label unresolved work as processed merely to empty the
queue.

### 7.15 Produce the final report

CODEX produces the standard report defined in Section 12. The report is a
review and audit aid. It does not replace the updated artifacts, source
provenance, Human Authority decision or raw control evidence.

## 8. Knowledge document quality criteria

A curated document is ready for Human Authority review when:

- it has one coherent purpose and explicit boundaries;
- it is written in original expert language rather than copied or mechanically
  summarized source text;
- every material claim has adequate provenance and declared applicability;
- facts, interpretations, assumptions and recommendations remain
  distinguishable;
- exceptions, conflicts, uncertainty and omitted scope are visible;
- existing authoritative knowledge was checked and duplication was avoided;
- the glossary is consistent and updated where needed;
- meaningful traceability and downstream impact are recorded;
- time-dependent content includes current freshness information and a review
  trigger;
- owner, reviewers, decision authority and lifecycle status are clear; and
- required documentation controls pass or their limitations are reported.

Expert quality does not mean certainty beyond the evidence. A bounded,
well-sourced statement with a visible uncertainty is preferable to confident
but unsupported prose.

## 9. Traceability model for curation

### 9.1 Two connected traceability layers

Knowledge curation connects two layers:

~~~text
source material and applicable primary references
→ curated knowledge and TERM definitions
→ CAP / BR / REQ / CON
→ ARC / ADR / CTR
→ INC / EVD / operations
~~~

The first arrow records provenance and synthesis. The later arrows record
semantic dependency and realization under the accepted
[Traceability Model][traceability-model]. A Markdown link is navigation; it
does not by itself establish a typed semantic relation.

### 9.2 Source-to-knowledge provenance

Each knowledge document records the material sources that contributed meaning,
including:

- stable source identifier or locator;
- version, publication date or immutable revision when available;
- observation or verification date for unstable information;
- applicable scope and authority;
- the claim or section supported;
- transformations or corroboration used; and
- known disagreement or uncertainty.

When a project models a staged source as an artifact, `derived_from` MAY link a
non-authoritative derivative to that source. Binding rules use
`sources_of_obligation` as defined for `BR`. A project MAY define a local
provenance representation, but it MUST NOT reinterpret a repository path or
web address as semantic authority.

### 9.3 Knowledge and glossary

Glossary `TERM` artifacts own canonical definitions. A curated document uses
those terms and provides context, rules or processes without creating a second
definition. A new or changed definition identifies the knowledge and sources
from which it follows and is reviewed by the authority for that domain.

### 9.4 Knowledge and Capability

A `CAP` MAY depend on applicable domain knowledge or a qualifying `BR` when
that knowledge constrains the ability the product provides. A knowledge
document MAY identify a candidate Capability impact, but only the Product
Authority changes or accepts the Capability.

### 9.5 Knowledge and Business Rules

A durable, independently normative domain or regulatory rule is a candidate
`BR` when it meets the [Business Rule qualification criteria][br-criteria].
Its source of obligation, scope and terminology are recorded. Descriptive
knowledge does not become a `BR` merely because it appears important or uses
imperative language.

### 9.6 Knowledge and Requirements

A `REQ` depends on applicable upstream `CAP`, `BR`, use-case or constraint
knowledge when it translates that meaning into an observable system
obligation. Curated knowledge can reveal a Requirement candidate; it does not
silently establish the obligation or expand delivery scope.

### 9.7 Knowledge and Architecture

An `ARC` depends on accepted Requirements, quality needs, constraints and
applicable domain knowledge. Curation records potential architectural impact
when new knowledge changes boundaries, ownership, data lifecycle, integration,
security or another structural concern. The Architecture Authority owns the
resulting change.

### 9.8 Knowledge and ADRs

An `ADR` references the accepted knowledge, Requirements, Business Rules and
constraints that affected a durable choice. New knowledge MAY invalidate an
assumption or reveal a decision impact. It does not edit the historical
meaning of an accepted ADR; a material decision change requires a new ADR that
supersedes the earlier one.

### 9.9 Minimum curation mapping

Every completed run retains a reproducible mapping with at least:

| From | To | Recorded meaning |
| --- | --- | --- |
| Source material | Knowledge document or explicit no-output disposition | What was synthesized, updated, rejected or deferred. |
| Source claim | Knowledge claim or section | Which source, version and scope support the meaning. |
| Knowledge document | `TERM` | Which definitions it uses or helps establish. |
| Knowledge document or `BR` | `CAP`, `REQ`, `CON`, `ARC`, `ADR` as applicable | Candidate impact or accepted semantic dependency, clearly distinguished. |
| Changed knowledge | Downstream artifacts and evidence | Which owners must review impact and which claims may require refresh. |

The mapping records `not applicable` with a rationale when an expected
downstream class has no meaningful relationship. It MUST NOT manufacture empty
links for completeness.

## 10. Approval and source disposition gates

The workflow uses the existing KGAID knowledge gates:

| Gate | Curation evidence |
| --- | --- |
| `KG-1 Proposal Ready` | Sources, provenance, scope, knowledge units, owner and assumptions are identified. |
| `KG-2 Decision Ready` | Duplicate analysis, source conflicts, glossary, traceability, impact, risks and controls have been reviewed. |
| `KG-3 Accepted Knowledge` | The applicable Human Authority accepted the exact curated artifacts and limitations. |

Moving a source to `processed` requires:

1. a complete source-to-outcome mapping;
2. no unrecorded blocking conflict;
3. required controls completed successfully or limitations accepted by the
   proper authority;
4. an approved or otherwise explicit Human Authority disposition; and
5. preservation of the source without semantic modification.

This disposition gate does not imply `KG-4 Realization Ready` or any claim
about implementation, verification, baseline or release.

## 11. Proposed future extension: temporal knowledge classification

> **Proposal — not current KGAID standard.** This entire section describes a
> possible extension of the methodology. It requires a separate Human
> Authority decision, metadata-profile design, compatibility analysis and
> acceptance through KGAID governance. The fields below MUST NOT be treated as
> required or currently supported KGAID governed-document metadata.

### 11.1 Candidate knowledge types

The 3ksef pilot exposed a useful distinction:

- **timeless** knowledge expresses a concept, invariant, relationship or
  expert explanation expected to remain valid until explicitly superseded;
- **temporal** knowledge is valid only for a known period, version,
  jurisdiction, external-system state or other time-bounded context.

`timeless` would not mean eternally true. It would mean that no known expiry is
part of the current claim. Source and review dates would still be retained
where required. `temporal` would make known applicability bounds explicit and
support freshness checks.

### 11.2 Candidate fields

One possible front-matter representation is:

~~~yaml
knowledge_type: timeless
valid_from:
valid_until:
~~~

or:

~~~yaml
knowledge_type: temporal
valid_from: YYYY-MM-DD
valid_until: YYYY-MM-DD
~~~

Candidate semantics:

| Field | Proposed meaning |
| --- | --- |
| `knowledge_type` | Controlled value `timeless` or `temporal`. |
| `valid_from` | First date or timestamp for which the represented knowledge is applicable; empty only when the start is unknown or not bounded. |
| `valid_until` | Last date or timestamp, or an exclusive boundary defined by the future profile, after which the knowledge is not applicable; empty when no known end exists. |

Before adoption, governance would need to decide:

- whether validity belongs at document, artifact or claim level;
- inclusive or exclusive date semantics;
- date versus timestamp and timezone rules;
- unknown, open-ended and version-based applicability;
- interaction with `status`, approval, supersession and source freshness;
- validation rules for documents containing both kinds of knowledge;
- migration of existing metadata and tools; and
- whether temporal expiry triggers review, status change, evidence
  invalidation or only a warning.

Until that decision is made, projects use existing source versions,
observation dates, applicability statements, review triggers and lifecycle
mechanisms. A local project MAY pilot equivalent fields only as an explicitly
documented project extension; that pilot does not alter KGAID conformance or
the current [Metadata Profile][metadata-profile].

## 12. Standard CODEX final report

After a curation run, CODEX SHOULD return a concise report with the following
sections.

### 12.1 Scope and result

- task objective and Knowledge Base scope;
- exact branch or working revision;
- completion claim and any limitation;
- Human Authority decision still required or already recorded.

### 12.2 Processed source materials

For every in-scope source:

- source identifier and original `incoming` path or stable locator;
- source version, date and provenance when available;
- final disposition: processed, rejected, deferred or blocked;
- resulting `processed` path when moved; and
- integrity or preservation note.

### 12.3 Knowledge changes

- new documents and artifacts;
- updated documents and artifacts;
- superseded or consolidated artifacts;
- source material mapped to every resulting knowledge document;
- deliberate no-output decisions and excluded content with rationale.

### 12.4 Glossary, duplication and consolidation

- terms added, changed or linked;
- duplicate candidates found;
- duplicates avoided or removed;
- decisions to split one source across documents;
- decisions to merge several sources into one topic; and
- unresolved ownership conflicts.

### 12.5 Traceability and impact

- source-to-knowledge mapping;
- links to related knowledge and `TERM` artifacts;
- accepted relationships and candidate impacts involving `CAP`, `BR`, `REQ`,
  `CON`, `ARC`, `ADR`, contracts, implementation and evidence;
- downstream artifacts requiring review; and
- explicitly non-applicable traceability classes with rationale where useful.

### 12.6 Authority, uncertainty and maintenance

- reviewers and decision authorities;
- approvals, requested decisions and accepted limitations;
- source conflicts, assumptions and unsupported claims;
- time-sensitive knowledge, source-review dates and maintenance triggers;
- proposed future extensions kept outside current standard.

### 12.7 Controls and repository state

- every command executed and its result;
- documentation validation result;
- internal-link validation result;
- `git diff --check` result;
- checks not run and the exact reason;
- files changed outside the expected scope, if any;
- local commit identifier and Conventional Commit subject when authorized; and
- explicit confirmation that no push was performed unless separately
  authorized.

The report MUST distinguish successful checks from checks that were not run or
were inconclusive. A narrative statement that the work looks correct is not a
substitute for raw or reproducible evidence.

## 13. Continuing maintenance

Accepted knowledge remains governed after the source leaves `incoming`.
Maintenance triggers include:

- a new edition or withdrawal of a source;
- arrival of a conflicting or more authoritative source;
- a known effective date or expiry;
- change in law, standard, external system or product boundary;
- downstream implementation or verification discovering an invalid
  assumption;
- glossary drift or duplicate meaning;
- broken traceability or a superseded dependency;
- scheduled domain review; and
- operational evidence that challenges accepted knowledge.

On a trigger, the owner:

1. identifies the affected claims and source versions;
2. traverses direct and transitive traceability;
3. classifies the change as clarification, compatible change or semantic
   change;
4. re-enters the knowledge lifecycle at the appropriate stage;
5. updates or supersedes the authoritative artifact;
6. refreshes glossary, downstream knowledge and evidence as required;
7. obtains renewed Human Authority review and approval; and
8. preserves historical sources, revisions, decisions and invalidated
   evidence.

An accepted knowledge document MUST NOT be edited in place to hide that its
former meaning was once applicable. Versioning, supersession and decision
history preserve that context.

## 14. Failure signals

The following indicate that the workflow is not operating as intended:

- source files are pasted or lightly paraphrased into the Knowledge Base;
- one source automatically becomes one document regardless of topic;
- a new file is created without checking the existing knowledge owner;
- multiple documents repeat the same normative meaning;
- source authority, version, date or applicability is missing for a material
  claim;
- temporal knowledge is written as an undated universal rule;
- a glossary restates rules instead of owning concise terms;
- product scope, Business Rules, Requirements or Architecture change as a side
  effect of curation without their authorities;
- staged files are overwritten or deleted;
- files move to `processed` while their disposition is unresolved;
- AI resolves source conflicts or approves its own proposal;
- links are added without real semantic meaning; or
- the final report claims checks or approval that did not occur.

## 15. Conformance of an adopting workflow

An adopting project follows this workflow when it:

- separates non-normative staging from governed knowledge;
- preserves source identity, provenance and applicable handling constraints;
- curates meaning in original expert language;
- designs documents by topic and ownership rather than input-file boundaries;
- checks existing knowledge and avoids competing sources of truth;
- maintains glossary and meaningful traceability;
- preserves Human Authority for consequential interpretation and acceptance;
- records source disposition and moves only completed material to
  `processed`;
- maintains accepted knowledge through change and supersession; and
- reports the result and controls reproducibly.

Conformance does not require the exact example directory tree, ChatGPT, CODEX,
a particular file format or adoption of the proposed temporal fields.

[artifact-model]: ../10-knowledge-architecture/12-artifact-model.md
[authority-model]: ../10-knowledge-architecture/14-authority-model.md
[br-criteria]: ../10-knowledge-architecture/12-artifact-model.md#42-business-rule-qualification
[collaboration-model]: 22-human-ai-collaboration.md
[knowledge-domains]: ../10-knowledge-architecture/16-knowledge-domains.md
[knowledge-lifecycle]: ../10-knowledge-architecture/13-knowledge-lifecycle.md
[metadata-profile]: ../50-governance/metadata-profile.md
[traceability-model]: ../10-knowledge-architecture/15-traceability-model.md
