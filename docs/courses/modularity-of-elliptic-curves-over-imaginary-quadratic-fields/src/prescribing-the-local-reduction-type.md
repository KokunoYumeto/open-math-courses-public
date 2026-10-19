# Prescribing the local reduction type

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lifting theorem of Lesson 1 asks, at every place above the coefficient prime, that the two Galois representations in a congruence have the same kind of local behaviour: both potentially crystalline and ordinary, both potentially crystalline and not ordinary, or both not potentially crystalline. This lesson arranges this for all character pieces \(V_\theta\) at once. The degeneration of Lesson 3 makes the Jacobian of \(C_n\) specialize to \(E^n\) at the origin of the parameter curve. Finite torsion is locally constant in a \(p\)-adic family, and a sufficiently deep torsion module determines the reduction type of a semistable abelian variety, because only finitely many Frobenius polynomials are possible. Consequently, for parameters \(p\)-adically close to the origin, the Jacobian has the same potential reduction type as \(E^n\): good ordinary, good with all slopes \(\frac12\), or totally toric. These are open conditions on the parameter \(t\), which Lesson 7 combines with Hilbert irreducibility.

**Prerequisites.** [*Two degenerations and a Jacobian of compact type*](two-degenerations-and-a-jacobian-of-compact-type.md), Corollary 2.7, and [*Rank-two systems and their congruences*](rank-two-systems-and-their-congruences.md). From *Local fields*: [*Hensel's lemma, squares and roots of unity in p-adic fields*](course:NT-LOC/NT-LOC-03), Theorem 1.1. From *Galois representations*: [*Weil–Deligne representations and Grothendieck’s monodromy theorem*](course:LG-GAL/weil-deligne-representations-and-monodromy), Theorem 2.2.

**Conventions.** A *local field* is a finite extension of \(\mathbb Q_\ell\) for some prime \(\ell\), the residue characteristic. For a local field \(L\) we write \(v_L\) for its normalized valuation, \(I_L\) for its inertia group and \(Q\) for the cardinality of its residue field. For an abelian variety \(A\) and a prime \(d\), \(V_dA=T_dA\otimes\mathbb Q_d\). In Sections 1–3 the auxiliary prime \(d\) is different from \(\ell\).

## 1. Finite torsion is locally constant

**Lemma 1.1 (local sections of étale maps).** Let \(L\) be a local field, \(f\colon T\to X\) an étale morphism of \(L\)-schemes of finite type, and \(P\in T(L)\) with \(x_0=f(P)\). There are open neighbourhoods \(W\) of \(P\) in \(T(L)\) and \(V\) of \(x_0\) in \(X(L)\) such that \(f\) restricts to a homeomorphism \(W\to V\).

**Proof.** By the local structure of étale morphisms [Stacks, Tag 02GT], there are affine opens \(P\in\operatorname{Spec}B\subset T\) and \(x_0\in\operatorname{Spec}A\subset X\) with \(B=(A[y]/(g))_h\), where \(g\in A[y]\) is monic and its derivative \(g'\) is invertible in \(B\). Embed \(\operatorname{Spec}A\) as a closed subscheme of an affine space, so that \(\operatorname{Spec}A(L)\) carries the topology of \(L^N\), and the coefficients of \(g\) are polynomial functions of \(x\). The point \(P\) is \((x_0,y_0)\) with \(g(x_0,y_0)=0\), \(g'(x_0,y_0)\ne0\) and \(h(x_0,y_0)\ne0\).

Expand \(g(x,y_0+\mu z)=\sum_ka_k(x)\mu^kz^k\), where \(a_k(x)=\frac1{k!}\partial_y^kg(x,y_0)\) depends continuously on \(x\) and \(a_1(x_0)=g'(x_0,y_0)\ne0\). Choose \(\mu\in L^\times\) so small that \(|a_k(x)\mu^{k-1}|\le|a_1(x_0)|\) for all \(k\ge2\) and all \(x\) near \(x_0\), and put
\[
F_x(z)=\frac{g(x,y_0+\mu z)}{a_1(x_0)\,\mu}.
\]
For \(x\) near \(x_0\), \(F_x\) has integral coefficients, \(|F_x'(0)|=|a_1(x)/a_1(x_0)|=1\), and \(|F_x(0)|=|g(x,y_0)|/|a_1(x_0)\mu|<1\), since \(g(x,y_0)\to g(x_0,y_0)=0\). By Newton lifting (Theorem 1.1 of [*Hensel's lemma*](course:NT-LOC/NT-LOC-03)), \(F_x\) has a unique root \(z_x\) with \(|z_x|<1\), and \(|z_x|\le|F_x(0)|\). So \(g(x,\cdot)\) has a unique root \(y(x)\) with \(|y(x)-y_0|<|\mu|\), and \(|y(x)-y_0|\le|\mu|\,|F_x(0)|\to0\) as \(x\to x_0\). Applying the same argument at nearby base points and using uniqueness shows that \(x\mapsto y(x)\) is continuous on a neighbourhood \(V\) of \(x_0\), on which \(h(x,y(x))\ne0\). Then \(W=\{(x,y):x\in V,\)\(\ |y-y_0|<|\mu|\}\cap T(L)\) maps bijectively and continuously onto \(V\), with continuous inverse \(x\mapsto(x,y(x))\). \(\square\)

**Lemma 1.2 (local constancy of finite torsion).** Let \(L\) be a local field, \(X\) an \(L\)-scheme of finite type, \(\mathcal T\to X\) a finite étale commutative group scheme, and \(x_0\in X(L)\). There is an open neighbourhood \(\mathcal N\) of \(x_0\) in \(X(L)\) such that for every \(x\in\mathcal N\),
\[
\mathcal T_x(\overline L)\cong\mathcal T_{x_0}(\overline L)\qquad\text{as }G_L\text{-modules.}
\]

**Proof.** Let \(L'/L\) be a finite Galois extension over which all points of the fibre \(\mathcal T_{x_0}\) are rational, and let \(\delta\) be the degree of \(\mathcal T\) over a neighbourhood of \(x_0\). By Lemma 1.1 over \(L'\), each \(P\in\mathcal T_{x_0}(L')\) has a continuous local section \(s_P\) through \(P\), defined near \(x_0\) in \(X(L')\), with values in a small neighbourhood \(W_P\) of \(P\). Choose the \(W_P\) as balls of a common small radius for a metric on the \(L'\)-points induced by coordinates defined over \(L\); then they are pairwise disjoint, and \(\operatorname{Gal}(L'/L)\) permutes them, since it acts isometrically. For \(x\) near \(x_0\) in \(X(L')\), the \(\delta\) points \(s_P(x)\) are distinct points of the fibre \(\mathcal T_x\), which has \(\delta\) geometric points, so \(\mathcal T_x(\overline L)=\{s_P(x)\}\).

Let \(x\in X(L)\) be near \(x_0\) and \(\sigma\in G_L\). Then \(\sigma(s_P(x))\) lies in \(\mathcal T_x\) and in \(\sigma(W_P)=W_{\sigma P}\), so it equals \(s_{\sigma P}(x)\) by the uniqueness in Lemma 1.1. Likewise \(s_P(x)+s_{P'}(x)\) is a point of \(\mathcal T_x\) close to \(P+P'\), by continuity of the group law, so it equals \(s_{P+P'}(x)\). Hence \(P\mapsto s_P(x)\) is a \(G_L\)-equivariant isomorphism of groups. \(\square\)

## 2. Grothendieck's description of semistable abelian varieties

We use the following results of Grothendieck, in the form surveyed by Illusie, together with Weil's theorem over finite fields.

**Theorem 2.1 (named result N8: semistable abelian varieties).** Let \(L\) be a local field with residue characteristic \(\ell\), \(A/L\) an abelian variety of dimension \(g\), and \(d\ne\ell\) a prime. Write \(U=T_dA\).

1. (Semistable reduction theorem.) \(A\) acquires semistable reduction over a finite extension of \(L\).
2. (Criterion.) \(A\) has semistable reduction over \(L\) if and only if \((\sigma-1)^2=0\) on \(U\) for every \(\sigma\in I_L\). For every abelian variety there is an open subgroup \(I_1\subseteq I_L\) with \((\sigma-1)^2=0\) on \(U\) for \(\sigma\in I_1\).
3. (Filtration.) Suppose \(A\) has semistable reduction, and let the identity component of the special fibre of its Néron model be an extension of an abelian variety \(B\) over the residue field by a torus \(\mathbb T\) of dimension \(r\), the toric rank. Then \(U\) has a \(G_L\)-stable filtration \(W\subseteq V\subseteq U\) with \(V=U^{I_L}=T_d\) of that identity component, \(W=T_d\mathbb T\cong X_*(\mathbb T)\otimes\mathbb Z_d(1)\), \(V/W\cong T_dB\), and \(U/V\cong X^*(\mathbb T')\otimes\mathbb Z_d\), where \(X_*\) and \(X^*\) are cocharacter and character groups and \(\mathbb T'\) is the torus of the dual abelian variety, of the same dimension \(r\). The Galois actions on \(X_*(\mathbb T)\) and \(X^*(\mathbb T')\) are unramified with finite image.
4. (Monodromy.) In the situation of (3), the operator \(N\) with \(\sigma x=x+t_d(\sigma)Nx\) for \(\sigma\in I_L\) has kernel \(V\), image in \(W(-1)\), and induces an injection \(U/V\to W(-1)\); in particular \(N\) has rank \(r\).
5. (Uniformization.) If \(A\) has semistable reduction of toric rank \(g\), then after a finite extension of \(L\) there is a free abelian group \(\Lambda\subset(L^\times)^g\) of rank \(g\) such that \(A(L')=(L'^\times)^g/\Lambda\) for every finite extension \(L'\), compatibly with Galois and with the topologies, the quotient map being a covering map with deck group \(\Lambda\).

Parts (1)–(4) are Grothendieck's results in SGA 7 IX: see Illusie's survey [Ill], Theorems 3.1–3.3, Remark 3.5, (3.4.1)–(3.4.4) and (4.1.3)–(4.1.10), with the references to SGA 7 IX there. Part (5) is Raynaud's uniformization; see [FvdP, Introduction and main theorem]. The course uses them without proof.

**Theorem 2.2 (Weil).** Let \(B\) be an abelian variety over a finite field with \(Q\) elements and \(P_B\) the characteristic polynomial of its Frobenius endomorphism. Then \(P_B\in\mathbb Z[T]\) is monic of degree \(2\dim B\), equal to the characteristic polynomial of Frobenius on \(V_dB\) for every \(d\ne\ell\), and its roots have complex absolute value \(Q^{1/2}\) [Milne, I, Proposition 10.20; II, Theorem 1.1].

## 3. Finitely many Frobenius polynomials

**Lemma 3.1.** Let \(L\) be a local field with residue field of \(Q\) elements, \(g\ge1\), \(d\ne\ell\) a prime, and \(A/L\) a semistable abelian variety of dimension \(g\). Let \(\operatorname{Frob}\in G_L\) be any lift of arithmetic Frobenius and
\[
P_A(T)=\det\bigl(T-\operatorname{Frob}\mid V_dA\bigr).
\]
Then \(P_A\in\mathbb Z[T]\) does not depend on the lift or on \(d\), and it lies in a finite set of polynomials depending only on \(g\) and \(Q\). Exactly \(r\) of its roots have absolute value \(Q\), exactly \(r\) have absolute value \(1\), and \(2(g-r)\) have absolute value \(Q^{1/2}\), where \(r\) is the toric rank. If \(r=0\), then \(A\) has good reduction and \(P_A\) is the polynomial \(P_B\) of Theorem 2.2 for the reduction.

**Proof.** Use the filtration of Theorem 2.1(3). Inertia acts trivially on \(V=U^{I_L}\), and it acts trivially on \(U/V\) because \((\sigma-1)U\subseteq W\subseteq V\) by Theorem 2.1(4). So \(P_A\) is the product of the characteristic polynomials of \(\operatorname{Frob}\) on \(W\), \(V/W\) and \(U/V\), and none of them depends on the lift. On \(W\otimes\mathbb Q_d=X_*(\mathbb T)\otimes\mathbb Q_d(1)\), arithmetic Frobenius acts as \(Q\) times a finite-order automorphism of the lattice \(X_*(\mathbb T)\), so its characteristic polynomial is \(Q^r\) times that of an integral matrix of finite order evaluated at \(T/Q\): integral, independent of \(d\), with roots \(Q\) times roots of unity. On \(U/V\otimes\mathbb Q_d\) it acts through a finite-order automorphism of \(X^*(\mathbb T')\), giving an integral polynomial with roots of unity as roots. On \(V/W\otimes\mathbb Q_d=V_dB\) it acts as the Frobenius of \(B\), with characteristic polynomial \(P_B\), integral, independent of \(d\), with roots of absolute value \(Q^{1/2}\) by Theorem 2.2. This gives integrality, independence of \(d\) and the count of absolute values; the three values \(Q\), \(1\), \(Q^{1/2}\) are distinct since \(Q>1\).

Every root has absolute value at most \(Q\), so the coefficient of \(T^{2g-j}\) has absolute value at most \(\binom{2g}{j}Q^j\). There are finitely many integral monic polynomials of degree \(2g\) with these bounds. If \(r=0\), the identity component of the special fibre is the abelian variety \(B\), so \(A\) has good reduction with reduction \(B\), and \(P_A=P_B\). \(\square\)

For good reduction, the *Newton polygon* of the reduction is the polygon of the \(\ell\)-adic valuations of the roots of \(P_B\), normalized by \(v(Q)=1\). The reduction is *ordinary* when the slopes are \(0\) and \(1\), each with multiplicity \(\dim B\).

**Proposition 3.2 (local constancy of the semistable type).** Let \(L_0\) be a local field, \(X\) a smooth \(L_0\)-curve, \(x_0\in X(L_0)\), and suppose that for every \(N\ge1\) there are a neighbourhood \(X_N\) of \(x_0\) and a finite étale group scheme \(\mathcal T_N\to X_N\) whose fibre at \(x\ne x_0\) is \(A_x[N]\) for a family of abelian varieties \(A_x\) of dimension \(g\), and whose fibre at \(x_0\) is \(A_0[N]\) for an abelian variety \(A_0\) over \(L_0\), compatibly with the maps \(\mathcal T_{NM}\to\mathcal T_N\). Then there are a finite extension \(L/L_0\) and an open neighbourhood \(\mathcal N\) of \(x_0\) in \(X(L_0)\) such that for every \(x\in\mathcal N\setminus\{x_0\}\), \(A_x\) is semistable over \(L\) with the same toric rank as \(A_0\) over \(L\), and, if \(A_0\) has good reduction over \(L\), with the same Newton polygon.

In particular, if \(A_0\cong E_0^g\) for an elliptic curve \(E_0/L_0\), then every \(A_x\) with \(x\in\mathcal N\setminus\{x_0\}\) has, over the same \(L\), the same one of the following properties as \(E_0^g\): good ordinary reduction; good reduction with all Newton slopes \(\frac12\); semistable reduction of toric rank \(g\).

**Proof.** Choose an odd prime \(d\ne\ell\) and a finite extension \(L/L_0\) over which \(A_0\) is semistable (Theorem 2.1(1)) and all points of \(A_0[d]\) are rational. By Lemma 1.2 for \(\mathcal T_d\) over \(L\), all nearby \(A_x\) also have \(A_x[d](\overline L)\) with trivial \(G_L\)-action. Then every \(\sigma\in I_L\) acts on \(T_dA_x\) by a matrix \(1+dM\) with \(M\) integral, so each eigenvalue \(\lambda\) satisfies \(v_d(\lambda-1)\ge1\). By Grothendieck's monodromy theorem (Theorem 2.2 of the Weil–Deligne lesson) the eigenvalues are roots of unity. For odd \(d\) the only root of unity with \(v_d(\lambda-1)\ge1\) is \(1\): a root of unity with nontrivial prime-to-\(d\) part has \(v_d(\lambda-1)=0\), and a primitive \(d^a\)-th root has \(v_d(\lambda-1)=1/(d^{a-1}(d-1))<1\). So \(\sigma\) acts unipotently. By Theorem 2.1(2), \((\tau-1)^2=0\) for \(\tau\) in an open subgroup \(I_1\); writing \(\sigma=\exp(t_d(\sigma)N)\) on the unipotent part shows \(N^2=0\), hence \((\sigma-1)^2=0\) for every \(\sigma\in I_L\). By Theorem 2.1(2), \(A_x\) is semistable over \(L\).

Let \(\mathcal P\) be the finite set of Lemma 3.1 for dimension \(g\) and the residue field of \(L\), and choose \(j\) so large that reduction modulo \(d^j\) is injective on \(\mathcal P\). By Lemma 1.2 for \(\mathcal T_{d^j}\), throughout a smaller neighbourhood \(A_x[d^j]\cong A_0[d^j]\) as \(G_L\)-modules, so \(P_{A_x}\equiv P_{A_0}\pmod{d^j}\), hence \(P_{A_x}=P_{A_0}\). Lemma 3.1 gives the same toric rank and, for good reduction, the same Newton polygon. The inverse image of this neighbourhood under \(X(L_0)\to X(L)\) is a neighbourhood of \(x_0\).

For \(A_0=E_0^g\), choose \(L\) so that \(E_0\) has good or split multiplicative reduction. In the good case \(E_0\) is ordinary, with slopes \(0,1\), or supersingular, with both slopes \(\frac12\), and \(E_0^g\) has the same slopes with multiplicity \(g\). In the multiplicative case \(E_0^g\) has toric rank \(g\). \(\square\)

## 4. Full monodromy in the totally toric case

**Lemma 4.1.** Let \(L\) be a local field with residue characteristic \(\ell\), and \(A/L\) an abelian variety of dimension \(g\) that acquires semistable reduction of toric rank \(g\) over a finite extension. For every prime \(d\), the monodromy operator of the Weil–Deligne representation of \(H^1(A)\) with \(\mathbb Q_d\)-coefficients has rank \(g\). For \(d=\ell\) the Weil–Deligne representation is the one attached by \(\ell\)-adic Hodge theory to the potentially semistable representation \(H^1(A)\).

**Proof.** The rank of monodromy does not change under finite extension, so we may assume that \(A\) has semistable reduction of toric rank \(g\) and a uniformization as in Theorem 2.1(5), with \(\Lambda\) having basis \(\lambda_1,\ldots,\lambda_g\), \(\lambda_j=(q_{1j},\ldots,q_{gj})\in(L^\times)^g\).

For \(d\ne\ell\), Theorem 2.1(4) gives rank \(r=g\) on \(T_dA\), and dualizing gives the same rank on \(H^1(A)\).

First, the matrix \(\bigl(v_L(q_{ij})\bigr)\) is nonsingular. Otherwise there is a nonzero linear form \(\phi\) on \(\mathbb R^g\) vanishing on \(v_L(\Lambda)\), where \(v_L\) is applied coordinatewise. Choose \(y_k\in(L^\times)^g\) with \(\phi(v_L(y_k))\to\infty\). Since \(A(L)\) is compact, a subsequence of the images of \(y_k\) converges, and since the quotient map is a covering map, there are \(\mu_k\in\Lambda\) with \(y_k\mu_k\) convergent in \((L^\times)^g\). But \(\phi(v_L(y_k\mu_k))=\phi(v_L(y_k))\to\infty\), which contradicts convergence.

Next, the \(\ell^k\)-torsion of \(A\) is \(\{y\in(\overline L^\times)^g:\ y^{\ell^k}\in\Lambda\}/\Lambda\), which sits in the exact sequence \(0\to\mu_{\ell^k}^g\to A[\ell^k]\to\Lambda/\ell^k\Lambda\to0\), the last map being \(y\mapsto y^{\ell^k}\). Passing to the limit,
\[
\begin{gathered}
0\longrightarrow\mathbb Q_\ell(1)^g\longrightarrow V_\ell A\\
\longrightarrow\Lambda\otimes\mathbb Q_\ell\longrightarrow0,\quad(4.1)
\end{gathered}
\]
and the extension class of the basis vector \(\lambda_j\) is the vector of Kummer classes \(\bigl(\kappa(q_{ij})\bigr)_i\in H^1(L,\mathbb Q_\ell(1))^g\): if \(y^{\ell^k}=\lambda_j\), then \(\sigma(y)/y\) is the Kummer cocycle.

The representation \(V_\ell A\) is semistable (Theorem 3.2(2) of Lesson 5). Let \(L_0\) be the maximal unramified subfield of \(L\) and \(\sigma\) its Frobenius. Monodromy is zero on the outer terms of (4.1), so it induces an \(L_0\)-linear map
\[
\begin{aligned}
&\nu\colon D_{\mathrm{st}}(\Lambda\otimes\mathbb Q_\ell)=L_0^g\\
&\quad\longrightarrow D_{\mathrm{st}}(\mathbb Q_\ell(1)^g)=L_0^g .
\end{aligned}
\]
On these spaces Frobenius is \(\sigma\) and \(\ell^{-1}\sigma\) respectively, and \(N\varphi=\ell\varphi N\) gives \(\nu\circ\sigma=\sigma\circ\nu\). So \(\ker\nu\) is a \(\sigma\)-stable \(L_0\)-subspace of \(L_0^g\), hence spanned by its \(\mathbb Q_\ell\)-rational vectors (Galois descent for the cyclic extension \(L_0/\mathbb Q_\ell\)). Suppose \(\nu\) has rank less than \(g\); then there is \(0\ne a=(a_j)\in\mathbb Q_\ell^g\cap\ker\nu\). The pullback of (4.1) along the line \(\mathbb Q_\ell a\) is an extension of \(\mathbb Q_\ell\) by \(\mathbb Q_\ell(1)^g\) that is semistable with zero monodromy, hence crystalline. Its \(i\)-th coordinate is the Kummer extension of \(\prod_jq_{ij}^{a_j}\in L^\times\otimes\mathbb Q_\ell\), a quotient of a crystalline representation and therefore crystalline. A Kummer class is crystalline exactly when it comes from \(\mathcal O_L^\times\otimes\mathbb Q_\ell\), that is, when its valuation vanishes (Theorem 4.2(1) below). Hence \(\sum_ja_jv_L(q_{ij})=0\) for every \(i\), contradicting the nonsingularity of \(\bigl(v_L(q_{ij})\bigr)\). So \(\nu\), and hence the monodromy of \(V_\ell A\), has rank \(g\); dualizing gives the same rank on \(H^1(A)\). \(\square\)

The proof used one more fact from \(p\)-adic Hodge theory; we collect it with the facts on crystalline Frobenius used in Section 6.

**Theorem 4.2 (named result N7, second part).** Let \(L\) be a local field with residue characteristic \(\ell\).

1. The classes in \(H^1(L,\mathbb Q_\ell(1))=\widehat{L^\times}\otimes\mathbb Q_\ell\) are all semistable, and the crystalline ones are exactly those coming from \(\mathcal O_L^\times\), that is, the kernel of the valuation [BC, Lemma 8.3.9 and Examples 9.2.8–9.2.9; Ber, Section II.4.4].
2. For a crystalline representation \(V\), the filtered \(\varphi\)-module \(D_{\mathrm{cris}}(V)\) is weakly admissible, and every weakly admissible filtered \(\varphi\)-module arises in this way (Colmez–Fontaine), with subobjects corresponding to subrepresentations [BC, Theorem 9.3.4 and Section 9.3]. Over \(\widehat{L_0^{\mathrm{un}}}\), the completion of the maximal unramified extension of \(L_0\), an isocrystal of slope \(0\) is spanned by \(\varphi\)-fixed vectors (Dieudonné–Manin, [BC, Theorem 8.1.4]); and for an unramified representation \(V\), \(D_{\mathrm{cris}}(V)=(\widehat{L_0^{\mathrm{un}}}\otimes V)^{G_L}\) has all its slopes equal to \(0\) [BC, Example 8.3.2 and Proposition 8.3.4 for dimension one].
3. If \(A/L\) has good reduction \(\widetilde A\), then \(H^1(A)\) is crystalline and the linearized Frobenius on \(D_{\mathrm{cris}}(H^1(A))\) has the same characteristic polynomial as the Frobenius of \(\widetilde A\) on \(H^1\); so its slopes are the Newton slopes of \(\widetilde A\) [Ber, Section II.5.1, for the comparison theorem; KM, Theorem 1, for the characteristic polynomials].

## 5. Open conditions on the parameter

Return to \(K\), \(E\), \(n=3p\) and \(F=K(\mu_n)\). By Corollaries 2.6 and 2.7 of Lesson 3, applied to the constant family with \(m=n\) over \(F\), the torsion of the Jacobians of \(C_{n,R}\) for \(R\) near the origin forms finite étale group schemes \(\mathcal T_N\) with fibre \(E^n[N]\) at \(O\). Proposition 3.2 therefore applies at every completion of \(F\).

**Proposition 5.1.** For every place \(v_0\mid3p\) of \(K\) there is a nonempty open subset \(\Omega_{v_0}\subseteq U(K_{v_0})\) with the following property. If \(t\in U(K)\) lies in \(\Omega_{v_0}\) for every \(v_0\mid3p\), then at every place \(v\mid3p\) of \(F\) the Jacobian \(J_t=\operatorname{Jac}(C_{n,t})\) has the same one of the following potential reduction types as \(E^n\): good ordinary reduction; good reduction with all slopes \(\frac12\); semistable reduction of toric rank \(n\). For each \(v\), the finite extension of \(F_v\) over which these properties hold can be chosen independently of \(t\).

**Proof.** Fix \(v_0\mid3p\). For each place \(v\mid v_0\) of \(F\), Proposition 3.2 over \(F_v\) at the point \(O\) of the parameter curve gives a neighbourhood of \(O\) in \(E(F_v)\) and an extension \(L_v/F_v\). The inverse images of these finitely many neighbourhoods in \(E(K_{v_0})\) intersect in a neighbourhood \(\mathcal N\) of \(O\). Choose \(R_0\in\mathcal N\setminus\{O\}\) in \(E^\circ(K_{v_0})\), possible since the excluded set is finite and \(E(K_{v_0})\) has no isolated points. The map \(x\colon E^\circ\to U\) is étale (Proposition 6.1 of Lesson 2), so by Lemma 1.1 there are a neighbourhood \(\Omega_{v_0}\) of \(x(R_0)\) in \(U(K_{v_0})\) and a continuous section \(t\mapsto R(t)=(t,y(t))\) with values in \(\mathcal N\). For \(t\in\Omega_{v_0}\), the isomorphism \(\phi_{R(t)}\) of Proposition 6.1 of Lesson 2, defined over \(K_{v_0}\), identifies \(C_{n,t}\) with \(C_{n,R(t)}\), so \(J_t\cong J_{R(t)}\) over every \(F_v\), \(v\mid v_0\), and \(J_{R(t)}\) has the required reduction types over \(L_v\). \(\square\)

## 6. The local types of the character pieces

**Corollary 6.1.** Let \(t\) satisfy the conditions of Proposition 5.1 and let \(v\mid3p\) be a place of \(F\) with residue characteristic \(\ell\). Simultaneously for every rotation character \(\theta\):

1. if \(E\) has potentially good ordinary reduction at \(v\), then \(V_{\theta,\ell}|_{G_{F_v}}\) is potentially crystalline and potentially ordinary of weight \(0\);
2. if \(E\) has potentially good supersingular reduction at \(v\), then \(V_{\theta,\ell}|_{G_{F_v}}\) is potentially crystalline and not potentially ordinary of weight \(0\);
3. if \(E\) has potentially multiplicative reduction at \(v\), then for every prime \(d\), including \(d=\ell\), the monodromy of \(V_{\theta,d}|_{G_{F_v}}\) has rank one; in particular \(V_{\theta,\ell}|_{G_{F_v}}\) is not potentially crystalline.

**Proof.** Let \(L/F_v\) be the extension of Proposition 5.1. The rotations are defined over \(F\), so they act on \(D_{\mathrm{cris}}\) or \(D_{\mathrm{st}}\) of \(H^1(J_t)|_{G_L}\) commuting with all structures, and the \(\theta\)-piece of these modules is the corresponding module of \(V_{\theta,\ell}|_{G_L}\).

(1) and (2): \(J_t\) has good reduction over \(L\), so \(H^1(J_t)\) and its summand \(V_{\theta,\ell}\) are crystalline over \(L\), and by Theorem 4.2(3) the slopes of \(D=D_{\mathrm{cris}}(V_{\theta,\ell}|_{G_L})\) are among the Newton slopes of the reduction of \(J_t\). The module \(D\) has rank two over \(E_\lambda\otimes L_0\), where \(E_\lambda\) is the coefficient field, and Hodge–Tate weights \(\{0,1\}\) at every embedding (Proposition 4.2 of Lesson 5); weak admissibility (Theorem 4.2(2)) makes its average slope \(\frac12\).

In the ordinary case the slopes lie in \(\{0,1\}\) and average \(\frac12\), so \(D=D_0\oplus D_1\) with \(D_0\) of slope \(0\) and \(D_1\) of slope \(1\), each of rank one. On \(D_0\) the Hodge filtration has no weight-one part: otherwise the subobject \(D_0\) would have Hodge number exceeding its Newton number \(0\), against weak admissibility. So \(D_0\) is itself weakly admissible, with Hodge–Tate weight \(0\) and slope \(0\), and by Theorem 4.2(2) it is \(D_{\mathrm{cris}}\) of a \(G_L\)-stable \(E_\lambda\)-line \(V_0\subset V_{\theta,\ell}\), with \(V_0=V_{\mathrm{cris}}(D_0)\). This line is unramified. Indeed, by Dieudonné–Manin the space \(\widehat{L_0^{\mathrm{un}}}\otimes_{L_0}D_0\) is spanned by \(\varphi\)-fixed vectors, which form a \(\mathbb Q_\ell\)-space of dimension \(\dim_{L_0}D_0=\dim_{\mathbb Q_\ell}V_0\). They lie in \(V_{\mathrm{cris}}(D_0)\), because the filtration of \(D_0\) is trivial, so they span \(V_0\); and inertia fixes \(\widehat{L_0^{\mathrm{un}}}\) inside \(B_{\mathrm{cris}}\), so it acts trivially on \(V_0\). The same argument applied to the twist \((V_{\theta,\ell}/V_0)\otimes\epsilon_\ell\), which has Hodge–Tate weight \(0\) and slope \(0\), shows that the quotient is \(\epsilon_\ell^{-1}\) times an unramified character. This is the ordinary filtration of weight zero.

In the case of slopes \(\frac12\): if \(V_{\theta,\ell}\) became ordinary over some finite extension \(L'\supseteq L\), its unramified line would have a slope-zero \(D_{\mathrm{cris}}\) (Theorem 4.2(2)) inside \(D_{\mathrm{cris}}(V_{\theta,\ell}|_{G_{L'}})\), whose slopes are all \(\frac12\), since normalized slopes do not change under finite extension. This is impossible.

(3): \(J_t\) acquires semistable reduction of toric rank \(n\). By Lemma 4.1, monodromy has rank \(n\) on the \(2n\)-dimensional space \(H^1(J_t)\), for every coefficient prime \(d\). It commutes with the rotations, so it preserves the \(n\) two-dimensional summands \(V_{\theta,d}\). On \(H^1\) of a semistable abelian variety \(N^2=0\) (Theorem 2.1(2)), so its rank on each summand is at most one. The ranks sum to \(n\) over \(n\) summands, so each is exactly one. Nonzero monodromy persists after finite extension and excludes potential crystallinity. \(\square\)

So the local behaviour at the places above \(3\) and \(p\) is the same for all the systems \(V_\eta,V_\chi,V_\psi,V_1\) of the congruence chain; Lesson 8 transfers it to the automorphic side.

## 7. Exercises

**7.1.** Show that a root of unity \(\lambda\) in \(\overline{\mathbb Q}_d\), \(d\) odd, with \(v_d(\lambda-1)\ge1\) is equal to \(1\), and give an example with \(d=2\) showing why \(d\) is taken odd.

**7.2.** For an elliptic curve with good ordinary reduction over a local field with residue field \(\mathbb F_Q\), write \(P_E(T)=T^2-aT+Q\). Show that ordinarity means \(\ell\nmid a\), and describe \(P_{E^g}\).

**7.3.** Let \(E_q\) be the Tate curve over \(\mathbb Q_\ell\), \(E_q(\overline{\mathbb Q}_\ell)=\overline{\mathbb Q}_\ell^\times/q^{\mathbb Z}\) with \(v(q)>0\). Write down the sequence (4.1) for \(E_q\) and explain why \(V_\ell E_q\) is not crystalline.

**7.4.** Let \(\ell\) be odd, and for \(x\in\mathbb Q_\ell\) with \(0<|x|<1\) let \(E_x\) be the Tate curve with parameter \(x\). Its \(\ell^k\)-torsion is an extension of \(\mathbb Z/\ell^k\) by \(\mu_{\ell^k}\). Fix \(x_1\). Show that for \(x\) with \(|x/x_1-1|<1\), the torsion modules \(E_x[\ell^k]\) and \(E_{x_1}[\ell^k]\) are isomorphic as extensions exactly when \(x\in x_1(1+\ell^{k+1}\mathbb Z_\ell)\). Conclude that the neighbourhood in Lemma 1.2 depends on \(N\).

## 8. Solutions

**7.1.** Write \(\lambda=\lambda_1\lambda_2\) with \(\lambda_1\) of order prime to \(d\) and \(\lambda_2\) of \(d\)-power order. If \(\lambda_1\ne1\), its reduction modulo the maximal ideal is a nontrivial root of unity in the residue field, so \(\lambda-1\) is a unit times \(\lambda_1-1\) plus a nonunit, and \(v_d(\lambda-1)=0\). If \(\lambda=\lambda_2\) is a primitive \(d^a\)-th root of unity with \(a\ge1\), then \(\lambda-1\) generates the prime above \(d\) in \(\mathbb Q_d(\lambda)\), whose ramification index is \(d^{a-1}(d-1)\), so \(v_d(\lambda-1)=1/(d^{a-1}(d-1))\). For odd \(d\) this is less than \(1\). For \(d=2\) and \(\lambda=-1\), \(v_2(\lambda-1)=v_2(-2)=1\), so \(-1\) is not excluded; for \(d=2\) one would need the full level-four structure.

**7.2.** The roots \(\alpha,\beta\) satisfy \(\alpha\beta=Q\), a power of \(\ell\), and \(\alpha+\beta=a\). The reduction is ordinary exactly when one root is an \(\ell\)-adic unit, which happens exactly when \(\ell\nmid a\): if \(\ell\mid a\) and \(\alpha\) were a unit, then \(\beta=a-\alpha\) would be a unit too, contradicting \(v(\alpha\beta)=v(Q)>0\); conversely if \(\ell\nmid a\) the two roots cannot both have positive valuation. Then \(P_{E^g}=P_E^g\), with slopes \(0\) and \(1\), each with multiplicity \(g\).

**7.3.** Here \(g=1\), \(\Lambda=q^{\mathbb Z}\), and (4.1) is \(0\to\mathbb Q_\ell(1)\to V_\ell E_q\to\mathbb Q_\ell\to0\), with extension class the Kummer class \(\kappa(q)\). Since \(v(q)\ne0\), Theorem 4.2(1) shows that the class is not crystalline, so neither is \(V_\ell E_q\); its monodromy has rank one, as Lemma 4.1 predicts.

**7.4.** By (4.1) with \(g=1\) and \(\Lambda=x^{\mathbb Z}\), the class of the extension \(0\to\mu_{\ell^k}\to E_x[\ell^k]\to\mathbb Z/\ell^k\to0\) in \(H^1(\mathbb Q_\ell,\mu_{\ell^k})=\mathbb Q_\ell^\times/\mathbb Q_\ell^{\times\ell^k}\) is the class of \(x\). Two extensions are isomorphic as extensions exactly when their classes agree, that is, when \(x/x_1\in\mathbb Q_\ell^{\times\ell^k}\). For \(|x/x_1-1|<1\) the quotient lies in \(1+\ell\mathbb Z_\ell\), and for odd \(\ell\) the \(\ell^k\)-th powers in \(1+\ell\mathbb Z_\ell\) are exactly \(1+\ell^{k+1}\mathbb Z_\ell\): the map \(u\mapsto u^{\ell^k}\) sends \(1+\ell\mathbb Z_\ell\) onto \(1+\ell^{k+1}\mathbb Z_\ell\), by the binomial theorem and Newton lifting. So the condition is \(x\in x_1(1+\ell^{k+1}\mathbb Z_\ell)\), a disc of radius \(\ell^{-k-1}|x_1|\) that shrinks as \(k\) grows. This is why Proposition 3.2 fixes one level \(d^j\) in advance, using the finiteness of Lemma 3.1.

## Sources

- [OpenAI-030] OpenAI, *Modularity of elliptic curves over imaginary quadratic fields*, OpenAI Math Release preprint, 4 October 2026, Section 7 (prescribing the local reduction type). https://github.com/openai/math/tree/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026
- [Ill] L. Illusie, *Grothendieck and vanishing cycles*, survey, Sections 3 and 4 (Theorems 3.1–3.3, Remark 3.5, (3.4.1)–(3.4.4), (4.1.3)–(4.1.10)), with references to SGA 7 IX. https://www.imo.universite-paris-saclay.fr/~luc.illusie/Illusie-Grothendieck-nearby-cycles12.pdf
- [FvdP] J. Fresnel and M. van der Put, *Uniformisation des variétés abéliennes*, Ann. Fac. Sci. Toulouse Math. (5) S10 (1989), 7–42. http://www.numdam.org/item?id=AFST_1989_5_S10__7_0
- [Milne] J. S. Milne, *Abelian Varieties* (version 2.00, 2008), Chapter I, Proposition 10.20; Chapter II, Theorem 1.1. https://www.jmilne.org/math/CourseNotes/AV.pdf
- [BC] O. Brinon and B. Conrad, *CMI Summer School notes on p-adic Hodge theory*, Theorem 8.1.4, Example 8.3.2, Proposition 8.3.4, Lemma 8.3.9, Examples 9.2.8–9.2.9, Theorem 9.3.4 and Section 9.3. https://math.stanford.edu/~conrad/papers/notes.pdf
- [Ber] L. Berger, *An introduction to the theory of p-adic representations*, Sections II.4.4 and II.5.1. https://arxiv.org/abs/math/0210184
- [KM] N. M. Katz and W. Messing, *Some consequences of the Riemann hypothesis for varieties over finite fields*, Invent. Math. 23 (1974), 73–77, Theorem 1. https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0023/LOG_0010.pdf
- [Stacks] The Stacks project, Tag 02GT (étale morphisms are locally standard étale). https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-locally-standard-etale
