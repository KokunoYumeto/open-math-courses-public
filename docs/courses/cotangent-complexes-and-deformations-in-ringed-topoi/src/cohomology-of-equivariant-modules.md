# Cohomology of equivariant modules

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

The modules of the category \(BX\) of equivariant sheaves on a pseudo-category \(X\) form an abelian category with enough injectives. So they have a derived category, cohomology and derived Hom complexes, whether or not \(BX\) is known to be a topos. The two nerves are exact functors into the module categories of the two total topoi of \(X\), and they induce maps from the derived Hom complexes of \(BX\) to those of the total topoi. This lesson shows that these maps are isomorphisms under natural conditions on \(X\). The only input needed is the vanishing of the higher Ext groups from nerves into nerves of injective modules, and the décalages of \(X\) reduce that vanishing to the levels. For a pseudo-category whose inverse images along the last vertices preserve injective modules, the cohomology of \(BX\), and more generally the derived Hom out of modules with invertible structure, is computed on either total topos. This gives a spectral sequence from the cohomology of the levels of \(X\) to that of \(BX\). For a group acting on a point it is the standard cochain complex of group cohomology. Under exactness conditions on left adjoints, which hold for the nerves of internal categories of a topos, all derived Hom complexes are computed on the total topoi, and the nerves are fully faithful on bounded derived categories.

**Prerequisites.** [*Equivariant sheaves on simplicial topoi*](equivariant-sheaves-on-simplicial-topoi.md) and [*Nerves of induced and coinduced modules*](nerves-of-induced-and-coinduced-modules.md); Theorem 2.1, Corollary 2.2, Proposition 3.2 and Proposition 4.2 of [*Cohomology of simplicial topoi and cohomological descent*](cohomology-of-simplicial-topoi-and-cohomological-descent.md); Lemmas 2.3 and 3.2 of [*Cohomology of the second total topos and local systems*](cohomology-of-the-second-total-topos-and-local-systems.md); Theorem 3.2 of [*Left derived functors of left adjoints on total topoi*](left-derived-functors-of-left-adjoints-on-total-topoi.md); Theorem 3.1 and Proposition 4.4 of [*Derived left adjoints on the second total topos and local inductive limits*](derived-left-adjoints-on-the-second-total-topos-and-local-inductive-limits.md); Remark 4.2 of [*Cohomology of total topoi*](cohomology-of-total-topoi.md); the face formulas of Section 2.5 of [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md); bounded below complexes of injectives are K-injective [[Stacks, Tag 070J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-bounded-below-injectives-K-injective)]; extension by zero is exact [[Stacks, Tag 03DJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-extension-by-zero-exact)] and commutes with tensor products [[Stacks, Tag 0E8I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-j-shriek-and-tensor)].

**Setting.** Notation is that of the two previous lessons. \(X\) is a pseudo-category with a ring \(\mathcal O\) of \(B'X\), and \(\operatorname{Mod}(BX)\) is the abelian category of modules of \(BX\), with the forgetful functor \(U\), the coinduction \(\operatorname{coind}\) and, for good \(X\), the induction \(\operatorname{ind}\). The décalage \(\operatorname{Dec}^1(X)\) comes with \(q\colon\operatorname{Dec}^1(X)\to X\) and the last vertex \(\lambda\colon\operatorname{Dec}^1(X)\to X_0\); the décalage \(\operatorname{Dec}_1(X)\) comes with \(q'\colon\operatorname{Dec}_1(X)\to X\) and the first vertex \(\pi\colon\operatorname{Dec}_1(X)\to X_0\). We write \(D(BX)\) for the derived category of \(\operatorname{Mod}(BX)\). For \(E\in D(BX)\) and \(F\in D^+(BX)\), \(R\operatorname{Hom}_{BX}(E,F)\) is the complex \(\operatorname{Hom}^\bullet(E,I)\), where \(I\) is a bounded below complex of injective modules representing \(F\); it is well defined because \(I\) is K-injective [Stacks, Tag 070J]. The same applies to the modules of the total topoi, which have enough injectives (for \(\operatorname{Top}^{\mathrm o}(X)\) when \(X\) is good, by Proposition 1.2 (4) of the lesson on the second total topos and its proof). The conditions used below are:

- **(I)** for every \(n\geq1\), the inverse image \(X(v_n)^*\colon\operatorname{Mod}(\mathcal O_0)\to\operatorname{Mod}(\mathcal O_n)\) along the last vertex carries injective modules to injective modules;
- **(E)** \(X\) is good, and every left adjoint \(X(\alpha)_!\) of a module inverse image carries flat modules to flat modules and short exact sequences of flat modules to exact sequences.

Both hold for the nerve of an internal category of a topos (Section 5).

## 1. The comparison maps

