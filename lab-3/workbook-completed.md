# Zadania

## 1. Słowa w macierzy zanurzeń mają następujące reprezentacje: Ala $(-1,0)$, Jurek $(1,0)$, ma $(1,1)$, kota $(-1, 1)$, i $(-0.5,-0.5)$, psa $(-1.1, 1.1)$. Rozważamy sieć splotową z jednym filtrem bigramowym (1, 1; -1, 1), funkcję katywacji $ReLU$ oraz funkcję redukcji $k-Max$ z $k=2$. Wynik funkcji redukcji jest następnie przetwarzany przez warstwę softmax

### (a) Jaka reprezentacja zdania "Ala ma kota i ma psa" jest podawana na wejście warstwy softmax? ( Kolejne wiersze macierzy wag filtra pokrywają się z kolejnymi słowami na weścju )

### (b) Jaki n-gram jest wykrywany przez filtr?

### (c) Jak zmieniłoby się wejście warstwy softmax gdyby zastosować dynamiczną funkcję redukcji?

### (d) Zakładając, że sieć rozszerzamy o dwa dodatkowe filtry unigramowe ( w ramach już istniejącej warstwy ) o wagach $(0, 1)$ i $(2, -1)$ - oblicz wejście do warstwy softmax po funkcji redukcji $k-Max$ z $k=2$

### (e) Czy funkcje redukcji "over time" takie jak $k-Max$ można stosować pomiędzy kolejnymi warstwami sieci splotowej dla tekstu?

## 2. Projektujesz agenta dialogowego do zamawiania pizzy. Zaprojektuj schemat tagowania sekwencji, który pozwoliłby na wykrycie wybranych przez Ciebie relewantnych dla systemu informacji. Otaguj zgodnie z nim następujący korpus, wykorzystując schemat BIO

Korpus:

- Chciałbym margheritę na grubym cieście.
- Dwa razy pepperoni na cienkim.
- Na wynos, pizze z pieczarkami i zielonymi oliwkami.
- Jedną małą pizzę z tuńczykiem, kukurydzą, karmelizowaną cebulą.

nasze BIO składa się z

- Smak
- Ciasto
- Ilość
- Rozmiar
- Dostawa
- Other

Przez co możemy to otagować jako

- Chciałbym(O) margheritę(B-S) na(O) grubym(B-C) cieście(O).
- Dwa(B-I) razy(O) pepperoni(S) na(O) cienkim(B-C).
- Na(B-D) wynos(I-D), pizze(O) z(O) pieczarkami(B-S) i(O) zielonymi(B-S) oliwkami(I-S).
- Jedną(B-I) małą(B-R) pizzę(O) z(O) tuńczykiem(B-S), kukurydzą(B-S), karmelizowaną(B-S) cebulą(I-S).

## 3. Mając poniższy korpus uczący

- Ala [N] ma [V] kota [N]
- Jacek [N] lubi [V] pluszowe [JJ] misie [N].

Policz prawdopodobieńtstwo sekwencji: "Ala [N] lubi [V] misie [N]" wg. bigramowego ukrytego modelu Markowa.

Sekwencje liczmy jako
$$P(x_1^n,y_1^n)=\prod\limits_{i=1}^nP(x_i|y_i)\prod^{n+1}_{i=1}P(y_i|y_{i-1})$$
Co się sprowadza do policzenia
$$ P(N|[Start])\cdot(V|N)\cdot(P|V)\cdot P(N|[Stop])\cdot P(Ala|N)\cdot P(lubi|V)\cdot P(misie|N)$$

Co robimy poprzez wyznaczenie prawdopodobieństw na korpusie jako zliczone pary (Słowo | Tag) oraz (Tag | Tag) i podzielenie ich przez sumę wszystkich wystąpień danego tagu.

$$
P(N|[Start])\cdot P(V|N)\cdot P(N|V)\cdot P(N|[Stop])\cdot P(Ala|N)\cdot P(lubi|V)\cdot P(misie|N)\\
= 1\cdot\frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{2}\cdot\frac{1}{1}\cdot\frac{1}{4}\cdot\frac{1}{2}\cdot\frac{1}{4}=\frac{1}{256}
$$

## 4. Rozważ korpus uczący

