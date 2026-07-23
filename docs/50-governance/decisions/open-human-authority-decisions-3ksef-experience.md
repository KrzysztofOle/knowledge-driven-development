---
document_id: KGAID-DEC-001
title: Open Human Authority Decisions for EXP-3KSEF-001

document_type: governance
status: draft
version: 0.1.0

owner: Governance

approval_status: draft
approved_by:
approved_at:
---

# Otwarte decyzje Human Authority po EXP-3KSEF-001

## Status rejestru

Rejestr przedstawia warianty, nie decyzje. Wszystkie pozycje mają stan `open`;
żadna nie zmienia KGAID, `3ksef`, baseline'u, approval ani publikacji.
Materiałem wejściowym są
[EXP-3KSEF-001](../../45-experience/reference-projects/3ksef/EXP-3KSEF-001.md)
i cztery [draft Change Proposals](../change-proposals/README.md).

## HDQ-001 — Publikacja KGAID-0.1.0

**Pytanie:** Czy opublikować `KGAID-0.1.0`, czy nadal traktować je jako
baseline eksperymentalny?

- kontekst: manifest ma `publication_status: prepared-unpublished`, a projekt
  wskazuje nazwę wersji bez opublikowanego, niezmiennego release;
- wariant A: publikacja tagu/release po osobnej kontroli i decyzji;
- wariant B: utrzymanie stanu eksperymentalnego i obowiązkowy pin commit SHA;
- korzyści: A daje stabilną referencję; B zachowuje przestrzeń na rozwiązanie
  konfliktów przed publikacją;
- koszt: A wymaga release controls i późniejszych wersji migracyjnych; B wymaga
  jawnych pinów i utrzymuje ograniczoną komunikowalność;
- ryzyko: A może utrwalić niespójny słownik; B może powodować dalsze
  nieodtwarzalne deklaracje, jeśli projekty nie pinują SHA;
- rekomendacja raportu: do czasu publikacji pinować `dcc9976…` i oznaczać
  baseline jako eksperymentalny; raport nie rozstrzyga terminu publikacji;
- **stan: open — decyzji nie podjęto.**

## HDQ-002 — Osie statusu wiedzy i dokumentu

**Pytanie:** Czy statusy wiedzy i dokumentu mają być dwiema osobnymi osiami?

- kontekst: Knowledge Lifecycle i Metadata Profile używają częściowo różnych
  pojęć; szczegóły analizuje `KGAID-CP-001`;
- wariant A: jedna canonical oś treści;
- wariant B: osobny `knowledge_status` i `document_status`;
- wariant C: jedna oś w Minimal i dwie w Extended;
- korzyści: A upraszcza kontrolę; B zachowuje precyzję; C umożliwia
  proportional rigor;
- koszt: A upraszcza złożone dokumenty; B zwiększa metadata/tooling; C wymaga
  mapowania profili;
- ryzyko: A może zgubić znaczenie artefaktu; B/C mogą mnożyć niespójne statusy;
- rekomendacja raportu: jawnie rozdzielić status wiedzy od technicznego
  approval; nie wskazuje finalnego modelu statusu dokumentu;
- **stan: open — decyzji nie podjęto.**

## HDQ-003 — Rola `approval_status`

**Pytanie:** Jaką rolę ma pełnić `approval_status`?

- kontekst: 130 z 138 zarządzanych artefaktów `3ksef` było `approved`, ale
  tylko 44 `accepted`;
- wariant A: wyłącznie stan kolejki i approval dokładnej rewizji;
- wariant B: projekcja osobnego Human Decision Record;
- wariant C: pole opcjonalne, jeśli projekt zapewnia równoważny record;
- korzyści: A jest proste; B zwiększa audytowalność; C zachowuje neutralność
  narzędziową;
- koszt: A wymaga osobnego lifecycle decision; B wymaga modelu HDR; C utrudnia
  jednolitą automatyczną kontrolę;
- ryzyko: każdy wariant jest błędny, jeśli `approved` automatycznie oznacza
  `accepted`;
- rekomendacja raportu: approval techniczny rewizji i decyzję o statusie wiedzy
  traktować osobno;
- **stan: open — decyzji nie podjęto.**

