# Fourier analysis and class functions on compact groups

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

Suppose a signal space contains several copies of several irreducible representations. A symmetry-respecting filter should select a representation type without selecting a basis inside its multiplicity space. Characters provide exactly those filters. On the function space of the group, the same operators become convolution, and their eigenvalues become scalar or matrix-valued Fourier data.

We begin with type selection and a concrete finite random walk. Then we package the complete coefficient expansion into Fourier matrices, distinguish conjugation-invariant data from arbitrary data, and study approximation by localized filters. Finally we ask a different reconstruction question: do all representations, together with their sum, tensor and dual operations, determine the group itself? The compact Tannaka theorem answers it with a full proof.

We use the full compact Hausdorff decomposition from [the first lesson](RT-CPT-01.md) and coefficient orthogonality and completeness from [Peter–Weyl](RT-CPT-02.md). Haar measure has mass one, inner products are linear in the first variable, and all sums have their Hilbert meaning without countability assumptions.

## Selecting a type without selecting a basis

**Theorem 4.3 (isotypic projections and character tests).** For any continuous unitary representation \(\rho\) on a Hilbert space,

\[
P_\pi=d_\pi\int_G\overline{\chi_\pi(g)}\,\rho(g)\,dg
\tag{4.4}
\]

is the orthogonal projection onto its \(\pi\)-isotypic component. The integral is strong, applied to each vector; no operator-norm continuity is required. Finite-dimensional characters determine representations up to equivalence, and a nonzero finite-dimensional representation is irreducible if and only if \(\int_G|\chi_\rho|^2=1\).

**Proof.** On an irreducible summand \(\sigma\), centrality of the integrand's scalar coefficient makes the integral commute with \(\sigma\), so Schur makes it \(cI\). Taking its trace gives

\[
c\,d_\sigma
=d_\pi\int_G\overline{\chi_\pi(g)}\chi_\sigma(g)\,dg
=d_\pi\delta_{\pi\sigma}.
\]

Thus it is identity on a \(\pi\) summand and zero on every other irreducible. The strong integral defines a bounded operator, of norm at most \(d_\pi\|\chi_\pi\|_1\). Agreement on finite sums in the full Hilbert decomposition extends by density to the isotypic orthogonal projection.

In finite dimension, write \(\rho\simeq\bigoplus_\pi m_\pi\pi\). Then \(\chi_\rho=\sum m_\pi\chi_\pi\), and orthogonality recovers \(m_\pi=\langle\chi_\rho,\chi_\pi\rangle\). This determines the representation. Moreover, \(\|\chi_\rho\|_2^2=\sum m_\pi^2\), which equals one exactly when a single multiplicity is one and all others are zero. Finite-dimensional continuous representations can first be unitarized by the first lesson. Orthogonality of (4.4) refers to that invariant inner product. ∎

## A finite filter that removes a whole representation

In \(S_3\), normalize counting measure to give each element mass \(1/6\). Let \(p\) be \(2\) on the three transpositions and zero elsewhere. Thus \(\int p=1\): the operation \((p*f)(x)=\frac13\sum_{s\text{ transposition}}f(s^{-1}x)\) averages over one transposition step. The trivial, sign and standard characters have class values \((1,1,1),(1,-1,1),(2,0,-1)\) on identity, transpositions and three-cycles, respectively, as constructed in the preceding lesson. Hence
\[
p=\chi_{\mathrm{triv}}-\chi_{\mathrm{sgn}}.
\]
The two scalar representations respond by \(1\) and \(-1\), whereas the two-dimensional standard representation responds by zero. To check the last assertion directly, \(\frac13\sum_{s\text{ transposition}}\pi(s)\) commutes with the standard representation because the set of transpositions is a conjugacy class. Schur makes it scalar; its trace is the class character value zero, so the scalar is zero. A single averaging step erases that entire type, not just one coordinate in it. Two steps have scalar responses \(1,1,0\). The sign change records alternation between even and odd permutations.

This example suggests three separate questions: how to select a type, how to record the response within a type of dimension greater than one, and how much information a central filter can retain. The character projectors answer the first; Fourier matrices answer the second. A central filter always gives a scalar response, which explains the third.

## Matrix-valued frequencies

For \(f\in L^1(G)\) and an irreducible unitary \(\pi\) on \(V_\pi\), define

\[
\widehat f(\pi)=\int_G f(g)\pi(g)^*\,dg.
\tag{1.1}
\]

