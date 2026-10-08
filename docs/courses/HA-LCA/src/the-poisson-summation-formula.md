# The Poisson summation formula

**Lesson HA-LCA-11.** Self-checked by the writing AI.

Poisson summation is Fourier inversion after averaging over a closed subgroup. The measures and the meaning of that average matter. We retain arbitrary locally compact Hausdorff abelian groups and the full complete Haar domains used in the preceding lessons.

Write \(E(t)=e^{2\pi it}\). Our Fourier transform uses the conjugate of the character:
\(\widehat f(\gamma)=\int f(x)\overline{\gamma(x)}\,dx\).
The general inversion theorem is [HA-LCA-09, Theorem 4.1](the-pontryagin-duality-theorem.md#ha-lca-09-theorem-4-1). Closed-subgroup duality, quotient integration and all three dual measure normalizations are [HA-LCA-10, Theorems 2.1 and 4.1, Proposition 5.1](subgroups-quotients-and-annihilators.md#ha-lca-10-theorem-2-1).

Free sources used for this lesson are David Applebaum, [*Probabilistic Trace and Poisson Summation Formulae on Locally Compact Abelian Groups*, §2 and §5.1](https://arxiv.org/pdf/1602.01252v2), version 4 February 2016, together with his [free author corrigendum](https://eprints.whiterose.ac.uk/id/eprint/106772/12/ProbTracecorrigendum1.pdf); Thomas Fidler and Otmar Scherzer, [*An Introduction to Signal and Image Processing*, Theorem 2.2](https://csc.univie.ac.at/files/SIP_lecture_notes_SS2012.pdf), 14 June 2012; and Keith Conrad, [*The Character Group of \(\mathbb Q\)*, §§2–4](https://kconrad.math.uconn.edu/blurbs/gradnumthy/characterQ.pdf). Quotient integration derives from the preceding lesson's reconstruction of D. H. Fremlin, [*Measure Theory*, §§443P–Q](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt443.tex). Every result used from these sources is proved here or in the linked earlier lessons.

Written by GPT-6 Astra (OpenAI), Ultra, October 2026. Original text: public domain (CC0). Fremlin's copyright 2001 and original notices are retained in the unchanged volume 4 source package. The other works are linked, not reproduced.

## 1. Inversion on a quotient

Let \(H\) be a closed subgroup of \(G\), put \(Q=G/H\), and write \(q:G\to Q\). Fix Haar measures \(dx,dh,dz\) so that
\[
 \int_G f(x)\,dx=\int_Q\int_H f(x+h)\,dh\,dz,\qquad z=q(x),
 \tag{1}
\]
on \(C_c(G)\). Put \(A=H^\perp\subseteq\widehat G\), identified with \(\widehat Q\). On \(A\) use the Haar measure \(da\) dual to \(dz\), not an independently selected normalization.

<a id="ha-lca-11-lemma-1-0"></a>
**Lemma 1.0 — Null sets under the quotient map.** If \(N\) is Haar-null in the full completed domain of \(Q\), then \(q^{-1}(N)\) is Haar-null in the full domain of \(G\).

**Proof.** First let \(U\subseteq G\) be relatively compact and open. Its compact image \(q(\overline U)\) is contained in an open sigma-compact subgroup \(J\) of \(Q\): adjoining a compact identity neighbourhood and taking finite sums and differences gives such a subgroup, by [the general Haar reading, Lemma 1.1](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-1-1). On \(J\), the full Haar domain is the completion of the sigma-compact Borel Haar measure. Thus \(N\cap J\) is contained in a Borel null set \(N_0\subseteq J\), which is also Borel in \(Q\).

Apply HA-LCA-10, Theorem 4.1, to the Borel function
\(1_U(x)1_{N_0}(q(x))\). It has finite integral and is zero outside a relatively compact set, so its representative satisfies the theorem's condition. Its coset integral is
\[
 1_{N_0}(z)\,dh\{h:x+h\in U\}.
\]
The second factor is finite for every coset, since its section is contained in a compact subset of \(H\). Consequently the integral over \(Q\) is zero. Hence \(U\cap q^{-1}(N)\), a subset of a Haar-null Borel set, is measurable and null.

Choose an open sigma-compact subgroup of \(G\). Each of its cosets has a countable cover by relatively compact open sets, so its intersection with \(q^{-1}(N)\) is null by the preceding paragraph. The full Haar domain and measure are the completed sum over these open cosets, as proved in [the general Haar reading, Theorem 3.1](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-theorem-3-1). All component measures are zero; their sum is zero, even if there are uncountably many components. \(\square\)

<a id="ha-lca-11-theorem-1-1"></a>
**Theorem 1.1 — Poisson summation for a closed subgroup.** Let \(f\in L^1(G)\), and let
\(F=P_1f\in L^1(Q)\) be the averaging contraction of HA-LCA-10, Theorem 4.1. Then, at every \(a\in A\),
\[
 \widehat F(a)=\widehat f(a).
 \tag{2}
\]
If \(\widehat f|_A\in L^1(A,da)\), then \(F\) has the continuous representative
\[
 F^\circ(q(x))=\int_A\widehat f(a)a(x)\,da.
 \tag{3}
\]
For a Borel representative \(f_0\) zero outside an open sigma-compact subgroup, the formula
\[
 \int_H f_0(x+h)\,dh
       =\int_A\widehat f(a)a(x)\,da
 \tag{4}
\]
holds for almost every coset and for almost every \(x\in G\). Every \(L^1\) class has such an \(f_0\). If \(G\) is sigma-compact, every completed-measurable representative is permitted. If the actual coset integrals exist absolutely everywhere and give a continuous function on \(Q\), equality holds everywhere for that function. In particular this last conclusion applies to \(f\in C_c(G)\) whenever the transform restriction is integrable.

**Proof.** Choose \(f_j\in C_c(G)\) with \(\|f_j-f\|_1\to0\), using [the general Haar reading, Lemma 5.1](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-5-1). Averaging is a contraction, so \(Pf_j\to F\) in \(L^1(Q)\). The integral definition gives the uniform bound
\(\|\widehat u\|_\infty\le\|u\|_1\) on each group. Thus \(\widehat{Pf_j}\to\widehat F\) uniformly, and \(\widehat f_j|_A\to\widehat f|_A\) uniformly. The \(C_c\) identity
\(\widehat{Pf_j}=\widehat f_j|_A\) is [HA-LCA-10, Lemma 5.0](subgroups-quotients-and-annihilators.md#ha-lca-10-lemma-5-0). Passing to the limit proves (2) at every point.

Under the extra integrability hypothesis, general inversion on the LCA group \(Q\), HA-LCA-09, Theorem 4.1, gives exactly (3), continuous and equal to \(F\) almost everywhere. The character \(a\) kills \(H\), so the integral depends only on \(q(x)\). The representative assertions and the almost-everywhere existence of the absolute coset integrals are precisely HA-LCA-10, Theorem 4.1. Combine its exceptional quotient null set with the inversion exceptional set and apply Lemma 1.0 to obtain the assertion on \(G\).

If the actual average is continuous, it and \(F^\circ\) are two continuous representatives of the same \(L^1(Q)\) class. Their difference vanishes everywhere: a nonzero continuous value would persist on an open set, which has positive Haar measure. For \(C_c(G)\), continuity and compact support of the average are HA-LCA-10, Lemma 3.1.

For later use, every continuous integrable function on \(G\) also satisfies the required support condition. Indeed, fix an open sigma-compact subgroup \(J\). A coset on which \(f\) is nonzero has strictly positive integral of \(|f|\), by continuity and full support. There can be only countably many such cosets: those with mass greater than \(1/n\) are finite for each \(n\). Adjoining one representative from each to \(J\) generates an open sigma-compact subgroup containing the nonzero set of \(f\). Thus the continuous functions used below are legitimate representatives. \(\square\)

The representative condition is essential on arbitrary groups. [HA-LCA-10, Example 4.0](subgroups-quotients-and-annihilators.md#ha-lca-10-example-4-0) proves that a Borel representative of zero on \(\mathbb R_d\times\mathbb R\) can have every coset integral equal to one. Equation (2), being an identity on \(L^1\) classes, has no such ambiguity.

<a id="ha-lca-11-proposition-1-2"></a>
**Proposition 1.2 — Convolution tests on a lattice.** Let \(L\le G\) be discrete and cocompact. Give \(L\) counting measure and let \(c=dz(G/L)\) for the quotient measure in (1). Then \(A=L^\perp\) is discrete with \(da=c^{-1}\) times counting measure. For \(u,v\in C_c(G)\) and \(f=u*\widetilde v\),
\[
 \sum_{\ell\in L}f(x+\ell)
 =\frac1c\sum_{a\in A}\widehat u(a)\overline{\widehat v(a)}a(x)
 \quad(x\in G).
 \tag{5}
\]
The left sum is finite at each point; the right sum is absolutely and uniformly convergent. The conclusion extends to every finite linear combination of these convolutions.

**Proof.** The discrete subgroup is closed by [HA-LCA-09, Lemma 1.2](the-pontryagin-duality-theorem.md#ha-lca-09-lemma-1-2). Subgroup duality identifies \(A\) with the dual of the compact quotient. Compact-discrete duality and [HA-LCA-07, Proposition 3.3](the-fourier-inversion-theorem-and-the-dual-haar-measure.md#ha-lca-07-proposition-3-3) give discreteness and point mass \(1/c\).

The averages \(Pu,Pv\) are continuous on the compact quotient, hence in \(L^2(Q)\). By (2) and [HA-LCA-08, Theorem 1.1](the-plancherel-theorem.md#ha-lca-08-theorem-1-1),
\[
 \frac1c\sum_{a\in A}|\widehat u(a)|^2=\|Pu\|_2^2,\qquad
 \frac1c\sum_{a\in A}|\widehat v(a)|^2=\|Pv\|_2^2.
\]
Cauchy–Schwarz, first for finite subsets and then taking their supremum, gives
\[
 \frac1c\sum_{a\in A}|\widehat u(a)\overline{\widehat v(a)}|
 \le\|Pu\|_2\|Pv\|_2<\infty.
 \tag{6}
\]
An absolutely summable family has countable support: for each \(n\), only finitely many terms exceed \(1/n\) in absolute value. Its finite-subset tails control the sup norm of the character series, proving absolute uniform convergence.

The function \(f\) is in \(C_c(G)\), supported in \(\operatorname{supp}u-\operatorname{supp}v\), and its transform is the product in (5), by [HA-LCA-03, Theorem 3.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-theorem-3-1). Apply Theorem 1.1 and (6). The intersection of \(L\) with any compact set is finite: it is a closed compact discrete space, whose singleton cover has a finite subcover. This proves the left-side finiteness. Finite linear combinations preserve all conclusions. \(\square\)

## 2. Integer periods and Euclidean lattices

<a id="ha-lca-11-lemma-2-0"></a>
**Lemma 2.0 — Decay and lattice sums.** For \(d\ge1\) and \(s>d\), \((1+\|x\|)^{-s}\) is integrable on \(\mathbb R^d\). If \(M\) is invertible and \(B\subset\mathbb R^d\) is bounded, then
\[
 \sum_{k\in\mathbb Z^d}\sup_{x\in B}(1+\|x+Mk\|)^{-s}<\infty.
 \tag{7}
\]

**Proof.** Split the complement of the unit ball into the regions
\(2^j\le\|x\|<2^{j+1}\), \(j\ge0\). The volume of each region is at most that of its enclosing cube, \((2^{j+2})^d\); the integrand is at most \(2^{-js}\). The resulting series is a constant times \(\sum_j2^{-j(s-d)}\), which converges by the finite geometric sum formula. The unit ball has finite volume and bounded integrand.

There is \(b>0\) with \(\|Mk\|\ge b\|k\|\): each coordinate of \(M^{-1}y\) is a finite linear combination of the coordinates of \(y\), giving \(\|M^{-1}y\|\le b^{-1}\|y\|\) by Cauchy–Schwarz. If \(\|x\|\le R\), then
\(\|x+Mk\|\ge b\|k\|-R\ge b\|k\|/2\) once \(\|k\|\ge2R/b\).
There are at most \((2^{j+2}+1)^d\) integer points in the shell \(2^j\le\|k\|<2^{j+1}\), by enclosing it in a cube and counting coordinate choices. The same geometric series bounds the shell sums, uniformly over \(x\in B\). The finitely many remaining terms are at most one each. This proves (7). \(\square\)

<a id="ha-lca-11-corollary-2-1"></a>
**Corollary 2.1 — Classical Poisson summation.** Suppose \(f\in L^1(\mathbb R)\cap C(\mathbb R)\) and
\[
 \sum_{n\in\mathbb Z}\sup_{0\le x\le1}|f(x+n)|<\infty,
 \qquad
 \sum_{n\in\mathbb Z}|\widehat f(n)|<\infty.
 \tag{8}
\]
Then, for every real \(x\),
\[
 \sum_{n\in\mathbb Z}f(x+n)
       =\sum_{n\in\mathbb Z}\widehat f(n)E(nx).
 \tag{9}
\]
The first series converges absolutely and uniformly on each compact interval. The second converges absolutely and uniformly on \(\mathbb R\).

**Proof.** The tails of the first series on \([0,1]\) are bounded by the corresponding tails of the first nonnegative sum in (8). Thus it is uniformly convergent and its sum is continuous there. A compact interval is covered by finitely many integer translates of \([0,1]\); shifting the summation index proves the same assertion on that interval. Absolute convergence permits reindexing, so the sum is one-periodic and descends to a continuous function on \(\mathbb R/\mathbb Z\).

For Lebesgue measure on \(\mathbb R\) and counting measure on \(\mathbb Z\), the quotient has mass one and its dual \(\mathbb Z\) has counting measure, by [HA-LCA-10, Example 6.2](subgroups-quotients-and-annihilators.md#ha-lca-10-example-6-2). The second condition in (8) is precisely the transform-restriction hypothesis of Theorem 1.1. That theorem gives (9) everywhere. The sup norm of each dual-series term is \(|\widehat f(n)|\); summable tails give the last convergence assertion. \(\square\)

<a id="ha-lca-11-corollary-2-2"></a>
**Corollary 2.2 — Poisson summation on a Euclidean lattice.** Let \(\Lambda=M\mathbb Z^d\), where \(M\) is invertible, put \(v=|\det M|\), and let \(\Lambda^*=M^{-T}\mathbb Z^d\). Suppose \(f\) is continuous and, for some \(C,\delta>0\),
\[
 |f(x)|+|\widehat f(x)|\le C(1+\|x\|)^{-d-\delta}.
 \tag{10}
\]
Then, for every \(x\in\mathbb R^d\),
\[
 \sum_{\lambda\in\Lambda}f(x+\lambda)
 =\frac1v\sum_{\xi\in\Lambda^*}\widehat f(\xi)E(x\cdot\xi).
 \tag{11}
\]
The first series converges absolutely and uniformly on compact sets, and the second absolutely and uniformly on all of \(\mathbb R^d\).

**Proof.** Lemma 2.0 makes \(f\) integrable and the first series locally uniformly absolutely convergent. It therefore defines a continuous \(\Lambda\)-periodic function. The same lemma with \(M^{-T}\) makes the transform values summable on \(\Lambda^*\).

HA-LCA-10, Example 6.2, proves both the annihilator formula \(\Lambda^\perp=\Lambda^*\) and the quotient mass \(v\), when \(dx\) is self-dual Lebesgue measure and the lattice has counting measure. The quotient is compact: the image of the compact parallelepiped \(M[0,1]^d\) covers it. Thus its dual measure is \(v^{-1}\) times counting measure, by HA-LCA-07, Proposition 3.3. Substitution into Theorem 1.1 gives (11) and the stated convergence. \(\square\)

<a id="ha-lca-11-example-2-3"></a>
**Example 2.3 — Point values require a hypothesis.** The decay bound (10), without continuity of \(f\), does not imply (11) at every point.

**Proof.** On \(\mathbb R^d\), take \(f=1_{\{0\}}\). Singletons have Lebesgue measure zero: enclose the origin in cubes of arbitrarily small positive volume. Hence \(\widehat f=0\), and (10) holds with \(C=1\) for any \(\delta>0\). At \(x=0\), the left side of (11) is one, while the right side is zero. This counterexample also explains why an \(L^1\) class alone cannot specify values on a lattice. \(\square\)

<a id="ha-lca-11-example-2-4"></a>
**Example 2.4 — Square and hexagonal lattices.** The square lattice \(\mathbb Z^2\) is self-dual with covolume one. For the hexagonal lattice generated by \((1,0)\) and \((1/2,\sqrt3/2)\),
\[
 M=\begin{pmatrix}1&1/2\\0&\sqrt3/2\end{pmatrix},
 \quad
 M^{-T}=\begin{pmatrix}1&0\\-1/\sqrt3&2/\sqrt3\end{pmatrix},
 \quad v=\frac{\sqrt3}{2}.
 \tag{12}
\]
Thus the coefficient in its Poisson formula is \(2/\sqrt3\).

**Proof.** The identity matrix gives the square assertions by HA-LCA-10, Example 6.2. For (12), multiplication verifies \(M^TM^{-T}=I\); the two-by-two determinant is \(\sqrt3/2\). A frequency \((\xi_1,\xi_2)\) annihilates the displayed generators exactly when
\(\xi_1\in\mathbb Z\) and \((\xi_1+\sqrt3\,\xi_2)/2\in\mathbb Z\).
Writing these two integers as \(m,n\) gives
\((\xi_1,\xi_2)=(m,(2n-m)/\sqrt3)=M^{-T}(m,n)\).
This checks the dual basis and the constant directly. Corollary 2.2 applies to any \(f\) satisfying its hypotheses. \(\square\)

## 3. Theta and the circle heat kernel

<a id="ha-lca-11-example-3-1"></a>
**Example 3.1 — The theta transformation.** For \(t>0\), define
\(\theta(t)=\sum_{n\in\mathbb Z}e^{-\pi t n^2}\). Then
\[
 \theta(1/t)=\sqrt t\,\theta(t).
 \tag{13}
\]

**Proof.** The Gaussian calculation proved in [HA-LCA-03, Example 5.2](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-example-5-2) is
\[
 \widehat{\,e^{-\pi t x^2}\,}(\xi)
        =t^{-1/2}e^{-\pi \xi^2/t}.
 \tag{14}
\]
Both functions decay faster than any prescribed inverse power. Indeed, the exponential series gives \(e^u\ge u^N/N!\) for \(u>0\); use a sufficiently large \(N\), and use boundedness on \([-1,1]\). The periodization and dual sums therefore converge as in Lemma 2.0. Corollary 2.1 at \(x=0\) gives
\(\theta(t)=t^{-1/2}\theta(1/t)\), which is (13). Applying the product Gaussian transform, [HA-LCA-07, Proposition 3.2](the-fourier-inversion-theorem-and-the-dual-haar-measure.md#ha-lca-07-proposition-3-2), proves the corresponding identity on \(\mathbb Z^d\), and Corollary 2.2 supplies the covolume factor for any full lattice. \(\square\)

<a id="ha-lca-11-example-3-2"></a>
**Example 3.2 — The heat kernel of \(\mathbb R/\mathbb Z\).** For \(t>0\),
\[
 K_t(x)=\sum_{k\in\mathbb Z}\frac{e^{-(x+k)^2/(4t)}}{\sqrt{4\pi t}}
       =\sum_{n\in\mathbb Z}e^{-4\pi^2n^2t}E(nx).
 \tag{15}
\]
It is positive, has integral one over a period, satisfies
\(\partial_tK_t=\partial_x^2K_t\) and \(K_s*K_t=K_{s+t}\), and for every continuous one-periodic \(F\),
\[
 \|K_t*F-F\|_\infty\longrightarrow0\quad(t\downarrow0).
 \tag{16}
\]

**Proof.** Apply (14) with parameter \(1/(4\pi t)\), including the prefactor in (15). Its transform is \(e^{-4\pi^2t\xi^2}\). Corollary 2.1 proves (15). The positive Gaussian summands make \(K_t>0\). Monotone convergence and the tiling of the line by intervals of length one give
\(\int_0^1K_t(x)\,dx=\int_\mathbb R(4\pi t)^{-1/2}e^{-x^2/(4t)}\,dx=1\).

On each region \(t\ge\varepsilon>0\), multiplying the Fourier terms by any fixed power of \(n\) still gives a uniformly summable family. To see this, absorb that power into \(e^{-2\pi^2\varepsilon n^2}\) using the exponential-series estimate in Example 3.1; the remaining Gaussian terms are summable. Thus the series of every fixed \(x\)-derivative and \(t\)-derivative converge uniformly there. The rule permitting these differentiations follows from the fundamental theorem of calculus already proved in [the real-variable reading, Lemmas 1.1–1.3](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-lemma-1-1): integrate the uniformly convergent derivative series on a compact interval, pass the limit through its finite integral, and recover the original uniformly convergent series at one endpoint. Repeat for each derivative. Both \(\partial_t\) and \(\partial_x^2\) multiply the \(n\)-th term by \(-4\pi^2n^2\), proving the equation.

The Fourier coefficients of \(K_s*K_t\) are the products of those of \(K_s,K_t\), hence those of \(K_{s+t}\). The convolution identity and uniqueness are HA-LCA-03, Theorem 3.1, and [HA-LCA-09, Corollary 4.2](the-pontryagin-duality-theorem.md#ha-lca-09-corollary-4-2). All these functions are continuous, so the equality is everywhere.

Finally let \(0<\eta<1/2\). On the circle, the mass of \(K_t\) outside the \(\eta\)-neighbourhood of zero is at most the real Gaussian mass over \(|y|\ge\eta\), since lifting that circle set to the line yields a subset of \(\{|y|\ge\eta\}\). This mass is at most
\[
 e^{-\eta^2/(8t)}
 \int_\mathbb R\frac{e^{-y^2/(8t)}}{\sqrt{4\pi t}}\,dy
       =\sqrt2\,e^{-\eta^2/(8t)}\longrightarrow0.
 \tag{17}
\]
Uniform translation continuity of continuous functions on the compact circle is [the general Haar reading, Lemma 1.1](../prerequisites/src/nonabelian-haar-integration.md#ha-lca-pre-nonabelian-haar-lemma-1-1). Split the convolution difference into the \(\eta\)-neighbourhood, where \(|F(x-y)-F(x)|\) is uniformly small, and its complement, bounded by \(2\|F\|_\infty\) times (17). This proves (16). For \(t>0\), differentiation under the compact convolution integral is justified by the derivative bounds above, so \(K_t*F\) solves the heat equation with this initial limit. \(\square\)

## 4. A rational series, finite groups and rational adèles

<a id="ha-lca-11-example-4-0"></a>
**Example 4.0 — Summing a rational series.** For \(a>0\),
\[
 \sum_{n\in\mathbb Z}\frac1{n^2+a^2}
       =\frac{\pi}{a}\coth(\pi a),\qquad
 \coth u=\frac{e^u+e^{-u}}{e^u-e^{-u}}\quad(u>0).
 \tag{18}
\]

**Proof.** Let \(f(x)=e^{-2\pi a|x|}\). Its transform, proved by integrating the two exponential half-lines in [HA-LCA-03, Example 5.2](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-example-5-2), is
\[
 \widehat f(\xi)=\frac{a}{\pi(a^2+\xi^2)}.
 \tag{19}
\]
The periodization condition in (8) follows from
\(|x+n|\ge|n|-1\) on \(0\le x\le1\) and a convergent geometric series. The transform values are summable, since for \(|n|\ge1\) they are at most \(a/(\pi n^2)\), and dyadic shells give \(\sum_{n\ge1}n^{-2}<\infty\) as in Lemma 2.0. Formula (9) at zero gives
\[
 \frac a\pi\sum_{n\in\mathbb Z}\frac1{n^2+a^2}
 =1+2\sum_{n=1}^\infty e^{-2\pi an}
 =\frac{1+e^{-2\pi a}}{1-e^{-2\pi a}}
 =\coth(\pi a).
\]
This proves (18). In particular the Fourier convention in (19) has the factor \(2\pi\) in the original exponential; replacing it by a different convention changes the calculation. \(\square\)

<a id="ha-lca-11-example-4-1"></a>
**Example 4.1 — Finite groups.** For a finite abelian group \(G\), a subgroup \(H\), and counting measures on both, the quotient has counting measure and
\[
 \sum_{h\in H}f(x+h)
 =\frac{|H|}{|G|}\sum_{a\in H^\perp}\widehat f(a)a(x),
 \qquad
 \widehat f(a)=\sum_{y\in G}f(y)\overline{a(y)}.
 \tag{20}
\]

**Proof.** The cosets partition \(G\), so counting measure satisfies (1), with quotient mass \(|G|/|H|\). The dual quotient measure is therefore \(|H|/|G|\) times counting measure, giving (20) from Theorem 1.1. There are no convergence questions because all sets are finite.

One can also check the identity directly by [HA-LCA-01, Theorem 3.1](fourier-analysis-on-finite-abelian-groups.md#ha-lca-01-theorem-3-1). That theorem gives \(|H^\perp|=|G|/|H|\) and says the sum of its characters at \(x-y\) is \(|H^\perp|\) if \(x-y\in H\), zero otherwise. Insert the finite definition of \(\widehat f\) in the right side of (20) and interchange two finite sums. The coefficient of \(f(y)\) is exactly the indicator of \(x-y\in H\). This recovers the finite Poisson formula with the present counting convention. \(\square\)

To give an actual adelic instance of Theorem 1.1, we now prove its needed group, measure and test-function facts. Only the rational field is considered. The \(p\)-adic fields, rings, characters and their self-dual Haar measures are already constructed in [HA-LCA-10, Example 6.4](subgroups-quotients-and-annihilators.md#ha-lca-10-example-6-4). Write
\(\psi_p(x)=E(\{x\}_p)\) for the character with kernel \(\mathbb Z_p\).

<a id="ha-lca-11-lemma-4-2"></a>
**Lemma 4.2 — The rational adelic lattice.** Put
\[
 K=\prod_p\mathbb Z_p,\qquad
 \mathbb A_f=\{(x_p)_p:x_p\in\mathbb Q_p,\ x_p\in\mathbb Z_p
                         \text{ for all but finitely many }p\},
 \qquad
 \mathbb A=\mathbb R\times\mathbb A_f.
 \tag{21}
\]
Give \(\mathbb A_f\) the restricted-product topology: an identity-neighbourhood basis consists of
\(\prod_{p\in S}U_p\times\prod_{p\notin S}\mathbb Z_p\), with \(S\) finite and \(U_p\) identity neighbourhoods in \(\mathbb Q_p\). These are LCA groups, \(\mathbb A\) is sigma-compact, and the diagonal copy of \(\mathbb Q\) is discrete and cocompact. For Haar measure
\[
 dx=dx_\infty\,du,\qquad du(K)=1,
 \tag{22}
\]
and counting measure on \(\mathbb Q\), the quotient \(\mathbb A/\mathbb Q\) has mass one. The set
\[
 \mathcal F=[0,1)\times K
 \tag{23}
\]
contains exactly one representative of every rational coset.

**Proof.** The restricted tuples form a group under coordinatewise addition, since the union of two finite sets of nonintegral coordinates is finite. The displayed neighbourhoods give a Hausdorff group topology: choose smaller coordinate neighbourhoods for addition and inversion at the finitely many designated coordinates; elsewhere \(\mathbb Z_p\) is already a subgroup. Any two different tuples are separated in a coordinate where they differ. This topology restricts to the product topology on \(K\).

The group \(K\) is compact by [the Banach reading, Lemma 4.1](../prerequisites/src/banach-spectrum.md#ha-lca-pre-banach-lemma-4-1) and compactness of every \(\mathbb Z_p\). It is open in \(\mathbb A_f\), so \(\mathbb A_f\) is locally compact. For every positive integer \(D\), multiplication by \(D\) is a homeomorphism of \(\mathbb A_f\): it and its inverse act continuously in each coordinate and alter the integrality condition at only the finitely many primes dividing \(D\). Therefore \(D^{-1}K\) is compact and open.

Every tuple belongs to some \(D^{-1}K\): choose \(D\) with sufficiently large powers of the finitely many primes at which the tuple is nonintegral. Moreover the sets \(n!^{-1}K\) are increasing and cover \(\mathbb A_f\), since every \(D\) divides some factorial. Thus \(\mathbb A_f\), and hence its product with \(\mathbb R\), is sigma-compact. Every compact subset of \(\mathbb A_f\) is contained in one \(D^{-1}K\), by a finite subcover. The sets \(DK\), \(D\ge1\), form an identity-neighbourhood basis: a large enough power at each of the finitely many specified primes fits inside the prescribed \(U_p\).

We use the elementary rational fact
\[
 \mathbb Q\cap\bigcap_p\mathbb Z_p=\mathbb Z.
 \tag{24}
\]
Here intersections mean membership under the embeddings of \(\mathbb Q\) in the local fields. To prove it, write a rational as \(a/b\) with coprime integers and \(b>0\). If \(b>1\), it has a prime divisor; removing prime factors repeatedly terminates because the remaining positive integer decreases. A prime dividing \(b\) cannot divide \(a\), by Bézout's identity from HA-LCA-01, Lemma 4.2. The valuation at that prime is negative, contradicting membership in its \(\mathbb Z_p\). The reverse inclusion is immediate. This argument also shows that each rational is integral at all but finitely many primes, so the diagonal embedding lies in \(\mathbb A\).

The neighbourhood \((-1/2,1/2)\times K\) meets the diagonal rationals only at zero by (24); hence they form a discrete subgroup. This subgroup is closed by HA-LCA-09, Lemma 1.2.

For an arbitrary \(x\in\mathbb A\), form the finite rational sum \(r=\sum_p\{x_p\}_p\). For each prime \(p\), the summand \(\{x_p\}_p\) removes the nonintegral part of \(x_p\), whereas every other summand has denominator a power of a different prime and is therefore in \(\mathbb Z_p\). Thus \(x_p-r\in\mathbb Z_p\) for all \(p\). Choose the integer \(m\) with \(0\le x_\infty-r-m<1\). Then \(x-(r+m)\in\mathcal F\). If two points of \(\mathcal F\) differ by a diagonal rational, its finite coordinates put it in \(\mathbb Z\) by (24), and its real coordinate has absolute value less than one. It is zero. This proves the assertion about representatives, and also the disjoint Borel tiling
\[
 \mathbb A=\bigsqcup_{q\in\mathbb Q}(q+\mathcal F).
 \tag{25}
\]
The compact set \([0,1]\times K\) maps onto \(\mathbb A/\mathbb Q\), proving cocompactness.

Normalize Haar measure on \(\mathbb A_f\) by \(du(K)=1\); this is possible since \(K\) is nonempty, open and compact. Product Haar measure with Lebesgue measure is (22), by [HA-LCA-07, Lemma 3.0](the-fourier-inversion-theorem-and-the-dual-haar-measure.md#ha-lca-07-lemma-3-0). The set \(\mathcal F\) has mass one. Its finite restricted measure is Radon, and so is its pushforward \(\rho\) to the quotient, by [HA-LCA-03, Lemma 4.1](the-dual-group-as-the-gelfand-spectrum-of-l1.md#ha-lca-03-lemma-4-1) and [the product reading, Proposition 3.1](../prerequisites/src/finite-radon-products.md#ha-lca-pre-product-proposition-3-1). For \(f\in C_c(\mathbb A)\), the countable tiling and translation invariance give
\[
 \int_\mathbb A f(x)\,dx
 =\int_\mathcal F\sum_{q\in\mathbb Q}f(x+q)\,dx
 =\int_{\mathbb A/\mathbb Q}Pf\,d\rho.
 \tag{26}
\]
Absolute integrability follows by first doing the calculation for \(|f|\), using monotone convergence on the countable tiling. The quotient measure of Weil's formula has the same integrals in (26); the surjectivity of \(P:C_c(\mathbb A)\to C_c(\mathbb A/\mathbb Q)\) identifies it with \(\rho\). Its mass is one. \(\square\)

<a id="ha-lca-11-lemma-4-3"></a>
**Lemma 4.3 — Adelic self-duality and the rational annihilator.** The pairing
\[
 \langle x,y\rangle_{\mathbb A}
 =E(x_\infty y_\infty)\prod_p\overline{\psi_p(x_p y_p)}
 \tag{27}
\]
identifies \(\mathbb A\) topologically with its dual. The Haar measure (22) is self-dual for this pairing, and
\[
 \mathbb Q^\perp=\mathbb Q
 \quad\text{inside }\mathbb A.
 \tag{28}
\]

**Proof.** For two restricted tuples, all but finitely many local products are integral; hence the product in (27) is finite. First consider its finite-place part
\(\langle u,v\rangle_f=\prod_p\overline{\psi_p(u_pv_p)}\).
For fixed \(v\in D^{-1}K\), it is trivial when \(u\in DK\), so it is a continuous character. If \(v\ne0\), test a tuple supported only at a coordinate where \(v_p\ne0\), and use the nondegeneracy proved in HA-LCA-10, Example 6.4. Thus the parameter map into \(\widehat{\mathbb A_f}\) is injective.

Let \(\chi\) be any continuous character of \(\mathbb A_f\). Its restriction to the \(p\)-th coordinate copy of \(\mathbb Q_p\) has the form
\(u_p\mapsto\overline{\psi_p(u_pv_p)}\) for a unique \(v_p\), by that same earlier example (replace its parameter by its negative). Continuity gives some subgroup \(DK\) whose image under \(\chi\) lies in \(\{z:|z-1|<1\}\). The small-arc lemma, [HA-LCA-02, Lemma 1.2](characters-and-the-dual-group.md#ha-lca-02-lemma-1-2), makes that image trivial. For every prime not dividing \(D\), the coordinate copy of \(\mathbb Z_p\) lies in \(DK\), so \(v_p\in\mathbb Z_p\) by the local annihilator formula. Consequently \(v\in\mathbb A_f\).

Tuples with finitely many nonzero coordinates are dense in \(\mathbb A_f\). Given a tuple and a basic neighbourhood of it, match its finitely many designated coordinates and its finitely many nonintegral coordinates; set the other coordinates to zero. The resulting tuple is in that neighbourhood. On these finite tuples, \(\chi\) and the character with parameter \(v\) agree by multiplication of the coordinate characters. Continuity and density prove agreement everywhere. This proves surjectivity.

It also gives the explicit annihilator identities
\[
 (DK)^\perp=D^{-1}K,\qquad (D^{-1}K)^\perp=DK
 \quad(D\ge1).
 \tag{29}
\]
Indeed, testing one coordinate at a time reduces them to
\((p^m\mathbb Z_p)^\perp=p^{-m}\mathbb Z_p\), already proved; integer factors coprime to \(p\) are units. Conversely those coordinate conditions make every local product integral.

For compact-open continuity of the parameter map, a compact set of \(\mathbb A_f\) lies in some \(D^{-1}K\), and all parameters in \(DK\) give characters identically one there. For inverse continuity, the image of \(DK\) is exactly
\[
 \left\{\chi:\sup_{u\in D^{-1}K}|\chi(u)-1|<1\right\}.
 \tag{30}
\]
The equality follows from (29) and the small-arc lemma applied to the image of the entire subgroup \(D^{-1}K\). This is an open set in the dual since \(D^{-1}K\) is compact. The sets \(DK\) form a neighbourhood basis, proving the inverse continuity.

The measure \(du\) is self-dual for this finite-place identification. To see the constant, \(1_K\in C_c(\mathbb A_f)\) is its own autocorrelation, since \(du(K)=1\), so it has positive type. Its Fourier transform is \(1_K\) under the identification: a character integral over \(K\) is one when it is trivial, and otherwise is zero by translating the integral by a point where the character is not one. The annihilator of \(K\) is \(K\). The transported dual measure is \(c\,du\) for some \(c>0\), by Haar uniqueness. The \(B^1\) inversion formula, [HA-LCA-07, Theorem 2.1](the-fourier-inversion-theorem-and-the-dual-haar-measure.md#ha-lca-07-theorem-2-1), at zero gives \(1=c\,du(K)=c\). Thus \(c=1\).

Real self-duality and finite-product duality, proved in HA-LCA-02, Theorem 3.1 and Proposition 4.1, now give precisely the topological identification (27). The product normalization of HA-LCA-07, Lemma 3.0, gives the self-duality of (22).

It remains to compute the rational annihilator, rather than assume it from a number-theory result. For rational \(r\),
\[
 r-\sum_p\{r\}_p\in\mathbb Z.
 \tag{31}
\]
The sum is finite. Its difference from \(r\) belongs to every \(\mathbb Z_p\): the \(p\)-summand removes the fractional part at \(p\), and all other summands are \(p\)-integral. Apply (24). For rational \(r,s\), (31) with \(rs\) gives \(\langle r,s\rangle_{\mathbb A}=1\). This proves \(\mathbb Q\subseteq\mathbb Q^\perp\).

Conversely take \(y\in\mathbb Q^\perp\). Subtract its unique rational translate to put it in \(\mathcal F\), using Lemma 4.2; subtracting a rational preserves the annihilator property. Call the resulting tuple \(z\). Testing against the rational \(1\) in (27) gives \(E(z_\infty)=1\), since each \(z_p\in\mathbb Z_p\). As \(0\le z_\infty<1\), this forces \(z_\infty=0\). Testing against \(1/p^n\) then gives \(\psi_p(z_p/p^n)=1\): all other local factors are one because their denominators are units. Hence \(z_p\in p^n\mathbb Z_p\) for every \(n\ge1\), so \(z_p=0\) by the compatible-residue construction. This holds for every \(p\). Therefore \(z=0\), and \(y\) was rational. This proves (28). \(\square\)

<a id="ha-lca-11-lemma-4-4"></a>
**Lemma 4.4 — A concrete adelic test space.** Let \(\mathcal S(\mathbb R)\) be the space of smooth functions \(g\) for which
\(\sup_x(1+|x|)^m|g^{(j)}(x)|<\infty\) for all nonnegative integers \(m,j\). Let \(\mathcal D(\mathbb A_f)\) be the locally constant compactly supported functions. Both spaces are preserved by their Fourier transforms. The finite linear span
\[
 \mathcal S(\mathbb A)
 =\operatorname{span}\{\,g(x_\infty)v(x_f):
                   g\in\mathcal S(\mathbb R),\
                   v\in\mathcal D(\mathbb A_f)\,\}
 \tag{32}
\]
is preserved by the Fourier transform for (27). For every member \(f\), the rational periodization
\(\sum_{q\in\mathbb Q}f(x+q)\) converges absolutely and uniformly on each compact subset of \(\mathbb A\), and \(\sum_{q\in\mathbb Q}|\widehat f(q)|<\infty\).

**Proof.** First consider the real factor. The decay conditions make every polynomial times every derivative of \(g\) integrable, using Lemma 2.0 in dimension one. Differentiation under the integral, as justified in [the real-variable reading, Lemma 1.4](../prerequisites/src/real-variable-calculations.md#ha-lca-pre-real-lemma-1-4), gives
\[
 \frac{d^j}{d\xi^j}\widehat g(\xi)
   =\int_\mathbb R(-2\pi ix)^j g(x)E(-x\xi)\,dx.
 \tag{33}
\]
The same integrable bounds give continuity of these derivatives by dominated convergence. Repeated integration by parts on finite intervals, followed by their limit to the whole line, gives
\[
 (2\pi i\xi)^N\frac{d^j}{d\xi^j}\widehat g(\xi)
  =\int_\mathbb R
       \frac{d^N}{dx^N}\bigl[(-2\pi ix)^jg(x)\bigr]E(-x\xi)\,dx.
 \tag{34}
\]
All boundary terms vanish by rapid decay, and the integrals are absolutely convergent. Repeated product differentiation expresses the derivative in (34) as a finite sum of polynomial multiples of derivatives of \(g\); this follows by induction from the product rule. Its \(L^1\) norm bounds the right side uniformly in \(\xi\). For \(|\xi|\ge1\), divide by \(|2\pi\xi|^N\); for \(|\xi|\le1\), use (33). Since \(N\) is arbitrary, these are exactly all the Schwartz bounds for \(\widehat g\).

Next let \(v\in\mathcal D(\mathbb A_f)\). Each point of its support has a coset neighbourhood on which \(v\) is constant. Its support is the nonzero set, since local constancy at any zero supplies a zero neighbourhood. Compactness therefore gives a finite cover of the support by such cosets. Choose \(D\) divisible by the finitely many integers defining their compact open subgroups. The subgroup \(DK\) lies in each of them. Refining to \(DK\)-cosets, of which only finitely many meet this compact support, expresses \(v\) as a finite linear combination of indicators \(1_{a+DK}\). These cosets also show global invariance under translation by \(DK\).

The quotient \(K/DK\) has exactly \(D\) elements. Indeed, if \(D=\prod_{p\mid D}p^{m_p}\), its quotient coordinates are the finite rings \(\mathbb Z_p/p^{m_p}\mathbb Z_p\), of sizes \(p^{m_p}\), and all other factors vanish; the coordinate map is onto and has kernel \(DK\). Thus \(du(DK)=1/D\). Character integration over this compact subgroup and (29) give
\[
 \widehat{1_{a+DK}}(y)
  =\frac1D\,\overline{\langle a,y\rangle_f}\,
                1_{D^{-1}K}(y).
 \tag{35}
\]
Every finite-place character is locally constant, since the proof of Lemma 4.3 shows that it kills some \(EK\). Consequently (35) is locally constant and compactly supported. Linearity proves Fourier stability of \(\mathcal D(\mathbb A_f)\).

Each tensor in (32) is continuous and in \(L^1(\mathbb A)\). The absolutely integrable product formula, or the sigma-finite Fubini theorem [in the integration reading, Theorem 4.4](../prerequisites/src/integration-and-l1.md#ha-lca-pre-integral-theorem-4-4), yields
\[
 \widehat{g\otimes v}=\widehat g\otimes\widehat v.
 \tag{36}
\]
Here the product Haar normalization is exactly (22); sigma-compactness was proved in Lemma 4.2. The preceding two stability arguments prove the assertion about (32).

For the convergence assertions, it is enough to treat one tensor. Let \(C\subset\mathbb A\) be compact. Its real projection is bounded, say \(|x_\infty|\le R\), and its finite-place projection is contained in some \(E^{-1}K\). The support of \(v\) is contained in some \(D^{-1}K\). If \(v(x_f+q)\ne0\) for \(x\in C\) and rational \(q\), then
\[
 q\in D^{-1}K+E^{-1}K\subseteq(DE)^{-1}K.
 \]
By (24), these rational numbers are all in \((DE)^{-1}\mathbb Z\). Thus the periodization on \(C\) is bounded termwise by the lattice sum
\[
 \|v\|_\infty
 \sum_{k\in\mathbb Z}\sup_{|t|\le R}|g(t+k/(DE))|,
 \tag{37}
\]
which converges by the Schwartz bound and Lemma 2.0. This proves absolute uniform convergence on \(C\). Each summand is continuous; a compact neighbourhood of any point makes the sum continuous there. Apply the same argument to \(\widehat g\otimes\widehat v\), now at the singleton \(x=0\), using (36) and the two stability assertions. This proves summability of the rational transform values. Finite linear combinations preserve all the properties. \(\square\)

<a id="ha-lca-11-proposition-4-5"></a>
**Proposition 4.5 — Rational adelic Poisson summation.** For \(f\in\mathcal S(\mathbb A)\),
\[
 \sum_{q\in\mathbb Q}f(x+q)
 =\sum_{q\in\mathbb Q}\widehat f(q)\langle x,q\rangle_{\mathbb A}
 \quad(x\in\mathbb A).
 \tag{38}
\]
In particular,
\[
 \sum_{q\in\mathbb Q}f(q)=\sum_{q\in\mathbb Q}\widehat f(q).
 \tag{39}
\]
Both sides converge absolutely; the primal sum is locally uniformly convergent and the dual sum is uniformly convergent on \(\mathbb A\).

**Proof.** Lemma 4.2 supplies a closed discrete rational subgroup and quotient Haar mass one. Lemma 4.3 identifies its annihilator with \(\mathbb Q\) using the precise pairing (27), and fixes the self-dual measure. The measure on that annihilator dual to the quotient is counting measure, by HA-LCA-07, Proposition 3.3. Lemma 4.4 makes the actual periodization continuous, absolutely convergent, and invariant under \(\mathbb Q\) by reindexing; it descends continuously through the quotient map. It also makes the transform restriction integrable for counting measure. Theorem 1.1 therefore gives (38) at every point. Put \(x=0\) to obtain (39). The bounds in Lemma 4.4 give primal local uniform convergence, and the summable coefficients on the right, whose characters have modulus one, give global uniform convergence. No further adelic duality or number-theory theorem is required. \(\square\)

## 5. Exercises with complete solutions

<a id="ha-lca-11-exercise-5-1"></a>
**Exercise 5.1 — A three-digit theta check.** Verify (13) at \(t=2\) from a few terms and bound the omitted tails.

**Solution.** For \(t>0\) and \(N\ge0\), the tail after the terms with \(|n|\le N\) satisfies
\[
 0<2\sum_{n=N+1}^\infty e^{-\pi t n^2}
 \le \frac{2e^{-\pi t(N+1)^2}}
                {1-e^{-\pi t(2N+3)}}.
 \tag{40}
\]
Indeed consecutive squared indices differ by \(2n+1\ge2N+3\) once \(n\ge N+1\); each successive summand is at most \(e^{-\pi t(2N+3)}\) times the preceding one. Sum the resulting geometric majorant.

For \(\theta(2)\), take \(N=1\):
\[
 1+2e^{-2\pi}\approx1.003734885463416.
 \]
The bound (40) is less than \(2.433\times10^{-11}\). For \(\theta(1/2)\), take \(N=3\):
\[
 1+2(e^{-\pi/2}+e^{-2\pi}+e^{-9\pi/2})
       \approx1.419495488059443,
 \]
and its tail bound is again less than \(2.434\times10^{-11}\).
Multiplying the first approximation by \(\sqrt2\) gives
\(1.419495488049368\), with its omitted-tail bound multiplied by \(\sqrt2\). The two error intervals overlap, as required by (13), and both values round to \(1.419\) at three decimal places. The exact bound (40), not the closeness of rounded numbers alone, explains why these few terms suffice. \(\square\)

<a id="ha-lca-11-exercise-5-2"></a>
**Exercise 5.2 — A rational series by periodization.** Derive (18) from Corollary 2.1 and verify its hypotheses.

**Solution.** Set \(f(x)=e^{-2\pi a|x|}\), \(a>0\), whose transform is (19). It is continuous and integrable. On \([0,1]\),
\[
 |f(x+n)|\le e^{2\pi a}e^{-2\pi a|n|}.
 \]
The right side is summable by a two-sided geometric series. For \(|n|\ge1\),
\(|\widehat f(n)|\le a/(\pi n^2)\); the \(n=0\) value is \(1/(\pi a)\), so all transform values are summable. Both conditions in (8) hold.

Poisson summation at zero therefore gives
\[
 \frac a\pi\sum_{n\in\mathbb Z}(a^2+n^2)^{-1}
 =1+\frac{2e^{-2\pi a}}{1-e^{-2\pi a}}
 =\frac{e^{\pi a}+e^{-\pi a}}{e^{\pi a}-e^{-\pi a}}.
 \]
Multiply by \(\pi/a\). Every sum used here is absolutely convergent by the verified bounds, and the denominator is positive since \(a>0\). This proves the formula for the entire stated range of \(a\). \(\square\)

<a id="ha-lca-11-exercise-5-3"></a>
**Exercise 5.3 — Recover the lattice constant.** Prove Corollary 2.2 from Theorem 1.1, and identify the roles of continuity and covolume.

**Solution.** With \(dx\) self-dual Lebesgue measure and counting measure on \(\Lambda=M\mathbb Z^d\), [HA-LCA-10, Example 6.2](subgroups-quotients-and-annihilators.md#ha-lca-10-example-6-2) gives quotient mass \(v=|\det M|\). Its dual group is \(\Lambda^*=M^{-T}\mathbb Z^d\). The Haar measure dual to a compact group's measure of mass \(v\) assigns each dual point mass \(1/v\), by HA-LCA-07, Proposition 3.3. Hence the right integral in (4) is exactly
\(v^{-1}\sum_{\xi\in\Lambda^*}\widehat f(\xi)E(x\cdot\xi)\).

The decay estimate with exponent \(d+\delta>d\) gives \(f\in L^1\), compact-local uniform convergence of its lattice periodization, and summability of the dual values, all by Lemma 2.0. Continuity of \(f\) then makes the actual periodization continuous, so Theorem 1.1 upgrades almost-everywhere equality to equality at every point. This gives every assertion of Corollary 2.2. If continuity is omitted, Example 2.3 shows that the numerical pointwise formula can fail even under arbitrary decay. \(\square\)

<a id="ha-lca-11-exercise-5-4"></a>
**Exercise 5.4 — Sampling a band-limited function.** Suppose \(f\in L^2(\mathbb R)\cap C(\mathbb R)\), and its Plancherel transform is zero almost everywhere off \(I=[-1/2,1/2]\). Prove
\[
 f(x)=\sum_{n\in\mathbb Z}f(n)\operatorname{sinc}(x-n),
 \qquad
 \operatorname{sinc}(y)=
 \begin{cases}
 \sin(\pi y)/(\pi y),&y\ne0,\\
 1,&y=0,
 \end{cases}
 \tag{41}
\]
with convergence in \(L^2(\mathbb R)\) and uniformly on \(\mathbb R\).

**Solution.** Let \(g=\mathcal F_2 f\). Since \(g\) is supported on a set of length one, Cauchy–Schwarz gives
\(\|g\|_1\le\|g\|_2\). Thus \(g\in L^1\cap L^2\). By [HA-LCA-08, Lemma 2.2](the-plancherel-theorem.md#ha-lca-08-lemma-2-2), its inverse integral is the inverse Plancherel transform and is continuous:
\[
 f(x)=\int_I g(\xi)E(x\xi)\,d\xi.
 \tag{42}
\]
Initially this equals \(f\) almost everywhere; both sides are continuous, so Haar full support gives equality everywhere.

The functions \(e_n(\xi)=E(-n\xi)\), \(n\in\mathbb Z\), are a complete orthonormal basis of \(L^2(I)\). This is the circle Fourier basis of [HA-LCA-08, Corollary 4.1](the-plancherel-theorem.md#ha-lca-08-corollary-4-1), with the endpoints identified; changing the values at those two null points does not alter the \(L^2\) space. Its coefficient for \(g\) is
\[
 \langle g,e_n\rangle=\int_I g(\xi)E(n\xi)\,d\xi=f(n).
 \tag{43}
\]
The Hilbert expansion and Parseval theorem, proved in [the Hilbert reading, Theorem 4.2](../prerequisites/src/hilbert-spaces-and-unitary-representations.md#ha-lca-pre-hilbert-theorem-4-2), therefore give
\[
 \sum_{n\in\mathbb Z}|f(n)|^2=\|g\|_2^2=\|f\|_2^2,\qquad
 g=\lim_{F}\sum_{n\in F}f(n)e_n
        \quad\text{in }L^2(I).
 \tag{44}
\]
Here \(F\) runs through finite subsets of \(\mathbb Z\), ordered by inclusion; symmetric partial sums are a particular convergent sequence.

Extend each finite sum by zero off \(I\). Its inverse integral is
\[
 S_F(x)=\sum_{n\in F}f(n)\int_{-1/2}^{1/2}E((x-n)\xi)\,d\xi
       =\sum_{n\in F}f(n)\operatorname{sinc}(x-n).
 \tag{45}
\]
For \(x\ne n\), integrate the exponential and subtract its two endpoint values to obtain the sine quotient; for \(x=n\), the integral is one. The inverse integral agrees with inverse Plancherel on each such finite sum. Unitarity and (44) give
\[
 \|f-S_F\|_2
 =\left\|g-\sum_{n\in F}f(n)e_n\right\|_{L^2(I)}
 =\left(\sum_{n\notin F}|f(n)|^2\right)^{1/2}\longrightarrow0.
 \tag{46}
\]
Moreover (42) and (45), followed by Cauchy–Schwarz on the interval of length one, give the uniform bound
\[
 \sup_{x\in\mathbb R}|f(x)-S_F(x)|
 \le\int_I\left|g-\sum_{n\in F}f(n)e_n\right|\,d\xi
 \le\left(\sum_{n\notin F}|f(n)|^2\right)^{1/2}\longrightarrow0.
 \tag{47}
\]
This proves both required convergences, with an explicit error bound and no pointwise Fourier-series assumption. \(\square\)

## Scope

The closed-subgroup formula holds for arbitrary LCA groups with the exact representative condition required by their full Haar domains. The lattice, Gaussian, heat-kernel, finite, rational-series and sampling assertions have complete proofs. The rational adelic example includes the construction, topology, self-dual measure, rational annihilator and test-function estimates it uses. Number-field generalizations and zeta functional equations are not asserted here.
