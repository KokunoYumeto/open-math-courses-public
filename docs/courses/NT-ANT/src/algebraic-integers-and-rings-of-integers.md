# Algebraic integers and rings of integers

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

Arithmetic in a number field starts by deciding which elements deserve to be called integers. A basis over the rational numbers cannot answer this: replacing a basis changes its integer span. Monic polynomial equations give a definition that survives every change of coordinates. We will turn that definition into practical tests, determine every quadratic ring of integers, and exhibit a failure of unique factorization.

The prerequisites are polynomial factorization and Gauss's lemma, field extensions and Galois theory, and modules and finite-dimensional linear algebra. The precise facts used are collected under [What this lesson does not prove](#what-this-lesson-does-not-prove). Freely accessible references are [Milne ANT], [Milne FGT] and [Stacks]. The general integral-extension arguments are taught in *Integral extensions: lying over, going up and going down*. Here we concentrate on arithmetic over the rational integers.

## 1. Seeing a field through its embeddings

A **number field** is an abstract field $K$ with a specified inclusion $\mathbb Q\subset K$ and finite degree $n=[K:\mathbb Q]$. It is not supplied with a preferred inclusion into $\mathbb C$. An **embedding** means a field homomorphism $\sigma:K\to\mathbb C$ fixing $\mathbb Q$. Field homomorphisms are injective.

Characteristic zero makes every finite extension separable. The primitive element theorem gives $K=\mathbb Q(\theta)$. If $f$ is the minimal polynomial of $\theta$, its $n$ distinct roots in $\mathbb C$ correspond to the embeddings: choosing a root determines the image of $\theta$, hence the entire map. Here are the algebraic proofs needed for these statements.

**Separable embeddings and a primitive element.** In characteristic zero an irreducible polynomial has nonzero derivative of smaller degree, so it is coprime to its derivative and has no repeated root. A finite separable extension $L/k$ has exactly $[L:k]$ embeddings into an algebraic closure. Write it as a tower adjoining finitely many elements. An embedding of an intermediate field extends in exactly as many ways as the degree of the next minimal polynomial: its distinct roots give the maps out of the polynomial quotient. Multiplying these counts along the tower proves the assertion. Products of basis elements give the same multiplication rule for the degrees.

If $k$ is infinite and $L=k(\alpha,\beta)$, list its embeddings as $\sigma_i$. Choose $c\in k$ so that all $\sigma_i(\alpha)+c\sigma_i(\beta)$ differ. For a pair with different $\beta$-images there is at most one forbidden $c$; if those images agree, the $\alpha$-images differ, since the embeddings agree on both generators only when they are the same. Finitely many forbidden values cannot exhaust $k$. Thus $\gamma=\alpha+c\beta$ has at least $[L:k]$ conjugates, forcing $[k(\gamma):k]=[L:k]$ and $L=k(\gamma)$. Induction handles more generators.

If $k$ is finite, so is $L$. The multiplicative group of any finite field is cyclic. Take the least common multiple $m$ of its element orders. For each prime dividing $m$, choose an element whose order contains the maximal power of that prime, and take a power to remove the other prime factors. The product of the resulting commuting elements of relatively prime orders has order $m$: raising to the separate orders proves that none of these components can cancel another. Every field unit is a root of $X^m-1$, so their number is at most $m$. The constructed element already has $m$ distinct powers, hence generates all units. Such a generator also generates $L$ as a field over $k$. This proves the primitive element theorem for every finite separable extension.

Complex conjugation sends $\sigma$ to $\bar\sigma$, where $\bar\sigma(x)=\overline{\sigma(x)}$. It fixes precisely those embeddings whose images lie in $\mathbb R$. All remaining embeddings occur in distinct pairs. The **signature** is $(r_1,r_2)$, where $r_1$ counts real embeddings and $r_2$ counts these pairs. Consequently

$$
n=r_1+2r_2.
$$

The roots of a primitive element's polynomial make the signature visible:

| Field | Minimal polynomial of the indicated generator | Images of the generator | Signature |
|---|---|---|---|
| $\mathbb Q(\sqrt2)$ | $X^2-2$ | $\sqrt2,-\sqrt2$ | $(2,0)$ |
| $\mathbb Q(\sqrt[3]2)$ | $X^3-2$ | $c,c\xi,c\xi^2$, with $c=\sqrt[3]2>0$, $\xi=e^{2\pi i/3}$ | $(1,1)$ |
| $\mathbb Q(2^{1/4})$ | $X^4-2$ | $u,-u,iu,-iu$, with $u=2^{1/4}>0$ | $(2,1)$ |
| $\mathbb Q(\zeta_7)$ | $X^6+X^5+\cdots+X+1$ | $\zeta_7^j$, $1\le j\le6$ | $(0,3)$ |

