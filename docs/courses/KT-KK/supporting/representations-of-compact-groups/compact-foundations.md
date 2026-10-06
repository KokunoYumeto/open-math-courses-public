# Foundations for compact-group averaging and coefficient approximation

*Written and self-checked by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Independently written proof companion; no separate review or formal verification is claimed. Original expression: public domain (CC0). Zorn's maximality principle is a declared set-theoretic axiom. The mathematical structures are over the complete real field and its complexification.*

This companion proves the analysis used in compact-group averaging and coefficient approximation. All statements retain compact Hausdorff spaces and arbitrary Hilbert spaces. No countable basis for the compact space or the Hilbert space is imposed. The free Gruson–Serganova author draft is a comparison source for compact representations; its omitted general Haar proof is supplied below. The continuous Banach and strict Hilbert-module integrals are constructed in CPT-F-010. The full Lie-group exponential and closed-subgroup background used in the compact-group and Lie arguments is proved in the separate [Lie companion](compact-lie-foundations.md).

<a id="cpt-f-001"></a>
## CPT-F-001 — Polynomial and algebra approximation

For a continuous real function \(f\) on \([0,1]\), its Bernstein polynomial is
\[
B_nf(t)=\sum_{k=0}^n f(k/n)\binom nk t^k(1-t)^{n-k}.
\]
The binomial weights sum to one. Differentiating \((a+b)^n\) once and twice and setting \(a=t,b=1-t\) gives their mean \(t\) and variance \(t(1-t)/n\). Consequently the sum of the weights with \(|k/n-t|\geq\delta\) is at most \(1/(4n\delta^2)\). Uniform continuity gives
\[
\|B_nf-f\|_\infty\leq\varepsilon+
 2\|f\|_\infty/(4n\delta^2)
\]
after choosing \(\delta\) so that the oscillation within \(\delta\) is below \(\varepsilon\). Thus polynomials approximate every continuous function uniformly, including the absolute-value function on a bounded real interval after affine rescaling. Uniform continuity here follows directly from compactness: choose for each point a neighbourhood on which the oscillation is small, take a finite subcover, and use the Lebesgue-number argument on the compact interval. Its proof is to assume no such number exists, choose intervals of lengths tending to zero that violate it, and extract a convergent sequence of their centres; an open member containing the limit gives the contradiction.

Let \(A\subset C(X,\mathbb R)\) be a unital algebra separating the points of a compact Hausdorff space. Its uniform closure \(\overline A\) is still an algebra: uniformly convergent sequences are uniformly bounded, so products converge uniformly. Polynomial approximation of \(|t|\) on \([-\|h\|_\infty,\|h\|_\infty]\) shows that \(|h|\in\overline A\) whenever \(h\in\overline A\). Hence maxima and minima of two elements belong to \(\overline A\), by \(\max(h,k)=(h+k+|h-k|)/2\) and the corresponding minus sign for the minimum.

Fix \(f\in C(X,\mathbb R)\) and \(\varepsilon>0\). For each \(x,y\in X\), separation and affine rescaling give \(h_{xy}\in A\) with values \(f(x),f(y)\) at those two points; use a constant if \(x=y\). For fixed \(x\), the sets on which \(h_{xy}>f-\varepsilon\) cover \(X\). A finite subcover and their maximum give \(h_x\in\overline A\), with \(h_x>f-\varepsilon\) everywhere and \(h_x(x)=f(x)\). The sets on which \(h_x<f+\varepsilon\) also cover \(X\). Their finite subcover and the minimum of the corresponding \(h_x\)'s give \(h\in\overline A\) with \(f-\varepsilon<h<f+\varepsilon\). Thus \(\overline A=C(X,\mathbb R)\). For a conjugation-closed complex algebra, real and imaginary parts belong to it and its real-valued part separates points; applying the real conclusion to both parts proves the complex Stone–Weierstrass theorem.

In particular, finite sums of products \(a(x)b(y)\) are uniformly dense in \(C(X\times Y)\): their algebra is unital and conjugation closed, and continuous functions separate points by CPT-F-002 below. This product conclusion requires no metrizability.

<a id="cpt-f-002"></a>
## CPT-F-002 — Normality, cutoffs and finite partitions

A compact subset of a Hausdorff space is closed: for a point outside it, separate that point from each of its points by disjoint open sets and take a finite subcover on the compact side. In a compact Hausdorff space, two disjoint closed sets \(K,L\) have disjoint open neighbourhoods. For each \(x\in K\), use the preceding finite-subcover argument to obtain an open \(U_x\) around \(x\) whose closure misses \(L\); a finite union of such \(U_x\)'s covers \(K\) and has closure missing \(L\). This also proves the shrinking property: if \(K\subset U\), with \(K\) closed and \(U\) open, there is open \(V\) with \(K\subset V\subset\overline V\subset U\).

