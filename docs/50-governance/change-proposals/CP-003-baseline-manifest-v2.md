---
document_id: KGAID-CP-003
title: Change Proposal Baseline Manifest v2

document_type: governance
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# CP-003 — Baseline Manifest v2

## Status propozycji

Projekt do decyzji Human Authority. Nie zmienia obecnego manifestu
`KGAID-0.1.0`, nie rozstrzyga `accepted-only` ani wyjątków i nie publikuje
baseline'u.

## Problem i evidence

Źródłowe obserwacje:

- `OBS-005` — nazwa przygotowanego, nieopublikowanego baseline'u nie jest
  niezmiennym pinem;
- `OBS-007` — lokalny baseline obejmuje wiedzę poniżej `accepted`;
- `OBS-012` — niejasna relacja review, readiness i baseline'u;
- `OBS-017` — member link może pozostać w manifeście po przeniesieniu pliku.

Dowody `EV-004`, `EV-006`, `EV-007`, `EV-010`, `EV-018`, `EV-029`, `EV-036`,
`EV-037` i `EV-038` są skatalogowane w
[EXP-3KSEF-001](../../45-experience/reference-projects/3ksef/EXP-3KSEF-001.md#katalog-dowodów).

## Cele

Manifest v2 powinien:

1. jednoznacznie identyfikować baseline metodologii albo projektu;
2. wiązać każdego członka z niezmienną treścią i statusem wiedzy;
3. zapisywać Human Decision bez uzależnienia od narzędzia;
4. umożliwiać automatyczną kontrolę integralności;
5. zachować supersession i relację z review;
6. nie nadawać autorytetu elementom przez samo umieszczenie na liście.

## Proponowany model roboczy

```yaml
schema: kgaid-baseline-manifest/v2-draft
baseline_id: PROJECT-BASELINE-1.0
baseline_kind: methodology | project
methodology:
  repository: owner/kgaid-methodology
  ref: full-commit-or-published-tag
  manifest_hash: sha256:optional
project:
  repository: owner/project
  ref: full-commit
scope: exact baseline boundary
created_at: YYYY-MM-DDThh:mm:ss+offset
publication_status: prepared-unpublished
membership_policy: accepted-only | accepted-with-controlled-exceptions
members:
  - id: ART-NNN
    path: path/to/member
    revision: full-commit
    content_hash: sha256:value
    knowledge_status: accepted
    exception: null
human_decision:
  decision_id: HD-NNN
  subject_ref: manifest-content-hash
related_reviews: []
supersedes: null
integrity:
  algorithm: sha256
  checked_at: YYYY-MM-DDThh:mm:ss+offset
  result: valid
```

Pole `revision` może wskazywać wspólny commit baseline'u, ale `content_hash`
każdego membera umożliwia wykrycie zmiany i przeniesienia. Human Authority musi
wybrać minimalny wymagany zestaw.

## Identyfikacja metodologii i projektu

Baseline projektu zapisuje oba punkty:

- dokładną rewizję projektu, której artefakty są członkami;
- dokładną rewizję lub opublikowany tag/manifest KGAID, według którego baseline
  został utworzony.

Stan `prepared-unpublished` jest jawny. Nazwa wersji bez niezmiennego ref nie
wystarcza do odtworzenia znaczenia.

## Członkostwo i status wiedzy

### Wariant A — bezwzględne `accepted-only`

Każdy member ma status `accepted` w dokładnej rewizji. Naruszenie blokuje
utworzenie lub walidację baseline'u.

- korzyść: jedno źródło autorytetu;
- koszt: potrzeba większej liczby decyzji przed baseline;
- ryzyko: projekty mogą tworzyć zbyt szerokie statusy `accepted`.

### Wariant B — kontrolowane wyjątki per item

Domyślnie obowiązuje `accepted-only`, ale member może zawierać:

```yaml
exception:
  decision_id: HD-NNN
  rationale: reason for bounded inclusion
  scope: allowed use
  risk_owner: human-role
  expires_at: YYYY-MM-DD
  required_follow_up: action
```

- korzyść: umożliwia kontrolowany baseline przy świadomym ryzyku;
- koszt: walidacja wyjątków, terminów i scope;
- ryzyko: wyjątki mogą stać się normalnym obejściem lifecycle.

CP nie wybiera wariantu.

## Human Decision i supersession

Decyzja wskazuje hash dokładnego manifestu i authority. Zmiana membera, statusu,
wyjątku, scope albo metadanych integralności tworzy nową rewizję wymagającą
impact review. Opublikowany baseline jest niezmienny; korekta tworzy nowy
baseline z `supersedes`.

Supersession nie usuwa:

- starego manifestu;
- starego decision record;
- wyniku integralności;
- review i wyjątków obowiązujących dla starej wersji.

## Walidacja integralności

Validator powinien co najmniej wykrywać:

| Kontrola | Oczekiwany wynik |
| --- | --- |
| Member exists | Ścieżka lub identyfikator istnieje w zadanej rewizji. |
| Identity | `id` odpowiada zawartości membera. |
| Revision/hash | Treść odpowiada `revision` i `content_hash`. |
| Knowledge status | `accepted` albo poprawny wyjątek według wybranego wariantu. |
| Exception | Decision, scope, owner i expiry są kompletne. |
| Broken links | Lokalne linki członka i manifestu są rozwiązywalne w baseline ref. |
| Missing dependency | Wymagana zależność jest członkiem lub jawnie zewnętrzna. |
| Changed after decision | Subject manifestu odpowiada Human Decision. |
| Duplicate member | Ten sam ID nie występuje sprzecznie więcej niż raz. |
| Supersession | Poprzedni baseline istnieje i nie tworzy cyklu. |
| Review validity | Review dotyczy dokładnego ref i wymagany scope jest pokryty. |

Wynik validatora jest evidence. Nie podejmuje decyzji o akceptacji wyjątku,
ryzyka ani publikacji.

## Relacja z review

Review baseline'u ocenia spójność listy i evidence dla dokładnej rewizji.
Review warstwy ocenia treść w określonym scope. Readiness do kolejnego kroku
nie jest automatycznie zgodą na członkostwo ani publikację baseline'u.
Manifest przechowuje identyfikatory review, ich subject refs, wyniki i warunki
ważności.

## Broken links, braki i późniejsza zmiana

- broken link w przygotowywanym manifeście blokuje wynik `valid`;
- brak membera albo content hash oznacza niekompletny manifest;
- zmiana membera po decyzji powoduje mismatch i wymaga nowej decyzji;
- naprawa ścieżki bez zmiany treści również tworzy nową rewizję manifestu,
  choć polityka może dopuścić ograniczony reapproval;
- narzędzie nie naprawia automatycznie ścieżki ani statusu.

## Compatibility i migracja

1. Obecny manifest pozostaje czytelny jako schema v1.
2. Migrator może wyliczyć hash tylko z dostępnej dokładnej rewizji.
3. Brak znanej rewizji oznacza `unresolved`, nie domyślne `current HEAD`.
4. Existing accepted status nie zastępuje Human Decision dla nowego manifestu.
5. Projekty mogą pilotować v2 bez publikowania baseline'u KGAID.
6. Wpływ SemVer i wymagany okres kompatybilności pozostają do oceny.

## Pytania do Human Authority

1. Czy baseline jest bezwzględnie `accepted-only`?
2. Czy dopuszczać kontrolowane wyjątki per item?
3. Czy content hash każdego membera jest obowiązkowy?
4. Czy commit + path wystarcza w repozytorium o chronionej historii?
5. Jakie kontrole blokują baseline, a jakie tworzą residual risk?
6. Kto akceptuje wyjątek i jego wygaśnięcie?
7. Jaka jest relacja review readiness do decyzji baseline?
8. Czy schema v2 ma dotyczyć baseline'ów projektu, metodologii czy obu?

Wszystkie pytania pozostają otwarte.
