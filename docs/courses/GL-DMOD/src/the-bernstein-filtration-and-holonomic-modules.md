# The Bernstein filtration and holonomic modules over the Weyl algebra

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An operator can be complicated in two different ways: it can differentiate many times, or its coefficients can have large polynomial degree. The order filtration measures the first. The Bernstein filtration measures both. Its finite-dimensional pieces let us count how quickly an operator module grows. A remarkable lower bound says that a nonzero module over differential operators in $n$ variables grows at least like a polynomial algebra in $n$ variables. At this smallest possible growth, a positive integer controls every chain of submodules.

We work over a field $k$ of characteristic zero and write

\[
A_n=k\langle x_1,\ldots,x_n,\partial_1,\ldots,\partial_n\rangle,
\qquad [\partial_i,x_j]=\delta_{ij}.
\]

All modules are left modules. Unless stated otherwise they are finitely generated. Geometric statements may be read over an algebraic closure. The preceding chapter, Good filtrations and the characteristic variety, provides the order characteristic variety, strict filtered exact sequences, generic component lengths, and Gabber's dimension bound. The finite polynomial normalization used in Section 4 is the proved AG-CA 09, Corollary 3.2. The Hilbert-series and numerical-polynomial arguments needed here are proved in Theorem 1.1 below.

## 1. Counting with the Bernstein filtration

Put $B_pA_n=0$ for $p<0$, and for $p\geq0$ put

\[
B_pA_n=\operatorname{span}_k\{x^\alpha\partial^\beta:
|\alpha|+|\beta|\leq p\}.
\tag{1.1}
\]

The normal forms proved in Differential operators and the Weyl algebra give

\[
\dim_k B_pA_n=\binom{p+2n}{2n},\qquad
\operatorname{gr}_B A_n\simeq
S=k[x_1,\ldots,x_n,\xi_1,\ldots,\xi_n],
\tag{1.2}
\]

where every variable in $S$ has degree one. Moving a derivative past a coordinate creates a term whose total degree is two smaller. Thus multiplication respects $B$, and

\[
[B_pA_n,B_qA_n]\subseteq B_{p+q-2}A_n.
\tag{1.3}
\]

In particular, a commutator with any $x_i$ or $\partial_i$ lowers Bernstein degree by at least one. The symbol ring is a domain, so for nonzero operators

\[
\deg_B(PQ)=\deg_B P+\deg_B Q.
\tag{1.4}
\]

A **good Bernstein filtration** on $M$ is an exhaustive increasing filtration $\Gamma_pM$, bounded below, such that $B_a\Gamma_b\subseteq\Gamma_{a+b}$ and $\operatorname{gr}_\Gamma M$ is a finite $S$-module. Its pieces are finite-dimensional. Indeed, homogeneous generators of the graded module lift to finitely many elements $m_j\in\Gamma_{a_j}M$, and induction from the lower bound gives

\[
\Gamma_pM=\sum_j B_{p-a_j}A_n\,m_j.
\tag{1.5}
\]

To see the induction, express the degree-$p$ symbol of an element using the chosen symbols, lift its coefficients, and subtract. The difference belongs to $\Gamma_{p-1}M$. Repeating terminates at the lower bound. Conversely, a filtration of the form (1.5) is good. Every finite module has one: choose a finite-dimensional generating space $V\subseteq M$ and take $\Gamma_p=B_pV$.

The lower bound is part of the definition. Assigning $\Gamma_p=M$ for every integer $p$ would give a zero graded module for a nonzero $M$, and would invalidate this argument.

### Theorem 1.1. The growth polynomial

For a good Bernstein filtration, $h_\Gamma(p)=\dim_k\Gamma_pM$ agrees for all sufficiently large integers $p$ with a polynomial $P_\Gamma(p)\in\mathbb Q[p]$. If $M\ne0$, it has the form

\[
P_\Gamma(p)=\frac{e(M)}{d(M)!}p^{d(M)}+
\text{terms of smaller degree},
\qquad e(M)\in\mathbb Z_{>0}.
\tag{1.6}
\]

Both the degree $d(M)$ and the integer $e(M)$ are independent of the good filtration. The whole polynomial need not be independent.