**1.1.** The nerves \(\operatorname{ner}\colon\operatorname{Mod}(BX)\to\operatorname{Mod}(\operatorname{Top}X)\) and \(\operatorname{ner}^{\mathrm o}\colon\operatorname{Mod}(BX)\to\operatorname{Mod}(\operatorname{Top}^{\mathrm o}X)\) are exact (Proposition 2.2 of the lesson on equivariant sheaves), so they act on complexes and on derived categories. For \(E\in D(BX)\) and \(F\in D^+(BX)\), represented by a complex \(E\) and a bounded below complex \(I\) of injectives, the maps
\[
\begin{gathered}\operatorname{Hom}^\bullet(E,I)\to\operatorname{Hom}^\bullet(\operatorname{ner}E,\operatorname{ner}I)\\ \to R\operatorname{Hom}(\operatorname{ner}E,\operatorname{ner}I)\end{gathered}
\]
define the comparison map, with values in the derived Hom complex on \(\operatorname{Top}X\),
\[
\begin{gathered}R\operatorname{Hom}_{BX}(E,F)\longrightarrow\\ R\operatorname{Hom}(\operatorname{ner}E,\operatorname{ner}F),\end{gathered}
\tag{1.1}
\]
the second map being the canonical map to the derived Hom complex. Likewise there is a comparison map for \(\operatorname{ner}^{\mathrm o}\), with values in the derived Hom complex on \(\operatorname{Top}^{\mathrm o}X\):
\[
\begin{gathered}R\operatorname{Hom}_{BX}(E,F)\longrightarrow\\ R\operatorname{Hom}(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}^{\mathrm o}F).\end{gathered}
\tag{1.2}
\]
On \(H^0\), for \(E\) and \(F\) bounded, these are the maps from \(\operatorname{Hom}_{D(BX)}(E,F)\) to \(\operatorname{Hom}_D(\operatorname{ner}E,\operatorname{ner}F)\) induced by the nerves.

**Lemma 1.2 (comparison criterion).** Let \(\Phi\colon\mathcal A\to\mathcal B\) be an exact functor between abelian categories with enough injectives, \(\mathcal P\) a class of objects of \(\mathcal A\), \(E\) a bounded above complex with terms in \(\mathcal P\), and \(F\in D^+(\mathcal A)\). Suppose that for every \(P\in\mathcal P\) and every injective object \(I\) of \(\mathcal A\), the map \(\operatorname{Hom}_{\mathcal A}(P,I)\to\operatorname{Hom}_{\mathcal B}(\Phi P,\Phi I)\) is bijective and \(\operatorname{Ext}^k_{\mathcal B}(\Phi P,\Phi I)=0\) for \(k\geq1\). Then the comparison map \(R\operatorname{Hom}_{\mathcal A}(E,F)\to R\operatorname{Hom}_{\mathcal B}(\Phi E,\Phi F)\) is an isomorphism.

**Proof.** Represent \(F\) by a bounded below complex \(I\) of injectives. The map \(\operatorname{Hom}^\bullet(E,I)\to\operatorname{Hom}^\bullet(\Phi E,\Phi I)\) is an isomorphism of complexes, because in each degree it is a finite product of the bijections \(\operatorname{Hom}(E^p,I^q)\to\operatorname{Hom}(\Phi E^p,\Phi I^q)\). It remains to see that \(\operatorname{Hom}^\bullet(\Phi E,\Phi I)\) computes \(R\operatorname{Hom}(\Phi E,\Phi F)\). Let \(\Phi I\to J\) be a quasi-isomorphism to a bounded below complex of injectives, and \(C\) its cone, a bounded below exact complex. Its terms \(C^q=\Phi I^{q+1}\oplus J^q\) satisfy \(\operatorname{Ext}^k(\Phi E^p,C^q)=0\) for \(k\geq1\). Let \(Z^q\) be the kernel of \(C^q\to C^{q+1}\). From the exact sequences \(0\to Z^q\to C^q\to Z^{q+1}\to0\), with \(Z^q=0\) for small \(q\), induction on \(q\) gives \(\operatorname{Ext}^k(\Phi E^p,Z^q)=0\) for \(k\geq1\), and then the sequences
\[
\begin{gathered}0\to\operatorname{Hom}(\Phi E^p,Z^q)\to\operatorname{Hom}(\Phi E^p,C^q)\\ \to\operatorname{Hom}(\Phi E^p,Z^{q+1})\to0\end{gathered}
\]
are exact. So \(\operatorname{Hom}(\Phi E^p,C^\bullet)\) is exact for every \(p\). In each degree, \(\operatorname{Hom}^\bullet(\Phi E,C)\) is a finite product of these terms, because \(E\) is bounded above and \(C\) bounded below; filtering by \(p\), it is exact. So \(\operatorname{Hom}^\bullet(\Phi E,\Phi I)\to\operatorname{Hom}^\bullet(\Phi E,J)\) is a quasi-isomorphism, and the target computes \(R\operatorname{Hom}(\Phi E,\Phi F)\). \(\square\)

In our applications, \(\operatorname{Hom}\) is bijective by the full faithfulness of the nerves. Every injective module of \(BX\) is a direct summand of a coinduced module \(\operatorname{coind}(J)\) with \(J\) injective (Proposition 6.2 of the lesson on equivariant sheaves), so it suffices to prove the vanishing of the Ext groups for \(I=\operatorname{coind}(J)\).

## 2. Décalage along the last vertex

**Lemma 2.1.** Assume (I). For every \(E\in D^+(\operatorname{Mod}\mathcal O_0)\), the unit \(E\to R\lambda_*\lambda^*E\) is an isomorphism, where \(\lambda\) is the morphism from \(\operatorname{Top}(\operatorname{Dec}^1X)\) to \(X_0\).

