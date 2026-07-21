# Kompatybilność

## Macierz kompatybilności

| Wersja narzędzia | Wersje metodyki KGAID | Status |
| --- | --- | --- |
| 0.5.x | KGAID-0.1.x | wspierana |
| 0.3.x | KGAID-0.1.x | wspierana |

Kompatybilność dotyczy metadanych dokumentu wymaganych przez narzędzie:
`approval_status`, `approved_by` i `approved_at`. Wersja 0.5.x rozpoznaje
`draft`, `pending` i `approved`; do kolejki oraz akceptacji kwalifikuje tylko
`pending`. Narzędzie zachowuje
pozostałe pola KGAID bez interpretowania ich znaczenia, dlatego projekt może
stosować rozszerzony profil metadanych, o ile nie zmienia semantyki tych trzech
pól.

## Zasady aktualizacji

- Wersja narzędzia i wersja metodyki są niezależne.
- Zmiana wspieranej wersji KGAID jest odnotowywana w tym dokumencie i w
  `CHANGELOG.md` narzędzia.
- Projekt konsumencki przypina używaną wersję narzędzia lub commit źródłowy,
  a aktualizację weryfikuje własnymi kontrolami.
- Brak wpisu w macierzy oznacza brak deklaracji kompatybilności, a nie
  automatyczną zgodność.
