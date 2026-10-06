# Measures on a compact convex space

**Self-checked by the writing AI.** The proofs are complete relative to their declared inputs.

The state space of a nonseparable algebra need not be metrizable. We therefore construct measures on compact Hausdorff spaces before discussing convex decompositions. The distinction between Borel sets and Baire sets is retained throughout.

The earlier scalar integration programme, Sections 0–2, proves the outer-measure extension and integration theorems on arbitrary measure spaces. Filters and compact products and Dual-ball compactness and the bidual criterion prove compact-product and dual-ball compactness. Those are the measure and compactness inputs below. Finite-dimensional Euclidean completeness and elementary real inequalities are understood. The argument uses the axiom of choice in its Zorn form.

For comparison and credit, Bishop and de Leeuw's freely accessible [1959 paper](https://aif.centre-mersenne.org/item/10.5802/aif.95.pdf), especially Theorems 3.2 and 5.3 and Corollary 5.4, establishes the countable-test route to the nonmetrizable boundary statement. [Davidson and Kennedy, §2.4](https://www.math.uwaterloo.ca/~krdavids/Preprints/DavidsonKennedy_hyperrigidity.v3.pdf), distinguishes maximal measures and their boundary concentration. We give all the arguments needed here, including the compact Hausdorff representation theorem and the common-refinement criterion.

## Continuous cutoffs on compact Hausdorff spaces

Let \(X\) be compact Hausdorff. If \(C\) is closed and \(U\) is open with \(C\subset U\), there is an open \(V\) such that

\[
 C\subset V\subset\overline V\subset U.
 \tag{CB.1}
\]

Here is the separation argument. For a point outside a compact set, separate it from each point of that set by disjoint open neighborhoods, and take a finite subcover on the compact side. The intersection of the finitely many neighborhoods on the first side has closure disjoint from the compact set. Apply this to each point of \(C\) and the compact set \(X\setminus U\), and take a finite union of the resulting neighborhoods. This proves (CB.1).

It also supplies a continuous function \(h:X\to[0,1]\) which equals one on \(C\) and whose support is contained in \(U\). For clarity, the usual continuous separation construction is as follows. Between two disjoint closed sets, use (CB.1) recursively to assign open sets \(V_r\) to the dyadic numbers in \([0,1]\), with \(\overline V_r\subset V_s\) when \(r<s\). The first closed set is contained in \(V_0\), and \(V_1\) avoids the second. Define \(f(x)\) as the infimum of those \(r\) for which \(x\in V_r\), with infimum one for an empty set. Then \(f=0\) on the first set and \(f=1\) on the second. For \(0<a<1\), the sets \(f<a\) are unions of \(V_r\) with \(r<a\), and the sets \(f>a\) are unions of \(X\setminus\overline V_r\) with \(r>a\). Hence \(f\) is continuous. First choose \(W\) with \(C\subset W\subset\overline W\subset U\), and apply this separation to \(C\) and \(X\setminus W\). The function \(h=1-f\) has support in \(\overline W\subset U\).

We shall also need a finite partition on a compact set. Suppose \(C\subset\bigcup_{j=1}^m U_j\), with the \(U_j\) open. Shrink neighborhoods of the individual points of \(C\), choose a finite subcover, and group their closures according to one containing \(U_j\). This gives compact sets \(C_j\subset U_j\) whose union covers \(C\); empty groups can be omitted. Choose cutoffs \(h_j=1\) on \(C_j\), supported in \(U_j\), and put

\[
 \begin{gathered}
 g_j=h_j/H,\\
 H=\max(1,\sum_k h_k)
 \end{gathered}
 \tag{CB.2}
\]

The \(g_j\) are continuous and nonnegative, supported in \(U_j\), and their sum is one on \(C\). Thus a continuous \(f\) supported in \(C\) splits as \(\sum_j fg_j\), with each term supported in the prescribed open set. No countable base for \(X\) has been used.

## Positive functionals are regular Borel measures

**Theorem.** A positive real-linear functional \(L\) on \(C(X,\mathbb R)\) has a unique finite regular Borel representing measure. Its total mass is \(L(1)\). This statement holds for every compact Hausdorff \(X\).

Positivity gives \(|L(f)|\leq L(1)\|f\|_\infty\), by comparison with the two constant functions. If \(L(1)=0\), the zero measure is the required measure; the construction below also covers it.

