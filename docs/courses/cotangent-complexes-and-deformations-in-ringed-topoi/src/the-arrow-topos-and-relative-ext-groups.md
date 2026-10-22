# The arrow topos and relative Ext groups

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

A morphism of ringed topoi \(f\colon X\to Y\) is itself a ringed topos. Its arrow topos \(XY\) has as objects the triples of a sheaf \(E\) on \(X\), a sheaf \(F\) on \(Y\) and a map \(f^{-1}F\to E\); modules over it are pairs of modules with such a map. Derived Hom on \(XY\) combines derived Hom on \(X\) and on \(Y\). The relative Ext groups \(\operatorname{Ext}^i(Y/X;M,F)\) of complexes \(M\), \(F\) on \(Y\) are the Ext groups on \(XY\) from \(M\), placed over \(Y\), into the pair formed by \(Lf^*F\) and \(F\). They fit into a long exact sequence with \(\operatorname{Ext}^i(M,F)\) and \(\operatorname{Ext}^i(Lf^*M,Lf^*F)\), and for an open subspace they are the cohomology groups with supports in the closed complement. A commutative square of ringed topoi gives a morphism of arrow topoi whose cotangent complex restricts to the cotangent complexes of the two sides. The lesson proves:

- the arrow topos, its restriction morphisms \(i_X\), \(i_Y\) and its projection \(\pi\) to \(Y\), with \(\pi^*M\) the pair \((f^*M\leftarrow M)\) and \(\pi_*\) the restriction to \(Y\); tensor products and internal Hom on \(XY\);
- \(R\Gamma(XY,(E\leftarrow F))\cong R\Gamma(Y,F)\); internal and global derived Hom out of objects over \(X\), out of quasi-cartesian objects, and out of objects over \(Y\);
- relative Ext groups and their long exact sequences;
- the category of triples \((E,F,Lf^*F\to E)\) of the derived categories is not triangulated, and the comparison of Hom groups with \(D(XY)\) is surjective but not injective in general;
- the cotangent complex of the morphism of arrow topoi defined by a commutative square.

