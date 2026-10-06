# Matrix coefficients and the Peter–Weyl theorem

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0).*

Fourier series express functions on a circle through its characters. For a noncommutative compact group, a character alone loses information: an irreducible representation may have dimension greater than one. Its individual matrix entries supply the missing functions. The Peter–Weyl theorem says that these entries give both uniform approximation of continuous functions and a complete orthogonal expansion in square-integrable functions.

The prerequisite [Representations of compact groups: unitarity, complete reducibility and finite dimension](RT-CPT-01.md) proves that every unitary representation is a Hilbert sum of finite-dimensional irreducibles. We also use the complex Stone–Weierstrass theorem, recalled precisely below. The proof will pass through smoothing operators before establishing point separation. Thus completeness is proved before it is used to approximate continuous functions. Basic references are [Gruson–Serganova 2018] and the open lectures [Etingof, Lie groups].

## Functions obtained from a representation

Let \(G\) be compact Hausdorff, with normalized Haar measure \(dg\). All Hilbert inner products are linear in the first variable. We impose no separability or metrizability condition.

For a finite-dimensional unitary representation \(\pi\) on \(V_\pi\), a **matrix coefficient** is a function

\[
c_{v,w}(g)=\langle\pi(g)v,w\rangle.
\]

Its coefficient space \(E_\pi\) is the span of these functions. If \((e_1,\ldots,e_d)\) is an orthonormal basis, write

\[
\pi_{ij}(g)=\langle\pi(g)e_j,e_i\rangle,\qquad d=d_\pi.
\tag{1.1}
\]

Changing the basis only forms linear combinations of the same functions. A unitary intertwiner replaces \(v,w\) by their images and leaves the functions unchanged. Thus \(E_\pi\) depends only on the equivalence class of \(\pi\).

Let \(E\) be the span of the coefficient spaces of all irreducibles. It contains coefficients of every finite-dimensional representation, since such a representation is a finite direct sum of irreducibles. Products belong to \(E\): the product \(c_{v,w}^\pi c_{x,y}^\sigma\) is the coefficient of \(v\otimes x,w\otimes y\) in \(\pi\otimes\sigma\), which is again a finite-dimensional unitary representation. Complex conjugation replaces \(\pi\) by its conjugate representation on \(\overline{V_\pi}\). The trivial representation supplies the constants. Consequently, \(E\) is a conjugation-closed algebra of continuous functions.

We use the commuting regular actions

\[
(L_hf)(g)=f(h^{-1}g),\qquad (R_kf)(g)=f(gk).
\tag{1.2}
\]

Matrix multiplication gives

\[
L_h\pi_{ij}=\sum_a\pi(h^{-1})_{ia}\pi_{aj},
\qquad
R_k\pi_{ij}=\sum_b\pi_{ib}\pi(k)_{bj}.
\tag{1.3}
\]

For fixed \(j\), the column space carries \(\bar\pi\) under \(L\), because its transformation matrix is \(\pi(h^{-1})^{\mathsf T}=\overline{\pi(h)}\). For fixed \(i\), the row space carries \(\pi\) under \(R\). On the circle, the coefficient \(g^n\) changes by \(h^{-n}\) on the left and \(k^n\) on the right. This small example fixes the convention throughout.

## Averaging removes all but a scalar

**Theorem 2.1 (Schur orthogonality).** Choose one representative and one orthonormal basis for each irreducible class. For coefficients of irreducibles \(\pi,\sigma\),

\[
\int_G\pi_{ij}(g)\overline{\sigma_{kl}(g)}\,dg
=
\begin{cases}
d_\pi^{-1}\delta_{ik}\delta_{jl},&\pi=\sigma,\\
0,&\pi\not\simeq\sigma.
\end{cases}
\tag{2.2}
\]

**Proof.** For a linear map \(A:V_\sigma\to V_\pi\), define

\[
\mathcal A(A)=\int_G\pi(g)A\sigma(g)^*\,dg.
\]

The integral is an ordinary finite-dimensional integral. Left invariance shows that \(\mathcal A(A)\) intertwines \(\sigma\) and \(\pi\). Schur's lemma makes it zero when the representations are inequivalent. When they are the same representative, it is scalar, and taking traces gives

\[
\mathcal A(A)=\frac{\operatorname{tr}A}{d_\pi}I.
\]

