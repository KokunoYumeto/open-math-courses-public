# Stacks in groupoids

*Algebraic spaces and stacks, Lesson 4 of 12.*

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

## Introduction

An algebraic space records families through a sheaf of sets. A stack records both families and their isomorphisms. This distinction matters even when the set of geometric isomorphism classes is small. A line bundle is locally trivial, but its transition functions carry information that disappears if one remembers only that local isomorphism class. Similarly, a quotient with a fixed point should remember the group that fixes it.

The basic objects and pullback conventions come from *Fibred categories and descent data*. We use its definitions of a category fibred in groupoids, cartesian arrows, a cleavage and descent data. The work here begins with the sheaves of isomorphisms and constructs the additional objects needed to make descent effective. Our main examples will then explain why these objects are torsors. Finally, a gerbe separates two questions: whether objects exist locally, and whether those local objects can be assembled into a global one.

Unless another site is specified, stacks are over the big fppf site of schemes over a scheme \(S\). In the general construction, \(\mathcal C\) is a site with the usual covering-family convention: pullbacks of covering arrows exist, and compositions and common refinements are coverings. One can equally use covering sieves. We work in fixed universes, allowing a larger universe for categories of families.

## 1. Isomorphisms and descent

Let \(\mathcal X\to\mathcal C\) be fibred in groupoids. For \(x,y\in\mathcal X(U)\), define a presheaf on \(\mathcal C/U\) by

\[
\operatorname{Isom}_{\mathcal X}(x,y)(v:V\to U)
=\operatorname{Isom}_{\mathcal X(V)}(v^*x,v^*y).
\tag{1.1}
\]

Restrictions use the canonical comparisons between successive pullbacks. Their coherence makes (1.1) a presheaf. Changing the chosen pullbacks gives a canonical isomorphism of presheaves: compare the two cartesian lifts, then conjugate an isomorphism by those comparisons. The uniqueness in the cartesian lifting property makes these comparisons compatible with restriction and composition. Thus the sheaf condition is independent of the cleavage.

A **prestack in groupoids** is a category fibred in groupoids for which every presheaf (1.1) is a sheaf. A **stack in groupoids** is a prestack in which every descent datum for objects is effective. Equivalently, for every covering \(\{U_i\to U\}\), restriction gives an equivalence

\[
\mathcal X(U)\longrightarrow
\operatorname{Desc}_{\mathcal X}(\{U_i\to U\}).
\tag{1.2}
\]

Full faithfulness of (1.2) is the sheaf condition for isomorphisms; essential surjectivity is effective descent for objects. These are [Stacks, Tags 02Z9, 02ZC and 02ZH]. Here “prestack” means the sheaf condition for isomorphisms. Behrend's topological notes use a stronger convention, requiring a representable diagonal; see *Introduction to algebraic stacks*, Remark 2.11. We do not build that additional requirement into the word.

Write \(U_{ij}=U_i\times_U U_j\), and suppress canonical pullback comparisons. A descent datum consists of objects \(x_i\in\mathcal X(U_i)\) and isomorphisms

\[
\phi_{ij}:x_i|_{U_{ij}}\longrightarrow x_j|_{U_{ij}},
\qquad
\phi_{jk}\phi_{ij}=\phi_{ik}\ \text{on }U_{ijk}.
\tag{1.3}
\]

The restriction of \(\phi_{ii}\) to the diagonal \(U_i\to U_{ii}\) is the identity. For a general fppf cover, the two projections \(U_{ii}\rightrightarrows U_i\) differ, so this does not say that the entire self-overlap isomorphism is an identity. This distinction will be essential in the construction below.

### 1.1. Setoids and sheaves

A groupoid is a **setoid** if there is at most one arrow between any two objects. Its automorphism groups are trivial, but isomorphic objects need not be literally equal.

**Proposition 1.1.** A stack in setoids is equivalent, over its site, to the discrete fibred category associated with a sheaf of sets.

**Proof.** Put \(F(U)=\pi_0(\mathcal X(U))\), the set of isomorphism classes. Suppose classes \([x_i]\in F(U_i)\) agree on overlaps. Their representatives admit isomorphisms \(\phi_{ij}\), because equality of classes means isomorphism in the overlap groupoid. Those isomorphisms are unique. Their uniqueness gives the cocycle, so effective descent produces \(x\in\mathcal X(U)\) with the prescribed local classes.

For uniqueness, suppose \(x,y\in\mathcal X(U)\) have equal local classes. Their unique local isomorphisms agree on overlaps, and the sheaf \(\operatorname{Isom}(x,y)\) glues them to an isomorphism over \(U\). Hence \(F\) is a sheaf. The functor sending an object to its class is fully faithful: its target has one arrow precisely when the two classes coincide, which is precisely when the source has its unique arrow. It is essentially surjective by the definition of \(F(U)\). It respects pullbacks and therefore is an equivalence over the site.

Conversely, for a sheaf \(F\), regard \(F(U)\) as a discrete groupoid. Compatible local objects glue uniquely by the sheaf axiom, and isomorphisms are identities. This is a stack in setoids. \(\square\)

*Reference:* [Stacks, Tag 042Y].

### 1.2. Inertia

The **inertia stack** \(I_{\mathcal X}\) of a stack \(\mathcal X\) has objects

\[
(x,\alpha),\qquad x\in\mathcal X(U),\quad
\alpha\in\operatorname{Aut}_{\mathcal X(U)}(x).
\]

An arrow \(u:(x,\alpha)\to(y,\beta)\) is an arrow of \(\mathcal X\) satisfying \(u\alpha=\beta u\), with the understood pullbacks if the base changes. It is again a stack. Indeed, local objects \(x_i\) descend in \(\mathcal X\). The compatibility of the \(\alpha_i\) then makes them a section of the sheaf of automorphisms of the descended object, so they glue uniquely. Isomorphisms of pairs form the subsheaf of \(\operatorname{Isom}(x,y)\) on which \(u\alpha=\beta u\); equality of these two composites can be checked locally.

The map \(I_{\mathcal X}\to\mathcal X\) therefore records the automorphisms of each family, compatibly with base change. It is also the 2-fibre product of the two copies of the diagonal \(\mathcal X\to\mathcal X\times\mathcal X\): a triple \((x,y,\alpha_1,\alpha_2)\) identifies, by \(\alpha_1\), with \(x\) and the automorphism \(\alpha_1^{-1}\alpha_2\). This gives an equivalence, including arrows, by the same conjugation rule. See [Stacks, Tag 036X].

## 2. Constructing stackification

The construction has two stages. First replace locally specified isomorphisms by actual isomorphisms. Then add objects specified by descent data. Keeping these stages separate prevents an ineffective descent datum from being mistaken for an existing object.

**Theorem 2.1.** Every category \(\mathcal X\) fibred in groupoids over a site has a stackification \(\eta:\mathcal X\to a\mathcal X\). For every stack in groupoids \(\mathcal H\), precomposition gives an equivalence of groupoids

\[
\eta^*:
\operatorname{Hom}_{\mathcal C}(a\mathcal X,\mathcal H)
\ \simeq\
\operatorname{Hom}_{\mathcal C}(\mathcal X,\mathcal H).
\tag{2.1}
\]

Here objects of a Hom groupoid are functors over \(\mathcal C\), and its arrows are natural transformations whose components lie over identity base maps. In particular the universal property includes natural transformations, not just the existence of an extended functor.

### 2.1. First stage: make isomorphisms into sheaves

**Proof, first stage.** Keep the objects of \(\mathcal X(U)\), and replace its Hom set between \(x\) and \(y\) by