**Proof.** Represent \(E\) by a bounded below complex \(I\) of injectives. By (I), the levels \(X(v_{k+1})^*I^q\) of \(\lambda^*I^q\) are injective, hence acyclic for the direct images. By Theorem 2.1 (2) of the lesson on simplicial topoi, applied to \(\lambda\), \(R\lambda_*\lambda^*E\) is represented by the total complex of the double complex \(A^{k,q}=X(v_{k+1})_*X(v_{k+1})^*I^q\), \(k\geq0\), whose cofaces in the direction \(k\) come from the faces of \(\operatorname{Dec}^1(X)\). Let \(\Delta_1\subset\Delta\) be the subcategory of the maps preserving the last vertex. For fixed \(q\), the rule \(\Phi([j])=X(v_j)_*X(v_j)^*I^q\) is a functor on \(\Delta_1\): for \(\alpha\colon[j]\to[j']\) in \(\Delta_1\), \(\alpha v_j=v_{j'}\), and \(\Phi(\alpha)\) is \(X(v_j)_*\) of the unit of \(X(\alpha)\). Then \(A^{k,q}=\Phi([k+1])\), the cofaces are the \(\Phi(\delta^i)\) for \(\delta^i\colon[k+1]\to[k+2]\), \(0\leq i\leq k+1\), and the unit \(I^q=\Phi([0])\to A^{0,q}\) is \(\Phi(\delta^0)\) for \(\delta^0\colon[0]\to[1]\). Put \(s=\Phi(\sigma^k)\colon A^{k,q}\to A^{k-1,q}\), where \(\sigma^k\colon[k+1]\to[k]\) repeats the last vertex; it lies in \(\Delta_1\). The identities \(\sigma^k\delta^k=\mathrm{id}\) and \(\sigma^k\delta^i=\delta^i\sigma^{k-1}\) for \(i<k\) give \(sd^k=\mathrm{id}\) and \(sd^i=d^is\) for \(i<k\). As in the proof of Proposition 4.2 of the lesson on simplicial topoi, with the last coface in place of the first, \(h=(-1)^ks\) contracts the augmented complex \(I^q\to A^{\bullet,q}\). So each row is a resolution of \(I^q\), and the map from \(I\) to the total complex is a quasi-isomorphism. \(\square\)

**Lemma 2.2.** Assume that \(X\) is good and satisfies (I). For every injective \(\mathcal O_0\)-module \(J\), the unit \(J\to R\lambda^{\mathrm o}_*\lambda^{\mathrm o*}J\) is an isomorphism, where \(\lambda^{\mathrm o}\) is the morphism from \(\operatorname{Top}^{\mathrm o}(\operatorname{Dec}^1X)\) to \(X_0\).

**Proof.** Let \(G=\lambda^{\mathrm o*}J\) and \(G\to R^\bullet\) its standard resolution. By the proof of Theorem 3.4 (2) of the lesson on nerves, \(R^\bullet\) consists of injective modules, so \(R\lambda^{\mathrm o}_*G\) is represented by \(\lambda^{\mathrm o}_*R^\bullet\). By Lemma 2.3 of the lesson on the second total topos, \(\lambda^{\mathrm o}_*R^\bullet\) is the cochain complex of the cosimplicial module \([n]\mapsto\lambda_{n*}C_n(G)\) of the simplicial topos \(C_\bullet(\operatorname{Dec}^1X)\) (Definition 3.1 of the lesson on simplicial topoi). The levels of \(C_\bullet(G)\) are modules \(c(x)^*G_{x(n)}\cong G_{x(0)}\), which are injective by (I). So, by Theorem 2.1 (2) of the lesson on simplicial topoi, the same complex represents \(R\lambda_*C_\bullet(G)\). By Lemma 3.2 of the lesson on the second total topos, \(C_\bullet(G)\cong C_\bullet(\overline G)\), where \(\overline G=\lambda^*J\) is the corresponding cartesian object of \(\operatorname{Top}(\operatorname{Dec}^1X)\). By Proposition 3.2 of the lesson on simplicial topoi, \(R\lambda_*C_\bullet(\overline G)\cong R\lambda_*\lambda^*J\), and by Lemma 2.1 this is \(J\). All these complexes receive \(J\) through the units, and the isomorphisms are compatible with these maps. The proofs of the two lemmas cited from the lesson on the second total topos are computations that do not use that the second total category is a topos. \(\square\)

## 3. Vanishing of higher Ext groups

**Proposition 3.1 (modules with invertible structure).** Let \(E\) be a module of \(BX\) whose structure is invertible, and \(J\) an injective \(\mathcal O_0\)-module.

1. Under (I), \(\operatorname{Ext}^k_{\operatorname{Top}X}\bigl(\operatorname{ner}E,\operatorname{ner}\operatorname{coind}(J)\bigr)=0\) for \(k\geq1\).
2. If \(X\) is good and (I) holds, the groups \(\operatorname{Ext}^k\bigl(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}^{\mathrm o}\operatorname{coind}(J)\bigr)\) on \(\operatorname{Top}^{\mathrm o}X\) vanish for \(k\geq1\).

