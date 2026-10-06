# Cohomology on sites

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Public domain (CC0).*

A section of a quotient sheaf can lift on every member of a covering and still fail to lift globally. Cohomology records this failure. In degree one, the local lifts themselves form a torsor. In higher degrees, an injective resolution organizes the successive failures into groups and connecting maps.

We develop the construction on an arbitrary small site. The proof of enough injectives uses generators and local exactness; it does not require points. A covering then supplies a second resolution, the Čech complex. Comparing the two resolutions explains when a calculation with overlaps computes cohomology, and when additional local cohomology intervenes. Finally, Leray compares cohomology before and after a morphism of topoi.

We use [Topoi, morphisms and points](topoi-morphisms-and-points.md), including its slice adjunctions, exact inverse image on abelian sheaves, and profinite classifying topos. Ordinary injective resolutions, their comparison maps and the spectral sequences of a first quadrant double complex are homological algebra prerequisites. The relevant exact statements and locators appear at the end. All rings in the discussion of line bundles are commutative. Sites and their covering families are small in a fixed universe; sheaves take values in a larger universe if necessary. We use the axiom of choice.

Cohomology of sheaves on topological spaces and Čech cohomology are treated in [Stacks, Tags 01DX and 01ED](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-section-introduction); here the proofs work on sites. Torsors under group schemes that are represented by schemes are a special case of the torsors here, which are sheaves with a locally simply transitive action, whether or not a geometric object represents them; see also [Stacks, Tag 03AG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-section-h1-torsors).

## 1. Why injective resolutions exist

Write \(a\) for associated sheaf. For an object \(U\) and a sheaf of rings \(\mathcal O\), define the free module sheaf

\[
P_U^{\mathcal O}=a\left(V\longmapsto
\bigoplus_{b:V\to U}\mathcal O(V)\right).
\tag{1.1}
\]

Restriction sends the summand labelled \(b\) to the summand labelled by its composite with the restricting arrow, and restricts the coefficient. A module map from (1.1) to \(M\) is determined by the image of the basis element labelled \(\mathrm{id}_U\). Conversely a section \(m\in M(U)\) gives the map \(r[b]\mapsto r b^*m\). These constructions are natural and inverse. Hence

\[
\operatorname{Hom}_{\mathcal O}(P_U^{\mathcal O},M)=M(U).
\tag{1.2}
\]

For abelian sheaves use \(P_U^{\mathbf Z}=a(\mathbf Z[h_U])\). It has the analogous universal property. The coproduct \(P=\bigoplus_U P_U\) is a **generator**: two different maps differ on a section over some \(U\), and (1.2) gives a map from \(P_U\), then from \(P\), detecting that difference. There is also an epimorphism \(\bigoplus_{(U,m)}P_U\to M\) taking each identity generator to \(m\). It is surjective on sections before sheafification.

**Proposition 1.1.** Abelian sheaves, and sheaves of left \(\mathcal O\)-modules, form Grothendieck abelian categories: they have all small colimits, exact filtered colimits, and a generator. They have enough injectives.

**Proof.** Kernels are sectionwise kernels. Cokernels and colimits are associated sheaves of the corresponding presheaf constructions. Addition and the \(\mathcal O\)-action extend uniquely through sheafification: define them on local representatives and glue. Their equations hold locally and therefore hold in the sheaf. The local image criterion identifies coimage with image, so the module category is abelian, just as the abelian sheaf category is. In particular, an epimorphism is locally surjective on underlying sections.

Associated sheaf is additive and exact. Indeed it preserves kernels by left exactness and cokernels by its left adjoint property. Filtered colimits of presheaf modules are exact, because this is true of modules at each object. To apply this observation to a diagram of short exact sequences of sheaves, first regard its rows as presheaf complexes. Their presheaf cokernels may differ from their sheaf cokernels, but sheafification annihilates precisely the resulting local failure of surjectivity. Filtered colimit commutes with presheaf kernels and cokernels. Applying the exact functor \(a\) therefore gives an exact colimit row of sheaves. The same argument, using direct sums, shows that coproducts preserve monomorphisms. Formula (1.2) gives the generator.

We prove the injective assertion in either category at once. Subobjects of any sheaf form a set: a subobject selects a subgroup or submodule of every section set, with compatibility conditions. Thus they are contained in a product of power sets over the small site.

First, an object \(J\) is injective if every map \(K\to J\), for every subobject \(K\subset P\), extends to \(P\). Necessity is the definition of injectivity. For sufficiency, let \(A\subset B\) and \(A\to J\) be given. Partially order extensions of this map to intermediate subobjects of \(B\), by restriction. A chain has an upper bound: exact filtered colimits give its union as a subobject of \(B\), and the compatible maps give a map on the union. Zorn's lemma provides a maximal extension \(C\to J\).

If \(C\ne B\), the generator detects the nonzero quotient map \(B\to B/C\): there is \(h:P\to B\) whose image is not contained in \(C\). Let \(K=h^{-1}C\). The induced map \(K\to C\to J\) extends to \(v:P\to J\) by the assumed test. On \(C\oplus P\), the map which is the sum of the existing map on \(C\) and \(v\) kills the kernel of \((c,p)\mapsto c+h(p)\), because that kernel is the image of \(k\mapsto(-h(k),k)\). It therefore descends to \(C+\operatorname{im}h\subset B\). This properly extends \(C\), a contradiction. Thus the test characterizes injectivity.

Now start with any \(M\). Take the set of all pairs \((K,v)\), where \(K\subset P\) and \(v:K\to M\). Push out the monomorphism \(\bigoplus_{(K,v)}K\to\bigoplus_{(K,v)}P\) along the sum of the maps \(v\). Call the result \(T(M)\). Pushout of a monomorphism in an abelian category is a monomorphism, so \(M\subset T(M)\). Every one of the specified maps extends to \(P\to T(M)\).

Iterate this construction: \(M_0=M\), \(M_{\alpha+1}=T(M_\alpha)\), and at a limit take the union. All transition maps are monomorphisms. Choose an infinite cardinal \(\kappa\) bounding the set of subobjects of \(P\), and a limit ordinal \(\beta\) of cofinality greater than \(\kappa\). Such an ordinal exists: take the first ordinal of cardinality greater than \(\kappa\). If it had a cofinal subset of size at most \(\kappa\), it would be a union of at most \(\kappa\) ordinals each of size at most \(\kappa\), contradicting its cardinality. It is a limit ordinal because adjoining one point does not increase an infinite cardinal.

For a map \(v:K\to M_\beta\), with \(K\subset P\), form \(K_\alpha=v^{-1}M_\alpha\). Exact filtered colimits commute with this pullback, since it is a kernel involving a finite direct sum. Consequently \(\bigcup_{\alpha<\beta}K_\alpha=K\). There are at most \(\kappa\) distinct \(K_\alpha\), because they are also subobjects of \(P\). Pick a stage for each distinct subobject. The cofinality bound gives a common stage \(\alpha<\beta\) above all of them. Then \(K_\alpha=K\): the map \(v\) factors through \(M_\alpha\). At the next stage it extends to \(P\). This extension takes values in \(M_\beta\), since \(\beta\) is a limit. The test just proved makes \(M_\beta\) injective. Thus every object embeds in an injective. \(\square\)

This argument includes abelian presheaves by taking the trivial topology. No bound on the cardinalities of sections of the varying \(M_\alpha\) is needed; the fixed set of subobjects of the generator supplies the bound. See [Stacks, Tags 01DP, 01DU and 079H] for the foundational injective results, and [Stacks, Tag 05N3] for the ordinal fact.

## 2. Sections, slices and local vanishing