## HDQ-004 — Zasada `accepted-only`

**Pytanie:** Czy baseline jest `accepted-only`?

- kontekst: normatywne KGAID wiąże baseline z accepted knowledge, lecz pilot
  użył baseline'u obejmującego `captured/proposed`;
- wariant A: bezwzględne `accepted-only`;
- wariant B: domyślne `accepted-only` z wyjątkami per item;
- korzyści: A daje jeden autorytet; B pozwala jawnie zarządzić ograniczonym
  ryzykiem;
- koszt: A może opóźnić baseline; B wymaga modelu wyjątków i walidacji;
- ryzyko: A może zachęcić do przedwczesnego `accepted`; B może normalizować
  obchodzenie lifecycle;
- rekomendacja raportu: accepted-only albo jawne, ograniczone wyjątki; wybór
  pozostawiony authority;
- **stan: open — decyzji nie podjęto.**

## HDQ-005 — Kontrolowane wyjątki członkostwa

**Pytanie:** Czy dopuszczać kontrolowane wyjątki członkostwa baseline'u?

- kontekst: `KGAID-CP-003` proponuje per-item decision, rationale, scope, owner,
  expiry i follow-up;
- wariant A: zakaz wyjątków;
- wariant B: wyjątki ograniczone w czasie i zakresie;
- wariant C: wyjątki tylko w baseline'ach projektu, nie metodologii;
- korzyści: A jest jednoznaczne; B/C umożliwiają świadome przejście przy
  niepełnej wiedzy;
- koszt: A zwiększa koszt wcześniejszej akceptacji; B/C zwiększają kontrolę,
  tooling i review;
- ryzyko: wyjątek bez expiry i decision record staje się drugim źródłem
  autorytetu;
- rekomendacja raportu: jeśli wyjątki będą dozwolone, tylko jawne i per item;
- **stan: open — decyzji nie podjęto.**

## HDQ-006 — Dokładna rewizja Human Decision

**Pytanie:** Czy decyzja Human Authority musi wskazywać dokładną rewizję?

- kontekst: `OBS-008`, `OBS-009` i `OBS-013` pokazują niejednoznaczność
  approval i review po zmianie treści;
- wariant A: pełny commit + path;
- wariant B: content hash;
- wariant C: równoważny immutable subject ID zapewniony przez workflow;
- korzyści: wszystkie warianty umożliwiają odtworzenie decyzji;
- koszt: A zależy od dostępności repo; B wymaga obliczania hashy; C wymaga
  audytowalnego systemu i eksportu;
- ryzyko: identyfikator bez odtwarzalnej treści tworzy approval theater;
- rekomendacja raportu: decyzja powinna być revision-bound i podlegać reapproval
  po zmianie semantycznej;
- **stan: open — decyzji nie podjęto.**

## HDQ-007 — Status projektu 3ksef

**Pytanie:** Czy `3ksef` jest pilotem, kandydatem czy oficjalnym projektem
referencyjnym?

- kontekst: analiza obejmuje tylko warstwy do Contracts i jeden projekt;
- wariant A: pozostaje `pilot`;
- wariant B: `candidate` po ustaleniu kryteriów;
- wariant C: `reference` po formalnej ocenie i decyzji;
- korzyści: A nie rozszerza claims; B tworzy ścieżkę walidacji; C daje publiczny
  case study;
- koszt: A ogranicza użycie promocyjne; B/C wymagają criteria, representative
  increment i utrzymania evidence;
- ryzyko: status `reference` przed Delivery/Verification może sugerować
  potwierdzenie end-to-end;
- rekomendacja raportu: nie ogłaszać pełnej zgodności ani skuteczności przed
  representative increment; bieżący rejestr używa `pilot`;
- **stan: open — decyzji nie podjęto.**

## HDQ-008 — BPS jako eksperyment

**Pytanie:** Czy BPS pozostaje eksperymentem?

- kontekst: BPS wnosi wartość między capability i BR/REQ, ale KGAID już
  klasyfikuje business process jako Domain knowledge;
