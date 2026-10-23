# Mixed Hom complexes and Ext groups of equivariant modules

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

The two nerves of an equivariant module use different vertices: the nerve places the module at the last vertex of each simplex, the second nerve at the first. A map from the second nerve of \(E\) to the nerve of \(F\) on the level of \(n\)-simplices therefore goes from the first vertex to the last, and these maps form a cosimplicial abelian group. This lesson shows that, under the conditions (I) and (E) of the lesson on cohomology of equivariant modules, its cochain complex computes all the Ext groups of \(E\) and \(F\) as equivariant modules. For a group acting on a point the result is the familiar description of \(\operatorname{Ext}\) over the group ring by cochains of the group with values in Hom groups. The construction rests on a mixed Hom functor, defined for every good fibred topos with values in functors on its index category, and on its compatibility with inverse and direct images, which also holds for unbounded complexes.

**Prerequisites.** [*Cohomology of equivariant modules*](cohomology-of-equivariant-modules.md), in particular the conditions (I) and (E); Lemma 1.2, Definition 2.1 and Proposition 6.2 of [*Equivariant sheaves on simplicial topoi*](equivariant-sheaves-on-simplicial-topoi.md); Propositions 3.1 and 5.1 of [*Nerves of induced and coinduced modules*](nerves-of-induced-and-coinduced-modules.md); Lemma 1.1, Proposition 1.4, Theorem 3.5, Proposition 4.1 and Remark 4.2 of [*Cohomology of total topoi*](cohomology-of-total-topoi.md); Theorem 2.1 of [*Cohomology of simplicial topoi and cohomological descent*](cohomology-of-simplicial-topoi-and-cohomological-descent.md); Lemma 1.2 and Theorem 3.2 of [*Left derived functors of left adjoints on total topoi*](left-derived-functors-of-left-adjoints-on-total-topoi.md); Proposition 1.2, Corollary 2.2, Proposition 3.1 and Proposition 4.2 of [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md); Corollary 4.1 of [*Giraud's characterization of topoi*](giraud-s-characterization-of-topoi.md); Proposition 2.2, Theorem 3.1, Corollary 4.2 and Proposition 4.4 of [*Derived left adjoints on the second total topos and local inductive limits*](derived-left-adjoints-on-the-second-total-topos-and-local-inductive-limits.md); the adjunction between \(Lf^*\) and \(Rf_*\) for a morphism of ringed topoi [[Stacks, Tag 07A6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-adjoint)]; bounded above complexes of flat modules, K-flat complexes and derived pullback [[Stacks, Tag 06YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-bounded-flat-K-flat), [Tag 06YS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-K-flat-resolution), [Tag 0G7E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-pullback-K-flat), [Tag 06YY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-derived-base-change)]; right adjoints of exact functors preserve injectives [[Stacks, Tag 015Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-adjoint-preserve-injectives)]; morphisms into bounded below complexes of injectives [[Stacks, Tag 05TG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-into-injective-complex)]; resolutions by a generating subcategory [[Stacks, Tag 05T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-resolution)]; double complexes with exact columns [[Stacks, Tag 0133](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-double-complex-gives-resolution)].

**Setting.** In Sections 1 and 2, \(X\) is a good topos fibred over a small category \(I\), with a *cartesian* ring \(\mathcal O\) of \(\operatorname{Top}(X)\): a ring whose maps \(f^{-1}\mathcal O_j\to\mathcal O_i\) are isomorphisms. Then the module inverse image \(f^*\) along an arrow \(f\colon i\to j\) is \(f^{-1}\), an exact functor, with a left adjoint \(f_!\) (Lemma 1.2 (1) of the lesson on left derived functors, applied to the morphism of ringed topoi defined by \(f\)). Inverting the maps of \(\mathcal O\) makes it a ring of \(\operatorname{Top}^{\mathrm o}(X)\), also written \(\mathcal O\). As in Proposition 4.2 (a) of the lesson on morphisms of fibred topoi, an \(\mathcal O\)-module \(F\) of \(\operatorname{Top}(X)\) has maps \(F_f\colon f^*F_j\to F_i\), and a module \(E\) of \(\operatorname{Top}^{\mathrm o}(X)\) has maps \(E_f\colon E_i\to f^*E_j\). We write \(\operatorname{Fun}(I^{\mathrm{op}},\operatorname{Ab})\) for the abelian category of functors \(I^{\mathrm{op}}\to\operatorname{Ab}\), and \(\varprojlim\) for the limit over \(I^{\mathrm{op}}\).

## 1. The mixed Hom functor

**Definition 1.1.** For a module \(E\) of \(\operatorname{Top}^{\mathrm o}(X)\) and a module \(F\) of \(\operatorname{Top}(X)\), the functor \(\operatorname{Hom}^!(E,F)\colon I^{\mathrm{op}}\to\operatorname{Ab}\) has the values \(\operatorname{Hom}_{\mathcal O_i}(E_i,F_i)\), and for \(f\colon i\to j\) the map
\[
\begin{gathered}\operatorname{Hom}(E_j,F_j)\longrightarrow\operatorname{Hom}(E_i,F_i),\\ \varphi\longmapsto F_f\circ f^*(\varphi)\circ E_f .\end{gathered}
\]
For complexes \(E\) and \(F\), \(\operatorname{Hom}^!(E,F)\) is the complex of functors whose value at \(i\) is the Hom complex \(\operatorname{Hom}^\bullet(E_i,F_i)\), with the same maps in each degree.

For \(i\xrightarrow{f}j\xrightarrow{g}k\), the identities \(E_{gf}=f^*(E_g)\circ E_f\) and \(F_{gf}=F_f\circ f^*(F_g)\) give
\[
\begin{aligned}&F_{gf}\circ(gf)^*(\varphi)\circ E_{gf}\\&\quad=F_f\circ f^*\bigl(F_g\circ g^*(\varphi)\circ E_g\bigr)\circ E_f,\end{aligned}
\]
so \(\operatorname{Hom}^!(E,F)\) is a functor. It is contravariant in \(E\) and covariant in \(F\).

**Remark 1.2.** An element of \(\varprojlim\operatorname{Hom}^!(E,F)\) is a family of maps \(\varphi_i\colon E_i\to F_i\) with \(\varphi_i=F_f\circ f^*(\varphi_j)\circ E_f\) for every \(f\colon i\to j\). If \(F\) is cartesian, let \(F'\) be the module of \(\operatorname{Top}^{\mathrm o}(X)\) with the same levels and the maps \(F_f^{-1}\); the condition says \(f^*(\varphi_j)\circ E_f=F_f^{-1}\circ\varphi_i\), so \(\varprojlim\operatorname{Hom}^!(E,F)=\operatorname{Hom}_{\operatorname{Top}^{\mathrm o}(X)}(E,F')\). In the same way, if \(E\) is cartesian, the limit is a Hom group in \(\operatorname{Top}(X)\). In general it is neither: \(\operatorname{Hom}^!\) compares objects of two different categories.

