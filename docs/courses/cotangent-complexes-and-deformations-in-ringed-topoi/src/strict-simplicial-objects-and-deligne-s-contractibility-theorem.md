# Strict simplicial objects and Deligne's contractibility theorem

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A strict simplicial object has face operators but no degeneracies. Strict simplicial objects are indexed by the category \(\Delta'\) of nonempty finite ordinals and injective increasing maps. They appear in the cohomology of diagrams whenever a construction is functorial only for injections, for example for spectral diagrams and stable derived functors. Two facts about \(\Delta'\) are used there.

The first says that the nerve of the category of simplices of a strict simplicial set has the homology of the complex of its alternating face sums. In particular, the categories of ordinals with at most \(n+1\) elements have the homology of a point for even \(n\) and of an \(n\)-sphere for odd \(n\). The second is Deligne's theorem: for every \(p\), the category of ordinals with at least \(p+1\) elements and injective maps is weakly contractible. This lesson proves both. The second follows from a contraction of a comma category by the functor that adds a new greatest element, together with Quillen's Theorem A.

**Prerequisites.** [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md), Sections 2–3; Quillen's Theorem A as proved in [*Test categories and Grothendieck's homotopy programme*](course:AG-AS/test-categories-and-homotopy-programme), Section 1.1; the chain complexes of a simplicial abelian group [[Stacks, Tag 0194](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-section-complexes), [Tag 019A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-decompose-associated-complexes), [Tag 0FKI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-remark-degenerate-subcomplex), [Tag 019C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-quasi-isomorphism), [Tag 019S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-homotopy-s-N)]; the first-quadrant spectral sequence of a double complex [[Stacks, Tag 0132](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-first-quadrant-ss)].

## 1. Strict simplicial objects