Here $\zeta_7=e^{2\pi i/7}$. The first three polynomials are Eisenstein at $2$. For the last one, substituting $X=Y+1$ gives

$$
Y^6+7Y^5+21Y^4+35Y^3+35Y^2+21Y+7,
$$

which is Eisenstein at $7$; translation preserves irreducibility. Its roots are the nontrivial seventh roots of unity, and conjugation pairs $j$ with $7-j$. More generally, for a primitive $m$th root $\zeta_m$, $m>2$, every embedding sends it to another primitive $m$th root. Such a root cannot be real, since the only real roots of unity are $1$ and $-1$. Thus every cyclotomic field of this kind has signature $(0,[\mathbb Q(\zeta_m):\mathbb Q]/2)$.

The four displayed minimal polynomials give traces $0,0,0,-1$ and norms $-2,2,-2,1$, respectively. These follow from minus the next-to-leading coefficient and $(-1)^n$ times the constant coefficient, as Section 3 will prove.

Two kinds of conjugates must be distinguished. An element $\alpha$ has distinct conjugates given by its minimal polynomial. Its images under all embeddings of a larger field $K$ can repeat. For example, $1$ has just one distinct conjugate, but all $n$ embeddings of $K$ send it to $1$. This multiplicity will matter for norms.

## 2. Integers defined by equations

An element of a field containing a ring $A$ is **integral over $A$** if it satisfies a monic polynomial with coefficients in $A$. The word “monic” means that the leading coefficient is $1$. An **algebraic integer** is an element integral over $\mathbb Z$. Every element of a number field is integral over $\mathbb Q$; that weaker statement does not make it an algebraic integer.

We need the finite-module criterion, the ring property and transitivity of integrality. We prove them for arbitrary commutative rings, with homomorphisms preserving the identity.

**Finite-module criterion.** An element $x$ in an $A$-algebra is integral over $A$ if and only if $A[x]$ is finite as an $A$-module. A monic equation expresses every sufficiently high power in the span of the lower powers, proving one direction. Conversely, multiplication by $x$ on generators $m_1,\ldots,m_r$ of a finite $A$-subalgebra $B$ is given by a matrix $C$ over $A$. The adjugate identity makes the monic polynomial $\det(TI-C)$ at $T=x$ annihilate all generators. It annihilates $1\in B$, so it vanishes at $x$. This also proves integrality whenever $x$ lies in any finite $A$-subalgebra, without requiring a free module or a domain.

**Ring property and transitivity.** If $x_1,\ldots,x_r$ are integral, adjoining them successively gives a finite module at every step, hence a finite $A$-module overall: products of finite generating sets generate the composite module. The criterion makes every element of $A[x_1,\ldots,x_r]$ integral. Taking $r=2$ proves closure under sums, differences and products. If $x$ is integral over an algebra $B$ integral over $A$, its monic equation uses only finitely many coefficients $b_i\in B$. The algebra $A[b_1,\ldots,b_m]$ is finite over $A$; adjoining $x$ is finite over that algebra. Their generating sets multiply, so the criterion makes $x$ integral over $A$. This proves transitivity even when $B$ itself is not finite over $A$.

The full statements are also in [Stacks, Tag 00GM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-integral), [Tag 00GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-transitive) and [Tag 00GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-closure-is-ring). The proofs above supply the dependencies here.

Therefore

$$
\mathcal O_K=\{\alpha\in K\mid\alpha\text{ is integral over }\mathbb Z\}
$$

is a subring of $K$, called its **ring of integers**. For instance, $\sqrt2$ and $\sqrt3$ are algebraic integers because their squares are integers. Their sum is an algebraic integer by the ring property, before we compute its polynomial.

**Proposition 1.1 (the minimal-polynomial test).** An element $\alpha\in K$ belongs to $\mathcal O_K$ if and only if its monic minimal polynomial over $\mathbb Q$ lies in $\mathbb Z[X]$. Moreover,

$$
\mathcal O_K\cap\mathbb Q=\mathbb Z,\qquad
K=\operatorname{Frac}(\mathcal O_K),
$$

and $\mathcal O_K$ is integrally closed in $K$. Every $\alpha\in K$ has a positive integer multiple belonging to $\mathcal O_K$.