- wariant A: lokalny Domain Process View;
- wariant B: kandydat nowego standardowego artifact type po drugim projekcie;
- wariant C: odrzucenie osobnego typu i użycie istniejącej kategorii;
- korzyści: A/C ograniczają proliferację; B może ustabilizować powtarzalny
  wzorzec;
- koszt: A wymaga mappingu; B wymaga drugiego przypadku i migracji; C może
  utracić użyteczną reprezentację;
- ryzyko: normatywizacja układu jednego projektu jako reguły uniwersalnej;
- rekomendacja raportu: pozostać przy eksperymencie, przenieść semantyczne
  ownership do Domain i zebrać drugi przypadek;
- **stan: open — decyzji nie podjęto.**

## HDQ-009 — Authority zamykania feedbacku

**Pytanie:** Kto może zamykać feedback po zmianie KGAID?

- kontekst: wpis może dotyczyć projektu, metodologii albo obu repozytoriów;
  `OBS-011` pokazuje historyczne `Open` po zmianie KGAID;
- wariant A: owner projektu;
- wariant B: właściciel metodyki;
- wariant C: obaj dla feedbacku cross-repository, każdy osobno dla własnego
  zakresu;
- korzyści: A/B są proste; C zachowuje rozdzieloną authority;
- koszt: C wymaga koordynacji i dwóch referencji weryfikacyjnych;
- ryzyko: jednostronne zamknięcie może potwierdzić wdrożenie albo rozwiązanie,
  którego druga strona nie zweryfikowała;
- rekomendacja raportu: zapisać `resolved_by`, `verified_at_ref` i jawną decyzję
  closing authority; nie wskazuje finalnego actor;
- **stan: open — decyzji nie podjęto.**

## HDQ-010 — Change Proposals do następnego etapu

**Pytanie:** Które Change Proposals przechodzą do kolejnego etapu?

- kontekst: `KGAID-CP-001`–`004` są odrębnymi draftami opartymi na tym samym
  Experience Record;
- wariant A: skierować wszystkie do Review;
- wariant B: priorytetowo CP-001–003, pozostawiając CP-004 jako eksperyment;
- wariant C: review każdego osobno według ryzyka i dostępnego evidence;
- wariant D: odroczyć wszystkie do representative increment lub drugiego
  projektu;
- korzyści: A utrzymuje tempo; B skupia blokery autoryzacji; C ogranicza
  sprzężenie; D zwiększa evidence;
- koszt: A może przeciążyć review; B/C wymagają priorytetyzacji; D utrzymuje
  znane niejasności;
- ryzyko: łączenie decyzji może niejawnie zaakceptować zależne rozwiązania;
- rekomendacja raportu: statusy, immutable decision i baseline membership są
  blockerami; zmiany core powinny mieć drugi projekt albo jawnie zaakceptowane
  ryzyko;
- **stan: open — decyzji nie podjęto.**

## HDQ-011 — Stan Architecture Baseline 3ksef

**Pytanie:** Czy `AB-001` ma zostać uznany za accepted Architecture Baseline,
czy wymaga nowej decyzji?

- kontekst: frontmatter ma `proposed/approved`, a treść `pending` i pustą
  sekcję Human Authority;
- wariant A: nowa decyzja dla dokładnej rewizji;
- wariant B: odrzucenie obecnego baseline'u i przygotowanie następcy;
- korzyści: oba warianty usuwają niejednoznaczność;
- koszt: lokalny rework statusów, katalogów i zależnych odwołań;
- ryzyko: retroaktywne uznanie bez subject ref stworzy fikcyjny ślad decyzji;
- rekomendacja raportu: jedna jawna decyzja exact revision i spójny zapis;
- **stan: open — decyzji nie podjęto; naprawa jest poza zakresem.**

## HDQ-012 — Profil adoption 3ksef

**Pytanie:** Czy dla `3ksef` przyjąć profil Extended?

- kontekst: zakres finansowy, podatkowy, multi-company i KSeF ma wysoki skutek,
  a projekt de facto stosuje wysoki rygor bez deklaracji;
