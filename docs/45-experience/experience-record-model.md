---
document_id: KGAID-EXP-001
title: KGAID Experience Record Model

document_type: knowledge
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# KGAID Experience Record Model

## Status i cel

To jest projekt informacyjnego modelu, a nie obowiązująca norma KGAID.
Experience Record (ER) zachowuje wynik analizy rzeczywistego użycia metodyki
tak, aby dowody, interpretacje, propozycje i decyzje pozostały rozdzielone.
Model jest niezależny od domeny projektu, technologii oraz układu jego
katalogów.

ER nie:

- przyznaje projektowi statusu oficjalnego projektu referencyjnego;
- akceptuje zmiany metodologii;
- zmienia statusu wiedzy w projekcie źródłowym;
- zastępuje Change Proposal, Human Decision ani evidence;
- tworzy zależności kodowej lub repozytoryjnej między KGAID a projektem.

## Jednostki modelu

Rekord zawiera metadane analizy, katalog obserwacji, katalog dowodów, listę
hipotez i działań oraz historię decyzji. Obserwacja jest podstawową jednostką
klasyfikacji. Może prowadzić do kilku działań, ale ma jeden główny wpis i jeden
aktualny wynik.

### Wymagane pola rekordu

| Pole | Znaczenie |
| --- | --- |
| `experience_id` | Stabilny i nieużywany ponownie identyfikator, np. `EXP-PROJECT-001`. |
| `source_project` | Nazwa i jednoznaczny identyfikator projektu źródłowego. |
| `source_repository` | Repozytorium dowodowe; odwołanie, nie zależność KGAID. |
| `source_ref` | Niezmienny commit, tag wskazujący niezmienną treść albo równoważny identyfikator. |
| `methodology_repository` | Repozytorium KGAID użyte do porównania. |
| `methodology_ref` | Dokładny commit albo opublikowana wersja i jej niezmienny manifest. |
| `methodology_publication_status` | Stan publikacji użytej wersji, jeśli jest znany. |
| `analysis_date` | Data analizy w formacie ISO 8601. |
| `analysis_scope` | Repozytoria, warstwy, okres, rodzaje artefaktów i pytań. |
| `limitations` | Braki danych, granice wnioskowania i niewykonane kontrole. |
| `source_materials` | Raporty, audyty lub zbiory danych będące wejściem ER. |
| `observations` | Stabilnie identyfikowane obserwacje i ich klasyfikacja. |
| `evidence_catalog` | Lokatory dowodów związane z niezmienną rewizją. |
| `hypotheses` | Twierdzenia wymagające dalszego sprawdzenia. |
| `local_project_issues` | Problemy, których rozwiązanie należy do projektu. |
| `methodology_change_candidates` | Kandydaci do clarification, eksperymentu lub CP. |
| `human_authority_decisions` | Podjęte i otwarte decyzje, authority oraz dokładny przedmiot. |
| `validation_status` | Stan dalszej walidacji rekordu i poszczególnych hipotez. |
| `cross_project_confirmation` | Projekty i rewizje potwierdzające albo podważające obserwację. |
| `related_change_proposals` | Stabilne identyfikatory CP i ich bieżące statusy. |
| `outcome` | `accepted`, `rejected`, `deferred` albo `experimental`; nadawany przez właściwą Human Authority. |

`outcome` pozostaje nieprzypisany, dopóki właściwa Human Authority nie zapisze
decyzji. Wynik obserwacji nie oznacza automatycznie wyniku całego rekordu.

### Wymagane pola obserwacji

| Pole | Znaczenie |
| --- | --- |
| `observation_id` | Stabilny identyfikator unikalny w rekordzie. |
| `title` | Krótka nazwa obserwacji. |
| `fact` | Co można bezpośrednio sprawdzić w evidence. |
| `interpretation` | Co fakt może znaczyć dla projektu lub KGAID. |
| `classification` | Jedna klasyfikacja główna i opcjonalne klasyfikacje pomocnicze. |
| `impact` | Wpływ według jawnej skali, np. `low`, `medium`, `high`, `critical`. |
| `confidence` | Pewność wniosku i ewentualne rozdzielenie pewności faktu od skutku. |
| `scope` | Projekt, metodologia, tooling albo relacja między nimi. |
| `recommendation` | Proponowana reakcja; nie jest decyzją. |
| `evidence_refs` | Odwołania do katalogu dowodów. |
| `local_action` | Działanie należące do projektu źródłowego. |
| `methodology_action` | Clarification, eksperyment lub formalny CP. |
| `confirmation` | `single-project`, `confirmed`, `contradicted` albo `cross-project-not-needed`, wraz z referencjami. |
| `related_cp` | Powiązane Change Proposals. |
| `authority_decision` | Identyfikator decyzji albo jawny stan `open`. |
| `outcome` | `accepted`, `rejected`, `deferred` albo `experimental`, wyłącznie po decyzji authority. |

