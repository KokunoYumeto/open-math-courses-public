# Chern classes of perfect complexes

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a map of rings \(A\to B\) of a topos, every perfect complex \(E\) of \(B\)-modules carries its Atiyah class \(\operatorname{at}(E)\colon E\to E\otimes^{\mathbf L}_BL_{B/A}[1]\), an endomorphism of \(E\) with coefficients in \(L_{B/A}[1]\). Its L-series and characteristic series, with the shift isomorphism \(LS^n(L_{B/A}[1])\cong L\Lambda^n(L_{B/A})[n]\), give classes
\[
c^n(E)\in H^n(T,L\Lambda^nL_{B/A}),
\]
the Chern classes of \(E\) with values in the cotangent complex. Their images in \(H^n(T,\Omega^n_{B/A})\) are Chern classes in Hodge cohomology. The lesson proves:

- the total Chern class \(c_t(E)=\sum c^n(E)t^n\) is multiplicative on filtrations, gradings and distinguished triangles, so it defines a homomorphism from the Grothendieck group of perfect complexes to the group of series with constant term \(1\);
- it is compatible with base change along squares of rings and along morphisms of ringed topoi;
- \(c^n(E)=0\) for \(n>r\) when \(E\) is a module in degree \(0\) that is locally a direct summand of a free module of rank \(r\);
- when \(B\) is a local ring, perfect complexes have an integral rank, additive on triangles, and the rank and the total Chern class together define a homomorphism on the Grothendieck group;
- the Hodge-cohomology classes \(c'_t(E)\) satisfy the same formulas, are computed from the extension of principal parts, and for an invertible module \(c'_t(E)=1+c'^1(E)t\), with \(c'^1(E)\) the negative of the class of the extension of \(B\) by \(\Omega_{B/A}\) whose local splittings are the local connections on \(E\); on a smooth scheme this is \(c'^1(L)=-c_1^{\mathrm{Hodge}}(L)\), the first Chern class defined through \(\mathrm d\log\).

**Prerequisites.** [*The Atiyah class of filtered complexes*](the-atiyah-class-of-filtered-complexes.md) (Definition 1.1, Proposition 1.2, Theorem 3.1, Corollary 3.2, Definition 3.3, Proposition 3.4, Definition 4.1, Proposition 4.2); [*L-series of endomorphisms of perfect complexes*](l-series-of-endomorphisms-of-perfect-complexes.md) (Propositions 1.2, 1.3, 3.2, 3.6, Theorem 3.3, Corollaries 3.4, 3.7, Definition 3.5); [*The Atiyah class of a module*](the-atiyah-class-of-a-module.md) (Lemma 1.2, Proposition 3.2); Lemma 3.7 of [*Deformations of modules and of their morphisms*](deformations-of-modules-and-of-their-morphisms.md) (boundaries through local lifts); [*Traces and cup products of perfect filtered complexes*](traces-and-cup-products-of-perfect-filtered-complexes.md) (Definitions 1.1, 2.1, Theorem 2.3); [*Filtered and graded powers of complexes*](filtered-and-graded-powers-of-complexes.md) (Lemma 1.3, Theorem 2.6); [*Filtered derived categories*](filtered-derived-categories.md) (Proposition 2.2). From the AI-integrated Stacks project: invertible modules and the first Chern class in Hodge cohomology [[Tag 09NU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-lemma-h1-invertible), [Tag 0FLE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derham.html#derham-section-first-chern-class)]; locally ringed topoi [[Stacks, Tag 04ES](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-locally-ringed), [Tag 04EU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-definition-locally-ringed)]; strictly perfect complexes [[Tag 08FL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-definition-strictly-perfect)], and morphisms out of them are locally maps of complexes [[Tag 08FR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-local-actual)]; the third vertex of a distinguished triangle [[Tag 014A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-third-isomorphism-triangle)]; triangles of short exact sequences [[Stacks, Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor)] and termwise split replacements [[Tag 014M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-sequence-maps-split)]; the cotangent complex of a morphism of ringed topoi [[Tag 08SU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-definition-cotangent-complex-morphism-ringed-topoi)].

## Conventions

As in the lesson on the Atiyah class of filtered complexes: \(T\) is a topos, \(A\to B\) a map of rings of \(T\), \(L=L_{B/A}\), \(\Omega=\Omega_{B/A}\), \(\alpha\colon L\to\Omega\) the augmentation, tensor products derived, and \(\operatorname{at}(E)\colon E\to E\otimes L[1]\) the Atiyah class of \(E\in D^-(B)\). An object of \(D(B)\) has bounded perfect amplitude if it has perfect amplitude in some interval, as in the lesson on L-series; such objects lie in \(D^-(B)\). For \(X\in D(B)\) and \(n\in\mathbf Z\), \(H^n(T,X)=\operatorname{Hom}_{D(B)}(B,X[n])\). Since \(L\) is concentrated in degrees \(\leq0\), \(L[1]\in D^{\leq0}(B)\), and the rings \(\operatorname{Hom}(B,LS^\bullet(L[1]))\) and \(\operatorname{Hom}(B,L\Lambda^\bullet(L)[1])=\) \(\prod_nH^n(T,L\Lambda^nL)\) of the lesson on L-series are commutative (Proposition 1.2 (2) there); \(\sigma^S\) is the ring isomorphism between them of Proposition 1.3 there.

## 1. Chern classes with values in the cotangent complex

**Definition 1.1.** Let \(E\in D(B)\) have bounded perfect amplitude. The *L-series* and the *total Chern class* of \(E\) relative to \(A\to B\) are
\[
\begin{aligned}&L_t(E)=L_t(E,B/A)\\
&\quad=\sigma^S\bigl(L_t(\operatorname{at}(E))\bigr),\\
&c_t(E)=c_t(E,B/A)\\
&\quad=\sigma^S\bigl(c_t(\operatorname{at}(E))\bigr)=L_t(E)^{-1},\end{aligned}
\]
in \(\operatorname{Hom}(B,L\Lambda^\bullet(L)[1])\), where \(L_t(\operatorname{at}(E))\) and \(c_t(\operatorname{at}(E))\) are the series of Definition 3.5 of the lesson on L-series for \(M=L[1]\). The coefficient of \(t^n\) in \(c_t(E)\) is the \(n\)-th *Chern class* \(c^n(E)=c^n(E,B/A)\in H^n(T,L\Lambda^nL)\); \(c^0(E)=1\).

**Proposition 1.2.** Let \(E,E'\in D(B)\) have bounded perfect amplitude.

1. If \(E\cong E'\), then \(L_t(E)=L_t(E')\).
2. \(L_t(E[1])=c_t(E)\); hence \(L_t(E[2])=L_t(E)\).
3. If \(E\in D^{\leq0}(B)\), then \(c_t(\operatorname{at}(E))=\) \(\sum_n(-1)^n\operatorname{Tr}(\psi^nL\Lambda^n\operatorname{at}(E))t^n\), with \(\psi^n=\psi^n_{E,L[1]}\).

**Proof.** (1) For an isomorphism \(u\colon E\to E'\), \(\operatorname{at}(E')=(u\otimes1)\circ\operatorname{at}(E)\circ u^{-1}\) (Proposition 3.4 of the lesson on the Atiyah class of filtered complexes), and Proposition 3.2 (2) of the lesson on L-series, in the form of Proposition 3.6 there, applies. (2) \(\operatorname{at}(E[1])=\operatorname{at}(E)[1]\) (Proposition 3.4 of the lesson on the Atiyah class of filtered complexes), and \(L_t(\operatorname{at}(E)[1])=c_t(\operatorname{at}(E))\) (Proposition 3.6 of the lesson on L-series). (3) Corollary 3.7 of the lesson on L-series, \(E\) and \(L[1]\) being in \(D^{\leq0}(B)\). \(\square\)

**Theorem 1.3 (multiplicativity).**

1. Let \(E\in DF(B)\) have bounded perfect amplitude. Then \(L_t(E)=\prod_pL_t(\operatorname{gr}^pE)\) and \(c_t(E)=\prod_pc_t(\operatorname{gr}^pE)\).
2. Let \(E\in DG(B)\) have bounded perfect amplitude, with components \(E_i\). Then \(L_t(\bigoplus_iE_i)=\prod_iL_t(E_i)\), and likewise for \(c_t\).
3. For a distinguished triangle \(E'\to E\to E''\to E'[1]\) of objects of bounded perfect amplitude, \(L_t(E)=L_t(E')L_t(E'')\) and \(c_t(E)=c_t(E')c_t(E'')\).

**Proof.** (1) By Proposition 3.4 of the lesson on the Atiyah class of filtered complexes, \(\operatorname{at}^F(E)\colon E\to E\otimes L[1]\) is a morphism of \(DF(B)\), \(L[1]\) in filtration \([0,0]\), with underlying morphism \(\operatorname{at}(E)\) and graded pieces \(\operatorname{at}(\operatorname{gr}^pE)\). Theorem 3.3 (1) and (2) of the lesson on L-series, in the form of Proposition 3.6 there, give \(L_t(\operatorname{at}(E))=\) \(L_t(\bigoplus_p\operatorname{at}(\operatorname{gr}^pE))=\) \(\prod_pL_t(\operatorname{at}(\operatorname{gr}^pE))\), and \(\sigma^S\) is a ring isomorphism. The ring is commutative, so the statement for \(c_t\) follows by taking inverses. (2) \(\operatorname{at}(\bigoplus_iE_i)=\bigoplus_i\operatorname{at}(E_i)\) is a morphism of \(DG(B)\), and Theorem 3.3 (2) of the lesson on L-series applies. (3) By [Tag 014M] and [Tag 0152] the triangle is isomorphic to the triangle of a short exact sequence \(0\to X'\to X\to X''\to0\) of complexes. The complex \(X\) filtered by \(F^1X=X'\), \(F^0X=X\), \(F^2X=0\) is an object of \(DF(B)\) with \(\operatorname{gr}^1=X'\) and \(\operatorname{gr}^0=X''\), of bounded perfect amplitude; (1) and Proposition 1.2 (1) give the statement. \(\square\)

**Corollary 1.4 (Grothendieck group).** Let \(K(B)\) be the Grothendieck group of the objects of \(D(B)\) of bounded perfect amplitude: the free abelian group on their isomorphism classes, modulo \([E]=[E']+[E'']\) for every distinguished triangle \(E'\to E\to E''\to E'[1]\). Then \([E]\mapsto c_t(E)\) is a homomorphism from \(K(B)\) to the multiplicative group of series with constant term \(1\) in \(\operatorname{Hom}(B,L\Lambda^\bullet(L)[1])\), and \([E]\mapsto L_t(E)\) is the composite with inversion. The trace of the identity, \([E]\mapsto\operatorname{Tr}(1_E)\in\Gamma(T,B)\), is additive on triangles (Theorem 2.3 of the lesson on traces, for the filtered object of the proof of Theorem 1.3 (3)), so \([E]\mapsto(\operatorname{Tr}(1_E),c_t(E))\) is a homomorphism to \(\Gamma(T,B)\times\operatorname{Hom}(B,L\Lambda^\bullet(L)[1])^+\).

**Proof.** Theorem 1.3 (3) and Proposition 1.2 (1). \(\square\)

**Proposition 1.5 (base change).**

1. Let \((A\to B)\to(A'\to B')\) be a commutative square of rings of \(T\), \(c\colon L_{B/A}\otimes B'\to L_{B'/A'}\) the functoriality map, and let \(\overline c\colon\operatorname{Hom}(B,L\Lambda^\bullet(L_{B/A})[1])\to\) \(\operatorname{Hom}(B',L\Lambda^\bullet(L_{B'/A'})[1])\) be extension of scalars to \(B'\) followed by \(L\Lambda^n(c)[n]\). For \(E\) of bounded perfect amplitude and an isomorphism \(E\otimes^{\mathbf L}_BB'\cong E'\), \(L_t(E',B'/A')=\overline c\,L_t(E,B/A)\) and \(c_t(E',B'/A')=\overline c\,c_t(E,B/A)\).
2. Let \(f\colon T'\to T\) be a morphism of topoi. Then \(L_t(f^{-1}E,f^{-1}B/f^{-1}A)=\) \(f^{-1}L_t(E,B/A)\), through \(f^{-1}L_{B/A}=L_{f^{-1}B/f^{-1}A}\).
3. Let \(g\colon X'\to X\) and \(h\colon Y'\to Y\) be morphisms of ringed topoi with \(f\circ g=h\circ f'\) for morphisms of ringed topoi \(f\colon X\to Y\), \(f'\colon X'\to Y'\), and write \(L_{X/Y}=L_{\mathcal O_X/f^{-1}\mathcal O_Y}\) [Tag 08SU], \(L_t(E,X/Y)=L_t(E,\mathcal O_X/f^{-1}\mathcal O_Y)\). For \(E\) of bounded perfect amplitude on \(X\), \(g^*L_t(E,X/Y)=L_t(Lg^*E,X'/Y')\), where \(g^*\) is the inverse image followed by the functoriality map \(Lg^*L_{X/Y}\to L_{X'/Y'}\).

**Proof.** (1) Let \(u\colon E\otimes B'\to E'\) be the isomorphism. By Proposition 1.2 (2) of the lesson on the Atiyah class of filtered complexes (with Proposition 3.4 there), \(\operatorname{at}(E')=(u\otimes c[1])\circ(\operatorname{at}(E)\otimes B')\circ u^{-1}\). By Proposition 3.2 of the lesson on L-series (invariance, naturality in \(M\) for \(c[1]\), and base change along the morphism of ringed topoi \((T,B')\to(T,B)\)), \(L_t(\operatorname{at}(E'))\) is the image of \(L_t(\operatorname{at}(E))\) under base change followed by \(LS^n(c[1])\). Finally \(\sigma^S\) is natural in the coefficient object. (2) Proposition 1.2 (3) of the lesson on the Atiyah class of filtered complexes and Proposition 3.2 (3) of the lesson on L-series. (3) \(Lg^*E=\mathcal O_{X'}\otimes_{g^{-1}\mathcal O_X}g^{-1}E\): apply (2) to the underlying morphism of topoi of \(g\), then (1) on \(X'\) to the square of rings \((g^{-1}f^{-1}\mathcal O_Y\to g^{-1}\mathcal O_X)\to\) \((f'^{-1}\mathcal O_{Y'}\to\mathcal O_{X'})\), whose functoriality map, composed with the identification of (2), is the functoriality map \(Lg^*L_{X/Y}\to L_{X'/Y'}\). \(\square\)

**Proposition 1.6 (rank).** Let \(E\) be a \(B\)-module, placed in degree \(0\), such that every object of \(T\) has a covering on whose members \(E\) is a direct summand of \(B^r\). Then \(E\) has perfect amplitude in \([0,0]\), and \(c^n(E)=0\) for \(n>r\).

**Proof.** \(E\) is locally a direct summand of a finite free module, so it is flat and has perfect amplitude in \([0,0]\), and \(L\Lambda^nE=\Lambda^nE\), which vanishes for \(n>r\) because it vanishes locally, being a direct summand of \(\Lambda^nB^r=0\). By Proposition 1.2 (3) the coefficient of \(t^n\) in \(c_t(\operatorname{at}(E))\) is a trace over the zero object, which is \(0\), and \(\sigma^S\) preserves degrees. \(\square\)

In the rest of this section, \(B\) is a *local ring*: for every object \(V\) of \(T\) and \(f\in B(V)\), \(V\) has a covering on whose members \(f\) or \(1-f\) is invertible, and \(B(V)\) is the zero ring only if \(V\) is initial. These are the conditions of a locally ringed topos [Stacks, Tags 04ES, 04EU]. The second is stated there as: the subsheaf of the final object over which \(0=1\) in \(B\) is initial. The two forms agree, because a sheaf with a morphism to the initial sheaf is itself initial: the initial sheaf has no sections over an object unless the empty family covers it, and then one. Over an initial object every sheaf has exactly one section.

A *finite free complex* over an object \(U\) is a bounded complex \(S\) of \(B|_U\)-modules whose terms are finite free, \(S^i\cong B^{r_i}|_U\); it is strictly perfect [Stacks, Tag 08FL], a strictly perfect complex being a bounded complex whose terms are direct summands of finite free modules. The *Euler number* of a finite free complex is \(\chi(S)=\sum_i(-1)^ir_i\). By the following lemma it is well defined when \(U\) is not initial.

**Lemma 1.7.** Let \(U\) be an object of \(T\) that is not initial.

1. Every covering of \(U\) has a member that is not initial, and \(B(U)\neq0\).
2. If \(B^m|_U\cong B^n|_U\) as \(B|_U\)-modules, then \(m=n\).
3. Every direct summand of \(B^n|_U\) is locally free: \(U\) has a covering on whose members it is isomorphic to some \(B^k\).
4. If \(S\) is an acyclic finite free complex over \(U\), then \(\chi(S)=0\).

**Proof.** (1) If every member \(U_j\) of a covering were initial, then \(B(U)\to\prod_jB(U_j)\) would be injective, with target the zero ring, so \(B(U)=0\) and \(U\) would be initial.

(2) Morphisms \(B^m|_U\to B^n|_U\) are \(n\times m\) matrices over \(B(U)\), so the isomorphism and its inverse give \(B(U)^m\cong B(U)^n\). Tensoring with the residue field of a maximal ideal of the nonzero ring \(B(U)\) gives vector spaces of dimensions \(m\) and \(n\), so \(m=n\).

(3) Let \(P\) be a direct summand of \(F=B^n|_U\), with complement \(Q\), and \(e\in M_n(B(U))\) the projection onto \(P\) along \(Q\). We argue by induction on \(n\), the case \(n=0\) being clear. Let \(f_1,\ldots,f_n\) be the standard basis. On the members of a covering, \(e_{11}\) or \(1-e_{11}\) is invertible. Where \(e_{11}\) is invertible, \(v=e(f_1)\in P\) has invertible first coordinate, so \(v,f_2,\ldots,f_n\) is a basis of \(F\), its matrix having determinant \(e_{11}\). Let \(C\) be the span of \(f_2,\ldots,f_n\). Since \(Bv\subseteq P\) and \(F=Bv\oplus C\), \(P=Bv\oplus(P\cap C)\). Moreover \(P\cap C\cong P/Bv\) is a direct summand of \(F/Bv=P/Bv\oplus Q\cong C\cong B^{n-1}\), so it is locally free by induction, and so is \(P\). Where \(1-e_{11}\) is invertible, the same argument for \(Q\), the image of \(1-e\), gives \(w=(1-e)(f_1)\) with \(F=Bw\oplus C\) and \(Bw\subseteq Q\). Then \(P\) maps isomorphically onto a direct summand of \(F/Bw=P\oplus Q/Bw\cong B^{n-1}\), and it is locally free by induction.

(4) Let \(S\) have terms in degrees \([a,b]\), with \(S^i\cong B^{r_i}\). If \(a=b\), then \(S^a=0\) and \(r_a=0\) by (2). Let \(a<b\). The differential \(d\colon S^{b-1}\to S^b\) is an epimorphism, so on a covering the basis of \(S^b\) lifts, which gives \(s\colon S^b\to S^{b-1}\) with \(ds=1\). Then \(S^{b-1}=K\oplus s(S^b)\), with \(K=\ker d\) a direct summand of \(B^{r_{b-1}}\). By (3), on a further covering \(K\cong B^k\). The complex with terms \(S^i\) for \(i<b-1\) and \(K\) in degree \(b-1\) is an acyclic finite free complex in degrees \([a,b-1]\). On a non-initial member of the covering, which exists by (1), \(r_{b-1}=k+r_b\) by (2), and by induction \(\sum_{i<b-1}(-1)^ir_i+(-1)^{b-1}k=0\). Hence \(\chi(S)=0\). \(\square\)

**Proposition 1.8 (the integral rank).** Let \(E\in D(B)\) have bounded perfect amplitude. There is a unique global section \(\operatorname{rg}(E)\) of the constant sheaf \(\mathbf Z\) on \(T\) such that \(\operatorname{rg}(E)|_U=\chi(S)\) for every object \(U\) and every finite free complex \(S\) over \(U\) with \(S\cong E|_U\). It depends only on the isomorphism class of \(E\), and for every distinguished triangle \(E'\to E\to E''\to E'[1]\) of objects of bounded perfect amplitude,
\[
\operatorname{rg}(E)=\operatorname{rg}(E')+\operatorname{rg}(E'').
\]

**Proof.** By definition of bounded perfect amplitude, the final object has a covering on whose members \(E\) is isomorphic to a strictly perfect complex. By Lemma 1.7 (3), applied to its finitely many terms, there is a finer covering \(\{U_j\}\) with finite free complexes \(S_j\cong E|_{U_j}\). Let \(S\) over \(U\) and \(S'\) over \(U'\) be two such representatives, and \(W=U\times U'\). On \(W\), the isomorphism \(S|_W\cong E|_W\cong S'|_W\) of \(D(B|_W)\) is given, on the members \(W_k\) of a covering, by maps of complexes \(\varphi_k\colon S|_{W_k}\to S'|_{W_k}\) [Stacks, Tag 08FR]. These are quasi-isomorphisms, so their cones are acyclic finite free complexes, with Euler numbers \(\chi(S')-\chi(S)\) because the cone of \(\varphi_k\) has the terms \(S^{i+1}\oplus S'^i\). By Lemma 1.7 (4), \(\chi(S)=\chi(S')\) on every non-initial \(W_k\). On an initial object all sections of \(\mathbf Z\) agree. So the sections \(\chi(S_j)\) of \(\mathbf Z\) over the \(U_j\) agree on the overlaps and glue to a unique global section \(\operatorname{rg}(E)\), with the stated property for every representative. A representative of \(E\) is one of every object isomorphic to \(E\).

Let \(E'\to E\to E''\to E'[1]\) be a distinguished triangle. On the members of a covering of the final object, \(E'\) and \(E\) have finite free representatives \(S'\) and \(S\), and by [Stacks, Tag 08FR] the morphism \(E'\to E\) is given by a map of complexes \(\varphi\colon S'\to S\). The triangle \(S'\to S\to\operatorname{cone}(\varphi)\to S'[1]\) is distinguished, so \(E''\) is isomorphic there to \(\operatorname{cone}(\varphi)\) [Tag 014A], a finite free complex with \(\chi(\operatorname{cone}(\varphi))=\chi(S)-\chi(S')\). Hence \(\operatorname{rg}(E'')=\operatorname{rg}(E)-\operatorname{rg}(E')\) on every member, and so globally. \(\square\)

**Corollary 1.9.** If \(B\) is a local ring, then
\[
\begin{aligned}[E]&\mapsto(\operatorname{rg}(E),c_t(E))\in\Gamma(T,\mathbf Z)\\&\qquad\times\operatorname{Hom}(B,L\Lambda^\bullet(L)[1])^+\end{aligned}
\]
is a homomorphism of groups on the Grothendieck group \(K(B)\) of Corollary 1.4, where \(\operatorname{Hom}(B,L\Lambda^\bullet(L)[1])^+\) is the multiplicative group of series with constant term \(1\).

**Proof.** Proposition 1.8 and Corollary 1.4. \(\square\)

## 2. Chern classes in Hodge cohomology

**Lemma 2.1.** Let \(V\) be a simplicial module and \(n\geq1\). Then \(\pi_0(\Lambda^nV)=\Lambda^n(\pi_0V)\) and \(\pi_0(S^nV)=S^n(\pi_0V)\). Consequently, for a \(B\)-module \(Q\) placed in degree \(0\), \(H^0(L\Lambda^nQ)=\Lambda^nQ\) and the truncation \(L\Lambda^nQ\to H^0(L\Lambda^nQ)\) is a morphism \(L\Lambda^nQ\to\Lambda^nQ\), compatible with the products.

**Proof.** \(\pi_0\) of a simplicial module \(W\) is the cokernel of \(d_0-d_1\colon W_1\to W_0\). Let \(N=(d_0-d_1)(V_1)\subseteq V_0\), so \(\pi_0V=V_0/N\). By Lemma 1.3 of the lesson on filtered and graded powers, \(\Lambda^nV_0\to\Lambda^n(V_0/N)\) is surjective with kernel \(N\wedge\Lambda^{n-1}V_0\). For \(w=v_1\wedge\cdots\wedge v_n\) with \(v_i\in V_1\),
\[
\begin{aligned}&d_0w-d_1w\\
&\quad=\sum_kd_1v_1\wedge\cdots\wedge d_1v_{k-1}\\
&\qquad\wedge(d_0-d_1)v_k\\
&\qquad\wedge d_0v_{k+1}\wedge\cdots\wedge d_0v_n,\end{aligned}
\]
which lies in \(N\wedge\Lambda^{n-1}V_0\). Conversely, for \(v\in V_1\) and \(m_2,\dots,m_n\in V_0\), the element \(w=v\wedge s_0m_2\wedge\cdots\wedge s_0m_n\) satisfies \(d_0w-d_1w=\) \((d_0-d_1)v\wedge m_2\wedge\cdots\wedge m_n\), since \(d_0s_0=d_1s_0=1\). So the image of \(d_0-d_1\) on \(\Lambda^nV_1\) is \(N\wedge\Lambda^{n-1}V_0\), which gives the first statement; the argument for \(S^n\) is the same. For \(Q\), \(L\Lambda^nQ\) is represented by \(N\Lambda^n(V)\) for a simplicial resolution \(V\to Q\) by flat modules (Theorem 2.6 of the lesson on filtered and graded powers), whose \(H^0\) is \(\pi_0\Lambda^n(V)=\Lambda^nQ\); the complex lies in degrees \(\leq0\), so the truncation is a morphism to \(H^0\). The products of \(\Lambda(V)\) induce on \(\pi_0\) the products of \(\Lambda(Q)\). \(\square\)

**Definition 2.2.** The augmentation \(\alpha\colon L\to\Omega\) and Lemma 2.1 give morphisms \(L\Lambda^n(L)\to L\Lambda^n(\Omega)\to\Lambda^n\Omega\), compatible with the products, hence a ring homomorphism
\[
\begin{aligned}&h\colon\operatorname{Hom}(B,L\Lambda^\bullet(L)[1])\\
&\quad\to\prod_{n\geq0}H^n(T,\Lambda^n\Omega),\end{aligned}\tag{2.1}
\]
the product on the right being that of \(\operatorname{Hom}(B,\Lambda^\bullet(\Omega)[1])\), cup product followed by the exterior product. For \(E\in D(B)\) of bounded perfect amplitude put \(c'_t(E)=h(c_t(E))=\sum_nc'^n(E)t^n\), with \(c'^n(E)\in H^n(T,\Lambda^n\Omega)\), the *Chern classes of \(E\) in Hodge cohomology*.

**Proposition 2.3.**

1. \(c'_t(E)\) is the image under the analogue of \(h\) for \(L\Lambda^\bullet(\Omega)\) of \(\sigma^S\bigl(c_t(\operatorname{at}^\Omega(E))\bigr)\), the characteristic series of the principal parts class of Definition 4.1 of the lesson on the Atiyah class of filtered complexes.
2. (*Whitney formula*) For a distinguished triangle \(E'\to E\to E''\to E'[1]\) of objects of bounded perfect amplitude, \(c'_t(E)=c'_t(E')c'_t(E'')\); for \(E\in DF(B)\) of bounded perfect amplitude, \(c'_t(E)=\prod_pc'_t(\operatorname{gr}^pE)\).
3. (*Functoriality*) In the situation of Proposition 1.5 (3), \(g^*c'_t(E,X/Y)=c'_t(Lg^*E,X'/Y')\).
4. If \(E\) is as in Proposition 1.6, then \(c'^n(E)=0\) for \(n>r\).

**Proof.** (1) By Proposition 4.2 (2) of the lesson on the Atiyah class of filtered complexes, \(\operatorname{at}^\Omega(E)=(1\otimes\alpha[1])\circ\operatorname{at}(E)\), so by Proposition 3.2 (1) of the lesson on L-series, \(c_t(\operatorname{at}^\Omega(E))=\alpha_*c_t(\operatorname{at}(E))\), and \(\sigma^S\) is natural in the coefficient object. (2), (4) Theorem 1.3, Proposition 1.6, and the fact that \(h\) is a ring homomorphism. (3) Proposition 1.5 (3), the maps of Definition 2.2 being compatible with the functoriality maps of \(L\) and of \(\Omega\). \(\square\)

**Proposition 2.4 (invertible modules).** Let \(E\) be a \(B\)-module such that every object of \(T\) has a covering on whose members \(E\) is isomorphic to \(B\), and let \(E^\vee=\mathcal Hom_B(E,B)\). Then \(c'_t(E)=1+c'^1(E)t\), and \(c'^1(E)\in H^1(T,\Omega)=\operatorname{Ext}^1_B(B,\Omega)\) is the negative of the class of the extension
\[
0\to\Omega\to E^\vee\otimes_BP^1_{B/A}(E)\to B\to0
\]
obtained from the extension of principal parts \(0\to\Omega\otimes_BE\to P^1_{B/A}(E)\to E\to0\) by tensoring with \(E^\vee\) and identifying \(E^\vee\otimes E\) with \(B\) by evaluation. The local \(B\)-linear splittings of this extension correspond to the local connections on \(E\) (Proposition 3.2 of the lesson on the Atiyah class). If \(e\) is a local basis of \(E\) and \(\nabla_e\) the connection with \(\nabla_e(be)=\mathrm db\otimes e\), then \(\nabla_{ge}=\nabla_e-g^{-1}\mathrm dg\) for a local unit \(g\) of \(B\), as maps \(E\to\Omega\otimes E\) with \(g^{-1}\mathrm dg\) acting by multiplication.

**Proof.** \(E\) is as in Proposition 1.6 with \(r=1\), so \(\Lambda^nE=0\) for \(n\geq2\). Since \(\Omega[1]\in D^{\leq0}(B)\), Corollary 3.7 of the lesson on L-series applies to \(\operatorname{at}^\Omega(E)\colon E\to E\otimes\Omega[1]\) and gives \(c_t(\operatorname{at}^\Omega(E))=1-\operatorname{Tr}(\psi^1\circ\operatorname{at}^\Omega(E))t\), with \(\psi^1\) the identity. By Proposition 2.3 (1), \(c'_t(E)=1+c'^1(E)t\) with \(c'^1(E)=-\operatorname{Tr}(\operatorname{at}^\Omega(E))\), because \(\sigma^S\) is the identity in degree \(1\) (Exercise 4.4 of the lesson on Koszul complexes) and the truncation \(L\Lambda^1\Omega=\Omega\to\Lambda^1\Omega\) is the identity. The module \(E\) is flat and in degree \(0\), so \(\kappa_E\) is the symmetry \(\Omega\otimes E\to E\otimes\Omega\), without sign, and \(\operatorname{at}^\Omega(E)\) is the class of the extension of principal parts of \(E\) (Definition 4.1 of the lesson on the Atiyah class of filtered complexes, with \(F=E\)). With the dual \(E^\vee\), the coevaluation \(\eta\) and the evaluation \(\varepsilon\colon E^\vee\otimes E\to B\), an isomorphism, the trace of Definition 1.1 of the lesson on traces is \(\operatorname{Tr}(g)=(\varepsilon\otimes1)(1\otimes g)(\sigma\otimes1)(\eta\otimes1)\); here \(\varepsilon\sigma\eta=\operatorname{Tr}(1_E)=1\), checked locally where \(E\cong B\), so \(\sigma\eta=\varepsilon^{-1}\) and \(\operatorname{Tr}(g)=(\varepsilon\otimes1)(1\otimes g)\varepsilon^{-1}\). Applied to \(g=\operatorname{at}^\Omega(E)\) this is the class of the twisted extension. For the last assertion, \(\nabla_{ge}-\nabla_e\) is \(B\)-linear, \(\nabla_e(e)=0\), and \(\nabla_{ge}(e)=\nabla_{ge}(g^{-1}\cdot ge)=\) \(\mathrm d(g^{-1})\otimes ge=-g^{-1}\mathrm dg\otimes e\). \(\square\)

**Corollary 2.5 (invertible modules on a smooth scheme).** Let \(Y\to S\) be a smooth morphism of schemes, \(T\) the Zariski topos of \(Y\), \(A=f^{-1}\mathcal O_S\to B=\mathcal O_Y\), and \(L\) an invertible \(\mathcal O_Y\)-module. Then \(c'^1(L)=-c_1^{\mathrm{Hodge}}(L)\) in \(H^1(Y,\Omega_{Y/S})\), where \(c_1^{\mathrm{Hodge}}(L)\) is the image of the class of \(L\) in \(H^1(Y,\mathcal O_Y^*)\) [Tag 09NU] under \(\mathrm d\log\colon g\mapsto g^{-1}\mathrm dg\) [Tag 0FLE].

**Proof.** Choose an open covering by the \(U_i\), with bases \(s_i\) of \(L\) over \(U_i\), and put \(f_{i_0i_1}=s_{i_1}s_{i_0}^{-1}\); then \(c_1^{\mathrm{Hodge}}(L)\) is the image of the Čech class of \((\mathrm d\log f_{i_0i_1})\) [Tag 0FLE]. By Proposition 2.4, \(-c'^1(L)\) is the class of the twisted extension \(0\to\Omega\to L^\vee\otimes P^1_{B/A}(L)\to\mathcal O_Y\to0\), that is, the boundary of \(1\in H^0(Y,\mathcal O_Y)\) in \(H^1(Y,\Omega)\). Write \(\nabla_i=\nabla_{s_i}\) and \(\sigma_i=\mathrm d^1-\iota\nabla_i\) for the corresponding section of the extension of principal parts (Proposition 3.2 of the lesson on the Atiyah class). For a local basis \(s\) of \(L\) over \(U_i\), the element \(s^\vee\otimes\sigma_i(s)\), with \(s^\vee\) the dual basis, does not depend on \(s\), as \(\sigma_i\) is \(\mathcal O_Y\)-linear; it lifts \(1\) over \(U_i\). By Proposition 2.4, \(\nabla_{i_1}=\nabla_{i_0}-\mathrm d\log f_{i_0i_1}\) over \(U_{i_0i_1}\). So the difference of the lifts over \(U_{i_0i_1}\) is
\[
\begin{aligned}&s^\vee\otimes(\sigma_{i_1}-\sigma_{i_0})(s)\\&\quad=s^\vee\otimes\iota(\mathrm d\log f_{i_0i_1}\otimes s),\end{aligned}
\]
which is \(\mathrm d\log f_{i_0i_1}\) under \(L^\vee\otimes\Omega\otimes L\cong\Omega\). By Lemma 3.7 of the lesson on deformations of modules, the boundary of \(1\) is the image of the Čech class of \((\mathrm d\log f_{i_0i_1})\), which is \(c_1^{\mathrm{Hodge}}(L)\). \(\square\)

## 3. Exercises

**Exercise 3.1.** Show that \(c_t(B^r)=1\) and \(c_t(E\oplus B^r)=c_t(E)\).

**Exercise 3.2.** Let \(T\) be the punctual topos. Show that \(c_t(E)=1\) for every \(E\) of bounded perfect amplitude, although \(\operatorname{at}(E)\) need not be \(0\) (Exercise 5.1 of the lesson on the Atiyah class of filtered complexes).

**Exercise 3.3.** Let \(T\) be the Zariski topos of the projective line over a field \(k\), \(A=k\), \(B=\mathcal O\), and \(E=\mathcal O(1)\), with bases \(e_0\) on \(U_0=\operatorname{Spec}k[x]\) and \(e_1=xe_0\) on \(U_1=\operatorname{Spec}k[y]\), \(y=1/x\). Show that \(E\) has no global connection, and deduce that \(c'^1(E)\ne0\).

**Exercise 3.4.** Let \(E\) be of bounded perfect amplitude. Show that \(c_t(E[1])=L_t(E)\) and \(c_t(E\oplus E[1])=1\).

## 4. Complete solutions

**Solution 3.1.** \(\operatorname{at}(B^r)=0\) (Proposition 1.2 (4) of the lesson on the Atiyah class of filtered complexes, with \(N=A^r\)), so every \(\varphi^n\circ LS^n(\operatorname{at}(B^r))\) is \(0\) for \(n\geq1\) and \(L_t(B^r)=1\). By Theorem 1.3 (2), \(c_t(E\oplus B^r)=c_t(E)c_t(B^r)=c_t(E)\).

**Solution 3.2.** On the punctual topos \(H^n(T,X)=H^n(X)\), the cohomology of the complex in degree \(n\). Since \(L\) is concentrated in degrees \(\leq0\), so is \(L\Lambda^nL\) (Theorem 2.6 of the lesson on filtered and graded powers), and \(H^n(T,L\Lambda^nL)=0\) for \(n\geq1\). So every \(c^n(E)\) with \(n\geq1\) vanishes and \(c_t(E)=1\). In Exercise 5.1 there, \(\operatorname{at}(k)\ne0\) for \(B=k[x]\).

**Solution 3.3.** A connection is determined by \(\nabla(e_0)=a\,\mathrm dx\otimes e_0\) on \(U_0\) and \(\nabla(e_1)=b\,\mathrm dy\otimes e_1\) on \(U_1\), with \(a\in k[x]\), \(b\in k[y]\). On \(U_0\cap U_1\), \(\nabla(e_1)=\nabla(xe_0)=\) \(\mathrm dx\otimes e_0+x\,a\,\mathrm dx\otimes e_0=\) \((x^{-1}+a)\,\mathrm dx\otimes e_1\), and \(\mathrm dy=-x^{-2}\mathrm dx\), so \(x^{-1}+a(x)=-x^{-2}b(x^{-1})\), that is \(x+x^2a(x)=-b(x^{-1})\) in \(k[x,x^{-1}]\). The left side is a polynomial in \(x\) without constant term and the right side a polynomial in \(x^{-1}\), so both are constant, hence \(0\); but \(x+x^2a(x)\ne0\). So \(E\) has no global connection, the extension of principal parts does not split (Proposition 3.2 of the lesson on the Atiyah class), and neither does its twist by \(E^\vee\), whose splittings are the same. Its class in \(H^1(T,\Omega)\) is therefore nonzero, and \(c'^1(E)\ne0\) by Proposition 2.4.

**Solution 3.4.** Proposition 1.2 (2) gives \(L_t(E[1])=c_t(E)\), so \(c_t(E[1])=L_t(E[1])^{-1}=L_t(E)\). By Theorem 1.3 (2), \(c_t(E\oplus E[1])=c_t(E)L_t(E)=1\).

## Sources

The Chern classes of perfect complexes with values in the cotangent complex, their multiplicativity on filtrations and triangles, their base change and the Hodge-cohomology classes are due to Illusie, in his work on the cotangent complex, where the homomorphism of Corollary 1.9 is stated with the rank of perfect complexes over a local ring, after SGA 6, and where the question whether it is a homomorphism of pre-λ-rings is left open. Chern classes in Hodge cohomology through the Atiyah class go back to Atiyah, for holomorphic vector bundles.
