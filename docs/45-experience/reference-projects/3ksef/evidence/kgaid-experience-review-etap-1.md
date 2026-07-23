---
document_id: EVD-3KSEF-001
title: KGAID Experience Review Etap 1

document_type: verification
status: draft
version: 0.1.0

owner: Quality

approval_status: draft
approved_by:
approved_at:
---

# KGAID Experience Review — etap 1

**Projekt referencyjny:** `KrzysztofOle/3ksef`
**Metodyka:** `KrzysztofOle/kgaid-methodology`
**Data analizy:** 2026-07-23
**Charakter pracy:** analiza wyłącznie do odczytu; bez zmian w repozytoriach
**Referencja 3ksef:** branch `agent/project-structure`, commit [`133817601f597a8b73902c411f3c547e82e54f91`](https://github.com/KrzysztofOle/3ksef/commit/133817601f597a8b73902c411f3c547e82e54f91)
**Referencja KGAID:** branch `main`, commit [`dcc9976ba523120e319cfa1f5fb4460a74a38e99`](https://github.com/KrzysztofOle/kgaid-methodology/commit/dcc9976ba523120e319cfa1f5fb4460a74a38e99)

> Ten dokument nie jest oceną jakości produktu 3ksef ani formalnym audytem zgodności. Jest przeglądem doświadczeń z pierwszego intensywnego użycia KGAID: co zadziałało, gdzie zastosowanie metodyki ujawniło niejednoznaczności, co jest problemem lokalnym projektu, a co może uzasadniać zmianę KGAID.

## 1. Executive Summary

3ksef jest wartościowym pierwszym projektem referencyjnym KGAID, ponieważ zastosował metodykę nie dekoracyjnie, lecz jako rzeczywisty system pracy: rozdzielił role Human–ChatGPT–Codex, zbudował warstwy Product → Domain → Requirements → Architecture → Contracts, wykonywał review i wracał do artefaktów wcześniejszych warstw po odkryciu braków. Historia commitów pokazuje iteracyjność zgodną z założeniem KGAID, a nie sztywny waterfall.

Najsilniejszy pozytywny wynik to działanie pętli wiedzy i review. Przeglądy produktu i architektury wykrywały konkretne braki, m.in. niepełne pokrycie capabilities, brakujące quality attributes, problemy z granicą KSeF 2.0 oraz niepełne kontrakty. Następnie artefakty były poprawiane. Eksperyment z curation workflow w 3ksef został też szybko uogólniony do propozycji w repozytorium metodyki.

Największe ryzyko nie dotyczy treści domenowej, lecz semantyki autoryzacji:

- projekt ma 138 artefaktów zarządzanych metadanymi, z czego 130 ma `approval_status: approved`, ale tylko 44 mają `status: accepted`;
- Product Baseline i Architecture Baseline próbują nadać autorytet kolekcji artefaktów, z których wiele pozostaje `captured`, `proposed` albo `reviewed`;
- lokalne rozstrzygnięcie, że baseline jako całość autoryzuje elementy niezależnie od ich statusu, jest sprzeczne z normatywną zasadą KGAID, według której baseline wiąże zaakceptowaną wiedzę;
- Architecture Baseline ma `proposed/approved` we frontmatter, ale w treści nadal informuje o oczekiwaniu na decyzję i zawiera niewypełnioną sekcję Human Authority;
- kontrakty używają fenced YAML zamiast frontmatter oraz `business-contract` zamiast lokalnego typu `contract`, przez co pozostają poza mechanizmem governance i approval.

Drugie źródło ryzyka leży po stronie samej metodyki. KGAID 0.1.0 jest oznaczony jako `prepared-unpublished`, a 3ksef odwołuje się jedynie do nazwy `KGAID-0.1.0`, bez niezmiennego taga lub SHA. Ponadto normatywny lifecycle używa statusów `captured/proposed/reviewed/accepted/superseded/retired/rejected`, podczas gdy Metadata Profile i projekt Approval Center operują częściowo innym słownikiem (`draft`, `deprecated`). To utrudnia poprawne wdrożenie dwóch niezależnych osi: dojrzałości wiedzy i technicznego approval.

3ksef dostarcza mocnych dowodów na użyteczność:

- Product Vision, Capability Map, BR, Requirements i Architecture Specification;
- review jako mechanizm odkrywania braków i uruchamiania rework;
- Human Authority i separacja prawa do publikacji;
- Contract Coverage Review jako uczciwy pomiar brakującego pokrycia;
- Knowledge Staging i rozdzielenie sources/evidence/facts.

3ksef dostarcza też dowodów na koszt:

- 180 aktualnych dokumentów Markdown, w tym 138 zarządzanych artefaktów, wytworzonych w bardzo krótkim czasie;
- liczne powtórzenia statusów, zakresu i traceability w metadanych, treści, katalogach, review i baseline’ach;
- sprzeczne lub szybko starzejące się dokumenty pomocnicze;
- koszt ręcznego utrzymania linków, macierzy i statusów.

**Wniosek:** KGAID działa jako model porządkowania wiedzy i kontroli decyzji, lecz pierwsze użycie ujawniło pilną potrzebę doprecyzowania baseline’ów, statusów, approval związanego z dokładną rewizją oraz granic review. Nie ma jeszcze podstaw do uogólniania skuteczności metodyki na implementację, weryfikację i operacje, ponieważ te warstwy w 3ksef są nadal placeholderami.

## 2. Zakres i metoda

### 2.1 Zakres

Analiza objęła:

- pełną historię 79 commitów aktualnej gałęzi 3ksef;
- strukturalny przegląd 180 aktualnych plików Markdown 3ksef;
- agregację metadanych 138 zarządzanych artefaktów;
- pogłębioną analizę 38 reprezentatywnych dokumentów 3ksef;
- analizę 23 plików KGAID, w tym 14 dokumentów normatywnych baseline’u 0.1.0, manifestu, governance, Metadata Profile, curation workflow i projektu Approval Center;
- warstwy Governance, Product, Domain, Requirements, Architecture, ADR, Contracts, Knowledge, Delivery, Verification i Operations;
- role Human Authority, ChatGPT i Codex, traceability, statusy, approval, review, baseline’y, bezpieczeństwo oraz koszt dokumentacyjny.

### 2.2 Metoda

Zastosowano pięć kroków:

1. Ustalono dokładne referencje obu repozytoriów oraz lokalne instrukcje `AGENTS.md`.
2. Zrekonstruowano chronologię na podstawie commitów i kolejnych stanów kluczowych dokumentów.
3. Porównano stan projektu z zasadami, lifecycle, process model, authority model, evidence model i adoption model KGAID.
4. Oddzielono:
   - **fakt** — bezpośrednio widoczny w repozytorium;
   - **obserwację** — wzorzec wynikający z jednego lub wielu faktów;
   - **interpretację** — znaczenie dla skuteczności KGAID;
   - **propozycję** — możliwą reakcję, jeszcze niezaakceptowaną;
   - **decyzję potrzebną** — pytanie pozostawione Human Authority.
5. Każdej obserwacji nadano wpływ, pewność, zakres oraz rekomendację.

### 2.3 Ograniczenia

- Analiza obejmuje stan repozytoriów na wskazanych commitach, nie rozmowy poza repozytoriami.
- Git nie dowodzi, kto faktycznie wykonał każdy krok poznawczy; role oceniono na podstawie instrukcji i zapisów w artefaktach.
- Nie wykonywano aplikacji, testów ani narzędzi projektu. 3ksef pozostaje projektem dokumentacyjno-architektonicznym przed implementacją.
- Nie oceniano merytorycznej zgodności z aktualnym prawem podatkowym lub KSeF.
- Jedno intensywne użycie metodyki nie wystarcza do uznania lokalnego rozwiązania za zasadę uniwersalną.

## 3. Rekonstrukcja osi czasu projektu

| Okres | Faktyczne działania | Oczekiwany model KGAID | Ocena |
|---|---|---|---|
| 2026-07-17 | Struktura repozytorium, instrukcje współpracy, rozdzielenie Human–ChatGPT–Codex. | PM1 Orient; ustalenie authority, scope i sposobu pracy. | Zgodne i wykonane wcześnie. |
| 2026-07-18 | Struktura dokumentacji KGAID, pierwsze artefakty Product, ADR i governance. | PM2 Product przed szczegółowym designem. | Zasadniczo zgodne. ADR pojawił się bardzo wcześnie, ale nie zdominował produktu. |
| 2026-07-19 rano | Domain Model, Requirement Model, Business Rules i pierwsze wymagania. | PM3 Domain, następnie PM4 Requirements. | Kolejność semantyczna zachowana. |
| 2026-07-19 później | Feedback do KGAID, Knowledge Staging, PI-1, BPS, dalsze requirements, Product Review i Architecture Readiness Review. | Iteracje i powroty między PM2–PM4 są dozwolone; review ma ujawnić braki. | Wysoka wartość, ale szybka proliferacja artefaktów i nakładanie się rodzajów review. |
| 2026-07-20 | Ujednolicanie metadanych, approval, System Workflow, ARR-001/002, neutralne GOV-005, ARR-003 i Product Baseline. | Human decision → accepted knowledge → baseline. | Treściowo silne, semantycznie problematyczne: baseline autoryzuje elementy o statusach niższych niż `accepted`. |
| 2026-07-21 rano | Curation źródeł; równoległe uogólnienie workflow w KGAID; rozszerzenie Product o PDF i accounting. | Knowledge coevolves; powrót do wcześniejszych warstw po zmianie zakresu. | Bardzo dobry dowód pętli uczenia. Nowy zakres wymusił ponowne przejście Product/Domain/Requirements. |
| 2026-07-21 południe | Architecture Vision, Architecture Specification, QA, Traceability Matrix i Architecture Review. Review przechodzi z `Not Ready` do `Ready` po poprawkach. | PM5 Architecture; readiness zależne od zakresu i dowodów. | KGAID działa jako mechanizm kontroli jakości. Sposób wersjonowania samego review wymaga poprawy. |
| 2026-07-21 popołudnie | Architecture Baseline i techniczny approval. | Human decision, accepted knowledge, następnie baseline. | Approval został zapisany, lecz status i treść baseline’u pozostają sprzeczne. |
| 2026-07-21 wieczór | Contract Foundation, CTR-001–004, Contract Coverage Review i Contracts Boundary Review. | PM6 Contracts po ustabilizowaniu architektury. | Kolejność właściwa; review uczciwie wykazał 7 brakujących kontraktów. Metadane kontraktów pozostają poza governance. |
| Stan końcowy | Delivery, Verification i Operations zawierają głównie README/placeholdery. | PM7–PM9 dopiero po wiedzy, architekturze i kontraktach. | Brak naruszenia kolejności, ale brak jeszcze dowodu skuteczności KGAID w implementacji i eksploatacji. |

### 3.1 Wniosek o sekwencji

Faktyczny przebieg nie był liniowy, ale zachował zależności semantyczne. Najważniejsze powroty:

- Requirements → Product/Business Processes po odkryciu brakującego modelu procesu;
- Product Baseline → Product/Domain/Requirements po rozszerzeniu zakresu o PDF i accounting;
- Architecture Review → Architecture po wykryciu braków QA, traceability i granicy KSeF 2.0;
- Contracts Review → przyszłe Contracts po pomiarze niepełnego pokrycia.

To jest zgodne z KGAID, który traktuje numerację jako zależności, a nie obowiązkowy waterfall. Problemem nie są powroty, lecz niejednoznaczne utrwalanie ich rezultatów w statusach, baseline’ach i review.

## 4. Macierz zgodności

Legenda: **silna** — dowody spójnego zastosowania; **częściowa** — działa, lecz z istotnym brakiem; **niezgodna** — praktyka przeczy zasadzie normatywnej; **brak dowodu** — warstwa jeszcze nie została rzeczywiście użyta.

| Obszar | Ocena | Dowód i uzasadnienie |
|---|---|---|
| Scope i boundaries | Częściowa | Zakres PI-1 jest jawny, ale adoption nie wskazuje wybranego profilu Minimal/Extended ani niezmiennego punktu baseline’u KGAID. |
| Product Vision | Silna | Vision, Value Proposition, Capability Map i PI-1 budują kontekst przed architekturą. |
| Capability Map | Silna | Capabilities są stabilnymi kotwicami traceability; review wykazał jednak wcześniejsze braki BR/REQ dla części CAP. |
| Business Processes | Częściowa | BPS rozwiązuje realną potrzebę opisu procesu, ale jest umieszczony w Product, podczas gdy KGAID klasyfikuje business processes jako Domain knowledge. |
| Domain | Częściowa | Model domeny i glossary są użyteczne; przeniesienie Domain Map do Architecture pozostawiło stare odwołania i niejasne ownership. |
| Business Rules | Silna | BR mają jawny sens, zakres, rationale i powiązania z wymaganiami. |
| Requirements i QR | Silna | Wymagania zawierają kryteria akceptacji i traceability. Lokalny Requirement Model używa jednak częściowo innego lifecycle. |
| Architecture | Silna treściowo / częściowa proceduralnie | Architektura wynika z upstream i została poprawiona po review; statusy baseline’u nie odzwierciedlają jednoznacznej decyzji. |
| ADR | Częściowa | Istnieje ADR i proces klasyfikacji. Architecture Review początkowo wskazał 14 kandydatów, później 0, co ujawnia potrzebę lepszych kryteriów zastosowania. |
| Contracts | Częściowa | CTR-001–004 są konkretne i traceable; review mierzy pokrycie. Metadane i typ dokumentu omijają jednak governance. |
| Traceability | Częściowa | Łańcuchy CAP/BP/BR/REQ/QR/ARC/CTR są bogate, ale w większości ręczne, powielone i słabo maszynowo weryfikowalne. |
| Review | Silna funkcjonalnie / częściowa modelowo | Review prowadzi do zmian, ale Product Review, ARR i baseline readiness nakładają się; review bywa mutowany w miejscu. |
| Status wiedzy | Niezgodna w baseline’ach | Większość zatwierdzonych technicznie artefaktów nie ma statusu `accepted`; baseline lokalnie obchodzi ten warunek. |
| Approval | Częściowa | Osobna oś istnieje i narzędzie zapisuje approver/date, ale approval nie jest jasno związany z dokładną rewizją ani pełnym Human Decision Record. |
| Baseline | Niezgodna / niejednoznaczna | Product Baseline obejmuje `captured/proposed`; Architecture Baseline jest `proposed/approved` i ma sprzeczną treść. |
| Human Authority | Silna intencja / częściowy zapis | Role i ograniczenia są jawne, push wymaga osobnej zgody. Nie każda decyzja ma kompletny, spójny zapis. |
| Human–ChatGPT–Codex | Silna | Instrukcje dobrze rozdzielają framing, review, execution i decyzję. |
| Knowledge curation | Silna jako eksperyment | Źródła zachowano, oddzielono incoming/processed, a wynik uogólniono w propozycji KGAID. Brak jeszcze normatywnego baseline’u. |
| Security i compliance | Częściowa, obiecująca | Wcześnie wykryto multi-company isolation, permissions, audit, idempotency, retry i ambiguity; brak implementacyjnego evidence. |
| Delivery | Brak dowodu | Warstwa jest placeholderem. |
| Verification | Brak dowodu | Istnieją dokumenty review, ale nie ma jeszcze evidence z implementacji i testów systemu. |
| Operations | Brak dowodu | Warstwa jest placeholderem. |
| Adoption model | Częściowa | Jest mapping ról i lokalnych artefaktów, lecz brakuje immutable pin, jawnego profilu, formalnych tailoring decisions i pełnego conformance record. |

### 4.1 Ocena ważnych artefaktów

| Artefakt / rodzina | Cel i moment powstania | Wartość | Zależności i ryzyko duplikacji | Akceptowalność i weryfikowalność | Rekomendacja |
|---|---|---|---|---|---|
| Vision / Value Proposition / Capability Map | Ramy produktu przed Domain i Architecture. | Wysoka; stabilne kotwice decyzji. | Część zakresu powtarza się w PI-1 i System Workflow. | Czytelne dla Human i ChatGPT; traceability możliwa dla Codex. | Utrzymać; ograniczyć powtórzenia opisowe. |
| Product Increment PI-1 | Wyznaczenie pierwszego outcome i zakresu. | Wysoka. | Rozszerzenie o PDF/accounting uruchomiło prawidłowy rework. | Dobra dla Human Authority, o ile baseline jasno wiąże rewizję. | Utrzymać; każdą zmianę zakresu wiązać z impact review. |
| BPS / Business Process Model | Uzupełnienie ścieżki CAP → BR/REQ o przebieg biznesowy. | Wysoka lokalnie. | Nakłada się na PI-1, System Workflow i Domain; obecnie ownership Product. | Dobre dla Human/ChatGPT, częściowo maszynowe dla Codex. | Kontynuować jako eksperyment; najpierw zmapować do Domain knowledge. |
| Business Rules | Oddzielenie trwałych reguł od wymagań systemu. | Wysoka. | Niskie ryzyko duplikacji, jeśli REQ odwołuje się do BR zamiast kopiować. | Dobra sprawdzalność. | Utrzymać jako standardową praktykę. |
| Requirements / QR | Testowalne obowiązki systemu. | Wysoka. | Manualne tabele pokrycia zwiększają koszt. | Dobre kryteria akceptacji; lifecycle modelu wymaga ujednolicenia. | Utrzymać; generować zestawienia z metadanych. |
| Domain Model / Glossary | Wspólny język i reguły domeny. | Wysoka. | Business Domain Map pod Architecture i usunięta ścieżka w Domain osłabiają single ownership. | Czytelne, ale broken links obniżają wiarygodność. | Przywrócić jedno ownership mapy domeny i naprawić referencje w etapie 2 projektu, nie w tym przeglądzie. |
| Architecture Specification i katalogi ARC | Struktura systemu po ustabilizowaniu upstream. | Wysoka. | Część treści powtarza Architecture Vision, Responsibility Matrix i review. | Review wykazał realne braki i doprowadził do poprawy. | Zachować jeden dokument nadrzędny; supporting views traktować jako projekcje. |
| ADR | Utrwalanie decyzji o istotnych alternatywach i konsekwencjach. | Umiarkowana na obecnym etapie. | Ryzyko nadużycia do decyzji implementacyjnych małego zasięgu. | Klasyfikacja kandydatów okazała się niepewna. | Doprecyzować kryteria, nie zwiększać liczby ADR mechanicznie. |
| Product Review / ARR / Architecture Review | Niezależne sprawdzenie readiness i spójności. | Bardzo wysoka funkcjonalnie. | Product Review i ARR częściowo pytają o to samo; kolejne ARR dały sprzeczne wyniki. | Działają, gdy mają zamrożony zakres i dokładną rewizję. | Ujednolicić pytania, wejścia, authority i wynik; nie tworzyć domyślnie osobnego review dla każdej warstwy. |
| Product / Architecture Baseline | Zamrożenie autorytatywnej kolekcji. | Potencjalnie bardzo wysoka. | Powtarza listy i statusy; obecnie rozchodzi się z lifecycle elementów. | Niska, dopóki nie wiąże accepted items, SHA/wersji i decyzji. | Formalna korekta modelu baseline/approval. |
| Contract Foundation / CTR | Observable obligations na granicach. | Wysoka. | Katalog i review dobrze wykazują luki; fenced metadata wyłącza je z governance. | Treść CTR jest sprawdzalna; lifecycle nie. | Naprawić lokalny format i typ; nie zmieniać semantyki kontraktów bez potrzeby. |
| Contract Coverage Review | Pomiar odpowiedzialności publicznych bez kontraktów. | Wysoka jako instrument diagnostyczny. | Może stać się automatyczną projekcją z katalogu. | Wynik 4/11 jest jasny i uczciwy. | Utrzymać, ale nie ustanawiać zasady „jeden moduł = jeden kontrakt”. |
| Knowledge Staging / Curated Knowledge | Oddzielenie źródeł, evidence i faktów. | Wysoka jako eksperyment. | Ryzyko używania `proposed/approved` wiedzy jak normatywnej. | Dobre provenance i daty review; niejasny moment wejścia do baseline’u. | Kontynuować z `derived_from`, expiry/review date i jawnym przejściem do accepted knowledge. |
| KGAID Feedback | Zapis gapów i eksperymentów. | Wysoka w chwili utworzenia. | Cztery otwarte gapy są dziś nieaktualne lub już pokryte przez KGAID. | Słaba bez mechanizmu zamykania i powiązania z rewizją metodyki. | Dodać lifecycle feedbacku i dowód rozwiązania. |
| Delivery / Verification / Operations | Realizacja, evidence i uczenie operacyjne. | Jeszcze nieoceniona. | Brak. | Brak dowodu. | Nie deklarować pełnej zgodności ani skuteczności KGAID przed representative increment. |

## 5. Katalog obserwacji

### OBS-001 — Zależności semantyczne są stosowane w praktyce

- **Obszar:** process model, Product → Contracts
- **Fakt:** Vision/Capabilities powstały przed Architecture, a Contracts po Architecture Baseline; po zmianach zakresu projekt wracał do wcześniejszych warstw.
- **Obserwacja:** projekt zachował zależności KGAID mimo nieliniowej historii.
- **Interpretacja:** numerowane warstwy nie wymusiły waterfall; działały jako mapa zależności.
- **Typ:** strength
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** project + methodology validation
- **Rekomendacja:** użyć tej historii jako przykładu referencyjnego w materiałach adoption.
- **Koszt/ryzyko:** niski koszt; ryzyko nadmiernego uogólnienia z jednego projektu.
- **Human Authority:** zgoda na użycie 3ksef jako publicznego lub wewnętrznego case study.

### OBS-002 — Model Human–ChatGPT–Codex i separacja publikacji działają

- **Obszar:** authority, collaboration
- **Fakt:** instrukcje przypisują Human decyzję, ChatGPT framing/review, Codex bounded execution; push, tag, release i PR wymagają osobnej zgody.
- **Obserwacja:** granice odpowiedzialności są bardziej jawne niż w typowym workflow repozytorium.
- **Interpretacja:** KGAID skutecznie ogranicza niekontrolowane rozszerzenie uprawnień AI.
- **Typ:** strength
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** project + methodology validation
- **Rekomendacja:** zachować model; rozszerzyć zapis Human Decision o dokładną rewizję.
- **Koszt/ryzyko:** niewielki narzut; ryzyko „approval theater”, jeśli decyzja nie wskazuje treści.
- **Human Authority:** określić minimalny zapis decyzji wystarczający dla projektu.

### OBS-003 — Review wykrywają realne błędy i uruchamiają rework

- **Obszar:** review, evidence
- **Fakt:** ARR i Architecture Review wskazały brakujące pokrycie, QA, traceability, granicę KSeF 2.0 i kandydatów ADR; kolejne commity poprawiły artefakty.
- **Obserwacja:** review nie są wyłącznie ceremonialne.
- **Interpretacja:** to najsilniejszy dowód skuteczności KGAID na obecnym etapie.
- **Typ:** strength
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** project + methodology validation
- **Rekomendacja:** utrzymać review oparte na pytaniach i evidence; zamrażać każdą instancję review.
- **Koszt/ryzyko:** średni koszt; opłacalny przy wysokim ryzyku domenowym.
- **Human Authority:** ustalić, które review są obowiązkowe dla wybranego profilu.

### OBS-004 — Curation workflow jest udanym eksperymentem transferu wiedzy

- **Obszar:** knowledge lifecycle
- **Fakt:** 3ksef wdrożył incoming/processed, zachowanie źródeł i kurację; kilka minut później w KGAID pojawiła się uogólniona propozycja workflow.
- **Obserwacja:** istnieje namacalna pętla projekt → metodologia.
- **Interpretacja:** KGAID może ewoluować empirycznie, o ile propozycja nie jest mylona z normą.
- **Typ:** strength / experiment
- **Wpływ:** medium
- **Pewność:** high
- **Zakres:** cross-repository
- **Rekomendacja:** w etapie 2 zarejestrować to jako experience record z hipotezą i ograniczeniami.
- **Koszt/ryzyko:** niski; ryzyko zbyt szybkiej normatywizacji.
- **Human Authority:** zdecydować, czy workflow pozostaje proposed do drugiego projektu.

### OBS-005 — 3ksef nie jest przypięty do niezmiennego baseline’u KGAID

- **Obszar:** adoption, baseline identity
- **Fakt:** projekt deklaruje `KGAID-0.1.0`; repo metodyki oznacza baseline jako `prepared-unpublished`, bez opublikowanego taga/release.
- **Obserwacja:** nazwa wersji nie identyfikuje niezmiennej treści.
- **Interpretacja:** późniejsza zmiana `main` może zmienić znaczenie deklarowanej zgodności projektu.
- **Typ:** methodology gap / adoption gap
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** cross-repository
- **Rekomendacja:** do czasu publikacji pinować commit SHA i jawnie oznaczać baseline jako eksperymentalny; po publikacji używać taga i manifestu.
- **Koszt/ryzyko:** niski koszt; wysokie ryzyko nieodtwarzalności bez korekty.
- **Human Authority:** opublikować 0.1.0 czy utrzymać stan eksperymentalny i pin SHA?

### OBS-006 — Approval jest powszechnie utożsamiany z akceptacją wiedzy

- **Obszar:** lifecycle, approval
- **Fakt:** spośród 138 zarządzanych artefaktów 130 ma approval `approved`, ale tylko 44 status `accepted`; 75 to `proposed`, 14 `captured`.
- **Obserwacja:** techniczny approval nie prowadzi konsekwentnie do Human lifecycle decision.
- **Interpretacja:** dwie niezależne osie są formalnie obecne, lecz ich znaczenie nie jest operacyjnie zrozumiałe.
- **Typ:** weakness / methodology ambiguity
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** project + methodology
- **Rekomendacja:** zdefiniować osobno „approval techniczny rewizji” i „decision zmieniający status wiedzy”; narzędzie nie powinno pozostawiać projektu w stanie pozornie zaakceptowanym.
- **Koszt/ryzyko:** średni koszt migracji; wysokie ryzyko błędnego autorytetu.
- **Human Authority:** czy `approved` ma tylko potwierdzać review, czy także autoryzować przejście do `accepted` poprzez osobną decyzję?

### OBS-007 — Product Baseline autoryzuje elementy niezaakceptowane

- **Obszar:** Product Baseline
- **Fakt:** GOV-004 i ARR-003 uznają baseline jako całość za autorytatywny mimo `captured/proposed` statusów części członków.
- **Obserwacja:** lokalny workaround obchodzi lifecycle członków baseline’u.
- **Interpretacja:** przeczy zasadzie KGAID, że baseline wiąże accepted knowledge, i tworzy dwa źródła autorytetu.
- **Typ:** project problem exposing methodology ambiguity
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** project + methodology
- **Rekomendacja:** baseline powinien obejmować accepted items albo jawne, per-item exceptions z zakresem, powodem, authority i datą wygaśnięcia.
- **Koszt/ryzyko:** średni; może wymagać ponownej decyzji dla wielu artefaktów.
- **Human Authority:** wybrać ścisły model accepted-only albo kontrolowane exceptions.

### OBS-008 — Architecture Baseline zawiera sprzeczny zapis decyzji

- **Obszar:** Architecture Baseline, Human Authority
- **Fakt:** frontmatter AB-001 ma `status: proposed` i `approval_status: approved`, podczas gdy treść nadal mówi `pending` i zawiera niewypełnioną sekcję decyzji.
- **Obserwacja:** narzędzie zmieniło pola techniczne, lecz nie doprowadziło dokumentu do spójnego stanu semantycznego.
- **Interpretacja:** nie można jednoznacznie stwierdzić, czy architektura została zaakceptowana jako wiedza.
- **Typ:** 3ksef-specific problem
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** project
- **Rekomendacja:** w etapie naprawczym projektu wykonać jedną jawną decyzję z exact revision i ujednolicić status, approval, treść oraz zależne katalogi.
- **Koszt/ryzyko:** niski koszt; wysokie ryzyko downstream ambiguity.
- **Human Authority:** potwierdzić lub odrzucić AB-001 jako accepted baseline.

### OBS-009 — Approval nie jest wystarczająco związany z dokładną rewizją

- **Obszar:** approval tooling
- **Fakt:** lokalny workflow aktualizuje kilka pól metadanych; projekt Approval Center dopiero proponuje content/revision identity, reapproval i supersession.
- **Obserwacja:** po merytorycznej zmianie artefaktu nie ma silnego dowodu, że wcześniejszy approval dotyczył nadal tej samej treści.
- **Interpretacja:** obecna praktyka nie spełnia w pełni wymogu traceable Human decision.
- **Typ:** methodology gap
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** methodology + tooling
- **Rekomendacja:** formalny Change Proposal dla revision-bound decisions, reapproval trigger i decision record.
- **Koszt/ryzyko:** średni/wysoki koszt narzędziowy; wysoka wartość kontrolna.
- **Human Authority:** zatwierdzić Stage 2 pilota Approval Center w 3ksef?

### OBS-010 — Kontrakty pozostają poza lokalnym governance

- **Obszar:** Contracts
- **Fakt:** dokumenty CTR używają fenced YAML zamiast YAML frontmatter, a template typu `business-contract`, którego nie ma w lokalnym słowniku `document_type`.
- **Obserwacja:** walidacja metadanych i approval nie widzą kluczowych artefaktów Contracts.
- **Interpretacja:** treść kontraktów jest mocna, lecz ich lifecycle jest nieweryfikowalny.
- **Typ:** 3ksef-specific problem
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** project
- **Rekomendacja:** ujednolicić typ i prawdziwy frontmatter; włączyć CTR do tego samego lifecycle co pozostałe artefakty.
- **Koszt/ryzyko:** niski/średni; brak korekty zablokuje wiarygodny Contracts Baseline.
- **Human Authority:** wybrać lokalny typ `contract` albo formalnie rozszerzyć słownik o `business-contract`.

### OBS-011 — Rejestr feedbacku nie ma skutecznego lifecycle

- **Obszar:** methodology feedback
- **Fakt:** GAP-001–004 nadal są `Open`, chociaż aktualny KGAID zawiera Business Rules, lifecycle, Human Authority i statusy.
- **Obserwacja:** feedback nie jest zamykany na podstawie rewizji metodyki.
- **Interpretacja:** projekt może podejmować decyzje na podstawie nieaktualnych gapów.
- **Typ:** 3ksef-specific problem exposing process gap
- **Wpływ:** medium
- **Pewność:** high
- **Zakres:** cross-repository
- **Rekomendacja:** dodać statusy feedbacku, `resolved_by`, `verified_at_ref` i decyzję o zamknięciu.
- **Koszt/ryzyko:** niski.
- **Human Authority:** wskazać, kto może zamknąć gap: właściciel projektu, metodyki czy obaj.

### OBS-012 — Rodzaje review nakładają się i potrafią dać sprzeczne wyniki

- **Obszar:** Product Review, Architecture Readiness Review
- **Fakt:** ARR-001 i ARR-002 dały odmienne obrazy readiness; GOV-005 musiał porównać 14 różnic, a ARR-003 zastąpił oba. Product Review obejmował część tych samych pytań.
- **Obserwacja:** nie było wystarczająco jasne, które review ocenia treść, które readiness do kolejnej warstwy, a które baseline.
- **Interpretacja:** KGAID dobrze wymusza review, ale słabiej definiuje ich granice i precedence.
- **Typ:** methodology ambiguity
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** project + methodology
- **Rekomendacja:** zdefiniować review contract: subject, exact ref, questions, evidence, authority, result, expiry i relację do baseline’u.
- **Koszt/ryzyko:** średni; redukuje powielanie.
- **Human Authority:** zdecydować, czy Product Review i ARR mają pozostać osobne.

### OBS-013 — Jedno review było mutowane od „Not Ready” do „Ready”

- **Obszar:** review history
- **Fakt:** Architecture Review v1.0 wskazywał `Not Ready`; po poprawkach ten sam plik przeszedł przez v1.1 do v1.2 `Ready`.
- **Obserwacja:** ślad jest dostępny w Git, ale bieżący dokument nie pokazuje samodzielnie wszystkich kolejnych review runs.
- **Interpretacja:** wynik review powinien być dowodem dla konkretnej rewizji, a nie tylko zmiennym dokumentem stanu.
- **Typ:** weakness
- **Wpływ:** medium
- **Pewność:** high
- **Zakres:** project + methodology
- **Rekomendacja:** freeze review runs albo przechowywać formalny decision/review log wskazujący subject SHA.
- **Koszt/ryzyko:** niski/średni.
- **Human Authority:** zaakceptować prosty append-only log czy osobne artefakty review?

### OBS-014 — Traceability jest użyteczne, lecz ręczne i powielone

- **Obszar:** traceability, cost
- **Fakt:** powiązania CAP/BP/BR/REQ/QR/ARC/CTR występują w wielu tabelach, listach i sekcjach; niewiele z nich jest canonical machine-readable metadata.
- **Obserwacja:** macierze pomagają review, ale szybko się starzeją.
- **Interpretacja:** KGAID generuje wartość poznawczą, lecz bez projekcji z jednego źródła koszt będzie rósł nieliniowo.
- **Typ:** weakness / automation opportunity
- **Wpływ:** medium
- **Pewność:** high
- **Zakres:** project + methodology tooling
- **Rekomendacja:** wybrać minimalny canonical link model i generować odwrotne macierze, coverage i broken-link checks.
- **Koszt/ryzyko:** średni koszt narzędziowy; znaczna redukcja kosztu utrzymania.
- **Human Authority:** ustalić minimalny zestaw typowanych relacji dla profilu 3ksef.

### OBS-015 — Zakres dokumentacji jest wysoki, a profil adoption nie został wybrany

- **Obszar:** proportional rigor, cost
- **Fakt:** 180 dokumentów Markdown i 138 artefaktów zarządzanych powstało w krótkim czasie; adoption nie deklaruje profilu Minimal/Extended.
- **Obserwacja:** projekt stosuje de facto rygor rozszerzony bez jawnej decyzji koszt/ryzyko.
- **Interpretacja:** dla systemu finansowo-podatkowego wysoki rygor może być właściwy, ale powinien być uzasadniony, a nie przypadkowy.
- **Typ:** excess / adoption gap
- **Wpływ:** medium
- **Pewność:** high
- **Zakres:** project
- **Rekomendacja:** wybrać profil Extended z tailoringiem, listą mandatory artifacts i dozwolonymi projekcjami.
- **Koszt/ryzyko:** niski koszt decyzji; może ujawnić artefakty do konsolidacji.
- **Human Authority:** potwierdzić profil Extended dla PI-1.

### OBS-016 — BPS ma wartość, ale nie dowodzi jeszcze potrzeby nowego typu KGAID

- **Obszar:** Business Process artifact
- **Fakt:** BPS wypełnia lukę między capabilities a rules/requirements, lecz KGAID już klasyfikuje business processes jako Domain knowledge; 3ksef umieszcza je w Product.
- **Obserwacja:** eksperyment może być lokalną reprezentacją istniejącej kategorii wiedzy, nie nową kategorią normatywną.
- **Interpretacja:** zbyt szybkie dodanie prefiksu/artifact type utrwaliłoby lokalny układ.
- **Typ:** experiment / hypothesis
- **Wpływ:** medium
- **Pewność:** medium
- **Zakres:** methodology candidate
- **Rekomendacja:** najpierw doprecyzować mapping Product capability → Domain process → BR/REQ; sprawdzić w drugim projekcie.
- **Koszt/ryzyko:** niski koszt eksperymentu; średnie ryzyko proliferacji artefaktów.
- **Human Authority:** zdecydować, czy w 3ksef przenieść ownership BPS do Domain bez zmiany treści.

### OBS-017 — Migracja Domain Map naruszyła single source of truth

- **Obszar:** Domain/Architecture ownership, references
- **Fakt:** `docs/20-domain/domain-map.md` został przeniesiony/usunięty na rzecz dokumentu w Architecture, ale Domain README i Product Baseline nadal wskazują starą ścieżkę.
- **Obserwacja:** baseline zawiera nieaktualny member link, a zakres mapy biznesowej i architektonicznej się zlał.
- **Interpretacja:** sam manifest nie wystarcza bez automatycznego sprawdzania integralności i jednoznacznego ownership.
- **Typ:** 3ksef-specific problem
- **Wpływ:** medium
- **Pewność:** high
- **Zakres:** project
- **Rekomendacja:** przywrócić mapę domeny do Domain albo rozdzielić Business Domain Map od Architecture Context; walidować linki baseline’u.
- **Koszt/ryzyko:** niski.
- **Human Authority:** wybrać właściciela mapy domenowej.

### OBS-018 — KGAID ujawnił ryzyka bezpieczeństwa i compliance przed kodem

- **Obszar:** security, compliance, architecture
- **Fakt:** artefakty i review identyfikują multi-company isolation, permissions, audit retention, idempotency, retries, reconciliation i ambiguity.
- **Obserwacja:** ryzyka zostały nazwane przed implementacją i powiązane z wymaganiami/architekturą.
- **Interpretacja:** knowledge-first obniża prawdopodobieństwo późnego odkrycia problemów systemowych.
- **Typ:** strength
- **Wpływ:** high
- **Pewność:** high co do wykrycia; niska co do skuteczności kontroli bez implementacji
- **Zakres:** project + methodology validation
- **Rekomendacja:** zachować traceability ryzyko → QR/ARC/CTR → evidence; zweryfikować w PI-1.
- **Koszt/ryzyko:** średni koszt, uzasadniony charakterem systemu.
- **Human Authority:** wskazać, które ryzyka wymagają V2/V3 niezależnej weryfikacji.

### OBS-019 — Klasyfikacja ADR wymaga lepszego przykładu stosowania

- **Obszar:** ADR
- **Fakt:** Architecture Review wskazał 14 pytań do ADR, później wszystkie sklasyfikowano jako niewymagające ADR.
- **Obserwacja:** review poprawił nadmierną eskalację, ale dopiero po dodatkowej iteracji.
- **Interpretacja:** ogólna definicja ADR jest poprawna, lecz aplikacja nie odróżniała jeszcze decyzji trwałej od zwykłego uszczegółowienia specyfikacji.
- **Typ:** application problem / clarification candidate
- **Wpływ:** medium
- **Pewność:** medium
- **Zakres:** project + methodology examples
- **Rekomendacja:** dodać krótkie przykłady positive/negative ADR, bez nowego artefaktu.
- **Koszt/ryzyko:** niski.
- **Human Authority:** brak koniecznej decyzji normatywnej; wystarczy zgoda redakcyjna.

### OBS-020 — Brak jeszcze evidence dla Delivery, Verification i Operations

- **Obszar:** maturity, conformance
- **Fakt:** katalogi 60/70/80 są głównie placeholderami, a repozytorium jest przed implementacją.
- **Obserwacja:** ocena kończy się na Contracts.
- **Interpretacja:** nie można twierdzić, że KGAID został zweryfikowany end-to-end ani że poprawia jakość kodu, testów czy operacji.
- **Typ:** uncertainty / maturity limit
- **Wpływ:** medium
- **Pewność:** high
- **Zakres:** project + methodology evidence
- **Rekomendacja:** Stage 2 doświadczenia dopiero po jednym representative increment z test/evidence/baseline.
- **Koszt/ryzyko:** naturalny koszt kolejnej fazy; ryzyko przedwczesnych claims.
- **Human Authority:** wskazać representative increment do przyszłej oceny.

### OBS-021 — KGAID ma wewnętrzną niespójność słownika statusów

- **Obszar:** methodology governance
- **Fakt:** Artifact Model i Knowledge Lifecycle używają canonical `captured/proposed/reviewed/accepted/superseded/retired/rejected`; Metadata Profile i Approval Center operują m.in. `draft` i `deprecated`.
- **Obserwacja:** wdrażający nie otrzymuje jednego słownika normatywnego.
- **Interpretacja:** niespójność prawdopodobnie przyczyniła się do lokalnych rozbieżności lifecycle.
- **Typ:** methodology weakness
- **Wpływ:** high
- **Pewność:** high
- **Zakres:** methodology
- **Rekomendacja:** formalny CP ujednolicający statusy albo jawnie rozdzielający status dokumentu technicznego od statusu wiedzy; dokument normatywny ma precedence.
- **Koszt/ryzyko:** średni koszt migracji; wysokie ryzyko długotrwałej fragmentacji.
- **Human Authority:** wybrać jeden canonical vocabulary przed publikacją 0.1.0.

### OBS-022 — Nie ma dowodu dla automatycznego mnożenia statusów i review

- **Obszar:** change control
- **Fakt:** KGAID już ma `superseded`, `retired` i `rejected`; projekt użył także osobnych Product Review, ARR, Architecture Review i review kontraktów.
- **Obserwacja:** problemem jest znaczenie i relacja istniejących pojęć, nie ich zbyt mała liczba.
- **Interpretacja:** dodanie `obsolete/deprecated` lub obowiązkowego Domain/Requirements Review zwiększyłoby koszt bez obecnego dowodu wartości.
- **Typ:** rejected idea / guardrail
- **Wpływ:** low
- **Pewność:** medium
- **Zakres:** methodology
- **Rekomendacja:** najpierw konsolidacja słownika i review contracts; nowe typy tylko po powtarzalnym problemie w drugim projekcie.
- **Koszt/ryzyko:** uniknięty koszt proliferacji.
- **Human Authority:** brak decyzji teraz; pozostawić jako hipotezę.

### 5.1 Rozkład obserwacji według wpływu

| Wpływ | Liczba |
|---|---:|
| Critical | 0 |
| High | 12 |
| Medium | 9 |
| Low | 1 |
| **Razem** | **22** |

## 6. Mocne strony

1. **Product przed Architecture.** Projekt najpierw zbudował vision, capabilities, procesy, rules i requirements.
2. **Jawna odpowiedzialność człowieka.** Human Authority pozostaje odpowiedzialny za decyzje i publikację.
3. **Review z konsekwencją.** Wyniki przeglądów prowadziły do konkretnych commitów korygujących.
4. **Traceability jako narzędzie myślenia.** Powiązania ujawniły capabilities bez BR/REQ oraz publiczne odpowiedzialności bez contracts.
5. **Oddzielenie BR od REQ.** Reguła biznesowa nie jest ukryta w wymaganiu technicznym.
6. **Kontrakty jako obowiązki biznesowe.** CTR-001–004 zawierają preconditions, guarantees, failures i upstream links.
7. **Wczesne security thinking.** Multi-tenancy, permission model, audit, idempotency i reconciliation pojawiają się przed kodem.
8. **Pętla uczenia między repozytoriami.** Curation workflow jest konkretnym przykładem przejścia od doświadczenia projektu do proposed methodology.
9. **Uczciwe raportowanie braków.** Contract Coverage Review nie ukrywa, że z 11 wymaganych odpowiedzialności tylko 4 mają kontrakt.
10. **Brak wymuszonego waterfall.** Powroty do Product/Domain/Requirements są widoczne i zgodne z ideą KGAID.

## 7. Problemy specyficzne dla 3ksef

Poniższe problemy powinny być naprawione w projekcie niezależnie od ewentualnych zmian KGAID:

1. **Niejednoznaczny Architecture Baseline:** `proposed/approved` w metadanych, `pending` i pusta decyzja w treści.
2. **Product Baseline z niezaakceptowanymi członkami:** baseline lokalnie zastępuje lifecycle elementów.
3. **Kontrakty poza governance:** fenced metadata oraz typ `business-contract` spoza słownika.
4. **Broken/stale references:** Product Baseline i Domain README wskazują usuniętą ścieżkę Domain Map.
5. **Nieaktualny Contract Catalog:** nadal traktuje AB-001 jako oczekujący na approval.
6. **Nieaktualny feedback:** GAP-001–004 nie odzwierciedlają bieżącego KGAID.
7. **Niejawny profil adoption:** faktyczny poziom rygoru wygląda na Extended, lecz brak decyzji i tailoring.
8. **Duplikacja statusów i zakresu:** frontmatter, sekcje treści, katalogi, review i baseline’y potrafią się rozchodzić.
9. **Requirement Model z innym lifecycle:** używa m.in. `Draft/Withdrawn`, niezgodnych z lokalnym canonical governance.
10. **Brak formalnej integralności baseline’u:** manifest nie wiąże elementów przez commit/content hash i nie jest automatycznie sprawdzany.

To nie są automatycznie „braki KGAID”. Część jest skutkiem lokalnego modelowania, narzędzia approval albo szybkości pracy.

## 8. Potencjalne zmiany KGAID

### 8.1 Szybkie doprecyzowania

1. **Immutable adoption pin:** projekt ma wskazywać tag/release lub commit SHA oraz publication status.
2. **Dwie osie statusu:** prosty przykład pokazujący, że `approval_status: approved` nie oznacza `status: accepted`.
3. **Baseline membership:** domyślnie accepted-only; wyjątki jawne, ograniczone i zatwierdzone.
4. **Review contract:** subject ref, scope, questions, evidence, reviewer, authority, outcome, validity.
5. **Business process mapping:** zaznaczyć, że proces jest Domain knowledge, choć może być prezentowany z perspektywy Product.
6. **ADR examples:** po dwa przykłady decyzji wymagającej i niewymagającej ADR.
7. **Normative precedence:** przy konflikcie Artifact/Lifecycle vs Metadata Profile/proposed Approval Center obowiązuje dokument normatywny baseline’u.

### 8.2 Kandydaci do formalnego Change Proposal

1. **CP — Canonical lifecycle vocabulary**
   - ujednolicenie `captured/proposed/reviewed/accepted/superseded/retired/rejected`;
   - rozstrzygnięcie `draft`, `deprecated`, `withdrawn`;
   - zasady migracji i compatibility.
2. **CP — Revision-bound Human Decision**
   - subject content ID/SHA;
   - approver, time, scope, rationale;
   - automatic reapproval trigger po semantic change;
   - supersession/retirement history.
3. **CP — Baseline Manifest v2**
   - immutable methodology/project ref;
   - ID, version/content hash i knowledge status każdego membera;
   - per-item exceptions;
   - decision record i automatyczna integrity check.
4. **CP — Experience Record**
   - projekt, ref, obserwacja, dowody, ograniczenia, hipoteza, wynik drugiego użycia i decyzja normatywna.

### 8.3 Eksperymenty do kontynuacji w 3ksef

1. BPS jako Domain Process View, bez powielania PI-1 i System Workflow.
2. Generowane macierze traceability i coverage z canonical metadata.
3. Automatyczny validator baseline’u: member exists, accepted/exception, content hash, brak broken links.
4. Pilot Approval Center na jednym baseline’ie, wraz z reapproval po kontrolowanej zmianie.
5. Jedna cross-layer consistency checklist używana przez Product/Baseline Readiness zamiast kolejnego typu review.
6. Knowledge curation z `derived_from`, review date, expiry i jawnym przejściem do accepted knowledge.

### 8.4 Hipotezy wymagające drugiego projektu

1. Czy BPS powinien być osobnym, standardowym artifact type KGAID.
2. Czy osobny Governance Conflict Analysis ma powtarzalną wartość, czy był jednorazową reakcją na ARR-001/002.
3. Czy profil Extended zawsze wymaga niezależnego V2 reviewer przed Architecture/Contracts baseline.
4. Jaki minimalny zestaw artefaktów daje większość wartości KGAID w projekcie o niższym ryzyku.
5. Czy review warstwowe powinno być osobnymi artefaktami, czy instancjami jednego Review Record.

### 8.5 Pomysły odrzucone na obecnym etapie

1. Dodanie wszystkich statusów `obsolete/deprecated/withdrawn` bez konsolidacji obecnego lifecycle.
2. Obowiązkowe osobne Domain Review, Requirements Review i Baseline Review dla każdego projektu.
3. Zasada „każdy moduł musi mieć dokładnie jeden kontrakt”.
4. Uznanie baseline’u za sposób na autoryzowanie dowolnych proposed/captured items bez wyjątków.
5. Ogłoszenie 3ksef dowodem pełnej zgodności lub skuteczności end-to-end przed implementacją i verification evidence.

## 9. Rekomendowany etap 2 — nie wykonywać w ramach tego zadania

### Cel

Przekształcić obserwacje w kontrolowany record doświadczeń i mały zestaw decyzji KGAID, bez automatycznego włączania lokalnych rozwiązań do normy.

### Proponowany przebieg

1. **Zamrozić evidence set** na dwóch commitach użytych w tym raporcie.
2. **Utworzyć Experience Record** np. `EXP-3KSEF-001`, mapujący OBS → evidence → hypothesis → candidate change.
3. **Oddzielić trzy strumienie:**
   - lokalne naprawy 3ksef;
   - redakcyjne clarifications KGAID;
   - formalne CP wymagające Human Authority.
4. **Rozstrzygnąć blocker decisions:** immutable baseline, canonical statuses, baseline membership i revision-bound approval.
5. **Uruchomić mały pilot:** jeden wybrany baseline 3ksef, exact revision, accepted members/exceptions, approval record i automatyczna integrity check.
6. **Wykonać representative increment:** ograniczony fragment od accepted knowledge przez implementation i test evidence do verified state.
7. **Porównać z drugim projektem:** przynajmniej BPS, review taxonomy i minimalny profile.
8. **Dopiero potem podjąć decyzje normatywne:** accepted, rejected albo pozostawione jako optional pattern.

### Kryteria zakończenia etapu 2

- każda zmiana KGAID ma co najmniej jedno OBS i dokładne evidence;
- zmiany core mają dowód z więcej niż jednego projektu albo jawnie przyjęte ryzyko;
- baseline wskazuje niezmienną treść i status każdego membera;
- approval wskazuje dokładną rewizję;
- istnieje co najmniej jeden dowód z Delivery/Verification;
- koszt artefaktów i utrzymania jest zmierzony, nie tylko opisany.

## 10. Pytania Human Authority do Krzysztofa Olejnika

1. Czy `KGAID-0.1.0` ma zostać teraz opublikowany jako niezmienny tag/release, czy 3ksef ma jawnie pinować commit `dcc9976…` jako baseline eksperymentalny?
2. Czy baseline może zawierać elementy o statusie niższym niż `accepted`?
   - rekomendacja: tylko poprzez jawne, ograniczone wyjątki per item;
   - alternatywa: bezwzględne accepted-only.
3. Czy `approval_status: approved` w 3ksef miał oznaczać jedynie techniczne zatwierdzenie rewizji, czy także decyzję o akceptacji wiedzy?
4. Czy AB-001 ma zostać uznany za accepted Architecture Baseline mimo sprzecznej treści, czy wymaga nowej decyzji?
5. Czy dla 3ksef przyjmujemy profil Extended ze względu na finanse, podatki, multi-company i KSeF?
6. Czy BPS pozostaje lokalnym eksperymentem, czy ma być kandydatem do standardowego artifact type? Rekomendacja: najpierw przenieść semantyczne ownership do Domain i zebrać drugi przypadek.
7. Czy Product Review i Architecture Readiness Review mają być osobne? Jeśli tak, jaka jest dokładna różnica subject, authority i outcome?
8. Czy Stage 2 Approval Center ma być pilotowany na jednym baseline’ie 3ksef przed formalną integracją z KGAID?
9. Kto ma authority do zamykania wpisów `kgaid-feedback.md` po zmianie metodyki?
10. Który mały, reprezentatywny increment ma posłużyć do pierwszej oceny Delivery/Verification end-to-end?
11. Które ryzyka wymagają V2/V3: permission isolation, audit, KSeF reconciliation, idempotency czy wszystkie?
12. Czy 3ksef może być nazwany oficjalnym projektem referencyjnym KGAID, czy na razie wyłącznie pilotem?

## 11. Aneks dowodowy

Wszystkie linki wskazują dokładne commity użyte w analizie.

| ID | Repozytorium i dokument | Dowód | Powiązane obserwacje |
|---|---|---|---|
| EV-001 | [3ksef/AGENTS.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/AGENTS.md) | Role, ograniczenia wykonawcze, osobna zgoda na push/tag/release/PR. | OBS-002 |
| EV-002 | [3ksef/instrukcja_ChatGPT.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/instrukcja_ChatGPT.md) | Cykl Human–ChatGPT–Codex i review wyniku. | OBS-002, OBS-003 |
| EV-003 | [docs/AGENTS.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/AGENTS.md) | Dokumentacja jako źródło wiedzy, single ownership, feedback do KGAID. | OBS-011, OBS-014 |
| EV-004 | [kgaid-adoption.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/00-governance/kgaid-adoption.md) | Deklaracja KGAID 0.1.0 bez immutable pin i bez profilu. | OBS-005, OBS-015 |
| EV-005 | [documentation-governance.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/00-governance/documentation-governance.md) | Lokalny canonical lifecycle, approval i słownik typów. | OBS-006, OBS-010, OBS-021 |
| EV-006 | [product-baseline-1.0.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/00-governance/product-baseline-1.0.md) | Członkowie Product Baseline oraz nieaktualna ścieżka Domain Map. | OBS-007, OBS-017 |
| EV-007 | [architecture-readiness-review-003.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/00-governance/architecture-readiness-review-003.md) | Baseline jako całość autoryzuje artefakty mimo indywidualnych statusów. | OBS-007, OBS-012 |
| EV-008 | [architecture-readiness-review.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/00-governance/architecture-readiness-review.md) | Pierwszy wynik readiness i ujawnione ryzyka. | OBS-003, OBS-012, OBS-018 |
| EV-009 | [architecture-readiness-review.md — Product](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/10-product/architecture-readiness-review.md) | Braki pokrycia, statusów, traceability i permission catalog. | OBS-003, OBS-012 |
| EV-010 | [arr-review-differences-analysis.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/00-governance/arr-review-differences-analysis.md) | 14 różnic między ARR-001 i ARR-002, neutralne opcje dla Human. | OBS-012 |
| EV-011 | [product-review.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/10-product/product-review.md) | Review treści Product i stan ówczesnego approval. | OBS-003, OBS-012 |
| EV-012 | [kgaid-feedback.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/00-governance/kgaid-feedback.md) | GAP-001–004 i eksperymenty EP-001–006. | OBS-004, OBS-011, OBS-016 |
| EV-013 | [business-process-model.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/10-product/business-processes/business-process-model.md) | Lokalny model BPS jako eksperymentalne rozszerzenie Product. | OBS-016 |
| EV-014 | [BP-001](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/10-product/business-processes/processes/BP-001-wystawienie-faktury-sprzedazy.md) | Pełny proces o statusie `captured`, ale approval `approved`. | OBS-006, OBS-016 |
| EV-015 | [business-rule-model.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/20-domain/business-rules/business-rule-model.md) | Rozdzielenie BR i REQ. | OBS-001 |
| EV-016 | [requirement-model.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/30-requirements/requirement-model.md) | Model wymagań oraz lokalnie rozbieżny lifecycle. | OBS-021 |
| EV-017 | [domain-model.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/20-domain/domain-model.md) | Encje, lifecycle faktury i relacja z KSeF. | OBS-001, OBS-018 |
| EV-018 | [Domain README](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/20-domain/README.md) | Referencja do usuniętej ścieżki Domain Map. | OBS-017 |
| EV-019 | [architecture-review-pi-1.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/00-governance/architecture-review-pi-1.md) | Końcowy wynik `Ready`, historia wersji i klasyfikacja ADR. | OBS-003, OBS-013, OBS-019 |
| EV-020 | [architecture-baseline-1.0.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/40-architecture/baselines/architecture-baseline-1.0.md) | `proposed/approved` vs treść `pending` i pusta decyzja. | OBS-008, OBS-009 |
| EV-021 | [architecture-specification-pi1.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/40-architecture/views/architecture-specification-pi1.md) | Nadrzędna specyfikacja i upstream traceability. | OBS-001, OBS-003, OBS-018 |
| EV-022 | [contract-catalog.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/50-contracts/contract-catalog.md) | Plan CTR i nieaktualny stan Architecture Baseline. | OBS-010 |
| EV-023 | [business-contract-template.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/50-contracts/templates/business-contract-template.md) | Fenced YAML i typ `business-contract`. | OBS-010 |
| EV-024 | [CTR-001](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/50-contracts/business-contracts/CTR-001-create-draft-invoice.md) | Przykład konkretnego, traceable kontraktu. | OBS-010, OBS-018 |
| EV-025 | [business-contracts-coverage-review-pi1.md](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/50-contracts/reviews/business-contracts-coverage-review-pi1.md) | 11 wymaganych odpowiedzialności, 4 istniejące i 7 brakujących kontraktów. | OBS-003, OBS-014 |
| EV-026 | [knowledge staging AGENTS](https://github.com/KrzysztofOle/3ksef/blob/133817601f597a8b73902c411f3c547e82e54f91/docs/90-knowledge/knowledge-staging/AGENTS.md) | Reguły preserve sources, incoming/processed i zakaz wynajdywania faktów. | OBS-004 |
| EV-027 | [KGAID README](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/README.md) | Zakres metodyki, 14 dokumentów normatywnych i prepared baseline. | OBS-005, OBS-020 |
| EV-028 | [KGAID principles](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/00-foundations/02-principles.md) | Knowledge-first, Human accountability, proportional rigor. | OBS-001, OBS-002, OBS-015 |
| EV-029 | [artifact-model.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/10-knowledge-architecture/12-artifact-model.md) | Katalog artefaktów, trzy osie statusu i accepted knowledge w baseline. | OBS-006, OBS-007, OBS-016, OBS-021 |
| EV-030 | [knowledge-lifecycle.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/10-knowledge-architecture/13-knowledge-lifecycle.md) | Canonical lifecycle i Human decision. | OBS-006, OBS-009, OBS-021 |
| EV-031 | [authority-model.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/10-knowledge-architecture/14-authority-model.md) | Human roles, delegation i ograniczenia AI. | OBS-002 |
| EV-032 | [knowledge-domains.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/10-knowledge-architecture/16-knowledge-domains.md) | Business processes jako Domain knowledge. | OBS-016, OBS-017 |
| EV-033 | [process-model.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/20-methodology/21-process-model.md) | PM1–PM9 i zależności bez wymuszonego waterfall. | OBS-001 |
| EV-034 | [human-ai-collaboration.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/20-methodology/22-human-ai-collaboration.md) | Delegation, execution, report, review i Human decision. | OBS-002 |
| EV-035 | [verification-and-evidence-model.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/30-quality/31-verification-and-evidence-model.md) | Claims ≤ evidence i poziomy V0–V3. | OBS-003, OBS-018, OBS-020 |
| EV-036 | [adoption-and-conformance-model.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/40-adoption/41-adoption-and-conformance-model.md) | Immutable pin, profile, mapping, tailoring i representative increment. | OBS-005, OBS-015, OBS-020 |
| EV-037 | [governance-and-release-model.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/50-governance/governance-and-release-model.md) | Oddzielenie przygotowania baseline’u od publikacji. | OBS-005 |
| EV-038 | [KGAID-0.1.0.yaml](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/50-governance/baselines/KGAID-0.1.0.yaml) | `publication_status: prepared-unpublished`. | OBS-005 |
| EV-039 | [metadata-profile.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/50-governance/metadata-profile.md) | Niezależne pola status/approval i odmienny słownik statusów. | OBS-006, OBS-021 |
| EV-040 | [knowledge-base-curation-workflow.md](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/20-methodology/25-knowledge-base-curation-workflow.md) | Proponowany workflow wyprowadzony empirycznie z pilota 3ksef. | OBS-004 |
| EV-041 | [Approval Center README](https://github.com/KrzysztofOle/kgaid-methodology/blob/dcc9976ba523120e319cfa1f5fb4460a74a38e99/docs/60-approval/README.md) | Approval Center jako proposed/informational, poza baseline’em. | OBS-009, OBS-021 |

## 12. Końcowy raport wykonania

### Repozytoria i referencje

- `KrzysztofOle/3ksef` — `agent/project-structure` @ `133817601f597a8b73902c411f3c547e82e54f91`
- `KrzysztofOle/kgaid-methodology` — `main` @ `dcc9976ba523120e319cfa1f5fb4460a74a38e99`

### Liczba i zakres dokumentów

- 180 aktualnych plików Markdown 3ksef objętych inwentaryzacją strukturalną;
- 138 zarządzanych artefaktów 3ksef objętych analizą metadanych;
- 38 kluczowych dokumentów 3ksef objętych pogłębioną analizą treści;
- 23 pliki KGAID objęte analizą, w tym 14 dokumentów normatywnych;
- łącznie 203 aktualne pliki w zakresie przeglądu strukturalnego i normatywnego;
- obszary: Governance, Product, Domain, Requirements, Architecture, ADR, Contracts, Knowledge, Delivery, Verification, Operations, Human Authority, collaboration, traceability, approval, baselines, security i cost.

### Wynik

- 22 obserwacje: 0 critical, 12 high, 9 medium, 1 low;
- 10 lokalnych problemów 3ksef;
- 7 szybkich doprecyzowań KGAID;
- 4 kandydatów do formalnego Change Proposal;
- 6 eksperymentów do kontynuacji;
- 5 hipotez wymagających drugiego projektu;
- 5 pomysłów odrzuconych na obecnym etapie;
- 41 pozycji w aneksie dowodowym.

### Ograniczenia końcowe

- brak evidence z implementacji, testów produkcyjnych i Operations;
- brak oceny prawnej/podatkowej;
- brak danych z rozmów i decyzji niezapisanych w repozytoriach;
- jeden projekt referencyjny nie wystarcza do pełnej walidacji metodyki.

### Potwierdzenia

- Nie zmodyfikowano `KrzysztofOle/3ksef`.
- Nie zmodyfikowano `KrzysztofOle/kgaid-methodology`.
- Nie utworzono commitów, branchy, PR-ów, tagów, release’ów, issues ani komentarzy.
- Nie wykonano push, merge, approval PR ani żadnej innej akcji zapisującej w GitHub.
- Rekomendowany etap 2 został wyłącznie opisany i nie został wykonany.