Repeated shrinking constructs open sets \(U_r\), indexed by dyadic rationals \(0<r<1\), with \(K\subset U_r\), \(\overline U_r\subset U_s\) for \(r<s\), and \(\overline U_r\subset U\). Start with one shrunk neighbourhood, insert one between each pair at the next dyadic level, and continue. Set
\(q(x)=\inf(\{r:x\in U_r\}\cup\{1\})\).
Then \(q=0\) on \(K\), \(q=1\) outside \(U\), and it is continuous: \(\{q<a\}=\bigcup_{r<a}U_r\) and \(\{q>a\}=\bigcup_{r>a}(X\setminus\overline U_r)\). Thus \(1-q\) is a continuous cutoff equal to one on \(K\) and zero outside \(U\). Shrink once more before this construction when its support must be contained in \(U\). Taking \(K\) to be one point and \(U\) to miss a second proves point separation.

A finite open cover \((U_i)\) of a compact set has a finite partition of unity near that set, with supports in the \(U_i\)'s. Indeed, finitely many shrunk neighbourhoods have closed closures \(K_j\) covering the set, with \(K_j\subset U_{i(j)}\). Choose cutoffs \(v_j=1\) on \(K_j\), supported in \(U_{i(j)}\). Their sum is positive near the set; divide by that sum there. When a partition on all of \(X\) is needed, add a cutoff for its remaining complement before normalizing. A function supported in the original compact set can be decomposed using this partition, with no contribution from the extra cutoff. All sums are finite.

<a id="cpt-f-003"></a>
## CPT-F-003 — A positive functional gives a Radon measure

Let \(I:C(X,\mathbb R)\to\mathbb R\) be positive and linear, with \(I(1)=1\). Positivity implies \(|I(f)|\leq\|f\|_\infty\). For open \(U\), define
\[
v(U)=\sup\{I(f):0\leq f\leq1,\ \operatorname{supp}f\subset U\},
\qquad
\mu^*(A)=\inf_{U\supset A,\ U\text{ open}}v(U).
\]
The empty supremum is zero. Open-set monotonicity is immediate. If \(U\subset\bigcup_jU_j\), each test function's compact support has a finite subcover; CPT-F-002 splits that test function into nonnegative functions supported in the corresponding \(U_j\)'s. Their functional values give \(v(U)\leq\sum_jv(U_j)\). For disjoint open sets, test functions with these disjoint supports can be added and remain at most one, giving the reverse inequality for every finite subcollection. Thus \(v\) is countably additive on disjoint opens whose union is open. Choosing open covers within any prescribed error proves that \(\mu^*\) is an outer measure. Also \(\mu^*(U)=v(U)\) for open \(U\).

For open \(U\),
\[
v(U)=\sup_{K\subset U,\ K\text{ compact}}\mu^*(K).
\tag{F3.1}
\]
The inequality from right to left is monotonicity. In the other direction, the support \(K\) of a test function \(f\) is compact. For every open \(V\supset K\), the same \(f\) is an allowed test, so \(I(f)\leq v(V)\) and hence \(I(f)\leq\mu^*(K)\). Take the supremum of the tests.

Every closed set \(F\) is measurable for this outer measure. Given an open \(U\supset A\), choose compact \(K\subset U\setminus F\) with \(\mu^*(K)>v(U\setminus F)-\varepsilon\), using (F3.1). Separate \(K\) and \(F\) by disjoint open neighbourhoods \(W,V\). Disjoint-open additivity and monotonicity give
\[
v(U)\geq v(U\cap V)+v(U\cap W)
\geq\mu^*(A\cap F)+\mu^*(K)
\geq\mu^*(A\cap F)+\mu^*(A\setminus F)-\varepsilon.
\]
Infimize over \(U\) and let \(\varepsilon\downarrow0\). The opposite inequality is outer subadditivity, proving the measurable-set splitting identity. The sets satisfying that identity form a sigma algebra: complements preserve the identity; successive splitting gives finite disjoint additivity; apply those splittings to the first \(n\) members of a disjoint sequence and let \(n\) increase, using outer subadditivity for the reverse bound. General countable unions reduce to disjoint ones by successive differences. Hence all Borel sets are measurable and \(\mu=\mu^*\) restricted to them is a measure. It is outer regular by definition. Since \(\mu(X)=1\), outer approximation of a Borel set's complement gives inner approximation of that set by closed, hence compact sets. Thus \(\mu\) is Radon.

