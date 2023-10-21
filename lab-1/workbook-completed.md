# Zadania

## 1. Podaj wzór na prawdopodobieństwo warunkowe, a następnie wyprowadź regułę łańcuchową prawdopodobieństwa

Pradopodobieństwo warunkowe $P(X|Y)$ jest zdefiniowane jako:
$$P(X|Y)=\frac{P(X,Y)}{P(Y)}$$

Reguła łańcuchowa prawdopodobieństwa:
Założenia:
$$P(X,Y)=P(X|Y)P(Y)$$
Symetria:
$$P(A), P(B) > 0: P(A|B)P(B)=P(B|A)P(A)$$

$$P(x_1,x_2,x_3,\dots,x_n)=P(x_1,x_2,x_3,\dots,x_{n-1}|x_n)\cdot P(x_n)=P(x_n|x_1,x_2,x_3,\dots,x_{n-1})\cdot P(x_1,x_2,x_3,\dots,x_{n-1})=\prod_{i=1}^{n}P\left(x_{i}|\bigcap_{j=1}^{i-1}x_j\right)$$

$$P(x_1,x_2,x_3,x_4)=P(x_4|x_1,x_2,x_3)P(x_3|x_1,x_2)P(x_2|x_1)P(x_1)$$

## 2. Zastosuj regułę łańcuchową do prawdopodobieństwa P(A, B, C, D)

$$P(A,B,C,D)=P(A,B,C)P(D|A,B,C)=P(D|A,B,C)P(C|A,B)P(B|A)P(A)$$

## 3. Wyraź $P(w_2, w_3, w_4 | w_1, w_0)$ tylko za pomocą rozkładu łącznego

$$P(w_2, w_3, w_4|w_1, w_0) = \frac{P(w_0,w_1,w_2,w_3,w_4)}{P(w_0, w_1)}=\frac{P(w_4|w_0,w_1,w_2,w_3)P(w_3|w_0,w_1,w_2)P(w_2|w_0,w_1)P(w_1|w_0)P(w_0)}{P(w_1|w_0)P(w_0)}=P(w_4|w_0,w_1,w_2,w_3)P(w_3|w_0,w_1,w_2)P(w_2|w_0,w_1)$$

## 4. Mając następujący zbiór uczący uzyskany z rzutów kostką sześcienną

$$1,1,5,2,2,6,2,3,6,3,4$$
Wyestymuj prawdopodobieństwo uzyskania poniższych wartości:
$$P(X=1)=\frac{2}{11}\;\;\;\;\;\;P(X=2)=\frac{3}{11}\;\;\;\;\;\;P(X=3)=\frac{2}{11}\;\;\;\;\;\;P(X=4)=\frac{1}{11}\;\;\;\;\;\;P(X=5)=\frac{1}{11}\;\;\;\;\;\;P(X=6)=\frac{2}{11}\;\;\;\;\;\;$$
Następnie zakładając, że podany zbiór jest sekwencją policz prawdopodobieństwa występowania po sobie różnych wartości $P(X_t|X_{t-1})$
$$P(X_t=2|X_{t-1}=6)=\frac{1}{2}\;\;\;\;\;\;P(X_t=1|X_{t-1}=1)=\frac{1}{2}\;\;\;\;\;\;P(X_t=3|X_{t-1}=2)=\frac{1}{3}\;\;\;\;\;\;P(X_t=1|X_{t-1}=5)=\frac{0}{1}\;\;\;\;\;\;$$

## 5. Dla podaneego zbioru trzech sekwencji: "Ala ma kota", "Jurek ma kota", "Kamil ma psa" wyznacz prawdopodobieństwo sekwencji "Ala ma kota" i "Kamil ma kota"

$$P(Ala\,ma\,kota)=\frac{1}{3}$$
$$P(Kamil\,ma\,kota)=\frac{0}{3}$$

## 6. Za rozmiar słownika przyjmij $|V|$ i spróbuj obliczyć liczbę parametrów: "pełnego" rozkładu $P(w_1,w_2,w_3,...,w_n)$ (tj. rozkładu łącznego przed zastosowaniem reguły łańcuchowej) oraz tego samego rozkładu po zastosowaniu reguły łańcuchowej

