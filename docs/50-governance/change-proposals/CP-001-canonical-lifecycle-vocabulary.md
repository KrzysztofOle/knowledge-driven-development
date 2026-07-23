---
document_id: KGAID-CP-001
title: Change Proposal Canonical Lifecycle Vocabulary

document_type: governance
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# CP-001 — Canonical lifecycle vocabulary

## Status propozycji

Projekt do decyzji Human Authority. Nie wybiera finalnego słownika, nie zmienia
istniejących dokumentów i nie należy do `KGAID-0.1.0`.

## Problem i evidence

`EXP-3KSEF-001` wskazuje:

- `OBS-006` — techniczny approval bywa odczytywany jako akceptacja wiedzy;
- `OBS-021` — normatywny Artifact Model i Knowledge Lifecycle używają innego
  słownika niż Metadata Profile i informacyjny Approval Center;
- `OBS-022` — brak dowodu, że rozwiązaniem jest dodanie kolejnych statusów.

Dowody: `EV-029`, `EV-030`, `EV-039`, `EV-041` z
[Experience Record](../../45-experience/reference-projects/3ksef/EXP-3KSEF-001.md#katalog-dowodów).

## Aktualne słowniki

| Pojęcie | Artifact Model / Knowledge Lifecycle | Metadata Profile | Approval Center / praktyka | Konflikt |
| --- | --- | --- | --- | --- |
| Wczesne uchwycenie | `captured` | `draft` | `draft` | Nie wiadomo, czy opisują wiedzę, dokument czy kolejkę. |
| Kandydat | `proposed` | `proposed` | proposal/draft | Częściowa zgodność. |
| Review | `reviewed` | review jako activity | `pending` jako kolejka approval | Stan wiedzy miesza się z aktywnością i stanem technicznym. |
| Autorytet | `accepted` | `accepted` | `approved` | `accepted` i `approved` bywają utożsamiane. |
| Zastąpienie | `superseded` | `superseded` | supersession projektowany | Zasadniczo zgodne, lecz brak jednego recordu przejścia. |
| Koniec użycia | `retired` | brak | `deprecated` | Niejasna różnica zakończenia obowiązywania i zniechęcenia. |
| Odrzucenie | `rejected` | brak | rejected/decision outcome | Brak reprezentacji w profilu dokumentu. |
| Wycofanie kandydata | brak jawnego `withdrawn` | brak | spotykane lokalnie | Nie wiadomo, czy mapować na `rejected`, `retired` czy historię propozycji. |
| Zniechęcenie | brak `deprecated` | `deprecated` | spotykane w narzędziach | Konflikt z `retired` i `superseded`. |

Analizowany pełny zbiór nazw to `captured`, `proposed`, `reviewed`, `accepted`,
`superseded`, `retired`, `rejected`, `draft`, `deprecated` i `withdrawn`.

## Osie wymagające rozdzielenia

### Status wiedzy

Odpowiada na pytanie, jaki autorytet ma twierdzenie lub artefakt wiedzy.
Obecny normatywny kandydat:
`captured → proposed → reviewed → accepted`, z wynikami `rejected`,
`superseded` i `retired`.

### Status dokumentu lub opracowania

Odpowiada na pytanie, czy kontener treści jest szkicem, gotowym kandydatem,
zastąpioną publikacją albo materiałem historycznym. Nie musi być tożsamy ze
statusem każdego artefaktu wiedzy zawartego w pliku.

### Techniczny status approval

Odpowiada wyłącznie na pytanie, czy dokładna rewizja została przekazana do
mechanizmu approval i czy zapisano decyzję. Obecne wartości to `draft`,
`pending`, `approved`. Nie powinny same nadawać autorytetu wiedzy.

## Warianty

### Wariant A — jedna oś treści zgodna z Knowledge Lifecycle

Metadata Profile przyjmuje pełny normatywny słownik wiedzy. Stan dokumentu nie
jest osobną osią, a approval pozostaje techniczny.

- korzyść: jeden słownik i prostsza walidacja;
- koszt: plik z wieloma artefaktami może mieć zbyt uproszczony status;
- ryzyko: `reviewed` nadal może być mylone z wykonaniem review;
- migracja: `draft → captured`, `deprecated → retired` albo `superseded`,
  `withdrawn → rejected` tylko po sprawdzeniu znaczenia.

### Wariant B — dwie jawne osie semantyczne plus approval

Wprowadzić osobno `knowledge_status`, `document_status` i techniczny
`approval_status`, wraz z regułami, która oś obowiązuje dla danego typu.

- korzyść: usuwa niejawne mieszanie trzech pytań;
- koszt: nowe pola, migracja narzędzi i wyższy narzut;
- ryzyko: trzy osie mogą zwiększyć koszt bez automatycznej kontroli;
- migracja: zachować stare `status` jako alias w okresie kompatybilności i
  wymagać jawnego mapowania.

### Wariant C — profil minimalny i rozszerzony

Profil minimalny używa jednego `status` oraz niezależnego approval. Profil
rozszerzony może adresować artefakty wiedzy wewnątrz dokumentu i osobny stan
kontenera.

- korzyść: rygor proporcjonalny do projektu;
- koszt: conformance musi sprawdzać dwa profile;
- ryzyko: różne profile mogą ponownie rozszczepić słownik;
- migracja: każdy projekt deklaruje profil i mapowanie wartości.

### Wariant D — tylko clarification precedence

Nie zmieniać pól przed `0.1.0`; dodać jednoznaczną tabelę precedence i
mapowanie, pozostawiając pełną zmianę do następnej wersji.

- korzyść: najmniejszy koszt przed publikacją;
- koszt: utrzymuje strukturalną niespójność;
- ryzyko: wdrażający nadal potrzebuje lokalnego workaround;
- migracja: brak natychmiastowej migracji danych, ale konieczny późniejszy CP.

## Compatibility i migracja

Każdy wybrany wariant powinien:

1. opublikować tabelę stara wartość → nowa wartość → warunek;
2. nie mapować automatycznie `approved` na `accepted`;
3. zachować historyczne wartości w Git i decision history;
4. zdefiniować odczyt starych dokumentów przez narzędzia;
5. określić wersję, w której aliasy staną się błędem;
6. rozróżnić migrację metadanych od nowej decyzji Human Authority;
7. sklasyfikować wpływ SemVer przed zmianą normy.

Automatyczna zamiana `deprecated` na `retired` albo `withdrawn` na `rejected`
nie jest bezpieczna bez sprawdzenia intencji. Zmiana nazwy nie może tworzyć
fikcyjnej decyzji lifecycle.

## Pytania do Human Authority

1. Czy status wiedzy i status dokumentu mają być osobnymi osiami?
2. Która oś pozostaje obowiązkowa w profilu Minimal?
3. Czy `reviewed` jest stanem wiedzy czy jedynie zapisem aktywności?
4. Czy `retired` i `deprecated` mają różne znaczenia?
5. Jak reprezentować wycofanie propozycji bez fałszywego odrzucenia?
6. Jaką rolę pełni `approval_status` i czy może towarzyszyć decyzji
   lifecycle bez jej zastępowania?
7. Który wariant kompatybilności jest akceptowalny przed publikacją?

Wszystkie pytania pozostają otwarte.

## Wpływ normatywny

Potencjalnie breaking: definicje lifecycle, metadata profile, narzędzia,
adoption mappings, baseline checks i dokumenty projektów. Wymagany osobny
compatibility assessment, review i jawna decyzja Maintainer przed jakąkolwiek
zmianą normy.