To check the representing identity, take \(0\leq f\leq M\), \(\delta=M/N\), and
\(g_j=\min(1,\max(0,f/\delta-j))\), \(0\leq j<N\).
Their sum times \(\delta\) is exactly \(f\). If a continuous \(g\) is between zero and one, equals one on a closed \(K\), and vanishes off open \(U\), then
\[
\mu(K)\leq I(g)\leq\mu(U).
\]
For the first bound, \(V=\{g>1-\eta\}\) contains \(K\); every test \(h\) supported in \(V\) satisfies \((1-\eta)h\leq g\), so \((1-\eta)\mu(K)\leq I(g)\). Let \(\eta\) tend to zero. For the second, the functions \((g-\eta)_+\) have compact supports in \(U\), are bounded by one, and converge uniformly to \(g\). Apply this to the level-set cutoffs \(g_j\). The lower and upper step sums built from \(\mu(\{f\geq(j+1)\delta\})\) and \(\mu(\{f>j\delta\})\) bound both \(I(f)\) and \(\int f\,d\mu\); their difference is at most \(\delta\), because the corresponding step functions differ pointwise by at most \(\delta\). Let \(N\to\infty\), and then use linearity and real/imaginary parts. Therefore \(I(f)=\int f\,d\mu\).

Any Radon measure representing \(I\) has the same value on every open set: inner regularity and CPT-F-002 give the displayed supremum of continuous tests. Outer regularity then gives equality on Borel sets. This proves uniqueness. The same construction, after multiplying by \(I(1)\), covers finite positive functionals; the zero functional gives the zero measure.

<a id="cpt-f-004"></a>
## CPT-F-004 — Integration, product measure and continuous density

The integral of a nonnegative measurable function is the supremum of the integrals of nonnegative simple functions below it. If \(f_n\uparrow f\), any simple \(s\leq f\) and \(0<c<1\) satisfy \(f_n\geq cs\) eventually at each point where \(s>0\). Continuity of measure from below follows by decomposing an increasing union into disjoint differences. Applying it to the finitely many positive levels of \(s\) gives \(\lim\int f_n\geq c\int s\). Supremize over \(s\) and then let \(c\uparrow1\). This proves monotone convergence. Applying it to \(\inf_{n\geq m}f_n\) proves Fatou's inequality. If \(|f_n|\leq g\), \(\int g<\infty\), and \(f_n\to f\) pointwise, apply Fatou to \(2g-|f_n-f|\); the integrals of the nonnegative difference tend to zero. This proves dominated convergence, for complex functions by the same absolute-value estimate. The integral triangle inequality follows first for simple functions and then by these limits.

For a finite Radon measure on compact \(X\), continuous functions are dense in \(L^p\), \(1\leq p<\infty\). For a Borel set \(B\), choose compact \(K\subset B\subset U\) open with \(\mu(U\setminus K)<\varepsilon\); CPT-F-002 supplies \(0\leq h\leq1\) equal to one on \(K\) and supported in \(U\). Then \(\|h-1_B\|_p^p<\varepsilon\). Measurable functions are approximated by bounded simple functions: truncate their absolute value, subdivide their bounded real and imaginary ranges, and use dominated convergence for the discarded integrable tails. Completed-measure functions have Borel representatives, since each completed measurable level set differs from a Borel set by a subset of a Borel null set; the same simple approximations give a Borel representative outside their countable union of null sets. Thus this density statement also holds for the completion.

For finite Radon measures \(\mu,\nu\) on compact \(X,Y\), the positive functional
\[
f\longmapsto\int_X\left(\int_Yf(x,y)\,d\nu(y)\right)d\mu(x),
\qquad f\in C(X\times Y),
\]
defines their Radon product by CPT-F-003. The inner integral is continuous: a finite-cover argument bounds its change by the uniform change of \(f\) in its first variable. CPT-F-001 approximates \(f\) uniformly by finite sums \(a(x)b(y)\). The two orders of integration agree on these sums, and the integral bound passes equality to \(f\).

Here are the measurable extensions needed for scalar Fubini. For open \(U\subset X\times Y\), its section-volume function \(q_U(x)=\nu(U_x)\) is lower semicontinuous. If \(q_U(x)>a\), inner regularity chooses a compact \(K\subset U_x\) with \(\nu(K)>a\); finitely many product neighbourhoods give a neighbourhood of \(x\) where this same \(K\) remains inside the sections. Further,
\[
\int q_U\,d\mu=\mu\times\nu(U).
\tag{F4.1}
\]
To verify it without an uncountable monotone-convergence assertion, observe that for any directed family of continuous nonnegative functions with lower semicontinuous supremum \(q\), the integral of \(q\) is the supremum of their integrals. For each positive level \(a\) and compact subset of \(\{q>a\}\), finitely many family members cover it by their \(>a\) sets; directedness gives one member exceeding \(a\) on that compact set. Use finitely many levels of a lower step approximation to \(q\), inner regularity at each level, and one further common upper member. This proves the stated supremum identity. Apply it to the functions \(x\mapsto\int h(x,y)d\nu(y)\), where \(0\leq h\leq1\) is continuous and supported in \(U\). CPT-F-002, applied to compact subsets of a section, makes their supremum \(q_U\). Their product integrals have supremum \(\mu\times\nu(U)\), giving (F4.1).

