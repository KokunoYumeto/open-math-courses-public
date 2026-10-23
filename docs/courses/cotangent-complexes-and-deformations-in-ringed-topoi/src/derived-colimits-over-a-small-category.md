# Derived colimits over a small category

*Written by Claude Opus 5.5 (Anthropic) on 20 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A diagram \(X\colon I\to\mathcal A\) in an abelian category has a colimit, but the colimit functor is only right exact. Its left derived functor is computed by an explicit complex, the simplicial replacement of the diagram, whose \(n\)-th term is the sum of the values of \(X\) at the sources of the strings of \(n\) composable arrows of \(I\). This lesson constructs the derived colimit on bounded-above complexes, identifies it with the simplicial replacement, and proves its adjunction with the constant diagram, both on morphisms of derived categories and as an isomorphism of derived Hom complexes; the latter uses an explicit resolution of constant diagrams by coinduced diagrams. It then applies Deligne's contractibility theorem: over the category of finite ordinals and injective maps, a diagram that is eventually locally constant has no higher derived colimits, and its colimit is its value at any stage from which it is locally constant. Finally it shows that over this category no diagram has higher derived colimits, so that the colimit is exact and the derived colimit of a bounded-above complex is its termwise colimit. In any additive category with sums, the chain complex of a simplicial object is homotopy equivalent to that of its simplicial replacement, naturally, and for a multisimplicial object the simplicial replacement is homotopy equivalent to the diagonal.

