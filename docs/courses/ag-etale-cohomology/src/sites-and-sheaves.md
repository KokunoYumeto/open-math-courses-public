# Sites and sheaves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Public domain (CC0).*

A function can be specified on overlapping open sets and then glued. A covering need not consist of open subsets, however. A surjection of sets, a finite separable field extension, and an étale map of schemes all provide useful ways to see an object locally. A site records which families count as coverings. A sheaf is a rule for assigning data that can be reconstructed from any such family.

Our route starts with matching data and constructs their universal completion. This gives both the existence of sheafification and practical rules for images, quotients and limits. We then use group actions to see a site without any ambient topological space, and sieves to distinguish a topology from a chosen list of covering families.

We assume categories, functors, natural transformations, limits and the Yoneda lemma. Sheaves on topological spaces, the model for the sites below, are treated in [Stacks, Tag 006S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-section-sheaves); no scheme theory is needed here. Basic references are [Stacks], [Leinster] and [Milne]. The proofs below are self-contained after the categorical prerequisites. The construction of sheafification is the classical plus construction.

## 1. Local data and their agreement

Fix a category \(\mathcal C\). Initially its objects and arrows form sets. All indexing families are sets as well. A **presheaf** is a functor \(F:\mathcal C^{\mathrm{op}}\to\mathrm{Sets}\). For an arrow \(v:V\to U\), write \(v^*s\), or \(s|_V\) when the arrow is understood, for the image of \(s\in F(U)\). Restrictions compose in the opposite direction to arrows.

A **site** consists of \(\mathcal C\) and specified covering families \(\{u_i:U_i\to U\}_{i\in I}\), satisfying the following rules.

1. A singleton isomorphism is a covering.
2. If \(\{U_i\to U\}\) covers and each \(\{V_{ij}\to U_i\}\) covers, the composite family \(\{V_{ij}\to U\}_{i,j}\) covers.
3. If \(\{U_i\to U\}\) covers and \(V\to U\) is an arrow, each \(U_i\times_U V\) exists and \(\{U_i\times_U V\to V\}\) covers.

We need fibre products involving members of coverings, rather than every possible fibre product in \(\mathcal C\). Empty families are allowed when the site's topology specifies them as coverings.

For a covering \(\mathcal U=\{U_i\to U\}\), let

\[
M(\mathcal U,F)=\left\{(s_i)\in\prod_i F(U_i):
\operatorname{pr}_1^*s_i=\operatorname{pr}_2^*s_j
\text{ in }F(U_i\times_U U_j)\text{ for all }i,j\right\}.
\]

This is also denoted \(\check H^0(\mathcal U,F)\). A presheaf is **separated** if \(F(U)\to M(\mathcal U,F)\) is injective for every covering, and is a **sheaf** if this map is bijective. Thus a sheaf satisfies the equalizer diagram

\[
F(U)\longrightarrow\prod_iF(U_i)
\rightrightarrows\prod_{i,j}F(U_i\times_U U_j).
\]

For the category of open subsets of a space, with inclusions as arrows and ordinary open coverings, this is the familiar sheaf condition. For the topology whose coverings are singleton isomorphisms, every presheaf is a sheaf. At the opposite extreme, if the empty family covers every object, the equalizer condition requires \(F(U)\) to be a singleton for every \(U\), so there is only the terminal sheaf up to isomorphism.

**Example 1.1.** Let \(B(U)\) be the bounded continuous real functions on an open subset \(U\subset\mathbb R\). Restriction defines a presheaf. Functions are determined pointwise, so it is separated. The functions \(x\mapsto x\) on \((-m,m)\), for positive integers \(m\), agree and cover \(\mathbb R\), but do not glue to a bounded function there. Thus separation alone does not supply gluing.

The representable presheaf attached to \(U\) is \(h_U(V)=\operatorname{Hom}_{\mathcal C}(V,U)\). A topology is **subcanonical** when every \(h_U\) is a sheaf. This is an additional property; it is not an axiom of a site.

## 2. Refining a description

A refinement from \(\mathcal V=\{V_j\to U\}\) to \(\mathcal U=\{U_i\to U\}\) chooses, for every \(j\), an index \(a(j)\) and an arrow \(V_j\to U_{a(j)}\) over \(U\). Pulling back the chosen sections gives a map

\[
M(\mathcal U,F)\longrightarrow M(\mathcal V,F).
\]

The pulled-back family matches: on \(V_j\times_U V_k\), its two sections are obtained by pulling the original matching equality through the map to \(U_{a(j)}\times_U U_{a(k)}\).

**Lemma 2.1.** Any two refinement maps with the same underlying arrow of targets induce the same map on matching families. Any two coverings of the same target have a common refinement.

