---
document_id: KGAID-CP-005
title: Change Proposal Simplify Document Metadata Model

document_type: governance
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# CP-005 — Simplify Document Metadata Model

## Status propozycji

Roboczy Change Proposal będący wynikiem Experience Review. Nie zmienia
metodyki, Metadata Profile, narzędzia Approval, walidatorów ani baseline'u.
Propozycja pozostaje nieautorytatywna do czasu jawnej decyzji Human Authority
i wdrożenia zaakceptowanej zmiany w osobnym kroku.

## Problem i evidence

Governance Experience Review wskazał, że obecny model metadanych dokumentu
częściowo dubluje odpowiedzialność systemu Git. Pole `status` opisuje
informacje, które są już reprezentowane przez branch, Pull Request, merge i
stan gałęzi `main`.

Równoległe utrzymywanie `status` i `approval_status` tworzy redundancję oraz
pozwala zapisać kombinacje, których znaczenie jest niejasne lub niespójne, na
przykład:

```yaml
status: accepted
approval_status: pending
```

Faktem jest istnienie dwóch niezależnych pól oraz natywnego workflow Git.
Interpretacją Experience Review jest częściowe nakładanie się ich
odpowiedzialności. Rekomendacją wymagającą decyzji Human Authority jest
usunięcie dokumentowego pola `status` i pozostawienie jednej osi approval.

## Oczekiwany wynik

Model metadanych dokumentu powinien jednoznacznie rozdzielać:

- stan pracy i historię zmiany, reprezentowane przez Git;
- gotowość dokumentu do przeglądu i decyzję Human Authority, reprezentowane
  przez metadane approval;
- publikację obowiązującej wersji metodologii, reprezentowaną przez baseline.

## Proponowane rozwiązanie

Usunąć pole:

```yaml
status:
```

Pozostawić wyłącznie następujące metadane approval:

```yaml
approval_status: draft | pending | approved
approved_by:
approved_at:
```

Znaczenie wartości `approval_status`:

| Wartość | Znaczenie |
| --- | --- |
| `draft` | Dokument jest roboczy i nie został przekazany do decyzji. |
| `pending` | Dokument jest gotowy do przeglądu i oczekuje na decyzję Human Authority. |
| `approved` | Dokładna rewizja dokumentu została zatwierdzona przez Human Authority. |

Pola `approved_by` i `approved_at` pozostają zapisem osoby zatwierdzającej i
czasu decyzji zgodnie z regułami approval obowiązującymi dla dokładnej
rewizji.

## Nowy podział odpowiedzialności

| Mechanizm | Odpowiedzialność |
| --- | --- |
| Git | Branch, Pull Request, merge i historia zmian. |
| `approval_status` | Gotowość dokumentu do przeglądu oraz decyzja Human Authority. |
| Baseline | Publikacja obowiązującej wersji metodologii. |

Żaden z mechanizmów nie przejmuje odpowiedzialności pozostałych. Merge do
`main` nie oznacza samodzielnie approval ani publikacji baseline'u,
`approval_status: approved` nie publikuje baseline'u, a obecność w baseline
nie zastępuje historii Git.

## Uzasadnienie

Nowy model:

- eliminuje redundancję;
- usuwa konflikt pomiędzy `status` i `approval_status`;
- wykorzystuje natywny workflow Git;
- upraszcza walidatory;
- upraszcza narzędzie Approval;
- jednoznacznie rozdziela odpowiedzialności pomiędzy Git i KGAID.

## Zakres i wyłączenia

Potencjalny zakres późniejszej zmiany obejmuje definicję metadanych dokumentu,
walidację wymaganych pól, zachowanie narzędzia Approval i dokumentację
adopcyjną zależną od pola `status`.

Ten Change Proposal:

- nie modyfikuje żadnego istniejącego dokumentu;
- nie aktualizuje Metadata Profile;
- nie modyfikuje narzędzia Approval ani walidatorów;
- nie zmienia znaczenia statusów artefaktów wiedzy lub statusów
  weryfikacyjnych;