**Lemma 1.3.** Every module of \(\operatorname{Top}(X)\) is a submodule of an injective module whose levels are injective \(\mathcal O_i\)-modules, and every injective module of \(\operatorname{Top}(X)\) has injective levels.

**Proof.** The maps \(f^{-1}\mathcal O_j\to\mathcal O_i\) are isomorphisms, so the morphisms of ringed topoi \((X_i,\mathcal O_i)\to(X_j,\mathcal O_j)\) are flat, and Proposition 1.4 (3) of the lesson on cohomology of total topoi gives the first assertion. An injective module \(J\) is then a submodule of such an injective module \(J'\), and the inclusion splits. Each level \(J_i\) is a direct summand of the injective \(\mathcal O_i\)-module \(J'_i\), hence injective. \(\square\)

**Lemma 1.4.** Let \(E\) be a complex of modules of \(\operatorname{Top}^{\mathrm o}(X)\).

1. If \(u\colon F\to F'\) is a quasi-isomorphism between bounded below complexes of modules of \(\operatorname{Top}(X)\) with injective levels, then \(\operatorname{Hom}^!(E,u)\) is a quasi-isomorphism.
2. If \(v\colon E'\to E\) is a quasi-isomorphism and \(F\) is a bounded below complex with injective levels, then \(\operatorname{Hom}^!(v,F)\) is a quasi-isomorphism.

**Proof.** A complex of functors \(I^{\mathrm{op}}\to\operatorname{Ab}\) is exact when its value at every \(i\) is, and the cone of \(\operatorname{Hom}^!(E,u)\) has the value \(\operatorname{Hom}^\bullet(E_i,C_i)\), where \(C_i\) is the cone of \(u_i\). (1) The cone \(C_i\) is a bounded below exact complex of injective \(\mathcal O_i\)-modules. By [Stacks, Tag 05TG], \(\operatorname{Hom}_{K}(C_i,C_i)=\operatorname{Hom}_D(C_i,C_i)=0\), so \(C_i\) is homotopy equivalent to zero, and so is \(\operatorname{Hom}^\bullet(E_i,C_i)\). (2) By [Stacks, Tag 05TG], \(H^k\operatorname{Hom}^\bullet(A,F_i)=\operatorname{Hom}_D(A,F_i[k])\) for every complex \(A\), so \(\operatorname{Hom}^\bullet(\operatorname{cone}(v_i),F_i)\) is exact. \(\square\)

**Definition 1.5.** For \(E\in D(\operatorname{Top}^{\mathrm o}(X))\) and \(F\in D^+(\operatorname{Top}(X))\), put
\[
\begin{aligned}&R\operatorname{Hom}^!(E,F) =\operatorname{Hom}^!(E,J)\\&\quad \in D\bigl(\operatorname{Fun}(I^{\mathrm{op}},\operatorname{Ab})\bigr),\end{aligned}
\]
where \(J\) is a bounded below complex of injective modules of \(\operatorname{Top}(X)\) with a quasi-isomorphism \(F\to J\). By Lemma 1.3 the levels of \(J\) are injective. By Lemma 1.4, \(R\operatorname{Hom}^!\) is a well defined functor \(D(\operatorname{Top}^{\mathrm o}(X))^{\mathrm{op}}\times D^+(\operatorname{Top}(X))\to\) \(D(\operatorname{Fun}(I^{\mathrm{op}},\operatorname{Ab}))\), and for every bounded below complex \(F'\) with injective levels and a quasi-isomorphism \(F\to F'\),
\[
\begin{aligned}&R\operatorname{Hom}^!(E,F)\\&\quad \cong\operatorname{Hom}^!(E,F').\end{aligned} \tag{1.1}
\]
Indeed, \(F\to J\) extends to a map \(F'\to J\) in \(D\), represented by a map of complexes [Stacks, Tag 05TG], which is a quasi-isomorphism between complexes with injective levels.

The functors \(I^{\mathrm{op}}\to\operatorname{Ab}\) are the abelian sheaves on the total topos of the constant fibred topos over \(I\) with value the punctual topos. On that topos every abelian sheaf has totally acyclic levels, so by Theorem 3.5 (2) of the lesson on cohomology of total topoi the derived limit \(R\varprojlim G\) of a bounded below complex \(G\) is the total complex of the Roos complexes \(C^\bullet(G^q)\). For \(I=\Delta^{\mathrm{op}}\) the functors are cosimplicial abelian groups, and by Theorem 2.1 (2) of the lesson on cohomology of simplicial topoi, \(R\varprojlim G\) is the total complex of the cochain complexes of the cosimplicial groups \(G^q\).

## 2. Inverse and direct images

In this section \(f\colon X\to Y\) is an \(I\)-morphism of good topoi fibred over \(I\), with components \(f_i\colon X_i\to Y_i\) and cartesian rings \(\mathcal O_X\), \(\mathcal O_Y\) of \(\operatorname{Top}(X)\), \(\operatorname{Top}(Y)\).

**Lemma 2.1.** Every module of \(\operatorname{Top}^{\mathrm o}(Y)\) is a quotient of a module whose levels are free \(\mathcal O_{Y,i}\)-modules.

**Proof.** For an arrow \(g\colon i\to j\) of \(I\), the module inverse image \(g^*=g^{-1}\) has a left adjoint \(g_!\), as in the Setting, and for an object \(U\) of \(Y_i\), \(g_!(\mathcal O_{Y,i,U})\cong\mathcal O_{Y,j,g_!U}\), where \(\mathcal O_{U}\) is the free module on \(U\) and \(g_!U\) is the left adjoint of \(g^*\) on sheaves of sets: for a module \(G\) of \(Y_j\), \(\operatorname{Hom}(\mathcal O_{Y,j,g_!U},G)=\) \(G(g_!U)=\) \((g^{-1}G)(U)=\) \(\operatorname{Hom}(\mathcal O_{Y,i,U},g^*G)\). So \(g_!\) carries free modules to free modules. Let \(E\) be a module, and for every \(i\) choose an epimorphism \(L_i\to E_i\) from a free module. By Proposition 2.2 (1) of the lesson on derived left adjoints, applied to the identity of \(Y\), the left adjoint \(e^{\mathrm o}_!\) of the level functors has the levels \((e^{\mathrm o}_!L)_j=\bigoplus_{g\colon i\to j}g_!L_i\), which are free. The adjoint map \(e^{\mathrm o}_!L\to E\) is an epimorphism, since on the level \(j\) its restriction to the summand of \(g=\mathrm{id}_j\) is \(L_j\to E_j\). \(\square\)

**Proposition 2.2.** Let \(f^{-1}\mathcal O_Y\to\mathcal O_X\) be a map of rings, compatible with the transition maps, so that every \(f_i\) is a morphism of ringed topoi. For \(L\in D(\operatorname{Top}^{\mathrm o}(Y))\) and \(M\in D^+(\operatorname{Top}(X))\) there is a canonical isomorphism
\[
\begin{gathered}R\operatorname{Hom}^!(L,Rf_*M)\\ \cong R\operatorname{Hom}^!(Lf^*L,M).\end{gathered}
\tag{2.1}
\]
Here \(f^*\) on modules of \(\operatorname{Top}^{\mathrm o}(Y)\) has the levels \(f_i^*L_i\), and \(Lf^*L\) is \(f^*P\) for a K-flat complex \(P\) with flat terms representing \(L\), for instance a bounded above complex with flat levels when \(L\) is bounded above; its levels represent the \(Lf_i^*L_i\).

**Proof.** *The functors.* The module inverse images \(f_i^*\) and the isomorphisms \(g^*f_j^*\cong f_i^*g^*\) of the \(I\)-morphism define \(f^*\) on modules of \(\operatorname{Top}^{\mathrm o}(Y)\), as for sheaves of sets in Proposition 1.2 of the lesson on morphisms of fibred topoi. The categories \(\operatorname{Top}^{\mathrm o}(X)\) and \(\operatorname{Top}^{\mathrm o}(Y)\) are topoi, and every level functor \(i^{\mathrm o*}\) is the inverse image of a morphism of topoi (Corollary 4.1 of [*Giraud's characterization of topoi*](giraud-s-characterization-of-topoi.md)). With the rings, these are morphisms of ringed topoi, and so is the morphism from \(\operatorname{Top}^{\mathrm o}(X)\) to \(\operatorname{Top}^{\mathrm o}(Y)\) of Proposition 3.1 of the lesson on morphisms of fibred topoi, whose module inverse image is \(f^*\), computed on the levels. So \(L\) is represented by a K-flat complex \(P\) with flat terms [Stacks, Tag 06YS], \(Lf^*L=f^*P\) [Stacks, Tag 06YY], and the levels \(P_i\) are K-flat with flat terms [Stacks, Tag 0G7E], so that the levels \(f_i^*P_i\) of \(f^*P\) represent the \(Lf_i^*L_i\). When \(L\) is bounded above, \(P\) may be taken bounded above with flat levels, by Lemma 2.1 and [Stacks, Tag 05T7], such a complex being K-flat [Stacks, Tag 06YQ]. On the other side, \(M\) is represented by a bounded below complex \(J\) of injective modules, with injective levels (Lemma 1.3). The direct image \(f_*J\) of the \(I\)-morphism has the levels \(f_{i*}J_i\) (Corollary 2.2 (b) of the lesson on morphisms of fibred topoi), and \(Rf_*M=f_*J\), with levels representing \(Rf_{i*}M_i\), by Proposition 4.1 and Remark 4.2 of the lesson on cohomology of total topoi.

*The map.* For every \(i\), adjunction gives an isomorphism of complexes
\[
\operatorname{Hom}^\bullet(P_i,f_{i*}J_i)\cong\operatorname{Hom}^\bullet(f_i^*P_i,J_i),
\]
natural in \(P_i\) and \(J_i\). The maps of \(\operatorname{Hom}^!\) are built from the maps of \(P\) and \(f_*J\), respectively \(f^*P\) and \(J\), and from the inverse images \(g^*\); by the naturality of the adjunction and its compatibility with the isomorphisms \(g^*f_j^*\cong f_i^*g^*\), these isomorphisms form an isomorphism of complexes of functors
\[
\Theta\colon\operatorname{Hom}^!(P,f_*J)\xrightarrow{\ \sim\ }\operatorname{Hom}^!(f^*P,J).
\]
By (1.1), the target represents \(R\operatorname{Hom}^!(Lf^*L,M)\).

*The source.* Choose a quasi-isomorphism \(f_*J\to J'\) to a bounded below complex with injective levels, so that \(\operatorname{Hom}^!(P,J')\) represents \(R\operatorname{Hom}^!(L,Rf_*M)\). We show that \(\operatorname{Hom}^!(P,f_*J)\to\operatorname{Hom}^!(P,J')\) is a quasi-isomorphism; then (2.1) is this map followed by the inverse of \(\Theta\) in the derived category. At the level \(i\), on \(H^k\), the map is
\[
\begin{aligned}&\operatorname{Hom}_K(P_i,f_{i*}J_i[k])\\&\quad \longrightarrow\operatorname{Hom}_D(P_i,f_{i*}J_i[k]),\end{aligned}
\]
since \(H^k\operatorname{Hom}^\bullet(P_i,J'_i)=\operatorname{Hom}_D(P_i,J'_i[k])\) by [Stacks, Tag 05TG]. Its composite with \(\operatorname{Hom}_K(f_i^*P_i,J_i[k])\cong\) \(\operatorname{Hom}_K(P_i,f_{i*}J_i[k])\) is the adjunction bijection \(\operatorname{Hom}_D(Lf_i^*L_i,M_i[k])\cong\) \(\operatorname{Hom}_D(L_i,Rf_{i*}M_i[k])\) of [Stacks, Tag 07A6], because \(\operatorname{Hom}_K(f_i^*P_i,J_i[k])=\) \(\operatorname{Hom}_D(f_i^*P_i,J_i[k])\) by [Stacks, Tag 05TG] and the derived adjunction is induced by the adjunction on complexes. So the map is bijective. \(\square\)

**Proposition 2.3.** Assume instead that we are given a map of rings \(\mathcal O_X\to f^{-1}\mathcal O_Y\), so that \(f^*\) is \(f^{-1}\) followed by restriction of scalars, and that the conditions (L), (H\(^{\mathrm o}\)) and (F) of the lesson on derived left adjoints hold. For \(E\in D^-(\operatorname{Top}^{\mathrm o}(X))\) and \(F\in D^+(\operatorname{Top}(Y))\) there is a canonical isomorphism
\[
\begin{gathered}R\operatorname{Hom}^!(Lf_!E,F)\\ \cong R\operatorname{Hom}^!(E,f^*F).\end{gathered}
\tag{2.2}
\]

**Proof.** By Theorem 3.1 of the lesson on derived left adjoints, \(E\) is represented by a bounded above complex \(Q\) of modules \(e^{\mathrm o}_!P\) with \(P\) flat, \(Lf_!E\) is represented by \(f_!Q\), and, \(f\) being an \(I\)-morphism, \((f_!Q)_i=f_{i!}Q_i\) represents \(Lf_{i!}E_i\) (Theorem 3.1 (4) and Proposition 2.2 (2) there). Represent \(F\) by a bounded below complex \(J\) of injective modules; its levels are injective by Lemma 1.3. Adjunction gives, as in the proof of Proposition 2.2, an isomorphism of complexes of functors
\[
\operatorname{Hom}^!(f_!Q,J)\cong\operatorname{Hom}^!(Q,f^*J),
\]
whose source represents \(R\operatorname{Hom}^!(Lf_!E,F)\) by (1.1). Let \(f^*J\to J''\) be a quasi-isomorphism to a bounded below complex with injective levels. It remains to see that \(\operatorname{Hom}^!(Q,f^*J)\to\operatorname{Hom}^!(Q,J'')\) is a quasi-isomorphism, and this is checked at each level \(i\). Theorem 3.2 (3) of the lesson on left derived functors, for the index category with one object and the morphism \(f_i\), whose conditions (L) and (H) are contained in (L) and (H\(^{\mathrm o}\)), shows that \(\operatorname{Hom}^\bullet(Q_i,f_i^*J_i)\to R\operatorname{Hom}(E_i,f_i^*F_i)\) is a quasi-isomorphism: its proof shows exactly this for bounded above complexes of the modules \(Q_i^p\), which satisfy \(\operatorname{Ext}^k(Q_i^p,f_i^*J_i^q)=\operatorname{Ext}^k(f_{i!}Q^p_i,J^q_i)=0\) for \(k\geq1\). The target \(\operatorname{Hom}^\bullet(Q_i,J''_i)\) also represents \(R\operatorname{Hom}(E_i,f_i^*F_i)\), by [Stacks, Tag 05TG], compatibly with the map. \(\square\)

**Proposition 2.4 (exact left adjoints).** In the situation of Proposition 2.3, suppose moreover that every \(f_{i!}\) is exact on modules. Then the left adjoint \(f_!\) of \(f^*\) on modules of the second total topoi is exact, with the levels \((f_!E)_i=f_{i!}E_i\). So \(Lf_!=f_!\) on \(D(\operatorname{Top}^{\mathrm o}(X))\), and (2.2) holds for every \(E\in D(\operatorname{Top}^{\mathrm o}(X))\) and \(F\in D^+(\operatorname{Top}(Y))\).

**Proof.** For an arrow \(g\colon i\to j\), the isomorphism \(g^*f_j^*\cong f_i^*g^*\) of the \(I\)-morphism has a mate \(f_{i!}g^*\to g^*f_{j!}\), adjoint to \(g^*\) of the unit of \(f_{j!}\) followed by this isomorphism. Put \((f_!E)_i=f_{i!}E_i\), with the maps \(f_{i!}E_i\to f_{i!}g^*E_j\to g^*f_{j!}E_j\) given by \(f_{i!}(E_g)\) and the mate. By adjunction at every level, a family of maps \(f_{i!}E_i\to G_i\) compatible with these maps and with those of a module \(G\) of \(\operatorname{Top}^{\mathrm o}(Y)\) is the same as a family of maps \(E_i\to f_i^*G_i\) compatible with the maps of \(E\) and of \(f^*G\). So \(f_!\) is left adjoint to \(f^*\). It is exact, exactness being checked on the levels, so \(Lf_!E=f_!E\) for every complex \(E\). Represent \(F\) by a bounded below complex \(J\) of injective modules, whose levels are injective (Lemma 1.3). Adjunction at every level gives an isomorphism of complexes of functors \(\operatorname{Hom}^!(f_!E,J)\cong\operatorname{Hom}^!(E,f^*J)\), as in the proof of Proposition 2.2, and its source represents \(R\operatorname{Hom}^!(Lf_!E,F)\) by (1.1). The levels \(f_i^*J_i\) of \(f^*J\) are bounded below complexes of injective modules, \(f_i^*\) being right adjoint to the exact functor \(f_{i!}\) [Stacks, Tag 015Z], and \(f^*\) is exact. So by (1.1) the target represents \(R\operatorname{Hom}^!(E,f^*F)\). \(\square\)

## 3. Ext groups of equivariant modules

In Sections 3 and 4, \(X\) is a good pseudo-category with a ring \(\mathcal O\) of \(B'X\), as in the lesson on cohomology of equivariant modules. Since the structure of \(\mathcal O\) is invertible, its nerves are cartesian rings of \(\operatorname{Top}(X)\) and of \(\operatorname{Top}^{\mathrm o}(X)\); on the level \(X_n\) we identify their values \(X(v_n)^*\mathcal O\) and \(X(v_0)^*\mathcal O\) by the transport of \(\mathcal O\) and write \(\mathcal O_n\). The index category is \(\Delta^{\mathrm{op}}\), and a functor \(\Delta\to\operatorname{Ab}\) is a cosimplicial abelian group. For modules \(L\), \(M\) of \(BX\), \(\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}L,\operatorname{ner}M)\) is the cosimplicial group with the values
\[
\operatorname{Hom}\bigl(X(v_0)^*L,X(v_n)^*M\bigr)\quad\text{on }X_n,
\]
and, for \(\alpha\colon[m]\to[n]\), the map
\[
\varphi\longmapsto b_{\alpha(m)\,n}\circ X(\alpha)^*(\varphi)\circ a_{0\,\alpha(0)},
\]
where \(a\) and \(b\) are the transports of \(L\) and \(M\) (Lemma 1.2 and Definition 2.1 of the lesson on equivariant sheaves).

**Lemma 3.1.** For modules \(L\), \(M\) of \(BX\), with structures \(a\) and \(b\), the map
\[
\begin{gathered}\operatorname{Hom}_{BX}(L,M)\\ \longrightarrow\varprojlim\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}L,\operatorname{ner}M),\\ u\longmapsto\bigl(b_{0n}\circ X(v_0)^*(u)\bigr)_n\end{gathered}
\]
is bijective, with inverse \((\varphi_n)_n\mapsto\varphi_0\).

**Proof.** *The image is compatible.* Let \(u\) be a morphism and \(\varphi_n=b_{0n}\circ X(v_0)^*(u)\). For \(\alpha\colon[m]\to[n]\), Lemma 1.2 of the lesson on equivariant sheaves gives \(X(\alpha)^*(b_{0m})=b_{\alpha(0)\alpha(m)}\), \(b_{\alpha(m)n}\circ b_{\alpha(0)\alpha(m)}=b_{\alpha(0)n}\) and \(X(v_k)^*(u)\circ a_{0k}=b_{0k}\circ X(v_0)^*(u)\). Hence
\[
\begin{aligned}&b_{\alpha(m)n}\circ X(\alpha)^*(\varphi_m)\circ a_{0\alpha(0)}\\&\quad=b_{\alpha(0)n}\circ X(v_{\alpha(0)})^*(u)\circ a_{0\alpha(0)}\\&\quad=b_{\alpha(0)n}\circ b_{0\alpha(0)}\circ X(v_0)^*(u)=\varphi_n .\end{aligned}
\]
*Every compatible family comes from \(\varphi_0\).* Let \((\varphi_n)\) be compatible. For the vertex \(v_k\colon[0]\to[n]\), compatibility gives
\[
\varphi_n=b_{kn}\circ X(v_k)^*(\varphi_0)\circ a_{0k}.
\]
For \(k=0\) this says \(\varphi_n=b_{0n}\circ X(v_0)^*(\varphi_0)\). For \(n=1\), the cases \(k=0\) and \(k=1\) give \(b\circ s^*(\varphi_0)=t^*(\varphi_0)\circ a\), so \(\varphi_0\) is a morphism \(L\to M\) of \(BX\). The two constructions are inverse to each other, because \(b_{00}=\mathrm{id}\). \(\square\)

For complexes, Lemma 3.1 applies in each degree. Let \(E\) be a complex of modules of \(BX\) and \(I\) a bounded below complex of injective modules of \(BX\). Under (I), the modules \(UI^q\) are injective (Proposition 6.2 (3) of the lesson on equivariant sheaves), and so are the levels \(X(v_n)^*UI^q\) of \(\operatorname{ner}(I^q)\). By (1.1), \(\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}I)\) represents \(R\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}F)\) when \(I\) represents \(F\in D^+(BX)\). The isomorphism of Lemma 3.1 followed by the map from the limit to the derived limit gives the *canonical map*
\[
\begin{gathered}R\operatorname{Hom}_{BX}(E,F)\\ \longrightarrow R\varprojlim\\ R\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}F).\end{gathered}
\tag{3.1}
\]
For \(E\) bounded above, the complex \(\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}I)\) is bounded below, and by Section 1 the target of (3.1) is represented by the total complex of the double complex
\[
\begin{gathered}G^{a,n}\\ =\prod_{q-p=a}\operatorname{Hom}\bigl(X(v_0)^*E^p,\\ X(v_n)^*I^q\bigr),\end{gathered}
\tag{3.2}
\]
with the Hom differential in the direction \(a\) and the alternating sum of the cofaces in the direction \(n\geq0\). The map (3.1) is the inclusion of the kernel of the first coface differential, \(\operatorname{Hom}^\bullet_{BX}(E,I)\to G^{\bullet,0}\to\operatorname{Tot}(G)\).

