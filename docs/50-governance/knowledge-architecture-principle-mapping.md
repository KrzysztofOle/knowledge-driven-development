# KGAID Knowledge Architecture Principle Mapping

**Status:** Accepted  
**Version:** 0.1.0  
**Baseline:** KGAID-0.1.0  
**Classification:** Informational governance mapping  
**Maintainer:** Krzysztof Olejnik — KGAID Methodology Maintainer  
**Last reviewed:** 2026-07-19

This mapping makes explicit how the Knowledge Architecture realizes KGAID principles. It is a navigation and assurance record; the listed normative documents remain the authoritative sources.

| Knowledge Architecture rule | Principle basis | Normative source | Implemented by | Evidence / artifact |
| --- | --- | --- | --- | --- |
| KA-1 Knowledge is governed | P1, P6 | [Architecture overview](../10-knowledge-architecture/11-knowledge-architecture.md), [Authority Model](../10-knowledge-architecture/14-authority-model.md) | Process Model, Human–AI Collaboration | accepted artifact, authority assignment, decision record |
| KA-2 Artifact is not a file | P1, P6 | [Artifact Model](../10-knowledge-architecture/12-artifact-model.md) | Process Model, Delivery Increment Model | artifact ID, metadata, authoritative location |
| KA-3 Independent status dimensions | P1, P8 | Artifact Model; [Verification and Evidence Model](../30-quality/31-verification-and-evidence-model.md) | Delivery Increment Model | knowledge, delivery, and canonical verification status |
| KA-4 Human acceptance | P6, P10 | Authority Model; [Knowledge Lifecycle](../10-knowledge-architecture/13-knowledge-lifecycle.md) | Human–AI Collaboration, AI Task Contract | human acceptance decision and delegated authority |
| KA-5 Upstream before downstream | P2, P3, P7 | [Traceability Model](../10-knowledge-architecture/15-traceability-model.md) | Process Model, Delivery Increment Model | trace links and impact analysis |
| KA-6 Contracts before code | P4, P5 | Traceability Model; Artifact Model | Process Model, AI Task Contract | accepted contract and implementation links |
| KA-7 Code is realization | P1, P4 | Architecture overview; Artifact Model | Delivery Increment Model | implementation status and linked accepted knowledge |
| KA-8 Evidence is bounded | P8, P9 | Verification and Evidence Model | Delivery Increment Model, Adoption Model | evidence record, declared boundary, limitations |
| KA-9 Learning re-enters lifecycle | P11, P12 | Knowledge Lifecycle | Process Model, Adoption Model | operation observation and change proposal |
| KA-10 History is preserved | P6, P12 | Traceability Model; Artifact Model | Governance and Release Model | supersession links, baseline manifest, audit record |

Evidence MUST be evaluated against the cited normative source, not merely the existence of this mapping.