**Prerequisites.** [*Strict simplicial objects and Deligne's contractibility theorem*](strict-simplicial-objects-and-deligne-s-contractibility-theorem.md); left derived functors on bounded-above derived categories [[Stacks, Tag 05T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-resolution), [Tag 05T9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-left-acyclics), [Tag 05TA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-proposition-enough-acyclics)] and their adjunctions [[Stacks, Tag 0DVC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-pre-derived-adjoint-functors)]; complexes of projective objects [[Tag 064B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-morphisms-from-projective-complex)]; K-injective complexes [[Tag 070I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-K-injective), [Tag 070J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-bounded-below-injectives-K-injective)], injective resolutions [[Tag 013K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-injective-resolutions-exist)] and Grothendieck abelian categories [[Tag 079P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/injectives.html#injectives-theorem-K-injective-embedding-grothendieck), [Tag 07D8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/injectives.html#injectives-lemma-grothendieck-products)].

Throughout, \(\mathcal A\) is an abelian category with all small colimits in which filtered colimits are exact (Grothendieck's axiom AB5). Examples are the categories of modules over a ring and of sheaves of modules on a ringed topos. In particular direct sums are exact, and the cohomology of a complex commutes with filtered colimits of complexes.

## 1. Diagrams and their simplicial replacement

Let \(I\) be a small category. The functors \(I\to\mathcal A\) form an abelian category \(\mathcal A^I\), in which kernels, cokernels, sums and filtered colimits are computed objectwise. The constant-diagram functor \(c\colon\mathcal A\to\mathcal A^I\) is exact, and the colimit \(\varinjlim_I\colon\mathcal A^I\to\mathcal A\) is its left adjoint. It is right exact.

**Induced diagrams.** Let \(\omega_*\colon\mathcal A^I\to\mathcal A^{\operatorname{Ob}I}\) forget the arrows. It has the left adjoint
\[
\omega^*(Y)(i)=\bigoplus_{a\colon j\to i}Y_j,\qquad Y=(Y_j)_{j\in\operatorname{Ob}I},
\]
where an arrow \(b\colon i\to i'\) sends the summand of \(a\) to the summand of \(ba\). By the Yoneda lemma, a morphism \(\omega^*(Y)\to X\) is the same as a family of morphisms \(Y_j\to X(j)\). Diagrams isomorphic to some \(\omega^*(Y)\) are called *induced*. The counit \(\omega^*\omega_*X\to X\) is surjective, since the summand of \(a=\mathrm{id}_i\) maps identically onto \(X(i)\). The composite of left adjoints \(\varinjlim_I\circ\,\omega^*\) is left adjoint to \(\omega_*\circ c\), so \(\varinjlim_I\omega^*(Y)=\bigoplus_jY_j\).

**The simplicial replacement.** For \(X\in\mathcal A^I\) and \(n\geq0\), put
\[
C_n(X)=\bigoplus_{\sigma=(i_0\to i_1\to\cdots\to i_n)}X(i_0),
\]
the sum over the \(n\)-simplices \(\sigma\) of the nerve \(N(I)\). The face \(d_0\) maps the summand of \(\sigma\) to that of \(d_0\sigma\) by \(X(i_0\to i_1)\). The faces \(d_k\), \(k\geq1\), and the degeneracies map it identically to the summand of the corresponding face or degeneracy of \(\sigma\). This defines a simplicial object \(C_\bullet(X)\) of \(\mathcal A\), functorial and exact in \(X\), since sums and evaluations are exact. The cokernel of \(d_0-d_1\colon C_1(X)\to C_0(X)\) is the usual presentation of the colimit. So the augmentation \(C_0(X)\to\varinjlim_IX\) identifies \(H_0\) of the chain complex \(sC_\bullet(X)\) with \(\varinjlim_IX\).

Since \(\varinjlim_I\omega^*=\bigoplus\), the object \(C_n(X)\) is also \(\varinjlim_I\omega^*(Y^{(n)})\), where \(Y^{(n)}_j=\bigoplus_{i_0\to\cdots\to i_{n-1}\to j}X(i_0)\).

**Lemma 1.1.** For every \(Y\in\mathcal A^{\operatorname{Ob}I}\), the augmented complex \(sC_\bullet(\omega^*Y)\to\bigoplus_jY_j\) is contractible.

**Proof.** The summands of \(C_n(\omega^*Y)\) are indexed by strings \(j\xrightarrow{a}i_0\to\cdots\to i_n\) and the summand \(Y_j\). Such a string is an \(n\)-simplex of the nerve of the category \(j/I\) of arrows out of \(j\), and the faces and degeneracies of \(C_\bullet(\omega^*Y)\) are those of \(N(j/I)\). The face \(d_0\) composes \(a\) with the first arrow. So \(sC_\bullet(\omega^*Y)\), with its augmentation, is the direct sum over \(j\) of \(Y_j\otimes\bigl(s\mathbb Z(N(j/I))\to\mathbb Z\bigr)\). Here \(Y\otimes\mathbb Z(S)\) denotes the sum of copies of \(Y\) indexed by the set \(S\), and integer matrices act on it in the evident way. The category \(j/I\) has the initial object \(\mathrm{id}_j\), so the augmented complex \(s\mathbb Z(N(j/I))\to\mathbb Z\) is contractible (Lemma 2.2 of the lesson on strict simplicial objects). Tensoring with \(Y_j\) and summing preserves contractibility. \(\square\)

## 2. The derived colimit

Call \(X\in\mathcal A^I\) *colimit-acyclic* if \(H_n(sC_\bullet(X))=0\) for all \(n>0\). Induced diagrams are colimit-acyclic, by Lemma 1.1.

For a complex \(X\) of \(\mathcal A^I\), written cohomologically, let \(L(X)\) be the total complex of the double complex \(C_p(X^q)\). Its horizontal differential is \(\sum_i(-1)^id_i\colon C_p\to C_{p-1}\), and its vertical differential is induced by \(X\), with the sign \((-1)^p\) on \(C_p(X^q)\). The total degree of \(C_p(X^q)\) is \(q-p\), and the total complex is formed with direct sums. The augmentations \(C_0(X^q)\to\varinjlim_IX^q\) define a morphism of complexes \(\varepsilon\colon L(X)\to\varinjlim_IX\), where the colimit is taken termwise.

**Lemma 2.1.** If \(X\) is acyclic, so is \(L(X)\). Hence \(L\) takes quasi-isomorphisms to quasi-isomorphisms.

**Proof.** For each \(p\), the column \(C_p(X^\bullet)\) is acyclic, because \(C_p\) is a sum of evaluation functors. Let \(F_P\subseteq L(X)\) be the sum of the columns \(p\leq P\). It is a subcomplex, because the horizontal differential lowers \(p\). By induction on \(P\), each \(F_P\) is an iterated extension of shifted acyclic columns, hence acyclic. Every element of \(L(X)\) is a finite sum of components, so \(L(X)=\bigcup_PF_P\) is a filtered union, and it is acyclic by AB5. For the second assertion, apply the first to the cone of a quasi-isomorphism, using that \(L\) commutes with cones. \(\square\)

**Lemma 2.2.** If \(X\) is a bounded-above complex of colimit-acyclic diagrams, then \(\varepsilon\colon L(X)\to\varinjlim_IX\) is a quasi-isomorphism.

**Proof.** Up to a shift, the cone of \(\varepsilon\) is the total complex of the double complex obtained by adding the column \(\varinjlim_IX^q\) in position \(p=-1\). Its row \(q\) is the augmented complex \(sC_\bullet(X^q)\to\varinjlim_IX^q\), which is acyclic because \(X^q\) is colimit-acyclic. Let \(X^q=0\) for \(q>Q\). The sum \(G_k\) of the rows \(q\geq Q-k\) is a subcomplex, because the vertical differential raises \(q\). Each \(G_k\) is acyclic, by induction on \(k\). The total complex is the filtered union of the \(G_k\), so it is acyclic by AB5. \(\square\)

**Theorem 2.3.** The colimit functor has a left derived functor
\[
L\varinjlim_I\colon D^-(\mathcal A^I)\longrightarrow D^-(\mathcal A),
\]
which is exact. Every bounded-above complex of colimit-acyclic diagrams computes it, in particular every bounded-above complex of induced diagrams. For every \(X\in D^-(\mathcal A^I)\) there is a canonical isomorphism \(L\varinjlim_IX\cong L(X)\). The functor \(L\varinjlim_I\) takes \(D^{\leq m}(\mathcal A^I)\) into \(D^{\leq m}(\mathcal A)\).

**Proof.** Let \(\mathcal P\) be the class of colimit-acyclic diagrams. Every diagram is a quotient of an induced diagram, which lies in \(\mathcal P\). Let \(0\to P\to Q\to R\to0\) be exact with \(Q,R\in\mathcal P\). Since \(C_\bullet\) is exact, the long exact homology sequence of \(sC_\bullet\) shows that \(H_n(sC_\bullet(P))=0\) for \(n\geq2\). It also gives an exact sequence
\[
\begin{gathered}0=H_1(sC_\bullet(R))\to\varinjlim_IP\\\to\varinjlim_IQ\to\varinjlim_IR\to0\end{gathered}
\]
together with \(H_1(sC_\bullet(P))=0\), the latter because \(H_2(sC_\bullet(R))=0=H_1(sC_\bullet(Q))\). So \(P\in\mathcal P\), and the colimit is exact on the sequence. By [Stacks, Tag 05T9], every object of \(\mathcal P\) is acyclic for \(L\varinjlim_I\). By [Stacks, Tag 05TA], \(L\varinjlim_I\) is defined on \(D^-(\mathcal A^I)\), is exact, and is computed by bounded-above complexes with terms in \(\mathcal P\).

Given \(X\), choose by [Stacks, Tag 05T7] a quasi-isomorphism \(P\to X\) from a bounded-above complex with terms in \(\mathcal P\). Then \(L\varinjlim_IX=\varinjlim_IP\). By Lemmas 2.2 and 2.1, \(L(P)\to\varinjlim_IP\) and \(L(P)\to L(X)\) are quasi-isomorphisms. This gives the isomorphism \(L\varinjlim_IX\cong L(X)\), independent of the choice because the morphisms involved are natural. If \(H^q(X)=0\) for \(q>m\), choose \(P\) with \(P^q=0\) for \(q>m\) (loc. cit.). Then \(\varinjlim_IP\) vanishes above degree \(m\). \(\square\)

**Corollary 2.4 (adjunction).** For \(X\in D^-(\mathcal A^I)\) and \(Y\in D(\mathcal A)\) there is a canonical isomorphism
\[
\begin{aligned}&\operatorname{Hom}_{D(\mathcal A)}\bigl(L\varinjlim_IX,Y\bigr)\\&\quad\cong\operatorname{Hom}_{D(\mathcal A^I)}(X,cY),\end{aligned}
\]
functorial in \(X\) and \(Y\). In particular \(\operatorname{Ext}^i_{\mathcal A}(L\varinjlim_IX,Y)\cong\operatorname{Ext}^i_{\mathcal A^I}(X,cY)\) for every \(i\).

**Proof.** The constant-diagram functor \(c\) is exact, so it is its own derived functor and is defined on all of \(D(\mathcal A)\). It is right adjoint to \(\varinjlim_I\), and \(L\varinjlim_I\) is defined at \(X\). Apply [Stacks, Tag 0DVC]. The second statement is the first for \(Y[i]\). \(\square\)

The natural morphism \(X_i\to L(X)\), the inclusion of the summand of the \(0\)-simplex \(i\) in \(C_0\), is a morphism of complexes, because no horizontal differential leaves column \(0\). Composed with \(\varepsilon\), it is the canonical morphism \(X_i\to\varinjlim_IX\). Through Theorem 2.3, it gives canonical morphisms \(X_i\to L\varinjlim_IX\) in \(D(\mathcal A)\), natural in \(X\).

**Coinduced diagrams.** Suppose in the rest of this section that \(\mathcal A\) also has small products. For a set \(S\) and an object \(J\), write \(J^S\) for the product of copies of \(J\) indexed by \(S\). A homomorphism of free abelian groups \(\mathbb Z(S)\to\mathbb Z(S')\) induces a morphism \(J^{S'}\to J^S\), whose component at \(s\in S\) is the combination of the projections given by the image of \(s\); this is a contravariant additive functor of \(\mathbb Z(S)\). For an object \(i\) of \(I\), let \(i/I\) be the category of arrows out of \(i\). A \(p\)-simplex of its nerve is a pair \((b,\sigma)\) of an arrow \(b\colon i\to i_0\) and a \(p\)-simplex \(\sigma=(i_0\to\cdots\to i_p)\) of \(N(I)\). For \(J\in\mathcal A\) and \(p\geq0\), let \(\Pi_p(J)\in\mathcal A^I\) be the diagram with \(\Pi_p(J)(i)=J^{N_p(i/I)}\), on which an arrow \(a\colon i\to i'\) acts through the map \((b',\sigma)\mapsto(b'a,\sigma)\) from \(N_p(i'/I)\) to \(N_p(i/I)\). A morphism \(X\to\Pi_p(J)\) is the same as a family of morphisms \(\varphi_\sigma\colon X(i_0)\to J\), one for each \(\sigma\in N_p(I)\): the family gives at \(i\) the morphism with components \(\varphi_\sigma\circ X(b)\), and the morphism gives back the family through its components at the pairs \((\mathrm{id}_{i_0},\sigma)\). A morphism \(C_p(X)\to J\) is also such a family, so there is an isomorphism
\[
\begin{gathered}\operatorname{Hom}_{\mathcal A}(C_p(X),J)\\ \cong\operatorname{Hom}_{\mathcal A^I}(X,\Pi_p(J)),\end{gathered}
\tag{2.5}
\]
natural in \(X\) and \(J\). The faces of the nerves \(N(i/I)\) induce cofaces \(d^k\colon\Pi_{p-1}(J)\to\Pi_p(J)\), and (2.5) turns composition with the face \(d_k\colon C_p(X)\to C_{p-1}(X)\) into composition with \(d^k\). The diagonal morphisms \(J\to J^{N_0(i/I)}\) form a morphism \(\eta\colon cJ\to\Pi_0(J)\). Under (2.5) and the adjunction of \(\varinjlim_I\) and \(c\), composition with the augmentation \(C_0(X)\to\varinjlim_IX\) becomes composition with \(\eta\).

For a complex \(J\) of \(\mathcal A\), let \(T(J)\) be the total complex, formed with products, of the double complex with the term \(\Pi_p(J^r)\), \(p\geq0\), in degree \(p+r\), and with the differential \(\sum_k(-1)^kd^k+(-1)^p\Pi_p(d_J)\) on \(\Pi_p(J^r)\). The morphisms \(\eta\) form a morphism of complexes \(cJ\to T(J)\), since the two cofaces agree on diagonal elements. For a complex \(X\) of \(\mathcal A^I\), a morphism of degree \(m\) from \(L(X)\) to \(J\) is a family of morphisms \(f_{p,q}\colon C_p(X^q)\to J^{q-p+m}\), and one from \(X\) to \(T(J)\) is a family of morphisms \(g_{p,q}\colon X^q\to\Pi_p(J^{q-p+m})\). Let \(g_{p,q}\) correspond to \(f_{p,q}\) under (2.5), multiplied by the sign \(s_{p,m}=(-1)^{pm+p(p-1)/2}\). This defines an isomorphism of complexes
\[
\begin{gathered}\operatorname{Hom}^\bullet(L(X),J)\\ \cong\operatorname{Hom}^\bullet(X,T(J)),\end{gathered}
\tag{2.6}
\]
natural in \(X\). Indeed, by (2.5) and its naturality, the terms of the differential of \(f\) that involve \(d_J\), the faces and \(d_X\) correspond to the terms of the differential of \(g\) that involve \(\Pi_p(d_J)\), the cofaces and \(d_X\), and the signs agree because \(s_{p,m+1}=(-1)^ps_{p,m}\) and \(s_{p-1,m}=-(-1)^ms_{p,m+1}\).

**Lemma 2.7.** Let \(J\) be a complex of \(\mathcal A\).

1. The morphism \(cJ\to T(J)\) is a quasi-isomorphism.
2. If \(J\) is K-injective, so is \(T(J)\). If \(J\) is a bounded below complex of injective objects, so is \(T(J)\).

**Proof.** (1) Quasi-isomorphisms of diagrams are detected at each object. Fix \(i\). The category \(i/I\) has the initial object \(\mathrm{id}_i\), so the augmented complex \(s\mathbb Z(N(i/I))\to\mathbb Z\) has a contraction \(h\) whose maps send simplices to simplices (Lemma 2.2 of the lesson on strict simplicial objects). The contravariant functor \(\mathbb Z(S)\mapsto(J^r)^S\) turns it into a contraction \(h^\vee\) of the complex \(J^r\to\Pi_0(J^r)(i)\to\Pi_1(J^r)(i)\to\cdots\), whose first map is \(\eta\) and whose other maps are the alternating sums of the cofaces. The maps \(h^\vee\) commute with the maps \(\Pi_p(d_J)\), since the functor is natural in the object \(J^r\). The cone of \(\eta\) at \(i\) is the total complex, formed with products, of the double complex enlarged by the column \(J^r\) in position \(p=-1\). Let \(H\) be \(h^\vee\) on every term. For the differential \(D\) of the cone, the terms of \(DH+HD\) that involve \(d_J\) cancel, because \(H\) lowers \(p\) by one and the vertical differential carries the sign \((-1)^p\), and the other terms give the identity. So the cone is contractible.

(2) If \(X\) is acyclic, so is \(L(X)\), by Lemma 2.1. If \(J\) is K-injective, \(H^0\) of (2.6) identifies \(\operatorname{Hom}_{K(\mathcal A^I)}(X,T(J))\) with \(\operatorname{Hom}_{K(\mathcal A)}(L(X),J)\), which vanishes. If \(E\) is an injective object, so is \(\Pi_p(E)\), because \(\operatorname{Hom}(-,\Pi_p(E))\cong\operatorname{Hom}(C_p(-),E)\) by (2.5) and \(C_p\) is exact. If \(J^r=0\) for \(r<r_0\), then \(T(J)^n\) is the finite product of the \(\Pi_p(J^{n-p})\), \(0\leq p\leq n-r_0\), and it vanishes for \(n<r_0\). \(\square\)

**Corollary 2.8 (the adjunction of derived Hom complexes).** For complexes \(E\), \(F\) of an abelian category such that \(F\) has a K-injective resolution \(F\to J\), put \(R\operatorname{Hom}(E,F)=\operatorname{Hom}^\bullet(E,J)\). It is an object of \(D(\mathrm{Ab})\) with \(H^i=\operatorname{Hom}_D(E,F[i])\) [Stacks, Tag 070I], independent of the choice of \(J\) up to canonical isomorphism, and it depends only on the images of \(E\) and \(F\) in the derived category. Let \(Y\) be a complex of \(\mathcal A\) with a K-injective resolution \(Y\to J\). Then \(cY\to T(J)\) is a K-injective resolution, and for \(X\in D^-(\mathcal A^I)\) there is an isomorphism in \(D(\mathrm{Ab})\), natural in \(X\) and \(Y\),
\[
\begin{gathered}R\operatorname{Hom}_{\mathcal A}\bigl(L\varinjlim_IX,Y\bigr)\\ \cong R\operatorname{Hom}_{\mathcal A^I}(X,cY),\end{gathered}
\]
which induces on \(H^i\) the isomorphism of Corollary 2.4 for \(Y[i]\). Such resolutions exist for every \(Y\in D^+(\mathcal A)\) when \(\mathcal A\) has enough injectives, after replacing \(Y\) by a bounded below truncation [Stacks, Tags 013K, 070J], and for every \(Y\) when \(\mathcal A\) is a Grothendieck abelian category, that is, when it also has a generator; such a category has small products [Stacks, Tags 079P, 07D8].

**Proof.** The functor \(c\) is exact, so \(cY\to cJ\to T(J)\) is a quasi-isomorphism by Lemma 2.7 (1), and \(T(J)\) is K-injective by Lemma 2.7 (2). So \(R\operatorname{Hom}(X,cY)=\operatorname{Hom}^\bullet(X,T(J))\). By Theorem 2.3, \(L\varinjlim_IX\cong L(X)\) in \(D(\mathcal A)\), so \(R\operatorname{Hom}(L\varinjlim_IX,Y)\cong\operatorname{Hom}^\bullet(L(X),J)\), and (2.6) gives the isomorphism. Both sides of (2.6) take quasi-isomorphisms \(X'\to X\) to quasi-isomorphisms, by Lemma 2.1 and because \(J\) and \(T(J)\) are K-injective [Stacks, Tag 070I]. A morphism \(Y\to Y'\) of \(D(\mathcal A)\) induces a morphism \(J\to J'\) of the K-injective resolutions, unique up to homotopy (loc. cit.), and \(T\) preserves homotopies, being additive. This gives the naturality.

For the last assertion, let \(P\to X\) be a quasi-isomorphism from a bounded above complex of colimit-acyclic diagrams. Then \(H^i\) of the left side is \(\operatorname{Hom}_{K(\mathcal A)}(\varinjlim_IP,J[i])\), through the quasi-isomorphisms \(\varepsilon\colon L(P)\to\varinjlim_IP\) and \(L(P)\to L(X)\). The class of \(g\colon\varinjlim_IP\to J[i]\) becomes that of \(g\varepsilon\), which vanishes on the columns \(p\geq1\). So (2.6), for \(P\), carries it to the morphism with the single component \(\eta g^\flat\), where \(g^\flat\colon P\to cJ[i]\) is adjoint to \(g\). Since \(T(J)\) is identified with \(cY\) through \(cY\to cJ\xrightarrow{\eta}T(J)\), this is the morphism of \(D(\mathcal A^I)\) obtained by composing \(X\cong P\), \(g^\flat\) and \(cJ[i]\cong cY[i]\). By the construction of the isomorphism of Corollary 2.4 [Stacks, Tag 0DVC], it is the image of the class of \(g\). \(\square\)

## 3. Colimits over injective ordinals

Now let \(I=\bar\Delta'\), the category of finite totally ordered sets and injective increasing maps, as in the lesson on strict simplicial objects. Write \(X_n=X([n])\). A diagram \(F\) is *locally constant on* \(\bar\Delta'_{\geq n}\) if it sends every arrow between objects of \(\bar\Delta'_{\geq n}\) to an isomorphism.

**Lemma 3.1.** (a) Let \(S\) be a diagram with \(S_n=0\) for \(n\neq k\). Then \(S\) is colimit-acyclic and \(\varinjlim S=0\). (b) Let \(M\in\mathcal A\) and \(n\ge-1\), and let \(M_{\geq n}\) be the diagram with value \(M\) and identity maps on \(\bar\Delta'_{\geq n}\), and \(0\) on the objects \([m]\), \(m<n\). Then \(M_{\geq n}\) is colimit-acyclic, and \(M=(M_{\geq n})_n\to\varinjlim M_{\geq n}\) is an isomorphism.

**Proof.** (a) Only strings that start at \([k]\) contribute to \(C_\bullet(S)\). The face \(d_0\) of such a string is \(0\) unless the first arrow is the identity of \([k]\). So \(C_\bullet(S)\) is \(S_k\otimes Q_\bullet\), where \(Q_\bullet\) is the quotient of \(\mathbb Z(N(\bar\Delta'_{\geq k}))\) by \(\mathbb Z(N(\bar\Delta'_{\geq k+1}))\). By Deligne's theorem (Theorem 4.2 of the lesson on strict simplicial objects), the chain complex of \(Q_\bullet\) is acyclic. It is a complex of free abelian groups in degrees \(\geq0\), hence contractible: every group of cycles is free, so every short exact sequence of cycles and boundaries splits. So \(sC_\bullet(S)\) is contractible.

(b) Every string that starts in \(\bar\Delta'_{\geq n}\) stays there. So \(C_\bullet(M_{\geq n})=M\otimes\mathbb Z(N(\bar\Delta'_{\geq n}))\), with its augmentation to \(M\). The augmented complex \(s\mathbb Z(N(\bar\Delta'_{\geq n}))\to\mathbb Z\) is acyclic by Corollary 4.3 of the lesson on strict simplicial objects. It is a complex of free abelian groups bounded below, hence contractible, as in (a). So \(sC_\bullet(M_{\geq n})\to M\) is a quasi-isomorphism. The composite \(M_n\to\varinjlim M_{\geq n}\cong M\) is the identity. \(\square\)

**Proposition 3.2.** Let \(F\colon\bar\Delta'\to\mathcal A\) be locally constant on \(\bar\Delta'_{\geq n}\) for some \(n\geq-1\). Then \(F\) is colimit-acyclic, and the canonical map \(F_n\to\varinjlim F\) is an isomorphism.

**Proof.** Let \(F''\subseteq F\) agree with \(F\) on \(\bar\Delta'_{\geq n}\) and vanish on the objects \([m]\), \(m<n\). It is a subdiagram, because arrows only go to larger objects. The quotient \(F'=F/F''\) vanishes on \(\bar\Delta'_{\geq n}\). By Proposition 3.1 of the lesson on strict simplicial objects, \(F''\) restricted to \(\bar\Delta'_{\geq n}\) is isomorphic to a constant diagram, so \(F''\cong(F_n)_{\geq n}\). By Lemma 3.1 (b), \(F''\) is colimit-acyclic and \(F_n\to\varinjlim F''\) is an isomorphism. The diagram \(F'\) has the finite filtration by the subdiagrams \(F'_{\geq k}\), equal to \(F'\) on the objects \([m]\), \(m\geq k\), and \(0\) below, for \(-1\le k\le n\). Its successive quotients are concentrated at single objects. By Lemma 3.1 (a) and the long exact sequences of \(sC_\bullet\), the diagram \(F'\) is colimit-acyclic with \(\varinjlim F'=0\). The long exact sequence for \(0\to F''\to F\to F'\to0\) then shows that \(F\) is colimit-acyclic and that \(\varinjlim F''\to\varinjlim F\) is an isomorphism. The canonical map \(F_n\to\varinjlim F\) is the composite \(F_n=F''_n\to\varinjlim F''\to\varinjlim F\). \(\square\)

**Theorem 3.3.** Let \(X\) be a bounded-above complex of diagrams \(\bar\Delta'\to\mathcal A\). Suppose that for every \(i\) there is \(n(i)\geq-1\) such that the cohomology diagram \(H^i(X)\) is locally constant on \(\bar\Delta'_{\geq n(i)}\).

1. For every \(i\), the canonical map \(H^i(X_{n(i)})\to H^i(L\varinjlim X)\) is an isomorphism.
2. If moreover every term \(X^q\) is colimit-acyclic, for instance locally constant on some \(\bar\Delta'_{\geq m_q}\), then \(L\varinjlim X\to\varinjlim X\) is an isomorphism, so \(H^i(X_{n(i)})\to H^i(\varinjlim X)\) is an isomorphism.

**Proof.** (1) Fix \(i\). By Theorem 2.3, the functor \(L\varinjlim\) takes \(\tau_{\leq i-1}X\) into degrees \(\leq i-1\). The triangle \(\tau_{\leq i-1}X\to X\to\tau_{\geq i}X\) therefore gives \(H^i(L\varinjlim X)\cong H^i(L\varinjlim\tau_{\geq i}X)\). Also \(H^i(X_n)=H^i((\tau_{\geq i}X)_n)\), because evaluation is exact. So we may replace \(X\) by \(\tau_{\geq i}X\), which has finitely many nonzero cohomology diagrams. Let \(N\) be the largest of the corresponding \(n(j)\). Each \(H^j(X)\) is then locally constant on \(\bar\Delta'_{\geq N}\), and \(H^i(X)_{n(i)}\to H^i(X)_N\) is an isomorphism. So it suffices to show that \(H^j(X_N)\to H^j(L\varinjlim X)\) is an isomorphism for all \(j\). For a complex with a single nonzero cohomology diagram \(F\) in degree \(j\), we have \(L\varinjlim X\cong(L\varinjlim F)[-j]=(\varinjlim F)[-j]\), and the claim is Proposition 3.2. In general, induct on the number of nonzero cohomology diagrams. Use the triangle \(\tau_{<j}X\to X\to H^j(X)[-j]\) for the top degree \(j\), and apply the five lemma to the morphism between the long exact sequences of \(H^*((-)_N)\) and of \(H^*(L\varinjlim(-))\).

(2) By Theorem 2.3, a bounded-above complex with colimit-acyclic terms computes \(L\varinjlim\). Proposition 3.2 shows that diagrams which are eventually locally constant are colimit-acyclic. \(\square\)

## 4. Exactness of the colimit over injective ordinals

The hypothesis on the terms in Theorem 3.3 (2) always holds: over \(\bar\Delta'\), every diagram is colimit-acyclic (Theorem 4.8). The proof compares the simplicial replacement with those of the slice categories \(\bar\Delta'/[N]\), which have final objects. The comparison maps are integer combinations of injections whose composites with all injections of a given source agree.

For \(N,N'\geq-1\), let \(\mathbb Z\operatorname{Hom}([N],[N'])\) be the free abelian group on the injective increasing maps \([N]\to[N']\), with \(\operatorname{aug}(\sum_gc_gg)=\sum_gc_g\). For \(t=\sum_gc_gg\) and an injective increasing map \(h\colon[m]\to[N]\), put \(th=\sum_gc_g\,(gh)\) in \(\mathbb Z\operatorname{Hom}([m],[N'])\). Then \(\operatorname{aug}(th)=\operatorname{aug}(t)\), and \(ut=\sum_gc_g\,(ug)\) is defined in the same way for \(u\colon[N']\to[N'']\).

**Definition 4.1.** An element \(t\in\mathbb Z\operatorname{Hom}([N],[N'])\) is *equalizing* if \(th=th'\) for every \(m\) and all injective increasing maps \(h,h'\colon[m]\to[N]\).

If \(t\) is equalizing, so is \(ut\), for every injective increasing \(u\colon[N']\to[N'']\), and \(\operatorname{aug}(ut)=\operatorname{aug}(t)\).

**Lemma 4.2.** If \(N\leq0\), every element of \(\mathbb Z\operatorname{Hom}([N],[N'])\) is equalizing. If \(N\geq1\) and the elements \(t\delta^i\in\mathbb Z\operatorname{Hom}([N-1],[N'])\), \(i\in[N]\), are all equal, then \(t\) is equalizing.

**Proof.** If \(N\leq0\), there is at most one injective map \([m]\to[N]\) for each \(m\). Let \(N\geq1\), and let \(s\) be the common value of the \(t\delta^i\). For \(0\leq a\leq b\leq N-1\), the relation \(\delta^{b+1}\delta^a=\delta^a\delta^b\) (fact (3) of Section 1 of the lesson on strict simplicial objects) gives
\[
s\delta^a=t\delta^{b+1}\delta^a=t\delta^a\delta^b=s\delta^b .
\]
So the \(s\delta^a\) are all equal, and \(s\) is equalizing, by induction on \(N\) (for \(N=1\), by the first assertion). Let \(h,h'\colon[m]\to[N]\). If \(m=N\), then \(h=h'\) is the identity. If \(m<N\), then \(h\) omits some \(i\in[N]\) and \(h'\) some \(i'\). By fact (1) of the same section, \(h=\delta^ik\) and \(h'=\delta^{i'}k'\) for injective increasing maps \(k,k'\colon[m]\to[N-1]\). So \(th=sk=sk'=th'\). \(\square\)

**Gap polynomials.** Let \(n\geq0\). An injective increasing map \(g\colon[n]\to[M]\) has the *gaps* \(e_0=g(0)\), \(e_l=g(l)-g(l-1)-1\) for \(1\leq l\leq n\), and \(e_{n+1}=M-g(n)\). They are nonnegative integers with sum \(M-n\). Every such sequence occurs, for exactly one \(g\), since \(g(l)=e_0+\cdots+e_l+l\). For \(t=\sum_gc_gg\) put
\[
P_t=\sum_gc_g\,z_0^{e_0(g)}z_1^{e_1(g)}\cdots z_{n+1}^{e_{n+1}(g)} .
\]
So \(t\mapsto P_t\) is an isomorphism from \(\mathbb Z\operatorname{Hom}([n],[M])\) onto the homogeneous polynomials of degree \(M-n\) in \(\mathbb Z[z_0,\dots,z_{n+1}]\), and \(\operatorname{aug}(t)=P_t(1,\dots,1)\). For \(0\leq i\leq n\), let
\[
D_i\colon\mathbb Z[z_0,\dots,z_{n+1}]\to\mathbb Z[y_0,\dots,y_n]
\]
be the ring homomorphism with \(D_i(z_l)=y_l\) for \(l\leq i\) and \(D_i(z_l)=y_{l-1}\) for \(l>i\). It identifies \(z_i\) with \(z_{i+1}\): it is surjective, with kernel \((z_i-z_{i+1})\). The same rule defines \(D_p\colon\mathbb Z[y_0,\dots,y_n]\to\mathbb Z[w_0,\dots,w_{n-1}]\) for \(0\leq p\leq n-1\).

**Lemma 4.3.** Let \(n\geq1\), \(t\in\mathbb Z\operatorname{Hom}([n],[M])\) and \(i\in[n]\). Then \(P_{t\delta^i}=y_i\,D_i(P_t)\).

**Proof.** The image of \(g\delta^i\) is that of \(g\) without \(g(i)\). So the two gaps of \(g\) around \(g(i)\) merge, together with the point \(g(i)\). The gaps of \(g\delta^i\) are \(e_0,\dots,e_{i-1}\), then \(e_i+e_{i+1}+1\), then \(e_{i+2},\dots,e_{n+1}\). Hence the monomial of \(g\delta^i\) is \(y_i\) times the image under \(D_i\) of the monomial of \(g\). \(\square\)

**Lemma 4.4.** Let \(n\geq0\), and let \(F_0,\dots,F_n\) be polynomials in the indeterminates \(x_0,\dots,x_n,u\) with integer coefficients, such that \(F_i-F_j\in(x_i,x_j)\) for all \(i,j\). Then there is a polynomial \(C\) with \(C-F_i\in(x_i)\) for every \(i\). If the \(F_i\) are homogeneous of degree \(d\), so is \(C\).

**Proof.** For \(S\subseteq\{0,\dots,n\}\), let \(\rho_S\) be the ring endomorphism that sends \(x_l\) to \(0\) for \(l\in S\) and fixes the other indeterminates. It kills \((x_i,x_j)\) for \(i,j\in S\). So, for \(S\neq\varnothing\), \(\Phi_S=\rho_S(F_i)\) does not depend on the choice of \(i\in S\). Put
\[
C=\sum_{\varnothing\neq S}(-1)^{|S|+1}\,\Phi_S .
\]
Fix \(j\). Every polynomial \(G\) satisfies \(G-\rho_{\{j\}}(G)\in(x_j)\), and \(\rho_{\{j\}}\rho_S=\rho_{S\cup\{j\}}\). So, for \(S\neq\varnothing\) not containing \(j\), computing both with the same \(i\in S\) gives \(\Phi_S-\Phi_{S\cup\{j\}}\in(x_j)\). The terms of \(S\) and \(S\cup\{j\}\) therefore cancel modulo \(x_j\), and \(C\equiv\Phi_{\{j\}}=\rho_{\{j\}}(F_j)\equiv F_j\). The \(\rho_S\) preserve degrees. \(\square\)

**Proposition 4.5.** For all \(n\geq0\) and \(k\geq1\), there is a homogeneous polynomial \(C\in\mathbb Z[z_0,\dots,z_{n+1}]\) with \(C(1,\dots,1)=1\) such that \(y_i^k\,D_i(C)\) is the same polynomial for all \(i\in\{0,\dots,n\}\).

**Proof.** By induction on \(n\), for all \(k\) at once. For \(n=0\), take \(C=1\). Let \(n\geq1\). The case \((n-1,2k)\), written in the variables \(y_0,\dots,y_n\), gives a homogeneous \(Q\in\mathbb Z[y_0,\dots,y_n]\) with \(Q(1,\dots,1)=1\) such that \(w_p^{2k}D_p(Q)\) does not depend on \(p\in\{0,\dots,n-1\}\). Put
\[
F_i=Q\prod_{l\neq i}y_l^k\qquad(0\leq i\leq n).
\]
The ring \(\mathbb Z[z_0,\dots,z_{n+1}]\) is the polynomial ring in \(x_l=z_l-z_{l+1}\) (\(0\leq l\leq n\)) and \(u=z_{n+1}\), and the kernel of \(D_i\) is \((x_i)\). Choose homogeneous polynomials \(\tilde F_i\) in the \(z_l\) with \(D_i(\tilde F_i)=F_i\). For \(i<j\), the composites \(D_{j-1}D_i\) and \(D_iD_j\) are equal: both send \(z_i\) and \(z_{i+1}\) to \(w_i\), \(z_j\) and \(z_{j+1}\) to \(w_{j-1}\), and the other variables, in order, to the remaining \(w_l\). Their kernel is \((x_i,x_j)\). So \(\tilde F_i-\tilde F_j\in(x_i,x_j)\) as soon as \(D_{j-1}(F_i)=D_i(F_j)\).

If \(j=i+1\), then \(D_{j-1}=D_i\), and \(D_i\) sends both \(\prod_{l\neq i}y_l\) and \(\prod_{l\neq i+1}y_l\) to \(\prod_lw_l\). If \(j\geq i+2\), put \(p=i\) and \(q=j-1\), so that \(p<q\). The map \(D_q\) sends the variables \(y_l\), \(l\neq i\), to all the \(w_l\) except \(w_p\), with \(w_q\) twice. The map \(D_p\) sends the \(y_l\), \(l\neq j\), to all the \(w_l\) except \(w_q\), with \(w_p\) twice. Hence
\[
\begin{aligned}D_q(F_i)&=w_q^{2k}D_q(Q)\textstyle\prod_{l\neq p,q}w_l^k,\\D_p(F_j)&=w_p^{2k}D_p(Q)\textstyle\prod_{l\neq p,q}w_l^k,\end{aligned}
\]
and these agree by the choice of \(Q\).

Lemma 4.4 gives a homogeneous \(C\) with \(C-\tilde F_i\in(x_i)\), that is, \(D_i(C)=F_i\), for every \(i\). Then \(y_i^kD_i(C)=Q\prod_ly_l^k\) for every \(i\), and \(C(1,\dots,1)=F_0(1,\dots,1)=1\). \(\square\)

**Example 4.6.** For \(n=1\) and \(k=1\), the construction gives \(Q=1\), \(F_0=y_1\), \(F_1=y_0\) and \(C=z_0-z_1+z_2\). Let \(g_{ab}\colon[1]\to[2]\) have image \(\{a,b\}\). The corresponding element of \(\mathbb Z\operatorname{Hom}([1],[2])\) is \(t=g_{12}-g_{02}+g_{01}\), and both \(t\delta^0\) and \(t\delta^1\) equal the map \([0]\to[2]\) with value \(1\). In general, the degree of \(C\) is \(k(2^{n+1}-n-2)\), by induction, since \(\deg C=\deg Q+nk\).

**Corollary 4.7.** For every \(N\geq-1\), there are \(N'>N\) and an equalizing \(t\in\mathbb Z\operatorname{Hom}([N],[N'])\) with \(\operatorname{aug}(t)=1\).

**Proof.** For \(N\leq0\), take \(t=\delta^{N+1}\colon[N]\to[N+1]\), by Lemma 4.2. For \(N\geq1\), take \(C\) as in Proposition 4.5 for \(n=N\) and \(k=1\), of degree \(d\), and \(t\in\mathbb Z\operatorname{Hom}([N],[N+d])\) with \(P_t=C\). By Lemma 4.3, \(P_{t\delta^i}=y_iD_i(C)\) does not depend on \(i\), so neither does \(t\delta^i\), and \(t\) is equalizing by Lemma 4.2. Also \(\operatorname{aug}(t)=C(1,\dots,1)=1\). Finally \(d\geq1\): otherwise \(t\) would be the identity of \([N]\), which is not equalizing, since \(\delta^0\neq\delta^1\). \(\square\)

**Theorem 4.8.** Every diagram \(X\colon\bar\Delta'\to\mathcal A\) is colimit-acyclic. Consequently, the colimit over \(\bar\Delta'\) is exact, and for every bounded-above complex \(X\) of diagrams \(\bar\Delta'\to\mathcal A\), the morphism \(L\varinjlim X\to\varinjlim X\) is an isomorphism.

**Proof.** *Slice complexes.* For \(N\geq-1\), let \(C_\bullet(X;N)\) be the simplicial replacement of the diagram \((i,a)\mapsto X(i)\) on the slice category \(\bar\Delta'/[N]\), whose objects are the arrows \(a\colon i\to[N]\). An \(n\)-simplex of its nerve is a string \(\sigma=(i_0\to\cdots\to i_n)\) of \(\bar\Delta'\) together with an arrow \(a\colon i_n\to[N]\), so
\[
C_n(X;N)=\bigoplus_{(\sigma,a)}X(i_0).
\]
The faces and degeneracies act on \(\sigma\) as those of \(C_\bullet(X)\). The face \(d_n\), which deletes \(i_n\), replaces \(a\) by its composite with the arrow \(i_{n-1}\to i_n\). Augment \(C_\bullet(X;N)\) to \(X_N\) by \(X(a)\) on the summand of \((i_0,a)\). Let \(h\) send the summand of \((\sigma,a)\) identically to the summand of the string \(i_0\to\cdots\to i_n\xrightarrow{a}[N]\) with the arrow \(\mathrm{id}_{[N]}\), and send \(X_N\) to the summand of the \(0\)-simplex \(([N],\mathrm{id})\). These maps satisfy \(d_{n+1}h=1\) and \(d_kh=hd_k\) for \(k\leq n\). So, as in Corollary 1.2 (2) of the lesson on décalage, the maps \((-1)^{n+1}h\) form a contracting homotopy of the augmented complex \(sC_\bullet(X;N)\to X_N\). In particular \(H_q(sC_\bullet(X;N))=0\) for \(q>0\).

*Comparison maps.* Let \(\pi_N\colon C_\bullet(X;N)\to C_\bullet(X)\) send the summand of \((\sigma,a)\) identically to the summand of \(\sigma\). For \(t=\sum_gc_gg\in\mathbb Z\operatorname{Hom}([N],[N'])\), let \(t_*\colon C_\bullet(X;N)\to C_\bullet(X;N')\) send the summand of \((\sigma,a)\) to the summands of the \((\sigma,ga)\), by \(c_g\) times the identity. Both are morphisms of simplicial objects, because the faces and degeneracies change \(a\) only by composition on the right. Moreover \(\pi_{N'}t_*=\operatorname{aug}(t)\,\pi_N\).

*Passage to the colimit.* By Corollary 4.7, there are \(-1\leq N_0<N_1<\cdots\) and equalizing \(t_k\in\mathbb Z\operatorname{Hom}([N_k],[N_{k+1}])\) with \(\operatorname{aug}(t_k)=1\). We show that the \(\pi_{N_k}\) identify \(C_n(X)\) with the colimit of the sequence of the \((t_k)_*\colon C_n(X;N_k)\to C_n(X;N_{k+1})\). All these maps respect the decompositions over the strings \(\sigma\), so fix \(\sigma\), with \(i_n=[m]\), and discard the first terms of the sequence, for which \(N_k<m\) and the part over \(\sigma\) is \(0\). The part \(A_k\) of \(C_n(X;N_k)\) over \(\sigma\) is the sum of copies of \(X(i_0)\) indexed by the \(a\colon[m]\to[N_k]\). Let \(p_k\colon A_k\to X(i_0)\) be the sum map, which is the part of \(\pi_{N_k}\). Since \(t_k\) is equalizing, \(T_k=t_ka\in\mathbb Z\operatorname{Hom}([m],[N_{k+1}])\) does not depend on \(a\). So \((t_k)_*=q_kp_k\) on \(A_k\), where \(q_k\colon X(i_0)\to A_{k+1}\) is given by the coefficients of \(T_k\), and \(p_{k+1}q_k=\operatorname{aug}(T_k)=1\).

The maps \(p_k\) then make \(X(i_0)\) a colimit of the \(A_k\). They form a cocone, since \(p_{k+1}q_kp_k=p_k\). Given a cocone \(\psi_k\colon A_k\to Y\), the morphism \(\psi=\psi_{k+1}q_k\) does not depend on \(k\), because \(\psi_{k+1}q_k=\psi_{k+2}q_{k+1}p_{k+1}q_k=\psi_{k+2}q_{k+1}\). It satisfies \(\psi p_k=\psi_{k+1}q_kp_k=\psi_k\). It is unique: if \(\psi'p_{k+1}=\psi_{k+1}\), then \(\psi'=\psi'p_{k+1}q_k=\psi_{k+1}q_k\).

Colimits of complexes are computed termwise, so \(sC_\bullet(X)\) is the colimit of the complexes \(sC_\bullet(X;N_k)\) along the \((t_k)_*\). By AB5, its homology is the colimit of their homology, which vanishes in positive degrees. So \(X\) is colimit-acyclic.

*Consequences.* The functor \(X\mapsto sC_\bullet(X)\) is exact, and \(H_0(sC_\bullet(X))=\varinjlim X\) (Section 1). For a short exact sequence of diagrams, the long exact homology sequence, in which the groups \(H_1\) vanish, shows that the colimit is exact on it. By Theorem 2.3, a bounded-above complex of colimit-acyclic diagrams computes \(L\varinjlim\), which gives the last assertion. \(\square\)

**Corollary 4.9.**

1. For \(p\geq-1\), every diagram \(G\colon\bar\Delta'_{\geq p}\to\mathcal A\) is colimit-acyclic.
2. Let \(X\) be a bounded-above complex of diagrams \(\bar\Delta'\to\mathcal A\), such that every \(H^i(X)\) is locally constant on some \(\bar\Delta'_{\geq n(i)}\), \(n(i)\geq-1\). Then \(H^i(X_{n(i)})\to H^i(\varinjlim X)\) is an isomorphism for every \(i\). This is Theorem 3.3 (2) without the hypothesis on the terms.
3. For \(p\geq-1\), the augmentation \(s\mathbb Z(N(\bar\Delta'_{\geq p}))\to\mathbb Z\) is a quasi-isomorphism.

**Proof.** (1) Extend \(G\) by \(0\) to the objects \([m]\), \(m<p\). This is a diagram on \(\bar\Delta'\), because no arrow leads from \(\bar\Delta'_{\geq p}\) to a smaller object. Its simplicial replacement is that of \(G\): the strings that start in \(\bar\Delta'_{\geq p}\) stay there, and the others contribute \(0\). Apply Theorem 4.8. (2) By Theorem 4.8, \(L\varinjlim X\to\varinjlim X\) is an isomorphism. Compose it with the isomorphism of Theorem 3.3 (1). (3) Take for \(\mathcal A\) the abelian groups, and \(M=\mathbb Z\) in Lemma 3.1 (b). As in its proof, \(C_\bullet(\mathbb Z_{\geq p})=\mathbb Z(N(\bar\Delta'_{\geq p}))\). By Theorem 4.8, the positive homology vanishes. In degree \(0\), the homology is \(\varinjlim\mathbb Z_{\geq p}\). It is \(\mathbb Z\), because \(\mathbb Z_{\geq p}\) has identity maps on the connected category \(\bar\Delta'_{\geq p}\) (Proposition 3.1 of the lesson on strict simplicial objects) and vanishes on the smaller objects. \(\square\)

**Remark 4.10.** Corollary 4.9 (3) is the homological content of Deligne's theorem, Corollary 4.3 of the lesson on strict simplicial objects. The proof of Theorem 4.8 does not use that theorem: it uses only the slice categories \(\bar\Delta'/[N]\) and the equalizing elements. These have targets much larger than their sources, and over a full subcategory of \(\bar\Delta'\) with finitely many objects the colimit need not be exact (Exercise 5.3).

## 5. The simplicial replacement of a simplicial object

In this section \(\mathcal A\) is only assumed to be an additive category with small coproducts. The simplicial replacement \(C_\bullet(X)\) of Section 1 uses only sums, so it is defined for every \(X\colon I\to\mathcal A\). For a simplicial object \(X\colon\Delta^{\mathrm{op}}\to\mathcal A\), with \(X_n=X([n])\), its terms are
\[
C_n(X)=\bigoplus_{[p_n]\to\cdots\to[p_0]}X_{p_0},
\]
over the strings of \(n\) composable arrows of \(\Delta\), a string \(i_0\to\cdots\to i_n\) of \(\Delta^{\mathrm{op}}\) being one of \(\Delta\) read backwards. For a simplicial object \(Y\), \(sY\) is its chain complex, with the alternating sums of the faces as differentials.

**5.1. Free functors.** For \([p]\) in \(\Delta\) let \(h^p=\mathbb Z\operatorname{Hom}_\Delta([p],-)\colon\Delta\to\mathrm{Ab}\). By the Yoneda lemma, \(\operatorname{Hom}(h^p,F)=F([p])\) for every functor \(F\colon\Delta\to\mathrm{Ab}\). So \(h^p\) is a projective object of the abelian category \(\mathrm{Ab}^\Delta\), and the morphisms \(h^p\to h^{p'}\) are the integral combinations of the maps \(h^f\), \(g\mapsto gf\), for \(f\colon[p']\to[p]\). Let \(\mathcal F\) be the full subcategory of the sums of such functors. A morphism from \(h^p\) to a sum factors through a finite subsum, as \((\bigoplus_bF_b)([p])=\bigoplus_bF_b([p])\). So a simplicial object \(X\) of \(\mathcal A\) defines an additive functor \(\Phi_X\colon\mathcal F\to\mathcal A\) that preserves sums, with \(\Phi_X(h^p)=X_p\) and \(\Phi_X(h^f)=X(f)\). It is natural in \(X\).

**Proposition 5.2.** Let \(X\) be a simplicial object of \(\mathcal A\).

1. For an \(n\)-simplex of the nerve of \((\Delta/[q])^{\mathrm{op}}\), that is, a string \([p_n]\to\cdots\to[p_0]\) of \(\Delta\) with maps \(f_k\colon[p_k]\to[q]\) compatible with it, the values \(f_0(0)\leq f_1(0)\leq\cdots\leq f_n(0)\) define an \(n\)-simplex of \(\Delta[q]\). These *first-vertex maps* form a map of simplicial sets \(N((\Delta/[q])^{\mathrm{op}})\to\Delta[q]\), natural in \([q]\), and they induce a map of simplicial objects \(\phi_X\colon C_\bullet(X)\to X\), natural in \(X\).
2. The map \(s(\phi_X)\colon sC_\bullet(X)\to sX\) is a homotopy equivalence. A homotopy inverse and the homotopies can be chosen natural in \(X\).
3. Let \(X\) be an \(r\)-simplicial object \((\Delta^{\mathrm{op}})^r\to\mathcal A\), and \(\delta X\) its diagonal, \([n]\mapsto X_{n,\ldots,n}\). The componentwise first-vertex maps induce a map \(C_\bullet(X)\to\delta X\), natural in \(X\), whose chain map is a homotopy equivalence, with a homotopy inverse and homotopies natural in \(X\).
4. Dually, if \(\mathcal A\) has small products, a cosimplicial object of \(\mathcal A\) is homotopy equivalent to its cosimplicial replacement, whose terms are the products of the values at the targets of the strings, by the statements (1) and (2) for the simplicial object of the opposite category \(\mathcal A^{\mathrm{op}}\); and likewise for \(r\)-cosimplicial objects.

**Proof.** (1) For an inner face or a degeneracy of the string, the sequence of first vertices loses or repeats the corresponding term. The face \(d_0\) drops \([p_0]\to[q]\), and \(d_n\) drops \([p_n]\to[p_{n-1}]\); in both cases the sequence loses its first, respectively last, term. Composition with a map \([q]\to[q']\) composes the \(f_k\) with it. This gives a natural map of simplicial sets. Let \(W_n\) and \(W'_n\) be the functors \([q]\mapsto\mathbb ZN_n((\Delta/[q])^{\mathrm{op}})\) and \([q]\mapsto\mathbb Z\Delta[q]_n\). Then \(W'_n=h^n\), and \(W_n\) is the sum of the \(h^{p_0}\) over the strings \([p_n]\to\cdots\to[p_0]\). So both are in \(\mathcal F\), and the first-vertex maps form a map of simplicial objects \(W\to W'\) of \(\mathcal F\). Applying \(\Phi_X\), \(\Phi_X(W')=X\), with the faces and degeneracies \(X(\delta^j)\) and \(X(\sigma^j)\), and \(\Phi_X(W)=C_\bullet(X)\), with the faces and degeneracies of Section 1: \(d_0\) applies \(X\) to \([p_1]\to[p_0]\), and the others act on the strings. This defines \(\phi_X\).

(2) For every \([q]\), the category \((\Delta/[q])^{\mathrm{op}}\) has the initial object \(\mathrm{id}_{[q]}\), and \([q]\) has the initial object \(0\), with nerve \(\Delta[q]\). So both augmented complexes \(s\mathbb ZN((\Delta/[q])^{\mathrm{op}})\to\mathbb Z\) and \(s\mathbb Z\Delta[q]\to\mathbb Z\) are contractible (Lemma 2.2 of the lesson on strict simplicial objects), and the first-vertex map, compatible with the augmentations, is a quasi-isomorphism at every \([q]\). Hence \(sW\to sW'\) is a quasi-isomorphism of bounded above complexes of projective objects of \(\mathrm{Ab}^\Delta\), so it is a homotopy equivalence: between such complexes the morphisms of the homotopy category are those of the derived category [Stacks, Tag 064B], where the map is invertible. A homotopy inverse and the homotopies are morphisms between objects of \(\mathcal F\), as \(\mathcal F\) is a full subcategory. The additive functor \(\Phi_X\) carries them to a homotopy inverse of \(s(\phi_X)\) and to homotopies, natural in \(X\).

(3) The same argument applies with \(\Delta^r\) in place of \(\Delta\). The functors \(h^{\underline p}=\mathbb Z\operatorname{Hom}_{\Delta^r}(\underline p,-)\) are projective, \(\Phi_X(h^{\underline p})=X_{\underline p}\), and \(C_n(X)=\Phi_X(W_n)\) for \(W_n(\underline q)=\mathbb ZN_n((\Delta^r/\underline q)^{\mathrm{op}})\). The diagonal is \(\Phi_X(W')\) for \(W'_n(\underline q)=\mathbb Z(\Delta[q_1]\times\cdots\times\Delta[q_r])_n\), which is \(h^{(n,\ldots,n)}\). The category \((\Delta^r/\underline q)^{\mathrm{op}}\) has an initial object, and \(\Delta[q_1]\times\cdots\times\Delta[q_r]\) is the nerve of the ordered set \([q_1]\times\cdots\times[q_r]\), with the least element \((0,\ldots,0)\).

(4) A cosimplicial object of \(\mathcal A\) is a simplicial object of \(\mathcal A^{\mathrm{op}}\), which is additive with small coproducts; sums in \(\mathcal A^{\mathrm{op}}\) are products in \(\mathcal A\). \(\square\)

The naturality in \(X\) makes these homotopy equivalences compatible with every family of simplicial objects indexed by a further category, for instance by the category of injective ordinals of Sections 3 and 4.

## 6. Exercises

**Exercise 6.1.** Let \(I\) have two objects \(a,b\) and two arrows \(f,g\colon a\to b\) besides the identities. For \(X=(X_a\rightrightarrows X_b)\), with \(u=X(f)\) and \(v=X(g)\), show that \(\varinjlim X=X_b/\operatorname{im}(u-v)\), that \(L_1\varinjlim X\cong\ker(u-v)\), and that \(L_n\varinjlim X=0\) for \(n\geq2\). Conclude that the colimit over \(I\) is not exact.

**Exercise 6.2.** Suppose \(I\) has a final object \(t\). Show that every diagram is colimit-acyclic and that \(\varinjlim_IX=X(t)\).

**Exercise 6.3.** Let \(M\neq0\) be an object of \(\mathcal A\), and define \(X\colon\bar\Delta'\to\mathcal A\) by \(X_0=X_1=M\), \(X(\delta^0)=X(\delta^1)=\mathrm{id}_M\colon X_0\to X_1\), and \(X_n=0\) for \(n\notin\{0,1\}\). Show that \(X\) is a functor with \(\varinjlim X=0\), and that \(X\) is colimit-acyclic. Let \(I\) be the full subcategory of \(\bar\Delta'\) on \([0]\) and \([1]\). Show that the restriction of \(X\) to \(I\) has colimit \(M\) and first derived colimit \(M\), so that the colimit over \(I\) is not exact.

**Exercise 6.4.** Show that the element \(t=g_{12}-g_{02}+g_{01}\) of Example 4.6 is the only equalizing element of \(\mathbb Z\operatorname{Hom}([1],[2])\) with augmentation \(1\), and that \(\mathbb Z\operatorname{Hom}([1],[1])\) contains no equalizing element with augmentation \(1\).

## 7. Complete solutions

**6.1.** The nerve of \(I\) has no strings of two composable non-identity arrows. By [Stacks, Tag 019C], the chain complex \(sC_\bullet(X)\) is quasi-isomorphic to its quotient by the degenerate part. That quotient is \(X_a\oplus X_a\to X_a\oplus X_b\) in degrees \(1\) and \(0\), with the two summands of degree \(1\) belonging to \(f\) and to \(g\). The differential \(d_0-d_1\) sends \(x\) in the summand of \(f\) to \((-x,u(x))\), and \(x\) in the summand of \(g\) to \((-x,v(x))\). Eliminating the summand \(X_a\) of degree \(0\), the cokernel is \(X_b/\operatorname{im}(u-v)\). The kernel consists of the pairs \((x,y)\) with \(x+y=0\) and \(u(x)+v(y)=0\), that is \(y=-x\) and \(x\in\ker(u-v)\). There is nothing in degrees \(\geq2\). For \(u=v=0\) and \(X_a\neq0\), the first derived colimit \(\ker(u-v)=X_a\) is nonzero, so the colimit is not exact.

**6.2.** A cocone from \(X\) to an object \(Z\) is determined by its component at \(t\), since every \(X(i)\to Z\) factors through \(X(i)\to X(t)\). So \(\varinjlim_IX=X(t)\). For the acyclicity, append \(t\) to every string: send the summand of \(i_0\to\cdots\to i_n\) identically to the summand of \(i_0\to\cdots\to i_n\to t\) in \(C_{n+1}(X)\), and send \(X(t)\) to the summand of the \(0\)-simplex \(t\). These maps satisfy \(d_{n+1}h=1\) and \(d_kh=hd_k\) for \(k\leq n\). So, as in Corollary 1.2 (2) of the lesson on décalage, the maps \((-1)^{n+1}h\) form a contracting homotopy of the augmented complex \(sC_\bullet(X)\to X(t)\).

**6.3.** An arrow of \(\bar\Delta'\) between objects of \(I\) is an identity, \(\delta^0\) or \(\delta^1\). Every other arrow has its source or its target outside \(I\), where \(X\) vanishes. A composite \(gf\) whose source and target lie in \(I\) passes through an object of \(I\), since the objects increase along arrows. So the rule given, with \(0\) on all other arrows, is a functor. A cocone \(\varphi_n\colon X_n\to Y\) satisfies \(\varphi_1=\varphi_2X(\delta^2)=0\), for \(\delta^2\colon[1]\to[2]\), and then \(\varphi_0=\varphi_1X(\delta^0)=0\). So \(\varinjlim X=0\). The diagram vanishes on \(\bar\Delta'_{\geq2}\), so it is colimit-acyclic by Proposition 3.2. The category \(I\) is that of Exercise 5.1, with \(u=v=\mathrm{id}_M\). So the colimit over \(I\) of the restriction is \(M/\operatorname{im}(u-v)=M\), and its first derived colimit is \(\ker(u-v)=M\neq0\). An exact functor has no higher left derived functors, so the colimit over \(I\) is not exact.

**6.4.** Write \(t=a\,g_{01}+b\,g_{02}+c\,g_{12}\), and let \(v_j\colon[0]\to[2]\) have value \(j\). Composing with \(\delta^0\) keeps the second point of the image, and composing with \(\delta^1\) the first. So
\[
\begin{aligned}t\delta^0&=a\,v_1+(b+c)\,v_2,\\ t\delta^1&=(a+b)\,v_0+c\,v_1 .\end{aligned}
\]
They agree exactly when \(a+b=0\), \(a=c\) and \(b+c=0\), that is, when \(t=a\,(g_{01}-g_{02}+g_{12})\), whose augmentation is \(a\). By Lemma 4.2 these are the equalizing elements, and \(a=1\) gives the element of Example 4.6. The group \(\mathbb Z\operatorname{Hom}([1],[1])\) is generated by the identity, and \(a\,\mathrm{id}\) composed with \(\delta^0\) and with \(\delta^1\) gives \(a\delta^0\) and \(a\delta^1\), which agree only for \(a=0\).

## Sources

The derived colimit computed by the simplicial replacement, and its application to colimits over the category of finite ordinals and injective maps, are in Illusie's work on the cotangent complex, where the derived colimit over that category of a bounded-above complex with eventually locally constant cohomology diagrams is identified with its termwise colimit. The proof given here of the exactness of that colimit (Section 4) goes through equalizing combinations of injections, built from gap polynomials by interpolation on the hyperplanes \(z_i=z_{i+1}\). The homotopy equivalences between a simplicial object and its simplicial replacement, and between the simplicial replacement of a multisimplicial object and its diagonal (Section 5), are also due to Illusie, who deduces them from the case of free simplicial abelian groups by the method of the Eilenberg–Zilber theorem; the proof given here compares the two weights, the nerves of the slice categories and the standard simplices, as complexes of projective functors on the simplex category. The adjunction in the form of derived Hom complexes is also in Illusie's work, for an abelian category with enough injectives and a bounded below second argument, where it is reduced to induced diagrams; the proof given here (Corollary 2.8) resolves constant diagrams by coinduced diagrams, which also gives the case of an unbounded second argument in a Grothendieck abelian category. The general framework of derived functors on bounded-above derived categories and of adjoint derived functors used here is that of the Stacks project, Chapter *Derived Categories*.