\[
\operatorname{Hom}_{P\mathcal X(U)}(x,y)
=a\operatorname{Isom}_{\mathcal X}(x,y)(U),
\tag{2.2}
\]

where \(a\) on the right denotes ordinary sheafification on \(\mathcal C/U\). A section of this sheaf is locally represented by original arrows; two representatives define the same section exactly when they agree after a further cover. Given two composable sections, represent both on a common cover, compose their representatives there, and glue the resulting sections. Different representatives give the same answer after refinement, hence the same glued section. Associativity, identities and inverses follow by representing all the arrows on a common cover and using those identities in \(\mathcal X\). Thus each fibre in (2.2) is a groupoid.

Restriction to a slice commutes with this sheafification: both sheaves have locally the same representatives and the same local equality relation. Consequently pullback functors and their comparison isomorphisms extend to (2.2). Their coherences hold locally and hence hold in the sheafified Hom sets. Forming the category from these groupoids and pullback functors gives a category \(P\mathcal X\) fibred in groupoids and a functor \(j:\mathcal X\to P\mathcal X\). Its Isom presheaves are sheaves, so it is a prestack.

If \(\mathcal H\) is a prestack, any functor \(F:\mathcal X\to\mathcal H\) extends to \(P\mathcal X\). On each Hom sheaf, send local representatives to their images under \(F\) and glue in \(\operatorname{Isom}_{\mathcal H}(F(x),F(y))\). The result is unique, and its compatibility with composition and restriction is checked on those representatives. A natural transformation between two such functors extends with the same components on objects; its naturality for sheafified arrows holds locally. Conversely the objects of \(P\mathcal X\) are the original objects, so a transformation is determined by its restriction. This proves

\[
\operatorname{Hom}(P\mathcal X,\mathcal H)
\simeq \operatorname{Hom}(\mathcal X,\mathcal H)
\quad\text{for every prestack }\mathcal H.
\tag{2.3}
\]

### 2.2. Second stage: add descent objects

Put \(\mathcal P=P\mathcal X\). An object of \(a\mathcal X(U)\) is a formal presentation

\[
A=(\{U_i\to U\},\,x_i,\,\phi_{ij})
\tag{2.4}
\]

with \(x_i\in\mathcal P(U_i)\) and descent isomorphisms (1.3). We retain presentations as objects rather than identifying them by an unproved assertion about a category of refinements.

