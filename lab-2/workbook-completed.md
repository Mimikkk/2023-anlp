# Zadania

## 1. W korpusie występują słowa z następującymi krotnościami ( w nawiasach ): low (5), lowest (2), newer (6), wider (3), new (2). Wykonaj pierwsze kilka iteracji algorytmu BPE

BPE polega na redukcje rozmiaru słownictwa w korpusie poprzez enkodowanie najczęściej występujących
znaków przez najczęstsze występujący grup znaków/bajtów w słowach.

Iteracje algorytmu BPE polegają na zliczaniu wystąpień par znaków w korpusie i łączeniu ich w grupy,
które następnie są traktowane jako pojedyncze znaki. W każdej iteracji algorytmu łączymy najczęściej
występujące pary znaków w grupy, a następnie zliczamy wystąpienia nowych par znaków.

Iteracja:

1. Zliczamy wystąpienia par znaków w korpusie
2. Łączymy najczęściej występujące pary znaków w grupy
3. Zliczamy wystąpienia nowych par znaków
4. Powtarzamy kroki 2-3 aż do osiągnięcia zadanego rozmiaru słownictwa

- low (5)
- lowest (2)
- newer (6)
- wider (3)
- new (2)

Iteracja 1:

- "l" "o" "w" 5
- "l" "o" "w" "e" "s" "t" 2
- "n" "e" "w" "e" "r" 6
- "w" "i" "d" "e" "r" 3
- "n" "e" "w" 2

```json
Vocabulary = { 
  "l": 7,
  "o": 7,
  "w": 15,
  "e": 13,
  "s": 2,
  "t": 2,
  "n": 8,
  "r": 9,
  "i": 3,
  "d": 3
}
```

```json
pairs = {
  "lo": 7,
  "ow": 7,
  "we": 8,
  "es": 2,
  "st": 2,
  "ne": 8,
  "ew": 8,
  /* Largest */
  "er": 9
}
```

Iteracja 2:

- "l" "o" "w" 5
- "l" "o" "w" "e" "s" "t" 2
- "n" "e" "w" "er" 6
- "w" "i" "d" "er" 3
- "n" "e" "w" 2

```json
Vocabulary = { 
  "l": 7,
  "o": 7,
  "w": 15,
  "e": 13,
  "s": 2,
  "t": 2,
  "n": 8,
  "r": 9,
  "i": 3,
  "d": 3,
  "er": 9
}
```

```json
pairs = {
  "lo": 7,
  "ow": 7,
  "we": 2,
  "es": 2,
  "st": 2,
  /** Largest - Wybieramy ten */ 
  "ne": 8,
  /** Largest */
  "ew": 8,
  "wer": 6,
  "der": 3,
}
```

Iteracja 3:

- "l" "o" "w" 5
- "l" "o" "w" "e" "s" "t" 2
- "ne" "w" "er" 6
- "w" "i" "d" "er" 3
- "ne" "w" 2

Itd...

## 2. Załóżmy, że używasz modelu trzy-gramowego, w którym każdy warunkowy rozkład prawdopodobieństwa jest rozkładem jednorodnym. Ile wynosi nieokreśloność

Nieokreśloność (eng. perplexity) to miara złożoności modelu języka. Im mniejsza wartość tym lepszy model.

Wyrażana poprzez wzór:
$$ PP_{test} = \sqrt[N]{\frac{1}{\prod\limits_{s\in D_{test}} P(s)}}$$

Zakładając model trzy-gramowy, w którym każdy warunkowy rozkład prawdopodobieństwa jest rozkładem jednorodnym, nieokreśloność wynosi $N^3$.

Podstawienie wartości:

$$ PP_{test} = \sqrt[N]{\frac{1}{\prod\limits_{s\in D_{test}} P(s)}} = \sqrt[N]{\frac{1}{\prod\limits_{s\in D_{test}} \frac{1}{N^3}}} = \sqrt[N]{\frac{1}{\left(\frac{1}{N^3}\right)^N}} = \sqrt[N]{\left(\frac{1}{N^3}\right)^{-N}}= \left(\frac{1}{N^3}\right)^{-1} = N^3 $$

