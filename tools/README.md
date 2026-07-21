# Narzędzia KGAID

Ten katalog jest źródłem niewielkich, niezależnych narzędzi wspierających
wdrożenie KGAID. Narzędzie nie jest funkcją biznesową projektu konsumenckiego:
projekt przechowuje własną dokumentację i konfigurację, a implementacja oraz
testy narzędzia pozostają tutaj.

## Zasada korzystania

Każde narzędzie jest samodzielnym pakietem w `tools/<nazwa>/` z własnym
`pyproject.toml`, wersją SemVer, `CHANGELOG.md`, dokumentacją, instrukcją
uruchomienia i testami. Katalog jest przygotowany do rozbudowy o kolejne
narzędzia, na przykład walidator dokumentacji, generator traceability lub
generator szablonów. Projekt konsumencki ma dwa wspierane sposoby użycia:

1. podczas lokalnego rozwoju instaluje pakiet editable z lokalnego klonu
   `kgaid-methodology`;
2. w powtarzalnym środowisku instaluje pakiet z adresu Git, przypinając tag
   wydania lub niezmienny commit i używając `#subdirectory=tools/<nazwa>`.

Projekt konsumencki zapisuje wybrany tag albo commit we własnej konfiguracji
zależności lub instrukcji developerskiej. Nie kopiuje kodu narzędzia; podnosi
wersję przez jawną aktualizację zależności, a potem wykonuje własne kontrole.
Taki podział zachowuje jedno źródło implementacji, a jednocześnie nie narzuca
projektom technologii ani nie miesza narzędzi KGAID z ich domeną biznesową.

## Dostępne narzędzia

- [KGAID Documentation Approval](kgaid_approval/README.md) — pierwsze
  oficjalne narzędzie ekosystemu KGAID: lokalna kolejka, podgląd i ręczna
  akceptacja dokumentów Markdown z front matter.
- [KGAID Documentation Archive](kgaid_docs_archive/README.md) — tworzy archiwum
  całego katalogu `docs/` o nazwie `docs_RRRR-MM-DD_hhmm.zip`.
- [KGAID Project Review](kgaid_project_review/README.md) — niezależny,
  działający wyłącznie w trybie odczytu raport zdrowia dokumentacji projektu;
  wspiera przegląd człowieka, ale nie podejmuje decyzji o baseline ani gotowości.