- I [O] book [V] a [O] flight [N].
- Dad [N] reads [V] a [O] book [N].
- Big [O] company [N] books [V] flights [N].
- I [O] like [V] A [N] company [N].

Zakładajac, że w korpusie uczącym zamieniono wszystkie duże litery na małe oraz usunięto literkę "s" jeśli znajdowała się na końcu wyrazu ( pozbycie się liczby mnogiej i odmiany czasowników ), wytrenuj bigramowy ukryty model Markowa, a następnie dokonaj predykcji algorytmem Viterbiego dla zdania "I book a book".

Korpus po zmianach

- i [O] book [V] a [O] flight [N].
- dad [N] read [V] a [O] book [N].
- big [O] company [N] book [V] flight [N].
- i [O] like [V] a [N] company [N].

Wzór: $Emisja\cdot \max\{Tranzycja,\,Bufor\}$, $P(Słowo|PoS)\cdot\max\{P(PoS_i|PoS_{i-1})\cdot bufor\}$

- B1 - i
N - $P(i|N) \cdot P(N|[start]) = ...\cdot 0 = 0$
V - $P(i|V) \cdot P(V|[start]) = 0\cdot ... =0 $
O - $P(i|O) \cdot P(O|[start]) = 2/5 \cdot 3/4 = 3/10$
[stop] - $0$

> Buffor = B1(PoS) = {N,V,O,[stop]} = {0,0,3/10,0}

- B2 - book
N - $P(book|N)\cdot \max\{B1(N|PoS)\cdot P(N|PoS)\}=P(book|N)\cdot \max\{B1(N|N)\cdot  P(N|N),B1(N|V)\cdot P(N|V),B1(N|O)\cdot P(N|O),B1(N|[stop])\cdot P(N|[stop])\}=1/7\cdot \max\{0,0,3/10\cdot P(N|O),0\} = 1/7\cdot 3/10\cdot 3/5 =9/350$
V - $P(book|V)\cdot \max\{B1(V|PoS)\cdot P(V|PoS)\}= 2/4\cdot \max\{B1(V|O)\cdot P(V|O)\}=1/2\cdot 3/10\cdot 2/5 = 3/50$
O - $P(book|O)\cdot \max\{B1(O|PoS)\cdot P(O|PoS)\}= 0\cdot...=0$
[stop] - $0$

> Bufor - B2(PoS) = {N,V,O,[stop]} = {9/350,3/50,0,0}

- B3 - a

N - $P(a|N)\cdot \max\{B2(PoS)\cdot P(N|PoS)\}=1/7\cdot \max\{9/350\cdot P(N|N), 3/50\cdot P(N|V)\}=1/7\cdot \max\{9/350 \cdot 1/7, 3/50\cdot 2/4\}=1/7\cdot 2/4 \cdot 3/50 = 3/700$
V - $0\cdot...=0$
O - $2/5\cdot ...= 3/100\cdot 2/5 = 3/250$
[stop] - $0$

- B4 - book

N - $...=9/8750$
V - $...=3/1250$
O - $...=0$
[stop] - $0$

- B5 - [stop]

N - $...=0$
V - $...=0$
O - $...=0$
[stop] - $...=18/30625$

Predykcja: Przechodzimy od tyłu co głosowaliśmy jako najprawdobodobniejsze

I(O) book(V) a(O) book(N)

## 5. Podaj korpus uczący, dla którego klasyfikator HMM popełni choć jeden błąd ( na korpusie uczącym )

- [O] [O] [A] [O] [O]

Ponieważ P(O|O) ma większe prawdopodobieństwo niż P([stop]|O), to algorytm może wypluwać cały czas [O].

## 6. Zapisz wzór na algorytm Viterbiego dla modelu MEMM z reprezentacją cech opartą na poprzednim tagu i aktualnym słowie

$$\max^Y_{y} \prod^N_{i=1} P(y_i|y_{i-1}, x)$$
$$\max^Y_y P(y_N|y_{N-1}, x) \cdot P(y_{N-1}|y_{N-2}, x)\cdot ... \cdot \max_{y_1}P(y_2|y_1,x)\cdot P(y_1|Start,x)=$$

Możemy zabuforować końcówki słów i tagów, żeby nie liczyć ich za każdym razem jako $B_1(y_1)$ co pozwala na skrócenie wzoru do