Liczba parametrów pełnego rozkładu wynosi: $|V|^n - 1$. Jedno prawdopodobienswo jest obliczalne na podstawie pozostałych, więc odejmujemy 1.

Liczba parametrów rozkładu po zastosowaniu reguły łańcuchowej wynosi:
$$|V|\times \frac{|V|^n-1}{|V|-1}$$

## 7. Wyjaśnij na czym polega założenie Markowa

Założenie Markowa polega na pominięciu części informacji o przeszłości, która nie jest istotna dla przewidywania przyszłości. W przypadku modeli językowych założenie Markowa polega na tym, że prawdopodobieństwo wystąpienia słowa zależy tylko od określonej liczby poprzedzających go słów, a nie od całej historii.

## 8. Zapisz rozkład sekwencji $P(w_1, w_2, w_3, ..., w_n)$ przy użyciu reguły łańcuchowej i założenia Markowa trzeciego rzędu

$$P(w_1, w_2, w_3, \dots, w_n)=\prod_{i=1}^{n}P(w_i|w_{i-1},w_{i-2})P(w_2|w_1)P(w_1)$$

## 9. Korzystając z postaci rokzładu uzyskanej w poprzednim zadaniu - w jaki sposób wygenerować losową sekwencje?

Aby wygenerować losową sekwencje należy wylosować pierwsze słowo z rozkładu $P(w_1|[start],[start])$, następnie wylosować drugie słowo z rozkładu $P(w_2|[start],w_1)$, kolejne słowo wylosować z rozkładu $P(w_3|w_1,w_2)$ itd aż do uzyskania tokenu stop.

## 10. Zakładając modelowanie rozkładu prawdopodobieństwa z założeniem Markowa drugiego rzędu na zbiorze sekwencji "Ala ma kota", "Jurek ma kota", "Kamil ma psa", oblicz prawdopodobieństwo sekwencji "Kamil ma kota"

Należy wyznaczyć prawdopodobieństwa: $P([Stop]|kota), P(kota|ma), P(ma|Kamil), P(Kamil|[Start])$ i obliczyć jako produkt.
$$P(Kamil\,ma\,kota)=P(Kamil|[Start])\cdot P(ma|Kamil)\cdot P(kota|ma)\cdot P([Stop]|kota)=\frac{1}{3}\times 1\times \frac{1}{3}\times 1=\frac{1}{9}$$

## 11. Zakładając, że w n-elementowych sekwencjach występuje $|V|$ unikalnych słów - ile parametrów będzie miał model z założeniem Markowa rzędu: pierwszego, drugiego, trzeciego i czwartego?

- Pierwszego $-$ $|V|$
- Drugiego $-$ $|V|^2$
- Trzeciego $-$ $|V|^3$
- Czwartego $-$ $|V|^4$

## 12. Rozważ ponizej zwizualizowany 4-elementowy zbiór danych i wykonaj na nim operację grupowania algorytmem AHC. Zastosuj metrykę Manhatańską oraz single-linkage. Wyniki gruypowania przedstaw na dendogramie

<center>
  <image width="280" height="280" src="./data-set.png">
</center>

1. AHC - Agglomerative Hierarchical Clustering
2. Obliczanie odległości między klastrami
3. Single-linkage - odległość między klastrami jest równa odległości między najbliższymi punktami w klastrach
4. Dendogram - graficzna reprezentacja hierarchicznej struktury grupowania
5. Metryka manhattańska - odległość między punktami jest równa sumie wartości bezwzględnych różnic współrzędnych punktów Wzór: $d(x,y)=\sum_{i=1}^{n}|x_i-y_i|$
Punkty:

- $a = (2, 3)$
- $b = (2, 4)$
- $c = (3, 4)$
- $d = (4, 0)$

Rozwiązanie:

1. Obliczamy odległości między punktami

- $d(a,b) = 1$
- $d(a,c) = 2$
- $d(a,d) = 5$
- $d(b,c) = 1$
- $d(b,d) = 6$
- $d(c,d) = 5$

Tworzymy klaster:
{a,b,c}, ponieważ odległość między najbliższymi punktami wynosi 1.
następnie łączony jest w klaster {a,b,c,d}.
Co daje nam dendogram:

<center>
 <image width="280" height="280" src="dendogram.png">
</center>
