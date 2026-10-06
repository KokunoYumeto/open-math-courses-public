# Noetherian polynomial rings and finite-type algebras

[Component notice and licence](NOTICE.md). Adapted from the exact [00FN statement and proof](00FN-proof.tex), with the elementary completions identified below. All rings here are commutative with a unit; homomorphisms preserve it. Natural-number induction and ordinary set-theoretic choice are the foundational conventions.

<a id="noetherian-permanence"></a>

## The statement

If every ideal of a ring $R$ is finitely generated, the same is true of $R[X]$, every finite-type $R$-algebra, and every localization $S^{-1}R$. Thus every ideal of $\mathbb C[X_1,\ldots,X_n]$ is finitely generated. This includes the zero ideal and the zero ring.

<a id="algebra-rings-and-fractions"></a>

## Elementary completion: the ring constructions

The polynomial ring consists of finite coefficient sequences, with coefficientwise addition and the convolution product. Finite distributivity proves its ring laws. Over a domain, the product of two nonzero one-variable polynomials has degree equal to the sum of the degrees, because its leading coefficient is the product of two nonzero coefficients. Iterating this observation shows that a polynomial ring in finitely many variables over a domain is a domain. Evaluation at commuting elements preserves sums and products.

For an ideal $I$, the quotient $R/I$ consists of additive cosets. If representatives are changed by elements of $I$, their sums and products change by elements of $I$: for products expand $(r+i)(s+j)-rs=rj+is+ij$. Thus the quotient operations are well-defined and inherit the ring laws. The kernel of a ring homomorphism is an ideal; a surjective homomorphism induces a bijection from the quotient by its kernel to its target, preserving both operations. Indeed equal images mean precisely that the representatives differ by a kernel element. A proper ideal is prime exactly when its quotient is a nonzero domain, by the definition that $rs\in I$ forces $r\in I$ or $s\in I$.

Here is the localization construction, including rings with zero divisors. Let $S$ be a multiplicatively closed subset containing $1$. On pairs $(r,s)\in R\times S$ set

$$
 \begin{gathered}
 (r,s)\sim(a,b)\quad\Longleftrightarrow\\
 u(rb-as)=0\text{ for some }u\in S.
 \end{gathered}
$$

Reflexivity and symmetry are immediate. For transitivity, multiply
$b(rc-ds)=c(rb-as)+s(ac-db)$ by witnesses annihilating the two terms on the right. The resulting witness for $(r,s)\sim(d,c)$ is their product times $b$, which belongs to $S$. Write $r/s$ for the class and define

$$
 \frac r s+\frac q t=\frac{rt+qs}{st},
 \qquad
 \frac r s\frac q t=\frac{rq}{st}.
$$

These formulas respect representatives. If $u(rb-as)=0$, the cross-multiplied difference for adding $q/t$ to $r/s$ and $a/b$ is $t^2(rb-as)$; for multiplication it is $qt(rb-as)$. The same witness annihilates both. Replace the other argument in turn. Negation respects the relation as well. Passing finitely many terms to a common denominator proves the ring laws by those of $R$; $0/1$ and $1/1$ are its zero and unit. The map $r\mapsto r/1$ is a homomorphism, and $s/1$ has inverse $1/s$ for every $s\in S$. If $0\in S$, all classes coincide and this gives the zero ring, as required.

If $R$ is a nonzero domain and $S=R\setminus\{0\}$, the relation reduces to $rb=as$. The map $R\to S^{-1}R$ is injective. A nonzero fraction $r/s$ has $r\ne0$ and inverse $s/r$, so this is a field, the fraction field. Any field containing $R$ contains these fractions with the same operations; hence the fraction field is the smallest such field. This supplies the fraction fields used in the critical-values argument.

<a id="noetherian-ascending-chains"></a>

## Elementary completion: finite generation and ascending chains

An ideal is an additive subgroup closed under multiplication by arbitrary ring elements. It is finitely generated if it consists of the finite sums $\sum_{j=1}^m r_ja_j$ for some fixed $a_1,\ldots,a_m$.

