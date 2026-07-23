---
document_id: KGAID-CP-002
title: Change Proposal Revision-Bound Human Decision

document_type: governance
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# CP-002 — Revision-bound Human Decision

## Status propozycji

Projekt do decyzji Human Authority. Definiuje wymagane znaczenie, nie wybiera
narzędzia i nie ustanawia Approval Center obowiązkową częścią KGAID.

## Problem i evidence

Źródłowe obserwacje: `OBS-002`, `OBS-003`, `OBS-006`, `OBS-008`, `OBS-009`,
`OBS-012` i `OBS-013`. Najważniejszy problem: zapis `approved_by` i daty bez
silnego `subject_ref` nie dowodzi, jakiej treści dotyczyła decyzja, a zmienny
review może utracić samodzielny ślad wcześniejszego wyniku.

Dowody `EV-001`, `EV-002`, `EV-007`–`EV-011`, `EV-019`, `EV-020`, `EV-030`,
`EV-039`, `EV-041` są opisane w
[EXP-3KSEF-001](../../45-experience/reference-projects/3ksef/EXP-3KSEF-001.md#katalog-dowodów).

## Proponowany model znaczeniowy

Human Decision Record (HDR) wiąże decyzję z dokładnie identyfikowanym
przedmiotem. Minimalny model do rozważenia:

```yaml
decision_id: HD-NNN
subject_id: stable-artifact-or-baseline-id
subject_ref:
  repository: owner/repository
  commit: full-commit-sha
  path: path/to/subject
  content_hash: sha256:optional-or-required-by-selected-variant
decision_scope: exact claims, sections, members or risks
approver: human-identity
authority_basis: role-or-delegation
decided_at: YYYY-MM-DDThh:mm:ss+offset
rationale: concise grounds and considered evidence
outcome: accepted | rejected | deferred | approved-for-review-only
conditions: []
supersedes_decision: null
related_review: []
related_evidence: []
```

Identyfikacja może używać pełnego commita i ścieżki, content hash albo
równoważnego niezmiennego identyfikatora. Wybrany wariant musi wykrywać zmianę
semantyczną i umożliwiać odtworzenie dokładnej treści.

## Zakres decyzji

`decision_scope` zapobiega rozszerzaniu decyzji poza intencję approvera. Może
obejmować cały dokument, wskazane sekcje, członkostwo baseline'u, wynik review,
określone wyjątki albo claim. Decyzja o zatwierdzeniu rewizji do review nie
oznacza automatycznie:

- `status: accepted`;
- akceptacji ryzyka;
- przyjęcia wszystkich zależności;
- członkostwa w baseline;
- publikacji, release ani conformance.

## Zmiana semantyczna i ponowne zatwierdzenie

Po zmianie treści wpływającej na znaczenie, zakres, obowiązek, ryzyko,
zależność, evidence lub warunek:

1. wcześniejsza decyzja pozostaje w historii dla starego `subject_ref`;
2. bieżąca rewizja nie dziedziczy jej automatycznie;
3. impact review ustala wymagany zakres ponownej decyzji;
4. nowa decyzja wskazuje poprzednią, jeżeli ją zastępuje;
5. projekcja `approval_status` wraca do stanu bez bieżącego approval.

Zmiany wyłącznie prezentacyjne mogą zachować decyzję tylko wtedy, gdy reguła
klasyfikacji jest jawna i audytowalna. Granica semantic/non-semantic pozostaje
do decyzji.

## Supersession i historia

Decision ID jest niezmienny. Korekta wyniku tworzy nowy record z
`supersedes_decision`, zamiast przepisywać poprzedni. Historia pokazuje:

- stary i nowy subject ref;
- actor i authority basis;
- datę, rationale i outcome;
- przyczynę reapproval lub supersession;
- zależne baseline'y, review i release'y.

## Relacja z `approval_status`

Rozważane warianty:

### Wariant A — `approval_status` jako projekcja HDR

Pole jest wygodnym indeksem `draft/pending/approved`, a HDR pozostaje źródłem
prawdy. `approved` jest poprawne tylko dla dokładnie zgodnego `subject_ref`.

### Wariant B — approval techniczny niezależny od decyzji lifecycle

`approval_status` mówi tylko o obsłudze kolejki. Osobny HDR nadaje outcome i
zmienia status wiedzy przez kontrolowane działanie.

### Wariant C — brak obowiązkowego pola

Projekt może przechowywać sam HDR, podpisany commit, wpis issue lub rekord
workflow, jeśli zachowuje wymagane znaczenie i odtwarzalność.

Żaden wariant nie może mapować `approved` na `accepted` bez jawnej decyzji
lifecycle.

## Stosowanie bez Approval Center

Model jest technology-neutral. Zgodną realizacją może być:

- plik decision record w repozytorium;
- podpisany lub chroniony commit/tag z powiązanym rationale;
- issue albo pull request z niezmiennym subject ref;
- system workflow eksportujący trwały record;
- ręczny rejestr podpisany przez właściwą authority.

Approval Center może być jedną implementacją, nie normą ani wymaganą
zależnością.

## Review jako przedmiot decyzji

Każdy review run powinien wskazywać subject ref, scope, questions, evidence,
reviewer, wynik i ważność. Kolejny run nie nadpisuje poprzedniego. Decyzja
Human Authority wskazuje konkretny run i nie dziedziczy automatycznie wyniku po
zmianie subject.

## Compatibility i migracja

- istniejące `approved_by/approved_at` bez subject ref pozostają historyczne,
  ale ich ograniczenie jest jawne;
- migracja nie może dopisać content hash jako rzekomego faktu, jeżeli dokładna
  rewizja nie jest znana;
- projekty mogą wprowadzić HDR stopniowo od nowych decyzji i nowych baseline'ów;
- narzędzia powinny wykrywać mismatch między bieżącą treścią i subject ref;
- wersja i wpływ SemVer wymagają osobnej oceny po wyborze wariantu.

## Pytania do Human Authority

1. Czy dokładna rewizja jest obowiązkowa dla każdej consequential decision?
2. Czy wystarcza commit + path, czy wymagany jest content hash?
3. Jak odróżnić approval kolejki od akceptacji wiedzy?
4. Które zmiany wymagają ponownego approval?
5. Czy decyzje mają być osobnymi append-only records?
6. Jaki minimalny `authority_basis` jest wymagany?
7. Jak długo zachowywać i jak unieważniać decision history?
8. Czy pilotować model bez przesądzania o Approval Center?

Wszystkie pytania i wybór wariantu pozostają otwarte.