**Proof.** Suppose a member \(V_j\) maps to \(U_a\) by one refinement and to \(U_b\) by another. These two arrows give a single arrow \(V_j\to U_a\times_U U_b\). The matching equality on this fibre product, pulled back to \(V_j\), says that the two proposed restrictions are equal. This works for every member and proves the first assertion. For the second, if \(\{U_i\to U\}\) and \(\{V_j\to U\}\) cover, pull the second covering back to each \(U_i\), then compose coverings. The resulting family \(\{U_i\times_U V_j\to U\}_{i,j}\) refines both. \(\square\)

The relation “admits a refinement” is a preorder. Quotienting by mutual refinement gives a directed partially ordered set, with finer coverings later in the order. Lemma 2.1 makes the matching-family maps well-defined on this quotient. It is this directed diagram that we use.

The category retaining every distinct refinement map need not itself be cofiltered. For example, let a nontrivial group \(G\) act on itself by left translation. The covering \(G\to *\) has distinct refinement endomorphisms given by right translations. The identity and right translation by \(g\ne1\) cannot be equalized by any covering refinement: equality would force the image of every member in \(G\) to consist of fixed points of that right translation, and there are none. Passing to the refinement preorder is justified by the first part of the lemma, not by claiming that those parallel maps admit an equalizer.

Define

\[
F^+(U)=\varinjlim_{\mathcal U\text{ covering }U}M(\mathcal U,F).
\]

Concretely, an element is represented by a covering with a matching family. Two representatives are equivalent exactly when their restrictions agree on a common refinement. Transitivity of this equivalence follows by taking a common refinement of the two coverings witnessing the successive equalities. This description also works for an empty covering.

The identity covering sends \(s\in F(U)\) to a class \(\eta_F(s)\). Pulling a representative back along \(V\to U\) defines \(F^+(U)\to F^+(V)\). A common refinement pulls back to a common refinement, so the restriction is independent of the representative. Canonical associativity of fibre products proves compatibility with composition. A map \(F\to E\) acts on each component of a matching family and hence gives \(F^+\to E^+\). Thus plus is a functor, and \(\eta_F:F\to F^+\) is natural.

Two facts will carry almost the whole proof:

1. Every section of \(F^+\) locally comes from \(F\). Indeed a representative \((s_i)\) on \(\{U_i\to U\}\) restricts on \(U_i\) to \(\eta_F(s_i)\). On the pullback covering, matching with the selected member gives precisely this equality.
2. Sections \(s,t\in F(U)\) have the same image in \(F^+(U)\) if and only if they agree on a covering of \(U\). This is the common-refinement description applied to the identity covering.

## 3. Why two completions suffice

**Theorem 3.1.** For any presheaf \(F\), the presheaf \(F^+\) is separated. If \(F\) is separated, then \(F\to F^+\) is injective on sections and \(F^+\) is a sheaf. If \(F\) is a sheaf, this map is an isomorphism. Consequently \(F^{++}\) is always a sheaf.

**Proof.** First consider \(a,b\in F^+(U)\) whose restrictions agree on a covering \(\{W_k\to U\}\). Choose representatives for \(a,b\) and a common refinement with this covering. On every member \(V\) of that refinement, the sections are images of two sections \(s_V,t_V\in F(V)\). Their images in \(F^+(V)\) agree. Fact 2 at the end of section 2 gives a covering of \(V\) on which \(s_V,t_V\) agree. Composing these coverings supplies a covering of \(U\) on which the two representatives agree. Their classes are equal, proving separation of \(F^+\).

If \(F\) is separated, Fact 2 immediately makes \(\eta_F\) injective on every object. Now let \(a_i\in F^+(U_i)\) be a matching family. Choose a covering \(\{V_{ij}\to U_i\}\) so that each restriction of \(a_i\) is \(\eta_F(s_{ij})\) for some \(s_{ij}\in F(V_{ij})\). The composite family \(\{V_{ij}\to U\}\) covers. On \(V_{ij}\times_U V_{kl}\), the images of \(s_{ij}\) and \(s_{kl}\) in \(F^+\) agree because the \(a_i\) match. Injectivity of \(F\to F^+\) on this object makes the original sections agree there. They therefore define a matching family in \(F\), hence a class \(a\in F^+(U)\).

On every \(V_{ij}\), the restriction of \(a\) equals that of \(a_i\). Separation of \(F^+\), applied to the covering of \(U_i\), gives \(a|_{U_i}=a_i\). Separation on \(U\) also gives uniqueness of \(a\). This proves that \(F^+\) is a sheaf.

If \(F\) was already a sheaf, every matching family has a unique global section. These bijections \(F(U)\simeq M(\mathcal U,F)\) are compatible with refinement, so \(F(U)\simeq F^+(U)\). Finally, the first assertion makes \(F^+\) separated, and the second makes \((F^+)^+\) a sheaf. \(\square\)

