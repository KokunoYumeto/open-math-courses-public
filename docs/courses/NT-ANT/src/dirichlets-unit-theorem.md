# Dirichlet's unit theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

The units of a number field can be infinite, but their multiplicative freedom has a finite dimension. Taking absolute values at the infinite places and then logarithms turns multiplication into addition. The norm forces these vectors into a hyperplane. Dirichlet's theorem says that they fill a complete lattice in that hyperplane.

## Places, norms, and prerequisites

Let \(K\) have signature \((r_1,r_2)\). Put \(m=r_1+r_2\), \(r=m-1\), and \(U=O_K^\times\). At a real place represented by \(\sigma\), set \(|a|_v=|\sigma a|\); at a complex place represented by \(\tau\), set
\[
|a|_v=|\tau a|^2.
\]
Thus
\[
\prod_{v\mid\infty}|a|_v=|N_{K/\mathbf Q}a|.
\tag{1}
\]
Define
\[
\lambda:K^\times\longrightarrow\mathbf R^m,\qquad
\lambda(a)=(\log|a|_v)_{v\mid\infty},
\qquad
H=\{x\in\mathbf R^m\mid\textstyle\sum_v x_v=0\}.
\tag{2}
\]
All logarithms are real natural logarithms.

From [*Lattices, Minkowski's theorem and the Minkowski embedding*](lattices-minkowskis-theorem-and-the-minkowski-embedding.md), we use Theorem 7.1, Proposition 7.2, and the lattice structure lemma: \(O_K\) is a complete lattice of covolume \(2^{-r_2}\sqrt{|d_K|}\), and a discrete subgroup has a free integral basis spanning its real span. From [*Finiteness of the class number*](finiteness-of-the-class-number.md) we use the bounded-ideal lemma and Corollary 8.2. Ideal norms are those of Proposition 4.1 in [*Norms, class groups, and modules over Dedekind domains*](norms-class-groups-and-modules-over-dedekind-domains.md).

An algebraic integer \(a\) is a unit precisely when \(|N a|=1\): the principal integral ideal \((a)\) has norm \(|N a|\), and norm \(1\) means it equals \(O_K\). Hence \(\lambda(U)\subseteq H\).

The complex factor \(2\) is part of the convention throughout this lesson, including the regulator.

## The kernel and discreteness

Write \(\mu_K\) for the roots of unity in \(K\).

**Kronecker lemma.** If a nonzero algebraic integer \(a\in K\) has every conjugate of modulus \(1\), then \(a\) is a root of unity.

**Proof.** All the powers \(a^j\), \(j\geq0\), lie in \(O_K\), and all their embedding coordinates have modulus \(1\). Their images lie in a fixed bounded subset of the Minkowski space. A bounded set meets the lattice \(O_K\) in finitely many points. Thus two powers agree, \(a^j=a^k\) with \(j>k\), and \(a^{j-k}=1\). \(\square\)

**Proposition 9.1.** The group \(\mu_K\) is finite cyclic, \(\ker(\lambda|_U)=\mu_K\), and \(\lambda(U)\) is discrete in \(H\).

**Proof.** Roots of unity are integral and all their conjugates have modulus \(1\); the same bounded-lattice argument makes their set finite. A finite multiplicative subgroup of a field is cyclic, by the elementary cyclicity lemma proved in the Gaussian example of [*Decomposition of primes in extensions*](decomposition-of-primes-in-extensions.md). This applies to \(K\), not only to finite fields.

Every root of unity has zero logarithms. Conversely a unit with zero logarithms satisfies the Kronecker lemma, proving the kernel assertion.

If \(\lambda(u)\) lies in any fixed bounded subset of \(H\), all the usual embedding moduli of \(u\) are bounded above. There are only finitely many such \(u\in O_K\), again by the lattice property. Therefore every bounded subset of \(H\) meets \(\lambda(U)\) in finitely many points. In particular a neighborhood of zero can be shrunk to exclude all its nonzero points. This proves discreteness. \(\square\)

Integrality matters in the Kronecker lemma. The number \((3+4i)/5\) and its conjugate both have modulus \(1\), but the number is not integral: its monic minimal polynomial is \(X^2-\frac65X+1\). The lemma does not apply to it.

## Producing enough units

The difficult part is to prove that the logarithm lattice spans all of \(H\). We first show that unit logarithms stay within a bounded distance of every point of \(H\).

**Approximation lemma.** There is a constant \(B\), depending only on \(K\), such that for every \(x\in H\), some \(u\in U\) satisfies
\[
|\lambda(u)_v-x_v|\leq B
\quad\hbox{for every infinite place }v.
\tag{3}
\]

**Proof.** Choose \(C>1\) so large that
\[
2^{r_1}\pi^{r_2}C^m
\geq2^{r_1+r_2}\sqrt{|d_K|}.
\tag{4}
\]
For \(x\in H\), form a compact product region with real intervals and complex discs whose normalized absolute values are bounded by \(Ce^{x_v}\). Its real radii are \(Ce^{x_v}\); its complex radii are \((Ce^{x_v})^{1/2}\). Its volume is
\[
2^{r_1}\pi^{r_2}C^m e^{\sum_v x_v}
=2^{r_1}\pi^{r_2}C^m.
\]
By (4) and Minkowski, it contains a nonzero \(a\in O_K\). For this element,
\[
\lambda(a)_v\leq x_v+\log C,\qquad
1\leq|Na|\leq C^m.
\tag{5}
\]

Only finitely many principal integral ideals have norm at most \(C^m\), by the bounded-ideal lemma. Choose one nonzero generator \(b_j\) for each of these ideals. Since \((a)\) equals one of them, \(u=a/b_j\) is a unit. Consequently
\[
\lambda(u)_v-x_v\leq \log C-\lambda(b_j)_v.
\]
Choose \(A\geq1\) bounding every quantity on the right, over the finite set of \(j,v\). The differences \(\lambda(u)_v-x_v\) have sum zero; since each is at most \(A\), each is at least \(-(m-1)A\). Taking \(B=\max(1,m-1)A\) proves (3), including \(m=1\). \(\square\)

**Theorem 9.2 (Dirichlet).** The group of units has the form
\[
O_K^\times\cong\mu_K\times\mathbf Z^{r_1+r_2-1}.
\]
More precisely, \(\lambda(U)\) is a complete lattice in \(H\).

**Proof.** If \(m=1\), then \(H=\{0\}\), and Proposition 9.1 gives \(U=\mu_K\). Assume \(m\geq2\), and number the infinite places \(1,\ldots,m\). Choose \(T>B\). For each \(i\leq r=m-1\), apply (3) to the vector
\[
x^{(i)}_i=(m-1)T,\qquad x^{(i)}_j=-T\ (j\ne i).
\]
It belongs to \(H\). We obtain a unit \(u_i\) whose logarithm is negative at every place except \(i\); its \(i\)-th logarithm is positive because all coordinates sum to zero.

Make the \(r\times r\) matrix \(A\) with row \(i\) consisting of the first \(r\) coordinates of \(\lambda(u_i)\). All off-diagonal entries are negative, and
\[
A_{ii}>\sum_{\substack{j\leq r\\j\ne i}}|A_{ij}|,
\tag{6}
\]
because the omitted \(m\)-th coordinate is also strictly negative.

This strict diagonal dominance implies that \(A\) is invertible. If \(Az=0\) and \(z\ne0\), choose \(i\) with \(|z_i|=\max_j|z_j|>0\). The \(i\)-th equation and the triangle inequality give
\[
A_{ii}|z_i|
\leq\sum_{j\ne i}|A_{ij}|\,|z_j|
\leq\left(\sum_{j\ne i}|A_{ij}|\right)|z_i|,
\]
contradicting (6). Thus the \(r\) logarithm vectors are real linearly independent.

Proposition 9.1 and the lattice structure lemma now make \(\lambda(U)\) a free abelian group of rank \(r\), spanning \(H\). Choose a \(\mathbf Z\)-basis \(v_1,\ldots,v_r\) of this lattice, and units \(\varepsilon_i\) with \(\lambda(\varepsilon_i)=v_i\). Each unit has a unique expression
\[
u=\zeta\varepsilon_1^{a_1}\cdots\varepsilon_r^{a_r},
\qquad \zeta\in\mu_K,\quad a_i\in\mathbf Z.
\tag{7}
\]
Existence follows by subtracting the basis expression for \(\lambda(u)\); the remaining element is in the kernel. Uniqueness follows from independence and the kernel description. This proves the direct product assertion. \(\square\)

The \(\varepsilon_i\) in (7) are a **fundamental system of units**. The sign-pattern units constructed during the proof establish the rank; their logarithms need not themselves be an integral basis. This proof combines the bounded-ideal construction and the diagonal dominance mechanism in [Milne, 5.9–5.10].

## The regulator

Let \(\varepsilon_1,\ldots,\varepsilon_r\) be a fundamental system, and let \(L\) be the \(m\times r\) matrix with column \(i\) equal to \(\lambda(\varepsilon_i)\). For an infinite place \(v\), delete its row to obtain \(L^{(v)}\). Define
\[
R_K=|\det L^{(v)}|.
\tag{8}
\]
When \(r=0\), the matrix is empty and its determinant is defined to be \(1\), so \(R_K=1\).

**Proposition 9.3.** The positive number \(R_K\) is independent of the omitted place and the fundamental system. For ordinary Euclidean measure on \(H\subseteq\mathbf R^m\),
\[
\operatorname{covol}_H\lambda(U)=\sqrt m\,R_K.
\tag{9}
\]

**Proof.** The sum of the rows of \(L\) is zero. The last row is therefore minus the sum of the first \(r\) rows. In a minor omitting row \(i<m\), replace the last row by that sum and expand multilinearly. All summands vanish from a repeated row except the missing \(i\)-th row. Thus its determinant differs from the minor omitting row \(m\) only by a sign. All minors have the same absolute value. They are nonzero because projection deleting any coordinate is an isomorphism \(H\to\mathbf R^r\).

Another fundamental system changes the column basis by a matrix in \(\mathrm{GL}_r(\mathbf Z)\); multiplying its determinant by \(\pm1\) leaves (8) unchanged. Root-of-unity factors contribute zero logarithms.

To compute the Euclidean covolume, append the unit normal vector \(q=(1,\ldots,1)/\sqrt m\) as a first column to \(L\). The absolute determinant of this square matrix is the Euclidean volume of the logarithm parallelepiped, because \(q\) is perpendicular to \(H\) and has length \(1\). Adding all rows to the last row makes its first entry \(\sqrt m\) and its other entries zero. Expansion gives \(\sqrt m|\det L^{(m)}|\), proving (9). The same formula gives \(1\) when \(m=1\). \(\square\)

If \(r\) independent units generate a subgroup of index \(q\) modulo \(\mu_K\), their determinant is \(qR_K\): express their logarithms in a fundamental basis and use the determinant-index formula of Lesson 2. Thus finding independent units alone does not establish their fundamentality.

## Units with allowed finite denominators

Let \(S\) be a **finite** set of places of \(K\) containing all infinite places. Write its finite places as \(\mathfrak p_1,\ldots,\mathfrak p_t\), and define
\[
O_{K,S}=\{a\in K\mid v_{\mathfrak p}(a)\geq0
\text{ for every finite }\mathfrak p\notin S\},
\]
\[
U_S=O_{K,S}^{\times}
=\{a\in K^\times\mid v_{\mathfrak p}(a)=0
\text{ for every finite }\mathfrak p\notin S\}.
\]
Here \(v_{\mathfrak p}(a)\) is the exponent of \(\mathfrak p\) in \((a)\), and may be negative.

**Theorem 9.4 (S-unit theorem).** There is an isomorphism
\[
U_S\cong\mu_K\times\mathbf Z^{|S|-1}.
\]

**Proof.** Consider the valuation homomorphism
\[
\nu:U_S\longrightarrow\mathbf Z^t,\qquad
a\longmapsto(v_{\mathfrak p_1}(a),\ldots,v_{\mathfrak p_t}(a)).
\]
Its kernel is \(U\), by unique factorization of fractional ideals. Its image is exactly the kernel of
\[
\mathbf Z^t\longrightarrow\mathrm{Cl}_K,\qquad
(a_i)\longmapsto\prod_i[\mathfrak p_i]^{a_i}.
\tag{10}
\]
Indeed the indicated product class is trivial precisely when the corresponding fractional ideal is \((a)\) for some \(a\in K^\times\), whose other valuations are zero.

Let \(h=h_K\). Lagrange's theorem in the finite class group gives \(\mathfrak p_i^h=(a_i)\) for some \(a_i\). These are S-units, and their valuation vectors are \(h\) times the standard basis vectors. Thus the image \(V=\nu(U_S)\) contains \(h\mathbf Z^t\) and is a free abelian subgroup of rank \(t\). Choose a basis of \(V\) and lift it to elements of \(U_S\). The subgroup on those lifts maps isomorphically to \(V\): any relation would induce a relation in its free basis. Every S-unit is a product of a lift and an ordinary unit. Therefore
\[
U_S\cong U\times\mathbf Z^t
\cong\mu_K\times\mathbf Z^{r+t},
\]
and \(r+t=|S|-1\). This also covers \(t=0\). \(\square\)

Normalize the absolute value at a finite prime by
\(|a|_{\mathfrak p}=(N\mathfrak p)^{-v_{\mathfrak p}(a)}\). Ideal norms and (1) give
\[
\prod_{v\mid\infty}|a|_v
\prod_{\mathfrak p}|a|_{\mathfrak p}=1.
\tag{11}
\]
For an S-unit the product is over \(S\), so its S-logarithms again have sum zero. For \(K=\mathbf Q\) and \(S=\{\infty,2,3,5\}\), the theorem reads
\[
U_S=\{\pm2^a3^b5^c\mid a,b,c\in\mathbf Z\}.
\]
Finiteness of \(S\) is required: allowing every rational prime gives \(\mathbf Q^\times\), whose prime-exponent group has infinitely many independent generators.

## Fundamental units in real quadratic fields

Fix the positive square root of a squarefree \(d>1\), and use that real embedding. The roots of unity are \(\{\pm1\}\), since a real root of unity is \(1\) or \(-1\). Dirichlet's theorem gives
\[
U=\{\pm\varepsilon^k\mid k\in\mathbf Z\}
\]
with a unique choice \(\varepsilon>1\) of generator. It is the smallest unit greater than \(1\). Its regulator is \(\log\varepsilon\).

In the full ring write \(u=(a+b\sqrt d)/q\), where \(q=1\) for \(d\equiv2,3\pmod4\), and \(q=2\) for \(d\equiv1\pmod4\), with \(a\equiv b\pmod2\) in the latter case. The unit equation is
\[
a^2-db^2=\pm q^2.
\tag{12}
\]
If \(1<u<E\), its conjugate \(u'\) equals \(1/u\) or \(-1/u\). Hence
\[
0<b=\frac{q(u-u')}{2\sqrt d}
<\frac{q(E+1)}{2\sqrt d}.
\tag{13}
\]
This reduces a proposed fundamental unit to a finite, complete coefficient search.

| Field | Fundamental unit \(\varepsilon>1\) | Norm | Coefficients to check below it |
| --- | --- | --- | --- |
| \(\mathbf Q(\sqrt2)\) | \(1+\sqrt2\) | \(-1\) | \(b=1\) |
| \(\mathbf Q(\sqrt3)\) | \(2+\sqrt3\) | \(1\) | \(b=1\) |
| \(\mathbf Q(\sqrt5)\) | \((1+\sqrt5)/2\) | \(-1\) | \(b=1\) |
| \(\mathbf Q(\sqrt7)\) | \(8+3\sqrt7\) | \(1\) | \(b=1,2,3\) |

The bounds in the last column follow directly from (13). For \(d=2\), the possibilities \(a^2=2b^2\pm1\) at \(b=1\) are \(1,3\); the only positive unit greater than \(1\) is the listed one. For \(d=3\), they are \(2,4\), giving \(2+\sqrt3\). For \(d=5\), the full half-integral equation gives \(a^2=5\pm4=1,9\); the \(a=1\) unit is the listed one, \(a=3\) gives a larger unit, and negative choices give values below \(1\).

For \(d=7\), the pairs \(7b^2\pm1\) for \(b=1,2,3\) are
\[
(6,8),\quad(27,29),\quad(62,64).
\]
Only \(64\) is a square; it gives \(8+3\sqrt7\). Each candidate satisfies (12), so is a unit, and the exhaustive searches show that there is no smaller unit greater than \(1\). These are therefore fundamental.

The full-ring equation for \(d\equiv1\pmod4\) must be \(\pm4\), rather than just \(\pm1\); omitting half-integral units would miss the fundamental unit of \(\mathbf Q(\sqrt5)\).

## The cubic field \(\mathbf Q(\sqrt[3]{2})\)

Let \(\alpha=\sqrt[3]{2}\) in its unique real embedding. We know \(O_K=\mathbf Z[\alpha]\), \(d_K=-108\), and unit rank \(1\). The element \(\beta=\alpha-1\) satisfies
\[
\beta^3+3\beta^2+3\beta-1=0,
\]
so \(N\beta=1\); moreover
\[
\varepsilon=\beta^{-1}=\alpha^2+\alpha+1.
\tag{14}
\]
We prove that \(\varepsilon\) is the fundamental unit greater than \(1\).

First there is no unit \(\eta\) with \(1<\eta\leq2\). Such a unit is not rational, because the rational units in \(O_K\) are \(\pm1\), and hence generates the cubic field. Its other conjugates are a nonreal conjugate pair. Its norm is positive and is a unit integer, so it is \(1\). Write the conjugates as
\[
\eta,\quad\eta^{-1/2}e^{i\theta},\quad
\eta^{-1/2}e^{-i\theta}.
\]
The product-of-differences discriminant formula gives
\[
|\operatorname{disc}(1,\eta,\eta^2)|
=4(\eta^{3/2}+\eta^{-3/2}-2\cos\theta)^2\sin^2\theta
\leq4(\eta^{3/2}+\eta^{-3/2}+2)^2.
\tag{15}
\]
The function \(s+s^{-1}\) increases for \(s\geq1\). If \(\eta\leq2\), the last expression is at most
\[
4\left(\frac94\sqrt2+2\right)^2
=\frac{113}{2}+36\sqrt2<108.
\]
For example \(\sqrt2<103/72\) proves the strict inequality by squaring the positive rational bound. But the discriminant-index formula of Lesson 2 says that this order discriminant is \(108\) times a positive integer square. This contradiction excludes the interval.

Now \(\alpha<13/10\), since \((13/10)^3>2\); (14) implies \(1<\varepsilon<399/100<4\). If \(\varepsilon=\eta^k\) for the fundamental unit \(\eta>1\) and \(k\geq2\), then \(\eta\leq\sqrt\varepsilon<2\), which was just excluded. Thus \(k=1\). We have proved
\[
U=\{\pm(\alpha-1)^k\mid k\in\mathbf Z\},
\qquad R_K=\log(\alpha^2+\alpha+1).
\]
The supplied small unit \(\alpha-1\) is fundamental up to inversion; the convention greater than \(1\) selects its inverse.

## Units in a CM field

A **CM field** is a totally imaginary quadratic extension \(K/F\) of a totally real field \(F\). Its nontrivial \(F\)-automorphism will be denoted \(c\), or \(a\mapsto\overline a\). For every embedding \(\tau:K\hookrightarrow\mathbf C\),
\[
\tau(\overline a)=\overline{\tau(a)}.
\tag{16}
\]
Indeed choose \(b\notin F\) with \(c(b)=-b\), for instance subtract the two conjugates of an element outside \(F\). Then \(b^2\in F\) and \(K=F(b)\). Under each real embedding of \(F\), the value of \(b^2\) is negative; otherwise that embedding would extend to a real embedding of \(K\), contrary to total imaginarity. Its two square roots in \(\mathbf C\) are therefore imaginary conjugates, proving (16).

**Proposition 9.5 (CM unit index).** For a CM field,
\[
[O_K^\times:\mu_K O_F^\times]\in\{1,2\}.
\]

**Proof.** If \(u\in O_K^\times\), the quotient \(u/\overline u\) is an integral unit, and every conjugate has modulus \(1\), by (16). The Kronecker lemma makes it a root of unity. Thus
\[
f:O_K^\times\longrightarrow\mu_K/\mu_K^2,\qquad
u\longmapsto[u/\overline u]
\]
is a homomorphism.

For \(\zeta\in\mu_K\) and \(v\in O_F^\times\), complex conjugation sends \(\zeta\) to \(\zeta^{-1}\), so
\((\zeta v)/\overline{\zeta v}=\zeta^2\). Hence \(\mu_K O_F^\times\subseteq\ker f\).
Conversely, if \(u/\overline u=\zeta^2\), then
\[
\overline{u/\zeta}=\overline u\,\zeta=u/\zeta.
\]
Thus \(u/\zeta\in F\). It and its inverse are integral, so it belongs to \(O_F^\times\). This proves \(\ker f=\mu_K O_F^\times\).

The finite cyclic group \(\mu_K\) has even order, because it contains \(-1\). Its quotient by squares has order \(2\). The group \(O_K^\times/\mu_K O_F^\times\) injects into that quotient, so its order is \(1\) or \(2\). \(\square\)

For an explicit example let \(\zeta=e^{2\pi i/5}\) and \(K=\mathbf Q(\zeta)\). The real element \(t=\zeta+\zeta^{-1}\) satisfies \(t^2+t-1=0\), by \(1+\zeta+\cdots+\zeta^4=0\). Thus
\[
F=\mathbf Q(t)=\mathbf Q(\sqrt5),\qquad
\varphi=1+t=\frac{1+\sqrt5}{2}.
\]
Here \(t>0\) selects the displayed root. The element \(\zeta\) satisfies \(X^2-tX+1=0\) and is nonreal, so \(K/F\) is quadratic. Both real embeddings of \(F\) send \(t\) to a value of modulus less than \(2\), making the two corresponding quadratic roots nonreal. Thus \(K\) is CM.

We can determine its index without a cyclotomic integral-basis theorem. The fundamental real unit \(\varphi\) has norm \(-1\); the totally positive units of \(F\) are exactly \(\varphi^{2k}\). For every \(u\in O_K^\times\), its relative norm \(u\overline u\) is a totally positive unit of \(F\), hence \(\varphi^{2k}\). The unit \(u/\varphi^k\) then has relative norm \(1\), so all its conjugates have modulus \(1\). It is a root of unity. Therefore
\[
O_K^\times=\mu_K\varphi^{\mathbf Z},
\qquad [O_K^\times:\mu_K O_F^\times]=1,
\qquad R_K=2\log\varphi.
\]
The factor \(2\) in this last regulator comes from the complex-place normalization.

## Exercises

1. **Easy.** Find all units of \(\mathbf Z[i]\) and \(\mathbf Z[\omega]\), where \(\omega=(-1+\sqrt{-3})/2\). Prove that these are the only imaginary quadratic fields with more than two roots of unity.

2. **Medium.** Find the fundamental unit greater than \(1\) in \(\mathbf Q(\sqrt7)\) and \(\mathbf Q(\sqrt{13})\), and prove fundamentality in the full rings of integers.

3. **Medium.** For a real quadratic field with fundamental unit \(\varepsilon>1\), prove that a unit of norm \(-1\) exists if and only if \(N\varepsilon=-1\). Deduce that \(\mathbf Q(\sqrt3)\) and \(\mathbf Q(\sqrt7)\) have no unit of norm \(-1\).

4. **Hard.** Prove the CM unit index assertion of Proposition 9.5, including the identification of the kernel of the map to \(\mu_K/\mu_K^2\).

## Solutions

**1.** A Gaussian unit has norm \(a^2+b^2=1\), so the four units are \(1,-1,i,-i\). In the Eisenstein ring, the norm of \(a+b\omega\) is
\[
a^2-ab+b^2=(a-b/2)^2+3b^2/4.
\]
Norm \(1\) implies \(b=0,\pm1\). At \(b=0\) we get \(a=\pm1\); at \(b=1\), \(a=0,1\); at \(b=-1\), \(a=0,-1\). These give exactly \(\{\pm1,\pm\omega,\pm\omega^2\}\).

Now suppose an imaginary quadratic field contains a root of unity \(\zeta\ne\pm1\). It is nonreal, has degree \(2\), and its conjugate is \(\zeta^{-1}\). Its trace is an integer
\[
a=\zeta+\zeta^{-1},\qquad -2<a<2.
\]
Thus \(a=-1,0,1\), and its minimal polynomial is \(X^2-aX+1\). Their discriminants are respectively \(-3,-4,-3\). The field is consequently \(\mathbf Q(\sqrt{-3})\) or \(\mathbf Q(i)\). All imaginary quadratic units are roots of unity by Dirichlet's rank-zero case, so this also accounts for their full unit groups.

**2.** For \(\mathbf Q(\sqrt7)\), the candidate \(E=8+3\sqrt7\) has norm \(1\). Formula (13) forces \(b\leq3\) for any unit \(1<u<E\). The pairs of possible squares \(7b^2\pm1\) are \((6,8),(27,29),(62,64)\); the only square is \(64\), giving \(u=E\), or its conjugate below \(1\). Thus \(E\) is fundamental.

For \(\mathbf Q(\sqrt{13})\), the full ring is \(\mathbf Z[(1+\sqrt{13})/2]\). The candidate
\[
E=\frac{3+\sqrt{13}}2
\]
has norm \(-1\). If \(1<u<E\), formula (13) with \(q=2\) gives
\[
0<b<\frac{E+1}{\sqrt{13}}<2,
\]
so \(b=1\). Equation (12) then gives \(a^2=13\pm4=9,17\). Only \(9\) is a square, and \(a=3\) yields \(E\); \(a=-3\) yields a value below \(1\). The parity condition is satisfied. There is no smaller unit greater than \(1\), proving fundamentality. Its regulator is \(\log((3+\sqrt{13})/2)\).

**3.** Every unit is \(\pm\varepsilon^k\), and the norm of \(-1\) in a quadratic field is \(1\). Therefore its norm is \((N\varepsilon)^k\). A norm-\(-1\) unit exists precisely when \(N\varepsilon=-1\), in which case \(\varepsilon\) itself is one.

The full rings for \(d=3,7\) are \(\mathbf Z[\sqrt d]\). A norm-\(-1\) unit would solve \(a^2-db^2=-1\). Modulo \(3\) or \(7\), this would make \(-1\) a square. The square residues are \(0,1\) modulo \(3\), and \(0,1,2,4\) modulo \(7\); neither list contains \(-1\). Thus no such unit exists in either field, consistent with the norm-\(1\) fundamental units already computed.

**4.** Let \(c\) be the nontrivial automorphism of \(K/F\). Writing \(K=F(b)\) with \(c(b)=-b\) and \(b^2\) totally negative proves \(\tau(cu)=\overline{\tau(u)}\) for every embedding. For \(u\in O_K^\times\), \(u/c(u)\) is an integral unit with all conjugates of modulus \(1\), hence belongs to \(\mu_K\).

Map \(u\) to its class in \(\mu_K/\mu_K^2\). Every product \(\zeta v\), with \(\zeta\in\mu_K\), \(v\in O_F^\times\), maps to the square class of \(\zeta^2\), hence to the identity. Conversely if \(u/c(u)=\zeta^2\), then \(c(u/\zeta)=u/\zeta\). The quotient belongs to \(F\), and it and its inverse are integral, so it is a unit of \(O_F\). The kernel is exactly \(\mu_K O_F^\times\).

Finally \(\mu_K\) is cyclic of even order, so its quotient by squares has order \(2\). The quotient of the unit group by the identified kernel is its image in this order-two group, and has order \(1\) or \(2\). This is the desired index.

## What this lesson does not prove

We use the complete lattice structure and compact-equality Minkowski theorem of Lesson 7, the bounded-ideal lemma and class-group finiteness of Lesson 8, and multiplicative principal-ideal norms of Proposition 4.1. Finite multiplicative subgroups of fields are cyclic by the lemma proved in Lesson 5's Gaussian example. The quadratic and pure-cubic full rings and discriminants are imported from Lessons 1–2; the discriminant-index formula used in (15) is from Lesson 2.

The examples use complete bounded coefficient searches, so no continued-fraction theorem is imported. No algorithm based on the generalized Riemann hypothesis is needed. The regulator here uses normalized complex logarithms; later class-number formulas must use this same convention.

## References

- J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, Chapter 5, pp. 85–94: 5.5–5.10 for the logarithm lattice and rank; 5.11 for S-units; 5.12 for CM units; the section “Regulators”.
- E. Hecke, *Vorlesungen über die Theorie der algebraischen Zahlen*, 1923: §§34–35, Sätze 99–100, pp. 122–131.