Let \(\bar\Delta'\) be the category of finite totally ordered sets, the empty set included, with injective increasing maps. Let \(\Delta'\subset\bar\Delta'\) be the full subcategory of nonempty sets. Every object is isomorphic to a unique \([n]=\{0<\cdots<n\}\), \(n\geq-1\), with \([-1]=\varnothing\). For \(p\geq-1\), let \(\bar\Delta'_{\geq p}\) be the full subcategory of the \([n]\) with \(n\geq p\). So \(\bar\Delta'_{\geq-1}=\bar\Delta'\) and \(\bar\Delta'_{\geq0}=\Delta'\). For \(0\leq n\leq\infty\), let \(\Delta'_{\leq n}\) be the full subcategory of the \([k]\) with \(0\leq k\leq n\).

A *strict simplicial object* of a category \(C\) is a functor \(\Delta'^{\mathrm{op}}\to C\), and an *augmented* one is a functor \(\bar\Delta'^{\mathrm{op}}\to C\). Strict cosimplicial objects are defined with \(\Delta'\) in place of \(\Delta'^{\mathrm{op}}\). Restricting a simplicial object along \(\Delta'\subset\Delta\) forgets its degeneracies.

Three elementary facts about injective increasing maps are used throughout.

1. An injective increasing map \(\alpha\colon[k]\to[l]\) is determined by its image. If \(m_1<\cdots<m_r\) are the elements of \([l]\) outside the image, then \(\alpha=\delta^{m_r}\circ\cdots\circ\delta^{m_1}\), where \(\delta^m\) is the increasing injection omitting \(m\).
2. An injective increasing map from \([k]\) to itself is the identity. So a morphism of \(\Delta'\) that is not an identity strictly increases the number of elements.
3. The cofaces satisfy \(\delta^j\delta^i=\delta^i\delta^{j-1}\) for \(i<j\). Exercise 5.3 shows that these relations present \(\bar\Delta'\).

By (1), a strict simplicial object \(X\) is determined by the objects \(X_k=X([k])\) and the faces \(d_i=X(\delta^i)\colon X_k\to X_{k-1}\), \(0\le i\le k\), and these satisfy \(d_id_j=d_{j-1}d_i\) for \(i<j\). If \(C\) is additive, the *associated complex* of \(X\) has \(X_k\) in degree \(k\) and differential \(d=\sum_i(-1)^id_i\). The face relations give \(d^2=0\), as for simplicial objects. For a functor \(X\) defined only on \(\Delta'_{\leq n}\), the associated complex stops in degree \(n\).

For a strict simplicial set \(E\), write \(\mathbb Z(E)\) for the strict simplicial abelian group of free abelian groups on the \(E_k\), and \(C(E)\) for its associated complex. Write \(\Delta'/E\) for its *category of simplices*. Its objects are the pairs \(([k],x)\) with \(x\in E_k\), and a morphism \(([k],x)\to([l],y)\) is an injective increasing \(\alpha\colon[k]\to[l]\) with \(E(\alpha)y=x\). For a simplicial set \(K\), \(\mathbb Z(K)\) is the free simplicial abelian group and \(s\mathbb Z(K)\) its chain complex [Stacks, Tag 0194].

## 2. The category of simplices of a strict simplicial set

**Lemma 2.1 (the strict simplex).** Let \(F\) be a nonempty finite totally ordered set with least element \(f_0\). The complex
\[
\begin{gathered}\cdots\to\mathbb Z\operatorname{Hom}_{\Delta'}([1],F)\\\to\mathbb Z\operatorname{Hom}_{\Delta'}([0],F)\xrightarrow{\ \varepsilon\ }\mathbb Z\to0,\end{gathered}
\]
with differential \(\beta\mapsto\sum_j(-1)^j\beta\circ\delta^j\) and augmentation \(\varepsilon(\beta)=1\), is contractible.

**Proof.** For an injective increasing \(\beta\colon[q]\to F\), let \(h(\beta)\colon[q+1]\to F\) be \(0\mapsto f_0\), \(j+1\mapsto\beta(j)\) when \(\beta(0)\neq f_0\), and let \(h(\beta)=0\) when \(\beta(0)=f_0\). Let \(h(1)\) be the vertex \(f_0\). If \(\beta(0)\neq f_0\), then \(h(\beta)\delta^0=\beta\) and \(h(\beta)\delta^{j+1}=h(\beta\delta^j)\), and every \(\beta\delta^j\) also avoids \(f_0\). So \(\partial h\beta=\beta-h\partial\beta\). If \(\beta(0)=f_0\) and \(q\ge1\), then \(\beta\delta^0\) avoids \(f_0\) and \(h(\beta\delta^0)=\beta\), while \(h(\beta\delta^j)=0\) for \(j\geq1\). So \(h\partial\beta=\beta\). In degree \(0\), \(\partial h(v)+h\varepsilon(v)=(v-f_0)+f_0=v\) for \(v\ne f_0\), and \(h\varepsilon(f_0)=f_0\). In degree \(-1\), \(\varepsilon h(1)=1\). \(\square\)

**Lemma 2.2 (initial objects).** If a small category \(D\) has an initial object \(o\), the augmented complex \(s\mathbb Z(N(D))\to\mathbb Z\) is contractible.

**Proof.** Put
\[
\begin{aligned}&h(c_0\to\cdots\to c_p)\\&\quad=(o\to c_0\to\cdots\to c_p),\end{aligned}
\]
and let \(h(1)\) be the vertex \(o\). Then \(d_0h=1\) and \(d_ih=hd_{i-1}\) for \(i\geq1\), and these give \(\partial h+h\partial=1\), the augmentation included. \(\square\)

**Theorem 2.3.** Let \(E\) be a strict simplicial set. There are quasi-isomorphisms
\[
s\mathbb Z\bigl(N(\Delta'/E)\bigr)\xleftarrow{\ \varepsilon'\ }\operatorname{Tot}B(E)\xrightarrow{\ \varepsilon''\ }C(E),
\]
natural in \(E\). In particular, \(H_*(N(\Delta'/E))\cong H_*(C(E))\).

**Proof.** For \(p,q\geq0\), let \(B(E)_{p,q}\) be the free abelian group on the pairs \((\sigma,\beta)\). Here \(\sigma=(c_0\xrightarrow{\alpha_1}c_1\to\cdots\xrightarrow{\alpha_p}c_p)\) is a \(p\)-simplex of \(N(\Delta'/E)\) with \(c_0=([k_0],x_0)\), and \(\beta\colon[q]\to[k_0]\) is injective and increasing. The horizontal differential is \(\partial'=\sum_{i=0}^p(-1)^id_i\). For \(i\geq1\), \(d_i\) acts on \(\sigma\) and keeps \(\beta\). The face \(d_0\) replaces \(\sigma\) by \(d_0\sigma\), which starts at \(c_1\), and \(\beta\) by \(\alpha_1\beta\). The vertical differential is \(\partial''(\sigma,\beta)=\sum_j(-1)^j(\sigma,\beta\delta^j)\). The two commute, since one composes \(\beta\) on the left and the other on the right. So \(B(E)\) is a first-quadrant double complex.

*Columns.* For fixed \(p\), the column is the direct sum over \(\sigma\) of the complexes of Lemma 2.1 for \(F=[k_0]\), without augmentation. Define \(\varepsilon'(\sigma,\beta)=\sigma\) on \(B(E)_{p,0}\). It vanishes on \(\partial''B(E)_{p,1}\), since \(\partial''(\sigma,\beta)=(\sigma,\beta\delta^0)-(\sigma,\beta\delta^1)\). It commutes with the horizontal differentials. So it is a morphism from \(B(E)\) to \(s\mathbb Z(N(\Delta'/E))\), placed in row \(0\). By Lemma 2.1, every augmented column is acyclic.

*Rows.* For fixed \(q\), define \(\varepsilon''(c_0,\beta)=E(\beta)x_0\in E_q\) on \(B(E)_{0,q}\). It vanishes on \(\partial'B(E)_{1,q}\): for \(\sigma=(c_0\xrightarrow{\alpha}c_1)\), we have \(E(\alpha\beta)x_1=E(\beta)E(\alpha)x_1=E(\beta)x_0\). It is compatible with the vertical differentials, because \(E(\beta\delta^j)x_0=d_j(E(\beta)x_0)\). So it is a morphism from \(B(E)\) to \(C(E)\), placed in column \(0\). The row \(B(E)_{\bullet,q}\) is the direct sum over \(y\in E_q\) of the pairs with \(E(\beta)x_0=y\), and the horizontal differential preserves this decomposition. The part over \(y\) is the chain complex of the nerve of the comma category \(D_y\) of pairs \((c,\beta)\), with \(c=([k],x)\) and \(\beta\colon([q],y)\to c\) a morphism of \(\Delta'/E\). Indeed, \((\sigma,\beta)\) is the \(p\)-simplex \((c_0,\beta)\to(c_1,\alpha_1\beta)\to\cdots\) of \(N(D_y)\), with the same faces. The category \(D_y\) has the initial object \((([q],y),\mathrm{id})\). By Lemma 2.2, every row, augmented by \(\varepsilon''\), is acyclic.

*Conclusion.* The cone of \(\operatorname{Tot}(\varepsilon')\) is the total complex of a first-quadrant double complex with acyclic columns, the augmented one. By [Stacks, Tag 0132], applied to the spectral sequence whose first page is the column homology, its total complex is acyclic. So \(\varepsilon'\) is a quasi-isomorphism, and the same argument with rows applies to \(\varepsilon''\). Every step is natural in \(E\). \(\square\)

**Corollary 2.4 (the truncated categories).** Let \(\mathcal Z\) be the complex \(\cdots\xrightarrow{1}\mathbb Z\xrightarrow{0}\mathbb Z\xrightarrow{1}\mathbb Z\xrightarrow{0}\mathbb Z\to0\), with \(\mathbb Z\) in every degree \(i\geq0\), and differential \(1\) from degree \(i\) to \(i-1\) for even \(i>0\) and \(0\) for odd \(i\). Let \(\mathcal Z_{\leq n}\) be its truncation to degrees \(\leq n\), for \(0\leq n\leq\infty\). Then:

1. \(s\mathbb Z(N(\Delta'_{\leq n}))\cong\mathcal Z_{\leq n}\) in the derived category of abelian groups, compatibly with the inclusions \(\Delta'_{\leq m}\subset\Delta'_{\leq n}\);
2. \(H_i(N(\Delta'_{\leq n}))\) is \(\mathbb Z\) for \(i=0\), \(\mathbb Z\) for \(i=n\) when \(n\) is odd, and \(0\) otherwise; in particular \(N(\Delta')\) has the homology of a point;
3. for \(1\leq n<\infty\), the quotient \(s\mathbb Z(N(\Delta'_{\leq n}))/s\mathbb Z(N(\Delta'_{\leq n-1}))\) is isomorphic to \(\mathbb Z[n]\) in the derived category.

**Proof.** Let \(E^{(n)}\) be the strict simplicial set with one simplex in each degree \(\leq n\) and none above. Then \(\Delta'/E^{(n)}=\Delta'_{\leq n}\), and \(C(E^{(n)})=\mathcal Z_{\leq n}\), because the differential in degree \(i\) is \(\sum_{j=0}^i(-1)^j\). So (1) is Theorem 2.3. The complex \(\mathcal Z_{\leq n}\) is the direct sum of \(\mathbb Z\) in degree \(0\), of the contractible pieces \(\mathbb Z\xrightarrow{1}\mathbb Z\) in degrees \((2j,2j-1)\), and, for odd \(n\), of \(\mathbb Z\) in degree \(n\). This gives (2). For (3), the inclusion \(E^{(n-1)}\subset E^{(n)}\) induces injective maps of the three complexes of Theorem 2.3, compatible with \(\varepsilon',\varepsilon''\). The induced maps on the quotients are quasi-isomorphisms by the five lemma, and \(\mathcal Z_{\leq n}/\mathcal Z_{\leq n-1}=\mathbb Z[n]\). \(\square\)

For \(n=1\), the category \(\Delta'_{\leq1}\) consists of two objects and two arrows \([0]\rightrightarrows[1]\), and its nerve is a circle (Exercise 5.1).

## 3. Locally constant functors on the categories of large ordinals

A functor is *locally constant* if it sends every arrow to an isomorphism.

**Proposition 3.1.** Let \(p\geq-1\), and let \(\mathcal C\) be any category. The category \(\bar\Delta'_{\geq p}\) is connected, and every locally constant functor \((\bar\Delta'_{\geq p})^{\mathrm{op}}\to\mathcal C\) or \(\bar\Delta'_{\geq p}\to\mathcal C\) is isomorphic to a constant functor.

**Proof.** Every object \([n]\), \(n\ge p\), receives an arrow from \([p]\), so the category is connected. A locally constant functor \(X\) on \(\bar\Delta'_{\geq p}\) gives a locally constant functor on the opposite category by \(\alpha\mapsto X(\alpha)^{-1}\), and one of them is isomorphic to a constant functor exactly when the other is. So let \(X\) be a locally constant functor on \((\bar\Delta'_{\geq p})^{\mathrm{op}}\). For \(n\geq p\), let \(\varphi_n\colon X_n\to X_p\) be the composite of the isomorphisms \(d_0=X(\delta^0)\) from \(X_n\) down to \(X_p\). Transport the structure along the \(\varphi_n\). This gives an isomorphic functor \(X'\) with \(X'_n=X_p\) for all \(n\) and \(X'(\delta^0)=1\). Write \(D^{(n)}_i\) for the automorphism \(X'(\delta^i)\) of \(X_p\), where \(\delta^i\colon[n-1]\to[n]\). By fact (1) of Section 1, it suffices to show that every \(D^{(n)}_i\) is the identity.

For \(n\geq p+2\) and \(i<j\), the relation \(\delta^j\delta^i=\delta^i\delta^{j-1}\) gives
\[
D^{(n-1)}_iD^{(n)}_j=D^{(n-1)}_{j-1}D^{(n)}_i.
\]
With \(i=0\), this says \(D^{(n)}_j=D^{(n-1)}_{j-1}\) for \(1\le j\le n\). Iterating, every \(D^{(n)}_j\) equals either some \(D^{(m)}_0=1\) or some \(D^{(p+1)}_k\). Put \(e_k=D^{(p+1)}_k\), so \(e_0=1\). For \(n=p+2\) and \(1\leq i<j\leq p+2\), the displayed relation and the case \(i=0\) give \(e_ie_{j-1}=e_{j-1}e_{i-1}\). Taking \(j=i+1\) gives \(e_ie_i=e_ie_{i-1}\), hence \(e_i=e_{i-1}\), since \(e_i\) is an isomorphism. By induction every \(e_i\) is the identity. \(\square\)

## 4. Deligne's theorem

For \(p\geq-1\), let \(J_p\) be the category whose objects are the pairs \(([m],f)\) with \(m\geq p+1\) and \(f\colon[p]\to[m]\) injective and increasing. A morphism \(([m],f)\to([m'],f')\) is an injective increasing \(g\colon[m]\to[m']\) with \(gf=f'\). For the inclusion \(i_p\colon\bar\Delta'_{\geq p+1}\to\bar\Delta'_{\geq p}\), the category \(J_p\) is the comma category \(([p]\downarrow i_p)\). For \(p=-1\) the map \(f\) is empty, and \(J_{-1}\) is isomorphic to \(\Delta'\).

**Lemma 4.1.** The identity of \(N(J_p)\) is homotopic to a constant map. Hence \(|N(J_p)|\) is contractible, and the augmented complex \(s\mathbb Z(N(J_p))\to\mathbb Z\) is acyclic.

**Proof.** Let \(F\colon J_p\to J_p\) add a new greatest element: \(F([m],f)=([m+1],f)\), where \([m]\subset[m+1]\), and \(F(g)=g\sqcup\mathrm{id}\), which sends \(m+1\) to \(m'+1\). The inclusions \([m]\subset[m+1]\) are a natural transformation \(\mathrm{id}\to F\), since \((g\sqcup\mathrm{id})\) restricted to \([m]\) is \(g\). Let \(c=([p+1],\iota)\), with \(\iota\colon[p]\subset[p+1]\). For each object \(([m],f)\), let \(h_f\colon[p+1]\to[m+1]\) be \(f\) on \([p]\) and send \(p+1\) to \(m+1\). It is injective and increasing, because \(f(p)\leq m<m+1\), and \(h_f\iota=f\), so \(h_f\) is a morphism \(c\to F([m],f)\). For \(g\colon([m],f)\to([m'],f')\), \((g\sqcup\mathrm{id})h_f=h_{f'}\). So the \(h_f\) form a natural transformation from the constant functor at \(c\) to \(F\). By Proposition 2.1 of [*Décalage, nerves and the homotopy type of a category*](decalage-nerves-and-the-homotopy-type-of-a-category.md), the identity of \(N(J_p)\) is homotopic to \(N(F)\), and \(N(F)\) is homotopic to the constant map at \(c\). Homotopic maps induce homotopic maps of chain complexes [Stacks, Tag 019S], so the identity of \(s\mathbb Z(N(J_p))\) is homotopic to a map factoring through \(s\mathbb Z(\Delta[0])\), whose homology is \(\mathbb Z\) in degree \(0\). This gives the last assertion. \(\square\)

**Theorem 4.2 (Deligne).** For every \(p\geq-1\), the inclusion \(\bar\Delta'_{\geq p+1}\subset\bar\Delta'_{\geq p}\) induces a quasi-isomorphism
\[
s\mathbb Z\bigl(N(\bar\Delta'_{\geq p+1})\bigr)\longrightarrow s\mathbb Z\bigl(N(\bar\Delta'_{\geq p})\bigr).
\]

**Proof.** For a simplicial set \(K\), \(s\mathbb Z(K)\) is quasi-isomorphic to its quotient by the subcomplex spanned by degenerate simplices, which is free on the nondegenerate simplices [Stacks, Tags 019A, 0FKI and 019C]. Write \(C(p)\) for this quotient for \(K=N(\bar\Delta'_{\geq p})\). By fact (2) of Section 1, its basis in degree \(n\) is the set of chains \([r_0]\to[r_1]\to\cdots\to[r_n]\) of injective increasing maps with \(p\leq r_0<r_1<\cdots<r_n\), and \(d=\sum_i(-1)^id_i\). The complex \(C(p+1)\) is the subcomplex of chains with \(r_0\geq p+1\), so it suffices to show that \(Q(p)=C(p)/C(p+1)\) is acyclic.

The basis of \(Q_n(p)\) consists of the chains \([p]\to[r_1]\to\cdots\to[r_n]\) with \(p<r_1<\cdots<r_n\), and the differential is \(\sum_{i=1}^n(-1)^id_i\), since \(d_0\) lands in \(C(p+1)\). For \(n\geq1\), such a chain is the same as the nondegenerate \((n-1)\)-simplex
\[
([r_1],f_1)\to([r_2],f_2)\to\cdots\to([r_n],f_n)
\]
of \(N(J_p)\), where \(f_j\colon[p]\to[r_j]\) is the composite. By fact (2), every nondegenerate simplex of \(N(J_p)\) arises once in this way. For \(n=0\), the chain \(([p])\) corresponds to the augmentation. Removing \([r_i]\) from the chain removes the \((i-1)\)-st vertex of the simplex. So \(Q(p)\) is isomorphic, up to the sign of its differential, to the augmented normalized chain complex of \(N(J_p)\) shifted up by one degree. That complex is acyclic by Lemma 4.1, together with [Stacks, Tag 019C] for the normalization. \(\square\)

**Corollary 4.3 (Deligne).** For every \(p\geq-1\), the category \(\bar\Delta'_{\geq p}\) is weakly contractible: \(|N(\bar\Delta'_{\geq p})|\) is weakly contractible, and \(s\mathbb Z(N(\bar\Delta'_{\geq p}))\to\mathbb Z\) is a quasi-isomorphism. In particular this holds for \(\Delta'\).

**Proof.** The category \(\bar\Delta'\) has the initial object \(\varnothing\), so it is weakly contractible (Corollary 2.2 of the lesson on décalage). Quillen's Theorem A, applied to \(u^{\mathrm{op}}\), says that a functor \(u\colon A\to B\) is a weak equivalence when every comma category \((b\downarrow u)\) is weakly contractible. This uses Lemma 3.1 of the lesson on décalage: \(u\) is a weak equivalence exactly when \(u^{\mathrm{op}}\) is, and \((b\downarrow u)\) is the opposite of the comma category \((u^{\mathrm{op}}\downarrow b)\), so one is weakly contractible exactly when the other is. Apply this to \(u=i_p\). For \(k\geq p+1\), the category \(([k]\downarrow i_p)\) has the initial object \(([k],\mathrm{id})\). For \(k=p\), it is \(J_p\), which is contractible by Lemma 4.1. So every \(i_p\) is a weak equivalence, and induction on \(p\) gives the first assertion. The second is Theorem 4.2 and induction, starting from Lemma 2.2 for \(\bar\Delta'\). \(\square\)

Proposition 3.1 gives the corresponding statement for locally constant presheaves directly from the cosimplicial identities. By Corollary 3.3 of the lesson on décalage, Corollary 4.3 says that \(\bar\Delta'_{\geq p}\) is isomorphic to the point in the category of small categories localized at weak equivalences.

**Remark 4.4.** Deligne's original proof, reported by Illusie, computes \(Q(p)\) directly. It filters \(Q(p)\) by the last ordinal \([r_n]\) and identifies each graded piece with a sum, over the injections \(f\colon[p]\to[k]\), of complexes of chains of subsets between \(f([p])\) and \([k]\). It shows, using Corollary 2.4 (3), that each of these complexes has homology only in its top degree. It then compares \(Q(p)\) with an explicit acyclic complex built from the groups \(\mathbb Z\operatorname{Hom}_{\Delta'}([p],[k])\). The argument above replaces this computation by the contraction of \(J_p\).

## 5. Exercises

**Exercise 5.1.** Show directly that \(|N(\Delta'_{\leq1})|\) is a circle, and compare with Corollary 2.4.

**Exercise 5.2.** Let \(E\) be a strict simplicial set with finitely many simplices. Show that \(N(\Delta'/E)\) has finitely many nondegenerate simplices and that its Euler characteristic is \(\sum_k(-1)^k|E_k|\).

**Exercise 5.3.** Show that the category \(\bar\Delta'\) is generated by the cofaces \(\delta^i\colon[n-1]\to[n]\) (\(0\le i\le n\), \(n\ge0\)) subject only to the relations \(\delta^j\delta^i=\delta^i\delta^{j-1}\) for \(i<j\). Deduce that a strict simplicial object is the same as a family of objects \(X_k\) with morphisms \(d_i\colon X_k\to X_{k-1}\) satisfying \(d_id_j=d_{j-1}d_i\) for \(i<j\).

## 6. Complete solutions

**5.1.** The objects are \([0]\) and \([1]\), and the non-identity arrows are \(\delta^0,\delta^1\colon[0]\to[1]\). There are no composable pairs of non-identity arrows. So \(N(\Delta'_{\leq1})\) has two nondegenerate vertices and two nondegenerate edges, each edge joining \([0]\) to \([1]\). Its realization is two arcs glued at their endpoints, a circle. Its homology, \(\mathbb Z\) in degrees \(0\) and \(1\), agrees with Corollary 2.4 for \(n=1\).

**5.2.** A nondegenerate simplex of \(N(\Delta'/E)\) is a chain of non-identity morphisms. By fact (2) of Section 1, the dimensions of the objects strictly increase along it, so it has at most \(d+1\) objects, where \(d\) is the top dimension of \(E\). There are finitely many objects and morphisms, hence finitely many such chains. The Euler characteristic is the alternating sum of the ranks of the normalized complex, which equals the alternating sum of the ranks of the homology. By Theorem 2.3, this homology is that of \(C(E)\), whose ranks give \(\sum_k(-1)^k|E_k|\).

**5.3.** By fact (1), every injective increasing map is a composite of cofaces, so the cofaces generate. Call a word \(\delta^{m_r}\cdots\delta^{m_1}\) normal if \(m_1<\cdots<m_r\); here \(\delta^{m_1}\) is applied first. A normal word is the injection omitting \(\{m_1,\ldots,m_r\}\), so distinct normal words give distinct maps. The relations hold in \(\bar\Delta'\), so words that are equal modulo the relations give the same map.

We show by induction on the length that every word is equal, modulo the relations, to a normal word. Write a word as \(\delta^mw'\), where by induction \(w'\) equals a normal word \(\delta^{n_{r-1}}\cdots\delta^{n_1}\). If \(m>n_{r-1}\), the word \(\delta^m\delta^{n_{r-1}}\cdots\delta^{n_1}\) is normal. Otherwise \(m\leq n_{r-1}\), and the relation, read as \(\delta^m\delta^{n}=\delta^{n+1}\delta^m\) for \(m\leq n\), moves \(\delta^m\) one place to the right and raises the index it passes by one. Repeat this while the next index \(n_t\) satisfies \(m\leq n_t\). The result, for the index \(s\) with \(n_s<m\leq n_{s+1}\), is
\[
\delta^{n_{r-1}+1}\cdots\delta^{n_{s+1}+1}\,\delta^m\,\delta^{n_s}\cdots\delta^{n_1},
\]
which is normal, since \(n_s<m<n_{s+1}+1<\cdots<n_{r-1}+1\). So every word equals a normal word, and two words define the same map exactly when they are equal modulo the relations. Hence the relations present \(\bar\Delta'\). A functor on \(\bar\Delta'^{\mathrm{op}}\) is therefore the same as values on the generators satisfying the dual relations \(d_id_j=d_{j-1}d_i\) for \(i<j\).

## Sources

Strict simplicial objects, the computation of the homology of the categories \(\Delta'_{\leq n}\), and the contractibility of the categories \(\bar\Delta'_{\geq p}\) are in Illusie's work on the cotangent complex, where the contractibility theorem and its original proof are credited to P. Deligne. Quillen's Theorem A, used for Corollary 4.3, is from D. Quillen's work on higher algebraic K-theory; its proof is in the programme lesson cited above. Strict simplicial sets are also called semi-simplicial sets or Δ-sets; an introduction to them and to simplicial sets is G. Friedman, *An elementary illustrated introduction to simplicial sets*, Rocky Mountain J. Math. 42 (2012), 353–423, [arXiv:0809.4221](https://arxiv.org/abs/0809.4221).