**Proof.** Let $N=\operatorname{gr}_\Gamma M$. A finite graded module over a polynomial ring in $r=2n$ degree-one variables has a Hilbert series of the form

\[
H_N(t)=\sum_p(\dim_kN_p)t^p=\frac{q(t)}{(1-t)^r},
\qquad q(t)\in\mathbb Z[t,t^{-1}].
\tag{1.7}
\]

Here is the induction behind this formula. For the last variable $z$, use the graded exact sequence

\[
0\longrightarrow (0:_Nz)(-1)\longrightarrow N(-1)
\xrightarrow{z}N\longrightarrow N/zN\longrightarrow0.
\]

The kernel and cokernel are finite modules over the polynomial ring with that variable removed. Consequently

\[
(1-t)H_N(t)=H_{N/zN}(t)-tH_{(0:_Nz)}(t).
\]

The case of no variables is a finite Laurent polynomial, which starts the induction. Summing graded dimensions multiplies the series by $1/(1-t)$. Expanding the resulting denominator shows that its coefficients are eventually a polynomial in $p$. This proves existence of $P_\Gamma$.

If $M\ne0$, the cumulative dimensions are eventually positive and nondecreasing, so their nonzero polynomial has positive leading coefficient. A rational polynomial that is integer-valued on all sufficiently large integers has integral finite differences. Its $d$-th difference is $d!$ times its leading coefficient. Thus the integer $e$ in (1.6) is positive.

For two good filtrations $\Gamma$ and $\Lambda$, (1.5) shows that their finite sets of generators occur in uniformly bounded degrees in the other filtration. There is therefore $c\geq0$ such that

\[
\Gamma_{p-c}\subseteq\Lambda_p\subseteq\Gamma_{p+c}
\quad\text{for all }p.
\tag{1.8}
\]

Comparing the eventual dimension polynomials in these inclusions gives the same degree and the same leading coefficient: shifting the argument by a constant changes neither. This proves the asserted independence. $\square$

For the zero module set $d(0)=-\infty$ and $e(0)=0$. The growth degree of a nonzero module also equals its **Gelfand–Kirillov dimension**, defined from a finite generating space by

\[
\operatorname{GKdim}M=
\inf\{a\geq0:\exists C>0,\ \dim_k(B_pV)\leq Cp^a
\text{ for }p\gg0\}.
\tag{1.9}
\]

Indeed, (1.6) gives growth bounded above and below by positive multiples of $p^{d(M)}$. In this setting GK dimension is an integer. This integrality uses the finite polynomial symbol ring; it is not a general property of finitely generated noncommutative algebras.

### Proposition 1.2. Exact sequences and leading coefficients

For an exact sequence of finite $A_n$-modules

\[
0\longrightarrow N\longrightarrow M\longrightarrow Q\longrightarrow0,
\tag{1.10}
\]

one has

\[
d(M)=\max\{d(N),d(Q)\}.
\tag{1.11}
\]

If every nonzero term has the same degree $d$, then

\[
e(M)=e(N)+e(Q).
\tag{1.12}
\]

**Proof.** Give $M$ a good filtration. Give $N$ the intersections $N\cap\Gamma_pM$ and $Q$ the images of $\Gamma_pM$. The resulting sequence is exact in every filtered degree and in every graded degree. The graded submodule and quotient of $\operatorname{gr}M$ are finite over the Noetherian ring $S$. The induced filtrations are bounded below and exhaustive, so they are good by the lifting argument above. Hence

\[
h_M(p)=h_N(p)+h_Q(p).
\]

The polynomials add. Their leading coefficients are positive when the modules are nonzero, which proves (1.11), and comparing equal-degree coefficients proves (1.12). $\square$

The ring $A_n$ is left Noetherian, as proved by lifting generators from its polynomial symbol ring in the first chapter. Thus every submodule occurring here is finite; there is no hidden restriction to a selected class of submodules.

## 2. Examples before the lower bound

On $\mathcal O=k[x_1,\ldots,x_n]$, coordinates multiply and derivatives differentiate. The generating vector $1$ gives