**Lemma 3.2.** Assume (I) and (E). Let \(Q\) be a flat \(\mathcal O_0\)-module and \(J\) an injective \(\mathcal O_0\)-module. Then the cochain complex of the cosimplicial group \(\operatorname{Hom}^!\bigl(\operatorname{ner}^{\mathrm o}\operatorname{ind}(Q),\operatorname{ner}\operatorname{coind}(J)\bigr)\) has no cohomology in degrees \(n\geq1\).

**Proof.** Write \(P=\operatorname{ind}(Q)\). We use the décalage \(q\colon\operatorname{Dec}^1(X)\to X\) and the last vertex \(\lambda\colon\operatorname{Dec}^1(X)\to X_0\), with components \(d_{n+1}\colon X_{n+1}\to X_n\) and \(\lambda_n=X(v_{n+1})\colon X_{n+1}\to X_0\). By Proposition 3.1 of the lesson on nerves, \(\operatorname{ner}(\operatorname{coind}J)\cong q_*\lambda^*J\). The morphism \(q\) is a morphism over \(\Delta^{\mathrm{op}}\), and its module inverse images \(d_{n+1}^*\) are exact, the rings being cartesian. Adjunction on each level gives, as in the proof of Proposition 2.2, an isomorphism of cosimplicial groups
\[
\begin{aligned}&\operatorname{Hom}^!\bigl(\operatorname{ner}^{\mathrm o}P,q_*\lambda^*J\bigr)\\&\quad\cong\operatorname{Hom}^!\bigl(q^{\mathrm o*}\operatorname{ner}^{\mathrm o}P,\lambda^*J\bigr).\end{aligned}
\]
By Proposition 5.1 (1) of the lesson on nerves, \(A=q^{\mathrm o*}\operatorname{ner}^{\mathrm o}P\) is the décalage \(\operatorname{Dec}^1_+(\operatorname{ner}^{\mathrm o}P)\), with levels \(A_n=X(v_0)^*P\) on \(X_{n+1}\). The levels of \(\lambda^*J\) are \(\lambda_n^*J\). Adjunction for \(\lambda_{n!}\) gives
\[
\operatorname{Hom}(A_n,\lambda_n^*J)\cong\operatorname{Hom}(\lambda_{n!}A_n,J),
\]
naturally in \(n\): the simplicial \(\mathcal O_0\)-module \(N\colon[n]\mapsto\lambda_{n!}A_n\) is the functor \(\underline\lambda_!A\) of Corollary 4.2 of the lesson on derived left adjoints, whose maps are adjoint to those of \(A\). So the cochain complex in question is \(\operatorname{Hom}(s(N),J)\), where \(s(N)\) is the chain complex of \(N\), and since \(J\) is injective its cohomology in degree \(n\) is \(\operatorname{Hom}(H_n(s(N)),J)\).

