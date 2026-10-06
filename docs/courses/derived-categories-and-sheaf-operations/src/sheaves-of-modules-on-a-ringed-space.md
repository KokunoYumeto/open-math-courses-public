# Sheaves of modules on a ringed space

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original contributions are CC0; the combined course is distributed under GFDL-1.2-or-later. Full authorship and source attribution appear in the [course notice](../LICENCE.md).*

The first task in derived sheaf theory is to decide what an exact sequence means. A map can lift every germ and still fail to lift a global section. A cokernel must therefore be constructed locally, whereas a kernel can be constructed directly on sections. Once this distinction is clear, the basic operations on sheaves acquire precise exactness properties. These properties will determine which operations need resolutions in later lessons.

The prerequisites are the elementary definitions of a topological space, a ring, a left module, a functor, a limit and an adjunction. The real-interval examples use the complete ordered field \(\mathbb R\) with its usual order topology; Example 6.2 proves interval connectedness and the needed Archimedean consequence from its least-upper-bound axiom. Section 1 recalls presheaves and proves the filtered-colimit, module-category, sheafification and stalk facts used below. In particular, [Lemma 1.3](#sheafification-and-the-stalk-test) supplies the germ construction, its universal property and the isomorphism test without assuming an abelian category of sheaves. Definitions and the germ construction are also freely readable in the Stacks project authors’ [*Sheaves on Spaces*](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/sheaves.tex), in the AI Integrated Stacks Project edition.

After this lesson, *Injective modules and bounded-below derived functors* will construct resolutions using skyscrapers. *Flat modules and K-flat resolutions* will use extensions by zero to construct flat resolutions. The distinction between inverse image and module pullback is the starting point for *Derived pullback and pushforward*.

The main construction source is the Stacks project authors’ *Sheaves of Modules*, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/modules.tex). The kernels, cokernels, colimits and sheaf operations developed below supply the foundations for the resolution lessons. Every proof prerequisite for this lesson is supplied below. Source attribution and the licence for adapted passages appear in the [course notice](../LICENCE.md).
## 1. Coefficients, germs and finite relations

Let \(X\) be any topological space and let \(\mathcal O\) be a sheaf of associative rings with identity. Commutativity is not assumed. A sheaf of left \(\mathcal O\)-modules assigns to each open \(V\) an \(\mathcal O(V)\)-module, with restriction maps compatible with restriction of scalars. Write \(\operatorname{Mod}(\mathcal O)\) for their category. The zero ring and the empty space are allowed. All indexing sets and diagrams lie in one fixed universe.

A stalk \(F_x\) consists of germs of sections near \(x\). To define its action by \(\mathcal O_x\), represent the scalar and section on a common neighbourhood and multiply there. Changing representatives does not change the resulting germ. The ring identities and module identities follow on such a common neighbourhood. In particular the action is meaningful for noncommutative rings, with the order of multiplication preserved.

**Lemma 1.1 (filtered colimits of modules).** For a fixed ring \(A\), filtered colimits in \(\operatorname{Mod}(A)\) preserve short exact sequences.

**Proof.** A category is filtered if every finite collection of objects and arrows has a compatible map to a common object. Equivalently, it is nonempty, any pair of objects maps to a common object, and any two parallel arrows become equal after a further arrow. Elements of a filtered colimit can be represented at one object. A finite list of elements can be moved to one common object. Equality of two representatives can be checked after maps to one further object: the relations defining a colimit involve finitely many arrows, and filteredness moves all of them to a common object and equalizes parallel arrows. Thus a representative is zero precisely when it becomes zero after some further arrow.

Given a filtered diagram of exact sequences \(0\to A_i\to B_i\to C_i\to0\), suppose an element of \(\varinjlim A_i\) maps to zero in \(\varinjlim B_i\). Represent it at \(i\), and move to an object where its image in \(B\) is zero. Injectivity of \(A\to B\) at that object makes the representative zero there. This proves injectivity on colimits. If a representative in \(B_i\) maps to zero in the colimit of \(C_i\), move to an object where its image in \(C\) is zero and use exactness there to lift it from \(A\). Finally every representative in \(C_i\) lifts from \(B_i\). These give exactness at the middle and surjectivity at the right. The constructions respect addition and the \(A\)-action. \(\square\)

In a neighbourhood diagram used to construct a stalk, the rings \(\mathcal O(V)\) vary. We apply Lemma 1.1 to the underlying abelian groups, which all have the fixed coefficient ring \(\mathbb Z\). The induced equalities of kernels and cokernels respect the \(\mathcal O_x\)-action, since every scalar germ and each finite list of section germs can be represented on a common neighbourhood. Thus there is no assumption that the neighbourhood diagram has one fixed section ring.

The word *filtered* cannot be removed. For a pushout diagram written \(L\leftarrow M\to R\), consider the following componentwise short exact sequence of diagrams:

\[
(\mathbb Z\leftarrow0\to0)
\longrightarrow(\mathbb Z\xleftarrow{1}\mathbb Z\to0)
\longrightarrow(0\leftarrow\mathbb Z\to0).
\]

The first map is the identity on the left object and the zero inclusion on the other objects; the second is the identity on the middle object and the quotient elsewhere. The maps commute with both arrows. The three pushouts are respectively \(\mathbb Z,0,0\). The first resulting map is not injective. This example already occurs on a one-point space.

**Lemma 1.2 (the elementary module category).** Left modules over any ring form an abelian category. Kernels are submodules, cokernels are quotient modules, and a sequence is exact if its ordinary image equals its ordinary kernel. Small limits exist as compatible tuples in products; small colimits exist as a direct sum modulo the relations from the arrows.

**Proof.** The kernel of \(u:M\to N\) is \(\{m:u(m)=0\}\); its universal property follows because a map killed by \(u\) lands there. The cokernel is \(N/u(M)\); a map vanishing on \(u(M)\) factors uniquely through that quotient. The map \(M/\ker u\to u(M)\), \([m]\mapsto u(m)\), is linear, onto and one-to-one. Thus the canonical coimage-to-image map is an isomorphism. Morphisms add, composition is bilinear, and finite direct sums are simultaneously products and coproducts. These facts establish the abelian-category axioms and the stated exactness criterion. For a diagram, compatible tuples in the product have the universal property of its limit. Quotienting the direct sum by all elements \(m_i-u(m_i)\) associated with arrows \(i\to j\) gives the colimit's universal property. These constructions are sets in the chosen universe. \(\square\)

Sheafification will be denoted \(P^+\).

### Sheafification and the stalk test

**Lemma 1.3 (sheafification and the stalk test).** Let \(X\) be any topological space.

1. Every presheaf of sets \(P\) has a sheaf \(P^+\) and a map \(\eta:P\to P^+\) that induces a bijection on every stalk. Every section of \(P^+\) is locally the image of a section of \(P\). For each sheaf \(H\), composition with \(\eta\) gives a bijection
   \(\operatorname{Hom}(P^+,H)\cong\operatorname{Hom}(P,H)\).
