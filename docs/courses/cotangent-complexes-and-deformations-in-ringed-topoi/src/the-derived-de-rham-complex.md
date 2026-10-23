# The derived de Rham complex

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

The derived de Rham complex of a map of rings \(A\to B\) of a topos replaces the de Rham complex of \(B\) by the de Rham complexes of a free simplicial resolution of \(B\), assembled into one complex. Its Hodge filtration has the derived exterior powers \(\Lambda^m L_{B/A}[-m]\) of the cotangent complex as graded pieces. This lesson constructs it, proves that it does not depend on the free resolution, together with its Hodge filtration, and computes it in three situations. Over a ring containing \(\mathbb Q\) it is just \(A\), whatever \(B\) is, so the Hodge filtration is far from complete. Its Hodge completion is computed by the Čech–Alexander complexes of the resolution, filtered by divided powers. And for a quotient by a weakly regular ideal the graded pieces are Koszul complexes of divided powers, which have no cohomology in negative degrees.

**Prerequisites.** [*Cotangent complexes of simplicial rings*](cotangent-complexes-of-simplicial-rings.md) (Lemma 1.1, Theorem 3.1, Corollary 3.5); [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md) (Corollary 7.2); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Proposition 2.3, Proposition 3.3, Lemma 4.1, Theorem 4.4); [*Koszul complexes and the shift formulas*](koszul-complexes-and-the-shift-formulas.md) (Proposition 1.1, Lemma 1.2, Theorem 2.1, Theorem 3.2); [*Derived tensor products of simplicial modules*](derived-tensor-products-of-simplicial-modules.md) (Lemma 2.1, Proposition 2.2); [*Filtered and graded powers of complexes*](filtered-and-graded-powers-of-complexes.md) (Proposition 2.8); [*Weakly regular ideals*](weakly-regular-ideals.md) (Definition 2.4, Proposition 4.2); [*Weak complete intersections*](weak-complete-intersections.md) (Definition 2.1, Theorem 4.2); [*The de Rham complex of a formal category with divided powers*](the-de-rham-complex-of-a-formal-category-with-divided-powers.md) (Example 3.5); [*Cohomology of flat formal categories with divided powers*](cohomology-of-flat-formal-categories-with-divided-powers.md) (Theorem 3.5).

## Conventions

\(T\) is a topos and rings are commutative. For a ring \(A\) of \(T\) and a sheaf of sets \(X\), \(A[X]\) is the free \(A\)-algebra on \(X\), and \(\Omega^\bullet_{C/A}\) is the de Rham complex of an \(A\)-algebra \(C\), with \(\Omega^j_{C/A}=\Lambda^j_C\Omega^1_{C/A}\). For a map of rings \(A\to B\), \(P_A(B)\) is the standard resolution and \(L_{B/A}=\Omega^1_{P_A(B)/A}\otimes_{P_A(B)}B\), as in the lesson on cotangent complexes of simplicial rings. A *degreewise free resolution* of \(B\) over \(A\) is a quasi-isomorphism \(P\to B\) of simplicial \(A\)-algebras with every \(P_n\) a free \(A\)-algebra; the standard resolution is one. For a flat simplicial \(B\)-module \(L\), \(\Lambda^mL\) is formed degree by degree; it represents the derived exterior power \(L\Lambda^m\) of Theorem 4.4 of the lesson on non-additive functors, and \(\Lambda^mL_{B/A}\) is the \(m\)-th derived exterior power of the cotangent complex. Complexes are cochain complexes; a simplicial module is regarded as a complex in degrees \(\leq0\) through its unnormalized complex, which has the homology of the normalized one.

## 1. Realizations of simplicial complexes

**Definition 1.1.** Let \(K\) be a simplicial object of the category of complexes of abelian sheaves: complexes \(K_n\) with differential \(d\), and face and degeneracy maps that are maps of complexes. Its *realization* \(|K|\) is the complex with
\[
\begin{aligned}&|K|^k=\bigoplus_{j-n=k}K_n^j,\\&D=\partial+(-1)^nd\ \text{ on }K_n^j,\\&\partial=\textstyle\sum_{i=0}^n(-1)^id_i.\end{aligned}
\]
Since the \(d_i\) commute with \(d\), \(D^2=(-1)^n(\partial d-d\partial)=0\). A family of subcomplexes \(F^rK_n\subseteq K_n\) stable under the simplicial maps gives subcomplexes \(|F^rK|\subseteq|K|\).