## 3. Rozważ poniższy korpus i zaproponuj dla niego przypisania słów do grup, takich jak w klasowym modelu n-gramowym, i co najmniej 3 prawidłowe schematy zdań możliwe do utworzenia z tych grup

- Ala ma kota i psa
- Kasia posiada psa i chomika
- Jurek kocha papugę
- Ona lubi papugę i chomika

Grupy korpusu to blisko powiązane słowa, które mogą być traktowane jako pojedyncze słowo w modelu n-gramowym.

np. C1 = { Ala, Kasia, Jurek, Ona }, C2 = { ma, posiada, kocha, lubi }, C3 = { kota, psa, chomika, papugę }, C4 = { i }

Ułożenia:

- C1 C2 C3
- C1 C2 C3 C4 C3
- C1 C4 C1 C2 C3
- C1 C4 C1 C2 C3 C4 C2 C3

## 4. Do kilku grup uzyskanych w poprzednim zadaniu dodaj po jednym nowym słowie. Ile nowych zdań można wygenerować z takiego model?

C1 = { Ala, Kasia, Jurek, Ona, Jan }
C4 = { i, oraz }

Liczba nowych zdań to różnica produktu schematu liczb słów w każdej z nowej grup i produktu schematu liczb słów w grupach bazowych.

Liczności Stare: $|C1|=4$, $|C2|=4$, $|C3|=4$, $|C4|=1$
Liczności Nowe: $|C1|=5$, $|C2|=4$, $|C3|=4$, $|C4|=2$

Nowe zdania w schemacie C1 C2 C3:
$$ 5 \times 4 \times 4 - 4 \times 4 \times 4 = 16 $$

itd...

## 5. Korzystając z klas słów $C_1\in\{\text{Śmignąłem}, \text{Pojechałem}\}$, $C_2\in\{\text{do}\}$, $C_3\in\{\text{szkoły}, \text{teatru}\}$, $C_4\in\{\text{metrem},\text{samochodem},\text{tramwajem}\}$, zdefiniuj co najmniej jeden schemat prawidłowego zdania

- C1 C2 C3
- C1 C4 C2 C3
- C2 C3 C1 C4

## 6. Załóżmy, że w korpusie mamy zdania: "Pojechałem do szkoły metrem", "Pojechałem do szkoły tramwajem", "Pojechałem do teatru metrem", "Pojechałem do teatru samochodem", "Śmignąłem do szkoły metrem", a klasy słów zostały zdefiniowane tak jak wyżej. Używajać bi-gramowego klasowego modelu języka oblicz prawdopodobieństwo sekwencji "Śmignąłem do szkoły samochodem"

- $P(Śmignąłem|[start]) = \dots$
- $P(do|Śmignąłem) = \dots$
- $P(szkoły|do) = \dots$
- $P(samochodem|szkoły) = \dots$
- $P([stop]|samochodem) = \dots$

$$ P(Śmignąłem\,do\,szkoły\,samochodem) = P(Śmignąłem|[start]) \times P(do|Śmignąłem) \times P(szkoły|do) \times P(samochodem|szkoły) \times P([stop]|samochodem) = \dots $$

## 7. Zakładając korpus

- Pojechałem rowerem
- Pojechałem samochodem
- Śmignąłem samochodem

Wykonaj pierwszą iterację algorytmu uczącego bi-gramowy model klasowy. Dla uproszczenia obliczeń w funkcji celu możesz pominąć logarytm. W poniższej tabelce umieszczono w wierszach kilka rozważanych przez algorytm par do połączenia w grupę, a w kolumnach umieszczono miejsca na kolejne prawdopodobieństwa tranzycji ( słowa skrócono do ich pierwszych liter ) oraz wszystkie wymnożone prawdopodobieństwa Emisji (łącznie, kolumna E).