The **global sections** of an abelian sheaf \(F\) are compatible sections over all objects and arrows of the site. Let \(\mathbf Z^\#\) be the associated sheaf of the constant presheaf \(\mathbf Z\). Sending \(1\) to those compatible sections gives

\[
\Gamma(\mathcal C,F)=\operatorname{Hom}(\mathbf Z^\#,F).
\tag{2.1}
\]

If \(\mathcal C\) has a final object \(X\), this group is \(F(X)\). Without a final object, formula (2.1) is still available. Both \(F\mapsto F(U)\) and \(\Gamma(\mathcal C,-)\) are left exact, because kernels and finite limits of sheaves are sectionwise. Choose an injective resolution \(F\to I^\bullet\), in nonnegative degrees, and set

\[
H^n(U,F)=H^n(I^\bullet(U)),\qquad
H^n(\mathcal C,F)=H^n(\Gamma(\mathcal C,I^\bullet)).
\tag{2.2}
\]

These are the right derived functors of sections. In particular
\(H^n(\mathcal C,F)=\operatorname{Ext}^n(\mathbf Z^\#,F)\), including when the site has no final object. The usual resolution comparison theorem makes (2.2) independent of the resolution and supplies functorial restriction maps, long exact sequences, and connecting homomorphisms. For modules, first use an injective resolution in \(\operatorname{Mod}(\mathcal O)\); section 5 will prove agreement with (2.2).

**Proposition 2.1.** For every \(U\), restriction to the slice site gives

\[
H^n(U,F)=H^n(\mathcal C/U,F|_U).
\tag{2.3}
\]

Every class in \(H^n(U,F)\), for \(n>0\), becomes zero on a covering of \(U\).

**Proof.** The abelian left adjoint of slice restriction is associated sheaf of
\(V\mapsto\bigoplus_{b:V\to U}E(V,b)\). It is exact. On a short exact sequence of slice sheaves it preserves injectivity on presheaf sections. A target section is a finite sum in these summands; each of its finitely many terms lifts locally by the epimorphism criterion. A common refinement lifts all of them. Thus the associated sheaf map is an epimorphism as well. Kernels and images give exactness in the middle.

An exact left adjoint makes its right adjoint preserve injectives: extending a map into the restricted injective is, by adjunction, extending a map into the original injective along the image of a monomorphism. Slice restriction itself is exact, by the preceding lesson. It therefore takes \(I^\bullet\) to an injective resolution. The final object of \(\mathcal C/U\) is \((U,\mathrm{id})\), where its sections are \(I^\bullet(U)\). This proves (2.3).

Represent a positive degree class by \(z\in I^n(U)\) with \(dz=0\). Exactness of the resolution as a sheaf complex says that \(\ker d\subset I^n\) is the sheaf image of \(I^{n-1}\to I^n\). Local surjectivity gives a covering \(\{U_i\to U\}\) and \(b_i\in I^{n-1}(U_i)\) such that \(db_i=z|_{U_i}\). The restricted class is therefore zero. \(\square\)

The presheaf

\[
\mathcal H^q(F):V\longmapsto H^q(V,F)
\tag{2.4}
\]

need not be a sheaf. For \(q>0\) its associated sheaf is zero, by local vanishing. Losing those local classes through sheafification does not mean that every global class is zero.

## 3. A covering gives a second resolution

Let \(\mathcal U=\{U_i\to U\}_{i\in I}\) be a covering. Put
\(U_{i_0\ldots i_p}=U_{i_0}\times_U\cdots\times_U U_{i_p}\). All these products exist: the site supplies base change by a covering member, and repeated base change constructs the longer products. Include repeated indices. For an abelian presheaf \(F\), define

\[
\check C^p(\mathcal U,F)=\prod_{(i_0,\ldots,i_p)\in I^{p+1}}
F(U_{i_0\ldots i_p}),\qquad
(dc)_{i_0\ldots i_{p+1}}=
\sum_{a=0}^{p+1}(-1)^a c_{i_0\ldots\widehat{i_a}\ldots i_{p+1}}|_{U_{i_0\ldots i_{p+1}}}.
\tag{3.1}
\]

Deleting two entries in either order gives terms with opposite signs, so \(d^2=0\). Its cohomology is \(\check H^p(\mathcal U,F)\). In degree zero the kernel is the group of matching families. Hence for a sheaf

\[
\check H^0(\mathcal U,F)=F(U).
\tag{3.2}
\]

A short exact sequence of **presheaves** gives a short exact sequence of these complexes: evaluation is exact, and products of surjections of abelian groups are surjective by choice. The long exact sequence of complex cohomology makes \(\check H^\bullet\) a \(\delta\)-functor on presheaves. For a short exact sequence of sheaves, surjectivity need only be local, so its evaluated Čech complexes need not form a short exact sequence.

**Lemma 3.1.** Injective abelian sheaves are Čech-acyclic. Injective \(\mathcal O\)-modules have the same property for their underlying abelian sheaves.

**Proof.** Form the augmented chain complex

\[
\cdots\longrightarrow\bigoplus_{i,j}P_{U_{ij}}^{\mathbf Z}
\longrightarrow\bigoplus_iP_{U_i}^{\mathbf Z}
\longrightarrow P_U^{\mathbf Z}\longrightarrow0,
\tag{3.3}
\]

whose differential is the alternating sum of projections. It is exact as a complex of sheaves. To check this without points, work with a local representative, a finite sum of actual arrows into the indicated products. After a covering and a common refinement, every arrow \(V\to U\) appearing in that sum lifts to a chosen \(U_i\), because \(\mathcal U\) is a covering. For each such arrow fix a lift. The tuples over that arrow are the nerve of its nonempty set of lifts. Inserting the chosen lift as the first entry is a contracting homotopy: its boundary plus its composite with the boundary is the identity, including the augmentation. This makes every local cycle a local boundary. Elements introduced by sheafification have local representatives, and equalities in the associated sheaf hold after a further covering; those two facts also apply to a cycle initially expressed only in sheaf sections. Thus (3.3) is exact.

Applying \(\operatorname{Hom}(-,J)\) for an injective abelian sheaf gives an exact augmented cochain complex. By (1.2), its unaugmented complex is (3.1), and its augmentation is \(J(U)\). This proves the assertion. Replace each \(P^{\mathbf Z}\) by \(P^{\mathcal O}\) for the module assertion. The same local contraction is \(\mathcal O\)-linear, so its chain complex is exact, without any flatness assumption on \(\mathcal O\) over \(\mathbf Z\). Applying module Hom into an injective module again gives precisely (3.1) on underlying groups. \(\square\)

For completeness, the presheaf \(\delta\)-functor above is universal. Before sheafification, let \(S(V)\) be the image of \(\coprod_i h_{U_i}(V)\to h_U(V)\). The free chain complex on the tuples in (3.3) is a resolution of \(\mathbf Z[S]\): separately over each arrow in \(S(V)\), insertion of one lift contracts the nonempty set of lifts. This is sectionwise exact, although the augmented map to \(\mathbf Z[h_U]\) may fail to be surjective. Each chain term is a coproduct of free representables, hence projective in abelian presheaves by (1.2). Injective presheaves consequently have zero positive Čech cohomology. Enough injectives and the resolution comparison theorem identify this effaceable \(\delta\)-functor with \(R^p\check H^0(\mathcal U,-)\). An injective sheaf is also injective as a presheaf, because sheafification is an exact left adjoint of inclusion. See [Stacks, Tags 03AR and 03AU].

**Theorem 3.2 (Čech-to-cohomology).** There is a natural spectral sequence

\[
E_2^{p,q}=\check H^p(\mathcal U,\mathcal H^q(F))
\ \Longrightarrow\ H^{p+q}(U,F),\qquad p,q\geq0,
\tag{3.4}
\]

with \(d_r:E_r^{p,q}\to E_r^{p+r,q-r+1}\).

**Proof.** Choose \(F\to I^\bullet\) and use the double complex
\(D^{p,q}=\check C^p(\mathcal U,I^q)\). The Čech differential \(d_h\) and resolution differential \(d_v\) commute. On its total complex use \(d=d_h+(-1)^p d_v\) in bidegree \((p,q)\); the mixed terms then cancel. In total degree \(n\) there are only \(n+1\) summands.

First take horizontal cohomology. Lemma 3.1 and (3.2) leave only \(I^q(U)\) in horizontal degree zero. The augmentation from \(I^\bullet(U)\) to the total complex therefore induces an isomorphism on cohomology. This identifies the total cohomology with the right side of (3.4).

Next filter the same total complex by the Čech degree \(p\). Taking vertical cohomology gives
\(E_1^{p,q}=\prod_{i_0,\ldots,i_p}H^q(U_{i_0\ldots i_p},F)\), since products are exact. The induced next differential is exactly the alternating restriction map in (3.1). Its cohomology is the stated \(E_2\). The first quadrant double complex theorem gives the indicated differentials and convergence, with a finite filtration on each total cohomology group. Resolution comparison maps induce maps of filtered double complexes; a homotopy between comparison maps induces the corresponding homotopy with the total signs. Thus the pages from \(E_2\) and their abutment maps are natural and independent of the resolution. This constructs the spectral sequence. \(\square\)

In particular, if every \(U_{i_0\ldots i_p}\) is \(F\)-acyclic, meaning \(H^q(U_{i_0\ldots i_p},F)=0\) for \(q>0\), only the row \(q=0\) remains. The resulting canonical map
\(\check H^n(\mathcal U,F)\to H^n(U,F)\) is an isomorphism for every \(n\). This is the acyclic-cover form of Leray's theorem. It is a condition on all finite intersections, including the individual members.

## 4. A practical vanishing criterion

**Theorem 4.1.** Let \(\mathcal B\) be a set of objects and \(\mathrm{Cov}\) a set of coverings with targets in \(\mathcal B\). Assume that every covering of each \(U\in\mathcal B\) is refined by a covering in \(\mathrm{Cov}\), and that every member and every finite iterated fibre product of each such covering belongs to \(\mathcal B\). If

\[
\check H^p(\mathcal V,F)=0\quad
(p>0,\ \mathcal V\in\mathrm{Cov}),
\tag{4.1}
\]

then \(H^p(U,F)=0\) for all \(p>0\) and all \(U\in\mathcal B\).

**Proof.** Induct simultaneously over all objects of \(\mathcal B\) on the positive degree \(n\). Suppose all degrees strictly between zero and \(n\) already vanish; for \(n=1\) this supposes nothing. Take \(\xi\in H^n(U,F)\). Proposition 2.1 supplies a covering killing its restrictions; refine it by \(\mathcal V\in\mathrm{Cov}\).

In (3.4) for this covering, the rows \(0<q<n\) vanish, because all intersections lie in \(\mathcal B\). Also \(E_2^{n,0}=0\) by (4.1). Thus every associated graded piece of total degree \(n\), except possibly \(E_\infty^{0,n}\), is zero. The filtration consequently embeds \(H^n(U,F)\) in \(E_2^{0,n}\): there are no incoming differentials to column zero, so \(E_\infty^{0,n}\) is a subgroup of \(E_2^{0,n}\). This edge map is restriction to the matching family of classes on the covering members, as follows directly from the augmentation used in the proof of (3.4). Our class restricts to zero on every member. Its edge image is zero, and injectivity gives \(\xi=0\). This proves the induction. \(\square\)

The requirement concerns all finite intersections. Pairwise intersections alone do not supply the entries in higher Čech degrees. This is the full hypothesis in [Stacks, Tag 03F9]. Section 7 will use the criterion on intervals, rather than merely recording it as an abstract tool.

## 5. Modules have the same cohomology

**Theorem 5.1.** Cohomology of an \(\mathcal O\)-module computed using injectives in \(\operatorname{Mod}(\mathcal O)\) agrees naturally with its cohomology as an abelian sheaf, both over every \(U\) and globally.

**Proof.** If \(J\) is an injective module, Lemma 3.1 gives (4.1) for every covering. Use \(\mathcal B=\operatorname{Ob}\mathcal C\) and all coverings in Theorem 4.1. Its underlying abelian sheaf is acyclic for sections over every object.

For global acyclicity when the site has no final object, the same argument can be performed on objects of its topos \(\mathcal E\), using the injectives already constructed in \(\operatorname{Ab}(\mathcal E)\). For a topos object \(A\), let \(\mathbf Z[A]\) and \(\mathcal O[A]\) denote the free abelian and module sheaves on \(A\), formed by sheafifying the sectionwise free constructions. Their universal properties identify Hom out of them with maps from \(A\) to the underlying sheaf. Define \(H^n(A,F)=\operatorname{Ext}^n(\mathbf Z[A],F)\). At \(A=h_U^\#\) this is (2.2), and at \(A=1\) it is global cohomology.

Local vanishing has an intrinsic version here. A cycle is a map \(A\to\ker(I^n\to I^{n+1})\). Pulling back the epimorphism \(I^{n-1}\to\ker(I^n\to I^{n+1})\) along this map supplies an epimorphism \(E\to A\) on which the cycle is a boundary. For any epimorphism \(E\to A\), its augmented Čech nerve has a locally contracting free abelian chain complex: after pulling back to \(E\), insert its diagonal section. Thus the proof of (3.4) gives the same spectral sequence with terms \(H^q(E\times_A\cdots\times_A E,F)\). The module chain complex is locally contracted by the same operation, so injectivity of \(J\) makes its higher Čech groups zero for every such epimorphism.

Induct on \(n>0\), simultaneously for every topos object \(A\). Kill a class in \(H^n(A,J)\) by the epimorphism just constructed. All rows \(0<q<n\) in its Čech spectral sequence vanish by induction, and its \(E_2^{n,0}\) vanishes by the module contraction. The edge injection from the proof of Theorem 4.1 makes the class zero. This proves acyclicity for every \(A\), in particular for \(1\). The induction uses a chosen cover for a chosen class at each step; it requires no small site containing every topos object.

An injective module resolution is therefore an acyclic resolution for every abelian sections functor. The forgetful functor is exact, so it is still a resolution after forgetting the module action. The acyclic-resolution theorem identifies its section complex with the abelian derived functor. This gives the claimed natural comparisons. \(\square\)

An injective module need not be injective as an abelian sheaf. On the one-point site, an injective \(\mathbf F_p\)-module can be \(\mathbf F_p\) itself. It is not injective as an abelian group: the map \(p\mathbf Z\to\mathbf F_p\) taking \(p\) to \(1\) cannot extend to \(\mathbf Z\). The proof above requires acyclicity, which is exactly what holds.

## 6. Degree one is a gluing problem

A **right \(G\)-torsor** for a sheaf of groups \(G\) is a sheaf of sets \(T\) with a right action such that \(T\to1\) is an epimorphism and

\[
T\times G\longrightarrow T\times T,\qquad(t,g)\longmapsto(t,tg)
\tag{6.1}
\]

is an isomorphism. Thus sections exist locally, and any two sections over the same object differ by a unique group section. A chosen section identifies a torsor with \(G\). A torsor is **trivial** if it has a global section. The sheaf of equivariant maps between two torsors is either locally empty or consists of isomorphisms: after choosing local sections such a map is translation between two copies of \(G\), hence is invertible.

For a cover \(\mathcal U\) of \(U\), a non-abelian Čech cocycle consists of
\(g_{ij}\in G(U_{ij})\) satisfying

\[
g_{ii}|_{\Delta U_i}=1,\qquad g_{ij}g_{jk}=g_{ik}
\quad\text{on }U_{ijk}.
\tag{6.2}
\]

The diagonal equation is understood on the diagonal, and the triple equation also implies the usual inverse relation after restriction and exchange of factors. Two cocycles represent the same class if
\(g'_{ij}=b_i^{-1}g_{ij}b_j\) for sections \(b_i\in G(U_i)\). Denote the set of classes by \(\check H^1(\mathcal U,G)\); it is pointed by the identity cocycle. For abelian \(G\), written additively, this is the degree-one group of (3.1). Indeed its cocycle equation is \(g_{jk}-g_{ik}+g_{ij}=0\), and its change of sections is addition of \(b_j-b_i\).

**Proposition 6.1.** For a fixed cover \(\mathcal U\), Čech cocycle classes are in bijection with torsors over \(\mathcal C/U\) which are trivial on every \(U_i\). Passing to refinements gives all torsors.

**Proof.** Choose sections \(t_i\) of a torsor. Define \(g_{ij}\) by \(t_j=t_i g_{ij}\). Uniqueness of the difference gives (6.2). Replacing \(t_i\) by \(t_i b_i\) gives precisely the stated equivalence, and an equivariant isomorphism preserves these differences.

Conversely, glue copies of \(G|_{U_i}\) using left multiplication by \(g_{ij}\). Explicitly, on an object \(V\to U\) take the set of families
\(x_i\in G(V\times_U U_i)\) with \(x_i=g_{ij}x_j\) on the double overlaps. Restrictions are restriction of families. This is a sheaf: matching sections glue separately in each \(G\), and the displayed equations persist after gluing by separation. Over \(U_i\) it is isomorphic to \(G\): a section \(x\) there gives the family \(g_{ki}x\) on its pulled back members, and the coordinate at the diagonal recovers \(x\). The cocycle equation checks these maps are inverse. Right multiplication on all coordinates defines the torsor action. Local identification with \(G\) proves both the epimorphism to \(1\) and (6.1).

The standard local section in the \(i\)-th copy has transition difference \(g_{ij}\), so extracting its cocycle recovers the input. Starting from \(T\), the map from the glued families to \(T\) glues the local sections \(t_i x_i\); the matching equation makes them agree. It is locally an isomorphism and hence an isomorphism. Finally, changing a cocycle by the \(b_i\) identifies the glued torsors by the corresponding change of coordinates. These checks prove both directions, including injectivity. Every torsor is locally trivial by its epimorphism to \(1\); over \(U\) this gives a covering of \(U\). Any two trivializing coverings have a common refinement. Thus refinements give all torsors and exactly their isomorphisms. \(\square\)

When the site has no final object, use covers of the terminal sheaf: an epimorphism \(E\to1\), with \(E\) a coproduct of associated representables, is a trivializing cover. Such a cover exists for a torsor by taking all local sections and the representing maps. Its overlaps are formed in the topos. The same descent proof applies, using the intrinsic nerve described in section 5. Common refinements exist by pulling back epimorphisms and then covering by associated representables. This defines the global non-abelian pointed set \(H^1(\mathcal C,G)\). It has no asserted group law when \(G\) is non-abelian.

Exact sequences with non-abelian coefficients must be interpreted as sequences of pointed sets at degree one, with exactness meaning that the inverse image of the distinguished point is the preceding image. The present construction supplies no subsequent non-abelian cohomology groups or longer group-valued exact sequence. Degree two in that setting requires additional structures such as gerbes.

**Theorem 6.2.** For an abelian sheaf \(G\), its derived group \(H^1(\mathcal C,G)\) classifies \(G\)-torsors. Likewise

\[
H^1(U,G)=\mathop{\mathrm{colim}}_{\mathcal U\text{ covering }U}
\check H^1(\mathcal U,G).
\tag{6.3}
\]

For a fixed cover, the map to \(H^1(U,G)\) is injective, and its image consists of the torsors trivialized by that cover.

**Proof.** Embed \(G\subset I\) with \(I\) injective and let \(Q=I/G\). The long exact sequence and \(H^1(\mathcal C,I)=0\) identify the derived group with

\[
\Gamma(\mathcal C,Q)/\operatorname{im}\Gamma(\mathcal C,I).
\tag{6.4}
\]

A global section \(q\) of \(Q\) has a sheaf of lifts \(T_q\subset I\). It is a \(G\)-torsor: local surjectivity supplies lifts, and their differences lie uniquely in \(G\). If \(q\) changes by a global section of \(I\), translation gives an isomorphism of the lift torsors.

We prove that every torsor arises and that (6.4) loses no information. For a \(G\)-torsor \(T\), sheafify the abelian presheaf generated by \(G\) and symbols \([t]\), for local sections of \(T\), subject to
\([t+g]=[t]+g\). Call it \(A(T)\). There is a sequence

\[
0\longrightarrow G\longrightarrow A(T)
\xrightarrow{\pi}\mathbf Z^\#\longrightarrow0,
\qquad \pi([t])=1,\quad \pi(g)=0.
\tag{6.5}
\]

Locally choose \(t_0\). Then \(g+n[t_0]\) identifies \(A(T)\) with \(G\oplus\mathbf Z^\#\), since every \([t]\) is uniquely \([t_0]+g\). This proves exactness of (6.5) and identifies its fibre over \(1\) with \(T\). All assertions are sheaf assertions; the presheaf may have no torsor symbol over an object where \(T\) has no section.

Injectivity of \(I\) extends \(G\to I\) to a map \(v:A(T)\to I\). Its composite to \(Q\) vanishes on \(G\), so factors through a map \(\mathbf Z^\#\to Q\), equivalently a global section \(q\). The map \(A(T)\to I\times_Q\mathbf Z^\#\) given by \((v,\pi)\) is an isomorphism: on kernels it is the identity on \(G\), on quotients the identity on \(\mathbf Z^\#\), and local lifting in the two extensions proves surjectivity. On the fibres over \(1\) it gives \(T\simeq T_q\). A different extension \(v\) differs by a map \(\mathbf Z^\#\to I\), so changes \(q\) by exactly an element allowed in (6.4).

Conversely an isomorphism \(T_q\to T_{q'}\) induces an isomorphism of (6.5), fixing its kernel and quotient. Compare its maps to \(I\); their difference factors through \(\mathbf Z^\#\to I\), because it is zero on \(G\). It follows that \(q-q'\) is the image of a global section of \(I\). Thus (6.4) is exactly the set of torsor isomorphism classes, and the two constructions are inverse. They are natural in \(G\). The group operation corresponds to the contracted sum of torsors: locally, differences add; equivalently the two lift sections in \(I\) add to a lift of \(q+q'\).

Apply this global result to \(\mathcal C/U\) and use (2.3). Proposition 6.1 gives (6.3) and the fixed-cover assertion. To check that this is the map from (3.4), choose local lifts \(t_i\in I(U_i)\) of \(q\). Their differences \(t_j-t_i\) are a Čech cocycle in \(G\). The connecting map defining (6.4) and the double-complex edge map both send these local lifts to this same cocycle class. This verifies the compatibility of the torsor classification with derived cohomology. \(\square\)

Here refinements do give a well-defined colimit. A choice of member of the old cover through which each refining member factors defines restriction on cochains. For two choices \(\lambda,\mu\), the prism homotopy is

\[
(Kc)_{j_0\ldots j_{n-1}}=
\sum_{a=0}^{n-1}(-1)^a
c_{\lambda j_0,\ldots,\lambda j_a,\mu j_a,\ldots,\mu j_{n-1}}|_{V_{j_0\ldots j_{n-1}}}.
\tag{6.6}
\]

The maps from the refining product into each old product exist by its universal property. Expanding the two alternating differentials cancels interior terms in pairs and leaves \(dK+Kd=\mu^*-\lambda^*\). Thus induced abelian cohomology maps are independent of choices. For non-abelian degree one the torsor construction proves the same independence: both choices simply restrict the same torsor. Common refinements make the directed colimit on cohomology or cocycle classes unambiguous. Equation (6.3) does not assert such an identification in degree two or above; a refinement can kill a degree-one class on each member while its higher overlap obstructions still remain. Hypercoverings will organize those obstructions in the next lesson.

**Proposition 6.3.** Isomorphism classes of locally free \(\mathcal O\)-modules of rank one form a group under tensor product, and

\[
\operatorname{Pic}_{\mathrm{lf},1}(\mathcal O)
\simeq H^1(\mathcal C,\mathcal O^\times).
\tag{6.7}
\]

**Proof.** For a locally free rank-one module \(L\), the sheaf of frames
\(\operatorname{Isom}_{\mathcal O}(\mathcal O,L)\) is an \(\mathcal O^\times\)-torsor, with the right action given by precomposition with multiplication by a unit. Maps and inverse maps glue, so it is a sheaf; local freeness supplies local sections, and two frames differ by one unique unit.

Conversely, choose local sections of an \(\mathcal O^\times\)-torsor and their cocycle \(g_{ij}\). Glue copies of \(\mathcal O\) by the equations \(x_i=g_{ij}x_j\). This uses the explicit sheaf construction in Proposition 6.1, now with addition and scalar multiplication on coordinates. These operations respect the equations because the transition units act linearly. The resulting module is locally free rank one. The coordinate vector \(1\) in each local copy is a frame with the prescribed transition units. Hence its frame torsor is the original torsor. In the other direction, the local frames identify this glued module with \(L\), and those identifications agree on overlaps. Changes of local sections give the same isomorphisms as before. The constructions are inverse on isomorphism classes.

The transition units of \(L\otimes L'\) are \(g_{ij}g'_{ij}\); this is addition in \(H^1(\mathcal O^\times)\). The dual module has transitions \(g_{ij}^{-1}\) and gives the inverse, while \(\mathcal O\) gives the identity. This proves (6.7) as an isomorphism of groups. \(\square\)

For a locally ringed site, **invertible module** in the tensor sense agrees with locally free rank one. The local-ring property needed here says that if finitely many sections generate the unit ideal, there is a covering on which one of them is a unit; the zero ring has only the empty locus. On a locally ringed space this follows at each stalk from its being a nonzero local ring, and invertibility of a section near a point follows by extending its stalk inverse.

Suppose \(\phi:L\otimes N\simeq\mathcal O\). Locally its inverse image of \(1\) has a finite tensor expression \(\sum_i l_i\otimes n_i\), so \(\sum_i\phi(l_i\otimes n_i)=1\). After a covering some term is a unit; rescale its \(n_i\) to obtain \(l,n\) with \(\phi(l\otimes n)=1\). The map \(\mathcal O\to N\) taking \(1\) to \(n\) is a split monomorphism, with retraction \(n'\mapsto\phi(l\otimes n')\). Tensoring this split monomorphism with \(L\) shows that \(x\mapsto\phi(x\otimes n)\) is a monomorphism \(L\to\mathcal O\). It is also a split epimorphism, with section \(1\mapsto l\). Hence it is an isomorphism and \(l\) is a local frame. Conversely a locally free rank-one module has an inverse given by its sheaf dual: the evaluation map is an isomorphism in each local frame and therefore globally. This proves the assertion, including the locally ringed site case of [Stacks, Tag 0B8Q]. Thus on a locally ringed space (6.7) is \(\operatorname{Pic}(X)=H^1(X,\mathcal O_X^\times)\). On an arbitrary ringed site we retain the explicitly stated locally free group in (6.7); tensor-invertibility alone must not silently replace its local hypothesis.

## 7. Calculations with covers and actions

**Intervals and the circle.** We first justify the acyclicity needed for the usual circle calculation. Let \(\mathcal B\) consist of open intervals in \(\mathbf R\) and the empty set. Every open cover of an interval has a refinement by a locally finite chain of open intervals \(J_n\), indexed by a finite consecutive range, a ray, or \(\mathbf Z\), such that only neighbouring distinct members intersect, and each neighbouring intersection is a nonempty interval. One construction is to exhaust the interval by compact subintervals and subdivide each band finely enough that each successive closed segment is in a member of the original cover. To justify this subdivision, around each point of a compact band choose a ball contained in one covering member. The concentric balls of half the radii still cover the band, and compactness gives finitely many. Any subset of the band of diameter smaller than half the least of those finitely many radii lies in an original ball: start with a point in a half-radius ball and use the triangle inequality. This provides the required subdivision size. Retaining band endpoints produces an increasing sequence of subdivision points with no accumulation inside the interval. Enlarge each closed segment slightly within its chosen covering member. Choose these enlargements smaller than one third of the adjacent segment lengths. They overlap at each common endpoint and have no intersection with non-neighbours. The enlargements cover the interval and give the stated refinement. A bounded compact part can of course require only finitely many segments. Unbounded ends and endpoints outside the interval are handled by the exhaustion.

For a constant sheaf \(\underline A\), its sections on each nonempty finite intersection in such a cover are \(A\), with identity restriction. Its Čech complex is the cochain complex of this chain nerve. We explain why discarding unordered and repeated tuples is legitimate in this calculation. On free chains send a tuple of distinct vertices to its increasing ordering with the permutation sign, and send a tuple with repetition to zero. This is a chain map onto the ordered simplicial chains, and inclusion of increasing tuples is a right inverse. Their composite is chain homotopic to the identity. To construct the homotopy inductively on a tuple, subtract the already constructed homotopy on its boundary from the difference of the two chain maps. This is a cycle supported on its vertex set. All vertices in that set have common intersection, so they span a simplex; insertion of its least vertex contracts its augmented tuple chains. Apply that contraction to fill the cycle. This gives the homotopy at the next degree, without leaving the same intersections. Dualizing proves the asserted cochain equivalence. For this cover the resulting ordered complex is just

\[
\prod_n A\longrightarrow\prod_n A,\qquad
(a_n)\longmapsto(a_{n+1}-a_n),
\tag{7.1}
\]

with one factor on the right for each edge and no higher terms. The difference map is surjective: choose a value at one vertex and recursively prescribe each next value along the line in either direction. Every value requires only a finite sum, even on an infinite line. Its kernel is the constant families. Thus every such cover has zero positive Čech cohomology. Its finite intersections lie in \(\mathcal B\), and the empty interval uses the empty cover. Theorem 4.1 gives

\[
H^q(J,\underline A)=0\qquad(q>0)
\tag{7.2}
\]

for every interval \(J\). This is a use of the vanishing criterion with a specified cofinal family of covers. Sheaves on a disjoint union are a product of the sheaf categories of its components; restriction and gluing give the inverse equivalences. Finite products preserve injective resolutions, so a finite disjoint union of these intervals is also acyclic.

Cover \(S^1\) by the complements \(U,V\) of two distinct points. They are intervals, and \(U\cap V\) consists of two intervals. Equation (7.2) and the acyclic-cover consequence of (3.4) apply. The ordered two-member Čech complex for \(\underline{\mathbf Z}\) is

\[
\mathbf Z\oplus\mathbf Z\longrightarrow\mathbf Z\oplus\mathbf Z,
\qquad(a,b)\longmapsto(b-a,b-a).
\tag{7.3}
\]

The tuple-chain reduction above works here as well: sorting a tuple preserves its intersection and its restrictions, including the two components of \(U\cap V\). Thus (7.3) computes all cohomology. Its kernel is \(\mathbf Z\) and its cokernel is \(\mathbf Z\), via \((r,s)\mapsto s-r\). Therefore
\(H^0(S^1,\underline{\mathbf Z})=\mathbf Z\),
\(H^1(S^1,\underline{\mathbf Z})=\mathbf Z\), and the higher groups vanish. The sign of the chosen generator changes when the two components of the intersection are exchanged.

**A profinite classifying topos.** Let \(G\) be profinite and \(M\) a discrete continuous left \(G\)-module. In \(BG\), global sections are invariant elements, so \(H^0(BG,M)=M^G\). An \(M\)-torsor is a nonempty set with a simply transitive translation action of \(M\), also carrying a continuous \(G\)-action satisfying \(g(t+m)=gt+gm\). Choose \(t\). Define \(c(g)=gt-t\). Continuity of the orbit map makes \(c:G\to M\) continuous, and the action equation gives

\[
c(gh)=c(g)+g c(h).
\tag{7.4}
\]

Replacing \(t\) by \(t+m\) changes \(c(g)\) by \(gm-m\). Conversely a continuous cocycle defines the affine action \(g\cdot x=gx+c(g)\) on \(M\). Equation (7.4) is its action law; the orbit of each \(x\) is a continuous map to the discrete set because both summands are continuous. It makes the translation torsor an object of \(BG\). Translating the chosen origin is exactly a coboundary change, and these constructions are inverse. Theorem 6.2 thus proves

\[
H^1(BG,M)=
\frac{\{\text{continuous }c:G\to M\text{ satisfying (7.4)}\}}
{\{g\mapsto gm-m:m\in M\}}.
\tag{7.5}
\]

The higher comparison with continuous group cohomology will be proved in the lesson on Galois cohomology.

**Line bundles on a ringed space.** A locally free rank-one module on \(X\), trivialized by an open cover \(U_i\), has frames \(e_i\) and transition units \(e_j=e_i g_{ij}\). The equations on threefold intersections are (6.2). Changing frames gives its coboundary relation. Thus (6.7) is the familiar description of line-bundle classes by transition functions, giving the usual \(\operatorname{Pic}(X)\) on a locally ringed space. For example, on a two-open cover any unit on the intersection gives a line bundle; it is trivial exactly when that unit is the ratio of units on the two opens. This last assertion follows from the fixed-cover injectivity in Theorem 6.2, not from an assumption that the cover computes higher cohomology.

## 8. Leray: cohomology through an intermediate topos

Let \(f:\mathcal E\to\mathcal F\) be a morphism of topoi. On abelian sheaves \(f^{-1}\) is exact, as proved in the preceding lesson. Consequently \(f_*\) preserves injectives: for a monomorphism \(A\subset B\) in \(\operatorname{Ab}(\mathcal F)\), the adjunction identifies extension into \(f_*I\) with extension along \(f^{-1}A\subset f^{-1}B\) into \(I\). Also
\(\Gamma(\mathcal F,f_*F)=\Gamma(\mathcal E,F)\), by adjunction and \(f^{-1}1=1\).

**Theorem 8.1 (Leray).** There is a natural spectral sequence

\[
E_2^{p,q}=H^p(\mathcal F,R^q f_*F)
\ \Longrightarrow\ H^{p+q}(\mathcal E,F).
\tag{8.1}
\]

For a second morphism \(g:\mathcal F\to\mathcal G\) there is the relative version

\[
E_2^{p,q}=R^p g_*(R^q f_*F)
\ \Longrightarrow\ R^{p+q}(g f)_*F
\tag{8.2}
\]

in abelian sheaves on \(\mathcal G\). Both have differentials of bidegree \((r,1-r)\) and finite filtrations in each total degree. The same statements hold for modules under arbitrary morphisms of ringed topoi.

**Proof for abelian sheaves.** Resolve \(F\to I^\bullet\) and put \(A^q=f_*I^q\). This is a bounded below complex of injective sheaves on \(\mathcal F\), with \(H^q(A^\bullet)=R^qf_*F\). Its section complex is \(\Gamma(\mathcal E,I^\bullet)\).

To obtain the required second page, resolve the complex \(A^\bullet\) together with its cycles, boundaries and cohomology. More explicitly, write \(Z^q=\ker d\), \(B^q=\operatorname{im}d\), \(H^q=Z^q/B^q\). Starting in degree zero, choose injective resolutions compatible with
\(0\to Z^q\to A^q\to B^{q+1}\to0\) and
\(0\to B^{q+1}\to Z^{q+1}\to H^{q+1}\to0\).
The injective horseshoe construction extends the already chosen left-hand resolution at each step. Its degreewise short exact sequences split, because their left-hand terms are injective. Composing the maps through the boundary resolutions gives a double complex \(J^{p,q}\), where \(p\) is resolution degree and \(q\) is the degree of \(A\). For fixed \(q\), \(J^{\bullet,q}\) resolves \(A^q\); for fixed \(p\), its \(q\)-cycles, boundaries and cohomology are injective, and its \(q\)-cohomology, as \(p\) varies, is an injective resolution of \(H^q\). This is a Cartan–Eilenberg resolution. Its existence is the ordinary homological algebra lemma [Stacks, Tag 015I]; here we have specified the complex to which it is applied and the maps it resolves.

Apply \(\Gamma(\mathcal F,-)\) and totalize, with differential \(d_p+(-1)^p d_q\) for commuting resolution and complex differentials. Taking \(p\)-cohomology first leaves only \(\Gamma(\mathcal F,A^q)\), since each \(A^q\) is injective. The augmentation therefore identifies total cohomology with \(H^*(\mathcal E,F)\).

Take \(q\)-cohomology first instead. The degreewise splitting in the construction is preserved by every additive functor, so this gives \(\Gamma(\mathcal F,J_H^{p,q})\), where \(J_H^{\bullet,q}\) resolves \(H^q(A)\). Taking \(p\)-cohomology then gives \(H^p(\mathcal F,R^qf_*F)\). Filter the total complex by \(p\); the usual double complex indexing in this direction gives the claimed \(E_2\) and differentials. In each total degree the filtration is finite. Comparison of resolutions and the horseshoe comparisons yield the natural pages from \(E_2\). This proves (8.1).

For (8.2), apply \(g_*\) to this same Cartan–Eilenberg resolution instead of applying global sections. Injectivity of the \(A^q\) makes the first computation leave \(g_*A^\bullet\); it computes \(R(gf)_*F\) by the original resolution \(I^\bullet\). The second computation uses the same splittings and leaves \(R^p g_*H^q(A)\). This proves the relative assertion. A bounded below complex in place of \(F\) is treated by a bounded below injective resolution and the same construction; translating the lower bound keeps each total-degree filtration finite. \(\square\)

There is an indexing distinction in this proof. Filtering by resolution degree makes the first operation cohomology in the complex degree \(q\), giving the page used in (8.1). Filtering by complex degree makes the first operation cohomology in the resolution degree \(p\), giving the collapsed computation of the abutment. These are the two filtrations of the same total complex.

**Module comparison and the ringed version.** A ringed morphism has module pullback
\(f^*M=\mathcal O_{\mathcal E}\otimes_{f^{-1}\mathcal O_{\mathcal F}} f^{-1}M\). This need not be exact. Thus \(f_*\) need not preserve injective modules unless \(f^*\) is exact, for example for a flat ringed morphism. We prove the acyclicity needed in its place.

If \(J\) is an injective \(\mathcal O_{\mathcal E}\)-module, section 5 shows that its underlying abelian sheaf is acyclic for sections over every object of \(\mathcal E\). For an abelian injective resolution \(J\to K^\bullet\), and any object \(V\) of a presenting site for \(\mathcal F\),

\[
(f_*K^\bullet)(V)=
\operatorname{Hom}_{\operatorname{Ab}(\mathcal E)}
\bigl(\mathbf Z[f^{-1}h_V^\#],K^\bullet\bigr).
\tag{8.3}
\]

This follows by adjunction; inverse image takes the free abelian sheaf on an object to the free abelian sheaf on its inverse image. To verify that last assertion, present the free sheaf by finite formal sums and their group equations, or use the free-group adjunction and the induced abelian adjunction of inverse and direct image. Thus the positive cohomology of (8.3) is zero. The complex \(f_*K^\bullet\) is exact in positive degrees on every site object, hence as a sheaf complex. This proves that \(J\) is \(f_*\)-acyclic in abelian sheaves.

An injective module resolution of any \(M\) is therefore an abelian \(f_*\)-acyclic resolution. Its underlying direct image is the same direct image as for abelian sheaves. The acyclic-resolution theorem proves the natural comparison

\[
R^q f_*^{\mathrm{modules}}M
\simeq R^q f_*^{\mathrm{abelian}}M
\tag{8.4}
\]

on underlying abelian sheaves, with its inherited module structure.

We also need the acyclicity of \(f_*J\) for subsequent sections or pushforward. For any epimorphism \(E\to A\) in \(\mathcal F\), its Čech cochains with \(f_*J\) are, by adjunction, maps from the free module sheaves on \(f^{-1}(E\times_A\cdots\times_AE)\) into \(J\). Exact inverse image takes this nerve to the covering nerve of the epimorphism \(f^{-1}E\to f^{-1}A\). The module contraction of Lemma 3.1 makes its Hom complex acyclic. The intrinsic vanishing induction of section 5 now gives \(H^n(A,f_*J)=0\) for all \(A\) and \(n>0\). Such a sheaf is often called **totally acyclic**. Equation (8.3), now for any following morphism \(g\), makes it abelian \(g_*\)-acyclic; comparison (8.4) makes it module \(g_*\)-acyclic too.

Consequently, in the ringed proof of (8.1)–(8.2) the complex \(A^\bullet=f_*I^\bullet\) has terms acyclic for the next functor, even when they are not injective. A Cartan–Eilenberg resolution in target modules still computes \(H^q(A)=R^q f_*F\). In the first computation, positive derived functors of each \(A^q\) vanish by this acyclicity; the other computation is unchanged. This proves both ringed spectral sequences. See [Stacks, Tags 072Z, 0730–0732 and 0734] for the distinctions between injectivity, flat pullback and total acyclicity.

## 9. The base change map

Fix a square of topoi with a specified commuting isomorphism:

\[
\begin{matrix}
\mathcal E'&\xrightarrow{g'}&\mathcal E\\
\scriptstyle f'\downarrow&&\downarrow\scriptstyle f\\
\mathcal F'&\xrightarrow{g}&\mathcal F.
\end{matrix}
\tag{9.1}
\]

It gives an identification \(f'^{-1}g^{-1}\simeq g'^{-1}f^{-1}\). Applying this to the counit produces
\(f'^{-1}g^{-1}f_*F\to g'^{-1}F\); adjunction gives the ordinary base change map \(g^{-1}f_*F\to f'_*g'^{-1}F\).

For a bounded below abelian complex \(K\), inverse images are exact and act directly on complexes. Their derived adjunctions give the canonical map

\[
g^{-1}Rf_*K\longrightarrow Rf'_*g'^{-1}K.
\tag{9.2}
\]

Explicitly, its adjoint is the composite

\[
f'^{-1}g^{-1}Rf_*K
\simeq g'^{-1}f^{-1}Rf_*K
\longrightarrow g'^{-1}K,
\tag{9.3}
\]

where the last arrow is the derived counit. This determines the map without choosing a resolution. One resolution model also checks its direction: resolve \(K\to I^\bullet\) and \(g'^{-1}K\to J^\bullet\). Since \(g'_*\) preserves abelian injectives, the unit map from \(K\) to \(g'_*J^\bullet\) extends to \(I^\bullet\to g'_*J^\bullet\), uniquely up to homotopy. Apply \(f_*\), identify \(f_*g'_*\simeq g_*f'_*\) using the square, and adjoint across \(g^{-1}\dashv g_*\). This gives \(g^{-1}f_*I^\bullet\to f'_*J^\bullet\), representing (9.2).

No isomorphism assertion is part of this definition. Proper and smooth base change later provide hypotheses under which related maps are isomorphisms. For modules under a ringed square, exact pullback requires flatness; otherwise the corresponding general formula uses derived pullback \(Lg^*\), rather than silently replacing it by underived \(g^*\). Our present map concerns abelian inverse images, which are always exact. See [Stacks, Tag 0735].

## 10. Exercises

1. **Global sections without a final object — easy.** Prove (2.1) directly from the sheafification adjunction, and show that \(H^0(\mathcal C,-)\) is left exact. Explain how the formula specializes when the site has a final object.

2. **An acyclic cover — medium.** If every finite fibre product of members of \(\mathcal U\) is \(F\)-acyclic, prove that its Čech complex computes \(H^*(U,F)\). Apply this to (7.3) and explain why connectedness of the two arcs alone would not justify the calculation.

3. **Non-abelian descent — medium.** Starting from right torsors and equations (6.2), construct both maps between the colimit of Čech cocycle classes and torsor isomorphism classes. Check independence of trivializations, both inverse identities, and compatibility with the derived group when \(G\) is abelian. Explain the modification if the site has no final object.

4. **Five terms — medium.** Deduce from (3.4) the exact sequence
\[
0\to\check H^1(\mathcal U,F)\to H^1(U,F)
\to\check H^0(\mathcal U,\mathcal H^1(F))
\xrightarrow{d_2}\check H^2(\mathcal U,F)\to H^2(U,F).
\tag{10.1}
\]
Describe \(d_2\) on local resolution cycles, with the total differential convention of Theorem 3.2.

5. **Forgetting a module action — hard.** Prove that an injective \(\mathcal O\)-module is \(f_*\)-acyclic as an abelian sheaf for any morphism of topoi \(f\). Deduce (8.4), and identify the weaker condition on \(f_*J\) needed for the ringed Leray sequence. Give an example showing why underlying abelian injectivity cannot replace acyclicity in this argument.

## 11. Solutions

**1.** A map of presheaves from the constant presheaf \(\mathbf Z\) to \(F\) is determined by sections \(s_U\in F(U)\), the images of \(1\). Naturality is exactly \(s_V=b^*s_U\) for every \(b:V\to U\). Conversely these sections define the maps \(n\mapsto ns_U\). Associated sheaf is left adjoint to inclusion, so the same maps are \(\operatorname{Hom}(\mathbf Z^\#,F)\). A map into a kernel is exactly a map into the original sheaf whose composite is zero; Hom from a fixed object is consequently left exact. Since \(H^0\) in (2.2) is the kernel of the first differential in a resolution, it agrees with this sections functor. If \(X\) is final, restriction of a single \(s_X\) gives the compatible family, and evaluating the family at \(X\) is the inverse. Thus \(\Gamma(\mathcal C,F)=F(X)\) in that case.

**2.** The \(E_1\)-page of (3.4) has entries \(\prod H^q(U_{i_0\ldots i_p},F)\). The assumed acyclicity makes every row with \(q>0\) zero. The remaining differential is the Čech differential, so \(E_2^{p,0}=\check H^p(\mathcal U,F)\). No later differential can enter or leave this row nontrivially. In total degree \(n\) the filtration therefore has exactly one possible nonzero graded piece, giving the canonical isomorphism with \(H^n(U,F)\). For the two arcs, (7.2) proves acyclicity of each arc and both components of their intersection; finite disjoint union preserves it. The reduced complex (7.3) has kernel the diagonal integers and cokernel the difference of the two overlap coordinates, giving \(\mathbf Z\) in degrees zero and one. Connectedness only identifies the degree-zero sections of a constant sheaf. It says nothing by itself about the vanishing of higher derived sections; that is the additional content of the interval argument.

**3.** Choose sections \(t_i\) and write \(t_j=t_i g_{ij}\). Applying this twice gives \(g_{ij}g_{jk}=g_{ik}\). Changing sections by \(t'_i=t_i b_i\) gives \(g'_{ij}=b_i^{-1}g_{ij}b_j\). These are exactly the cocycle and equivalence rules. From a cocycle, the families \(x_i=g_{ij}x_j\) define a sheaf by gluing in \(G\) on each pulled back covering member. Locally it is \(G\), with the right action on coordinates, so it is a torsor. Changing the cocycle changes coordinates and gives an isomorphism. The local section with coordinate \(1\) recovers the original transition differences. Starting from a torsor, the families map to it by gluing \(t_i x_i\); local trivializations show the map is an isomorphism. Thus both inverse identities hold.

Every torsor has a trivializing cover. Two covers have a common refinement, and restricting local sections restricts their cocycles. An isomorphism of torsors gives, after a common refinement, sections \(b_i\) realizing the equivalence rule; this proves injectivity in the colimit. In the abelian case the rules are the differential in (3.1), and the lift torsor of \(q\in Q\) has differences \(t_j-t_i\). These are exactly the resolution connecting class from (6.4), proving compatibility with derived \(H^1\). If there is no final site object, replace its cover by an epimorphism from a coproduct of associated representables to the terminal sheaf, form its nerve in the topos, and perform the same descent. Such covers and their common refinements exist by local sections and the generator presentation.

**4.** In total degree one the spectral filtration gives a subgroup \(E_\infty^{1,0}=E_2^{1,0}\) and quotient \(E_\infty^{0,1}=\ker(d_2:E_2^{0,1}\to E_2^{2,0})\). There are no other possible differentials involving these entries, by the first quadrant bounds. This proves exactness through \(E_2^{0,1}\). At \((2,0)\), the only possible incoming differential is the same \(d_2\), and there is no outgoing one; hence \(E_\infty^{2,0}=E_2^{2,0}/\operatorname{im}d_2\). This entry embeds as the last step \(F^2H^2\subset H^2\) of the filtration. Its kernel when viewed as a map from \(E_2^{2,0}\) is exactly \(\operatorname{im}d_2\). Substituting the page entries yields (10.1).

For the differential, represent a matching family of local classes by vertical cycles \(z_i\in I^1(U_i)\). Their horizontal difference is a vertical boundary: choose \(b_{ij}\in I^0(U_{ij})\) with \(d_v b=d_h z\). This choice is possible by the matching condition in the presheaf \(\mathcal H^1(F)\), which is equality of cohomology classes on each overlap. In bidegree \((1,0)\), the total differential contributes \(-d_v b\), so the degree \((1,1)\) term of \(d(z+b)\) is zero. The remaining degree \((2,0)\) term is \(d_h b\). It is a vertical cycle, since \(d_vd_hb=d_h^2z=0\), and consequently lies in \(F(U_{ijk})\). Its Čech class is \(d_2[z]\). Altering \(b\) by vertical cycles changes this by a Čech coboundary in \(F\); altering \(z\) by vertical boundaries changes \(b\) by the corresponding horizontal differential and has the same consequence. This checks independence and the sign with the stated convention.

**5.** Lemma 3.1 applies to an injective module \(J\) using the augmented free module chain complex, whose local contraction does not need \(\mathbf Z\)-flatness. The vanishing criterion, and its intrinsic extension in section 5, show \(H^q(A,J)=0\) for every topos object \(A\) and \(q>0\). Resolve its underlying abelian sheaf by \(K^\bullet\). By adjunction, evaluating \(f_*K^\bullet\) at \(V\) is the resolution sections over \(f^{-1}h_V^\#\), as in (8.3). Its positive cohomology vanishes. Sheaf cohomology of this complex is the sheafification of its sectionwise cohomology, since sheafification is exact; it therefore vanishes too. Thus \(J\) is abelian \(f_*\)-acyclic.

Now resolve an arbitrary module \(M\) by injective modules. Forgetting the action is exact, and every term is abelian \(f_*\)-acyclic. The acyclic-resolution comparison identifies the abelian derived direct image with the underlying complex used for the module derived direct image. This proves (8.4), including naturality of the inherited action. For the ringed Leray sequence, \(f_*J\) need only be acyclic for global sections, or for the following \(g_*\) in the relative case. Its covering nerve cochains identify with the Hom complex of a source covering nerve into \(J\), because inverse image preserves that nerve and its covering epimorphism. They vanish in positive degrees, giving total acyclicity and therefore both required conditions. Module injectivity of \(f_*J\) would follow from exact \(f^*\), but is unnecessary. On a point with ring \(\mathbf F_p\), \(\mathbf F_p\) is an injective module and is not an injective abelian group, by the nonextendable map \(p\mathbf Z\to\mathbf F_p\) from section 5. This is the promised distinction.

## What this lesson does not prove

The sheafification, local image, generator presentation of sheaves of sets, slice adjunctions and exact abelian inverse-image results are the prerequisites [Sites and sheaves](sites-and-sheaves.md) and [Topoi, morphisms and points](topoi-morphisms-and-points.md). The comparison theorem for ordinary bounded below injective resolutions, long exact derived-functor sequences, acyclic resolutions and universal effaceable \(\delta\)-functors are homological algebra prerequisites; precise statements are [Stacks, Tags 013P, 013S, 015B, 0156, 015E, 015M and 010T]. We use the first quadrant double complex spectral-sequence theorem: its two filtrations converge with a finite filtration in each total degree, and its differentials have bidegree \((r,1-r)\), as in [Stacks, Tags 0130 and 0132]. We use the injective horseshoe and Cartan–Eilenberg resolution existence theorem, with the cycle, boundary and cohomology compatibility described in section 8, at [Stacks, Tags 013T and 015I]. These general homological algebra tools are separate from the site-specific constructions proved here.

Compactness of closed bounded real intervals is an elementary real-analysis prerequisite. Section 7 proves the small-diameter cover property it needs, constructs the chain refinement, and proves its Čech contraction and its application to derived cohomology. We do not prove a general comparison with singular cohomology, the higher continuous group-cohomology comparison, or any base change isomorphism. Each has its own later lesson.

## References

- **[Stacks]** The Stacks Project Authors, *The Stacks Project*, “Cohomology on Sites”: [Tag 01FT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-section-cohomology-sheaves) for the definitions; [Tags 03F3 and 01FW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-section-locality) for slices and locality; [Tags 03AK–03AZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-section-cech) for Čech complexes and comparison; [Tag 0A6G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-cech-h1) for degree one; [Tag 03F9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-cech-vanish-collection) for the vanishing criterion; [Tag 03AJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-torsors-h1) for torsors; and [Tag 040E](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-lemma-h1-invertible) for the Picard interpretation on a locally ringed site. The Leray and base change passages are [Tags 072X–0735](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-cohomology.html#sites-cohomology-section-leray). The AI Integrated Stacks Project reader linked here contains AI-proposed corrections and AI-written additions and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
- **[Stacks, foundations]** “Injectives”: [Tags 01DP and 01DU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/injectives.html#injectives-theorem-sheaves-injectives), and [Tag 079H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/injectives.html#injectives-theorem-injective-embedding-grothendieck). “Sets”: [Tag 05N3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sets.html#sets-proposition-exist-ordinals-large-cofinality). “Modules on Sites”: [Tag 0B8Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-invertible-is-locally-free-rank-1). “Derived Categories”: [Tags 015I–015N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-lemma-cartan-eilenberg), for the ordinary double-resolution construction used in Leray.
- **[Stacks, étale prologue]** “Étale Cohomology”: [Tags 03NT–03NU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-cohomology), [Tags 03OK–03OS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-cech-cohomology), and [Tags 03OU–03OW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-cech-ss). These present the same foundations in the setting that motivates the rest of this course.