Take \(Ax=\langle x,e_l\rangle e_j\). The \((i,k)\) entry of the integrand is \(\pi_{ij}(g)\overline{\sigma_{kl}(g)}\). For equal representatives, \(\operatorname{tr}A=\delta_{jl}\), giving (2.2). ∎

In particular, \(\dim E_\pi=d_\pi^2\), and the functions \(\sqrt{d_\pi}\pi_{ij}\) are orthonormal. Distinct coefficient spaces are orthogonal in \(L^2(G)\). Also the characters \(\chi_\pi=\sum_i\pi_{ii}\) satisfy \(\langle\chi_\pi,\chi_\sigma\rangle=\delta_{\pi\sigma}\), by summing (2.2). Orthogonality does not yet prove completeness. For that, we must show that no nonzero \(L^2\) function is orthogonal to every coefficient.

## Smoothing produces finite-dimensional spaces

We use two analytic results in the following precise forms. The complex Stone–Weierstrass theorem says that a unital, conjugation-closed subalgebra of \(C(X)\) separating points of a compact Hausdorff space \(X\) is uniformly dense. The compact self-adjoint spectral theorem says that the closed span of an operator's nonzero eigenspaces is the orthogonal complement of its kernel; every nonzero eigenspace is finite-dimensional. Neither result requires separability.

Continuous functions are dense in \(L^2(G)\). To see this, regularity of finite Haar measure gives, for a measurable set \(A\), a compact \(K\subset A\) and an open \(U\supset A\), up to completion by null sets, with \(\mu(U\setminus K)<\varepsilon\). Urysohn's lemma gives \(0\leq f\leq1\), equal to one on \(K\) and zero outside \(U\). Then \(\|f-1_A\|_2^2<\varepsilon\). Approximate simple functions this way, and arbitrary \(L^2\) functions by simple functions.

Both regular actions are strongly continuous. For a continuous function, compactness gives \(\|L_hf-f\|_\infty\to0\) as \(h\to e\), and likewise for \(R\). Approximation by continuous functions and the fact that translations are isometries prove strong continuity on \(L^2(G)\).

For \(\psi\in C(G)\), define

\[
(K_\psi f)(x)=\int_G\psi(xy^{-1})f(y)\,dy.
\tag{3.1}
\]

Cauchy–Schwarz gives \(\|K_\psi f\|_\infty\leq\|\psi\|_2\|f\|_2\). The kernel depends continuously on \(x\), uniformly in \(y\), so its output is continuous. Changing variables \(z=yh\) shows that

\[
K_\psi R_h=R_hK_\psi.
\tag{3.2}
\]

**Lemma 3.3.** \(K_\psi\) is compact. If \(\psi(g^{-1})=\overline{\psi(g)}\), it is self-adjoint.

**Proof.** Finite sums \(\sum_\nu a_\nu(x)b_\nu(y)\) with continuous factors form a unital, conjugation-closed algebra separating points of \(G\times G\). Stone–Weierstrass therefore approximates \(\psi(xy^{-1})\) uniformly by these kernels. Their operators have range in the finite-dimensional span of their \(a_\nu\). A uniform kernel error \(\delta\) gives operator-norm error at most \(\delta\), because the measure has total mass one. Thus \(K_\psi\) is a norm limit of finite-rank operators. The identity \(\psi(xy^{-1})=\overline{\psi(yx^{-1})}\), together with Fubini's theorem, proves self-adjointness. ∎

**Lemma 3.4.** Every nonzero eigenspace of a self-adjoint \(K_\psi\) lies in \(E\).

**Proof.** For \(\lambda\ne0\), let \(N=\ker(K_\psi-\lambda I)\). The compact spectral theorem makes \(N\) finite-dimensional; (3.2) makes it invariant under \(R\). The restriction \(\tau\) of \(R\) is a continuous unitary representation. Every element of \(N\) has a continuous representative since \(f=\lambda^{-1}K_\psi f\). Such a representative is unique: a nonempty open set has positive Haar measure, because its translates cover \(G\) and a finite subcover would otherwise force \(\mu(G)=0\). A continuous function zero almost everywhere is therefore zero everywhere.

Evaluation at \(e\) consequently defines a linear functional \(\ell:N\to\mathbb C\), continuous by finite dimension. For every \(g\),

\[
f(g)=\ell(R_gf)=\ell(\tau(g)f).
\tag{3.5}
\]