If every ideal is finitely generated and $I_1\subset I_2\subset\cdots$, their union $I$ is an ideal. Its finitely many generators all lie in one $I_k$, so $I=I_k$ and the chain stabilizes. Conversely, if an ideal $I$ has no finite generating set, choose $a_1\in I$ and recursively choose $a_{j+1}\in I\setminus(a_1,\ldots,a_j)$. The resulting strictly ascending chain contradicts the ascending chain condition (ACC). Consequently the two definitions of Noetherian ring agree.

## Elementary completion of the source's $\mathbb N^2$ hint

Every infinite sequence of natural numbers has an infinite nondecreasing subsequence. If some value appears infinitely often, take that constant subsequence. Otherwise every bounded set of values appears only finitely often; recursively choose later terms larger than the last one. Apply this first to the first coordinates of a sequence of distinct pairs, and then to the second coordinates of the resulting subsequence. This gives an infinite subsequence nondecreasing in both coordinates. In particular every infinite subset of $\mathbb N^2$ contains an infinite increasing sequence of distinct pairs. Therefore a family of ideals increasing in both indices cannot assume infinitely many distinct values in a Noetherian ring: choosing one pair for each of infinitely many different ideals and applying this argument would produce a strictly ascending chain of ideals.

The uniform stabilization needed below also has the following direct proof. For ideals $I_{i,d}$ increasing in both indices, the diagonal chain $I_{k,k}$ stabilizes, say at $I_{K,K}=J$. For $i,d\geq K$, sandwich $I_{i,d}$ between $I_{K,K}$ and $I_{\max(i,d),\max(i,d)}$, so it equals $J$. For each of the finitely many $d<K$, the chain in $i$ stabilizes. Choose $i_0\geq K$ greater than all those stabilization indices. Then $I_{i,d}=I_{i_0,d}$ for every $i\geq i_0$ and every $d\geq0$.

<a id="noetherian-polynomial-proof"></a>

## Polynomial-ring proof

Let $J_1\subset J_2\subset\cdots$ be ideals of $R[X]$. Define $I_{i,d}$ to be the coefficients of $X^d$ in polynomials of $J_i$ of degree at most $d$. This includes zero and is an ideal: addition and scalar multiplication keep degree at most $d$. Equivalently its nonzero elements are the leading coefficients of degree-$d$ polynomials in $J_i$. Multiplying a polynomial by $X$ shows $I_{i,d}\subset I_{i,d+1}$, and the chain in $i$ gives the other monotonicity. The preceding argument supplies a single $i_0$ with $I_{i,d}=I_{i_0,d}$ for all $i\geq i_0,d\geq0$.

For $f\in J_i$, $i\geq i_0$, induct on its degree. The zero polynomial lies in $J_{i_0}$. If $f$ has degree $d$, its leading coefficient lies in $I_{i_0,d}$, so choose $g\in J_{i_0}$ of degree at most $d$ with that coefficient; since it is nonzero, $g$ has degree $d$. Then $f-g\in J_i$ has smaller degree, hence lies in $J_{i_0}$ by induction. Thus $f\in J_{i_0}$, and the chain stabilizes. ACC equivalence proves that $R[X]$ is Noetherian.

## Quotients, finite type, and localization

If $\pi:R\to R/I$ is the quotient map and $J$ is an ideal of $R/I$, then $\pi^{-1}(J)$ is an ideal of $R$; images of a finite generating set generate $J$. Any algebra generated by finitely many elements $b_1,\ldots,b_m$ is a quotient of $R[X_1,\ldots,X_m]$ by the evaluation homomorphism $X_j\mapsto b_j$. Iterating the one-variable result and applying the quotient result proves finite-type permanence.

For an ideal $J\subset S^{-1}R$, put $I=\{r\in R:r/1\in J\}$. If $r/s\in J$, then $r/1=(s/1)(r/s)\in J$; conversely $r\in I$ implies $r/s=(1/s)(r/1)\in J$. Hence $J=I S^{-1}R$ and images of finitely many generators of $I$ generate $J$.

Finally, a field is Noetherian because its ideals are zero and the whole field: a nonzero element of an ideal is invertible. Apply this to $\mathbb C$ and then iterate the polynomial-ring result. No algebraic-closure theorem, algebraic-geometric dimension theorem, or external closed textbook proof is an input to this argument.
