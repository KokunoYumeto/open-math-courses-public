# Scalar continuity implies norm continuity for Banach representations

<a id="gbac-setting"></a>
Let \(G\) be a locally compact Hausdorff topological group, let \(E\) be a real or complex Banach space, and let
\[
 U:G\longrightarrow \mathrm{GL}(E),\qquad U(st)=U(s)U(t),
\]
be an algebraic homomorphism into the invertible bounded linear operators. Assume that
\[
 s\longmapsto \ell(U(s)x)
 \quad\hbox{is continuous for every }x\in E,\ \ell\in E^*.
 \tag{BC1}
\]
Then \(s\mapsto U(s)x\) is norm continuous for every \(x\in E\). Conversely, norm continuity of every orbit implies (BC1), by boundedness of each \(\ell\).

No isometry, global operator bound, separability, second countability, metrizability, sigma compactness or unimodularity is assumed. The case \(E=\{0\}\) is immediate. Otherwise the homomorphism has \(U(e)=I\), since \(U(e)\) is invertible and idempotent.

The argument first establishes an auxiliary compactness statement by reducing each **sequence of finite convex combinations** to its own separable subspace. It then constructs averages through their scalar values in a weakly compact convex set. Thus the original orbit is never presumed to be Bochner measurable before norm continuity is proved.

<a id="gbac-inputs"></a>
## Earlier proofs