\[
B_p1=k[x_1,\ldots,x_n]_{\leq p},\qquad
h_{\mathcal O}(p)=\binom{p+n}{n}.
\tag{2.1}
\]

Multiplication produces every polynomial of degree at most $p$, and derivatives cannot increase degree. Hence $d(\mathcal O)=n$ and $e(\mathcal O)=1$. At the other extreme, (1.2) gives $d(A_n)=2n$ and $e(A_n)=1$. A multiplicity of one does not by itself mean small dimension or finite module length.

The point module $\delta_0=A_n/\sum_iA_nx_i$ has basis $\partial^\beta\delta$. Normal forms give

\[
x_i\partial^\beta\delta=-\beta_i\partial^{\beta-e_i}\delta.
\]

Thus its Bernstein filtration has the same counting function as (2.1), with $x$-monomials replaced by derivative monomials. It too has $d=n,e=1$.

There is a useful exact formula in one variable. Write $A=A_1$.

### Proposition 2.1. A single operator on the line

Let $P\in A$ be nonzero, with $r=\deg_BP$. Give $M_P=A/AP$ the quotient Bernstein filtration. If $r>0$, then, for $p\geq r$,

\[
h_{M_P}(p)=\binom{p+2}{2}-\binom{p-r+2}{2}
=rp+\frac{3r-r^2}{2}.
\tag{2.2}
\]

Consequently $d(M_P)=1$ and $e(M_P)=r$. If $r=0$, $P$ is a nonzero scalar and $M_P=0$.

**Proof.** By (1.4), right multiplication by $P$ identifies $B_{p-r}A$ with $AP\cap B_pA$. It is injective, since $A$ is a domain. Taking dimensions gives (2.2). Equivalently,

\[
\operatorname{gr}_B M_P\simeq k[x,\xi]/(\sigma_B(P)).
\tag{2.3}
\]

For $r>0$, the polynomial in (2.2) is nonzero, so the quotient is nonzero and has the stated invariants. For $r=0$, the left ideal is the entire ring. $\square$

For $P=\partial-1$, (2.2) gives $h(p)=p+1$. The quotient is the rank-one connection with basis $v$, where

