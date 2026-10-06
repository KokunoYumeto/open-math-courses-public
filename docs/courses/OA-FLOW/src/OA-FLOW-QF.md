# Local foundations for quotient fields

*Programme proof restoration and additional foundation proofs by GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original programme expression is dedicated under CC0 to the extent of rights held. No human review is asserted.*

The following elementary proofs supply the precise inputs of the four induction chapters. Groups and Hilbert spaces are arbitrary. A Radon measure initially uses the outer regular convention of [HR2–3](OA-FLOW-HR.md#hr-02); whenever the induction chapters use the inner regular representative, their explicit conversion applies. No countable base, disintegration theorem or measurable choice of a coset representative is assumed.

The earlier inputs are [H0](OA-FLOW-TOPOLOGY.md#l138-h0) for compact cutoffs and finite partitions, CF1 for norm separation and norm series, [HR2–3](OA-FLOW-HR.md#hr-02) for positive Riesz representation and finite regularity, [HR5](OA-FLOW-HR.md#hr-05) for finite Radon products, [HR8](OA-FLOW-HR.md#hr-08) for open sigma compact subgroups, [SC4–7](OA-FLOW-SC.md#sc-04) for sequential scalar integration, and the simple-function construction of [L24 Proposition4.1](OA-FLOW-L24.md#oa-flow.grp.vectorintegration). Hilbert completions and orthogonal projections are proved in CF8 and CF10.

<a id="qf-1"></a>
## QF1. Closed-subspace extension and quotient topology

If \(A\) is closed in a compact Hausdorff space \(Z\), every continuous complex function on \(A\) extends continuously to \(Z\). Here is the proof needed for compact support. For a real \(g\) with \(\|g\|_\infty\le M\), H0 separates the disjoint closed subsets \(\{g\ge M/3\}\) and \(\{g\le-M/3\}\) of \(Z\). A continuous function \(u\), bounded by \(M/3\), can therefore equal \(M/3\) on the first and \(-M/3\) on the second. Then \(\|g-u|_A\|_\infty\le2M/3\). Repeat on this residual. The successive extensions have bounds \((M/3)(2/3)^n\); their uniformly convergent sum is continuous and restricts to \(g\). The case \(M=0\) is immediate. Apply the construction to the real and imaginary parts for complex \(g\).

Consequently, if \(H\) is a closed subspace of an LCH space \(X\), the restriction map \(C_c(X)\to C_c(H)\) is onto. For \(f\in C_c(H)\), its extension by zero at infinity is continuous on the closed subset \(H\cup\{\infty\}\) of the one-point compactification \(X^+\) constructed in H0. Extend it to \(X^+\) by the preceding argument. Multiply the restriction to \(X\) by a compact cutoff equal to one on \(\operatorname{supp}f\). The result still restricts to \(f\), and has compact support. Positivity of this extension is not needed below; for nonnegative \(f\), replacing a real extension by its positive part does preserve the restriction.

Let now \(G\) be an LCH group, \(H\) a closed subgroup, \(Y=G/H\), and \(q(s)=sH\). The map \(q\) is open because \(q^{-1}(q(O))=OH\) for open \(O\). Distinct cosets \(xH,yH\) have disjoint open quotient neighborhoods: continuity and \(y^{-1}x\notin H\) give neighborhoods \(V,W\) with \(W^{-1}V\cap H=\varnothing\). The compact image of a compact neighborhood of \(x\) contains the open image of its interior. Thus \(Y\) is LCH.

Every compact \(E\subset Y\) lifts to a compact subset of \(G\). Choose a relatively compact identity neighborhood \(V\) and finitely many \(q(g_iV)\) covering \(E\). Then

<a id="equation-qf1"></a>

\[
 K=q^{-1}(E)\cap\bigcup_i g_i\overline V
 \tag{QF1}
\]

is compact and maps onto \(E\). Closedness uses the Hausdorff property just proved. No continuous section is involved.

<a id="qf-2"></a>
## QF2. Compact quotient averaging

Fix left Haar measure on \(H\), and define

<a id="equation-qf2"></a>

\[
 Qf(sH)=\int_H f(sh)\,dh\qquad(f\in C_c(G)).
 \tag{QF2}
\]

Left invariance makes this independent of the representative. Near \(s_0\), keep \(s\) in a compact neighborhood \(A\); only \(h\in H\cap A^{-1}\operatorname{supp}f\), a compact set, contributes. Finite continuity neighborhoods give uniform convergence in this compact \(h\)-variable as \(s\to s_0\). The integral is continuous, and its support lies in the compact set \(q(\operatorname{supp}f)\).

For compact \(E\subset Y\), lift it to \(K\) by QF1 and choose \(a\in C_c(G)_+\) equal to one on \(K\). Haar positivity on nonempty opens, proved in [HR7](OA-FLOW-HR.md#hr-07), gives \(Qa>0\) on \(E\). Choose \(0\le\eta\le1\) compactly supported inside \(\{Qa>0\}\), with \(\eta=1\) on \(E\). Then

<a id="equation-qf3"></a>

\[
 b(s)=a(s)\frac{\eta(q(s))}{Qa(q(s))}
 \tag{QF3}
\]

with zero extension off the positive denominator set is continuous, nonnegative and compactly supported, and \(Qb=\eta\). The quotient has continuous zero extension because \(\operatorname{supp}\eta\) is compactly contained in that open set. For \(F\in C_c(Y)\), choose \(b\) for \(E=\operatorname{supp}F\); the function \((F\circ q)b\in C_c(G)\) maps to \(F\). It is nonnegative when \(F\) is. In particular \(Q\) is onto.

<a id="qf-3"></a>
## QF3. A locally finite cutoff over all cosets

Choose an open sigma compact subgroup \(L\subset G\) by HR8. Its orbits on \(Y\) are open, since \(q\) is open, and closed, since the other orbits form their open complements. Each is a continuous image of \(L\), hence sigma compact. The same facts give a decomposition of \(G\) into open and closed sigma compact cosets.

On any one orbit \(Y_0\), a countable compact cover can be enlarged to compact sets \(K_n\subset\operatorname{int}K_{n+1}\) covering \(Y_0\): at each step cover the preceding compact set and the next member of the given cover by finitely many relatively compact neighborhoods, and use their compact closures. Put \(K_0=K_{-1}=\varnothing\). The compact shells \(S_n=K_n\setminus\operatorname{int}K_{n-1}\) lie in \(W_n=\operatorname{int}K_{n+1}\setminus K_{n-2}\). Use H0 to choose a nonnegative compact function \(\theta_n\), equal to one on \(S_n\), supported in \(W_n\). These functions are locally finite: a neighborhood in \(\operatorname{int}K_N\) misses \(W_n\) for \(n\ge N+2\). Their sum is positive, so \(\psi_n=\theta_n/\sum_j\theta_j\) is a compactly supported partition of one. Extend by zero and do this on all the disjoint open orbits. The resulting family \((\psi_i)\) on \(Y\) remains locally finite.

Choose \(b_i\ge0\) as in QF2 with \(Qb_i=1\) on \(\operatorname{supp}\psi_i\). Then

<a id="equation-qf4"></a>

\[
 k(s)=\sum_i\psi_i(q(s))b_i(s),\qquad Qk=1.
 \tag{QF4}
\]

Local finiteness makes \(k\) continuous. A compact \(E\subset Y\) meets only finitely many supports of the locally finite family. The closed set \(\operatorname{supp}k\cap q^{-1}(E)\) lies in the union of their finitely many compact \(b_i\)-supports, hence is compact. This is the exact proper-support property used in all later integrations. It does not say that \(k\) has compact support on \(G\).

<a id="qf-4"></a>
## QF4. Locally bounded complex functionals

We need a small consequence of positive Riesz representation, not an additional complex representation theorem. Let \(\ell:C_c(X)\to\mathbb C\) be complex linear and bounded in supremum norm on every fixed compact support. For its real part \(\lambda\) on real functions, put, for \(f\ge0\),

<a id="equation-qf5"></a>

\[
 P(f)=\sup_{0\le g\le f}\lambda(g).
 \tag{QF5}
\]

This is finite by the compact-support bound and is nonnegative. It is homogeneous. To prove additivity, sums of admissible functions give \(P(f+h)\ge P(f)+P(h)\). Conversely split any \(0\le g\le f+h\) into \(gf/(f+h)\) and \(gh/(f+h)\), with zero values where the denominator vanishes. They are continuous: the first is bounded in absolute value by \(f\), the second by \(h\), which both tend to zero at any zero of \(f+h\). Their supports are compact, and they are bounded by \(f,h\), respectively. This gives the opposite inequality. The additive positive-cone map \(P\) extends to real functions by differences; independence of the difference follows by adding the two positive decompositions of the same function. Its complex-linear extension is positive. Also \(P-\lambda\) is positive on real nonnegative functions. Do the same for the imaginary part. Thus \(\ell\) is a complex linear combination of four positive functionals, each represented by HR2.

On every relatively compact part these four measures have finite total mass; their linear combination is a finite complex Radon measure there. Restrictions are compatible and unique: multiply tests by a cutoff on a compact neighborhood, and apply positive Riesz uniqueness to the real and imaginary differences. We use “locally finite complex Radon measure” in this sense. No finite total variation on all of \(X\) is claimed. Every subsequent integral with such a measure has compact support, and may be calculated using these four finite positive restrictions. In particular HR5 justifies product interchanges there. A continuous density representing a positive functional is real by uniqueness and complex conjugation, and is nonnegative pointwise: a negative value would persist on a nonempty open neighborhood and contradict a nonnegative compact test and Haar positivity.

<a id="qf-5"></a>
## QF5. Scalar measures of a nondegenerate representation

Let \(\pi:C_0(Y)\to B(\mathcal L)\) be a nondegenerate star representation, on any Hilbert space. It is contractive. Extend it algebraically to the unitization by \(\widetilde\pi(F+c)=\pi(F)+cI\). For \(c=\|F\|_\infty^2>0\), the square root of \(c-|F|^2\) belongs to that unitization, so positivity of its represented square gives \(\|\pi(F)\xi\|^2\le c\|\xi\|^2\). The zero case is immediate.

Take compact cutoffs \(0\le e_K\le1\), equal to one on compact \(K\), directed by inclusion of \(K\). Then \(\|(1-e_K)F\|_\infty\to0\) for \(F\in C_0(Y)\). Contractivity and nondegeneracy imply \(\pi(e_K)\xi\to\xi\) for every vector, first on the dense span of \(\pi(F)\eta\), then on its closure by the uniform bound. HR2 gives the finite positive measure \(\mu_\xi\) representing \(F\mapsto\langle\pi(F)\xi,\xi\rangle\). Its mass is \(\|\xi\|^2\): the upper bound follows from contractivity and the compact-cutoff mass formula; the preceding convergence gives the lower bound. Polarization gives finite complex measures \(\mu_{\xi,\eta}\), and

<a id="equation-qf6"></a>

\[
 \langle\pi(F)\xi,\eta\rangle=\int_Y F\,d\mu_{\xi,\eta},
 \qquad \mu_{\xi,\eta}(Y)=\langle\xi,\eta\rangle.
 \tag{QF6}
\]

These scalar measures suffice for the converse proof. A projection-valued measure theorem is not required. These finite outer regular measures are already inner regular on every Borel set by HR3. They are therefore the exact scalar representatives used in the following chapters.

For completeness, a nonzero covariant representation of a transitive \(G\)-space \(Y\) is faithful. If \(\pi(F)=0\) for a nonzero \(F\in C_0(Y)\), then \(\pi(|F|^2)=0\). There is a nonempty open \(O\) on which \(|F|^2>c>0\). Translates of \(O\) cover \(Y\). For an arbitrary \(g\in C_c(Y)\), a finite subordinate partition on its support writes \(g=\sum_jg_j\), each \(g_j\) compactly supported in one such translate. Divide \(g_j\) by the corresponding translate of \(|F|^2\) on that open set, extending by zero; this is in \(C_c(Y)\). Covariance therefore gives \(\pi(g_j)=0\), and then \(\pi(g)=0\). Density of \(C_c(Y)\) in \(C_0(Y)\), proved in HR2, forces \(\pi=0\), contrary to nondegeneracy on a nonzero Hilbert space.

<a id="qf-6"></a>
## QF6. Local vector measurability and finite-measure integration

On a compact space with finite completed Radon measure, an almost everywhere limit of finite-valued measurable simple functions is continuous after deleting a set of arbitrarily small measure and retaining a compact subset. Here are the details. If \(s_n\to v\) pointwise off a null set, let

<a id="equation-qf7"></a>

\[
 A_{m,N}=\bigcup_{n\ge N}\{\|s_n-v\|>1/m\}.
 \tag{QF7}
\]

For fixed \(m\), these sets decrease to a null set. Finite-measure continuity from SC4 gives \(N_m\) with \(\mu(A_{m,N_m})<\epsilon2^{-m-2}\). Off their union convergence is uniform. For each \(n\), finite inner regularity replaces each of the finitely many level sets of \(s_n\) by a compact subset, with total loss below \(\epsilon2^{-n-2}\). On their finite union \(s_n\) is continuous, since disjoint compact subsets are relatively open there. Intersect these retained sets for all \(n\), and use finite inner regularity once more to retain a compact subset of the uniform-convergence set. The total loss can be made less than \(\epsilon\). Uniform convergence on it makes \(v\) continuous.

Conversely, continuity on compact subsets with omitted measures tending to zero gives, outside a null set, a range contained in a countable union of compact metric images, hence a separable closed subspace. A Borel representative on that range has simple approximants by the countable-ball construction of L24. On a space decomposed into open and closed sigma compact pieces \(O_i\) as in QF3, the Borel representative can be constructed without an uncountable union of Borel sets of uncontrolled complexity. Choose compact exhaustions \(C_{i,n}\) whose interiors cover each \(O_i\). Local measurability gives compact \(F_{i,n,m}\subset C_{i,n}\) on which the field is continuous, with omitted measure below \(2^{-m}\). Each \(F_{n,m}=\bigcup_iF_{i,n,m}\) is closed in the whole space, and the restricted field is continuous there, since the pieces \(O_i\) are open and closed. Its complement \(N=X\setminus\bigcup_{n,m}F_{n,m}\) is Borel and null on every compact: in each \(C_{i,n}\) its measure is at most \(2^{-m}\) for every \(m\), and any compact meets only finitely many pieces. Define the field to be zero on \(N\), and use its original values on the first \(F_{n,m}\) containing a point. This is a countable Borel partition with continuous restrictions, hence a Borel field. In the inner-regular convention \(N\) is globally null as well. This proves the needed representative assertion both for scalar locally integrable densities and for the vector fields below. Their local continuity convention and compactwise strong measurability agree, without a globally separable target.

The Bochner integral construction of L24 also applies to a finite completed measure \(\nu\), not just to Haar measure. Explicitly, for a strongly measurable Banach-valued \(v\) with \(\int\|v\|\,d\nu<\infty\), truncate its norm and approximate its separable range by a countable \(1/n\)-net; truncate the resulting countable partition to finitely many pieces. These simple functions approximate \(v\) in \(L^1(\nu)\). Their integrals are Cauchy by the simple-function norm inequality, so completeness gives \(\int v\,d\nu\), with \(\|\int v\|\le\int\|v\|\). The same inequality proves independence of approximants and permits every bounded linear map to pass through the integral. This is all the vector integration used below.

<a id="qf-7"></a>
## QF7. Finite densities and compact carriers

Let \(\mu\) be a locally finite Borel measure inner regular on every Borel set, and \(w\ge0\) Borel with \(\int w\,d\mu<\infty\). Then \(\nu=w\mu\) is a finite inner regular measure. Indeed the positive-level truncations \(\{1/n\le w\le n\}\) have finite \(\mu\)-measure; bounded simple functions there approximate \(w\) in \(L^1(\mu)\) by SC4–7. Each finite weighted restriction to a Borel level set is inner regular. Transferring compact approximations across the \(L^1\) error proves inner regularity of \(\nu\). Finite inner regularity also gives outer regularity: approximate the complement of any Borel set by a compact subset and subtract its measure from \(\nu(X)\). Compact sets \(C_n\) with \(\nu(X\setminus C_n)<1/n\) therefore carry \(\nu\) on their countable union. These facts hold for completions as well, by discarding a Borel null superset of each exceptional set. This is the finite carrier used in the predual proof, rather than a countable exhaustion of \(G\).

The topology and averaging arguments in QF1–3 retain the complete mathematical content of the programme's CC0 quotient-measure provider (Lemma1.2, Lemma2.1 and the cutoff proof of Lemma4.1). Their foundations are rebound here to current H0 and HR. QF4–7 spell out the complex-functional, scalar-measure and vector-integration steps required by the preserved induction proofs. The classical mathematical comparison is M. Takesaki, *Theory of Operator Algebras II*, §X.4, and *Theory of Operator Algebras I*, Definition IV.7.1 and Proposition IV.7.2; ordinary source attribution is separate from the complete local proofs above.