*Proof.* If $\alpha$ satisfies a monic $F\in\mathbb Z[X]$, its minimal polynomial $f\in\mathbb Q[X]$ divides $F$. Here is the needed form of Gauss's lemma. A polynomial is primitive when the gcd of its integer coefficients is one. The product of two primitive polynomials is primitive: a prime dividing every product coefficient would give a zero product of two nonzero polynomials over $\mathbf F_p$, impossible in that domain. Write the two monic rational factors of $F$ as $P/a,Q/b$, with primitive integer $P,Q$ and positive integers $a,b$ equal to their leading coefficients. Then $PQ=abF$. Its left side has coefficient gcd one; its right side has gcd $ab$, since $F$ is monic. Thus $a=b=1$, proving $f\in\mathbb Z[X]$. The converse follows from the definition. For $q\in\mathbb Q$, the minimal polynomial is $X-q$, so this test gives $q\in\mathcal O_K$ exactly when $q\in\mathbb Z$.

Write the minimal polynomial of an arbitrary $\alpha$ as

$$
X^d+c_1X^{d-1}+\cdots+c_d,\qquad c_j\in\mathbb Q.
$$

Choose a positive common denominator $m$ for the $c_j$. Then $m\alpha$ satisfies

$$
X^d+(mc_1)X^{d-1}+(m^2c_2)X^{d-2}+\cdots+m^dc_d\in\mathbb Z[X].
$$

Thus $\alpha=(m\alpha)/m$ is a fraction of elements of $\mathcal O_K$, proving the fraction-field assertion. Finally, if $x\in K$ is integral over $\mathcal O_K$, transitivity applied to $\mathbb Z\subset\mathcal O_K\subset\mathcal O_K[x]$ makes $x$ integral over $\mathbb Z$. Hence $x\in\mathcal O_K$. This is precisely integral closedness. $\square$

The same transitivity argument shows that an element integral over any ring all of whose elements are algebraic integers is itself an algebraic integer. Also, if $L/K$ is an extension of number fields, then $\mathcal O_L\cap K=\mathcal O_K$: both sides use exactly the same monic equations over $\mathbb Z$.

**Polynomial irreducibility tests used here.** The same primitive-product argument shows that a primitive integer polynomial factoring over $\mathbf Q$ factors into nonconstant integer polynomials: clear rational denominators, divide out coefficient gcds, and write $f=cPQ$ with primitive $P,Q$ and rational $c$. Integrality of the coefficients forces the denominator of $c$ to divide their gcd one; primitiveness of $f$ then forces $c=\pm1$. If a prime $p$ divides all nonleading coefficients but not the leading one, reduction of such a factorization makes both factors monomials over $\mathbf F_p$, with their positive degrees preserved. Both constant coefficients are divisible by $p$, forcing $p^2\mid f(0)$. Excluding that square proves Eisenstein's criterion. Finally a root $a/b$ in lowest terms of a monic integer polynomial satisfies $b\mid a^n$ after denominators are cleared, so $b=1$; its integer value divides the constant coefficient. This proves the rational-root test used in the examples.

## 3. Multiplication as a linear transformation

For a finite field extension $L/K$, multiplication by $\alpha\in L$ is the $K$-linear map $m_\alpha:x\mapsto\alpha x$. Define

$$
\chi_{\alpha,L/K}(X)=\det(XI-m_\alpha),\quad
\operatorname{Tr}_{L/K}(\alpha)=\operatorname{tr}(m_\alpha),\quad
N_{L/K}(\alpha)=\det(m_\alpha).
$$

These do not depend on the chosen basis. If $n=[L:K]$, then

$$
\chi_{\alpha,L/K}(X)=X^n-\operatorname{Tr}_{L/K}(\alpha)X^{n-1}
+\cdots+(-1)^nN_{L/K}(\alpha).
$$

When a number field $K$ is fixed, $\operatorname{Tr}$ and $N$ without subscripts mean $\operatorname{Tr}_{K/\mathbb Q}$ and $N_{K/\mathbb Q}$.

Linearity of matrix trace gives additivity and $K$-linearity of field trace. The identity $m_{\alpha\beta}=m_\alpha m_\beta$ gives multiplicativity of norm. For $a\in K$, the matrix is $aI$, so its trace is $na$ and its norm is $a^n$. In particular, norms of rational elements still depend on the field degree.

**Proposition 1.2 (conjugates and towers).** If $L/K$ is finite separable and $\alpha\in L$, then

$$
\chi_{\alpha,L/K}(X)=\prod_{\sigma:L\hookrightarrow\overline K}(X-\sigma(\alpha)),
$$

where the embeddings fix $K$. Thus trace and norm are the sum and product of these images, including repetitions. For every tower $M/L/K$ of finite field extensions, including inseparable ones,