Wymnożenie wszystkich prawdopodobieństw w wierszu powinno w rezultacie dać wynik funkcji celu dla rozważanej pary (pomijając logarytm).

| Para słów | E | $PI[start]$ | $rIP$ | $[stop]Ir$ | $PI[start]$ | $sIP$ | $[stop]Is$ | $ŚI[start]$ | $sIŚ$ | $[stop]Is$ | f. celu |
| - | - | - | - | - | - | - | - | - | - | - | - |
| $\emptyset$ |  |  |  |  |  |  |  |  |  |  |  |
| $P,Ś$ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| $r,s$ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| $P,r$ |  |  |  |  |  |  |  |  |  |  |  |  |  |

## 8. Zakładając, że poniższe drzewo jest wynikiem grupowania Browna, podaj binarną reprezentację słów evaluation, analysis, house

<center>
  <image src="./brown-tree.png">
</center>

Zakładając trawersal jako `lewo -> 0`, `prawo -> 1`:

- `0000` - evaluation
- `001` - analysis
- `10` - house

## 9. Jaką miarą odległości można szacować podobieństwo pomiędzy kodami Browna?

Kody Browna to hierarchiczne grupowanie słów na podstawie ich częstości występowania w korpusie. W każdym kroku algorytmu grupujemy dwa najczęściej występujące słowa w jedną grupę, a następnie przypisujemy im nowy kod. W ten sposób otrzymujemy hierarchiczne grupowanie słów.

Podobieństwo pomiędzy kodami Browna można szacować za pomocą odległości Hamminga oraz odległości Levenshteina, ew. euklidesową ( liczności słów itp. ).

## 10. Podaj wzór na klasyfikator softmax. Wymień właściwości tej funkcji, a także zademonstruj te właściwoiści albo poprzez odpowiednie wyprowadzenie matematyczne, albo poprzez przykład obliczeniowy

Klasyczny wzór:
$$softmax(x_i) = \frac{e^{x_i}}{\sum\limits_{j=1}^{k}e^{x_j}}$$

Klasyfikator softmax: $$P(\hat{y}=y_i|x) = \frac{e^{w^{T}_i\times +\,b_i}}{\sum\limits_{j=1}^{k}e^{w^{T}_j\times +\,b_j}}$$

Właściwości:

- niezmienność ze wzgl̨edu na dodawanie stałej.
- mozliwość uzyskania tej samej ekspresywności modelu poprzez usunięcie modelu liniowego dla jednej z klas.
- Powyższa właściwość ta pozwala nam pokazać, że dwu-klasowy klasyfikator soft-max jest tożsamy z (dwuklasową) regresją logistyczną oraz na pozbycie się jednego z wektorów $w_i$.
- wymnażając wartości przez dodatnią stałą $c > 1$ softmax dąży do rozkładu z P(y = i|x) = 1 dla pewnego i oraz P(y = j|x) = 0 dla wszystkich innych klas j.
- wymnażając wartości przez dodatnią stałą c <1 softmax dąży do rozkładu jednorodnego.

Dobrze! Zaczynając od właściwości funkcji softmax, rozważmy każdą z nich oddzielnie.

1. Niezmienność ze względu na dodawanie stałej

Załóżmy, że dodajemy stałą \( C \) do każdego elementu \( x \):
\[ \tilde{x_i} = x_i + C \]

Wtedy:
\[ softmax(\tilde{x_i}) = \frac{e^{\tilde{x_i}}} {\sum_{j=1}^{k} e^{\tilde{x_j}}} = \frac{e^{x_i + C}}{\sum_{j=1}^{k} e^{x_j + C}} \]

Korzystając z własności \( e^a \cdot e^b = e^{a+b} \), możemy podzielić górę i dół przez \( e^C \):
\[ \frac{e^{x_i + C}}{\sum_{j=1}^{k} e^{x_j + C}} = \frac{e^{x_i} \cdot e^C}{e^C \sum_{j=1}^{k} e^{x_j}} = \frac{e^{x_i}}{\sum_{j=1}^{k} e^{x_j}} \]
Co jest równoważne pierwotnej definicji softmax dla \( x_i \).