$$\max_{y_2} P(y_3|y_2,x) \max_{y_1} P(y_2|y_1,x) B_1(y_1)$$

Co możemy dalej skrócić przez zabuforowanie $B_2(y_2)$ co dalej transformuje wyrażenie do

$$\max_{y_n} B_n(y_n)$$

## 7. Zapisz wzór na algorytm Viterbiego dla modelu trzygramowego HMM

## 8. Rozważając korpus uczącyh z zadania 3, zapisz w postaci tabelki zbiór uczący klasyfikatora MEMM

## 9. Aby otagować n-elementową sekwencję modelem MEMM - ile razy należy wykorzystać klasyfikator? Opisz przebieg predykcji zachłannej przez ten model

## 10. Projektujemy klasyfikator softmax przypisujący część mowy dla danego słowa $P(PoS|word)$. Rozważane części mowy to $PoS \in \{N, V, JJ\}$, a $V=\{\text{być, mieć, złoto, tabletka, piękny, żółty}\}$. Podaj minimalny zbiór cech binarnych $\phi(x, y)$, który może zamodelować następujący rozkład

$$P(JJ|\text{żółty})=0.6\;\;P(N|tabletka)=0.8\;\;P(V|\text{być})=0.99$$
$$P(JJ|\text{mieć})=P(JJ|\text{złoty})=P(JJ|\text{piękny})=0.4$$

pozostałe wartości rozkładu nie są dla nas interesujące (mogą przyjąć dowolną wartość).

## 11. Rozważmy model softmax $\sigma(x)_y=\frac{e^{W^{T}\phi(x,y)}}{\sum\limits_{x'}e^{W^{T}\phi(x,y')}}$, który jest nauczony poprzez maksymalizację logarytmicznej funkcji wiarygodności wraz z termem regularyzacyjnym L2. Załóż, że w czasie optymalizacji osiągnięto optimum funkcji celu. Odpowiedz na poniższe pytania i uzasadnij

Mem, wszystko się znosi.

### (a) Zakładając cechę $\phi_1(x,y)=0$, dla każdego $x\in X$ oraz $y\in Y$, ile wynosi wartość $w_1$?

$w_1 = 0$, ponieważ nie ma żadnego wpływu na wynik

### (b) Zakładając cechę $\phi_2(x,y)=1$, dla każdego $x\in X$ oraz $y\in Y$, ile wynosi wartość $w_2$?

$w_2 = 0$, ponieważ nie ma żadnego wpływu na wynik

### (c) Zakładając cechę $\phi_3(x,y)=idx(x)$, dla każdego $x\in X$ oraz $y\in Y$, gdzie funkcja idx() przypisuje kolejnym wektorom kolejne liczby naturalne - ile wynosi wartość $w_3$?

$w_3 = 0$, ponieważ nie ma żadnego wpływu na wynik

### (d) Utworzono zestaw cech $\phi_i(x,y)=1_{x=x'\wedge\, y=y'}$, po jednej cesze dla każdej $x'\in X$ oraz $y'\in Y$. Zakładając cechę bez pokrycia $\phi_j(x,y)$ (tj. cecha ta nie akywuje się ani razu w zbiorze uczącym). Jakie są wartości $w_j$?

$w_j = 0$, ponieważ nie ma żadnego wpływu na wynik i nie jest aktywowana

## 12. Czy do klasyfikacji wieloklasowej możemy zastosować zamiast warstwy softmax, warstwę złożoną z neuronów logistycznych? W jaki sposób taka sieć byłaby trenowana? Jakie są zalety stosowania warstwy sofrtmax zamiast zwykłych neuronów logistycznych?

## Słowniczek

- BIO - Algorytm tagowania do rozpoznawania encji nazwanych ( Named Entity Recognition, NER )
  - BIO składa się z ( B - Begin, I - Inside, O - Outside )
  - B - początek encji
  - I - środek encji
  - O - brak encji
- BIOES - Rozszerzenie algorytmuy BIO o rozpoznawanie pojedynczych encji
  - BIOES składa się z ( B - Begin, I - Inside, O - Outside, E - End, S - Single )
  - B - początek encji
  - I - środek encji
  - O - brak encji
  - E - koniec encji
  - S - pojedyncza encja
