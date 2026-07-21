# KGAID Documentation Approval

Samodzielne narzędzie Python do lokalnego przeglądu i ręcznej akceptacji
dokumentów Markdown zgodnych z metodyką KGAID. Jest pierwszym oficjalnym
narzędziem ekosystemu KGAID: może być kopiowane do dowolnego projektu
korzystającego z metodyki, nie zawiera pojęć ani zależności domeny projektu
konsumenckiego.

Narzędzie udostępnia lokalną kolejkę dokumentów oczekujących na akceptację,
bezpieczny podgląd Markdown i jednorazową akceptację. Zmienia wyłącznie pola
`approval_status`, `approved_by` i `approved_at` w YAML front matter, a zapis
pliku wykonuje atomowo.

## Szybki start

```bash
cd tools/kgaid_approval
python3.12 -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
.venv/bin/kgaid-doc-approval --version
.venv/bin/kgaid-doc-approval --docs-dir ../../docs --approver "Imię i nazwisko"
```

Interfejs jest domyślnie dostępny pod `http://127.0.0.1:8765`. Polecenie
`--version` pokazuje wersję oraz ścieżki interpretera, modułu i instalacji,
a zwijany panel „Diagnostics” na stronie głównej uzupełnia je o konfigurację
bieżącego uruchomienia.

## Przykładowe użycie

Po uruchomieniu wybierz dokument oczekujący na akceptację, sprawdź jego
wyrenderowaną treść i użyj przycisku **Akceptuj**. Podgląd obsługuje pełny
Markdown, w tym tabele, oraz bezpiecznie filtruje osadzony HTML. Lokalne linki
do dokumentów i katalogów zawierających `README.md` otwierają właściwy podgląd
w aplikacji.

```bash
# Uruchomienie na innym porcie
.venv/bin/kgaid-doc-approval \
  --docs-dir ../../docs \
  --approver "Anna Kowalska" \
  --host 127.0.0.1 \
  --port 9000

# Informacje o zainstalowanej wersji i środowisku
.venv/bin/kgaid-doc-approval --version
```

## Diagnostics i wersja

Zwijany panel **Diagnostics** na dole strony głównej pokazuje wersję narzędzia,
interpreter Python, lokalizację pakietu, katalog dokumentacji, osobę
zatwierdzającą i katalog roboczy. W kopii narzędzia zawierającej `UPSTREAM.md`
pokazuje także zapisane źródło. Dane te pomagają rozpoznać używaną instalację;
panel nie uruchamia poleceń Git ani nie zmienia dokumentów.

Polecenie `kgaid-doc-approval --version` wypisuje wersję i diagnostykę
instalacji w terminalu, po czym kończy działanie bez uruchamiania serwera.

## Dokumentacja

- [Instalacja w projekcie](docs/installation.md)
- [Użycie narzędzia](docs/usage.md)
- [Aktualizacja w istniejącym projekcie](docs/update.md)
- [Architektura](docs/architecture.md)
- [Kompatybilność z metodyką KGAID](docs/compatibility.md)
- [Historia zmian](CHANGELOG.md)

## Versioning

Narzędzie ma własne wersje SemVer, niezależne od wersji projektu, w którym
zostało skopiowane, oraz niezależne od wersji metodyki KGAID. Bieżąca wersja
to **0.4.0** i jej źródłem prawdy jest `pyproject.toml`.

- **MAJOR** — niekompatybilna zmiana publicznej komendy, formatu konfiguracji
  lub zachowania akceptacji;
- **MINOR** — wstecznie kompatybilna funkcja;
- **PATCH** — wstecznie kompatybilna poprawka lub zmiana dokumentacji.

Wydanie narzędzia powinno otrzymać tag `kgaid-approval-v<wersja>` i wpis w
lokalnym `CHANGELOG.md`. Przed aktualizacją projekt konsumencki powinien
sprawdzić [macierz kompatybilności](docs/compatibility.md) i przypiąć dokładną
wersję lub commit źródła.

## Granice narzędzia

Narzędzie nie zapewnia logowania, ról, odrzucania, komentarzy, historii
decyzji, diffów, traceability, automatycznego unieważniania, integracji Git ani
zewnętrznego API. Działa wyłącznie na katalogu podanym przez `--docs-dir`.

## Rozwój

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
ruff format --check .
```
