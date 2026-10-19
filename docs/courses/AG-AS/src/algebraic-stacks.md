# Algebraic stacks

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An algebraic stack has two kinds of local coordinates. A smooth atlas supplies families of objects; its self-intersection supplies isomorphisms between those objects. An algebraic space is the case in which these isomorphisms carry no stabilizers. The main task of this lesson is to prove both directions of this description, allowing the atlas and the arrow space to be arbitrary algebraic spaces and imposing no separation condition.

We work over a scheme \(S\), on the big fppf site of \(S\)-schemes. An algebraic space is regarded as its sheaf of points, and also as the associated stack with discrete fibres. Products of stacks are over \(S\); fibre products of stacks are **2-fibre products**. Read [Stacks in groupoids](stacks-in-groupoids.md) and [Properties and morphisms of algebraic spaces](properties-and-morphisms.md) first. We use the stackification constructed in the former and the smooth and flat bootstrap proved in [The bootstrap theorem](bootstrap-theorem.md). The scheme prerequisites used for the elliptic-curve example are stated precisely at the end.

## 1. What representability means

### 1.1. Objects and liftings

For an algebraic space \(F/S\), let \(h_F\) denote the fibred category whose fibre over \(T\) is the discrete set \(F(T)\). A category fibred in groupoids \(\mathcal X\) is **represented by \(F\)** if it is equivalent, over the base site, to \(h_F\). This is a claim about the whole family of fibre categories, rather than just their sets of isomorphism classes [Stacks, Tags 02ZQ, 02ZV].

The criterion is elementary: \(\mathcal X\) is represented by an algebraic space if and only if its fibres are setoids and the presheaf
\[
T\longmapsto \pi_0(\mathcal X(T))
\tag{1.1}
\]
is an algebraic space. Indeed, passage to isomorphism classes gives a functor from a setoid to its discrete set of classes. It is fully faithful because each Hom set is either empty or a singleton, and it is essentially surjective by the definition of a class. Pullback respects classes. Conversely, an equivalence with a discrete fibred category makes every automorphism trivial and identifies (1.1) with the representing sheaf. For a stack in setoids, Lesson 4 proves that (1.1) is a sheaf; algebraicity remains an additional condition.

**Definition 1.1.** A morphism \(f:\mathcal X\to\mathcal Y\) is **representable by algebraic spaces** if, for every scheme \(T/S\) and every \(y\in\mathcal Y(T)\), the stack
\[
T\times_{y,\mathcal Y,f}\mathcal X
\tag{1.2}
\]
is represented by an algebraic space over \(T\). Replace “algebraic spaces” by “schemes” for the stronger notion [Stacks, Tags 04ST, 04SX].

Over \(V\to T\), objects of (1.2) are pairs \((x,\alpha)\), with \(x\in\mathcal X(V)\) and \(\alpha:y|_V\xrightarrow{\sim}f(x)\). A morphism to \((x',\alpha')\) is \(\beta:x\to x'\) satisfying \(f(\beta)\alpha=\alpha'\). Thus representability forces \(f\) to be faithful on each fibre: two arrows with the same image differ by an automorphism in one of these lifting categories, and a represented category has none.

More generally, representability of \(f\) is equivalent to the following two conditions: \(f\) is faithful on the fibres, and, for every \(y/T\), the presheaf of isomorphism classes of the pairs just described is an algebraic space over \(T\). Faithfulness makes the lifting fibres setoids, so the criterion preceding Definition 1.1 proves this equivalence. Faithfulness alone is insufficient for arbitrary fibred categories.

**Lemma 1.2 (base change, composition and testing by spaces).** Representability by algebraic spaces is stable under base change and composition. If \(f\) is representable by algebraic spaces and \(Z\) is an algebraic space mapping to its target, then \(Z\times_{\mathcal Y}\mathcal X\) is an algebraic space. Representability is invariant under equivalences of source and target.

*Proof.* After base change, a scheme test gives exactly the original lifting category with the composed test object. This proves the first assertion.

For the assertion about \(Z\), the projection \(Z\times_{\mathcal Y}\mathcal X\to Z\) has setoid fibres: an automorphism fixes the \(Z\)-coordinate and maps to the identity in \(\mathcal Y\), so faithfulness of \(f\) kills it. Pass to its presheaf \(H\) of classes. For every scheme \(T\to Z\), the presheaf \(H\times_ZT\) is an algebraic space by the hypothesis on \(f\); the identification follows directly from the pairs in (1.2). The recognition result of Lesson 2 for a presheaf representable by spaces over an algebraic space therefore represents \(H\) by an algebraic space. The setoid criterion gives the asserted equivalence.

Now test a composite \(\mathcal X\to\mathcal Y\to\mathcal Z\) by \(T\to\mathcal Z\). The first lifting \(Y_T=T\times_{\mathcal Z}\mathcal Y\) is an algebraic space. The second lifting is \(\mathcal X\times_{\mathcal Y}Y_T\), an algebraic space by the preceding paragraph. Objects on both sides are the same liftings with their specified comparison isomorphisms. Finally, equivalences transport these lifting categories by equivalences, which do not change their representability. \(\square\)

There is no ambiguity in calling the space in (1.2) \(X_y\). Its map \(X_y\to T\) is determined by the projection. Between stacks represented by spaces, the Hom groupoid is the discrete set of morphisms of those spaces: a functor determines the map on classes, and every comparison between functors representing that map is unique. This uniqueness is special to setoids. For a map \(T\to\mathcal X\), 2-Yoneda instead identifies its entire Hom groupoid with \(\mathcal X(T)\), including automorphisms [Stacks, Tag 04SS; Lesson 4, Lemma 3.1].

### 1.2. Properties and the diagonal

Let \(P\) be a property of morphisms of algebraic spaces stable under base change and local on the target for the fppf topology. A representable morphism \(f\) has \(P\) if every \(X_y\to T\) has \(P\). We will use smoothness, étaleness, flatness, local finite presentation and surjectivity in this sense [Stacks, Tags 03YJ, 03YK].

The elementary rules follow without choices of coordinates. Base change replaces \(X_y\to T\) by its ordinary base change. If \(P\) is also stable under composition, Lemma 1.2 writes a tested composite as two morphisms of spaces with \(P\), so the composite has \(P\). To test \(P\) after a morphism locally surjective on objects, take an fppf cover on which a given \(y/T\) lifts to that morphism; the tested maps have \(P\) on that cover, and fppf locality gives \(P\) over \(T\). The same argument permits tests by algebraic spaces: choose an étale scheme cover of the test space, apply the scheme tests, and descend \(P\). Products of representable maps have \(P\) when \(P\) is stable under composition, because their product factors as two base changes.

**Lemma 1.3 (diagonal tests).** For a stack \(\mathcal X\), the following conditions are equivalent:

1. \(\Delta_{\mathcal X}:\mathcal X\to\mathcal X\times_S\mathcal X\) is representable by algebraic spaces.
2. For each scheme \(T/S\) and \(x,y\in\mathcal X(T)\), the sheaf \(\operatorname{Isom}_T(x,y)\) is an algebraic space.
3. For any two schemes \(T_1,T_2\) mapping to \(\mathcal X\), the stack \(T_1\times_{\mathcal X}T_2\) is an algebraic space.
4. Every morphism from an algebraic space to \(\mathcal X\) is representable by algebraic spaces.

The analogous first three conditions hold with schemes in place of spaces.

*Proof.* A test of the diagonal by \((x,y):T\to\mathcal X\times_S\mathcal X\) has objects \((z,a:z\to x,b:z\to y)\). The functor sending this triple to \(ba^{-1}:x\to y\) identifies its setoid with \(\operatorname{Isom}_T(x,y)\); an inverse uses \(z=x,a=1\). This proves \(1\Longleftrightarrow2\).

For \(x_i/T_i\), put \(B=T_1\times_ST_2\). The fibre product \(T_1\times_{\mathcal X}T_2\) is the sheaf over \(B\) of isomorphisms between the pullbacks of \(x_1,x_2\). Thus 2 implies 3. Conversely, for \(x,y/T\), pull \(T\times_{\mathcal X}T\) back along the diagonal \(T\to T\times_ST\); this recovers \(\operatorname{Isom}_T(x,y)\), proving the converse. Ordinary fibre products of spaces, or of schemes in the scheme version, justify these steps.

Condition 3 says precisely that every scheme map to \(\mathcal X\) is representable. For an algebraic space \(U\to\mathcal X\) and a scheme \(T\to\mathcal X\), apply Lemma 1.2 to the representable map \(T\to\mathcal X\), with the test space \(U\). This gives condition 4. Its converse includes scheme maps. \(\square\)

In particular, the diagonal condition makes the phrase “smooth atlas \(U\to\mathcal X\)” meaningful before we know whether any atlas exists. Representability of Isom sheaves is stronger than the prestack sheaf condition recalled in [Stacks, Tag 0304].

### 1.3. A local recognition lemma

We shall repeatedly use one consequence of the **proved** flat bootstrap from Lesson 2.

**Lemma 1.4.** Let \(F\) be an fppf sheaf over a scheme \(T\). If there is an fppf cover \(T_i\to T\) such that every \(F\times_TT_i\) is an algebraic space, then \(F\) is an algebraic space. If a morphism of the resulting spaces has a property local on the target for the fppf topology, that property can be checked on this cover.

*Proof.* First suppose \(T\) affine. Refine the cover by affine opens of the \(T_i\). Their maps to \(T\) are flat and locally of finite presentation, hence open. A finite number of their images cover the quasi-compact scheme \(T\). Their disjoint union \(W\to T\) is a surjective flat morphism of finite presentation: each map between these affines is quasi-compact as well as locally of finite presentation. The sheaf \(Q=F\times_TW\) is a finite disjoint union of algebraic spaces, hence an algebraic space.

The map \(Q\to F\) is representable **by schemes**, flat, locally of finite presentation and surjective. Indeed, a scheme \(V\to F\) pulls it back to \(V\times_TW\to V\). The flat bootstrap of Lesson 2 therefore makes \(F\) an algebraic space.

For arbitrary \(T\), apply this argument over every affine open of \(T\). The resulting open subspaces of \(F\) agree on intersections as sheaves. Gluing open algebraic spaces, as proved in Lesson 1, gives \(F\). The last assertion is the stated locality property applied after representability has been established. \(\square\)

## 2. Algebraic stacks and trivial inertia

**Definition 2.1.** An **algebraic stack** over \(S\) is a stack in groupoids \(\mathcal X\) on the big fppf site such that its diagonal is representable by algebraic spaces and there is a scheme \(U/S\) with a smooth surjective morphism \(U\to\mathcal X\). Such a morphism is a **smooth atlas** [Stacks, Tags 026N, 026O].

A **Deligne–Mumford stack** is an algebraic stack admitting an étale surjective atlas by a scheme [Stacks, Tag 03YO]. Neither definition adds quasi-compactness, quasi-separatedness, separatedness, finite-type hypotheses over \(S\), or affineness of the diagonal. Étale morphisms are smooth, so an étale atlas is a smooth atlas.

Replacing an atlas space by an étale scheme cover gives a scheme atlas. Consequently one may use an algebraic space as the domain of a smooth or étale atlas whenever the diagonal is already known to be representable. The definition is also invariant under equivalence: Isom sheaves are transported by equivalence, and the same atlas composed with the equivalence still has the same tested morphisms.

