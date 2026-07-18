# KGAID Normative Document Metadata Profile

**Status:** Accepted  
**Version:** 0.1.0  
**Baseline:** KGAID-0.1.0  
**Classification:** Informational governance control  
**Maintainer:** Krzysztof Olejnik — KGAID Methodology Maintainer  
**Last reviewed:** 2026-07-19

## Required front matter

Every normative KGAID document MUST begin with YAML front matter containing exactly one value for each required field below. The profile makes document identity, authority, and baseline membership machine-checkable.

| Field | Requirement |
| --- | --- |
| `document_id` | Stable identifier from the baseline manifest. |
| `title` | Canonical document title. |
| `status` | `Accepted` for a baseline member. |
| `version` | Semantic document version. |
| `baseline` | Baseline identifier, or `null` before baselining. |
| `normative` | Boolean indicating normative or informational status. |
| `maintainer` | Durable methodology maintainer role and person. |
| `last_reviewed` | ISO 8601 review date. |
| `dependencies` | IDs of directly depended-on normative documents. |
| `supersedes` | Replaced document/version, or `null`. |
| `superseded_by` | Replacement document/version, or `null`. |
| `verification_status` | Status from the canonical verification taxonomy. |
| `change_control` | `docs/50-governance/governance-and-release-model.md`. |

`document_id` MUST remain stable across renames. The front matter MAY contain additional fields, but they MUST NOT redefine the profile fields.

## Canonical verification taxonomy

The Verification and Evidence Model is the source of truth for verification status. The permitted values are `not-planned`, `planned`, `in-progress`, `partially-supported`, `failed`, `verified`, `verified-with-limitations`, `inconclusive`, `invalidated`, and `expired`.

An evidence result (`supports`, `contradicts`, `partial`, `inconclusive`, `not-executed`, or `invalid`) is not a verification status. Statuses in other models MUST use these canonical values or explicitly map a local label to one of them.

## Normative language

KGAID uses the keywords **MUST**, **SHOULD**, and **MAY** as defined in [KGAID Principles](../00-foundations/02-principles.md#2-normative-language): MUST denotes a requirement, SHOULD a strong recommendation with explicit rationale for departure, and MAY a permitted option. Their negative forms have the corresponding meaning. Lower-case occurrences are avoided in normative rules so the meaning is unambiguous.