- wariant A: Extended z tailoringiem;
- wariant B: udokumentowany hybrid;
- wariant C: Minimal z jawnym uzasadnieniem odstępstw;
- korzyści: jawny profil pozwala ocenić koszt i conformance;
- koszt: mapping artefaktów, mandatory set i tailoring decisions;
- ryzyko: profil bez decyzji utrudnia ocenę nadmiaru i braków;
- rekomendacja raportu: Extended z tailoringiem dla PI-1;
- **stan: open — decyzji nie podjęto; zmiana 3ksef jest poza zakresem.**

## HDQ-013 — Granice rodzajów review

**Pytanie:** Czy Product Review i Architecture Readiness Review mają być
osobne?

- kontekst: review pokrywały część tych samych pytań, a ARR-001/002 wymagały
  analizy 14 różnic;
- wariant A: osobne review z różnym subject, authority i outcome;
- wariant B: jeden Review Record z profilami pytań;
- wariant C: jedna cross-layer checklist i osobna decyzja baseline;
- korzyści: A zachowuje specjalizację; B/C ograniczają duplikację;
- koszt: A zwiększa liczbę artefaktów; B/C wymagają migracji praktyki;
- ryzyko: niejasne precedence może ponownie dać sprzeczne readiness claims;
- rekomendacja raportu: zdefiniować review contract i nie tworzyć obowiązkowo
  osobnego review dla każdej warstwy;
- **stan: open — decyzji nie podjęto.**

## HDQ-014 — Pilot Approval Center

**Pytanie:** Czy pilotować Stage 2 Approval Center na jednym baseline'ie
`3ksef`?

- kontekst: potrzebny jest revision-bound record, lecz rozwiązanie ma pozostać
  tool-neutral;
- wariant A: pilot narzędzia na jednym baseline;
- wariant B: pilot ręcznego HDR bez Approval Center;
- wariant C: odroczenie do decyzji CP-002/003;
- korzyści: A/B dostarczają evidence praktycznego; C unika implementacji przed
  modelem;
- koszt: A wymaga tooling i migracji; B ręcznej kontroli; C opóźnia evidence;
- ryzyko: pilot narzędzia może zostać błędnie uznany za normę;
- rekomendacja raportu: ewentualny pilot ograniczyć do jednego baseline'u i
  reapproval po kontrolowanej zmianie;
- **stan: open — decyzji nie podjęto; pilot jest poza zakresem.**

## HDQ-015 — Representative increment

**Pytanie:** Który mały increment ma posłużyć do pierwszej oceny
Delivery/Verification end-to-end?

- kontekst: obecny evidence kończy się na Contracts;
- warianty: wybrać ograniczony przepływ o wysokiej traceability albo odroczyć
  ocenę do naturalnego incrementu projektu;
- korzyści: uzyskanie evidence implementacji, testów i baseline;
- koszt: implementacja, testy, review i utrzymanie pełnego łańcucha;
- ryzyko: niereprezentatywny slice może dać mylący claim skuteczności;
- rekomendacja raportu: jeden representative increment przed deklaracją
  pełnej skuteczności;
- **stan: open — decyzji nie podjęto; wykonanie jest poza zakresem.**

## HDQ-016 — Poziom niezależności evidence

**Pytanie:** Które ryzyka wymagają V2/V3: permission isolation, audit,
reconciliation, idempotency czy wszystkie?

- kontekst: ryzyka wykryto przed kodem, ale nie ma evidence skuteczności
  kontroli;
- wariant A: V2/V3 dla wszystkich czterech;
- wariant B: poziom według consequence i reversibility każdego claim;
- wariant C: etapowanie poziomu wraz z dojrzałością incrementu;
- korzyści: A maksymalizuje niezależność; B/C proporcjonalność kosztu;
- koszt: niezależny reviewer, środowisko i powtarzalne evidence;
- ryzyko: zbyt niski poziom dla izolacji lub audytu może nie wspierać claim;
- rekomendacja raportu: authority powinna jawnie wskazać ryzyka wymagające
  V2/V3; raport nie wybiera zestawu;
- **stan: open — decyzji nie podjęto; weryfikacja jest poza zakresem.**

## Zapis przyszłej decyzji

Każde rozstrzygnięcie powinno otrzymać osobny stabilny identyfikator, dokładny
`subject_ref`, approvera, czas, scope, rationale, outcome i relację
supersession. Aktualizacja tego rejestru nie może zastąpić decision record.