Write \(F^\#=F^{++}\) and call this the **associated sheaf**. Iterating Fact 1 and composing coverings shows that every section of \(F^\#\) locally comes from \(F\). Moreover, two sections of \(F\) have the same image in \(F^\#\) exactly when they agree locally: equality in the second plus is local equality in the first plus, and a second refinement reduces that to equality in \(F\).

**Theorem 3.2.** For any sheaf \(E\), composition with \(F\to F^\#\) gives a natural bijection

\[
\operatorname{Hom}(F^\#,E)\simeq\operatorname{Hom}(F,E).
\]

**Proof.** Given \(v:F\to E\), apply \(v\) to a matching family and glue in \(E\). Refining the family leaves the glued section unchanged, because its restrictions determine it. This defines \(F^+\to E\); repeating defines \(F^{++}\to E\). It extends \(v\). If two extensions agree on \(F\), every section of \(F^\#\) is locally represented by sections of \(F\), so the extensions agree locally on every section. Separation of \(E\) makes them agree globally. Naturality follows because applying a presheaf morphism commutes with restriction and gluing. \(\square\)

Thus sheafification is left adjoint to the inclusion of sheaves into presheaves.

**Theorem 3.3.** Sheafification commutes with finite limits.

**Proof.** For each covering, \(M(\mathcal U,-)\) preserves limits: products and equalizers of matching families are calculated componentwise. We also need the elementary fact that directed colimits of sets commute with finite limits. For a finite product, any finite collection of classes has representatives at one common later stage. For an equalizer, equality of two images of a class is witnessed at a later stage, where that representative lies in the equalizer. These descriptions prove both surjectivity and injectivity of the comparison maps. The terminal set causes no exception, since the indexing preorder is nonempty.

Apply this fact to the directed refinement diagram. It proves \((\lim_{a\in A}F_a)^+\simeq\lim_{a\in A}F_a^+\) for a finite diagram. Apply plus once more. A limit of sheaves is a sheaf: a matching family in the limit glues in every component, and uniqueness makes those glued sections compatible with every arrow of the diagram. Therefore the resulting presheaf limit is also the sheaf limit, proving the assertion. \(\square\)

**Example 3.4.** For a set \(A\), sheafifying the constant presheaf on a space gives the sheaf \(\underline A\) of locally constant functions to the discrete set \(A\). Matching constant values glue to locally constant functions; conversely each such function is constant on a covering. These two operations identify the plus construction with \(\underline A\). In particular the empty open has one section, even when the constant presheaf has \(A\) there.

If \(X\) is connected and nonempty, the constant functions identify \(A\) with \(\underline A(X)\). The converse requires \(A\) to have at least two elements: a disconnection then gives a nonconstant locally constant function. With a singleton coefficient set, every space has just one such function; with empty coefficients, a nonempty space has none. Connectedness describes this map on global sections, not equality of the constant presheaf with its sheafification on all opens.

The presheaf \(B\) of Example 1.1 has associated sheaf \(C\), the continuous real functions. Every continuous function is bounded on some neighbourhood of each point, and equality of continuous functions is local. Hence \(B\to C\) induces a bijection on associated sheaves, by local representation and local equality. Since \(B\) is separated, even \(B^+\simeq C\).

## 4. Images and quotients are local

A map of sheaves \(v:F\to E\) is **locally surjective** when, for every \(e\in E(U)\), there is a covering \(\{U_i\to U\}\) and \(f_i\in F(U_i)\) with \(v(f_i)=e|_{U_i}\). This does not require the \(f_i\) to match.

**Theorem 4.1.** A map of sheaves is a monomorphism exactly when it is injective on every set of sections, and an epimorphism exactly when it is locally surjective. It is an isomorphism exactly when both conditions hold.

**Proof.** Pointwise injectivity implies the categorical cancellation condition for a monomorphism. Conversely a section of \(F(U)\) corresponds, by Yoneda and Theorem 3.2, to a map \(h_U^\#\to F\). Two sections with the same image under a monomorphism therefore coincide.

Local surjectivity implies the epimorphism cancellation condition: if \(a,b:E\to H\) agree after composition with \(v\), their values on a section of \(E\) agree after passing to a covering where it lifts to \(F\). Separation of \(H\) makes those values equal.

For the converse, form the presheaf image \(P(U)=v(F(U))\subset E(U)\), and its local saturation

\[
I(U)=\{e\in E(U):e\text{ belongs to }P\text{ on a covering of }U\}.
\]

This is a subsheaf of \(E\). Restriction preserves the condition; matching local sections glue in \(E\), and composing their witnessing coverings puts the glued section in \(I\). The map factors through \(I\).

Take the pointwise presheaf pushout \(Q=E\amalg_I E\) and sheafify it. If \(v\) is an epimorphism, the two maps \(E\to Q^\#\), which agree on \(F\), agree everywhere. For \(e\in E(U)\), equality of its two copies in \(Q^\#(U)\) means they are equal locally in \(Q\), by the local-equality property after Theorem 3.1. In the set pushout of two copies of a set along a subset, the two copies of an element are equal exactly when it belongs to that subset. Thus \(e\) locally belongs to \(I\), hence belongs to \(I(U)\) since \(I\) is a subsheaf. Consequently \(I=E\), proving local surjectivity.

Finally suppose \(v\) is pointwise injective and locally surjective. Local lifts of \(e\in E(U)\) agree on all overlaps by injectivity, so they glue uniquely in \(F\). This gives an inverse on each set of sections. Uniqueness makes these inverses commute with restriction. \(\square\)

**Theorem 4.2.** Sheaves have all small limits and colimits. Limits are calculated on sections. Colimits are obtained by sheafifying the pointwise presheaf colimit. Abelian sheaves form an abelian category.

**Proof.** The limit argument in Theorem 3.3 used no finiteness: a compatible matching family glues componentwise in an arbitrary diagram. This gives all limits. For a diagram \(F_a\) of sheaves, let \(P\) be its presheaf colimit. For any sheaf \(E\), Theorem 3.2 identifies maps \(P^\#\to E\) with maps \(P\to E\), which are exactly compatible families of maps \(F_a\to E\). This is the colimit universal property.

For abelian presheaves the matching families and their refinement colimits are abelian groups, so plus and sheafification preserve addition. Theorem 3.3 remains valid on underlying sets and hence on abelian groups. Abelian presheaves form an abelian category by computing kernels and cokernels pointwise. Abelian sheafification is an additive left adjoint, preserves finite limits, and therefore preserves kernels and cokernels. For a map of abelian sheaves its kernel is the pointwise kernel, and its cokernel is the sheafified pointwise cokernel. Sheafify the pointwise isomorphism from coimage to image; exactness of sheafification makes this the coimage-to-image isomorphism in sheaves. Finite products are finite biproducts, and the zero presheaf is already a sheaf. These facts verify the abelian-category axioms. \(\square\)

**Example 4.3.** On \(X=\mathbb C^*\), let \(\mathcal O\) be the holomorphic functions and \(\mathcal O^*\) the nowhere-zero holomorphic functions. The exponential map \(\mathcal O\to\mathcal O^*\) is locally surjective: near any point a nowhere-zero holomorphic function has a holomorphic logarithm. It need not be surjective on global sections. In particular \(z\) has no logarithm on \(\mathbb C^*\). If \(\exp(g)=z\), differentiation would give \(g'=1/z\); integrating around the unit circle gives \(0=2\pi i\), a contradiction.

The presheaf cokernel therefore has a nonzero class represented by \(z\) on \(X\), whose restriction is zero near every point. It is not separated, hence not a sheaf. Its associated sheaf is zero because every local section of \(\mathcal O^*\) locally has a logarithm. Thus even a categorical epimorphism can have a nonzero pointwise presheaf cokernel.

## 5. Recovering an action from descent

Let \(G\) be an abstract group. The category \(T_G\) has left \(G\)-sets as objects, equivariant maps as arrows, and jointly surjective families as coverings. Pullbacks have their diagonal action. Composition and pullback preserve joint surjectivity, so these families give a site.

For precision about size, choose universes \(\mathbb U\in\mathbb V\), with \(G\) a \(\mathbb U\)-small group. Take a skeleton of the \(\mathbb U\)-small \(G\)-sets as the category; it is small in \(\mathbb V\). Take sheaves valued in \(\mathbb V\)-small sets. Coverings may be normalized to families with no repeated arrows; there is then a set of coverings in \(\mathbb V\). Removing repetitions does not alter matching data or the generated sieves. The statements below identify these sheaves with \(\mathbb V\)-small \(G\)-sets. In particular the set assigned by a sheaf need not itself be an object of the chosen site. The notation \(h_S(V)=\operatorname{Hom}_G(V,S)\) still defines a presheaf in that case. For an ordinary small site no change of universe is necessary. Big scheme sites will require a similarly stated size convention later.

For any \(G\)-set \(S\), the presheaf \(h_S\) is a sheaf. An equivariant map to \(S\) is determined by its pullbacks along a jointly surjective family. Conversely, matching equivariant maps \(V_i\to S\) define a map \(V\to S\) by selecting a preimage of each element. Matching on \(V_i\times_V V_j\) makes the value independent of the selection; equivariance follows by translating a preimage. This also proves subcanonicity.

**Theorem 5.1.** Evaluation on the regular \(G\)-set gives an equivalence

\[
\operatorname{Sh}(T_G)\simeq G\text{-}\mathrm{Sets},
\qquad F\longmapsto F(G),\quad S\longmapsto h_S.
\]

**Proof.** For \(g\in G\), right translation \(R_g:G\to G\) is equivariant. Give \(S=F(G)\) the left action \(g\cdot s=F(R_g)(s)\). Since \(R_h\circ R_g=R_{gh}\), contravariance gives \(F(R_{gh})=F(R_g)F(R_h)\), which is exactly the left-action rule.

For \(u\in U\), the equivariant map \(q_u:G\to U\) sends \(a\) to \(au\). Define

\[
\theta_U:F(U)\longrightarrow\operatorname{Hom}_G(U,S),
\qquad \theta_U(t)(u)=q_u^*t.
\]

The equality \(q_{gu}=q_uR_g\) proves equivariance; composition with an arrow \(V\to U\) proves naturality.

The family \(\{q_u:G\to U\}_{u\in U}\) is jointly surjective. To construct an inverse, take an equivariant map \(b:U\to S\) and put the section \(b(u)\in F(G)\) on the copy indexed by \(u\). We must verify matching on the fibre product of the copies indexed by \(u,v\). Its elements are pairs \((a,c)\) with \(au=cv\). It is covered by equivariant maps from regular copies of \(G\), one for each such pair, sending \(k\) to \((ka,kc)\). On that copy the two sections restrict to \(a\cdot b(u)\) and \(c\cdot b(v)\). They agree because both are \(b(au)=b(cv)\). Separation of \(F\) proves equality on the whole fibre product, and gluing gives a unique \(t\in F(U)\). Its pullbacks are the prescribed \(b(u)\), so \(\theta_U(t)=b\). Conversely the pullbacks \(q_u^*t\) determine \(t\) by separation. Finally \(\operatorname{Hom}_G(G,S)\simeq S\) by evaluation at \(1\). These natural identifications give the two inverse equivalences, including their action on morphisms. \(\square\)

For \(G=\mathbb Z\), an action is a set with one specified bijection, the action of \(1\). Under the equivalence, \(h_{\mathbb Z}\) is the regular action, with the bijection \(m\mapsto m+1\).

The finite continuous \(G\)-sets for a profinite group give a different site: the regular action on \(G\) is not a finite object when \(G\) is infinite. Exercise 6 proves the replacement formula using finite quotients.

## 6. A topology without a preferred covering list

A **sieve** on \(U\) is a subpresheaf \(R\subset h_U\): if an arrow lies in \(R\), every precomposition with it lies in \(R\). The sieve generated by a family contains exactly the arrows factoring through some member of the family. Its pullback along \(f:V\to U\) is the sieve

\[
f^*R(W)=\{a:W\to V:fa\in R(W)\}.
\]

This definition requires no fibre products in the category. A **Grothendieck topology** assigns covering sieves \(J(U)\) subject to three rules: the maximal sieve covers; pullback preserves covering; and if \(R\) covers and \(f^*Q\) covers for every arrow \(f\) in \(R\), then \(Q\) covers. These rules also imply that a sieve containing a covering sieve covers.

**Theorem 6.1.** On a site, declare a sieve covering when it contains the sieve generated by a covering family. This is a Grothendieck topology. A presheaf is a sheaf for the families exactly when

\[
F(U)=\operatorname{Hom}(h_U,F)\longrightarrow\operatorname{Hom}(R,F)
\]

is bijective for every covering sieve \(R\).

**Proof.** The identity covering proves the maximal-sieve rule. Base change of a covering family supplies a covering family contained in the pulled-back sieve. For transitivity, choose a covering family \(\{U_i\to U\}\) contained in \(R\). For each member, choose a covering family of \(U_i\) contained in its pullback of \(Q\). Composing the families gives a covering of \(U\) contained in \(Q\).

A matching family \((s_i)\) determines a natural transformation from its generated sieve to \(F\): on an arrow \(a:T\to U\), choose a factorization \(T\to U_i\to U\) and pull back \(s_i\). Two choices agree by pulling back the matching equality from \(U_i\times_U U_j\). The definition is natural under precomposition. Conversely a transformation on the sieve restricts to a matching family by evaluating on the covering arrows. Thus the sieve condition implies the family condition.

Now suppose the family condition holds and \(\varphi:R\to F\) is given on a covering sieve. A covering family contained in \(R\) gives sections \(s_i=\varphi(U_i\to U)\) that match by naturality. Glue them to \(s\in F(U)\). For any \(a:T\to U\) in \(R\), pull back the chosen covering to \(T\). On each member, \(a^*s\) and \(\varphi(a)\) agree by naturality of \(\varphi\). Separation gives equality on \(T\). Hence \(s\) extends all of \(\varphi\), and uniqueness follows on the chosen covering. \(\square\)

**Proposition 6.2.** Every small category has a finest subcanonical Grothendieck topology, called the canonical topology.

**Proof.** For a presheaf \(H\), declare \(R\) to belong to \(J_H(U)\) when, for every \(f:V\to U\), the map \(H(V)\to\operatorname{Hom}(f^*R,H)\) is bijective. Maximal sieves and pullback stability follow directly. We check transitivity. Suppose \(R\in J_H(U)\) and \(r^*Q\in J_H(V)\) for every \(r:V\to U\) in \(R\). To extend \(\varphi:Q\to H\), first extend its pullback to each \(r^*Q\), obtaining a unique section \(s_r\in H(V)\). Uniqueness makes \(s_r\) compatible with every arrow between members of \(R\). The resulting transformation \(R\to H\) extends uniquely to \(s\in H(U)\).

For \(q:W\to U\) in \(Q\), compare \(q^*s\) with \(\varphi(q)\) on the covering sieve \(q^*R\). On an arrow in this sieve the comparison reduces to the defining equality on the pullback of \(Q\) at a member of \(R\), so it is equality. Injectivity of \(H(W)\to\operatorname{Hom}(q^*R,H)\) proves \(q^*s=\varphi(q)\). The same reasoning proves uniqueness of the extension. Repeating this construction after any \(f:V\to U\) proves the universal condition, hence transitivity for \(J_H\).

Intersect \(J_{h_T}\) over all objects \(T\). Intersections preserve the topology axioms, so this is a topology making every representable a sheaf. Any other subcanonical topology is contained in it: a covering sieve and every pullback satisfy the sheaf condition for every \(h_T\). This proves maximality. \(\square\)

**Theorem 6.3.** Two Grothendieck topologies on the same small category with the same sheaves as full subcategories of its presheaves are equal.

**Proof.** We first recall how sheafification works for a topology that is presented directly by sieves. Replace \(M(\mathcal U,F)\) by \(\operatorname{Hom}(R,F)\) and take the colimit over covering sieves \(R\), ordered by reverse inclusion. Intersections of two covering sieves are covering: pull back the second along the arrows of the first and use transitivity. This is a directed diagram. Pullback of sieves gives restrictions.

An element represented on \(R\) restricts at an arrow \(r:V\to U\) of \(R\) to the image of the section assigned to \(r\). Equality of two representatives is witnessed on a smaller covering sieve. These give the two local facts used in section 3. For separation of plus, take local witnesses for equality along a covering sieve and then the sieve of their composites; transitivity makes that sieve covering. For gluing when \(F\) is separated, represent each local plus-section on a covering sieve. On any arrow where two representatives meet, their images agree in plus; injectivity of \(F\to F^+\) makes their sections equal. They define a transformation on the covering sieve of composites, whose class glues the given sections. Separation proves uniqueness. Thus double plus is a sheaf. Sending a representative to its glued image in a sheaf gives the same universal property as Theorem 3.2. The directed-colimit proof gives left exactness as well.

Let \(a_J\) be this sheafification. For a sieve inclusion \(R\subset h_U\), left exactness makes \(a_JR\to a_Jh_U\) a monomorphism. It is an isomorphism if \(R\) covers, since maps out of the inclusion into any sheaf are precisely the bijections in the sheaf condition.

Conversely, if it is an isomorphism, lift the image of \(\operatorname{id}_U\) to a section of \(a_JR(U)\). Local representation gives a covering sieve on whose arrows that section comes from \(R\). Its image equals the restriction of \(\operatorname{id}_U\) in \(a_Jh_U\). Local equality permits further covering refinements on which the representing arrow is literally that restriction in \(h_U\). These arrows belong to \(R\). Transitivity shows that \(R\) contains a covering sieve, so \(R\) covers.

It follows that \(R\) covers exactly when \(\operatorname{Hom}(h_U,E)\to\operatorname{Hom}(R,E)\) is bijective for every \(J\)-sheaf \(E\): by the adjunction these are maps out of \(a_Jh_U\) and \(a_JR\), and a map inducing bijections into every object is an isomorphism by Yoneda. This criterion uses only the full subcategory of sheaves, so that subcategory determines \(J\). \(\square\)

Different lists of covering families can therefore generate the same topology. Different categories can also present equivalent categories of sheaves. The last theorem concerns topologies on one fixed category, with their inclusion into its presheaves; an abstract equivalence between two categories of sheaves does not identify their sites.

In the language of local epimorphisms, the sieve generated by a family is covering exactly when \(\coprod_i h_{U_i}^\#\to h_U^\#\) is locally surjective. One implication follows by pulling back a covering contained in that sieve; the converse follows by representing the identity locally and using local equality, as in Theorem 6.3. This recognizes coverings in the generated topology, which can contain more covering families than the initially specified list. It describes the same gluing mechanism in categorical terms.

## 7. Exercises

1. **First steps.** Prove that a sheaf on the open subsets of a space has exactly one section on the empty open. Then prove directly that a pointwise injective, locally surjective map of sheaves has a natural inverse.
2. **Orbit values.** Sheafify the constant presheaf with value \(A\) on \(T_G\). Describe its sections on a \(G\)-set with three orbits, and explain what happens on the empty \(G\)-set.
3. **Universal gluing.** For any presheaf \(H\), use universal matching on pulled-back sieves to construct the finest topology making \(H\) a sheaf. Deduce the existence of the canonical topology without assuming any fibre products in the category.
4. **Finite limits and cokernels.** Give an elementwise proof that plus preserves binary products and equalizers. On \(\mathbb C^*\), find a nonzero section of the presheaf cokernel of the exponential map that becomes zero on an open covering, and compute the sheaf cokernel.
5. **When a coefficient detects disconnection.** Let \(A\) have at least two elements. Prove that \(A\to\underline A(X)\) is bijective exactly when \(X\) is connected and nonempty. Treat \(A=\varnothing\) and \(A\) a singleton separately. Does bijectivity on global sections make the constant presheaf a sheaf?
6. **Finite probes of an infinite group.** Let \(G\) be profinite. On the site of finite continuous left \(G\)-sets with finite jointly surjective coverings, prove subcanonicity and the equivalence with continuous discrete \(G\)-sets. Construct the associated \(G\)-set as

   \[
   S_F=\varinjlim_{N\triangleleft G\ \mathrm{open}}F(G/N),
   \]

   where a smaller normal subgroup gives a later stage. Prove both directions of the equivalence, including continuity and the independence of choices.

## 8. Solutions

**1.** The empty family covers the empty open. Its matching-family set is the empty product, a singleton, so the sheaf condition gives the first assertion. For the second, lift a section on a covering. The two restrictions of any pair of lifts have the same image on their fibre product and therefore agree by injectivity. Gluing gives a unique lift. Restricting this lift to another object gives the unique lift of the restricted section, so the pointwise inverses are natural.

**2.** Give \(A\) the trivial \(G\)-action. Theorem 5.1 supplies the sheaf

\[
h_A(U)=\operatorname{Hom}_G(U,A)=\operatorname{Maps}(U/G,A).
\]

The constant-presheaf map sends \(a\) to the constant orbit function. Any orbit function is locally of this form: the individual orbits cover \(U\), and the function has one value on each orbit. For a nonempty \(U\), two constant values have equal images exactly when they are equal. On \(U=\varnothing\), all images agree and the empty covering witnesses their local equality. The local-representation and local-equality properties of sheafification therefore prove that \(h_A\) is the associated sheaf. With three orbits its value is \(A^3\); on the empty object it is a singleton. These statements include empty and singleton \(A\).

**3.** Define \(J_H\) by the condition

\[
R\in J_H(U)\quad\Longleftrightarrow\quad
H(V)\xrightarrow{\sim}\operatorname{Hom}(f^*R,H)
\text{ for every }f:V\to U.
\]

The maximal sieve is immediate, and pulling back merely replaces \(f\) by a composite. For transitivity, start with \(R\in J_H(U)\) and \(Q\) covering after pullback along each member of \(R\). A matching transformation on \(Q\) extends uniquely on each such pullback to a section on the member of \(R\). Uniqueness makes those sections natural, so they extend on \(R\) to a section on \(U\). To check its restriction on \(Q\), pull back \(R\) along every member of \(Q\); the two proposed sections agree on that sieve and hence agree. The same argument after an arbitrary \(V\to U\) proves the required universal condition. Thus \(J_H\) is a topology. It makes \(H\) a sheaf by taking \(f=\operatorname{id}\). Any topology making \(H\) a sheaf has every covering sieve, and its pullbacks, in \(J_H\), so is contained in it. Intersect these topologies for \(H=h_T\). This is exactly the canonical topology of Proposition 6.2, and uses pullbacks of sieves, not fibre products of objects.

**4.** A pair of plus-classes for \(F,E\) has representatives on a common refinement. Pairing the component sections gives a matching family for \(F\times E\). Conversely a matching pair gives two classes. If their components agree in both colimits, a common later refinement witnesses both equalities and hence equality of the paired classes. This proves preservation of products. For an equalizer \(K=\operatorname{Eq}(F\rightrightarrows E)\), a plus-class of \(F\) whose two images agree has a representative for which those images agree on a later refinement. Its component sections then lie in \(K\). Equality of two such representatives is witnessed in the same manner, proving the equalizer assertion. Applying plus twice gives left exactness of sheafification.

The class of \(z\) in \(\mathcal O^*(\mathbb C^*)/\exp\mathcal O(\mathbb C^*)\) is nonzero by the integral in Example 4.3. Cover \(\mathbb C^*\) by small disks avoiding \(0\); each disk has a holomorphic logarithm of \(z\), so the class restricts to zero. More generally every nowhere-zero holomorphic function locally has a logarithm. The sheafified cokernel is therefore zero.

**5.** On a connected nonempty space every locally constant function is constant: two distinct attained values would partition the space into the inverse image of one value and its nonempty open complement. Constants are distinct because there is a point. On a disconnected nonempty space choose a nontrivial clopen partition and two distinct elements of \(A\). The resulting two-valued locally constant function is not constant. On the empty space the target is a singleton, whereas \(A\) has at least two elements.

For singleton \(A\) the map is bijective for every space. For empty \(A\), the map is a bijection for every nonempty space, and fails for the empty space. Even on connected nonempty \(X\), the constant presheaf with \(|A|\ge2\) is not a sheaf: its value on the empty open is \(A\), and any disconnected open can have additional locally constant sections after sheafification. Global sections alone do not test the sheaf axiom.

**6.** Finite continuous \(G\)-sets are closed under finite fibre products. Joint surjectivity is stable under pullback and composition. The proof that equivariant maps glue in section 5 applies to finite families, so every representable is a sheaf. The same proof shows that

\[
H_S(U)=\operatorname{Hom}_G(U,S)
\]

is a sheaf for any continuous discrete \(G\)-set \(S\), even an infinite one.

For open normal \(N'\subset N\), the quotient map \(G/N'\to G/N\) gives the transition \(F(G/N)\to F(G/N')\). Intersections give common later stages. Right translations on \(G/N\) define a left action on \(F(G/N)\), as in Theorem 5.1, and the transitions respect these actions. A class represented at stage \(N\) is fixed by \(N\), so its stabilizer is open. This is exactly continuity of an action on a discrete set. Thus \(S_F\) is a continuous discrete \(G\)-set.

For \(t\in F(U)\) and \(u\in U\), choose an open normal \(N\) fixing every element of \(U\), and pull \(t\) back by \(q_u:G/N\to U\), \(aN\mapsto au\). Put

\[
\theta_U(t)(u)=[q_u^*t]\in S_F.
\]

Two choices of \(N\) agree after passing to their intersection. Right translations prove equivariance, and composition with arrows of \(U\) proves naturality.

To prove injectivity, suppose \(\theta_U(t)=\theta_U(t')\). For each of the finitely many \(u\), equality of the classes is witnessed at a sufficiently small open normal subgroup. Intersect those subgroups with one that acts trivially on \(U\). At this common stage the pullbacks of \(t,t'\) along every \(q_u\) agree. The finite family \(\{q_u:G/N\to U\}_{u\in U}\) covers, so separation gives \(t=t'\). For empty \(U\), both section sets are singletons by the empty covering.

For surjectivity let \(b:U\to S_F\) be equivariant. Its finitely many values have representatives \(t_u\in F(G/N)\) at one common stage, with \(N\) also acting trivially on \(U\). In the colimit, the relations

\[
F(R_g)t_u=t_{gu}
\]

hold. It suffices first to consider one representative of each coset of \(G/N\): there are finitely many relations, since \(U\) is finite. All become literal equalities after passing to a common smaller open normal subgroup \(N'\). The pulled-back sections are still fixed by \(N\), so the equalities also hold for every \(g\in G\), not merely the selected representatives.

Use these sections on the covering \(\{G/N'\to U\}_{u\in U}\). A fibre product of two members is covered by the diagonal regular quotient orbits corresponding to pairs \((aN',cN')\) with \(au=cv\). On such an orbit the restrictions are \(F(R_a)t_u\) and \(F(R_c)t_v\), now equal to \(t_{au}\) and \(t_{cv}\). They agree. Gluing gives \(t\in F(U)\), with \(\theta_U(t)=b\). We have proved \(F\simeq H_{S_F}\) naturally.

Finally

\[
S_{H_S}=\varinjlim_N\operatorname{Hom}_G(G/N,S)
=\varinjlim_N S^N=S.
\]

Every element of \(S\) has an open stabilizer, which contains an open normal subgroup: the kernel of the permutation action on the finite coset space of that stabilizer is such a subgroup. The transition maps are the inclusions of fixed subsets. Evaluation at the identity coset identifies the actions as well as the sets. These natural identifications prove the claimed equivalence. They explain why the finite-quotient formula replaces evaluation on the regular \(G\)-set.

## What this lesson does not prove

We use the Yoneda lemma, in the form \(\operatorname{Hom}(h_U,F)\simeq F(U)\) for every presheaf \(F\), and elementary categorical universal properties as prerequisites; the precise Yoneda statement is [Stacks, Tag 001P]. No scheme-theoretic or cohomological theorem is assumed. The identification of the finite continuous group-set site with the étale site of a field will require the equivalence between finite separable field extensions and finite Galois sets, and is proved in the lesson on Galois cohomology.

## References

- **[Stacks]** The Stacks Project Authors, *The Stacks Project*, “Sites and Sheaves”: Tags [00WB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-theorem-plus), [00WH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-proposition-sheafification-adjoint), [00W0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-proposition-sheaves-on-group), [00ZC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-lemma-site-gives-topology), [00ZP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-theorem-topology-and-topos); “Categories”, Tag [001P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-yoneda); and “Étale Cohomology”, Tag [03NP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-G-sets). The linked AI Integrated Stacks Project reader is an edition with AI-proposed corrections and AI-written additions, not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
- **[Leinster]** Tom Leinster, *An informal introduction to topos theory* (2010), [arXiv:1012.5647](https://arxiv.org/abs/1012.5647), section 1. Motivation and examples of categories of sheaves.
- **[Milne]** J. S. Milne, *Lectures on Étale Cohomology*, [author's course notes](https://www.jmilne.org/math/CourseNotes/lec.html), sections on sheaves and the étale topology. A complementary route toward the scheme-theoretic examples developed later in this course.