For open \(U\subset X\), define

\[
 m(U)=\sup L(f),
 \tag{CB.3}
\]

where the supremum is over continuous \(0\leq f\leq1\) with support contained in \(U\). In particular \(m(X)=L(1)\). The partition in CB-01 shows that \(m(U\cup V)\leq m(U)+m(V)\): split each test function on its compact support. For disjoint open sets the reverse inequality follows by adding two nearly optimal tests, whose sum remains at most one. More generally, if \(U\subset\bigcup_{j\geq1}U_j\), any test support in \(U\) has a finite subcover; its finite partition gives
\(m(U)\leq\sum_j m(U_j)\).

For arbitrary \(E\subset X\), set

\[
 \mu^*(E)=\inf_{U\supset E}m(U),
 \tag{CB.4}
\]

where \(U\) is open. This is an outer measure: for countably many \(E_j\), choose open supersets whose values differ from \(\mu^*(E_j)\) by at most \(\varepsilon2^{-j}\), and use the preceding open-cover inequality. Monotonicity and the empty-set condition are immediate. For open \(U\), monotonicity gives \(\mu^*(U)=m(U)\).

An auxiliary inner approximation will prove measurability:

\[
 m(U)=\sup_{C\subset U}\mu^*(C),
 \tag{CB.5}
\]

where \(C\) is compact. The inequality from right to left is monotonicity. For the other one, if \(f\) is a test in (CB.3) and \(C=\operatorname{supp}f\), every open neighborhood of \(C\) admits \(f\) as a test. Hence \(L(f)\leq\mu^*(C)\), and taking the supremum proves (CB.5).

Fix open \(U\), arbitrary \(E\), and \(\varepsilon>0\). Choose open \(V\supset E\) with \(m(V)\leq\mu^*(E)+\varepsilon\). Choose compact \(C\subset V\cap U\) with \(\mu^*(C)\geq m(V\cap U)-\varepsilon\), and shrink \(C\subset W\subset\overline W\subset V\cap U\). The disjoint open sets \(W\) and \(V\setminus\overline W\) give

\[
 \begin{gathered}
 m(V)\geq m(W)\\
 {}+m(V\setminus\overline W),\\
 m(W)\geq\mu^*(C).
 \end{gathered}
 \tag{CB.6}
\]

Since \(E\setminus U\subset V\setminus\overline W\) and \(E\cap U\subset V\cap U\), these inequalities imply
\(\mu^*(E\cap U)+\mu^*(E\setminus U)\leq\mu^*(E)+2\varepsilon\).
Let \(\varepsilon\) decrease to zero. The reverse inequality is outer subadditivity, so \(U\) is Carathéodory measurable. The proved outer-measure theorem in the scalar programme now gives a finite measure \(\mu\) on all Borel sets.

Equation (CB.4) gives outer regularity, and (CB.5) gives inner regularity on open sets. Inner regularity on every Borel set follows from finiteness and outer approximation of its complement: if \(U\supset X\setminus B\) has almost the same measure as that complement, then \(X\setminus U\) is a compact subset of \(B\) with almost the same measure as \(B\).

We verify the integral, rather than infer it from the construction. Suppose \(0\leq f\leq M\), with \(M>0\), and let \(\delta=M/n\). For \(j=1,\ldots,n\), put \(U_j=\{f>j\delta\}\) and choose continuous tests \(h_j\) whose \(L\)-values approach \(m(U_j)=\mu(U_j)\). Pointwise, \(\delta\sum_jh_j\leq f\). Consequently

\[
 L(f)\geq\delta\sum_{j=1}^n\mu(U_j).
 \tag{CB.7}
\]

The step function on the right differs from \(f\) by at most \(\delta\). Letting \(n\) increase gives \(L(f)\geq\int f\,d\mu\). Apply the same inequality to \(M-f\), using \(\mu(X)=L(1)\), to get the reverse inequality. Adding constants proves representation for every real continuous function.

For uniqueness, a finite regular Borel measure satisfies (CB.3) with \(L(f)=\int f\): approximate an open set internally by compact sets and use CB-01's cutoff equal to one on each compact set. Thus its values on open sets, and then on all Borel sets by outer regularity, are determined by \(L\). Complex functionals obtained by complexifying a positive real functional have the corresponding complex integral representation.