$$
\operatorname{Tr}_{M/K}=\operatorname{Tr}_{L/K}\circ\operatorname{Tr}_{M/L},\qquad
N_{M/K}=N_{L/K}\circ N_{M/L}.
$$

If $L/K$ is an extension of number fields and $\alpha\in\mathcal O_L$, every coefficient of $\chi_{\alpha,L/K}$, in particular its trace and norm, belongs to $\mathcal O_K$.

*Proof.* Put $E=K(\alpha)$, let $f=X^d+c_1X^{d-1}+\cdots+c_d$ be the minimal polynomial, and set $r=[L:E]$. On $E$, use the basis $1,\alpha,\ldots,\alpha^{d-1}$. Multiplication shifts each basis vector to the next, while

$$
\alpha^d=-c_d-c_{d-1}\alpha-\cdots-c_1\alpha^{d-1}.
$$

Its matrix has ones immediately below the diagonal, zeros elsewhere except for the last column $(-c_d,-c_{d-1},\ldots,-c_1)^t$. Expanding $\det(XI-m_\alpha)$ along that column gives $f(X)$. A basis $v_1,\ldots,v_r$ of $L/E$ decomposes $L$ as $\bigoplus_j Ev_j$, with multiplication having the same matrix on every summand. Consequently

$$
\chi_{\alpha,L/K}=f^r. \tag{1}
$$

This equality needs no separability. In the separable case, $E/K$ has $d$ embeddings and each extends to exactly $r$ embeddings of $L$. This extension count was proved in Section 1. Each root of $f$ therefore occurs $r$ times in the required product. Equation (1) proves the characteristic-polynomial formula. Comparing coefficients gives trace and norm.

To prove the tower identities without a separability assumption, let $A=(a_{ij})$ represent an $L$-linear map on $L^s$. Over $K$, each entry becomes the block representing multiplication by $a_{ij}$ on $L$. The sum of the traces of the diagonal blocks is

$$
\operatorname{tr}_K(A)=\operatorname{Tr}_{L/K}\left(\sum_i a_{ii}\right).
$$

We also have

$$
\det_K(A)=N_{L/K}(\det_L A). \tag{2}
$$

If $A$ is singular, a nonzero kernel vector makes both sides zero. If it is invertible, Gaussian elimination expresses it as a product of row additions, diagonal scalings and row interchanges. Both sides of (2) multiply under products. A row addition has determinant $1$ over both fields. Scaling one coordinate by $a$ gives determinant $N_{L/K}(a)$ over $K$. Interchanging two $L$-coordinates interchanges two blocks of size $[L:K]$, giving $(-1)^{[L:K]}=N_{L/K}(-1)$. This proves (2) for every factor and hence for $A$. Apply these two identities to multiplication by $x$ on $M$, considered first as an $L$-vector space. Its $L$-trace and determinant are precisely $\operatorname{Tr}_{M/L}(x)$ and $N_{M/L}(x)$. This proves both tower identities.

Finally, an embedding sends a monic equation over $\mathbb Z$ for $\alpha$ to the same equation for $\sigma(\alpha)$. Thus all those images are algebraic integers. Every elementary symmetric expression in them is an algebraic integer by the ring property. These expressions are the coefficients of $\chi_{\alpha,L/K}$, which already lie in $K$. They therefore lie in $\mathcal O_K$. $\square$

For $\alpha\in K$, Proposition 1.2 and (1) now give a second integrality test:

$$
\alpha\in\mathcal O_K\quad\Longleftrightarrow\quad
\chi_{\alpha,K/\mathbb Q}\in\mathbb Z[X]. \tag{3}
$$

The forward implication was proved above. For the converse, (1) shows that $\chi_{\alpha,K/\mathbb Q}(\alpha)=0$, so it is a monic integer equation for $\alpha$. In a quadratic field, its only nonleading coefficients are minus the trace and the norm. Hence trace and norm being integers is sufficient there. For larger degrees, (3) asks for all coefficients, not just those two.

For a concrete distinction, let $\gamma$ be a root of $X^3+\tfrac12X+1$. The polynomial $2X^3+X+2$ has none of its possible rational roots $\pm1,\pm2,\pm\tfrac12$, so the cubic is irreducible. In $\mathbb Q(\gamma)$, its trace is $0$ and its norm is $-1$, yet Proposition 1.1 shows that $\gamma$ is not an algebraic integer. Thus integer trace and norm, even norm $\pm1$, cannot replace the full integrality test.

**A real cyclotomic integer.** Let $t=2\cos(2\pi/7)=\zeta_7+\zeta_7^{-1}$. Roots of unity are algebraic integers since they satisfy $X^m-1$, so $t$ is one too. Dividing $1+\zeta_7+\cdots+\zeta_7^6=0$ by $\zeta_7^3$ gives