This finite-dimensional integral satisfies \(\|\widehat f(\pi)\|_{\mathrm{op}}\leq\|f\|_1\). Replacing \(\pi\) by \(U\pi U^{-1}\) replaces its Fourier matrix by \(U\widehat f(\pi)U^{-1}\). Thus the construction does not depend on a chosen basis. The convolution convention is

\[
(f*h)(x)=\int_G f(y)h(y^{-1}x)\,dy.
\tag{1.2}
\]

Fubini and the substitution \(x=yz\) give

\[
\begin{aligned}
\widehat{f*h}(\pi)
&=\int_{G\times G}f(y)h(z)\pi(yz)^*\,dy\,dz\\
&=\widehat h(\pi)\widehat f(\pi).
\end{aligned}
\tag{1.3}
\]

The reversed order follows from \(\pi(yz)^*=\pi(z)^*\pi(y)^*\). The same substitution gives

\[
\widehat{L_xf}(\pi)=\widehat f(\pi)\pi(x)^*,
\qquad
\widehat{R_xf}(\pi)=\pi(x)\widehat f(\pi).
\tag{1.4}
\]

For \(f^*(g)=\overline{f(g^{-1})}\), inversion invariance of compact Haar measure gives \(\widehat{f^*}(\pi)=\widehat f(\pi)^*\).

The Fourier transform is injective on \(L^1(G)\). If all its matrices vanish, \(f\,dg\) integrates every conjugate matrix coefficient to zero. Their algebra is conjugation-closed and uniformly dense in \(C(G)\), so \(\int fq=0\) for every continuous \(q\). The finite measure \(|f|\,dg\) is regular: truncate \(|f|\) at a large constant \(M\), make the tail integral small, and use Haar regularity with set error smaller than \(\varepsilon/M\). The Urysohn and simple-function approximation argument of the preceding lesson therefore applies to this weighted measure. Approximate the bounded function \(s=\bar f/|f|\), set to zero where \(f=0\), by continuous \(q\) in \(L^1(|f|\,dg)\). Then \(\int fq\to\int fs=\int|f|\). The left side is always zero, proving \(f=0\) almost everywhere.

There is also a compact-group Riemann–Lebesgue statement: \(\|\widehat f(\pi)\|_{\mathrm{op}}\) tends to zero outside finite sets of irreducible classes. Finite coefficient sums have finitely supported Fourier transforms by Schur orthogonality. They are dense in \(L^1\), since they uniformly approximate continuous functions and continuous functions are \(L^1\)-dense. If \(p\) is such a sum with \(\|f-p\|_1<\varepsilon\), (1.1) bounds every Fourier-matrix error by \(\varepsilon\); outside the finite support of \(\widehat p\), this bounds \(\widehat f\) itself. Thus only finitely many classes exceed any fixed positive norm threshold.

**Theorem 1.5 (Plancherel and inversion).** For \(f\in L^2(G)\),

\[
\|f\|_2^2=\sum_{[\pi]\in\widehat G}
d_\pi\|\widehat f(\pi)\|_{\mathrm{HS}}^2,
\qquad
f=\sum_{[\pi]\in\widehat G}
d_\pi\operatorname{tr}\bigl(\widehat f(\pi)\pi(\,\cdot\,)\bigr)
\quad\text{in }L^2.
\tag{1.6}
\]

The map \(f\mapsto(\sqrt{d_\pi}\widehat f(\pi))_\pi\) is a unitary isomorphism onto the Hilbert direct sum of the finite matrix spaces with their Hilbert–Schmidt inner products.

If \(f=h*k\), with \(h,k\in L^2(G)\), it has a continuous representative, and its **trace-block series** in (1.6) converges absolutely and uniformly:

\[
\sum_\pi
\left\|d_\pi\operatorname{tr}
  \bigl(\widehat f(\pi)\pi(\,\cdot\,)\bigr)\right\|_\infty
\leq\|h\|_2\|k\|_2.
\tag{1.7}
\]

Here each summand is the complete trace for one irreducible class. We do not assert an absolute bound after splitting those traces into every individual matrix entry.

**Proof.** With \(\pi_{ij}(g)=\langle\pi(g)e_j,e_i\rangle\),

\[
\widehat f(\pi)_{ji}
=\int_G f(g)\overline{\pi_{ij}(g)}\,dg.
\]