2. Możliwość uzyskania tej samej ekspresywności modelu poprzez usunięcie modelu liniowego dla jednej z klas.

Jeśli założymy \( w_i = 0 \) i \( b_i = 0 \) dla pewnego \( i \), to dla klasy \( i \):
\[ P(\hat{y}=y_i|x) = \frac{e^0}{\sum_{j=1}^{k} e^{w^{T}_j\times + b_j}} = \frac{1}{\sum_{j=1}^{k} e^{w^{T}_j\times + b_j}} \]

Jest to stała względem \( x \). Możemy więc "usunąć" ten model liniowy dla tej klasy, a pozostałe wagi dostosują się, aby uzyskać tę samą ekspresywność.

3. Dwuklasowy klasyfikator softmax jest tożsamy z (dwuklasową) regresją logistyczną.

Dla dwóch klas \( y_1 \) i \( y_2 \), mamy:
\[ P(\hat{y}=y_1|x) = \frac{e^{w^{T}_1\times + b_1}}{e^{w^{T}_1\times + b_1} + e^{w^{T}_2\times + b_2}} \]

Jeśli założymy \( w_2 = 0 \) i \( b_2 = 0 \), to:
\[ P(\hat{y}=y_1|x) = \frac{e^{w^{T}_1\times + b_1}}{e^{w^{T}_1\times + b_1} + 1} \]

To jest forma funkcji sigmoidalnej, co jest podstawą dla regresji logistycznej.

4. Wymnażając wartości przez dodatnią stałą \( c > 1 \)

Załóżmy \( \tilde{x_i} = cx_i \):
\[ softmax(\tilde{x_i}) = \frac{e^{cx_i}}{\sum_{j=1}^{k} e^{cx_j}} \]

Jeśli \( c > 1 \) i \( x_i > x_j \) dla każdego \( j \neq i \), to \( e^{cx_i} \) rośnie szybciej niż \( e^{cx_j} \). W miarę wzrostu \( c \), \( softmax(\tilde{x_i}) \) dąży do 1 dla pewnego \( i \) i 0 dla pozostałych.

5. Wymnażając wartości przez dodatnią stałą \( c < 1 \)

Podobnie jak powyżej, ale gdy \( c < 1 \), wartości w liczniku i mianowniku dążą do siebie nawzajem, co prowadzi do bardziej jednorodnego rozkładu prawdopodobieństwa.

## 11. Przypomnij sobie jak działa algorytm SGD ( stochastycznego spadku wzdłuż gradientu ). W jaki sposób ten algorytm uzyskuje przyśpieszenie nad algorytmem GD (spadku wzdłuż gradientu )? Czym różnią się kierunki/wektory, w których stronę aktualizowane są wagi modeli uczonych SGD od modeli uczonych GD?

Algorytm SGD (stochastic gradient descent) działa poprzez wybieranie losowego podzbioru danych treningowych w każdej iteracji i aktualizowanie wag modelu na podstawie gradientu funkcji kosztu dla tego podzbioru. To sprawia, że ​​jest znacznie szybszy niż algorytm GD (gradient descent), który oblicza gradient dla całego zbioru danych treningowych w każdej iteracji. Przyśpieszenie algorytmu SGD wynika z kilku czynników:

- Redukcja obliczeń gradientu: Algorytm SGD nie musi obliczać gradientu dla całego zbioru danych treningowych, co jest kosztowne obliczeniowo. Zamiast tego, korzysta z losowego podzbioru, co prowadzi do znacznego zmniejszenia wymaganego czasu obliczeniowego.
- Szybsze zbieżność: Dzięki częstym aktualizacjom wag w każdej iteracji, SGD może szybciej zbliżać się do minimum funkcji kosztu. Algorytm GD może wymagać wielu iteracji, zanim osiągnie zbliżone rezultaty.
- Unikanie minimum lokalnych: Losowe próbkowanie danych treningowych pomaga uniknąć utknięcia w minimum lokalnych funkcji kosztu, co może być problemem w przypadku algorytmu GD, który korzysta z całego zbioru danych.