The levels of \(A\) are flat: \(P=t_!s^*Q\), and \(t_!\) preserves flat modules by (E), while \(s^*\) and \(X(v_0)^*\) preserve flatness. The conditions (L), (H\(^{\mathrm o}\)) and (F) for \(\lambda\), and the hypotheses of Proposition 4.4 of the lesson on derived left adjoints, are instances of (E), as in the proof of Proposition 3.2 of the lesson on cohomology of equivariant modules. By Corollary 4.2 (2) there, \(s(N)\) represents \(L\lambda_!A\), and by Proposition 4.4 there, \(L\lambda_!\operatorname{Dec}^1_+(\operatorname{ner}^{\mathrm o}P)\cong(\operatorname{ner}^{\mathrm o}P)_0=UP\). So \(H_n(s(N))=0\) for \(n\geq1\). \(\square\)

**Theorem 3.3.** Let \(X\) be a good pseudo-category with a ring \(\mathcal O\) of \(B'X\) satisfying (I) and (E). For \(E\in D^-(BX)\) and \(F\in D^+(BX)\), the canonical map (3.1)
\[
\begin{gathered}R\operatorname{Hom}_{BX}(E,F)\longrightarrow\\ R\varprojlim R\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}F)\end{gathered}
\]
is an isomorphism.