Two consequences will be used below. First, the pushforward of a finite regular Borel measure under a continuous map between compact Hausdorff spaces is again regular. For inner regularity, choose a compact subset of the inverse image of a Borel set; its compact image is contained in that Borel set and has at least the mass of the chosen subset. Outer regularity follows by complements and finiteness.

Second, for a bounded upper-semicontinuous real function \(u\),

\[
 \begin{gathered}
 \int u\,d\mu\\
 =\inf_{g\geq u}\int g\,d\mu,
 \end{gathered}
 \tag{CB.8}
\]

where \(g\) is continuous. After adding a constant assume \(0\leq u\leq M\). Its upper-level sets \(F_j=\{u\geq j\delta\}\) are compact. By outer regularity and CB-01 choose continuous \(0\leq h_j\leq1\), equal to one on \(F_j\), whose integrals exceed \(\mu(F_j)\) by arbitrarily small amounts. The continuous function \(\delta+\delta\sum_jh_j\) majorizes \(u\); its integral is at most \(\int u+\delta\mu(X)\) plus those small errors. Let the mesh and errors tend to zero. This proves (CB.8).

## Affine coordinates, barycentres and envelopes

Let \(K\) be a nonempty compact convex subset of a Hausdorff locally convex space, considered as a real space. Write \(\mathcal A\) for its continuous real affine functions. They contain the constants and separate points. To justify separation, for a nonzero difference \(v\) choose a continuous seminorm \(p\) with \(p(v)>0\). The functional \(tv\mapsto tp(v)\) on its real span is dominated by \(p\). The full sublinear Hahn–Banach proof in NP1 extends it with the same domination. Applying domination to both signs gives \(|\ell(w)|\leq p(w)\), so the extension is continuous and separates the original points. The evaluation map embeds \(K\) into \(\mathbb R^{\mathcal A}\); it is a homeomorphism onto its image because it is a continuous injection from a compact space to a Hausdorff space. We may consequently work in these product coordinates.

**Density of affine lattice expressions.** Every continuous real function is a uniform limit of expressions obtained from finitely many members of \(\mathcal A\) by taking minima and maxima. To prove this, fix \(f\in C(K,\mathbb R)\) and \(\varepsilon>0\). For two points \(x,y\), an affine function separating them can be scaled and translated to equal \(f\) at both; if \(x=y\), use the constant \(f(x)\). Fixing \(x\), the open sets on which these two-point functions exceed \(f-\varepsilon\) cover \(K\). A finite subcover and its maximum give a lattice expression \(h_x>f-\varepsilon\) everywhere, with \(h_x(x)=f(x)\). Near \(x\), it is also less than \(f+\varepsilon\). A finite collection of these latter neighborhoods covers \(K\); the minimum of their \(h_x\)'s approximates \(f\) within \(\varepsilon\) everywhere.

Let \(\mathcal C\) denote the continuous convex real functions. The linear space
\(\mathcal D=\mathcal C-\mathcal C\) is a vector lattice: for convex \(f_1,f_2,g_1,g_2\),

\[
 \begin{aligned}
 &\max\bigl(f_1-g_1,\\
 &\qquad f_2-g_2\bigr)\\
 &\quad=\max\bigl(f_1+g_2,\\
 &\qquad f_2+g_1\bigr)\\
 &\qquad{}-g_1-g_2.
 \end{aligned}
 \tag{CB.9}
\]

It contains the affine functions and their finite lattice expressions, so the preceding approximation proves that \(\mathcal D\) is uniformly dense in \(C(K,\mathbb R)\).

By CB-02 and AB-05, the regular Borel probability measures \(\mathcal P(K)\) form a compact space for convergence of integrals of continuous functions. Indeed they correspond exactly to the positive functionals of mass one in the weak-star compact unit ball of \(C(K,\mathbb R)^*\). Positivity and the mass equation are closed conditions.

Every \(\mu\in\mathcal P(K)\) has a unique barycentre \(b(\mu)\in K\), characterized by

\[
 \begin{gathered}
 a(b(\mu))=\int a\,d\mu\\
 (a\in\mathcal A).
 \end{gathered}
 \tag{CB.10}
\]

