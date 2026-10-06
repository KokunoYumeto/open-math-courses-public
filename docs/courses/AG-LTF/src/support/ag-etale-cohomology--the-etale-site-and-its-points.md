# The étale site and its points

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. **Self-checked by the writing AI, GPT-6.1 Sol (OpenAI).** Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Public domain (CC0).*

An ordinary point of a scheme does not select a branch of an étale cover. A geometric point does: its algebraically closed residue field supplies a lift to each nonempty étale fibre. Following that chosen lift through successively smaller étale neighbourhoods defines a stalk. The resulting local ring is a strict henselization, and every point of the étale topos arises in this way.

We begin with these neighbourhoods and their exactness properties, then identify their rings and classify topos points. The same local method makes extraction of roots of units possible when the exponent is invertible. Kummer theory consequently describes degree-one cohomology by a line bundle together with a trivialization of its tensor power.

We use Topologies on schemes, especially its small site, representable sheaves and Hilbert 90, and the point formalism and cohomology of lessons 2–3. The existence and characterization of henselizations are the algebraic prerequisites stated precisely in section 3. We prove the particular lifting and neighbourhood comparisons needed here.

## 1. The small site remembers branches

The small étale site \(X_{\mathrm{ét}}\) has schemes étale over \(X\) as objects and all \(X\)-morphisms as arrows. Its coverings are jointly surjective families. Every arrow between its objects is étale: its graph is an open immersion, since the target is unramified over \(X\), and the remaining projection is a base change of the source's étale structural map. Thus the covering description really is equivalent to the étale-cover description of lesson 5. No separatedness assumption on \(X\) or on its étale objects is imposed.

We retain the two-universe convention of that lesson. Affine open charts of objects are again objects. An étale algebra is locally standard étale: around a chosen point its presentation has the form

\[
B=(A[z]/(f))_g,\qquad
f\text{ monic},\qquad f'(z)\in B^\times.
\tag{1.1}
\]

This local structure theorem is cited from [Stacks, Tag 03PE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-standard-etale) and used without proof; we do not assume that a given object has one preferred global presentation. In particular, over a field \(k\), an étale scheme is a disjoint union of spectra of finite separable extensions of \(k\) ([Stacks, Tag 02GL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-over-field)). Over an algebraically closed field, these are copies of \(\operatorname{Spec}k\).

The standard sheaves on this site are

\[
\mathcal O(U)=\Gamma(U,\mathcal O_U),\quad
\mathbf G_m(U)=\Gamma(U,\mathcal O_U)^\times,\quad
\mu_n(U)=\{a\in\mathbf G_m(U):a^n=1\},\quad n\geq1,
\tag{1.2}
\]

together with constant sheaves and \(h_V(U)=\operatorname{Mor}_X(U,V)\) for \(V\in X_{\mathrm{ét}}\). They are restrictions of the representable sheaves proved in lesson 5. The additive group is the underlying additive sheaf of \(\mathcal O\). A constant sheaf with a small fibre \(A\) is the sheaf of locally constant maps to \(A\), represented by \(\coprod_A X\).

## 2. Neighbourhoods, stalks and exactness

A **geometric point** is a map \(\bar x:\operatorname{Spec}\Omega\to X\) with \(\Omega\) algebraically closed. Write \(x\) for its image and \(k(x)\subset\Omega\) for the induced residue-field inclusion. An **étale neighbourhood** of \(\bar x\) is an object \(U\to X\) together with a lift \(\bar u:\operatorname{Spec}\Omega\to U\). A map of neighbourhoods preserves that lift. Denote this category by \(\mathcal N_{\bar x}\).

**Lemma 2.1.** The category \(\mathcal N_{\bar x}\) is nonempty and cofiltered. Affine neighbourhoods, and affine neighbourhoods factoring through any chosen affine open about \(x\), suffice for its stalk colimits. A covering of a neighbourhood admits a member with a compatible geometric lift.

**Proof.** The identity object \((X,\bar x)\) proves nonemptiness. The fibre product of two neighbourhoods, with its paired lift, maps to both. To equalize two arrows \(a,b:(U,\bar u)\to(V,\bar v)\), pull back the diagonal \(V\to V\times_X V\) along \((a,b)\). The diagonal of an étale morphism is an open immersion. Its pullback is an open subscheme \(W\subset U\) containing the chosen lift, on which \(a=b\). It is again an étale neighbourhood. This proves the three cofilteredness conditions.

Every neighbourhood has an affine open containing its selected point. Intersect first with the inverse image of a chosen affine open of \(X\), if desired. To compare two such choices, take the preceding fibre product or equalizer and then an affine open about its lift. Thus the affine subcategory still supplies common refinements and equalizers; it gives exactly the same classes and equality relations in the colimit.

Finally, base change a neighbourhood cover to \(\operatorname{Spec}\Omega\). Some member is nonempty. Its fibre is étale over the algebraically closed field and therefore has an \(\Omega\)-point. This point is the required compatible lift. \(\square\)

For a presheaf \(F\), define

\[
F_{\bar x}=\operatorname*{colim}_{\mathcal N_{\bar x}^{\mathrm{op}}}F(U).
\tag{2.1}
\]

A germ is represented by \((U,\bar u,s)\). Two germs are equal exactly when their sections become equal on a common pointed refinement. This is a filtered colimit: neighbourhood arrows shrink domains, while restrictions carry sections in the opposite direction.

