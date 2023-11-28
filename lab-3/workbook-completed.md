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
- IlośćadP
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

## 4. Rozważ korpus uczący

- I [O] book [V] a [O] flight [N].
- Dad [O] reads [V] a [O] book [N].
- Big [O] company [N] books [V] flights [N].
- I [O] like [V] A [N] company [N].

Zakładajac, że w korpusie uczącym zamieniono wszystkie duże litery na małe oraz usunięto literkę "s" jeśli znajdowała się na końcu wyrazu ( pozbycie się liczby mnogiej i odmiany czasowników ), wytrenuj bigramowy ukryty model Markowa, a następnie dokonaj predykcji algorytmem Viterbiego dla zdania "I book a book".

## 5. Podaj korpus uczący, dla którego klasyfikator HMM popełni choć jeden błąd ( na korpusie uczącym )

## 6. Zapisz wzór na algorytm Viterbiego dla modelu MEMM z reprezentacją cech opartą na poprzednim tagu i aktualnym słowie

## 7. Zapisz wzór na algorytm Viterbiego dla modelu trzygramowego HMM

## 8. Rozważając korpus uczącyh z zadania 3, zapisz w postaci tabelki zbiór uczący klasyfikatora MEMM

## 9. Aby otagować n-elementową sekwencję modelem MEMM - ile razy należy wykorzystać klasyfikator? Opisz przebieg predykcji zachłannej przez ten model

## 10. Projektujemy klasyfikator softmax przypisujący część mowy dla danego słowa $P(PoS|word)$. Rozważane części mowy to $PoS \in \{N, V, JJ\}$, a $V=\{\text{być, mieć, złoto, tabletka, piękny, żółty}\}$. Podaj minimalny zbiór cech binarnych $\phi(x, y)$, który może zamodelować następujący rozkład

$$P(JJ|\text{żółty})=0.6\;\;P(N|tabletka)=0.8\;\;P(V|\text{być})=0.99$$
$$P(JJ|\text{mieć})=P(JJ|\text{złoty})=P(JJ|\text{piękny})=0.4$$

pozostałe wartości rozkładu nie są dla nas interesujące (mogą przyjąć dowolną wartość).

## 11. Rozważmy model softmax $\sigma(x)_y=\frac{e^{W^{T}\phi(x,y)}}{\sum\limits_{x'}e^{W^{T}\phi(x,y')}}$, który jest nauczony poprzez maksymalizację logarytmicznej funkcji wiarygodności wraz z termem regularyzacyjnym L2. Załóż, że w czasie optymalizacji osiągnięto optimum funkcji celu. Odpowiedz na poniższe pytania i uzasadnij

### (a) Zakładając cechę $\phi_1(x,y)=0$, dla każdego $x\in X$ oraz $y\in Y$, ile wynosi wartość $w_1$?

### (b) Zakładając cechę $\phi_2(x,y)=1$, dla każdego $x\in X$ oraz $y\in Y$, ile wynosi wartość $w_2$?

### (c) Zakładając cechę $\phi_3(x,y)=idx(x)$, dla każdego $x\in X$ oraz $y\in Y$, gdzie funkcja idx() przypisuje kolejnym wektorom kolejne liczby naturalne - ile wynosi wartość $w_3$?

### (d) Utworzono zestaw cech $\phi_i(x,y)=1_{x=x'\wedge\, y=y'}$, po jednej cesze dla każdej $x'\in X$ oraz $y'\in Y$. Zakładając cechę bez pokrycia $\phi_j(x,y)$ (tj. cecha ta nie akywuje sięani razu w zbiorze uczącym). Jakie są wartości $w_j$?

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
- 