2. If \(P\) is separated, \(\eta_U\) is injective for each open \(U\).
3. For a presheaf of rings, the same construction preserves addition, multiplication and the identity. For a presheaf of left modules over a sheaf of associative unital rings \(\mathcal O\), it produces a sheaf of left \(\mathcal O\)-modules with the same universal property for linear maps. Commutativity is unnecessary.
4. A map of sheaves of sets whose stalk maps are all bijective is an isomorphism. This also holds for sheaves of rings and of modules.

**Proof.** Recall the elementary definitions. A presheaf gives sections on opens and restriction maps compatible with composition. A sheaf glues every family of sections agreeing on overlaps to a unique section on the union. A separated presheaf has the uniqueness part of this condition. Empty covers are included, so a sheaf of sets has exactly one section on the empty open.

For an open \(U\), define \(P^+(U)\) to be the families \((a_x)_{x\in U}\), with \(a_x\in P_x\), having the following property: each \(x\) has a neighbourhood \(V\subset U\) and \(p\in P(V)\) such that \(a_y=p_y\) for every \(y\in V\). Restrictions discard coordinates, and \(\eta_U(p)=(p_x)_{x\in U}\). Compatible families on a cover glue coordinate by coordinate. At a point, any local representative from a covering member represents the glued family on that same neighbourhood. This proves existence and uniqueness of gluing in \(P^+\), including its one empty family on the empty open.

A germ of a section of \(P^+\) at \(x\) has a local representative \(\eta(p)\); hence \(\eta_x\) is surjective. If two germs from \(P_x\) have the same image, their images as families agree on a neighbourhood of \(x\). Their coordinates at \(x\) are therefore equal in \(P_x\), proving injectivity. If \(P\) is separated and \(\eta_U(p)=\eta_U(q)\), equality of germs gives a cover of \(U\) on which \(p\) and \(q\) agree. Separatedness then gives \(p=q\), proving (2).

Sections of any sheaf \(H\) with the same germs agree: germ equality gives equality on a neighbourhood of each point, and the uniqueness part of the sheaf condition gives equality on the union. Given \(b:P\to H\), choose local representatives \(p_i\) of a family in \(P^+(U)\). On an overlap, \(b(p_i)\) and \(b(p_j)\) have the same germs, so they agree. Glue them in \(H\). Changing representatives produces sections with the same germs and hence the same glued section. The construction commutes with restrictions and extends \(b\). Any extension must agree with it locally on all representatives, hence globally by uniqueness of gluing. This proves the universal property in (1).

For (3), form the algebraic operations coordinatewise on germs. To check local representability of a sum or product, restrict the finitely many representatives to one common neighbourhood and perform the corresponding operation there. Zero and the identity are locally represented by their section values. All ring identities therefore hold on germs and on their families, with the given order of multiplication. The extension of a ring map preserves these operations, as is checked on those local representatives. For a module presheaf, define
\((c\cdot a)_x=c_xa_x\) for \(c\in\mathcal O(U)\). Near a point, represent \(a\) by \(p\) and use \(c|_V p\); thus the action preserves local representability. The module identities and restriction compatibility follow from the section identities. The universal extension of a linear map is linear because that identity can be checked on local representatives and then glued. On the empty open the ring and module have their unique zero element. None of these arguments uses an abelian category of sheaves.

Finally let \(u:F\to G\) have bijective stalk maps. Injectivity on stalks implies injectivity on sections, by the germ-equality argument above. Given \(g\in G(U)\), lift its germ at each point, represent the lift on a neighbourhood, and shrink until its image equals the restriction of \(g\). The local lifts agree on overlaps by sectionwise injectivity. They glue to an \(f\in F(U)\) with \(u(f)=g\). Thus every \(u_U\) is bijective. Its inverse commutes with restrictions, since restricting a lift is the unique lift on the smaller open. For rings and modules the inverses preserve the operations because the original bijections do. This proves (4). \(\square\)

