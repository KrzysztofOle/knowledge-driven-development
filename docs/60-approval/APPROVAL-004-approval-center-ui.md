# APPROVAL-004 — Approval Center UI

- **Status:** Proposed
- **Classification:** Informational functional design
- **Scope:** Reusable KGAID capability
- **Depends on:** [APPROVAL-002](APPROVAL-002-approval-process.md),
  [APPROVAL-003](APPROVAL-003-metadata-specification.md)

## 1. Purpose

This document defines the future user experience of Approval Center. It
describes information, actions, safeguards and views without selecting a user
interface framework, visual system or delivery technology.

The interface is a decision workspace, not a file browser with approval
buttons. It must keep the exact revision, authority, change and impact visible
at the point of decision.

## 2. Users and goals

| User responsibility | Primary goal |
| --- | --- |
| Author or contributor | Prepare, submit and respond to review findings. |
| Knowledge Owner | Maintain quality, status, relationships and current meaning. |
| Reviewer | Evaluate changes within an assigned concern. |
| Decision Authority | Make an informed, scoped and attributable decision. |
| Knowledge Steward | Detect structural, metadata and traceability problems. |
| Auditor or observer | Reconstruct decisions and their historical context. |

A person may switch between responsibilities. The interface makes the active
responsibility and authority scope explicit, especially when one person is
both author and Decision Authority.

## 3. Information architecture

Approval Center contains seven primary views:

1. Dashboard;
2. approval queue;
3. document details;
4. change comparison;
5. traceability and relationships;
6. decision and event history; and
7. governance and data-quality findings.

Every view retains a visible path back to the authoritative Markdown content.
Derived summaries disclose their source revision and freshness.

## 4. Dashboard

The Dashboard provides an orientation to current approval work, not a quality
score. It should show:

- decisions awaiting the current user's action;
- reviews assigned to the current user;
- submissions returned for changes;
- approvals blocked by missing authority, metadata or dependencies;
- recently accepted, rejected, superseded and retired documents;
- changed accepted knowledge with unresolved downstream impact;
- stale or invalidated review and approval cases;
- unresolved conflicts and significant relationship gaps; and
- project or knowledge-space context.

Dashboard summaries must be explainable. Selecting a count opens the exact
set and filter that produced it. A zero count must distinguish “none found”
from “data unavailable” or “index out of date.”

Approval volume, reviewer speed and queue age may support capacity planning,
but the interface must not present them as evidence of decision quality.

## 5. Approval queue

The queue is the main work view for submissions and reviews. Each row or item
must expose enough context to prioritize safely:

- document ID, title, type and project;
- candidate version and previous accepted version;
- knowledge and approval status;
- submitted scope and change classification;
- author, Knowledge Owner and Decision Authority;
- current user's required action and review discipline;
- submission time and applicable due condition, if any;
- open blockers, conflicts, risks and missing reviews;
- impact summary and number of affected dependants; and
- freshness of the indexed source.

Bulk selection may support navigation or assignment. Consequential decisions
must not be reduced to an unexplained bulk action. A grouped decision is
available only when the process requirements for a coherent decision boundary
are satisfied.

## 6. Filters, sorting and saved views

Users need combinable filters for:

- project or knowledge space;
- document type and scope;
- knowledge status and approval status;
- author, owner, reviewer and Decision Authority;
- action required from the current user;
- submitted or decision time range;
- change classification;
- required review discipline;
- blocker, conflict, risk or missing metadata;
- dependency or affected artifact;
- baseline membership; and
- current, superseded, retired or rejected history.

Filters show their active values and can be cleared individually. Search and
filter results distinguish exact identifiers from textual matches. Saved views
store query intent, not copied document status, so they remain current.

Sorting should support decision relevance, age, impact and stable document
identity. A default sort must not hide high-impact or blocked work merely
because it is newer or older.

## 7. Document details

The document-details view combines the authoritative content with decision
context. It contains:

- identity, title, type, scope, version and exact revision;
- authoritative location and source freshness;
- current accepted version and candidate version;
- knowledge, approval, implementation and verification statuses separately;
- author, owner, reviewers and scoped Decision Authority;
- change summary, rationale and classification;
- required metadata and validation findings;
- open review comments, conditions, limitations and risks;
- dependencies, dependants, conflicts and related artifacts;
- approval actions available to the current user; and
- links to full history, comparison and traceability views.

The interface must visually distinguish authoritative document content,
recorded metadata, derived summaries and AI-generated analysis. A generated
summary never obscures or replaces the exact content under review.

## 8. Change comparison

The comparison view answers both “what text changed?” and “what meaning may be
affected?” It should provide:

- candidate revision versus the selected comparison reference;
- default comparison with the previous accepted version;
- added, removed and changed content with surrounding context;
- metadata and relationship changes alongside content changes;
- moved or renamed sections without presenting all movement as new meaning;
- a change summary supplied by the author;
- AI-assisted semantic observations clearly marked as recommendations;
- review comments anchored to the compared revision; and
- warnings when the comparison source is missing or not the accepted reference.

Users can inspect the complete candidate and complete accepted version at any
time. Collapsed unchanged sections remain discoverable. A small textual diff
must not be equated automatically with a low semantic impact.

## 9. Traceability and relationships

The traceability view presents the candidate in its knowledge context:

- direct upstream dependencies and their versions and statuses;
- derived downstream dependants and likely impact;
- `supersedes`, `derived_from`, `satisfies`, `realizes`, constraints, evidence
  and conflict relationships;