**Proof.** By Proposition 6.2 (3) of the lesson on equivariant sheaves and [Stacks, Tag 05T7], \(E\) is represented by a bounded above complex of modules \(\operatorname{ind}(Q^p)\) with \(Q^p\) free, hence flat; the modules \(\operatorname{ind}(Q)\) are closed under finite sums, since \(\operatorname{ind}\) is additive. Represent \(F\) by a bounded below complex \(I\) of injective modules; by Proposition 6.2 (2) there, every \(I^q\) is a direct summand of some \(\operatorname{coind}(J^q)\) with \(J^q\) injective. We apply [Stacks, Tag 0133] to \(K=\operatorname{Hom}^\bullet_{BX}(E,I)\) and the double complex \(G\) of (3.2), with \(G^{a,n}\) in degree \(a+n\).

Its first two conditions hold: \(G^{a,n}=0\) for \(n<0\), and \(G^{a,n}=0\) unless \(a\geq q_0-p_0\), where \(I^q=0\) for \(q<q_0\) and \(E^p=0\) for \(p>p_0\); so for each total degree only finitely many \(G^{a,n}\) are nonzero, and each is a finite product. The map \(K\to G^{\bullet,0}\) is a map of complexes. The last condition asks that, for each \(a\), the complex \(G^{a,\bullet}\) be exact in degrees \(n\geq1\) and that \(K^a\) be the kernel of \(G^{a,0}\to G^{a,1}\). Both properties hold for finite products, and \(G^{a,\bullet}\) is the product over \(q-p=a\) of the cochain complexes of the cosimplicial groups \(\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}E^p,\operatorname{ner}I^q)\). For these, the statement about the kernel is Lemma 3.1. Exactness in degrees \(n\geq1\) holds for \(\operatorname{ner}\operatorname{coind}(J^q)\) by Lemma 3.2, and so for its direct summand \(\operatorname{ner}I^q\). So \(K\to\operatorname{Tot}(G)\) is a quasi-isomorphism, and this is (3.1). \(\square\)