**Proposition 2.2.** Stalks preserve finite limits and all colimits of presheaves of sets, preserve exact sequences of presheaves of abelian groups, and satisfy

\[
F_{\bar x}\ \xrightarrow{\sim}\ (F^\#)_{\bar x}.
\tag{2.2}
\]

Consequently on sheaves they preserve finite limits and all colimits and are exact on abelian sheaves. Each is the inverse image of a point of the étale topos.

**Proof.** Filtered colimits of sets commute with finite limits; colimits commute with colimits. Filtered colimits of abelian groups are exact. These give the presheaf assertions. For surjectivity in (2.2), a section of the associated sheaf is locally represented by a section of the original presheaf, by the sheafification theorem of lesson 1. Choose a covering on which it has such representatives, and then the member with the lift supplied by Lemma 2.1. The corresponding original germ gives the desired preimage.

For injectivity, suppose two original germs become equal after sheafification. On a common neighbourhood their associated sections agree. Local equality in sheafification supplies a covering on which the original sections agree. Choose a pointed member of that cover. The original germs were already equal there. This argument works for sets, and hence also for abelian presheaves.

Sheaf limits are presheaf limits, while sheaf colimits are sheafifications of presheaf colimits. Equation (2.2) therefore proves the sheaf assertions. For abelian exactness, a sheaf cokernel is the sheafification of the presheaf cokernel, so presheaf exactness and (2.2) give the claimed exact stalk sequence.

More explicitly, the site functor

\[
v_{\bar x}(U)=\operatorname{Mor}_X(\operatorname{Spec}\Omega,U)
\tag{2.3}
\]

preserves the final object and fibre products, and sends covers to jointly surjective families by Lemma 2.1. The point construction of lesson 2 applies. Its category of elements is precisely \(\mathcal N_{\bar x}\), so its inverse image is (2.1). This also identifies the right adjoint and establishes that we have a topos point, not merely an exact functor on abelian sheaves. \(\square\)

**Theorem 2.3 (geometric stalk criterion).** A map of sheaves of sets on \(X_{\mathrm{ét}}\) is a monomorphism or an epimorphism if and only if it is respectively injective or surjective on every geometric stalk. A sequence of abelian sheaves is exact if and only if all its geometric stalk sequences are exact.

**Proof.** Proposition 2.2 proves necessity. For the converse monomorphism assertion, take \(s,t\in F(U)\) with equal images in \(G(U)\). For each point \(u\in U\), choose an algebraically closed residue extension and its geometric point \(\bar u\); compose with \(U\to X\) to obtain \(\bar x\). Injectivity on that stalk makes the two germs equal. A pointed refinement \(V_u\to U\) therefore makes \(s,t\) equal. These refinements cover \(U\), because their images contain their respective \(u\). The sheaf's separatedness gives \(s=t\).

For epimorphisms, take \(t\in G(U)\). At each \(\bar u\), stalk surjectivity represents its germ by a germ of \(F\). Refine the representing neighbourhood and \((U,\bar u)\) together; refine once more to realize equality of the two \(G\)-germs. We obtain \(V_u\to U\) and \(s_u\in F(V_u)\) whose image is \(t|_{V_u}\). These form a covering of \(U\), proving the local epimorphism condition from lesson 1.

For an abelian sequence, its compositions vanish if they vanish on every stalk: apply the monomorphism argument to the equality of the composition and the zero map. Then form each cohomology sheaf, the kernel modulo the sheaf image. Exact stalks make all its stalks zero by Proposition 2.2. A sheaf with zero stalks has each section locally zero by the same neighbourhood argument, and hence is zero. The sequence is exact. The converse was already proved by stalk exactness. \(\square\)

One algebraic closure of \(k(x)\) for each \(x\in X\) gives a set of points sufficient for this criterion. To justify independence of the choice, every lift to an étale object factors through the separable algebraic closure of \(k(x)\) inside the chosen algebraically closed field. An isomorphism between two such separable closures therefore gives an isomorphism of their neighbourhood categories and stalk functors. The isomorphism need not be unique. Extension of a fixed algebraically closed field gives the same lifts canonically, since an étale fibre is a disjoint union of its finite separable branches.

**Representable stalks.** There is a natural bijection

\[
(h_V)_{\bar x}=\operatorname{Mor}_X(\operatorname{Spec}\Omega,V).
\tag{2.4}
\]

Send \((U,\bar u,a:U\to V)\) to \(a\bar u\). Every lift is the image of the identity section on its own pointed neighbourhood \((V,\bar v)\). If two representatives have the same lift, use their pointed fibre product, followed by the open equalizer of the two maps to \(V\). They agree on that refinement. This proves both surjectivity and injectivity in (2.4), and the formula is compatible with maps of \(V\).

## 3. Henselian local rings provide sections

A local ring \((R,\mathfrak m,k)\) is **henselian** if every simple root in \(k\) of a monic polynomial over \(R\) lifts to a root in \(R\). It is **strictly henselian** if it is henselian and \(k\) is separably closed. A lift of a specified simple root is unique: for roots \(b,c\) with the same residue \(a\),

\[
0=f(b)-f(c)=(b-c)q(b,c),\qquad
q(b,c)\bmod\mathfrak m=f'(a)\ne0.
\tag{3.1}
\]

The second factor is a unit in the local ring, so \(b=c\).

We use without proof the existence theorem for the **henselization** \(R^h\) and the **strict henselization** \(R^{\mathrm{sh}}\) with a specified \(k\subset k^{\mathrm{sep}}\): they are flat local extensions, henselian and strictly henselian respectively, with maximal ideals generated by \(\mathfrak m\) and residue fields \(k\) and \(k^{\mathrm{sep}}\). The precise colimit characterization used here is

\[
R^{\mathrm{sh}}=\operatorname*{colim}_{(B,\mathfrak q,\iota)}B
=\operatorname*{colim}_{(B,\mathfrak q,\iota)}B_{\mathfrak q},
\tag{3.2}
\]

where \(B\) is an étale \(R\)-algebra, \(\mathfrak q\) lies over \(\mathfrak m\), and \(\iota:k(\mathfrak q)\hookrightarrow k^{\mathrm{sep}}\) is a \(k\)-embedding. Arrows are ring maps preserving the selected prime and residue embedding. For \(R^h\), require the residue field to be \(k\) itself. These are [Stacks, Tags 03QL, 04GP and 04GW]. The theorem includes the ordinary construction on local rings; the passages from scheme neighbourhoods and from an arbitrary topos point will be proved below. With a fixed residue-field embedding, the construction is canonical. Forgetting that choice leaves non-unique isomorphisms between strict henselizations.

**Lemma 3.1 (strictly local lifting).** Let \(R\) be strictly henselian, and let \(U\to\operatorname{Spec}R\) be étale. Every point of its closed fibre lifts uniquely to a section \(\operatorname{Spec}R\to U\). Equivalently,

\[
\operatorname{Mor}_R(\operatorname{Spec}R,U)
\xrightarrow{\sim}U(k).
\tag{3.3}
\]

**Proof.** The closed fibre is étale over the separably closed field \(k\), so its points have residue field \(k\). Choose a standard étale affine neighbourhood (1.1) of such a point. Its polynomial has a simple residue root \(a\). Henselianity lifts it to a root \(b\in R\). The localizing element \(g(b)\) has nonzero residue, so is a unit, giving the section into that chart. Any necessary affine open of the base containing the closed point is the whole local spectrum, so no shrinking of the base remains.

For uniqueness of two sections with the same closed-fibre point, their equalizer is the pullback of the open diagonal of \(U\). It is an open subset of \(\operatorname{Spec}R\) containing its closed point, hence is the entire spectrum. The sections agree. This argument also covers nonseparated \(U\). Every section has a closed-fibre value, proving both inverse directions of (3.3). \(\square\)

In particular every étale cover of a strictly henselian local spectrum has a member admitting a section: some member meets the closed fibre, and Lemma 3.1 applies. Sections of arbitrary sheaves and cohomological vanishing will follow from this fact in Solution 5.

## 4. The ring seen by a geometric stalk

Let \(k^{\mathrm{sep}}\subset\Omega\) be the separable algebraic closure of \(k(x)\) in the field of \(\bar x\). Write \(\mathcal O_{X,x}\) for the Zariski local ring and \(\mathcal O_{X,\bar x}\) for the stalk of (1.2) on the étale site.

**Theorem 4.1.** There is a canonical identification, with respect to this residue-field choice,

\[
\mathcal O_{X,\bar x}\simeq
(\mathcal O_{X,x})^{\mathrm{sh}}.
\tag{4.1}
\]

**Proof.** Choose an affine open \(\operatorname{Spec}A\) about \(x\), with corresponding prime \(\mathfrak p\). By Lemma 2.1, it is enough to use affine étale neighbourhoods \(\operatorname{Spec}B\to\operatorname{Spec}A\). Their lifts are precisely triples \((B,\mathfrak q,\iota)\), where \(\mathfrak q\) lies over \(\mathfrak p\) and \(\iota:k(\mathfrak q)\hookrightarrow\Omega\) is a \(k(x)\)-embedding. The residue extension is finite separable, so \(\iota\) lands in \(k^{\mathrm{sep}}\). Thus

\[
\mathcal O_{X,\bar x}=\operatorname*{colim}_{(B,\mathfrak q,\iota)}B.
\tag{4.2}
\]

Replacing \(B\) by \(B_{\mathfrak q}\) does not change this colimit. Every element inverted in \(B_{\mathfrak q}\) is already inverted on a principal open about its selected point, which is another neighbourhood. Finite fractions and equalities are realized on such refinements. Likewise every element of \(A\setminus\mathfrak p\) is inverted on a base principal open about \(x\). We may therefore compare (4.2) with the local-ring construction (3.2) over \(R=A_{\mathfrak p}\).

One direction sends a neighbourhood to its base change over \(R\). For the converse, an étale \(R\)-algebra with a selected residue embedding may first be restricted to a standard étale chart about its selected prime. Its monic polynomial and localizing element use only finitely many coefficients of \(A_{\mathfrak p}\). Choose \(s\notin\mathfrak p\) clearing their denominators. Over \(A_s\), form the same monic quotient, localizing also at the derivative. This is an étale \(A\)-algebra, and after base change it is the chosen chart: the derivative was already a unit there. Its selected residue-field embedding supplies a pointed scheme neighbourhood. Every element of the local construction is thus represented in (4.2).

Maps and equality relations spread in the same way. An algebra in these charts is finitely presented, so a map into a filtered localization is specified by finitely many generator images and finitely many relations. Clear the finitely many additional denominators to realize the map over another \(A_s\). Equalities of finitely many images are realized after one further such restriction. Selected residue embeddings are preserved throughout. Consequently neither construction creates additional identifications absent from the other. The two natural maps on colimits are inverse. By (3.2), the result is \((A_{\mathfrak p})^{\mathrm{sh}}\), proving (4.1). Changing the affine open passes to a common neighbourhood and gives the same identification. \(\square\)

The finite-equation description of units and roots gives

\[
(\mathbf G_m)_{\bar x}=(\mathcal O_{X,\bar x})^\times,
\qquad (\mu_n)_{\bar x}=\mu_n(\mathcal O_{X,\bar x}).
\tag{4.3}
\]

For the first formula, a unit and its inverse in a filtered ring colimit have representatives on a common stage, and their product equals \(1\) at a further stage. For the second, represent the element and its inverse there, then realize the finite equation \(a^n=1\) at a further stage. This proves both inverse directions of the formulas. If \(n\) is invertible, reduction identifies these roots with the \(n\)-th roots in \(k^{\mathrm{sep}}\): Lemma 3.1, or simple-root lifting and uniqueness, gives the bijection. A choice of primitive root identifies this group with \(\mathbf Z/n\mathbf Z\); that last identification is not canonical.

**Examples.** At a geometric point of \(\operatorname{Spec}k\), (4.1) gives \(k^{\mathrm{sep}}\). The stalk of an arbitrary sheaf carries a continuous action of \(G_k=\operatorname{Gal}(k^{\mathrm{sep}}/k)\): send a representative with residue embedding \(\iota\) to the representative with embedding \(g\iota\). Common-refinement relations are preserved, and each representative is fixed by the open subgroup fixing its finite residue extension. This is a preview of the field comparison in lesson 8, not its proof.

For \(\mathbf Z_{(p)}\), the strict henselization is the colimit of étale neighbourhood rings with primes over \((p)\) and embeddings of their finite residue fields into \(\overline{\mathbf F}_p\). Its residue field is \(\overline{\mathbf F}_p\), whereas the henselization has residue field \(\mathbf F_p\). The latter uses only the neighbourhoods whose chosen residue field is \(\mathbf F_p\). These are descriptions by neighbourhoods, not identifications with the completion \(\mathbf Z_p\).

For \(k[t]_{(t)}\), the strict version likewise selects embeddings of the finite separable residue extensions into \(k^{\mathrm{sep}}\). If \(k\) is algebraically closed of characteristic different from two, the ordinary and strict henselizations coincide. They contain the root of \(z^2=1+t\) with residue \(z=1\), represented by the étale chart with selected prime \((t,z-1)\). This root is not in \(k(t)\), because \(1+t\) has valuation one at \(t=-1\), while a square has even valuation. Thus even with algebraically closed residue field, the original local ring need not be strictly henselian.

## 5. Every topos point is geometric

It is not enough to know that geometric points detect isomorphisms. We must also show that an arbitrary topos point has one of their stalk functors. We give a construction using the ring of germs of that arbitrary point.

Let \(p\) be a point of \(\operatorname{Sh}(X_{\mathrm{ét}})\), and put
\(v(U)=p^{-1}h_U\).
By lesson 2, \(v\) preserves finite limits, sends covers to jointly surjective families, and determines the point and its stalks. Some affine open \(A_0\subset X\) has \(v(A_0)\ne\varnothing\), since affine opens cover \(X\). Being a subobject of the final object, its value is a singleton. Also
\(v(U\times_X A_0)=v(U)\times v(A_0)=v(U)\).
We may perform the construction over \(A_0=\operatorname{Spec}A\) and recover the original values by this formula.

Use all pairs \((U,a)\) with \(U\) affine étale over \(A\) and \(a\in v(U)\). They form a nonempty cofiltered category. Products follow from finite-limit preservation. Equalizers are open subschemes of the source, by the étale diagonal; a cover of an equalizer by affine opens and the cover property supply an affine refinement carrying its selected element. Set

\[
R_p=\operatorname*{colim}_{(U,a)^{\mathrm{op}}}\Gamma(U,\mathcal O_U).
\tag{5.1}
\]

**Lemma 5.1.** The ring \(R_p\) is nonzero, local and strictly henselian. If \(\mathfrak p\subset A\) is the inverse image of its maximal ideal, its residue field is a separable algebraic closure of \(k(\mathfrak p)\).

**Proof.** If \(0=1\) in the filtered colimit, that equation holds on a later affine stage. That stage is empty, contradicting its selected element, since the empty cover makes \(v(\varnothing)=\varnothing\).

Represent \(r\in R_p\) by \(b\in\Gamma(U,\mathcal O_U)\) at \((U,a)\). The cover \(U=D(b)\cup D(1-b)\) makes \(a\) lift to at least one of the two opens. Thus either \(r\) or \(1-r\) is a unit in \(R_p\). In a nonzero commutative ring this implies locality: nonunits are closed under multiplication by any element; if a sum of two nonunits were a unit, division by that unit would contradict the preceding property. The nonunits therefore form the unique maximal ideal \(\mathfrak m_p\).

We need a precise link between selected elements and ordinary points of a stage. A represented function \(b\) becomes a unit in \(R_p\) exactly when \(a\) belongs to the image of \(v(D(b))\). One implication was just proved. For the other, represent an inverse on a common stage and realize the inverse equation on a further stage. Its map to \(U\) then factors through \(D(b)\), and its selected element maps to \(a\). Define

\[
q_a=\ker\bigl(\Gamma(U,\mathcal O_U)\to R_p/\mathfrak m_p\bigr).
\tag{5.2}
\]

For every Zariski open \(W\subset U\), we have
\(a\in\operatorname{image}v(W)\) if and only if \(q_a\in W\).
This follows for principal opens from the unit criterion, and for arbitrary opens from their principal-open coverings. It also shows that \(q_a\) lies over \(\mathfrak p\).

To prove henselianity, take a monic \(f\in R_p[z]\) and a simple residue root, represented by \(c\in R_p\). Represent \(f,c\) together on a stage \((U,a)\), with polynomial still monic. There \(f(c)\in q_a\) and \(f'(c)\notin q_a\). Write
\(h(z)=(f(z)-f(c))/(z-c)\), a polynomial with \(h(c)=f'(c)\). The scheme

\[
V=\operatorname{Spec}\bigl(\Gamma(U,\mathcal O_U)[z]/(f)\bigr)_{f'(z)h(z)}
\tag{5.3}
\]

is étale over \(U\); its image is open and contains \(q_a\), since the chosen simple residue root gives a point there. By (5.2), \(a\) belongs to \(v\) of that image. The cover of its image by \(V\) therefore supplies an element of \(v(V)\) above \(a\). The coordinate \(z\) supplies a root in \(R_p\). Modulo \(\mathfrak m_p\), the equation is \((z-\bar c)\bar h(z)=0\), with \(\bar h(z)\) invertible, so its residue is the specified root. This proves henselianity; uniqueness was (3.1).

Next take a monic separable polynomial of positive degree over \(R_p/\mathfrak m_p\). Lift its coefficients to a common stage. Its discriminant has nonzero residue, so the unit criterion permits restriction to the open where that discriminant is invertible. Adjoining a root is now a finite free étale cover: the discriminant Bezout identity makes the derivative invertible in the quotient. A selected lift to this cover supplies a root in the residue field of \(R_p\). Thus every separable irreducible polynomial has a root, and this residue field is separably closed.

Finally each residue element is represented on some stage \(U\). The induced map from its ring into \(R_p/\mathfrak m_p\) factors through an embedding of \(k(q_a)\), which is finite separable over \(k(\mathfrak p)\) because \(U\) is étale. All residue elements are therefore separably algebraic over \(k(\mathfrak p)\). The separably closed residue field is a separable algebraic closure of that field. \(\square\)

**Theorem 5.2.** Every point of the small étale topos is isomorphic to the point associated with a geometric point of \(X\).

**Proof.** There is a natural bijection

\[
v(U)\simeq\operatorname{Mor}_A(\operatorname{Spec}R_p,U)
\tag{5.4}
\]

for every étale \(U\) over \(A\). To construct it, lift \(a\in v(U)\) to an affine open \(V\subset U\), using the cover property. The stage \((V,b)\) of (5.1) gives \(\operatorname{Spec}R_p\to V\to U\). Two choices have a common selected refinement over \(U\), by finite-limit preservation and an affine cover of their fibre product, so the resulting maps agree. This also proves compatibility with arrows of \(U\).

For surjectivity, a map \(\operatorname{Spec}R_p\to U\) lands in an affine open \(V\subset U\) about the image of the closed point: its inverse image is an open of a local spectrum containing the closed point, and hence the entire spectrum. The étale affine algebra of \(V\) is finitely presented over \(A\). Its map into the filtered colimit (5.1) factors through a stage \((W,b)\), by taking finitely many generator images and then realizing finitely many relations. Apply \(v(W\to V)\) to \(b\). Its image in \(v(U)\) produces the original map.

For injectivity, represent two elements by affine lifts and take a common selected affine stage mapping to both over \(A\). Its two maps to \(U\) have equalizer an open subscheme \(E\). If the induced maps from \(\operatorname{Spec}R_p\) agree, its closed point maps into \(E\). Thus the stage's point \(q_a\) lies in \(E\); (5.2) puts its selected element in the image of \(v(E)\). After an affine pointed refinement within \(E\), the two maps agree, so their images in \(v(U)\) were equal. This proves (5.4) with both inverse directions.

By Lemmas 5.1 and 3.1, restriction to the closed point identifies the right side of (5.4) with \(U(k_p)\), where \(k_p=R_p/\mathfrak m_p\). Lemma 5.1 identifies \(k_p\), as a field over \(k(x)\), with a separable closure of \(k(x)\), where \(x\) corresponds to \(\mathfrak p\). Transport it to a separable closure in the smaller universe, and choose an algebraic closure \(\Omega\) there. This gives an embedding \(k_p\hookrightarrow\Omega\). Since \(k_p\) is separably closed, every étale fibre over it is a disjoint union of copies of \(\operatorname{Spec}k_p\), so \(U(k_p)\to U(\Omega)\) is a natural bijection. The residue map \(R_p\to k_p\hookrightarrow\Omega\) gives a geometric point \(\operatorname{Spec}\Omega\to\operatorname{Spec}R_p\to A_0\to X\). Equation (5.4) is a natural isomorphism with its site-point functor (2.3); the correspondence of site points and topos points from lesson 2 gives the required isomorphism of points, hence of their entire stalk functors. \(\square\)

The underlying point \(x\) is determined by the values on Zariski opens, through the principal-open criterion in (5.2). Choices of separable closure and its identifications account for the non-unique point isomorphisms. The theorem classifies objects of the category of points; it does not classify all morphisms between them, which may also reflect specialization.

Together with Theorem 4.1, this proves that every point-stalk of \(\mathcal O\) is a local ring, so \((X_{\mathrm{ét}},\mathcal O)\) is locally ringed. The local-ring property is also visible in the site: for every function \(f\) on an object \(U\), the cover \(D(f)\cup D(1-f)=U\) makes either \(f\) or \(1-f\) invertible. The equation \(0=1\) occurs only on the empty scheme. These are the local-ring conditions, and the enough-points criterion verifies their stalk interpretation.

## 6. Kummer theory: roots and tensor powers

**Theorem 6.1 (Kummer).** If \(n\geq1\) is invertible on \(X\), the following is an exact sequence of abelian sheaves on \(X_{\mathrm{ét}}\):

\[
0\longrightarrow\mu_n\longrightarrow\mathbf G_m
\xrightarrow{a\mapsto a^n}\mathbf G_m\longrightarrow0.
\tag{6.1}
\]

It gives the natural short exact sequence

\[
0\longrightarrow
\Gamma(X,\mathcal O_X)^\times/
\bigl(\Gamma(X,\mathcal O_X)^\times\bigr)^n
\longrightarrow H^1(X_{\mathrm{ét}},\mu_n)
\longrightarrow\operatorname{Pic}(X)[n]
\longrightarrow0.
\tag{6.2}
\]

Here \(\operatorname{Pic}(X)[n]\) means the kernel of the tensor-power map \([L]\mapsto[L^{\otimes n}]\).

**Proof.** The kernel in (6.1) is \(\mu_n\) by definition. To prove its last epimorphism, let \(a\) be a unit on an object \(U\) and form

\[
U'=\operatorname{Spec}_U\bigl(\mathcal O_U[z]/(z^n-a)\bigr).
\tag{6.3}
\]

Over an affine open with ring \(A\), the new algebra is free with basis \(1,z,\ldots,z^{n-1}\). Its positive rank gives faithful flatness and surjectivity. Its coordinate \(z\) is a unit, since \(z^n=a\), and its derivative \(nz^{n-1}\) is a unit. It is therefore étale by (1.1). These affine checks make (6.3) a surjective étale morphism; its source is also étale over \(X\), by composition. The unit \(a\) has the root \(z\) there. This proves étale local surjectivity for arbitrary \(U\).

The long exact cohomology sequence of (6.1), followed by Hilbert 90 from lesson 5, contains

\[
\Gamma(X,\mathcal O_X)^\times
\xrightarrow{(-)^n}\Gamma(X,\mathcal O_X)^\times
\xrightarrow{\partial}H^1(X_{\mathrm{ét}},\mu_n)
\longrightarrow\operatorname{Pic}(X)
\xrightarrow{n}\operatorname{Pic}(X).
\tag{6.4}
\]

The last map is tensor power: on torsor transitions it raises units to their \(n\)-th powers, which are the transitions of \(L^{\otimes n}\). Exactness of (6.4) gives precisely the two kernels and quotient in (6.2), proving every position of that short sequence. \(\square\)

For a field, this gives \(H^1(k_{\mathrm{ét}},\mu_n)=k^\times/(k^\times)^n\), since every line bundle on a field spectrum is trivial. On \(\operatorname{Spec}\mathbf R\), for instance, adjoining \(i\) makes \(-1\) a square étale locally, while it is not a square Zariski locally: the spectrum has only one nonempty open. When the characteristic divides \(n\), étale local surjectivity need not hold, as the \(\mu_p\) example of lesson 5 showed. Root covers remain fppf, but the étale assertion here requires invertibility.

**Pairs describing \(H^1\).** There is also a concrete description of the middle group. Its elements are isomorphism classes of pairs

\[
(L,\alpha),\qquad L\text{ a line bundle},\quad
\alpha:L^{\otimes n}\xrightarrow{\sim}\mathcal O_X,
\tag{6.5}
\]

with tensor product as the group law. An isomorphism \(L\to L'\) must carry \(\alpha\) to \(\alpha'\).

To prove the description, let \(P_{L,\alpha}\) be the sheaf of frames \(e\) of \(L\) satisfying \(\alpha(e^{\otimes n})=1\). On a trivializing open, write \(\alpha(e_0^{\otimes n})=a\). The cover adjoining a root of \(a^{-1}\) supplies a normalized frame. Two normalized frames differ by a unique element of \(\mu_n\). The sheaf is consequently a \(\mu_n\)-torsor.

Conversely choose local sections of a \(\mu_n\)-torsor. Their comparison units \(g_{ij}\) have \(g_{ij}^n=1\) and satisfy the usual triple cocycle. Descent glues their frames into \(L\), as in lesson 5. Their tensor powers agree on overlaps, so the maps sending each \(e_i^{\otimes n}\) to \(1\) descend to an isomorphism \(\alpha\). The local torsor identifications agree on overlaps, giving the original torsor \(P_{L,\alpha}\). Starting with a pair recovers its frames and its original \(\alpha\). An isomorphism of torsors descends a frame-preserving module isomorphism, which respects the tensor-power trivializations; conversely an isomorphism of pairs induces an equivariant torsor isomorphism. These are inverse constructions on isomorphism classes.

Tensor product multiplies the comparison units and the normalized frames. It therefore agrees with the sum of torsor classes from lesson 3. Forgetting \(\alpha\) is the map to \(\operatorname{Pic}(X)[n]\) in (6.2). With the convention that \(\partial(a)\) is the torsor of roots \(b^n=a\), its pair is \((\mathcal O_X,a^{-1})\): multiplication by \(a^{-1}\) makes exactly these frames have normalized tensor power \(1\). This specifies the inverse-unit convention rather than leaving the connecting map ambiguous. In particular \(H^1(\mu_n)\) need not equal \(\operatorname{Pic}(X)[n]\); changing the tensor-power trivialization accounts for the unit quotient on the left.

## 7. Sections have closed support; sheaves may not

For an abelian sheaf \(F\), define

\[
\operatorname{Supp}F=\{x\in X:F_{\bar x}\ne0\}.
\tag{7.1}
\]

The set does not depend on the geometric point over \(x\), because its stalks are isomorphic as explained after Theorem 2.3. For a section \(s\in F(U)\), let \(W\subset U\) be the union of the Zariski opens on which it vanishes. Zariski sheaf gluing makes \(s|_W=0\), so \(W\) is the largest such open.

**Proposition 7.1.** The germ of \(s\) at a geometric point \(\bar u\) vanishes if and only if its underlying point \(u\) lies in \(W\). Thus

\[
\operatorname{Supp}(s)=U\setminus W
\tag{7.2}
\]

is closed in \(U\).

**Proof.** Membership in \(W\) clearly makes the germ zero. Conversely a zero germ is zero on a pointed étale refinement \(V\to U\). The image \(\operatorname{image}(V\to U)\) is open because étale maps are open. The map from \(V\) to that image is an étale cover. Separatedness of \(F\) descends the equality \(s|_V=0\) to the image, which therefore lies in \(W\). It contains \(u\), proving the assertion. \(\square\)

Closed support here belongs to a section on its own domain. The support of the whole sheaf is the union of the images in \(X\) of such supports, over all sections on all objects, and need not be closed. For an explicit example, take \(X=\mathbf A^1_k\), \(D=D(t)\subset X\), and

\[
F=\mathbf Z[h_D]^\#,
\tag{7.3}
\]

the associated free abelian sheaf on the representable open \(h_D\). Stalks commute with this free construction: free abelian groups commute with colimits, and (2.2) removes the associated sheaf without changing a stalk. Equation (2.4) makes \((h_D)_{\bar x}\) a singleton for \(x\in D\) and empty otherwise. Therefore

\[
F_{\bar x}=\begin{cases}\mathbf Z,&x\in D,\\0,&x\notin D.\end{cases}
\qquad\operatorname{Supp}F=D(t).
\tag{7.4}
\]

This is a dense proper open, so is not closed. The calculation uses the free sheaf already constructed in lesson 3; no theorem about extension by zero or closed-immersion pushforward is required.

## 8. Exercises

1. **Easy.** Prove all three cofilteredness conditions for étale neighbourhoods of a geometric point. Explain why affine neighbourhoods suffice without assuming the scheme is separated.
2. **Medium.** Compute \(H^1(\operatorname{Spec}\mathbf Z[1/2]_{\mathrm{ét}},\mu_2)\). Exhibit torsors representing a basis of the resulting group.
3. **Medium.** Prove that the stalk of \(h_U\) at \(\bar x\) is the set of lifts of \(\bar x\) to \(U\). Check both inverse directions and naturality in \(U\).
4. **Medium.** Give an abelian sheaf on \(\mathbf A^1_k{}_{\mathrm{ét}}\) whose support is not closed. Prove its stalk calculation, and explain why it does not contradict closedness of the support of each section.
5. **Hard.** Let \(R\) be strictly henselian local, with a geometric point \(\bar s\) over its closed point. For every abelian sheaf \(F\) on \(\operatorname{Spec}R_{\mathrm{ét}}\), prove naturally that \(\Gamma(\operatorname{Spec}R,F)=F_{\bar s}\), and deduce \(H^q(\operatorname{Spec}R_{\mathrm{ét}},F)=0\) for all \(q>0\).

## 9. Solutions

**Solution 1.** The pointed identity object makes the category nonempty. The paired geometric lift to \(U\times_X V\) makes a common predecessor for two neighbourhoods. For two parallel maps, pull back the open diagonal of their étale target; the resulting open equalizer contains the chosen geometric lift and is étale over \(X\). It is a predecessor equalizing them. After any of these constructions, select an affine open about that lift. First intersect with the inverse image of a fixed affine base neighbourhood if necessary. These operations preserve the selected lift, give both common refinements and equalizers inside the affine subcategory, and show its stalk colimit has the same representatives and equalities. No closed diagonal and no affine-intersection property of the base was used.

**Solution 2.** Put \(A=\mathbf Z[1/2]\). A localization of a principal ideal domain is a principal ideal domain, so \(\operatorname{Pic}(\operatorname{Spec}A)=0\): a finite projective rank-one module is a fractional invertible ideal, and that ideal is principal. The units are \(A^\times=\{\pm2^m:m\in\mathbf Z\}\). Indeed a fraction with denominator a power of two is a unit exactly when its numerator has no odd prime factor. Modulo squares, the sign and the parity of \(m\) are independent. Theorem 6.1 gives

\[
H^1(\operatorname{Spec}A_{\mathrm{ét}},\mu_2)
=A^\times/(A^\times)^2
\simeq(\mathbf Z/2\mathbf Z)^2.
\tag{9.1}
\]

The root torsors \(z^2=-1\) and \(w^2=2\) represent a basis. Both covers are finite free of rank two and étale, since \(2\), \(z\), and \(w\) are units in their respective algebras. Their classes are nontrivial: a rational square cannot have negative sign, and the two-adic valuation of a rational square is even. These also show independence, with the fourth square class represented by \(-2\).

**Solution 3.** Map the germ represented by \((V,\bar v,a:V\to U)\) to the lift \(a\bar v\). This respects common-refinement relations. A lift \(\bar u\) is represented by the identity on \((U,\bar u)\), proving surjectivity. For two representatives yielding the same lift, form their pointed fibre product, then the open equalizer of the two resulting maps to \(U\). An affine neighbourhood within that equalizer is a common pointed refinement on which their sections agree. This proves injectivity. Composition with an arrow \(U\to U'\) commutes with both the germ construction and the displayed lift, proving naturality.

**Solution 4.** Use (7.3). The presheaf of free abelian groups on \(h_D\) has stalk the free group on the stalk of \(h_D\), because free groups commute with this colimit. Sheafification leaves the stalk unchanged by Proposition 2.2. Solution 3 gives a unique lift to the open \(D(t)\) for points inside it and no lift for points outside it. The stalks are exactly (7.4), so the support is \(D(t)\), which contains the generic point but not the origin and is not closed. A section on an object has a largest open vanishing locus, so its support is closed in that object by Proposition 7.1. Taking the union of images over all those sections does not preserve closedness; in particular a section on \(D(t)\) has a domain different from \(X\).

**Solution 5.** For every neighbourhood \((U,\bar u)\) of the closed geometric point, its selected point in the closed fibre is defined over the separably closed residue field \(k\) of \(R\). The lift \(\bar u\) to an algebraically closed extension selects precisely that same \(k\)-point. Lemma 3.1 supplies a unique section \(s_U:\operatorname{Spec}R\to U\) with this value. It is a pointed neighbourhood map: its composition with \(\bar s\) equals the selected \(\bar u\).

For a map of pointed neighbourhoods \(a:U\to V\), the two sections \(a s_U\) and \(s_V\) have the same closed value, and hence are equal by Lemma 3.1. Restriction along the \(s_U\) therefore gives a well-defined natural map

\[
F_{\bar s}\longrightarrow F(\operatorname{Spec}R).
\tag{9.2}
\]

The natural map in the opposite direction restricts a global section to any neighbourhood. On the identity neighbourhood, (9.2) is the identity, so one composite is the identity on global sections. A germ represented on \(U\) becomes its pullback along the pointed map \(s_U\) on the identity neighbourhood; this is exactly the stalk's refinement relation. Thus the other composite is the identity as well.

Proposition 2.2 makes the closed-point stalk an exact functor on abelian sheaves. Its naturally isomorphic global-section functor is consequently exact. Applying it to an injective resolution gives an exact complex in all positive degrees, proving the asserted higher-cohomology vanishing for every abelian sheaf. This does not say that the closed-point stalk alone detects every sheaf; it is the global-section functor which is exact.

## What this lesson does not prove

The local standard étale theorem and the classification of étale schemes over a field are cited from [Stacks, Tag 03PE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-standard-etale) and [Tag 02GL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-over-field). Existence and the colimit characterization of henselization and strict henselization are cited from [Stacks, Tags 03QL, 04GP and 04GW]; their exact statements are recorded in section 3. Their uses here are supplied by the simple-root uniqueness, strictly local section proof and scheme-neighbourhood comparison above.

We use lessons 1–3 for sheafification, the local epimorphism criterion, the equivalence between site points and topos points, enough-point detection, free abelian sheaves, cohomology and its torsor interpretation. Hilbert 90 is proved in lesson 5. Every stalk, exactness, point-classification, Kummer, support and exercise argument specific to the present lesson is given here. Classification of all morphisms between points, equivalence with the Galois-module topos over a field, and functorial direct and inverse images belong to later lessons.

## References

- **[Stacks, étale objects and Kummer theory]** The Stacks Project Authors, *The Stacks Project*, [Tags 03P9–03PE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-etale-morphism) for the local standard presentation and morphism facts; [Tags 03PF–03PG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-etale-covering) for the small site; and [Tags 03PK–03PL and 040Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-kummer) for the root cover and degree-one description. The normalized-frame construction above specifies both inverses, the tensor product and the unit convention for the connecting map.
- **[Stacks, stalks and points]** [Tags 03PN–03PQ, 040R, 03PT–03PU and 04HU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-stalks) for neighbourhoods, stalk exactness and point classification. Section 5 gives the complete ring-of-germs proof of the last assertion; enough geometric points alone would not prove it. [Tags 04FQ–04FS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-support) give the support formalism, with the explicit free-sheaf example computed above.
- **[Stacks, henselian rings and étale local rings]** [Tags 03QD, 03QF, 03QK–03QL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-henselian-ring) for the algebraic definitions and existence theorem; [Tags 04HW–04HZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-stalks-structure-sheaf) for the structure-sheaf stalk; and the precise algebraic constructions in [Tag 04GP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-strict-henselization) and [Tag 04GW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-strict-henselization-different). The scheme-to-local-ring comparison is proved in Theorem 4.1.

The linked AI Integrated Stacks Project reader contains AI-proposed corrections and AI-written additions and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
