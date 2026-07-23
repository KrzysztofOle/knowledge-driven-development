---
document_id: KGAID-EXP-003
title: KGAID Methodology Feedback Lifecycle Proposal

document_type: governance
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# Propozycja lifecycle feedbacku metodologicznego

## Status

Model jest roboczą propozycją wynikającą z `OBS-011`. Nie zmienia historycznych
wpisów feedbacku w `3ksef` ani zasad KGAID.

## Proponowane stany

| Stan | Znaczenie |
| --- | --- |
| `open` | Feedback zapisany, jeszcze nieoceniony. |
| `under-review` | Ustalane są evidence, owner, wpływ i właściwa reakcja. |
| `confirmed` | Problem lub szansa zostały potwierdzone dla wskazanej rewizji. |
| `rejected` | Evidence nie wspiera feedbacku albo propozycja jest sprzeczna z zakresem; rationale jest obowiązkowe. |
| `resolved` | Zatwierdzona reakcja została wdrożona i zweryfikowana na dokładnej rewizji. |
| `superseded` | Nowszy wpis przejął zakres; wskazuje jego identyfikator. |
| `deferred` | Ocena lub reakcja jest odłożona z jawnym warunkiem powrotu. |

Przejście do `resolved` nie wynika automatycznie z commita. Wymaga wskazania
reakcji, `resolved_by`, `verified_at_ref` i decyzji authority właściwej dla
zakresu. `rejected` zachowuje evidence i rationale.

## Minimalny rekord

```yaml
feedback_id: FB-NNN
status: open
title: Concise feedback title
reported_by: actor
reported_at: YYYY-MM-DD
source_project: project-id
source_ref: immutable-ref
evidence_refs: []
experience_record: EXP-NNN
change_proposal: null
authority_decision: null
resolved_by: null
verified_at_ref: null
supersedes: null
superseded_by: null
reopen_count: 0
next_review_condition: null
history: []
```

`resolved_by` identyfikuje zmianę, decyzję lub działanie rozwiązujące problem,
nie osobę klikającą status. `verified_at_ref` wskazuje dokładną rewizję KGAID,
projektu albo obu, na której sprawdzono rezultat.

## Przejścia

```text
open -> under-review
under-review -> confirmed | rejected | deferred
confirmed -> resolved | deferred | superseded
deferred -> under-review
resolved | rejected -> open
open | under-review | confirmed | deferred -> superseded
```

Ponowne otwarcie wymaga nowego evidence, zmiany kontekstu albo wykazania, że
rozwiązanie nie działa. Historia zachowuje poprzedni stan, decyzję, czas,
authority i dokładne referencje.

## Authority

- owner projektu może potwierdzić i rozwiązać problem wyłącznie lokalny;
- właściciel metodyki może potwierdzić wpływ na KGAID i wskazać wdrożoną
  zmianę;
- zamknięcie feedbacku obejmującego oba repozytoria wymaga uzgodnionego modelu
  authority; ta decyzja pozostaje otwarta;
- AI może proponować przejście i sprawdzać evidence, lecz nie podejmuje
  decyzji authority.

## Weryfikacja

Rekord `resolved` powinien dać się odtworzyć bez dostępu do rozmów:

1. źródłowy feedback i immutable source ref;
2. powiązany Experience Record;
3. CP lub uzasadnienie braku CP;
4. decyzja authority;
5. zmiana oznaczona w `resolved_by`;
6. wynik sprawdzenia na `verified_at_ref`;
7. warunki ponownego otwarcia.