**Corollary 3.4.** Under the hypotheses of Theorem 3.3 there is a spectral sequence, functorial in \(E\) and \(F\),
\[
\begin{gathered}E_1^{n,k}=\operatorname{Ext}^k_{\mathcal O_n}\bigl(X(v_0)^*E,X(v_n)^*F\bigr)\\ \Longrightarrow\operatorname{Ext}^{n+k}_{BX}(E,F),\end{gathered}
\]
in which \(E_1^{\bullet,k}\) is the cochain complex of the cosimplicial group \([n]\mapsto\operatorname{Ext}^k\bigl(X(v_0)^*E,X(v_n)^*F\bigr)\), with the maps induced by those of \(\operatorname{Hom}^!\).

**Proof.** Filter \(\operatorname{Tot}(G)\) by the cosimplicial degree \(n\). In each total degree the filtration is finite, as in the proof of Theorem 3.3, so the spectral sequence converges. Its \(E_1\) term is the cohomology of the columns \(G^{\bullet,n}=\operatorname{Hom}^\bullet\bigl(X(v_0)^*E,X(v_n)^*I\bigr)\). Since \(X(v_n)^*I\) is a bounded below complex of injective \(\mathcal O_n\)-modules quasi-isomorphic to \(X(v_n)^*F\), this cohomology is \(\operatorname{Ext}^k\bigl(X(v_0)^*E,X(v_n)^*F\bigr)\) [Stacks, Tag 05TG]. \(\square\)