Here is the existence argument. Given finitely many continuous tests and an error tolerance, partition \(K\) into finitely many Borel sets on each of which those tests have small oscillation; choose one point in each nonempty positive-mass piece. The atomic measure with those masses approximates all the tests. Thus finite atomic probabilities are weak-star dense. Their finite convex-combination barycentres belong to \(K\). Compactness supplies a cluster point, and each affine coordinate of it is the required integral. Coordinates separate points, proving uniqueness. This also proves continuity of \(b:\mathcal P(K)\to K\).

The same finite-atom construction on a closed subset \(C\) proves density of finite atomic measures supported on \(C\) among positive measures supported there, with total mass fixed. Also \(b(\mu)\) lies in the closed convex hull of the support: the finite approximations can be taken on that support.

For \(f\in\mathcal C\), finite Jensen inequalities and the preceding net approximation give

\[
 f(b(\mu))\leq\int f\,d\mu.
 \tag{CB.11}
\]

No vector-valued integration or measurable choice of measures is involved.

We record a useful envelope identity for any continuous real \(g\), convex or not. For \(x\in K\), let \(P_x=\{\mu:b(\mu)=x\}\). This is a nonempty compact set. Then

\[
 \begin{gathered}
 \min_{\mu\in P_x}\mu(g)\\
 =\sup_{\substack{a\in\mathcal A\\a\leq g}}a(x).
 \end{gathered}
 \tag{CB.12}
\]

To prove the nontrivial inequality, consider the compact convex set
\(T=\{(b(\mu),\mu(g)):\mu\in\mathcal P(K)\}\).
A point \((x,r)\) strictly below its fibre can be strictly separated from \(T\) by a function involving finitely many affine coordinates and the last real coordinate. For completeness, finite-coordinate separation here needs only Euclidean geometry: a basic product neighborhood separates the point from the compact set, so its finite-coordinate projection lies outside the corresponding compact convex projection of \(T\). A nearest point in that Euclidean projection exists; expanding squared distance along each line segment gives a strict separating affine functional. Pull it back to \(T\).

Orient the separator as \(\ell(y)+ct\geq d>\ell(x)+cr\). Comparing with a point of \(T\) above the same \(x\) gives \(c>0\). At the point masses \(\delta_y\) it gives the continuous affine minorant \(a(y)=(d-\ell(y))/c\leq g(y)\), and \(a(x)>r\). Let \(r\) increase to the minimum. The other inequality follows by integrating any affine minorant. Reversing signs proves the upper-envelope identity

\[
 \begin{aligned}
 \widehat g(x)&=\max_{\mu\in P_x}\mu(g)\\
 &=\inf_{\substack{a\in\mathcal A\\a\geq g}}a(x).
 \end{aligned}
 \tag{CB.13}
\]

The function \(\widehat g\) is bounded, concave and upper semicontinuous. Concavity follows by mixing maximizing measures. For upper semicontinuity, if \(x_i\to x\), take cluster points of the corresponding maximizing measures; continuity of the barycentre and of integration of \(g\) gives the required upper bound.

There is no hidden extreme-point existence theorem in the boundary arguments below. Every nonempty compact convex set has an extreme point: order its nonempty compact faces by reverse inclusion and use compactness to intersect a chain. A minimal face exists by Zorn. If it contained two different points, an affine function separating them would have a proper nonempty compact maximum face inside it, a contradiction. Thus the minimal face is a singleton. In particular, if \(q:K\to L\) is a continuous affine surjection and \(y\) is extreme in \(L\), its fibre is a compact face of \(K\), so it contains an extreme point of \(K\).

Finally, \(x\) is extreme exactly when \(P_x=\{\delta_x\}\). A nontrivial finite decomposition already proves one direction. For the converse, suppose \(x\) is extreme and \(\mu\in P_x\). If a continuous affine function \(a\) were not constant \(\mu\)-almost everywhere, splitting its distribution at a real threshold would give two positive-mass pieces with different \(a\)-means. Their normalized barycentres would give a nontrivial decomposition of \(x\), impossible. Hence every \(a\) equals \(a(x)\) almost everywhere. For each \(y\ne x\), choose \(a\) distinguishing it from \(x\); a neighborhood of \(y\) on which their values stay separated has measure zero. Every compact subset of \(K\setminus\{x\}\) has a finite cover by such neighborhoods. Inner regularity therefore gives \(\mu(K\setminus\{x\})=0\).

