# Architektura

## Struktura katalogów

```text
kgaid_approval/
├── src/kgaid_approval/   # pakiet aplikacji
├── tests/                # testy zachowania i bezpieczeństwa
├── docs/                 # dokumentacja użytkownika i utrzymania
├── CHANGELOG.md          # historia wydań narzędzia
├── README.md             # punkt wejścia dokumentacji
└── pyproject.toml        # metadane pakietu, zależności i konfiguracja narzędzi
```

Układ `src/` oddziela kod importowanego pakietu od konfiguracji i testów.
Chroni to przed przypadkowym przejściem testów dzięki importowaniu pakietu z
katalogu roboczego zamiast z instalowanej dystrybucji.

## Komponenty

- `cli.py` odczytuje argumenty i uruchamia lokalny serwer Flask.
- `diagnostics.py` identyfikuje wersję, instalację i środowisko uruchomieniowe
  bez wywoływania poleceń Git.
- `app.py` tworzy aplikację Flask i definiuje kolejkę, podgląd oraz akcję
  akceptacji.
- `repository.py` bezpiecznie skanuje katalog dokumentacji, interpretuje YAML
  front matter i atomowo zapisuje trzy pola decyzji.
- `web.py` renderuje i sanitizuje Markdown oraz tworzy prosty interfejs HTML.
- `routes.py` centralizuje nazwy endpointów i parametrów URL.

Przepływ jest celowo jednokierunkowy:

```text
CLI → DocumentationRepository → Flask routes → HTML/Markdown view
                 ↑                    │
                 └── atomowy zapis ←──┘
```

`DocumentationRepository` jest granicą bezpieczeństwa: rozwiązuje ścieżki
względem `--docs-dir`, odrzuca wyjście poza katalog oraz pliki inne niż
Markdown. Warstwa webowa nie zapisuje plików bezpośrednio.

## Stabilne interfejsy

Wersja 0.4.0 zachowuje dotychczasowe interfejsy dla projektów konsumenckich:

- nazwę dystrybucji `kgaid-documentation-approval`;
- moduł Python `kgaid_approval`;
- komendę `kgaid-doc-approval`;
- argumenty `--docs-dir`, `--approver`, `--host` i `--port`;
- format i zakres aktualizacji YAML front matter.

Zmiany tych interfejsów wymagają wydania MAJOR i opisanej migracji.
