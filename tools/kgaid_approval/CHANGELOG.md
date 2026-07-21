# Changelog

Wszystkie istotne zmiany tego narzędzia są dokumentowane w tym pliku.
Format jest oparty na [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/),
a wersje stosują [Semantic Versioning](https://semver.org/lang/pl/).

## [Unreleased]

## [0.5.0] - 2026-07-21

### Added

- Dodano obsługę statusu `approval_status: draft` dla dokumentów roboczych.

### Changed

- Kolejka Human Authority i akcja akceptacji obsługują wyłącznie dokumenty ze
  statusem `pending`; dokumenty `draft` są pomijane do czasu jawnego przejścia
  `draft` → `pending`.

### Tests

- Dodano testy dokumentów `draft` w kolejce i przy próbie akceptacji.

## [0.4.0] - 2026-07-21

### Added

- Dodano pełny renderer Markdown, w tym obsługę tabel.
- Dodano bezpieczne renderowanie osadzonego HTML przez filtrowanie dozwolonych
  elementów, atrybutów i protokołów.
- Dodano panel **Diagnostics** z wersją, ścieżkami instalacji i konfiguracją
  bieżącego uruchomienia.
- Dodano polecenie `--version` pokazujące wersję i diagnostykę środowiska bez
  uruchamiania serwera.
- Dodano obsługę linków do katalogów zawierających `README.md`.

### Fixed

- Poprawiono rozwiązywanie względnych linków do dokumentów Markdown, kotwic,
  parametrów zapytania i zasobów względem bieżącego dokumentu.

### Tests

- Rozszerzono testy renderowania Markdown i HTML, tabel, bezpieczeństwa
  odnośników, linków katalogowych, diagnostyki oraz polecenia `--version`.

## [0.3.0] - 2026-07-21

### Changed

- Przeniesiono pakiet do układu `src/`, aby narzędzie było samodzielnym,
  przenośnym pakietem Python.
- Usunięto z narzędzia opis i zależności związane z pilotażem konkretnego
  projektu.
- Dodano pełną dokumentację instalacji, użycia, aktualizacji, architektury i
  kompatybilności z KGAID.

### Compatibility

- Zachowano nazwę pakietu `kgaid-documentation-approval`, moduł
  `kgaid_approval` i komendę `kgaid-doc-approval`.
- Zachowano dotychczasowe zachowanie aplikacji i istniejące testy.

## [0.2.3]

### Changed

- Ostatnia wersja przed usamodzielnieniem struktury narzędzia.
