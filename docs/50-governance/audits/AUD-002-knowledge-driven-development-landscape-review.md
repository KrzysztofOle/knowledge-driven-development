# AUD-002 — Knowledge-Driven Development Name and Prior-Use Landscape Review

**Artifact type:** AUD  
**Audit status:** Completed  
**Knowledge status:** Reviewed  
**Version:** 1  
**Project:** Knowledge-Driven Development  
**Review date:** 2026-07-18  
**Owner:** Knowledge Steward  
**Decision authority:** Krzysztof Olejnik — KDD Methodology Owner  
**Performed by:** ChatGPT acting as Knowledge and Review AI  
**Independence:** V0 semantic review with external primary-source evidence  
**Normative effect:** None; this review does not rename KDD, determine legal rights, or change accepted methodology knowledge

## 1. Decision Context

This review was commissioned before selecting a repository license because the exact term **Knowledge Driven Development** and the abbreviation **KDD** were already visible in public software-engineering literature.

The review answers four questions:

1. Was the exact name used before this repository?
2. Does earlier work describe only a generic idea, or a named software-development methodology?
3. Where does the methodology in this repository overlap with and differ from earlier uses?
4. What decisions are required before a public KDD 0.1 baseline?

## 2. Executive Conclusion

**The exact name “Knowledge Driven Development” and abbreviation “KDD” predate this repository and identify a published software-development methodology.**

The strongest evidence is Manoj Kumar Lal's 2018 book *Knowledge Driven Development: Bridging Waterfall and Agile Methodologies*, published by Cambridge University Press. Its accessible publisher material describes:

- a named KDD methodology;
- project knowledge as a primary companion to software;
- a structured Project Knowledge Model;
- end-to-end project delivery;
- traceability;
- quality gates;
- compatibility with existing delivery methods;
- knowledge evolution and reuse.

Earlier academic material also used the broader phrase **knowledge-driven software development**. A 2010 University of Malta record refers to PhD research titled *A knowledge driven software development life cycle*. Other papers use “knowledge-driven” descriptively for model-aware, ontology-based, or domain-specific development approaches.

Therefore this project MUST NOT claim that it coined the term, abbreviation, or general proposition that software development can be driven by structured knowledge.

The methodology in this repository still contains potentially original expression, structure, synthesis, rules, and practices. Its clearest documented differentiators are:

- explicit human decision authority;
- separation of Knowledge and Review AI from Execution AI;
- the Human–ChatGPT–Codex control loop;
- bounded AI Execution Task Contracts;
- contracts-before-code as a foundational rule;
- claim-first verification and evidence boundaries;
- explicit artifact lifecycle, semantic authority, conformance, and baseline models.

Those differentiators do not remove the naming conflict or the material conceptual overlap.

**Recommendation:** do not publish the first baseline under the unqualified name “Knowledge-Driven Development (KDD)” until the Methodology Owner chooses either a distinctive name or a clearly qualified identity with an explicit prior-use acknowledgment and comparison.

## 3. Scope and Method

The review covered:

- exact phrase: “Knowledge Driven Development”;
- hyphenated variant: “Knowledge-Driven Development”;
- broader phrase: “knowledge-driven software development”;
- abbreviation: “KDD”;
- primary publisher, academic, institutional, professional-association, and first-party practitioner sources;
- comparison with the accepted principles and models in this repository;
- publicly visible origin evidence from KSeF_2.

Sources were classified as:

- **named methodology** — the source presents KDD as an identified method or framework;
- **descriptive use** — “knowledge-driven” characterizes another method or technical approach;
- **acronym collision** — KDD has a well-established unrelated meaning;
- **contemporary use** — current usage that helps assess discoverability but does not by itself establish the earliest origin.

## 4. Limitations

- This is not legal advice and does not determine copyright, trademark, unfair-competition, or naming rights.
- No comprehensive trademark clearance was performed.
- The full 2018 book was not reviewed; the analysis uses its official front matter, contents, foreword, and preface plus ACM metadata and later author publications.
- Paywalled or non-indexed literature may contain earlier or additional uses.
- The search was conducted mainly in English, with one contemporary Spanish-language source.
- Public repository history does not prove when Krzysztof Olejnik first conceived or privately used the working method.
- Similarity findings compare concepts available in reviewed sources, not source code or sentence-level copying.
- V0 means the semantic comparison was performed in the same AI collaboration context that helped author the current repository.