Finite-dimensional Riesz representation makes this a matrix coefficient of \(\tau\). Its irreducible decomposition, proved in the preceding lesson, puts this coefficient in \(E\). ∎

The continuity step is essential: point evaluation is not defined on arbitrary \(L^2\) equivalence classes.

Direct the symmetric identity neighborhoods \(U\) by reverse inclusion. Choose a nonnegative continuous function supported in \(U\) and positive at \(e\), using compact Hausdorff regularity and Urysohn's lemma. Add its inverse translate \(a(g^{-1})\) and normalize the integral to obtain a continuous, nonnegative, symmetric \(\psi_U\), supported in \(U\), of integral one. Full support makes the normalizing integral positive. Then

\[
K_{\psi_U}f=\int_G\psi_U(g)L_gf\,dg,\qquad
\|K_{\psi_U}f-f\|_2
\leq\sup_{g\in U}\|L_gf-f\|_2\longrightarrow0.
\tag{3.6}
\]

The Hilbert-space integral exists: the continuous orbit map has compact image, whose closed linear span is separable. This does not assume that the entire Hilbert space is separable. The limit is a net limit.

## Completeness and uniform approximation

**Theorem 4.1 (Peter–Weyl).** For every compact Hausdorff group:

1. The functions \(\sqrt{d_\pi}\pi_{ij}\) form an orthonormal Hilbert basis of \(L^2(G)\).
2. Irreducible matrix coefficients, and finite-dimensional unitary representations, separate points.
3. Their algebra \(E\) is uniformly dense in \(C(G)\).
4. With the actions (1.2),
   \[
   L^2(G)=\widehat{\bigoplus}_{[\pi]\in\widehat G}E_\pi,
   \qquad E_\pi\simeq\bar V_\pi\otimes V_\pi,
   \tag{4.2}
   \]
   carrying \(\bar\pi\) on the left and \(\pi\) on the right. Either regular representation contains every irreducible with multiplicity equal to its dimension.

**Proof.** If \(f\perp E\), Lemma 3.4 makes it orthogonal to every nonzero eigenspace of every \(K_{\psi_U}\). The compact self-adjoint spectral theorem gives \(K_{\psi_U}f=0\). Equation (3.6) then gives \(f=0\). Thus \(E\) is dense in \(L^2(G)\), and Schur orthogonality gives the claimed basis.

If \(x\ne e\) but \(\pi(x)=I\) for every irreducible, (1.3) says that \(R_x\) fixes \(E\) pointwise. Density makes it fix all of \(L^2(G)\). Choose \(f\in C(G)\) with \(f(e)\ne f(x)\). The continuous function \(R_xf-f\), zero almost everywhere, would be zero everywhere, a contradiction at \(e\). Thus some \(\pi(x)\ne I\). Apply this to \(x=g^{-1}h\) to separate any distinct \(g,h\); some matrix entry then separates them.

The algebra \(E\) is already unital and conjugation-closed. Point separation now permits Stone–Weierstrass and proves uniform density. Completeness was proved before point separation was used.

The coefficient basis gives (4.2). Schur orthogonality makes

\[
\bar w\otimes v\longmapsto
\sqrt{d_\pi}\,\langle\pi(\,\cdot\,)v,w\rangle
\tag{4.3}
\]

a unitary map onto \(E_\pi\). Formula (1.3) identifies the actions. Its \(d_\pi\) column spaces are orthogonal copies of \(\bar\pi\) under \(L\), and its \(d_\pi\) row spaces are orthogonal copies of \(\pi\) under \(R\). A given \(\sigma\) thus has left multiplicity \(d_{\bar\sigma}=d_\sigma\), in \(E_{\bar\sigma}\), and right multiplicity \(d_\sigma\), in \(E_\sigma\). ∎

An uncountable Hilbert direct sum has its usual meaning: each vector has at most countably many nonzero coordinates, and finite partial sums converge in norm. The theorem does not assert pointwise convergence of arbitrary Fourier series.

**Corollary 4.4.** \(\widehat G\) is countable if and only if \(L^2(G)\) is separable.

**Proof.** A countable union of finite coefficient bases gives a countable complete orthonormal set. Conversely, every orthonormal set in a separable Hilbert space is countable: disjoint balls of radius less than \(\sqrt2/2\) around its elements contain distinct points of a countable dense set. Choose one unit coefficient from each class. ∎

## A faithful representation detects the Lie structure