**Proof.** (1) By Proposition 3.1 of the lesson on nerves, \(\operatorname{ner}\operatorname{coind}(J)\cong Rq_*\lambda^*J\). The inverse image \(q^*\) is exact, so \(q_*\) carries injectives to injectives and \(R\operatorname{Hom}(A,Rq_*B)\cong R\operatorname{Hom}(q^*A,B)\). The level \(k\) of \(q^*\operatorname{ner}(E)\) is \(d_{k+1}^*X(v_k)^*E=X(v_k)^*E\) on \(X_{k+1}\), and its map for \(\beta\colon[k]\to[l]\) is \(e_{\beta(k)\,l}\), the transport of \(E\) along the edge \((\beta(k),l)\) of \([l+1]\). The invertible maps \(e_{k,k+1}\colon X(v_k)^*E\to X(v_{k+1})^*E\) form an isomorphism \(q^*\operatorname{ner}(E)\cong\lambda^*E\): the compatibility with \(\beta\) is \(e_{l,l+1}\circ e_{\beta(k)\,l}=e_{\beta(k),l+1}\), which is Lemma 1.2 of the lesson on equivariant sheaves. Hence
\[
\begin{aligned}&R\operatorname{Hom}\bigl(\operatorname{ner}E,\operatorname{ner}\operatorname{coind}J\bigr)\\&\quad\cong R\operatorname{Hom}(\lambda^*E,\lambda^*J)\\&\quad\cong R\operatorname{Hom}(E,R\lambda_*\lambda^*J)\\&\quad\cong R\operatorname{Hom}(E,J)\end{aligned}
\]
by Lemma 2.1, and the cohomology in degrees \(k\geq1\) vanishes because \(J\) is injective.

(2) By Theorem 3.4 of the lesson on nerves, \(\operatorname{ner}^{\mathrm o}\operatorname{coind}(J)\cong Rq^{\mathrm o}_*\lambda^{\mathrm o*}J\). By Proposition 5.1 (1) there, \(q^{\mathrm o*}\operatorname{ner}^{\mathrm o}(E)\) has the levels \(X(v_0)^*E\) on \(X_{k+1}\) and the maps \(e_{0\,\beta(0)}\). The invertible maps \(e_{0,k+1}\colon X(v_0)^*E\to X(v_{k+1})^*E\) form an isomorphism with \(\lambda^{\mathrm o*}E\), whose maps are identities: the compatibility is \(e_{\beta(0),l+1}\circ e_{0\,\beta(0)}=e_{0,l+1}\). As in (1), with Lemma 2.2,
\[
\begin{gathered}R\operatorname{Hom}\bigl(\operatorname{ner}^{\mathrm o}E,\operatorname{ner}^{\mathrm o}\operatorname{coind}J\bigr)\\ \cong R\operatorname{Hom}(E,J). \qquad\square\end{gathered}
\]

**Proposition 3.2 (all modules, second total topos).** Assume (I) and (E). For every module \(M\) of \(BX\) and every injective \(\mathcal O_0\)-module \(J\), \(\operatorname{Ext}^k_{\operatorname{Top}^{\mathrm o}X}\bigl(\operatorname{ner}^{\mathrm o}M,\operatorname{ner}^{\mathrm o}\operatorname{coind}(J)\bigr)=0\) for \(k\geq1\).

**Proof.** As in Proposition 3.1 (2),
\[
\begin{aligned}&R\operatorname{Hom}\bigl(\operatorname{ner}^{\mathrm o}M,\operatorname{ner}^{\mathrm o}\operatorname{coind}J\bigr)\\&\quad\cong R\operatorname{Hom}\bigl(\operatorname{Dec}^1_+(\operatorname{ner}^{\mathrm o}M),\lambda^{\mathrm o*}J\bigr)\\&\quad\cong R\operatorname{Hom}\bigl(L\lambda^{\mathrm o}_!\operatorname{Dec}^1_+(\operatorname{ner}^{\mathrm o}M),J\bigr)\\&\quad\cong R\operatorname{Hom}(UM,J).\end{aligned}
\]
The second isomorphism is Theorem 3.1 (3) of the lesson on derived left adjoints, applied to \(\lambda\colon\operatorname{Dec}^1(X)\to X_0\). Its condition (L) holds because \(X\) is good, and conditions (H\(^{\mathrm o}\)) and (F) are instances of (E): the left adjoints involved are the \(X(v_{k+1})_!\) and the \(X(\beta\sqcup\mathrm{id})_!\). The third is Proposition 4.4 there, whose hypotheses are again instances of (E), since \((\operatorname{ner}^{\mathrm o}M)_0=UM\). The groups \(\operatorname{Ext}^k(UM,J)\) vanish for \(k\geq1\). \(\square\)

**Proposition 3.3 (induced modules, first total topos).** Let \(X\) be a two-sided pseudo-category satisfying (I) and (E). For every flat \(\mathcal O_0\)-module \(P\) and every injective module \(I\) of \(BX\), \(\operatorname{Ext}^k_{\operatorname{Top}X}\bigl(\operatorname{ner}\operatorname{ind}(P),\operatorname{ner}I\bigr)=0\) for \(k\geq1\).

