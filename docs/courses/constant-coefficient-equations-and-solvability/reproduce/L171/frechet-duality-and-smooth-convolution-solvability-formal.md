# Fréchet duality and smooth convolution solvability

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Support geometry controls where a transpose inverse can live. Fourier division controls its order. Together these give smooth convolution solvability, once the relevant dual range is closed. We prove the two general Fréchet-space duality statements needed for that conclusion, including the polar-section closure criterion, and then construct the uniform bounds for convolution.

Basic references are [Tao's notes on Baire's theorem and its Banach-space consequences](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/), [Grubb's Fourier-distribution notes](https://web.math.ku.dk/~grubb/dist5.pdf), and Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. Normed Hahn–Banach, dual norm tests, dual operator-space completeness, Baire and the full Fréchet open-mapping theorem are proved in Sections 3, 5, 6 and 14 of Banach estimates, quotient spaces and compact parameter arguments. We use the seminorm extension and gauge arguments proved in Propositions 1.1–1.2 of Continuous functionals, test families and compact limits. Compact scalar disks and their finite-dimensional topology are supplied by Metric and topological foundations.

The exact Fourier inputs are the entire-division characterization in Theorem 1.1 of Slow decrease and entire Fourier division, the local nonzero-entire-multiplier estimate in Lemma 2.1 of Analytic forcing and smooth convolution solutions, and the compact Fourier growth criterion in Theorem CF2.1 of Compact Fourier division and multiplicity-sensitive annihilators. Support distances and admissible convolution domains supplies confinement for compact distributions. We supply every additional duality and uniform-bound argument below.

The Fourier pairing uses Theorem 1.1, with its full normalization, of Fourier transforms, finite spectra and convex separation. Smooth cutoffs inside an arbitrary open domain are proved in Section 13.10 of the linked metric foundation.

## 1. Weak-star polars and compactness

All vector spaces in the duality sections are over \(\mathbb R\) or \(\mathbb C\). Duals consist of continuous linear functionals; the pairing is bilinear. For a locally convex space \(E\), its weak-star dual topology \(\sigma(E',E)\) is pointwise convergence on \(E\). For \(U\subset E\), write
\[
 U^\circ=\{\ell\in E':|\ell(x)|\le1\text{ for every }x\in U\}.
 \tag{1.1}
\]
For \(A\subset E'\), its prepolar is defined by the same inequality with the roles reversed. A set is absolutely convex when it is convex and balanced under scalar multiplication by scalars of modulus at most one.

**Lemma 1.1 (compact seminorm polars).** If \(p\) is a continuous seminorm on \(E\), then
\[
 B_p=\{\ell\in E':|\ell(x)|\le p(x)\text{ for every }x\in E\}
 \tag{1.2}
\]
is weak-star compact and closed. It is the polar of \(\{x:p(x)<1\}\).

*Proof.* Homogeneity, including scaling vectors in \(\ker p\), proves the last assertion. Embed \(B_p\) by its values in the product of compact scalar disks
\[
 \prod_{x\in E}\{z:|z|\le p(x)\}.
 \tag{1.3}
\]
Linearity is a closed condition: the equations at \(x+y\) and at \(\lambda x\) are closed equations between finitely many coordinates. Any point satisfying those equations is linear and is continuous by the bound \(p\). Thus \(B_p\) is a closed subset of this product. The product topology on it is exactly the weak-star topology.

Here is the needed arbitrary-product compactness argument. We use Zorn's lemma, also used in the normed Hahn–Banach proof. Every proper filter extends to an ultrafilter: order proper filters containing it by inclusion; the union of a chain remains a proper filter, since each finite collection of its members lies in one filter of the chain. A maximal member therefore exists. Its maximality implies that for any subset \(A\), either \(A\) or its complement belongs to it. Indeed, if adjoining \(A\) cannot preserve properness, one existing filter member is disjoint from \(A\), so the complement belongs to the filter.

On a compact space, the closures of the members of an ultrafilter have the finite-intersection property and hence have a common point. Every neighborhood of that point belongs to the ultrafilter: otherwise its closed complement would belong to it and would exclude the point from one of those closures. The filter therefore converges. Conversely, if every ultrafilter converges but an open cover has no finite subcover, the complements of finite unions of cover members generate a proper filter. An ultrafilter extending it cannot converge, since at any candidate limit a containing cover member and its complement would both belong to the filter. This is a contradiction.

For a product of compact Hausdorff spaces, each coordinate image of an ultrafilter converges to a unique coordinate point. These points form a product point, and every finite-coordinate basic neighborhood belongs to the ultrafilter. Hence it converges in the product. The disk product in (1.3) is nonempty, since the zero coordinates belong to every factor. This proves its compactness with no countability or separability restriction. A closed subset is compact. The weak-star topology is Hausdorff, since distinct functionals differ at some vector, so compact subsets are closed. \(\square\)

**Lemma 1.2 (bipolar separation).** In a Hausdorff locally convex space \(Z\), the bipolar of a nonempty absolutely convex set \(A\) is its closure, using the continuous dual pairing.

*Proof.* Every continuous functional bounded by one on \(A\) remains so on its closure \(C\), giving one inclusion. Let \(z_0\notin C\). Choose a balanced convex open neighborhood \(W\) of zero such that \((z_0+W)\cap C=\varnothing\). Put \(V=W/3\). Choose \(0<\lambda<1\) sufficiently close to one that \((\lambda-1)z_0\in W/3\). Then \(\lambda z_0\notin C+V\): otherwise \(c=\lambda z_0-v\) would lie in \(z_0+W\) for some \(c\in C\), a contradiction.

The open absolutely convex absorbing set \(C+V\) has a continuous seminorm gauge \(g\), by the linked gauge proof. It satisfies \(g(c)\le1\) on \(C\) and
\[
 g(z_0)\ge1/\lambda>1.
 \tag{1.4}
\]
On the scalar line through \(z_0\), define \(L(tz_0)=t g(z_0)\). It is bounded by \(g\). The linked seminorm Hahn–Banach theorem extends it continuously to \(Z\), with \(|L|\le g\). Thus \(|L(c)|\le1\) on \(A\), but \(L(z_0)>1\). This excludes \(z_0\) from the bipolar and proves equality. \(\square\)

For \(Z=E'\) with its weak-star topology, every continuous linear \(L\) is evaluation at a vector of \(E\). Continuity bounds \(L\) by finitely many evaluations at \(x_1,\ldots,x_k\). It therefore vanishes when those evaluations vanish, and factors through their range in the finite-dimensional scalar space. Extend that finite-dimensional linear map and write
\[
 L(\ell)=\sum_j a_j\ell(x_j)=\ell\left(\sum_j a_jx_j\right).
 \tag{1.5}
\]
Consequently Lemma 1.2 also gives the weak-star bipolar theorem in the dual pair \((E',E)\). In particular a weak-star closed linear \(M\subset E'\) equals the annihilator of its preannihilator.

## 2. Turning approximate openness into openness

**Lemma 2.1 (summable lifting).** Let \(E\) be Fréchet, let \(G\) be a Hausdorff metrizable locally convex space, and let \(S:E\to G\) be continuous and linear. Suppose the closure of \(S(U)\) contains a neighborhood of zero in \(G\) for every neighborhood \(U\) of zero in \(E\). Then \(S\) is open and surjective. Completeness of \(G\) is not required for this implication.

*Proof.* Choose increasing defining seminorms \(p_j\) on \(E\) and \(q_j\) on \(G\). To prove that the image of an arbitrary neighborhood \(U\) contains a neighborhood, choose \(j_0,\varepsilon>0\) such that \(\{p_{j_0}<\varepsilon\}\subset U\). For \(j\ge0\), put
\[
 U_j=\{x:p_{j_0+j}(x)<\varepsilon2^{-j-2}\}.
 \tag{2.1}
\]
Choose balanced open neighborhoods \(V_j\) in \(G\) contained in \(\overline{S(U_j)}\) and also in \(\{q_{j+1}<2^{-j}\}\).

For \(y\in V_0\), use its membership in \(\overline{S(U_0)}\) to choose \(x_0\in U_0\) with \(r_1=y-Sx_0\in V_1\). Inductively, from \(r_j\in V_j\subset\overline{S(U_j)}\), choose \(x_j\in U_j\) with \(r_{j+1}=r_j-Sx_j\in V_{j+1}\). Every fixed \(p_k\) is eventually bounded on the terms by the summable \(\varepsilon2^{-j-2}\), so \(\sum_jx_j\) is Cauchy in every defining seminorm. Completeness gives \(x\in E\). Also \(p_{j_0}(x)\le\varepsilon/2<\varepsilon\), hence \(x\in U\).

The residuals tend to zero in every \(q_k\), because \(q_k(r_j)\le q_{j+1}(r_j)<2^{-j}\) once \(j+1\ge k\). Continuity and Hausdorffness give \(Sx=y\). Therefore \(V_0\subset S(U)\). This proves openness. The linear range contains a neighborhood of zero; that neighborhood absorbs every vector of \(G\), so the range is all of \(G\). \(\square\)

## 3. Closed polar sections determine a closed dual subspace

**Theorem 3.1 (linear polar-section criterion).** If \(E\) is Fréchet and \(M\) is a linear subspace of \(E'\), then \(M\) is weak-star closed if and only if \(M\cap U^\circ\) is weak-star closed for every neighborhood \(U\) of zero in \(E\).

The nontrivial direction is the linear polar-section form of the Banach–Dieudonné theorem. We prove it for general Fréchet spaces.

*Proof.* If \(M\) is closed, every section is closed because a polar is an intersection of closed evaluation inequalities.

Conversely, choose increasing defining seminorms \(p_j\), set \(B_j=B_{p_j}\), and put \(C_j=M\cap B_j\). The hypothesis makes \(C_j\) weak-star closed. It is absolutely convex and contains zero. Define
\[
 q_j(x)=\sup_{\ell\in C_j}|\ell(x)|,\qquad
 N=\{x:\ell(x)=0\text{ for all }\ell\in M\}.
 \tag{3.1}
\]
Then \(q_j\le p_j\), and the \(q_j\) increase. They vanish exactly on \(N\) as a family. Indeed every \(\ell\in M\) is bounded by some \(c p_j\), so \(\ell/c\in C_j\). On \(G=E/N\), the \(q_j\) therefore define a Hausdorff metrizable locally convex topology.

The continuous dual of this \(G\), identified by pullback to \(E\), is exactly \(M\). Every \(\ell\in M\) is bounded by \(c q_j\), as just shown, so is continuous on \(G\). Conversely, a functional continuous for the \(q_j\) is bounded by \(c q_j\) for some \(j\) and is also continuous for the original topology because \(q_j\le p_j\). Lemma 1.2 on the weak-star closed \(C_j\) gives
\[
 \{\ell\in E':|\ell(x)|\le q_j(x)\text{ for all }x\}=C_j.
 \tag{3.2}
\]
For completeness, the prepolar of \(C_j\) is \(\{q_j\le1\}\); homogeneity, including \(\ker q_j\), identifies its polar with the set on the left of (3.2). The weak-star bipolar equality then proves (3.2). Thus the continuous functional divided by \(c\) lies in \(C_j\), hence in \(M\).

Let \(S:E\to G\) be the quotient map, continuous since \(q_j\le p_j\). For \(U_j=\{p_j<1\}\), its image has polar \(C_j\) in the dual \(G'=M\). Apply Lemma 1.2 in \(G\):
\[
 \overline{S(U_j)}=\{z\in G:q_j(z)\le1\}.
 \tag{3.3}
\]
In particular it contains a neighborhood of zero. Scaling and the increasing seminorm base show the same for the image of every original neighborhood. Lemma 2.1 makes \(S\) open.

Its quotient topology from the original \(E\) is therefore exactly the \(q_j\) topology. Continuous functionals on that quotient are precisely the original functionals annihilating \(N\): continuity in either direction follows from the quotient map being continuous and open. Since its dual is \(M\), we get
\[
 M=N^\perp=\{\ell\in E':\ell|_N=0\}.
 \tag{3.4}
\]
This is weak-star closed, being an intersection of closed evaluation kernels. The cases \(M=\{0\}\), \(N=E\) and zero seminorms are included. No separability or sequential characterization of weak-star compactness was used. \(\square\)

## 4. Surjectivity through the adjoint

**Lemma 4.1 (complete Fréchet quotients).** If \(N\) is a closed linear subspace of a Fréchet \(E\), then \(E/N\) is Fréchet. For increasing seminorms \(p_j\), its defining seminorms are
\[
 \overline p_j(x+N)=\inf_{n\in N}p_j(x+n).
 \tag{4.1}
\]

*Proof.* These are well-defined increasing seminorms. Their balls are the images of the corresponding open balls of \(p_j\), by the infimum definition. They give the quotient topology and make the quotient map open. Closedness of \(N\) makes the family separate cosets: if \(x\notin N\), one original seminorm ball about \(x\) misses \(N\), so its quotient seminorm is positive.

For a Cauchy sequence of cosets, extract a subsequence \(y_j\) such that \(\overline p_j(y_{j+1}-y_j)<2^{-j}\). Choose representatives \(e_j\) of those differences with \(p_j(e_j)<2^{1-j}\). A representative of \(y_1\) plus \(\sum_je_j\) converges in \(E\), since every fixed seminorm bounds the tail by a summable series. Its coset is the limit of the extracted sequence. The original Cauchy sequence has the same limit by the seminorm triangle inequalities. The quotient is metrizable from the countable separating family, so this proves completeness. \(\square\)

**Theorem 4.2 (adjoint surjectivity criterion).** For a continuous linear \(T:E\to F\) between Fréchet spaces, \(T\) is surjective if and only if its adjoint
\[
 T':F'\to E',\qquad (T'g)(x)=g(Tx),
 \tag{4.2}
\]
is injective and has weak-star closed range.

*Proof, necessity.* Surjectivity gives injectivity of \(T'\). The full Fréchet open-mapping theorem in the linked foundation makes \(T\) open. Every \(\ell\in E'\) annihilating \(\ker T\) defines a well-defined linear \(g\) on \(F\) by \(g(Tx)=\ell(x)\). Choose a neighborhood \(U\) on which \(|\ell|\le1\). Openness makes \(T(U)\) a neighborhood and bounds \(g\) there, so \(g\) is continuous. Thus
\[
 T'(F')=(\ker T)^\perp,
 \tag{4.3}
\]
which is weak-star closed.

*Proof, sufficiency.* Injectivity of \(T'\) makes \(T(E)\) dense: otherwise the linked closed-subspace separation theorem gives a nonzero \(g\in F'\) vanishing on its closure, contradicting injectivity. Put \(N=\ker T\). The weak-star closed linear range has preannihilator \(N\), because the continuous dual of the Hausdorff locally convex \(F\) separates points. Lemma 1.2 therefore gives \(T'(F')=N^\perp\). On the complete quotient \(H=E/N\), the induced \(\widetilde T:H\to F\) is injective, continuous and has dense range, and its adjoint maps onto all of \(H'\).

Fix a defining seminorm \(p_j\) of \(H\). The space
\[
 D_j=\{\ell\in H':\|\ell\|_j
       :=\sup_{p_j(x)\le1}|\ell(x)|<\infty\}
 \tag{4.4}
\]
is Banach: it is the bounded dual of the normed quotient \(H/\ker p_j\), whose dual completeness is proved in the linked operator-space theorem; completeness of that normed quotient is unnecessary. Normed Hahn–Banach gives
\(p_j(x)=\sup_{\|\ell\|_j\le1}|\ell(x)|\).

For increasing defining seminorms \(q_m\) on \(F\), put
\[
 A_m=D_j\cap\widetilde T'(mB_{q_m}).
 \tag{4.5}
\]
Lemma 1.1 and weak-star continuity of the adjoint make \(\widetilde T'(mB_{q_m})\) compact, hence weak-star closed. Norm convergence in \(D_j\) implies pointwise convergence, so \(A_m\) is norm-closed. These sets cover \(D_j\): every functional has a lift in \(F'\), bounded by \(c q_k\), and an integer \(m\ge\max(c,k)\) puts that lift in \(mB_{q_m}\).

If \(D_j=\{0\}\), then \(p_j=0\) and the desired estimate is automatic. Otherwise Baire gives a norm ball \(B(\ell_0,r)\subset A_m\). Subtracting its two lifts shows that every \(h\) with \(\|h\|_j<r\) has a lift \(g\) with \(|g(y)|\le2m q_m(y)\). Rescaling shows that each \(\|\ell\|_j\le1\) has a lift bounded by \((4m/r)q_m\). The dual norm test yields
\[
 p_j(x)\le (4m/r)q_m(\widetilde Tx).
 \tag{4.6}
\]
For every \(j\) there is such a bound. Thus the inverse on the range is continuous. If \(\widetilde Tx_k\) converges in \(F\), (4.6) makes \(x_k\) Cauchy in every seminorm of \(H\). Completeness gives \(x_k\to x\), and continuity gives the limit \(\widetilde Tx\). The range is therefore sequentially closed, hence closed in the metrizable \(F\). Its density makes it all of \(F\). Hence \(T\) is surjective. \(\square\)

## 5. A uniform real bound for entire quotients

Let \(\mu\) be an invertible compact distribution on \(\mathbb R^n\), \(n\ge1\), and put
\[
 A(\zeta)=F_{\check\mu}(\zeta)=F_\mu(-\zeta),\qquad
 F_a(\zeta)=a_x(e^{-ix\cdot\zeta}).
 \tag{5.1}
\]
Reflection preserves the slow-decrease window bounds by replacing both the real center and the complex argument by their negatives. Thus \(\check\mu\) is invertible too, and \(A\not\equiv0\).

**Lemma 5.1 (uniform weighted division).** For every nonempty compact convex \(K\subset\mathbb R^n\) and integer \(N\ge0\), there are \(C<\infty\) and integer \(m\ge0\) such that every entire \(G\) with
\[
 \|G\|_{N,K}=
 \sup_{\zeta\in\mathbb C^n}|A(\zeta)G(\zeta)|
          (1+|\zeta|)^{-N}e^{-H_K(\operatorname{Im}\zeta)}<\infty
 \tag{5.2}
\]
satisfies
\[
 |G(\xi)|\le C\|G\|_{N,K}(1+|\xi|)^m
                 \quad(\xi\in\mathbb R^n).
 \tag{5.3}
\]
The constants depend on \(\mu,N,K\), not on \(G\).

*Proof.* The space in (5.2) is Banach. The local division estimate in the linked analytic-forcing lesson bounds each compact supremum of \(G\) by a compact supremum of \(AG\), hence by a constant times this norm. The weight and its reciprocal are bounded on that compact set. A norm-Cauchy sequence converges locally uniformly to an entire \(G\). Passing to the pointwise limit in its weighted norm inequality, then taking the supremum, proves norm convergence and finiteness of the limit's norm. Nondegeneracy follows because \(A\) is nonzero on an open set and the identity theorem determines \(G\). The exact polynomial factor is retained throughout.

The product \(AG\) obeys the compact Fourier growth criterion with this fixed \(K,N\), so it is a compact-distribution transform by Theorem CF2.1. The entire-division characterization of invertibility for \(\check\mu\) makes \(G\) a compact-distribution transform too. It therefore has some polynomial growth on real frequencies.

On the complete space in (5.2), the sets
\[
 D_j=\{G:|G(\xi)|\le j(1+|\xi|)^j
                     \text{ for every real }\xi\},\qquad j\ge1,
 \tag{5.4}
\]
are closed by evaluation continuity and cover the space. Baire gives \(B(G_0,r)\subset D_j\). Subtracting the bounds at \(G_0+H\) and \(G_0\) gives \(|H(\xi)|\le2j(1+|\xi|)^j\) for \(\|H\|_{N,K}<r\). Scaling \(H=rG/(2\|G\|_{N,K})\) gives (5.3) with \(m=j\), \(C=4j/r\). The zero space and zero quotient are immediate. \(\square\)

## 6. Compact duals and continuity of convolution

Let \(X_1,X_2\) be nonempty open sets with
\[
 X_2-\operatorname{supp}\mu\subset X_1.
 \tag{6.1}
\]
The linked smooth-space completeness theorem makes \(E=C^\infty(X_1)\), \(F=C^\infty(X_2)\) Fréchet. Their continuous duals are \(\mathcal E'(X_1)\), \(\mathcal E'(X_2)\).

Here is the exact dual identification. A continuous functional on \(C^\infty(X)\) is bounded by
\[
 |\ell(h)|\le C\max_{|\alpha|\le N}\sup_K|\partial^\alpha h|
 \tag{6.2}
\]
for one compact \(K\subset X\), after taking a finite union of the observation compacts. Its restriction to compact tests is a distribution supported in \(K\). Inserting a cutoff equal to one near \(K\) leaves every value unchanged, because the difference has zero displayed seminorm. Thus it is the compact distributional action on all smooth functions near that support. Conversely a compact distribution has a finite-order bound on a compact neighborhood of its support inside \(X\), making its action continuous on \(C^\infty(X)\). Convexity is unnecessary.

Convolution is a continuous linear map
\[
 T:C^\infty(X_1)\to C^\infty(X_2),\qquad Tu=\mu*u.
 \tag{6.3}
\]
For compact \(Q\subset X_2\), the whole set \(Q-\operatorname{supp}\mu\) is compact inside \(X_1\). Choose a fixed small neighborhood of the kernel support whose differences with \(Q\) still lie in one compact neighborhood \(L\subset X_1\), and insert one cutoff there. Finite order \(r\) of \(\mu\), Leibniz's rule and differentiation under its pairing give
\[
 \max_{|\alpha|\le k}\sup_Q|\partial^\alpha(\mu*u)|
       \le C_Q\max_{|\beta|\le k+r}\sup_L|\partial^\beta u|.
 \tag{6.4}
\]
These are the actual seminorm bounds for continuity.

The bilinear adjoint is
\[
 T'\phi=\check\mu*\phi,\qquad \phi\in\mathcal E'(X_2).
 \tag{6.5}
\]
Its image support lies in \(\operatorname{supp}\phi-\operatorname{supp}\mu\subset X_1\). For nonzero \(\mu\), compact convolution injectivity makes \(T'\) injective: the transforms of nonzero compact factors are nonzero entire functions, and their product cannot vanish identically. The exact ordinary-support theorem gives the same conclusion.

## 7. Compact inverse polars from Fourier division

**Lemma 7.1.** Suppose \(\mu\) is invertible and the pair in (6.1) is \(\mu\)-convex for supports. For every basic neighborhood
\[
 U=\{u\in C^\infty(X_1):
          q_{K_1,N}(u):=\max_{|\alpha|\le N}
                          \sup_{K_1}|\partial^\alpha u|<1\},
 \tag{7.1}
\]
the set \(U^\circ\cap T'(F')\) is weak-star compact.

*Proof.* Each \(\psi\in U^\circ\) obeys
\[
 |\psi(u)|\le q_{K_1,N}(u),\qquad
                \operatorname{supp}\psi\subset K_1.
 \tag{7.2}
\]
Scaling gives the bound for a positive seminorm; arbitrarily large scalar multiples give vanishing for seminorm zero, and also the support inclusion. Put
\[
 \Phi=\{\phi\in\mathcal E'(X_2):T'\phi\in U^\circ\}.
 \tag{7.3}
\]
Distributional confinement in the linked support-distance criterion gives one compact \(K_2\subset X_2\) containing every support in \(\Phi\). If \(K_1\) or \(K_2\) is empty, only the zero inverse remains and the assertion follows. Assume both are nonempty.

Evaluate (7.2) on the exponential, with a cutoff constant near \(K_1\):
\[
 |F_\psi(\zeta)|\le
     (1+|\zeta|)^N e^{H_{K_1}(\operatorname{Im}\zeta)}.
 \tag{7.4}
\]
The cutoff derivatives vanish on \(K_1\), so no enlarged support enters this bound. Replace \(K_1\) by its compact convex hull in the support function. That hull need not lie inside a nonconvex \(X_1\); only the entire growth bound uses it.

Since \(F_\psi=A F_\phi\), Lemma 5.1 gives uniformly
\[
 |F_\phi(\xi)|\le C(1+|\xi|)^m\quad(\phi\in\Phi).
 \tag{7.5}
\]
Choose a fixed \(\chi\in C_c^\infty(X_2)\) equal to one near \(K_2\), with compact support \(L_2\). For \(h\in C^\infty(X_2)\), extend \(\chi h\) by zero to the real space. For an integer \(s\) with \(2s>m+n\), integration by parts gives
\[
 |F_{\chi h}(-\xi)|\le C_\chi(1+|\xi|^2)^{-s}
          \max_{|\alpha|\le2s}\sup_{L_2}|\partial^\alpha h|.
 \tag{7.6}
\]
Indeed \((1+|\xi|^2)^sF_{\chi h}=F_{(1-\Delta)^s(\chi h)}\). The right side's \(L^1\) norm is bounded by a fixed finite box volume, cutoff derivative constants and the finite Leibniz coefficients.

Schwartz inversion, with finite-order uniform interchange in the compact distributional pairing, yields
\[
 \begin{aligned}
 |\phi(h)|
 &\le (2\pi)^{-n}C
           \int(1+|\xi|)^m|F_{\chi h}(-\xi)|\,d\xi\\
 &\le B\max_{|\alpha|\le2s}
                       \sup_{L_2}|\partial^\alpha h|.
 \end{aligned}
 \tag{7.7}
\]
The integral of \((1+|\xi|)^m(1+|\xi|^2)^{-s}\) is finite since \(2s>m+n\). Thus \(\Phi\) lies in one seminorm polar \(V^\circ\) of \(F\), compact by Lemma 1.1.

The adjoint is weak-star continuous, because evaluation of \(T'\phi\) at \(u\) is evaluation of \(\phi\) at the fixed \(Tu\). Since \(U^\circ\) is closed, \(\Phi=(T')^{-1}(U^\circ)\) is closed. It is a closed subset of the compact \(V^\circ\), hence compact. Its continuous image is exactly
\[
 T'\Phi=U^\circ\cap T'(F'),
 \tag{7.8}
\]
proving the lemma. \(\square\)

## 8. The exact smooth solvability equivalence

**Theorem 8.1.** For a compact distribution \(\mu\) and nonempty open domains satisfying (6.1), these conditions are equivalent:

1. Every \(f\in C^\infty(X_2)\) has \(u\in C^\infty(X_1)\) with \(\mu*u=f\) on \(X_2\).
2. Every \(f\in C^\infty(X_2)\) has \(u\in\mathcal D'(X_1)\) with \(\mu*u=f\) on \(X_2\).
3. The kernel is invertible and \((X_1,X_2)\) is \(\mu\)-convex for supports.

The forcing is smooth in both solution statements. Arbitrary distributional forcing requires additional singular-support geometry.

*Proof.* The zero kernel makes all three conditions false: nonempty \(X_2\) has nonzero smooth functions, and zero is not invertible. For nonzero \(\mu\), condition 1 implies condition 2 by the regular-distribution inclusion.

Condition 2 implies invertibility by Theorem 1.1 of Smooth forcing, invertible kernels and support confinement. Its Theorem 5.1 gives confinement, and the linked support-distance equivalence gives \(\mu\)-convexity. Thus condition 3 follows.

Assume condition 3. The operator (6.3) is continuous between Fréchet spaces and its adjoint is injective. Lemma 7.1 makes every basic polar section of its dual range compact, hence closed. For any other neighborhood \(U\), choose a basic \(U_0\subset U\). Then
\[
 U^\circ\cap T'(F')
       =U^\circ\cap\bigl(U_0^\circ\cap T'(F')\bigr)
 \tag{8.1}
\]
is closed, since the basic section is compact and \(U^\circ\) is closed. Theorem 3.1 makes the entire dual range weak-star closed; Theorem 4.2 makes \(T\) surjective. This proves condition 1 for every smooth forcing and completes the equivalence on arbitrary compatible open domains. \(\square\)

## References

- Terence Tao, “245B, Notes 9: The Baire category theorem and its Banach space consequences,” 2009, freely readable [notes](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/).
- Gerd Grubb, *Distributions and Operators*, Chapter 5, “Fourier transformation of distributions,” freely readable [lecture notes](https://web.math.ku.dk/~grubb/dist5.pdf).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
- The normed Hahn–Banach, Baire and Fréchet open-mapping proofs and exact Fourier/support inputs are the internal lessons linked above. The arbitrary polar compactness, bipolar receiver, summable lifting, polar-section theorem, quotient completeness, adjoint criterion and uniform convolution estimate are proved here.
