1.

We have $A\times B = \{(a, b)\mid a\in A \text{ and } b\in B\}$

$A\times B = \{1,2,3\}\times\{\text{green}, \text{blue}\} = \{(1, \text{green}), (1, \text{blue}),(2, \text{green}), (2, \text{blue}),(3, \text{green}), (3, \text{blue})\}$

$A\times \empty = \empty$

$\mathscr{P} (B) = \{\empty, \{\text{green}\}, \{\text{blue}\}, \{\text{green, blue}\}\}$

 We have $|A\times B| = |A||B|$  and $|A\times(A\times B)| = |A||A\times B| = |A||A||B| = 3\times 3 \times 2 = 18$

The typical element of $A\times B$ is $(a,b)$ where $a\in A$ and $b\in B$.

Then the typical element of $A\times(A\times B)$ is $(a_1, (a_2, b))$ where $a_1, a_2\in A$ and $b\in B$. Note that $a_1\in A$ and $(a_2, b)\in A\times B$.

2.

(a) $\{1 + 3n : n\in \mathbb{Z}\}$

(b) $\{\frac{1}{2^n}:n\in \mathbb{N}\}$

3.

(a) $\{0, 2, -2\}$

(b) We have $\mathscr{P} (\empty) = \{\empty\}$, then $\mathscr{P} (\mathscr{P} (\empty) ) = \mathscr{P} (\{\empty\}) = \{\empty, \{\empty\}\}$.

(c) We have $\mathscr{P} (\{1,2,3,4\}) = \{\empty, \{1\}, \{2\}, \{3\}, \{4\}, \{1,2\}, \{1,3\}, \{1,4\}, \{2,3\}, \{2,4\}, \{3,4\},\{1,2,3\},\{1,2,4\},\{1,3,4\},\{2,3,4\}, \{1,2,3,4\}\}$

For all $X\in \mathscr{P} (\{1,2,3,4\})$, we need $|X|\leq 2$. Then $|X| = 0, 1 \text{ or } 2$.

Hence, $X = \empty, \{1\}, \{2\}, \{3\}, \{4\}, \{1,2\}, \{1,3\}, \{1,4\}, \{2,3\}, \{2,4\} \text{ or } \{3,4\}$.

We conclude the answer is $\{\empty, \{1\}, \{2\}, \{3\}, \{4\}, \{1,2\}, \{1,3\}, \{1,4\}, \{2,3\}, \{2,4\} \text{ or } \{3,4\}\}$.

4.

5.

Let $A_i = \left(\frac{1}{i}, 2-\frac{1}{i}\right]$.

For any $m, n\in \mathbb{N}$ and $m<n$, we have $A_m = \left(\frac{1}{m}, 2-\frac{1}{m}\right], A_n = \left(\frac{1}{n}, 2-\frac{1}{n}\right]$.

Since $m<n$, $\frac{1}{m} > \frac{1}{n}$. Then $-\frac{1}{m} < -\frac{1}{n}$. Therefore, $2-\frac{1}{m} <2 - \frac{1}{n}$.

Then we have $\frac{1}{n} < \frac{1}{m}$ and $2-\frac{1}{m} <2 - \frac{1}{n}$, which implies that $A_m\subset A_n$.

Note that for any $k\in\mathbb{N}$, $A_{k - 1}\subset A_k, A_{k-2} \subset A_{k-1}, \cdots, A_1\subset A_2$.

Then $A_1\subset A_2\subset \cdots\subset A_{k-2}\subset A_{k-1}\subset A_k$.

Hence, as $i$ increases, the interval $A_i$ becomes wider and is the superset of $A_j$ for $j\in [1, i-1]$.

Then when $i$ approaches infinity, $A_i$ is widest.

We have $\lim_{i\rightarrow \infty} \frac{1}{i} = 0$ and $\lim_{i\rightarrow \infty} 2 -\frac{1}{i} = 2$.

Hence, the widest interval is $(0,2]$.

We conclude that the interval represented by the infinite union is $\cup_{i = 1}^n \left(\frac{1}{i}, 2 - \frac{1}{i}\right]$ is $(0,2]$. 





