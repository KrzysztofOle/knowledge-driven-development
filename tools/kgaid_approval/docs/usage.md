# Użycie

## Uruchomienie

Z katalogu głównego projektu:

```bash
tools/kgaid_approval/.venv/bin/kgaid-doc-approval \
  --docs-dir docs \
  --approver "Imię i nazwisko"
```

Opcje:

- `--version` — wypisuje wersję narzędzia, lokalizację instalacji i informacje
  o interpreterze, po czym kończy działanie bez uruchamiania serwera;
- `--docs-dir` — wymagany katalog dokumentacji; narzędzie nie odczytuje ani
  nie modyfikuje plików poza nim;
- `--approver` — wymagana nazwa osoby zatwierdzającej;
- `--host` — adres serwera, domyślnie `127.0.0.1`;
- `--port` — port serwera, domyślnie `8765`.

Po uruchomieniu otwórz adres wypisany w terminalu. Kolejka zawiera wyłącznie
poprawne dokumenty Markdown (`.md` lub `.markdown`) z jawnym statusem
`approval_status: pending`.

## Wymagany front matter

Minimalny dokument, który pojawi się w kolejce:

```yaml
---
document_id: REQ-001
title: Utworzenie faktury roboczej
approval_status: pending
---
```

Pola `document_id` i `title` są prezentowane w interfejsie, ale nie są
wymagane do akceptacji. Zachowaj w dokumencie pola wymagane przez profil KGAID
stosowany przez Twój projekt, na przykład `document_type`, `status`, `version`
i `owner`.

## Akceptacja

W kolejce wybierz **Podgląd**, aby przeczytać dokument, albo **Akceptuj**, aby
zapisać decyzję. Po akceptacji narzędzie atomowo aktualizuje tylko poniższe
pola:

```yaml
approval_status: approved
approved_by: "Imię i nazwisko"
approved_at: 2026-07-21T12:34:56+02:00
```

Pozostały front matter i treść dokumentu nie są przeformatowywane. Dokument ze
statusem `approved` można oglądać przez link w innym dokumencie, lecz nie można
go zatwierdzić drugi raz.

## Bezpieczeństwo i ograniczenia

Nieprawidłowy lub niejednoznaczny YAML jest pomijany w kolejce i nie zostanie
zapisany. Ścieżki wychodzące poza `--docs-dir` oraz niebędące Markdown są
odrzucane. Podgląd renderuje Markdown z listą dozwolonych elementów HTML;
lokalne linki do innych dokumentów Markdown są bezpiecznie prowadzone przez
interfejs narzędzia.

## Panel Diagnostics

Zwijany panel **Diagnostics** na dole strony głównej pokazuje wersję narzędzia,
interpreter Python, lokalizację pakietu, katalog dokumentacji, osobę
zatwierdzającą oraz katalog roboczy. Jeżeli instalacja zawiera plik
`UPSTREAM.md`, panel pokazuje również zapisane źródło kopii. Informacje służą
wyłącznie do identyfikacji uruchomionej instalacji.
