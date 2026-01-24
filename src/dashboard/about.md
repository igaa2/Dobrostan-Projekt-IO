## 📊 Dashboard Dobrostanu Województw Polski

### O aplikacji
Aplikacja wizualizuje wskaźnik kompozytowy dobrostanu dla 16 województw Polski, oparty na 11 zmiennych składowych.

### ⚖️ Metodologia
Wskaźnik kompozytowy został obliczony metodą COPRAS. Zastosowano wagi hybrydowe, uzyskane jako iloczyn współczynnika zmienności (CV) oraz ważności przypisanej przez użytkownika. Następnie wagi zostały znormalizowane w taki sposób, aby ich suma wynosiła 100%.

### 🎚️ Jak używać wag?
**Suwaki po lewej stronie** pozwalają ustawić ważność zmiennej
- **0%** = wskaźnik jest ignorowany w obliczeniach
- **100%** = wskaźnik ma maksymalny wpływ

### 🎚️ Jak używać dźwigni?
**Dźwignie** pozwalają ustawić kierunek wpływu zmiennej
- **OFF** = zmienna jest stymulantą (jej wyższa wartość jest korzystniejsza)
- **ON** = zmienna jest destymulantą (jej niższa wartość jest korzystniejsza)

### 📈 Interpretacja mapy
Im ciemniejszy kolor województwa, tym wyższy poziom dobrostanu.
Mapa przedstawia wartości wskaźnika kompozytowego dla poszczególnych województw. Skala kolorów jest uporządkowana rosnąco — jaśniejsze obszary oznaczają niższy wynik, ciemniejsze — wyższy. Dzięki temu można szybko zobaczyć, które regiony wypadają korzystniej, a które wymagają poprawy.

### 📈 Interpretacja wykresu słupkowego
- **Zielone słupki** - województwa powyżej średniej krajowej
- **Czerwone słupki** - województwa poniżej średniej krajowej
- **Przerywana linia** - średnia wartość wskaźnika

### 📈 Interpretacja wykresu radarowego
Im dalej od środka na danej osi, tym korzystniejszy wynik danej zmiennej.
Wykres radarowy umożliwia jednoczesne porównanie wielu zmiennych dla jednej jednostki lub kilku jednostek. Większa powierzchnia figury oznacza lepszy ogólny wynik, a kształt wykresu wskazuje, w jakich obszarach dana jednostka wypada lepiej lub gorzej w porównaniu z innymi.

---
**Wersja:** 1.0.0  
**Autor:** Agnieszka, Hanna, Iga
**Dane:** Bank Danych Lokalnych GUS