A product-null Borel set \(N\) lies inside opens \(U_n\) of product measure below \(2^{-n}\). Equation (F4.1) and monotone convergence show that \(\sum_nq_{U_n}(x)<\infty\) for almost every \(x\). Hence \(\nu(N_x)=0\) almost everywhere. For any product-integrable Borel \(f\), choose continuous \(f_n\) with \(\sum_n\|f_n-f\|_1<\infty\), by continuous density. A subsequence of the summable approximation converges to \(f\) outside a product-null set: the integral of \(\sum_n|f_n-f|\) is finite by monotone convergence. The continuous differences also have summable section \(L^1\) norms for almost every \(x\), by continuous Fubini and monotone convergence. For those \(x\), the sections converge in \(L^1(Y)\) and pointwise to \(f_x\), using the null-section result. The integral triangle inequality bounds the resulting integral functions' \(L^1(X)\) differences by the product \(L^1\) differences. Passing to the limit proves Fubini, both orders, with absolutely integrable sections almost everywhere. Completing either measure does not change the assertion after choosing a Borel representative.

For later \(L^2\) use, scalar Cauchy–Schwarz follows by expanding \(\int|f-tg|^2\geq0\) and minimizing in \(t\). It proves the triangle inequality for the \(L^2\) norm. Completeness follows from a Cauchy sequence by taking a subsequence with successive norm differences summing to a finite number. The partial sums of the absolute differences have bounded \(L^2\) norms by the triangle inequality; Fatou shows that their pointwise sum is finite almost everywhere and in \(L^2\). The subsequence therefore has a pointwise limit and converges in \(L^2\) by the tail bound and Fatou. The original Cauchy sequence has the same norm limit. Thus \(L^2\) is a Hilbert space.

<a id="cpt-f-005"></a>
## CPT-F-005 — Haar measure on every compact Hausdorff group

For nonnegative continuous \(f\) and nonzero nonnegative continuous \(g\) on a compact group, put
\[
(f:g)=\inf\left\{\sum_{i=1}^Nc_i:
 f(x)\leq\sum_{i=1}^Nc_i g(x_i^{-1}x),\ c_i>0\right\},
\qquad J_g(f)=(f:g)/(1:g).
\]
Finite translates of \(\{g>0\}\) cover the group. Their sum has a positive minimum, so the infimum is finite. Also \((1:g)\geq1/\|g\|_\infty>0\). Directly from the definition, \(J_g\) is monotone, positively homogeneous, subadditive, left invariant, and \(J_g(1)=1\). Consequently \(0\leq J_g(f)\leq\|f\|_\infty\) and \(|J_g(f+\varepsilon)-J_g(f)|\leq\varepsilon\).

Choose \(g_U\) supported in each identity neighbourhood \(U\), with \(g_U(e)=1\), using CPT-F-002. Shrinking neighbourhoods form a directed set. Extend its tail filter to an ultrafilter by Zorn: order proper filters containing the tails by inclusion, take chain unions, and use maximality. An ultrafilter decides every subset, since adjoining any undecided set would otherwise give a larger proper filter. Each bounded real family has a unique limit along it. Bisect a closed interval containing the values and choose a half whose inverse image belongs to the ultrafilter; nested bisection and real completeness give the limit. Uniqueness follows from disjoint neighbourhoods. Define \(I(f)=\lim J_{g_U}(f)\) for each nonnegative \(f\).

We verify additivity, which is the substantive step. First take \(f_1+f_2>0\) and \(h=f_1/(f_1+f_2)\). For any \(\eta>0\), there is an identity neighbourhood \(U\) with \(|h(xu)-h(x)|<\eta\) for all \(x\in G,u\in U\). This follows from continuity on the compact set \(G\times\{e\}\), choosing finitely many product neighbourhoods and intersecting their identity factors. In a covering sum for \(f_1+f_2\) by translates of \(g_U\), replace \(c_i\) by \(c_i(h(x_i)+\eta)\) to dominate \(f_1\), and by \(c_i(1-h(x_i)+\eta)\) to dominate \(f_2\). Only points in \(x_iU\) contribute. Therefore
\[
J_{g_U}(f_1+f_2)\leq J_{g_U}(f_1)+J_{g_U}(f_2)
\leq(1+2\eta)J_{g_U}(f_1+f_2).
\]
Infima are handled by choosing covering sums arbitrarily close to their infimum. Pass to the ultrafilter limit and let \(\eta\downarrow0\). For general nonnegative \(f_i\), add \(\varepsilon\) to each, apply the strictly positive case, and use the preceding \(\varepsilon\) bound before letting \(\varepsilon\downarrow0\). Thus \(I\) is additive. Extend it to real functions by differences of nonnegative functions; additivity makes this independent of the decomposition. Complexification gives a positive unital left-invariant functional on \(C(G)\). CPT-F-003 supplies a left-invariant Radon probability measure: uniqueness of that representation transfers functional invariance to measure invariance.