If \(B=(\{V_j\to U\},y_j,\psi_{jj'})\), an arrow \(A\to B\) is a family

\[
a_{ij}:x_i|_{U_i\times_U V_j}
\longrightarrow y_j|_{U_i\times_U V_j}
\tag{2.5}
\]

satisfying the two compatibility conditions

\[
a_{i'j}\phi_{ii'}=a_{ij},
\qquad
\psi_{jj'}a_{ij}=a_{ij'}.
\tag{2.6}
\]

The first equality is read on \(U_i\times_U U_{i'}\times_U V_j\), and the second on \(U_i\times_U V_j\times_U V_{j'}\). These conditions include self-overlaps. They compare the two ways of expressing the same isomorphism in different local coordinates.

To compose \(A\to B\to C\), with \(C\) presented over \(\{W_k\to U\}\), use the arrows \(b_{jk}a_{ij}\) on \(U_i\times_U V_j\times_U W_k\). For fixed \(i,k\), these agree over the overlaps in the covering indexed by \(j\): equation (2.6) for \(a\) contributes \(\psi_{jj'}\), and the corresponding equation for \(b\) cancels it. The Isom sheaf of \(\mathcal P\) therefore glues them uniquely to \(c_{ik}\) on \(U_i\times_U W_k\). Its two compatibility conditions follow after pullback to the same cover, where they are (2.6) for \(a\) and \(b\).

The identity of \(A\) has components \(\phi_{ii'}\). An inverse of (2.5) has components \(a_{ij}^{-1}\), with the source and target indices interchanged; equations (2.6) give its compatibilities. The composites are the identity families because this can be checked after pulling back to the common cover. For three arrows, the two parenthesizations of their composite agree on the cover using all four presentations, where they are the same composite in \(\mathcal P\). Sheaf uniqueness proves associativity. Thus \(a\mathcal X(U)\) is a groupoid.

Pull back presentations, their covers and their arrows along a base map. The canonical comparisons for pullbacks in \(\mathcal P\) induce comparisons here; the identity and associativity constraints hold because they hold on all the component objects and arrows. We have therefore constructed a category fibred in groupoids. The identity cover gives a functor \(i:\mathcal P\to a\mathcal X\), fully faithful on every fibre: (2.5) for two identity-cover presentations is exactly an arrow of \(\mathcal P(U)\).

Every presentation \(A\) is locally in this functor's image. Over \(U_i\), the arrows \(\phi_{ij}\) give an isomorphism

\[
i(x_i)\ \simeq\ A|_{U_i}.
\tag{2.7}
\]

The self-overlap parts of the descent datum are included in this assertion.

### 2.3. Verify the stack axioms

The presheaf of arrows between two fixed presentations is a sheaf. To see this, take locally given families (2.5) that agree on an additional cover of \(U\). Each component glues in its Isom sheaf on \(U_i\times_U V_j\). Their compatibility equations hold locally and hence globally. The glued family is unique component by component.

For effective descent, let \(\{T_a\to T\}\) be a cover and let \(A_a\) be formal presentations over \(T_a\), with compatible isomorphisms
\(\sigma_{aa'}:A_a|_{T_{aa'}}\to A_{a'}|_{T_{aa'}}\).
Present \(A_a\) on a cover \(\{T_{ab}\to T_a\}\). By (2.7), over each \(T_{ab}\) it is identified with \(i(x_{ab})\) for an object \(x_{ab}\) of \(\mathcal P\).

Transport \(\sigma_{aa'}\) through these identifications. Full faithfulness of \(i\) turns it into an actual arrow of \(\mathcal P\) on every
\(T_{ab}\times_T T_{a'b'}\). The cocycle for \(\sigma\) gives the cocycle for these arrows, again by full faithfulness. Their diagonal restrictions are identities. They consequently form one presentation over the composite cover \(\{T_{ab}\to T\}\), which is a cover by the site axioms.

Its restrictions recover the \(A_a\) and the specified \(\sigma_{aa'}\), using the same component arrows. This proves effectivity. The preceding sheaf argument gives full faithfulness for descent. Therefore \(a\mathcal X\) is a stack.

### 2.4. Verify the entire universal property

Let \(F:\mathcal P\to\mathcal H\), with \(\mathcal H\) a stack. For a presentation (2.4), the objects \(F(x_i)\) and the images of the \(\phi_{ij}\), using the pullback comparisons for \(F\), form a descent datum in \(\mathcal H\). Choose its effective object \(\overline F(A)\), together with its descent identifications.

An arrow (2.5) gives an arrow between the two image descent data. Full faithfulness of descent in \(\mathcal H\) gives a unique arrow between their effective objects. Composition and identities are preserved because the restrictions of both proposed arrows coincide. The pullback comparison
\(\overline F(A)|_V\simeq\overline F(A|_V)\)
is likewise the unique isomorphism with the prescribed identifications on the pulled-back cover. The two comparisons for a composite base map agree locally with those for \(F\); uniqueness gives their coherence. These choices thus define a functor over the site, together with a natural isomorphism \(\overline F i\simeq F\).

If \(\tau:F\Rightarrow G\), its local components \(\tau_{x_i}\) respect the image descent data by naturality for \(\phi_{ij}\). They descend to a unique component
\(\overline F(A)\to\overline G(A)\).
Naturality follows locally from that for \(\tau\), and hence holds globally. Conversely, a natural transformation between two functors \(a\mathcal X\to\mathcal H\) is determined by its components on \(i(\mathcal P)\), since (2.7) covers every object and the target Isom presheaves are sheaves. Every transformation on that restriction extends by the gluing just described. Precomposition by \(i\) is therefore fully faithful and essentially surjective on Hom groupoids.

Combining this result with (2.3) proves (2.1), for \(\eta=ij\). It also proves uniqueness of stackification as a stack with its unit: compare two constructions by applying (2.1) to their units, then compare the composites with the identity functors. The required 2-isomorphisms are unique once their restrictions to the specified units are fixed. No assertion of uniqueness without those restrictions is needed. \(\square\)

*References:* [Stacks, Tags 02ZM, 0435, 04W9, 02ZO and 0436]. The proof explicitly constructs the arrows between presentations and verifies effectivity and the universal property on natural transformations.

### 2.5. Restriction and change of topology

Restricting a stack to \(\mathcal C/U\) gives a stack: covers and descent data there are precisely the corresponding covers and data with a specified map to \(U\). The construction above commutes with this restriction up to its unit-preserving equivalence, since its representatives, sheafified arrows and descent presentations are the same on that slice.

There is a second, related localization statement. If \(h_U\) is a sheaf, a stack over \(\mathcal C/U\), regarded by composition as a category over \(\mathcal C\), is a stack with a map to \(h_U\). For descent over \(V\in\mathcal C\), first glue the compatible maps \(V_i\to U\) using \(h_U\), then descend the objects over the resulting object \(V\to U\) of the slice. Isomorphisms descend in the same slice. Conversely a stack over \(\mathcal C\) with a map to \(h_U\) is a stack over \(\mathcal C/U\), since that specified map is preserved in every descent datum. These operations preserve functors and natural transformations and undo one another. This proves the localization correspondence of [Stacks, Tag 04WT]. Without the sheaf hypothesis, the represented category \(\mathcal C/U\) itself need not be a stack.

A fibred category \(\mathcal P\to\mathcal C\) also inherits a topology: a covering is a family of cartesian arrows whose base maps form a covering in \(\mathcal C\). Identities and composition satisfy the cover axioms because cartesian arrows do. To pull a cover back along \(y\to x\), pull each base cover map back and choose its cartesian lift into \(y\). The cartesian universal property identifies this lift with the fibre product over \(x\). Thus these are indeed the covers of a site. If \(\mathcal P\) is fibred in groupoids, all its arrows are cartesian. Moreover, for \(x\) over \(U\), the site \(\mathcal P/x\) is equivalent to \(\mathcal C/U\): cartesian lifts give essential surjectivity and unique arrows over any slice arrow give full faithfulness, with identical covers. This is the inherited topology of [Stacks, Tag 06NT].

Suppose two topologies on the same category are ordered, with \(\tau'\) having more covering families than \(\tau\). A \(\tau'\)-stack is automatically a \(\tau\)-stack. A \(\tau\)-stack can be stackified for \(\tau'\) by Theorem 2.1, universally among maps to \(\tau'\)-stacks. In particular an étale stack need not already have fppf descent. For a functor between sites that sends covers and their overlap diagrams to covers and overlap diagrams, composing a stack's pullback groupoids with that functor produces a stack by (1.2). This is the elementary change-of-site case in [Stacks, Tag 04WA]. We will not use its more general inverse-image construction.

## 3. Objects as maps: the 2-Yoneda lemma

For \(U\in\mathcal C\), the category \(\mathcal C/U\to\mathcal C\) is the category fibred in sets represented by \(U\).

**Lemma 3.1 (2-Yoneda).** For any category \(\mathcal X\) fibred in groupoids, evaluation at \(1_U:U\to U\) is an equivalence

\[
\operatorname{Hom}_{\mathcal C}(\mathcal C/U,\mathcal X)
\ \simeq\ \mathcal X(U).
\tag{3.1}
\]

This does not require a stack condition.

**Proof.** For \(x\in\mathcal X(U)\), choose cartesian pullbacks \(v^*x\) for maps \(v:V\to U\). For an arrow \(h:(W,w)\to(V,v)\) of the slice, the cartesian property gives the unique arrow \(w^*x\to v^*x\) over \(h\) compatible with their arrows to \(x\). Uniqueness makes this assignment a functor \(F_x\) over \(\mathcal C\). Choose the identity pullback so \(F_x(1_U)=x\). Evaluation is essentially surjective.

For any functor \(F\) over \(\mathcal C\), the arrow from \(F(v)\) to \(F(1_U)\) is cartesian, since every arrow in a category fibred in groupoids is cartesian. It therefore gives a canonical comparison
\(F(v)\simeq v^*F(1_U)\), compatible with all arrows of the slice. Given
\(\alpha:F(1_U)\to G(1_U)\), transport \(v^*\alpha\) through these comparisons to define a natural transformation \(F\Rightarrow G\). Naturality follows from the uniqueness of arrows into the chosen cartesian pullbacks.

Conversely, naturality along the slice arrow \(v\to1_U\) forces a transformation's component at \(v\) to be exactly this transported pullback of its component at \(1_U\). Thus evaluation is bijective on every Hom set and proves (3.1). \(\square\)

*Reference:* [Stacks, Tag 04SS]. Specifying the component at \(1_U\) matters: if \(x\) has nontrivial automorphisms, \(F_x\) has corresponding nontrivial natural automorphisms.

### 3.1. Representable morphisms

For \(f:\mathcal X\to\mathcal Y\) and \(y\in\mathcal Y(U)\), use (3.1) to form the 2-fibre product \(U\times_{\mathcal Y}\mathcal X\). Over \(v:V\to U\), its objects are pairs

\[
(x,\alpha),\qquad x\in\mathcal X(V),\quad
\alpha:v^*y\xrightarrow{\sim}f(x).
\tag{3.2}
\]

An arrow from \((x,\alpha)\) to \((x',\alpha')\) over the identity is an isomorphism \(h:x\to x'\) satisfying \(f(h)\alpha=\alpha'\). The definition along a base map uses the same equality with pullbacks.

The morphism \(f\) is **representable by schemes**, or **representable by algebraic spaces**, if (3.2) is equivalent to the discrete fibred category of a scheme, or an algebraic space, over \(U\), for every scheme \(U\) and every \(y\). These two meanings are distinct. A scheme base change is an ordinary space only after this representability has been proved. See [Stacks, Tag 04ST].

Representability is preserved by base change: testing an object of the new target just gives the original fibre (3.2), with its map to the testing scheme. It is preserved by composition as well. If \(f\) and \(g\) are representable and \(U\to\mathcal Z\) is a scheme test for \(gf\), first form \(V=U\times_{\mathcal Z}\mathcal Y\). If both morphisms are representable by schemes, \(V\) is a scheme and the second fibre is a scheme by definition. For algebraic spaces, choose an étale scheme atlas of \(V\); the second fibre is represented over that atlas and its overlaps, and its étale descent is an algebraic space by the quotient construction of Algebraic spaces. Thus \(U\times_{\mathcal Z}\mathcal X\) is an algebraic space in this case too.

The diagonal has a particularly useful test. Its base change by two objects \(x,y\in\mathcal X(U)\) is the discrete fibred category of \(\operatorname{Isom}_{\mathcal X}(x,y)\). Indeed, a diagonal-fibre object is an object \(z\) with isomorphisms to \(x\) and \(y\); their composite determines an isomorphism \(x\to y\). Conversely such an isomorphism gives this object with \(z=x\). Arrows between two descriptions are unique precisely when the composites agree. Hence a representable diagonal says that all these Isom sheaves are represented by spaces or schemes. It says more than the prestack axiom.

## 4. Torsors and quotient stacks

Let \(G\) be a sheaf of groups on a site. A **right \(G\)-torsor** \(P\) is a sheaf with a right action such that it is locally isomorphic to \(G\) with its right multiplication action. Equivalently, \(P\) is locally nonempty and

\[
P\times G\longrightarrow P\times P,\qquad
(p,g)\longmapsto(p,pg)
\tag{4.1}
\]

is an isomorphism of sheaves. To prove the equivalence, a local section \(p\) makes \(g\mapsto pg\) an isomorphism by (4.1); conversely (4.1) is an isomorphism on any trivializing cover and hence globally. Torsors here are sheaves; representability is a separate conclusion when \(G\) is algebraic.

**Lemma 4.1.** Right \(G\)-torsors, with equivariant isomorphisms and pullbacks, form a stack.

**Proof.** An equivariant map between torsors is an isomorphism: locally choose sections in both torsors, where the map is left multiplication by a group section, with inverse multiplication by its inverse. Such maps form a sheaf, since maps between sheaves glue and equivariance is an equality checked locally.

Given torsors \(P_i\) and equivariant descent isomorphisms over a cover \(\{U_i\to U\}\), construct their glued sheaf explicitly. Over \(V\to U\), its sections are families of sections of \(P_i\) on \(V\times_U U_i\), agreeing under the given identifications on all pairwise overlaps. These compatible families form a sheaf, by the sheaf conditions of the \(P_i\). Its restriction to \(U_i\) is \(P_i\): from a section of \(P_i\), use the descent isomorphisms to obtain the compatible family on the pulled-back cover; conversely take its \(i\)-component along the diagonal and use the compatibility equations. These two operations are inverse by the descent cocycle.

The componentwise action glues to an action on this sheaf. The identity and associativity equations hold locally, and so does (4.1). A composite of the given cover with trivializing covers of the \(P_i\) provides local sections. The glued sheaf is therefore a torsor and realizes the prescribed descent datum. The sheaf of maps proved above gives full faithfulness. \(\square\)

*References:* [Stacks, Tags 036Z and 04UJ].

### 4.1. Why algebraic torsors are algebraic spaces

**Lemma 4.2.** Let \(G\) be a group algebraic space over a scheme \(T\). Every fppf sheaf torsor under \(G\) is represented by an algebraic space over \(T\). No flatness or finite-presentation hypothesis on \(G\to T\) is required.

**Proof.** First assume \(T\) affine. Refine a trivializing fppf cover by affine schemes. The images of these flat locally finitely presented maps are open. Quasi-compactness of \(T\) therefore allows finitely many of them, \(W_1,\ldots,W_r\), still covering \(T\). Put \(W=\coprod W_i\). The sheaf

\[
Q=P\times_T W\simeq G\times_T W
\]

is an algebraic space. For every scheme \(Z\to P\),
\(Z\times_P Q=Z\times_T W\) is a scheme. Thus \(Q\to P\) is representable, flat, locally of finite presentation and surjective, because it is the base change of \(W\to T\). The flat bootstrap theorem of The bootstrap theorem, Section 4, says exactly that a sheaf with such an algebraic-space cover is an algebraic space. It applies to \(P\).

For general \(T\), use affine open subsets of \(T\). The spaces just obtained on them agree on overlaps because they represent the same restricted sheaf. Their open-subspace gluing, proved in Algebraic spaces, gives the required algebraic space over \(T\). \(\square\)

This also proves effective descent for algebraic fppf torsors: Lemma 4.1 glues the sheaf torsor, and Lemma 4.2 represents it. Compare [Stacks, Tags 04UR and 04U1]. Here fppf refers to the covers trivializing the torsor. The morphism \(P\to T\) inherits properties of \(G\to T\), so it need not itself be flat when \(G\) is not flat.

For clarity about [Stacks, Tag 04UN], a principal homogeneous algebraic \(G\)-space means an algebraic space locally isomorphic to \(G\) for the fpqc topology. If \(G\to T\) is flat and locally of finite presentation, such a space \(P\to T\) is flat, locally of finite presentation and surjective by fpqc descent of these properties. An étale scheme atlas \(W\to P\) then gives an fppf cover \(W\to T\) on which the torsor has a section, hence is trivial. Under these additional hypotheses the fpqc and fppf torsor descriptions agree. We do not use this assertion to impose those hypotheses in the next theorem.

### 4.2. The torsor description of a quotient

Let \(B\) be an algebraic space over \(S\), let \(G\) be a group algebraic space over \(B\), and let \(X\to B\) be an algebraic space with a left action of \(G\). The **action prestack** \(\mathcal A\) has, over a scheme \(T\), objects \(x:T\to X\). An arrow over the identity from \(x\) to \(x'\) is a section \(g\) of \(G_T\) such that \(x'=gx\). Here \(G_T\) uses their common map \(T\to B\); if the maps to \(B\) differ, there is no arrow. Composition is multiplication in the order

\[
x\xrightarrow{g}gx\xrightarrow{h}hgx.
\tag{4.2}
\]

These arrow presheaves are sheaves, since they are fibres of maps of fppf sheaves. Thus \(\mathcal A\) is a prestack. Define \([X/G]\) as its fppf stackification.

**Theorem 4.3.** The stack \([X/G]\) is equivalent to the following stack \(\mathcal Q\). An object over \(T\) is a map \(b:T\to B\), a right fppf \(G_T\)-torsor \(P\), and a map of algebraic spaces \(\varphi:P\to X\) over \(B\) satisfying

\[
\varphi(pg)=g^{-1}\varphi(p).
\tag{4.3}
\]

An isomorphism is a \(G_T\)-equivariant torsor isomorphism commuting with \(\varphi\), and pullbacks give the arrows over base maps.

**Proof.** First \(\mathcal Q\) is a stack. Compatible local maps to \(B\) glue because \(B\) is an fppf sheaf. Lemma 4.1 glues the torsors, and Lemma 4.2 represents the result, applied to the group space \(G_T\) over the testing scheme \(T\). Maps from the glued torsor to \(X\) glue as maps of sheaves, using the same compatible-family construction. Equality (4.3) is checked locally. Isomorphisms form a sheaf by Lemma 4.1 with the additional equality for \(\varphi\) checked locally.

Send an action-prestack object \(x\) to the trivial right torsor \(G_T\) with
\(\varphi_x(h)=h^{-1}x\). Send \(g:x\to x'=gx\) to the torsor map \(h\mapsto gh\). It commutes with the maps to \(X\), since
\((gh)^{-1}x'=h^{-1}g^{-1}gx=h^{-1}x\).
It preserves (4.2). An equivariant map between trivial right torsors has the form \(h\mapsto gh\), uniquely determined by its value at the identity. Commutation with \(\varphi\) says exactly \(x'=gx\). This proves full faithfulness on every Isom sheaf of \(\mathcal A\).

Theorem 2.1 extends this functor to \(F:[X/G]\to\mathcal Q\). Objects of \([X/G]\) are locally action-prestack objects by construction, so the map on Isom sheaves of any two objects can be tested on a common such cover. There it is the isomorphism just proved for trivial torsors. A map of sheaves which is locally an isomorphism is an isomorphism, so \(F\) is fully faithful.

Every object \((P,\varphi)\) of \(\mathcal Q(T)\) admits local sections \(p_i\) on an fppf cover. Put \(x_i=\varphi(p_i)\). If \(p_j=p_i h_{ij}\) on the overlap, (4.3) gives \(x_j=h_{ij}^{-1}x_i\). The torsor identities give
\(h_{ij}h_{jk}=h_{ik}\); hence \(g_{ij}=h_{ij}^{-1}\) satisfies
\(g_{jk}g_{ij}=g_{ik}\), the descent convention (1.3) and (4.2). The \(x_i\) and \(g_{ij}\) descend in \([X/G]\). Their trivial torsors descend to \(P\), with the specified map \(\varphi\), by the transition equations. Thus \(F\) is essentially surjective. It is an equivalence of stacks. \(\square\)

*References:* [Stacks, Tags 04UI, 04UV and 04WM]. Replacing right torsors and (4.3) by left torsors and ordinary equivariance gives the equivalent left-action convention.

**Corollary 4.4.** If the action is free as an action of fppf sheaves, then \([X/G]\) is equivalent to the fppf sheaf quotient \(X/G\).

**Proof.** Freeness means that \((g,x)\mapsto(x,gx)\) is a monomorphism, so an action-prestack object has no nonidentity automorphism. Every quotient-stack object is locally such an object; its automorphism sheaf is therefore trivial. All the quotient-stack fibres are setoids: two arrows with the same endpoints differ by an automorphism. Proposition 1.1 identifies this stack with the sheaf \(F(T)=\pi_0(X/G)\).

Its objects are locally images of sections of \(X\); two such sections have equal classes exactly when, locally, they are related by a section of \(G\). Thus \(F\) is the sheafification of the orbit presheaf, which is the sheaf quotient \(X/G\). This proves the asserted equivalence. \(\square\)

The hypothesis is freeness on all scheme tests, including nilpotent tests. Freeness only on geometric points would not justify the conclusion.

### 4.3. Two examples

The **classifying stack** \(BG=[S/G]\), for the trivial action on \(S\), is the stack of \(G\)-torsors by Theorem 4.3. For a finite abstract group, its constant group scheme is finite étale, in every characteristic. Its torsors are therefore finite étale covers of degree \(|G|\) with a simply transitive right action: this is true after trivialization and descends. Over an algebraically closed field every such torsor has a rational point and is trivial. The fibre groupoid is nevertheless not a one-element set; the automorphism group of the trivial right torsor is \(G\), acting by left multiplication.

For scalar multiplication on \(\mathbb A^1\), Theorem 4.3 identifies
\(\mathbb A^1/\mathbb G_m\) with pairs \((L,s)\), a line bundle and a global section. Indeed, the frame torsor of \(L\) is a right \(\mathbb G_m\)-torsor: multiplying a frame \(p\) by \(g\) multiplies its basis by \(g\). The coordinate of \(s\) in that frame satisfies
\(\varphi(pg)=g^{-1}\varphi(p)\).
Conversely, trivialize a torsor and use its transition functions to glue rank-one free modules. The values of \(\varphi\) transform by the inverse transition functions, exactly as section coordinates do, so they glue a section of the resulting line bundle. These operations also identify all isomorphisms and undo one another.

Over an algebraically closed field, there are two isomorphism classes: the zero section and a nonzero section. The first has automorphism group \(\mathbb G_m\), and the second has trivial automorphism group. The open substack where the section is nowhere vanishing is a point over the base: the section itself uniquely trivializes \(L\). The substack with zero section is \(B\mathbb G_m\). Over a general scheme \(T\), pairs \((L,s)\) include nontrivial line bundles and varying zero loci, so the two-class description is a geometric-point description only.

## 5. Modules, covers and line bundles

The fppf stack of quasi-coherent modules in groupoids has objects \((T,M)\), with \(M\) quasi-coherent on \(T\), and arrows over \(v:T'\to T\) given by isomorphisms \(M'\simeq v^*M\). Effective fpqc descent for quasi-coherent modules [Stacks, Tag 023T] gives effective descent here, and its full faithfulness gives the sheaf condition for Isom. Indeed, compatible local maps descend uniquely as module maps, and if each is invertible, their local inverses descend and prove that the resulting map is invertible.

Allowing all module homomorphisms instead gives a stack in categories, with noninvertible arrows in its fibres. It is not a stack in groupoids. The groupoid just described is its subcategory of cartesian arrows. This is the relevant groupoid version of [Stacks, Tag 03YL], with any necessary enlargement of universe understood. We are proving descent here, not asserting algebraicity of this unrestricted moduli problem.

The same reasoning gives the stack of finite étale covers, with isomorphisms of covers. For effectivity on an affine base, a finite cover is the spectrum of a finite locally free algebra. Descend its underlying module by [Stacks, Tag 023T], and descend its unit and multiplication by full faithfulness. The algebra identities hold after faithful flat pullback and hence hold in the descended algebra. Finite local freeness descends [Stacks, Tag 05B2]. Its spectrum is the descended finite cover; étaleness descends [Stacks, Tag 02VN]. On a nonaffine base these affine constructions glue, since their algebra identifications are unique. Morphisms of the algebras descend by the same full faithfulness, including their inverses when they are isomorphisms. This proves both stack axioms. As with modules, retaining all maps of finite étale covers gives a stack in categories rather than in groupoids. See [Stacks, Tag 0BLY].

### 5.1. The Picard stack

Let \(X\to B\) be any morphism of algebraic spaces over \(S\). The **Picard stack** \(\mathcal{Pic}_{X/B}\) has, over \(T\), a map \(b:T\to B\) and a line bundle \(L\) on \(X_T=T\times_B X\). Arrows are the isomorphisms of line bundles compatible with base change.

It is an fppf stack. To give the effectivity argument for arbitrary algebraic spaces explicitly, compatible local maps \(T_i\to B\) first glue to \(b\). Their line bundles have descent data for the fppf cover \(X_{T_i}\to X_T\). Choose an étale scheme atlas \(V\to X_T\). Pulling these data to \(V\) gives fppf descent data for modules on a scheme, so [Stacks, Tag 023T] produces a quasi-coherent module \(M_V\). On \(R=V\times_{X_T}V\), the two pullbacks of \(M_V\) have the same local identifications with the original line-bundle data. Full faithfulness of scheme module descent gives a unique comparison between them. Its cocycle follows after fppf pullback, again by full faithfulness.

The quasi-coherent descent theorem proved in Properties and morphisms of algebraic spaces, Theorem 2.1, now gives \(M\) on \(X_T\). Locally on \(V\), its fppf pullback has rank one and is finite locally free; descent of these properties makes \(M_V\) invertible. Thus \(M\) is a line bundle. The identical procedure for maps gives full faithfulness and the Isom sheaf condition. This proves the claim at the generality of [Stacks, Tag 0372].

For \(X=B=S\), this is \(B\mathbb G_m\), by the frame-torsor equivalence of Section 4.3. For general \(X/B\) it records line bundles on the entire fibre \(X_T\); it need not be a gerbe, since those line bundles need not become isomorphic after a cover of \(T\). The isomorphism-class presheaf and its sheafification also discard scalar automorphisms. Algebraicity of suitable Picard stacks is a later theorem in *Moduli stacks are algebraic*.

Stacks of modules with the descent and Morita structures studied in [Descent through replacement objects](https://kokunoyumeto.github.io/open-math-courses-public/courses/categorical-tools-for-analytic-sheaves/descent-through-replacement-objects.html), [Representing objects from local data](https://kokunoyumeto.github.io/open-math-courses-public/courses/categorical-tools-for-analytic-sheaves/representing-objects-from-local-data.html), [Local module categories and Morita equivalence](https://kokunoyumeto.github.io/open-math-courses-public/courses/categorical-tools-for-analytic-sheaves/local-module-categories-and-morita-equivalence.html), and [Twisted modules from coherent gluing](https://kokunoyumeto.github.io/open-math-courses-public/courses/categorical-tools-for-analytic-sheaves/twisted-modules-from-coherent-gluing.html) belong to a further discussion. Only descent of modules and isomorphisms, not their Morita theory, is used here.

## 6. Gerbes and the obstruction to gluing objects

A **gerbe** \(\mathcal G\) over a site is a stack in groupoids with two additional properties: every base object has a cover on which objects of \(\mathcal G\) exist, and any two objects over the same base are locally isomorphic. A gerbe is **neutral over \(U\)** if it has an object over \(U\). Local existence in the definition does not assert neutrality. See [Stacks, Tags 06NY and 06NZ].

If \(x,y\in\mathcal G(U)\), then \(\operatorname{Isom}(x,y)\) is a right torsor under \(\operatorname{Aut}(x)\), acting by precomposition. It is a sheaf because \(\mathcal G\) is a stack, it is locally nonempty by the gerbe condition, and for two isomorphisms \(u,v:x\to y\), the unique automorphism taking \(u\) to \(v\) is \(u^{-1}v\). Thus both assertions in (4.1) hold.

### 6.1. The band in the abelian case

**Theorem 6.1.** Suppose every automorphism sheaf of a gerbe \(\mathcal G\) is abelian. There is a canonical abelian sheaf \(A\) on its site and, for every \(x\in\mathcal G(U)\), a canonical identification

\[
A|_U\simeq\operatorname{Aut}(x).
\tag{6.1}
\]

These identifications respect pullback, and every isomorphism \(u:x\to y\) identifies them by conjugation \(\alpha\mapsto u\alpha u^{-1}\). No final object of the site is required.

**Proof.** If \(u,v:x\to y\) are two isomorphisms, write \(v=u\gamma\), with \(\gamma\in\operatorname{Aut}(x)\). Since this group is abelian,
\[
v\alpha v^{-1}
=u\gamma\alpha\gamma^{-1}u^{-1}
=u\alpha u^{-1}.
\tag{6.2}
\]
Thus conjugation does not depend on the chosen isomorphism. If \(x,y\) are only locally isomorphic, their local conjugation maps agree on overlaps by (6.2) and glue to a canonical isomorphism of their automorphism sheaves. For three objects, the resulting comparisons compose correctly because locally one can compose the chosen isomorphisms. They also commute with every base restriction.

Here is a global construction even when the site has no final object. Let \(H(U)\) be the set of isomorphism classes of pairs \((x,\alpha)\), with \(x\in\mathcal G(U)\) and \(\alpha\in\operatorname{Aut}(x)(U)\). An isomorphism of pairs is an isomorphism \(u:x\to y\) conjugating \(\alpha\) to the second automorphism. Pullback makes \(H\) a presheaf of sets. Put \(A=aH\), its sheafification.

For each \(x\in\mathcal G(U)\), the map
\(\operatorname{Aut}(x)\to A|_U\) sending \(\alpha\) to \([(x,\alpha)]\) is an isomorphism of sheaves of sets. It is locally surjective: a section of \(A\) is locally represented by a pair \((y,\beta)\); refine until \(y\) is isomorphic to the restriction of \(x\), then transport \(\beta\) to that restriction. It is injective: local equality of the pairs means local conjugacy by an automorphism of \(x\), and abelianness makes this conjugacy equality. Equality in the automorphism sheaf then holds globally. This proves the assertion.

To define multiplication on \(A\), take two sections over any object and cover it by objects admitting an \(x\). Use the preceding identification with \(\operatorname{Aut}(x)\) to multiply their restrictions. On overlaps the identifications differ by the canonical conjugation maps, which preserve multiplication and are independent of choices. The products therefore glue uniquely. The same procedure defines the unit and inverses. Group identities and commutativity hold locally and hence globally. It gives \(A\) its abelian sheaf structure and turns the identifications into group isomorphisms (6.1). Their pullback and conjugation compatibilities follow from the construction. Any other sheaf with these specified local identifications is uniquely isomorphic to this one, since objects exist locally everywhere. \(\square\)

*Reference:* [Stacks, Tag 0CJY]. The sheaf \(A\) is called the **band** in this abelian situation. For nonabelian automorphism groups, conjugation depends on the isomorphism up to an inner automorphism; a general band requires additional language which is not used here.

### 6.2. A vanishing criterion for a global object

For an object \(U\) of a site, \(H^q(U,A)\) denotes cohomology on \(\mathcal C/U\), with the restriction of \(A\).

**Theorem 6.2.** Let \(\mathcal G\) be a gerbe with abelian band \(A\). Suppose \(H^2(U,A)=0\), and suppose a cofinal collection of covers \(\{U_i\to U\}\) satisfies

\[
H^1(U_i,A)=0,\qquad H^1(U_i\times_U U_j,A)=0
\quad\text{for every }i,j.
\tag{6.3}
\]

Then \(\mathcal G(U)\) is nonempty.

**Proof.** Choose a cover with objects \(x_i\). Refine it by a cover satisfying (6.3), which is possible by cofinality, and restrict the objects. The Isom sheaf between the two restrictions on \(U_{ij}\) is an \(A|_{U_{ij}}\)-torsor, by Section 6 and (6.1). Torsors under an abelian sheaf are classified by \(H^1\), with zero corresponding to the trivial torsor [Stacks, Tag 03AJ]. Thus the second vanishing in (6.3) lets us choose
\(\phi_{ij}:x_i|_{U_{ij}}\to x_j|_{U_{ij}}\).
These isomorphisms need not satisfy the cocycle.

Use additive notation for \(A\). Write \(\iota_i:A|_{U_i}\simeq\operatorname{Aut}(x_i)\). Define \(c_{ijk}\in A(U_{ijk})\) by

\[
\phi_{jk}\phi_{ij}=\phi_{ik}\iota_i(c_{ijk}).
\tag{6.4}
\]

Transporting automorphisms through an isomorphism preserves their band section, by Theorem 6.1. Compute \(\phi_{kl}\phi_{jk}\phi_{ij}\) in two ways. Combining the last two arrows first gives
\(\phi_{il}\iota_i(c_{ikl}+c_{ijk})\).
Combining the first two arrows first gives
\(\phi_{il}\iota_i(c_{ijl}+c_{jkl})\).
Cancel \(\phi_{il}\) and use the injectivity of \(\iota_i\). This proves

\[
c_{jkl}-c_{ikl}+c_{ijl}-c_{ijk}=0,
\tag{6.5}
\]

so \(c\) is a Čech 2-cocycle for the cover.

We must justify why its Čech class vanishes from the sheaf-cohomology hypothesis. The Čech-to-cohomology spectral sequence [Stacks, Tag 03AZ] has
\[
E_1^{p,q}=
\prod_{i_0,\ldots,i_p}H^q(U_{i_0\cdots i_p},A),
\qquad
E_2^{p,0}=\check H^p(\{U_i\},A),
\]
and converges to \(H^{p+q}(U,A)\). By the first vanishing in (6.3), \(E_1^{0,1}=0\), hence \(E_2^{0,1}=0\). The only possible incoming differential to \(E_r^{2,0}\), for \(r\ge2\), is \(d_2:E_2^{0,1}\to E_2^{2,0}\); for larger \(r\) its source has negative first index. Every outgoing differential has negative second index. Therefore \(E_\infty^{2,0}=E_2^{2,0}\), which is the last filtration piece inside \(H^2(U,A)\). This proves the required injection
\(\check H^2(\{U_i\},A)\hookrightarrow H^2(U,A)\).

Since the target vanishes, choose a Čech 1-cochain \(a=(a_{ij})\) with
\(\delta a=-c\), where \((\delta a)_{ijk}=a_{jk}-a_{ik}+a_{ij}\).
Replace \(\phi_{ij}\) by
\(\phi'_{ij}=\phi_{ij}\iota_i(a_{ij})\).
Equation (6.4), and the compatibility of the band with transport, show that the new defect is
\[
c'_{ijk}=c_{ijk}+a_{ij}+a_{jk}-a_{ik}=0.
\]
The \(\phi'_{ij}\) satisfy the descent cocycle. Pulling that cocycle back to diagonal tuples also makes the diagonal restrictions identities, since an invertible idempotent arrow is an identity. Thus the data descend to an object of \(\mathcal G(U)\), because \(\mathcal G\) is a stack. \(\square\)

*Reference:* [Stacks, Tag 0CK0]. The two \(H^1\) assumptions have distinct roles: vanishing on pairwise overlaps supplies isomorphisms, and vanishing on the covering objects makes the Čech comparison in degree two injective. This proof does not use the classification theorem below.

### 6.3. The classification theorem, stated

**Theorem 6.3 (abelian gerbe classification; not proved here).** On a site with a final object \(U\), equivalence classes of gerbes with a specified band identification with an abelian sheaf \(A\) are naturally classified by \(H^2(U,A)\). Equivalences must preserve that band identification. The zero class is the class of the neutral gerbe of \(A\)-torsors; a gerbe has zero class exactly when it has a global object.

We use the usual cocycle normalization: local objects and chosen arrows between them give the defect (6.4), and its class is the class of the gerbe. If the arrows require further covers of the pairwise overlaps, one refines those overlaps as well; the same defect is then a cocycle on a hypercover. It is not necessary to assume that ordinary Čech cohomology on a particular cover equals sheaf cohomology.

*Locator:* A. Deopurkar, *Torsors and gerbes*, §2 “Preliminaries”, theorem labelled *theorem-cohomologies-and-torsors-gerbes*, [arXiv:2305.15412](https://arxiv.org/abs/2305.15412). The classification is stated there. For the cohomology computation by refinements of hypercovers on a site with fibre products, see [Stacks, Tag 01H0]. All applications here are on a scheme's fppf site or on \(\mathcal C/U\), which has a final object.

The neutrality statement also has a direct categorical explanation. Fix \(x\in\mathcal G(U)\). Send \(y\) over \(V\to U\) to the right \(A|_V\)-torsor \(\operatorname{Isom}(x|_V,y)\), with precomposition as action. An isomorphism of \(y\)'s induces an equivariant isomorphism of torsors. Locally, where both objects are identified with \(x\), this is the correspondence between arrows and translations of trivial torsors, so it is fully faithful on Isom sheaves. Given any \(A\)-torsor, choose sections \(p_i\) and write \(p_j=p_i a_{ij}\). Glue local copies \(x_i\) of \(x\) by the automorphisms \(\iota_i(a_{ij}^{-1})\). The torsor cocycle, and abelianness of \(A\), give (1.3), so they descend to \(y\). If \(q_i:x_i\to y|_{U_i}\) are the descent identifications, then \(q_j=q_i\iota_i(a_{ij})\); the right torsor \(\operatorname{Isom}(x,y)\) therefore has the same transition sections as the given torsor and recovers it. Thus a chosen global object gives an equivalence \(\mathcal G|_U\simeq BA\).

### 6.4. Root gerbes in every characteristic

Let \(Z\) be a scheme, let \(L\) be a line bundle on \(Z\), and let \(n\ge1\). Define \(\mathcal R_n(L)\) over the fppf site of \(Z\) by objects

\[
(M,\theta),\qquad
M\text{ a line bundle on }T,\quad
\theta:M^{\otimes n}\xrightarrow{\sim}L|_T.
\tag{6.6}
\]

An isomorphism \(u:(M,\theta)\to(M',\theta')\) satisfies
\(\theta' u^{\otimes n}=\theta\).
This is a stack: line bundles descend by Section 5, and their specified isomorphisms \(\theta\) descend by the full faithfulness of module descent. The compatibility equation for arrows is local.

It has objects Zariski locally, since a trivialization of \(L\) gives the trivial line bundle with a specified \(n\)-th-power isomorphism. Any two objects are fppf locally isomorphic. Trivialize both line bundles and \(L\); their specified power isomorphisms then differ by a unit \(a\) in the base ring \(R\). An isomorphism of the two pairs is obtained by adjoining an \(n\)-th root of this unit, with the direction chosen to satisfy their compatibility equation. The ring

\[
R[t]/(t^n-a)
\tag{6.7}
\]

is free of rank \(n\) over \(R\), hence finite faithfully flat, and \(t\) is a unit since \(t^n=a\). It supplies the required fppf cover. This works when \(n\) is not invertible.

An automorphism of a line bundle is scalar multiplication by a unit. For (6.6) it must satisfy \(a^n=1\). Its automorphism sheaf is therefore canonically \(\mu_n\), and these identifications respect all conjugations and pullbacks. Thus \(\mathcal R_n(L)\) is a gerbe banded by the fppf sheaf \(\mu_n\). It has a global object exactly when there is a line bundle \(M\) with \(M^{\otimes n}\simeq L\), or equivalently
\([L]\in n\operatorname{Pic}(Z)\).
In characteristic dividing \(n\), the band can be nonreduced; this is why the fppf topology, rather than an unqualified étale Kummer assertion, is used.

## 7. Exercises and complete solutions

**Exercise 1 (easy).** Show that a stack in setoids is equivalent to a sheaf of sets.

**Solution.** Take isomorphism classes \(F(U)=\pi_0(\mathcal X(U))\). Compatible local classes have representatives \(x_i\) and unique overlap isomorphisms; uniqueness forces their cocycle. They descend to a global object. If two global objects have the same local classes, their unique local isomorphisms glue in the Isom sheaf, so their global classes agree. This proves both sheaf axioms for \(F\). The class functor is essentially surjective and is bijective on arrows, because two classes agree exactly when their objects have their unique isomorphism. It is the required equivalence, compatible with pullback.

**Exercise 2 (medium).** For objects \(x,y\) of a stack over \(U\), show that \(\operatorname{Isom}(x,y)\) is a sheaf.

**Solution.** For a cover of a test object \(V\to U\), pull back \(x\) and \(y\) to \(V\). Compatible local isomorphisms are an arrow between their restriction descent data. Full faithfulness of the descent equivalence (1.2) gives a unique arrow \(x|_V\to y|_V\). The inverses of the local isomorphisms are compatible too and descend to its inverse; equivalently, the fibre is already a groupoid. Thus the unique descended arrow is an isomorphism. This is exactly existence and uniqueness in the sheaf condition on every test \(V\).

**Exercise 3 (medium).** Show that a free action has \([X/G]\simeq X/G\), where the quotient on the right is a sheaf quotient.

**Solution.** For a trivial torsor object associated with \(x:T\to X\), its automorphisms are the sections \(g\) satisfying \(gx=x\). Freeness as a sheaf action makes \(g\) the identity on every test. Every quotient-stack object is locally a trivial torsor object, so its automorphism sheaf is trivial as well. Its fibres are consequently setoids. Exercise 1 replaces the stack by its sheaf of isomorphism classes. That sheaf is locally covered by sections of \(X\), and equality of two local sections means, locally, that an arrow \(g\) relates them. These are precisely the generators and local equality rule for the sheafification of the orbit presheaf. Hence it is \(X/G\). Algebraicity of that sheaf is a further question, already answered under the flat hypotheses of Lesson 2.

**Exercise 4 (medium).** Construct the gerbe of \(n\)-th roots of a line bundle \(L\), identify its band, and characterize its global objects.

**Solution.** Use the pairs and isomorphisms (6.6). Line-bundle descent and descent of \(\theta\) show that this is a stack. Local trivializations of \(L\) give objects. To compare two objects, trivialize their line bundles and adjoin an \(n\)-th root of the ratio of their power trivializations. Equation (6.7) is a finite free faithfully flat cover of positive rank, so the required comparison exists fppf locally for every positive \(n\). The compatible automorphisms are precisely multiplication by units satisfying \(a^n=1\), giving the canonical band \(\mu_n\). A global pair exists if and only if \(M^{\otimes n}\simeq L\) for a line bundle on \(Z\), which is exactly the assertion that the class of \(L\) is divisible by \(n\) in \(\operatorname{Pic}(Z)\).

**Exercise 5 (hard).** Use Theorem 6.3 to identify the root gerbe's class with the Kummer boundary, fixing its sign.

**Solution.** On the fppf site the sequence of abelian sheaves

\[
1\longrightarrow\mu_n\longrightarrow\mathbb G_m
\xrightarrow{a\mapsto a^n}\mathbb G_m
\longrightarrow1
\tag{7.1}
\]

is exact. The kernel assertion is the definition of \(\mu_n\), and local surjectivity is exactly (6.7). Use the transition-coordinate convention for the identification of \(\operatorname{Pic}(Z)\) with \(H^1(Z,\mathbb G_m)\): for local frames \(\ell_i\) of \(L\), write
\(\ell_i=g_{ij}\ell_j\).
Then \(g_{ij}g_{jk}=g_{ik}\), and \((g_{ij})\) represents \([L]\) in this convention. In frame-torsor terms these are the left multipliers taking the \(i\)-coordinates to the \(j\)-coordinates. This specifies the sign of the identification as well as the differential used below.

Choose local root objects \(M_i\) with basis \(m_i\) and \(\theta_i(m_i^{\otimes n})=\ell_i\). A compatible isomorphism
\(\phi_{ij}:M_i\to M_j\) has
\(\phi_{ij}(m_i)=r_{ij}m_j\), where \(r_{ij}^n=g_{ij}\).
Roots \(r_{ij}\) exist after fppf covering the overlaps, by (6.7). The associativity defect of these isomorphisms is multiplication by

\[
c_{ijk}=r_{ij}r_{jk}r_{ik}^{-1}\in\mu_n.
\tag{7.2}
\]

Indeed, the two successive isomorphisms multiply \(m_i\) by \(r_{ij}r_{jk}\), whereas the direct one multiplies it by \(r_{ik}\). Its \(n\)-th power is one by the cocycle for \(g\).

The connecting homomorphism for (7.1) uses the cochain differential with alternating signs. Thus it lifts the 1-cocycle \(g\) to \(r\), then takes
\((\delta r)_{ijk}=r_{jk}r_{ik}^{-1}r_{ij}\), the same element as (7.2), since the sheaves are abelian. This is the usual lift-and-differentiate construction of a connecting homomorphism.

If the chosen roots exist only on covers of the overlaps, take those covers as degree-one data of a hypercover of the degree-zero trivializing cover. In degree two, cover the matching objects, so that all three arrows in (7.2) are defined together; subsequent matching covers complete the hypercover. The same computation holds there. Hypercover cohomology, after refinement, computes sheaf cohomology [Stacks, Tag 01H0]; the boundary construction is compatible with these refinements. This justifies the calculation for arbitrary \(Z\), without assuming that the selected ordinary Čech cover computes \(H^2\).

The normalization of Theorem 6.3 sends the gerbe to precisely this defect class. Consequently, with the conventions just fixed,

\[
[\mathcal R_n(L)]=\delta[L]\quad\text{in }H^2(Z,\mu_n).
\tag{7.3}
\]

Reversing the transition or defect convention would reverse the sign. As a consistency check, exactness of the cohomology sequence makes \(\delta[L]=0\) exactly when \([L]\) is in the image of multiplication by \(n\) on \(\operatorname{Pic}(Z)\), which agrees with Exercise 4 and the neutrality assertion of Theorem 6.3.

## What this lesson does not prove

- The definitions and basic cartesian-pullback formalism of categories fibred in groupoids are prerequisites from *Fibred categories and descent data*. Their use is limited to the canonical comparisons for pullbacks and the definition of descent data.
- Ordinary sheafification on a site, fpqc descent for quasi-coherent modules [Stacks, Tag 023T], descent of finite local freeness [Stacks, Tag 05B2], and fpqc descent of étaleness [Stacks, Tag 02VN] are site and scheme prerequisites. Section 5 explains exactly how they yield the module, finite-cover and Picard stacks.
- The classification of abelian torsors by \(H^1\) [Stacks, Tag 03AJ] and the Čech-to-cohomology spectral sequence [Stacks, Tag 03AZ] are prerequisites from *Cohomology on sites*. Theorem 6.2 proves the gerbe existence criterion from them, including the needed injection and defect calculation.
- The abelian gerbe classification is stated in Theorem 6.3 with Deopurkar's §2 locator. Its general proof is not included. The hypercover comparison on a site with fibre products [Stacks, Tag 01H0] is used only to interpret the overlap-refinement calculation in Exercise 5 as sheaf cohomology. We do not assert that an arbitrary ordinary Čech cover computes that cohomology.
- The general inverse-image theory for stacks under change of site [Stacks, Tag 04WA], algebraicity of module and Picard moduli, and nonabelian bands are beyond this lesson. The elementary pullback and localization cases used here are proved in Section 2.5.

## References

The [AI Integrated Stacks Project English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains the Stacks tags. The relevant reading is *Stacks*, Tags 0267, 02Z9, 02ZC, 0268, 02ZH, 042Y, 036X, 02ZM, 0435, 04W9, 02ZO, 0436, 06NT, 06NY, 06NZ, 0CJY, 04WA and 04WT; *Examples of Stacks*, Tags 04SQ, 03YL, 0BLY, 04UG, 04UI, 036Z, 04UJ, 04UN, 04UR, 04UV, 04WM and 0372; *Algebraic Stacks*, Tags 04SS and 04ST; and *Cohomology on Sites*, Tags 0CJZ and 0CK0. Individual tags also identify the corresponding statements in the [Stacks project](https://stacks.math.columbia.edu/).

K. Behrend, *Introduction to algebraic stacks*, lecture notes dated 17 December 2012, Chapter 1, pp. 8–31, develops the motivation through families and their symmetry groupoids. Chapter 2, pp. 73–80, introduces the fibred-category formalism; Remark 2.11 explains its stronger topological prestack convention.

A. Deopurkar, [*Torsors and gerbes*](https://arxiv.org/abs/2305.15412), §2 “Preliminaries”, gives the banded-gerbe terminology and states the \(H^1\) and \(H^2\) classification theorem cited above.

For historical context, [SGA 1](https://github.com/KokunoYumeto/sga-en), Exposé VI, develops fibred categories and descent. Exposé XIII, §0, is a review of stacks and gerbes; cohomological properness is the subject of that exposé as a whole. [FGA](https://github.com/KokunoYumeto/fga-en), Exposé 190, §A.1, sets out the categorical pullback and descent preliminaries. These references supply context for the prerequisite formalism.