$$
1+t+(t^2-2)+(t^3-3t)=0.
$$

Thus $t^3+t^2-2t-1=0$. This cubic has no rational root: a rational root of a monic integer polynomial must be an integer dividing its constant coefficient, and neither $1$ nor $-1$ is a root. It is therefore the minimal polynomial. Sending $\zeta_7$ to $\zeta_7^j$ gives the three distinct conjugates

$$
2\cos(2\pi/7),\quad2\cos(4\pi/7),\quad2\cos(6\pi/7).
$$

They are distinct because cosine decreases on $(0,\pi)$. In $\mathbb Q(t)$, the trace of $t$ is $-1$ and its norm is $1$. In $\mathbb Q(\zeta_7)$, each image occurs twice, so its trace is $-2$ and its norm is $1$.

**Proposition 1.3 (recognizing units).** For $\alpha\in\mathcal O_K$,

$$
\alpha\in\mathcal O_K^\times\quad\Longleftrightarrow\quad
N_{K/\mathbb Q}(\alpha)=\pm1.
$$

*Proof.* If $\alpha\beta=1$ with $\beta\in\mathcal O_K$, multiplicativity gives $N(\alpha)N(\beta)=1$. Both factors are integers, so $N(\alpha)=\pm1$. Conversely, write

$$
\chi_{\alpha,K/\mathbb Q}=X^n+b_1X^{n-1}+\cdots+b_n.
$$

All $b_j$ are integers and $b_n=(-1)^nN(\alpha)=\pm1$. Put $b_0=1$. Since this polynomial vanishes at $\alpha$,

$$
\alpha^{-1}=-b_n^{-1}\sum_{j=0}^{n-1}b_j\alpha^{n-1-j}\in\mathcal O_K.
$$

The norm hypothesis ensures $\alpha\ne0$, so this division is valid. $\square$

For example, $1+\sqrt2$ satisfies $X^2-2X-1$, has trace $2$, norm $-1$, and inverse $\sqrt2-1$. Similarly, $2+\sqrt3$ satisfies $X^2-4X+1$, has trace $4$, norm $1$, and inverse $2-\sqrt3$. These equations prove integrality as well as invertibility.

## 4. Solving the quadratic case completely

Let $d\ne0,1$ be a squarefree integer, possibly negative. Write $s=\sqrt d$ and $K=\mathbb Q(s)$. Its nonidentity automorphism sends $s$ to $-s$. Thus, for $a,b\in\mathbb Q$,

$$
\operatorname{Tr}(a+bs)=2a,\qquad N(a+bs)=a^2-db^2.
$$

**Theorem 1.4 (quadratic rings of integers).**

$$
\mathcal O_{\mathbb Q(\sqrt d)}=
\begin{cases}
\mathbb Z[\sqrt d],&d\equiv2,3\pmod4,\\
\mathbb Z[(1+\sqrt d)/2],&d\equiv1\pmod4.
\end{cases}
$$

*Proof.* If $a+bs$ is integral, its trace and norm are integers. Set $u=2a\in\mathbb Z$, $v=2b\in\mathbb Q$. Then

$$
dv^2=u^2-4N(a+bs)\in\mathbb Z.
$$

Write $v=r/q$ in lowest terms with $q>0$. The condition implies $q^2\mid d$, because $r$ and $q$ are coprime. Squarefreeness of $|d|$ forces $q=1$. Thus $v\in\mathbb Z$, and norm integrality becomes

$$
u^2\equiv dv^2\pmod4. \tag{4}
$$

If $d\equiv2$ or $3\pmod4$, odd $v$ would force a square to be $2$ or $3\pmod4$. Therefore $v$ is even, and (4) makes $u$ even too. We obtain $a,b\in\mathbb Z$.

If $d\equiv1\pmod4$, (4) holds exactly when $u,v$ have the same parity. In that case

$$
\frac{u+vs}{2}=\frac{u-v}{2}+v\frac{1+s}{2}
$$

belongs to the asserted integer span. Conversely, every element satisfying these parity conditions has integer trace and norm, so is integral by the quadratic case of (3). Equivalently, the extra generator $w=(1+s)/2$ satisfies

$$
w^2-w+\frac{1-d}{4}=0.
$$

In each case the two displayed generators are linearly independent over $\mathbb Q$ and span exactly the ring described. $\square$