- nie podejmuje decyzji o migracji istniejących dokumentów;
- nie zmienia baseline'u ani nie publikuje nowej wersji metodologii.

## Warianty

### Wariant A — usunięcie `status`

Przyjąć proponowany model i pozostawić `approval_status`, `approved_by` oraz
`approved_at` jako jedyne pola dotyczące approval dokumentu. Git reprezentuje
przebieg pracy, a baseline reprezentuje publikację obowiązującej wersji.

### Wariant B — pozostawienie obecnego modelu

Zachować oba pola i doprecyzować ich semantykę oraz dozwolone kombinacje.
Wariant nie usuwa kosztu utrzymywania dwóch osi ani ryzyka ich rozbieżności.

### Wariant C — okres kompatybilności

Przyjąć wariant A, lecz przez określony czas tolerować `status` jako pole
przestarzałe. Walidator ostrzega o jego użyciu przed przejściem do modelu, w
którym pole jest niedozwolone.

## Compatibility i migracja

Usunięcie wymaganego pola metadanych może być zmianą niekompatybilną dla
istniejących dokumentów, walidatorów, narzędzia Approval i integracji
projektowych. Przed wdrożeniem należy:

1. zinwentaryzować użycia `status` i zależne reguły;
2. rozstrzygnąć, czy wymagany jest okres kompatybilności;
3. zdefiniować zachowanie narzędzi wobec dokumentów historycznych;
4. oddzielić mechaniczną migrację pola od decyzji Human Authority;
5. potwierdzić, że usunięcie `status` nie zmienia statusów wiedzy,
   weryfikacji ani publikacji baseline'u;
6. wykonać osobny impact review i walidację po implementacji.

Nie należy automatycznie mapować wartości `status` na `approval_status`,
ponieważ pola mają inne znaczenie, a takie mapowanie mogłoby utworzyć fikcyjną
decyzję Human Authority.

## Wpływ normatywny i SemVer

Propozycja ma potencjalnie breaking wpływ na Metadata Profile, dokumenty
normatywne, repository controls, narzędzie Approval oraz projekty korzystające
z obecnego profilu. Wstępna rekomendacja to sklasyfikowanie zaakceptowanej
zmiany jako wymagającej co najmniej minor release przed stabilnym `1.0.0`;
ostateczny wpływ SemVer wymaga osobnej decyzji po ocenie kompatybilności.

Proponowany podział zachowuje role Human Authority, Git i baseline'u, a jego
celem jest uproszczenie reprezentacji bez osłabienia audytowalności,
traceability ani jawności decyzji.

## Potwierdzenie i ryzyko uogólnienia

Propozycja wynika z Governance Experience Review i dotyczy wspólnego profilu
metadanych KGAID, nie lokalnego formatu jednego projektu. Nie przedstawiono
jeszcze potwierdzenia między projektami. Przed przyjęciem należy sprawdzić, czy
projekty adopcyjne nie wykorzystują `status` do znaczeń, których Git,
`approval_status` i baseline nie reprezentują.

## Wymagane review i Human Authority

Wymagane są co najmniej:

- architecture impact review modelu metadanych;
- compatibility review istniejących dokumentów i projektów adopcyjnych;
- tooling impact review walidatorów i narzędzia Approval;
- decyzja KGAID Methodology Maintainer jako właściwej Human Authority.

## Pytania do Human Authority

1. Czy `status` można usunąć bez utraty niezależnej informacji o dokumencie?
2. Czy wymagany jest okres kompatybilności, a jeśli tak, jak długi?
3. Jak walidować historyczne dokumenty zawierające `status`?
4. Czy `approval_status: approved` zawsze musi być związany z dokładną
   rewizją?
5. Jaki wpływ SemVer ma zaakceptowana zmiana?

Wszystkie pytania pozostają otwarte.