Inversion transfers any left-invariant probability to a right-invariant one. Let \(\mu\) be left invariant and \(\nu\) right invariant. For continuous \(f\), Fubini from CPT-F-004 applied to \(f(yx)\) gives
\[
\int\!\int f(yx)\,d\mu(x)d\nu(y)
=\int f\,d\mu=\int f\,d\nu.
\]
The first evaluation uses left invariance in \(x\), the second right invariance in \(y\). Radon uniqueness gives \(\mu=\nu\). Taking \(\nu\) to be the inverse image of \(\mu\) proves that \(\mu\) is also right invariant. Taking any other left-invariant probability in the same comparison proves uniqueness. Finally, any nonempty open \(O\) has finitely many left translates covering \(G\); invariance gives \(1\leq N\mu(O)\), so \(\mu(O)>0\). The one-point group is included.

<a id="cpt-f-006"></a>
## CPT-F-006 — Hilbert projections, bases and their cardinality

For a closed subspace \(M\subset H\) and \(x\in H\), choose \(m_n\in M\) with \(\|x-m_n\|^2\to d^2\), the distance infimum. The parallelogram identity gives
\[
\|m_n-m_k\|^2\leq
2\|x-m_n\|^2+2\|x-m_k\|^2-4d^2.
\]
Completeness and closedness give a limit \(m\in M\) attaining the distance. Minimizing \(\|x-m-tz\|^2\) for real and purely imaginary \(t\), with \(z\in M\), gives \(x-m\perp M\). This also proves uniqueness, linearity of \(P_Mx=m\), and \(\|P_M\|\leq1\).

Finite orthonormal vectors give \(\|x\|^2=\sum|\langle x,e_j\rangle|^2+\|x-\sum\langle x,e_j\rangle e_j\|^2\). This proves Bessel's inequality. Zorn applied to orthonormal sets gives a maximal one \(E\); if its closed span were proper, the projection construction would give a nonzero vector perpendicular to it, contradicting maximality. Each vector's coefficients have countable support, since only finitely many can have size at least \(1/n\). Finite coefficient sums are Cauchy by Bessel, and their remainder is perpendicular to every element of \(E\), hence zero. This proves Parseval and the expansion on an arbitrary Hilbert space.

Two infinite orthonormal bases \(E,F\) have the same cardinality. Each \(e\in E\) has countable support in \(F\); their union must be all of \(F\), since a missing vector would be perpendicular to the dense span of \(E\). Thus \(|F|\leq|E|\cdot\aleph_0=|E|\); the reverse bound is identical and the two injections give a bijection. The cardinal identity follows by well-ordering the infinite set and the usual transfinite enumeration of pairs by their maximum coordinate; for a countable set it is diagonal enumeration. For finite bases, mutual spanning and elimination give the two dimension inequalities. A finite basis cannot coexist with an infinite orthonormal set by Bessel applied to the finite basis and summing its coordinate squares. These observations prove the finite and mixed cases too.

A bounded linear functional \(l\ne0\) has a closed kernel. Choose \(u\) with \(l(u)\ne0\), and put \(w=u-P_{\ker l}u\). Then \(w\ne0\) and \(x-l(x)w/l(w)\in\ker l\), so
\(l(x)=l(w)\langle x,w\rangle/\|w\|^2\).
This proves the Hilbert representation of functionals. Applied to \(x\mapsto\langle Tx,y\rangle\), it constructs \(T^*\), with the usual adjoint identity and norm bound, without separability.

<a id="cpt-f-007"></a>
## CPT-F-007 — Compact spectral theory and finite square roots

For a positive compact \(K\), positivity of its scalar quadratic form gives
\(|\langle Kx,y\rangle|^2\leq\langle Kx,x\rangle\langle Ky,y\rangle\), by minimizing in the scalar coefficient. Put \(a=\sup_{\|x\|=1}\langle Kx,x\rangle\). Taking the supremum over unit \(y\) gives \(\|Kx\|^2\leq a\langle Kx,x\rangle\), whence \(a=\|K\|\). If \(a>0\), choose unit \(x_n\) approaching that supremum. Then
\[
\|(K-a)x_n\|^2\leq a^2-a\langle Kx_n,x_n\rangle\longrightarrow0.
\]
Compactness gives a convergent subsequence of \(Kx_n\), and therefore a convergent subsequence of \(x_n\), whose unit limit is an \(a\)-eigenvector. Its eigenspace is finite dimensional: infinitely many orthonormal vectors there would have images separated by \(\sqrt2a\), contradicting compactness. Split off the full maximum eigenspace and repeat on the invariant orthogonal complement. If there are infinitely many stages, their eigenvalues tend to zero by the same separated-image argument. A nonzero remaining restriction would have a positive maximum eigenvalue bounded above by every previously selected one, a contradiction. The remaining space is \(\ker K\). CPT-F-006 supplies its basis. This proves the positive compact decomposition on arbitrary \(H\).