For $d=5$, $w=(1+\sqrt5)/2$ satisfies $X^2-X-1$, with trace $1$ and norm $-1$. It is an integer and a unit. For $d=3$, $(1+\sqrt3)/2$ has trace $1$ but norm $-1/2$, and minimal polynomial $X^2-X-1/2$. It is not integral.

Negative $d$ uses the same congruences. Since $-3\equiv1\pmod4$, putting $\omega=(-1+\sqrt{-3})/2$ gives

$$
\mathcal O_{\mathbb Q(\sqrt{-3})}=\mathbb Z[\omega],\qquad
\omega^2+\omega+1=0.
$$

The integer $\omega$ has trace $-1$ and norm $1$, but does not lie in $\mathbb Z[\sqrt{-3}]$. Indeed,

$$
\mathbb Z[\sqrt{-3}]=\{a+2b\omega:a,b\in\mathbb Z\},
$$

since $\sqrt{-3}=1+2\omega$. The two additive cosets are represented by $0,\omega$. Thus even an integral primitive generator can generate a proper subring of the full ring of integers.

For $d=-1$, Theorem 1.4 gives $\mathcal O_{\mathbb Q(i)}=\mathbb Z[i]$. The norm of $a+bi$ is $a^2+b^2$. Proposition 1.3 reduces the unit equation to $a^2+b^2=1$, whose integer solutions give exactly $1,-1,i,-i$. Their traces are $2,-2,0,0$, respectively, and all have norm $1$.

## 5. When irreducible elements stop factoring uniquely

In a domain, a **unit** has a multiplicative inverse in the domain. Two elements are **associates** if one is a unit times the other. A nonzero nonunit is **irreducible** if every factorization of it has a unit factor. Unique factorization requires that products of irreducibles representing the same element agree up to associates and reordering.

**Proposition 1.5.** The ring $\mathbb Z[\sqrt{-5}]$ is not a unique factorization domain.

*Proof.* Since $-5\equiv3\pmod4$, this is the full ring of integers. Write $s=\sqrt{-5}$. For $a,b\in\mathbb Z$,

$$
N(a+bs)=a^2+5b^2.
$$

The only elements of norm $1$ are $\pm1$, so these are its units. No element has norm $2$ or $3$: if $b\ne0$ the norm is at least $5$, and if $b=0$ it is a square. Now

$$
6=2\cdot3=(1+s)(1-s),\qquad
N(2)=4,\ N(3)=9,\ N(1\pm s)=6.
$$

A factorization of $2$ into nonunits would split $4$ into two integer norms greater than $1$, necessarily $2\cdot2$. A factorization of $3$ would similarly require $3\cdot3$; one of $1\pm s$ would require $2\cdot3$. All are impossible. The four factors are irreducible. Associates have the same norm, so all pairs with different norms are excluded. Finally $1+s$ is neither $1-s$ nor $-(1-s)$, excluding the remaining pair. These are two inequivalent factorizations. $\square$

Integral closedness has therefore not restored unique factorization of elements. The next arithmetic step changes the objects being factored. *Discrete valuation rings and Dedekind domains* develops ideal factorization; *Noether's axioms for Dedekind domains* presents its global axiomatic proof.

## 6. Exercises

