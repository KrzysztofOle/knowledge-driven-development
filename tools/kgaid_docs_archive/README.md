# KGAID Documentation Archive

Narzędzie tworzy archiwum ZIP całej dokumentacji projektu, zachowując strukturę
`docs/`. Domyślna nazwa pliku ma postać `docs_RRRR-MM-DD_hhmm.zip`, na przykład
`docs_2026-07-20_1430.zip`.

## Instalacja lokalna

```bash
python3 -m pip install -e tools/kgaid_docs_archive
```

## Użycie

Uruchomione z katalogu głównego projektu:

```bash
kgaid-docs-archive
```

Archiwum zostanie zapisane w katalogu głównym projektu. Aby wskazać inny projekt
lub katalog docelowy:

```bash
kgaid-docs-archive --root /sciezka/do/projektu --output-dir /sciezka/do/archiwow
```

Można również uruchomić moduł bez instalowania pakietu:

```bash
PYTHONPATH=tools/kgaid_docs_archive python3 -m kgaid_docs_archive
```

Jeśli katalog `docs/` nie istnieje albo katalog docelowy nie istnieje, narzędzie
kończy się komunikatem błędu i nie tworzy częściowego archiwum.
Nie nadpisuje też archiwum utworzonego już w tej samej minucie.