**Proof.** By Theorem 4.3 (2) of the lesson on nerves, whose hypothesis on \(d_{0!}\) is an instance of (E), \(\operatorname{ner}\operatorname{ind}(P)\cong Lq'_!\pi^*P\). Hence
\[
\begin{aligned}&R\operatorname{Hom}\bigl(\operatorname{ner}\operatorname{ind}P,\operatorname{ner}I\bigr)\\&\quad\cong R\operatorname{Hom}(\pi^*P,q'^*\operatorname{ner}I)\\&\quad\cong R\operatorname{Hom}\bigl(\pi^*P,\operatorname{Dec}_1^+(\operatorname{ner}I)\bigr)\\&\quad\cong R\operatorname{Hom}\bigl(P,R\pi_*\operatorname{Dec}_1^+(\operatorname{ner}I)\bigr)\\&\quad\cong R\operatorname{Hom}(P,UI).\end{aligned}
\]
The first isomorphism is Theorem 3.2 (3) of the lesson on left derived functors, applied to \(q'\), whose conditions (L) and (H) hold by (E). The second is Proposition 5.1 (2) of the lesson on nerves. The third is the adjunction between the exact functor \(\pi^*\) and \(\pi_*\). The fourth is Proposition 4.2 of the lesson on simplicial topoi, which says that \(M_0\to R\pi_*\operatorname{Dec}_1^+(M)\) is an isomorphism; here \(M=\operatorname{ner}I\) and \(M_0=UI\). By (I), \(t^*=X(v_1)^*\) preserves injectives, so \(UI\) is injective (Proposition 6.2 (3) of the lesson on equivariant sheaves), and \(\operatorname{Ext}^k(P,UI)=0\) for \(k\geq1\). \(\square\)

## 4. The comparison theorems

**Theorem 4.1.** Assume (I). Let \(E\) be a bounded above complex of modules of \(BX\) with invertible structures, and \(F\in D^+(BX)\). Then the comparison map (1.1) is an isomorphism. If \(X\) is good, so is (1.2).

**Proof.** Apply Lemma 1.2 to the nerve, respectively the second nerve, with \(\mathcal P\) the modules with invertible structure. The maps on \(\operatorname{Hom}\) are bijective by Proposition 2.2 (2) of the lesson on equivariant sheaves. By the remark after Lemma 1.2, the vanishing of the higher Ext groups is Proposition 3.1. \(\square\)

The ring \(\mathcal O\) is a module of \(BX\) with invertible structure, and \(\operatorname{Hom}_{BX}(\mathcal O,F)\) is the module of global sections \(\Gamma(BX,F)\) of \(F\). Its nerves are the rings of the total topoi. So Theorem 4.1 contains the following.

**Corollary 4.2 (cohomology of \(BX\)).** Assume (I). For \(F\in D^+(BX)\), the nerve induces an isomorphism
\[
R\Gamma(BX,F)\xrightarrow{\ \sim\ }R\Gamma(\operatorname{Top}X,\operatorname{ner}F),
\]
and, if \(X\) is good, the second nerve an isomorphism \(R\Gamma(BX,F)\cong R\Gamma(\operatorname{Top}^{\mathrm o}X,\operatorname{ner}^{\mathrm o}F)\). There is a spectral sequence, functorial in \(F\),
\[
\begin{gathered}E_1^{p,q}=H^q(X_p,\operatorname{ner}_pF)\\ \Longrightarrow H^{p+q}(BX,F),\end{gathered}
\]
where \(E_1^{\bullet,q}\) is the cochain complex of the cosimplicial abelian group \([p]\mapsto H^q(X_p,\operatorname{ner}_pF)\). If \(F\) is a module whose nerve has totally acyclic levels, \(R\Gamma(BX,F)\) is the cochain complex of \([p]\mapsto\Gamma(X_p,\operatorname{ner}_pF)\).

**Proof.** The isomorphisms are Theorem 4.1 with \(E=\mathcal O\). The spectral sequence is Corollary 2.2 of the lesson on simplicial topoi, for the morphism from \(X\) to the punctual topos, combined with the first isomorphism; the last assertion is Theorem 2.1 (2) there. Derived functors of modules and of their underlying abelian sheaves agree (Remark 4.2 of the lesson on cohomology of total topoi). \(\square\)

**Theorem 4.3.** Assume (I) and (E). Let \(E\in D^-(BX)\) and \(F\in D^+(BX)\).

1. The comparison map (1.2) for the second nerve is an isomorphism.
2. If \(X\) is a two-sided pseudo-category, the comparison map (1.1) for the nerve is an isomorphism.

**Proof.** (1) Represent \(E\) by a bounded above complex of modules and apply Lemma 1.2 with \(\mathcal P\) all modules: the vanishing is Proposition 3.2. (2) By Proposition 6.2 (3) of the lesson on equivariant sheaves, every module of \(BX\) is a quotient of a module \(\operatorname{ind}(P)\) with \(P\) free, hence flat. So \(E\) is represented by a bounded above complex of such modules [Stacks, Tag 05T7]. Apply Lemma 1.2 with \(\mathcal P\) the modules \(\operatorname{ind}(P)\), \(P\) flat: the vanishing is Proposition 3.3. \(\square\)

**Corollary 4.4.** Under the hypotheses of Theorem 4.3 (1), respectively (2), the functor \(\operatorname{ner}^{\mathrm o}\colon D^b(BX)\to D^b(\operatorname{Top}^{\mathrm o}X)\), respectively \(\operatorname{ner}\colon D^b(BX)\to D^b(\operatorname{Top}X)\), is fully faithful. Its essential image consists of the objects all of whose cohomology modules are isomorphic to second nerves, respectively nerves, of modules, that is, satisfy the condition of Proposition 2.3 of the lesson on equivariant sheaves.

**Proof.** We treat \(\operatorname{ner}\); the other case is the same. For \(E,F\in D^b(BX)\), \(\operatorname{Hom}_D(E,F)=H^0R\operatorname{Hom}(E,F)\), so Theorem 4.3 gives full faithfulness. If \(M\cong\operatorname{ner}(E)\), then \(H^i(M)\cong\operatorname{ner}(H^iE)\), as \(\operatorname{ner}\) is exact. Conversely, let every \(H^i(M)\) be isomorphic to a nerve. We argue by induction on the number of nonzero cohomology modules. If there is only one, \(M\cong H^i(M)[-i]\) is a nerve. Otherwise choose \(a\) with \(\tau_{\leq a}M\) and \(\tau_{>a}M\) both nonzero; by induction they are nerves of objects \(A\) and \(B\). The map \(\tau_{>a}M\to(\tau_{\leq a}M)[1]\) of the truncation triangle is the nerve of a map \(g\colon B\to A[1]\), by full faithfulness. The nerve of the triangle on \(g\) is a distinguished triangle with the same two vertices and the same map, so its third vertex, the nerve of the cone of \(g\) shifted by \(-1\), is isomorphic to \(M\). \(\square\)

## 5. Groups and internal categories

**Proposition 5.1.** Let \(C\) be an internal category of a topos \(T\) with a ring \(\mathcal O_T\), and \(X\) the simplicial topos of its nerve, with the inverse images of \(\mathcal O_T\). Then \(X\) is a good two-sided pseudo-category satisfying (I) and (E). So Theorems 4.1 and 4.3 and Corollaries 4.2 and 4.4 apply.

**Proof.** The first assertion is Proposition 3.4 of the lesson on equivariant sheaves. Every \(X(\alpha)\) is the localization of \(T\) along a morphism of the nerve. The module inverse image along a localization has the exact left adjoint "extension by zero" [Stacks, Tag 03DJ], so it carries injectives to injectives [Stacks, Tag 015Z]; this gives (I). By [Stacks, Tag 0E8I], \(j_!G\otimes F=j_!(G\otimes F|_U)\) for extension by zero \(j_!\) along a localization at \(U\). If \(G\) is flat, the right side is exact in \(F\), so \(j_!G\) is flat. Since \(j_!\) is exact, this gives (E). \(\square\)

**Example 5.2 (groups acting on an object).** Let \(G\) be a group of \(T\) acting on \(Y\), and \(X\) the simplicial topos of \(N(G,Y)\), so that \(BX\) is the category of \(G\)-objects over \(Y\) (Examples 1.4 (c) of the lesson on equivariant sheaves). Let \(F\) be an abelian \(G\)-object over \(Y\), that is, an abelian sheaf on \(T/Y\) with a compatible action. The level \(p\) of \(\operatorname{ner}F\) is the inverse image of \(F\) along the last vertex
\[
\begin{gathered}G^p\times Y\to Y,\\ (g_1,\ldots,g_p,y)\mapsto g_p\cdots g_1y .\end{gathered}
\]
Corollary 4.2 gives the spectral sequence
\[
\begin{gathered}E_1^{p,q}=H^q(G^p\times Y,\operatorname{ner}_pF)\\ \Longrightarrow H^{p+q}(BX,F).\end{gathered}
\]
If the sheaf on \(T/Y\) underlying \(F\) is totally acyclic, so are its restrictions to the localizations \(T/(G^p\times Y)\), and \(R\Gamma(BX,F)\) is the cochain complex of the cosimplicial group \(\Gamma(G^p\times Y,\operatorname{ner}_pF)\). Its cofaces are given by the transports of \(\operatorname{ner}F\) along the faces of \(N(G,Y)\). Let \(u\) be a section over \(G^p\times Y\), that is, a map \(u(g_1,\ldots,g_p,y)\in F_{g_p\cdots g_1y}\). By the formulas for the faces of \(N(G,Y)\) in Section 2.5 of the lesson on décalage, and Definition 2.1 of the lesson on equivariant sheaves for the transports,
\[
\begin{aligned}&(d^0u)(g_1,\ldots,g_{p+1},y)\\&\quad=u(g_2,\ldots,g_{p+1},g_1y),\\&(d^iu)(g_1,\ldots,g_{p+1},y)\quad(0<i<p+1)\\&\quad=u(\ldots,g_{i+1}g_i,\ldots,y),\\&(d^{p+1}u)(g_1,\ldots,g_{p+1},y)\\&\quad=g_{p+1}\,u(g_1,\ldots,g_p,y).\end{aligned}
\]
Only the last coface moves the last vertex, so only it involves the action.

**Example 5.3 (group cohomology).** Let \(T\) be the topos of sets, \(G\) a group, \(Y\) a point and \(\mathcal O=\mathbb Z\). Then \(\operatorname{Mod}(BX)\) is the category of \(G\)-modules, and \(\Gamma(BX,M)=\operatorname{Hom}_G(\mathbb Z,M)=M^G\). So \(H^n(BX,M)\) is the group cohomology \(H^n(G,M)\), the \(n\)-th derived functor of \(M\mapsto M^G\). Every abelian group is totally acyclic on the punctual topos, so Example 5.2 computes it as the cohomology of the complex of maps \(u\colon G^p\to M\) with the differential \(\sum_i(-1)^id^i\), where \(d^0\) drops \(g_1\), \(d^i\) replaces \(g_i,g_{i+1}\) by \(g_{i+1}g_i\), and \(d^{p+1}u=g_{p+1}u(g_1,\ldots,g_p)\). Reversing the order of the arguments, \(u'(h_1,\ldots,h_p)=u(h_p,\ldots,h_1)\), turns this differential into \((-1)^{p+1}\) times the usual inhomogeneous coboundary
\[
\begin{aligned}&(\delta u')(h_1,\ldots,h_{p+1})\\&\quad=h_1u'(h_2,\ldots,h_{p+1})\\&\qquad+\sum_{j=1}^p(-1)^ju'(\ldots,h_jh_{j+1},\ldots)\\&\qquad+(-1)^{p+1}u'(h_1,\ldots,h_p).\end{aligned}
\]
The signs \(\epsilon_p=(-1)^{p(p+1)/2}\) give an isomorphism of complexes \(u\mapsto\epsilon_pu'\). So group cohomology is computed by the inhomogeneous cochains.

## 6. Direct images to a base

**Proposition 6.1.** Let \(T\) be a topos with a ring \(\mathcal O_T\), \(X\) a pseudo-category and \(p\colon X\to T\) a morphism of fibred topoi, with components \(p_n\colon X_n\to T\). Give \(X\) the inverse images of \(\mathcal O_T\), and assume (I). Let \(p^*\colon\operatorname{Mod}(\mathcal O_T)\to\operatorname{Mod}(BX)\) send \(G\) to \(p_0^*G\) with its canonical invertible structure, and let \(p_*\) be its right adjoint. Then for \(F\in D^+(BX)\) the canonical maps
\[
Rp_*F\longrightarrow Rp^{\operatorname{Top}}_*(\operatorname{ner}F)
\]
and, if \(X\) is good, \(Rp_*F\to Rp^{\mathrm o}_*(\operatorname{ner}^{\mathrm o}F)\) are isomorphisms. Here \(p^{\operatorname{Top}}\) and \(p^{\mathrm o}\) are the morphisms from the two total topoi to \(T\) defined by \(p\).

**Proof.** The structure of \(p_0^*G\) is the composite of the isomorphisms \(s^*p_0^*G\cong p_1^*G\cong t^*p_0^*G\) given by the morphism \(p\), and it satisfies conditions 1 and 2 because these isomorphisms are compatible with composites. The functor \(p^*\) is exact. Its nerve is \(\operatorname{ner}(p^*G)=p^{\operatorname{Top}*}G\): both have the levels \(p_n^*G\) and the canonical maps. By the full faithfulness of \(\operatorname{ner}\),
\[
\begin{aligned}&\operatorname{Hom}_{BX}(p^*G,M)\\&\quad=\operatorname{Hom}(p^{\operatorname{Top}*}G,\operatorname{ner}M)\\&\quad=\operatorname{Hom}(G,p^{\operatorname{Top}}_*\operatorname{ner}M),\end{aligned}
\]
so \(p_*=p^{\operatorname{Top}}_*\circ\operatorname{ner}\) is a right adjoint of \(p^*\); the canonical map is the comparison \(R(p^{\operatorname{Top}}_*\circ\operatorname{ner})\to Rp^{\operatorname{Top}}_*\circ\operatorname{ner}\). Since \(p^*\) and \(p^{\operatorname{Top}*}\) are exact,
\[
\begin{aligned}&\operatorname{Hom}_D(G,Rp_*F[n])\\&\quad=\operatorname{Hom}_D(p^*G,F[n]),\\&\operatorname{Hom}_D(G,Rp^{\operatorname{Top}}_*\operatorname{ner}F[n])\\&\quad=\operatorname{Hom}_D(\operatorname{ner}p^*G,\operatorname{ner}F[n]),\end{aligned}
\]
and under these identifications the canonical map induces the map of (1.1) for \(E=p^*G\). It is bijective by Theorem 4.1, since \(p^*G\) has invertible structure. Take \(G=\mathcal O_{T,V}\), the free module on an object \(V\) of \(T\): then \(\operatorname{Hom}_D(G,K[n])=H^n(V,K)\). So the cone \(C\) of the canonical map, an object of \(D^+(\mathcal O_T)\), has \(H^n(V,C)=0\) for all \(V\) and \(n\). If \(H^m(C)\) were the first nonzero cohomology sheaf, then \(H^m(V,C)=\Gamma(V,H^m(C))\) would be nonzero for some \(V\). So \(C=0\). The second nerve is treated in the same way, with \(p^{\mathrm o}\). \(\square\)

For a group \(G\) of \(T\) acting on \(Y\), and \(p\) the projection from \(N(G,Y)\) to \(T\), Proposition 6.1 identifies the derived direct image of a \(G\)-module over \(Y\) along \(BX\to T\) with that of its nerve, which is computed level by level on the topoi \(T/(G^p\times Y)\).

## 7. Exercises

**Exercise 7.1.** Use Example 5.3 to compute \(H^n(G,\mathbb Z)\) for \(G=\mathbb Z/2\mathbb Z\) acting trivially on \(\mathbb Z\) and \(n\leq2\).

**Exercise 7.2.** Let \(X\) be the simplicial topos of the nerve of the ordered set \(\{0<1\}\) in the topos of sets, with \(\mathcal O=\mathbb Z\). A module of \(BX\) is a homomorphism \(\mu\colon F_0\to F_1\) of abelian groups (Exercise 7.3 of the lesson on equivariant sheaves). Show directly that \(\Gamma(BX,F)=F_0\) and that \(H^n(BX,F)=0\) for \(n\geq1\). Write the complex of Corollary 4.2 in degrees \(0\) and \(1\) and check that its cohomology in degree \(0\) is \(F_0\).

**Exercise 7.3.** Let \(X\) be the constant simplicial topos with value a topos \(T\), so that \(BX=T\). Show that Corollary 4.2 reduces to the statement of Exercise 6.3 of the lesson on simplicial topoi.

## 8. Complete solutions

**7.1.** By Example 5.3, \(H^n(G,\mathbb Z)\) is the cohomology of the complex of maps \(G^p\to\mathbb Z\). In degree \(0\), \(u\in\mathbb Z\) and \(\delta u(g)=u-g\cdot u=0\) for the trivial action, so \(H^0=\mathbb Z\). In degree \(1\), \(\delta u(g_1,g_2)=u(g_2)-u(g_2g_1)+u(g_1)\); the cocycles are the homomorphisms \(G\to\mathbb Z\), and the coboundaries are \(0\). There is no nonzero homomorphism \(\mathbb Z/2\mathbb Z\to\mathbb Z\), so \(H^1=0\). In degree \(2\), write \(G=\{1,g\}\). A map \(u\colon G^2\to\mathbb Z\) is a cocycle when
\[
\begin{gathered}u(g_2,g_3)-u(g_2g_1,g_3)\\+u(g_1,g_3g_2)-u(g_1,g_2)=0\end{gathered}
\]
for all \(g_1,g_2,g_3\). At \((1,1,g)\) this says \(u(1,g)=u(1,1)\), and at \((g,1,1)\) it says \(u(g,1)=u(1,1)\). Given these, the conditions at the other six triples hold, and \(u(g,g)\) occurs in none of them with a nonzero total coefficient. So the cocycles are given by \(c=u(1,1)=u(1,g)=u(g,1)\) and \(d=u(g,g)\), arbitrary. Coboundaries: for \(w\colon G\to\mathbb Z\), \(\delta w(g_1,g_2)=w(g_2)-w(g_2g_1)+w(g_1)\) gives \(c=w(1)\) and \(d=2w(g)-w(1)\). So \(H^2\cong\mathbb Z^2/\{(c,d)=(a,2b-a)\}\cong\mathbb Z/2\mathbb Z\), generated by \((0,1)\).

**7.2.** A global section of \(F\) is a morphism from the constant module \(\mathbb Z\to\mathbb Z\) (with identity map) to \(F\), that is, a pair \((x_0,x_1)\) with \(\mu(x_0)=x_1\); so \(\Gamma(BX,F)=F_0\). This functor is exact, so \(H^n(BX,F)=0\) for \(n\geq1\). The levels \(X_p\) are sets over the sets of simplices, and every abelian group is totally acyclic there, so Corollary 4.2 computes \(R\Gamma(BX,F)\) by the complex \(\prod_{x\in N_p}F_{x_p}\). In degree \(0\) it is \(F_0\times F_1\); in degree \(1\), the factors are those of the \(1\)-simplices \((0,0)\), \((0,1)\), \((1,1)\), namely \(F_0\times F_1\times F_1\). The differential sends \((x_0,x_1)\) to \(d^0-d^1\), where \(d^0\) and \(d^1\) restrict to the last and to the first vertex, the latter followed by the transport \(\mu\) along the simplex. At \((0,0)\) and \((1,1)\) it gives \(0\), and at \((0,1)\) it gives \(x_1-\mu(x_0)\). The kernel is \(\{(x_0,\mu(x_0))\}\cong F_0\).

**7.3.** For the constant simplicial topos, \(\operatorname{ner}F\) is the constant cosimplicial sheaf with value \(F\), and the condition (I) holds, since every \(X(\alpha)\) is the identity. Corollary 4.2 says \(R\Gamma(T,F)\cong R\Gamma(\operatorname{Top}X,\operatorname{ner}F)\). Exercise 6.3 of the lesson on simplicial topoi shows \(Rp_*p^*F\cong F\) for the identity morphism \(p\) on every level, where \(p^*F=\operatorname{ner}F\); taking global sections gives the same statement.

## Sources

The comparison of the cohomology and of the Ext groups of equivariant modules with those of the nerves, the spectral sequence of Corollary 4.2 and the statement of Proposition 6.1 are due to Illusie, in his work on the cotangent complex and the cohomology of diagrams. In Illusie's work, the comparison of all derived Hom complexes is stated for good pseudo-categories under the injectivity condition (I) alone; the proofs given here use in addition the exactness condition (E) and, for the first nerve, two-sidedness. The inhomogeneous cochains of group cohomology go back to Eilenberg and Mac Lane.