Różnica w kierunkach/wektorach aktualizacji wag między SGD a GD polega na tym, że SGD aktualizuje wagi na podstawie gradientu funkcji kosztu dla losowego podzbioru danych treningowych, podczas gdy GD używa gradientu funkcji kosztu dla całego zbioru danych treningowych. To oznacza, że w każdej iteracji w algorytmie SGD wykorzystywany jest inny gradient, co może prowadzić do większej zmienności w aktualizacjach wag. W GD gradient jest bardziej stabilny, ponieważ opiera się na pełnym zbiorze danych treningowych.

## 12. Dany jest korpus "Ala ma kota. Jurek ma kota.". Używajac kodowania "1 z n" stwórz zbiór treningowy dla klasyfikatora (np. sieci neuronowej), aby móc go wykorzystać w modelu 3 -gramowym języka

Kodowanie: "1 z n" (eng. one-hot encoding) to reprezentacja słów w postaci wektora o długości równej liczbie słów w słowniku. Wartość 1 w wektorze oznacza wystąpienie słowa w zdaniu, a 0 jego brak.

Kroki:

1. Tokenizacja korpusu.
2. Utworzenie listy 3-gramów.
3. Utworzenie słownika one-hot-encoding.
4. Konwersja 3-gramów na wektory one-hot-encoding.

```py
tokeny: [ "Ala", "ma", "kota", "Jurek", "ma", "kota"]

3-gramy: [ "Ala ma kota", "ma kota Jurek", "kota Jurek ma", "Jurek ma kota" ]

słownik: {
  "Ala"             : [1, 0, 0, 0]
  "ma"              : [0, 1, 0, 0]
  "kota"            : [0, 0, 1, 0]
  "Jurek"           : [0, 0, 0, 1]
}
wektory: [
  "Ala ma kota"     : [1, 1, 1, 0]
  "ma kota Jurek"   : [0, 1, 1, 1]
  "kota Jurek ma"   : [0, 1, 1, 1]
  "Jurek ma kota"   : [1, 1, 0, 1]
]
```

## 13. Zakładając, że słowa wejściowe są kodowane "1 z n" rozpisz wzór na klasyfikator softmax dla podanych prawdopodobieństw w modelach n-gramowych. Aby operować na prostszych wzorach możesz skorzystać z notacji "proporcjonalne", w której softmax możemy zapisać jako $P(\hat{y}=y_i|x)\propto w^{T}_i\times +\,b_i$ (prawdopodobieństwo klasy jest proporcjonalne [choć nie wprost] z wynikiem wyrażenia liniowego). Po zapisaniu wzorów postraj się uprościć je tak bardzo jak potrafisz i zinterpretuj je

Załóżmy, że mamy słownik \(V\) o rozmiarze \(|V|\). Wektory \(w^{T}_i\) i skalary \(b_i\) to parametry modelu dla każdego słowa \(i\) w słowniku \(V\).

- Dla modelu bi-gramowego $P(Ala|[start])\propto$

Jeśli weźmiemy pod uwagę bi-gram "[start] Ala", gdzie "[start]" jest poprzednim słowem, a "Ala" jest aktualnym słowem:

\[P(Ala|[start]) \propto w^{T}_{Ala} \times x_{[start]} + b_{Ala}\]

gdzie:

- \(w^{T}_{Ala}\) to wektor wagi dla słowa "Ala"
- \(x_{[start]}\) to zakodowane słowo "[start]" w reprezentacji "1 z n"
- \(b_{Ala}\) to bias dla słowa "Ala"

- Dla modelu tri-gramowego $P(kota|Ala,ma)\propto$