\[
\partial(fv)=(f'+f)v.
\]

Every element of $B_pv$ has polynomial coefficient of degree at most $p$, and all such coefficients occur by multiplication with $x$. Thus the connection description checks the same polynomial directly.

For $Q_\lambda=A/A(x\partial-\lambda)$, the Bernstein symbol is $x\xi$, regardless of $\lambda$. The standard monomials in its symbol quotient are $1,x,\ldots,x^p,\xi,\ldots,\xi^p$. Therefore

\[
h_{Q_\lambda}(p)=2p+1,\qquad d(Q_\lambda)=1,\qquad e(Q_\lambda)=2.
\tag{2.4}
\]

The preceding chapter computed its order characteristic variety as the union of the zero section and the fibre over zero. For a nonintegral $\lambda$, $Q_\lambda$ is simple even though its Bernstein multiplicity is two. The forthcoming length bound can be strict.

## 3. Joseph's argument for Bernstein's inequality

The next proof uses only commutators, finite-dimensional spaces, and polynomial growth. It avoids any dimension theorem about symplectic varieties.

### Theorem 3.1. Bernstein's inequality

For a nonzero finite $A_n$-module,

\[
d(M)\geq n.
\tag{3.1}
\]

**Proof.** Choose a finite-dimensional nonzero generating space $V$ and set $\Gamma_p=B_pV$, with $\Gamma_p=0$ for $p<0$. For every $p\geq0$, consider the action map

\[
\rho_p:B_pA_n\longrightarrow
\operatorname{Hom}_k(\Gamma_pM,\Gamma_{2p}M).
\tag{3.2}
\]

We prove by induction that $\rho_p$ is injective. For $p=0$, a scalar killing the nonzero space $V$ is zero. Suppose injectivity is known at $p-1$, and $T\in B_p$ kills $\Gamma_p$. For $w\in\Gamma_{p-1}$, both $x_iw$ and $\partial_iw$ belong to $\Gamma_p$. Consequently

\[
[x_i,T]w=x_iTw-Tx_iw=0,\qquad
[\partial_i,T]w=\partial_iTw-T\partial_iw=0.
\]

Both commutators lie in $B_{p-1}$. By the induction hypothesis they are zero as operators in $A_n$.

An operator commuting with all coordinates and derivatives is a scalar. To verify this directly, write $T=\sum c_{\alpha\beta}x^\alpha\partial^\beta$. Commuting with $x_i$ differentiates this normal-form polynomial with respect to $\partial_i$, up to sign, so characteristic zero forces all positive derivative exponents to disappear. Commuting next with $\partial_i$ removes every positive coordinate exponent. Thus $T\in k$, and its action on the nonzero space $\Gamma_p$ forces $T=0$. This completes the induction.

Injectivity of (3.2) now gives

\[
\binom{p+2n}{2n}\leq
(\dim_k\Gamma_pM)(\dim_k\Gamma_{2p}M).
\tag{3.3}
\]

For large $p$, the left side has positive leading term of degree $2n$; the right side has positive leading term of degree $2d(M)$. An inequality of this form for arbitrarily large $p$ requires $2n\leq2d(M)$. $\square$

The action map in the proof is injective on a bounded operator space, although $M$ may have many vectors killed by individual nonzero operators. It says that no nonzero operator of degree at most $p$ can kill the whole space of vectors already obtainable in degree $p$.

Every finite module is a quotient of $A_n^s$, so Proposition 1.2 also gives $d(M)\leq2n$. The possible dimensions of nonzero finite modules are therefore the integers between $n$ and $2n$.

## 4. Equality with the order characteristic dimension

The order filtration gives degree zero to every $x_i$ and degree one to every $\partial_i$. Its symbol ring is also the polynomial algebra $S=k[x,\xi]$, but now only $\xi$ has positive degree. Its pieces need not be finite-dimensional over $k$. Neither a constant shift nor a fixed rescaling compares the order and Bernstein filtrations on the entire ring: $x^a$ has order zero for arbitrarily large $a$.

### Theorem 4.1. Comparison of dimensions

For every nonzero finite $A_n$-module,

\[
d(M)=\dim\operatorname{Ch}_{\mathrm{ord}}(M).
\tag{4.1}
\]

We give a proof for all finite modules, then make the cyclic calculation explicit. The finite basis in the proof is essential: symbols of an arbitrary generating set for a left ideal or submodule may miss additional relations.

**A commutative growth lemma.** For a finite module $N$ over a polynomial ring $S=k[z_1,\ldots,z_s]$, with the filtration generated by a finite set using polynomials of total degree at most $p$, its growth degree equals $\dim\operatorname{Supp}N$.

Here are the details of the dimension assertion. The Hilbert-series proof in Section 1 applies to the total-degree symbol module, so there is an eventual growth polynomial. A finite module has a finite filtration with factors $S/\mathfrak p$. Indeed, a maximal annihilator of a nonzero element is prime: if $ab$ kills that element and $b$ does not, the annihilator of the nonzero element obtained by multiplying by $b$ contains the original annihilator; maximality forces $a$ into it. Insert the resulting cyclic submodule and repeat on the quotient. The ascending chain condition makes this process terminate. Good induced filtrations and strict exact sequences, exactly as in Proposition 1.2, show that the growth degree and support dimension are the maxima of the respective quantities for these factors.

For $R=S/\mathfrak p$, Noether normalization gives a polynomial subring $T=k[y_1,\ldots,y_r]\subseteq R$ such that $R$ is finite over $T$ and $r=\dim R$. Represent the $y_i$ by polynomials of degrees at most $L$, taking $L\geq1$. Their monomials of degree at most $\lfloor p/L\rfloor$ are independent and belong to $R_{\leq p}$; this gives a lower bound proportional to $p^r$. For the upper bound choose finite $T$-module generators $v_j$ of $R$, including $1$. Multiplication by each $z_i$ on these generators is expressed using finitely many coefficient polynomials in $y$, of degrees at most $C$, with $C\geq1$. A word of length at most $p$ in the $z_i$, acting on $1$, is therefore a combination of the $v_j$ with coefficients of degree at most $Cp$. Its span has dimension at most

\[
(\#\{v_j\})\binom{Cp+r}{r}.
\]

The two bounds give growth degree $r$, proving the lemma. For $r=0$, they mean bounded positive dimension, and the same conclusion holds.

**Proof of Theorem 4.1.** Choose a presentation $M=A_n^s/K$. Give the free module the filtration with all its basis vectors in degree zero and give $M$ the quotient filtrations. We will compare both growth and order symbols through the same set of monomials.

Order the free-module monomials $x^\alpha\partial^\beta e_j$ first by $|\beta|$, then by $|\alpha|$, then by a fixed lexicographic order on exponents and basis positions. Larger tuples mean larger monomials. This is a well-order compatible with adding exponent vectors. The leading monomial of a product is the product of leading monomials, since the additional terms in commuting derivatives past coordinates have smaller derivative degree.

The monomial submodule generated by the leading monomials of all nonzero elements of $K$ is a submodule of the Noetherian polynomial module $S^s$. Choose finitely many $g_1,\ldots,g_a\in K$ whose leading monomials generate it. These form a left Gröbner basis in the following concrete sense. Whenever the leading monomial of an element of $K$ is divisible by one of theirs, subtract a monomial multiple of that $g_i$ to cancel it. The leading monomial strictly decreases. The process terminates, since the order is a well-order, and a nonzero remainder in $K$ would still have a divisible leading monomial. Hence every element of $K$ reduces to zero.

Call a monomial **standard** if it is not divisible, in its basis position, by any of these leading monomials. Division of any vector in $A_n^s$, moving nondivisible terms to the remainder, terminates by the same argument. Standard monomials span the quotient. They are independent: a nonzero linear combination belonging to $K$ would have a standard leading monomial, which is impossible. Thus they form a $k$-basis of $M$.

There is a uniform positive integer $c$ for which division does not increase the weight

\[
w(x^\alpha\partial^\beta e_j)=|\alpha|+c|\beta|.
\tag{4.2}
\]

To choose it, inspect the finitely many terms in the $g_i$. A nonleading term with the same derivative degree has no larger coordinate degree. A term of smaller derivative degree can have larger coordinate degree, but taking $c$ larger than all such finite degree increases makes its weight no larger than the leading term's. Multiplying a $g_i$ by a monomial preserves these weight inequalities; every commutation term further lowers weight. Each subtraction in division consequently has this same property.

Let $a(p)$ count standard monomials of ordinary total degree at most $p$, and let $h_M(p)$ be the quotient Bernstein counting function. Standard monomials of degree at most $p$ are independent elements of $B_pM$, so $a(p)\leq h_M(p)$. Conversely, a representative of Bernstein degree at most $p$ has weight at most $cp$. Its standard remainder has weight at most $cp$, hence total degree at most $cp$. Therefore

\[
a(p)\leq h_M(p)\leq a(cp).
\tag{4.3}
\]

It remains to identify the growth exponent of $a(p)$. Put $J=\operatorname{gr}_{\mathrm{ord}}K\subseteq S^s$, so that $\operatorname{gr}_{\mathrm{ord}}M=S^s/J$. The leading monomial submodule of $J$, for the same monomial order, is exactly the leading monomial submodule of $K$. In one direction, the order symbol of $u\in K$ retains its terms of highest derivative degree, including its leading monomial. In the other, $J$ is graded in derivative degree, and every homogeneous component is such an order symbol; the highest derivative-degree component of an arbitrary element of $J$ supplies its leading monomial. These observations prove both inclusions.

Thus the order symbols $\sigma_{\mathrm{ord}}(g_i)$ form a commutative Gröbner basis of $J$. Each such symbol is homogeneous in derivative degree, and its leading term has greatest coordinate degree among its terms. Division by these symbols cannot increase ordinary total degree. Consequently the ordinary total-degree filtration on $S^s/J$ has dimension exactly $a(p)$: the same standard monomials form a basis, and degree-bounded division gives both inequalities for that assertion.

The commutative growth lemma identifies the exponent of $a(p)$ with $\dim\operatorname{Supp}(S^s/J)=\dim\operatorname{Ch}_{\mathrm{ord}}M$. The bounds (4.3) identify it with $d(M)$. This proves (4.1). $\square$

### The cyclic comparison without a Gröbner basis

For $P\in A_1$ nonzero, write

\[
P=\sum_{j=0}^m a_j(x)\partial^j,\qquad a_m\ne0.
\]

The integral order symbol ring gives

\[
\operatorname{gr}_{\mathrm{ord}}(A_1/A_1P)
\simeq k[x,\xi]/(a_m(x)\xi^m).
\tag{4.4}
\]

If $P$ is nonconstant, the support in (4.4) has dimension one. For $m>0$, it contains the zero section, together with fibres over the roots of $a_m$. For $m=0$, $a_0$ is nonconstant, and its roots give fibres of dimension one after extending to an algebraic closure. Proposition 2.1 independently gave $d=1$. A nonzero constant gives the zero module on both sides.

The dimension comparison does not equate the two multiplicities. For example, $A_1/A_1(\partial-x^2)$ is the polynomial rank-one connection $\partial(fv)=(f'+x^2f)v$. Its order characteristic cycle is the zero section with multiplicity one, while (2.2) gives Bernstein multiplicity two. Both dimensions are one. Even the supports given by the two filtrations differ: the Bernstein symbol is $-x^2$, whereas the order symbol is $\xi$.

## 5. Holonomicity and finite length

A finite $A_n$-module is **holonomic** if it is zero or $d(M)=n$. By Theorem 4.1, this is equivalent to the geometric definition: its order characteristic variety has dimension at most $n$. Bernstein's inequality makes the dimension exactly $n$ when the module is nonzero.

### Theorem 5.1. The holonomic category

Holonomic modules form a Serre subcategory of finite $A_n$-modules: they are closed under submodules, quotients, and extensions. On this category the Bernstein multiplicity is additive. Every holonomic module has finite length, with

\[
\operatorname{length}_{A_n}M\leq e(M).
\tag{5.1}
\]

**Proof.** For a submodule $N\subseteq M$, Proposition 1.2 bounds the dimensions of $N$ and $M/N$ by $d(M)$. If $M$ is holonomic, every nonzero one of those modules has dimension at least $n$ by Theorem 3.1, hence exactly $n$. Conversely, an extension of two holonomic modules has dimension $n$ when it is nonzero, again by Proposition 1.2. This proves the Serre assertion. Every nonzero term of an exact sequence in this category has dimension $n$, so (1.12) gives multiplicity additivity, including zero terms with $e(0)=0$.

Consider any finite strictly increasing chain

\[
0=N_0\subsetneq N_1\subsetneq\cdots\subsetneq N_r\subseteq M.
\]

Every quotient $N_i/N_{i-1}$ is nonzero and holonomic, so its multiplicity is a positive integer. Repeated additivity gives

\[
e(M)=e(M/N_r)+\sum_{i=1}^r e(N_i/N_{i-1})\geq r.
\tag{5.2}
\]

The same argument bounds the number of strict inclusions in a decreasing chain. Thus both ascending and descending chains terminate. To construct a composition series explicitly, if $M$ is not simple choose a proper nonzero submodule. Both that submodule and its nonzero quotient have smaller positive multiplicity than $M$. Induction on $e(M)$ constructs composition series for them; lifting the quotient's series and joining it to the submodule's series constructs one for $M$. Formula (5.2), applied to this series, proves (5.1). The zero module is immediate. $\square$

Every nonzero module on the line defined by one nonconstant operator is holonomic, by Proposition 2.1. The statement also includes nonzero constant operators, whose quotients are zero. Therefore it is correct to say that $A_1/A_1P$ is holonomic for every nonzero $P$, provided zero is included in the holonomic category.

The modules $\mathcal O$ and $\delta_0$ from Section 2 are simple: they are nonzero holonomic modules of multiplicity one. In contrast, the left regular module $A_n$, for $n\geq1$, is not holonomic. It has an infinite descending chain of left ideals

\[
A_n\supsetneq A_nx_1\supsetneq A_nx_1^2\supsetneq\cdots.
\]

Strictness follows from (1.4): an equation $x_1^r=Qx_1^{r+1}$ would require $r=\deg_BQ+r+1$.

There is also a useful geometric consequence beyond affine space. On a smooth variety $X$ of pure dimension $n$, a coherent $\mathcal D_X$-module is holonomic if its characteristic support has dimension at most $n$. The independently proved whole-dimension bound, Theorem 7.2, makes the characteristic dimension of every nonzero such module exactly $n$. Characteristic support is a union in a short exact sequence, so these modules form a Serre category. Take the dimension-$n$ part of the characteristic cycle, summing only the dimension-$n$ components. The earlier generic-length theorem makes this part additive; it requires no assertion about smaller-dimensional components.

Let $c(M)$ be the sum of the generic component lengths in this dimension-$n$ cycle, and set $c(0)=0$. There are finitely many components, and $c(M)$ is a positive integer for $M\ne0$. The local Noetherian property of $\mathcal D_X$, together with a finite affine covering of $X$, makes submodules of coherent modules coherent. Additivity of the cycles gives the same chain argument as (5.2), with $c$ in place of $e$. Thus a holonomic coherent sheaf has finite length, bounded by $c(M)$. This geometric bound and the Bernstein bound use different multiplicities; the example following (4.4) shows why their values need not agree.

## 6. Exercises with complete solutions

### Exercise 6.1 — easy: a polynomial module on the line

Compute the Bernstein Hilbert polynomial of $k[x]$ from the generator $1$. Then give a different good filtration with a different Hilbert polynomial and the same $d,e$.

**Solution.** Since $\partial1=0$, every normal-form operator applied to $1$ produces a polynomial of degree at most its Bernstein degree. All $1,x,\ldots,x^p$ occur. Thus $\Gamma_p=k[x]_{\leq p}$, with $h(p)=p+1$ for $p\geq0$, $d=1$, and $e=1$. Set $\Lambda_p=\Gamma_{p+1}$ for every integer $p$. This is a shifted good filtration, bounded below by $\Lambda_p=0$ for $p<-1$, with eventual polynomial $p+2$. Its degree and leading coefficient are unchanged.

### Exercise 6.2 — easy: the regular module

Compute the Bernstein invariants of $A_n$, and explain why its multiplicity does not make it holonomic when $n\geq1$.

**Solution.** Normal forms are indexed by $2n$ nonnegative exponents. Introducing a slack exponent gives $\binom{p+2n}{2n}$ monomials of total degree at most $p$. The leading term is $p^{2n}/(2n)!$, so $d=2n$ and $e=1$. Holonomicity is the condition $d=n$, not the condition $e=1$. For $n\geq1$ these dimensions differ. The descending chain in Section 5 also shows directly that the module does not have finite length.

### Exercise 6.3 — medium: submodules and multiplicity

Let $N\subseteq M$, where $M$ is holonomic. Prove that $N$ is holonomic and that $e(N)\leq e(M)$, with equality precisely when $N=M$.

**Solution.** The ring is Noetherian, so $N$ is finite. Exactness gives $d(N)\leq n$. If $N\ne0$, Bernstein's inequality gives $d(N)\geq n$, so $N$ is holonomic; the zero case is included by definition. The quotient is holonomic by the identical argument. Thus $e(M)=e(N)+e(M/N)$. This implies the inequality, and a nonzero quotient has positive multiplicity, so equality occurs exactly for the zero quotient. In this proof, dimension exactness and Bernstein's inequality establish holonomicity before multiplicity additivity is used; assuming equal-degree additivity first would be circular.

### Exercise 6.4 — medium: an arbitrary equation on the line

For nonzero $P\in A_1$, prove holonomicity of $A_1/A_1P$ and compute its Bernstein multiplicity. Apply your formula to $P=x^2\partial-1$, and compare its order characteristic cycle.

**Solution.** If $P$ is a scalar the quotient is zero and has $e=0$. Otherwise $r=\deg_BP\geq1$, and right multiplication by $P$ gives the dimension difference (2.2). Its degree is one and its leading coefficient is $r$; thus the module is holonomic with $e=r$. For $x^2\partial-1$, $r=3$, and $h(p)=3p$ for $p\geq3$. Its order symbol is $x^2\xi$, giving zero section $Z$ and fibre $F$ over zero. At the generic prime $(\xi)$, $x$ is invertible and the symbol quotient has local length one. At $(x)$, $\xi$ is invertible and it has local length two. The order cycle is $[Z]+2[F]$, in agreement with the previous chapter's calculation.

### Exercise 6.5 — hard: the precise length bound

Prove (5.1) without assuming in advance that a composition series exists. Determine when a holonomic module attains equality in that bound.

**Solution.** Every nonzero holonomic module has a positive integer multiplicity. If the module is simple its length is one, at most that integer. If it is not simple, take a proper nonzero submodule $N$. Both $e(N)$ and $e(M/N)$ are positive and smaller than $e(M)$, by the Serre property and additivity. Induction therefore constructs finite composition series for both pieces, and their concatenation constructs one for $M$. If its simple factors are $L_1,\ldots,L_r$, then $e(M)=\sum_i e(L_i)\geq r$. Equality holds exactly when every simple factor has multiplicity one. This criterion does not depend on a chosen series, since it is equivalent to the numerical equality $\operatorname{length}M=e(M)$.

### Exercise 6.6 — hard: a bound that is strict

Prove that $E=A_1/A_1(\partial-x^2)$ is simple. Compute its Bernstein multiplicity and its order characteristic multiplicity.

**Solution.** Let $v$ denote the cyclic generator. The map to the polynomial connection $k[x]v$, with $\partial(fv)=(f'+x^2f)v$, is an isomorphism: reduction using the monic derivative relation writes every class as $f(x)v$, and the target proves these polynomial classes independent. A submodule corresponds to an ideal $I\subseteq k[x]$ stable under $f\mapsto f'+x^2f$. Since $I$ is already stable under multiplication by $x^2$, it is stable under ordinary differentiation. If nonzero, choose a nonzero polynomial in it of smallest degree. A positive-degree polynomial has a nonzero derivative of smaller degree in characteristic zero, a contradiction. Thus $I$ contains a nonzero constant, so $I=k[x]$. This proves simplicity and length one. The Bernstein degree of the defining operator is two, so Proposition 2.1 gives $e(E)=2$. The constant bundle order filtration has $\operatorname{gr}_{\mathrm{ord}}E=k[x]$, supported on the zero section with generic length one. Hence this example has length one, Bernstein multiplicity two, and geometric multiplicity one.

## References and what this lesson does not prove

The central module statements in this chapter are proved above: the independence of growth degree and multiplicity, exactness, Joseph's injectivity argument and Bernstein's inequality, the full order–Bernstein dimension comparison, cyclic holonomicity, the Serre property, and finite length with its bound. All six exercises have complete solutions.

The Noether normalization used in Section 4 is proved in the earlier AG-CA 09, Corollary 3.2: a finite-type algebra has a polynomial subring of the same dimension over which it is finite. Theorem 1.1 here proves the Hilbert-series and numerical-polynomial statements used in the growth argument. The geometric extension in Section 5 uses the independent whole-dimension inequality proved in the preceding chapter, Theorem 7.2, and top-dimensional cycle additivity. This finite-length proof uses that independent inequality; the preceding chapter also now proves the full Gabber theorem and componentwise coisotropy in Theorem 7.0 and Corollary 7.1.

For the growth perspective, see R. Bezrukavnikov, [*Noncommutative Algebra*, MIT 18.706](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/mit18_706_s23_full_lec.pdf), Sections 24.1 and 24.6, especially Definition 24.14 and Proposition 24.17. The polynomial symbol algebra and finite generation hypotheses are essential in applying that comparison here. D. Miličić, [*D-modules on smooth algebraic varieties*, Chapter I](https://www.math.utah.edu/~milicic/Eprints/hk_chapter1.pdf), Theorem 6.3, Theorem 7.7, and Theorem 8.1, give further treatments of the inequality, characteristic dimension, and holonomic category. Section 4 above supplies the finite Gröbner-basis justification needed for the comparison, rather than assuming that symbols of arbitrary generators generate an initial ideal. E. Frenkel, [*Lectures on the Langlands program and conformal field theory*](https://arxiv.org/abs/hep-th/0512172), Section 3.5, discusses the Euler-module example; its actions and both filtrations are computed explicitly in this course.