The germ construction follows the Stacks project authors’ [*Sheaves on Spaces*, sheafification](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/sheaves.tex#L1522), in the AI Integrated Stacks Project edition. The proof above includes the stalk-isomorphism argument and the associative-ring module operations in full. Adapted material retains GFDL-1.2-or-later; the expansion and checks are by GPT-6.1 Sol (OpenAI), at Ultra.

**Lemma 1.4 (colimits and adjoints).** Whenever the indicated small colimits exist, the two iterated colimits of a diagram indexed by a product of two small categories are canonically isomorphic. A left adjoint preserves all existing small colimits, and a right adjoint preserves all existing small limits.

**Proof.** For a diagram \(D:I\times J\to\mathcal C\), a map from \(\varinjlim_i\varinjlim_jD(i,j)\) to an object \(T\) is, by the two colimit universal properties, a family of maps \(D(i,j)\to T\) compatible with every arrow in both indices. The same description holds for maps from \(\varinjlim_j\varinjlim_iD(i,j)\). Applying the first description to the structural maps into the second colimit constructs a unique comparison, and reversing the roles constructs its inverse. Their composites fix every structural map, so uniqueness makes them identities. This also proves naturality of the comparison.

Suppose \(L:\mathcal C\to\mathcal D\) is left adjoint to \(R\). A map \(L(\varinjlim_iD_i)\to T\) corresponds successively to a map \(\varinjlim_iD_i\to RT\), a compatible family \(D_i\to RT\), and a compatible family \(LD_i\to T\). The adjunction is natural, so these correspondences respect the diagram arrows. Thus \(L(\varinjlim_iD_i)\), with the images of the structural maps, has exactly the colimit universal property for \((LD_i)\). For limits, a map \(T\to R(\varprojlim_iE_i)\) corresponds successively to a map \(LT\to\varprojlim_iE_i\), a compatible family \(LT\to E_i\), and a compatible family \(T\to RE_i\). This is the limit universal property for \((RE_i)\). The canonical comparisons are therefore isomorphisms. \(\square\)

## 2. The abelian category of module sheaves

**Theorem 2.1.** Let \(\mathcal O\) be any sheaf of rings on \(X\).

1. \(\operatorname{Mod}(\mathcal O)\) is additive. A morphism \(\varphi:F\to G\) has a kernel, computed on sections: \((\operatorname{Ker}\varphi)(U)=\ker\varphi_U\). It has a cokernel: the sheafification of \(U\mapsto\operatorname{coker}\varphi_U\).
2. For each \(x\), the stalk functor \(F\mapsto F_x\), from \(\operatorname{Mod}(\mathcal O)\) to \(\operatorname{Mod}(\mathcal O_x)\), is additive, and \((\operatorname{Ker}\varphi)_x=\ker\varphi_x\), \((\operatorname{Coker}\varphi)_x=\operatorname{coker}\varphi_x\).
3. \(\operatorname{Mod}(\mathcal O)\) is abelian, and each stalk functor is exact.
4. A sequence \(F\to G\to H\) with zero composite is exact at \(G\) if and only if \(F_x\to G_x\to H_x\) is exact at \(G_x\) for every \(x\). A morphism \(\varphi\) is a monomorphism (epimorphism, isomorphism) if and only if every \(\varphi_x\) is one.

**Proof.** (1) Morphisms add on sections, and composition is bilinear. The zero sheaf is a zero object. Finite direct sums are formed on sections: \(U\mapsto F(U)\oplus G(U)\) is a sheaf, because sections glue coordinatewise. Let \(\varphi:F\to G\). The presheaf \(U\mapsto\ker\varphi_U\) is a sheaf. Indeed, let a section \(s\) of \(F\) lie in the kernel on each set of an open cover. Then \(\varphi(s)\) vanishes on that cover, so \(\varphi(s)=0\), since \(G\) is a sheaf. Sections of the kernel that agree on overlaps glue in \(F\), and by this remark the glued section lies in the kernel. Each \(\varphi_U\) is \(\mathcal O(U)\)-linear, so the kernel is a subpresheaf of left modules. A morphism \(E\to F\) whose composite with \(\varphi\) is zero lands in it on every open set. So it is the kernel. For the cokernel, let \(P(U)=\operatorname{coker}\varphi_U\), a presheaf of left \(\mathcal O\)-modules. By [Lemma 1.3](#sheafification-and-the-stalk-test), morphisms \(P^+\to H\) into a sheaf \(H\) correspond to morphisms of presheaves \(P\to H\). These are the morphisms \(G\to H\) that vanish after \(\varphi\). So \(P^+\) is the cokernel.

(2) The stalk \(F_x=\varinjlim_{U\ni x}F(U)\) is a left module over \(\mathcal O_x=\varinjlim_{U\ni x}\mathcal O(U)\), and the functor is additive. The open neighbourhoods of \(x\) form a filtered system, and filtered colimits are exact (Lemma 1.1). Hence \((\operatorname{Ker}\varphi)_x=\varinjlim_U\ker\varphi_U=\ker\varphi_x\). By [Lemma 1.3](#sheafification-and-the-stalk-test), \(\eta\) is bijective on stalks, so \((P^+)_x=P_x\); and by (Lemma 1.1) again, \(P_x=\varinjlim_U\operatorname{coker}\varphi_U=\operatorname{coker}\varphi_x\).

(3) The coimage of \(\varphi\) is the cokernel of \(\operatorname{Ker}\varphi\to F\). The image is the kernel of \(G\to\operatorname{Coker}\varphi\). By (2), at each \(x\) the canonical map \(\operatorname{Coim}\varphi\to\operatorname{Im}\varphi\) becomes the canonical map \(\operatorname{Coim}\varphi_x\to\operatorname{Im}\varphi_x\) of \(\mathcal O_x\)-modules. That map is an isomorphism, because modules over a ring form an abelian category. By [Lemma 1.3](#sheafification-and-the-stalk-test)(4) the map of sheaves is an isomorphism. Its inverse is \(\mathcal O\)-linear, as the map is. So \(\operatorname{Mod}(\mathcal O)\) is abelian. The stalk functor preserves kernels and cokernels by (2), so it is exact.

(4) Exactness at \(G\) means that \(\operatorname{Im}(F\to G)\to\operatorname{Ker}(G\to H)\) is an isomorphism. Both sides are built from kernels and cokernels. By (2), the map at \(x\) is the same map for the stalk sequence. If every stalk sequence is exact, [Lemma 1.3](#sheafification-and-the-stalk-test)(4) gives exactness. Conversely, exact functors preserve exactness. A sheaf whose stalks all vanish is zero, since each section then vanishes on an open cover. Hence \(\varphi\) is a monomorphism iff \(\operatorname{Ker}\varphi=0\) iff every \(\ker\varphi_x=0\). The same holds with cokernels. An isomorphism is a morphism that is both. \(\square\)

The proof never uses commutativity of \(\mathcal O\). In particular, Theorem 2.1 holds for the constant sheaf \(k_X\) of any unital ring \(k\), commutative or not.

## 3. Limits, colimits, stalks, and sections of sums

**Theorem 3.1.** Let \(\mathcal O\) be any sheaf of rings on \(X\).

1. Every small diagram \((F_i)\) in \(\operatorname{Mod}(\mathcal O)\) has a limit, computed on sections. So \(\Gamma(U,-)\) commutes with limits.
2. Every small diagram has a colimit: the sheafification of the presheaf colimit. Stalks commute with colimits: \((\varinjlim_iF_i)_x=\varinjlim_i(F_i)_x\).
3. Filtered colimits are exact.
4. Finite direct sums are computed on sections.
5. If \(U\) is a quasi-compact open set, the canonical map \(\bigoplus_i\Gamma(U,F_i)\to\Gamma(U,\bigoplus_iF_i)\) is bijective for every family. Without quasi-compactness it can fail to be onto (Exercise 5).
6. Products exist and are computed on sections, but they need not be exact (Exercise 6).

**Proof.** (1) Let \(L(U)=\varprojlim_iF_i(U)\), with coordinatewise restriction and module structure. It is a sheaf. A local section on a cover is a compatible family on each piece. Glue each coordinate in \(F_i\). The glued coordinates again form a compatible family, because the transition maps are morphisms of sheaves and sections of a sheaf are determined locally. A morphism \(E\to L\) is the same as a compatible family of morphisms \(E\to F_i\), open set by open set. So \(L\) is the limit, and \(\Gamma(U,L)=\varprojlim_i\Gamma(U,F_i)\).

(2) Let \(P(U)=\varinjlim_iF_i(U)\). By [Lemma 1.3](#sheafification-and-the-stalk-test), morphisms \(P^+\to H\) into a sheaf correspond to compatible families of morphisms \(F_i\to H\). So \(P^+\) is the colimit. At \(x\),
\[
(P^+)_x=P_x=\varinjlim_{U\ni x}\varinjlim_iF_i(U)=\varinjlim_i\varinjlim_{U\ni x}F_i(U)=\varinjlim_i(F_i)_x ,
\]
by the iterated-colimit argument of Lemma 1.4, applied to the underlying abelian groups. The isomorphism respects the stalk-ring action: a scalar germ and each finite expression in the module colimit have representatives on a common neighbourhood, where the structural maps are linear.

(3) Let \(0\to A_i\to B_i\to C_i\to0\) be exact, naturally in \(i\) over a filtered category. At each \(x\), by (2), the stalk sequence of the colimits is the filtered colimit of the exact sequences \(0\to(A_i)_x\to(B_i)_x\to(C_i)_x\to0\). It is exact by (Lemma 1.1). Since exactness is checked on stalks ([Theorem 2.1](#2-the-abelian-category-of-module-sheaves)(4)), the colimit sequence is exact.

(4) This was shown in the proof of [Theorem 2.1](#2-the-abelian-category-of-module-sheaves)(1).

(5) Let \(S=\bigoplus_iF_i\), the sheafification of \(P(V)=\bigoplus_iF_i(V)\). The germ at \(x\) of \(p=(p_i)\in P(V)\) is \((p_{i,x})_i\in\bigoplus_i(F_i)_x\). If all germs of \(p\) vanish, each \(p_i\) has zero germs and is zero. So \(P\) is separated, and \(\theta:P(V)\to S(V)\) is injective for every \(V\). For \(V=U\) this is the injectivity of the canonical map. For surjectivity, let \(t\in S(U)\). By [Lemma 1.3](#sheafification-and-the-stalk-test), every point of \(U\) has an open neighbourhood \(V\subset U\) and some \(p\in P(V)\) with \(\theta(p)=t|_V\). As \(U\) is quasi-compact, finitely many such pairs \((V_1,p_1),\ldots,(V_m,p_m)\) cover \(U\). Each \(p_k\) has finitely many nonzero coordinates. Let \(J\) be the finite set of indices that occur, and \(S_J=\bigoplus_{i\in J}F_i\). By (4), \(S_J\) is a sheaf. It is also a subpresheaf of \(P\) that contains all \(p_k\). On \(V_k\cap V_l\), the restrictions of \(p_k\) and \(p_l\) have the same image under the injective map \(\theta\), so they are equal. Glue them to \(s\in S_J(U)=\bigoplus_{i\in J}F_i(U)\). Then \(\theta(s)\) and \(t\) agree on each \(V_k\), so \(\theta(s)=t\).

(6) Products are limits, so (1) applies. Exercise 6 proves that a product of epimorphisms need not be an epimorphism. \(\square\)

## 4. Exact inverse image

**Theorem 4.1.** Let \(f:X\to Y\) be continuous and \(\mathcal O_Y\) a sheaf of rings on \(Y\).

1. On \(X\), \(f^{-1}\mathcal O_Y\) is a sheaf of rings, with stalks \((f^{-1}\mathcal O_Y)_x=\mathcal O_{Y,f(x)}\). For \(G\in\operatorname{Mod}(\mathcal O_Y)\), \(f^{-1}G\) is a sheaf of left \(f^{-1}\mathcal O_Y\)-modules, and the canonical map \(G_{f(x)}\to(f^{-1}G)_x\) is an isomorphism of \(\mathcal O_{Y,f(x)}\)-modules.
2. \(f^{-1}:\operatorname{Mod}(\mathcal O_Y)\to\operatorname{Mod}(f^{-1}\mathcal O_Y)\) is exact and commutes with colimits.
3. For a unital ring \(k\), \(f^{-1}k_Y=k_X\) as sheaves of rings. So \(f^{-1}:\operatorname{Mod}(k_Y)\to\operatorname{Mod}(k_X)\) is exact, and \((f^{-1}G)_x=G_{f(x)}\) as \(k\)-modules. This holds for every unital ring \(k\), commutative or not.
4. \(f^{-1}\) is left adjoint to \(f_*:\operatorname{Mod}(f^{-1}\mathcal O_Y)\to\operatorname{Mod}(\mathcal O_Y)\).

All four assertions are proved below. For the freely accessible source treatment of exact inverse image on sheaves of abelian groups, see [the Stacks project, Tag 01AJ](https://stacks.math.columbia.edu/tag/01AJ).

**Proof of (1)–(3).** Recall that \(f^{-1}G\) is the sheafification of the presheaf \(V\mapsto\varinjlim_{W\supset f(V)}G(W)\), where \(W\) runs over the open sets containing \(f(V)\). We use its description by germs. For \(V\subset X\) open, \(f^{-1}G(V)\) is the set of maps \(s\) that give each \(x\in V\) an element \(s(x)\in G_{f(x)}\), such that each point of \(V\) has an open neighbourhood \(V'\subset V\), an open \(W\supset f(V')\) and a section \(g\in G(W)\) with \(s(x')=g_{f(x')}\) for all \(x'\in V'\). The condition is local, so this is a sheaf of sets. Take \(G=\mathcal O_Y\) to get \(f^{-1}\mathcal O_Y\). Sum, product and the action are defined pointwise, through the ring \(\mathcal O_{Y,f(x)}\) and its module \(G_{f(x)}\). They preserve the local condition: if near a point \(s\) is represented by \(g\in G(W)\) and \(a\) by \(h\in\mathcal O_Y(W')\), then near that point \(as\) is represented by \(h|_{W\cap W'}\,g|_{W\cap W'}\). This gives the ring and module structures. Evaluation at \(x\) is a ring map, and a module map over it.

Evaluation \((f^{-1}G)_x\to G_{f(x)}\) is onto: \(g\in G(W)\) with \(W\ni f(x)\) defines a section over \(f^{-1}(W)\). It is one-to-one: if \(s(x)=0\), represent \(s\) near \(x\) by \(g\in G(W)\). Then \(g_{f(x)}=0\), so \(g\) vanishes on an open \(W_0\ni f(x)\), and \(s\) vanishes on \(V'\cap f^{-1}(W_0)\). The canonical map \(G_{f(x)}\to(f^{-1}G)_x\) sends the germ of \(g\) to the germ of the section defined by \(g\). It is inverse to evaluation. This proves (1).

(2) Exactness can be checked on stalks ([Theorem 2.1](#2-the-abelian-category-of-module-sheaves)(4)). By (1), the stalk of \(f^{-1}G\) at \(x\) is \(G_{f(x)}\), so on stalks \(f^{-1}\) acts as the identity, and \(f^{-1}\) is exact. For a colimit, the canonical map \(\varinjlim_if^{-1}G_i\to f^{-1}\varinjlim_iG_i\) is, at \(x\), the map \(\varinjlim_i(G_i)_{f(x)}\to(\varinjlim_iG_i)_{f(x)}\). This map is bijective, because stalks commute with colimits ([Theorem 3.1](#3-limits-colimits-stalks-and-sections-of-sums)(2)). So the canonical map is an isomorphism by [Lemma 1.3](#sheafification-and-the-stalk-test)(4).

(3) A germ of a section of \(k_Y\) is the germ of a locally constant function. So the sections of \(f^{-1}k_Y\) over \(V\) are the maps \(V\to k\) that are constant near each point, that is, the sections of \(k_X\). The ring operations agree pointwise. The argument never uses commutativity of \(k\). \(\square\)

**Proof of (4).** Let \(G\) be an \(\mathcal O_Y\)-module and \(F\) an \(f^{-1}\mathcal O_Y\)-module. A map \(\alpha:f^{-1}G\to F\) sends a section \(g\in G(W)\) to the image under \(\alpha\) of its pullback section on \(f^{-1}(W)\). This defines
\[
\beta_W:G(W)\longrightarrow F(f^{-1}(W))=(f_*F)(W).
\]
The maps commute with restriction and are \(\mathcal O_Y(W)\)-linear through the canonical map \(\mathcal O_Y(W)\to(f^{-1}\mathcal O_Y)(f^{-1}(W))\).

Conversely, suppose \(\beta:G\to f_*F\) is \(\mathcal O_Y\)-linear. Locally a section \(s\) of \(f^{-1}G\) on \(V\) is represented by a section \(g\in G(W)\), with \(f(V)\subset W\). Send it to \(\beta_W(g)|_V\). If two representatives have the same germ at \(x\), their germs in \(G_{f(x)}\) agree, so they agree on some smaller neighbourhood \(W'\) of \(f(x)\). Their proposed images therefore agree near \(x\). This proves independence of representatives; the proposed local images glue uniquely. Multiplication is checked after locally representing the scalar by a section of \(\mathcal O_Y\), so the glued map is \(f^{-1}\mathcal O_Y\)-linear. The two constructions undo one another on local representatives, and hence everywhere. They commute with maps of \(G\) and \(F\); this is the adjunction. \(\square\)


### Composing inverse images

**Lemma 4.2 (inverse-image composition).** For continuous maps \(X\xrightarrow fY\xrightarrow gZ\) and a sheaf of rings or modules \(H\) on \(Z\), there is a canonical natural isomorphism
\[
f^{-1}g^{-1}H\cong(gf)^{-1}H.
\]
For modules it is linear over the corresponding ring isomorphism. These comparisons agree for every association of three successive inverse images. No commutativity of the coefficient rings is required.

**Proof.** Use the local germ description in Theorem 4.1. A section of \(f^{-1}g^{-1}H\) near \(x\) is locally represented by a section \(t\) of \(g^{-1}H\) near \(f(x)\). Shrink that neighbourhood so that \(t\) is itself represented by a section \(h\in H(W)\), where \(W\) contains the image under \(g\) of the smaller neighbourhood. On its inverse image in \(X\), send the original section to the section of \((gf)^{-1}H\) represented by this same \(h\). Changing representatives does not change its germ at \(x\): the stalk evaluations in Theorem 4.1 identify both with the same germ in \(H_{g(f(x))}\). Therefore the proposed local images agree on overlaps and glue uniquely. They commute with restrictions and with ring operations or scalar multiplication, as is checked on those representatives.

At every \(x\) this sheaf map is the identity under the identifications of both stalks with \(H_{g(f(x))}\). Lemma 1.3 makes it an isomorphism. A morphism of \(H\)'s acts on the same local representatives, proving naturality. For three maps, every route sends a locally represented section of the original sheaf to the germ of that same section at the final image point. The routes have equal stalk maps, and equality of sheaf maps can be checked on germs, so the comparisons agree. \(\square\)

### Module pullback and extension of scalars

The inverse image changes the space. A morphism of ringed spaces also changes the coefficient ring. Let

\[
f:(X,\mathcal O_X)\longrightarrow(Y,\mathcal O_Y)
\]

consist of a continuous map and a specified homomorphism \(f^{-1}\mathcal O_Y\to\mathcal O_X\). Write \(A=f^{-1}\mathcal O_Y\) and \(B=\mathcal O_X\). Then \(B\) is a \((B,A)\)-bimodule: its right \(A\)-action is multiplication by the image of \(A\). For an \(A\)-module \(N\), the sheaf \(B\otimes_A N\) is the sheafification of \(V\mapsto B(V)\otimes_{A(V)}N(V)\). It is a sheaf of left \(B\)-modules.

**Lemma 4.3 (tensor and stalks).** There is a natural isomorphism

\[
(B\otimes_A N)_x\cong B_x\otimes_{A_x}N_x.
\]

**Proof.** A tensor on either side is a finite sum of elementary tensors. Choose representatives for its finitely many factors on one neighbourhood of \(x\); this constructs the inverse of the canonical map from the left side to the right. The tensor relations are finite sums of additivity and balancing relations \(ba\otimes n=b\otimes an\). Any finite collection of germs witnessing those relations can again be represented on a common neighbourhood. Thus two representing expressions give the same germ exactly when the corresponding tensors agree on the right. Sheafification preserves stalks, so this verifies both injectivity and surjectivity for the displayed sheaf tensor product. \(\square\)

**Theorem 4.4 (pullback adjunction and exactness).** Define

\[
f^*G=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}G.
\]

For sheaves of left modules over arbitrary unital coefficient rings, \(f^*\) is left adjoint to \(f_*\). It is right exact; \(f_*\) is left exact. At a point,

\[
(f^*G)_x=\mathcal O_{X,x}\otimes_{\mathcal O_{Y,f(x)}}G_{f(x)}.
\]

**Proof.** First, extension of scalars is left adjoint to forgetting the \(B\)-action. Given a \(B\)-linear map \(t:B\otimes_A N\to F\), define \(a:N\to F\) by \(n\mapsto t(1\otimes n)\). It is \(A\)-linear by the balancing relation. Conversely an \(A\)-linear map \(a\) defines \(b\otimes n\mapsto ba(n)\) on elementary tensors. This is balanced, hence gives a map on the presheaf tensor product and uniquely on its sheafification. The two formulas undo one another, commute with restriction, and are natural in both modules. Combining them with Theorem 4.1(4) gives

\[
\operatorname{Hom}_{\mathcal O_X}(f^*G,F)
\cong\operatorname{Hom}_{f^{-1}\mathcal O_Y}(f^{-1}G,F)
\cong\operatorname{Hom}_{\mathcal O_Y}(G,f_*F).
\]

Here the middle term regards \(F\) as an \(f^{-1}\mathcal O_Y\)-module through the specified ring map. Thus the adjunction has the required coefficient structures. The stalk formula follows from Lemma 4.3 and Theorem 4.1(1).

For completeness, tensor over a ring is right exact. If \(N\to N'\to N''\to0\) is exact, present \(N''\) as the quotient of \(N'\) by the image of \(N\). A balanced map on \(B\times N''\) is exactly a balanced map on \(B\times N'\) vanishing on \(B\times\operatorname{im}N\). The defining universal property of tensor therefore identifies \(B\otimes N''\) with the cokernel of \(B\otimes N\to B\otimes N'\). This also proves surjectivity of the map to that cokernel. Apply this fact to the stalk formula and use Theorem 2.1 to obtain right exactness of \(f^*\).

Finally \((f_*F)(V)=F(f^{-1}V)\). Kernels of module-sheaf maps are computed on sections, so \(f_*\) preserves kernels. It preserves finite products as well, again by their sectionwise description. These are the left-exactness assertions. No commutativity was used. \(\square\)

The tensor of two *left* \(\mathcal O\)-modules used in later lessons requires commutative \(\mathcal O\). The tensor in Theorem 4.4 has a specified right action on its first factor and therefore does not need that hypothesis.

**Example 4.5 (an exact inverse image with a nonexact pullback).** Take both spaces to be a point and use the coefficient map \(\mathbb Z\to\mathbb Z/2\). Inverse image on abelian groups is the identity. Module pullback is \(\mathbb Z/2\otimes_{\mathbb Z}-\). The injection \(\mathbb Z\xrightarrow{2}\mathbb Z\) becomes the zero map \(\mathbb Z/2\to\mathbb Z/2\), so pullback is not left exact. If the specified structure map \(f^{-1}\mathcal O_Y\to\mathcal O_X\) is an isomorphism, the formula instead identifies \(f^*\) with \(f^{-1}\), and pullback is exact.


## 5. Extension by zero and skyscrapers

**Lemma 5.1 (extension by zero from an open set).** Let \(j:U\hookrightarrow X\) be open and \(B\) a sheaf of left \(\mathcal O|_U\)-modules. For \(V\subset X\) open put
\[
j_!B(V)=\{\,s\in B(U\cap V):\ \operatorname{supp}s\text{ is closed in }V\,\}.
\]
1. \(j_!B\) is a sheaf of left \(\mathcal O\)-modules, with \((j_!B)_x=B_x\) for \(x\in U\) and \((j_!B)_x=0\) for \(x\notin U\). So \(j_!\) is exact.
2. \(\operatorname{Hom}_{\mathcal O}(j_!B,G)\cong\operatorname{Hom}_{\mathcal O|_U}(B,G|_U)\), naturally in \(B\) and \(G\).
3. \(\operatorname{Hom}_{\mathcal O}(j_!\mathcal O_U,G)\cong G(U)\) by \(\varphi\mapsto\varphi(1)\). For opens \(V\subset W\), the morphism \(j_{V!}\mathcal O_V\to j_{W!}\mathcal O_W\) that corresponds to \(1\in\mathcal O(V)=(j_{W!}\mathcal O_W)(V)\) is a monomorphism, and under these identifications it induces restriction \(G(W)\to G(V)\).

**Proof.** (1) Supports of sections are closed in their domains. Closedness of a support in \(V\) is a local condition on \(V\), so sections of \(B\) glue within \(j_!B\), and \(j_!B\) is a sheaf. Module operations do not enlarge supports. If \(x\in U\), the opens inside \(U\) are cofinal among neighbourhoods of \(x\), and there \(j_!B=B\); so \((j_!B)_x=B_x\). If \(x\notin U\) and \(s\in j_!B(V)\) with \(x\in V\), then \(x\notin\operatorname{supp}s\), and this support is closed in \(V\); so \(s\) vanishes near \(x\) and the stalk is \(0\). Exactness is checked on stalks ([Theorem 2.1](#2-the-abelian-category-of-module-sheaves)(4)), and on each stalk \(j_!\) acts as the identity or as zero; so \(j_!\) is exact.

(2) A morphism \(j_!B\to G\) restricts over \(U\) to a morphism \(B\to G|_U\). Conversely, let \(\alpha:B\to G|_U\) and \(s\in j_!B(V)\). The section \(\alpha(s)\) on \(U\cap V\) and the section \(0\) on \(V\setminus\operatorname{supp}s\) agree on the overlap. The two open sets cover \(V\), because \(\operatorname{supp}s\subset U\cap V\). Glue them to a section of \(G\) over \(V\). This defines the inverse bijection; linearity and naturality are checked on the two pieces.

(3) By (2), a morphism \(j_!\mathcal O_U\to G\) is a left-linear map \(\mathcal O_U\to G|_U\), and such a map is \(a\mapsto as\) with \(s\) the image of \(1\in\mathcal O(U)\). For \(V\subset W\), \((j_{W!}\mathcal O_W)(V)=\mathcal O(V)\). At \(x\in V\) the morphism is the identity of \(\mathcal O_x\); at other points its source stalk is \(0\). So it is injective on every stalk, hence a monomorphism by [Theorem 2.1](#2-the-abelian-category-of-module-sheaves)(4). Composing with it sends the morphism with \(\varphi(1)=s\in G(W)\) to the one with value \(s|_V\) at \(1\). \(\square\)

**Lemma 5.2 (skyscrapers).** Let \(x\in X\) and let \(J\) be a left \(\mathcal O_x\)-module. Put \(x_*J(V)=J\) if \(x\in V\) and \(0\) otherwise, with identity restrictions between opens containing \(x\), and let \(\mathcal O(V)\) act through \(\mathcal O(V)\to\mathcal O_x\). Then \(x_*J\) is a sheaf of left \(\mathcal O\)-modules, and
\[
\operatorname{Hom}_{\mathcal O}(F,x_*J)\cong\operatorname{Hom}_{\mathcal O_x}(F_x,J),
\tag{5.2}
\]
naturally in \(F\) and \(J\). 

**Proof.** Let \(x\in V\) and let \((V_i)\) cover \(V\). Some \(V_i\) contains \(x\). Compatible sections agree on all \(V_i\) that contain \(x\), since their pairwise overlaps contain \(x\); this common value is the glued section, and it is unique. If \(x\notin V\), all sections are \(0\). A morphism \(\varphi:F\to x_*J\) has components \(\varphi_V\), for \(x\in V\), that are compatible with restriction. So they define an \(\mathcal O_x\)-linear map \(F_x\to J\). Conversely, given \(g:F_x\to J\), put \(\varphi_V(s)=g(s_x)\) if \(x\in V\) and \(0\) otherwise. These constructions are inverse. \(\square\)


### The right adjoint of a skyscraper

The stalk records sections on shrinking neighborhoods. A second functor records maps *from* a skyscraper. Murfet, [*Modules over a Ringed Space*, §1.1, p. 5](https://therisingsea.org/notes/RingedSpaceModules.pdf), explains this third adjoint. The following proof also treats noncommutative coefficient rings.

**Proposition 5.3 (the costalk adjunction).** For every point \(x\), put \(R=\mathcal O_x\) and
\[
c_xF=\operatorname{Hom}_{\mathcal O}(x_*R,F),
\qquad (r\phi)_V(t)=\phi_V(tr).
\]
Here \(V\) contains \(x\), and \(t,r\in R\). This is a left \(R\)-module, and there are natural adjunctions
\[
(-)_x\dashv x_*\dashv c_x.
\]
In particular \(x_*\) preserves all small limits and colimits. If \(x\) is closed, there is a natural identification
\[
c_xF=\bigl(\ker(F\longrightarrow j_*F|_{X\setminus\{x\}})\bigr)_x,
\]
where \(j:X\setminus\{x\}\hookrightarrow X\). No closed-point hypothesis is needed for the adjunction itself.

**Proof.** Right multiplication \(t\mapsto tr\) is a morphism of left \(R\)-modules, so precomposition defines a sheaf map \(r\phi\). Moreover

\[
r(s\phi)(t)=\phi((tr)s)=\phi(t(rs))=((rs)\phi)(t).
\]

Addition and the identity follow from the same formula. For a left \(R\)-module \(M\), a sheaf map \(v:x_*M\to F\) determines a map \(a:M\to c_xF\) by
\[
a(m)_V(t)=v_V(tm).
\]
It is \(R\)-linear: \(a(rm)_V(t)=v_V(trm)=(r a(m))_V(t)\). Conversely, given \(a\), set \(v_V(m)=a(m)_V(1)\) on opens containing \(x\), and set \(v_V=0\) on other opens. If \(V'\subset V\) does not contain \(x\), the restriction of \(a(m)_V(1)\) to \(V'\) is zero because \(a(m)\) is a map from \(x_*R\). If both opens contain \(x\), compatibility is the restriction compatibility of \(a(m)\). For \(b\in\mathcal O(V)\), writing \(\bar b\in R\),
\[
v_V(\bar b m)=(\bar b a(m))_V(1)=a(m)_V(\bar b)=b\,a(m)_V(1).
\]
Thus \(v\) is a module sheaf map. These constructions are inverse: for the second composite use \(a(tm)_V(1)=(t a(m))_V(1)=a(m)_V(t)\). They commute with maps in both variables. Lemma 5.2 supplies the first adjunction. Lemma 1.4 now proves that \(x_*\), as both a left and a right adjoint, preserves all existing limits and colimits.

Suppose now that \(x\) is closed. The image of every map \(x_*R\to F\) has zero stalks away from \(x\), so it factors through the displayed support kernel \(S\). The unit \(S\to x_*S_x\) is an isomorphism: at \(x\) it is the identity, and all other stalks are zero, since a point different from \(x\) has a neighborhood avoiding \(x\). Lemma 5.2 identifies maps \(x_*R\to x_*S_x\) with maps \(R\to S_x\), which are determined by the image of \(1\). This proves the identification, including its scalar action. \(\square\)

At the closed point \(c\) of the Sierpiński space in Section 6, a sheaf is a map \(M\xrightarrow{r}N\). Its stalk is \(M\), whereas its costalk is \(\ker r\): a map \((Q\to0)\to(M\to N)\) must land in that kernel. At the open point \(o\), a map \((Q\xrightarrow{1}Q)\to(M\to N)\) is determined by its component \(Q\to M\), so \(c_oF=M\) when the coefficient ring is constant. The stalk at \(o\) is \(N\). This explains why the two adjoints describe different information.

## 6. Three local and global computations

**Example 6.1 (the two-point space).** Let \(S=\{o,c\}\), with opens \(\varnothing,\{o\},S\). Fix any ring \(A\), and give \(S\) the constant coefficient sheaf \(A_S\). A module sheaf is exactly a homomorphism \(r:M\to N\) of left \(A\)-modules: its sections on \(S\) are \(M\), on \(\{o\}\) are \(N\), and the only nontrivial restriction is \(r\). Every covering of \(S\) contains \(S\), and the sheaf condition imposes no further restriction. The stalk at \(c\) is \(M\), since its only neighbourhood is \(S\); the stalk at \(o\) is \(N\). Kernels, cokernels and exactness are therefore computed componentwise.

For \(j:\{o\}\to S\), restriction sends \((M\to N)\) to \(N\), extension by zero sends \(Q\) to \((0\to Q)\), and direct image sends \(Q\) to \((Q\xrightarrow{1}Q)\). A section of \(j_!Q\) on \(S\) has support contained in \(\{o\}\); that subset is not closed in \(S\), so only the zero section is allowed. For the closed point, \(c_*Q=(Q\to0)\). For the open point, the skyscraper is \(o_*Q=(Q\xrightarrow{1}Q)\). Thus a skyscraper at a point need not have zero stalks at all other points. No closed-point assumption appeared in Lemma 5.2.

As a concrete cokernel, map \((A\xrightarrow{1}A)\) to \((A\to0)\) by the identity at \(c\) and zero at \(o\). Its kernel is \((0\to A)\), which is precisely \(j_!A\). This gives the short exact sequence

\[
0\to j_!A\to o_*A\to c_*A\to0.
\]

It records the open and closed pieces of this space without any separation hypothesis. In the lesson on supports the same space will make a localization triangle completely explicit.

**Example 6.2 (an endpoint quotient with no global lift).** First we prove the interval fact used in this example and below. Every nonempty real interval is connected. Indeed, suppose an interval \(I\) were the disjoint union of nonempty relatively open sets \(A,B\). Choose \(a\in A\), \(b\in B\), interchanging \((A,a)\) and \((B,b)\) if necessary so that \(a<b\). The whole segment \([a,b]\) lies in \(I\). By the least-upper-bound property of the real numbers, the nonempty bounded set \(A\cap[a,b]\) has a supremum \(s\). Openness near \(a\) gives a point of \(A\) greater than \(a\); openness near \(b\) excludes \(A\) from a segment ending at \(b\). Consequently \(a<s<b\). If \(s\in A\), openness gives a point of \(A\) greater than \(s\), contradicting the upper bound. If \(s\in B\), an open interval around \(s\) lies in \(B\), whereas the supremum property gives a point of \(A\) in its left half. Both alternatives are impossible. This proves connectedness. A locally constant map from an interval to any discrete set is therefore constant: the inverse image of any value and its complement are open, and two attained values would give a separation.

We will also use the consequence that the positive integers are unbounded in \(\mathbb R\). If they had a supremum \(s\), the supremum property would give a positive integer \(n>s-1\), and then \(n+1>s\), a contradiction. Thus for every \(\delta>0\) there is an integer \(N>1/\delta\), and \(1/n<\delta\) for all \(n\geq N\).

Now let \(X=[0,1]\), \(U=(0,1)\), \(D=\{0,1\}\), and let \(j:U\hookrightarrow X\), \(i:D\hookrightarrow X\) be the inclusions. The sheaf \(i_*\mathbb Z_D\) has one independent integer value at each endpoint contained in an open set. Evaluation at the endpoints gives a morphism of \(\mathbb Z_X\)-modules and an exact sequence
\[
0\longrightarrow j_!\mathbb Z_U
\longrightarrow\mathbb Z_X
\longrightarrow i_*\mathbb Z_D
\longrightarrow0.
\]
The first arrow is the extension-by-zero map of Lemma 5.1. At an interior point its stalk is the identity \(\mathbb Z\to\mathbb Z\), and the last stalk is zero. At either endpoint its source stalk is zero, and evaluation identifies the last two stalks with the identity of \(\mathbb Z\). These assertions about \(i_*\mathbb Z_D\) follow by taking a neighbourhood meeting only the chosen endpoint, or no endpoint at an interior point. Theorem 2.1 proves exactness of the displayed sheaf sequence.

By interval constancy, the global sections of \(\mathbb Z_X\) are \(\mathbb Z\). Those of \(i_*\mathbb Z_D\) are \(\mathbb Z^2\). Evaluation is the diagonal map \(n\mapsto(n,n)\), which cannot lift the section \((0,1)\). Thus the cokernel sheaf is zero even though the cokernel on global sections is nonzero.

**Example 6.3 (extension by zero at an endpoint).** Let \(X=[0,1]\), \(U=(0,1)\), and let \(\mathcal O_X\) be the sheaf of continuous real-valued functions. A global section of \(j_!\mathcal O_U\) is a continuous function on \(U\) whose support is closed in \(X\) and contained in \(U\). Because this closed support misses both endpoints, its complement is an open neighbourhood of each endpoint. Consequently the section vanishes on a neighbourhood of each endpoint. Conversely any such function extends by zero to a continuous function on \(X\): near each endpoint it is identically zero, and at interior points it is the original continuous function. Its support is closed in \(X\), since its complement is the union of the open sets where the extended function is zero on a neighbourhood, and it misses both endpoints. The constant function one on \(U\) is a section of \(j_*\mathcal O_U\), but not of \(j_!\mathcal O_U\) on \(X\). At either endpoint \(j_!\mathcal O_U\) has zero stalk; at an interior point it has stalk \(\mathcal O_x\). These stalks, rather than the global section module, give the later flatness calculation.

## 7. Exercises with complete solutions

The first two exercises test the exactness criteria. The next two compare constructions. The last two concern finiteness and topology.

**Exercise 1 (easy: an isomorphism criterion).** Show directly that a morphism of module sheaves with isomorphisms on all stalks has an inverse sheaf morphism. Explain why the inverse is module-linear.

**Solution.** If two sections have the same image, their germs have the same image at every point. Stalkwise injectivity makes their germs equal, hence the sections equal. Given a section \(t\) in the target, lift each of its germs, choose local representatives, and shrink until the image of each representative is \(t\) on that neighbourhood. On overlaps the representatives have the same image, so the just-proved injectivity makes them agree. They glue to a unique section in the source. These inverses commute with restriction by uniqueness. The inverse sends \(a t\) to \(a s\), because the forward map sends \(a s\) to \(a t\), again with a unique preimage. It preserves sums for the same reason. Thus it is a linear inverse sheaf morphism.

**Exercise 2 (medium: filtered and unfiltered colimits).** Prove exactness of filtered colimits of module sheaves. Then verify every arrow in the pushout counterexample in Section 1 and compute its three pushouts.

**Solution.** Stalks of a colimit are the colimits of the stalks by Theorem 3.1(2). For a diagram of short exact sequences, the stalk diagrams are exact by Theorem 2.1. Lemma 1.1 gives exactness after taking their filtered colimits. Theorem 2.1 then gives exactness of the sheaf sequence. In the counterexample, at the left object the sequence is \(0\to\mathbb Z\xrightarrow{1}\mathbb Z\to0\to0\), at the middle object it is \(0\to0\to\mathbb Z\xrightarrow{1}\mathbb Z\to0\), and at the right all terms vanish. The square for the arrow middle-to-left in the first morphism is \(0\to\mathbb Z\) followed by the identity on the left, and on the other side the zero inclusion followed by the identity middle-to-left; both composites from the zero group are zero. In the second morphism, both composites from the middle \(\mathbb Z\) to the last left object zero are zero. The middle-to-right squares are zero throughout. A module pushout of \(L\leftarrow M\to R\) is \((L\oplus R)/\{(a(m),-b(m)):m\in M\}\), as its universal property shows. This gives \(\mathbb Z\), \(0\) and \(0\). Thus the pushout functor does not preserve the displayed injection of diagrams.

**Exercise 3 (medium: extension by zero).** Given a map \(B\to G|_U\), construct its adjoint \(j_!B\to G\) on every open set. Show this construction gives the identity in both adjunction compositions, and deduce exactness of \(j_!\).

**Solution.** For \(s\in j_!B(V)\), glue its image on \(V\cap U\) with zero on \(V\setminus\operatorname{supp}s\). These sets cover \(V\), and the images agree on the intersection because \(s\) is zero there. Restriction commutes with gluing, as do sums and scalar multiplication. Restricting the resulting map to \(U\) recovers the original map, since \(j_!B|_U=B\). Starting with a map \(j_!B\to G\), the reconstructed section has the same restriction on \(V\cap U\) and is zero off the support; these are also the restrictions of the original image. Uniqueness of gluing recovers it. At a point of \(U\), the stalk functor of \(j_!\) is the identity; elsewhere it is zero. Both preserve exact sequences, so stalkwise exactness proves exactness of \(j_!\).

**Exercise 4 (medium: scalar extension).** For a homomorphism of possibly noncommutative rings \(A\to B\), write the unit and counit of \(B\otimes_A-\dashv\operatorname{Res}_A^B\). Check both triangle identities. Apply the formulas to the pullback adjunction in Theorem 4.4.

**Solution.** The unit is \(M\to\operatorname{Res}(B\otimes_A M)\), \(m\mapsto1\otimes m\). It is \(A\)-linear because \(1\otimes am=a\otimes m\), with \(a\) acting through \(A\to B\). The counit is \(B\otimes_A\operatorname{Res}N\to N\), \(b\otimes n\mapsto bn\), which is balanced and \(B\)-linear. The first composite sends \(b\otimes m\) to \(b\otimes(1\otimes m)\) and then to \(b\otimes m\). The second sends \(n\) to \(1\otimes n\) and then to \(n\). These verify the triangle identities. For sheaves the formulas hold on local tensor representatives and pass through sheafification. Compose with the inverse-image/direct-image adjunction: the pullback unit sends a section \(g\) over \(V\subset Y\) to \(1\otimes f^{-1}g\) over \(f^{-1}V\). The pullback counit sends a local tensor \(b\otimes s\), where \(s\) is locally represented by a section of \(f_*F\), to \(b\) times its restriction to the relevant open subset of \(X\). These are precisely the formulas in the proof of Theorem 4.4.

**Exercise 5 (hard: sections of an infinite direct sum).** Let \(X=\mathbb N\) be discrete, let \(A\ne0\) be a ring, and let \(F_n\) be the skyscraper \(A\) at \(n\). Compute \(\Gamma(X,\bigoplus_nF_n)\) and compare it with \(\bigoplus_n\Gamma(X,F_n)\).

**Solution.** A sheaf on a discrete space has sections on an open subset \(V\) equal to the product of its stalks at the points of \(V\). Indeed, the singleton opens cover \(V\), their intersections are empty, and the sheaf condition says that all choices of singleton sections glue uniquely. The direct sum sheaf has stalk \(A\) at each \(n\), since at that stalk only \(F_n\) is nonzero. Its sections on \(X\) are therefore \(\prod_nA\). In contrast \(\Gamma(X,F_n)=A\), so the sum of the global sections is \(\bigoplus_nA\). The canonical map is the inclusion of finitely supported sequences into all sequences, and is not onto: the sequence with every entry one is absent. The open \(X\) is not quasi-compact, as the singleton cover has no finite subcover. This does not contradict Theorem 3.1(5).

**Exercise 6 (hard: products need not preserve epimorphisms).** Let \(X=\mathbb R\), let \(k\) be a field, and put \(U_n=(-1/n,1/n)\), for \(n\geq1\). For each \(n\), extend the identity germ at zero to a morphism \(j_{n!}k_{U_n}\to0_*k\). Prove it is an epimorphism and show that the product of these maps is not an epimorphism.

**Solution.** By Lemma 5.2 a map to \(0_*k\) is determined by the map of stalks at zero. Choose the identity \(k\to k\). At zero it is onto; at every other point the target stalk is zero because zero is closed in \(\mathbb R\). Thus Theorem 2.1 makes it an epimorphism. Products are computed on sections. A germ at zero of a section of \(\prod_nj_{n!}k_{U_n}\) is represented on one common neighbourhood \(V\) of zero. Choose an open interval \(W\) containing zero inside \(V\). Each factor restricts to a locally constant function on the interval \(W\cap U_n\). The interval argument in Example 6.2, applied to the discrete set \(k\) in place of \(\mathbb Z\), makes it constant; its support is closed in \(W\). For every sufficiently large \(n\), the closure of \(U_n\) is contained in \(W\). A nonzero constant on \(U_n\) would have support \(U_n\), which is not closed in \(W\); hence that factor is zero. The images of the germ at zero thus have only finitely many nonzero coordinates. The target product sheaf has stalk \(\prod_nk\) at zero: on every neighbourhood of zero its sections are that product and all restrictions are identities. The germ with every coordinate one is not in the image. The product map is not onto on the stalk, hence is not an epimorphism. This argument uses one common neighbourhood for all factors; commuting a stalk with an infinite product would lose exactly that condition.

## References

- **[Stacks]** The Stacks project authors, *The Stacks project*, chapter *Sheaves of Modules*, [kernels and cokernels](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/modules.tex#L60), [the abelian category](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/modules.tex#L149), and [limits and colimits](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/modules.tex#L207), in the AI Integrated Stacks Project edition. Stacks-derived material retains GFDL-1.2-or-later; the edition is an unofficial AI-integrated derivative.
