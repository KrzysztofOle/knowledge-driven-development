# Instalacja

Ten dokument opisuje instalację samodzielnej kopii narzędzia w projekcie
korzystającym z KGAID. Narzędzie należy umieszczać w
`tools/kgaid_approval/`; katalog `docs/` projektu pozostaje własnością
projektu konsumenckiego.

## Wymagania

- Python 3.12 lub nowszy;
- Git, jeśli narzędzie jest pobierane z repozytorium KGAID;
- dostęp do katalogu dokumentacji projektu.

## Dodanie do nowego projektu

1. Sklonuj repozytorium metodyki do katalogu tymczasowego. Dla
   powtarzalnego wdrożenia po klonowaniu przełącz się na tag wydania narzędzia
   `kgaid-approval-v<wersja>` albo na zatwierdzony commit.

   ```bash
   git clone https://github.com/KrzysztofOle/kgaid-methodology.git /tmp/kgaid-methodology
   # Opcjonalnie po opublikowaniu wydania:
   # git -C /tmp/kgaid-methodology checkout kgaid-approval-v0.4.0
   ```

2. Z katalogu głównego projektu skopiuj wyłącznie wersjonowane pliki
   narzędzia. Nie kopiuj środowiska wirtualnego, cache ani artefaktów buildu.

   ```bash
   mkdir -p tools
   rsync -a --delete \
     --exclude '.venv' --exclude '.pytest_cache' --exclude '.ruff_cache' \
     --exclude '__pycache__' --exclude 'build' --exclude 'dist' \
     --exclude '*.egg-info' \
     /tmp/kgaid-methodology/tools/kgaid_approval/ tools/kgaid_approval/
   ```

3. Utwórz izolowane środowisko Python i zainstaluj aplikację wraz z narzędziami
   testowymi.

   ```bash
   cd tools/kgaid_approval
   python3.12 -m venv .venv
   .venv/bin/python -m pip install --upgrade pip
   .venv/bin/python -m pip install -e ".[dev]"
   ```

4. Sprawdź instalację i uruchom aplikację dla katalogu dokumentacji projektu.

   ```bash
   .venv/bin/python -m pytest
   .venv/bin/ruff check .
   .venv/bin/kgaid-doc-approval \
     --docs-dir ../../docs \
     --approver "Imię i nazwisko"
   ```

   Otwórz `http://127.0.0.1:8765`. Przerwij serwer przez `Ctrl+C`.

## Przykładowe polecenia

```bash
# Inny katalog dokumentacji i port
tools/kgaid_approval/.venv/bin/kgaid-doc-approval \
  --docs-dir documentation \
  --approver "Anna Kowalska" \
  --host 127.0.0.1 \
  --port 9000

# Kontrole jakości po instalacji
tools/kgaid_approval/.venv/bin/python -m pytest tools/kgaid_approval/tests
tools/kgaid_approval/.venv/bin/ruff check tools/kgaid_approval
tools/kgaid_approval/.venv/bin/ruff format --check tools/kgaid_approval
```

## Polecenie dla CODEX — dodanie narzędzia

Skopiuj poniższy tekst jako polecenie dla CODEX:

```text
Dodaj do bieżącego projektu najnowszą stabilną wersję narzędzia KGAID
Documentation Approval z https://github.com/KrzysztofOle/kgaid-methodology.
Skopiuj wyłącznie tools/kgaid_approval do tools/kgaid_approval, bez .venv,
cache, build, dist i *.egg-info. Jeżeli istnieje tag kgaid-approval-v*, użyj
najnowszego tagu; w przeciwnym razie użyj aktualnego commita domyślnej gałęzi
i zapisz jego hash w tools/kgaid_approval/UPSTREAM.md. Utwórz w tym katalogu
.venv z Pythonem 3.12+, zainstaluj pip install -e ".[dev]", następnie uruchom
pytest, ruff check ., ruff format --check . oraz aplikację z --docs-dir docs i
--approver "KGAID reviewer". Nie zmieniaj dokumentów projektu ani nie wykonuj
push; przedstaw wynik walidacji i źródłową wersję/commit narzędzia.
```