**Prerequisites.** [*Fibred topoi and their total topoi*](fibred-topoi-and-their-total-topoi.md) (Examples 1.2 (a), Definition 2.1, Propositions 2.2 and 3.1, Theorem 4.2); [*Morphisms of fibred topoi and modules on total topoi*](morphisms-of-fibred-topoi-and-modules-on-total-topoi.md) (Definition 1.1, Propositions 2.1 and 4.2); [*Cohomology of total topoi*](cohomology-of-total-topoi.md) (Examples 3.10 (a)); [*Filtered internal Hom and the formulas of Cartan*](filtered-internal-hom-and-the-formulas-of-cartan.md) (Proposition 4.1); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Lemma 4.2). From the AI-integrated Stacks project: localization of a topos at an object [[Stacks, Tag 04GZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-localize-topos)]; extension by zero [[Tag 03DJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-extension-by-zero-exact)]; internal Hom and derived internal Hom restrict to localizations [[Tag 0E8H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-internal-hom-restriction), [Tag 08JB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-restriction-RHom-to-U)]; right adjoints of exact functors preserve injectives [[Tag 015Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/homology.html#homology-lemma-adjoint-preserve-injectives)]; resolutions by a cofinal class of injectives [[Tag 05T6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-subcategory-right-resolution)]; bounded below complexes of injectives are K-injective [[Tag 070J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-bounded-below-injectives-K-injective)]; K-flat resolutions [[Tag 06YS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-K-flat-resolution)]; derived pullback [[Tag 06YY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-derived-base-change), [Tag 0D6D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-derived-pullback-composition)], the canonical map of a derived functor [[Tag 05SX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-definition-computes)] and the adjunction of derived pullback with \(Rf_*\) [[Tag 07A6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-adjoint)]; global derived Hom [[Tag 0B6E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-section-global-RHom)]; the triangle of a short exact sequence [[Tag 0152](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-derived-canonical-delta-functor)] and the long exact Hom sequences [[Tag 0149](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-representable-homological)]; the cotangent complex of a morphism of ringed topoi [[Tag 08SU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-definition-cotangent-complex-morphism-ringed-topoi)] and its transitivity triangle [[Tag 08V1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-lemma-triangle-ringed-topoi)].

## Conventions

Complexes are indexed cohomologically. For a ringed topos \((X,\mathcal O_X)\), \(D(X)\) is the derived category of \(\mathcal O_X\)-modules, \(D^+(X)\) and \(D^-(X)\) its full subcategories of complexes with cohomology bounded below, respectively above; \(\mathcal Hom\) and \(R\mathcal Hom\) are the internal Hom and its derived functor, \(\mathcal Ext^i=H^iR\mathcal Hom\), \(R\operatorname{Hom}=R\Gamma\circ R\mathcal Hom\) [Tag 0B6E] and \(\operatorname{Ext}^i=H^iR\operatorname{Hom}\), so that \(\operatorname{Ext}^i(K,L)=\operatorname{Hom}_{D(X)}(K,L[i])\). For a morphism of ringed topoi \(f\colon X\to Y\), \(f^{-1}\) is the inverse image of sheaves, \(f^*=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}\) the inverse image of modules, \(Lf^*\) and \(Rf_*\) the derived functors. Every complex \(L\) with \(H^n(L)=0\) for \(n>b\) receives a quasi-isomorphism from a complex of flat modules vanishing in degrees \(>b\) (Lemma 4.2 (1) of the lesson on non-additive functors), and \(Lf^*\) is computed by such complexes [Tag 06YY]. A bounded below complex of injective modules is K-injective [Tag 070J], so it computes \(R\mathcal Hom\) into it from any complex.

## 1. The arrow topos

Throughout, \(f\colon X\to Y\) is a morphism of topoi, and from 1.3 on a morphism of ringed topoi.

**Definition 1.1.** The *arrow topos* \(XY=\operatorname{Top}(f)\) is the total topos of the fibred topos over \(\{0\to1\}\) defined by \(f\) (Examples 1.2 (a) and Definition 2.1 of the lesson on fibred topoi). An object is a triple of \(E\in X\), \(F\in Y\) and a map \(\varphi\colon f^{-1}F\to E\), written \((E\xleftarrow{\varphi}F)\) or \((E\leftarrow F)\). A morphism \((E\leftarrow F)\to(E'\leftarrow F')\) is a pair \(a\colon E\to E'\), \(b\colon F\to F'\) with \(a\circ\varphi=\varphi'\circ f^{-1}(b)\). By Theorem 4.2 of the lesson on fibred topoi, \(XY\) is a topos.

**Proposition 1.2.**

1. The restrictions \(i_X^{-1}(E\leftarrow F)=E\) and \(i_Y^{-1}(E\leftarrow F)=F\) are the inverse images of morphisms of topoi \(i_X\colon X\to XY\) and \(i_Y\colon Y\to XY\), with
\[
\begin{gathered}i_{X*}L=(L\leftarrow f_*L),\\ i_{X!}L=(L\leftarrow\varnothing),\\ i_{Y*}M=(e_X\leftarrow M),\\ i_{Y!}M=(f^{-1}M\leftarrow M),\end{gathered}
\]
where \(f^{-1}f_*L\to L\) is the counit, \(e_X\) is the final object of \(X\), and the map of \(i_{Y!}M\) is the identity.
2. \(i_X\) is the localization of \(XY\) at the object \((e_X\leftarrow\varnothing)\).
3. \(i_{Y!}\) is the inverse image of a morphism of topoi \(\pi\colon XY\to Y\), with \(\pi_*=i_Y^{-1}\). There are canonical isomorphisms \(\pi\circ i_Y\cong\mathrm{id}_Y\) and \(\pi\circ i_X\cong f\).
4. The objects \((U\leftarrow\varnothing)\), \(U\in X\), and \((f^{-1}V\leftarrow V)\), \(V\in Y\), generate \(XY\).

**Proof.** (1) Proposition 3.1 of the lesson on fibred topoi, for \(I=\{0\to1\}\): there are no arrows \(1\to0\), so the coproduct defining \(i_{X!}L\) at level \(1\) is empty and the product defining \(i_{Y*}M\) at level \(0\) is empty, while the only arrow \(0\to1\) gives \(f^{-1}M\) and \(f_*L\). As \(i_X^{-1}\) and \(i_Y^{-1}\) have left adjoints, they preserve limits; with their right adjoints they are inverse images of morphisms of topoi.

(2) If \((E\leftarrow F)\) maps to \((e_X\leftarrow\varnothing)\), then \(F\) maps to the initial object \(\varnothing\) of \(Y\), so \(F\) is initial: over every object \(V\), \(\varnothing(V)\) is empty or, when \(V\) is covered by the empty family, a point, and in the second case \(F(V)\) is a point as well, \(F\) being a sheaf. So the objects over \((e_X\leftarrow\varnothing)\) are the \((E\leftarrow\varnothing)\), and \(XY/(e_X\leftarrow\varnothing)\) is identified with \(X\) [Tag 04GZ]. The inverse image of the localization morphism is \(W\mapsto W\times(e_X\leftarrow\varnothing)=(i_X^{-1}W\leftarrow\varnothing)\), products being computed levelwise (Proposition 2.2 of the lesson on fibred topoi), and under the identification this is \(i_X^{-1}\).

(3) Limits in \(XY\) are computed levelwise, and \(f^{-1}\) preserves finite limits, so \(i_{Y!}\) preserves finite limits; it preserves colimits as a left adjoint. So \((i_{Y!},i_Y^{-1})\) is a morphism of topoi. Then \(i_Y^{-1}\pi^{-1}M=M\) and \(i_X^{-1}\pi^{-1}M=f^{-1}M\).

(4) By adjunction, \(\operatorname{Hom}((U\leftarrow\varnothing),W)=\operatorname{Hom}(U,i_X^{-1}W)\) and \(\operatorname{Hom}((f^{-1}V\leftarrow V),W)=\) \(\operatorname{Hom}(V,i_Y^{-1}W)\), naturally in \(W\). So two morphisms \(W\to W'\) that agree after composition with every morphism from these objects have the same components over \(X\) and over \(Y\), and a morphism \((a,b)\) of \(XY\) is determined by \(a\) and \(b\). \(\square\)

**1.3. Rings and modules.** Let \(f\colon(X,\mathcal O_X)\to(Y,\mathcal O_Y)\) be a morphism of ringed topoi. Then \(\mathcal O=(\mathcal O_X\leftarrow\mathcal O_Y)\), with the structure map \(f^{-1}\mathcal O_Y\to\mathcal O_X\), is a ring of \(XY\). By Proposition 4.2 (a) of the lesson on morphisms of fibred topoi, an \(\mathcal O\)-module is a pair \((E\leftarrow F)\) of an \(\mathcal O_X\)-module \(E\) and an \(\mathcal O_Y\)-module \(F\) with an \(\mathcal O_X\)-linear map \(\varphi\colon f^*F\to E\). Since \(i_X^{-1}\mathcal O=\mathcal O_X\) and \(i_Y^{-1}\mathcal O=\mathcal O_Y\), \(i_X\) and \(i_Y\) are morphisms of ringed topoi with exact inverse images \(i_X^*=i_X^{-1}\) and \(i_Y^*=i_Y^{-1}\) on modules. The map \(\pi^{-1}\mathcal O_Y=(f^{-1}\mathcal O_Y\leftarrow\mathcal O_Y)\to\mathcal O\) makes \(\pi\) a morphism of ringed topoi, and tensor products of \(\mathcal O\)-modules are computed levelwise,
\[
\begin{aligned}&(E\leftarrow F)\otimes_{\mathcal O}(E'\leftarrow F')\\&\quad=(E\otimes E'\leftarrow F\otimes F'),\end{aligned}
\]
since inverse images commute with tensor products. Hence \(\pi^*M=(f^*M\xleftarrow{\mathrm{id}}M)\), and \(\pi_*=i_Y^*\) on modules, an exact functor. On modules, \(i_{X!}L=(L\leftarrow0)\) is the extension by zero [Tag 03DJ], \(i_{X*}L=(L\leftarrow f_*L)\) and \(i_{Y*}M=(0\leftarrow M)\).

**Lemma 1.4.** Let \(L\) be an \(\mathcal O_X\)-module, \(M\) an \(\mathcal O_Y\)-module and \((E\xleftarrow{\varphi}F)\) an \(\mathcal O\)-module.

1. \(\mathcal Hom((L\leftarrow0),(E\leftarrow F))=\) \(i_{X*}\mathcal Hom(L,E)\), that is \((\mathcal Hom(L,E)\leftarrow f_*\mathcal Hom(L,E))\).
2. \(\mathcal Hom(\pi^*M,(E\leftarrow F))=\) \((\mathcal Hom(f^*M,E)\leftarrow\) \(\mathcal Hom(M,F))\), with the map \(f^*\mathcal Hom(M,F)\to\) \(\mathcal Hom(f^*M,f^*F)\to\) \(\mathcal Hom(f^*M,E)\) given by \(\varphi\).

**Proof.** For \(\mathcal O\)-modules \(A\), \(B\), \(i_X^*\mathcal Hom(A,B)=\mathcal Hom(i_X^*A,i_X^*B)\), by Proposition 1.2 (2) and [Tag 0E8H]; this gives the levels over \(X\). For \(V\in Y\), the objects of \(XY\) over \(\pi^{-1}V=(f^{-1}V\leftarrow V)\) are the triples over \(X/f^{-1}V\) and \(Y/V\), so the localization \(XY/\pi^{-1}V\) is the arrow topos of the restriction \(f_V\colon X/f^{-1}V\to Y/V\). The sections of \(i_Y^*\mathcal Hom(A,B)=\pi_*\mathcal Hom(A,B)\) over \(V\) are the morphisms \(A\to B\) over this localization. For \(A=(L\leftarrow0)\) these are the morphisms \(L|_{f^{-1}V}\to E|_{f^{-1}V}\), by the adjunction of \(i_{X!}\) and \(i_X^*\) for \(f_V\), that is the sections of \(f_*\mathcal Hom(L,E)\) over \(V\). For \(A=\pi^*M\) they are the morphisms \(M|_V\to F|_V\), by the adjunction of \(\pi^*\) and \(\pi_*\) for \(f_V\), that is the sections of \(\mathcal Hom(M,F)\) over \(V\). The map from the level over \(Y\) to the level over \(X\) sends such a morphism to its component over \(X\): in (1) this is the counit \(f^{-1}f_*\mathcal Hom(L,E)\to\mathcal Hom(L,E)\); in (2) a morphism is determined by its component \(\beta\colon M|_V\to F|_V\), its component over \(X\) being \(\varphi\circ f^*\beta\), as stated. \(\square\)

## 2. Derived Hom on the arrow topos

Call an \(\mathcal O\)-module *special injective* if it is \(i_{X*}I\oplus i_{Y*}J=(I\leftarrow f_*I\oplus J)\) with \(I\) an injective \(\mathcal O_X\)-module and \(J\) an injective \(\mathcal O_Y\)-module.

**Lemma 2.1.** Special injective modules are injective, every \(\mathcal O\)-module is a submodule of one, and every complex in \(D^+(XY)\) is quasi-isomorphic to a bounded below complex of special injective modules. The restriction of a special injective module to \(X\) is injective.

**Proof.** \(i_{X*}\) and \(i_{Y*}\) are right adjoint to the exact functors \(i_X^*\), \(i_Y^*\), so they preserve injectives [Tag 015Z]. The units give a map \((L\leftarrow M)\to i_{X*}L\oplus i_{Y*}M\), which over \(X\) is \(L\to L\oplus0\) and over \(Y\) is \(M\to f_*L\oplus M\), the second component the identity; it is injective on both levels, hence injective. Embed \(L\subseteq I\) and \(M\subseteq J\) in injectives; \(i_{X*}\) and \(i_{Y*}\) preserve monomorphisms. The resolutions exist by [Tag 05T6]. Finally \(i_X^*(i_{X*}I\oplus i_{Y*}J)=I\). \(\square\)

**Proposition 2.2.** For \(C=(E\leftarrow F)\in D^+(XY)\), restriction to \(Y\) is an isomorphism \(R\Gamma(XY,C)\to R\Gamma(Y,F)\).

**Proof.** For every \(\mathcal O\)-module, \(\Gamma(XY,(E\leftarrow F))=\Gamma(Y,F)\), a global section being determined by its component over \(Y\) (Examples 3.10 (a) of the lesson on cohomology of total topoi). Represent \(C\) by a bounded below complex \(K\) of special injective modules (Lemma 2.1). Then \(R\Gamma(XY,C)=\Gamma(XY,K)=\Gamma(Y,i_Y^*K)\). The terms of \(i_Y^*K\) are \(f_*I\oplus J\); here \(Rf_*I=f_*I\), so \(H^q(Y,f_*I)=H^q(X,I)=0\) for \(q>0\), and \(J\) is injective. So \(i_Y^*K\) is a bounded below complex of \(\Gamma(Y,-)\)-acyclic modules representing \(F\), and \(\Gamma(Y,i_Y^*K)\) represents \(R\Gamma(Y,F)\). \(\square\)

**Proposition 2.3.** Let \(L\in D^-(X)\) and \(C=(E\leftarrow F)\in D^+(XY)\). There are canonical isomorphisms
\[
\begin{aligned}&i_X^*R\mathcal Hom((L\leftarrow0),C)\cong R\mathcal Hom(L,E),\\&i_Y^*R\mathcal Hom((L\leftarrow0),C)\\&\quad\cong Rf_*R\mathcal Hom(L,E),\\&R\operatorname{Hom}((L\leftarrow0),C)\cong R\operatorname{Hom}(L,E).\end{aligned}
\]

**Proof.** Represent \(L\) by a bounded above complex \(P\) of flat \(\mathcal O_X\)-modules and \(C\) by a bounded below complex \(K\) of special injective modules. Since \(i_{X!}\) is exact, \((P\leftarrow0)\) represents \((L\leftarrow0)\), and, by Lemma 1.4 (1),
\[
\begin{aligned}&R\mathcal Hom((L\leftarrow0),C)\\&\quad=\mathcal Hom^\bullet((P\leftarrow0),K)\\&\quad=i_{X*}\mathcal Hom^\bullet(P,i_X^*K).\end{aligned}
\]
 Here \(i_X^*K\) is a bounded below complex of injectives representing \(E\), so \(\mathcal Hom^\bullet(P,i_X^*K)\) represents \(R\mathcal Hom(L,E)\). Its terms are finite products of the modules \(\mathcal Hom(P^p,i_X^*K^q)\), which are injective, \(P^p\) being flat; and it is bounded below. So \(f_*\) of it represents \(Rf_*R\mathcal Hom(L,E)\). This gives the first two isomorphisms. The third follows by applying \(R\Gamma(XY,-)\), which is \(R\Gamma(Y,i_Y^*-)\) by Proposition 2.2, and \(R\Gamma(Y,Rf_*-)=R\Gamma(X,-)\). \(\square\)

**Proposition 2.4.** For \(L\in D(Y)\) and \(M\in D(X)\) there are canonical isomorphisms
\[
\begin{aligned}&R\mathcal Hom(L,Rf_*M)\\&\quad\cong Rf_*R\mathcal Hom(Lf^*L,M),\\&R\operatorname{Hom}(L,Rf_*M)\\&\quad\cong R\operatorname{Hom}(Lf^*L,M).\end{aligned}
\]
If \(L\) is a flat \(\mathcal O_Y\)-module and \(I\) an injective \(\mathcal O_X\)-module, then \(\mathcal Ext^i(L,f_*I)=0\) and \(\operatorname{Ext}^i(L,f_*I)=0\) for \(i>0\).

**Proof.** The isomorphisms are Proposition 4.1 (3) of the lesson on filtered internal Hom, applied to objects with the trivial filtration and read on \(\operatorname{gr}^0\). For the vanishing, \(Rf_*I=f_*I\) and \(Lf^*L=f^*L\) [Tag 06YY]. The module \(\mathcal Hom(f^*L,I)\) is injective, as \(f^*L\) is flat and \(I\) injective, so \(R\mathcal Hom(f^*L,I)=\mathcal Hom(f^*L,I)\), and both \(Rf_*\mathcal Hom(f^*L,I)\) and \(R\Gamma(X,\mathcal Hom(f^*L,I))\) are concentrated in degree \(0\). By the two isomorphisms, so are \(R\mathcal Hom(L,f_*I)\) and \(R\operatorname{Hom}(L,f_*I)\). \(\square\)

**Lemma 2.5.** Let \(P\) be a bounded above complex and \(N\) a bounded below complex of \(\mathcal O_Y\)-modules with \(\mathcal Ext^k(P^p,N^q)=0\) for all \(p\), \(q\) and all \(k\geq1\). Then \(\mathcal Hom^\bullet(P,N)\) represents \(R\mathcal Hom(P,N)\).

**Proof.** Let \(N\to I\) be a quasi-isomorphism to a bounded below complex of injectives, and \(Z\) its cone, a bounded below acyclic complex whose terms satisfy the same vanishing. Write \(B^q\subseteq Z^q\) for the cycles, so that \(0\to B^q\to Z^q\to B^{q+1}\to0\) is exact and \(B^q=0\) for \(q\) small. By induction on \(q\), \(\mathcal Ext^k(P^p,B^q)=0\) for \(k\geq1\): the long exact sequence gives \(\mathcal Ext^k(P^p,B^{q+1})\cong\mathcal Ext^{k+1}(P^p,B^q)=0\). So \(\mathcal Hom(P^p,-)\) is exact on these sequences and \(\mathcal Hom(P^p,Z)\) is acyclic for every \(p\). The complex \(\mathcal Hom^\bullet(P,Z)\) is the total complex of a double complex with acyclic rows and finitely many terms in each total degree, so it is acyclic. Hence \(\mathcal Hom^\bullet(P,N)\to\mathcal Hom^\bullet(P,I)\) is a quasi-isomorphism, and the second complex represents \(R\mathcal Hom(P,N)\). \(\square\)

**Definition 2.6.** For a complex \(C=(L\xleftarrow{\varphi}M)\) of \(\mathcal O\)-modules, the map \(u_C\colon Lf^*M\to L\) *defined by* \(C\) is the composite of the canonical map \(Lf^*M\to f^*M\) of the derived functor [Tag 05SX] with \(\varphi\colon f^*M\to L\). For a quasi-isomorphism \(s\colon P\to M\) from a K-flat complex with flat terms [Tag 06YS], or from a bounded above complex of flat modules when \(M\) has bounded above cohomology, \(Lf^*M=f^*P\) and \(u_C=\varphi\circ f^*(s)\) [Tag 06YY]. The map \(u_C\) is natural in \(C\), so it is defined for objects of \(D(XY)\). An object \(C=(L\leftarrow M)\) of \(D^-(XY)\) is *quasi-cartesian* if \(u_C\) is an isomorphism of \(D(X)\).

**Proposition 2.7.** Let \(C=(L\leftarrow M)\in D^-(XY)\) be quasi-cartesian and \(C'=(E\leftarrow F)\in D^+(XY)\). The restriction maps
\[
\begin{aligned}i_X^*R\mathcal Hom(C,C')&\to R\mathcal Hom(L,E),\\ i_Y^*R\mathcal Hom(C,C')&\to R\mathcal Hom(M,F)\end{aligned}
\]
are isomorphisms.

**Proof.** Represent \(C\) by a complex \((L\xleftarrow{\varphi}M)\), and let \(s\colon P\to M\) be a quasi-isomorphism from a bounded above complex of flat modules, so that \(u_C=\varphi\circ f^*(s)\). The pair \((\varphi\circ f^*(s),s)\) is a morphism of complexes \(\pi^*P=(f^*P\leftarrow P)\to C\); it is a quasi-isomorphism over \(Y\), and over \(X\) because \(C\) is quasi-cartesian. Quasi-isomorphisms of \(\mathcal O\)-modules are detected on the two levels, \(i_X^*\) and \(i_Y^*\) being exact and jointly faithful. So we may take \(C=\pi^*P\), and \(C'\) a bounded below complex \(K\) of special injective modules. By Lemma 1.4 (2),
\[
\begin{aligned}&\mathcal Hom^\bullet(\pi^*P,K)\\&\quad=\bigl(\mathcal Hom^\bullet(f^*P,i_X^*K)\\&\qquad\leftarrow\mathcal Hom^\bullet(P,i_Y^*K)\bigr),\end{aligned}
\]
and this complex represents \(R\mathcal Hom(C,C')\), \(K\) being K-injective. Over \(X\), \(i_X^*K\) is a bounded below complex of injectives, so \(\mathcal Hom^\bullet(f^*P,i_X^*K)\) represents \(R\mathcal Hom(L,E)\). Over \(Y\), the terms \(f_*I\oplus J\) of \(i_Y^*K\) satisfy \(\mathcal Ext^k(P^p,f_*I\oplus J)=0\) for \(k\geq1\) (Proposition 2.4), so \(\mathcal Hom^\bullet(P,i_Y^*K)\) represents \(R\mathcal Hom(M,F)\) by Lemma 2.5. Both identifications are the restriction maps. \(\square\)

**Proposition 2.8.** Let \(M\in D^-(Y)\) and \(C=(E\leftarrow F)\in D^+(XY)\), and let \(\epsilon\colon F\to Rf_*E\) be adjoint to the map \(Lf^*F\to E\) defined by \(C\) [Tag 07A6].

1. \(i_X^*R\mathcal Hom((0\leftarrow M),C)=0\).
2. There is a distinguished triangle
\[
\begin{aligned}&i_Y^*R\mathcal Hom((0\leftarrow M),C)\\&\quad\to R\mathcal Hom(M,F)\\&\quad\to R\mathcal Hom(M,Rf_*E)\to\end{aligned}
\]
whose first map is restriction to \(Y\) and whose second map is \(R\mathcal Hom(M,\epsilon)\); and \(R\mathcal Hom(M,Rf_*E)\cong\) \(Rf_*R\mathcal Hom(Lf^*M,E)\) by Proposition 2.4.
3. There is a distinguished triangle
\[
\begin{aligned}&R\operatorname{Hom}((0\leftarrow M),C)\\&\quad\to R\operatorname{Hom}(M,F)\\&\quad\to R\operatorname{Hom}(Lf^*M,E)\to\end{aligned}
\]
whose second map sends \(b\colon M\to F[i]\) to the composite of \(Lf^*b\) with the map \(Lf^*F\to E\) defined by \(C\).

**Proof.** Let \(P\to M\) be a quasi-isomorphism from a bounded above complex of flat modules. The sequence of complexes of \(\mathcal O\)-modules
\[
\begin{aligned}&0\to(f^*P\leftarrow0)\to\pi^*P\\&\quad\to(0\leftarrow P)\to0\end{aligned}
\]
is exact on both levels, hence exact, and gives a distinguished triangle [Tag 0152]; \(R\mathcal Hom(-,C)\) carries it to a distinguished triangle
\[
\begin{aligned}&R\mathcal Hom((0\leftarrow P),C)\to R\mathcal Hom(\pi^*P,C)\\&\quad\to R\mathcal Hom((f^*P\leftarrow0),C)\to.\end{aligned}
\]
Take \(C\) to be a bounded below complex \(K\) of special injective modules, so that the terms are \(\mathcal Hom^\bullet\) complexes. Over \(X\), by Propositions 2.7 and 2.3 the second map becomes the identity of \(R\mathcal Hom(f^*P,E)\), the inclusion being the identity over \(X\); so the first term vanishes over \(X\). Over \(Y\), Proposition 2.7 and Lemma 1.4 (1) give the triangle with second map \(\mathcal Hom^\bullet(P,i_Y^*K)\to\) \(f_*\mathcal Hom^\bullet(f^*P,i_X^*K)=\) \(\mathcal Hom^\bullet(P,f_*i_X^*K)\), which sends \(b\) to the adjoint of the composite of \(f^*b\) with the structure map of \(K\), that is to the composite of \(b\) with \(i_Y^*K\to f_*i_X^*K\). This map represents \(\epsilon\), since \(f_*i_X^*K=Rf_*E\). This proves (1) and (2). Applying \(R\Gamma(XY,-)=R\Gamma(Y,i_Y^*-)\) (Proposition 2.2) and the global form of Proposition 2.4 gives (3); under that isomorphism, composing with \(\epsilon\) becomes composing \(Lf^*\) with the adjoint of \(\epsilon\). \(\square\)

## 3. Relative Ext groups

**Definition 3.1.** For \(F\in D(Y)\) put \((Lf^*F\leftarrow F)=L\pi^*F\in D(XY)\). Since \(\pi\circ i_X\cong f\), \(\pi\circ i_Y\cong\mathrm{id}\) and \(i_X^*\), \(i_Y^*\) are exact, its restrictions are \(Lf^*F\) and \(F\) [Tag 0D6D]; for a K-flat resolution \(Q\to F\) with flat terms it is \(\pi^*Q=(f^*Q\leftarrow Q)\) [Tag 06YY]. Let \(M\in D^-(Y)\) and \(F\in D^+(Y)\) with \(Lf^*F\in D^+(X)\), for instance \(f\) flat, or \(F\) of finite tor amplitude. The *relative derived Hom* and *relative Ext groups* are
\[
\begin{aligned}&R\mathcal Hom(Y/X;M,F)\\&\quad=i_Y^*R\mathcal Hom((0\leftarrow M),L\pi^*F),\\&R\operatorname{Hom}(Y/X;M,F)\\&\quad=R\operatorname{Hom}((0\leftarrow M),L\pi^*F),\end{aligned}
\]
with cohomology \(\mathcal Ext^i(Y/X;M,F)\) and \(\operatorname{Ext}^i(Y/X;M,F)\). For abelian sheaves, that is \(\mathcal O_X=\mathbf Z\), \(\mathcal O_Y=\mathbf Z\), the condition holds for every \(F\in D^+(Y)\), \(f^{-1}\) being exact, and the *relative cohomology* is \(R\Gamma(Y/X;F)=R\operatorname{Hom}(Y/X;\mathbf Z,F)\), with \(H^i(Y/X;F)=H^iR\Gamma(Y/X;F)\).

**Proposition 3.2.** Let \(M\), \(F\) be as in Definition 3.1, and \(\eta\colon F\to Rf_*Lf^*F\) the unit. There are distinguished triangles
\[
\begin{aligned}&R\mathcal Hom(Y/X;M,F)\to R\mathcal Hom(M,F)\\&\quad\to R\mathcal Hom(M,Rf_*Lf^*F)\to,\\ &R\operatorname{Hom}(Y/X;M,F)\to R\operatorname{Hom}(M,F)\\&\quad\to R\operatorname{Hom}(Lf^*M,Lf^*F)\to,\end{aligned}
\]
the second maps being \(R\mathcal Hom(M,\eta)\) and the functor \(Lf^*\). In particular there are long exact sequences
\[
\begin{aligned}&\cdots\to\operatorname{Ext}^{i-1}(Lf^*M,Lf^*F)\\&\quad\to\operatorname{Ext}^i(Y/X;M,F)\to\operatorname{Ext}^i(M,F)\\&\quad\to\operatorname{Ext}^i(Lf^*M,Lf^*F)\to\cdots,\end{aligned}
\]
and the same with the sheaves \(\mathcal Ext\) and \(\mathcal Ext^i(M,Rf_*Lf^*F)\cong\) \(\mathcal H^iRf_*R\mathcal Hom(Lf^*M,Lf^*F)\) in the last place.

**Proof.** Proposition 2.8 for \(C=L\pi^*F\), whose map \(Lf^*F\to Lf^*F\) is the identity, so that \(\epsilon=\eta\). By the adjunction [Tag 07A6], a map \(b\colon M\to F[i]\) followed by \(\eta\) corresponds to \(Lf^*b\), since the composite \(Lf^*F\to Lf^*Rf_*Lf^*F\to Lf^*F\) of the unit and the counit is the identity. \(\square\)

**Proposition 3.3.** Let \(D'\) be the category whose objects are triples \((E,F,u)\) with \(E\in D(X)\), \(F\in D(Y)\) and \(u\colon Lf^*F\to E\) in \(D(X)\), and whose morphisms \((E,F,u)\to(E',F',u')\) are pairs \(a\colon E\to E'\), \(b\colon F\to F'\) with \(a\circ u=u'\circ Lf^*b\).

1. If \(Lf^*F\neq0\) for some \(F\in D(Y)\), then \((0,\mathrm{id}_F)\colon(Lf^*F,F,\mathrm{id})\to(0,F,0)\) is an epimorphism of \(D'\) without a section. So \(D'\) admits no structure of triangulated category.
2. The functor \(\Phi\colon D(XY)\to D'\), \(C\mapsto(i_X^*C,i_Y^*C,u_C)\) with \(u_C\) the map of Definition 2.6, is conservative.
3. Let \(M\in D^-(Y)\) and \(F\) be as in Definition 3.1. The map
\[
\begin{aligned}&\operatorname{Ext}^0(Y/X;M,F)\\&\quad=\operatorname{Hom}_{D(XY)}((0\leftarrow M),L\pi^*F)\\&\quad\to\operatorname{Hom}_{D'}(\Phi(0\leftarrow M),\Phi L\pi^*F)\end{aligned}
\]
induced by \(\Phi\) is surjective onto \(\operatorname{Ker}(\operatorname{Ext}^0(M,F)\to\) \(\operatorname{Ext}^0(Lf^*M,Lf^*F))\), and its kernel is the image of \(\operatorname{Ext}^{-1}(Lf^*M,Lf^*F)\).

**Proof.** (1) A morphism \((a,b)\) out of \((0,F,0)\) with \((a,b)\circ(0,\mathrm{id}_F)=0\) has \(b=0\), and \(a\) has source \(0\); so \((0,\mathrm{id}_F)\) is an epimorphism. A section would be a morphism \((a',\mathrm{id}_F)\colon(0,F,0)\to(Lf^*F,F,\mathrm{id})\), which requires \(a'\circ0=\mathrm{id}\circ Lf^*(\mathrm{id}_F)\), that is \(\mathrm{id}_{Lf^*F}=0\). In a triangulated category every epimorphism \(e\colon A\to B\) has a section: in a distinguished triangle \(A\xrightarrow{e}B\xrightarrow{g}D\to\), \(g\circ e=0\) forces \(g=0\), and the exact sequence \(\operatorname{Hom}(B,A)\to\operatorname{Hom}(B,B)\to\) \(\operatorname{Hom}(B,D)\) [Tag 0149] gives \(s\) with \(e\circ s=\mathrm{id}_B\).

(2) A morphism of \(D(XY)\) is an isomorphism if its two restrictions are, since cohomology sheaves are computed on the two levels.

(3) A morphism of \(D'\) from \((0,M,0)\) to \((Lf^*F,F,\mathrm{id})\) is a pair \((0,b)\) with \(\mathrm{id}\circ Lf^*b=0\); so these morphisms form the stated kernel. The map induced by \(\Phi\) sends a morphism to its restriction to \(Y\), the restriction to \(X\) being zero, its source vanishing there. By Proposition 3.2 the image of \(\operatorname{Ext}^0(Y/X;M,F)\to\operatorname{Ext}^0(M,F)\) is that kernel, and the kernel of this map is the image of \(\operatorname{Ext}^{-1}(Lf^*M,Lf^*F)\). \(\square\)

So the triples of Proposition 3.3 do not form a triangulated category, and \(\Phi\) loses information: Exercise 5.2 gives a case where \(\Phi\) is not faithful.

## 4. Squares of ringed topoi

**Proposition 4.1.** Let \(f\colon X\to Y\), \(g\colon Z\to T\), \(p\colon X\to Z\) and \(q\colon Y\to T\) be morphisms of ringed topoi with an isomorphism \(c\colon q\circ f\cong g\circ p\). There is a morphism of ringed topoi \((p,q)\colon XY\to ZT\) with
\[
(p,q)^{-1}(E\xleftarrow{\psi}F)=(p^{-1}E\leftarrow q^{-1}F),
\]
the map being \(p^{-1}(\psi)\) composed with the isomorphism \(f^{-1}q^{-1}F\cong p^{-1}g^{-1}F\) given by \(c\), and the same formula for \((p,q)^*\) on modules. It satisfies \((p,q)\circ i_X\cong i_Z\circ p\) and \((p,q)\circ i_Y\cong i_T\circ q\).

**Proof.** The levels \(p\), \(q\) with \(c\) form a morphism of fibred topoi over the identity of \(\{0\to1\}\) (Definition 1.1 of the lesson on morphisms of fibred topoi), which induces a morphism of the total topoi with the stated inverse image (Proposition 2.1 there). The maps \(p^{-1}\mathcal O_Z\to\mathcal O_X\) and \(q^{-1}\mathcal O_T\to\mathcal O_Y\) are compatible with the structure maps, so they define \((p,q)^{-1}\mathcal O_{ZT}\to\mathcal O_{XY}\). The two isomorphisms hold on inverse images, by restriction to the levels. \(\square\)

**Proposition 4.2.** In the situation of Proposition 4.1, the transitivity triangles give isomorphisms
\[
\begin{gathered}i_X^*L_{XY/ZT}\cong L_{X/Z},\\ i_Y^*L_{XY/ZT}\cong L_{Y/T}.\end{gathered}
\]
Similarly, for morphisms \(f\colon X\to Y\), \(p\colon X\to Z\), \(q\colon Y\to Z\) of ringed topoi with \(q\circ f\cong p\), the morphism \((p,q)\colon XY\to Z\) with \((p,q)^{-1}G=(p^{-1}G\leftarrow q^{-1}G)\) satisfies \(i_X^*L_{XY/Z}\cong L_{X/Z}\) and \(i_Y^*L_{XY/Z}\cong L_{Y/Z}\).

**Proof.** The cotangent complex of a morphism of ringed topoi \(h\colon X'\to Y'\) is \(L_{X'/Y'}=L_{\mathcal O_{X'}/h^{-1}\mathcal O_{Y'}}\) [Tag 08SU]. Since \(i_X^{-1}\mathcal O_{XY}=\mathcal O_X\), \(L_{X/XY}=L_{\mathcal O_X/\mathcal O_X}=0\); likewise \(L_{Z/ZT}=0\). The transitivity triangles [Tag 08V1] of \(X\xrightarrow{i_X}XY\xrightarrow{(p,q)}ZT\) and of \(X\xrightarrow{p}Z\xrightarrow{i_Z}ZT\), whose composites agree by Proposition 4.1, give isomorphisms \(Li_X^*L_{XY/ZT}\to L_{X/ZT}\to L_{X/Z}\), and \(Li_X^*=i_X^*\), \(i_X^*\) being exact. The same argument applies over \(Y\) and to \((p,q)\colon XY\to Z\), whose inverse image is a morphism of topoi as in Proposition 4.1 for the square with \(g=\mathrm{id}_Z\), composed with the projection \(ZZ\to Z\). \(\square\)

## 5. Exercises

**Exercise 5.1.** Let \(Y\) be a topological space, \(j\colon U\to Y\) the inclusion of an open subset and \(Z=Y\smallsetminus U\), with the sheaves of abelian groups. Show that \(H^i(Y/U;F)\cong H^i_Z(Y,F)\) canonically for \(F\in D^+(Y)\).

**Exercise 5.2.** In Exercise 5.1 let \(Y=\mathbf R\), \(U=\mathbf R\smallsetminus\{0\}\) and \(F=\mathbf Z[1]\). Show that \(\operatorname{Ext}^0(Y/U;\mathbf Z,F)\cong\mathbf Z\), while the corresponding group of morphisms of the category \(D'\) of Proposition 3.3 vanishes.

**Exercise 5.3.** For the identity \(f=\mathrm{id}_X\) of a ringed topos, show that \(R\operatorname{Hom}(X/X;M,F)=0\) for \(M\in D^-(X)\), \(F\in D^+(X)\).

## 6. Complete solutions

**Solution 5.1.** Here \(j^{-1}=j^*\) is exact, so \(\pi^*G=(j^{-1}G\leftarrow G)\) is exact and \(L\pi^*=\pi^*\). For a sheaf \(G\) on \(Y\), a morphism \((0\leftarrow\mathbf Z)\to\pi^*G\) is a section \(s\in\Gamma(Y,G)\) whose image in \(\Gamma(U,G)\) vanishes, by the compatibility with the maps of the two objects; so \(\operatorname{Hom}((0\leftarrow\mathbf Z),\pi^*G)=\Gamma_Z(Y,G)\), naturally in \(G\). The functor \(\pi^*\) has the exact left adjoint \(\lambda(A_U\xleftarrow{\psi}A_Y)=(A_Y\oplus j_!A_U)/j_!j^{-1}A_Y\), the quotient by the image of \((\iota,-j_!\psi)\), with \(\iota\colon j_!j^{-1}A_Y\to A_Y\) the inclusion: a morphism \(A\to\pi^*G\) is a pair of maps \(A_Y\to G\) and \(j_!A_U\to G\) (adjoint to \(A_U\to j^{-1}G\)) that agree on \(j_!j^{-1}A_Y\). \(\lambda\) is exact, being the cokernel of a natural monomorphism between exact functors. So \(\pi^*\) preserves injectives [Tag 015Z]. For \(F\) represented by a bounded below complex of injectives \(I\), \(\pi^*I\) is a bounded below complex of injectives representing \(L\pi^*F\), and \(R\operatorname{Hom}(Y/U;\mathbf Z,F)\) is represented by \(\operatorname{Hom}^\bullet((0\leftarrow\mathbf Z),\pi^*I)=\Gamma_Z(Y,I)\), which represents \(R\Gamma_Z(Y,F)\).

**Solution 5.2.** By Exercise 5.1, \(\operatorname{Ext}^0(Y/U;\mathbf Z,\mathbf Z[1])=H^1_{\{0\}}(\mathbf R,\mathbf Z)\). In the exact sequence
\[
\begin{aligned}&H^0(\mathbf R,\mathbf Z)\to H^0(U,\mathbf Z)\\&\quad\to H^1_{\{0\}}(\mathbf R,\mathbf Z)\to H^1(\mathbf R,\mathbf Z)=0,\end{aligned}
\]
the first map is the diagonal \(\mathbf Z\to\mathbf Z^2\), \(U\) having two connected components, so \(H^1_{\{0\}}(\mathbf R,\mathbf Z)\cong\mathbf Z^2/\mathbf Z\cong\mathbf Z\). The morphisms of \(D'\) form the kernel of \(\operatorname{Ext}^0(\mathbf Z,\mathbf Z[1])=H^1(\mathbf R,\mathbf Z)=0\to\) \(\operatorname{Ext}^0(\mathbf Z_U,\mathbf Z_U[1])\), which is \(0\) (Proposition 3.3 (3)). So \(\Phi\) is not injective on this Hom group: its kernel is the image \(\mathbf Z\) of \(\operatorname{Ext}^{-1}(\mathbf Z_U,\mathbf Z_U[1])=H^0(U,\mathbf Z)\).

**Solution 5.3.** For \(f=\mathrm{id}\), \(Lf^*\) is the identity functor, so in the triangle of Proposition 3.2 the map \(R\operatorname{Hom}(M,F)\to R\operatorname{Hom}(Lf^*M,Lf^*F)\) is the identity; hence the first term vanishes.

## Sources

The arrow topos, relative Ext groups and their exact sequences, and the computation of the cotangent complex of a morphism of arrow topoi are due to Illusie, in his work on the cotangent complex, where they serve to deform morphisms together with their target; there the relative Ext groups are credited to Grothendieck, who defined them through the triangle of Proposition 3.2.
