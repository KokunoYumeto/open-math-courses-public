# Sheaves and D-modules on Bun_G

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Draft under mathematical proof repair; full proof closure pending. Public domain (CC0).*

An automorphic category has to remember two kinds of geometry: how bundles vary, and how their automorphisms act. The second survives even when the space of isomorphism classes is a point. We will calculate this for \(B\mathbb G_m\), then use it to describe the entire rank-one automorphic category.

The statements using truncatability, a global normalized half root, nilpotent regularity, derived tempered Satake or general Riemann–Hilbert remain conditional on the exact complete proofs listed in §9. The categorical and algebraic calculations below do not supply those geometric assertions.

Our standing assumptions are those of the [previous lesson](the-moduli-stack-of-bundles.md): \(X\) is a smooth projective connected curve over an algebraically closed field \(k\) of characteristic zero, and \(G\) is connected reductive. Write \(Y=\operatorname{Bun}_G(X)\). Complexes have cohomological grading; \(k[1]\) lies in degree \(-1\). A DG category here is a stable, presentable, \(k\)-linear category, and its tensor product is the tensor product of presentable categories. All limits and equivalences retain the complexes of morphisms and their homotopy coherences.

We use right D-modules and exceptional pullback \(f^!\) for descent on stacks. On a smooth scheme we can convert to left D-modules by tensoring with the inverse canonical line; we will use left modules only for the elementary characteristic-variety calculation. In comparisons with topology, \(k_Y\) denotes the constant object in the Riemann–Hilbert normalization. Thus on a complex smooth space of dimension \(d\), \(p_Y^!k\) corresponds to the dualizing complex \(k_Y[2d]\). Shifts do not affect singular support or compactness, but we retain the shift when calculating the fibre adjunction in §5.

