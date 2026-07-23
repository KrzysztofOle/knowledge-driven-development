---
document_id: EXP-3KSEF-001
title: 3ksef KGAID Experience Record

document_type: knowledge
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# EXP-3KSEF-001 — doświadczenie z pilota 3ksef

## Stan rekordu

| Pole | Wartość |
| --- | --- |
| Experience ID | `EXP-3KSEF-001` |
| Projekt źródłowy | `3ksef` |
| Repozytorium | `KrzysztofOle/3ksef` |
| Branch analizy | `agent/project-structure` |
| Niezmienny punkt projektu | `133817601f597a8b73902c411f3c547e82e54f91` |
| Metodyka | `KrzysztofOle/kgaid-methodology` |
| Branch metodyki | `main` |
| Niezmienny punkt metodyki | `dcc9976ba523120e319cfa1f5fb4460a74a38e99` |
| Deklarowana wersja | `KGAID-0.1.0`, `prepared-unpublished` |
| Data analizy | `2026-07-23` |
| Status projektu | `pilot`; brak decyzji o statusie `candidate` lub `reference` |
| Stan walidacji | `single-project` |
| Potwierdzenie w innym projekcie | Nie; wymagane dla wskazanych hipotez |
| Wynik rekordu | Nieustalony; `accepted`, `rejected`, `deferred` ani `experimental` nie zostało nadane przez Human Authority |

KGAID w bieżącym repozytorium nadal wskazuje commit `dcc9976…`; w chwili
tworzenia tego rekordu nie występują późniejsze zmiany względem punktu
odniesienia raportu.

## Materiał źródłowy, zakres i ograniczenia

Źródłem jest
[KGAID Experience Review — etap 1](evidence/kgaid-experience-review-etap-1.md).
Raport pozostaje evidence i zachowuje pełny aneks 41 lokatorów. Ten rekord
redukuje powtórzenia: utrwala klasyfikację, wynik reakcji i powiązania z CP,
a szczegółową rekonstrukcję pozostawia raportowi.

Etap 1 objął 79 commitów historii `3ksef`, 180 plików Markdown, metadane 138
zarządzanych artefaktów, pogłębiony przegląd 38 dokumentów projektu i 23 plików
KGAID. Analizowano Governance, Product, Domain, Requirements, Architecture,
ADR, Contracts, Knowledge, Delivery, Verification, Operations, collaboration,
traceability, approval, baselines, security i koszt dokumentacji.

Ograniczenia:

- brak implementacji, test evidence i Operations dla representative increment;
- brak oceny prawnej, podatkowej i rzeczywistej poprawności produktu;
- brak rozmów oraz decyzji niezapisanych w repozytorium;
- autorstwo kroków poznawczych wywnioskowano z artefaktów;
- jeden projekt nie dowodzi uniwersalności lokalnych rozwiązań.

## Katalog obserwacji