A group has **no small subgroups** if some identity neighborhood contains no subgroup except \(\{e\}\).

**Lemma 5.1.** Every finite-dimensional real Lie group has no small subgroups.

**Proof.** In positive dimension, choose a norm on its Lie algebra and \(r>0\) so that \(\exp\) is injective on \(B_r\) and is a homeomorphism there onto an identity neighborhood. Set \(U=\exp(B_{r/3})\). If a subgroup inside \(U\) contained \(h=\exp X\ne e\), choose the least positive \(n\) with \(n\|X\|\geq r/3\). Then

\[
r/3\leq n\|X\|<2r/3<r,\qquad h^n=\exp(nX).
\]

Because \(h^n\in U\), it also equals \(\exp Y\) for \(\|Y\|<r/3\), contradicting injectivity on \(B_r\). In dimension zero, \(\{e\}\) is itself open. ∎

Here we import that the Lie exponential is a local diffeomorphism and \((\exp X)^n=\exp(nX)\). We also import the closed subgroup theorem: a closed subgroup of a finite-dimensional real Lie group is a Lie subgroup. Its precise statement is [Etingof, Theorem 2.16].

**Theorem 5.2.** A compact Hausdorff group is a finite-dimensional real Lie group if and only if it admits a faithful continuous finite-dimensional representation. Every compact group with no small subgroups has such a representation, which can be chosen unitary.

**Proof.** Choose \(U\) containing no nontrivial subgroup. For each \(x\notin U\), point separation gives an irreducible \(\pi_x\) with \(\pi_x(x)\ne I\). The open complements of these kernels cover the compact set \(G\setminus U\). A finite subcover gives \(\pi_1,\ldots,\pi_m\), and

\[
\rho=\pi_1\oplus\cdots\oplus\pi_m,\qquad
\ker\rho=\bigcap_{\nu=1}^m\ker\pi_\nu\subset U.
\tag{5.3}
\]

That kernel is a subgroup and hence trivial. If \(G\setminus U\) is empty, \(G\) is trivial and its one-dimensional trivial representation is faithful.

Lemma 5.1 proves that a compact Lie group meets this condition. Conversely, average an inner product on a faithful finite-dimensional representation, as in the preceding lesson. Its map into \(U(n)\) is a continuous injection from a compact space to a Hausdorff space, hence a homeomorphism onto its compact, closed image. The closed subgroup theorem gives a Lie subgroup, and therefore the required Lie structure on \(G\). ∎

This proof uses a finite subcover, without a decreasing sequence of kernels or a countable neighborhood basis.

**Corollary 5.4.** Every compact Hausdorff group is an inverse limit of compact Lie groups.

**Proof.** For each finite set \(F\) of irreducible classes, let \(G_F\) be the image in \(\prod_{\pi\in F}U(V_\pi)\). This image is compact and closed, hence a Lie subgroup. For \(F\subset F'\), coordinate projection maps \(G_{F'}\) onto \(G_F\). The natural map \(G\to\varprojlim_FG_F\) is injective by point separation. For a compatible family \((x_F)\), the closed fibers \(\{g:\pi_F(g)=x_F\}\) are nonempty. Any finite collection intersects, by using the fiber for the union of its index sets. Compactness makes their total intersection nonempty, proving surjectivity. The map is continuous and respects multiplication; compactness and the Hausdorff target make it a homeomorphism. ∎

## Three concrete coefficient systems

**The circle.** For \(G=S^1\), the characters \(\chi_n(e^{it})=e^{int}\), \(n\in\mathbb Z\), give the usual orthonormal system. Their Laurent polynomials form a unital, conjugation-closed algebra separating points. Stone–Weierstrass and density of continuous functions therefore make these characters complete in \(L^2\). They are all irreducible classes: an additional class would have a nonzero coefficient orthogonal to a dense subspace. Under \(L_h\), \(\chi_n\) carries \(\chi_{-n}\).

**A finite group.** Haar integration is \(|G|^{-1}\sum_{g\in G}\). The complete orthogonal coefficient decomposition gives

\[
|G|=\sum_{[\pi]\in\widehat G}d_\pi^2.
\tag{6.1}
\]

There are finitely many classes because their nonzero coefficient spaces are mutually orthogonal in a finite-dimensional space. The map