The real and complex forms of [Hahn–Banach and norm separation][HB], [dual completeness and uniform boundedness][HB4], and [convex separation][HB6] supply the Banach-space arguments. [Banach–Alaoglu and separable metrizability][WT3], [Mazur's closure equality][WT4], and the full [Eberlein–Šmulian theorem][WT] supply the weak-topology compactness arguments.

[Compact shrinking and cutoffs][H0], [Riesz representation for compact spaces][HR], and [left Haar existence, local finiteness and positivity][HR6] supply the locally compact measure arguments. Scalar [simple integration][SC], [finite-measure continuity and monotone convergence][SC4], and [signed and complex integration][SC5] give the scalar operations. [Banach norm and series operations][CF] supply completeness and norm separation; uniform boundedness is the theorem linked above.

[Left-translation continuity][L24] and [finite-simple vector integration][L24integral] provide useful comparisons. Both the finite-probability construction and the compact-support translation argument are proved explicitly below, so no Haar carrier convention is transferred to a different measure space.

Only the topology part of H0 is used, not its tensor construction. Only a left Haar measure finite on compact sets is used; no product-measure theorem or global finite-measure exhaustion of \(G\) is needed.

<a id="gbac-local-bound"></a>
## 1. Bounds on compact parameter sets

For a compact \(S\subset G\) and a fixed \(x\in E\), (BC1) gives
\[
 \sup_{s\in S}|\ell(U(s)x)|<\infty\qquad(\ell\in E^*).
\]
To get a norm bound, apply uniform boundedness on the Banach space \(E^*\) to the evaluation maps
\[
 J_{s,x}:E^*\to\mathbb K,\qquad J_{s,x}(\ell)=\ell(U(s)x).
\]
The norming formula in [HB], Corollary 2.3, gives \(\|J_{s,x}\|=\|U(s)x\|\). Hence \(\sup_{s\in S}\|U(s)x\|<\infty\) for every \(x\). A second application of [HB4], Theorem 4.2, now to \(\{U(s):s\in S\}\subset B(E)\), proves
\[
 M_S:=\sup_{s\in S}\|U(s)\|<\infty.
 \tag{BC2}
\]
This is a bound on each compact set separately. It does not supply a bound on all of \(G\). The same first application shows that any weakly compact subset of any normed space is norm bounded: every bounded linear functional has a bounded image on that compact set.

<a id="gbac-metric-barycentre"></a>
## 2. Probability barycentres on a separable weakly compact set

Let \(F\) be a separable Banach space and let \(L\subset F\) be nonempty and weakly compact. It is norm bounded; write \(B=\sup_{z\in L}\|z\|\).

**Its weak topology is metrizable.** Choose a norm-dense sequence \((a_n)\) in \(F\). Hahn–Banach gives \(\ell_n\in F^*\) with \(\|\ell_n\|\le1\) and \(\ell_n(a_n)=\|a_n\|\). These functionals separate points: if \(v\ne0\), choose \(a_n\) with \(\|v-a_n\|<\|v\|/3\); then
\[
 |\ell_n(v)|\ge\|a_n\|-\|v-a_n\|>\|v\|/3.
\]
Consequently
\[
 d(z,w)=\sum_{n\ge1}2^{-n}\min\{1,|\ell_n(z-w)|\}
 \tag{BC3}
\]
is a metric on \(L\). Uniform convergence of this series makes the identity from weak \(L\) to metric \(L\) continuous. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism: images of closed sets are compact and therefore closed. Thus (BC3) gives exactly the weak topology of \(L\). The zero-space case has its one-point metric and needs no norming sequence.

**Probability measures on \(L\) form a compact metric space.** To see the required separability of \(C(L,\mathbb C)\) explicitly, for every positive integer \(m\) choose a finite \(1/m\)-net \(a_{m,1},\dots,a_{m,k_m}\) for the compact metric space \(L\). Put
\[
 h_{m,j}(z)=\max\{0,2/m-d(z,a_{m,j})\},\qquad
 p_{m,j}=h_{m,j}/\sum_i h_{m,i}.
\]
The denominator is positive, and the \(p_{m,j}\) sum to one. Continuity on a compact metric space is uniform: choose at each centre a radius on which the value changes by less than half the desired error, retain a finite cover by balls of half those radii, and use the least of the finitely many half-radii to put two nearby points in the same original ball. Uniform continuity therefore shows that \(\sum_j f(a_{m,j})p_{m,j}\) converges uniformly to every \(f\in C(L,\mathbb C)\): a nonzero summand has its centre within \(2/m\). Replacing these finitely many coefficients by rational complex numbers gives a countable uniformly dense family. The real-valued version is identical.

The space \(C(L,\mathbb C)\) is Banach: a uniform Cauchy sequence has a uniform limit, and uniform limits of continuous functions are continuous. By [WT3], Theorem 3.1, its dual unit ball is weak-star compact; Proposition 3.2 makes that ball metrizable. Positive functionals \(p\) with \(p(1)=1\) form a weak-star closed subset. Positivity implies \(\|p\|=p(1)=1\), by the phase and order estimate of [HR], (HR-02c), and evaluation at the constant one. By [HR], these functionals are precisely the Borel Radon probability measures on \(L\), acting by integration. Denote this compact metric space by \(\mathcal P(L)\). A sequence in a compact metric space has a convergent subsequence: the closures of its tails have a common point, and balls of radii \(1/n\) select successively later terms. Thus every sequence in \(\mathcal P(L)\) has a subsequence converging on every member of \(C(L)\).

**The inclusion \(L\to F\) is integrable for each \(\mu\in\mathcal P(L)\).** It need not be norm continuous. For a fixed \(a\in F\), however, the sets
\[
 \{z\in L:\|z-a\|\le r\}
 =\bigcap_{\|\ell\|\le1}\{z:|\ell(z-a)|\le r\}
\]
are weakly closed. The sets \(\|z-a\|<r\) are countable unions of such closed sublevel sets. A countable norm-dense set in \(F\) provides a countable base of norm balls; therefore the inclusion is Borel measurable for the norm topology.

For each \(n\), choose the first norm-dense point within \(1/n\) of \(z\). This gives a measurable countably valued map \(s_n\) with \(\|s_n(z)-z\|<1/n\) and \(\|s_n(z)\|\le B+1\). Truncate its countable measurable partition to finitely many pieces, putting zero on the omitted pieces, so that their total \(\mu\)-measure is less than \(2^{-n}\). This is possible by continuity from below of the finite measure. Call the finite-valued map \(t_n\). Then
\[
 \int_L\|t_n(z)-z\|\,d\mu(z)
 \le 1/n+B2^{-n}\longrightarrow0.
 \tag{BC4}
\]
The omitted sets occur infinitely often only on a measurable null set: the measure of their union for \(n\ge N\) is at most \(\sum_{n\ge N}2^{-n}\), which tends to zero. Thus \(t_n(z)\to z\) in norm almost everywhere as well. This verifies strong measurability rather than invoking it from weak measurability alone.

For a finite simple map \(t=\sum_j1_{A_j}v_j\) on a disjoint partition, define \(I_\mu(t)=\sum_j\mu(A_j)v_j\). Refining two partitions and using the triangle inequality gives
\[
 \|I_\mu(t)-I_\mu(t')\|
 \le\int_L\|t-t'\|\,d\mu.
\]
Equation (BC4) makes \(I_\mu(t_n)\) Cauchy; completeness of \(F\) gives a vector \(b_\mu\in F\). For every \(\ell\in F^*\), scalar integral error is at most \(\|\ell\|\) times (BC4), so
\[
 \ell(b_\mu)=\int_L\ell(z)\,d\mu(z),\qquad
 \|b_\mu\|\le B.
 \tag{BC5}
\]
This is the probability barycentre. Uniqueness follows from norm separation. These arguments use only finite measure and the scalar operations of [SC]; no separability of a surrounding Banach space or measurable parameter group was introduced.

<a id="gbac-closed-convex-hull"></a>
## 3. The closed convex hull of a weakly compact set

Let \(K\) be a nonempty weakly compact subset of an arbitrary Banach space \(E\), and set
\[
 C=\overline{\operatorname{co}K}^{\,\|\cdot\|},
\]
where convex coefficients are nonnegative real numbers summing to one, also when \(E\) is complex. We prove that \(C\) is weakly compact.

Given any sequence \((x_n)\) in \(C\), choose finite convex combinations
\[
 y_n=\sum_{j=1}^{k_n}\lambda_{n,j}z_{n,j},\quad
 z_{n,j}\in K,\quad \lambda_{n,j}\ge0,\quad
 \sum_j\lambda_{n,j}=1,\quad \|x_n-y_n\|<1/n.
 \tag{BC6}
\]
The set of all atoms \(z_{n,j}\) is countable. Its closed linear span \(F\subset E\) is separable and Banach: finite combinations of the atoms with rational real coefficients, or rational real and imaginary coefficients in the complex case, form a countable dense subset; a closed subspace of a complete normed space is complete. It is weakly closed: a point outside a closed subspace is separated from it by [HB], Corollary 2.3(3). Moreover, Hahn–Banach extension identifies the weak topology on \(F\) with the topology inherited from \(E\).

Hence \(L=K\cap F\) is weakly compact and contains all those atoms. If \(F=\{0\}\), (BC6) already gives \(x_n\to0\) in norm. Otherwise Section 2 applies. The atomic probabilities
\[
 \mu_n=\sum_j\lambda_{n,j}\delta_{z_{n,j}}\in\mathcal P(L)
\]
have a subsequence \(\mu_{n_i}\to\mu\) on \(C(L)\). The barycentre \(b_\mu\in F\) exists by (BC5). For every \(\ell\in E^*\), its restriction to \(L\) is weakly continuous, so
\[
 \ell(y_{n_i})=\int_L\ell\,d\mu_{n_i}
 \longrightarrow\int_L\ell\,d\mu=\ell(b_\mu).
\]
The norm error in (BC6) tends to zero, so \(x_{n_i}\to b_\mu\) weakly in \(E\). Every sequence in \(C\) therefore has a subsequence converging weakly to a point of \(E\). The complete Eberlein–Šmulian theorem in [WT], Theorem 7.2, implies that \(C\) is relatively weakly compact. Since \(C\) is norm closed and convex, Mazur's theorem [WT4], Theorem 4.1, makes it weakly closed. It is thus weakly compact, as claimed.

Only the subspace generated by the atoms of one approximating sequence was made separable. Neither \(K\) nor \(E\) was assumed separable. This proves the required convex-hull compactness statement here; it does not assume the general statement as an unproved integration theorem.

<a id="gbac-scalar-averages"></a>
## 4. Construct the orbital averages inside \(E\)

Choose the outer regular Borel left Haar measure \(m\) from [HR6], Theorem HR-06. It is finite on compact sets and positive on every nonempty open set. All integrals below have compact support, so this convention suffices.

Fix \(x\in E\) and \(f\in C_c(G)\), with real scalar functions when \(E\) is real. We construct a unique \(A(f)x\in E\) satisfying
\[
 \ell(A(f)x)=\int_G f(t)\ell(U(t)x)\,dm(t)
 \quad(\ell\in E^*).
 \tag{BC7}
\]
Scalar integration exists because the coefficient is continuous and bounded on \(\operatorname{supp}f\), whose measure is finite.

First suppose \(f\ge0\). Put \(S=\operatorname{supp}f\), \(a=\int f\,dm\). If \(a=0\), every scalar integral in (BC7) is zero, so take \(A(f)x=0\). Suppose \(a>0\). The set
\[
 K=\{U(t)x:t\in S\}
\]
is weakly compact: (BC1) makes the map from compact \(S\) to weak \(E\) continuous. By Section 3, \(C=\overline{\operatorname{co}K}^{\,\|\cdot\|}\) is weakly compact.

For any finite \(\ell_1,\dots,\ell_q\in E^*\) and \(\varepsilon>0\), cover \(S\) by finitely many relative open sets on each of which every scalar function \(\ell_j(U(t)x)\) has oscillation less than \(\varepsilon\). Make these sets into a disjoint finite Borel partition \((B_i)\) by subtracting preceding sets, discard empty pieces, and choose \(t_i\in B_i\). The weights
\[
 c_i=a^{-1}\int_{B_i} f(t)\,dm(t)
\]
are nonnegative and sum to one. Therefore \(v=\sum_i c_iU(t_i)x\in C\), and
\[
 \left|\ell_j(v)-a^{-1}\int f(t)\ell_j(U(t)x)\,dm(t)\right|
 \le\varepsilon\qquad(1\le j\le q).
 \tag{BC8}
\]
For each finite family and positive error, the corresponding weakly closed constraints in \(C\) are consequently nonempty. They have the finite intersection property: combine finitely many families and take the smallest error. Compactness of \(C\) gives a point satisfying all such constraints. Letting the error range over \(1/n\) gives \(b\in C\) with every required scalar value. Set \(A(f)x=ab\). This constructs the vector in \(E\), not merely in its bidual.

For real \(f\), subtract the constructions for \(f_+\) and \(f_-\). For complex \(f\), also subtract the constructions for the positive and negative parts of its imaginary part and multiply their difference by \(i\). All four parts are continuous and have support in \(S\). Formula (BC7) holds, and uniqueness by separation makes the construction independent of the decomposition. The same scalar formula proves linearity in \(f\) and in \(x\).

The norming formula and (BC2) give the precise estimate
\[
 \|A(f)x\|\le M_S\|f\|_{L^1(m)}\|x\|,
 \qquad \|A(f)\|\le M_S\|f\|_1.
 \tag{BC9}
\]
For \(f=0\) these estimates mean zero. Thus \(A(f)\) is a bounded operator, with a compact-support-dependent bound. No extension to every \(L^1(G)\) function is claimed in the absence of a global operator bound.

<a id="gbac-smoothing"></a>
## 5. Translate the test function to obtain continuous orbits

Let \(L_s f(t)=f(s^{-1}t)\). Applying (BC7) to \(U(s)^*\ell=\ell\circ U(s)\), using the group law, and making a left Haar substitution gives
\[
 \begin{aligned}
 \ell(U(s)A(f)x)
 &=\int f(t)\ell(U(st)x)\,dm(t)\\
 &=\int f(s^{-1}u)\ell(U(u)x)\,dm(u)\\
 &=\ell(A(L_s f)x).
 \end{aligned}
\]
Separation proves
\[
 U(s)A(f)x=A(L_s f)x.
 \tag{BC10}
\]
The substitution uses left translation only; no modular factor is missing and no unimodularity is needed.

Here is the local translation estimate with all supports controlled. Let \(V\) be a compact identity neighbourhood and \(S=\operatorname{supp}f\ne\varnothing\). The set \(T=VS\) is compact: it is the continuous image of the compact product \(V\times S\). It contains both \(S\) and \(sS\) for \(s\in V\). At each \(t\in T\), continuity of
\[
 (s,u)\longmapsto f(s^{-1}u)-f(u)
\]
at \((e,t)\) gives a product neighbourhood on which its absolute value is less than any prescribed \(\varepsilon>0\). Finitely many second-coordinate neighbourhoods cover \(T\); intersect their first-coordinate neighbourhoods with \(\operatorname{int}V\). For all \(s\) there, the bound holds on \(T\). Off \(T\), both terms are zero. Hence
\[
 \|L_s f-f\|_1
 \le m(T)\sup_{t\in T}|f(s^{-1}t)-f(t)|\longrightarrow0.
 \tag{BC11}
\]
The case \(f=0\) is immediate. This is the compact-support part of [L24], Lemma 3.1, with its finite-cover argument displayed; no countable local base or Haar exhaustion is involved.

For \(s\in V\), the difference \(L_s f-f\) is supported in \(T\). Equations (BC9) and (BC10) therefore give
\[
 \|U(s)A(f)x-A(f)x\|
 \le M_T\|x\|\,\|L_s f-f\|_1\longrightarrow0.
 \tag{BC12}
\]
Every orbital average, and every finite linear combination of orbital averages, has a norm-continuous orbit at \(e\).

<a id="gbac-density"></a>
## 6. Density of these vectors and the final estimate

Let \(Y\) be the linear span of all \(A(f)x\), \(f\in C_c(G)\), \(x\in E\). We prove that \(Y\) is norm dense.

Fix a compact identity neighbourhood \(V\). For each open identity neighbourhood \(W\subset\operatorname{int}V\), H0.1 supplies a nonnegative \(h_W\in C_c(G)\), supported in \(W\), with \(h_W(e)=1\). Haar positivity makes its integral positive, and compact support makes it finite. Set
\[
 a_W=h_W/\int h_W\,dm,\qquad
 a_W\ge0,\quad\operatorname{supp}a_W\subset W,\quad\int a_W\,dm=1.
\]
Order these neighbourhoods by reverse inclusion. This is a directed set, with no assertion that a sequence is cofinal. For fixed \(x\in E\), (BC7) gives
\[
 |\ell(A(a_W)x-x)|
 \le\sup_{t\in W}|\ell(U(t)x)-\ell(x)|\longrightarrow0
 \quad(\ell\in E^*).
 \tag{BC13}
\]
The supremum becomes arbitrarily small once \(W\) is contained in a scalar continuity neighbourhood at \(e\). Thus \(A(a_W)x\to x\) weakly. Each average lies in \(Y\). The norm closure \(\overline Y\) is a closed linear subspace and therefore weakly closed by Hahn–Banach; equivalently, apply Mazur's theorem. It contains this weak limit \(x\). Since \(x\) was arbitrary, \(\overline Y=E\).

Finally keep the compact neighbourhood \(V\) and its finite bound \(M_V\). Given \(x\in E\) and \(\varepsilon>0\), choose \(y\in Y\) with
\[
 \|x-y\|<\frac{\varepsilon}{2(M_V+1)}.
\]
By (BC12) and finite linearity, there is an identity neighbourhood inside \(\operatorname{int}V\) on which \(\|U(s)y-y\|<\varepsilon/2\). For such \(s\),
\[
 \begin{aligned}
 \|U(s)x-x\|
 &\le\|U(s)(x-y)\|+\|U(s)y-y\|+\|y-x\|\\
 &\le(M_V+1)\|x-y\|+\|U(s)y-y\|<\varepsilon.
 \end{aligned}
 \tag{BC14}
\]
This proves norm continuity at \(e\). At any \(g\in G\),
\[
 \|U(t)x-U(g)x\|
 \le\|U(g)\|\,\|U(g^{-1}t)x-x\|\longrightarrow0
 \quad(t\to g).
 \tag{BC15}
\]
Every orbit is therefore norm continuous on the whole group, completing the theorem.


<a id="gbac-context"></a>
## Sources and scope

The theorem is the classical continuity equivalence in Takesaki, *Theory of Operator Algebras II*, Chapter X, Proposition 1.2-prime, printed page 239. Its proof uses Arens–Mackey continuity to identify the averages, invoking compact convex hulls, and then continuous vectors. The proof above establishes the needed convex-hull result by atomic probability measures and Eberlein–Šmulian, constructs averages by finite scalar constraints in a compact convex set, and uses an explicit neighbourhood net and local operator estimates. Averaging and density are the classical mathematical mechanisms used here.

The Eberlein–Šmulian proof [WT] explicitly credits R. Whitley, “An elementary proof of the Eberlein–Šmulian theorem,” *Mathematische Annalen* 172 (1967), 116–118, for its proof route. Its freely readable original is linked by the provider through [Göttingen's digitized volume](https://gdz.sub.uni-goettingen.de/id/PPN235181684_0172?tify=%7B%22pages%22:%5B126%5D%7D). The Radon and Haar proofs [HR] retain D. H. Fremlin's comparison references, including [436J](https://www1.essex.ac.uk/maths/people/fremlin/chap43.pdf) and [441C–441E](https://www1.essex.ac.uk/maths/people/fremlin/chap44.pdf). The left-translation and integration lesson cites Dana P. Williams and Siegfried Echterhoff for comparison. These human references accompany the actual programme proofs; none replaces a needed proof.



The argument uses the earlier results in this order: Hahn–Banach/Baire precedes the weak-topology compactness proofs; the measure/topology foundations precede HR and the finite-simple integration method; Sections 2 and 3 precede orbital averaging; averaging precedes smoothing, density and (BC14). Neither predual continuity of normal actions nor real-parameter continuity of automorphisms is a premise. An operator-domain core, a continuous von Neumann core and modular-weight existence are not used.


[HB]: ../../foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-02
[HB4]: ../../foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-04
[HB6]: ../../foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-06
[WT]: ../../foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#oa-fnd-wt-07
[WT3]: ../../foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#oa-fnd-wt-03
[WT4]: ../../foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html#oa-fnd-wt-04
[H0]: OA-FLOW-TOPOLOGY.md#oa-flow.hr.topology
[HR]: OA-FLOW-HR.md#hr-02
[HR6]: OA-FLOW-HR.md#hr-06
[SC]: OA-FLOW-SC.md#sc-03
[SC4]: OA-FLOW-SC.md#sc-04
[SC5]: OA-FLOW-SC.md#sc-05
[CF]: OA-FLOW-CF.md#oa-flow.cf.1
[L24]: OA-FLOW-L24.md#oa-flow.grp.translations
[L24integral]: OA-FLOW-L24.md#oa-flow.grp.vectorintegration