Klasyfikacja główna używa
[modelu Experience Record](../../experience-record-model.md#klasyfikacja-obserwacji).
Wartości wpływu, pewności, zakresu i rekomendacje zachowują sens raportu.
Dla każdej obserwacji `OBS-001`–`OBS-022` pole cross-project confirmation ma
wartość `none`; żadnej nie potwierdzono jeszcze w innym projekcie.

| ID | Skrót obserwacji | Klasyfikacja | Wpływ | Pewność | Zakres | Rekomendacja | Evidence | CP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `OBS-001` | Zależności semantyczne działają bez wymuszenia waterfall. | methodology-strength | high | high | project + methodology validation | Użyć historii jako case study dopiero po decyzji o statusie 3ksef. | `EV-015`, `EV-017`, `EV-021`, `EV-033` | `KGAID-CP-004` |
| `OBS-002` | Model Human–ChatGPT–Codex i separacja publikacji działają. | methodology-strength | high | high | project + methodology validation | Zachować model i wiązać Human Decision z dokładną rewizją. | `EV-001`, `EV-002`, `EV-031`, `EV-034` | `KGAID-CP-002` |
| `OBS-003` | Review wykrywają błędy i uruchamiają rework. | methodology-strength | high | high | project + methodology validation | Zachować review oparte na pytaniach/evidence i zamrażać runs. | `EV-008`, `EV-009`, `EV-019`, `EV-025`, `EV-035` | `KGAID-CP-002`, `KGAID-CP-004` |
| `OBS-004` | Curation jest udanym eksperymentem transferu wiedzy. | experiment; methodology-strength | medium | high | cross-repository | Utrzymać jako propozycję do sprawdzenia w drugim projekcie. | `EV-012`, `EV-026`, `EV-040` | `KGAID-CP-004` |
| `OBS-005` | 3ksef nie przypięto do niezmiennego baseline'u KGAID. | methodology-gap-or-ambiguity | high | high | cross-repository | Do publikacji pinować SHA i jawnie oznaczać baseline eksperymentalny. | `EV-004`, `EV-027`, `EV-036`, `EV-037`, `EV-038` | `KGAID-CP-003` |
| `OBS-006` | Approval jest utożsamiany z akceptacją wiedzy. | methodology-application-problem; methodology-gap-or-ambiguity | high | high | project + methodology | Rozdzielić approval rewizji od decyzji o statusie wiedzy. | `EV-005`, `EV-014`, `EV-029`, `EV-030`, `EV-039` | `KGAID-CP-001`, `KGAID-CP-002` |
| `OBS-007` | Product Baseline autoryzuje niezaakceptowane elementy. | methodology-application-problem; methodology-gap-or-ambiguity | high | high | project + methodology | Accepted-only albo jawne wyjątki per item po decyzji authority. | `EV-006`, `EV-007`, `EV-029`, `EV-030` | `KGAID-CP-003` |
| `OBS-008` | Architecture Baseline ma sprzeczny zapis decyzji. | local-project-problem | high | high | project | W projekcie wykonać jedną decyzję exact revision i ujednolicić zapis. | `EV-020` | `KGAID-CP-002` |
| `OBS-009` | Approval nie jest silnie związany z dokładną rewizją. | methodology-gap-or-ambiguity | high | high | methodology + tooling | Formalnie opisać revision-bound decision, reapproval i historię. | `EV-020`, `EV-030`, `EV-039`, `EV-041` | `KGAID-CP-002` |
| `OBS-010` | Kontrakty pozostają poza lokalnym governance. | local-project-problem | high | high | project | Lokalnie włączyć CTR do frontmatter, słownika i lifecycle. | `EV-005`, `EV-022`, `EV-023`, `EV-024` | — |
| `OBS-011` | Feedback nie ma skutecznego lifecycle. | local-project-problem; methodology-gap-or-ambiguity | medium | high | cross-repository | Dodać status, `resolved_by`, `verified_at_ref` i closing authority. | `EV-003`, `EV-012`, `EV-040` | `KGAID-CP-004` |
| `OBS-012` | Rodzaje review nakładają się i dają sprzeczne wyniki. | methodology-gap-or-ambiguity | high | high | project + methodology | Zdefiniować review contract, precedence i relację z baseline'em. | `EV-007`–`EV-011` | `KGAID-CP-002`, `KGAID-CP-003` |
| `OBS-013` | Jedno review mutowano od Not Ready do Ready. | methodology-application-problem | medium | high | project + methodology | Freeze runs albo append-only log z subject SHA. | `EV-019` | `KGAID-CP-002` |
| `OBS-014` | Traceability jest użyteczne, ręczne i powielone. | methodology-application-problem | medium | high | project + methodology tooling | Ustalić minimalne canonical links i generować projekcje. | `EV-021`, `EV-024`, `EV-025`, `EV-035` | — |
| `OBS-015` | Rygor jest wysoki, a profil adoption niewybrany. | methodology-application-problem | medium | high | project | Lokalnie wybrać profil i tailoring; zmierzyć koszt. | `EV-004`, `EV-028`, `EV-036` | — |
| `OBS-016` | BPS ma wartość, ale nowy typ nie jest potwierdzony. | experiment; cross-project-hypothesis | medium | medium | methodology candidate | Mapować Product → Domain process → BR/REQ i sprawdzić drugi projekt. | `EV-012`, `EV-013`, `EV-029`, `EV-032` | `KGAID-CP-004` |
| `OBS-017` | Migracja Domain Map naruszyła single source of truth. | local-project-problem | medium | high | project | Ustalić owner, naprawić linki i walidować integralność baseline'u. | `EV-006`, `EV-018`, `EV-032` | `KGAID-CP-003` |
| `OBS-018` | Ryzyka security/compliance wykryto przed kodem. | methodology-strength | high | high dla wykrycia; low dla skuteczności kontroli | project + methodology validation | Zachować traceability do evidence i sprawdzić w PI-1. | `EV-008`, `EV-017`, `EV-021`, `EV-035` | `KGAID-CP-004` |
| `OBS-019` | Klasyfikacja ADR wymaga lepszych przykładów. | methodology-application-problem | medium | medium | project + methodology examples | Dodać przykłady positive/negative bez nowego artefaktu. | `EV-019`, `EV-029` | — |
| `OBS-020` | Brak evidence dla Delivery, Verification i Operations. | cross-project-hypothesis | medium | high | project + methodology evidence | Nie zgłaszać end-to-end claims; wykonać representative increment. | `EV-027`, `EV-035`, `EV-036` | `KGAID-CP-004` |
| `OBS-021` | KGAID ma wewnętrznie niespójny słownik statusów. | methodology-gap-or-ambiguity | high | high | methodology | Ujednolicić słownik lub jawnie rozdzielić osie przed publikacją. | `EV-029`, `EV-030`, `EV-039`, `EV-041` | `KGAID-CP-001` |
| `OBS-022` | Brak dowodu dla mnożenia statusów i review. | rejected-for-now | low | medium | methodology | Najpierw konsolidować; nowe typy dopiero po drugim przypadku. | `EV-029`, `EV-030`, `EV-039` | `KGAID-CP-001` |

Rozkład wpływu: 12 `high`, 9 `medium`, 1 `low`, 0 `critical`.

## Katalog dowodów

Lokatory poniżej wskazują repozytorium, commit, ścieżkę i sekcję albo
sprawdzalne twierdzenie. Pełne adresy źródeł są w aneksie raportu.

| Evidence | Niezmienny lokator | Sekcja lub twierdzenie |
| --- | --- | --- |
| `EV-001` | `3ksef@1338176:AGENTS.md` | Podział obowiązków; zgoda na publikację |
| `EV-002` | `3ksef@1338176:instrukcja_ChatGPT.md` | Cykl Human–ChatGPT–Codex |
| `EV-003` | `3ksef@1338176:docs/AGENTS.md` | Jedno źródło prawdy; feedback do KGAID |
| `EV-004` | `3ksef@1338176:docs/00-governance/kgaid-adoption.md` | Baseline i zakres adoption |
| `EV-005` | `3ksef@1338176:docs/00-governance/documentation-governance.md` | Status, approval i typy |
| `EV-006` | `3ksef@1338176:docs/00-governance/product-baseline-1.0.md` | Baseline members; Domain Map |
| `EV-007` | `3ksef@1338176:docs/00-governance/architecture-readiness-review-003.md` | Autorytet baseline'u |
| `EV-008` | `3ksef@1338176:docs/00-governance/architecture-readiness-review.md` | Pierwszy wynik readiness |
| `EV-009` | `3ksef@1338176:docs/10-product/architecture-readiness-review.md` | Coverage, status i traceability |
| `EV-010` | `3ksef@1338176:docs/00-governance/arr-review-differences-analysis.md` | 14 różnic review |
| `EV-011` | `3ksef@1338176:docs/10-product/product-review.md` | Wynik Product Review |
| `EV-012` | `3ksef@1338176:docs/00-governance/kgaid-feedback.md` | GAP-001–004; EP-001–006 |
| `EV-013` | `3ksef@1338176:docs/10-product/business-processes/business-process-model.md` | BPS jako rozszerzenie |
| `EV-014` | `3ksef@1338176:docs/10-product/business-processes/processes/BP-001-wystawienie-faktury-sprzedazy.md` | `captured` i `approved` |
| `EV-015` | `3ksef@1338176:docs/20-domain/business-rules/business-rule-model.md` | BR a REQ |
| `EV-016` | `3ksef@1338176:docs/30-requirements/requirement-model.md` | Lifecycle wymagań |
| `EV-017` | `3ksef@1338176:docs/20-domain/domain-model.md` | Model i lifecycle faktury |
| `EV-018` | `3ksef@1338176:docs/20-domain/README.md` | Usunięta Domain Map |
| `EV-019` | `3ksef@1338176:docs/00-governance/architecture-review-pi-1.md` | Ready history; ADR |
| `EV-020` | `3ksef@1338176:docs/40-architecture/baselines/architecture-baseline-1.0.md` | Frontmatter, pending i Human Decision |
| `EV-021` | `3ksef@1338176:docs/40-architecture/views/architecture-specification-pi1.md` | Upstream traceability |
| `EV-022` | `3ksef@1338176:docs/50-contracts/contract-catalog.md` | Stan AB-001 i katalog CTR |
| `EV-023` | `3ksef@1338176:docs/50-contracts/templates/business-contract-template.md` | Fenced YAML; document type |
| `EV-024` | `3ksef@1338176:docs/50-contracts/business-contracts/CTR-001-create-draft-invoice.md` | Traceable contract |
| `EV-025` | `3ksef@1338176:docs/50-contracts/reviews/business-contracts-coverage-review-pi1.md` | Coverage 4 z 11 |
| `EV-026` | `3ksef@1338176:docs/90-knowledge/knowledge-staging/AGENTS.md` | Zachowanie źródeł |
| `EV-027` | `kgaid-methodology@dcc9976:README.md` | Status i prepared baseline |
| `EV-028` | `kgaid-methodology@dcc9976:docs/00-foundations/02-principles.md` | Knowledge-first; proportional rigor |
| `EV-029` | `kgaid-methodology@dcc9976:docs/10-knowledge-architecture/12-artifact-model.md` | Osie statusu; baseline |
| `EV-030` | `kgaid-methodology@dcc9976:docs/10-knowledge-architecture/13-knowledge-lifecycle.md` | Canonical lifecycle; Human decision |
| `EV-031` | `kgaid-methodology@dcc9976:docs/10-knowledge-architecture/14-authority-model.md` | Role i ograniczenia AI |
| `EV-032` | `kgaid-methodology@dcc9976:docs/10-knowledge-architecture/16-knowledge-domains.md` | Business processes w Domain |
| `EV-033` | `kgaid-methodology@dcc9976:docs/20-methodology/21-process-model.md` | PM1–PM9 bez waterfall |
| `EV-034` | `kgaid-methodology@dcc9976:docs/20-methodology/22-human-ai-collaboration.md` | Delegation, review, decision |
| `EV-035` | `kgaid-methodology@dcc9976:docs/30-quality/31-verification-and-evidence-model.md` | Claims i V0–V3 |
| `EV-036` | `kgaid-methodology@dcc9976:docs/40-adoption/41-adoption-and-conformance-model.md` | Pin, profil, tailoring, increment |
| `EV-037` | `kgaid-methodology@dcc9976:docs/50-governance/governance-and-release-model.md` | Przygotowanie a publikacja |
| `EV-038` | `kgaid-methodology@dcc9976:docs/50-governance/baselines/KGAID-0.1.0.yaml` | `prepared-unpublished` |
| `EV-039` | `kgaid-methodology@dcc9976:docs/50-governance/metadata-profile.md` | Status i approval vocabulary |
| `EV-040` | `kgaid-methodology@dcc9976:docs/20-methodology/25-knowledge-base-curation-workflow.md` | Proposed curation workflow |
| `EV-041` | `kgaid-methodology@dcc9976:docs/60-approval/README.md` | Informacyjny Approval Center |

Skróty SHA w tabeli są czytelną projekcją. Autorytatywne pełne wartości znajdują
się w tabeli „Stan rekordu” oraz w raporcie evidence.

## Strumienie reakcji

### Mocne strony

`OBS-001`, `OBS-002`, `OBS-003`, `OBS-004` i `OBS-018` potwierdzają wartość
zależności semantycznych, jawnej authority, review, transferu wiedzy oraz
wczesnego wykrywania ryzyka. Nie dowodzą skuteczności end-to-end.

### Lokalne problemy projektu

`OBS-008`, `OBS-010` i `OBS-017` są głównie lokalne. Lokalne działania wynikają
także z `OBS-005`–`OBS-007`, `OBS-011`–`OBS-015` i `OBS-019`. Naprawa `3ksef`
jest poza zakresem tego rekordu.

### Kandydaci zmian KGAID

- `KGAID-CP-001` — status vocabulary: `OBS-006`, `OBS-021`, `OBS-022`;
- `KGAID-CP-002` — revision-bound decision: `OBS-002`, `OBS-003`, `OBS-006`,
  `OBS-008`, `OBS-009`, `OBS-012`, `OBS-013`;
- `KGAID-CP-003` — baseline manifest: `OBS-005`, `OBS-007`, `OBS-012`,
  `OBS-017`;
- `KGAID-CP-004` — evidence-based evolution: `OBS-001`, `OBS-003`, `OBS-004`,
  `OBS-011`, `OBS-016`, `OBS-018`, `OBS-020`.

### Hipotezy i eksperymenty

- BPS jako osobny typ, taxonomy review, minimalny profil i niezależny reviewer
  wymagają innego projektu;
- curation, generowane traceability, validator baseline'u, revision-bound
  decision i cross-layer checklist pozostają eksperymentami;
- mnożenie statusów, obowiązkowych review i reguła jeden moduł–jeden kontrakt
  są odrzucone na obecnym etapie, nie usunięte z historii.

## Human Authority i outcome

Żadna decyzja nie została podjęta. Otwarte pytania są zebrane w
[rejestrze decyzji](../../../50-governance/decisions/open-human-authority-decisions-3ksef-experience.md).
Do czasu decyzji:

- rekord i cztery CP pozostają `draft`;
- `3ksef` pozostaje `pilot`;
- cross-project confirmation pozostaje puste;
- nie zmienia się baseline, status wiedzy ani approval w żadnym repozytorium;
- outcome każdej obserwacji i całego rekordu pozostaje nieprzypisany; etykiety
  `experiment` i `cross-project-hypothesis` są klasyfikacją, a nie decyzją.