**Corollary 3.5.** Under the hypotheses of Theorem 3.3, let \(F\) be a bounded below complex of modules of \(BX\) whose underlying \(\mathcal O_0\)-modules \(UF^q\) are injective, and \(E\) a bounded above complex. Then \(R\operatorname{Hom}_{BX}(E,F)\) is represented by the total complex of the cosimplicial complex
\[
[n]\longmapsto\operatorname{Hom}^\bullet\bigl(X(v_0)^*E,X(v_n)^*F\bigr).
\]

**Proof.** By (I), the levels \(X(v_n)^*UF^q\) of \(\operatorname{ner}F^q\) are injective. So by (1.1), \(\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}F)\) represents \(R\operatorname{Hom}^!(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}F)\), and its derived limit is the stated total complex (Section 1). Theorem 3.3 identifies it with \(R\operatorname{Hom}_{BX}(E,F)\). \(\square\)

For \(E=\mathcal O\), whose structure is invertible, \(X(v_0)^*\mathcal O=\mathcal O_n\) and \(\operatorname{Hom}(\mathcal O_n,X(v_n)^*F)=\Gamma(X_n,\operatorname{ner}_nF)\); Corollary 3.5 then describes \(R\Gamma(BX,F)\) as in Corollary 4.2 of the lesson on cohomology of equivariant modules.

## 4. Examples

**Example 4.1 (groups acting on a point).** Let \(T\) be the topos of sets, \(G\) a group, \(X\) the simplicial topos of the nerve of \(G\), and \(\mathcal O=k\) a commutative ring. A module of \(BX\) is a \(k\)-module with a \(k\)-linear action of \(G\), that is, a module over the group ring \(k[G]\); write \(\rho_E(g)\) for the action of \(g\) on \(E\). An element of \(\operatorname{Hom}(X(v_0)^*E,X(v_n)^*F)\) is a map \(u\colon G^n\to\operatorname{Hom}_k(E,F)\). The transport of \(E\) along the edge \((k,l)\) of the simplex \((g_1,\ldots,g_n)\) is the action of \(g_l\cdots g_{k+1}\), so the cofaces of Section 3 are
\[
\begin{aligned}&(d^0u)(g_1,\ldots,g_{n+1})\\&\quad=u(g_2,\ldots,g_{n+1})\circ\rho_E(g_1),\\&(d^iu)(g_1,\ldots,g_{n+1})\quad(0<i<n+1)\\&\quad=u(\ldots,g_{i+1}g_i,\ldots),\\&(d^{n+1}u)(g_1,\ldots,g_{n+1})\\&\quad=\rho_F(g_{n+1})\circ u(g_1,\ldots,g_n).\end{aligned}
\]
The nerve of \(G\) is the nerve of an internal category of the topos of sets, so (I) and (E) hold (Proposition 5.1 of the lesson on cohomology of equivariant modules). If \(F\) is injective as a \(k\)-module, for instance if \(k\) is a field, Corollary 3.5 says that \(\operatorname{Ext}^n_{k[G]}(E,F)\) is the cohomology of this complex. Exercise 5.2 identifies it with the cochain complex of group cohomology with coefficients in \(\operatorname{Hom}_k(E,F)\), on which \(G\) acts by \(g\cdot\varphi=\rho_F(g)\circ\varphi\circ\rho_E(g)^{-1}\).

**Example 4.2 (a quiver with two vertices).** Let \(X\) be the simplicial topos of the nerve of the ordered set \(\{0<1\}\), and \(\mathcal O=k\) a field. A module of \(BX\) is a linear map \(\mu_E\colon E_0\to E_1\) (Exercise 7.3 of the lesson on equivariant sheaves), a representation of the quiver with one arrow \(0\to1\). The simplices are the sequences \(x=(x_0\leq\cdots\leq x_n)\), and Corollary 3.5 gives \(\operatorname{Ext}^\bullet_{BX}(E,F)\) as the cohomology of the complex
\[
C^n=\prod_{x\in N_n}\operatorname{Hom}_k(E_{x_0},F_{x_n}),
\]
with the cofaces \((d^iu)(x)=u(d_ix)\) for \(0<i<n+1\), \((d^0u)(x)=u(d_0x)\circ\mu_E^{[x_0<x_1]}\) and \((d^{n+1}u)(x)=\mu_F^{[x_n<x_{n+1}]}\circ u(d_{n+1}x)\), where \(\mu^{[a<b]}\) is \(\mu\) if \(a<b\) and the identity if \(a=b\). For the simple representations \(S_0=(k\to0)\) and \(S_1=(0\to k)\), only the simplices with \(x_0=0\) and \(x_n=1\) contribute to \(C^\bullet(S_0,S_1)\), and Exercise 5.1 computes \(\operatorname{Ext}^1(S_0,S_1)=k\) and \(\operatorname{Ext}^n(S_0,S_1)=0\) for \(n\neq1\). The nonsplit extension is the representation \(k\xrightarrow{\mathrm{id}}k\).

## 5. Exercises

**Exercise 5.1.** In Example 4.2, describe the complex \(C^\bullet(S_0,S_1)\) and compute its cohomology. Show that \(C^\bullet(S_1,S_0)=0\).

**Exercise 5.2.** In Example 4.1, put \(u'(g_1,\ldots,g_n)=\) \(u(g_1,\ldots,g_n)\circ\rho_E(g_n\cdots g_1)^{-1}\). Show that \(u\mapsto u'\) carries the complex of Example 4.1 to the complex of Example 5.3 of the lesson on cohomology of equivariant modules for the \(G\)-module \(\operatorname{Hom}_k(E,F)\), with \(g\cdot\varphi=\rho_F(g)\circ\varphi\circ\rho_E(g)^{-1}\).

