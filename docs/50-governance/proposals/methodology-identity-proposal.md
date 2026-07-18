# Methodology Identity Proposal

**Proposal status:** Accepted  
**Knowledge status:** Accepted  
**Version:** 1  
**Project:** Knowledge-Governed AI-Assisted Development  
**Created:** 2026-07-18  
**Accepted:** 2026-07-18  
**Accepted by:** Krzysztof Olejnik — KGAID Methodology Owner  
**Owner:** Knowledge Steward  
**Decision authority:** Krzysztof Olejnik — KGAID Methodology Owner  
**Proposed by:** Human–ChatGPT collaboration  
**Depends on:** [AUD-002 — Knowledge-Driven Development Name and Prior-Use Landscape Review](../audits/AUD-002-knowledge-driven-development-landscape-review.md)  
**Normative effect:** Establishes the official methodology identity and authorizes controlled documentation migration

## 1. Purpose

This proposal explores a distinctive methodology name after AUD-002 confirmed that **Knowledge Driven Development (KDD)** was already published as the name of a materially related software-development methodology.

The new identity should preserve three meanings:

1. accepted knowledge constrains and guides project work;
2. AI supports analysis, execution, testing, and review;
3. humans retain authority, risk ownership, and final acceptance.

## 2. Evaluation of the Initial Suggestion

The initial working suggestion was similar to:

> Knowledge–AI-Driven Development

The grammatically clearer English form would be:

> Knowledge- and AI-Driven Development

This form is not recommended because **AI-driven** suggests that AI directs the project. That conflicts with the accepted KGAID principle that AI assists while humans retain consequential decision authority. It also retains **Driven Development**, which remains close to the earlier Knowledge Driven Development name.

## 3. Candidate Comparison

| Candidate | Strength | Weakness | Preliminary landscape |
| --- | --- | --- | --- |
| **Knowledge- and AI-Driven Development** | Mentions both knowledge and AI. | Implies AI authority; remains close to prior KDD. | Not recommended on semantic grounds. |
| **Knowledge-First Development** | Short and understandable. | Does not expose AI or human governance; phrase is already used in current agentic-development writing. | Existing descriptive uses found. |
| **Knowledge-Guided Development** | Expresses the role of knowledge. | Previously used in domain-specific academic software work; does not expose AI governance. | “Knowledge Guided Development of Videogames” appeared in 2011. |
| **Human-Governed AI-Assisted Development** | Correctly expresses human authority and AI's supporting role. | Knowledge disappears from the name; the exact phrase is already used publicly. | Existing 2026 practitioner use found. |
| **Knowledge-Guided AI-Assisted Development** | Accurate separation between knowledge and AI. | Long; “guided” may understate the authority of accepted knowledge. | No exact indexed match found in the preliminary search. |
| **Knowledge-Governed AI-Assisted Development** | Expresses governed knowledge, AI assistance, and a distinct identity. | Human authority requires an explicit subtitle and definition; name is long. | No exact indexed match found in the preliminary search. |

Search absence is not proof of legal or global availability. This was not a trademark clearance.

## 4. Accepted Identity

### Knowledge-Governed AI-Assisted Development (KGAID)

**Official abbreviation:** **KGAID**

The abbreviation treats **AI** as one semantic element:

- **K** — Knowledge;
- **G** — Governed;
- **AI** — AI-Assisted;
- **D** — Development.

### Accepted descriptor

> An open, human-governed methodology in which accepted knowledge guides and constrains AI-assisted software development from product intent to verified operation.

### Accepted short proposition

> Knowledge governs the work. AI assists the work. Humans authorize the work.

## 5. Why This Name Fits the Methodology

### Knowledge-Governed

Project work is governed by explicit, accepted, versioned, and traceable knowledge. Code does not silently redefine product intent, business rules, architecture, contracts, or evidence.

“Governed” does not mean knowledge makes decisions by itself. Humans establish authority and accept knowledge; accepted knowledge then constrains downstream action until it is explicitly changed.

### AI-Assisted

ChatGPT and Codex may analyze, propose, implement, test, and review, but neither AI accepts its own proposal, project risk, baseline, or release.

This avoids the misleading implication of **AI-driven** development.

### Development

The scope remains broader than coding. It covers product framing, domain understanding, requirements, architecture, contracts, implementation, verification, operation, and learning.

## 6. Relationship to the Previous Name

Following acceptance:

- **Knowledge Driven Development** and **KDD** become the historical working name of this repository;
- **knowledge-driven development** may remain a descriptive phrase where it is clearly not presented as a proprietary or uniquely coined name;
- AUD-002 remains the provenance record explaining the rename;
- the new identity must not imply ownership of the earlier KDD term or methodology;
- repository content remains subject to a separate licensing decision.

## 7. Decision Record

**Decision:** Accept **Knowledge-Governed AI-Assisted Development (KGAID)** as the official methodology name.

**Human decision:** Krzysztof Olejnik accepted the name on 2026-07-18.

**Rationale:** The name distinguishes the methodology from earlier Knowledge Driven Development usage and accurately states that governed knowledge constrains the process while AI assists and humans retain authority.

## 8. Acceptance Assessment

The Methodology Owner confirmed that:

- the name represents knowledge, AI assistance, and human authority accurately;
- it is sufficiently distinct from the earlier KDD methodology for continued methodology development;
- its length and abbreviation are usable;
- the migration scope is understood;
- the descriptor and short proposition are accepted.

A broader name, acronym, domain, repository, and trademark review remains an open assurance activity and may trigger a later review if it reveals an unacceptable conflict.

## 9. Migration Scope

The controlled migration covers:

- repository name and description;
- root README;
- normative document titles and metadata;
- internal links and diagrams;
- artifact prefixes only where they encode the methodology name;
- adoption and conformance declarations;
- references in KSeF_2, 3ksef, and future projects;
- baseline, release, and license preparation;
- prior-use acknowledgment and changelog.

Acceptance authorizes a controlled documentation migration. Renaming the GitHub repository remains a separate decision because it changes external addresses and integrations.
