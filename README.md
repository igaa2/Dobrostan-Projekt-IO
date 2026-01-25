# Wskaźnik Kompozytowy Jakości Życia Polskich Województw (DobrostanPL) :shamrock:

## Spis treści
* [Charakterystyka oprogramowania](#charakterystyka-oprogramowania)
* [Prawa autorskie](#prawa-autorskie)
* [Specyfikacja wymagań](#specyfikacja-wymagań)
* [Architektura oprogramowania](#architektura-oprogramowania)
* [Procedura instalacji i uruchomienia](#procedura-instalacji-i-uruchomienia)
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

*Wymagania funkcjonalne zdefiniowane w formie historyjek użytkownika (User Stories). W nawiasach kwadratowych określono priorytety.*

### Moduł Danych i Obliczeń (Backend)

> **US-01:** [1] Jako **Administrator Systemu**, chcę, aby aplikacja **automatycznie pobierała dane z API Banku Danych Lokalnych (GUS)**, aby wskaźniki opierały się na oficjalnych i najbardziej aktualnych statystykach.

> **US-02:** [1] Jako **Analityk**, chcę, aby system **normalizował dane wejściowe (sprowadzał do wspólnej skali)**, aby możliwe było poprawne obliczenie wskaźnika kompozytowego dla różnych typów danych.

### Moduł Interfejsu i Prezentacji (Frontend)

> **US-03:** [1] Jako **Użytkownik** szukający miejsca do życia, chcę **zobaczyć ranking województw posortowany według jakości życia**, aby szybko zidentyfikować najlepsze regiony do zamieszkania.

> **US-04:** [2] Jako **Użytkownik**, chcę **mieć możliwość zmiany wag poszczególnych kryteriów**, aby obliczony wskaźnik kompozytowy odpowiadał moim osobistym preferencjom.

> **US-05:** [2] Jako **Użytkownik**, chcę **zobaczyć wyniki na interaktywnej mapie Polski**, aby łatwiej ocenić rozkład jakości życia w interesującym mnie województwie.

> **US-06:** [3] Jako **Użytkownik**, chcę **porównać kilka wybranych województw w widoku "obok siebie"**, aby wyraźnie zobaczyć różnice w konkretnych składowych wskaźnika.

*Priorytety: 1 - wymagane, 2 - przydatne, 3 - opcjonalne.*

## Architektura oprogramowania

### Architektura rozwoju
*Stos technologiczny wykorzystywany podczas tworzenia oprogramowania.*

| Nazwa Technologii | Przeznaczenie | Wersja |
| :--- | :--- | :--- |
| **Python** | Główny język programowania | >= 3.12 |
| **Visual Studio Code** | Zintegrowane środowisko programistyczne (IDE) do edycji kodu źródłowego | >= 1.96.2 |
| **Black** | Formater kodu i kontrola jakości | >= 25.12.0 |
| **Git & GitHub** | System kontroli wersji oraz repozytorium zdalne do pracy grupowej | >= 2.47.1 |
| **Setuptools** | Narzędzie do budowania i pakowania projektu | >= 61.0 |

### Architektura uruchomieniowa
*Technologie wymagane do działania systemu w środowisku docelowym.*

| Nazwa Technologii | Przeznaczenie | Wersja |
| :--- | :--- | :--- |
| **Python** | Środowisko uruchomieniowe (interpreter języka) | >= 3.12 |
| **Streamlit** | Framework do obsługi interfejsu użytkownika i renderowania aplikacji webowej | >= 1.52.2 |
| **Pandas** | Biblioteka do manipulacji danymi, strukturyzowania DataFrame i normalizacji | >= 2.3.3 |
| **NumPy** | Wykonywanie obliczeń numerycznych (np. wektorowa normalizacja danych) | >= 2.3.0 |
| **SciPy** | Obliczenia statystyczne (wyliczanie współczynnika skośności w walidatorze) | >= 1.16.3 |
| **Plotly** | Generowanie interaktywnych wizualizacji (mapy, wykresy słupkowe, wykresy radarowe) | >= 6.5.2 |
| **Requests** | Obsługa protokołu HTTP do komunikacji z API Banku Danych Lokalnych | >= 2.32.5 |
| **Loguru** | System logowania zdarzeń w aplikacji (obsługa błędów i informacji) | >= 0.7.3 |
| **Jsonschema** | Walidacja poprawności struktur danych i plików konfiguracyjnych | >= 4.26.0 |
| **PyYAML** | Obsługa plików konfiguracyjnych w formacie YAML | >= 6.0.3 |

## Procedura instalacji i uruchomienia
*Poniższa instrukcja opisuje kroki niezbędne do uruchomienia aplikacji w środowisku lokalnym.*

**Wymagania wstępne**

> Zainstalowany język **Python w wersji >= 3.12**.

> Zainstalowany system kontroli wersji **Git**.

> Dostęp do internetu (pobieranie danych z API BDL GUS).

### Krok 1: Pobranie kodu źródłowego

Sklonuj repozytorium na dysk lokalny, używając terminala:

```python
git clone https://github.com/igaa2/Dobrostan-Projekt-IO.git
cd Dobrostan-Projekt-IO/src
```

### Krok 2: Przygotowanie środowiska (opcjonalne, ale zalecane)

```python
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Krok 3: Instalacja zależności

Projekt wykorzystuje plik `pyproject.toml`, który zawiera wymagane biblioteki. Zainstaluj je za pomocą komendy:

```python
pip install .
```

### Krok 4: Uruchomienie aplikacji

```python
streamlit run ./src/app.py
```

Aplikacja powinna automatycznie otworzyć się w domyślnej przeglądarce.

### Krok 5: Rozwiązywanie problemów

> Błąd "Command not found: streamlit": Upewnij się, że aktywował*ś środowisko wirtualne (Krok 2) przed instalacją.

> Błąd połączenia: Przy pierwszym uruchomieniu aplikacja pobiera dane z API GUS. Upewnij się, że masz aktywne połączenie z internetem.

## Testy

### Scenariusze testów

| ID | Wymaganie | Nazwa Scenariusza | Kroki do wykonania | Oczekiwany rezultat |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | US-01, US-03 | Uruchomienie i dane | 1. Uruchom aplikację.<br>2. Poczekaj na załadowanie danych z API GUS. | Aplikacja uruchamia się bez błędów. Wyświetla się tytuł, mapa Polski, ranking województw oraz wykres radarowy. |
| **TC-02** | US-05 | Interakcja z mapą | 1. Najedź kursorem na dowolne województwo na mapie.<br>2. Sprawdź etykietę. | Mapa reaguje na kursor. Wyświetla się dymek (tooltip) z nazwą województwa i wartością wskaźnika w %. |
| **TC-03** | US-04 | Zmiana wag (suwaki) | 1. Przesuń suwak wagi dla wybranej zmiennej na 100%.<br>2. Ustaw inną wagę na 0%. | Ranking na wykresie słupkowym oraz kolory na mapie automatycznie się aktualizują zgodnie z nowymi wagami. |
| **TC-04** | US-06 | Porównanie regionów | 1. W sekcji "Porównanie" wybierz z listy dwa województwa.<br>2. Obserwuj wykres radarowy. | Generuje się wykres radarowy z nałożonymi na siebie obrysami dla wybranych regionów. |
| **TC-05** | US-02 | Destymulanty | 1. Zmień przełącznik przy zmiennej na "ON".<br>2. Sprawdź ranking. | Ranking przelicza się. Województwa z wysoką wartością tej cechy spadają w rankingu. |
| **TC-06** | US-01, US-02 | Walidacja wag 0 | 1. Ustaw wszystkie suwaki wag na 0%. | Aplikacja wyświetla ostrzeżenie (Warning), że nie można obliczyć rankingu. Aplikacja nie ulega awarii. |

### Sprawozdanie z wykonania scenariuszy testów

| ID Scenariusza | Wynik | Uwagi |
| :--- | :--- | :---: |
| **TC-01** | Pozytywny | - |
| **TC-02** | Pozytywny | - |
| **TC-03** | Pozytywny | Odświeżanie działa płynnie. |
| **TC-04** | Pozytywny | - |
| **TC-05** | Pozytywny | - |
| **TC-06** | Pozytywny | Komunikat jest czytelny. |