**Lemma 1.2.** Let \(f\colon K\to K'\) be a map of simplicial objects of complexes such that every \(f_n\colon K_n\to K'_n\) is a quasi-isomorphism. Then \(|f|\) is a quasi-isomorphism.

**Proof.** Let \(G_N\subseteq|K|\) be the sum of the \(K_n\) with \(n\leq N\). It is a subcomplex, because \(\partial\) lowers \(n\), and \(G_N/G_{N-1}\) is \(K_N[N]\), with differential \((-1)^Nd\). By induction on \(N\) and the five lemma, \(G_N\to G'_N\) is a quasi-isomorphism for every \(N\). The \(G_N\) exhaust \(|K|\) and cohomology commutes with filtered colimits. \(\square\)

**Lemma 1.3.** Let \(K\) be a simplicial object of complexes with an augmentation \(\varepsilon\colon K_0\to C\) to a complex, \(\varepsilon d_0=\varepsilon d_1\), and put \(K_{-1}=C\), \(d_0=\varepsilon\). Suppose there are maps of complexes \(k_n\colon K_n\to K_{n+1}\), \(n\geq-1\), with \(\partial k+k\partial=1\) on the augmented unnormalized complex \(\cdots\to K_1\to K_0\to K_{-1}\to0\). Then the map \(|K|\to C\) given by \(\varepsilon\) on \(K_0\) is a quasi-isomorphism.

**Proof.** The map is a map of complexes because \(\varepsilon\partial=\varepsilon(d_0-d_1)=0\) on \(K_1\). Its cone is, up to a shift, the realization of the augmented object, with \(K_{-1}\) in simplicial degree \(-1\). There \(Dk+kD\) is \(\partial k+k\partial+(-1)^{n+1}(dk-kd)=1\), because the \(k_n\) commute with \(d\). So the cone is contractible. \(\square\)

**Lemma 1.4.** Let \(C\) be a complex and \(\underline C\) the constant simplicial object with value \(C\). The map \(|\underline C|\to C\) given by the identity in simplicial degree \(0\) is a homotopy equivalence, compatible with subcomplexes of \(C\).

**Proof.** On the augmented unnormalized complex of \(\underline C\), \(\partial=\sum_{i=0}^n(-1)^i\) is the identity from simplicial degree \(n\) to \(n-1\) for \(n\) even and \(0\) for \(n\) odd, \(n\geq0\). The maps \(k_n=1\) for \(n\) odd or \(n=-1\), and \(k_n=0\) for \(n\geq0\) even, satisfy \(\partial k+k\partial=1\). Lemma 1.3 applies, and the contraction preserves subcomplexes of \(C\). \(\square\)

## 2. The derived de Rham complex

For a degreewise free resolution \(P\to B\), the de Rham complexes \(\Omega^\bullet_{P_n/A}\) form a simplicial object of complexes \(\Omega^\bullet_{P/A}\), with the Hodge filtration \(F^m\Omega^\bullet_{P_n/A}=\Omega^{\geq m}_{P_n/A}\).

**Definition 2.1.** The *derived de Rham complex* of \(B\) over \(A\) is \(L\Omega^\bullet_{B/A}=|\Omega^\bullet_{P_A(B)/A}|\), with the *Hodge filtration* \(F^mL\Omega^\bullet_{B/A}=|\Omega^{\geq m}_{P_A(B)/A}|\). For a morphism of ringed topoi \(f\colon X\to S\), \(L\Omega^\bullet_{X/S}=L\Omega^\bullet_{\mathcal O_X/f^{-1}\mathcal O_S}\).

The Hodge filtration is decreasing, \(F^0=L\Omega^\bullet_{B/A}\), and each \(F^m\) is a subcomplex; it is exhaustive and separated, but not complete in general (Section 3).

**Proposition 2.2.** For every degreewise free resolution \(P\to B\) and every \(m\geq0\), the graded piece \(\operatorname{gr}^m|\Omega^\bullet_{P/A}|\) is the simplicial module \(\Omega^m_{P/A}\) placed so that \(\Omega^m_{P_n/A}\) sits in degree \(m-n\), and the maps \(\Omega^m_{P/A}\to\Omega^m_{P/A}\otimes_PB=\Lambda^m_BL_{B/A}\) are quasi-isomorphisms. So \(\operatorname{gr}^mL\Omega^\bullet_{B/A}\cong\Lambda^mL_{B/A}[-m]\).

**Proof.** On \(\operatorname{gr}^m\) the differential \(d\) vanishes, so \(\operatorname{gr}^m\) is the unnormalized complex of \(\Omega^m_{P/A}\), shifted by \(m\). The \(P\)-module \(\Omega^m_{P/A}=\Lambda^m_P\Omega^1_{P/A}\) is degreewise free, and \(P\to B\) is a quasi-isomorphism, so \(\Omega^m_{P/A}\to\Omega^m_{P/A}\otimes_PB\) is a quasi-isomorphism by Proposition 2.2 of the lesson on derived tensor products. Exterior powers commute with base change, so the target is \(\Lambda^m_B(\Omega^1_{P/A}\otimes_PB)\), which is \(\Lambda^m_BL_{B/A}\) for the standard resolution. \(\square\)

**Theorem 2.3.** Let \(P'\to B\) be a degreewise free resolution. There is a canonical chain of maps of complexes
\[
L\Omega^\bullet_{B/A}\xleftarrow{\ \beta\ }|\Omega^\bullet_{R/A}|\xrightarrow{\ \alpha\ }|\Omega^\bullet_{P'/A}|,
\]
compatible with the Hodge filtrations, such that \(\alpha\) and \(\beta\) are quasi-isomorphisms on every \(F^m\). In particular the derived de Rham complex, with its Hodge filtration, can be computed with any degreewise free resolution.

**Proof.** *The bisimplicial resolution.* Let \(R=P_A(P')\) be the bisimplicial \(A\)-algebra of Construction 2.1 of the lesson on cotangent complexes of simplicial rings, \(R_{n,m}=P_A(P'_n)_m=G^{m+1}(P'_n)\) with \(G\) the comonad \(C\mapsto A[C]\). The de Rham complexes \(\Omega^\bullet_{R_{n,m}/A}\) form a bisimplicial object of complexes, and \(|\Omega^\bullet_{R/A}|\) is its realization in both simplicial directions: the complex \(\bigoplus\Omega^j_{R_{n,m}/A}\) in degree \(j-n-m\), with differential \(\partial_n+(-1)^n\partial_m+(-1)^{n+m}d\). It is the realization in \(n\) of the realizations in \(m\), and also the realization in \(m\) of the realizations in \(n\), up to the isomorphism that changes signs by \((-1)^{nm}\). The Hodge filtration is the sum of the \(\Omega^{\geq r}\).

*The map \(\alpha\).* Fix \(n\) and choose an isomorphism \(P'_n\cong A[X_n]\). The augmented simplicial algebra \(R_{n,\bullet}\to P'_n\) is the standard resolution of a free algebra, so Lemma 1.1 of the lesson on cotangent complexes of simplicial rings, applied to the functor \(\Omega^\bullet_{-/A}\) with values in complexes, gives a contraction of the augmented unnormalized complex by maps of complexes, compatible with the Hodge filtration. By Lemma 1.3, the realization in \(m\) maps to \(\Omega^\bullet_{P'_n/A}\) by a quasi-isomorphism on every \(F^r\). These maps commute with the simplicial maps in \(n\), the augmentation being natural, although the contractions need not. Lemma 1.2 in the direction \(n\), applied to every \(F^r\), shows that \(\alpha\) is a quasi-isomorphism on every \(F^r\).

*The map \(\beta\).* Fix \(m\). The maps \(P'\to B\) induce \(R_{\bullet,m}\to P_A(B)_m\), with the target constant in \(n\); let \(S_n\) and \(S\) be the underlying sheaves of sets of \(G^m(P'_n)\) and \(G^m(B)\) (for \(m=0\), of \(P'_n\) and \(B\)), so that \(R_{n,m}=A[S_n]\) and \(P_A(B)_m=A[S]\), and the simplicial maps of \(R_{\bullet,m}\) are induced by the maps of sheaves of sets \(S_n\to S_{n'}\). By Theorem 3.1 (1) of the lesson on cotangent complexes of simplicial rings, applied to the square with top row \(A\to P'\), bottom row \(A\to B\), \(u=1_A\) and \(v\colon P'\to B\), the map \(G^m(P')\to G^m(B)\) is a quasi-isomorphism of simplicial rings (for \(m=0\), it is \(v\)). It is a homomorphism of simplicial abelian sheaves, so \(\mathbb Z^{(S_\bullet)}\to\mathbb Z^{(S)}\) is a quasi-isomorphism by Corollary 7.2 of the Whitehead lesson, and so is \(M=A^{(S_\bullet)}\to M_\infty=A^{(S)}\), by Lemma 2.1 of the lesson on derived tensor products, these being degreewise free.

The de Rham complex of a free algebra is graded by the polynomial weight: the part of weight \(w\) of \(\Omega^j_{A[S]/A}\) is \(\operatorname{Sym}^{w-j}_A(A^{(S)})\otimes_A\Lambda^j_A(A^{(S)})\), and \(d\) preserves the weight. Maps of sheaves of sets preserve it too. In weight \(w\), only the degrees \(0\leq j\leq w\) occur, and for each \(j\) the map of simplicial modules
\[
\begin{aligned}&\operatorname{Sym}^{w-j}(M)\otimes\Lambda^j(M)\\&\quad\to\operatorname{Sym}^{w-j}(M_\infty)\otimes\Lambda^j(M_\infty)\end{aligned}
\]
is a quasi-isomorphism: for \(w\geq1\) the functor \(N\mapsto\operatorname{Sym}^{w-j}(N)\otimes\Lambda^j(N)\) is reduced and commutes with restriction and local inductive limits, so Lemma 4.1 of the lesson on non-additive functors applies to the normalized complexes, which consist of flat modules; for \(w=0\) the map is the identity of \(A\). The weight \(w\) part of the realization in \(n\) has a finite filtration by \(j\), and on every graded piece the map is a quasi-isomorphism. So the realization in \(n\) of \(\Omega^{\geq r}_{R_{\bullet,m}/A}\) maps quasi-isomorphically, weight by weight, to that of the constant object \(\Omega^{\geq r}_{P_A(B)_m/A}\), and hence, by Lemma 1.4, to \(\Omega^{\geq r}_{P_A(B)_m/A}\) itself, through the map given in simplicial degree \(0\), for every \(r\). These maps commute with the simplicial maps in \(m\), and Lemma 1.2 in the direction \(m\) shows that \(\beta\) is a quasi-isomorphism on every \(F^r\).

The chain depends only on \(P'\to B\). \(\square\)

So, by Proposition 2.2, \(\operatorname{gr}^m\) of the derived de Rham complex is \(\Lambda^mL_{B/A}[-m]\) whichever degreewise free resolution computes it, and a map of rings \(B\to B'\) over \(A\) induces a map \(L\Omega^\bullet_{B/A}\to L\Omega^\bullet_{B'/A}\) through the functoriality of the standard resolution.

## 3. Characteristic zero

**Lemma 3.1.** Let \(A\) be a ring of \(T\) in which every nonzero integer is invertible, and \(X\) a sheaf of sets. The inclusion \(A\to\Omega^\bullet_{A[X]/A}\) of the constants is a homotopy equivalence of complexes of \(A\)-modules.

**Proof.** Let \(\Omega^j_{(w)}\) be the part of weight \(w\) of \(\Omega^j_{A[X]/A}\), where \(x\in X\) and \(dx\) have weight \(1\). The \(A\)-linear contraction with the Euler derivation, defined on monomials by
\[
\begin{aligned}&\iota(f\,dx_1\wedge\cdots\wedge dx_j)\\&\quad=\sum_{i=1}^j(-1)^{i-1}fx_i\\&\qquad\quad dx_1\wedge\cdots\widehat{dx_i}\cdots\wedge dx_j,\end{aligned}
\]
on the presheaf free algebras and then sheafified, preserves the weight. It satisfies \(d\iota+\iota d=w\) on \(\Omega^\bullet_{(w)}\). Both sides are derivations of degree \(0\) for the product of forms, so it suffices to check this on \(x\) and \(dx\): \(\iota dx=x\), so \((d\iota+\iota d)(x)=x\), and \((d\iota+\iota d)(dx)=d(x)=dx\). The part of weight \(0\) is \(A\) in degree \(0\). So \(h=\sum_{w\geq1}w^{-1}\iota\) on the parts of positive weight satisfies \(dh+hd=1-\pi\), where \(\pi\) is the projection onto the part of weight \(0\), which is \(A\). \(\square\)

**Theorem 3.2.** Let \(A\) be a ring of \(T\) in which every nonzero integer is invertible, and \(B\) an \(A\)-algebra. The map \(A\to L\Omega^\bullet_{B/A}\), the unit in simplicial degree \(0\), is a quasi-isomorphism.

**Proof.** The units \(A\to\Omega^\bullet_{P_n/A}\) form a map from the constant simplicial object \(A\) to \(\Omega^\bullet_{P/A}\), \(P=P_A(B)\), which is a quasi-isomorphism in every simplicial degree by Lemma 3.1. By Lemma 1.2 its realization is a quasi-isomorphism. The realization of the constant simplicial object \(A\) is the unnormalized complex \(\cdots\to A\xrightarrow{1}A\xrightarrow{0}A\), whose only cohomology is \(A\) in degree \(0\), through the inclusion in simplicial degree \(0\). \(\square\)

So in characteristic zero the derived de Rham complex keeps no information about \(B\), although its graded pieces \(\Lambda^mL_{B/A}[-m]\) do (Example 5.6). The Hodge filtration is then far from complete, and the Hodge completion is the object of interest.

## 4. The Hodge completion

**Definition 4.1.** The *Hodge-completed derived de Rham complex* \(\widehat{L\Omega}^\bullet_{B/A}\) is the inverse system of complexes \((L\Omega^\bullet_{B/A}/F^mL\Omega^\bullet_{B/A})_{m\geq1}\), with the filtrations induced by \(F^r\). A map of such inverse systems is a *filtered quasi-isomorphism* if it is a quasi-isomorphism on every \(F^r/F^m\), \(r<m\).

By Theorem 2.3, any degreewise free resolution computes \(\widehat{L\Omega}^\bullet_{B/A}\) up to canonical filtered quasi-isomorphism, and each \(L\Omega^\bullet_{B/A}/F^m\) has a finite filtration with graded pieces \(\Lambda^iL_{B/A}[-i]\), \(i<m\). Working with the inverse system, rather than a limit in the derived category, keeps everything at finite levels.

**Theorem 4.2.** Let \(P\to B\) be a degreewise free resolution, and for every \(n\) let \(C_{P_n/A}\) be the Čech–Alexander complex of \(P_n\) over \(A\), with augmentation ideal \(J\) and its divided power filtration \(J^{[r]}\), as in the lessons on formal categories with divided powers. The comparison maps \(p\colon N(C_{P_n/A})\to\Omega^\bullet_{P_n/A}\) of the lesson on cohomology of flat formal categories form a map of simplicial objects of complexes, and induce filtered quasi-isomorphisms
\[
|N(J^{[r]}/J^{[m]})|\longrightarrow|\Omega^{\geq r}_{P/A}/\Omega^{\geq m}_{P/A}|
\]
for \(r<m\),
so that the inverse system \((|N(C_{P/A}/J^{[m]})|)_m\), filtered by the \(J^{[r]}\), is filtered quasi-isomorphic to \(\widehat{L\Omega}^\bullet_{B/A}\).

**Proof.** Each \(P_n\) is a free \(A\)-algebra, so \(\Omega^1_{P_n/A}\) is free, and by Example 3.5 of the lesson on the de Rham complex of a formal category with divided powers the de Rham complex of the Čech–Alexander category of \(P_n/A\) is \(\Omega^\bullet_{P_n/A}\). By Theorem 3.5 of the lesson on cohomology of flat formal categories, \(p\) is a quasi-isomorphism from \(N(J^{[r]}/J^{[m]})\) to \(\Omega^{\geq r}_{P_n/A}/\Omega^{\geq m}_{P_n/A}\) for all \(r<m\). The Čech–Alexander complex and \(p\) are functorial in the algebra, so these maps form maps of simplicial objects of complexes, and Lemma 1.2 applies. \(\square\)

## 5. Weak complete intersections

For a map \(u\colon E\to F\) of modules over a ring \(B\), \(\operatorname{Kos}^\bullet(u)=(\Gamma E\otimes\Lambda F,d)\) is the Koszul complex of divided powers of Proposition 1.1 of the lesson on Koszul complexes, with \(\Gamma^pE\otimes\Lambda^qF\) in cohomological degree \(q\), and \(\operatorname{Kos}^\bullet(u)_n\) its part of weight \(p+q=n\): the complex \(\Gamma^nE\to\Gamma^{n-1}E\otimes F\to\cdots\to\Lambda^nF\) in degrees \(0,\dots,n\).

**Lemma 5.1.** Let \(0\to E\xrightarrow{u}F\xrightarrow{v}G\to0\) be an exact sequence of flat \(B\)-modules and \(n\geq1\). The map \(\operatorname{Kos}^\bullet(u)_n\to\Lambda^nG[-n]\), given by \(\Lambda^nv\) in degree \(n\), is a quasi-isomorphism: the sequence
\[
\begin{gathered}0\to\Gamma^nE\to\Gamma^{n-1}E\otimes F\to\cdots\\\cdots\to E\otimes\Lambda^{n-1}F\to\Lambda^nF\to\Lambda^nG\to0\end{gathered}
\]
is exact.

**Proof.** The map is a map of complexes because \(\Lambda^nv\) kills the image of \(E\otimes\Lambda^{n-1}F\), which consists of the \(u(x)\wedge z\). *Finite free split case.* Suppose \(F=E\oplus G\) with \(u\), \(v\) the inclusion and projection, \(E\) and \(G\) finite free. Then \(u=1_E\oplus(0\to G)\), and by Lemma 1.2 of the lesson on Koszul complexes \(\operatorname{Kos}^\bullet(u)\cong\operatorname{Kos}^\bullet(1_E)\otimes\Lambda G\), with zero differential on \(\Lambda G\). Theorem 2.1 there, applied to the exact sequence \(0\to0\to E\xrightarrow{1}E\to0\), shows that the part of weight \(a\geq1\) of \(\operatorname{Kos}^\bullet(1_E)\) is acyclic; it is a bounded complex of finite free modules, so locally contractible. Hence the weight \(n\) part of \(\operatorname{Kos}^\bullet(u)\) is quasi-isomorphic to the weight \(0\) part of \(\operatorname{Kos}^\bullet(1_E)\), namely \(B\) in degree \(0\), tensored with \(\Lambda^nG\) in degree \(n\), through \(\Lambda^nv\). *General case.* The sequence is a bounded acyclic complex of flat modules, so by Proposition 3.3 of the lesson on non-additive functors it is a local inductive limit of split exact sequences of finite free modules over objects \(U_i\). Koszul complexes, exterior and divided powers commute with local inductive limits, and local inductive limits are exact, as in the proof of Theorem 2.1 of the lesson on Koszul complexes. \(\square\)

**Proposition 5.2.** Let \(u\colon N\to M\) be a map of flat \(B\)-modules and \(K\) the complex \(N\xrightarrow{u}M\) in degrees \(-1\), \(0\). For every \(n\geq0\) there is an isomorphism \(L\Lambda^n(K)\cong\operatorname{Kos}^\bullet(u)_n[n]\) in \(D(B)\), natural in commutative squares of maps of flat modules.

**Proof.** For \(n=0\) both sides are \(B\). Let \(n\geq1\). Let \(C(N)\) be the cone of \(1_N\), the contractible complex \(N\xrightarrow{1}N\) in degrees \(-1\), \(0\), and \(\iota\colon N\to M\oplus C(N)\), \(x\mapsto(u(x),x)\), from \(N\) in degree \(0\). This is an injective map of complexes of flat modules, and its cokernel is \(N\xrightarrow{-u}M\), isomorphic to \(K\) by \(-1\) on \(N\). Applying the Dold–Kan functor \(\Gamma_{\mathrm{DK}}\), which is exact and carries flat complexes to flat simplicial modules, gives an exact sequence of flat simplicial modules
\[
\begin{aligned}0\to\Gamma_{\mathrm{DK}}N&\to\Gamma_{\mathrm{DK}}(M\oplus C(N))\\&\to\Gamma_{\mathrm{DK}}K\to0,\end{aligned}
\]
with \(\Gamma_{\mathrm{DK}}N\) constant.

By Lemma 5.1 in each simplicial degree, the Koszul complexes \(\operatorname{Kos}^\bullet(\Gamma_{\mathrm{DK}}\iota)_n\) form a simplicial object of complexes, finite in the Koszul direction, mapping in each simplicial degree quasi-isomorphically to \(\Lambda^n\Gamma_{\mathrm{DK}}K[-n]\). By Lemma 1.2, the realizations are quasi-isomorphic, and the realization of \(\Lambda^n\Gamma_{\mathrm{DK}}K[-n]\) is \(L\Lambda^n(K)[-n]\) (Theorem 4.4 of the lesson on non-additive functors).

The projection \(M\oplus C(N)\to M\) is a homotopy equivalence of complexes, and its composite with \(\iota\) is \(u\). So the commutative square from \(N\xrightarrow{\iota}M\oplus C(N)\) to \(N\xrightarrow{u}M\), identity on \(N\), induces a map \(\operatorname{Kos}^\bullet(\Gamma_{\mathrm{DK}}\iota)_n\to\operatorname{Kos}^\bullet(u)_n\), the target constant in the simplicial direction. In Koszul degree \(q\) it is \(\Gamma^{n-q}N\otimes\Lambda^q\) of the projection \(\Gamma_{\mathrm{DK}}(M\oplus C(N))\to M\), which is a homotopy equivalence by Proposition 2.3 of the lesson on non-additive functors, tensored with the flat module \(\Gamma^{n-q}N\); so it is a quasi-isomorphism of simplicial modules. Filter both realizations by the Koszul degree, a finite filtration: the graded pieces are the unnormalized complexes of these simplicial modules, shifted, so the map of realizations is a quasi-isomorphism. The realization of the constant object \(\operatorname{Kos}^\bullet(u)_n\) is quasi-isomorphic to \(\operatorname{Kos}^\bullet(u)_n\) by Lemma 1.4. Altogether \(L\Lambda^n(K)[-n]\cong\operatorname{Kos}^\bullet(u)_n\). Every construction is functorial in commutative squares. \(\square\)

**Corollary 5.3.** Let \(u\colon E\to F\) be a map of flat \(B\)-modules, placed in degrees \(0\), \(1\). Then \(L\Gamma^n(E\xrightarrow{u}F)\cong\operatorname{Kos}^\bullet(u)_n\) in \(D(B)\), compatibly with the gradings.

**Proof.** Put \(X=(E\to F)\) in degrees \(0\), \(1\). Then \(X[1]\) is the complex \(E\xrightarrow{-u}F\) in degrees \(-1\), \(0\), and \(\operatorname{Kos}^\bullet(-u)\cong\operatorname{Kos}^\bullet(u)\) by the sign \((-1)^q\) in Koszul degree \(q\). By the shift formula (ii) of Theorem 3.2 of the lesson on Koszul complexes, \(L\Gamma^n(X)\cong L\Lambda^n(X[1])[-n]\), which is \(\operatorname{Kos}^\bullet(u)_n\) by Proposition 5.2. \(\square\)

**Corollary 5.4.** Let \(A\to C\to B\) be maps of rings of \(T\), with \(C\to B\) surjective with weakly regular kernel \(I\), such that \(L_{C/A}\to\Omega^1_{C/A}\) is a quasi-isomorphism and \(\Omega^1_{C/A}\) is flat. Then, for every \(n\),
\[
\begin{aligned}&\Lambda^nL_{B/A}[-n]\\&\quad\cong\operatorname{Kos}^\bullet\big(I/I^2\xrightarrow{\ d\ }\Omega^1_{C/A}\otimes_CB\big)_n\end{aligned}
\]
in \(D(B)\), with \(d(\bar f)=df\otimes1\).

**Proof.** By Theorem 4.2 of the lesson on weak complete intersections, \(L_{B/A}\) is isomorphic in \(D(B)\) to the complex \(I/I^2\xrightarrow{d}\Omega^1_{C/A}\otimes_CB\) in degrees \(-1\), \(0\). Both terms are flat: \(I/I^2\) by the definition of weak regularity (Definition 2.4 of the lesson on weakly regular ideals), and \(\Omega^1_{C/A}\otimes_CB\) by base change. Proposition 5.2 applies, and \(\Lambda^nL_{B/A}\) represents \(L\Lambda^n\) of this complex. \(\square\)

**Corollary 5.5.** If \(B\) is a weak complete intersection over \(A\), then \(\operatorname{gr}^nL\Omega^\bullet_{B/A}\) has no cohomology in negative degrees for every \(n\), and neither has \(L\Omega^\bullet_{B/A}/F^mL\Omega^\bullet_{B/A}\) for every \(m\).

**Proof.** By Definition 2.1 of the lesson on weak complete intersections, \(L_{B/A}\) has tor amplitude in \([-1,0]\). By Proposition 2.8 of the lesson on filtered and graded powers, \(L\Lambda^nL_{B/A}\) has tor amplitude in \([-n,0]\), so its cohomology lies in degrees \([-n,0]\), and \(\operatorname{gr}^n=\Lambda^nL_{B/A}[-n]\) has its cohomology in degrees \([0,n]\). The quotient \(L\Omega^\bullet_{B/A}/F^m\) is a finite extension of the \(\operatorname{gr}^n\), \(n<m\). \(\square\)

**Example 5.6.** Let \(f\) be a nonzerodivisor of a ring \(A\), in the sense that \(A\xrightarrow{f}A\) is injective, and \(B=A/fA\). Then \(I=fA\) is weakly regular (Proposition 4.2 of the lesson on weakly regular ideals), and Corollary 5.4 with \(C=A\), \(\Omega^1_{A/A}=0\), gives \(\operatorname{gr}^nL\Omega^\bullet_{B/A}\cong\Gamma^n_B(I/I^2)\) in degree \(0\), a free \(B\)-module of rank \(1\). If every nonzero integer is invertible in \(A\), Theorem 3.2 gives \(L\Omega^\bullet_{B/A}\cong A\). So the graded pieces are nonzero in every degree while the complex is \(A\), whatever \(f\) is: the complex cannot be recovered from its graded pieces, and the Hodge completion of Section 4 is what keeps them.

## 6. Exercises

**Exercise 6.1.** Show that \(L\Omega^\bullet_{A/A}\cong A\) for every ring \(A\), and that \(L\Omega^\bullet_{B/A}\cong\Omega^\bullet_{B/A}\), with its Hodge filtration, when \(B\) is a free \(A\)-algebra.

**Exercise 6.2.** In Example 5.6, show that \(L\Omega^\bullet_{B/A}/F^m\) has cohomology only in degree \(0\), and that \(H^0(L\Omega^\bullet_{B/A}/F^m)\) has a filtration of length \(m\) with graded pieces \(\Gamma^n_B(I/I^2)\), \(0\leq n<m\).

## 7. Complete solutions

**Solution 6.1.** The constant simplicial algebra \(B\) is a degreewise free resolution of \(B\) when \(B\) is free over \(A\); for \(B=A\) it is free on the empty sheaf. By Theorem 2.3, \(L\Omega^\bullet_{B/A}\) is filtered quasi-isomorphic to the realization of the constant simplicial object \(\Omega^\bullet_{B/A}\), and by Lemma 1.4 this realization is homotopy equivalent to \(\Omega^\bullet_{B/A}\), compatibly with the Hodge filtration. For \(B=A\), \(\Omega^\bullet_{A/A}=A\).

**Solution 6.2.** By Example 5.6, every \(\operatorname{gr}^n\) has cohomology only in degree \(0\). Write \(Q_m=L\Omega^\bullet_{B/A}/F^m\). For \(m\geq1\), the exact sequence of complexes \(0\to\operatorname{gr}^m\to Q_{m+1}\to Q_m\to0\) gives a long exact sequence. By induction on \(m\), starting from \(Q_1=\operatorname{gr}^0\cong B\), the cohomology of \(Q_{m+1}\) vanishes outside degree \(0\), and the sequence
\[
\begin{aligned}0\to\Gamma^m_B(I/I^2)&\to H^0(Q_{m+1})\\&\to H^0(Q_m)\to0\end{aligned}
\]
is exact. The kernels of the maps \(H^0(Q_m)\to H^0(Q_n)\), \(n\leq m\), form the filtration.

## Sources

The derived de Rham complex, its Hodge filtration with graded pieces the derived exterior powers of the cotangent complex, its Hodge completion, the comparison with the Čech–Alexander complex and the Koszul description for weak complete intersections are due to Illusie, in his work on the cotangent complex. The comparison of free resolutions through the bisimplicial standard resolution and the polynomial weight applies to the uncompleted complex, whose Hodge filtration is not complete. The triviality of the derived de Rham complex in characteristic zero is due to Bhatt, *p-adic derived de Rham cohomology* ([arXiv:1204.6560](https://arxiv.org/abs/1204.6560)), Section 2.
