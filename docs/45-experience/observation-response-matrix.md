---
document_id: KGAID-EXP-002
title: EXP-3KSEF-001 Observation and Response Matrix

document_type: governance
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# Macierz obserwacji i reakcji EXP-3KSEF-001

Każda obserwacja ma dokładnie jeden główny wiersz. `Tak` wskazuje właściwy
strumień reakcji, a `Poza zakresem` oznacza działanie celowo niewykonywane w
tym zadaniu. Żaden wpis nie jest decyzją Human Authority.

| Observation | Experience Record | Local 3ksef fix | KGAID clarification | Change Proposal | Experiment | Deferred |
| --- | --- | --- | --- | --- | --- | --- |
| `OBS-001` | Tak — strength | Nie | Case study po decyzji authority | `KGAID-CP-004` | Drugie zastosowanie procesu | Tak — status projektu otwarty |
| `OBS-002` | Tak — strength | Nie | Minimalny zapis Human Decision | `KGAID-CP-002` | Revision-bound decision | Tak — authority |
| `OBS-003` | Tak — strength | Nie | Review contract | `KGAID-CP-002`, `KGAID-CP-004` | Zamrożone review runs | Tak — obowiązkowe review |
| `OBS-004` | Tak — strength/experiment | Nie | Rozdzielenie propozycji od normy | `KGAID-CP-004` | Curation w drugim projekcie | Tak — potwierdzenie |
| `OBS-005` | Tak — gap | Poza zakresem: immutable pin | Publication status i pin | `KGAID-CP-003` | Nie | Tak — publikacja `0.1.0` |
| `OBS-006` | Tak — ambiguity | Poza zakresem: rozdzielić lokalne osie | Dwie osie statusu | `KGAID-CP-001`, `KGAID-CP-002` | Pilot decyzji | Tak — znaczenie approval |
| `OBS-007` | Tak — application/ambiguity | Poza zakresem: naprawa Product Baseline | Zasada członkostwa | `KGAID-CP-003` | Validator baseline'u | Tak — accepted-only/exceptions |
| `OBS-008` | Tak — local problem | Poza zakresem: spójna decyzja AB-001 | Nie | `KGAID-CP-002` jako zapobieganie | Nie | Tak — stan AB-001 |
| `OBS-009` | Tak — gap | Poza zakresem: lokalny reapproval | Exact revision | `KGAID-CP-002` | Tool-neutral pilot | Tak — zakres decyzji |
| `OBS-010` | Tak — local problem | Poza zakresem: frontmatter/type CTR | Nie | Nie | Nie | Tak — lokalny typ |
| `OBS-011` | Tak — process gap | Poza zakresem: historyczny feedback | Lifecycle feedbacku | `KGAID-CP-004` | Proponowany lifecycle | Tak — closing authority |
| `OBS-012` | Tak — ambiguity | Poza zakresem: konsolidacja review | Granice i precedence review | `KGAID-CP-002`, `KGAID-CP-003` | Cross-layer checklist | Tak — taxonomy review |
| `OBS-013` | Tak — weakness | Poza zakresem: zachować runs | Review związane z rewizją | `KGAID-CP-002` | Append-only log | Tak — format |
| `OBS-014` | Tak — automation opportunity | Poza zakresem: canonical links | Minimalny model relacji | Nie | Generowane macierze | Tak — drugi projekt/tooling |
| `OBS-015` | Tak — adoption gap | Poza zakresem: wybrać profil | Jawny koszt i tailoring | Nie | Pomiar minimalnego profilu | Tak — profil 3ksef |
| `OBS-016` | Tak — experiment/hypothesis | Poza zakresem: ownership BPS | Mapping do Domain | `KGAID-CP-004` | BPS jako Domain Process View | Tak — drugi projekt |
| `OBS-017` | Tak — local problem | Poza zakresem: naprawa mapy/linków | Integralność manifestu | `KGAID-CP-003` | Broken-link validator | Tak — ownership mapy |
| `OBS-018` | Tak — strength | Nie | Evidence nie dowodzi kontroli | `KGAID-CP-004` | Representative increment | Tak — V2/V3 |
| `OBS-019` | Tak — application problem | Poza zakresem: lokalna klasyfikacja | Przykłady ADR positive/negative | Nie | Weryfikacja przykładu | Tak — zgoda redakcyjna |
| `OBS-020` | Tak — maturity limit | Nie | Ograniczyć claims | `KGAID-CP-004` | Delivery/Verification increment | Tak — brak evidence |
| `OBS-021` | Tak — methodology weakness | Nie | Normative precedence | `KGAID-CP-001` | Nie | Tak — słownik |
| `OBS-022` | Tak — rejected-for-now | Nie | Konsolidacja przed rozszerzeniem | `KGAID-CP-001` | Drugie użycie review | Tak — odrzucone obecnie |

## Kontrola kompletności

- zakres identyfikatorów: `OBS-001`–`OBS-022`;
- główne wiersze: 22;
- naprawy `3ksef`: wszystkie oznaczone poza zakresem;
- propozycje normatywne: wyłącznie jako draft CP;
- decyzje: pozostawione Human Authority.