**Exercise 5.3.** Let \(X\) be the constant simplicial topos with value a topos \(T\) and a ring \(\mathcal O_T\), so that \(BX=\operatorname{Mod}(\mathcal O_T)\). Show that for modules \(E\), \(F\) with \(F\) injective, the complex of Corollary 3.5 is the cochain complex of the constant cosimplicial group \(\operatorname{Hom}(E,F)\), and that its cohomology is \(\operatorname{Hom}(E,F)\) in degree \(0\).

## 6. Complete solutions

**5.1.** A simplex \(x\in N_n\) contributes to \(C^n(S_0,S_1)\) only if \(x_0=0\) and \(x_n=1\), that is, \(x=0^a1^b\) with \(a,b\geq1\) and \(a+b=n+1\); let \(e_{a,b}\) be the basis vector of its factor \(\operatorname{Hom}(k,k)=k\). So \(C^0=0\), and \(C^n\) has dimension \(n\). Consider the differential at a simplex \(0^{a'}1^{b'}\) of degree \(n+1\). The inner faces \(d_i\), \(0<i<n+1\), omit a \(0\) when \(i<a'\) and give \(0^{a'-1}1^{b'}\), and omit a \(1\) when \(i\geq a'\) and give \(0^{a'}1^{b'-1}\). The face \(d_0\) gives \(0^{a'-1}1^{b'}\) with the identity transport when \(a'\geq2\), and contributes nothing when \(a'=1\), since its transport is the map \(0\) of \(S_0\). Likewise \(d_{n+1}\) gives \(0^{a'}1^{b'-1}\) when \(b'\geq2\) and nothing when \(b'=1\). Adding the signs \((-1)^i\), the coefficient of \(e_{a'-1,b'}\) is \(\sum_{i=0}^{a'-1}(-1)^i\) and that of \(e_{a',b'-1}\) is \(\sum_{i=a'}^{n+1}(-1)^i\). Hence
\[
\begin{gathered}d(e_{a,b})=[a\text{ even}]\,e_{a+1,b}\\+[b\text{ even}]\,(-1)^a\,e_{a,b+1}.\end{gathered}
\]
Let \(A\) be the complex with basis \(e_1,e_2,\ldots\) in degrees \(0,1,\ldots\) and the differential \(e_{2j}\mapsto e_{2j+1}\), \(e_{2j+1}\mapsto0\). Then \(e_{a,b}\mapsto e_a\otimes e_b\) identifies \(C^\bullet(S_0,S_1)\), with its degrees lowered by one, with \(A\otimes A\), up to the sign of the second differential, which does not change the cohomology. The complex \(A\) is the sum of \(ke_1\) in degree \(0\) and of the exact complexes \(ke_{2j}\to ke_{2j+1}\), so \(H^\bullet(A)=k\), in degree \(0\). By the Künneth formula over the field \(k\), \(H^n\bigl(C^\bullet(S_0,S_1)\bigr)\) is \(k\) for \(n=1\) and \(0\) otherwise; the class of \(e_{1,1}\) spans \(\operatorname{Ext}^1(S_0,S_1)\). Finally, \(C^\bullet(S_1,S_0)\) is built from \(\operatorname{Hom}\bigl((S_1)_{x_0},(S_0)_{x_n}\bigr)\), which is nonzero only if \(x_0=1\) and \(x_n=0\), impossible since \(x_0\leq x_n\).

**5.2.** For \(\sigma=(g_1,\ldots,g_{n+1})\) write \(\gamma=g_{n+1}\cdots g_1\). Then \((d^0u)'(\sigma)=\) \(u(g_2,\ldots,g_{n+1})\rho_E(g_1)\rho_E(\gamma)^{-1}=\) \(u'(g_2,\ldots,g_{n+1})\), because \(\rho_E(g_{n+1}\cdots g_2)=\rho_E(\gamma)\rho_E(g_1)^{-1}\). For \(0<i<n+1\), \((d^iu)'(\sigma)=u'(\ldots,g_{i+1}g_i,\ldots)\), the total product being unchanged. Finally \((d^{n+1}u)'(\sigma)=\) \(\rho_F(g_{n+1})u(g_1,\ldots,g_n)\rho_E(\gamma)^{-1}=\) \(\rho_F(g_{n+1})u'(g_1,\ldots,g_n)\rho_E(g_{n+1})^{-1}=\) \(g_{n+1}\cdot u'(g_1,\ldots,g_n)\). These are the cofaces of Example 5.3 of the lesson on cohomology of equivariant modules for the module \(\operatorname{Hom}_k(E,F)\). The map \(u\mapsto u'\) is bijective, with inverse \(u'\mapsto u'\circ\rho_E(g_n\cdots g_1)\).

**5.3.** Every \(X(\alpha)\) is the identity and every structure is the identity, so the cosimplicial group of Corollary 3.5 is constant with value \(\operatorname{Hom}(E,F)\). Its cochain complex has the differentials \(\sum_{i=0}^{n+1}(-1)^i\mathrm{id}\), which are \(0\) for \(n\) even and the identity for \(n\) odd; so it is \(\operatorname{Hom}(E,F)\xrightarrow{0}\) \(\operatorname{Hom}(E,F)\xrightarrow{\mathrm{id}}\) \(\operatorname{Hom}(E,F)\xrightarrow{0}\) \(\cdots\), with cohomology \(\operatorname{Hom}(E,F)\) in degree \(0\), and \(\operatorname{Ext}^n(E,F)=0\) for \(n\geq1\) as \(F\) is injective.

## Sources

The mixed Hom functor, its compatibility with inverse and direct images, and the computation of the Ext groups of equivariant modules by the nerves are due to Illusie, in his work on the cotangent complex and the cohomology of diagrams. The description of the Ext groups over a group ring by cochains of the group with values in Hom groups is classical; Example 4.1 and Exercise 5.2 derive it here when the second module is injective over the coefficient ring.
