---
document_id: KGAID-CP-004
title: Change Proposal Experience Record and Evidence-Based Evolution

document_type: governance
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# CP-004 — Experience Record and Evidence-Based Evolution

## Status propozycji

Projekt formalnego modelu uczenia się KGAID. Nie ustanawia
[Experience Record Model](../../45-experience/experience-record-model.md) normą,
nie uznaje `3ksef` za oficjalny projekt referencyjny i nie akceptuje żadnej
obserwacji jako zmiany metodologii.

## Problem i evidence

Źródłowe obserwacje:

- `OBS-001` i `OBS-003` — process i review mają evidence wartości;
- `OBS-004` — praktyka curation przeszła szybko z projektu do propozycji KGAID;
- `OBS-011` — feedback bez lifecycle pozostaje nieaktualny;
- `OBS-016` — wartościowy BPS może być lokalną reprezentacją, nie nowym typem;
- `OBS-018` — wykrycie ryzyka nie dowodzi skuteczności kontroli;
- `OBS-020` — brak evidence end-to-end ogranicza claims.

Dowody `EV-001`–`EV-003`, `EV-008`–`EV-013`, `EV-019`, `EV-025`–`EV-036` i
`EV-040` są dostępne przez
[EXP-3KSEF-001](../../45-experience/reference-projects/3ksef/EXP-3KSEF-001.md#katalog-dowodów).

## Proponowany przepływ

```text
evidence
  -> observation
  -> hypothesis
  -> bounded experiment
  -> confirmation or contradiction
  -> change proposal
  -> normative decision
  -> baseline and separate publication decision
  -> operational evidence and learning
```

Przejście nie jest automatyczne. Każdy krok zachowuje swój owner, authority,
referencję do wejścia, ograniczenia i wynik.

## Jednostki

### Observation

Sprawdzalny wzorzec wyprowadzony z faktów. Ma impact, confidence, scope,
evidence i klasyfikację. Obserwacja nie jest regułą.

### Hypothesis

Twierdzenie, które wyjaśnia obserwację albo przewiduje wartość zmiany. Zawiera
warunek falsyfikacji, oczekiwany kontekst i wskazanie, czy potrzebny jest drugi
projekt.

### Experiment

Ograniczone użycie praktyki bez nadawania jej statusu normatywnego. Zapisuje
baseline wejściowy, zakres, ryzyko, owner, oczekiwany sygnał, evidence plan i
warunek zakończenia.

### Confirmation

Wynik wskazujący dokładny projekt, ref i evidence. Potwierdzenie może być
lokalne albo cross-project. Brak sprzeczności nie jest sam potwierdzeniem.

### Change Proposal

Opisuje problem, evidence, warianty, compatibility, migrację, wpływ normatywny
i pytania. Status `draft` nie zmienia normy.

### Normative decision

Human Authority przyjmuje, odrzuca albo odracza CP dla dokładnej rewizji.
Akceptacja uruchamia zwykłą zmianę dokumentów i review; nie publikuje sama
baseline'u.

## Minimalne wymagania dowodowe

Każdy claim prowadzący do CP wskazuje:

1. co najmniej jeden Experience Record;
2. repozytorium, immutable ref, ścieżkę/ID i sekcję dowodu;
3. rozdzielenie faktu, interpretacji i rekomendacji;
4. zakres analizy i nieweryfikowane warstwy;
5. impact i confidence;
6. alternative explanation albo lokalny problem;
7. status cross-project confirmation;
8. ryzyko przedwczesnego uogólnienia.

Dowód może być przechowywany jako raport lub niezmienny eksport w KGAID.
Repozytorium projektu pozostaje zewnętrznym źródłem; KGAID nie tworzy
submodułu, subtree, vendored copy ani runtime dependency.

## Zasady dla jednego projektu

Jedno użycie może wystarczyć do:

- zapisania strength i ograniczenia;
- naprawy konfliktu wewnątrz istniejących dokumentów KGAID;
- clarification, które nie zmienia obowiązku;
- rozpoczęcia CP i eksperymentu;
- odrzucenia claim, którego evidence jawnie nie wspiera.

Nie wystarcza domyślnie do:

- ustanowienia nowego obowiązkowego artifact type;
- wymagania osobnego review w każdym projekcie;
- uznania narzędzia za obowiązkowe;
- stwierdzenia skuteczności end-to-end bez Delivery/Verification/Operations;
- nadania projektowi statusu `reference`.

## Kiedy wymagany jest drugi projekt

Drugi projekt jest wymagany, gdy propozycja:

- uogólnia lokalną strukturę artefaktów;
- zwiększa minimalny koszt adoption;
- ustanawia obowiązkową rolę, review albo narzędzie;
- zależy od domeny, skali lub ryzyka pierwszego projektu;
- ma być przedstawiona jako dowód powtarzalnej skuteczności.

Human Authority może przyjąć zmianę wcześniej tylko przez jawną decyzję
opisującą ograniczone evidence, konsekwencje i plan rewalidacji.

## Odrzucanie, odraczanie i supersession

- `rejected` zachowuje evidence, rationale i warunki ewentualnego reopen;
- `deferred` podaje brakujące evidence, owner i trigger powrotu;
- `experimental` określa granice użycia i nie pozwala na conformance claim;
- nowy rekord superseduje, ale nie usuwa wcześniejszej obserwacji lub decyzji.

Pomysły odrzucone obecnie w `EXP-3KSEF-001` obejmują niekontrolowane mnożenie
statusów i review, obowiązek jeden moduł–jeden kontrakt oraz claim pełnej
skuteczności przed representative increment.

## Relacja z feedbackiem

[Feedback lifecycle proposal](../../45-experience/feedback-lifecycle-proposal.md)
wiąże feedback z ER, CP, authority decision, `resolved_by` i
`verified_at_ref`. Feedback może rozpocząć obserwację, lecz zamknięcie wymaga
sprawdzenia dokładnej rewizji. Historyczne wpisy projektu nie są przepisywane
przez KGAID.

## Relacja z governance i release

```text
Experience Record
  -> draft CP
  -> Review
  -> explicit Maintainer decision
  -> normative document change
  -> repository controls
  -> Accepted
  -> new baseline manifest
  -> separate publication decision
```

Żaden ER ani CP nie obchodzi
[Governance, Versioning, and Release Model](../governance-and-release-model.md).
Evidence wpływa na decyzję, ale jej nie podejmuje.

## Role

| Rola | Odpowiedzialność |
| --- | --- |
| Projekt | Udostępnia dokładne evidence, ograniczenia i odpowiada za lokalne naprawy. |
| Owner Experience Record | Utrzymuje klasyfikację, lokatory i historię bez rozszerzania claims. |
| Reviewer | Sprawdza odtwarzalność dowodów i alternative explanations. |
| Właściciel metodyki | Łączy wzorce, przygotowuje CP i compatibility assessment. |
| Human Authority / Maintainer | Nadaje outcome, przyjmuje lub odrzuca zmianę i osobno autoryzuje baseline/release. |
| AI | Analizuje i proponuje; nie potwierdza własnego eksperymentu ani nie podejmuje decyzji. |

## Warianty wdrożenia

### Wariant A — model informacyjny

ER pozostaje zalecanym formatem, a CP odwołuje się do niego opcjonalnie.
Najniższy koszt, ale słabsza kompletność.

### Wariant B — ER wymagany dla zmian empirycznych

Normatywna zmiana deklarowana jako wynik doświadczenia musi wskazywać ER.
Większa audytowalność, wyższy narzut.

### Wariant C — rejestr plus automatyczne kontrole

Oprócz wariantu B validator sprawdza unikalność OBS, immutable refs, status CP,
lokalne linki i outcome authority. Najwyższa kontrola i koszt tooling.

CP nie wybiera wariantu.

## Compatibility i migracja

Model dodaje governance evidence i nie musi zmieniać istniejących artefaktów
projektów. Historyczne raporty mogą otrzymać wrapper ER bez przepisywania
źródeł. Obowiązkowość ER, format machine-readable i wpływ SemVer wymagają
osobnej decyzji.

## Pytania do Human Authority

1. Czy ER ma pozostać informacyjny, czy być wymagany dla zmian empirycznych?
2. Które propozycje wymagają drugiego projektu?
3. Kto może nadać outcome obserwacji i całego rekordu?
4. Kto zamyka feedback obejmujący projekt i KGAID?
5. Jakie evidence pozwala odstąpić od drugiego projektu?
6. Czy projekty mogą przechowywać evidence tylko przez immutable links?
7. Które pola powinien automatycznie walidować repository control?
8. Które CP z `EXP-3KSEF-001` przechodzą do Review?

Wszystkie pytania pozostają otwarte.