**Proposition 2.2.** Every algebraic space is a Deligne–Mumford stack; in particular every scheme is an algebraic stack [Stacks, Tag 03YR].

*Proof.* The discrete fibred category \(h_F\) is a stack because \(F\) is a sheaf. Its diagonal is the diagonal of \(F\), representable even by schemes by the algebraic-space definition. An étale scheme atlas \(U\to F\) gives the required atlas of \(h_F\). For a scheme its identity map is an atlas. \(\square\)

Recall that the inertia stack \(\mathcal I_{\mathcal X}\) has objects \((x,\alpha)\) with \(x\in\mathcal X(T)\) and \(\alpha\in\operatorname{Aut}(x)\). Its arrows conjugate \(\alpha\), and the map \(q:\mathcal I_{\mathcal X}\to\mathcal X\) forgets \(\alpha\). The identity section sends \(x\) to \((x,1)\).

**Theorem 2.3 (spaces are exactly algebraic stacks with trivial inertia).** For an algebraic stack \(\mathcal X/S\), these conditions are equivalent:

1. \(\mathcal X\) is a stack in setoids.
2. \(q:\mathcal I_{\mathcal X}\to\mathcal X\) is an equivalence.
3. \(\mathcal X\) is represented by an algebraic space.

This is [Stacks, Tag 04SZ] at its full, possibly non-separated, generality.

*Proof.* If all automorphisms are identities, the identity section and \(q\) are inverse equivalences, proving \(1\Rightarrow2\). Conversely, if \(q\) is an equivalence, \((x,\alpha)\) is isomorphic to \((x,1)\): fullness lifts the identity of \(x\) to an arrow between them. That arrow has underlying map \(1_x\), so its conjugation equation gives \(\alpha=1\). Thus \(2\Rightarrow1\). Representation by a space makes every fibre discrete up to equivalence, giving \(3\Rightarrow1\).

Assume 1. Lesson 4 identifies \(\mathcal X\) with the sheaf \(F(T)=\pi_0(\mathcal X(T))\). Choose a smooth scheme atlas \(U\to\mathcal X\). It gives a map \(U\to F\). Lemma 1.3 makes this map representable by algebraic spaces, and the tested maps are smooth and surjective because they are the original atlas tests. They are therefore flat and locally of finite presentation. The flat bootstrap proved in Lesson 2 makes \(F\) an algebraic space, proving 3. No étale atlas was assumed in this argument; Proposition 2.2 supplies one afterwards. \(\square\)

The condition ranges over objects on **all** scheme tests. The absence of nonidentity automorphisms merely at geometric points does not exclude infinitesimal stabilizers. For example, in characteristic \(p\) the group scheme \(\mu_p\) has only one point over an algebraically closed field, but has nonidentity sections over rings with nilpotents.

## 3. Smooth groupoids and their quotients

### 3.1. Keeping the arrows

A groupoid in algebraic spaces consists of \(U,R\), source and target maps \(s,t:R\to U\), identity \(e:U\to R\), inverse, and composition
\[
c:R\times_{s,U,t}R\longrightarrow R.
\tag{3.1}
\]
Our convention is that \(r\) is an arrow \(s(r)\to t(r)\), and \(c(h,g)=h\circ g\). The groupoid axioms are identities of morphisms of spaces; equivalently they hold on every scheme test. It is **smooth** if \(s\) and \(t\) are smooth. Inversion exchanges them, so it suffices to test either. This adjective does not say that \(U\), \(R\), or the quotient is smooth over \(S\).

Its prestack has objects \(u:T\to U\) and arrows \(r:T\to R\) with the indicated endpoints. It is a prestack because its Isom presheaves are represented by the spaces
\[
R\times_{(s,t),\,U\times_SU,\,(u,v)}T.
\tag{3.2}
\]
Define \([U/R]\) to be its fppf stackification from Lesson 4. Objects of this stack are fppf locally maps to \(U\), with arrows in \(R\) satisfying the groupoid cocycle. Since the original prestack has sheaf Isom presheaves, its functor into the stackification is fully faithful.

**Lemma 3.1.** For every groupoid in algebraic spaces, without a smoothness assumption, the diagonal of \([U/R]\) is representable by algebraic spaces.

*Proof.* Given objects \(a,b\) over a scheme \(T\), choose a common fppf cover on which both come from maps \(u_i,v_i:T_i\to U\). Full faithfulness of the prestack embedding identifies
\(\operatorname{Isom}(a,b)\times_TT_i\) with (3.2) for \(u_i,v_i\). The global Isom functor is a sheaf because \([U/R]\) is a stack. Lemma 1.4 represents it by an algebraic space. Lemma 1.3 now represents the diagonal. \(\square\)

This proof gives the diagonal directly, rather than assuming that arbitrary descent data of spaces are already known to be effective. The required recognition is exactly the bootstrap input isolated in Lemma 1.4.

**Theorem 3.2 (algebraicity of a smooth groupoid quotient).** If \((U,R,s,t,c)\) is a smooth groupoid in algebraic spaces over \(S\), then \([U/R]\) is an algebraic stack. The map \(U\to[U/R]\) is representable by algebraic spaces, smooth and surjective [Stacks, Tags 04TJ, 04TK].

*Proof.* The quotient is a stack by its construction, and Lemma 3.1 proves the diagonal condition. Lemma 1.3 therefore makes \(U\to[U/R]\) representable.

For a scheme \(T\) and \(a\in[U/R](T)\), let \(P=T\times_{[U/R]}U\). It is an algebraic space. On an fppf cover where \(a\) is the image of \(u:T_i\to U\), describe a point of \(P_{T_i}\) as a map \(v\) to \(U\) and an arrow \(u\to v\). Formula (3.2), with \(v\) allowed to vary, gives
\[
P\times_TT_i\cong T_i\times_{u,U,s}R.
\tag{3.3}
\]
The projection in (3.3) is smooth by base change of \(s\), and surjective because \(s\) has the identity section. Smoothness and surjectivity descend for morphisms of algebraic spaces along fppf covers, so \(P\to T\) has both properties. Finally choose an étale surjective scheme cover \(V\to U\). The composite \(V\to U\to[U/R]\) is smooth and surjective by the rules of §1.2, and is a scheme atlas. \(\square\)

If \(s,t\) are étale, the same proof makes (3.3) étale and gives an étale scheme atlas. The quotient is then Deligne–Mumford. A free smooth groupoid has setoid quotient fibres, since local stabilizers are trivial and equality of arrows is local; Theorem 2.3 then makes its quotient an algebraic space.

### 3.2. Recovering the stack from an atlas

**Theorem 3.3 (presentation theorem).** Let \(\mathcal X\) be an algebraic stack and \(p:U\to\mathcal X\) a smooth surjective morphism from an algebraic space. Then
\[
R=U\times_{\mathcal X}U
\]
is an algebraic space with a canonical smooth groupoid structure, and its quotient is equivalent to \(\mathcal X\) [Stacks, Tags 04T3, 04T5].

*Proof.* Lemma 1.3 represents \(R\). Describe its points as
\[
(u_0,u_1,\alpha:p(u_0)\xrightarrow{\sim}p(u_1)).
\tag{3.4}
\]
Put \(s(u_0,u_1,\alpha)=u_0\) and \(t(u_0,u_1,\alpha)=u_1\). Identity uses \(1_{p(u)}\), inversion replaces \(\alpha\) by \(\alpha^{-1}\) and exchanges the endpoints, and composition sends consecutive triples to
\((u_0,u_2,\beta\alpha)\). Each is a morphism of spaces because these formulas define natural transformations of their represented sheaves. The unit, inverse and associativity identities follow from those in the fibre groupoids of \(\mathcal X\). Both projections \(s,t\) are base changes of the smooth surjective atlas \(p\).

The prestack functor sending \(u\) to \(p(u)\) and (3.4) to \(\alpha\) extends by the universal property of stackification to
\[
F:[U/R]\longrightarrow\mathcal X.
\tag{3.5}
\]
For two objects of the quotient over \(T\), choose an fppf cover on which both are represented by maps to \(U\). On that cover the map of Isom sheaves induced by \(F\) is an isomorphism, by the defining description (3.4) of \(R\). A map of sheaves that is an isomorphism on a cover is an isomorphism globally. Thus \(F\) is fully faithful on every fibre.

Given \(x\in\mathcal X(T)\), the algebraic space \(P=T\times_{\mathcal X}U\) is smooth and surjective over \(T\). An étale scheme atlas of \(P\), followed by affine open refinements, gives an fppf covering family of \(T\) on which \(x\) is isomorphic to the image of some \(u_i:T_i\to U\). The chosen local isomorphisms with \(x\) give transition arrows \(p(u_i)\to p(u_j)\). Full faithfulness lifts them uniquely to arrows between the quotient objects. Their cocycle identity lifts too, by faithfulness. Effectivity in \([U/R]\) gives an object \(a/T\), and the local maps \(F(a)\to x\) glue in \(\mathcal X\) to an isomorphism. This proves essential surjectivity, and hence (3.5) is an equivalence. \(\square\)

The same equivalence proof works for a representable surjective flat morphism locally of finite presentation \(U\to\mathcal X\); its groupoid is then flat and locally of finite presentation. The smooth hypothesis in Theorem 3.2 is what supplies algebraicity of a quotient starting from an arbitrary groupoid.

A presentation records more than an orbit set. In (3.4), different isomorphisms with the same endpoints are different points of \(R\). Collapsing them to an equivalence relation would remove the stabilizers that distinguish a stack from a space.

## 4. Fibre products and useful recognition tests

**Theorem 4.1.** Suppose \(\mathcal X,\mathcal Y\) are algebraic stacks and \(\mathcal Z\) is a stack whose diagonal is representable by algebraic spaces. For arbitrary morphisms \(f:\mathcal X\to\mathcal Z\) and \(g:\mathcal Y\to\mathcal Z\), the stack
\[
\mathcal W=\mathcal X\times_{f,\mathcal Z,g}\mathcal Y
\tag{4.1}
\]
is algebraic. In particular, algebraic stacks have 2-fibre products [Stacks, Tag 04TD].

*Proof.* An object of \(\mathcal W(T)\) is a triple \((x,y,\alpha:f(x)\xrightarrow{\sim}g(y))\). An arrow \((a,b)\) between two such triples satisfies
\[
g(b)\alpha=\alpha'f(a).
\tag{4.2}
\]
For an fppf descent datum, the \(x\)'s descend in \(\mathcal X\), the \(y\)'s descend in \(\mathcal Y\), and the compatible \(\alpha\)'s descend as a section of an Isom sheaf in \(\mathcal Z\). Equation (4.2) can be checked on the cover. The same argument glues arrows and proves uniqueness. Thus \(\mathcal W\) is a stack.

