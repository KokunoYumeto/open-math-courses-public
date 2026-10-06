# Topoi, morphisms and points

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Public domain (CC0).*

An ordinary point tests a sheaf by taking germs. A topos lets us retain this operation even when our coverings come from group actions or algebraic maps. The important datum of a point is then a functor to sets, together with the properties that make germs respect gluing and finite equations.

We begin with the maps that preserve this local structure. Localization supplies a particularly concrete map: it replaces a site by objects equipped with an arrow to one chosen object. After constructing its adjoints, we identify two definitions of a point and prove that finite coverings provide enough points to detect every sheaf isomorphism. The final examples explain both what points remember about a space and how one point can remember an entire profinite group.

The prerequisite is Sites and sheaves, including its sheafification, local image and group-action results. We also use basic category theory and the axiom of choice. Sites are small in our fixed universe; sets and sheaves take values in a chosen larger universe when necessary. Basic references are [Stacks] and [Leinster]. The enough-points theorem is due to Deligne.

## 1. Maps between categories of local data

A **Grothendieck topos** is a category equivalent to the category of sheaves of sets on a site. We use *topos* with this meaning throughout. Examples are \(\operatorname{Sh}(X)\) for a space, sets themselves, and the category \(BG\) of continuous discrete left \(G\)-sets for a profinite group. The last example is a topos by the finite continuous group-set equivalence proved in the preceding lesson. Giraud’s characterization gives an intrinsic axiomatic approach to Grothendieck topoi; [Leinster, section 3] discusses its role. Our proofs use the site presentation.

A **morphism of topoi** \(f:\mathcal E\to\mathcal F\), also called a geometric morphism, is an adjunction

\[
f^{-1}:\mathcal F\rightleftarrows\mathcal E:f_*,
\qquad f^{-1}\dashv f_*,
\]

whose left adjoint preserves finite limits. We call this preservation *left exactness*. Since a left adjoint also preserves all colimits, inverse image preserves both finite equations and arbitrary presentations. On abelian group objects it is an exact functor: it preserves kernels by finite limits, and cokernels by colimits. To justify the assertion about cokernels, factor an abelian sheaf map through its local image. Inverse image preserves the epimorphism onto that image and its monomorphism into the target, hence preserves the image. The cokernel is the quotient by this subgroup, formed as the sheaf coequalizer of the subgroup action on the target. Finite products preserve that action, and colimits preserve its coequalizer. The right adjoint need not preserve cokernels.

We will use one elementary presentation repeatedly. Every presheaf \(F\) has a natural presentation

\[
F=\varinjlim_{(U,s),\ s\in F(U)}h_U.
\tag{1.1}
\]