Jeśli rozważymy tri-gram "Ala ma kota", gdzie "Ala" i "ma" są poprzednimi słowami, a "kota" jest aktualnym słowem:

\[P(kota|Ala,ma) \propto w^{T}_{kota} \times (x_{Ala} + x_{ma}) + b_{kota}\]

gdzie:

- \(x_{Ala}\) i \(x_{ma}\) to zakodowane słowa "Ala" i "ma" w reprezentacji "1 z n"

Interpretacja: Klasyfikator softmax w modelach n-gramowych używa liniowych kombinacji parametrów (wag i biasów) wraz z zakodowanymi reprezentacjami słów w kontekście, aby oszacować prawdopodobieństwo następnego słowa w sekwencji.

## 14. W kontekście modeli n-gramowych uczonych przez zliczanie ( z technikami rozmywania estymat ) oraz na podstawie zapisu z poprzedniego ćwiczenia, dokonaj interpretacji działania klasyfikatora softmax w modelu języka i porównaj  jego działanie do modeli uczonych przez zliczanie

W modelach n-gramowych uczonych przez zliczanie, prawdopodobieństwa są obliczane na podstawie częstości występowania danego n-gramu w danych uczących. W przypadku klasyfikatora softmax w modelu języka, prawdopodobieństwa są obliczane na podstawie optymalizacji funkcji kosztu (np. entropia krzyżowa) w procesie uczenia.

Porównanie

- Modele przez zliczanie: Proste, deterministyczne, oparte na częstości występowania n-gramów. Mogą cierpieć z powodu problemu zerowego prawdopodobieństwa (rozwiązane przez techniki wygładzania).
- Klasyfikator softmax: Elastyczniejszy, pozwala na uczenie się skomplikowanych zależności między słowami. Wymaga optymalizacji w procesie uczenia.

## 15. Dane są trzy modele 3-gramowe

- standardowy tj. oparty o zliczanie
- zbudowany na klasyfikatorze softmax i reprezentacji "1 z n"
- zbudowany na klasyfikatorze MLP i reprezentacji "1 z n". Rozważane MLP to dwuwarstwowa sieć neuronowa ( tylko jedna warstwa ukryta ) z h = 500 neuronami ukrytymi, a ostatnia warstwa to softmax.

Przyjmując $|V|=50\,000$  oszacuj liczbę parametrów w każdym z tych modeli. Który z tych modeli jest najmniejszy w sensie liczby parametrów? Który z tych modeli jest najbardziej ekspresywny?

Liczba parametrów dla poszczególnych modeli:

1. Standardowy model oparty o zliczanie: Teoretycznie potrzebuje przetrzymać prawdopodobieństwo dla każdego możliwego 3-gramu, czyli \(|V|^3\). W praktyce jednak nie wszystkie kombinacje 3-gramów będą występować, więc rzeczywista liczba parametrów będzie mniejsza.

2. Klasyfikator softmax i reprezentacja "1 z n": Dla każdego słowa w \(V\) mamy wektor wag o rozmiarze \(|V|\) (dla poprzedniego słowa) i bias, czyli \(2|V|^2\).

3. Model z MLP:
   - Wejście do pierwszej warstwy ukrytej: \(|V| \times h = 50,000 \times 500 = 25,000,000\)
   - Bias dla pierwszej warstwy ukrytej: \(h = 500\)
   - Wejście do warstwy softmax z warstwy ukrytej: \(h \times |V| = 500 \times 50,000 = 25,000,000\)
   - Bias dla warstwy softmax: \(|V| = 50,000\)

Łącznie dla MLP: \(25,000,500 + 25,050,000 = 50,050,500\)

Podsumowanie:

- Najmniejszy w sensie liczby parametrów: Model standardowy (choć w praktyce różnica może być nieznaczna w porównaniu z klasyfikatorem softmax, w zależności od rzeczywistej liczby unikalnych trigramów)
- Najbardziej ekspresywny: Model z MLP, ponieważ ma najwięcej parametrów i może uczzyć się bardziej złożonych zależności między słowami
