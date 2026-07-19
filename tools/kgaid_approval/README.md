# KGAID Documentation Approval MVP

To niezależne, lokalne narzędzie deweloperskie do przeglądania i ręcznego
akceptowania dokumentacji Markdown. Jego kod źródłowy należy do repozytorium
KGAID Methodology. Projekty przyjmujące KGAID, takie jak 3ksef, używają tego
pakietu jako zewnętrznego narzędzia i nie kopiują jego implementacji do własnej
domeny.

To jest MVP proponowanego Approval Center, a nie implementacja pełnego
Approval Framework ani normatywne rozszerzenie metodyki.

## Instalacja i uruchomienie

### Z lokalnego klonu KGAID

W projekcie korzystającym z narzędzia:

```bash
python -m pip install \
  -e /ścieżka/do/kgaid-methodology/tools/kgaid_approval
kgaid-doc-approval --docs-dir docs --approver "Imię i nazwisko"
```

### Z repozytorium KGAID

Wersję należy przypiąć do tagu wydania albo niezmiennego commita KGAID:

```bash
python -m pip install \
  "kgaid-documentation-approval @ git+ssh://git@github.com/KrzysztofOle/kgaid-methodology.git@<tag-lub-commit>#subdirectory=tools/kgaid_approval"
kgaid-doc-approval --docs-dir docs --approver "Imię i nazwisko"
```

Domyślny adres lokalnego interfejsu to `http://127.0.0.1:8765`. Zmień go przez
`--host` i `--port`; `--docs-dir` jest jedynym katalogiem, w którym narzędzie
może wyszukiwać i modyfikować pliki.

## VS Code

Repozytorium zawiera konfigurację **KGAID: Documentation Approval MVP** w
`.vscode/launch.json`. Po wybraniu jej w panelu Run and Debug i uruchomieniu
VS Code poprosi o nazwę osoby zatwierdzającej, a następnie otworzy narzędzie
dla katalogu `docs` pod adresem `http://127.0.0.1:8765`.

Po instalacji projekt konsumencki powinien zapisać wybrany tag lub commit w
swoim pliku zależności albo instrukcji deweloperskiej. Dzięki temu używa
powtarzalnej wersji narzędzia, a aktualizacja KGAID jest jawną zmianą zależności
z własnymi testami i akceptacją.

## Wymagane metadane

Do kolejki trafia wyłącznie dokument Markdown, który zaczyna się od YAML front
matter i ma jawne pole:

```yaml
---
document_id: REQ-001
title: Utworzenie faktury roboczej
approval_status: pending
approved_by:
approved_at:
---
```

Dokument bez `approval_status` oraz dokument ze statusem `approved` nie trafia
do kolejki. Po użyciu przycisku **Akceptuj** narzędzie zapisuje `approved`,
wartość `--approver` i lokalny czas ISO 8601 z przesunięciem strefy. Zachowuje
pozostałe pola i treść poniżej front matter.

## Pilotaż 3ksef

Pierwszym konsumentem jest 3ksef. Pilotaż obejmuje dwa istniejące Requirements
z `CAP-003`: `REQ-001-utworzenie-faktury-roboczej.md` i
`REQ-005-walidacja-faktury.md`. Ich front matter oznacza oczekiwanie na
świadomą decyzję człowieka; 3ksef nie zawiera kodu narzędzia ani zależności
biznesowych z nim związanych.

## Granice MVP

MVP oferuje kolejkę, podgląd i jednorazową akceptację pojedynczego dokumentu.
Nie oferuje logowania, ról, odrzucania, komentarzy, historii decyzji, diffów,
traceability, automatycznego unieważniania, integracji z GitHubem ani API dla
klientów zewnętrznych. Nie wykonuje też żadnych poleceń Git.

Zapis jest atomowy w katalogu docelowym. Nieprawidłowy lub niejednoznaczny YAML
jest pomijany w kolejce i blokuje zapis, a ścieżka poza skonfigurowanym
katalogiem jest odrzucana.

## Rozwój narzędzia

Uruchom kontrole z katalogu tego narzędzia:

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
ruff format --check .
```