## Maximal measures and countable variance tests

The Choquet order on \(\mathcal P(K)\) is

\[
 \begin{gathered}
 \mu\preceq\nu
 \quad\Longleftrightarrow\\
 \mu(f)\leq\nu(f)\\
 (f\in\mathcal C).
 \end{gathered}
 \tag{CB.14}
\]

Both \(a\) and \(-a\) are convex when \(a\) is affine, so comparable measures have the same barycentre. Antisymmetry follows from density of \(\mathcal D\) and uniqueness in CB-02. Thus this is an order, not merely a preorder.

Every representing measure is dominated by a maximal one. The set of measures above it is compact: it is the intersection of the closed inequalities in (CB.14). For an ordered chain, the upper sets of its members have the finite intersection property, hence a common member by compactness. Zorn supplies a maximal measure. The same argument works in any compact barycentre fibre.

Fix \(a\in\mathcal A\) and a positive integer \(m\). Define the compact set

\[
 \begin{gathered}
 x\in C_{a,m}\quad\Longleftrightarrow\\
 \text{some }\nu\in P_x\text{ has}\\
 \nu(a^2)-a(x)^2\\
 {}\geq1/m.
 \end{gathered}
 \tag{CB.15}
\]

Compactness follows by projecting the closed condition in \(K\times\mathcal P(K)\). We claim that every maximal \(\mu\) satisfies \(\mu(C_{a,m})=0\).

Otherwise let \(\rho\) be its restriction to this compact set, with mass \(c>0\). Approximate \(\rho\) weak-star by finite atomic measures \(\rho_i\) of mass \(c\) supported there. Replace each atom at \(x\) by a witnessing measure in \(P_x\) from (CB.15), multiplied by the atom's mass. The resulting positive measure \(\eta_i\) dominates \(\rho_i\) on every continuous convex function by (CB.11), agrees on every affine function, and gains at least \(c/m\) on \(a^2\). A weak-star cluster point \(\eta\) has all three properties relative to \(\rho\). Thus \(\mu-\rho+\eta\) is a probability measure above \(\mu\), strictly above it on \(a^2\). This contradicts maximality and proves the claim.

If \(K\) is metrizable, choose a countable family \(a_j\in\mathcal A\) separating points. Such a family exists: the sets of pairs distinguished by individual affine functions form an open cover of \(K\times K\setminus\{(x,x)\}\); a countable base gives a countable subcover. A nonextreme point has a nontrivial finite representing measure, and one of the \(a_j\)'s distinguishes its two endpoints. That measure has strictly positive variance for \(a_j\). CB-03 gives the converse for extreme points. Consequently

\[
 \begin{gathered}
 K\setminus\operatorname{ext}K\\
 =\bigcup_{j,m\geq1} C_{a_j,m}.
 \end{gathered}
 \tag{CB.16}
\]

The extreme boundary is a Borel \(G_\delta\), and every maximal measure assigns it mass one.

Conversely, a regular probability measure concentrated on the extreme boundary is maximal. Here the boundary must be measurable; in particular this applies in the metrizable case. Suppose \(\mu\preceq\nu\), and fix \(f\in\mathcal C\). Every finite minimum \(h\) of continuous affine majorants of \(f\) is continuous concave, so

\[
 \begin{aligned}
 \nu(f)&\leq\nu(h)\\
       &\leq\mu(h).
 \end{aligned}
 \tag{CB.17}
\]

These minima decrease, as a directed family, to \(\widehat f\) from (CB.13). Their integrals have infimum \(\mu(\widehat f)\). To justify this net assertion, take a continuous \(k>\widehat f\). At each point some member of the directed family is below \(k\); compactness gives finitely many such choices, and their minimum is below \(k\) everywhere. Equation (CB.8), followed by adding arbitrarily small positive constants, gives the asserted infimum of integrals. At an extreme point, CB-03 gives \(\widehat f=f\). Thus (CB.17) implies \(\nu(f)\leq\mu(f)\), and (CB.14) gives equality. Density of \(\mathcal D\) proves \(\nu=\mu\).

## Boundary concentration without metrizability

A **Baire set** is a member of the sigma-algebra generated by continuous real functions. These sets need not include all Borel sets. We shall prove that every maximal measure gives mass zero to every Baire set disjoint from \(\operatorname{ext}K\).