## Klasyfikacja obserwacji

Główna klasyfikacja wskazuje właściciela reakcji:

- `methodology-strength` — dowód, że mechanizm KGAID przyniósł wartość;
- `methodology-application-problem` — problem zastosowania istniejącej zasady;
- `local-project-problem` — problem projektu, który nie uzasadnia sam zmiany
  KGAID;
- `methodology-gap-or-ambiguity` — luka lub niejednoznaczność mogąca wymagać
  clarification albo CP;
- `experiment` — kontrolowana praktyka bez statusu normatywnego;
- `cross-project-hypothesis` — hipoteza wymagająca kolejnego projektu;
- `rejected-for-now` — pomysł bez wystarczającego dowodu, nieusuwany z historii.

Klasyfikacje pomocnicze są dozwolone, gdy obserwacja ujawnia problem lokalny i
jednocześnie niejasność metodyki. Nie wolno przez to przenosić odpowiedzialności
za lokalną naprawę do KGAID.

## Minimalne wymagania dowodowe

Każdy dowód wskazuje:

1. repozytorium albo trwały pakiet dowodowy;
2. niezmienny commit, tag, hash treści lub równoważny identyfikator;
3. ścieżkę lub identyfikator artefaktu;
4. sekcję, anchor, zakres danych albo sprawdzalne twierdzenie;
5. datę dostępu lub analizy, gdy źródło może ulec zmianie;
6. ograniczenie mówiące, czego dowód nie wykazuje.

KGAID przechowuje raport, eksport lub lokator dowodu. Nie kopiuje repozytorium
projektu, nie dodaje go jako submodułu i nie zakłada jego układu katalogów w
modelu.

## Walidacja między projektami

Obserwacja z jednego projektu może:

- uzasadnić lokalną naprawę;
- uzasadnić clarification niesprzeczne z normą;
- rozpocząć eksperyment albo formalny CP;
- potwierdzić brak integralności lub konflikt już istniejących dokumentów.

Nie wystarcza sama do uznania lokalnego typu artefaktu, obowiązkowego review,
profilu albo narzędzia za regułę uniwersalną. Takie twierdzenie wymaga drugiego
projektu o odpowiednio innym kontekście albo jawnej decyzji Human Authority
akceptującej ryzyko ograniczonego evidence.

## Stan walidacji i historia

Zalecane stany dalszej walidacji to `unassessed`, `single-project`,
`awaiting-second-project`, `confirmed`, `contradicted` i `closed`. Zmiana stanu
zapisuje datę, actor, dokładną rewizję evidence i rationale. Nowe evidence nie
nadpisuje wcześniejszego wyniku; dodaje wpis historii i może supersedować
wniosek.

## Role

- projekt źródłowy dostarcza evidence i odpowiada za lokalne naprawy;
- właściciel metodyki utrzymuje ER, wykrywa wzorce i przygotowuje CP;
- reviewer sprawdza lokatory, kompletność i granice wnioskowania;
- Human Authority rozstrzyga wyniki, zmiany normatywne i status projektu
  referencyjnego;
- AI może analizować, wiązać i proponować, lecz nie ustala wyniku ani nie
  potwierdza własnej hipotezy.

## Relacje governance

ER może być wejściem do feedbacku, audytu i CP. Dopiero zaakceptowany CP albo
inna formalna decyzja może uruchomić zmianę dokumentu normatywnego. Następnie
obowiązują zwykłe review, compatibility assessment, baseline i oddzielna
decyzja publikacyjna opisana w
[Governance, Versioning, and Release Model](../50-governance/governance-and-release-model.md).