For \(w=(x,y,\alpha)\) and \(w'=(x',y',\alpha')\) over \(T\), write
\[
\begin{aligned}
I_X&=\operatorname{Isom}_T(x,x'),&
I_Y&=\operatorname{Isom}_T(y,y'),\\
J&=\operatorname{Isom}_T(f(x),g(y')).
\end{aligned}
\]
These are algebraic spaces by the diagonal assumptions. The two maps to \(J\) are \(a\mapsto\alpha'f(a)\) and \(b\mapsto g(b)\alpha\). Equation (4.2) identifies
\[
\operatorname{Isom}_T(w,w')=I_X\times_JI_Y.
\tag{4.3}
\]
The right side is an algebraic space, so the diagonal of \(\mathcal W\) is representable.

Choose smooth scheme atlases \(U\to\mathcal X\), \(V\to\mathcal Y\). The space \(A=U\times_{\mathcal Z}V\) is algebraic by Lemma 1.3 applied to \(\mathcal Z\). The map \(A\to\mathcal W\) factors through \(\mathcal X\times_{\mathcal Z}V\); its two factors are base changes of the two atlases. It is therefore representable, smooth and surjective. Choose an étale scheme cover \(B\to A\). Then \(B\to\mathcal W\) is a smooth surjective scheme atlas, proving algebraicity.

Finally, the usual 2-fibre-product universal property is explicit: a morphism from any stack \(\mathcal T\) to \(\mathcal W\) is a pair of morphisms to \(\mathcal X,\mathcal Y\), together with a specified 2-isomorphism between their composites to \(\mathcal Z\); transformations satisfy (4.2). Restricting the test stacks to algebraic stacks preserves this equivalence of Hom groupoids. \(\square\)

**Corollary 4.2.** A morphism \(f:\mathcal X\to\mathcal Y\) between algebraic stacks is representable by algebraic spaces if and only if it is faithful on all fibre categories.

*Proof.* Necessity was proved in §1.1. For sufficiency, test by \(y/T\). Theorem 4.1 and Proposition 2.2 make \(T\times_{\mathcal Y}\mathcal X\) an algebraic stack. Its automorphisms are the \(\beta\in\operatorname{Aut}(x)\) with \(f(\beta)=1\), which faithfulness kills. Theorem 2.3 makes the lifting stack an algebraic space. \(\square\)

**Lemma 4.3 (compatible atlases).** For \(f:\mathcal X\to\mathcal Y\) and a chosen smooth scheme atlas \(V\to\mathcal Y\), there is a smooth scheme atlas \(U\to\mathcal X\), a map \(U\to V\), and a specified 2-isomorphism making the resulting square commute.

*Proof.* Choose a smooth scheme atlas \(W\to\mathcal X\). The space \(A=W\times_{\mathcal Y}V\) is algebraic, and \(A\to W\) is smooth and surjective. An étale scheme cover \(U\to A\) gives the desired smooth surjective composite \(U\to\mathcal X\), its map to \(V\), and the comparison isomorphism contained in the fibre-product datum. \(\square\)

**Proposition 4.4 (a representable smooth cover suffices).** Let \(\mathcal X\) be a stack and \(U\to\mathcal X\) a representable, smooth, surjective morphism from an algebraic space. Then \(\mathcal X\) is algebraic. Consequently a stack representable by algebraic spaces over an algebraic stack is algebraic.

*Proof.* Lemma 1.2 represents \(R=U\times_{\mathcal X}U\), even though the diagonal of \(\mathcal X\) is not yet known to be representable. For objects \(x,y/T\), the two pullbacks \(T\times_{\mathcal X}U\) are smooth surjective spaces over \(T\). Choose a common fppf scheme cover on which both have sections. The objects then become \(p(u),p(v)\), and their Isom sheaf is the pullback of \(R\to U\times_SU\). Lemma 1.4 represents the global Isom sheaf. This proves the diagonal condition. An étale scheme cover of \(U\) now gives the required atlas.

For the last assertion, pull a smooth scheme atlas of the target back to the source. Representability makes the pullback a space, and its projection to the source is representable, smooth and surjective. Apply the first assertion. \(\square\)

These statements explain the basic “overhaul” results in [Stacks, Tag 04T0]. In particular, a smooth atlas and a quotient presentation may be changed without changing the stack. A common refinement is obtained by taking the two atlases' fibre product over the stack and then an étale scheme cover of that space.

## 5. Smooth groups acting on spaces

Let \(G/S\) be a smooth group algebraic space acting on an algebraic space \(X/S\) on the left. Its action groupoid has objects \(X\), arrows \(G\times_SX\), source \(x\), target \(gx\), and composition
\[
(h,gx)\circ(g,x)=(hg,x).
\tag{5.1}
\]
The source is smooth by base change of \(G\to S\), and the target is smooth because inversion gives an isomorphism exchanging source and target.

**Proposition 5.1.** The quotient \([X/G]\) is algebraic, and \(X\to[X/G]\) is a smooth surjective morphism representable by algebraic spaces.

*Proof.* Apply Theorem 3.2 to (5.1). Lesson 4, Theorem 4.3 identifies its stackification with the stack of right fppf \(G_T\)-torsors \(P\to T\) endowed with maps \(\phi:P\to X\) satisfying \(\phi(pg)=g^{-1}\phi(p)\). This identifies the quotient in the statement with that torsor model. \(\square\)

One can see the atlas tests directly. The pullback \(T\times_{[X/G]}X\) is the torsor \(P\): a point of \(P\) trivializes the torsor and supplies the corresponding point of \(X\). Locally this is \(G_T\to T\), so the test is smooth and surjective. Its representability is provided by Lesson 4's torsor lemma, or by Theorem 3.2.

For \(X=S\), this is the **classifying stack** \(BG\), with atlas \(S\to BG\). Smooth affine group schemes give the announced first examples. A right \(G_T\)-torsor \(P\) has automorphism sheaf the inner form of \(G_T\) obtained from conjugation: if local sections satisfy \(p_j=p_i h_{ij}\), a left-translation automorphism has coordinates \(g_j=h_{ij}^{-1}g_i h_{ij}\). For an abelian group this gluing is the identity, so \(\operatorname{Aut}(P)\cong G_T\) canonically. For a nonabelian group one must retain the inner form.

For \(G=\mathbf G_m\), objects of \(B\mathbf G_m(T)\) are invertible modules \(L\), and their automorphism functors are \(\mathbf G_{m,T}\), not merely the units of one residue field. Its atlas is \(\operatorname{Spec}\mathbf Z\to B\mathbf G_m\) over the absolute base, or \(S\to B\mathbf G_{m,S}\) relatively.

The stack \(B\mathbf G_m\) is not Deligne–Mumford on a nonempty base. Here is a direct test. Base change to an algebraically closed field \(k\), and suppose there were an étale scheme atlas \(V\to B\mathbf G_m\). The fibre of the atlas over the trivial torsor is a nonempty étale algebraic space over \(k\); an étale scheme cover supplies a \(k\)-point of \(V\) representing that object up to isomorphism. The arrow space \(R=V\times_{B\mathbf G_m}V\) is étale over \(V\) by either projection. A nonidentity automorphism \(1+\epsilon\) over \(k[\epsilon]/(\epsilon^2)\), specializing to the identity, would give two distinct lifts of the identity arrow with the same constant source. Formal unramifiedness of \(R\to V\) forbids this. Thus no étale atlas exists.

The quotient \([\mathbf A^1/\mathbf G_m]\), for scalar multiplication, has the smooth atlas \(\mathbf A^1\). Lesson 4 identifies its objects with pairs \((L,s)\), an invertible module and a section. Their automorphisms are the units \(\lambda\) satisfying \(\lambda s=s\). Over an algebraically closed field the nonzero-section object has trivial stabilizer and the zero-section object has stabilizer \(\mathbf G_m\). The open substack where \(s\) never vanishes is the base \(S\), since \(s\) trivializes \(L\); the zero-section substack is \(B\mathbf G_m\).

Over a ring, stabilizers retain more information. For \(L=R\) and a section \(a\in R\), they are the solutions of \((\lambda-1)a=0\) with \(\lambda\) invertible. For example, when \(a\) is a zero divisor this can leave automorphisms invisible on some fibres. The atlas remembers these equations through the whole arrow space.

Even a finite diagonal does not by itself force the Deligne–Mumford condition. Over a field of characteristic \(p>0\), let the smooth group \(\mathbf G_m\) act on \(X=\mathbf G_m\) by \(\lambda x=\lambda^p x\). The action-to-endpoints map is finite free of rank \(p\): over \((x,y)\) its equation is \(\lambda^p=y/x\). Isom sheaves in the quotient are locally these finite free schemes, and descent of finite algebras makes the quotient diagonal finite. Its stabilizer at \(x=1\) is \(\mu_p\). The automorphism \(1+\epsilon\) over \(k[\epsilon]/(\epsilon^2)\) is nonidentity but reduces to the identity. The same formal-unramifiedness test used for \(B\mathbf G_m\) excludes an étale atlas. Smoothness of the acting group therefore does not eliminate nonreduced stabilizers.

## 6. Elliptic curves from Weierstrass equations

An elliptic curve over a scheme \(T\) is a proper smooth morphism of finite presentation \(p:E\to T\), with geometrically connected genus-one fibres, together with a section \(e:T\to E\). Arrows over \(T\) are isomorphisms preserving \(e\); arrows over a base map are the corresponding cartesian isomorphisms. These define a category fibred in groupoids \(\mathcal M_{1,1}\) [Stacks, Tags 072J, 072K]. We will prove it is a stack and exhibit its atlas.

### 6.0. Cohomology and divisors before choosing an equation

Let \(p:C\to T\) be a proper smooth morphism of finite presentation, with geometrically connected one-dimensional fibres of genus one. The scheme \(T\) is arbitrary. A section will be specified when required. For a line bundle \(M\), degree on a geometric fibre means the change in Euler characteristic
\[
\deg M_{\bar t}=\chi(C_{\bar t},M_{\bar t})
                         -\chi(C_{\bar t},\mathcal O_{C_{\bar t}}).
\]
We first justify the curve calculations that use this convention, then pass from a Noetherian cohomology complex to an arbitrary base with its canonical comparisons.

#### 6.0.1. Divisors and duality on the geometric curve

**Lemma 6.0.1 (the geometric curve and its degree formula).** Let \(k\) be algebraically closed and let \(D/k\) be a smooth proper connected curve. Put \(g=\dim_k H^1(D,\mathcal O_D)\). The curve is integral and projective, \(H^0(D,\mathcal O_D)=k\), and every line bundle \(N\) has an integer degree satisfying
\[
\chi(D,N)=\deg N+1-g.                                      \tag{E.1}
\]
This degree is additive under tensor products and equals the length of an effective divisor. A line bundle of negative degree has no nonzero global section.

*Proof.* Smoothness makes the local rings regular. In dimension one they are domains. Distinct irreducible components therefore cannot meet; the finitely many components are open and closed, so connectedness gives one integral component. Proper coherent cohomology over the field is finite, by AG-QC, *Coherence of higher direct images under proper morphisms*, Corollary 5.1. The algebra \(H^0(D,\mathcal O_D)\) is consequently a finite-dimensional domain over \(k\), hence a finite field extension of \(k\), and therefore is \(k\).

At a closed point \(P\), the regular local ring is a discrete valuation ring. Here is the relevant local argument. Its maximal ideal has one generator \(t\). A nonzero element cannot be divisible by every power of \(t\): otherwise its successive quotients would generate an ascending chain of principal ideals, and stabilization would give \(y=tay\), contradicting that \(1-ta\) is a unit. Every nonzero element thus has the form \(t^nu\) with \(u\) a unit. Choosing an element of least valuation in an ideal shows that every nonzero ideal is a power of \((t)\). In particular the closed point is an effective Cartier divisor.

We justify projectivity before applying projective duality. Choose a closed point \(P\). The quotient in
\[
0\longrightarrow\mathcal O_D\longrightarrow\mathcal O_D(nP)
   \longrightarrow Q_n\longrightarrow0
\]
has length \(n\), supported at \(P\), and \(H^0(Q_n)\) has dimension \(n\). The cohomology sequence therefore gives
\[
h^0(\mathcal O_D(nP))\ge 1+n-g .
\]
For \(n>g\) there is a section, viewed as a rational function \(f\), outside the constant line. At each point the valuation description extends \(f\) to a map
\(h:D\to\mathbf P^1_k\): use \((f:1)\) when \(f\) is regular, and \((1:f^{-1})\) at a pole. These formulas agree where both are defined.

The map \(h\) is proper, by its closed graph and properness of \(D/k\). It is quasi-finite. Over a closed point, its fibre is the zero or pole divisor of a nonconstant rational function and has finitely many points. Its generic fibre is finite because \(k(D)/k(f)\) is an algebraic finitely generated field extension, hence finite. The precise proper quasi-finite scheme theorem, AG-MO, *Zariski's Main Theorem*, Theorem 5.1, makes \(h\) finite.

Its line bundle \(H=h^*\mathcal O_{\mathbf P^1}(1)\) is ample, with an explicit affine-section test. The pulled-back coordinate sections \(s_0,s_1\) have affine nonvanishing opens, since \(h\) is finite. Given a principal open \(D(a)\) in \(D_{s_i}\), the denominator extension lemma, AG-QC, *Serre's theorems*, Lemma 1.1, writes \(a=b/s_i^m\) for a global section \(b\) of \(H^m\). The nonvanishing open of \(bs_i\) is exactly \(D(a)\), and is contained in \(D_{s_i}\). Such opens form a basis. Thus \(H\) is ample. Lemma 1.3 of that same provider gives a closed immersion of proper \(D\) in projective space.

The inverse images of the two standard affine opens of \(\mathbf P^1\), and their intersection, are affine. Their two-term Čech complex consequently gives \(H^q(D,F)=0\) for \(q>1\) and every quasi-coherent \(F\).

Choose a nonzero rational section of a line bundle \(N\). In a local frame it has a valuation at every closed point. Only finitely many are nonzero: on each member of a finite affine trivializing cover the section is a quotient of two nonzero functions, whose zero loci on the integral Noetherian curve are finite. The resulting divisor \(A=\sum_P a_PP\) identifies \(N\) with \(\mathcal O_D(A)\): at \(P\), multiplication by the rational section takes \(t^{-a_P}\) to a unit times the local frame. For every divisor \(A\), including those with negative coefficients,
\[
0\longrightarrow\mathcal O_D(A)
 \longrightarrow\mathcal O_D(A+P)
 \longrightarrow k(P)\longrightarrow0
\]
has a quotient of length one. Additivity of Euler characteristic, proved in AG-QC, *Euler characteristics and Hilbert polynomials*, Proposition 1.1, yields
\[
\chi(\mathcal O_D(A))=\chi(\mathcal O_D)+\sum_P a_P.
\]
Since \(H^0(\mathcal O_D)=k\) and higher cohomology stops in degree one, this is (E.1). It identifies the divisor degree with the Euler-characteristic definition. A principal divisor has degree zero because its line bundle is trivial, so the divisor degree is independent of the rational section. Adding divisors proves tensor additivity.

A nonzero regular section of \(N\) gives an effective divisor by the same local calculation. Its degree is the sum of nonnegative orders, or equivalently its finite length. Negative degree therefore excludes such a section. \(\square\)

**Lemma 6.0.2 (Riemann–Roch and positive-degree vanishing).** For the curve of Lemma 6.0.1, its dualizing sheaf \(\omega_D\) is a line bundle, and
\[
H^1(D,N)^\vee\cong H^0(D,\omega_D\otimes N^{-1}),\qquad
\deg\omega_D=2g-2.                                          \tag{E.2}
\]
Consequently
\[
h^0(D,N)-h^0(D,\omega_D\otimes N^{-1})=\deg N+1-g.             \tag{E.3}
\]
If \(g=1\) and \(\deg N=d>0\), then
\[
H^1(D,N)=0,\qquad h^0(D,N)=d.                                \tag{E.4}
\]
All these assertions include characteristics \(2\) and \(3\).

*Proof.* The actual duality provider is AG-QC Lesson 15, *Dualizing sheaves and Serre duality for projective schemes*, Theorem 4.2, with the local and adjunction proofs in §§2–4. A smooth projective curve is Cohen–Macaulay and equidimensional of dimension one, so its stated hypotheses hold.

We also verify the required invertibility, rather than infer it merely from Cohen–Macaulayness. Embed \(D\) in \(\mathbf P^N_k\). At a point, the surjection from the regular ambient local ring \(R\) to the regular curve local ring \(B\) has kernel generated by a regular sequence of length \(N-1\). To see this, lift a basis of the kernel of the surjection of cotangent spaces and complete it to a regular parameter system in \(R\). Quotienting by those \(N-1\) parameters gives a regular local ring of the dimension of \(B\), which is zero at the generic point and one at a closed point. Its surjection onto \(B\) has zero kernel: in the zero-dimensional case the source is a field; in the one-dimensional case a nonzero ideal in the discrete valuation source would make the quotient zero-dimensional. The local Koszul resolution therefore makes
\[
\mathcal E xt_{\mathbf P^N}^{N-1}
             (\mathcal O_D,\omega_{\mathbf P^N})
\]
locally free of rank one on \(D\). This is the dualizing sheaf constructed in the provider's Theorem 4.1.

Theorem 4.2 with \(F=N\) and \(i=0\) is the first comparison of (E.2): Hom from a line bundle is \(H^0(\omega_D\otimes N^{-1})\). With \(F=\mathcal O_D\) and \(i=0,1\), it gives
\[
h^0(\omega_D)=g,\qquad h^1(\omega_D)=1.
\]
Thus \(\chi(\omega_D)=g-1\), and Lemma 6.0.1 gives
\(\deg\omega_D=(g-1)-(1-g)=2g-2\). Equation (E.3) now follows from (E.1) and duality. For \(g=1\), the degree of \(\omega_D\otimes N^{-1}\) is \(-d\). Lemma 6.0.1 makes its global sections zero. Duality and (E.1) give (E.4). \(\square\)

Equations (E.1)–(E.3) derive the curve Riemann–Roch interface from projective Serre duality. They apply before a Weierstrass equation is chosen.

**Lemma 6.0.3 (the degree-three geometric embedding).** A line bundle of degree at least \(3\) on a smooth proper connected genus-one curve over an algebraically closed field is very ample.

*Proof.* Every finite subscheme of the smooth curve is an effective Cartier divisor, by the discrete valuation calculation. For a point \(P\), the line bundle \(N(-P)\) has positive degree, and its \(H^1\) vanishes by Lemma 6.0.2. Thus global sections generate \(N\) at every closed point, and hence everywhere by Nakayama. For every subscheme \(Z\) of length two, \(N(-Z)\) again has positive degree. The sequence
\[
0\longrightarrow N(-Z)\longrightarrow N\longrightarrow N|_Z
 \longrightarrow0
\]
therefore makes the evaluation onto \(N|_Z\) surjective. This separates distinct points and tangent directions, including the divisor \(2P\).

Here is the resulting closed-immersion argument. The complete system defines a map \(i:D\to\mathbf P(H^0(N))\), using the quotient convention for projective space. It is proper. Choose two independent sections \(s_0,s_1\); their ratio is a nonconstant rational function and gives a finite map \(D\to\mathbf P^1\) as in Lemma 6.0.1. In the target chart with coordinate \(s_0\ne0\), a fibre of \(i\) is contained in a fibre of that finite map. Outside that chart its source is contained in the finite zero divisor of \(s_0\). Thus \(i\) is quasi-finite and hence finite by the same proper quasi-finite theorem.

Over a closed target point a nonempty fibre has exactly one point, by separation of pairs. The separation of \(2P\) makes its cotangent space zero: in a local generating frame, the ratios of sections have a nonzero linear part and span the curve's cotangent space. The finite local fibre algebra therefore has maximal ideal \(\mathfrak m\) with \(\mathfrak m/\mathfrak m^2=0\). Nakayama gives \(\mathfrak m=0\), so that fibre is \(k\). The finite cokernel of
\(\mathcal O_{\mathbf P(H^0(N))}\to i_*\mathcal O_D\) vanishes on every closed fibre. Nakayama and the Jacobson property of finite-type \(k\)-schemes make it zero. Hence \(i\) is a closed immersion. \(\square\)

For the smooth cubic below, the genus computation has its own earlier provider. AG-QC Lesson 4, *Cohomology of projective space*, Lemma 2.1 and Theorem 2.2, compute every twist over every ring. On a geometric plane cubic its exact equation sequence
\[
0\to\mathcal O_{\mathbf P^2}(-3)\to\mathcal O_{\mathbf P^2}
  \to\mathcal O_D\to0
\]
gives \(H^0(\mathcal O_D)=k\), \(H^1(\mathcal O_D)=k\), and no higher cohomology: the only top class in degree \(-3\) is \(1/(XYZ)\), and intermediate projective-plane cohomology is zero. This establishes connectedness and genus one of the smooth geometric fibres in Lemma 6.1, independently of the relative Weierstrass construction.

#### 6.0.2. A cohomology complex over an arbitrary base

**Lemma 6.0.4 (the arbitrary-base line-bundle complex).** Let \(f:X\to\operatorname{Spec}A\) be a proper flat morphism of finite presentation of schemes, and let \(M\) be a line bundle on \(X\). There is a finite complex \(K\) of finite projective \(A\)-modules in nonnegative degrees, with canonical, functorial comparisons
\[
H^q(K\otimes_A B)\cong H^q(X_B,M_B)                            \tag{E.5}
\]
for every \(A\)-algebra \(B\). The same comparison holds for tensoring by any \(A\)-module. Neither \(A\) nor \(B\) is assumed Noetherian.

*Proof.* Write \(A\) as the filtered union of its finitely generated \(\mathbf Z\)-subalgebras \(A_i\). The finite-presentation descent and invertible-module descent providers give a pair \((X_i,M_i)\), with specified base-change identification \((X_i,M_i)_A\cong(X,M)\). Increase \(i\) so that \(X_i/A_i\) is proper and flat. These are separate, exact eventual-property statements, not consequences merely of having written a model. The coherent-existence treatment assigned to [Lesson 8](moduli-stacks-are-algebraic.md#reader-section-2) supplies these through the incorporated lemmas “Eventually proper” and “Descend flat finite presentation”, together with “Descend finite presentation” and “Descend invertible modules”. Its cohomological Bridge 2 and arbitrary-base passage provide this approximation interface. These proofs are written in [Lesson 8, Appendix A §§A.2–A.4](moduli-stacks-are-algebraic.md#reader-section-2), with invertible-module descent at [its exact supporting lemma](moduli-stacks-are-algebraic.md#native-spaces-limits-lemma-descend-invertible-modules); the genuine scheme-approximation foundations of *Limits of schemes and approximation* (AG-MO-03) retain their written or planned states.

The ring \(A_i\) is Noetherian. The line bundle \(M_i\) is coherent and flat over \(A_i\): the model is flat, and a line bundle is locally a copy of its structure sheaf. We may therefore apply the actual AG-QC Lesson 8, *Base change and the Grothendieck complex*, Theorem 3.2, whose base is explicitly Noetherian.

That proof gives a fixed chain map \(K_i\to C_i\), where \(K_i\) is finite projective in nonnegative degrees and \(C_i\) is the finite affine-cover Čech complex of \(M_i\). Properness ensures separation, so its intersections are affine. Lemma 3.1 of the same provider proves that this map remains a quasi-isomorphism after tensoring with every \(A_i\)-module.

Put \(K=K_i\otimes_{A_i}A\). For an \(A\)-algebra \(B\), the specified model identifies \(X_B\) with \((X_i)_B\) and \(M_B\) with \((M_i)_B\). On each affine intersection the section module pulls back by ordinary tensor product. Thus \(C_i\otimes_{A_i}B\) is precisely the Čech complex of \(M_B\), and
\[
K\otimes_A B=K_i\otimes_{A_i}B
 \longrightarrow C_i\otimes_{A_i}B
\]
is the asserted quasi-isomorphism. This is the return from the Noetherian model to the original family, including every nonflat base change. For an \(A\)-module the same affine section calculation proves the module version.

All comparisons come from the fixed chain map and the actual affine tensor identifications. They respect morphisms and successive base changes, and compute the canonical cohomology comparisons defined in Lesson 8, §1. Different finite covers or models give the same canonical derived comparison. Localizing on the parameter scheme gives the corresponding sheaf statements. In particular no assumption about genus or the degrees at the unused fibres of \(X_i/A_i\) was introduced: the model theorem needs only properness and the flat coherent line bundle. \(\square\)

This is the line-bundle specialization of the broader algebraic-space Bridge 2 in Lesson 8’s coherent-existence treatment. That bridge allows a perfect \(P\), a bounded relatively flat finitely presented complex \(F\), and proper support, and proves perfection of \(Rf_*(P\otimes^{\mathbf L}F)\) with arbitrary base change. Here \(P=\mathcal O_X\) and \(F=M[0]\); properness of \(X/A\) supplies the support condition and separation. The present deduction retains the narrower scheme hypotheses of the Noetherian provider, then explains their actual arbitrary-base extension.

**Proposition 6.0.5 (cohomology of genus-one families).** For the family \(p:C\to T\) at the start and a line bundle \(M\) of positive degree \(d_{\bar t}\) on every geometric fibre,
\[
R^qp_*M=0\quad(q>0),\qquad p_*M\ \text{is finite locally free},
                                                               \tag{E.6}
\]
with rank \(d_{\bar t}\) at \(t\). Formation of \(p_*M\) commutes with every base change. The ranks are consequently locally constant. Moreover
\[
\mathcal O_T\xrightarrow{\sim}p_*\mathcal O_C,\qquad
R^1p_*\mathcal O_C\ \text{is an invertible module},\qquad
R^qp_*\mathcal O_C=0\quad(q>1),                                 \tag{E.7}
\]
and these canonical direct images also commute with every base change. The family need not have a section.

*Proof.* Work on an affine open of \(T\). Smoothness gives flatness, and Lemma 6.0.4 applies to \(M\). On a geometric fibre, Lemma 6.0.2 gives cohomology only in degree zero, of dimension \(d_{\bar t}\). The same assertions hold over the residue field: extension to its algebraic closure is faithfully flat, and the affine-cover complex computes that extension by tensor product.

Fix a point of the base and locally trivialize the finite projective terms of \(K\). If a differential has an entry nonzero at the residue field, it is a unit on a neighbourhood. Row and column operations split off a two-term identity complex; the chain identities make the adjacent entries in that block zero. Repeat finitely many times. The remaining differentials vanish after reduction to the residue field. Its terms therefore equal its fibre cohomology there. All terms except degree zero have zero fibre; finite generation and Nakayama remove them on a neighbourhood. The degree-zero term has rank \(d_{\bar t}\). We have thus obtained a homotopy-equivalent finite free complex concentrated in degree zero. This homotopy equivalence remains one after every tensor product. Equation (E.5) proves (E.6), including the canonical comparison for every base change.

For \(M=\mathcal O_C\), geometric fibre cohomology is \(k\) in degrees zero and one, and zero elsewhere. The same cancellation leaves a two-term complex of rank-one free modules in degrees zero and one near the chosen point. The unit of the structure sheaf is indispensable here. It gives the actual derived map \(A[0]\to K\), represented by a cycle \(v\in K^0\), since \(A[0]\) is projective. On the residue field this cycle is the nonzero constant function, so it is a basis of \(K^0\) after shrinking. Since \(dv=0\), the remaining differential is zero. Thus locally
\[
K\cong A[0]\oplus A[-1],
\]
with the unit identifying the first summand. Tensoring this zero-differential model proves (E.7), including all canonical cohomology comparisons. The rank-one module in degree one is intrinsic as \(R^1p_*\mathcal O_C\), though its displayed free frame was a local choice. Quasi-coherent localization and the canonical comparison maps glue these conclusions on arbitrary \(T\). \(\square\)

#### 6.0.3. The section and its principal parts

**Lemma 6.0.6 (the section divisor over every base).** Suppose \(e:T\to C\) is a section. It is a closed effective Cartier divisor. Its line bundle \(L=\mathcal O_C(e)\) pulls back canonically to \(\mathcal O_{C'}(e')\) after every base change, and has degree one on every geometric fibre.

*Proof.* The section is closed because \(p\) is separated. Locally on \(T\), take an affine neighbourhood of its image on which \(C\to T\) is finitely presented. The augmentation of its algebra by the section has a finitely generated ideal \(I\): if the algebra generators are \(z_j\), the differences \(z_j-e^*z_j\) generate its kernel. The augmentation also identifies
\[
I/I^2\cong e^*\Omega_{C/T},
\]
by the universal property of relative derivations. This is a line bundle, since the relative dimension is one along the section.

Use the first clause of AG-FSE, *Smooth morphisms*, Theorem 4.1 to choose an étale coordinate \(z:C\to\mathbf A^1_T\) near a given section point. Translate it by \(e^*z\), and put \(h=z-e^*z\). The function \(h\) vanishes on the section and its class generates \(I/I^2\). Its zero is a nonzerodivisor because the translated coordinate map is étale, hence flat, and the coordinate of \(\mathbf A^1_T\) is a nonzerodivisor over every ring. Nakayama applied to the finite module \(I/(h)\) makes \(I=(h)\) near the section point. This proves the effective Cartier assertion, including over non-Noetherian and nonreduced bases.

In \(0\to I\to\mathcal O_C\to e_*\mathcal O_T\to0\), the quotient is flat over \(T\). Tensoring by any new base ring therefore stays exact. It identifies the pulled-back ideal with the ideal of \(e'\). Dualizing the invertible ideal gives the specified comparison for \(L\). On a geometric fibre, that ideal is the maximal ideal of the smooth rational point \(e_{\bar t}\), with order one. Lemma 6.0.1 makes its line bundle have degree one. \(\square\)

Put \(F_n=p_*L^n\) for \(n\ge1\), and \(N=e^*L\). Proposition 6.0.5 gives finite local freeness of \(F_n\), of rank \(n\), and formation of every \(F_n\) commutes with arbitrary base change. It also gives \(R^qp_*L^n=0\) for \(q>0\).

The section \(1\) generates \(F_1\): on every geometric fibre it is nonzero in a one-dimensional space, so the map \(\mathcal O_T\to F_1\) is an isomorphism. For \(n\ge2\), the exact Cartier sequence and positive-degree vanishing give canonical short exact sequences
\[
0\longrightarrow F_{n-1}\longrightarrow F_n
 \longrightarrow e^*L^n\longrightarrow0.                       \tag{E.8}
\]
Every comparison in (E.8) commutes with every base change. The last term is \(N^n\). For \(a,b\ge2\), restriction of products induces the usual multiplication
\(N^a\otimes N^b\to N^{a+b}\) on these quotients: a product involving \(F_{a-1}\) or \(F_{b-1}\) lies in \(F_{a+b-1}\). Thus principal parts of products are the products of principal parts. Choosing complements \(x\) and \(y\) in ranks two and three therefore gives the pole-order bases used in Lemma 6.2. Lemma 6.0.3 supplies the very ampleness of \(L_{\bar t}^3\) used there. Generation on fibres gives generation of \(L^3\) by the three relative sections by Nakayama, with no Noetherian assumption on \(T\).

The same sequence for \(n=1\), with \(p_*\mathcal O_C\cong F_1\), makes its connecting map a canonical isomorphism
\[
N\xrightarrow{\sim}R^1p_*\mathcal O_C .
\]
This records the precise normal-line comparison for a pointed family; choosing a frame is unnecessary for the cohomology statement.

For the remaining smooth-atlas uses, the exact existing section contract is AG-FSE, *Smooth morphisms*, Theorem 5.2: if a point of the base lies in the image of a smooth scheme morphism, there is an étale neighbourhood of that point with a section of its pullback. The theorem and its proof impose no Noetherian condition and do not prescribe a section through an arbitrary specified fibre point. A smooth surjection supplies such neighbourhoods covering the base; for a smooth morphism of algebraic spaces, first use an étale scheme atlas. This is precisely the local lifting used in Lemma 7.1.

The existing polarized graded-algebra descent in §6.4, now uses the proved \(F_{3n}\) base-change maps and its intrinsic line bundle \(\mathcal O_C(3e)\). Its multiplication, unit and cubic-relation descent remain that section's written proof. The support insert supplies the cohomology and geometric degree inputs to it; the graded-algebra effectivity argument does not need to be repeated.

The geometric degree and Riemann–Roch arguments, the local complex calculation and the Cartier-section comparisons above are independently expressed programme writing under CC0. Their cited human cohomology, duality, ample-line and approximation providers retain their actual source terms. The ordinary proper quasi-finite theorem is *Zariski’s Main Theorem* (AG-MO-12), Theorem 5.1, with its existing foundation contract.

### 6.1. A smooth universal cubic in every characteristic

For coefficients \(a=(a_1,a_2,a_3,a_4,a_6)\), define
\[
\begin{aligned}
b_2&=a_1^2+4a_2,& b_4&=a_1a_3+2a_4,\\
b_6&=a_3^2+4a_6,&
b_8&=a_1^2a_6+4a_2a_6-a_1a_3a_4+a_2a_3^2-a_4^2,\\
\Delta&=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6.
\end{aligned}
\tag{6.1}
\]
Let
\[
W=\operatorname{Spec}\mathbf Z[a_1,a_2,a_3,a_4,a_6,\Delta^{-1}].
\tag{6.2}
\]
The plane cubic \(E_a\) has equation
\[
Y^2Z+a_1XYZ+a_3YZ^2
=X^3+a_2X^2Z+a_4XZ^2+a_6Z^3,
\tag{6.3}
\]
with section \(e=(0:1:0)\).

**Lemma 6.1.** For any coefficient ring, (6.3) is a flat projective family of plane cubics. A geometric fibre is smooth if and only if \(\Delta\ne0\). Consequently (6.3) over \(W\) is an elliptic curve.

*Proof.* Regard its homogeneous equation \(F\) as a polynomial in \(X\) over \(R[Y,Z]\), with coefficient \(-1\) of \(X^3\). The quotient by \(F\) is a free \(R[Y,Z]\)-module with basis \(1,X,X^2\), compatible with the grading. Every graded piece is finite free over \(R\); homogeneous localizations and their degree-zero direct summands are \(R\)-flat. They cover the relative Proj, proving flatness. The equation defines a closed subscheme of \(\mathbf P^2_R\), so the family is projective and finitely presented.

Work now over an algebraically closed field. At infinity the only point is \(e\); the derivative with respect to \(Z\) at \(e\) is \(1\), so this point is smooth. On \(Z=1\) the equation is
\[
y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6.
\tag{6.4}
\]
If the characteristic is different from \(2\), put \(z=2y+a_1x+a_3\). Then (6.4) becomes
\[
z^2=4x^3+b_2x^2+2b_4x+b_6.
\]
The cubic on the right has discriminant \(16\Delta\). This follows by inserting its four coefficients in the polynomial discriminant formula and using \(b_2b_6-b_4^2=4b_8\). A singular point is exactly a repeated root of that cubic, with \(z=0\); hence smoothness is equivalent to \(\Delta\ne0\). This argument includes characteristic \(3\).

In characteristic \(2\), the two affine derivatives are \(a_1x+a_3\) and \(a_1y+x^2+a_4\). If \(a_1\ne0\), their unique common zero is
\[
x=a_3/a_1,\qquad y=(x^2+a_4)/a_1.
\]
Substitution in \(F(x,y,1)\) gives \(a_1^6F(x,y,1)=\Delta\); thus this common zero lies on the curve exactly when \(\Delta=0\). If \(a_1=0\), (6.1) gives \(\Delta=a_3^4\). When \(a_3\ne0\), the \(y\)-derivative never vanishes. When \(a_3=0\), choose \(x\) with \(x^2+a_4=0\), and then choose \(y\) solving (6.4); such a point is singular. This proves the criterion in the remaining characteristic.

Over \(W\), flatness, finite presentation and geometric smoothness imply smoothness by the scheme criterion [Stacks, Tag 01V8]. The projective-plane twist calculation in §6.0.1 gives \(H^0(E_{\bar t},\mathcal O)=\kappa(\bar t)\) and \(\dim H^1(E_{\bar t},\mathcal O)=1\). In particular each smooth geometric fibre is connected of genus one. Properness and the displayed section complete the elliptic-curve conditions. \(\square\)

### 6.2. Why every family locally has this equation

The needed inputs have now been proved: Lemma 6.0.6 makes the section a Cartier divisor; Lemmas 6.0.1–6.0.3 give the fibre degree, vanishing and very ampleness; Lemma 6.0.4 and Proposition 6.0.5 give the cohomology complex and canonical base changes over arbitrary parameter schemes.

**Lemma 6.2 (relative Weierstrass equation).** Every elliptic curve \((E,e)/T\) is Zariski locally isomorphic, as a pointed curve, to (6.3) for coefficients with \(\Delta\) invertible.

*Proof.* Let \(L=\mathcal O_E(e)\), and put \(F_n=p_*L^{\otimes n}\) for \(n\ge1\). The inputs just stated show that \(F_n\) is locally free of rank \(n\), and that its formation commutes with every base change.

Here is the deduction from the cohomology input, including its arbitrary-base content. Over an affine open of \(T\), Lemma 6.0.4 represents \(R\Gamma(E,L^n)\), compatibly with base change, by a finite complex of finite projective modules. At each residue field its cohomology is concentrated in degree zero and has dimension \(n\). Locally trivialize the projective modules and cancel every differential entry that is a unit at the chosen point, splitting off two-term contractible complexes. The remaining complex has zero differentials after reduction to that residue field. Therefore its terms in degrees other than zero vanish there; Nakayama and localization remove those terms on a neighbourhood. Its degree-zero term has rank \(n\). This proves the local freeness and all the asserted base changes.

The constant section \(1\) is nonzero in \(H^0(L_{\bar t})\), so it generates the rank-one bundle \(F_1\). The inclusions \(F_n\hookrightarrow F_{n+1}\) for \(n\ge1\) have locally free rank-one cokernels: on each geometric fibre they are injective maps of ranks \(n,n+1\), and an invertible maximal minor locally splits each inclusion. Choose, after shrinking \(T\), a section \(x\in F_2\) complementary to \(1\), and a section \(y\in F_3\) complementary to \(1,x\).

Principal parts along \(e\) control their products. For \(n\ge2\), the exact sequence
\[
0\to L^{n-1}\to L^n\to e_*(L^n|_e)\to0
\]
and the vanishing of \(R^1p_*L^{n-1}\) identify \(F_n/F_{n-1}\) with \(L^n|_e\). The leading principal parts of \(x,y\) are units in the appropriate rank-one modules. Their products therefore have nonzero, generating leading parts. Successively,
\[
1,\ x,\ y,\ x^2,\ xy,\ x^3
\tag{6.5}
\]
form a basis of \(F_6\), with pole orders \(0,2,3,4,5,6\). The other section \(y^2\) has order \(6\). Its coefficient of \(x^3\) in (6.5) is a unit \(c\). Replacing \(x,y\) by \(cx,cy\) makes this coefficient \(1\), without extracting any root. The unique resulting relation has the form (6.4).

For completeness, these functions give an isomorphism of the original family with the cubic, not just a birational equation. The three sections \(1,x,y\) generate \(L^3\): they do so on each geometric fibre, since degree \(3\) is very ample on a genus-one curve, and their cokernel vanishes by Nakayama. The very-ampleness assertion on a fibre follows from the degree-one vanishing after removing any length-two subscheme; global sections then separate both pairs of points and tangent directions. Thus they define a map
\[
E\longrightarrow\mathbf P^2_T
\]
whose geometric fibres are closed immersions. This map is proper, since \(E\to T\) is proper and \(\mathbf P^2_T\to T\) separated. It has finite fibres, hence is finite by [Stacks, Tag 02LS]. The cokernel of \(\mathcal O_{\mathbf P^2_T}\to\phi_*\mathcal O_E\) is a finite-type module, and vanishes after every residue-field base change because the fibre maps are closed immersions. Nakayama makes that map surjective, so \(\phi\) is a closed immersion.

The homogeneous version of the relation (6.4) vanishes on \(E\), and at \(e\) the coordinates are \((0:1:0)\): with a local equation \(t\) for \(e\), the sections of \(L^3\) have orders \(t^3,t,t^0\). Let \(C\) be the cubic defined by this relation. Each geometric fibre of \(E\hookrightarrow C\) is an equality. Indeed, the embedded genus-one curve has degree \(3\), and its cubic relation is its plane equation. Both \(C\) and \(E\) are flat over \(T\). Thus the ideal of \(E\) in \(C\) has zero residue-field fibres: tensor the sequence \(0\to I\to\mathcal O_C\to\mathcal O_E\to0\), using flatness of \(\mathcal O_E\). This ideal is of finite type, since the closed immersion is of finite presentation. Nakayama gives \(I=0\). Hence \(E=C\).

Every geometric fibre is smooth, so Lemma 6.1 makes \(\Delta\) nonzero at every point of \(T\). On the affine neighbourhood under consideration this means that \(\Delta\) is a unit. \(\square\)

### 6.3. All changes of equation

Let \(\Gamma=\operatorname{Spec}\mathbf Z[u,u^{-1},r,s,t]\). It parametrizes changes of affine coordinates
\[
x=u^2x'+r,\qquad
y=u^3y'+u^2s x'+t.
\tag{6.6}
\]
Substitution and division by \(u^6\) produce new coefficients \(a'=a\cdot\gamma\):
\[
\begin{aligned}
u a'_1&=a_1+2s,\\
u^2 a'_2&=a_2-sa_1+3r-s^2,\\
u^3 a'_3&=a_3+ra_1+2t,\\
u^4 a'_4&=a_4-sa_3+2ra_2-(t+rs)a_1+3r^2-2st,\\
u^6 a'_6&=a_6+ra_4+r^2a_2+r^3-ta_3-rta_1-t^2.
\end{aligned}
\tag{6.7}
\]
Composition of the substitutions makes \(\Gamma\) a group scheme, with product
\[
(u,r,s,t)(v,r',s',t')
=\bigl(uv,\ r+u^2r',\ s+us',\ t+u^2sr'+u^3t'\bigr).
\tag{6.8}
\]
The identity is \((1,0,0,0)\); the inverse is obtained uniquely by solving (6.8). These formulas define a smooth group scheme over \(\mathbf Z\), with underlying scheme \(\mathbf G_m\times\mathbf A^3\).

Equation (6.7) is a right action. It preserves \(W\), since
\[
\Delta(a\cdot\gamma)=u^{-12}\Delta(a).
\tag{6.9}
\]
One verification of (6.9) works first over the universal rational coefficient ring: in the square-completed equation, (6.6) takes the cubic \(f(x)\) to \(u^{-6}f(u^2x'+r)\); its discriminant is multiplied by \(u^{-12}\). Clearing denominators gives a polynomial identity in the torsion-free ring \(\mathbf Z[a_i,u,u^{-1},r,s,t]\), so it holds over every coefficient ring, including characteristics \(2\) and \(3\). To use the left-action convention of §5, set \(\gamma\cdot a=a\cdot\gamma^{-1}\). Both conventions describe the same quotient.

**Lemma 6.3.** A pointed isomorphism between two Weierstrass curves over the same scheme is given by a unique change (6.6), with the coefficients related by (6.7), taking account of the direction of the isomorphism.

*Proof.* Suppose the isomorphism takes the primed curve to the unprimed curve. It preserves \(e\), and hence the inclusions in the pole-order filtration \(F_n\). The bases constructed in Lemma 6.2, or their explicit versions on (6.3), give
\[
x=\lambda x'+r,\qquad
y=\mu y'+\nu x'+t
\]
after pullback, with \(\lambda,\mu\) units. Comparing the degree-six leading relation \(y^2=x^3+\text{lower pole order}\) gives \(\mu^2=\lambda^3\). Put \(u=\mu/\lambda\); then \(u^2=\lambda\) and \(u^3=\mu\), over an arbitrary ring. Set \(s=\nu/u^2\). This gives (6.6), uniquely. The comparison of the equations gives exactly (6.7).

Conversely, a substitution satisfying (6.7) extends to an invertible projective linear change of \((X,Y,Z)\), maps the primed cubic isomorphically onto the unprimed cubic, and fixes \((0:1:0)\). For curves with global Weierstrass equations, the coefficients just found are global sections: the filtration bases are global, so local coefficient computations agree on every overlap. \(\square\)

### 6.4. Descent of elliptic curves

**Lemma 6.4.** The category \(\mathcal M_{1,1}\) is a stack for the fppf topology.

*Proof.* Isomorphisms of two fixed elliptic curves are an fppf sheaf. Indeed, after a base cover, the corresponding cover of the first curve is fpqc. Morphisms from it to the second curve descend uniquely by fpqc descent of scheme morphisms [Stacks, Tag 023Q]. The inverse morphisms descend as well, and the two inverse identities and preservation of the section can be checked on that cover. This proves the sheaf condition for Isom.

For effectivity, work first over an affine \(T\), and refine a given fppf cover by a finite collection of affine pieces whose images cover \(T\), as in Lemma 1.4. We have a single affine faithfully flat cover \(T'\to T\) of finite presentation, an elliptic curve \(E'/T'\), and isomorphisms over \(T'\times_TT'\) satisfying the cocycle. Put \(L'=\mathcal O_{E'}(e')\). Since every transition preserves the section, it supplies the canonical descent isomorphism of \(L'\), compatible with its tensor powers and the cocycle.

Consider the graded algebra
\[
A'=\bigoplus_{n\ge0}p'_*(L'^{\,3n}).
\tag{6.10}
\]
Its degree zero is \(\mathcal O_{T'}\): the inclusion \(p'_*\mathcal O_{E'}\hookrightarrow F_1\) and the isomorphism \(\mathcal O_{T'}\xrightarrow{1}F_1\) in Lemma 6.2 force this equality. For \(n\ge1\), its degree \(n\) is locally free of rank \(3n\) and commutes with arbitrary base change. Thus the transitions induce descent data on every graded component, as well as compatible multiplication and unit maps. Effective and fully faithful module descent [Stacks, Tag 023T] gives a graded quasi-coherent algebra \(A\) on \(T\). Its positive components are finite locally free by faithful flat descent, as recalled in Lesson 4.

This algebra is generated in degree one with a finitely generated cubic ideal of relations. To verify this assertion, work Zariski locally on \(T'\) in the Weierstrass coordinates of Lemma 6.2. The exact sequence of a plane cubic, twisted by \(n\), and the vanishing of \(H^1(\mathbf P^2_R,\mathcal O(n-3))\) [Stacks, Tag 01XT] identify (6.10) with the homogeneous algebra \(R[X,Y,Z]/(F)\). Hence the degree-one symmetric algebra maps onto every component. Surjectivity descends under the faithfully flat cover. The kernel \(K_3\) in degree three is a locally free rank-one module, since locally its generator is the cubic equation and the degree-three quotient is locally free. Its generated homogeneous ideal equals the full kernel after pullback to \(T'\), and therefore before pullback as well. This makes
\[
E=\operatorname{Proj}_T(A)
\tag{6.11}
\]
a closed, finitely presented subscheme of the projective bundle \(\mathbf P_T(A_1)\).

Relative Proj commutes with base change. The same local cubic calculation identifies \(E\times_TT'\) with \(E'\); these identifications respect the prescribed transitions, because they come from the canonical graded section algebra. The local sections \(e'\) now descend to \(e:T\to E\), using descent of morphisms into the fixed scheme \(E\). Properness, smoothness and finite presentation descend along \(T'\to T\). The geometric fibres of \(E\) have the elliptic-curve conditions because they acquire those conditions after a faithfully flat field extension and are the fibres of \(E'\). Thus (6.11), with \(e\), is the required elliptic curve.

For a general cover, the construction on its finite affine refinements recovers the original datum: on the original cover, the comparison isomorphisms exist on a common refinement and agree there by the original cocycle, so the Isom sheaf condition glues them. For a general \(T\), construct the curve on affine opens and glue it over their intersections, again using that condition. Arrows descend uniquely by the first paragraph. This proves both full faithfulness and effectivity of descent. \(\square\)

The polarization in this proof is intrinsic: \(L^3=\mathcal O_E(3e)\). It is preserved by every allowed isomorphism. A statement that arbitrary projective schemes descend as schemes, without specifying compatible polarizations, would not justify this argument.

**Theorem 6.5 (the elliptic-curve atlas).** There is an equivalence
\[
\mathcal M_{1,1}\simeq[W/\Gamma],
\tag{6.12}
\]
with the action convention of §6.3. In particular, \(\mathcal M_{1,1}\) is algebraic, and the family (6.3) defines a smooth surjective atlas \(W\to\mathcal M_{1,1}\) [Stacks, Tags 072S, 072T].

*Proof.* The Weierstrass family defines a functor from the action prestack to \(\mathcal M_{1,1}\). In the right-action convention, \(\gamma:a\to a\cdot\gamma\) is sent to the inverse of the isomorphism \(E_{a\cdot\gamma}\to E_a\) in (6.6). Composition agrees by (6.8). Lemma 6.3 makes this functor fully faithful on Isom sheaves. Lemma 6.2 makes it locally essentially surjective for the Zariski topology, hence for the fppf topology.

Since the target is a stack by Lemma 6.4, the functor extends to (6.12) by stackification. Its full faithfulness is checked on a cover where the two objects are equations. For essential surjectivity, choose local Weierstrass equations for an elliptic curve. Their pointed comparison isomorphisms give unique coordinate changes by Lemma 6.3; uniqueness makes these changes satisfy the groupoid cocycle. They therefore descend to a quotient-stack object, whose image is the original elliptic curve. This proves the equivalence.

The group scheme \(\Gamma\to\operatorname{Spec}\mathbf Z\) is smooth, so Proposition 5.1 applies. More explicitly, a base change of the atlas by \((E,e)/T\) is the space of pointed Weierstrass equations for that curve, with a specified identification. Lemma 6.2 gives local sections, and Lemma 6.3 says that two such sections differ by a unique element of \(\Gamma\). It is a Zariski locally trivial \(\Gamma_T\)-torsor, hence a scheme, smooth and surjective over \(T\). This also verifies the atlas tests directly. \(\square\)

The torsor in the last paragraph is representable by a scheme by gluing its copies of \(\Gamma_{T_i}\) along the open overlaps. It is the functor that remembers the comparison isomorphism; forgetting that isomorphism would quotient out stabilizers and would not give the same atlas test.

### 6.5. What the coordinates reveal

Define
\[
c_4=b_2^2-24b_4,\qquad
c_6=-b_2^3+36b_2b_4-216b_6.
\]
Direct expansion gives \(c_4^3-c_6^2=1728\Delta\). Under (6.6), \(c_4\) and \(c_6\) have weights \(4,6\), while \(\Delta\) has weight \(12\), with the inverse powers of \(u\) as in (6.9). The same square-completion calculation followed by the universal integral polynomial argument proves these transformation identities in every characteristic. Therefore
\[
j=c_4^3/\Delta
\tag{6.13}
\]
is invariant and defines a morphism \(\mathcal M_{1,1}\to\mathbf A^1_{\mathbf Z}\). Equivalently, its values on locally chosen equations agree on overlaps, and scheme-valued maps descend as sheaves.

When \(6\) is invertible, complete the square and translate \(x\) to remove its square term. The equation becomes \(y^2=x^3+Ax+B\), with \(\Delta=-16(4A^3+27B^2)\). Comparing (6.7) for two such short equations forces \(s=0,r=0,t=0\); the remaining changes are scalings. Thus, over \(\mathbf Z[1/6]\),
\[
\mathcal M_{1,1}\simeq
\left[
\operatorname{Spec}\mathbf Z[1/6,A,B,(4A^3+27B^2)^{-1}]
\big/\mathbf G_m
\right],
\tag{6.14}
\]
where the left action has weights \(4,6\) on \(A,B\). This is a smaller smooth atlas. The long equation (6.3), rather than (6.14), is needed over \(\mathbf Z\).

Several properties can be read from the atlas [Stacks, Tag 072V]. In the definition of smoothness of an algebraic stack over a scheme, one asks for its smooth atlas to be smooth over that scheme; independence of the atlas follows by their common refinement and descent of smoothness for scheme morphisms. Since \(W\) is an open subscheme of affine five-space over \(\mathbf Z\), \(\mathcal M_{1,1}\to\operatorname{Spec}\mathbf Z\) is smooth. It has a quasi-compact atlas because \(W\) is affine. Its topological space is irreducible because \(W\) is irreducible and maps continuously and surjectively to it. Here the topology is the smooth-atlas quotient topology: an invariant subset is open precisely when its inverse image on an atlas is open, and the common-refinement argument makes this independent of the atlas. The image of any irreducible topological space under a continuous surjection is irreducible.

There is also a concrete description of quasi-coherent modules. Define a quasi-coherent module on a stack to be a compatible assignment of a quasi-coherent module to every scheme-valued object, with specified pullback isomorphisms and their coherence. On \([W/\Gamma]\), restriction gives a module \(M\) on \(W\), together with an isomorphism \(s^*M\cong t^*M\) on the action arrow space, satisfying the composition cocycle and the unit identity. Conversely, for each object over \(T\), pull \(M\) to the locally trivial torsor \(T\times_{\mathcal M_{1,1}}W\); the cocycle supplies descent data there. Module descent, and then its fully faithful statement for maps and arbitrary pullbacks, gives the compatible module on \(T\). These two constructions are inverse, since this can be checked after the torsor cover. Hence quasi-coherent modules on \(\mathcal M_{1,1}\) are exactly \(\Gamma\)-equivariant quasi-coherent modules on \(W\).

## 7. The original definition and the modern one

There are two distinctions to keep separate: the topology in which descent is formulated, and the representability and smoothness conditions on the atlas and diagonal.

**Lemma 7.1 (comparison of descent topologies in this situation).** Suppose \(\mathcal X\) is a stack for the étale topology on \(S\)-schemes, its diagonal is representable by algebraic spaces, and it has a representable smooth surjection \(U\to\mathcal X\) from a scheme. Then it is an fppf stack. If the given atlas is étale, it is a Deligne–Mumford stack in Definition 2.1.

*Proof.* The same fibre-product definitions give an algebraic space \(R=U\times_{\mathcal X}U\), with the groupoid structure (3.4) and smooth source and target. Thus \(Q=[U/R]_{\mathrm{fppf}}\) is algebraic by Theorem 3.2.

We first construct a fully faithful functor \(\mathcal X\to Q\). For \(x/T\), the space \(T\times_{\mathcal X}U\) is smooth and surjective over \(T\). A smooth surjection of schemes has sections étale locally on its target, by *Smooth morphisms* (AG-FSE-05), Theorem 5.2 at its arbitrary-base scope; for a space, first take an étale scheme atlas and apply that scheme fact. Therefore choose an étale cover \(T_i\to T\), maps \(u_i:T_i\to U\), and specified isomorphisms \(p(u_i)\to x|_{T_i}\). Their transition isomorphisms are arrows in \(R\), with the cocycle inherited from \(x\). They descend in \(Q\) to an object \(F(x)\). A morphism between two \(x\)'s gives compatible arrows on a common cover and hence a morphism in \(Q\). Changes of choices give the unique comparisons recovering the specified local arrows; their coherence follows from uniqueness after restriction. This defines the functor over the base site. Its map on Isom sheaves is an isomorphism on these covers, because \(R\) was defined by all Isom arrows in \(\mathcal X\), and hence globally. Thus \(F\) is fully faithful.

For \(q/T\) in \(Q\), Theorem 3.2 makes \(T\times_QU\to T\) smooth and surjective. Choose an **étale** cover with sections, using the same local-section fact. The resulting objects \(p(u_i)\) in \(\mathcal X\) have transition arrows lifted from the quotient: full faithfulness on their Isom sheaves identifies those arrows with arrows in \(\mathcal X\). Their cocycle holds there. Effectivity for the étale topology gives \(x/T\), and \(F(x)\cong q\). Hence \(F\) is an equivalence of fibred categories.

Since \(Q\) is an fppf stack, the equivalence transports fppf descent to \(\mathcal X\). If \(U\to\mathcal X\) is étale, then \(s,t\) are étale; the étale version of Theorem 3.2 makes the same atlas of \(Q\), and thus of \(\mathcal X\), étale. \(\square\)

Here are the conditions, with “representable” made explicit:

| Convention | Descent topology | Diagonal | Scheme atlas |
| --- | --- | --- | --- |
| Algebraic stack in this course | fppf | Representable by algebraic spaces | Smooth and surjective |
| Deligne–Mumford stack in this course | fppf | Representable by algebraic spaces | Étale and surjective |
| Deligne–Mumford, Definition (4.6), 1969 | Étale | Representable by schemes | Étale and surjective |

Lemma 7.1 removes the topology discrepancy. Thus the objects of Definition (4.6) are precisely the modern Deligne–Mumford stacks whose diagonal is representable by schemes. A smooth atlas alone does not satisfy that original definition; \(B\mathbf G_m\) demonstrates the difference. These are definitional distinctions, not an error in the older terminology.

The paper separately defines quasi-separatedness in (4.5) by requiring the scheme-representable diagonal to be quasi-compact and separated. Its footnote to (4.6) restricts the intended adequacy of the framework to that quasi-separated setting; it does not insert those conditions into the two displayed axioms. Definition (4.7) defines separatedness by properness of the diagonal. Example (4.8) treats a scheme acted on by an **étale, separated group scheme of finite type**, and forms the quotient using torsors. Our smooth-group theorem allows a larger range of groups and spaces.

Behrend's Chapter 3 works with an additional affine-diagonal restriction over a fixed field. Its groupoid presentations are smooth scheme groupoids whose arrow-to-endpoint map is affine. The proofs above establish the presentation statements without that restriction. In particular, an étale group scheme need not be separated, as the next exercise shows.

## 8. Exercises and complete solutions

### Exercise 8.1 — easy: spaces as stacks

Show that every scheme and every algebraic space is an algebraic stack.

*Solution.* For a space \(F\), its category of points has discrete fibres, and its fppf descent is precisely the sheaf condition. Its diagonal is representable by schemes, and its étale scheme atlas is also smooth and surjective. These are all three algebraic-stack conditions. For a scheme one can choose the identity atlas. In fact both are Deligne–Mumford stacks, as Proposition 2.2 proves. \(\square\)

### Exercise 8.2 — medium: automorphisms of an invertible module

Show that \(B\mathbf G_m\) is algebraic and that the automorphism group of every object is \(\mathbf G_m\).

*Solution.* Over \(T\), identify a \(\mathbf G_m\)-torsor with the frame torsor \(L^\times\) of an invertible \(\mathcal O_T\)-module \(L\), as in Lesson 4. The map \(T\times_{B\mathbf G_m}S\to T\), for the trivial-torsor atlas, is \(L^\times\to T\). Zariski locally it is \(\mathbf G_{m,T}\to T\), so it is smooth and surjective. The diagonal's Isom sheaf between \(L\) and \(M\) is \((L^\vee\otimes M)^\times\), a scheme. Descent of invertible modules makes this a stack, and these facts prove algebraicity.

The canonical scalar map \(\mathcal O_T\to\mathcal E nd(L)\) is an isomorphism: this is true in each local trivialization of \(L\), and is unchanged when that trivialization is multiplied by a unit. Its invertible elements are exactly automorphisms. After any \(T'\to T\), they are \(\Gamma(T',\mathcal O_{T'})^\times\). Thus the full automorphism **group scheme over \(T\)** is canonically \(\mathbf G_{m,T}\); the abstract group of automorphisms over \(T\) is its group of \(T\)-sections. \(\square\)

### Exercise 8.3 — medium: a non-separated diagonal

Let \(S=\mathbf A^1_k\), and form \(G\) by gluing two copies of \(S\) along \(S\setminus\{0\}\). Give it the group structure with fibre \(\mathbf Z/2\mathbf Z\) at the origin and trivial fibre elsewhere. Show that \(G\to S\) is étale and non-separated, and that the diagonal of \(BG\) is not separated.

*Solution.* Label the copies \(G_0,G_1\), and let their common open be \(D(x)\). Both maps \(G_i\to S\) are identities, so their glued map is étale. On the four open charts \(G_i\times_SG_j\cong S\), define multiplication to land in \(G_{i+j\bmod2}\) by the identity map on \(S\). Whenever two such charts overlap, the base point lies in \(D(x)\), where the target copies are identified; hence these maps glue. Define the unit by \(G_0\), and inversion to be the identity on each copy. On the eight charts of a triple product, associativity is addition modulo \(2\); the unit and inverse identities hold on the same charts. The morphisms therefore define a group scheme. The two points of its origin fibre remain distinct even in characteristic \(2\); this is the constant étale two-element group there, not \(\mu_2\).

Let \(e_0,e_1:S\to G\) be the two chart sections. Their equalizer is exactly \(D(x)\). Thus the pullback of
\(\Delta_{G/S}:G\to G\times_SG\) by \((e_0,e_1)\) is
\[
D(x)\longrightarrow S.
\tag{8.1}
\]
This is not a closed immersion, since \(D(x)\) is not closed in the affine line. Therefore \(G\to S\) is not separated.

Since \(G\to S\) is étale, Theorem 3.2 and its étale variant make \(BG\) a Deligne–Mumford stack with atlas \(S\to BG\). Pull its diagonal back by the pair of trivial torsors \(S\to BG\times_SBG\). The resulting morphism is
\(\operatorname{Isom}_S(G,G)\to S\). A right-equivariant automorphism of the trivial torsor is left multiplication by its value at the identity, identifying this morphism with \(G\to S\). If \(\Delta_{BG}\) were separated, so would be every base change, contradicting (8.1). Hence the diagonal of this Deligne–Mumford stack is itself non-separated. \(\square\)

### Exercise 8.4 — hard: a 2-fibre product is algebraic

Prove that \(\mathcal X\times_{\mathcal Z}\mathcal Y\) is algebraic for arbitrary morphisms of algebraic stacks [Stacks, Tag 04TD; Behrend, Exercise 3.38].

*Solution.* An object is \((x,y,\alpha:f(x)\to g(y))\); arrows are pairs obeying (4.2). Descent of \(x,y\) uses the two source stacks, and descent of \(\alpha\) and the equations uses Isom sheaves in the target. Thus the fibre product is a stack.

For two such objects, use the three spaces \(I_X,I_Y,J\) in the proof of Theorem 4.1. Equation (4.2) represents the Isom sheaf by \(I_X\times_JI_Y\), proving the diagonal condition. If \(U\to\mathcal X\), \(V\to\mathcal Y\) are smooth scheme atlases, the diagonal condition on \(\mathcal Z\) represents \(A=U\times_{\mathcal Z}V\) by an algebraic space. Its map to the fibre product factors as the two base changes of those atlases, so is smooth and surjective. An étale scheme cover \(B\to A\) makes \(B\) a smooth scheme atlas of the fibre product. All three conditions are now proved. The result does not require either given morphism to be representable, smooth or surjective. \(\square\)

## Prerequisites and sources

The quotient and presentation theorems, trivial-inertia criterion, fibre-product theorem, elliptic-stack effectivity and atlas, and topology comparison have been proved here. Their foundational inputs are:

- The complete flat bootstrap and its recognition over an algebraic space from Lesson 2; the gluing and scheme atlas results from Lessons 1–3; and the stackification, setoid–sheaf correspondence, torsor representation and quotient-torsor equivalence proved in Lesson 4.
- The scheme theory of smooth morphisms from *Smooth morphisms*: stability and descent of smoothness and étaleness, flatness and local finite presentation of a smooth map, openness of a flat locally finitely presented map, and sections étale locally for a smooth surjection [Stacks, Tags 055U, 055V]. The flat finite-presentation fibre criterion is [Stacks, Tag 01V8].
- The exact module descent theorem [Stacks, Tag 023T], its finite locally free descent consequence [Stacks, Tag 05B2], and the universal effective-epimorphism theorem for fpqc scheme covers [Stacks, Tag 023Q]. Relative Proj, its base-change compatibility, and ordinary Zariski gluing of schemes are scheme-construction prerequisites.
- Section 6.0 proves the Cartier-section assertion over every base, the divisor degree and curve Riemann–Roch formula, genus-one positive-degree vanishing, degree-three very ampleness, and the arbitrary-base cohomology comparison. Its Noetherian complex input is *Base change and the Grothendieck complex* (AG-QC-08), Lemma 3.1 and Theorem 3.2, used only on a Noetherian model. Its field duality input is *Dualizing sheaves and Serre duality for projective schemes* (AG-QC-15), Theorems 4.1–4.2, used after proving projectivity. The full algebraic-space cohomological bridge is the owned coherent-existence treatment of Lesson 8, currently being integrated; exact approximation prerequisite states are recorded in §6.0.2.
- Proper locally quasi-finite scheme morphisms are finite [Stacks, Tag 02LS]; the cohomology of twists on projective space over an arbitrary ring [Stacks, Tag 01XT], including its plane-curve genus consequence [Stacks, Tag 0BYD]. Coherent cohomology on a proper curve over a field vanishes above degree one, a case of [Stacks, Tag 02V7] over a Noetherian base. Descent of the usual scheme properties of the family in Lemma 6.4 is part of the scheme descent prerequisites.

We have not proved a general criterion equating the Deligne–Mumford condition with an unramified diagonal, nor algebraicity for arbitrary flat groupoid quotients, nor Artin's representability criteria. Those are subsequent topics. We do not compute the Picard group or étale cohomology of \(\mathcal M_{1,1}\) here. The invariant (6.13) is a morphism; no coarse-moduli universal property has been asserted for it.

## References

The Stacks project, *Algebraic Stacks*, Tags 026L, 0400, 02ZQ, 04SS, 04ST, 02ZV, 04SX, 03YJ, 03YK, 0304, 026N, 026O, 03YO, 03YR, 04SZ, 04TD, 04T0, 04T3, 04T5, 04TJ and 04TK; *Introducing Algebraic Stacks*, Tags 072I, 072J, 072K, 072Q, 072R, 072S, 072T and 072V. The scheme prerequisite tags are identified above.

K. Behrend, *Introduction to Algebraic Stacks* (2012), Chapter 3, §§3.1–3.3, especially Exercise 3.38. Its affine-diagonal conventions are compared in §7.

P. Deligne and D. Mumford, [*The Irreducibility of the Space of Curves of Given Genus*](https://www.numdam.org/item/PMIHES_1969__36__75_0/), *Publications Mathématiques de l'IHÉS* **36** (1969), 75–109, §4, Definitions (4.1)–(4.11), especially (4.5)–(4.7) and Example (4.8).
