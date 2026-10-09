# The uniform commutator estimate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lesson bounded matrix commutators for a II\(_1\) factor acting on finitely many copies of its standard space. This lesson removes every restriction on the von Neumann algebra and its representation [OpenAI-288, Section 7]. The result is the uniform commutator estimate: there is one numerical constant \(C\) such that, for every von Neumann algebra \(P\subseteq B(K)\), every \(Y\in B(K)\) and every matrix \(X\in M_h(P)\),
\[
\|[Y^{(h)},X]\|\le C\,g_P(Y)\,\|X\| .
\]
In other words, the inner derivation \(x\mapsto Yx-xY\) of \(P\) is completely bounded with \(\|\cdot\|_{\rm cb}\le C\|\cdot\|\). The proof treats factors on separable spaces by type: II\(_1\) factors embed into countably many copies of their standard space, properly infinite factors absorb matrices through isometries with orthogonal ranges, and finite type I factors are handled by averaging over their compact unitary groups. The central decomposition then assembles factors, and a separable reduction removes the separability assumption.

We use: Proposition 4.1 of [Matrix commutators in finite factors](matrix-commutators-in-finite-factors.md) and its notation \(g_P\); Proposition 2.2 of [Row, column and cyclic estimates](row-column-and-cyclic-estimates.md), with \(c_{\rm row}=4\sqrt2\); the commutation theorem and the normality of the standard representation, [Theorem 3.1 of Integration for a trace](course:traces-and-noncommutative-integration/integration-for-a-trace-the-commutation-theorem-and-applications#3-the-commutation-theorem); from [Projections and types of von Neumann algebras](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-08), Proposition 18.2 (if a von Neumann algebra has a separating vector, every positive normal functional on it is a vector functional), [Corollary 7.3](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-10) (the types of factors), [Corollary 10.4](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-14) (type I factors are \(B(L)\)) and [Corollary 13.5](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-17) (a properly infinite projection is a sum of countably many mutually orthogonal projections equivalent to it); the central decomposition, [Theorem 4.1, Lemma 3.1 and Fact 1.1 of The central decomposition and the types of the fibres](course:measurable-fields-and-direct-integrals/the-central-decomposition-and-the-types-of-the-fibres#4-the-central-decomposition); and Kaplansky's density theorem, [Theorem 7.1](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences#OA-FND-KD-07), which applies to \(*\)-algebras that are not norm closed; and a left-invariant Haar probability measure on a compact group, Theorem 8.3 of [Haar measure on locally compact groups](course:harmonic-analysis-on-locally-compact-groups/reader/haar-measure-on-locally-compact-groups#OA-FND-HM-05). Set
\[
C_{\rm fac}=3c_1+2,\qquad C=3C_{\rm fac}+2,\qquad c_1=3\pi^2(1+4c_0),\ c_0=4\sqrt2 .
\tag{0.1}
\]
Numerically \(c_1<700\), \(C_{\rm fac}<2102\) and \(C<6308\). Note \(C_{\rm fac}\ge1+2c_{\rm row}\) and \(C_{\rm fac}\ge2\).

## 1. Factors on separable Hilbert spaces

**Proposition 1.1.** Let \(P\subseteq B(K)\) be a factor on a separable Hilbert space. For every \(Y\in B(K)\), \(h\ge1\) and \(X\in M_h(P)\),
\[
\|[Y^{(h)},X]\|\le C_{\rm fac}\,g_P(Y)\,\|X\| .
\]

**Proof.** Put \(\delta=g_P(Y)\). A nonzero factor is finite or properly infinite, and a finite factor is of type II\(_1\) or of type I; a finite type I factor is \(B(L)\) with \(L\) finite-dimensional (Corollaries 7.3 and 10.4 of the projections lesson; \(B(L)\) contains a non-unitary isometry when \(L\) is infinite-dimensional).

*Type II\(_1\).* \(P\) has separable predual. Let \(\lambda:P\to B(L^2(P))\) be the standard representation of its trace; it is a normal \(*\)-isomorphism onto a von Neumann algebra with the separating vector \(1\) (commutation theorem). For \(\xi\in K\), the functional \(\lambda(x)\mapsto\langle x\xi,\xi\rangle\) is positive and normal on \(\lambda(P)\), so by Proposition 18.2 of the projections lesson it is \(\langle\lambda(x)\zeta,\zeta\rangle\) for some \(\zeta\in L^2(P)\). The map \(x\xi\mapsto\lambda(x)\zeta\) is then isometric, since both squared norms are \(\langle x^*x\xi,\xi\rangle\), and it intertwines the two actions of \(P\). By Zorn's lemma \(K\) is an orthogonal sum of cyclic subspaces \(\overline{P\xi_n}\), countably many because \(K\) is separable. Hence there is an isometry of \(K\) into \(\widetilde K=L^2(P)^{\oplus\mathbb N}\) intertwining the action of \(P\) on \(K\) with its common left action on \(\widetilde K\), and its range reduces this action. Transport \(Y\) and extend it by \(0\) on the orthogonal complement of the range; \(g_P\) does not change, because the range projection commutes with \(P\). Let \(p_n\) be the projection onto the first \(n\) copies. It commutes with \(P\), so \([p_nYp_n,x]=p_n[Y,x]p_n\) and \(g_P(p_nYp_n|_{p_n\widetilde K})\le\delta\). Proposition 4.1 of the previous lesson gives \(\|[(p_nYp_n)^{(h)},X]\|\le(3c_1+2)\delta\|X\|\) on \(L^2(P)^n\). For fixed \(X\), these commutators \(p_n^{(h)}[Y^{(h)},X]p_n^{(h)}\) converge strongly to \([Y^{(h)},X]\), and a norm bound passes to strong limits. Restricting to the original space gives the claim with \(3c_1+2=C_{\rm fac}\).

*Properly infinite.* By Corollary 13.5 of the projections lesson, \(1=\sum_ne_n\) with mutually orthogonal \(e_n\sim1\); this gives isometries \(v_1,\dots,v_h\in P\) with orthogonal ranges. The row \(V=(v_1\ \cdots\ v_h):K^h\to K\) satisfies \(V^*V=I\). The map \(\Delta(x)=Yx-xY\) is a rectangular derivation of \(P\) for the identity representation on both sides, with \(\|\Delta\|=\delta\). Proposition 2.2 of the cyclic estimates lesson, applied to the row \(V\) and the column \(V^*\), gives
\[
\|YV-VY^{(h)}\|\le c_{\rm row}\delta,\qquad\|Y^{(h)}V^*-V^*Y\|\le c_{\rm row}\delta .
\]
For \(X\in M_h(P)\), \(VXV^*\in P\) has norm \(\|X\|\), and
\[
[Y,VXV^*]=(YV-VY^{(h)})XV^*+V[Y^{(h)},X]V^*+VX(Y^{(h)}V^*-V^*Y).
\]
Since \(V^*V=I\), \(\|V[Y^{(h)},X]V^*\|=\|[Y^{(h)},X]\|\). Therefore \(\|[Y^{(h)},X]\|\le(1+2c_{\rm row})\delta\|X\|\le C_{\rm fac}\delta\|X\|\).

*Finite type I.* \(P\cong M_n(\mathbb C)\) has a compact unitary group. Let \(Y_0=\int_{\mathcal U(P)}uYu^*\,du\), with Haar probability measure. Then \(Y_0\in P'\) and \(\|Y-Y_0\|\le\sup_u\|uYu^*-Y\|=\sup_u\|[u,Y]\|\le\delta\). Since \([Y^{(h)},X]=[(Y-Y_0)^{(h)},X]\), the commutator has norm at most \(2\delta\|X\|\le C_{\rm fac}\delta\|X\|\). \(\square\)

## 2. The central decomposition

**Proposition 2.1.** Let \(P\subseteq B(K)\) be a von Neumann algebra on a separable Hilbert space. For every \(Y\in B(K)\), \(h\ge1\) and \(X\in M_h(P)\),
\[
\|[Y^{(h)},X]\|\le C\,g_P(Y)\,\|X\| .
\]

**Proof.** Put \(\delta=g_P(Y)\). For a finite partition of unity \(z_1,\dots,z_n\) by central projections, the unitaries \(\sum_j\zeta_jz_j\), \(|\zeta_j|=1\), form a compact group in \(P\), and averaging \(Y\) over it gives \(\sum_jz_jYz_j\). Each conjugate \(uYu^*\) of the average lies within \(\|[u,Y]\|\le\delta\) of \(Y\), so the averages lie within \(\delta\) of \(Y\). Direct the partitions by refinement and let \(Y_1\) be a weak operator cluster point of the averages. Every central projection \(z\) commutes with all averages over partitions refining \(\{z,1-z\}\), so \(Y_1\) commutes with the centre \(Z(P)\). Moreover \(\|Y_1-Y\|\le\delta\) and \(g_P(Y_1)\le g_P(Y)+2\|Y_1-Y\|\le3\delta\).

Take the central decomposition of Theorem 4.1 of the central decomposition lesson: \(K=\int^\oplus K(t)\,d\mu(t)\) with separable fibres, and \(P=\int^\oplus M(t)\) with every \(M(t)\) a factor; the centre is the diagonal algebra, so \(Y_1\), which commutes with it, is decomposable, \(Y_1=\int^\oplus Y_1(t)\) (Fact 1.1(f) there). We show
\[
g_{M(t)}(Y_1(t))\le3\delta\qquad\text{for almost every }t.
\tag{2.1}
\]
Lemma 3.1 of the central decomposition lesson gives a countable unital \(*\)-algebra \(\mathcal Q\subseteq P\) over \(\mathbb Q(i)\), fields \(\beta_b\) representing \(b\in\mathcal Q\), and a null set \(N\) such that for \(t\notin N\) the map \(b\mapsto\beta_b(t)\) is a unital \(*\)-homomorphism of \(\mathbb Q(i)\)-algebras whose image has complex span strongly dense in \(M(t)\). Enlarging \(N\), we may assume \(\|\beta_b(t)\|\le\|b\|\) for \(t\notin N\) and \(b\in\mathcal Q\) (Fact 1.2(b) there).

Let \(\Theta(y)=y(1+y^*y)^{-1/2}\) on a C\*-algebra. It is norm continuous and maps the algebra onto its open unit ball, with inverse \(c\mapsto c(1-c^*c)^{-1/2}\). For \(b\in\mathcal Q\) put \(c_b=\Theta(b)\in P\), a contraction. Choosing polynomials \(q_k\) with rational coefficients converging uniformly to \((1+x)^{-1/2}\) on \([0,\|b\|^2]\), the elements \(bq_k(b^*b)\in\mathcal Q\) converge to \(c_b\) in norm, and their fields converge off \(N\) to \(\Theta(\beta_b(t))\); since the norm of a decomposable operator is the essential supremum of the norms of its fibres (Fact 1.1(e) there), \(c_b\) is represented by \(t\mapsto\Theta(\beta_b(t))\). As \(\|[Y_1,c_b]\|\le3\delta\), the same essential supremum formula gives \(\|[Y_1(t),\Theta(\beta_b(t))]\|\le3\delta\) outside a null set \(N_b\). Let \(t\notin N\cup\bigcup_bN_b\), a countable union of null sets. Let \(A(t)\) be the norm closure of the complex span of \(\{\beta_b(t):b\in\mathcal Q\}\); the set \(\{\beta_b(t)\}\) is norm dense in \(A(t)\), because \(\mathbb Q(i)\) is dense in \(\mathbb C\). By continuity of \(\Theta\), the contractions \(\Theta(\beta_b(t))\) are norm dense in the open, hence in the closed, unit ball of \(A(t)\), and by Kaplansky's density theorem strongly dense in the unit ball of \(M(t)\). A norm bound on commutators passes to strong limits, which proves (2.1).

Each \(M(t)\) is a factor on a separable space, so Proposition 1.1 gives \(\|[Y_1(t)^{(h)},X(t)]\|\le3C_{\rm fac}\delta\|X(t)\|\) for almost every \(t\), where \(X(t)\) is the fibre of \(X\) on \(K(t)^h\), with \(\|X(t)\|\le\|X\|\) almost everywhere. The operator \([Y_1^{(h)},X]\) is decomposable on \(K^h=\int^\oplus K(t)^h\) with these fibres, so its norm is at most \(3C_{\rm fac}\delta\|X\|\). Finally \([Y^{(h)},X]=[Y_1^{(h)},X]+[(Y-Y_1)^{(h)},X]\), and the last term has norm at most \(2\delta\|X\|\). \(\square\)

## 3. Removing separability

**Theorem 3.1** (uniform commutator estimate). For every Hilbert space \(K\), every von Neumann algebra \(P\subseteq B(K)\) with \(1_K\in P\), every \(Y\in B(K)\), every \(h\ge1\) and every \(X\in M_h(P)\),
\[
\|[Y^{(h)},X]\|\le C\,g_P(Y)\,\|X\| .
\tag{3.1}
\]
Equivalently, the derivation \(x\mapsto Yx-xY\) of \(P\) into \(B(K)\) has completely bounded norm at most \(C\) times its norm.

**Proof.** Fix \(h\), \(X\in M_h(P)\) and a unit vector \(\xi=(\xi_1,\dots,\xi_h)\in K^h\). Let \(A_X\subseteq P\) be the unital C\*-algebra generated by the entries of \(X\). The C\*-algebra generated by \(A_X\) and \(Y\) is norm separable, so the closed span \(K_0\) of its images of \(\xi_1,\dots,\xi_h\) is a separable subspace reducing \(A_X\) and \(Y\). Let \(\sigma(a)=a|_{K_0}\) for \(a\in A_X\), \(Y_0=Y|_{K_0}\) and \(P_0=\sigma(A_X)''\subseteq B(K_0)\). For \(a\in A_X\), \(\|[Y_0,\sigma(a)]\|\le g_P(Y)\|a\|\). Every \(b\in\sigma(A_X)\) is \(\sigma(a)\) with \(\|a\|=\|b\|\) (Proposition 17.1 of [C\*-algebras, continuous functional calculus, automatic continuity and positive cones](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-29)), so \(\|[Y_0,b]\|\le g_P(Y)\|b\|\), and by Kaplansky's density theorem \(g_{P_0}(Y_0)\le g_P(Y)\). Proposition 2.1 applied to \(P_0\) and \(\sigma_h(X)\) gives \(\|[Y_0^{(h)},\sigma_h(X)]\|\le Cg_P(Y)\|\sigma_h(X)\|\le Cg_P(Y)\|X\|\). Since \(K_0\) reduces all operators involved and contains every \(\xi_i\), \([Y^{(h)},X]\xi=[Y_0^{(h)},\sigma_h(X)]\xi\). Take the supremum over \(\xi\). \(\square\)

Combined with Arveson's distance formula, Corollary 4.5 of [Completely bounded homomorphisms and similarity](completely-bounded-homomorphisms-and-similarity.md), Theorem 3.1 says: for every von Neumann algebra \(P\subseteq B(K)\) and every \(Y\in B(K)\),
\[
\operatorname{dist}(Y,P')\le\tfrac C2\,g_P(Y).
\tag{3.2}
\]
A C\*-algebra \(A\subseteq B(K)\) has the same commutant and, by Kaplansky's density theorem, the same \(g\) as its weak closure, so (3.2) holds for all C\*-algebras containing \(1_K\) as well.

## 4. Exercises

**Exercise 4.1.** Show that \(g_P(Y)\le2\operatorname{dist}(Y,P')\), and that \(g_P(Y)=0\) if and only if \(Y\in P'\).

**Exercise 4.2.** Let \(P\) be properly infinite. Construct isometries \(v_1,\dots,v_h\in P\) with mutually orthogonal ranges from Corollary 13.5 of the projections lesson.

**Exercise 4.3.** Let \(P=M_n(\mathbb C)\otimes1\) on \(\mathbb C^n\otimes\mathbb C^k\). Compute \(P'\), and show directly that \(Y_0=\int uYu^*\,du\) is the conditional expectation \(Y\mapsto(\operatorname{tr}\otimes\mathrm{id})(Y)\) onto \(P'\) after the identification \(P'=1\otimes M_k(\mathbb C)\).

**Exercise 4.4.** Show that the map \(\Theta(y)=y(1+y^*y)^{-1/2}\) sends every element of a C\*-algebra to its open unit ball, and that \(c\mapsto c(1-c^*c)^{-1/2}\) is its inverse there.

## 5. Solutions

**Solution 4.1.** If \(Z\in P'\), then \([Y,a]=[Y-Z,a]\), of norm at most \(2\|Y-Z\|\|a\|\). If \(g_P(Y)=0\), \(Y\) commutes with the unit ball of \(P\), hence with \(P\).

**Solution 4.2.** Write \(1=\sum_ne_n\) with \(e_n\sim1\) mutually orthogonal, and let \(v_n\) implement \(1\sim e_n\): \(v_n^*v_n=1\), \(v_nv_n^*=e_n\). For \(n\ne n'\), \(v_n^*v_{n'}=v_n^*e_ne_{n'}v_{n'}=0\).

**Solution 4.3.** \(P'=1\otimes M_k(\mathbb C)\). For \(Y=a\otimes b\), the Haar average of \(uau^*\) over \(U(n)\) commutes with all unitaries, so it is a scalar, which equals \(\operatorname{tr}(a)\) by taking traces; hence \(Y_0=\operatorname{tr}(a)1\otimes b\). Extend linearly.

**Solution 4.4.** \(\Theta(y)^*\Theta(y)=(1+y^*y)^{-1/2}y^*y(1+y^*y)^{-1/2}=f(y^*y)\) with \(f(x)=x/(1+x)\), whose values on the spectrum of \(y^*y\) are at most \(\|y\|^2/(1+\|y\|^2)<1\). For \(\|c\|<1\), \(\Theta(c(1-c^*c)^{-1/2})=c(1-c^*c)^{-1/2}(1+(1-c^*c)^{-1/2}c^*c(1-c^*c)^{-1/2})^{-1/2}=c(1-c^*c)^{-1/2}(1-c^*c)^{1/2}=c\), all functions of \(c^*c\) commuting; the other composition is checked in the same way with \(y^*y\).

## References

- [OpenAI-288] OpenAI, Kadison's similarity theorem through uniform derivation estimates, preprint, 23 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026