For compact self-adjoint \(A\), \(A^2\) is positive compact. Its positive eigenspaces are finite dimensional and invariant under \(A\); diagonalize \(A\) on each. The kernel of \(A^2\) is the kernel of \(A\), since \(\langle A^2x,x\rangle=\|Ax\|^2\). To justify the finite diagonalization just used, maximize the real quadratic form of a self-adjoint matrix on its compact unit sphere. Differentiation in every orthogonal real and imaginary direction makes the maximizing vector an eigenvector. Its orthogonal complement is invariant; induction gives an orthonormal eigenbasis. Compactness of this sphere follows from successive convergent coordinate subsequences in a bounded finite-dimensional set, or equivalently the nested-box proof of finite-dimensional compactness. This proof also constructs the positive square root of a positive matrix by replacing each nonnegative eigenvalue \(\lambda\) by \(\sqrt\lambda\); it is invertible for a positive definite matrix.

The general bounded Borel spectral theorem for bounded selfadjoint operators has an existing programme proof in [Positive spectral calculus](../NCG-LOCAL-INDEX/dependencies/AN-03/lower-bounded-spectral-calculus.md#AN03-SPC-003), AN03-SPC-001–003, under its displayed independent programme source notice. For a bounded self-adjoint \(A\ne0\), take \(c=\|A\|\) and \(S=(A+2cI)/(3c)\). This is a positive injective contraction, because \(\langle(A+2cI)x,x\rangle\geq c\|x\|^2\). The affine inverse \(\lambda=3ct-2c\) transfers its proved PVM to \(A\). For \(A=0\), use the identity mass at zero. An operator commuting with \(A\) commutes with every continuous polynomial limit; the scalar-measure uniqueness and bounded-Borel extension in that same proof then give commutation with all spectral projections. A nonscalar self-adjoint \(A\) must have a nontrivial spectral projection: if every projection were zero or identity, the associated scalar probability would be a point mass (bisect its bounded interval repeatedly, retaining the half with identity projection), and the integral would be scalar. This is precisely the implication needed in Schur's lemma.

<a id="cpt-f-008"></a>
## CPT-F-008 — Translation and scalar separation

For \(f\in C(G)\), compactness and continuity of \((g,x)\mapsto f(g^{-1}x)\) imply \(\|L_gf-f\|_\infty\to0\): take finitely many product neighbourhoods at \((e,x)\) and intersect their identity factors. The same proof applies to \(f(xg)\). Haar invariance gives norm-one translations on every \(L^p\). CPT-F-004 gives continuous density, so
\[
\|L_gu-u\|_p\leq2\|u-f\|_p+\|L_gf-f\|_p
\]
proves translation continuity for every \(u\in L^p\), \(1\leq p<\infty\). This is a neighbourhood-limit statement, not a sequence-limit statement.

Let \(V\ne0\) be Hausdorff locally convex and choose \(v\ne0\). Its defining continuous seminorms separate points, so some \(p(v)>0\). The quotient \(V/\ker p\), with norm \(p\), is a normed space; its quotient map is continuous because \(p\) is. Define \(l(z[v])=zp(v)\) on the line through \([v]\). The complex norm-preserving extension proved in [Banach foundations](../NCG-LOCAL-INDEX/dependencies/AN-03/banach-foundation-bridges.md#section-5), Section 5, extends \(l\) to that normed space. Composing with the quotient gives a nonzero continuous complex functional on \(V\). No Banach completeness is imposed on \(V\).

<a id="cpt-f-009"></a>
## CPT-F-009 — Real-line and circle characters

Let \(\chi:\mathbb R\to\mathbb T\) be continuous and multiplicative. Near zero it has a unique continuous argument \(a(x)\in(-\pi/3,\pi/3)\), with \(a(0)=0\): on this arc, cosine and sine parametrize a continuous inverse angle, for example through arctangent of the imaginary part divided by the positive real part. On a sufficiently small symmetric interval, \(a(x+y)=a(x)+a(y)\) whenever \(x,y,x+y\) are in that interval, because their difference is a multiple of \(2\pi\) with absolute value below \(\pi\). Extend this to an additive function on \(\mathbb R\) by \(A(x)=n a(x/n)\), with \(n\) large enough. Repeated local additivity and a common refinement \(mn\) prove independence of \(n\). The same common refinement proves global additivity. Continuity near zero gives continuity everywhere. Additivity first gives \(A(q)=qA(1)\) for rational \(q\), and rational approximation then gives \(A(x)=cx\) for every real \(x\). Also \(\chi(x)=\chi(x/n)^n=e^{iA(x)}\). The coefficient \(c\) is unique, since \(e^{i(c-c')x}=1\) for all sufficiently small real \(x\) forces \(c=c'\).

For a circle character in the angle convention \(\mathbb T=\mathbb R/2\pi\mathbb Z\), compose with the quotient map. The preceding result gives \(e^{ic\theta}\), and the quotient condition \(e^{2\pi ic}=1\) forces \(c\in\mathbb Z\). Conversely each integer gives a continuous circle character. The normalized measure \(d\theta/(2\pi)\) is translation invariant by the periodic change-of-variable calculation on intervals, hence is the Haar measure by CPT-F-005's uniqueness. This proves both the classification and the normalization for the circle characters.

<a id="cpt-f-010"></a>
## CPT-F-010 — Continuous vector integrals and strict averages

Let \(X\) be compact Hausdorff, \(\mu\) a finite positive Radon measure, and \(V\) a real or complex Banach space. Every continuous \(f:X\to V\) has a norm integral. For \(\varepsilon>0\), take finitely many open sets \(U_i\) covering \(X\), with sample points \(x_i\in U_i\), so that \(\|f(x)-f(x_i)\|<\varepsilon\) on \(U_i\). Continuity and compactness supply these sets. Disjointize the cover to the Borel partition
\[
E_1=U_1,\qquad E_i=U_i\setminus\bigcup_{j<i}U_j.
\]
The simple function \(s_\varepsilon=\sum_i1_{E_i}f(x_i)\) uniformly approximates \(f\). Define \(\int s_\varepsilon=\sum_i\mu(E_i)f(x_i)\). For any two finite simple functions, their common partition and the triangle inequality give
\[
\left\|\int s-\int t\right\|
 \leq\int\|s-t\|\,d\mu.
\tag{F10.1}
\]
Hence the approximating integrals are Cauchy, and Banach completeness gives a limit independent of every partition and sample choice. Define it as \(\int f\,d\mu\). Applying (F10.1) and uniform convergence also gives
\[
\left\|\int f\,d\mu\right\|\leq\int\|f\|\,d\mu
 \leq\mu(X)\|f\|_\infty.
\tag{F10.2}
\]
Linearity follows by taking a common refinement of simple approximations to the two functions. Every bounded linear map commutes with the integral; bounded real-linear maps do so too, because the weights are real. Closed linear subspaces containing all the values contain the integral. If \(\mu(X)=1\), the integral is in the closed convex hull of the values, as each simple integral is a convex combination. More generally a closed convex cone containing the values contains the integral for any finite positive \(\mu\).

This is also the Bochner integral of \(f\). Indeed \(f(X)\) is a compact metric subspace of \(V\). Choosing finite \(1/n\)-nets in this image gives a countable dense subset; their linear span has separable closure. The finite simple functions above, with \(\varepsilon=1/n\), prove strong measurability directly, and their uniform convergence proves integrability without an ambient separability assumption. A change of variable by a measure-preserving homeomorphism preserves the integral, first for the finite simple sums and then by the norm limit.

Continuous vector Fubini also holds on products of compact Hausdorff spaces, without metrizability. For continuous \(f:X\times Y\to V\), a finite-cover argument gives a neighborhood of \(x\) on which \(\sup_y\|f(x',y)-f(x,y)\|\) is small: take finitely many product neighborhoods over \(\{x\}\times Y\) and intersect their \(X\)-factors. Cover \(X\) by finitely many such neighborhoods with samples \(x_i\), and then cover \(Y\) so that all the finitely many functions \(f(x_i,\cdot)\) have small oscillation, with samples \(y_j\). CPT-F-002 gives continuous finite partitions \(\phi_i,\psi_j\) subordinate to these covers. The functions
\[
\sum_{i,j}\phi_i(x)\psi_j(y)f(x_i,y_j)
\]
approximate \(f\) uniformly. Both iterated integrals and the product integral agree on each such finite sum by scalar continuous Fubini, CPT-F-004. Estimate (F10.2) passes their equality to \(f\). That estimate and the uniform-in-\(y\) continuity just proved also make \(x\mapsto\int_Y f(x,y)\,d\nu(y)\) continuous. This proves every continuous vector integral used in compact-group averaging.

Now let \(E\) be any Hilbert \(B\)-module, and let \(T:X\to\mathcal L(E)\) be uniformly bounded, with both \(x\mapsto T(x)\xi\) and \(x\mapsto T(x)^*\xi\) norm continuous for every \(\xi\in E\). Define
\[
S\xi=\int_XT(x)\xi\,d\mu(x),
\qquad
R\eta=\int_XT(x)^*\eta\,d\mu(x).
\tag{F10.3}
\]
Estimate (F10.2) gives bounded operators of norm at most \(\mu(X)\sup_x\|T(x)\|\). Integration commutes with the bounded right-multiplication maps on \(E\), so both are \(B\)-linear. The two bounded real-linear inner-product maps give
\[
\langle S\xi,\eta\rangle
=\int_X\langle T(x)\xi,\eta\rangle\,d\mu(x)
=\int_X\langle\xi,T(x)^*\eta\rangle\,d\mu(x)
=\langle\xi,R\eta\rangle.
\]
Thus \(S\) is adjointable and \(S^*=R\). This constructs the strict integral; it does not assert norm continuity of \(T\). If every \(T(x)\) is positive, then \(\langle\xi,S\xi\rangle\) is an integral of positive elements of \(B\), so is positive by the closed-convex-cone assertion. Hence \(S\) is positive. Here is the order test used in this assertion. It is self-adjoint by (F10.3). If its spectrum contained a negative point, continuous functional calculus would give a real \(h\), nonzero on that spectrum and supported where \(t\leq-\delta\), \(\delta>0\). Choose \(y\) with \(x=h(S)y\ne0\). The positive operator \((-S-\delta)h(S)^2\), through its square root, gives \(-\langle x,Sx\rangle-\delta\langle x,x\rangle\geq0\). Together with \(\langle x,Sx\rangle\geq0\), this forces \(x=0\), a contradiction. The coefficient positive cone and continuous functional calculus here have the earlier programme proofs in [C*-algebra foundations](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html), Theorem 5.1 and Proposition 8.5, also bound explicitly in Lesson 05. Self-adjointness, contractions for probability measure, and linear identities pass to the integral in the same way.

The integral is also a limit in the strict topology on \(\mathcal L(E)=M(\mathcal K(E))\). For a finite list of vectors, choose the finite cover above simultaneously for the continuous functions \(T(\cdot)\xi\) and \(T(\cdot)^*\xi\) in that list. The finite sums \(\sum_i\mu(E_i)T(x_i)\) have a common operator bound and approximate (F10.3) on these vectors and their adjoints. Direct the choices by enlarging the finite list and decreasing the error. They converge on every vector in both senses. Such bounded convergence implies strict convergence: on rank-one operators,
\[
(T_j-S)\theta_{\xi,\eta}=\theta_{(T_j-S)\xi,\eta},
\qquad
\theta_{\xi,\eta}(T_j-S)=\theta_{\xi,(T_j^*-S^*)\eta};
\]
the rank-one norm estimate makes both tend to zero. Finite sums and the common bound extend this to every element of \(\mathcal K(E)\). This gives the strict-limit assertion directly, without a countable list of vectors or a norm-continuous operator field.

If \(T\) is norm continuous with values in the closed Banach subspace \(\mathcal K(E)\), its norm integral is compact and acts on vectors as (F10.3); uniqueness identifies the two integrals. More generally if, for a fixed \(a\in\mathcal L(E)\), the fields \(T(x)a\) or \(aT(x)\) are norm-continuous compact-valued fields, then
\[
Sa=\int_XT(x)a\,d\mu(x),
\qquad
aS=\int_XaT(x)\,d\mu(x)
\tag{F10.4}
\]
are compact, by evaluating on vectors. This proves the source-localized compact-integral step in equivariant cycles, connections and technical partitions.

For a compact Hausdorff group \(G\), use its probability Haar measure from CPT-F-005. Let \(U_g\) be a strongly continuous Hilbert-module action, allowed to be semilinear for the coefficient-algebra action. Each \(U_g\) is a bounded complex-linear isometry on the underlying Banach space. The conjugate \(T(g)=U_gTU_g^{-1}\) is adjointable, of constant norm, and its adjoint is the conjugate of \(T^*\). Its action on each vector is continuous: replace the moving input \(U_g^{-1}\xi\) by a fixed input, use boundedness of \(T\), and then strong continuity of \(U_g\). The same argument applies to \(T^*\). Formula (F10.3) therefore defines its average. Since bounded linear maps commute with these vector integrals and left Haar translation preserves them,
\[
U_hSU_h^{-1}\xi
=\int_G U_{hg}TU_{hg}^{-1}\xi\,dg
=S\xi.
\]
Thus it is invariant even for a semilinear action. On rank-one operators the formula
\(g\cdot\theta_{\xi,\eta}=\theta_{U_g\xi,U_g\eta}\), with
\(\|\theta_{\xi,\eta}\|\leq\|\xi\|\|\eta\|\), proves norm continuity of compact orbits by finite sums and norm closure. Compact-valued localized orbit defects consequently have compact norm integrals as in (F10.4).

These are the continuous Banach and strict Hilbert-module integrals used by Lesson 17 Lemma 1.1 and its compact-group averages, and Lesson 13 Lemma 9.0. No countability, fullness, coefficient unit or nondegeneracy of a representation was imposed on \(E\). The earlier Hilbert-module inner-product and positivity facts remain their declared programme prerequisites. This section concerns finite Radon measures on compact spaces; it does not claim a Haar-existence or general Bochner-Fubini proof for noncompact locally compact groups.

## Free comparison text and licence boundary

Caroline Gruson and Vera Serganova, [*A sentimental journey through representation theory: from finite groups to quivers (via algebras)*, author-hosted draft](https://math.berkeley.edu/~serganov/math252/Bookrep.pdf), Chapter 3. The checked draft contains compact representations and matrix-coefficient arguments. It explicitly does not prove Haar existence in full generality. Its functionals and Hilbert facts are also prerequisites, rather than complete proofs. No copying, translation or relicensing permission is inferred from free access; its prose is not incorporated here. The linked independently written programme proof components retain their displayed source notices.