1. **Easy.** Show that $\sqrt2+\sqrt3$ is an algebraic integer and find its minimal polynomial over $\mathbb Q$.
2. **Easy.** Compute the trace and norm of $1+\sqrt[3]2+\sqrt[3]4$ in $\mathbb Q(\sqrt[3]2)$. Decide whether it is a unit and exhibit its inverse if it is.
3. **Medium.** Prove that $2,3,1+\sqrt{-5},1-\sqrt{-5}$ are irreducible and pairwise nonassociate in $\mathbb Z[\sqrt{-5}]$. Also show directly that $2$ is not prime.
4. **Medium.** If $\alpha$ is a root of $X^2+3$, show that $\mathbb Z[\alpha]$ is not integrally closed in its fraction field and identify its integral closure.
5. **Hard (Kronecker's theorem).** An algebraic integer all of whose distinct conjugates have absolute value $1$ is a root of unity. Prove this by considering polynomials whose roots are powers of its conjugates.
6. **Hard.** For $K=\mathbb Q(\sqrt2,\sqrt3)$, prove that

   $$
   1,\quad\sqrt2,\quad\sqrt3,\quad\frac{\sqrt2+\sqrt6}{2}
   $$

   is a $\mathbb Z$-basis of $\mathcal O_K$. Define the discriminant of such a basis as $\det(\operatorname{Tr}_{K/\mathbb Q}(b_i b_j))$. Compute $d_K=2304$ and verify $2304=8\cdot12\cdot24$, the product of the discriminants of the three quadratic subfields.

## 7. Complete solutions

**1.** Put $s=\sqrt2$, $t=\sqrt3$, $z=s+t$. The ring property proves integrality. Since $z^2=5+2\sqrt6$, we have $(z^2-5)^2=24$, giving $z^4-10z^2+1=0$.

For minimality, first $\sqrt3\notin\mathbb Q(\sqrt2)$. If $t=a+bs$ with rational $a,b$, squaring forces $ab=0$. The alternatives would make $3$ or $3/2$ a rational square; prime exponents show neither is. Hence $[\mathbb Q(s,t):\mathbb Q]=4$. But $z(t-s)=1$, so

$$
s=\frac{z-z^{-1}}2,\qquad t=\frac{z+z^{-1}}2.
$$

Thus $\mathbb Q(z)=\mathbb Q(s,t)$ has degree $4$, and the displayed quartic is the minimal polynomial. Its distinct roots are the four signed sums $\pm s\pm t$.

**2.** Put $c=\sqrt[3]2$, so $c^3=2$ and $1,c,c^2$ is a basis. Multiplication by $\beta=1+c+c^2$ has matrix

$$
\begin{pmatrix}1&2&2\\1&1&2\\1&1&1\end{pmatrix}.
$$

Its trace is $3$ and determinant is $1$. Its characteristic polynomial is $X^3-3X^2-3X-1$. The element is integral because it is a sum of algebraic integers, and norm $1$ makes it a unit. More directly,

$$
(c-1)(1+c+c^2)=c^3-1=1,
$$

so its inverse is $c-1\in\mathcal O_K$.

**3.** The norm $a^2+5b^2$ is positive for nonzero elements, and norms $2,3$ cannot occur. The only units are $\pm1$. A nontrivial factorization would require norms $2,2$ for $2$, norms $3,3$ for $3$, or norms $2,3$ for $1\pm\sqrt{-5}$; none exists. Their norms $4,9,6,6$ separate every pair except the last. Those two differ neither by $1$ nor by $-1$, so all four are pairwise nonassociate.

Nevertheless $2$ divides $(1+\sqrt{-5})(1-\sqrt{-5})=6$, and divides neither factor: dividing either by $2$ gives half-integer coefficients in the basis $1,\sqrt{-5}$. Thus it is irreducible but not prime.

**4.** The fraction field is $\mathbb Q(\alpha)$, with $\alpha^2=-3$. The element $w=(1+\alpha)/2$ satisfies $w^2-w+1=0$, a monic equation even over $\mathbb Z[\alpha]$, but $w\notin\mathbb Z[\alpha]$. The ring is not integrally closed. Its integral closure is

$$
\mathcal O_{\mathbb Q(\alpha)}=\mathbb Z[w]
$$

by Theorem 1.4. To check that “integral closure” over $\mathbb Z[\alpha]$ gives the same answer as over $\mathbb Z$, note that $\mathbb Z[\alpha]$ is integral over $\mathbb Z$. Transitivity makes every element integral over it an algebraic integer. Conversely, every algebraic integer satisfies a monic equation over $\mathbb Z\subset\mathbb Z[\alpha]$.

**5.** Let $\alpha_1,\ldots,\alpha_d$ be the distinct conjugates of $\alpha$, and let $F=\mathbb Q(\alpha)$. For every positive integer $m$,

$$
P_m(X)=\prod_{j=1}^d(X-\alpha_j^m)
$$

is the characteristic polynomial of multiplication by $\alpha^m$ on $F$. Proposition 1.2 makes it a monic polynomial in $\mathbb Z[X]$, even if some powers coincide. Its coefficient of $X^{d-k}$ has absolute value at most $\binom dk$: it is a sum of that many products, each of absolute value $1$. There are therefore only finitely many possible $P_m$.

The union of the root sets of these finitely many polynomials is finite. It contains every $\alpha^m$, so $\alpha^r=\alpha^s$ for some $r>s>0$. Since $|\alpha|=1$, $\alpha\ne0$, and division yields $\alpha^{r-s}=1$. This proves the theorem. Finiteness of the polynomials alone would not justify matching their roots in the same order; using their finite union avoids that issue.

### A biquadratic integral basis

**6.** Put $s=\sqrt2$, $t=\sqrt3$, $u=st=\sqrt6$, and $v=(s+u)/2$. Solution 1 proved $[K:\mathbb Q]=4$. Its four embeddings independently change the signs of $s,t$. The elements $1,s,t$ are integral, and

$$
v^2=2+t,\qquad (v^2-2)^2=3,\qquad v^4-4v^2+1=0
$$

shows that $v$ is integral. The proposed four elements are a $\mathbb Q$-basis, since replacing $u$ by $v=(s+u)/2$ is an invertible change of basis. Their integer span is therefore contained in $\mathcal O_K$. The essential remaining step is to prove it contains every integer.

Write $x=a+bs+ct+eu\in\mathcal O_K$, with rational coefficients. The relative traces to $\mathbb Q(s),\mathbb Q(t),\mathbb Q(u)$ are respectively

$$
2a+2bs,\qquad2a+2ct,\qquad2a+2eu.
$$

They lie in the corresponding quadratic rings of integers, which are $\mathbb Z[s],\mathbb Z[t],\mathbb Z[u]$. Thus $2a,2b,2c,2e$ are integers. We can write

$$
x=\frac{A+Bs+Ct+Du}{2},\qquad A,B,C,D\in\mathbb Z.
$$

Its relative norm to $\mathbb Q(s)$, obtained by changing the sign of $t$, equals

$$
\frac{A^2+2B^2-3C^2-6D^2}{4}
+\frac{AB-3CD}{2}s.
$$

Since it lies in $\mathbb Z[s]$, its rational coefficient is an integer. Reducing its numerator modulo $2$ gives $A\equiv C\pmod2$. The relative norm to $\mathbb Q(t)$ is

$$
\frac{A^2+3C^2-2B^2-6D^2}{4}
+\frac{AC-2BD}{2}t.
$$

Its $t$-coefficient must be integral, so $AC$ is even. Together with equal parity, this forces both $A,C$ even. Return to the first norm's rational coefficient and reduce its numerator modulo $4$. We obtain $2B^2-6D^2\equiv0\pmod4$, hence $B\equiv D\pmod2$. It follows that

$$
x=\frac A2+\frac{B-D}{2}s+\frac C2t+Dv
$$

has integer coefficients in the proposed basis. This proves the basis assertion, without presupposing the answer from a discriminant calculation.

The absolute trace of $a+bs+ct+eu$ is $4a$. Using $s^2=2$, $t^2=3$, $sv=1+t$ and $v^2=2+t$, the trace matrix in the order $1,s,t,v$ is

$$
G=\begin{pmatrix}
4&0&0&0\\
0&8&0&4\\
0&0&12&0\\
0&4&0&8
\end{pmatrix}.
$$

Therefore

$$
d_K=\det G=4\cdot12\cdot(8\cdot8-4\cdot4)=2304.
$$

This value is independent of the integer basis: changing between two such bases uses an integer matrix whose inverse is also integral, hence whose determinant is $\pm1$. The Gram determinant changes by the square of that determinant. Finally, the quadratic bases $1,\sqrt d$ for $d=2,3,6$ have trace matrices $\operatorname{diag}(2,2d)$, so their discriminants are $8,12,24$. Their product is $2304$, as claimed. The equality here is a computation, not an assumed general formula for composita.

## What this lesson does not prove

The finite-module criterion, transitivity and ring property of integrality were proved in Section 2 without a Noetherian hypothesis. The same section proves Gauss's lemma in the forms used here, Eisenstein's criterion and the rational-root test. Section 1 proves degree multiplication, the embedding count and the primitive element theorem for every finite separable extension. These full arguments supply the imports of the following lessons; the Stacks and Milne links are additional human-source context.

Matrix trace, determinant, Gaussian elimination and change of basis are assumed from linear algebra. We have proved the arithmetic propositions and both hard exercises. We have not proved the general existence of integral bases, ideal factorization, or the general discriminant theory; the following lessons develop those topics. [Stacks, Tag 0BIE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-section-trace-pairing) is the section *Trace and norm*, giving broader algebraic context for Section 3.

## References

- **[Milne ANT]** J. S. Milne, *Algebraic Number Theory*, version 3.08, 2020, Chapter 2, from *First proof that the integral elements form a ring* through *Review of norms and traces*. [Author's lecture notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- **[Milne FGT]** J. S. Milne, *Fields and Galois Theory*, version 5.10, 2022, Chapters 1–3 and the primitive element theorem in Chapter 5. [Author's lecture notes](https://www.jmilne.org/math/CourseNotes/FT.pdf).
- **[Stacks]** The Stacks project authors, *The Stacks project*. The tag citations here link to the corresponding statements in the AI Integrated Stacks Project: [00GM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-integral), [00GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-transitive), [00GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-closure-is-ring), [030N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-primitive-element), and [0BIE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-section-trace-pairing). The AI Integrated Stacks Project is an edition with AI-proposed corrections and AI-written additions, not reviewed by the maintainers of the [official Stacks project](https://stacks.math.columbia.edu/).