Start with a closed \(G_\delta\) set \(S\) containing no extreme point. By CB-01, there are continuous \(0\leq g_n\leq1\), decreasing pointwise to \(1_S\): take cutoffs equal to one on \(S\), supported in the first \(n\) defining open neighborhoods, and take successive minima.

We first prove an escape assertion: for each \(x\in S\), some \(\nu\in P_x\) has \(\nu(S)<1\). Suppose the contrary for one \(x\). Then \(\nu(g_n)=1\) for every \(\nu\in P_x\) and every \(n\). By (CB.12), for each \(n,m\) choose an affine \(a_{n,m}\leq g_n\) with \(a_{n,m}(x)>1-1/m\).

Using CB-03's lattice approximation, choose countably many affine functions whose lattice expressions uniformly approximate all the \(g_n\). Add all the \(a_{n,m}\). Their evaluation map \(q:K\to L\) has compact convex metrizable image, after rescaling the countably many bounded coordinates if necessary. Each \(g_n\) is constant on the fibres and descends to a continuous function \(\gamma_n\) on \(L\). Continuity follows because a continuous surjection from a compact space to a Hausdorff space is a quotient map. The set \(S\) is saturated:

\[
 \begin{gathered}
 S=q^{-1}(q(S)),\\
 \gamma_n\downarrow1_{q(S)}.
 \end{gathered}
 \tag{CB.18}
\]

Indeed the limiting values of all the \(g_n\) determine membership in \(S\).

For any representing measure \(\lambda\) of \(q(x)\), integration of the descended affine \(a_{n,m}\)'s gives
\(\lambda(\gamma_n)\geq a_{n,m}(x)>1-1/m\).
Let \(m\) increase, then \(n\) increase. Since \(0\leq\gamma_n\leq1\), scalar monotone convergence applied to \(1-\gamma_n\) shows \(\lambda(q(S))=1\). But CB-04 supplies such a \(\lambda\) concentrated on \(\operatorname{ext}L\). That set is disjoint from \(q(S)\): an extreme point of \(L\) lifts to an extreme point of \(K\) by CB-03, and saturation would place that lift in \(S\). This contradiction proves the escape assertion.

For this \(S\), choose a countable family of affine coordinates \(b_j\) that makes \(S\) saturated; the \(g_n\)-approximation construction just used provides one, without the \(a_{n,m}\). If every \(b_j\) had zero variance in an escaping measure \(\nu\in P_x\), then each would equal \(b_j(x)\) almost everywhere. Their countable intersection would have full measure, placing \(\nu\) on the fibre of \(x\), which is contained in \(S\). This contradicts escape. Hence

\[
 S\subset\bigcup_{j,m\geq1}C_{b_j,m}.
 \tag{CB.19}
\]

CB-04 gives \(\mu(S)=0\) for every maximal \(\mu\).

Now let \(B\) be any Baire set disjoint from the extreme boundary. Its description uses only countably many continuous functions: the sets expressible through some countable subfamily form a sigma-algebra containing every generator. Thus there is a continuous map \(q\) onto a compact metric space \(Y\) and a Borel set \(D\subset Y\) such that \(B=q^{-1}(D)\). The pushforward of \(\mu\) is regular by CB-02. If \(\mu(B)>0\), inner regularity supplies a compact \(F\subset D\) of positive pushforward mass. Then \(q^{-1}(F)\) is a closed \(G_\delta\) subset of \(B\) with positive \(\mu\)-mass, contradicting the preceding paragraph. This proves the Baire assertion.

It provides a precise measure on the boundary even when the boundary is not Borel. Put \(E=\operatorname{ext}K\). A set in the sigma-algebra generated by \(E\) and the Baire sets has the form

\[
 \begin{gathered}
 (B_1\cap E)\\
 {}\cup(B_2\cap E^c),
 \end{gathered}
 \tag{CB.20}
\]

with \(B_1,B_2\) Baire. Assign it the value \(\mu(B_1)\). This is well defined: two choices of \(B_1\) have symmetric difference disjoint from \(E\), so that difference has measure zero. For disjoint sets of form (CB.20), the corresponding \(B_1\)'s intersect only in such null sets; ordinary countable additivity of \(\mu\) then proves countable additivity of this extension. It agrees with \(\mu\) on Baire sets and assigns \(E\) mass one. Equivalently, the boundary carries the measure
\(\mu_E(B\cap E)=\mu(B)\) on traces of Baire sets. This does not assert that \(E\) itself belongs to the original Borel sigma-algebra.