\[
\mathbb C[G]\longrightarrow
\bigoplus_{[\pi]\in\widehat G}\operatorname{End}(V_\pi),
\qquad
\sum_g a_g g\longmapsto\left(\sum_g a_g\pi(g)\right)_\pi
\tag{6.2}
\]

is an algebra homomorphism by \(\pi(gh)=\pi(g)\pi(h)\). If its image is zero, \(\sum_g a_gf(g)=0\) for every coefficient and hence every function on \(G\). Indicators of points force all \(a_g=0\). Equation (6.1) then gives equal dimensions, proving that (6.2) is an algebra isomorphism. For \(S_3\), the dimensions \(1,1,2\) account for six group elements.

**The defining representation of \(SU(2)\).** Its matrices are

\[
g=\begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix},
\qquad |a|^2+|b|^2=1.
\tag{6.3}
\]

A line invariant under all \(\operatorname{diag}(e^{it},e^{-it})\) must be a coordinate line, since one such matrix has distinct eigenvalues. The element \(a=0,b=1\) interchanges these lines. Thus the defining representation is irreducible. Its four entries \(a,b,-\bar b,\bar a\) are orthogonal in \(L^2(SU(2))\), each with squared norm \(1/2\). Multiplication by \(\sqrt2\) normalizes them. A later lesson constructs all irreducibles.

## Exercises with complete solutions

**Exercise 1 — direct orthogonality (easy).** Compute the coefficient inner products for the characters of \(SO(2)\), and for the trivial, sign and standard representations of \(S_3\). Verify completeness in both cases.

**Solution.** Parametrize \(SO(2)\) by \(0\leq t<2\pi\). Its characters \(e^{int}\) satisfy

\[
\frac1{2\pi}\int_0^{2\pi}e^{i(n-m)t}\,dt=\delta_{nm}.
\]

When \(n\ne m\), evaluation of \(e^{i(n-m)t}/(i(n-m))\) at the endpoints gives zero. Completeness follows from the Laurent-polynomial argument in the circle example.

Write \(S_3=\langle r,s:r^3=s^2=e,\ srs=r^{-1}\rangle\), let \(\omega=e^{2\pi i/3}\), and take

