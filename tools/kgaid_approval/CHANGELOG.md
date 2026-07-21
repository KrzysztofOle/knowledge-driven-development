# Changelog

Wszystkie istotne zmiany tego narzędzia są dokumentowane w tym pliku.
Format jest oparty na [Keep a Changelog](https://keepachangelog.com/pl/1.1.0/),
a wersje stosują [Semantic Versioning](https://semver.org/lang/pl/).

## [Unreleased]

### Added

- Dodano diagnostykę środowiska w `--version` i na stronie głównej aplikacji.
- Dodano obsługę linków do katalogów zawierających `README.md`.

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