- missing, ambiguous or unresolved references;
- relationship direction and meaning;
- paths from purpose through accepted knowledge to evidence; and
- baseline membership and cross-project boundaries where applicable.

Users can switch between a concise relationship list and a graph-oriented
view. Both represent the same underlying relationships. The graph limits
visible depth by default, explains hidden nodes and avoids implying that visual
proximity means semantic dependency.

Every derived inverse relationship identifies its authoritative forward link.
Users may propose a relationship correction, but the interface does not edit
the inverse as an independent source.

## 10. History

History supports two complementary perspectives.

### 10.1 Version history

Version history shows:

- all durable revisions and governed versions;
- current accepted, candidate, rejected, superseded and retired states;
- change summaries and comparison links;
- previous accepted version and supersession chain; and
- baseline membership for historical reconstruction.

### 10.2 Decision and event history

Decision history shows:

- creation, submission, review and resubmission events;
- reviewer findings and their disposition;
- approval, rejection, cancellation, supersession and retirement;
- actor, responsibility, scope, time and rationale for each action;
- conditions, limitations, waivers and accepted risks; and
- source or authority gaps known at that point in time.

History is append-oriented. Corrections retain the original event and record
the correction, reason and authorized actor. The view can reconstruct what a
decision maker saw without presenting old content as current.

## 11. Review and decision workflow

### 11.1 Submit

Before submission, the interface presents a readiness summary containing the
exact revision, comparison reference, required reviewers, Decision Authority,
validation findings and declared exceptions. The submitter confirms the scope
and change rationale.

### 11.2 Review

Reviewers can:

- record a scoped recommendation;
- add findings anchored to content, metadata or relationships;
- request changes;
- identify conflicts, risks and additional review needs; and
- state limitations of their review.

The interface makes clear that a recommendation is not acceptance.

### 11.3 Decide

Approval and rejection actions require a final decision view showing:

- exact candidate and comparison reference;
- authority under which the user acts;
- completed and missing reviews;
- unresolved blockers, conflicts and risk decisions;
- downstream impact;
- rationale, scope, limitations and conditions to be recorded; and
- effect on any previous accepted version.

The decision confirmation states the semantic consequence in plain language.
The control is unavailable when human authority or revision integrity cannot be
established. It never defaults to approval.

### 11.4 Revise and resubmit

Authors can see findings grouped by disposition, compare the new revision with
both the rejected or returned candidate and the last accepted version, and
submit a new case. Previous reviews remain visible but are marked stale when
their subject changed.

### 11.5 Retire

Retirement uses a dedicated impact-focused workflow. It shows active
dependants, baselines, replacement status, effective timing and required
authorities before the decision is recorded.

## 12. Notifications and attention

Approval Center should notify users when:

- an assigned review or decision becomes actionable;
- a candidate changes and invalidates their review;
- a finding is answered or requires follow-up;
- authority or dependency changes affect a case;
- accepted upstream knowledge changes;
- a decision is recorded; or
- a retirement or supersession affects owned knowledge.

Notifications link to the exact subject and reason. They are reminders, not
decision records. Users can control non-consequential frequency without
suppressing mandatory governance conditions in the workspace.

## 13. Permissions and authority safeguards

The interface distinguishes visibility, contribution, review and decision
capabilities. It must:

- show why an action is available or unavailable;
- evaluate authority within project, artifact and decision scope;
- expose applicable delegation and its limits;
- prevent AI or automation from performing human acceptance;
- prevent stale pages from deciding on a changed revision;
- require explicit acknowledgement of waivers and accepted risks; and
- record denied or failed consequential actions proportionately.

Permission to use a control is not proof of domain competence. Approval policy
and organizational accountability remain necessary.

## 14. States, errors and freshness

Every view accounts for:

- loading or incomplete derived information;
- no matching records;
- stale source or index;
- inaccessible authoritative content;
- invalid or incomplete metadata;
- unresolved identity or authority;
- changed revision during review;
- broken relationships; and
- partial history.

In uncertain states, Approval Center may allow investigation and comment but
must prevent an ambiguous acceptance. Error messages state what is known, what
is unknown, the affected scope and the next responsible action.

## 15. Usability and accessibility requirements

The future interface must:

- be usable without relying only on color, pointer interaction or graph views;
- give every action and status a textual meaning;
- preserve keyboard navigation and logical focus order;
- expose complete labels for identifiers, roles and decision consequences;
- support readable comparison of long documents;
- avoid motion or density that hides consequential information;
- adapt to different display sizes without removing decision context; and
- use consistent KGAID terminology across projects.

## 16. Functional acceptance criteria

The UI design is adequate when a user can:

1. find every case requiring their scoped action;
2. identify the exact candidate and currently accepted version;
3. understand content, metadata and relationship changes;
4. inspect upstream justification and downstream impact;
5. distinguish review recommendations from human acceptance;
6. record a scoped decision with rationale and limitations;
7. revise and resubmit without losing earlier history;
8. reconstruct rejection, supersession and retirement; and
9. recognize stale, incomplete or unavailable data before deciding.

## 17. Related documents

- [Vision](APPROVAL-001-vision.md)
- [Approval Process](APPROVAL-002-approval-process.md)
- [Metadata Specification](APPROVAL-003-metadata-specification.md)
- [Architecture](APPROVAL-005-architecture.md)
- [Roadmap](APPROVAL-006-roadmap.md)
- [Approval Center index](README.md)