\[
\rho(r)=\begin{pmatrix}\omega&0\\0&\omega^{-1}\end{pmatrix},
\qquad \rho(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

These satisfy the relations. The eigenlines of \(\rho(r)\) are swapped by \(\rho(s)\), proving irreducibility. On \(r^a\), the diagonal entries are \(\omega^a,\omega^{-a}\), and the off-diagonal entries vanish. On \(sr^a\), the diagonal entries vanish, and the off-diagonal entries are \(\omega^{-a},\omega^a\).

Every entry has squared norm \(3/6=1/2\). Entries with disjoint parity supports are orthogonal. The two entries on either support are orthogonal because \(\sum_{a=0}^2\omega^{2a}=0\). Each entry has zero sum on its support, making it orthogonal to both the trivial and sign characters. Those characters have norm one and mutual inner product \((3-3)/6=0\). The two characters and four normalized entries form six orthonormal functions in a six-dimensional space, and hence a complete basis. Schur orthogonality excludes further irreducibles.

**Exercise 2 — square-integrable kernels (medium).** For \(\psi\in L^2(G)\), prove that convolution is Hilbert–Schmidt with

\[
\|K_\psi\|_{\mathrm{HS}}=\|\psi\|_2.
\tag{7.1}
\]

Do not assume separability.

**Solution.** Define the squared Hilbert–Schmidt norm of \(A\) as the supremum of \(\sum_{j=1}^m\|Ae_j\|^2\) over finite orthonormal families. For a finite product kernel, orthonormalize the span of the conjugates of its input factors to write

\[
k(x,y)=\sum_{j=1}^m a_j(x)\overline{e_j(y)},\qquad
A_kf=\sum_j\langle f,e_j\rangle a_j.
\]

Finite-dimensional Parseval and integration give

\[
\|A_k\|_{\mathrm{HS}}^2
=\sum_j\|a_j\|_2^2
=\int_{G\times G}|k(x,y)|^2\,dx\,dy.
\tag{7.2}
\]

For the first equality, \(A_k\) vanishes on the orthogonal complement of the input span. Any finite orthonormal family gives a sum bounded by the trace of the positive matrix \(A_k^*A_k\) on this span, while the displayed input basis attains it.

Hilbert–Schmidt operators are complete in this norm. Indeed, \(\|A\|\leq\|A\|_{\mathrm{HS}}\) gives an operator-norm limit for a Cauchy sequence; passing to the limit on each finite orthonormal family retains its Cauchy bound in Hilbert–Schmidt norm. Finite product kernels are dense in \(L^2(G\times G)\), by Stone–Weierstrass on continuous functions and regularity of product Haar measure. Thus the isometry (7.2) extends to all square-integrable kernels. The extension is compact, being an operator-norm limit of finite-rank operators.

For continuous \(\psi\), invariance of Haar measure gives

\[
\int_{G\times G}|\psi(xy^{-1})|^2\,dx\,dy
=\int_G|\psi(z)|^2\,dz.
\]

Approximate arbitrary \(\psi\in L^2(G)\) by continuous functions. Applying this identity to differences constructs \(\psi(xy^{-1})\) as an \(L^2\) kernel, independently of the approximation. Its integral operator is convolution by \(\psi\), interpreted almost everywhere. Equation (7.2) proves (7.1), without a sum over an uncountable basis.

**Exercise 3 — the left isotypic component (medium).** Show that \(E_\pi\) is exactly the left \(\bar\pi\)-isotypic subspace, and identify the left \(\sigma\)-isotypic component for any \(\sigma\).

**Solution.** The column decomposition and orthogonality give \(d_\pi\) copies of \(\bar\pi\) in \(E_\pi\). Each other \(E_\tau\) in the complete sum (4.2) contains only \(\bar\tau\). Distinct irreducibles have orthogonal isotypic spaces by the preceding lesson. Thus none with \(\tau\not\simeq\pi\) contributes to the left \(\bar\pi\)-isotypic space, which is exactly \(E_\pi\). Replacing \(\pi\) by \(\bar\sigma\) gives \(E_{\bar\sigma}\), with multiplicity \(d_\sigma\). The conjugate is forced by (1.2).

**Exercise 4 — a faithful matrix model (hard).** Derive a faithful finite-dimensional unitary representation from no small subgroups, without a countable neighborhood basis. Explain where compactness enters, and deduce a Lie structure.

**Solution.** Choose \(U\) containing no nontrivial subgroup. For each \(x\notin U\), point separation gives an irreducible whose kernel misses \(x\). The complements of these closed kernels cover \(G\setminus U\). A finite subcover makes the direct-sum representation's kernel a subgroup contained in \(U\), hence trivial. If the complement is empty, the group is trivial. Compactness also makes its injective unitary image closed and the map a homeomorphism onto that image. The closed subgroup theorem now gives a Lie subgroup. The two uses of compactness are the finite subcover and the closed embedded image; neither uses sequences.

## What this lesson does not prove

The Haar and compact spectral theorems are imported in the precise forms and with the locators given in the preceding lesson. Urysohn's lemma, regularity of finite Radon measure, and scalar Fubini and simple-function approximation are analysis prerequisites.

Stone–Weierstrass is proved in [*The Stone–Weierstrass theorem for functions vanishing at infinity*](../../../function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity.html#oa-fnd-sw-09), Theorem 10.1, for self-adjoint subalgebras of the continuous functions vanishing at infinity on a locally compact Hausdorff space that separate points and vanish nowhere. On a compact space every continuous function vanishes at infinity, and an algebra containing the constants vanishes nowhere; this is the complex form used here.

The Lie facts are [Etingof, Theorem 5.16](https://math.mit.edu/~etingof/lnlg.pdf), for the local exponential map and its one-parameter subgroup property, and Theorem 2.16 of the same lectures, for the closed subgroup theorem. Their proofs belong to Lie-group background. The faithful representation criterion and the inverse-limit result have been proved here.

## References and convention checks

- C. Gruson and V. Serganova, *A Journey Through Representation Theory* (2018), Chapter 3, §2: compact-group matrix coefficients. Our proof establishes continuous representatives before evaluation at the identity.
- P. Etingof, [*Lie Groups and Lie Algebras*](https://math.mit.edu/~etingof/lnlg.pdf), Theorem 2.16 for the closed subgroup theorem, §5.3 for the local exponential map, and §§36–37 for comparison with compact Lie and compact topological groups.

The approximation theorems retain their compact Hausdorff hypotheses. The distinctions between \(E_\pi\) and the left \(\pi\)-isotypic component, and between nets and sequences, are part of the mathematical content.