## Common refinements give a unique maximal representing measure

We now give a criterion adapted to equilibrium states. Suppose every two finite convex decompositions of a point of \(K\) admit a common refinement. Explicitly, if
\(x=\sum_i t_i x_i=\sum_j s_j y_j\),
there are nonnegative \(r_{ij}\) and points \(z_{ij}\in K\) for nonzero coefficients such that the row sums are \(t_i\), the column sums are \(s_j\), and

\[
 \begin{aligned}
 t_i x_i&=\sum_jr_{ij}z_{ij},\\
 s_j y_j&=\sum_ir_{ij}z_{ij}.
 \end{aligned}
 \tag{CB.21}
\]

The equations include their coefficient-sum conditions, so they are affine identities independent of the chosen origin. Zero coefficients are omitted.

For \(f\in\mathcal C\), define \(Q_x(f)\) as the supremum of \(\sum_i t_i f(x_i)\) over all finite decompositions of \(x\). It is finite, bounded between the minimum and maximum of \(f\). Refining a decomposition increases its value on a convex function, by finite Jensen. Given almost optimal decompositions for \(f\) and \(g\), a common refinement is at least as good for each. Together with the reverse inequality obtained on each individual decomposition, this proves

\[
 \begin{gathered}
 Q_x(f+g)\\
 =Q_x(f)\\
 {}+Q_x(g).
 \end{gathered}
 \tag{CB.22}
\]

Positive homogeneity, monotonicity and \(Q_x(f+c)=Q_x(f)+c\) follow directly.

Define \(L_x(f-g)=Q_x(f)-Q_x(g)\) on \(\mathcal D\). Additivity shows this is independent of the representation: equality of two differences gives equality after cross-adding their convex terms. If \(f-g\geq0\), monotonicity gives \(L_x(f-g)\geq0\). Thus \(L_x\) is positive, \(L_x(1)=1\), and \(|L_x(h)|\leq\|h\|_\infty\). Uniform approximation extends it uniquely to \(C(K,\mathbb R)\): the norm bound makes the functional values Cauchy and independent of the approximating sequence. Positivity persists, since an approximation to a nonnegative function within \(\varepsilon\) becomes nonnegative after adding the constant \(\varepsilon\). CB-02 gives a regular Borel probability \(\mu_x\). Affine functions have the same value on every decomposition of \(x\), so (CB.10) shows that it represents \(x\).

We prove that it dominates every other representing measure. Fix \(\rho\in P_x\), \(f\in\mathcal C\), and \(\varepsilon>0\). Cover \(K\) by finitely many relatively open convex neighborhoods whose closures have \(f\)-oscillation less than \(\varepsilon\). Such neighborhoods exist in the finite-coordinate product topology, by continuity of \(f\). Partition \(K\) into finitely many Borel pieces subordinate to this cover. A piece of positive mass \(t_i\) has a normalized restricted measure with barycentre \(x_i\). CB-03 places \(x_i\) in the closed convex hull of that piece, hence in the same closed convex neighborhood. Therefore

\[
 \begin{gathered}
 |\rho(f)-S_f|\leq\varepsilon,\\
 S_f=\sum_i t_i f(x_i).
 \end{gathered}
 \tag{CB.23}
\]

The barycentre identities give \(x=\sum_i t_i x_i\). Thus \(\rho(f)\leq Q_x(f)+\varepsilon=\mu_x(f)+\varepsilon\). Let \(\varepsilon\) decrease to zero. This proves \(\rho\preceq\mu_x\).

Consequently \(\mu_x\) is the greatest representing measure in the Choquet order and is the unique maximal one. CB-05 gives its canonical boundary measure on traces of Baire sets. If \(K\) is metrizable, CB-04 identifies maximal measures with regular Borel measures concentrated on the extreme boundary. In that case every point has exactly one such boundary probability.

This is the precise simplex conclusion we shall use. In the general compact Hausdorff case, uniqueness refers to the maximal regular Borel representing measure and the boundary measure induced from it. A claim about arbitrary measures on an unspecified sigma-algebra of a possibly non-Borel extreme boundary would be a different statement.
