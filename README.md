# Wskaźnik Kompozytowy Jakości Życia Polskich Województw (DobrostanPL) :shamrock:

## Spis treści
* [Charakterystyka oprogramowania](#charakterystyka-oprogramowania)
* [Prawa autorskie](#prawa-autorskie)
* [Specyfikacja wymagań](#specyfikacja-wymagań)
* [Architektura oprogramowania](#architektura-oprogramowania)
* [Testy](#testy)

## Charakterystyka oprogramowania
System `DobrostanPL` to narzędzie analityczne służące do oceny i porównywania jakości życia w polskich województwach. Aplikacja dynamicznie pobiera dane z publicznego API Banku Danych Lokalnych Głównego Urzędu Statystycznego (BDL GUS), co gwarantuje dostęp do oficjalnych danych statystycznych. Na ich podstawie generowane są rankingi oraz wizualizacje mapowe. Dobór zakresu czasowego danych następuje w oparciu o weryfikację metadanych poszczególnych zmiennych, co pozwala na pobranie wartości z najnowszego dostępnego roku. 

Głównym celem projektu jest dostarczenie użytkownikowi rzetelnej informacji o tym, gdzie w Polsce panują najlepsze warunki do życia, z uwzględnieniem spersonalizowanych kryteriów.

## Prawa autorskie
* **Autorzy oprogramowania:**
  - Iga Bochniak
  - Agnieszka Góral
  - Hanna Sopala
* **Licencja:** MIT

## Specyfikacja wymagań

*Wymagania funkcjonalne zdefiniowane w formie historyjek użytkownika (User Stories).*

### Moduł Danych i Obliczeń (Backend)

> **US-01:** Jako **Administrator Systemu**, chcę, aby aplikacja **automatycznie pobierała dane z API Banku Danych Lokalnych (GUS)**, aby wskaźniki opierały się na oficjalnych i najbardziej aktualnych statystykach.

> **US-02:** Jako **Analityk**, chcę, aby system **normalizował dane wejściowe (sprowadzał do wspólnej skali)**, aby możliwe było poprawne obliczenie wskaźnika kompozytowego dla różnych typów danych.

### Moduł Interfejsu i Prezentacji (Frontend)

> **US-03:** Jako **Użytkownik Szukający Miejsca do Życia**, chcę **zobaczyć ranking województw posortowany według jakości życia**, aby szybko zidentyfikować najlepsze regiony do zamieszkania.

> **US-04:** Jako **Użytkownik**, chcę **mieć możliwość zmiany wag poszczególnych kryteriów**, aby obliczony wskaźnik kompozytowy odpowiadał moim osobistym preferencjom.

> **US-05:** Jako **Użytkownik**, chcę **zobaczyć wyniki na interaktywnej mapie Polski**, aby łatwiej ocenić rozkład jakości życia w interesującym mnie województwie.

> **US-06:** Jako **Użytkownik**, chcę **porównać kilka wybranych województw w widoku "obok siebie"**, aby wyraźnie zobaczyć różnice w konkretnych składowych wskaźnika.

## Architektura oprogramowania

### Architektura rozwoju
*Stos technologiczny wykorzystywany podczas tworzenia oprogramowania.*

| Nazwa Technologii | Przeznaczenie | Wersja |
| :--- | :--- | :--- |
| **Python** | Główny język programowania do implementacji logiki biznesowej i interfejsu | 3.12 |
| **Visual Studio Code** | Zintegrowane środowisko programistyczne (IDE) do edycji kodu źródłowego | Najnowsza |
| **Black** | Formater kodu i kontrola jakości (Dev dependency) | 25.12.0 |
| **Git & GitHub** | System kontroli wersji oraz repozytorium zdalne do pracy grupowej | - |
| **Setuptools** | Narzędzie do budowania i pakowania projektu | ≥61.0 |

### Architektura uruchomieniowa
*Technologie wymagane do działania systemu w środowisku docelowym.*

| Nazwa Technologii | Przeznaczenie | Wersja |
| :--- | :--- | :--- |
| **Streamlit** | Framework do obsługi interfejsu użytkownika i renderowania aplikacji webowej | 1.52.2 |
| **Pandas** | Biblioteka do manipulacji danymi, strukturyzowania DataFrame i normalizacji | 2.3.3 |
| **NumPy** | Wykonywanie obliczeń numerycznych (np. wektorowa normalizacja danych) | 2.3.0 |
| **SciPy** | Obliczenia statystyczne (wyliczanie współczynnika skośności w walidatorze) | 1.16.3 |
| **Plotly** | Generowanie interaktywnych wizualizacji (mapy, wykresy słupkowe, wykresy radarowe) | 6.5.2 |
| **Requests** | Obsługa protokołu HTTP do komunikacji z API Banku Danych Lokalnych | 2.32.5 |
| **Loguru** | System logowania zdarzeń w aplikacji (obsługa błędów i informacji) | 0.7.3 |
| **Jsonschema** | Walidacja poprawności struktur danych i plików konfiguracyjnych | 4.26.0 |
| **PyYAML** | Obsługa plików konfiguracyjnych w formacie YAML | 6.0.3 |

## Testy