The background is D-modules on smooth schemes, derived descent, and compact objects in a presentable category. The [D-module course](https://kokunoyumeto.github.io/open-math-courses-public/courses/GL-DMOD/) and [perverse-sheaf course](https://kokunoyumeto.github.io/open-math-courses-public/courses/GL-PERV/) supply the introductory material. Their planned units on stacks are not needed as unpublished references: the descent construction and the calculations used here are given below. The foundational D-module descent, base-change, and adjunction formalism is an input, not an assertion proved by treating stacks as sets of points.

## 1. Defining the category on an unbounded stack

On a smooth finite-type scheme \(S\), \(\operatorname{Dmod}(S)\) is the unbounded derived category of quasicoherent right D-modules. The extension to a prestack is the category of crystals, expressed as a limit

\[
\operatorname{Dmod}(Y)
  =\lim_{(S\to Y)}\operatorname{Dmod}(S),
\]

over affine schemes mapping to \(Y\), with exceptional pullback as transition functor. For an algebraic stack, smooth descent gives the equivalent description using smooth charts and their Čech nerves. An object includes identifications between its pullbacks and coherent identifications on multiple overlaps. Dropping this higher descent data changes the category.

Let \(\mathcal U(Y)\) be the poset of quasicompact open substacks. It is filtered: the union of two such opens is quasicompact. The intersections are quasicompact here because \(Y\) has affine diagonal.

**Proposition 1.1.** Restriction induces an equivalence

\[
\operatorname{Dmod}(Y)
  \simeq \lim_{U\in\mathcal U(Y)^{\mathrm{op}}}
            \operatorname{Dmod}(U).                 \tag{1.1}
\]

For \(U\subset V\), the transition is \(j^!\), also denoted \(j^*\) for this open embedding.

**Proof.** Every point of \(Y\) has a quasicompact open neighbourhood, so the opens in question cover \(Y\). More strongly, a map from a quasicompact affine scheme \(S\) to \(Y\) factors through one of them: its image is quasicompact and is covered by finitely many such neighbourhoods; take their union.

Suppose we have a compatible family \(M_U\). For an affine map \(f:S\to Y\), choose an open \(U\) through which it factors, and define \(M_S=f^!M_U\). If two choices \(U,V\) are made, their union \(W\) identifies both answers with the pullback of \(M_W\). The space of choices is filtered, so these identifications have coherent higher compatibilities, not merely pairwise isomorphisms. The same construction for maps between affine charts supplies a crystal on \(Y\). Its restriction recovers the family.

Conversely, pullbacks of a crystal give such a family. The two constructions compose to the identity. In particular their maps on morphism complexes are equivalences:

\[
\operatorname{RHom}_Y(M,N)
 \simeq \lim_U\operatorname{RHom}_U(M|_U,N|_U).
\]

This proves full faithfulness as well as essential surjectivity. The proof applies unchanged to a twisting gerbe pulled back to all charts. \(\square\)

This limit allows an object to have nonzero restrictions on arbitrarily unstable bundles and on infinitely many components. It does not impose finite support. Nor does the formula imply compact generation: limits of compactly generated categories need not be compactly generated.

Here are the specific deep inputs we use from [Drinfeld–Gaitsgory, Theorem 0.1.2 and Corollary 4.3.2, version 8](https://arxiv.org/abs/1112.2402v8). Under our assumptions, \(\operatorname{Dmod}(\operatorname{Bun}_G)\) is compactly generated. There is a cofinal system \(\mathcal U_{\mathrm{ct}}(Y)\) of quasicompact **co-truncative** opens; for them restriction has a continuous left adjoint \(j_!\). Define

\[
\operatorname{Dmod}_{\mathrm{co}}(Y)
 :=\mathop{\operatorname{colim}}_{U\in\mathcal U_{\mathrm{ct}}(Y)}
       \operatorname{Dmod}(U),
 \qquad\text{transition }j_* .
                                                        \tag{1.2}
\]

Then

\[
\operatorname{Dmod}(Y)^\vee
 :=\operatorname{Funct}_{\mathrm{cont}}
       (\operatorname{Dmod}(Y),\operatorname{Vect})
 \simeq \operatorname{Dmod}_{\mathrm{co}}(Y).             \tag{1.3}
\]

The geometric construction of these opens and this duality theorem are imported. We compute (1.1)–(1.3) directly for a discrete stack in §6. In general, the transition functor matters: the same co-truncative system presents \(\operatorname{Dmod}(Y)\) by a colimit with \(j_!\), whereas its dual uses \(j_*\). The two extensions agree for open-and-closed components; they can differ at a boundary.

### 1.1. The formal compact-generation proof

Let \(C\) be a stable presentable category, and let \(r_i:C\to C_i\) be a jointly conservative family of continuous functors. Suppose each \(C_i\) has a set \(G_i\) of compact generators and \(r_i\) has a continuous left adjoint \(l_i\). Then the objects \(l_i(g)\), for \(g\in G_i\), are compact generators of \(C\).

Indeed, for a filtered diagram \(M_a\), adjunction and continuity give

\[
\operatorname{RHom}_{\mathcal C}(l_i g,\operatorname{colim}_a M_a)
 \simeq\operatorname{RHom}_{\mathcal C_i}
 (g,\operatorname{colim}_a r_iM_a)
 \simeq\operatorname{colim}_a
 \operatorname{RHom}_{\mathcal C}(l_i g,M_a).
\]

Thus these objects are compact. If all their mapping complexes into \(M\) vanish, the generator property in \(C_i\) implies \(r_iM=0\) for every \(i\); conservativity then gives \(M=0\). Their localizing closure is all of \(C\): the inclusion of the localizing subcategory generated by a set admits a right adjoint; the cofiber of its counit is right orthogonal to the generating set and therefore zero. Equivalently, successively attach coproducts of shifts of the generators to kill every mapping class, take the sequential colimit, and apply the same orthogonality test. This proves the generator assertion.

For an open exhaustion the conservativity needed here is already proved by the restriction-limit argument of Proposition 1.1. If \(l_i=j_{i!}\) exists on the full category, this proof gives the precise generators \(j_{i!}G_i\). It does not construct a single co-truncative open, prove finite-type QCA compact generation, or prove preservation of the half twist. Those are separate hypotheses requiring their own programme proofs.

One can also prove the colimit presentation directly. Assume the system of opens is directed, and every transition has continuous extension \(j_{ij!}\) with the usual restriction and composition identities. For a compatible family \(M=(M_i)\) form

\[
\operatorname{colim}_i j_{i!}M_i.
\]

For a fixed \(a\), restriction to \(U_a\) agrees with \(M_a\) on the cofinal subposet of indices \(i\) containing \(a\). The counit maps give the transition arrows. Restriction preserves colimits, so its restriction is \(M_a\). Joint conservativity identifies the colimit with \(M\). Conversely, a coherent cocone of continuous functors \(T_i:C_i\to E\), compatible with \(j_{ij!}\), extends by \(M↦\operatorname{colim}_i T_iM_i\). The same restriction computation shows that this extension restricts to \(T_i\); the displayed reconstruction makes it the unique continuous extension, including natural transformations. This proves \(C\simeq \operatorname{colim}_{j_!}C_i\) through its universal property.

### 1.2. Why the continuous dual uses the other extensions

The formal assertion needed here is the following conditional statement. Suppose the local categories \(C_i\) are compactly generated and have specified dualities \(C_i^\vee\simeq C_i\). Suppose the restriction functor \(r_{ij}:C_j\to C_i\) is dual, under those specified pairings, to \(e_{ij}:C_i\to C_j\). Assume \(e_{ij}\) preserves compact objects. Let

\[
\mathcal E=\operatorname{colim}_{e_{ij}}\mathcal C_i.
\]

Then

\[
\mathcal E^\vee\simeq\lim_{r_{ij}}\mathcal C_i,
\qquad
\left(\lim_{r_{ij}}\mathcal C_i\right)^\vee\simeq\mathcal E.
\]

Here is the construction. Let \(D\) be the idempotent completion of the small stable colimit of the categories \(C_i^c\) and their compact-preserving transitions. Its ind-completion satisfies the universal property of \(E\): a continuous exact functor \(\operatorname{Ind}(D)\to T\) is exactly an exact functor on \(D\), and that is exactly a coherent family of exact functors on the \(C_i^c\). Extending those functors by colimits gives the coherent continuous cocones on \(C_i\). Thus \(E=\operatorname{Ind}(D)\) and is compactly generated.

For completeness, \(\operatorname{Ind}(D)\) has dual \(\operatorname{Ind}(D^op)\). The evaluation on generators \(d^op,d'\) is \(\operatorname{RHom}_D(d,d')\), extended continuously in each argument. Its coevaluation is the diagonal bimodule. The two triangle identities are the enriched Yoneda identity: tensoring a representable with the diagonal reproduces that representable; continuous extension reproduces every object. Applying the construction twice returns \(\operatorname{Ind}(D)\), so its canonical bidual map is an equivalence.

Now a continuous functional \(E\to \operatorname{Vect}\) is, by the colimit universal property, precisely a coherent family of continuous functionals \(C_i\to \operatorname{Vect}\). This identifies \(E^\vee\) with the limit of the local dual categories. Under the specified local dualities its transition is \(r_{ij}\), because it is precomposition with \(e_{ij}\). This proves the first formula; the bidual equivalence proves the second. It also proves that the dual of the \(i\)th restriction is the \(i\)th insertion into \(E\).

Apply this only after proving the local hypotheses. For D-modules the intended \(e_{ij}\) is \(j_{ij*}\), and the resulting \(E\) is \(\operatorname{Dmod}_{\mathrm{co}}(Y)\). The local dualities, the identity \((j^!)^\vee=j_*\), and the compact-preservation condition must be established in the stack formalism. They are not consequences of the existence of \(j_!\) by notation. A proof that instead dualizes the \(j_!\) diagram while calling its arrows \(j_*\) omits this issue.

The open-and-closed example in §6 verifies all these conditions directly for a discrete union. It cannot verify them at Harder–Narasimhan boundaries of a general bundle stack.

## 2. The half twist and its local meaning

The tangent complex at a bundle \(P\) is \(R\Gamma(X,\operatorname{ad}(P))[1]\). For a perfect complex \(V\), \(\det(V[1])=\det(V)^{-1}\) and \(\det(V^\vee)=\det(V)^{-1}\). Consequently the determinant of the cotangent complex, namely the canonical line of the stack, has fibre

\[
\omega_Y|_P=\det R\Gamma(X,\operatorname{ad}(P)).
\]

Following [GLC I, §1.1.1](https://arxiv.org/abs/2405.03599), use the normalized line

\[
\mathcal D|_P
 =\det R\Gamma(X,\operatorname{ad}(P))
   \otimes
   \det R\Gamma(X,\mathfrak g\otimes\mathcal O_X)^{-1}.
                                                        \tag{2.1}
\]

It differs from \(\omega_Y\) by a constant line and is trivialized at the trivial bundle.

The root gerbe \(\sqrt{\mathcal D}\to Y\) assigns to \(S\to Y\) pairs
\((L,\phi:L^{\otimes2}\simeq\mathcal D|_S)\). Its band is \(\mu_2\). Define

\[
\operatorname{Dmod}_{1/2}(Y)
 =\operatorname{Dmod}(\sqrt{\mathcal D})_{\mathrm{sign}},
                                                        \tag{2.2}
\]

where the band acts through its nontrivial character. The definition exists whether or not a global square root has been selected.

To see the differential operators in this definition, choose local frames of \(\mathcal D\) with coordinate transitions \(g_{ab}\), and local roots \(h_{ab}\) satisfying \(h_{ab}^2=g_{ab}\). If local sections of a root satisfy \(f_a=h_{ab}f_b\), an operator changes by conjugation:

\[
D_a=h_{ab}D_bh_{ab}^{-1},\qquad
h_{ab}\partial h_{ab}^{-1}
 =\partial-\frac12\,\partial\log(g_{ab}).                \tag{2.3}
\]

On a triple overlap the product of the \(h\)'s is a constant sign. Conjugation by that sign is the identity, so the sheaf of twisted differential operators glues. The sign remains in the descent of modules; the gerbe records it. This distinguishes the existence of the twisted category from the existence of a chosen global root line.

A global root neutralizes the gerbe and gives an equivalence with the untwisted category. In local operator language, \(M\mapsto L\otimes M\) is an equivalence from ordinary D-modules to modules for the differential operators acting on \(L\). This does not assert that \(L\) has an ordinary flat connection: the operators themselves have changed.

For this particular stack, a choice of theta characteristic on \(X\) supplies a root of (2.1); this is the input in GLC I §1.1.2. The classical half-form construction for semisimple \(G\) is [Beilinson–Drinfeld, §4.4.1, equation (209), PDF pp.163–164](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf). It uses Pfaffian data for the orthogonal adjoint representation. We use its normalized square-root assertion, not a claim that an arbitrary canonical line on an arbitrary stack has a square root.

The twist is retained even after choosing an untwisting equivalence. GLC I §1.1, the remark following (1.1), explains its compatibility with the usual dual-group representation category in Hecke functors. Changing the root can change the chosen identification with ordinary D-modules; it does not change the definition (2.2).

### 2.1. The finite Pfaffian calculation and its family obligation

The finite-dimensional core of the Pfaffian construction has an equally precise scope. Let \(E\) be a vector bundle, and let \(a:E\to E^\vee\) be skew-symmetric. For the two-term complex \(K=[E\to E^\vee]\) in degrees zero and one,

\[
\det K=\det E\otimes(\det E^\vee)^{-1}
       =(\det E)^{\otimes2}.
\]

Thus \(\det E\) is a square root for this presentation. Stabilizing by an acyclic skew block supplies its Pfaffian trivialization: if the block is \(F\to F^\vee\) with invertible alternating form, its top exterior power gives the canonical trivialization of \(\det F\); it squares to the corresponding determinant trivialization. Basis changes transform the top exterior form by the determinant, so this statement is independent of the chosen basis. Composition of orthogonal changes preserves these identifications. This proves the algebraic compatibility for such finite presentations.

It does **not** yet produce a line on \(\operatorname{Bun}_G\). To do that one must construct compatible skew-self-dual perfect representatives of \(R\Gamma(X,\operatorname{ad}(P)\otimes \kappa)\) in families, prove that the Pfaffian transitions across quasi-isomorphisms satisfy the cocycle, and prove the determinant comparison

\[
\frac{\det R\Gamma(X,\operatorname{ad}(P)\otimes\kappa)}
     {\det R\Gamma(X,\mathfrak g\otimes\kappa)}
\simeq
\frac{\det R\Gamma(X,\operatorname{ad}(P))}
     {\det R\Gamma(X,\mathfrak g\otimes\mathcal O_X)}.
\]

The quotient notation means tensoring by the inverse constant line. Pointwise identities between cohomology determinants do not prove this family identity or its descent. Once those assertions are proved, the normalized Pfaffian ratio squares to (2.1), and its value at the trivial bundle is canonically trivial. The existing local conjugation formula (2.3) only proves the twisting-gerbe description; it proves neither the family comparison nor existence of a global root. The semisimple construction must additionally be extended to the connected reductive case actually used by the lesson, accounting for its central adjoint summand.

## 3. Singular support and what nilpotence requires

For a coherent D-module on a smooth scheme, a good filtration produces a finitely generated module over
\(\operatorname{gr}\mathcal D_S=\operatorname{Sym}_{\mathcal O_S}T_S\).
Its support in \(T^*S\), independent of the good filtration, is its characteristic variety. On a smooth stack this condition is tested on smooth charts and descends. For arbitrary objects the support condition is imposed in the corresponding category closed under colimits; it can have an ind-closed support. Thus a statement about a large category is not a claim that every object has a single finite good filtration.

For a smooth map \(f:S\to Y\), a covector on \(Y\) pulls back through \(df^*\) to one on \(S\). This is the comparison used on charts; \(T^*Y\) must retain the stack cotangent geometry computed in Lesson 2. Twisting differential operators by a line does not change their associated graded algebra or this support condition.

**Proposition 3.1.** A finite-rank flat connection on a smooth scheme has characteristic variety the zero section over its nonzero fibres. A lisse object on a smooth stack has singular support contained in the zero section. For the nonzero constant object on \(Y\), the support is the full zero section.

**Proof.** Convert to a left D-module \(E\), and take the filtration \(F_iE=0\) for \(i<0\), \(F_iE=E\) for \(i\ge0\). It is good: its associated graded is the finite-rank \(\mathcal O_S\)-module \(E\), concentrated in filtration degree zero. The principal symbol of a vector field has positive degree and acts by zero on this graded module, since the connection maps \(E\) to \(E\). All fibre-linear functions on \(T^*S\) therefore annihilate it. The support is precisely the zero section over the ordinary support of \(E\). For a flat vector bundle this is a union of connected components.

A bounded complex of connections has the same containment, by the support rule for exact triangles. The large lisse category is defined locally with the corresponding colimit closure. Smooth pullback tests the stack condition, so the containment descends. The constant connection is nonzero on every chart and every component; its support is the whole zero section. \(\square\)

The qualification about nonzero fibres is necessary: the zero object has empty singular support, and a local system supported on one open-and-closed component does not fill the other components.

For a coherent D-module the converse on a smooth scheme is also useful. If its characteristic variety lies in the zero section, a power of the positive-symbol ideal annihilates its associated graded module. That module is therefore finite over \(\mathcal O_S\), and its good filtration is bounded above locally. Hence the original module is \(\mathcal O_S\)-coherent and its D-action is an integrable connection. Such a coherent module with connection is locally free in characteristic zero. One can check this on a completed smooth local ring: commuting connection operators \(\nabla_i\) give the formal Taylor projection
\[
P(m)=\sum_{\alpha\ge0}
       \frac{(-t)^\alpha}{\alpha!}\nabla^\alpha m .
\]
The series converges in the maximal-ideal topology. The commutator
\([\nabla_i,t_j]=\delta_{ij}\) shows \(\nabla_iP(m)=0\) and \(P(t_im)=0\). Thus \(P\) identifies the fibre with horizontal lifts, and the inverse Taylor expansion identifies the completed module with the free module on that fibre. Faithful flatness of completion proves local freeness. Consequently coherent zero-support modules are precisely finite-rank flat connections; the large zero-support condition uses their ind and derived version.

Using a nondegenerate invariant form when we identify adjoint and coadjoint bundles, the cotangent stack consists of Higgs bundles \((P,\phi)\). Let

\[
\operatorname{Nilp}_G
 =\{(P,\phi):\phi\text{ is pointwise nilpotent}\}
 =h^{-1}(0)\subset T^*Y .
\]

Nilpotence kills the central component of a Higgs field as well as its invariant polynomials in the semisimple directions. Define the full subcategory

\[
\operatorname{Dmod}_{1/2,\operatorname{Nilp}}(Y)
 =\{M:\operatorname{SS}(M)\subset\operatorname{Nilp}_G\}.
                                                        \tag{3.1}
\]

The constant object belongs to it. A general object of the full de Rham automorphic category need not: on the Picard variety of a positive-genus curve, a skyscraper D-module has the entire cotangent fibre as characteristic variety.

**Imported regularity theorem.** Under our characteristic-zero curve and group assumptions, (3.1) equals its subcategory obtained from ind-regular holonomic D-modules on affine charts, followed by descent. In particular its objects are locally ind-holonomic with regular singularities. The exact source is [AGKRRV, Corollary 16.5.6](https://arxiv.org/abs/2010.01906), headed “The regular singularity property”; [GLC I, §4.2.1 and its footnote](https://arxiv.org/abs/2405.03599) states the equality and the chartwise meaning of ind-completion. We do not prove the spectral-projector argument establishing this theorem.

The word “ind” matters. An infinite direct sum of regular connections is an allowed object, with no finite-rank assertion. On an unbounded stack, one must also distinguish global compactness, chartwise constructibility, and coherent or holonomic cohomology. The explicit counterexample in §5 prevents identifying these notions.

Extension from an arbitrary open can add characteristic directions at its boundary. AGKRRV’s section “Preservation of nilpotence of singular support” constructs suitable bounded opens for which both extensions preserve the nilpotent condition. Its introductory main theorem, labelled \(t:\mathrm{preserve\ Nilp\ Sing\ Supp\ prel}\) in the consulted TeX, gives a cofinal system; it does not assert this for every open. We use this as a scoped input, not as a consequence of the definition of (3.1).

## 4. Betti, constructible, and tempered categories

Now suppose \(k=\mathbb C\), and choose a coefficient field \(E\) of characteristic zero. The **large Betti** category consists of complexes of \(E\)-sheaves on the analytic stack, with no finite-dimensional stalk requirement. Its automorphic subcategory is

\[
\operatorname{Shv}^{\mathrm{Betti}}_{1/2,\operatorname{Nilp}}(Y)
 \subset\operatorname{Shv}^{\mathrm{Betti}}_{1/2}(Y).
                                                        \tag{4.1}
\]

Here singular support is the microlocal support on smooth analytic charts. The zero-support condition on a smooth space says that a sheaf is locally constant as a derived sheaf. “Derived” is essential on a stack: local systems include higher coherent monodromy, not just representations of its ordinary fundamental group.

There is also a chartwise ind-constructible theory: on each finite-type affine chart, ind-complete the category of bounded complexes with algebraically constructible finite-dimensional cohomology, then descend. This is the theory denoted \(\operatorname{Shv}^{\mathrm{Betti,constr}}\) in GLC I. Its nilpotent subcategory is the **restricted** automorphic variant. It can be smaller than the large category. Compact objects of the large category are not defined by finite-dimensional stalks; §7 gives a rank-one example.

Riemann–Hilbert, with ind-completion on charts, identifies the regular de Rham nilpotent category with this ind-constructible Betti nilpotent category for complex coefficients. It does not identify every algebraic D-module with every arbitrary topological sheaf. The precise comparison appears in GLC I §4.2.1; the large and restricted Betti variants are separated in §§3.1 and 3.6. In particular the Betti spectral stack has a restricted-variation version distinct from the entire character stack, even though they have the same field-valued local systems. Point sets cannot specify their categories of families.

Over a finite field one instead uses \(\ell\)-adic sheaves, \(\ell\ne\operatorname{char}(k)\), formed from constructible finite-type-chart categories with their ind-completions and descent. Frobenius descent supplies arithmetic trace functions. A Weil structure and a continuous étale representation are different conditions, as in Lesson 1. This paragraph specifies the sheaf theory used for motivation; it does not infer a positive-characteristic equivalence from the characteristic-zero proof.

Temperedness is another condition. Its construction uses the spherical Hecke category at a point \(x\), introduced in the Satake lesson. Derived Satake defines an anti-tempered subcategory \(\mathcal C_{\mathrm{anti},x}\) of the automorphic category \(\mathcal C\). The quotient has a fully faithful left adjoint, so it can also be realized as a full subcategory:

\[
\mathcal C_{\mathrm{temp},x}
 =\mathcal C/\mathcal C_{\mathrm{anti},x},\qquad
u:\mathcal C_{\mathrm{temp},x}\hookrightarrow\mathcal C,
\qquad u\dashv u^R .                                  \tag{4.2}
\]

We import this local Hecke construction and its point independence. Confirmed locators are [Færgeman–Raskin, the conventions subsection “Tempered D-modules,” “Local formalism” and “Global setting”](https://arxiv.org/abs/2207.02955), and GLC I §§5.1.1 and 5.2.1. The original [Arinkin–Gaitsgory §12.8.4](https://arxiv.org/abs/1201.6343) defines the Hecke-support condition and states point independence as a conjecture in that earlier work; the later sources establish it. The de Rham reference to “17.8.4” in GLC I §5.1.1 differs from the confirmed §12.8.4 in the consulted AG source and from GLC I’s own Betti citation.

The notation
\(\operatorname{Dmod}_{1/2,\operatorname{Nilp}}(Y)_{\mathrm{temp}}\)
means the intersection of (3.1) with the full-subcategory realization in (4.2). The nilpotent condition uses covectors on \(Y\); the tempered condition uses the local Hecke action and, on the spectral side, its zero singular-support part. Their supports live on different geometric objects.

For a concrete distinction take \(G=SL_2\). The zero element of \(\mathfrak{sl}_2\) is **irregular**: its centralizer has dimension three, greater than the rank one. Thus the constant object, whose support is the zero section, has support in the irregular part of the global nilpotent cone. The theorem in Færgeman–Raskin, Part I, “Irregular singular support on \(\operatorname{Bun}_G\),” labelled \(t:\mathrm{at}\), says objects with such support are anti-tempered. The constant object is nonzero, so it cannot also lie in the tempered image, since the quotient kills the anti-tempered category and is the identity on that image. This example uses the stated theorem; nilpotent support alone does not prove temperedness.

The full proof of geometric Langlands and its relation to the tempered quotient belong to later lessons. The constructions here specify their automorphic categories.

## 5. A classifying stack computed by descent

Put

\[
A=k[\epsilon]/(\epsilon^2),\qquad |\epsilon|=-1,\quad d\epsilon=0.
                                                        \tag{5.1}
\]

The tensor product in
\(\operatorname{Spec}k\times^{\mathbf R}_{\mathbb A^1}\operatorname{Spec}k\)
is derived, with both maps landing at \(0\). Resolving \(k\) over \(k[t]\) by its two-term Koszul complex gives

\[
k\otimes^{\mathbf L}_{k[t]}k\simeq A.
                                                        \tag{5.2}
\]

The ordinary fibre product would be a point and would lose \(\epsilon\).

**Proposition 5.1.** With the fibre normalization specified above,

\[
\operatorname{Dmod}(B\mathbb G_m)
 \simeq \operatorname{Mod}_A
 \simeq
\operatorname{QCoh}
  (\operatorname{Spec}k\times^{\mathbf R}_{\mathbb A^1}\operatorname{Spec}k).
                                                        \tag{5.3}
\]

The constant object corresponds to the augmentation module \(k=A/(\epsilon)\); a compact generator corresponds to \(A\).

**Proof.** Let \(p:\operatorname{Spec}k\to B\mathbb G_m\) be the smooth atlas. Normalize its pullback \(F\) to take the ordinary fibre of a local system, so \(F(k_{B\mathbb G_m})=k\). Over \(\mathbb C\), this is \(p^![-2]\), since the atlas has relative complex dimension one. Its left adjoint \(L\) is the correspondingly shifted compact-support direct image. This normalized adjunction has the same algebraic de Rham construction over any characteristic-zero \(k\).

The smooth-descent formalism makes \(F\) conservative and colimit preserving. Thus \(Q=L(k)\) is compact, because

\[
\operatorname{RHom}(Q,M)=F(M)
\]

commutes with colimits. It generates: if that complex vanishes, smooth descent gives \(M=0\).

The fibre of the atlas over itself is \(\mathbb G_m\). Exceptional base change identifies the monad \(FL\) with tensoring by its de Rham homology algebra, with multiplication induced by group multiplication. In the complex normalization its underlying complex is
\(R\Gamma_c(\mathbb G_m,k)[2]\): it has \(k\) in degrees \(0,-1\).
The algebraic calculation is equally explicit. The de Rham complex

\[
k[t,t^{-1}]\longrightarrow k[t,t^{-1}]\,d\log t
\]

has a quasi-isomorphic subalgebra \(k\oplus k\,d\log t\), with \(d\log t\) in degree one: every nonzero Laurent mode is exact because its integer exponent is invertible in \(k\). This is a Hopf model, since multiplication pulls \(d\log t\) back to
\(d\log t_1+d\log t_2\). Its homological dual is (5.1), with the Pontryagin multiplication. Hence \(FL\simeq A\otimes-\) as a monad.

The adjunction is monadic. To spell out the argument, the bar resolution of an \(A\)-module is built from free modules \(A\otimes V\). Apply \(L\) to the corresponding free diagram and take its geometric realization. Applying \(F\), which preserves that realization, recovers the module's bar resolution. Conversely the adjunction bar construction for any \(M\) maps to \(M\); applying \(F\) makes that map an equivalence, and conservativity makes it an equivalence before applying \(F\). This proves (5.3), including morphisms. The constant object has trivial group action and therefore the augmentation action; \(L(k)\) is the free module. \(\square\)

This calculation agrees with AG §11.2, the remark in “The case of a torus.” It uses D-module descent and base change, but proves the specific algebra and the formal equivalence instead of replacing \(B\mathbb G_m\) by its single isomorphism class.

### 5.1. The finite-cell compactness criterion

The compact-module criterion used in Proposition 5.2 can be supplied locally. A DG algebra \(A\) has a semifree resolution of every DG module: start with free cells mapping to representatives of every cohomology class, then attach free cells with chosen nullhomotopies to kill the cohomology of the mapping fiber, and repeat. The sequential union maps quasi-isomorphically to the module because every surviving fiber class is killed at a later stage. Every cell differential uses only finitely many cells from earlier stages. Consequently this semifree resolution is a filtered union of finite-cell submodules: close a finite set of cells under the finitely many differential dependencies, working down its finitely many construction stages.

A finite-cell module is compact, because \(\operatorname{RHom}_A(A,-)\) is the underlying complex functor, and shifts and finite cofibers preserve compactness. Retracts preserve compactness too. Conversely, if \(M\) is compact, replace it by the semifree resolution \(P\). The identity of \(M\simeq P\), considered as a map into the filtered colimit of the finite-cell submodules of \(P\), factors through one finite-cell module. Hence \(M\) is its retract in the derived category. This proves the criterion used in the noncompactness argument, rather than importing it under a generic prerequisite label.

**Proposition 5.2.** The constant object in (5.3) is coherent but not compact.

**Proof.** Its underlying \(A\)-module \(k\) has bounded finite-dimensional cohomology, so it is coherent. Resolve it by the semifree module

\[
P=\bigoplus_{n\ge0}Ae_n,\quad |e_n|=-2n,\quad
de_0=0,\quad de_n=\epsilon e_{n-1}\ (n\ge1).
                                                        \tag{5.4}
\]

Its degree-zero cohomology is \(ke_0\). Every \(\epsilon e_n\) is the boundary of \(e_{n+1}\); every other \(e_n\), \(n>0\), has nonzero differential. Thus \(P\to k\) is a quasi-isomorphism.

Applying \(\operatorname{Hom}_A(-,k)\) gives one copy of \(k\) in each degree \(2n\), with zero differential. The degree-two chain map sending \(e_n\) to \(e_{n-1}\) for \(n\ge1\), and \(e_0\) to zero, generates the Yoneda products. Therefore

\[
\operatorname{Ext}^*_A(k,k)=k[u],\qquad |u|=2.           \tag{5.5}
\]

Compact modules over a DG algebra are the retracts of finite cell modules. For a finite cell \(A\)-module \(C\), \(\operatorname{RHom}_A(C,k)\) is bounded: start with
\(\operatorname{RHom}_A(A,k)=k\), and use finite shifts, cofibres, and retracts. Equation (5.5) is unbounded, so \(k\) cannot be compact. \(\square\)

The standard heart of \(\operatorname{Mod}_A\) is \(\operatorname{Vect}_k\), since \(H^0(A)=k\). But \(\operatorname{Dmod}(B\mathbb G_m)\) is not the ordinary derived category of that heart: the latter has no positive self-extensions of \(k\), whereas (5.5) does. A connected stabilizer can be invisible in the heart while contributing higher morphisms.

## 6. The Picard stack and categorical support on degrees

Choose \(x\in X(k)\), and write \(J=\operatorname{Pic}^0(X)\). Rigidifying degree-zero line bundles along \(x\) gives the normalized Poincaré line bundle \(\mathcal P\) on \(X\times J\). We use the representability of the rigidified Picard functor from Lesson 2.

For \(\mathbb G_m\), \(\operatorname{ad}(P)=\mathcal O_X\) canonically for every bundle. Thus the normalized determinant line (2.1) is trivial. Using its trivial root identifies the half-twisted category with the untwisted one in the rank-one calculations.

**Theorem 6.1.** The chosen point yields an equivalence of stacks

\[
\operatorname{Bun}_{\mathbb G_m}
 \simeq J\times B\mathbb G_m\times\underline{\mathbb Z}.
                                                        \tag{6.1}
\]

For a family, its degree is locally constant; \(\underline{\mathbb Z}\) is the discrete scheme of all degrees.

**Proof.** Work on an open-and-closed part of a base \(S\) where the degree is \(d\). For a line bundle \(M\) on \(X\times S\), put

\[
M_0=M\otimes\mathcal O_X(-dx),\quad
N=M_0|_{x\times S},\quad
M_{\mathrm{rig}}=M_0\otimes\pi_S^*N^{-1}.
\]

The last bundle has degree zero and a canonical rigidification at \(x\). It gives a unique map \(f:S\to J\) and a rigidified isomorphism
\(M_{\mathrm{rig}}\simeq(1_X\times f)^*\mathcal P\).
We recover

\[
M\simeq(1_X\times f)^*\mathcal P
        \otimes\pi_S^*N\otimes\mathcal O_X(dx).           \tag{6.2}
\]

Conversely \(f,N,d\) give (6.2). These constructions commute with base change. An isomorphism of line bundles preserves the degree and the rigidified Picard class and induces precisely an isomorphism of \(N\). There are no additional automorphisms of a rigidified line bundle: global invertible functions on \(X\times S\) come from \(S\), and their value at \(x\) is one. Here we use \(\pi_*\mathcal O_{X\times S}=\mathcal O_S\), with its base-change compatibility for the proper geometrically connected curve.

Thus the two constructions are inverse on arrows as well as objects, proving the equivalence. \(\square\)

The \(J\) in (6.1) is the degree-zero Picard scheme. Using the entire Picard scheme in that factor and also multiplying by \(\mathbb Z\) would count degrees twice.

**Theorem 6.2.** There are equivalences

\[
\begin{aligned}
\operatorname{Dmod}(\operatorname{Bun}_{\mathbb G_m})
 &\simeq
 \prod_{d\in\mathbb Z}
       \bigl(\operatorname{Dmod}(J)\otimes\operatorname{Mod}_A\bigr)\\
 &\simeq
 \operatorname{Dmod}(J)\otimes
 \operatorname{Dmod}(B\mathbb G_m)\otimes
 \operatorname{Dmod}(\underline{\mathbb Z}).
\end{aligned}                                         \tag{6.3}
\]

**Proof.** First apply the atlas argument in Proposition 5.1 with coefficients in \(\operatorname{Dmod}(J)\): pull back from \(J\times B\mathbb G_m\) to \(J\). Base change now gives the monad \(M\mapsto A\otimes M\), because the atlas fibre is the constant group \(\mathbb G_m\) over \(J\). Pullback is conservative and preserves colimits. Its bar construction identifies the category with \(A\)-modules in \(\operatorname{Dmod}(J)\), which is
\(\operatorname{Dmod}(J)\otimes\operatorname{Mod}_A\).

Next, a sheaf or crystal on a disjoint union is exactly a family on its components. Proposition 1.1 applied to finite unions also gives this product, with componentwise colimits. Finally, in stable presentable categories the product \(\prod_d\mathcal C_d\) is also their categorical coproduct: every family is the coproduct of its individual component insertions. A continuous functor out of it is therefore uniquely determined by its continuous functors on the factors. The tensor product preserves this coproduct. Since
\(\operatorname{Dmod}(\underline{\mathbb Z})=\prod_d\operatorname{Vect}\),
this proves the second line. \(\square\)

For \(\underline{\mathbb Z}\), the quasicompact opens are the finite subsets \(F\). The limit of their restriction categories is
\(\prod_{d\in\mathbb Z}\operatorname{Vect}\).
The colimit in presentable categories of
\(\prod_{d\in F}\operatorname{Vect}\), using zero extension, is **also** this category: it includes all colimits of the finite-support insertions. In particular

\[
(k)_{d\in\mathbb Z}
 =\mathop{\operatorname{colim}}_{F\text{ finite}}
        (k\text{ on }F,\ 0\text{ elsewhere}).           \tag{6.4}
\]

Thus \(\operatorname{Dmod}_{\mathrm{co}}(\underline{\mathbb Z})\)
and \(\operatorname{Dmod}(\underline{\mathbb Z})\) are canonically equivalent in this example. Nonquasicompactness alone does not make them different.

What changes is the compact-object calculation. A family \(M=(M_d)\) is compact exactly when its support is finite and each \(M_d\) is a perfect \(k\)-complex. Necessity of componentwise perfection follows by testing diagrams in one component. For finite support it is also sufficient, since

\[
\operatorname{RHom}(M,N)
 =\prod_{d\in\operatorname{supp}M}\operatorname{RHom}(M_d,N_d)
\]

is a finite product commuting with filtered colimits. If infinitely many \(M_d\) are nonzero, write \(M\) as the filtered colimit of its finite truncations. Compactness would make its identity factor through one of those truncations, forcing every component outside that finite set to be zero. This is a contradiction.

The continuous dual of the product category is again the product. Explicitly, a family \(V=(V_d)\) defines the continuous functional

\[
N\longmapsto\bigoplus_{d\in\mathbb Z}V_d\otimes N_d.
                                                        \tag{6.5}
\]

Every continuous functional has this form, by the component decomposition of \(N\). Its evaluation uses a direct sum of **vector spaces**, while its parameter \(V\) can have infinite support. Confusing these two levels would incorrectly turn (1.2) into a category consisting only of finite-support objects.

For \(X=\mathbb P^1\), \(J\) is a point, and (6.3) becomes
\(\prod_{d\in\mathbb Z}\operatorname{Mod}_A\).
An object concentrated in one degree and equal to \(A\) is compact. The constant family of augmentation modules \(k\) is not compact, both because each component fails Proposition 5.2 and because its degree support is infinite. Its singular support is nevertheless zero.

## 7. Rank-one Betti nilpotent sheaves, including higher monodromy

For \(\mathbb G_m\), the adjoint representation is trivial. The cotangent fibre at any line bundle is \(H^0(X,\omega_X)\), and the invariant-polynomial map is the identity in these central directions. Therefore the nilpotent cone is exactly the zero section. The Betti nilpotent category consists of derived local systems on (6.1).

For complex \(X\) of genus \(g\), the analytic Jacobian is a real torus:
\(J^{\mathrm{an}}\simeq K(\mathbb Z^{2g},1)\). Its universal cover is a contractible complex vector space and its lattice is \(H_1(X,\mathbb Z)\). Also
\(B\mathbb C^\times\simeq K(\mathbb Z,2)\), since
\(\mathbb C^\times\) retracts onto \(S^1\).
For \(R=E[\mathbb Z^{2g}]\), and \(A_E=E[\epsilon]/(\epsilon^2)\) as above, we obtain

\[
\operatorname{Shv}^{\mathrm{Betti}}_{\operatorname{Nilp}}
       (\operatorname{Bun}_{\mathbb G_m})
 \simeq
 \prod_{d\in\mathbb Z}\operatorname{Mod}_{R\otimes_E A_E}.
                                                        \tag{7.1}
\]

**Derivation.** A local system on a connected homotopy type \(Z\), valued in complexes, is a module over \(C_*(\Omega Z,E)\): evaluation at a base point and its left adjoint give the loop-chain monad, with the same bar argument as §5. For \(J\), the loop components are the lattice and each component is contractible, giving \(R\). For \(B\mathbb C^\times\), loop chains give \(A_E\). The product gives their tensor product; disjoint degrees give the categorical product. The vanishing-cycles criterion for locally constant sheaves identifies these with zero singular support. This proves (7.1). It is the rank-one calculation underlying [Ben-Zvi–Nadler, §4.3 “Betti class field theory”](https://arxiv.org/abs/1606.08523).

The ordinary fundamental group of \(B\mathbb C^\times\) is trivial, but its loop-chain algebra has \(\epsilon\). Replacing its derived local systems by representations of that fundamental group would replace \(\operatorname{Mod}_{A_E}\) by \(\operatorname{Vect}_E\) and erase (5.5).

The restricted category can be described as \(A_E\)-modules with coefficients in the ind-completion of finite-dimensional derived local systems on \(J\), one family in each degree. It is obtained by taking these ind-completions on charts before descent. For \(g>0\) it does not contain the local system corresponding to the regular \(R\)-module \(R\): at a point of \(J\) its fibre is infinite dimensional and its lattice action is not locally finite. Every vector in an ind-finite-dimensional lattice representation lies in a finite-dimensional invariant subspace; the orbit of \(1\in R\) spans all of \(R\). This demonstrates the distinction without imposing finite support on the degree family.

In contrast, \(R\otimes A_E\) is compact in the large module category in one fixed degree, since it is free of rank one over its defining algebra. It has infinite-dimensional fibre when \(g>0\). The constant object \(E\), with trivial lattice and \(\epsilon\) actions, has finite-dimensional fibre but is not compact. Indeed use the finite Koszul resolution for the augmentation of the Laurent polynomial ring \(R\), and tensor it with (5.4). Applying \(\operatorname{Hom}(-,E)\) retains the unbounded powers of \(u\) from (5.5). A perfect module has bounded such Hom, so the same contradiction proves noncompactness.

In the de Rham nilpotent category, the \(J\)-factor is the category of ind-flat connections, and the \(B\mathbb G_m\)-factor remains (5.3). Since \(J\) is proper, finite-rank connections have no boundary at infinity at which irregular singularities could occur. Riemann–Hilbert identifies this with the restricted Betti description, consistent with the imported regularity theorem. All these are rank-one computations of categories; their Hecke eigenobjects and Fourier transform are developed in the class-field-theory lessons.

## 8. Exercises

**Exercise 8.1 — easy.** For a finite-rank flat connection, compute the annihilator of its associated graded module using the filtration in Proposition 3.1. Explain exactly when “its support is the zero section” needs a qualification. Apply this to the constant object on \(Y\).

**Exercise 8.2 — easy.** Construct the equivalence (6.1) on families and on their automorphisms. Identify what goes wrong if \(J\) is replaced by the entire degree-graded Picard scheme.

**Exercise 8.3 — medium.** Compute the derived algebra in (5.2), resolve its augmentation module, and prove that the constant object of \(B\mathbb G_m\) is not compact. Explain why its coherence and the semisimplicity of the heart do not contradict this.

**Exercise 8.4 — medium.** Describe the large Betti nilpotent category for \(\mathbb G_m\) on a curve of genus \(g\). For \(g=0\), simplify it. For \(g>0\), produce a compact object with infinite-dimensional fibre and an object in the large category excluded from the restricted one.

**Exercise 8.5 — hard.** Starting from finite subsets of \(\mathbb Z\), compute the restriction limit, the zero-extension colimit in presentable categories, their compact objects, and the continuous dual. Use this to explain the role of \(\operatorname{Dmod}_{\mathrm{co}}\) without claiming that the two categories must differ on \(\underline{\mathbb Z}\).

### Solutions

**Solution 8.1.** On a connected component where \(E\ne0\), the graded module is locally a nonzero finite-rank free module over \(\mathcal O_S\). Its annihilator in \(\operatorname{Sym}T_S\) is exactly the ideal generated by \(T_S\), because every positive-degree symbol acts by zero and no nonzero function annihilates a free module. Thus the support is that component's zero section. If the rank vanishes on a component, the graded module there is zero and its support is empty. A zero complex also has empty support; a complex of connections has support on the components where some cohomology connection is nonzero. Passing to charts proves the stack containment. The constant object is nonzero on every component of \(Y\), so its support is the entire zero section, contained in \(\operatorname{Nilp}_G\).

**Solution 8.2.** Degree gives a locally constant map \(d:S\to\mathbb Z\). On each degree part form
\(M_0=M(-dx)\), \(N=M_0|_x\), and
\(M_{\mathrm{rig}}=M_0\otimes\pi_S^*N^{-1}\).
The rigidified bundle determines \(f:S\to J\). Reversing these operations gives (6.2), with a canonical isomorphism to the original \(M\). An isomorphism \(M\to M'\) induces the same \(f,d\) and an isomorphism \(N\to N'\). Conversely such an isomorphism of \(N\)'s induces one of \(M\)'s. For a fixed bundle its automorphism group is \(\mathbb G_m(S)\), since a global invertible function on \(X\times S\) is pulled back from \(S\); rigidification removes it from the \(J\)-factor and leaves it in \(B\mathbb G_m\). Thus the equivalence retains stabilizers and is functorial in \(S\). The entire Picard scheme already has a degree coordinate. Multiplying it by another \(\mathbb Z\) duplicates that coordinate instead of parameterizing line bundles once.

**Solution 8.3.** The free resolution of \(k\) over \(k[t]\) has generators \(1,\eta\), \(|\eta|=-1\), \(d\eta=t\). Tensor with \(k\) at \(t=0\) to get \(A\) with \(d\eta=0\) and \(\eta^2=0\); rename \(\eta=\epsilon\). The augmentation \(A\to k\) has the resolution (5.4). The differential sends \(e_n\) bijectively to the span of \(\epsilon e_{n-1}\) for \(n>0\), so only \(e_0\) survives. Its derived Hom into \(k\) has one generator in every even nonnegative degree, and the shift map on the resolution proves their products are \(u^n\). Hence \(k\) is not a finite-cell retract: otherwise that Hom would be bounded. The free module \(A\) is compact, while \(k\) is coherent with a nonzero \(H^0\) and no other cohomology. The heart is vector spaces, but (5.5) supplies morphisms absent from its ordinary derived category; coherence does not imply perfection over this derived algebra.

**Solution 8.4.** For a torus, every nonzero central Higgs field is non-nilpotent, so the nilpotent support condition is zero support. Formula (6.1) identifies its analytic components with
\(K(\mathbb Z^{2g},1)\times K(\mathbb Z,2)\).
Loop-chain descent gives precisely (7.1); the \(2g\) generators of \(R\) act as commuting invertible monodromies, and \(\epsilon\) records the higher stabilizer monodromy. For \(g=0\), \(R=E\), giving
\(\prod_d\operatorname{Mod}_{A_E}\).
For \(g>0\), choose one degree and the free module \(R\otimes A_E\) in it; this is compact and has infinite-dimensional fibre. It also provides an object excluded from the restricted category: its fibre contains \(1\), whose lattice orbit spans an infinite-dimensional regular representation. Ind-finite-dimensional local systems have locally finite lattice actions. The same obstruction already applies to \(R\) with augmentation action of \(A_E\). These examples change stalk size and monodromy, not the nilpotent support condition or the possibility of arbitrary degree families.

**Solution 8.5.** A compatible family on all finite subsets is uniquely the tuple of its restrictions to individual integers; morphisms are tuples too. This proves the restriction limit is \(\prod_d\operatorname{Vect}\). For the colimit, a compatible family of continuous functors from the finite-subset categories to any presentable stable category \(\mathcal E\) determines functors \(T_d:\operatorname{Vect}\to\mathcal E\). Their unique continuous extension to the product sends
\((N_d)\mapsto\bigoplus_dT_d(N_d)\).
It restricts to the prescribed finite-subset functors. This is the universal property of the presentable colimit, proving the same answer for it; the colimit contains (6.4).

A compact tuple has perfect components by testing one component. If its support were infinite, compactness applied to its finite truncations would factor its identity through one finite truncation, an impossibility on a nonzero outside component. Conversely a finite-support tuple of perfect complexes is compact because its Hom is a finite product of colimit-preserving Homs. The small category of these compact tuples contains only finite support; its ind-completion contains all tuples.

Taking \(\mathcal E=\operatorname{Vect}\) in the functor calculation yields (6.5) and computes the continuous dual. All component inclusions are open-and-closed, so \(j_!=j_*\), and the ordinary and co categories agree. For \(\operatorname{Bun}_G\), the dual still uses the co construction, with the specified \(j_*\) transitions; open boundaries need not make these equal to \(j_!\). The discrete example proves why the categorical colimit must admit infinite colimits and why compactness must be checked separately. It does not establish a counterexample to equivalence of the two categories.

## 9. Proof status and remaining geometric arguments

We proved the quasicompact-open restriction limit, the local half-operator gluing formula, the zero-support calculation for connections, the derived \(B\mathbb G_m\) algebra and its noncompact constant object, the Picard-stack splitting on families and arrows, its D-module factorization, the discrete duality calculation, and the full rank-one Betti nilpotent category. All five exercises have solutions.

We imported the D-module descent and base-change formalism, the Picard representability input already specified in Lesson 2, the Drinfeld–Gaitsgory compact-generation and co-duality theorems, the normalized square-root construction on \(\operatorname{Bun}_G\), the nilpotent regularity and suitable-open preservation theorems, Riemann–Hilbert, and the local tempered construction and its point independence. We did not prove the geometric truncatability estimates, Pfaffian construction, spectral projector, or derived Satake. Nor did we assert a positive-characteristic geometric Langlands equivalence.

The conditional formal compact-generation and co-duality proofs above do not prove their geometric hypotheses for the bundle stack. The following arguments remain required within this lesson's original scope:

1. **Truncatability for arbitrary connected reductive \(G\).** Prove the Harder–Narasimhan bounded opens are quasi-compact and cofinal; construct the relevant parabolic/Levi neighborhoods; prove the contraction principle for D-modules; prove the curve cohomology estimates for each root direction; and use the contraction to show the boundary is truncative. Only then apply §1.1. The finite-type local QCA compact-generation and duality proofs must be tracked too. Current GL-DMOD-17, Theorem 6.1, explicitly states this theorem without its proof.

2. **Normalized global half root.** Complete the family Pfaffian construction and normalized determinant comparison specified in §2.1. The free BD draft, §4.4.1, equation (209), states the semisimple result with a reference to its earlier Pfaffian construction and determinant comparison. Its subsequent normalization annotations must not be used to guess a corrected formula. Current GL-DMOD-15, §7, also cites this construction rather than proving it.

3. **Nilpotent regularity.** Prove the spectral action and the Beilinson projector, identify its image with the singular-support subcategory, and prove that this image is chartwise ind-regular holonomic. The definition \(\operatorname{SS}(M)\subset \operatorname{Nilp}\) and the flat-connection calculation do not imply regular singularities for a general nilpotent covector. An irregular rank-one connection on an affine line has zero characteristic variety, so even zero characteristic variety on a nonproper chart is insufficient by itself. For the torus on the proper Picard variety the elementary argument is valid: its nilpotent cone is zero, coherent zero-support modules are flat vector bundles by the existing Taylor proof, and the proper Picard variety itself is a compactification with empty boundary. The general descent and nonabelian theorem remain separate obligations. Current GL-PERV-11 constructs perverse descent; it does not prove nilpotent regularity.

4. **Preservation by suitable opens.** Prove a cofinal choice of opens on which each of the two extensions preserves nilpotent support. General extension across an arbitrary boundary can introduce conormal directions. Neither the restriction-limit proof nor §1.1 proves this support assertion.

5. **Tempered and anti-tempered statements actually used in §4.** Prove the derived spherical action, the quotient/full-subcategory realization, point independence, and the irregular-support criterion used to put the constant \(SL_2\) object in the anti-tempered category. GL-SAT-13 is only a plan and its sketch explicitly states derived Satake; only GL-SAT-01 currently exists in the inspected outbox. Ordinary geometric Satake would not by itself prove any of these derived statements.

6. **Riemann–Hilbert generality.** The existing GL-DMOD-14 proves its affine-line monodromic correspondence, but states the general algebraic regular-holonomic theorem. The stack ind-regular comparison in the present lesson therefore has no complete earlier proof from that provider. The one-dimensional quiver proof cannot be cited for every smooth affine chart.

These items remain active proof work. None is marked completed by these formal calculations. External references identify comparison sources; they do not replace the required programme proofs.

The source locators above are for the consulted versions. In addition to the inline references, the central rank-one comparison is AG §11.2, remark in “The case of a torus”; the large Betti definitions and torus calculation are Ben-Zvi–Nadler §§4.2–4.3. These older conjectural formulations are used for their category constructions, not presented as the current status of the theorem.

The [next lesson](hecke-functors-and-hecke-eigensheaves.md) constructs Hecke functors on these automorphic categories and formulates their coherent eigencondition. Local systems and their derived moduli will be developed later, before the spectral categories.
