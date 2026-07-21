# Aktualizacja

Aktualizacja zastępuje kod narzędzia, ale nie może zastąpić dokumentacji ani
konfiguracji projektu. Przed rozpoczęciem zapisz lokalne rozszerzenia poza
`tools/kgaid_approval/` lub w osobnym commicie. Katalog narzędzia powinien
pozostać kopią wydania KGAID bez lokalnych modyfikacji.

## Aktualizacja krok po kroku

1. Sprawdź używaną wersję w `tools/kgaid_approval/pyproject.toml` i przeczytaj
   `CHANGELOG.md` oraz `docs/compatibility.md` wersji docelowej.
2. Pobierz źródło nowej wersji. Preferuj najnowszy tag
   `kgaid-approval-v<wersja>`; jeśli wydanie nie ma jeszcze tagu, przypnij
   dokładny commit i zapisz go w `tools/kgaid_approval/UPSTREAM.md`.
3. Zastąp zawartość `tools/kgaid_approval/` wersjonowanymi plikami ze źródła,
   nie kopiując `.venv`, cache i artefaktów buildu.
4. Odtwórz zależności i przeprowadź walidację:

   ```bash
   cd tools/kgaid_approval
   .venv/bin/python -m pip install --upgrade pip
   .venv/bin/python -m pip install -e ".[dev]"
   .venv/bin/python -m pytest
   .venv/bin/ruff check .
   .venv/bin/ruff format --check .
   .venv/bin/kgaid-doc-approval --docs-dir ../../docs --approver "KGAID reviewer"
   ```

5. Sprawdź ręcznie kolejkę w przeglądarce, przerwij serwer i zapisz wersję
   narzędzia oraz wynik kontroli w dokumentacji zmian projektu.

## Polecenie dla CODEX — aktualizacja do najnowszej wersji

Skopiuj poniższy tekst jako polecenie dla CODEX:

```text
Zaktualizuj w bieżącym projekcie tools/kgaid_approval do najnowszej stabilnej
wersji z https://github.com/KrzysztofOle/kgaid-methodology. Najpierw sprawdź
bieżące pyproject.toml, CHANGELOG.md i lokalne zmiany. Pobierz najnowszy tag
kgaid-approval-v*; jeżeli żaden tag nie istnieje, użyj aktualnego commita
domyślnej gałęzi i zapisz hash w tools/kgaid_approval/UPSTREAM.md. Zastąp tylko
wersjonowane pliki narzędzia, bez .venv, cache, build, dist i *.egg-info, nie
modyfikując docs/ ani innych plików projektu. Następnie wykonaj w katalogu
narzędzia pip install -e ".[dev]", pytest, ruff check ., ruff format --check .
i uruchom aplikację z --docs-dir ../../docs oraz --approver "KGAID reviewer".
Nie wykonuj push. Podaj starą i nową wersję/commit, listę zmian z changeloga
oraz wyniki wszystkich kontroli; przerwij serwer po potwierdzeniu startu.
```