The indexing category has an arrow \((V,t)\to(U,s)\) for an arrow \(a:V\to U\) with \(a^*s=t\). Evaluate the proposed colimit at \(W\). A representative is \((U,s,b:W\to U)\); send it to \(b^*s\). It is identified with \((W,b^*s,\operatorname{id})\), so this map is surjective, and two representatives with the same value are identified through that common representative. It is therefore bijective. Sheafifying (1.1) gives the same presentation for a sheaf, with \(h_U^\#\) and colimits taken in sheaves. In particular, these associated representables determine every colimit-preserving functor and its natural transformations.

For later use, an epimorphism of sheaves is the coequalizer of its kernel pair. Indeed it is locally surjective by the preceding lesson. Two maps out of its source that agree on the kernel pair assign the same value to any two local lifts of a target section. Their values match and glue uniquely. This proves the coequalizer property. Consequently every inverse image preserves epimorphisms, since it preserves this coequalizer.

## 2. From a functor of sites to an inverse image

Let \(u:\mathcal C\to\mathcal D\) be a functor. Restriction of presheaves is

\[
u^pE(V)=E(uV).
\]

We call \(u\) **continuous** when it takes specified covering families to covering families and preserves their base changes: for a covering member \(V_i\to V\) and any \(W\to V\), the natural map

\[
u(W\times_V V_i)\longrightarrow uW\times_{uV}uV_i
\]

is an isomorphism. This is the covering-family convention of [Stacks, Tag 00WU]. The sheaf equalizer diagram then shows that restriction sends sheaves to sheaves. Write \(u^s\) for that restricted functor. The adjunction construction below only needs restriction to preserve sheaves. Our continuity convention includes the stated covering and base-change conditions.

Here is the left adjoint on presheaves, with its indexing direction made explicit. For \(D\in\mathcal D\), let \(\mathcal K_D\) have objects \((V,b:D\to uV)\). An arrow from \((V,b)\) to \((W,c)\) is an arrow \(a:V\to W\) with \(u(a)b=c\). Put

\[
(u_pF)(D)=\varinjlim_{\mathcal K_D^{\mathrm{op}}}F(V).
\tag{2.1}
\]

A map \(D'\to D\) precomposes \(b\), giving the presheaf restriction. Maps from (2.1) to \(E(D)\), natural in \(D\), correspond to maps \(F(V)\to E(uV)\): send a representative \((V,b,s)\) to the restriction along \(b\) of the chosen image of \(s\). Conversely evaluate at \(D=uV,b=\operatorname{id}\). The colimit relations and naturality make these constructions inverse. Thus \(u_p\dashv u^p\). It is the left Kan extension appropriate to contravariant presheaves.

Sheafification gives

\[
u_sF=(u_pF)^\#,
\qquad u_s\dashv u^s.
\tag{2.2}
\]

Indeed, for a sheaf \(E\) on \(\mathcal D\), both adjunctions identify maps \((u_pF)^\#\to E\) with maps \(F\to u^sE\). The same argument shows \((u_pF)^\#\simeq(u_pF^\#)^\#\) for a presheaf \(F\).

**Theorem 2.1.** Suppose \(\mathcal C\) has a final object and fibre products, and \(u\) preserves them. If \(u\) is continuous, (2.2) is a morphism of topoi

\[
\begin{array}{ccc}
\mathcal C&\xrightarrow{\ u\ }&\mathcal D\\
\operatorname{Sh}(\mathcal C)&\xleftarrow{\ f\ }&\operatorname{Sh}(\mathcal D),
\end{array}
\qquad f^{-1}=u_s,\quad f_*=u^s.
\]

Thus the morphism of sites and the geometric morphism go opposite to the underlying functor of sites.

**Proof.** The category \(\mathcal K_D\) is nonempty because there is an arrow \(D\to uX\), where \(X\) is final. A pair of its objects has a common object mapping to both: use \(V\times_X W\) and the pair of arrows from \(D\). Parallel arrows are equalized by their equalizer in \(\mathcal C\). Final objects and fibre products supply equalizers, by pulling back a diagonal along the pair of arrows; preservation of these constructions ensures that the arrow from \(D\) factors through the equalizer. Hence \(\mathcal K_D\) is cofiltered.

Filtered colimits of sets commute with finite limits. The elementwise proof from the previous lesson works for a filtered category as well: finitely many representatives have a common target, and finitely many equalities become equalities at a further target; the ability to equalize parallel arrows makes the representative description well-defined. Formula (2.1) therefore preserves finite limits, section by section. Sheafification does too. Limits of sheaves are sectionwise, so \(u_s\) is left exact. Together with (2.2) this proves the claim. \(\square\)

Continuity alone does not ensure left exactness. Give both sites trivial covering families, let \(\mathcal C\) be the discrete category with two objects, and let \(\mathcal D\) have one object and only its identity. The unique functor is continuous. Its left adjoint takes a pair of sets \((A,B)\) to \(A\amalg B\), so it takes the terminal presheaf \((*,*)\) to a two-element set. It cannot be an inverse image.

For a continuous map \(g:Y\to X\), the functor \(\operatorname{Open}(X)\to\operatorname{Open}(Y)\), \(V\mapsto g^{-1}V\), preserves coverings, the final open and intersections. The theorem gives

\[
(g_*E)(V)=E(g^{-1}V),\qquad g^{-1}F=(u_pF)^\#.
\]

This constructs the usual inverse image without assuming a bundle description of sheaves.

## 3. Working over one object

Fix \(U\in\mathcal C\). The **slice site** \(\mathcal C/U\) consists of arrows \(a:V\to U\); its coverings are those whose underlying families cover in \(\mathcal C\). The axioms follow by retaining the structure maps to \(U\) in each composition and base change. Restriction is

\[
(j_U^{-1}F)(V,a)=F(V).
\]

It preserves sheaves and finite limits directly. Restriction also commutes with sheafification: coverings of \((V,a)\) are exactly coverings of \(V\) equipped with their forced composite arrows to \(U\), so their matching-family diagrams and refinement colimits are identical. Apply the plus construction twice.

**Theorem 3.1.** There are adjoints

\[
j_{U!}\dashv j_U^{-1}\dashv j_{U*},
\qquad
\operatorname{Sh}(\mathcal C/U)\simeq
\operatorname{Sh}(\mathcal C)/h_U^\#.
\]

For a sheaf \(H\) on the slice, \(j_{U!}H\) is the associated sheaf of

\[
L_H(V)=\coprod_{a:V\to U}H(V,a).
\tag{3.1}
\]

The right adjoint has the formula

\[
(j_{U*}H)(V)=
\operatorname{Hom}_{\mathcal C/U}
\bigl(j_U^{-1}h_V^\#,H\bigr),
\tag{3.2}
\]

where the Hom denotes maps of sheaves. If \(V\times U\) exists, (3.2) is \(H(V\times U,\operatorname{pr}_U)\).

**Proof.** A map from (3.1) to a presheaf \(F\) is precisely a natural family of maps \(H(V,a)\to F(V)\). This proves the left adjunction after sheafification.

To construct the right adjoint before sheafification, replace the first argument of (3.2) by the restricted presheaf \(h_V\). A member of its section set assigns an element of \(H(W,a)\) to each arrow \(b:W\to V\), naturally in the object \((W,a)\) of the slice. This presheaf is a sheaf. Given matching such rules over a covering \(V_i\to V\), pull that covering back along \(b\). The resulting cover of \((W,a)\) supplies matching elements of \(H\), which glue uniquely. Uniqueness also proves that the glued rules are natural in \((W,a)\). It proves separation as well. Since restriction commutes with sheafification, this section set is exactly (3.2).

A map \(j_U^{-1}F\to H\) sends a section \(s\in F(V)\) to the rule that assigns the image of \(b^*s\) on every \((W,a,b:W\to V)\). Conversely a map \(F\to j_{U*}H\) gives a map \(F(W)\to H(W,a)\) by evaluating its rule on \(\operatorname{id}_W\). These operations are inverse, proving the right adjunction. If the product exists, restricted \(h_V\) is represented in the slice by \(V\times U\); Yoneda proves the last formula.

For the equivalence, (3.1) has a map \(L_H\to h_U\), sending a section in the summand labelled \(a\) to that arrow. Sheafify to obtain \(j_{U!}H\to h_U^\#\). In the other direction, from \(E\xrightarrow{q}h_U^\#\) form the sheaf on the slice

\[
H_q(V,a)=\{s\in E(V):q(s)=\eta(a)\}.
\tag{3.3}
\]

It is a sheaf because sections glue in \(E\), and equality of their images is tested on a covering.

We check both composites, including the case where \(h_U\) is not a sheaf. The natural map \(L_{H_q}\to E\) is locally surjective: a section's image in \(h_U^\#\) locally has an actual arrow \(a\) as representative, which places that section in the corresponding summand. If two representatives have the same image in \(E\), their labels have the same image in \(h_U^\#\). Refine until the arrows themselves agree; they then belong to one summand and are equal there. Local equality therefore makes \(L_{H_q}^\#\to E\) an isomorphism.

For the other composite, the natural map \(H(V,a)\to H_q(V,a)\) sends a section to the sheafified summand labelled \(a\). A member of the target locally has a representative labelled \(b\); because its image is \(\eta(a)\), a further covering makes \(b=a\). It is thus locally in the image of \(H\). If two original sections acquire the same image, refine their equality in \(L_H\); their labels remain the same arrow, so the sections are equal locally in \(H\), hence equal. The map is injective and locally surjective, and is consequently an isomorphism. All constructions are natural in arrows and morphisms of sheaves. They give the equivalence. \(\square\)

Under this equivalence, \(j_U^{-1}F\) corresponds to \(F\times h_U^\#\to h_U^\#\); the left adjoint forgets that structure map. In particular, for sets \(j_{U!}\) extends by the empty set and takes the terminal sheaf to \(h_U^\#\). It need not preserve the terminal object.

For abelian sheaves, the left adjoint instead sheafifies

\[
V\longmapsto\bigoplus_{a:V\to U}H(V,a).
\tag{3.4}
\]

The direct-sum universal property proves the adjunction just as in (3.1). The right adjoint is (3.2) applied to underlying sets, with pointwise addition on natural rules. The formulas and gluing proof show that its values are abelian groups and that the adjunction respects addition. The slice equivalence above concerns sheaves of sets; it must not be read as an equivalence with a slice of the abelian category.

**Example 3.2.** For an open inclusion \(j:U\hookrightarrow X\), (3.4) starts with \(H(V)\) when \(V\subset U\) and zero otherwise. Its associated sheaf is **extension by zero**. Concretely, a section over \(V\) is a section \(s\in H(V\cap U)\) such that every \(x\in V\setminus U\) has a neighbourhood \(W\subset V\) on which \(s|_{W\cap U}=0\). To prove the description, local representatives from (3.4) are sections inside \(U\) and zero representatives near points outside it. Conversely glue \(s\) on \(V\cap U\) to these zeros; the stated condition is exactly agreement on their overlaps. Uniqueness follows from separation. Thus its stalk is \(H_x\) inside \(U\) and zero outside. Equivalently the support of the extended section is closed in \(V\) and contained in \(U\).

For \(U=(0,1)\subset\mathbb R\) and the constant abelian sheaf \(\underline{\mathbb Z}\) on \(U\), a locally constant section on \(U\) is constant. The condition at either endpoint forces that constant to be zero. Hence \(\Gamma(\mathbb R,j_!\underline{\mathbb Z})=0\), whereas \(\Gamma(\mathbb R,j_*\underline{\mathbb Z})=\mathbb Z\).

## 4. A point is an exact way to take germs

For a functor \(v:\mathcal C\to\mathrm{Sets}\), its **neighbourhood category** has objects \((U,x)\) with \(x\in vU\). An arrow \((V,y)\to(U,x)\) is an arrow \(a:V\to U\) satisfying \(v(a)y=x\). For any presheaf define

\[
F_v=\varinjlim_{(U,x)^{\mathrm{op}}}F(U).
\tag{4.1}
\]

A representative is a triple \((U,x,s)\); the relations identify it with \((V,y,a^*s)\) along such an arrow. These relations generate an equivalence relation, which need not have a common-refinement description for an arbitrary \(v\).

A **point of the site** is a functor \(v\) with three properties:

1. Coverings induce jointly surjective families of sets \(vU_i\to vU\).
2. For each covering member \(U_i\to U\) and arrow \(V\to U\), the map \(v(U_i\times_U V)\to vU_i\times_{vU}vV\) is bijective.
3. The functor (4.1) on sheaves preserves finite limits.

This definition retains the exactness condition; it does not silently infer it from the first two properties.

**Theorem 4.1.** A point of a site defines a geometric morphism \(p:\mathrm{Sets}\to\operatorname{Sh}(\mathcal C)\) with \(p^{-1}F=F_v\). Conversely every such geometric morphism comes from a point of the site. Stalks preserve all colimits and finite limits. For an abelian sheaf the stalk is an abelian group, and this functor is exact.

**Proof.** For a set \(A\), define

\[
(p_*A)(U)=\operatorname{Maps}(vU,A).
\tag{4.2}
\]

Compatible maps on a covering glue uniquely as functions on \(vU\): joint surjectivity supplies all arguments, and property 2 makes equality on overlaps the equality required for independence of the chosen lift. Hence (4.2) is a sheaf. For an arbitrary presheaf \(F\), a natural map \(F\to p_*A\) is a natural family of pairings \(F(U)\times vU\to A\). This is precisely a map \(F_v\to A\), by the relations in (4.1). Thus stalk is left adjoint to (4.2), also when restricted to sheaves. Property 3 now gives a geometric morphism. Left adjointness proves preservation of all sheaf colimits.

This argument also proves that sheafification does not change the stalk: maps \(F_v\to A\) and \((F^\#)_v\to A\) are naturally the same, by the sheafification adjunction into the sheaf (4.2). Yoneda for sets identifies the two stalks.

Conversely let \(p\) be a geometric morphism and set \(vU=p^{-1}h_U^\#\). A covering gives an epimorphism \(\coprod h_{U_i}^\#\to h_U^\#\); local representation of arrows proves this directly. Preservation of epimorphisms and coproducts proves property 1. Associated representables preserve any existing fibre product, by the Yoneda description and left exact sheafification. Applying \(p^{-1}\) proves property 2.

For any functor \(v\), the stalk of \(h_U\) is naturally \(vU\). Send a triple \((V,y,b:V\to U)\) to \(v(b)y\); it is identified with \((U,v(b)y,\operatorname{id})\), which proves both directions of the bijection. For our reconstructed \(v\), (4.2) is a sheaf by the already proved properties 1 and 2. Thus \((h_U^\#)_v=(h_U)_v=vU=p^{-1}h_U^\#\). The comparison sends the class of \((U,x,s)\), viewed as the arrow \(s:h_U^\#\to F\), to \(p^{-1}(s)(x)\). On \(h_U\) it is exactly the displayed bijection. Both sides preserve colimits, so the sheaf presentation (1.1) proves the comparison is an isomorphism for every \(F\). Property 3 follows from left exactness of \(p^{-1}\), and the constructed geometric morphism is isomorphic to \(p\). The constructions are inverse up to their natural identifications.

An inverse image takes group objects to group objects because their multiplication, inverse, identity and axioms use finite products and equalities. Its abelian functor preserves kernels and cokernels as observed in section 1. Alternatively the pairing proof with abelian-group-valued (4.2) proves the abelian adjunction directly. Hence abelian stalks are exact. \(\square\)

**Proposition 4.2.** If \(\mathcal C\) has finite limits, its points are exactly the finite-limit-preserving functors \(v:\mathcal C\to\mathrm{Sets}\) that take coverings to jointly surjective families. Their neighbourhood categories are cofiltered.

**Proof.** A finite-limit-preserving \(v\) supplies a nonempty neighbourhood, using the final object. Products give common neighbourhoods of a pair, and equalizers give neighbourhoods equalizing parallel arrows. Thus the neighbourhood category is cofiltered, and the filtered-colimit argument proves that (4.1) preserves finite limits. It also supplies property 2, so such a \(v\) is a point. Conversely Theorem 4.1 identifies a site's point functor with \(U\mapsto p^{-1}h_U^\#\), which preserves finite limits. \(\square\)

For a space and \(x\in X\), use \(v_x(U)=*\) when \(x\in U\) and \(\varnothing\) otherwise. Its nonempty neighbourhoods are the ordinary open neighbourhoods of \(x\); intersections make them cofiltered. Formula (4.1) is the ordinary germ stalk. For a continuous map \(g:Y\to X\), the composite of the point at \(y\) with its geometric morphism has value \(*\) on \(h_V^\#\) exactly when \(g(y)\in V\). Theorem 4.1 and (1.1) therefore give \((g^{-1}F)_y\simeq F_{g(y)}\).

## 5. Constructing enough tests

A family of points is **conservative** if a map of sheaves that is an isomorphism at every point is already an isomorphism. A topos **has enough points** if it has such a family.

**Proposition 5.1.** For a conservative family, a map of sheaves is a monomorphism, an epimorphism or an isomorphism exactly when its stalk maps have that property. A sequence of abelian sheaves is exact exactly when its stalk sequences are exact. A family is conservative if and only if it detects epimorphisms.

**Proof.** Inverse images preserve finite limits and epimorphisms, so all the forward implications hold. A map \(a:F\to E\) is a monomorphism exactly when its diagonal \(F\to F\times_E F\) is an isomorphism; this follows sectionwise. If all stalks of \(a\) are injective, the diagonal is an isomorphism at every point and hence an isomorphism.

Let \(I\subset E\) be the local image of \(a\). The factorization \(F\to I\) is an epimorphism: sections of \(I\) locally lift by its definition. At any point the factorization has a surjection followed by an injection, so the latter identifies \(I_p\) with the set image of \(a_p\). If all \(a_p\) are surjective, \(I\to E\) is an isomorphism at all points, hence an isomorphism. Thus \(a\) is an epimorphism. Combined with the mono criterion, this proves the isomorphism criterion.

For abelian sheaves, stalks preserve kernels and cokernels and therefore images. When the composite in a sequence is zero, its exactness is equivalent to the natural map from the image of the first arrow to the kernel of the second being an isomorphism. Apply the isomorphism criterion. If the composite has not been assumed zero, zero composites at all points imply it is zero: its equalizer with the zero map becomes an isomorphism at all points and hence is an isomorphism.

We have proved that a conservative family detects epimorphisms. Conversely suppose it detects epimorphisms, and let \(a\) have bijective stalk maps. It is an epimorphism. Its diagonal also has bijective stalk maps, so is an epimorphism by the same detection assumption. A diagonal is a monomorphism; the mono-and-epi criterion for sheaves makes it an isomorphism. Thus \(a\) is a monomorphism as well, and is an isomorphism. \(\square\)

We now construct points by retaining distinctions while resolving covering requests. Let \(I\) be a nonempty directed partially ordered set, and let \((V_i)\) be an inverse system: for \(i'\ge i\) there are compatible transition arrows \(V_{i'}\to V_i\). Define

\[
v(W)=\varinjlim_i\operatorname{Hom}(V_i,W).
\tag{5.1}
\]

Each representable functor on the right preserves finite limits that exist in \(\mathcal C\). Directed colimits commute with finite limits, so \(v\) does too. Its stalk on a presheaf is

\[
F_v=\varinjlim_i F(V_i).
\tag{5.2}
\]

To verify this formula, a representative \((W,[b:V_i\to W],s)\) in (4.1) maps to \([b^*s]\). A different representative of \([b]\) agrees after a later stage, so it gives the same class. The neighbourhood relations also preserve this class. Conversely send \([t]\), with \(t\in F(V_i)\), to \((V_i,[\operatorname{id}_{V_i}],t)\). Transition arrows identify these triples; the two constructions are inverse. These checks also prove naturality.

An **extension** of the system will mean a larger directed index set containing the original as an induced subposet, with the same objects and transitions on it. The original index set need not be cofinal in the extension. Such an extension gives natural maps of the functors (5.1) and stalks (5.2).

**Lemma 5.2.** Suppose \(F\) is a sheaf, and two classes \(s,t\in\varinjlim_iF(V_i)\) are distinct. For a finite covering \(\{W_k\to W\}_{k=1}^m\) and \(b\in v(W)\), there is an extension in which \(s,t\) remain distinct and the image of \(b\) lifts to one of the sets \(v(W_k)\).

**Proof.** Represent \(b\) by \(b_0:V_{i_0}\to W\). On the cofinal tail \(I_0=\{i:i\ge i_0\}\), set

\[
V_{i,k}=V_i\times_W W_k.
\]

This is a finite covering of \(V_i\). Separation gives injections \(F(V_i)\to\prod_kF(V_{i,k})\). Taking the directed colimit and commuting it with the finite product gives an injection

\[
\varinjlim_i F(V_i)\longrightarrow
\prod_{k=1}^m\varinjlim_{i\in I_0}F(V_{i,k}).
\]

Hence some factor retains the distinction between \(s,t\). If \(m=0\), the injection into a singleton would contradict their distinction; thus such an empty-cover request cannot occur here.

Choose a factor \(k\) retaining the distinction. Use the index set

\[
I'= (I\times\{0\})\amalg(I_0\times\{1\}).
\]

Within each summand retain the old order. Put \((i,0)\le(j,1)\) exactly when \(i\le j\), and put no element of the second summand below one of the first. It is directed: a common upper bound in the old tail gives a common upper bound in the second summand. Attach \(V_i\) to \((i,0)\) and \(V_{i,k}\) to \((i,1)\). Transitions within the second summand are induced by base change. A transition from \((j,1)\) to \((i,0)\) is the projection to \(V_j\) followed by its old transition to \(V_i\). The universal property of the fibre products proves compatibility of all these transitions.

The second summand is cofinal in \(I'\), so (5.2) for the extension is the chosen factor colimit. The two classes remain distinct. The arrow \(V_{i_0,k}\to W_k\) gives a lift of \(b\), since its composite to \(W\) is the pullback of \(b_0\). \(\square\)

**Theorem 5.3 (Deligne).** If a small site has finite limits and every covering has a refinement by a finite covering, then its topos has enough points.

**Proof.** We first separate any two distinct sections \(s,t\in F(U)\) of any sheaf. Start with the one-object system \(V_0=U\). Its stalk is \(F(U)\), so the distinction is present.

For any current system, consider the set of all requests

\[
\bigl(\{W_k\to W\}_{k=1}^m,\ b\in v(W)\bigr)
\tag{5.3}
\]

over its finite coverings. This is a set: the category is small, finite lists of its arrows form a set, and every \(v(W)\) is a set. Well-order the requests. Apply Lemma 5.2 successively, retaining the distinction throughout. At a limit ordinal take the union of the previous index sets, orders, objects and transitions. The union is directed, because any pair of its indices occurs at some earlier stage. Distinctness persists: an equality in its directed colimit would have a representative and a witnessing index at an earlier stage, contradicting distinctness there. Previously obtained lifts persist under all later extensions. Transfinite recursion along this set-sized well-order therefore gives a system that resolves every request of the system at the start of the recursion.

There can be new arrows in (5.1) after that recursion. To handle them, repeat this entire operation for the resulting system, and do so for each nonnegative integer. At the end take the union of these countably many systems. Every index, and hence every representative arrow \(V_i\to W\), occurs in one of the rounds. Its request for any finite covering is resolved in the following round. Thus the final functor \(v\) takes every finite covering to a jointly surjective family. A finite refinement of an arbitrary covering then gives joint surjectivity for that covering too: each refining member factors through an original member.

The final functor preserves finite limits by (5.1). Proposition 4.2 makes it a point. Formula (5.2) shows that our original two sections still have distinct germs. All index sets used are sets: each successor step adds one copy of a tail, and the transfinite and countable unions have set-sized indexing. No maximality assertion on a proper class is involved.

We finish by obtaining a set of points that is conservative. The associated representables \(A_U=h_U^\#\) form a set of generators by (1.1). For each proper subsheaf \(I\subset A_U\), form the sheaf pushout \(Q=A_U\amalg_I A_U\). The two copies of the identity section on \(U\) are distinct in \(Q(U)\). Otherwise local equality in the pointwise pushout would put that identity locally in \(I\), hence in \(I(U)\). Restrictions would then put every actual arrow into \(I\), and local representation of every section of \(A_U\) would force \(I=A_U\). Apply the construction above to these two sections and choose one separating point. At this point \(I_p\to(A_U)_p\) cannot be surjective, since the two copy maps agree on \(I_p\) but differ on a germ.

There is a set of such pairs \((U,I)\): a subsheaf chooses subsets of each of the sets \(A_U(V)\), subject to restriction and gluing conditions. These choices lie in a product of power sets over the small category. Now if a map \(F\to E\) is not an epimorphism, its local image \(J\subset E\) is proper. Choose \(e\in E(U)\setminus J(U)\), and pull \(J\) back along the corresponding map \(A_U\to E\). This is a proper subsheaf \(I\subset A_U\). A point chosen for \(I\) makes \(I_p\to(A_U)_p\) nonsurjective. Since inverse image preserves the pullback, \(J_p\to E_p\) cannot be surjective either. The map \(F_p\to E_p\), which factors through \(J_p\), is therefore nonsurjective. The chosen set of points detects epimorphisms. Proposition 5.1 makes it conservative. \(\square\)

The repeated rounds in this proof have a specific purpose: resolving every request for the starting functor need not resolve requests involving elements that only appear in the enlarged functor. Each element of the final union must be handled at a later round.

This criterion has hypotheses. It does not assert that every site has enough points. For the later étale examples we will use a finite-presentation basis over a quasi-compact quasi-separated scheme: its finite limits and finite covering refinements will be verified there. Large lists of arbitrary étale objects need not themselves have finite covering refinements.

## 6. What points remember about a space

A family \(\mathcal P\) of open subsets of \(X\) is a **completely prime filter** if it contains \(X\), does not contain \(\varnothing\), is upward closed and closed under finite intersections, and has the following property: if an arbitrary union belongs to \(\mathcal P\), at least one member of the union belongs to \(\mathcal P\). It defines a functor on opens by assigning \(*\) to the members and \(\varnothing\) to the other opens. This preserves finite limits and sends open coverings to jointly surjective families. Proposition 4.2 therefore gives a point.

Conversely a point \(p\) assigns to the representable sheaf of an open \(V\) a subobject of \(p^{-1}*=*\), because that representable is subterminal. The value is either \(*\) or \(\varnothing\). The opens with value \(*\) form a completely prime filter: inclusions give upward closure, intersections give finite intersection closure, and a covering by the members of an arbitrary union gives complete primeness. Theorem 4.1 shows that this reconstructs the point up to isomorphism. Thus points of \(\operatorname{Sh}(X)\) are classified by these filters.

**Proposition 6.1.** If \(X\) is sober, every point of \(\operatorname{Sh}(X)\) comes from a unique point of \(X\), up to isomorphism of geometric points.

**Proof.** Recall that sober means every nonempty irreducible closed subset has a unique generic point, a point whose closure is that subset. Given a completely prime filter \(\mathcal P\), let

\[
B=\bigcup_{V\notin\mathcal P}V,\qquad C=X\setminus B.
\]

Complete primeness shows \(B\notin\mathcal P\), so \(C\ne\varnothing\). For an open \(V\), we claim

\[
V\in\mathcal P\quad\Longleftrightarrow\quad V\cap C\ne\varnothing.
\tag{6.1}
\]

If \(V\notin\mathcal P\), it is contained in \(B\). If \(V\in\mathcal P\) were contained in \(B\), write it as the union of its intersections with all the opens outside \(\mathcal P\). None of these intersections belongs to \(\mathcal P\), by upward closure. Their union cannot belong to it either, a contradiction. This proves (6.1). Finite intersection closure of the filter now shows that two opens meeting \(C\) have an intersection meeting \(C\). This is exactly irreducibility of the nonempty closed subset \(C\).

Let \(x\) be its unique generic point. An open meets \(\overline{\{x\}}\) exactly when it contains \(x\): if it contains a point in that closure, its being a neighbourhood of that point forces it to meet \(\{x\}\). Thus (6.1) says \(\mathcal P\) is the neighbourhood filter of \(x\). Its site functor is \(v_x\), and Theorem 4.1 identifies its point with the ordinary point at \(x\). Uniqueness follows from sobriety, or from equality of the corresponding closures. \(\square\)

**Example 6.2.** Let \(X\) be infinite with the cofinite topology. The family of all nonempty opens is a completely prime filter: two cofinite opens intersect, and any nonempty union has a nonempty member. Its stalk is

\[
F\longmapsto\varinjlim_{\varnothing\ne V\subset X\ \mathrm{open}}F(V).
\]

This point comes from no element of \(X\). For any \(x\), the nonempty open \(X\setminus\{x\}\) belongs to the filter but not to the neighbourhood filter of \(x\). The associated closed irreducible set is all of \(X\), while \(X\) is \(T_1\), so no individual point is generic for it. This explains the sobriety hypothesis.

Ordinary space points nevertheless form a conservative family for any space. If a germ map is injective everywhere, two sections with equal images agree on a neighbourhood of each point and therefore agree. If all germ maps are surjective, a target section has a lift on a neighbourhood of each point, which is precisely local surjectivity. The criteria from the preceding lesson give an isomorphism. Extra topos points do not remove the usefulness of the ordinary ones.

## 7. What a single point remembers about a group

All actions in this section are left actions on discrete sets, and all groups are profinite. Continuity means that stabilizers are open. We first construct a map of topoi from a continuous homomorphism \(\varphi:H\to G\).

Restriction gives \(f^{-1}:BG\to BH\): let \(h\) act through \(\varphi(h)\). The restricted action is continuous because preimages of open stabilizers are open. Finite limits are formed on underlying sets with the induced action, so restriction preserves them.

For \(T\in BH\), define

\[
\operatorname{Coind}_{H}^{G}T=
\{b:G\to T\text{ continuous}:b(\varphi(h)g)=h\,b(g)
\text{ for all }h,g\}.
\tag{7.1}
\]

Give it the discrete topology and the left \(G\)-action

\[
(a\cdot b)(g)=b(ga).
\tag{7.2}
\]

The defining relation is preserved by right translation, and \(a\cdot(c\cdot b)=(ac)\cdot b\). The action on this discrete set is continuous. To check it, a continuous function from compact \(G\) to discrete \(T\) is constant on a neighbourhood of each argument. Choose these neighbourhoods to have the form \(g_iN_i\), with \(N_i\) open normal, and take a finite subcover. The intersection \(N\) of these finitely many subgroups makes \(b(gn)=b(g)\) for all \(n\in N\): when \(g\in g_iN_i\), both arguments lie in that same coset. Thus \(N\) fixes \(b\) in (7.2), so its stabilizer is open.

**Proposition 7.1.** Restriction and (7.1) are adjoint. They define a morphism \(BH\to BG\) with \(f_*T=\operatorname{Coind}_{H}^{G}T\).

**Proof.** From an \(H\)-equivariant map \(\psi:f^{-1}S\to T\), define

\[
\beta_\psi(s)(g)=\psi(gs).
\]

The orbit map \(G\to S\) is continuous, so this function is continuous. The \(H\)-equivariance of \(\psi\) gives the relation in (7.1), and (7.2) gives \(G\)-equivariance of \(\beta_\psi\). Conversely evaluate a \(G\)-equivariant map \(\beta:S\to\operatorname{Coind}_{H}^{G}T\) at \(1\). For \(h\in H\),

\[
\beta(\varphi(h)s)(1)
=\beta(s)(\varphi(h))
=h\,\beta(s)(1),
\]

so the resulting map is \(H\)-equivariant. Evaluation recovers \(\psi\), and \(G\)-equivariance recovers \(\beta(s)(g)\) from its value at \(1\). These inverse natural constructions prove the adjunction. Restriction is left exact, so it is an inverse image. \(\square\)

For \(H=1\), this map is the forgetful point \(p:\mathrm{Sets}\to BG\). Its right adjoint consists of continuous functions \(G\to A\), with right translation on arguments. For \(G=\mathbb Z/2\mathbb Z\) and \(A=\{0,1\}\), it is a four-element \(G\)-set: the two constant functions are fixed, and the two nonconstant functions are exchanged. This explicitly computes a direct image, whose underlying set is larger than \(A\).

We need a small compactness fact. An inverse system of nonempty finite sets over a directed set has a nonempty inverse limit. Here is a choice-based proof. In the product of the finite sets, the compatibility conditions have the finite intersection property: choose an upper bound of all indices occurring in finitely many conditions, an element at that upper bound, and its images at those indices. Extend the resulting filter of subsets of the product to an ultrafilter, using Zorn's lemma on the set of filters. For each finite coordinate partition, exactly one cell belongs to the ultrafilter; choose its value. Every compatibility condition belongs to the ultrafilter and hence holds for the selected coordinate values, since a conflicting pair of coordinate cells would have empty intersection with it. The values form an element of the inverse limit.

**Theorem 7.2.** Every point of \(BG\) is isomorphic to the forgetful point. The automorphism group of the forgetful point is naturally \(G\); its finite-quotient topology is the original profinite topology.

**Proof.** Let \(P:BG\to\mathrm{Sets}\) be the inverse image of a point. For an open normal subgroup \(N\), put \(A_N=G/N\) with its regular left action. Right translations are equivariant endomorphisms of \(A_N\). They make \(P(A_N)\) a right \(G/N\)-set. The map \(A_N\to *\) is an epimorphism, so \(P(A_N)\) is nonempty. There is an isomorphism of left \(G\)-sets

\[
\coprod_{a\in G/N}A_N\xrightarrow{\sim}A_N\times A_N,
\qquad (a,z)\longmapsto(z,za).
\]

Since \(P\) preserves coproducts and products, any two elements of \(P(A_N)\) are related by a unique right translation. Thus \(P(A_N)\) is a right torsor under the finite group \(G/N\), and is a nonempty finite set. For \(N'\subset N\), the quotient map induces a surjection \(P(A_{N'})\to P(A_N)\). The compactness fact supplies a compatible choice \(a_N\in P(A_N)\).

For a finite continuous \(G\)-set \(S\), choose \(N\) acting trivially on it. An element \(s\in S\) defines \(q_s:A_N\to S\), \(gN\mapsto gs\). Set

\[
\lambda_S(s)=P(q_s)(a_N).
\tag{7.3}
\]

Passing to a smaller normal subgroup leaves this formula unchanged by compatibility of the choices. It is natural under equivariant maps. We show it is a bijection. For a transitive \(S=G/K\) with \(N\subset K\), the map \(A_N\to G/K\) is the coequalizer of the right translations by \(K/N\). This follows on sets by taking their orbits, and the quotient has its continuous induced action. Applying \(P\), its value is the quotient of the right torsor \(P(A_N)\) by \(K/N\). The choice \(a_N\) identifies this quotient with the set of right cosets \((G/N)/(K/N)=G/K\); this is (7.3). A finite \(G\)-set is a finite disjoint union of these orbits, and \(P\) preserves that coproduct. Thus (7.3) is bijective for all finite \(S\).

Every continuous discrete \(G\)-set is the filtered union of its finite invariant subsets. Each orbit is finite because its stabilizer is open and the compact group has only finitely many cosets of an open subgroup. Finite unions of orbits form the required directed family. Both \(P\) and the forgetful functor preserve its colimit; the latter's right adjoint was constructed above. Therefore (7.3) extends to a natural isomorphism between them on all continuous \(G\)-sets. An isomorphism of left adjoints identifies their right adjoints and their adjunctions, so it is an isomorphism of points.

Now let \(\alpha\) be a natural automorphism of the forgetful functor. On \(A_N\), naturality with all right translations shows

\[
\alpha_{A_N}(z)=g_Nz,
\qquad g_N=\alpha_{A_N}(1N)\in G/N.
\]

Naturality with quotient maps makes the \(g_N\) compatible. They give an element \(g\in\varprojlim_N G/N=G\). For completeness, this identification follows from compactness: the compatible cosets in \(G\) are closed and have the finite intersection property, so they have a common element. That element is unique because open normal subgroups form a neighbourhood basis and \(G\) is Hausdorff. For any \(s\) in a continuous \(G\)-set, choose \(N\) inside its stabilizer and use naturality with \(q_s:A_N\to S\). It gives \(\alpha_S(s)=gs\). Conversely left multiplication by a fixed \(g\) commutes with every equivariant map and is invertible, so gives a natural automorphism. Composition corresponds to multiplication in \(G\). Requiring trivial action on each \(A_N\) gives the kernels \(N\), which are exactly a neighbourhood basis for its profinite topology. \(\square\)

The isomorphism of an arbitrary point with the forgetful point uses choices of torsor elements and is not canonical. Its automorphisms retain the group even though there is only one isomorphism class of points. This is the fibre-functor phenomenon that also appears in Galois categories.

## 8. Exercises

1. **Generators determine a map — easy.** Suppose two inverse-image functors between categories of sheaves have a natural isomorphism on the associated representables, compatible with every arrow of the site. Extend it to all sheaves and show the geometric morphisms are isomorphic. Explain why merely knowing the isomorphism classes of the generator images is insufficient.
2. **Coinduction in coordinates — medium.** Verify the action and adjunction in (7.1)–(7.2) directly. If \(H\subset G\) is a closed subgroup and acts trivially on a finite set \(A\), describe the coinduction using left cosets. Compute it for \(G=\mathbb Z/3\mathbb Z\), \(H=1\) and \(A=\{0,1\}\), including its orbit decomposition.
3. **An extra generic point — medium.** Recover the closed irreducible subset from a completely prime filter. Deduce the sober-space classification, and compute the additional point for an infinite cofinite space on a representable open sheaf. Compare it with evaluation at an actual point.
4. **Testing only surjectivity — medium.** Prove the final equivalence in Proposition 5.1 using diagonals and local images. Indicate where finite-limit preservation and preservation of epimorphisms are used.
5. **Recover the group — hard.** Reconstruct a natural automorphism of the forgetful functor from its value on the identity coset of every finite normal quotient. Prove compatibility, uniqueness on infinite continuous sets, and the assertion about topology.
6. **A round of lifting is not the end — hard.** In the construction of Theorem 5.3, explain precisely which requests a single well-ordered recursion handles. Prove that countably repeated rounds handle every request of the final functor, including when the initial directed system has no largest index.

## 9. Solutions

**1.** Express \(F\) by (1.1), sheafified. Each inverse image preserves that colimit. The compatible isomorphisms on \(h_U^\#\) are an isomorphism between the two diagrams presenting its images, and therefore induce an isomorphism on their colimits. Naturality of (1.1) makes this isomorphism natural in \(F\). The right adjoints are then identified by the adjunction bijections, so the geometric morphisms are isomorphic. Compatibility on generator arrows is essential: it determines the arrows in the colimit diagram. Objectwise isomorphism classes do not specify them.

**2.** Right translation preserves the relation \(b(hg)=h b(g)\), and successive translations give \((a\cdot(c\cdot b))(g)=b(gac)\). Compactness gives a finite cover by cosets on which \(b\) is constant; their common open normal subgroup fixes \(b\). Thus the action is continuous. The maps \(\psi\mapsto[s\mapsto(g\mapsto\psi(gs))]\) and \(\beta\mapsto[s\mapsto\beta(s)(1)]\) are inverse by equivariance, giving the adjunction.

If \(H\) acts trivially on \(A\), the relation says \(b\) is constant on each left coset \(Hg\). Coinduction is the continuous maps \(H\backslash G\to A\), with \(a\) acting by \(Hg\mapsto Hga\) on the argument. The quotient topology and the discrete target express continuity. For the stated cyclic group of order three it is the eight binary words of length three, with cyclic shift. The words \(000\) and \(111\) are fixed. The three words with exactly one \(1\) form one orbit of size three, and those with exactly two \(1\)'s form the other. This computes all eight elements and their stabilizers.

**3.** The closed subset is \(C=X\setminus\bigcup_{V\notin\mathcal P}V\). The proof of (6.1) uses complete primeness for arbitrary unions; finite intersection closure makes \(C\) irreducible. In a sober space its unique generic point recovers the filter. In the infinite cofinite space the filter contains every nonempty open, so \(C=X\). For an open \(V\), the representable \(h_V\) has stalk \(*\) at this extra point if \(V\ne\varnothing\), and \(\varnothing\) if \(V=\varnothing\). This follows either from the filter functor or by restricting along nonempty opens contained in \(V\). At an ordinary point \(x\), its value is instead \(*\) exactly when \(x\in V\). The open \(X\setminus\{x\}\) distinguishes the two.

**4.** If the family is conservative and every stalk map of \(F\to E\) is surjective, factor the map through its local image \(I\). Preservation of epimorphisms makes \(F_p\to I_p\) surjective, and finite-limit preservation makes \(I_p\to E_p\) injective. Thus the latter is bijective, so conservativity gives \(I=E\). Conversely if a family detects epimorphisms, any map with bijective stalks is an epimorphism, and so is its diagonal, since finite-limit preservation makes the diagonal stalk an isomorphism. The diagonal is already a monomorphism, so is an isomorphism; the original map is both mono and epi, hence an isomorphism. This is precisely conservativity.

**5.** Put \(g_N=\alpha_{G/N}(1N)\). Naturality with right multiplication forces \(\alpha_{G/N}(z)=g_Nz\), and naturality with normal-quotient maps forces \(g_{N'}\mapsto g_N\) for \(N'\subset N\). These give the unique \(g\in G\). For any element \(s\) of any continuous set, an open normal subgroup lies in its stabilizer. Naturality with \(q_s:G/N\to S\) gives \(\alpha_S(s)=gs\). Thus all infinite sets as well as finite ones are determined. Conversely the action of \(g\) defines the required natural automorphism. The subgroup fixing the entire finite quotient \(G/N\) is \(N\), so the resulting inverse-limit topology is the original one.

**6.** A single recursion fixes its request set at the beginning; its elements \(b\in v(W)\) are elements of that beginning functor. New indices and arrows may contribute new classes to the enlarged \(v(W)\), which that recursion did not list. In the countable sequence, every final index belongs to some round, since the final index set is a union. A class at the end has a representative at that index. For any finite covering of its target, its request is therefore listed in the next round and resolved there. The chosen lift survives in the final union. No largest index is required: directedness gives common upper bounds for finite comparisons, and union at limit stages preserves directedness. Distinctness survives because any equality would be witnessed by an index in an earlier round.

## What this lesson does not prove

We use the results proved in Sites and sheaves, including the exact sheafification adjunction, local surjectivity criterion, limits and colimits, and finite continuous group-set equivalence. The Yoneda lemma and the axiom of choice remain categorical and set-theoretic prerequisites. Giraud’s intrinsic characterization is mentioned only for orientation, following [Leinster, section 3]; its axioms and proof are not used. Scheme-theoretic points and the finite-presentation étale basis are established in the later lesson on the étale site and its points.

## References

- **[Stacks]** The Stacks Project Authors, *The Stacks Project*, “Sites and Sheaves”: [Tag 00WU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-section-continuous-functors) on continuity; [Tag 00X6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-proposition-get-morphism) on the left exact adjunction; [Tag 00XZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-section-localize) on localization; [Tags 00Y3 and 00Y5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-section-points) on points; and [Tag 00YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites.html#sites-proposition-criterion-points), Deligne's enough-points theorem, whose origin is SGA 4, Exposé VI, appendix, Proposition 9.0. The AI Integrated Stacks Project reader linked here contains AI-proposed corrections and AI-written additions and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
- **[Leinster]** Tom Leinster, *An informal introduction to topos theory* (2010), [arXiv:1012.5647](https://arxiv.org/abs/1012.5647), sections 1 and 3. Motivation for topoi as spaces and geometric morphisms.