The orthonormal basis \(\sqrt{d_\pi}\pi_{ij}\) gives Parseval with summands \(d_\pi|\widehat f(\pi)_{ji}|^2\). Summing the entries proves the norm formula. The coefficient expansion has terms \(d_\pi\widehat f(\pi)_{ji}\pi_{ij}\); collecting a finite block gives the trace in (1.6). Conversely, any square-summable family of these matrix entries defines a vector by that complete Hilbert basis, proving surjectivity and the unitary assertion.

For \(h,k\in L^2\), Cauchy–Schwarz in (1.2) gives \(|h*k(x)|\leq\|h\|_2\|k\|_2\). If \(x'=xa\), the difference is bounded by \(\|h\|_2\|R_ak-k\|_2\), after the invariant change of variable \(z=y^{-1}x\). Strong translation continuity therefore makes this representative continuous.

For finite matrices \(A,B\) and unitary \(U\), the Hilbert–Schmidt Cauchy–Schwarz inequality gives \(|\operatorname{tr}(BAU)|\leq\|B\|_{\mathrm{HS}}\|A\|_{\mathrm{HS}}\), since \(\|AU\|_{\mathrm{HS}}=\|A\|_{\mathrm{HS}}\). By (1.3),

\[
\begin{aligned}
\sum_\pi d_\pi
\left|\operatorname{tr}
 \bigl(\widehat k(\pi)\widehat h(\pi)\pi(x)\bigr)\right|
&\leq
\sum_\pi
 \bigl(\sqrt{d_\pi}\|\widehat k(\pi)\|_{\mathrm{HS}}\bigr)
 \bigl(\sqrt{d_\pi}\|\widehat h(\pi)\|_{\mathrm{HS}}\bigr)\\
&\leq\|k\|_2\|h\|_2.
\end{aligned}
\tag{1.8}
\]

The estimate holds for the supremum norm of each block as well. The summable bound gives uniform convergence of finite partial sums. Its sum equals \(h*k\) in \(L^2\) by (1.6); both functions are continuous, so equality holds everywhere. All sums mean suprema over finite subsets; square-summability leaves only countably many nonzero blocks for any particular function. ∎

## Conjugation makes the Fourier matrix scalar

Call \(f\in L^p(G)\) **central** if \(f(a^{-1}(\,\cdot\,)a)=f\) as an \(L^p\) equivalence class for every \(a\in G\). For continuous functions this is precisely constancy on conjugacy classes. This definition specifies a norm-class identity for each \(a\); it does not choose simultaneous pointwise representatives of all \(L^p\) functions.

**Lemma 2.1.** A function \(f\in L^1(G)\) is central if and only if

\[
\widehat f(\pi)=a_\pi(f)I,\qquad
a_\pi(f)=\frac1{d_\pi}\int_G f(g)\overline{\chi_\pi(g)}\,dg
\tag{2.2}
\]

for every irreducible \(\pi\).

**Proof.** Conjugating the variable in (1.1) makes its Fourier matrix conjugate by \(\pi(a)\). Invariance of \(f\) thus makes \(\widehat f(\pi)\) commute with every \(\pi(a)\). Schur's lemma makes it scalar; its trace determines that scalar as (2.2). Conversely, scalar matrices do not change under this conjugation. The Fourier transforms of \(f(a^{-1}(\,\cdot\,)a)\) and \(f\) agree, so injectivity on \(L^1\) makes their classes equal. ∎

Convolution makes \(L^p(G)\), \(1\leq p\leq\infty\), a Banach algebra: Young's inequality gives \(\|f*h\|_p\leq\|f\|_1\|h\|_p\leq\|f\|_p\|h\|_p\). The same estimate with the supremum norm applies to \(C(G)\); convolution of continuous functions is continuous. Associativity follows by Fubini on the absolutely integrable triple product.

Its centre is exactly the central functions. A central Fourier matrix commutes with every Fourier matrix, so (1.3) and injectivity prove that a central function commutes with every convolution factor. Conversely, if \(f\) commutes with every factor in the algebra, test it against the matrix coefficients. At \(\pi\), their Fourier matrices are all matrix units divided by \(d_\pi\), by Schur orthogonality. Thus \(\widehat f(\pi)\) commutes with every matrix, hence is scalar. Lemma 2.1 proves centrality. This also works for \(p=\infty\), since all functions involved lie in \(L^1\) on our probability space.

**Theorem 2.3 (character completeness).** The irreducible characters are an orthonormal Hilbert basis of \(ZL^2(G)\), and their span is uniformly dense in \(ZC(G)\). For central \(f\in L^2\),

\[
f=\sum_\pi\langle f,\chi_\pi\rangle\chi_\pi,\qquad
\|f\|_2^2=\sum_\pi|\langle f,\chi_\pi\rangle|^2.
\tag{2.4}
\]

**Proof.** Schur orthogonality gives \(\langle\chi_\pi,\chi_\sigma\rangle=\delta_{\pi\sigma}\). By Lemma 2.1, the block of a central \(f\) in (1.6) is

\[
d_\pi\operatorname{tr}\bigl(a_\pi(f)I\pi(g)\bigr)
=\langle f,\chi_\pi\rangle\chi_\pi(g).
\]

Plancherel proves both identities in (2.4), so no central orthogonal remainder exists.

For the uniform claim, average a continuous function over conjugation:

\[
(\mathcal Cf)(g)=\int_Gf(a^{-1}ga)\,da.
\tag{2.5}
\]

This continuous central function satisfies \(\|\mathcal Cf\|_\infty\leq\|f\|_\infty\), and \(\mathcal Cf=f\) when \(f\) is central. Averaging the matrices \(\pi(a)^{-1}\pi(g)\pi(a)\) and applying Schur and trace gives

\[
\mathcal C\pi_{ij}=\frac{\delta_{ij}}{d_\pi}\chi_\pi.
\tag{2.6}
\]

Uniformly approximate a central continuous \(f\) by a finite coefficient sum, using Peter–Weyl, and apply the contraction \(\mathcal C\). Equation (2.6) converts it into a finite character sum without increasing the error. ∎

For arbitrary \(f\in L^1\), trace and (1.1) also give the block identity

\[
d_\pi(f*\chi_\pi)(x)
=d_\pi\operatorname{tr}\bigl(\widehat f(\pi)\pi(x)\bigr).
\tag{2.7}
\]

For central \(f\), this becomes

\[
d_\pi f*\chi_\pi
=\left(\int_Gf\,\overline{\chi_\pi}\right)\chi_\pi.
\tag{2.8}
\]

The conjugate in the integral and the dimension in the denominator of (2.2) are both required.

Character sums are dense in \(ZL^1(G)\) as well. To see this without a convergence prescription, approximate a central \(f\) in \(L^1\) by continuous functions \(q\). Translation continuity in \(L^1\) follows from this density and the translation isometries, by the same approximation argument used for \(L^2\) in lesson 2. Conjugation averaging \(\mathcal C\) is an \(L^1\) contraction by the integral triangle inequality and invariance of Haar measure; on \(L^1\) it is the vector integral of the strongly continuous conjugation orbit. It fixes central classes. Thus \(\mathcal Cq\) are continuous central approximants to \(f\). The uniform character density just proved approximates each of them in \(L^1\), since the measure has mass one. This proves the density used in the next spectral theorem independently of the localized approximate identities below.

## Converting a finite class table into filter responses

For a finite group, no convergence issue remains. Class indicators form a basis of central functions, while Theorem 2.3 gives a basis of irreducible characters. Hence the number of irreducible classes equals the number of conjugacy classes. The identity \(|G|=\sum d_\pi^2\) was proved in the preceding lesson.

For \(S_3\), list the classes as identity, transpositions and three-cycles, of sizes \(1,3,2\). The characters constructed in the preceding lesson have values

\[
\chi_{\mathrm{triv}}=(1,1,1),\qquad
\chi_{\mathrm{sgn}}=(1,-1,1),\qquad
\chi_{\mathrm{std}}=(2,0,-1).
\]

For a central function with values \((u,v,w)\), its three character coefficients are

\[
\alpha_{\mathrm{triv}}=\frac{u+3v+2w}{6},\qquad
\alpha_{\mathrm{sgn}}=\frac{u-3v+2w}{6},\qquad
\alpha_{\mathrm{std}}=\frac{u-w}{3}.
\tag{5.3}
\]

The scalar Fourier blocks are the first two coefficients and \(\alpha_{\mathrm{std}}/2\). This division by two is what makes convolution become multiplication of the scalars. For example, the indicator of the identity is \((\chi_{\mathrm{triv}}+\chi_{\mathrm{sgn}}+2\chi_{\mathrm{std}})/6\). The convolution unit for normalized counting measure is six times that indicator.

## The responses of all central filters

**Theorem 4.1.** The Gelfand spectrum of the commutative convolution algebra \(ZL^1(G)\) is the discrete set \(\widehat G\), through the functionals \(a_\pi\) in (2.2).

**Proof.** Each \(a_\pi\) is bounded by the \(L^1\) norm and multiplicative by (1.3), since its Fourier block is scalar. Orthogonality and injectivity give

\[
\chi_\pi*\chi_\sigma
=\delta_{\pi\sigma}\frac{\chi_\pi}{d_\pi}.
\tag{4.2}
\]

Hence \(e_\pi=d_\pi\chi_\pi\) are pairwise orthogonal convolution idempotents. If a nonzero continuous multiplicative functional \(b\) vanished on all of them, character-span density in \(ZL^1\) would force \(b=0\). Thus \(b(e_\pi)\ne0\) for some \(\pi\), and idempotence forces \(b(e_\pi)=1\). Equation (2.8) says \(f*e_\pi=a_\pi(f)e_\pi\). Applying \(b\) gives \(b(f)=a_\pi(f)\) for every central \(f\). Orthogonality of the idempotents makes the index unique. Finally evaluation at \(e_\pi\) is continuous on the spectrum in its weak topology, and the condition \(|b(e_\pi)-1|<1/2\) isolates \(a_\pi\). Every point is open. ∎

For an irreducible of dimension two, the wrong candidate \(f\mapsto2\int f\overline{\chi_\pi}\) takes the value four on the idempotent \(2\chi_\pi\). It cannot be multiplicative, because a multiplicative functional takes only zero or one on an idempotent. Formula (2.2) instead takes value one, as required.

## Central approximate identities

Compactness makes conjugation-invariant identity neighborhoods a neighborhood basis. Indeed, given \(U\), joint continuity of \((a,x)\mapsto axa^{-1}\) gives, for each \(a\), neighborhoods \(V_a\) of \(a\) and \(W_a\) of \(e\) with \(bW_ab^{-1}\subset U\) for \(b\in V_a\). A finite subcover of the \(V_a\) gives \(W=\bigcap W_a\), and

\[
V=\bigcup_{b\in G}bWb^{-1}\subset U
\tag{3.1}
\]

is an open invariant identity neighborhood. Shrinking \(W\) symmetrically also makes \(V\) symmetric.

Take a continuous nonnegative symmetric function of integral one supported in such a \(V\), as in the preceding lesson, and average it by (2.5). The resulting \(\mu_V\) is central, nonnegative, symmetric, has integral one, and is still supported in \(V\). The conjugates of its compact support form a compact subset of \(V\), so there is no support problem in this averaging.

As \(V\) shrinks, \(f*\mu_V\to f\) uniformly for \(f\in C(G)\) and in \(L^p\) for \(1\leq p<\infty\). For example,

\[
\|f*\mu_V-f\|_p
\leq\sup_{y\in V}\|R_{y^{-1}}f-f\|_p.
\tag{3.2}
\]

Use the equivalent convolution formula \((f*\mu_V)(x)=\int\mu_V(y)f(xy^{-1})\,dy\). Strong \(L^p\) continuity follows from continuous-function density and isometry of translations, just as for \(p=2\) in the preceding lesson. The uniform case follows directly from uniform continuity.

The scalar Fourier multiplier \(a_\pi(\mu_V)\) tends to one for each fixed \(\pi\), because \(\pi(y)^*\) tends uniformly to \(I\) on shrinking identity neighborhoods. It has absolute value at most one. Its exact Plancherel normalization is

\[
\|\mu_V\|_2^2
=\sum_\pi d_\pi^2|a_\pi(\mu_V)|^2.
\tag{3.3}
\]

For \(f\in L^1\), set \(\zeta_V=\mu_V*\mu_V\). Then \(f*\mu_V\in L^2\) by Young, so Theorem 1.5 gives an absolutely uniformly convergent trace-block series for \((f*\mu_V)*\mu_V=f*\zeta_V\). These \(\zeta_V\) are also nonnegative central functions of mass one, supported in \(V^2\); their supports shrink to \(e\). Thus they give uniform Fourier summation after smoothing, even for \(L^1\) input, and \(f*\zeta_V\to f\) in \(L^p\), \(p<\infty\), or uniformly for continuous input. For central input all the trace blocks are scalar multiples of characters. This proves character-span density in \(ZL^p(G)\), \(p<\infty\), as well.

## A positive summation rule on the circle

For the circle, write \(g=e^{it}\), \(dt/(2\pi)\), and \(\chi_n(g)=e^{int}\). Then (1.1) is the ordinary convention

\[
\widehat f(n)=\frac1{2\pi}\int_0^{2\pi}f(e^{it})e^{-int}\,dt.
\tag{5.1}
\]

For a compact abelian group every irreducible has dimension one, by Schur's lemma in the first lesson, so the matrix formulas become these scalar character formulas. If another convention labels a frequency by \(\int f\chi\), its label is \(\bar\chi\) in (1.1); on the circle this replaces \(n\) by \(-n\).

An explicit central approximate identity on the circle is the Fejér kernel

\[
F_N(t)=\frac1{N+1}\left|\sum_{j=0}^N e^{ijt}\right|^2
=\sum_{|n|\leq N}\left(1-\frac{|n|}{N+1}\right)e^{int}.
\tag{5.2}
\]

Expanding the square counts \(N+1-|n|\) pairs with difference \(n\), proving the second equality. The first proves nonnegativity, and the constant Fourier coefficient proves integral one. Outside the angular neighborhood \(|t|<\delta\) modulo \(2\pi\), the geometric sum gives

\[
F_N(t)\leq\frac1{(N+1)\sin^2(\delta/2)}.
\]

Thus its mass away from the identity tends to zero. In the norm of \(C(G)\) or \(L^p\), \(p<\infty\), split the integral of the translation difference into this tail and its complement. The tail is bounded by twice the function's norm times the tail mass, and translation continuity makes the complement small. Consequently \(f*F_N\to f\) in the respective norm. These are the Fejér means of its Fourier series. For \(f(e^{it})=1+\cos t\), the \(N\)-th mean, \(N\geq1\), is \(1+\frac{N}{N+1}\cos t\).

## Reconstructing the compact group

Choose a set of finite-dimensional Hilbert spaces containing every \(\mathbb C^n\) and closed under finite direct sums, tensor products and duals. Include all continuous unitary representations of \(G\) on those spaces; this makes the indexing collection an actual set. Let \(\Gamma\) consist of unitary families \(A=(A_\pi)_\pi\) compatible with unitary equivalences, direct sums, tensor products and duals. On the dual space the operator is \(A_\pi^{-t}\), the inverse transpose. Use pointwise multiplication and the topology determined by all scalar coefficients of \(A_\pi\).

**Theorem 7.1 (compact Tannaka duality).** The group \(\Gamma\) is compact, and

\[
G\longrightarrow\{A\},\qquad g\longmapsto(\pi(g))_\pi
\]

is an isomorphism of topological groups.

*Proof.* The families form a closed subset of the compact product \(\prod_\pi U(V_\pi)\): each compatibility condition is a closed matrix equality, including the continuous inverse-transpose condition. Products and inverses preserve all conditions, so this is a compact Hausdorff topological group. Evaluation at \(g\in G\) gives a continuous homomorphism. Matrix coefficients separate points by lesson two, hence this homomorphism is injective.

First note two consequences of compatibility. On the one-dimensional trivial representation, tensor compatibility gives \(A_1=A_1^2\); unitarity forces \(A_1=1\). Direct sums then give the identity on every trivial representation. Moreover the family respects every intertwiner \(T:V_\pi\to V_\sigma\), not only unitary equivalences. The graph of \(T\) and its orthogonal complement are invariant subspaces of \(V_\pi\oplus V_\sigma\). Choose unitary coordinates on them. The representations in those coordinates are among the indexed representations, and sum compatibility plus unitary-equivalence compatibility makes \(A_\pi\oplus A_\sigma\) preserve the graph. Thus
\[
A_\sigma T=TA_\pi.
\]
In particular \(A_\tau\) fixes every \(G\)-fixed vector in any representation \(\tau\). On a conjugate unitary representation, dual compatibility gives \(\overline{A_\pi}\), since inverse transpose equals complex conjugation for a unitary matrix.

Fix one finite-dimensional representation \(\pi\), and put \(H=\pi(G)\), a closed subgroup of \(U(V_\pi)\). We show \(A_\pi\in H\). Suppose otherwise. The function
\[
f(u)=\operatorname{dist}(u,H)
\]
for the Hilbert–Schmidt matrix distance is continuous and right-\(H\)-invariant, with \(f(1)=0\) and \(f(A_\pi)=d>0\). Polynomials in the matrix entries of \(u\) and their conjugates are uniformly dense in \(C(U(V_\pi))\): they contain constants, are closed under conjugation and separate matrices, so the complex Stone–Weierstrass theorem applies. Choose such a polynomial \(p\) with \(\|p-f\|_\infty<d/3\), and average on the right:
\[
q(u)=\int_H p(uh)\,dh.
\]
Then \(\|q-f\|_\infty<d/3\).

Each monomial of \(p\) is a matrix coefficient of a tensor representation
\[
r(u)=u^{\otimes a}\otimes\overline u^{\otimes b}.
\]
Averaging a coefficient \(\phi(r(u)v)\) replaces \(v\) by
\(v_H=\int_H r(h)v\,dh\), an \(H\)-fixed vector. Pull \(r\) back through \(\pi\); it becomes a tensor-and-dual representation \(\tau\) of \(G\). Tensor compatibility gives \(A_\tau=r(A_\pi)\), and the preceding intertwiner argument gives \(r(A_\pi)v_H=v_H\). Consequently each averaged coefficient has the same value at \(A_\pi\) and at \(1\), so
\[
q(A_\pi)=q(1).
\]
This contradicts \(f(A_\pi)-f(1)=d\) and the approximation error smaller than \(2d/3\). Thus \(A_\pi\in\pi(G)\).

Apply this argument to the direct sum of any finite collection of representations. It produces one \(g\in G\) with all their matrices equal to the prescribed \(A_\pi\)'s simultaneously. The closed sets
\[
\{g\in G:\pi(g)=A_\pi\}
\]
therefore have the finite intersection property. Compactness of \(G\) supplies a point in their intersection over all \(\pi\). This proves surjectivity without a countability assumption. A continuous bijection from compact \(G\) to Hausdorff \(\Gamma\) is a homeomorphism, proving the theorem. \(\square\)

The proof here uses the earlier coefficient-separation theorem, compact Haar averaging and Stone–Weierstrass; it does not assume a duality theorem for abelian groups or a finite-group reconstruction theorem.

## Exercises with complete solutions

**Exercise 1 — character convolution (easy).** Prove (4.2), including its dimension factor.

**Solution.** The \((i,j)\) entry of \(\widehat{\chi_\pi}(\sigma)\) is the sum over the diagonal entries of \(\pi\) of their inner products with \(\sigma_{ji}\). Schur orthogonality makes it zero for \(\sigma\not\simeq\pi\), and \(\delta_{ij}/d_\pi\) for \(\sigma=\pi\). Thus the Fourier transform of \(\chi_\pi*\chi_\tau\) is zero at every class unless \(\pi=\tau\); in that case its only nonzero matrix is \(I/d_\pi^2\) at \(\pi\). This is exactly the transform of \(\chi_\pi/d_\pi\). Injectivity proves the identity. The factor is also forced by idempotence of \(d_\pi\chi_\pi\).

**Exercise 2 — isotypic projection (medium).** Verify (4.4) for an arbitrary unitary Hilbert representation, including infinite multiplicities. Explain why it need not be an orthogonal projection for a nonunitary representation in its original inner product.

**Solution.** On any irreducible summand \(\sigma\), conjugation invariance of \(\overline{\chi_\pi}\) makes the averaged operator scalar. Trace gives scalar \(d_\pi\delta_{\pi\sigma}/d_\sigma\), hence one for \(\sigma=\pi\) and zero otherwise. Finite sums of summand vectors are dense in the Hilbert direct sum. Since the integral has the bound \(d_\pi\|\chi_\pi\|_1\), its action extends from these sums to the whole space. It selects every copy of \(\pi\), irrespective of how many copies there are. Its range is therefore the canonical isotypic subspace, and its kernel is the orthogonal sum of the other types.

For the second assertion, let \(z\in S^1\) and

\[
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
\rho(z)=A\begin{pmatrix}z&0\\0&1\end{pmatrix}A^{-1}
=\begin{pmatrix}z&1-z\\0&1\end{pmatrix}.
\]

Using the character \(\chi_1(z)=z\), the integral in (4.4) is

\[
P_{\chi_1}=\begin{pmatrix}1&-1\\0&0\end{pmatrix}.
\]

Its square is itself, but its adjoint is different. Thus it is an isotypic projection and is not orthogonal in the Euclidean inner product. The averaged invariant inner product makes the two invariant lines orthogonal and restores the orthogonal-projection statement.

**Exercise 3 — a sufficient uniform character bound (medium).** If \(f\in ZC(G)\) and \(\sum_\pi d_\pi|\langle f,\chi_\pi\rangle|<\infty\), prove that its character expansion converges uniformly to \(f\).

**Solution.** Every eigenvalue of a unitary \(\pi(g)\) has modulus one, so \(|\chi_\pi(g)|\leq d_\pi\). The hypothesis therefore bounds the sum of the supremum norms of the character terms. Finite partial sums converge uniformly to a continuous function \(u\). By (2.4), the same sums converge in \(L^2\) to \(f\); uniform convergence also implies \(L^2\) convergence to \(u\). Thus \(u=f\) almost everywhere. The full support of Haar measure makes equal continuous representatives equal everywhere. This proves the claim for arbitrary compact \(G\), with finite-subset sums if its dual is uncountable.

**Exercise 4 — uniform convolution expansion (hard).** Prove the absolute uniform convergence part of Theorem 1.5 and give an explicit tail bound.

**Solution.** Let \(B_\pi(x)=d_\pi\operatorname{tr}(\widehat k(\pi)\widehat h(\pi)\pi(x))\). Finite-dimensional Hilbert–Schmidt Cauchy–Schwarz gives

\[
\|B_\pi\|_\infty
\leq d_\pi\|\widehat k(\pi)\|_{\mathrm{HS}}
             \|\widehat h(\pi)\|_{\mathrm{HS}}.
\]

Weighted Cauchy–Schwarz and Plancherel bound its sum by \(\|k\|_2\|h\|_2\). For any finite set \(F\subset\widehat G\),

\[
\left\|\sum_{\pi\notin F}B_\pi\right\|_\infty
\leq
\left(\sum_{\pi\notin F}
 d_\pi\|\widehat h(\pi)\|_{\mathrm{HS}}^2\right)^{1/2}
\|k\|_2.
\tag{6.1}
\]

The right side tends to zero as \(F\) increases, by summability. Its bound also applies to every finite tail before the sum is defined, so it proves uniform Cauchy convergence without assuming a pre-existing enumeration. The limit agrees with the \(L^2\) expansion of \(h*k\); the convolution is continuous by the translation estimate in Theorem 1.5. Equal continuous functions with equal \(L^2\) classes agree everywhere. This establishes both the convergence and its identification with convolution, rather than just convergence to an unspecified function.

## What this lesson does not prove

The Haar, Schur and Peter–Weyl prerequisites are imported from the two preceding lessons, in their stated compact Hausdorff forms. Scalar Fubini, regularity, simple-function approximation, Stone–Weierstrass and compact product topology are the ordinary measure and topology prerequisites. The convolution estimate used above follows directly from normalized Haar measure: translations are isometries and the integral triangle inequality gives
\[
\|f*h\|_p
\leq\int_G |f(y)|\,\|h(y^{-1}\,\cdot)\|_p\,dy
=\|f\|_1\|h\|_p,\qquad 1\leq p<\infty.
\]
For \(p=\infty\), the essential bound under Haar-preserving translations and Fubini give the same result directly for measurable functions. For finite \(p\), continuous-function density and this estimate extend the result to \(L^p\) classes. The \(L^2\) continuity and uniform estimates required for convolution were proved explicitly above.

## References

- C. Gruson and V. Serganova, *A Journey Through Representation Theory* (2018), Chapter 3, §2, Corollaries 2.7 and 2.9, for coefficient spaces and central functions.

For compact abelian groups, [**HA-LCA-08**, Theorem 1.1](course:HA-LCA/HA-LCA-08#section-1) is the general LCA Plancherel counterpart. It uses the same conjugate-character transform and inner products linear in the first variable. Its arbitrary locally compact statement is stronger in the abelian direction; the present matrix formulas and compact reconstruction are proved here and do not follow from that scalar theorem alone.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §§35–37. Its orthogonality and Peter–Weyl treatment provide compact coefficient context. They are not used as a proof of the tensor reconstruction theorem; the full arbitrary-compact reconstruction argument is supplied here.