## 5. Source Landscape

| ID | Date | Source | Classification | Material evidence |
| --- | --- | --- | --- | --- |
| **SRC-01** | 2010 | [University of Malta — *On knowledge management in software development life cycles*](https://www.um.edu.mt/library/oar/handle/123456789/94413) | Descriptive and research-program use | The institutional record says software engineering is knowledge-intensive and refers to ongoing PhD research titled *A knowledge driven software development life cycle*. |
| **SRC-02** | 2013 | [MDPI — *Architecture and Knowledge-Driven Self-Adaptive Security in Smart Space*](https://www.mdpi.com/2073-431X/2/1/34) | Descriptive technical use | The paper combines quality-, model-, and knowledge-driven software development through ontologies and adaptive-security design. |
| **SRC-03** | 2018 | [Cambridge University Press — official front matter for *Knowledge Driven Development*](https://assets.cambridge.org/97811084/75211/frontmatter/9781108475211_frontmatter.pdf) | Exact named methodology | First published in 2018, ISBN 978-1-108-47521-1. The publisher material identifies Manoj Kumar Lal, KDD, the Project Knowledge Model, end-to-end delivery, traceability, quality gates, reuse, and Waterfall/Agile integration. |
| **SRC-04** | 2018/2019 | [SCITEPRESS — *Model-Aware Software Engineering*](https://www.scitepress.org/papers/2018/66941/66941.pdf) | Descriptive method use | The paper positions Model-Aware Software Engineering as a knowledge-driven software-development method centered on evolving modeling languages and knowledge representation. |
| **SRC-05** | 2022 | [ACM — *Seeding industry knowledge in computer science education*](https://dl.acm.org/doi/10.1145/3561833.3564559) | Continuation of named framework | Lal describes KDD as a knowledge-management framework that drives software development through reusable industry knowledge. |
| **SRC-06** | current | [ACM SIGKDD](https://kdd.org/) | Acronym collision | ACM's long-established SIGKDD expands KDD as Knowledge Discovery and Data Mining and dominates search results for the abbreviation. |
| **SRC-07** | 2026 | [AWS Builder Center — *Qué es Knowledge Driven Development y por qué la IA lo necesita*](https://builder.aws.com/content/3Euh1e1W8NQquMJZM2LTCtsbABQ/que-es-knowledge-driven-development-y-por-que-la-ia-lo-necesita) | Contemporary practitioner use | The indexed first-party article describes project knowledge as structured, versioned, and actively used in AI-assisted software development. It demonstrates that similar terminology remains in active independent use. |
| **SRC-08** | 2026 | [KSeF_2 initial public commit](https://github.com/KrzysztofOle/KSeF_2/commit/44a2b82945990a91ba9c6b309f6f697d0bde08d3) | This project's empirical provenance | The reviewed public KSeF_2 history begins on 2026-07-08. It supports practical provenance for this repository but does not establish priority over the earlier literature. |

## 6. The Strongest Prior Use: Lal's KDD

The 2018 publication is not merely an incidental use of an adjective. It explicitly presents **Knowledge Driven Development (KDD)** as a new project-delivery methodology driven by a **Project Knowledge Model (PKM)**.

The accessible publisher material establishes the following conceptual structure:

| Lal's published KDD | Meaning visible in reviewed source |
| --- | --- |
| Project knowledge separated from technical implementation | Requirements and solution knowledge form a structured knowledge concern; coding and testing realize it. |
| Project Knowledge Model | Project knowledge is decomposed into defined building blocks and relationships. |
| Knowledge as a primary companion artifact | Structured knowledge is delivered and maintained alongside software. |
| End-to-end delivery | PKM is extended across project delivery rather than limited to one phase. |
| Traceability | The model integrates project knowledge through explicit relationships. |
| Knowledge evolution | Contextual knowledge changes during delivery and must remain consistent. |
| Quality gates and metrics | Delivery quality is governed across the lifecycle. |
| Method independence | KDD can assist or integrate with existing lifecycle models and standards. |
| Automation and AI | The contents include tooling, automation, machine learning, and AI as enabling concerns. |

This creates both a **name collision** and a **substantive conceptual neighborhood** with this repository.

## 7. Comparison with This Repository

The comparison is bounded to concepts explicitly available in the reviewed material. “Not established” means the feature was not demonstrated by the accessible sources; it does not prove absence from the full publication.

| Dimension | Lal's 2018 KDD | This repository | Assessment |
| --- | --- | --- | --- |
| Knowledge as a primary project asset | Explicit | Foundational principle P1 | Strong overlap |
| Project knowledge distinct from implementation | Explicit | Explicit; code realizes accepted knowledge | Strong overlap |
| Structured knowledge model | PKM with building blocks and relationships | Artifact, domain, lifecycle, authority, and traceability models | Strong overlap, different decomposition |
| End-to-end delivery | Explicit | Product stimulus through operation and learning | Strong overlap |
| Traceability | Central PKM characteristic | Intent-to-evidence traceability | Strong overlap |
| Existing-method compatibility | Explicit | Technology- and framework-independent adoption | Strong overlap |
| Quality gates | Explicit | Semantic checkpoints, claims, evidence, baseline | Related, with a more explicit evidence model here |
| Business before architecture | Business/project knowledge is upstream of implementation | Normative P2–P4 ordering | Related; stronger constitutional formulation here |
| Contracts before code | Not established from reviewed accessible material | Normative P5 and dedicated process concern | Clear documented differentiator |
| Human authority over AI | Not established from reviewed accessible material | Normative P10 and Authority Model | Clear documented differentiator |
| Knowledge AI vs Execution AI | Not established | Explicit ChatGPT/Codex separation | Clear documented differentiator |
| AI Execution Task Contract | Not established | Dedicated governed contract | Clear documented differentiator |
| AI reviewer checks AI executor | Not established | Explicit controlled verification loop | Clear documented differentiator |
| Claim-first verification | Not established | Dedicated Verification and Evidence Model | Clear documented differentiator |
| Conformance profiles and declarations | Standards compatibility is discussed | Dedicated adoption and conformance model | Different governance structure |
| Origin | Published conceptual methodology | Generalized from KSeF_2 practice and Human–AI collaboration | Independent practical provenance is plausible but priority is not established |

## 8. Findings

### AUD-002-F01 — Exact prior named methodology

**Severity:** High  
**Status:** Confirmed

The exact name and abbreviation were published by Cambridge University Press in 2018 as a software-development methodology.

**Effect:** the repository cannot credibly claim authorship or exclusivity over the name, abbreviation, or basic named proposition.

### AUD-002-F02 — Material conceptual overlap

**Severity:** High  
**Status:** Confirmed

Both approaches place structured, evolving project knowledge before and alongside technical implementation and connect it across end-to-end delivery.

**Effect:** presenting this repository as an unrelated methodology with the same unqualified name would create avoidable confusion even if every sentence and model were independently authored.

### AUD-002-F03 — Meaningful Human–AI differentiation

**Severity:** Positive differentiator  
**Status:** Confirmed within current repository; not established in reviewed prior sources

The current methodology formalizes a controlled three-part pattern:

1. Human and ChatGPT establish what must be done.
2. ChatGPT produces a bounded task contract for Codex.
3. Codex implements and tests.
4. ChatGPT reviews the actual result and evidence.
5. The Human accepts, rejects, or redirects the work.

This separation creates two opportunities to catch execution error before human acceptance and prevents the execution AI from authorizing its own result.

**Effect:** this is a strong basis for a distinctive methodology identity, but not a basis for claiming the pre-existing name.

### AUD-002-F04 — Acronym ambiguity

**Severity:** Medium  
**Status:** Confirmed

KDD is globally associated with Knowledge Discovery and Data Mining through ACM SIGKDD.

**Effect:** the abbreviation alone has poor discoverability and creates ambiguity in search, academic references, event names, and tooling.

### AUD-002-F05 — Public provenance does not establish priority

**Severity:** Medium  
**Status:** Confirmed

The current repository says the methodology is extracted from KSeF_2. The reviewed public KSeF_2 history begins in July 2026, while exact and related uses date to 2010 and 2018.

**Effect:** KSeF_2 is valid empirical provenance for the present synthesis, but not evidence that this project originated the general term or earlier concepts.

### AUD-002-F06 — License and name solve different problems

**Severity:** Informational  
**Status:** Confirmed

A license governs permissions for the concrete text, diagrams, templates, code, and other repository expression. It does not make the term or underlying idea exclusive. Conversely, earlier use of the term does not prevent the authors from licensing their independently created repository content.

Under [GitHub's licensing guidance](https://docs.github.com/articles/licensing-a-repository), the absence of a license leaves default copyright restrictions in place. Article 1(2¹) of the [Polish Copyright Act](https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU19940240083/U/D19940083Lj.pdf) distinguishes protected expression from ideas, procedures, methods, and principles of operation.

**Effect:** a repository license is still necessary for an open methodology, but license selection should follow the identity and provenance decision.

### AUD-002-F07 — Legal and trademark clearance remains open

**Severity:** Open risk  
**Status:** Not assessed

This review did not search or interpret trademark registrations, publisher contracts, passing-off rules, or jurisdiction-specific naming rights.

**Effect:** no statement should be made that the name is legally available or unavailable. If the exact or a closely qualified name is retained for public promotion, specialist clearance is appropriate.

## 9. Required Repository Corrections Before Baseline

Regardless of the final name, the repository SHOULD:

1. add an explicit **Prior Use and Relationship** statement;
2. name Manoj Kumar Lal's 2018 publication as prior use of the exact methodology name;
3. state that this project does not claim to have coined “Knowledge Driven Development” or “KDD”;
4. distinguish independent provenance from priority;
5. describe the Human–Knowledge AI–Execution AI pattern as the project's principal differentiator;
6. avoid language such as “the KDD methodology” when it could imply a unique global referent;
7. retain this audit as evidence for the naming decision;
8. record the final decision in a human-accepted decision artifact before licensing and baseline release.

## 10. Identity Options

| Option | Description | Benefits | Risks | Audit recommendation |
| --- | --- | --- | --- | --- |
| **A — Distinctive new name** | Rename the methodology and preserve “knowledge-driven development” as a descriptive principle. | Lowest confusion; strongest discoverability and independent identity. | Migration work; a new name must be selected and checked. | **Recommended** |
| **B — Qualified identity** | Use a distinctive qualifier, for example a Human–AI or evidence-oriented designation, always with prior-use acknowledgment. | Preserves continuity with current vocabulary; makes differentiation visible. | May still be confused with Lal's KDD; acronym collision remains. | Acceptable after review |
| **C — Unqualified KDD** | Continue as “Knowledge-Driven Development (KDD)” with attribution and disclaimer. | No immediate rename. | Highest conceptual and branding confusion; weakest search identity; may require legal review and external communication. | Not recommended for public baseline |

No option is accepted by this audit. Naming is a human product and governance decision.

## 11. Recommended Decision Sequence

1. Krzysztof Olejnik reviews and accepts or corrects this factual landscape.
2. Define the methodology's irreducible distinctive proposition.
3. Choose Option A, B, or C.
4. If A or B is chosen, perform a targeted name and acronym landscape search.
5. If B or C is chosen, consider legal naming review and respectful communication with the earlier methodology author.
6. Record the decision, alternatives, rationale, and migration impact.
7. Update repository title, scope, README, document metadata, and links consistently.
8. Select the content license.
9. Perform another consistency audit before the first public baseline.

## 12. Audit Disposition

**Disposition:** the current unqualified methodology identity is not ready for public baseline.

This disposition does not reject the methodology content. It recognizes that the repository has developed a substantial Human–AI governance and verification synthesis while using a name already assigned to materially related prior work.

The correct next task is not license selection. It is a human decision about distinctive identity, made with transparent attribution and preserved evidence.


## 13. Post-Audit Human Decision

**Decision date:** 2026-07-18  
**Decision authority:** Krzysztof Olejnik — KGAID Methodology Owner  
**Decision:** Accept **Knowledge-Governed AI-Assisted Development (KGAID)** as the official methodology identity.

This decision implements Identity Option A: a distinctive new name. The earlier name **Knowledge-Driven Development (KDD)** remains in this audit as historical evidence and as the exact name of prior work reviewed here.

**Resolution status:**

- the naming blocker for an unqualified KDD public baseline is resolved by human decision;
- controlled migration of methodology documents to KGAID is authorized;
- the repository slug is not changed by this decision and requires separate migration review;
- license selection remains a separate open decision;
- broader trademark and naming clearance remains outside this audit.
