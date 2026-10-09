# Sheaves and D-modules on Bun_G

*Working draft. Public domain (CC0).*

An automorphic category has to remember two kinds of geometry: how bundles vary, and how their automorphisms act. The second survives even when the space of isomorphism classes is a point. We will calculate this for \(B\mathbb G_m\), then use it to describe the entire rank-one automorphic category.

Sections 1.3–1.15 prove the truncatability, compact-generation and co-duality assertions used here. Sections 3.2–3.15 prove suitable-open nilpotent support preservation on the full unbounded category. Sections 3.16–3.19 prove finite chart-point detection under its exact support dimension bound and generation under a continuous conservative adjunction. Sections 3.20–3.22 prove the general-group nilpotent application, chartwise ind-holonomic cohomology, and stagewise detection of all unbounded objects and morphisms. Sections 3.23–3.25 prove the compatible Jordan and cocharacter construction, formal Levi normalization, local Hecke cotangent pairs and the positive moving-point residue. Section 3.26 proves bounded affine-Springer scheme isolation of the central Levi modification and its inverse, with all coefficient-ring tangent equations. Sections 3.27–3.29 prove the global Hecke cotangent relation, all-coefficient compatible-Higgs fibres and invariant transport, and the nonzero moving-point curve covector with bounded isolation in both directions. Nilpotent regularity, derived tempered Satake and the nilpotent microlocal support comparison retain the exact proof obligations listed in §9. Sections 3.55–3.58 prove the full complex chartwise ind-regular Riemann–Hilbert comparison and its half-twist transport.

Our standing assumptions are those of the [previous lesson](the-moduli-stack-of-bundles.md): \(X\) is a smooth projective connected curve over an algebraically closed field \(k\) of characteristic zero, and \(G\) is connected reductive. Write \(Y=\operatorname{Bun}_G(X)\). Complexes have cohomological grading; \(k[1]\) lies in degree \(-1\). A DG category here is a stable, presentable, \(k\)-linear category, and its tensor product is the tensor product of presentable categories. All limits and equivalences retain the complexes of morphisms and their homotopy coherences.

We use right D-modules and exceptional pullback \(f^!\) for descent on stacks. On a smooth scheme we can convert to left D-modules by tensoring with the inverse canonical line; we use left modules for characteristic varieties and the Weyl–Spencer calculations, with their density conversion and shifts retained. In comparisons with topology, \(k_Y\) denotes the constant object in the Riemann–Hilbert normalization. Thus on a complex smooth space of dimension \(d\), \(p_Y^!k\) corresponds to the dualizing complex \(k_Y[2d]\). Shifts do not affect singular support or compactness, but we retain the shift when calculating the fibre adjunction in §5.

The background is D-modules on smooth schemes, derived descent, and compact objects in a presentable category. The [D-module course](../../GL-DMOD/index.html) and [perverse-sheaf course](../../GL-PERV/index.html) supply the introductory material. For the full smooth-nerve construction we use the proved earlier lesson linked by title in §1.10. Sections 1.10–1.15 give the required unbounded transfer, quotient-category and finite-complement arguments. More general derived foundations outside this class retain their explicit boundaries in §9.

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

Sections 1.3–1.15 prove the following assertions, including their geometric and categorical hypotheses. The free [Drinfeld–Gaitsgory paper, Theorem 0.1.2 and Corollary 4.3.2, version 8](https://arxiv.org/abs/1112.2402v8), is further reading on these results. Under our assumptions, \(\operatorname{Dmod}(\operatorname{Bun}_G)\) is compactly generated. There is a cofinal system \(\mathcal U_{\mathrm{ct}}(Y)\) of quasicompact **co-truncative** opens; for them restriction has a continuous left adjoint \(j_!\). Define

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

The root blocks, cofinal opens and duality are proved in §§1.3–1.15. We compute (1.1)–(1.3) directly for a discrete stack in §6. In general, the transition functor matters: the same co-truncative system presents \(\operatorname{Dmod}(Y)\) by a colimit with \(j_!\), whereas its dual uses \(j_*\). The two extensions agree for open-and-closed components; they can differ at a boundary.

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

For an open exhaustion the conservativity needed here is already proved by the restriction-limit argument of Proposition 1.1. If \(l_i=j_{i!}\) exists on the full category, this proof gives the precise generators \(j_{i!}G_i\). This formal lemma by itself does not construct co-truncative opens or prove the finite-type and half-twist hypotheses. Sections 1.3–1.15 establish those hypotheses for the bounded presentations and full bundle stack needed here.

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

The open-and-closed example in §6 verifies these conditions for a discrete union. Sections 1.3–1.15 prove them at the Harder–Narasimhan boundaries of the full bundle stack.

### 1.3. Root chambers and the blocks of a bounded complement

We retain the curve and group assumptions of the lesson. Put
\[
 c=\max(0,2g-2).
 \tag{GT.1}
\]
The root calculations will explain this bound. They also explain why one must allow the Levi bundle to vary within a bounded open: a single unstable type is too small for the contraction argument in general.

Fix a maximal torus and a Borel. Write \(\alpha_1,\ldots,\alpha_\ell\) for the simple roots and \(h_i=\alpha_i^\vee\) for the simple coroots. Let \(V=X_*(T)\otimes_{\mathbb Z}\mathbb Q\). A dominant element \(\lambda\) satisfies \(\alpha_i(\lambda)\geq0\). For a subset \(I\) of the simple roots, use the order
\[
 \nu\leq_I\lambda
 \quad\Longleftrightarrow\quad
 \lambda-\nu=\sum_{i\in I}a_i h_i,\qquad a_i\in\mathbb Q_{\geq0}.
 \tag{GT.2}
\]
The order with every simple root is denoted \(\leq_G\). All these comparisons are made at a fixed central degree. Integral component classes, including torsion in the coroot quotient, remain separate labels as in [*The moduli stack of bundles*](the-moduli-stack-of-bundles.md), §§3.1–3.8 and 4.8.

We need one elementary positivity fact. The principal Cartan matrix \(C_I=(\alpha_i(h_j))_{i,j\in I}\) has positive diagonal, nonpositive off-diagonal entries, and a positive diagonal symmetrizer \(D_I\) for which \(D_IC_I\) is positive definite. These are the root-basis and invariant-form identities proved in [*Root systems and root data*](../../AG-RG/AG-RG-04.md), §§1–3. If \(C_Ix\geq0\) coordinatewise, then \(x\geq0\). Indeed write \(x=x^+-x^-\), with disjoint nonnegative parts. If \(x^-\ne0\), then
\[
 0\leq (x^-)^TD_IC_Ix
 \leq -(x^-)^TD_IC_Ix^-<0.
 \tag{GT.3}
\]
The middle inequality uses the nonpositive off-diagonal entries and the disjoint supports. This contradiction proves the assertion, and in particular proves that \(C_I^{-1}\) has nonnegative entries.

Let \(\operatorname{pr}_I\lambda\) be the unique element obtained from \(\lambda\) by subtracting an \(I\)-coroot combination and setting its \(I\)-root pairings to zero. Solving
\(C_Ia=(\alpha_i(\lambda))_{i\in I}\) and applying (GT.3) gives
\[
 \operatorname{pr}_I\lambda\leq_I\lambda,\qquad
 \alpha_j(\operatorname{pr}_I\lambda)\geq\alpha_j(\lambda)
 \quad(j\notin I).
 \tag{GT.4}
\]
The second assertion follows because \(\alpha_j(h_i)\leq0\) when \(j\ne i\). More generally, if \(\nu\leq_I\lambda\), the same calculation gives \(\alpha_j(\nu)\geq\alpha_j(\lambda)\) for \(j\notin I\). Thus an \(I\)-dominant \(\nu\leq_I\lambda\), with \(\lambda\) dominant for \(G\), is dominant for \(G\) as well.

Take a dominant cutoff \(\theta\) with \(\alpha_i(\theta)\geq c\) for every \(i\). For a type \(\lambda\not\leq_G\theta\), define
\[
 I_\lambda=\{i:\alpha_i(\lambda)\leq c\},\qquad
 S_\lambda=\{\nu\text{ dominant}:\nu\leq_{I_\lambda}\lambda\}.
 \tag{GT.5}
\]
This set has fixed projection \(\operatorname{pr}_{I_\lambda}\lambda\), is downward closed for the \(I_\lambda\)-order, and satisfies
\[
 \alpha_j(\nu)\geq\alpha_j(\lambda)>c
 \quad(\nu\in S_\lambda,\ j\notin I_\lambda).
 \tag{GT.6}
\]
It is therefore an admissible set for the parabolic with Levi roots \(I_\lambda\).

Every type in \(S_\lambda\) lies outside the cutoff. Here is the required separation proof. Suppose that \(\nu\in S_\lambda\) and \(\nu\leq_G\theta\). Then \(\theta-\lambda=\sum_j b_jh_j\), with \(b_j\geq0\) for \(j\notin I_\lambda\). For \(i\in I_\lambda\), the cutoff inequalities give \(\alpha_i(\theta-\lambda)\geq0\). Put \(v=\sum_{i\in I_\lambda}b_i h_i\). The off-diagonal Cartan signs imply \(\alpha_i(v)\geq0\) for \(i\in I_\lambda\). Apply (GT.3) to its coefficients. All \(b_i\) are nonnegative. Hence \(\lambda\leq_G\theta\), a contradiction. We have proved
\[
 S_\lambda\cap\{\nu:\nu\leq_G\theta\}=\varnothing.
 \tag{GT.7}
\]
This is a statement in every root system, with the central direction unchanged.

For a fixed \(I\), the set \(\{\nu\text{ dominant}:\nu\leq_I\lambda\}\) is bounded. Write \(\nu=\lambda-\sum_{i\in I}a_i h_i\). Then \(a_i\geq0\) and \(C_Ia\leq(\alpha_i(\lambda))_{i\in I}\); applying \(C_I^{-1}\) bounds every \(a_i\). The possible Harder–Narasimhan types in such a set are finite. One way to see the denominator bound is to use the fixed faithful representation from the previous lesson: its slopes have integral numerators and ranks bounded by its fixed dimension; its finitely many weights recover the rational cocharacter by a fixed rational linear system. Bounded coordinates therefore leave only finitely many types. The integral Levi labels over a rational degree have only the finite torsion ambiguity described in that lesson.

The previous lesson, §§4.8–4.10, proves that Harder–Narasimhan types are locally finite in coefficient families and that bounded loci have finite-type framed atlases. It also proves specialization in the coroot order. Consequently a downward-closed set at fixed Levi degree gives an open bounded locus in \(\operatorname{Bun}_M\). For the sets used in (GT.5), their \(G\)-locus is locally closed directly: with \(\mu=\operatorname{pr}_{I_\lambda}\lambda\), one has \(S_\lambda=\{\nu:\mu\leq_G\nu\leq_G\lambda\}\). Indeed \(\lambda-\mu\) has only \(I_\lambda\)-coroot coefficients, so the two nonnegative differences through any element of this interval can have no other coefficients. The downward bound is open and the upward bound is closed. To verify this from specialization, restrict to a bounded chart: only finitely many locally closed strata occur, so the closure of their union is the union of their closures; every specialized type is higher in the coroot order. Thus an upward-closed union is closed, and its complement is open. We use the reduced structure on the resulting locally closed locus. Denote the two loci by \(B_M(S)\) and \(Z_G(S)\), respectively. Their integral degree labels are retained. The parabolic construction below applies to these finite admissible intervals.

### 1.4. The root cohomology estimates, including families

Let \(P\) be the standard parabolic with Levi \(M\) and simple-root set \(I\). Write \(U^+\) for its unipotent radical, \(P^-\) for the opposite parabolic, and \(U^-\) for the radical of \(P^-\). Let \(F_M\) be a Levi bundle of dominant \(G\)-type \(\nu\), with
\[
 \alpha_j(\nu)>c\qquad(j\notin I).
 \tag{GT.8}
\]
We claim
\[
 H^1(X,\mathfrak u^+_{F_M})=0,\qquad
 H^0(X,(\mathfrak g/\mathfrak p)_{F_M})=0.
 \tag{GT.9}
\]
The bundle \(F_M\) itself need not be semistable.

Use its canonical Harder–Narasimhan reduction inside \(M\), proved in the previous lesson, §§4.4–4.8. Its Levi \(M_\nu\) has simple roots on which \(\nu\) vanishes. Filtering an associated representation by this reduction gives semistable \(M_\nu\)-modules with slopes equal to their central weights paired with \(\nu\). This representation statement was proved there using tensor semistability and the reductive tensor generators; it does not presume that an arbitrary faithful sum is semistable.

Each weight of \(\mathfrak u^+\) is a positive root \(\beta=\sum_i n_i\alpha_i\) with \(n_j>0\) for some \(j\notin I\). Every \(n_i\) is a nonnegative integer. Thus
\[
 \beta(\nu)\geq n_j\alpha_j(\nu)>c\geq2g-2.
 \tag{GT.10}
\]
Weights in one \(M_\nu\)-central summand differ by roots pairing to zero with \(\nu\), so that whole summand has this slope. A semistable bundle of slope greater than \(2g-2\) has zero \(H^1\): duality identifies that group with the dual of \(\operatorname{Hom}(E,\omega_X)\), and the slope comparison proved in the previous lesson makes this Hom zero. An exact-sequence induction through the filtration proves the first equality of (GT.9). The weights of \(\mathfrak g/\mathfrak p\) are the negatives of those roots. Their semistable graded summands have negative slope, and hence zero \(H^0\). The same induction proves the second equality.

The assertion also holds for each central vector-group quotient in either radical. In characteristic zero an invariant decomposition of the root representation splits these quotients as \(M\)-representations; alternatively their weights and the same \(M_\nu\) filtration give the identical argument. Thus every positive quotient has zero \(H^1\), and every negative quotient has zero \(H^0\).

These are coefficient-family assertions. On a noetherian affine parameter scheme, the universal finite projective cohomology complex from the previous lesson, §§1.1 and 4.1, computes these bundles with every coefficient module. When the degree-zero cohomology vanishes on every geometric fibre, its differential is fibrewise injective, hence a split injection locally; the cokernel is finite projective. When degree-one cohomology vanishes, the differential is a split surjection and its kernel is finite projective. Both conclusions survive arbitrary tensor products. Consequently
\[
 R\Gamma(E^-)\simeq H^1(E^-)[-1],\qquad
 R\Gamma(E^+)\simeq H^0(E^+)
 \tag{GT.11}
\]
for every negative and positive quotient under consideration, and the two displayed cohomology modules are finite projective with arbitrary base change. Their ranks are determined by the Euler characteristic already proved in the previous lesson. A finite-presentation model and pullback give the assertion over every ordinary coefficient algebra. This proves more than vanishings at closed bundles.

### 1.5. Unipotent torsors and the opposite-parabolic affine map

Choose an integral central cocharacter \(\gamma:\mathbb G_m\to Z(M)\), with zero pairing on \(I\) and positive pairing on its complement. To construct it, solve the Cartan equations with values zero on \(I\) and one off \(I\), using the inverse-matrix positivity proved in §1.3, and clear denominators. Its pairing with every positive root outside \(M\) is positive.

Filter \(U^-\) by these positive degrees for the action
\[
 \rho_t(u)=\gamma(t)^{-1}u\gamma(t).
 \tag{GT.12}
\]
Thus a negative root \(-\beta\) has degree \(\beta(\gamma)>0\). The filtration is finite, is preserved by \(M\), and satisfies \([U_{\geq a},U_{\geq b}]\subset U_{\geq a+b}\). The quotients are vector groups. The polynomial exponential and group law for these nilpotent root groups were proved in the previous lesson, §6.8; their finite formulas have rational coefficients and hence hold over every coefficient algebra. This also constructs the filtration and its central quotients over those algebras.

Fix a family \(F_M\) satisfying (GT.8). Passing through the central quotients constructs the stack of twisted \(U^-\)-torsors on the curve. At a quotient \(E^-\), obstruction to lifting is in \(H^2(E^-)\), which is zero on the curve with arbitrary coefficient modules. Two lifts differ by \(H^1(E^-)\), and their relative automorphisms are \(H^0(E^-)=0\). These assertions can be checked directly in a two-affine cover of the curve: vector torsors on either affine are trivial; their transition is a section on the intersection, modulo the two changes of frame. The resulting two-term Čech complex computes \(H^0\) and \(H^1\) and has no \(H^2\). The central group-extension identities make precisely this additive lifting calculation at every successive quotient.

By (GT.11), \(H^1(E^-)\) is a finite projective parameter module. The stack at each stage is therefore a torsor under its vector bundle, with no relative inertia. Such a torsor is an affine smooth scheme over the preceding stage: after a faithfully flat local trivialization it is affine space; affine-algebra and smoothness descent were proved in the previous lesson, §§7.1–7.9. The maps between trivializations are affine translations, so they glue the same scheme and retain every base change. Iterating proves that
\[
 q^-:\operatorname{Bun}_{P^-}\times_{\operatorname{Bun}_M}B_M(S)
       \longrightarrow B_M(S)
 \tag{GT.13}
\]
is schematic, affine, smooth and of finite presentation. Its split-bundle section is a closed immersion, because an affine morphism is separated. This conclusion includes arbitrary test rings and all torsor isomorphisms.

For \(U^+\), each quotient has \(H^1(E^+)=0\). The same central lifting calculation says that every torsor is locally the split torsor, and its automorphism group is a successive extension of the vector bundles \(H^0(E^+)\). They are finite projective by (GT.11). The group is smooth affine, with the polynomial group law retained from the finite filtration. Consequently the split section gives a smooth surjection
\[
 B_M(S)\longrightarrow
 \operatorname{Bun}_{P}\times_{\operatorname{Bun}_M}B_M(S).
 \tag{GT.14}
\]
Its fibres are the isomorphism torsors under this automorphism group. Thus (GT.14) is a statement about families and their inertia, not a claim that the positive-radical group has no sections.

### 1.6. The parabolic block inside the bundle stack

Take an admissible \(S\) with all outside root pairings greater than \(c\). The map
\[
 p:\operatorname{Bun}_{P}\times_{\operatorname{Bun}_M}B_M(S)
       \longrightarrow Z_G(S)
 \tag{GT.15}
\]
is an isomorphism. We give the properness and coefficient argument that a pointwise canonical reduction alone would omit.

First work over a field. The Harder–Narasimhan parabolic of a Levi bundle of type \(\nu\in S\) has simple roots where \(\nu\) vanishes. By (GT.8) those roots lie in \(I\). Its inverse image in \(P\) is the canonical \(G\)-parabolic: its finer Levi is semistable and every outside slope is positive. The uniqueness proved in the previous lesson therefore makes (GT.15) bijective on geometric points and on their stabilizers. Conversely the canonical \(G\)-reduction extends to \(P\), giving the Levi bundle of type \(\nu\). The rational projection and integral Levi degree are retained in both directions.

To prove properness, use the finite relative projective flag Quot scheme of the previous lesson, §§1.2 and 4.8. Choose finitely many highest-weight Plücker lines for \(G/P\), using integral multiples of the fundamental weights off \(I\); such multiples are characters of the actual group and give the closed flag embedding proved in [*Automorphisms, forms and parabolic subgroups*](../../AG-RG/AG-RG-06.md), §§1–2. Their degrees depend only on the fixed projection of \(S\), so they are fixed in this Quot problem.

A specialization in this projective Quot scheme can initially give nonsaturated lines. Saturating them on the smooth curve increases their degrees by their effective torsion defects. The maximal possible degree of each highest-weight line is its pairing with the canonical type, by the slope and flag bounds of the previous lesson. At every target in \(Z_G(S)\), this maximal value is exactly its fixed projection value. Thus no positive defect is possible for any of the defining Plücker lines. They remain subbundles. Their closed incidence and tensor equations persist under specialization, so they give an actual \(P\)-reduction.

Here is the required bound on its Levi type \(\nu'\), before knowing that \(\nu'\) is \(G\)-dominant. Refine the Levi reduction by its canonical \(M\)-parabolic and lift that parabolic to \(P\). For a dominant highest weight \(\eta\) of an actual \(G\)-representation, take the highest-weight representation of this finer Levi inside the representation. Its weights differ from \(\eta\) only by roots on which \(\nu'\) is zero. The associated subbundle is semistable, by the reductive representation argument of the previous lesson, and its slope is \(\eta(\nu')\). The largest slope of the ambient \(G\)-bundle representation is \(\eta(\nu)\). Hence \(\eta(\nu')\leq\eta(\nu)\). Integral multiples of all fundamental weights, together with central characters and their negatives, test the coroot cone, so \(\nu'\leq_G\nu\). Its projection is unchanged; thus the difference is an \(I\)-coroot combination and \(\nu'\leq_I\nu\). For a simple root outside \(I\), the off-diagonal Cartan signs give \(\alpha_j(\nu')\geq\alpha_j(\nu)>c\). Within \(I\), \(\nu'\) is dominant by its definition as the Levi type. It is therefore \(G\)-dominant. Downward closure makes \(\nu'\in S\). This proves the valuative closedness of the selected reduction locus inside that projective flag Quot, and hence properness of (GT.15).

The relative tangent space of the reduction map is \(H^0(X,(\mathfrak g/\mathfrak p)_{F_P})\). The \(P\)-root filtration of this bundle has the associated \(M\)-graded bundle from (GT.9), so its \(H^0\) is zero. The cohomology argument of §1.4 retains this vanishing with arbitrary square-zero coefficient modules. Thus the represented proper reduction map is unramified. Its geometric fibres contain one point, so it is universally injective; a proper unramified universally injective map is a closed immersion. Properness and finite fibres first make it finite by the projective affine-neighbourhood argument of the previous lesson, §4.7. Over a strictly henselian local target, its finite unramified fibre is reduced, and the unique point makes that fibre exactly the residue field. The finite algebra modulo the target submodule generated by \(1\) therefore has zero residue module. Nakayama makes this quotient zero. Hence the target algebra surjects onto the finite algebra. These quotients descend and give the closed immersion.

The target \(Z_G(S)\) has its reduced locally closed structure. A closed immersion onto all of its geometric points has defining ideal contained in its nilradical, hence zero. This proves (GT.15) as an isomorphism of stacks. Its subsequent pullbacks retain all nilpotent coefficient rings. The reduced structure defines the block; arbitrary coefficient families are then maps to that block, not a separate reduced-point construction.

There is also a smooth map from the opposite-parabolic space of (GT.13) to \(\operatorname{Bun}_G\). The obstruction module for this reduction map is \(H^1(X,(\mathfrak g/\mathfrak p^-)_{F_{P^-}})\). Its root filtration has the positive bundle \(\mathfrak u^+_{F_M}\) as its associated graded. Equations (GT.9)–(GT.11) make that obstruction zero for every coefficient module. The map is of finite presentation by the reduction section scheme of the previous lesson, §1.5. Its square-zero lifting calculation therefore proves that it is smooth, with no appeal solely to a pointwise dimension count.

Finally, the map
\[
 B_M(S)\longrightarrow
 \bigl(\operatorname{Bun}_{P}\times_{\operatorname{Bun}_M}B_M(S)\bigr)
       \times_{\operatorname{Bun}_G}
 \bigl(\operatorname{Bun}_{P^-}\times_{\operatorname{Bun}_M}B_M(S)\bigr)
 \tag{GT.16}
\]
is an open immersion. An opposite pair of flags has stabilizer \(M=P\cap P^-\), including its schematic stabilizer. In cocharacter weight coordinates one parabolic preserves the upper weight filtration and the other the lower filtration; their intersection preserves every weight summand and is the Levi. The tangent map
\(\mathfrak g/\mathfrak m\to\mathfrak g/\mathfrak p\oplus\mathfrak g/\mathfrak p^-\)
is an isomorphism. The resulting monomorphism \(G/M\to G/P\times G/P^-\) is therefore étale and hence an open immersion; the all-ring homogeneous quotient \(G/M\) was constructed in the previous lesson, §4.7. A section of the product flag bundle has values in this open orbit exactly when its flags are opposite everywhere on \(X\). The locus in the parameter scheme where this holds is open: its complement is the proper image of the closed nonopposite locus on the curve. This proves (GT.16) on the entire parameter scheme.

### 1.7. The actual contraction chart

In the cocharacter grading of §1.5, formula (GT.12) multiplies every negative root coordinate by \(t^{\beta(\gamma)}\), a positive integer power. The finite polynomial group law is graded, so this defines a group endomorphism also for nonunits \(t\), over every coefficient ring. At \(t=0\) it kills \(U^-\) and retains \(M\). Applying these group endomorphisms to torsors gives an action of the multiplicative monoid \(\mathbb A^1\) on the space \(W\) in (GT.13), over \(B_M(S)\), with
\[
 \rho_0=i^-q^-,\qquad
 i^-:B_M(S)\hookrightarrow W.
 \tag{GT.17}
\]
For \(t\) invertible, the action is inner conjugation. Multiplication by \(\gamma(t)\) gives a natural isomorphism between the transformed torsor and the original one. The identity \(\gamma(ts)=\gamma(t)\gamma(s)\) proves coherence of these isomorphisms. Thus the \(\mathbb G_m\)-action is trivial as an action on the absolute stack. Its trivialization acts by the central automorphism \(\gamma(t)\) on the Levi bundle, and is not a trivialization over \(\operatorname{Bun}_M\).

Here is a precise way to pass to scheme contraction charts. Form
\[
 \overline W=W/\mathbb G_m,\qquad
 \overline B=B_M(S)/\mathbb G_m
             =B_M(S)\times B\mathbb G_m.
 \tag{GT.18}
\]
The relative monoid action gives an affine morphism \(\overline W\to\overline B\). The absolute coherent trivialization identifies \(\overline W\) with \(W\times B\mathbb G_m\). Let \(\psi:\overline W\to W\) be its projection and \(\varphi:W\to\overline W\) the quotient atlas. Then \(\psi\varphi\simeq\operatorname{id}_W\), and both maps are smooth and surjective.

The closed substack \(\overline B\) is \(\psi^{-1}(B_M(S))\). Indeed pull both closed substacks back along the faithfully flat atlas \(\varphi\): the first becomes the split section by the relative quotient square, and the second becomes that same section by \(\psi\varphi\simeq\operatorname{id}\). Faithfully flat descent of their ideal sheaves makes the equality valid before pullback. In particular \(\overline B\to B_M(S)\) is smooth and surjective.

Choose a smooth affine chart \(T\to B_M(S)\). Pulling the affine relative action back to \(T\) gives an affine scheme \(W_T\), a section \(T\hookrightarrow W_T\), and a nonnegative grading of its coordinate algebra, with degree-zero part \(\mathcal O_T\). The quotient diagram
\[
 T/\mathbb G_m\hookrightarrow W_T/\mathbb G_m
 \tag{GT.19}
\]
maps smoothly to \(\overline B\hookrightarrow\overline W\) and then to \(B_M(S)\hookrightarrow W\). Its inverse-image square is Cartesian. Combining it with (GT.14)–(GT.16) gives a diagram from (GT.19) to
\[
 Z_G(S)\hookrightarrow\operatorname{Bun}_G
 \tag{GT.20}
\]
whose vertical maps are smooth, the left one is surjective, and the map from the top closed substack to the inverse image of the bottom block is an open immersion. These are the geometric contraction-chart conditions. Their construction has been proved on coefficient families and all arrows.

Sections 1.10–1.14 prove that (GT.19) is truncative and transfer its compactness property to (GT.20). The proof uses the actual strong equivariant category, the full Levi-base coefficient representation and the unipotent-gerbe section. The monoid action on a scheme by itself would not supply this result: the quotient by \(\mathbb G_m\) and its derived equivariance are essential.

### 1.8. A rank-two chamber and its extension spaces

For \(G=SL_3\), write a cocharacter as \(a h_1+b h_2\). Its standard diagonal coordinates are \((a,-a+b,-b)\), and its simple-root pairings are
\[
 r_1=2a-b,\qquad r_2=-a+2b,\qquad
 a=(2r_1+r_2)/3,\quad b=(r_1+2r_2)/3.
 \tag{GT.21}
\]
Take \(g=2\), so \(c=2\), and take \(\theta=(a,b)=(2,2)\). The dominant cutoff consists of
\(a,b\leq2\), \(b\leq2a\), and \(a\leq2b\).
For \(\lambda=(3,5)\), the simple-root pairings are \((1,7)\). Thus \(I_\lambda=\{1\}\), and the admissible segment is
\[
 (a,b)=(3-u,5),\quad 0\leq u\leq\tfrac12;\qquad
 (r_1,r_2)=(1-2u,7+u).
 \tag{GT.22}
\]
It joins \(\lambda\) to its Levi projection \((5/2,5)\). The entire segment lies outside the cutoff because its \(b\)-coordinate is \(5\). This is the separation argument (GT.7) in exact coordinates.

The corresponding parabolic preserves a two-dimensional subspace. Choose line bundles \(L_3,L_2\) of degrees \(3,2\), and put \(L_{-5}=(L_3\otimes L_2)^{-1}\). The split Levi bundle is
\(E_M=(L_3\oplus L_2)\oplus L_{-5}\), with determinant one. The positive-radical bundle is
\(\operatorname{Hom}(L_{-5},L_3\oplus L_2)\), whose two line degrees are \(8,7\); its dual is the negative-radical bundle. Since the radicals of this maximal parabolic are abelian, their torsor calculations are already the vector calculations. Duality and Euler characteristic give
\[
 H^1(E^+)=0,\quad \dim H^0(E^+)=13,\qquad
 H^0(E^-)=0,\quad \dim H^1(E^-)=17.
 \tag{GT.23}
\]
For example the negative line degrees contribute \(9\) and \(8\) to \(H^1\). The degree-one difference between \(L_3\) and \(L_2\) is allowed inside the Levi block; the estimate concerns the two roots outside that Levi.

Choose \(\gamma(t)=\operatorname{diag}(t,t,t^{-2})\). Both negative-radical coordinates in (GT.12) have weight \(3\). Thus the fibre of the affine map \(q^-\) at this fixed Levi bundle is the actual extension space
\[
 H^1(E^-)\simeq\mathbb A^{17},\qquad
 v\longmapsto t^3v.
 \tag{GT.24}
\]
It contracts to the split extension. The positive split section is smooth with relative automorphism dimension \(13\). The opposite map to \(\operatorname{Bun}_{SL_3}\), over the full Levi open, is smooth of relative dimension \(13\). The frozen fibre \(\mathbb A^{17}\) alone is not asserted to be a smooth atlas of that bundle stack: the Levi family in (GT.19) is retained.

![Exact root chamber, opposite-parabolic extension space and weighted Cartan normal complex](figures/truncatability-root-chamber.svg)

**Figure 1.** The chamber panel uses exact coroot coefficients. The red numerical admissible segment has fixed outside coefficient \(b=5\), so it misses the green cutoff \(a,b\leq2\), even though its Levi root gap is small. For the rank-two Levi bundle of degree five in this example, its actual HN types in this segment are the two endpoints: the rank-one slopes \(3,2\), and the semistable rank-two slope \(5/2\). The upper right panel shows the algebraic zero map in the stated \(17\)-dimensional extension fibre, with the full Levi-base maps and dimensions from (GT.21)–(GT.24). The lower lattice is the separate two-variable Cartan calculation of §1.11: positivity selects three derivative monomials, each retaining its free exterior-algebra operator; it is not a plot of the \(17\)-dimensional fibre. Over a Levi base their full coefficient representation is retained by (RV.2)–(RV.3). Proof locators are (GT.5)–(GT.7), (GT.21)–(GT.24), (CW.6)–(CW.9) and (RV.2)–(RV.3). Free human-source reading for the root-chart construction is Drinfeld–Gaitsgory, [*Compact generation of the category of D-modules on the stack of G-bundles on a curve*](https://arxiv.org/pdf/1112.2402v8), §§9–11; for the Cartan-complex formalism, Pandžić, [*A simple proof of Bernstein–Lunts equivalence*](https://arxiv.org/pdf/math/0401105), §1. The proofs used here are given in the text and the earlier programme lessons named above.

**Exercise 1.A.** Prove the separation (GT.7) for a nonsimply laced root system. Which positivity assertion must replace a picture?

**Solution 1.A.** Its principal Cartan matrix need not be symmetric. Multiply by its positive diagonal symmetrizer. Its off-diagonal entries stay nonpositive and its quadratic form is positive definite. Splitting a coefficient vector into disjoint positive and negative parts gives exactly (GT.3). Applying this to the \(I_\lambda\)-coefficients of \(\theta-\lambda\) proves they are nonnegative. The other coefficients were already nonnegative, so \(\lambda\leq_G\theta\), the required contradiction. The proof uses neither equality of root lengths nor a planar diagram.

**Exercise 1.B.** In the \(SL_3\) example compute the projection endpoint, both root degrees, the two extension dimensions and the contraction weights. Explain why the small Levi gap does not spoil (GT.23).

**Solution 1.B.** Setting \(r_1=1-2u=0\) gives \(u=1/2\), hence endpoint \((5/2,5)\). The outside positive root degrees are \(r_2=7\) and \(r_1+r_2=8\). Their \(H^0\) dimensions in genus two are \(7-1=6\) and \(8-1=7\), while their duals have \(H^1\) dimensions \(7+1=8\) and \(8+1=9\). These give \(13\) and \(17\). Conjugation by \(\gamma(t)^{-1}\) multiplies either lower-left entry by \(t^3\). The root of the Levi has degree one, but it is not a weight of either radical. The estimate follows from the outside roots, whose degrees exceed \(2g-2=2\).

### 1.9. A cofinal quasicompact exhaustion

For a dominant rational \(\theta\), at its fixed central degree define
\[
 U_\theta=\{P:\operatorname{HN}(P)\leq_G\theta\}.
 \tag{GT.25}
\]
Retain an integral component label if desired. The preceding specialization argument makes this locus open. It is quasicompact by the faithful framed atlas of the previous lesson. Here is how its numerical hypotheses are verified. For a dominant highest weight \(\eta\), a canonical reduction filters its representation bundle into semistable central-weight pieces, and its largest slope is \(\eta(\operatorname{HN}(P))\). Since \(\eta(h_i)\geq0\), (GT.25) bounds this slope by \(\eta(\theta)\). Apply the same statement to the dual representation to bound the smallest slope below. A fixed faithful sum therefore has uniformly bounded extremal slopes and fixed rank and degree in each of the finitely many integral components over this central degree. The finite-type Quot atlas and affine reduction section scheme in the previous lesson, §§1.1–1.6 and 4.10, apply. Its smooth image is all of \(U_\theta\), proving quasicompactness.

These opens are cofinal among quasicompact opens of \(\operatorname{Bun}_G\) after finite unions over central degrees. A quasicompact open meets only finitely many components of the discrete component group, and its finite-type charts have only finitely many Harder–Narasimhan types. For each central degree, choose one dominant rational \(\theta\) above all those types and satisfying
\[
 \alpha_i(\theta)\geq c\quad\text{for every simple root }i.
 \tag{GT.26}
\]
Such a \(\theta\) exists: solve \(C a=\mathbf1\) on each semisimple factor. Positivity of \(C^{-1}\) gives a strictly dominant element \(\zeta=\sum_i a_i h_i\) with every \(\alpha_i(\zeta)=1\). In an irreducible factor every \(a_i>0\), since otherwise the nonpositive off-diagonal entries in that row could not sum to \(1\). Add a sufficiently large positive multiple of \(\zeta\) to the fixed central element. Its coroot coefficients dominate the finitely many types, and its root pairings satisfy (GT.26). This proves the cofinality in every genus.

For two such cutoffs at one central degree with \(\theta\leq_G\theta'\), only finitely many types occur in
\[
 U_{\theta'}\setminus U_\theta.
 \tag{GT.27}
\]
Each type \(\lambda\) in this difference lies in a block \(Z_G(S_\lambda)\) constructed in §§1.3–1.7. By (GT.7), that block avoids \(U_\theta\). Its intersection with \(U_{\theta'}\) has the same contraction charts, as follows. Restrict the Levi open to types \(\nu\leq_G\theta'\), and pull the affine map \(q^-\) back to this smaller open. Every opposite extension over it maps into \(U_{\theta'}\): the monoid family (GT.17) has constant bundle type away from zero and type \(\nu\) at zero, so the proved specialization inequality bounds its original type above by \(\nu\). The restricted affine map retains its monoid action and split section. Equations (GT.14)–(GT.16) retain smoothness, surjectivity and the open inverse-image condition. Thus the bounded complement is covered by finitely many blocks whose geometric contraction conditions have been proved. This supplies the geometric input for the finite-recollement D-module argument; it does not assume that truncativity of one stratum follows merely from its slope.

If \(G\) is a torus, the root set is empty. The component theorem and boundedness result of the previous lesson give quasicompact open-and-closed degree components. Finite unions of them are the required cofinal opens. For a general reductive group the central directions and the finite torsion labels are carried by the finite unions above. The positive and negative root estimates use only the derived root system; no central adjoint direction is assigned a spurious positive weight.

**Exercise 1.C.** Why can a root cutoff at one central degree not exhaust \(\operatorname{Bun}_{\mathbb G_m}\)? How does the cofinality proof correct this for every reductive group?

**Solution 1.C.** There are no roots, so the root inequalities say nothing about the integral degree of a line bundle. A cutoff at one central degree sees only that degree component. A quasicompact open meets finitely many open-and-closed components, so their finite union contains it. For a reductive group first retain its finitely many component labels, then choose a sufficiently dominant semisimple cutoff at each of their central degrees. The finite union contains the original open and is quasicompact. Torsion in the component group changes the component label, not the rational root inequalities.

### 1.10. Smooth pullback and the unipotent-gerbe section

We now work in the full unbounded derived category. A compact object is an object whose mapping-complex functor commutes with filtered colimits. All limits of categories and mapping complexes below are homotopy limits. Our scheme convention is that a smooth map of relative dimension \(r\) has \(f^!=f^\natural[r]\), where \(f^\natural\) is ordinary flat pullback of left D-modules. Strong smooth descent, including its higher maps, is proved in [*D-modules on stacks, ind-schemes and the de Rham prestack*](../../GL-DMOD/src/stacks-ind-schemes-and-the-de-rham-prestack.md), §§1–2. We use that descent construction, rather than the derived category of the ordinary equivariant heart.

**Smooth transfer lemma.** For a schematic quasicompact smooth map \(f:Y'\to Y\) between smooth stacks with affine diagonal, of constant relative dimension \(r\), there is an adjunction
\[
 f^!\dashv f_{\mathrm{dR},*}[-2r].
 \tag{CC.1}
\]
The functor on the right preserves colimits. Consequently \(f^!\) preserves compact objects. Locally constant relative dimensions are handled on the finitely many open and closed pieces of a quasicompact source.

We give the transfer calculation and its unbounded justification. On an affine product chart \(Y'=Y\times\mathbb A^r\), put \(B=\mathcal D_Y\otimes_k\mathcal D_{\mathbb A^r}\). The \((B,\mathcal D_Y)\)-bimodule for \(f^\natural\) is \(\mathcal O_{\mathbb A^r}\otimes_k\mathcal D_Y\). It has the finite free relative Spencer resolution: in degree \(-j\) its term is \(B\otimes\bigwedge^j k^r\), and the differential uses right multiplication by the commuting vertical derivatives. Exactness follows from the regular sequence of their symbols in the order-associated graded ring, followed by induction on order. Applying Hom gives the relative de Rham cochain complex in degrees \(0,\ldots,r\). Differential-operator direct image is this complex shifted by \([r]\). Tensor–Hom adjunction thus gives
\[
 \operatorname{RHom}_{Y'}(f^\natural M[-r],N)
 \simeq
 \operatorname{RHom}_{Y}(M,f_{\mathrm{dR},*}N).
 \tag{CC.2}
\]
Replacing \(M\) by \(M[2r]\) proves (CC.1). Smooth étale coordinates give the same relative Spencer resolution with its intrinsic exterior-power and bracket differential. Its chain-rule transition maps identify the displayed adjunctions on overlaps.

For a nonaffine source over an affine target, a finite affine cover and its intersection cover compute the direct image of each quasi-coherent Spencer term. The affine-diagonal hypothesis makes these intersections affine; it need not make the diagonal a closed immersion. The finite Čech complex and the finite Spencer complex use only finite sums, cones and shifts. They therefore commute with arbitrary colimits, and have a cohomological bound independent of the input complex. No boundedness of \(M\) or \(N\) is needed: a semifree resolution of \(M\) proves (CC.2) first on free cells, then on their sums and realizations; the finite Spencer calculation computes the other variable on an arbitrary complex. We have not replaced an infinite product totalization by a direct sum.

On a smooth chart of the target stack, schematicity makes the base change of \(f\) a scheme map. The relative Spencer and Čech construction just given defines the direct image on that chart. The smooth base-change comparisons are the chain-rule comparisons of these same transfer complexes. They identify their units and counits and commute with composition. Strong descent therefore glues the functors, the unit and the counit, and their triangle identities. Their chartwise colimit compatibility proves colimit compatibility on the stack, since chart pullback is conservative and preserves colimits. Finally (CC.1) gives, for a compact \(F\),
\[
 \operatorname{RHom}_{Y'}(f^!F,\mathop{\mathrm{colim}}_a N_a)
 \simeq
 \mathop{\mathrm{colim}}_a
 \operatorname{RHom}_{Y'}(f^!F,N_a).
 \tag{CC.3}
\]
This proves compact preservation by this smooth pullback. It does not assert that arbitrary smooth pullback reflects compactness.

**Unipotent-gerbe lemma.** Let \(S\) be a smooth stack and \(N\to S\) a smooth group scheme whose underlying scheme is a finite-rank vector bundle, with the zero section as its identity. For the neutral gerbe \(q:B_SN\to S\) and its section \(s:S\to B_SN\), there are mutually inverse equivalences
\[
 q^!: \mathrm{Dmod}(S)\ \simeq\ \mathrm{Dmod}(B_SN):s^!.
 \tag{CC.4}
\]
The statement concerns the full derived descent category and arbitrary coefficient complexes.

First let \(v:E\to S\) be a vector bundle of rank \(n\). In a local vector-bundle trivialization, its relative de Rham complex decomposes by total polynomial degree, counting a fibre differential as degree one. Contraction with the fibre Euler field \(e\) satisfies
\[
 d_{E/S}\iota_e+\iota_e d_{E/S}=m\,\operatorname{id}
 \quad\text{on total degree }m.
 \tag{CC.5}
\]
For \(m>0\), division by \(m\) gives a contraction. Total degree zero is exactly \(\mathcal O_S\) in degree zero. Euler contraction is intrinsic under linear changes of fibre coordinates, so these calculations glue. The augmentation from \(\mathcal O_S\) is a quasi-isomorphism to the pushed-forward relative de Rham complex. Together with (CC.2) and the projection formula, this gives
\[
 \operatorname{RHom}_{E}(v^!A,v^!B)
 \simeq\operatorname{RHom}_{S}(A,B).
 \tag{CC.6}
\]
For clarity about shifts, \(v_{\mathrm{dR},*}v^!B\simeq B[2n]\), and the right adjoint of \(v^!\) is \(v_{\mathrm{dR},*}[-2n]\). Their composite is the identity. Formula (CC.6) would have the wrong shift if ordinary flat pullback were used in place of the smooth de Rham normalization. The relative complex is finite in exterior degree and the contraction is coefficientwise, so the argument also holds for unbounded \(A,B\).

The Čech nerve of the section \(s\) has level \(p\) equal to \(N^p_S\); all its face and degeneracy maps are over \(S\). Its structural map \(v_p:N^p_S\to S\) is a vector-bundle map as a morphism of schemes, independently of whether the group law of \(N\) is commutative. By (CC.6), \(v_p^!\) is fully faithful. Every cartesian descent object on this nerve has its level \(p\) identified with \(v_p^!\) of its level-zero object, by pulling along a vertex. The same observation holds for maps and all higher homotopies. We may therefore restrict every level to this fully faithful image. Under \(v_p^!\), all transition functors become the identity on \(\mathrm{Dmod}(S)\), with the coherent identifications supplied by composition of !-pullbacks. The homotopy limit of this constant diagram over the contractible simplex category is \(\mathrm{Dmod}(S)\). This proves both essential surjectivity and full faithfulness of (CC.4). The identity \(q\circ s=\operatorname{id}\) identifies its two inverse functors. This proof takes a limit of the full nerve; it does not truncate the nerve to the ordinary equivariant heart.

Apply this to \(Z=Z_G(S)\), with the notation \(S\) for the admissible set distinguished from its Levi stack \(B_M(S)\). Equations (GT.9)–(GT.14) show that every positive unipotent torsor is locally trivial and that its automorphism group on a fixed Levi bundle is \(N=H^0(X,U^+_{F_M})\). The finite characteristic-zero exponential and logarithm of the preceding lesson identify the underlying scheme of \(U^+_{F_M}\) with \(\mathfrak u^+_{F_M}\). These polynomial maps commute with taking sections over the curve. By (GT.11), their section scheme is the vector bundle \(H^0(X,\mathfrak u^+_{F_M})\), with arbitrary base change. Thus \(\operatorname{Bun}_P^S\to B_M(S)\) is the neutral gerbe \(B_{B_M(S)}N\). Using the isomorphism (GT.15), the split-bundle map
\[
 f_Z:B_M(S)\longrightarrow Z_G(S)
 \quad\text{has }\quad
 f_Z^!: \mathrm{Dmod}(Z_G(S))\simeq\mathrm{Dmod}(B_M(S)).
 \tag{CC.7}
\]
In particular its pullback preserves and reflects compact objects. This conclusion uses the unipotent-gerbe structure, not smooth surjectivity alone.

**Transfer to the root block.** Let \(f_Y:W\to Y\) be the opposite-parabolic smooth map of §1.6, restricted to a bounded ambient open \(Y\), and let \(i_S:B_M(S)\hookrightarrow W\) be the split section. Its composite is the block inclusion \(i_Z:Z_G(S)\hookrightarrow Y\) after \(f_Z\). Suppose that the contraction calculation proves that \(i_S^!\) preserves compact objects. For any compact \(F\in\mathrm{Dmod}(Y)\), (CC.3) makes \(f_Y^!F\) compact. Functoriality of !-pullback gives
\[
 f_Z^!i_Z^!F\simeq i_S^!f_Y^!F.
 \tag{CC.8}
\]
The right side is compact by the stated hypothesis; (CC.7) reflects compactness, so \(i_Z^!F\) is compact. This is the exact descent argument needed for the root blocks. The remaining hypothesis is a statement about the full derived category on \(W\); an attracting monoid on its scheme atlas alone would not prove it.

**Exercise 1.D.** Explain why smooth surjectivity cannot replace (CC.7). Use the smooth atlas \(\mathrm{pt}\to B\mathbb G_m\).

**Solution 1.D.** The point-quotient calculation in [*D-modules on stacks, ind-schemes and the de Rham prestack*](../../GL-DMOD/src/stacks-ind-schemes-and-the-de-rham-prestack.md), §5, identifies the category on \(B\mathbb G_m\) with modules over \(A=\Lambda(\epsilon)\), \(|\epsilon|=-1\). The constant object corresponds, up to the fixed normalization shift, to the augmentation module \(k\). Its atlas pullback is a one-dimensional perfect complex. Nevertheless the resolution \(\bigoplus_{j\geq0}Ae_j\), \(|e_j|=-2j\), \(de_j=\epsilon e_{j-1}\), gives \(\operatorname{Ext}^*_A(k,k)=k[c]\) with \(|c|=2\). A finite cell \(A\)-module has bounded self-Hom; so does a retract of one. The unbounded polynomial self-Ext proves that \(k\) is not compact. Thus this smooth atlas pulls a noncompact object to a compact object. In (CC.7), the vector-bundle de Rham contraction makes pullback an equivalence, which is the additional reason compactness can be reflected there.

### 1.11. The weighted Weyl calculation

The following algebraic calculation isolates what the derived multiplicative-group direction does at the contracted point. It includes the degree-minus-one operator; replacing its module category by the ordinary equivariant heart would lose the compact objects that the calculation produces.

Let \(D_r\) be the Weyl algebra on \(x_1,\ldots,x_r,\partial_1,\ldots,\partial_r\), with \([\partial_i,x_j]=\delta_{ij}\). Fix positive integers \(n_1,\ldots,n_r\), put \(\deg x_i=n_i\), \(\deg\partial_i=-n_i\), and set
\[
 E=\sum_i n_i x_i\partial_i,\qquad N=\sum_i n_i.
 \tag{CW.1}
\]
A Cartan complex in this calculation is a complex of graded left \(D_r\)-modules, with a grading-preserving \(D_r\)-linear operator \(\epsilon\) of cohomological degree \(-1\), satisfying
\[
 \epsilon^2=0,\qquad d\epsilon+\epsilon d=Q,
 \qquad Q(v)=mv-Ev\quad(v\text{ of grading }m).
 \tag{CW.2}
\]
The operator \(Q\) is \(D_r\)-linear: \([E,a]=(\deg a)a\) for a homogeneous Weyl operator \(a\). Morphisms respect the grading and \(\epsilon\), and quasi-isomorphisms are detected on the underlying complex. Denote the resulting derived category by \(\mathcal C_r\).

For \(m\in\mathbb Z\), let \(P_m\) be a free graded Weyl module with generator of grading \(m\). Its free Cartan extension \(F_m\) has terms \(P_m\epsilon\) in degree \(-1\) and \(P_m\) in degree zero, with
\[
 d(a\epsilon)=a(m-E),\qquad
 \epsilon(a)=a\epsilon,\qquad \epsilon(a\epsilon)=0.
 \tag{CW.3}
\]
Here \(a(m-E)\) means right multiplication in the free Weyl module. Its grading-difference operator is precisely \(m-R_E\), so (CW.2) holds in both degrees.

A morphism from \(F_m\) to a Cartan complex is determined by the image of its generator. The image of the degree-minus-one generator is then forced by \(\epsilon\), and (CW.2) supplies its differential. This gives, with the usual graded signs,
\[
 \operatorname{RHom}_{\mathcal C_r}(F_m,M)\simeq M_m.
 \tag{CW.4}
\]
The ordinary mapping complex already computes the derived one here: for an acyclic \(M\), each grading summand \(M_m\) is acyclic. Thus \(F_m\) is projective for quasi-isomorphisms, and (CW.4) proves its compactness. The family \((F_m)_{m\in\mathbb Z}\) detects zero objects, so it generates \(\mathcal C_r\).

We also need the finite cell consequence, rather than just detection. Attach sums of shifted \(F_m\)'s to represent all homogeneous cohomology classes of an object, and then attach cells to kill the cohomology of the mapping cone. Repeating this gives a semifree complex mapping by a quasi-isomorphism to that object: every cone class is killed at the next stage, and filtered colimits of complexes of vector spaces are exact. Each cell boundary involves finitely many earlier cells, since a map from a free cell is specified by one element of a direct sum. At any fixed stage its full set of boundary ancestors is finite. The semifree complex is therefore the filtered colimit of its finite subcomplexes closed under cell boundaries. If the object is compact, its identity factors through one such finite cell complex. It is a retract of that complex. Conversely finite cells and their retracts are compact by (CW.4). We have proved the compact-object description used below.

For \(r=0\), (CW.2) reads \(d\epsilon+\epsilon d=m\) in grading \(m\). A nonzero grading has the contraction \(\epsilon/m\), hence is acyclic. Grading zero is the category of modules over
\[
 A=\Lambda(\epsilon),\qquad |\epsilon|=-1,\qquad d\epsilon=0.
 \tag{CW.5}
\]
Thus \(\mathcal C_0\simeq A\text{-}\mathrm{mod}\). This is also the point-quotient category proved in §5 of [*D-modules on stacks, ind-schemes and the de Rham prestack*](../../GL-DMOD/src/stacks-ind-schemes-and-the-de-rham-prestack.md).

We now construct the normal Koszul functor, including its Cartan operator. The delta module is
\(\Delta=D_r/\sum_iD_rx_i\), with generator of grading \(-N\). Its grading operator equals the action of \(E\): on the generator, \(E=-N\), and each derivative lowers both operators by \(n_i\). Give \(\Delta\) the zero \(\epsilon\)-operator. Resolve it by the finite free Koszul complex \(K_\Delta\) on right multiplication by the \(x_i\). A wedge basis \(e_J\) lies in degree \(-|J|\) and has generator grading \(-N+\sum_{j\in J}n_j\). Write
\[
 d_K(ae_J)=\sum_i a x_i\,\iota_i(e_J),\qquad
 \epsilon_K(ae_J)=-\sum_i n_i a\partial_i\,e_i\wedge e_J.
 \tag{CW.6}
\]
The exterior signs give \(\epsilon_K^2=0\). Using
\(\iota_i(e_j\wedge -)+e_j\wedge\iota_i=\delta_{ij}\) and
\(\partial_jx_i-x_i\partial_j=\delta_{ij}\), we obtain
\[
 (d_K\epsilon_K+\epsilon_Kd_K)(ae_J)
 =a\left(-E-N+\sum_{j\in J}n_j\right)e_J.
 \tag{CW.7}
\]
This is exactly \(Q\) on that free summand. Thus the Koszul resolution itself is a Cartan complex, and its augmentation to \(\Delta\) respects \(\epsilon\). Its exactness follows directly from PBW: it is the Koszul resolution of the right-coordinate generators in the free left Weyl module, or from their regular symbols followed by induction on order.

For \(M\in\mathcal C_r\), use the full graded Hom complex
\(\operatorname{Hom}_{D_r}(K_\Delta,M)\), with operator
\(\epsilon(f)=\epsilon_Mf-(-1)^{|f|}f\epsilon_K\). The two Weyl-moment terms cancel because \(f\) is \(D_r\)-linear. The remaining commutator with its differential is the grading operator on Hom. Hence it is an object of \(\mathcal C_0\). Taking its grading-zero summand gives a functor \(T:\mathcal C_r\to A\text{-}\mathrm{mod}\). The finite free Koszul resolution makes this functor exact, colimit preserving, and invariant under quasi-isomorphisms, even on unbounded complexes.

Compute \(T(F_m)\). The Koszul cochain complex of left multiplication by the \(x_i\) on a free Weyl module has cohomology only in degree \(r\). Its quotient there is
\(D_r/\sum_i x_iD_r\), which has PBW basis \(\partial_1^{q_1}\cdots\partial_r^{q_r}\), \(q_i\geq0\). Notice the side of the ideal: this quotient uses \(x_iD_r\), whereas \(\Delta\) uses \(D_rx_i\). In the quotient, right multiplication by \(E\) has eigenvalue \(\sum_i n_iq_i\), since
\(\partial^q x_i\partial_i\equiv q_i\partial^q\) modulo \(\sum_jx_jD_r\). The top Koszul source generator has grading zero. Thus Hom grading zero selects precisely
\[
 Q_m=\left\{q\in\mathbb Z_{\geq0}^r: \sum_i n_iq_i=m\right\}.
 \tag{CW.8}
\]
On these basis elements the differential from (CW.3) is zero. The operator induced by \(\epsilon_M\) remains the free degree-minus-one operator. The precomposition term involving \(\epsilon_K\) lowers Koszul cochain degree, so vanishes in the top cohomology projection. That projection respects both the differential and \(\epsilon\); it is a quasi-isomorphism because the Koszul complex has only this cohomology. Consequently
\[
 T(F_m)\simeq\bigoplus_{q\in Q_m} A[-r].
 \tag{CW.9}
\]
Positivity of every \(n_i\) makes \(Q_m\) finite, and it is empty if \(m<0\). Formula (CW.9) and the finite cell description therefore prove that \(T\) preserves all compact objects of \(\mathcal C_r\). The answer is a finite sum of **free** \(A\)-modules. Replacing it by two copies of the augmentation in consecutive degrees would erase its \(\epsilon\)-action and give an incorrect compactness conclusion.

For the frozen \(17\)-dimensional extension fibre in §1.8, all weights are \(3\). Here \(Q_m\) is empty unless \(m=3d\) for an integer \(d\geq0\), and then
\[
 |Q_{3d}|=\binom{d+16}{16}.
 \tag{CW.10}
\]
Indeed the tuple \(q\) is a decomposition of \(d\) into \(17\) nonnegative parts: insert \(16\) separators among \(d\) marks, giving the displayed binomial coefficient. In particular \(T(F_0)=A[-17]\), \(T(F_3)=A^{\oplus17}[-17]\), and \(T(F_{-3})=0\). The grading-zero functor has retained finitely many derivative monomials in each of these cases.

The corresponding ordinary scheme calculation, without the group grading and Cartan operator, retains the entire polynomial space \(k[\partial_1,\ldots,\partial_r][-r]\) when applied to the free Weyl module. For \(r>0\) this is an infinite-dimensional complex on a point and is not compact. This explains the categorical distinction in §1.7. Sections 1.12–1.14 identify (CW.9) with the strong smooth-descent normal functor and carry the full Levi-base equivariance through the calculation; the fibre calculation alone is not the complete root-block argument.

The algebraic calculation also supplies its own contraction adjunction. Define
\[
 \Pi^!_{\mathrm{alg}}(L)=k[x_1,\ldots,x_r]\otimes_k L[r]
 \quad\text{from }A\text{-}\mathrm{mod}\text{ to }\mathcal C_r.
 \tag{CW.11}
\]
The variables have their stated gradings, the Weyl operators act on the polynomial factor, and the point-module factor has grading zero. The shifted differential is \((-1)^r d_L\) and the shifted Cartan operator is \((-1)^r\epsilon_L\). Both obey (CW.2), since the grading and Euler operators agree on polynomials. This functor preserves colimits.

For each \(m\), pair the finite derivative space indexed by \(Q_m\) with polynomials of weighted degree \(m\) by
\[
 \langle\partial^q,x^p\rangle
   =\left.\partial^q x^p\right|_{x=0}
   =q_1!\cdots q_r!\,\delta_{q,p}.
 \tag{CW.12}
\]
This is a perfect pairing in characteristic zero. Right multiplication by \(x_i\) on the derivative quotient lowers \(q_i\) with coefficient \(q_i\); it is adjoint to multiplication by \(x_i\) on polynomials. Right multiplication by \(\partial_i\) raises \(q_i\); it is adjoint to differentiation of polynomials. Thus (CW.12) respects every Weyl operator and its compositions.

Using (CW.4) and (CW.9), the pairing gives
\[
 \operatorname{RHom}_A(TF_m,L)
   \simeq\operatorname{RHom}_{\mathcal C_r}
                 (F_m,\Pi^!_{\mathrm{alg}}L),
 \qquad T\dashv\Pi^!_{\mathrm{alg}}.
 \tag{CW.13}
\]
Here is why the first isomorphisms give the entire adjunction. A derived morphism between free Cartan cells is represented in (CW.4) by a homogeneous Weyl element, or by such an element times its degree-minus-one free generator. The first kind respects (CW.12) by the coordinate and derivative checks just given. For the second kind, precomposition acts by \((-1)^j\epsilon_L\) on a degree-\(j\) mapping complex. The shift in (CW.11) contributes \((-1)^r\); the identification of a Hom out of a degree-\(r\) normal generator with the shifted coefficient complex contributes \((-1)^{rj}\). These are exactly the graded tensor–Hom signs, so this second kind also respects the isomorphism. The differential is right multiplication by \(m-E\), already respected by the pairing. Hence the isomorphisms are natural on the full DG subcategory of the free cells, not merely on their degree-zero maps. Extending along their sums, cones and semifree realizations gives the isomorphism for every object. Both sides convert colimits in that object into limits of mapping complexes; the cell-generation proof above therefore gives the full unbounded adjunction.

Its counit \(T\Pi^!_{\mathrm{alg}}L\to L\) is an isomorphism. The coordinate Koszul complex on polynomials has only its top cohomology, the evaluation quotient at zero. Its degree \(r\) cancels the shift \([r]\) in (CW.11). Under that top-cochain identification, both the coefficient differential and \(\epsilon\) have the factor \((-1)^r\); multiplying a degree-\(j\) coefficient by \((-1)^{rj}\) identifies them with the differential and operator of \(L\). This also identifies the counit with evaluation. Thus the algebraic proof supplies the adjunction and the normalization as well as compactness. The next sections supply the geometric comparison and full Levi-base extension used in (GT.20).

**Exercise 1.E.** Take \(r=2\), weights \((1,2)\), and \(m=4\). Determine \(T(F_4)\), and explain what changes if the second weight is zero.

**Solution 1.E.** The nonnegative solutions of \(q_1+2q_2=4\) are \((4,0),(2,1),(0,2)\). Thus \(T(F_4)=A^{\oplus3}[-2]\), including each free \(\epsilon\)-action. If the second weight is zero, the solutions are \((4,q_2)\) for all \(q_2\geq0\). The same PBW calculation then gives an infinite sum of shifted free \(A\)-modules, which is not compact: its identity does not factor through any finite subsum. Strict positivity is exactly the hypothesis that prevents this failure.

### 1.12. Strong equivariance and the Spencer comparison

Let a smooth affine algebraic group \(H\) act on a smooth quasicompact scheme \(Z\) with affine diagonal. Write \(\mathfrak h=\operatorname{Lie}H\) and \(\sigma:\mathfrak h\to\Theta_Z\) for the infinitesimal action. A weakly equivariant D-complex has a rational \(H\)-action compatible with the differential operators. Its infinitesimal action \(\nu_\xi\) need not be their moment action. For left modules the moment is \(\sigma(\xi)\); for right modules it is \(-R_{\sigma(\xi)}\). In either convention their difference \(Q_\xi\) is D-linear. A Cartan D-complex additionally has D-linear operators \(\epsilon_\xi\) of degree \(-1\), equivariant in \(\xi\), with
\[
 [d,\epsilon_\xi]=Q_\xi,\qquad
 \epsilon_\xi\epsilon_\zeta+\epsilon_\zeta\epsilon_\xi=0,
 \qquad [Q_\xi,\epsilon_\zeta]=\epsilon_{[\xi,\zeta]}.
 \tag{SC.1}
\]
The last relation follows as well by differentiating \(H\)-equivariance and using D-linearity. Quasi-isomorphisms are detected on the underlying D-complex.

**Comparison theorem.** The DG localization of Cartan D-complexes on \(Z\) is the full strong descent category
\[
 \mathrm{Dmod}([Z/H]).
 \tag{SC.2}
\]
The comparison holds on unbounded complexes and on mapping complexes. It is compatible with commuting group actions, equivariant smooth pullback and closed transfer. We prove the comparison using the de Rham differential algebra with its Spencer weak equivalences. It does not require the ring of operators to be projective over \(U(\mathfrak h)\).

We normalize its underlying atlas complex as \(q^!M[-\dim H]\), where \(q:Z\to[Z/H]\) is the smooth atlas. This is the normalized pullback of the earlier smooth-descent theorem. The raw right Spencer form model below carries its ordinary chart-dimension shifts; these are adjusted to this normalization in the comparison. For an equivariant map with the same group on both charts, the group shift is the same on source and target. The Cartesian atlas square and !-base change therefore identify its geometric pullback with scheme !-pullback on the Cartan complexes. In particular a smooth scheme map of relative dimension \(r\) uses \([r]\), not unshifted form pullback. This normalization is retained in (SC.11).

First describe the equivariant differential-form model. The graded algebra of forms on \(H\) is \(\mathcal O_H\otimes\bigwedge\mathfrak h^*\), using invariant forms. Its multiplication pullback is the coproduct of the group object \(H_\Omega=(H,\Omega_H^\bullet)\). Its infinitesimal DG Lie algebra has the two copies of \(\mathfrak h\), in degrees zero and minus one:
\[
 d\iota_\xi=L_\xi,\quad
 [L_\xi,L_\zeta]=L_{[\xi,\zeta]},\quad
 [L_\xi,\iota_\zeta]=\iota_{[\xi,\zeta]},\quad
 [\iota_\xi,\iota_\zeta]=0.
 \tag{SC.3}
\]
An \(H_\Omega\)-equivariant \(\Omega_Z\)-complex is a rational \(H\)-equivariant complex \(F\) with operators \(\iota_\xi\) satisfying
\[
 [d_F,\iota_\xi]=\nu_\xi,
 \qquad
 \iota_\xi(\alpha f)
   =\iota_{\sigma(\xi)}(\alpha)f
       +(-1)^{|\alpha|}\alpha\iota_\xi(f).
 \tag{SC.4}
\]
Its odd operators anticommute and transform by the adjoint action. These conditions are exactly the groupoid descent equations. Indeed an isomorphism between action pullback and projection pullback on \(H\times Z\) has, in exterior degree zero, the rational \(H\)-action. In invariant-form coordinates its coefficients of degree one are the contractions. Multiplication in two independent sets of odd variables makes the contractions anticommute and determines every higher coefficient by their products. The finite exterior exponential, together with the rational action, reconstructs the isomorphism. The group product identifies these coefficients by the adjoint transformation; its unit and associative product give all the groupoid coherences. Finally differentiating the isomorphism gives (SC.4); the invariant-form equation \(d\theta=-\tfrac12[\theta,\theta]\) gives the brackets in (SC.3). Conversely those equations make the reconstructed isomorphism commute with the differential and group product. The construction is polynomial in the odd variables and uses the actual rational group action, so it holds on the group scheme, not just on its points.

The smooth-descent reconstruction proved in [*D-modules on stacks, ind-schemes and the de Rham prestack*](../../GL-DMOD/src/stacks-ind-schemes-and-the-de-rham-prestack.md), §§1–2, now identifies the localization of these global equivariant form complexes with the category defined by the full action nerve. The weak equivalences in this assertion are the Spencer D-cohomology equivalences defined below. Recall the precise unbounded part of that reconstruction: after a faithfully flat covering pullback, inserting the distinguished vertex contracts the augmented Čech complex; hence its unit and counit induce isomorphisms on D-module cohomology before pullback. For normalized bounded-below truncations the nerve calculation computes the reconstruction. For an unbounded D-complex, take their compatible homotopy limit on each affine chart. Complexes of modules are complete for this truncation limit, and the covering contraction respects the truncations. Mapping complexes are limits with the same coherent maps. This gives the unbounded comparison, including its products; it is not a replacement of an infinite totalization by a direct sum. Under (SC.4), it is precisely the global form-complex construction appearing in that earlier proof.

We next prove the equivariant Spencer equivalence explicitly. Use right modules for its formulas and set
\[
 R_Z=\Omega_Z^\bullet\otimes_{\mathcal O_Z}\mathcal D_Z,
 \quad
 d_R(\alpha\otimes a)
   =d\alpha\otimes a+
       \sum_i dx_i\wedge\alpha\otimes\partial_i a
 \tag{SC.5}
\]
in étale coordinates. The chain rule makes this an intrinsic \((\Omega_Z,\mathcal D_Z)\)-bimodule. The expression is the de Rham differential of the left regular operator module; its right operator action commutes with that differential. Let \(\iota^R_\xi\) contract the form factor by \(\sigma(\xi)\). Cartan's coordinate identity gives
\[
 [d_R,\iota^R_\xi]=\nu^R_\xi+R_{\sigma(\xi)}.
 \tag{SC.6}
\]
For example, for a coordinate vector field the commutator acts by left multiplication by its derivative, whereas the rational infinitesimal action on the operator factor is its adjoint action. Their difference is right multiplication. The same computation for a general vector field includes its action on forms and yields (SC.6). Thus \(R_Z\) is itself a right Cartan complex for the group action.

Define the adjoint DG functors
\[
 \mathsf D(F)=F\otimes_{\Omega_Z}R_Z,
 \qquad
 \mathsf\Omega(M)=
       \mathcal Hom_{\mathcal D_Z}(R_Z,M).
 \tag{SC.7}
\]
The tensor carries the diagonal contraction. On its representatives \(f\otimes a\), with \(a\) in degree-zero forms, the contraction is just \(\iota_\xi f\otimes a\). The Leibniz term in (SC.4) and contraction on \(R_Z\) make this formula well defined on the balanced tensor. Its commutator with the differential is the rational infinitesimal action plus right multiplication by \(\sigma(\xi)\), exactly \(Q_\xi\) for a right module. It is D-linear. On Hom the contraction is
\[
 \iota_\xi(f)=\epsilon^M_\xi f
          -(-1)^{|f|}f\iota^R_\xi.
 \tag{SC.8}
\]
Here the moment terms cancel by right D-linearity of \(f\), leaving its rational infinitesimal action. Precomposition with the form action supplies the Leibniz rule in (SC.4). Anticommutation and group equivariance follow on both functors from their diagonal tensor and Hom formulas. Thus (SC.7) are adjoint between the two equivariant DG categories, with equivariant evaluation and coevaluation maps.

The counit \(\mathsf D\mathsf\Omega(M)\to M\) is a quasi-isomorphism for every unbounded complex \(M\). We verify this without a convergence assumption on its cohomology. Locally its terms have the form
\(M^a\otimes\bigwedge^b\Theta_Z\otimes\mathcal D_Z\), in degree \(a-b\). Filter by exterior degree plus operator order, using the submodules
\[
 V_j^i=\sum_{a-b=i,\ b+c\leq j}
       M^a\otimes\bigwedge^b\Theta_Z
                         \otimes\mathcal D_Z^{\leq c}.
 \tag{SC.9}
\]
These are increasing subcomplexes. The piece \(V_0\) maps identically to \(M\). The associated graded in positive total degree \(j\) is its coefficient complex tensored with the homogeneous Koszul strand
\[
 \bigoplus_{b=0}^{\min(j,\dim Z)}
   \bigwedge^b\Theta_Z\otimes
          \operatorname{Sym}^{j-b}\Theta_Z,
 \qquad d=\sum_i p_i\iota_i.
 \tag{SC.10}
\]
The homotopy \(h=\sum_i e_i\wedge\partial/\partial p_i\) satisfies \(dh+hd=j\). Division by \(j\) contracts the strand. This is invariant under linear coordinate changes, and the tensor-complex signs make the contraction anticommute with the coefficient differential. Thus it works for an arbitrary coefficient complex, even without O-flatness or a cohomological bound. Each \(V_j/V_0\) is acyclic by finite induction on its filtration. The filtration is exhaustive and filtered colimits of quasi-coherent modules are exact, so its union proves the counit assertion. The PBW filtration and its homotopy are natural under \(H\); the quasi-isomorphism is the equivariant counit itself.

Declare a map of form complexes to be a D-equivalence when \(\mathsf D\) sends it to a quasi-isomorphism. The unit \(F\to\mathsf\Omega\mathsf D F\) is a D-equivalence by the counit just proved and the adjunction triangle identity. The Hom functor in (SC.7) preserves ordinary quasi-isomorphisms locally: its exterior degree is finite and its operator-module terms are locally finite free. Consequently both functors descend to the DG localizations. Their unit and counit are equivalences there, so they are inverse equivalences of DG categories, including all mapping complexes. Together with the preceding strong form-complex descent, this proves (SC.2).

Tensoring a right module by \(\omega_Z^{-1}\) converts to the left convention. The rational action on the canonical line cancels the divergence term in the right moment action, so \(Q_\xi\) becomes \(\nu_\xi-\sigma(\xi)\). This recovers exactly (CW.2) for the weighted multiplicative-group action. Every construction above is natural for group-scheme products and their commuting actions. Pullback and closed transfer use the same Spencer bimodules, with their tensor–Hom contraction operators, so the comparison respects these functors and their shifts.

In particular let \(i:B\mathbb G_m\hookrightarrow[\mathbb A^r/\mathbb G_m]\) be the zero section for the positive weights of §1.11, and let \(\pi\) be the projection to \(B\mathbb G_m\). The comparison identifies the two categories with \(\mathcal C_0\) and \(\mathcal C_r\), and
\[
 i^!\longleftrightarrow T,
 \qquad \pi^!\longleftrightarrow\Pi^!_{\mathrm{alg}},
 \qquad i^!\dashv\pi^!.
 \tag{SC.11}
\]
To check the first identification on the full derived category, closed pushforward of a point module \(L\) is \(\Delta\otimes L\). Its density gives the delta generator weight \(-N\). Resolve \(\Delta\) by the Cartan Koszul resolution (CW.6). For the free point module \(A\), a projective Cartan resolution of \(\Delta\otimes A\) is obtained by freely adjoining the odd operator to that weak Koszul complex. Its differential is \(d_K+Q_K\partial_\tau\) and its odd operator is multiplication by \(\tau\). Conjugating by \(1+\epsilon_K\partial_\tau\) changes these into \(d_K\) and \(\epsilon_K+\tau\): the identities are \([d_K,\epsilon_K]=Q_K\), \(\partial_\tau^2=0\), and \(\partial_\tau\tau+\tau\partial_\tau=1\). Augmentation then maps to \(\Delta\otimes A\) by a quasi-isomorphism. The free-extension adjunction computes Hom out of this resolution as the grading-zero complex \(\mathcal Hom_{D_r}(K_\Delta,M)\), with induced odd operator \(\epsilon_Mf-(-1)^{|f|}f\epsilon_K\). That is the functor \(T\). Resolving an arbitrary \(A\)-module by free cells proves the full closed adjunction and the identification of \(i^!\). Smooth pullback to affine space is polynomial pullback shifted by \([r]\), with the same shift on the odd operator, giving the second identification. Formula (CW.13) now proves the geometric adjunction in (SC.11). Since \(\pi^!\) is continuous, \(i^!\) preserves compact objects. The zero substack is therefore truncative.

Free human-source reading for this comparison is Beilinson–Drinfeld, [*Quantization of Hitchin's integrable system and Hecke eigensheaves*](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), §§7.2.1–7.2.9 and 7.6.3–7.6.11. The formulas and the unbounded filtration proof needed here have been given above; the full smooth-descent reconstruction is the proved earlier programme result explicitly linked in this section.

**Exercise 1.F.** Explain why replacing D-equivalences of form complexes by their ordinary cohomology equivalences would change this construction. Where does the proof keep unbounded coefficients under control?

**Solution 1.F.** Over affine space the ordinary de Rham algebra has only the field as its cohomology. Its ordinary derived DG-module category therefore cannot retain the Weyl module category. A form complex here is tested after the Spencer functor \(\mathsf D\); the unit is inverted by that test, not by a declaration about ordinary de Rham cohomology. The counit proof tensors an explicitly contractible, finite-exterior Koszul strand with each arbitrary coefficient complex. It then uses finite induction and an exact filtered colimit. It never asks a spectral sequence of an unbounded coefficient complex to converge. The separate smooth-nerve comparison uses the earlier chartwise truncation limits with their products.

### 1.13. Compact generators and duality on the bounded presentations

The bounded framed presentations needed here have frame group \(GL_a\), possibly with extra multiplicative groups for line frames. We prove the categorical assertions for these presentations; the group whose bundles are parametrized remains any connected reductive \(G\).

We first prove the representation fact used in the argument. Every finite-dimensional rational \(GL_a\)-representation in characteristic zero is semisimple. Here is an algebraic proof with the needed exactness consequence. On \(V^{\otimes b}\), \(V=k^a\), the image of the symmetric-group algebra is semisimple: averaging by \(1/b!\) splits every subrepresentation. Its commutant is therefore a product of matrix algebras. Under
\(\operatorname{End}(V^{\otimes b})=\operatorname{End}(V)^{\otimes b}\), that commutant is the space of symmetric tensors. Polarization in characteristic zero shows that it is spanned by \(A^{\otimes b}\) for matrices \(A\). Invertible matrices suffice, since any linear functional vanishing on their powers is a polynomial vanishing on the dense open \(GL_a\). Consequently
\[
 \operatorname{span}\{g^{\otimes b}:g\in GL_a\}
     =\operatorname{End}_{k[S_b]}(V^{\otimes b}).
 \tag{AF.1}
\]
The action algebra is semisimple, so \(V^{\otimes b}\) is a semisimple \(GL_a\)-module.

For an arbitrary finite rational representation, multiply its matrix coefficients by a sufficiently large determinant power to make them polynomial. Decompose by the scalar-centre weights. Each resulting coefficient space is homogeneous of some nonnegative degree \(b\). The coaction embeds the representation in finitely many copies of the degree-\(b\) polynomial functions on matrices; evaluation at the identity makes this embedding injective. Such polynomial functions are a direct summand of the tensor powers of finitely many standard or dual-standard copies, by the symmetrizing projector. They are semisimple by (AF.1). Untwisting the determinant proves the assertion. Additional multiplicative groups are handled by their integer-weight decompositions. Thus finite rational representations of
\(H=GL_a\times\mathbb G_m^s\) are semisimple.

Every vector in an arbitrary rational representation belongs to a finite-dimensional subrepresentation. An invariant vector in a quotient therefore lifts through a finite semisimple subrepresentation of the source: choose a lift, take its finite orbit span, and split the resulting surjection onto its image. Invariants are exact. For a finite representation \(W\), \(\operatorname{Hom}_H(W,-)\) is consequently exact and commutes with filtered colimits. The latter follows also directly from its finitely many coefficient equations. A nonzero rational representation has a nonzero map from a finite one, so these Hom functors detect zero.

Let \(Z\) now be smooth and quasiaffine, with an \(H\)-action. The finite affine Čech calculation makes \(R\Gamma(Z,-)\) on quasi-coherent complexes continuous and of finite cohomological dimension. It is conservative. Indeed embed \(Z\) as an open in an affine scheme \(C\), as in the definition of quasiaffineness. The quasi-coherent derived open direct image is fully faithful, and restriction of that direct image recovers the original complex. On the affine scheme, derived global sections are conservative. Hence \(R\Gamma(Z,M)=0\) implies \(M=0\), also for an unbounded complex. The ambient affine scheme need not be smooth for this argument about quasi-coherent complexes.

In the weakly equivariant derived D-module category define
\(P_E=\mathcal D_Z\otimes_{\mathcal O_Z}E\) for an \(H\)-linearized finite-rank vector bundle \(E\). The PBW filtration makes operator induction O-flat. Induction–forgetful adjunction and the finite affine-cover calculation therefore give
\[
 \operatorname{RHom}_{\mathrm{weak},H}(P_E,M)
   =R\Gamma(Z,E^*\otimes_{\mathcal O_Z}M)^H.
 \tag{AF.2}
\]
This is a derived assertion: induction is exact, and its right adjoint preserves injectives; the right side uses derived sheaf global sections. Exact rational invariants then compute equivariant Hom. Equivariant resolutions can be formed by the affine group coaction followed by ordinary sheaf resolutions; exactness of invariants removes the group-resolution cohomology. The finite Čech bound supplies the unbounded extension. Thus neither a stable affine cover nor exact degree-zero global sections is assumed. Formula (AF.2) proves compactness of \(P_E\). Taking \(E=\mathcal O_Z\otimes W\) for all finite rational representations \(W\) gives compact generators of the weak category, by the conservativity just proved and the representation detection property.

Pass to the strong category by freely adjoining the Cartan operators. Let \(N(\mathfrak h)\) be the enveloping DG algebra of the cone Lie algebra (SC.3), with even generators \(Q_\xi\), odd generators \(\epsilon_\xi\), and \(d\epsilon_\xi=Q_\xi\). PBW gives its finite exterior description as a graded right \(U(\mathfrak h)\)-module. A weak complex \(P\) is a left \(U(\mathfrak h)\)-module through its difference action \(Q\). Set
\[
 \mathcal F(P)=N(\mathfrak h)\otimes_{U(\mathfrak h)}P.
 \tag{AF.3}
\]
The rational action is diagonal, using the adjoint action on \(N\). The operator action is on \(P\), commuting with \(Q\). The left even \(N\)-action is the rational infinitesimal action minus the operator moment action on this tensor: commuting an even generator past a PBW exterior monomial supplies its adjoint action, and its action on \(P\) supplies \(Q_P\). Thus (AF.3) is a Cartan complex. It is left adjoint to forgetting the odd operators.

This adjunction descends to the full derived categories. In fact \(N\) is graded finite free as a right enveloping-algebra module. Filtering its underlying complex by exterior degree gives a finite filtration with quotients equal to finite exterior powers of \(\mathfrak h\) tensored with \(P\). Thus it sends acyclic \(P\)'s to acyclic complexes, with no bound on the coefficients. Forgetting the odd operators also preserves quasi-isomorphisms and colimits. The adjunction unit and counit consequently descend to the DG localizations. By (AF.2), the strong objects
\[
 \mathcal F(P_{\mathcal O_Z\otimes W})
   \quad(W\text{ finite rational }H\text{-representation})
 \tag{AF.4}
\]
are compact. They detect zero by adjunction and the weak generator property. The finite cell argument of §1.11 therefore proves that all compact objects are retracts of finite cells in these generators. This proves compact generation of \(\mathrm{Dmod}([Z/H])\), using (SC.2).

We prove duality on these compact objects rather than infer it from their atlas coherence. On a smooth scheme of dimension \(d\), the dual of a perfect left operator complex is
\(\omega_Z^{-1}\otimes\mathcal Hom_{\mathcal D_Z}(M,\mathcal D_Z)[d]\). Its double dual is the original complex by evaluation on finite projective modules and their finite cones and retracts. On the Hom before the density conversion, give the odd operator by
\(\epsilon_\xi(f)=-(-1)^{|f|}f\epsilon^M_\xi\). The rational action is the contragredient action together with the adjoint action on the coefficient operators. Its difference from the right moment is \(-fQ^M_\xi\): the left coefficient moment cancels by D-linearity of \(f\). This proves the Cartan differential identity on the dual. Anticommutation and rational equivariance follow from the same Hom formula. Density conversion and the shift give the normalized left dual.

Here is the calculation on an induced generator. Complementary exterior powers give
\[
 (\bigwedge\mathfrak h)^*
    =\bigwedge\mathfrak h\otimes
                \det(\mathfrak h)^*[-\dim H].
 \tag{AF.5}
\]
In the enveloping differential, transposition of an even coefficient action makes it the contragredient difference action; transposition of its bracket terms contributes the trace of \(\operatorname{ad}\xi\). For \(\mathfrak{gl}_a\) this trace is zero: left multiplication on matrix space has trace \(a\operatorname{tr}\xi\), and right multiplication has the same trace. The extra torus factors have zero bracket. Pairing complementary wedges now identifies the transposed exterior differential with that of (AF.3). The differential-operator transpose changes a vector field to its negative and includes the divergence on the density line. This changes \(E\) to \(E^*\otimes\omega_Z^{-1}\). Consequently, including both dimension shifts,
\[
 \mathbb D_{[Z/H]}\mathcal F(P_E)
   \simeq\mathcal F(P_{E^*\otimes\omega_Z^{-1}})
           \otimes\det(\mathfrak h)^*[d-\dim H].
 \tag{AF.6}
\]
The formula uses the finite exterior pairing, so it applies to the actual differential and odd operators. The determinant line is retained; for the frame groups its rational action is trivial, since
\(\mathfrak{gl}_a=V\otimes V^*\) has adjoint determinant one and the tori act trivially on their Lie algebras. No chosen volume is needed.

To relate this to intrinsic stack duality, recall the atlas normalization from §1.12. Smooth duality on perfect complexes is checked by the relative Spencer resolution: the trivial relative connection is self-dual, and reversing its finite exterior resolution cancels its density and dimension factors. Thus
\[
 \mathbb D_Z(q^!M[-\dim H])
   \simeq q^!(\mathbb D_{[Z/H]}M)[-\dim H].
 \tag{AF.7}
\]
Equivalently duality of \(q^!\) differs by \([-2\dim H]\) before normalizing. This explains both the scheme shift and group shift in (AF.6). The same finite transfer calculation makes the dual complexes and their comparisons agree on every overlap of two presentations, with composition comparisons from tensor–Hom adjunction. Hence the construction descends with all higher maps.

The right side of (AF.6) is compact by (AF.2)–(AF.3), since its coefficient is again a finite-rank linearized vector bundle. Exactness and double-dual evaluation now show that duality is an anti-equivalence on the full compact subcategory. A compact generator has a bounded, locally perfect underlying operator complex, since its exterior degree is finite; finite cells and retracts retain that property, so all duals just used are defined.

For completeness, a compactly generated category \(\mathcal C\) has continuous dual \(\operatorname{Ind}((\mathcal C^c)^{\mathrm{op}})\). Choose its small DG category of compact generators. The free-module bar resolution identifies \(\mathcal C\) with modules over that DG category: evaluate mapping complexes on the generators and reconstruct by their coend tensor; the unit holds on free cells and their realizations, and conservativity proves the counit. A continuous functor to complexes is then specified by its values on the generators and their DG maps, and its extension is the same coend. These are precisely modules over the opposite DG category. Finite cell objects and their retracts give the asserted Ind description. Applying the anti-equivalence just proved gives
\[
 \mathrm{Dmod}([Z/H])^\vee\simeq\mathrm{Dmod}([Z/H]).
 \tag{AF.8}
\]
Its pairing, on a compact first argument, is
\(\operatorname{RHom}(\mathbb D F,M)\), extended continuously to all first arguments.

Finally a smooth quasiprojective scheme \(Z_0\) with an \(H\)-linearized ample line has a quasiaffine line-frame presentation. Take a sufficiently large power whose sections give a locally closed projective embedding, and enlarge a finite such linear system to its finite rational \(H\)-orbit span. This retains the embedding and makes it equivariant. The nonzero vectors in the inverse ample line form the cone over that locally closed embedding, an open subset of its affine cone closure. Thus their scheme \(Z\) is quasiaffine and
\[
 [Z_0/H]\simeq[Z/(H\times\mathbb G_m)].
 \tag{AF.9}
\]
The additional multiplicative group acts freely on the line frame, so this is an equivalence on all coefficient families. Applying (AF.4) and (AF.8) to the right side proves compact generation and self-duality for the left side.

These hypotheses hold for every bounded bundle open used here. The faithful framed Quot construction in [*The moduli stack of bundles*](the-moduli-stack-of-bundles.md), §§1.2–1.5, gives a smooth scheme of frames and reductive reductions over an open of a projective Quot scheme, with frame group \(GL_a\). The reduction scheme is affine of finite presentation over that open. Pullback of its Plücker ample line is ample along this affine map and is frame-linearized. One can verify ampleness directly: a coherent generating module for an affine finite-type algebra is generated after ample twists on the base, giving a closed embedding in a finite sum of such line bundles. Its pullback ample twists generate all coherent sheaves. Thus the reduction scheme is quasiprojective and has the linearized ample line required in (AF.9). A quasicompact open of it retains that ample line. The same argument covers a smooth locally closed block: its preimage in the framed presentation is a smooth locally closed scheme with the restricted linearized ample line. A bounded bundle open meets only finitely many integral component and degree labels; use finitely many such presentations and the open-and-closed component decomposition if the frame rank varies. The preceding arguments give the claimed compact generators and duality for every bounded \(G\)- and Levi-bundle open, in every genus. The framing group here is \(GL_a\); it does not replace or restrict the connected reductive bundle group \(G\).

**Exercise 1.G.** For one variable of weight \(n>0\), compute the dual of \(F_m\) from (AF.6). Check it on the cyclic Weyl module presentations when \(n=1\) and \(m=0\).

**Solution 1.G.** The chart has dimension one and the group dimension one, so the total shift is zero. The inverse canonical line has weight \(-n\); the dual input weight is therefore \(-m-n\). Thus \(\mathbb D F_m=F_{-m-n}\). For \(n=1,m=0\), the underlying two-term free resolution has cokernel \(D_1/D_1(x\partial)\). Formal transposition sends \(x\partial\) to \(-\partial x\); dualizing the resolution, with the scheme dimension shift, gives \(D_1/D_1(\partial x)\). Its generator has weight \(-1\), exactly the cokernel of \(F_{-1}\). This checks the density weight and both dimension shifts, not just the ungraded module.

### 1.14. Contraction over the full Levi base

Let \(S\) be one of the bounded smooth stack presentations of §1.13. Let \(q:W\to S\) be a smooth affine morphism of finite presentation with a section \(i:S\hookrightarrow W\), and an \(\mathbb A^1\)-action over \(S\) whose zero map is \(iq\). We first prove contraction on its quotient by the action of \(\mathbb G_m\). This quotient keeps the full group action on the base.

Choose the line-frame presentation \(S=[Z/H]\) in (AF.9), with \(Z\) quasiaffine and \(H=GL_a\times\mathbb G_m^s\). Write \(W_Z=\operatorname{Spec}_Z\mathcal A\). The monoid action gives a nonnegative grading, with \(\mathcal A_0=\mathcal O_Z\); its augmentation is the section. Indeed the pullback of the zero map sends a function to its degree-zero coefficient and equals pullback along \(iq\). This proves the equality of degree-zero functions with functions from the base, not just their equality on geometric fibres.

There is an equivariant closed embedding in a positively weighted affine space over \(Z\). To construct it, choose finitely many coherent homogeneous generating modules of \(\mathcal A\) in positive degrees. They exist because the algebra is of finite presentation and its grading is nonnegative with the specified degree zero. Each needed degree module is coherent: a finite collection of positive generators has only finitely many monomials of a fixed degree. On a quasiaffine scheme every quasi-coherent sheaf is generated by its global sections, by open direct image into an affine scheme. Quasicompactness selects finitely many sections generating these coherent modules. Enlarge their spans to their finite rational \(H\)-orbit spans; the linearization gives a rational action on global sections. Thus, for a finite coordinate representation \(B=\bigoplus_{n>0}B_n\),
\[
 \mathcal O_Z\otimes\operatorname{Sym}(B)\twoheadrightarrow\mathcal A,
 \qquad W_Z\hookrightarrow Y:=Z\times B^*.
 \tag{RV.1}
\]
Here the contracting multiplicative group acts on a coordinate in \(B_n\) with weight \(n\); its action commutes with \(H\). The zero section of \(Y\) pulls back to the section of \(W_Z\), scheme-theoretically, since quotienting \(\mathcal A\) by these positive generators leaves \(\mathcal A_0\).

Put \(r=\dim B\). Compact generators on \([Y/(H\times\mathbb G_m)]\) are, by (AF.4), the strong inductions from free weak modules with finite \(H\)-coefficient \(V\) and contracting-group weight \(m\). The normal Koszul calculation of §1.11 now gives
\[
 i_Y^!\mathcal F_{\mathfrak h\oplus k}
       (\mathcal D_Y\otimes V\otimes\chi^m)
  \simeq
 \mathcal F_{\mathfrak h\oplus k}
       (\mathcal D_Z\otimes V\otimes S_m\otimes\chi^0)[-r],
 \tag{RV.2}
\]
where
\[
 S_m=
 \bigoplus_{\sum n d_n=m,\ d_n\geq0}
             \bigotimes_{n>0}\operatorname{Sym}^{d_n}(B_n^*).
 \tag{RV.3}
\]
These are finite-dimensional \(H\)-representations; if \(m<0\) the sum is zero. The contracting-group odd operator on the right is still free. We verify the base-group part of this formula explicitly.

Induction by the commuting Lie cones \(\mathfrak h\) and \(k\) is induction by their direct sum: their odd generators anticommute and their even generators commute. Use the relative delta Koszul resolution for the normal coordinates. Its delta density is \(\det B^{-1}\); its top Koszul term has the compensating \(\det B\), so the top source generator has trivial \(H\)-character. The positive-group calculation consequently selects the derivative space (RV.3). For an infinitesimal \(\xi\in\mathfrak h\) acting on the normal coordinates with matrix \(b_{ij}\), its normal moment is \(\sum b_{ij}x_j\partial_i\). Its normal Koszul homotopy is \(-\sum b_{ij}R_{\partial_i}e_j\wedge\). This is (CW.6) with the diagonal matrix replaced by the actual action matrix. Its commutator with the Koszul differential is the normal difference action, with the density trace and exterior trace cancelling at the top term.

In the top quotient, right multiplication by that normal moment sends a derivative monomial to
\(\sum b_{ij}q_j\partial^{q-e_j+e_i}\). Its negative is exactly the infinitesimal action on \(\operatorname{Sym}(B^*)\). The weak difference action therefore becomes the difference action on \(\mathcal D_Z\otimes V\otimes S_m\). The bracket terms in the Lie-cone differential are unchanged. Projection to top normal cohomology kills precomposition by each normal Koszul homotopy, which lowers normal cochain degree; the odd operators on the induced module remain. This proves (RV.2) with the full base Lie differential, rational action and odd operators. The calculation is intrinsic in the normal representation \(B\), so it glues on every chart of \(Z\). We have computed the image of global generators, rather than tested compactness separately on those charts.

The right side of (RV.2) is compact by (AF.2)–(AF.4), including its finite coefficient representation and free odd operator. Finite cells and retracts prove that \(i_Y^!\) preserves every compact object. Thus the zero section in this quotient of \(Y\) is truncative.

Pass from \(Y\) to \(W_Z\) using the closed embedding (RV.1). Closed direct image preserves compact objects: it is left adjoint to the continuous normal !-functor, computed by its finite Spencer–Koszul transfer. For a compact object \(F\) on \([W_Z/(H\times\mathbb G_m)]\), its closed direct image is therefore compact on the ambient quotient. Proper closed base change in the zero-section square identifies its normal pullback with \(i^!F\), since that square is scheme-theoretically Cartesian. This base change is the closed transfer calculation proved in [*Adjunctions, base change and the projection formula*](../../GL-DMOD/src/adjunctions-base-change-and-the-projection-formula.md), §§1–2; its normal complexes are finite, so it applies to unbounded coefficients and passes to the Cartan operators by (SC.7)–(SC.8). It follows that
\[
 S/\mathbb G_m\hookrightarrow W/\mathbb G_m
       \quad\text{is truncative}.
 \tag{RV.4}
\]
All bases and all their frame actions have been retained.

Now suppose the \(\mathbb G_m\)-action on the absolute stack \(W\) is coherently trivial, as for the opposite-parabolic space of §1.7. There is an equivalence \(W/\mathbb G_m\simeq W\times B\mathbb G_m\). The closed substack \(S/\mathbb G_m\) becomes \(S\times B\mathbb G_m\) under the induced restriction of that equivalence, by the ideal-sheaf descent in §1.7. Use this induced equivalence on the substack: its identification with the *relative* quotient can include the central line-torsor twist, and need not be its untwisted projection to the Levi base.

For any of these finite-type presentations, the point-quotient calculation gives
\[
 \mathrm{Dmod}(T\times B\mathbb G_m)
     \simeq \mathrm{Dmod}(T)\otimes A\text{-}\mathrm{mod},
 \qquad A=\Lambda(\tau),\quad |\tau|=-1.
 \tag{RV.5}
\]
Here is the comparison on the full category. In a Cartan presentation, the additional group acts trivially on the chart, so its moment is zero. Its nonzero integer weights contract by \(\epsilon/m\); weight zero is an additional anticommuting odd operator with zero differential. This is the category of \(A\)-modules in the original DG model. Its free-module bar resolution gives (RV.5): evaluation on free \(A\)-objects and their realizations gives the unit, and the conservative underlying-object functor gives the counit. The atlas normalization is additive in the two group dimensions, so it agrees with the external-product normalization, and uses the same compact free point object in source and target.

In the internal module category let \(L_A(M)=A\otimes M\) and let \(U_A\) forget the operator. There are adjunctions
\[
 L_A\dashv U_A\dashv\operatorname{Hom}_k(A,-).
 \tag{RV.6}
\]
The first right adjoint is continuous. The second right adjoint is continuous as well, because \(A\) is a bounded finite-dimensional complex. Thus both \(L_A\) and \(U_A\) preserve compact objects. This uses the free object of the point-quotient category and its finite underlying complex, not the noncompact augmentation object.

Take a compact \(F\) on \(W\). Its free \(A\)-extension on the product is compact. By (RV.4), its pullback to the closed product substack is compact. Product compatibility of the finite normal transfer makes that pullback \(L_A(i^!F)\). Forgetting the odd operator keeps it compact and gives
\[
 U_A L_A(i^!F)=i^!F\oplus(i^!F)[1].
 \tag{RV.7}
\]
The first summand is a retract, hence compact. This proves that the actual split section \(S\hookrightarrow W\) is truncative. It is not an inference of compactness from an arbitrary smooth atlas.

Apply this to the full opposite-parabolic affine family \(W\to B_M(S)\), including the bounded open restriction of §1.9. Its affine smooth map, positive graded monoid action and coherent absolute trivialization were proved in (GT.13)–(GT.19). The base presentations satisfy §1.13. Consequently (RV.7) supplies exactly the missing hypothesis of (CC.8). The split unipotent-gerbe equivalence (CC.7) and smooth compact-preserving map (CC.3) now prove
\[
 Z_G(S)\hookrightarrow\operatorname{Bun}_G
        \quad\text{is truncative on every bounded ambient open.}
 \tag{RV.8}
\]
The admissible sets, radical cohomology and chart maps used here were proved for every connected reductive characteristic-zero group, every genus and every coefficient family. The proof has retained the Levi family throughout, including its automorphisms and derived equivariance.

**Exercise 1.H.** Let two independent multiplicative groups act on \(\mathbb A^2\): a base group scales both coordinates with weight one, and the contracting group also scales both with weight one. For an induced generator with base-group coefficient weight \(a\) and contracting weight \(2\), compute the zero-section image for \(a=2\) and for \(a=0\).

**Solution 1.H.** The selected derivative monomials are \(\partial_1^2,\partial_1\partial_2,\partial_2^2\). Each has base-group weight \(-2\), so its coefficient after the normal functor has base weight \(a-2\). For \(a=2\), both point moments vanish and the image is three copies of the free module \(\Lambda(\epsilon_{\mathrm{base}},\tau)[-2]\). For \(a=0\), the point differential satisfies \([d,\epsilon_{\mathrm{base}}]=-2\); division by \(-2\) contracts the entire image, so it is zero. Counting the three monomials without their base action would miss this distinction. Both images are compact, as required by (RV.2).

### 1.15. Finite complements, extension and the global dual

We supply the categorical assembly. All quasicompact ambient opens below are the finite-type smooth bundle presentations of §1.13, or their quasicompact open subsets. Their categories are compactly generated and self-dual by that section. A boundary need not be smooth; the closed-support argument below takes place in its smooth ambient category.

For an open immersion \(j:U\hookrightarrow Y\), restriction has the continuous right adjoint \(j_*\). It is fully faithful. The finite affine Čech calculation constructs it on every chart and proves continuity also on unbounded complexes, as in (CC.1)–(CC.2). For the closed complement \(Z\), define the support functor by
\[
 \Gamma_ZF\longrightarrow F\longrightarrow j_*j^*F.
 \tag{FT.1}
\]
On an affine chart this is the local cohomology complex computed by the finite localization Čech complex of generators of the closed ideal. Its differentials and localizations respect differential operators; smooth descent glues it on the stack. It depends only on the closed support and is continuous. Its image is the kernel of restriction to \(U\). For an object \(T\) in that kernel, adjunction gives \(\operatorname{RHom}(T,j_*N)=0\), so (FT.1) identifies \(\Gamma_Z\) as right adjoint to the inclusion of the closed-supported category. That inclusion is fully faithful and continuous and preserves compact objects, since its right adjoint is continuous. It reflects compact objects as well: compute their mapping complexes in the ambient category after applying the fully faithful, colimit-preserving inclusion.

For a smooth closed substack, this is \(i_*i^!\). The coordinate proof of this assertion is Kashiwara's equivalence in [*Kashiwara's equivalence and D-modules on singular spaces*](../../GL-DMOD/src/kashiwaras-equivalence-and-singular-spaces.md), §§1–3, and the localization calculation in [*Adjunctions, base change and the projection formula*](../../GL-DMOD/src/adjunctions-base-change-and-the-projection-formula.md), §1. Their derived extension here is unbounded: the normal Koszul complex has finite width, and on supported cohomology its only cohomology is the degree-zero Kashiwara inverse. The finite filtration then identifies the unit and counit on arbitrary coefficient complexes. We therefore have the stated support functor whenever using a smooth root block. For a singular union we can continue to use (FT.1) in the same ambient category, without assigning it a ring of operators on its singular coordinate ring.

Compactness is local on a *finite Zariski open cover* in these categories. For two opens \(Y=U\cup V\), descent gives the finite mapping-complex fibre
\[
 \operatorname{RHom}_{Y}(M,N)
 =\operatorname{fib}\left(
  \operatorname{RHom}_{U}(M_U,N_U)\oplus
  \operatorname{RHom}_{V}(M_V,N_V)
       \longrightarrow\operatorname{RHom}_{U\cap V}(M,N)
                       \right).
 \tag{FT.2}
\]
Restriction preserves compact objects because its right adjoint is continuous. If both \(M_U,M_V\) are compact, their intersection restrictions are too. Filtered colimits of complexes commute with the finite fibre in (FT.2), so \(M\) is compact. Finite induction proves the assertion for any finite cover. The affine diagonal ensures that all intersections used here are quasicompact. This proof concerns a finite open cover, not an arbitrary smooth covering.

For a closed \(Z\subset Y\), the following are equivalent:
\[
 \Gamma_Z\text{ preserves compact objects};
 \qquad j_*\text{ preserves compact objects}.
 \tag{FT.3}
\]
If the first holds, (FT.1) makes \(j_*j^*F\) compact for every compact \(F\) on \(Y\). The restrictions of compact generators of \(Y\) generate the category on \(U\): their mapping complexes into \(M\) test \(j_*M\), and \(j_*\) is fully faithful. These restrictions are compact. The finite cell description therefore says that every compact object on \(U\) is obtained by finite cones and retracts from such restrictions. Applying \(j_*\) proves its compact preservation. The converse follows at once from (FT.1). In particular a smooth closed truncative block, whose \(i^!\) preserves compactness, has this property by closed direct image.

The properties used here pass to an open restriction of the ambient stack. Indeed compact objects of that open are finite cells and retracts of restrictions of ambient compact objects, by the same generator argument. Support functors commute with open restriction by their finite localization complex. For a locally closed smooth block, !-pullback also commutes with the open square, and open restriction on the block preserves compactness. This proves open base change of the root-block truncativity property for every compact object, rather than only for those visibly extended from the ambient stack.

We next prove the finite-union assertion needed for the HN cuts. Suppose \(Z_0\subset Z\subset Y\) are closed, \(\Gamma_{Z_0}\) preserves compactness on \(Y\), and the support functor of \(Z-Z_0\) preserves compactness on \(Y-Z_0\). Then \(\Gamma_Z\) preserves compactness. By (FT.3), the open direct image from \(Y-Z_0\) preserves compact objects. Localization applied to \(\Gamma_ZF\) gives
\[
 \Gamma_{Z_0}F\longrightarrow\Gamma_ZF
   \longrightarrow j_*
        \Gamma_{Z-Z_0}(j^*F),\qquad j:Y-Z_0\hookrightarrow Y.
 \tag{FT.4}
\]
The first identification uses \(\Gamma_{Z_0}\Gamma_Z=\Gamma_{Z_0}\): their adjunction characterization on objects supported on \(Z_0\) proves this by Yoneda. Open restriction gives the last term. If \(F\) is compact, both end terms are compact by the hypotheses and (FT.3); hence the middle term is compact.

Now let a closed \(Z\) be covered by finitely many locally closed truncative root blocks \(Z_1,\ldots,Z_b\). For each \(Z_i\) take the open complement of \(\overline Z_i-Z_i\); there \(Z_i\) is closed. These opens, together with \(Y-Z\), form a finite open cover of \(Y\). They are quasicompact, since the bounded ambient stack is Noetherian. On the open belonging to \(Z_i\), its complement in \(Z\) is covered by the other \(b-1\) blocks, restricted to the open complement of \(Z_i\). Open base change retains their truncativity. Induction on \(b\), followed by (FT.4), proves compact preservation by \(\Gamma_Z\) on each such open. Formula (FT.2) then proves it on \(Y\). This proves the finite-union assertion even when the closed union is singular.

Use the exhaustion (GT.25)–(GT.27). Choose dominant \(\theta\) with \(\alpha_i(\theta)\geq c=\max(0,2g-2)\), at the chosen central and integral labels. For any larger dominant cut \(\theta'\), the complement \(U_{\theta'}-U_\theta\) has finitely many HN types. Section 1.9 covers it by the admissible root blocks, restricted to that larger cut. Their truncativity is (RV.8). The preceding finite-union proof and (FT.3) therefore give
\[
 (U_\theta\hookrightarrow U_{\theta'})_*
           \text{ preserves compact objects}.
 \tag{FT.5}
\]
These cuts are cofinal among quasicompact opens. This is the geometric and categorical truncatability assertion, with its central labels retained.

For such a pair of bounded opens, define on compact objects
\[
 j_!F=\mathbb D_{U_{\theta'}}j_*\,
                              \mathbb D_{U_\theta}F.
 \tag{FT.6}
\]
It is compact by (FT.5) and §1.13. Extend continuously from compact objects by their Ind presentation. To prove the adjunction, first let \(F,M\) be compact. Anti-duality, the ordinary open adjunction and compatibility of duality with restriction give
\[
 \operatorname{RHom}(j_!F,M)
   =\operatorname{RHom}(\mathbb D M,j_*\mathbb D F)
   =\operatorname{RHom}(j^*\mathbb D M,\mathbb D F)
   =\operatorname{RHom}(F,j^*M).
 \tag{FT.7}
\]
For compact \(F\), both sides preserve colimits in \(M\), so the generator property extends the equality to all \(M\). For arbitrary \(F\), both sides send its colimits to limits, proving the adjunction on the full unbounded categories. Also \(j^*j_!=\operatorname{id}\), first by dualizing \(j^*j_*\) on compact objects and then by continuity. Thus \(j_!\) is fully faithful. For nested cuts, their composite !-extensions represent the same mapping-complex functor; Yoneda supplies their coherent composition identifications.

Let \(\mathcal I\) be the filtered cofinal poset of these cuts, including finite unions of central components. Set \(\mathcal C=\mathrm{Dmod}(\operatorname{Bun}_G)\) and \(\mathcal C_i=\mathrm{Dmod}(U_i)\). Proposition 1.1 already proved \(\mathcal C=\lim_i\mathcal C_i\) by restriction. A left adjoint \(l_i\) to its global restriction is now constructed, not assumed. For \(j\geq i\), give \(l_iF\) the component
\[
 (l_iF)|_{U_j}=j_{ij!}F.
 \tag{FT.8}
\]
For any other index, choose a later one containing it and \(i\), and restrict this extension. The full-faithfulness and composition identities just proved make the answer independent of the later choice, including higher comparisons. These components therefore define an object of the restriction limit. Their colimit compatibility proves continuity of \(l_i\): colimits in that limit are computed componentwise, as is verified by the universal mapping property and the commutation of limits of mapping complexes. Finally
\[
 \operatorname{RHom}_{\mathcal C}(l_iF,M)
   =\lim_{j\geq i}\operatorname{RHom}_{\mathcal C_j}
                                    (j_{ij!}F,M_j)
   =\operatorname{RHom}_{\mathcal C_i}(F,M_i).
 \tag{FT.9}
\]
The last diagram is coherently constant by the adjunctions. This proves the global left adjoint on all D-modules. Its existence is precisely the co-truncative property of the open \(U_i\).

Each \(\mathcal C_i\) has the compact generators of §1.13. Restriction is continuous and jointly conservative. The formal proof in §1.1, now with all its geometric hypotheses established, gives the compact generators
\[
 \{l_iG:\ i\in\mathcal I,
                  G\text{ one of the generators of }\mathcal C_i\}
       \quad\text{of }\mathrm{Dmod}(\operatorname{Bun}_G).
 \tag{FT.10}
\]
This proves compact generation for the full unbounded bundle stack, not for a single bounded component.

We also prove the stated co-duality. For an open restriction \(r_{ij}:\mathcal C_j\to\mathcal C_i\), finite-stage duality identifies its continuous dual with \(j_{ij*}\). Test this on a compact \(F\in\mathcal C_j\) and any \(M\in\mathcal C_i\):
\[
 \langle r_{ij}F,M\rangle_i
   =\operatorname{RHom}_i(r_{ij}\mathbb D_jF,M)
   =\operatorname{RHom}_j(\mathbb D_jF,j_{ij*}M)
   =\langle F,j_{ij*}M\rangle_j.
 \tag{FT.11}
\]
This is an equality of the pairings on their compact generators, natural in all DG maps. Their continuous extensions give the equality of the dual functors.

Put \(\mathcal E=\operatorname{colim}_{i,j_{ij*}}\mathcal C_i\). By (FT.5) the transition functors preserve compact objects; they are fully faithful as open direct images. Their small compact DG subcategories therefore have a filtered union, with its finite cones and idempotents. The Ind category of this union is \(\mathcal E\): a continuous functor out of it is exactly a compatible collection of continuous functors out of the stages, as follows from the free-module bar presentation. In particular \(\mathcal E\) is compactly generated. Continuous functors from a colimit to complexes are the compatible limit of the stage functors, including their mapping complexes. Using (FT.11) and finite-stage self-duality gives \(\mathcal E^\vee=\lim_i\mathcal C_i=\mathcal C\). The double-dual identification for compactly generated categories follows from the same small-DG-module description used in (AF.8). Consequently
\[
 \mathrm{Dmod}(\operatorname{Bun}_G)^\vee
       \simeq\operatorname{colim}_{i,j_{ij*}}\mathrm{Dmod}(U_i)
       =\mathrm{Dmod}_{\mathrm{co}}(\operatorname{Bun}_G).
 \tag{FT.12}
\]
This proves (1.3) with its actual \(*\)-transition maps. It does not identify that colimit with the colimit using \(!\)-extensions.

The normalized half-root constructed in §§2.2–2.9 gives the same statements for the half-twisted category. Locally its operator algebra is conjugated by that root line; tensoring with its inverse is the Morita untwisting. On overlaps the actual root-line transition functions make these conjugations satisfy the cocycle, and on an open they restrict to the same transition functions. Thus the untwisting equivalences commute with every restriction and with their uniquely characterized left and right adjoints. Transport the compact-object dualities through these equivalences. Equivalently, the neutralized root gerbe has its prescribed sign sector of the finite group \(\mu_2\); averaging makes that sector a copy of complexes, and its sign character is its own dual. Hence the finite-stage dualities and their restriction comparisons give
\[
 \mathrm{Dmod}_{1/2}(\operatorname{Bun}_G)^\vee
      \simeq\mathrm{Dmod}_{1/2,\mathrm{co}}(\operatorname{Bun}_G).
 \tag{FT.13}
\]
A choice of root trivializes the twisting gerbe; the proof of §§2.2–2.9 retains the determinant normalization and all coefficient families. No claim about an arbitrary unrelated twisting gerbe is needed.

If the root system is empty, each integral torus degree component is itself quasicompact; finite unions of them give the required cuts, and their open-and-closed extensions satisfy the same adjunctions. For a general reductive group, §1.9 already retained the central and torsion labels and finite unions of their bounded cuts. Hence (FT.5)–(FT.13) apply in every genus, with every connected component included. The formal compact-generation and co-duality calculations at the start of this lesson now have the complete truncatability, finite-presentation-category and half-root hypotheses they require.

**Exercise 1.I.** Why does the finite Zariski-cover assertion (FT.2) not imply compactness from an infinite cover by open points? Give an example and compare it with Exercise 1.D.

**Solution 1.I.** On the discrete stack \(\mathbb Z\), take the family with one copy of \(k\) at every point. Every point restriction is compact. The family is the filtered colimit of its finite-support subfamilies. If it were compact, its identity would factor through one of those finite-support objects, which is impossible at a point outside that support. Formula (FT.2) uses a finite mapping-complex fibre; an infinite-cover mapping limit need not commute with filtered colimits. Exercise 1.D gives a different failure: a single smooth atlas of \(B\mathbb G_m\) pulls a noncompact object to a compact one. The root-block proof used the special unipotent-gerbe equivalence, while the finite-union proof used only the genuinely finite Zariski argument.

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

For this particular stack, §§2.2–2.8 construct a root of (2.1) after choosing a theta characteristic on \(X\), an invariant adjoint form and a scalar whose square is minus one. This proves the assertion used in GLC I §1.1.2 for every connected reductive \(G\). The free [Beilinson–Drinfeld draft, §§4.2–4.4, especially equation (209), PDF pp.163–164](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf), gives further reading on the Clifford half-form construction. The proof below includes coefficient families, the normalized determinant comparison and the central adjoint summand.

The twist is retained even after choosing an untwisting equivalence. GLC I §1.1, the remark following (1.1), explains its compatibility with the usual dual-group representation category in Hecke functors. Changing the root can change the chosen identification with ordinary D-modules; it does not change the definition (2.2).

### 2.1. The finite Pfaffian calculation and its family obligation

The finite-dimensional core of the Pfaffian construction has an equally precise scope. Let \(E\) be a vector bundle, and let \(a:E\to E^\vee\) be skew-symmetric. For the two-term complex \(K=[E\to E^\vee]\) in degrees zero and one,

\[
\det K=\det E\otimes(\det E^\vee)^{-1}
       =(\det E)^{\otimes2}.
\]

Thus \(\det E\) is a square root for this presentation. Stabilizing by an acyclic skew block supplies its Pfaffian trivialization: if the block is \(F\to F^\vee\) with invertible alternating form, its top exterior power gives the canonical trivialization of \(\det F\); it squares to the corresponding determinant trivialization. Basis changes transform the top exterior form by the determinant, so this statement is independent of the chosen basis. Composition of orthogonal changes preserves these identifications. This proves the algebraic compatibility for such finite presentations.

This finite calculation alone does not produce a line on \(\operatorname{Bun}_G\). Sections 2.2–2.8 construct finite residue representatives of \(R\Gamma(X,\operatorname{ad}(P)\otimes \kappa)\) in families, use actual Clifford reduction maps to prove their transition cocycle, and establish the determinant comparison

\[
\frac{\det R\Gamma(X,\operatorname{ad}(P)\otimes\kappa)}
     {\det R\Gamma(X,\mathfrak g\otimes\kappa)}
\simeq
\frac{\det R\Gamma(X,\operatorname{ad}(P))}
     {\det R\Gamma(X,\mathfrak g\otimes\mathcal O_X)}.
\]

The quotient notation means tensoring by the inverse constant line. Pointwise cohomology determinants alone do not give this family identity or its descent. The proof in §§2.2–2.8 supplies both, and the normalized Pfaffian ratio squares to (2.1), with a canonical trivialization at the trivial bundle. Formula (2.3) continues to describe the local twisted operators. The global construction includes the connected reductive case by cancelling its constant central adjoint summand.

### 2.2. Clifford modules over coefficient rings

We fix a theta characteristic \((\kappa,\kappa^2\simeq\omega_X)\) and a scalar \(i\in k\) with \(i^2=-1\). The scalar is part of the square identification below. First we construct the finite algebra that will make the line in families. All rings in the construction are \(k\)-algebras; in particular \(2\) is invertible.

Let \(W\) be a finite projective module with a nondegenerate symmetric form \(b\), and let \(A\subset W\) be a Lagrangian subbundle. Thus \(A=A^\perp\) and \(W/A\) is projective. Locally \(W=A\oplus A^\vee\) as an orthogonal hyperbolic module. Indeed choose any splitting of \(W\to A^\vee\). Its restriction has a symmetric matrix \(c\); subtract half that matrix, viewed as a map into \(A\), to make the complementary submodule isotropic. This argument works over rings with nilpotents.

Define the Clifford algebra by
\[
 \mathrm{Cl}(W,b)=T(W)/(uv+vu-b(u,v)),\qquad
 u^2=\tfrac12b(u,u).
 \tag{PF.1}
\]
It is graded by parity, with \(W\) odd. In dual hyperbolic bases \(e_j,\phi_j\), its relations are
\[
 e_j e_l+e_l e_j=0,\quad
 \phi_j\phi_l+\phi_l\phi_j=0,\quad
 e_j\phi_l+\phi_l e_j=\delta_{jl}.
 \tag{PF.2}
\]
They put every word into a linear combination of ordered square-free words. These words are independent. Act on \(\Lambda A^\vee\), with \(e_j\) contraction and \(\phi_j\) exterior multiplication. The commuting operators \(\phi_je_j\) project onto wedges containing \(\phi_j\); \(1-\phi_je_j\) project onto the others. Products of these projections select any single exterior basis vector. Composing with exterior multiplication and contraction gives every matrix unit, with coefficient \(1\) or \(-1\). Thus the Clifford algebra surjects onto the matrix algebra of the \(2^{\operatorname{rk}A}\)-dimensional exterior module. Both have at most the same number \(2^{2\operatorname{rk}A}\) of the ordered generators. The matrix units make those generators independent and prove
\[
 \mathrm{Cl}(W,b)\simeq
 \mathcal E nd(\Lambda A^\vee).
 \tag{PF.3}
\]
This also proves the PBW filtration identity
\(\operatorname{gr}\mathrm{Cl}(W)=\Lambda W\).
Every assertion is an identity of modules and matrices over the coefficient ring.

For two Lagrangian subbundles \(A,B\subset W\), take the actual quotient
\[
 Q_b(A,B)=
 \mathrm{Cl}(W,b)/(B\,\mathrm{Cl}(W,b)+\mathrm{Cl}(W,b)\,A),
 \qquad
 \mathrm{Pf}_b(A,B)=Q_b(A,B)^\vee.
 \tag{PF.4}
\]
The sums are respectively a right ideal and a left ideal; their sum is used only as a submodule. We prove that this quotient is a line and that it commutes with every base change.

The module \(M_A=\mathrm{Cl}(W)/\mathrm{Cl}(W)A\) is locally \(\Lambda A^\vee\), by (PF.2). It is a projective module of rank \(2^{\operatorname{rk}A}\). Use a hyperbolic basis for \(B\) as well. The resulting \(M_B\) has the same rank over the same Clifford matrix algebra. Matrix units give the elementary Morita calculation: for a module \(M\) over \(\operatorname{Mat}_d(R)\), the maps
\[
 R^d\otimes E_{11}M\longrightarrow M,\qquad
 v_j\otimes m\longmapsto E_{j1}m
 \tag{PF.5}
\]
are inverse to \(m\mapsto\sum_j v_j\otimes E_{1j}m\). Hence \(M_A=M_B\otimes\ell\) for a projective line \(\ell\), locally on the base. In \(M_B=\Lambda B^\vee\), quotienting by the contractions from \(B\) leaves exactly the top exterior degree, a projective line. Thus \(Q_b(A,B)=M_A/BM_A\) is a projective line. Locally the quotient map is a split projection; its formation commutes with arbitrary tensor products of coefficient rings. The construction is functorial for isometries of triples, so it retains their automorphisms.

The line has a parity. Over a field split a pair of Lagrangians into transverse hyperbolic pairs and coincident ones: pair complementary parts of \(A\) and \(B\), then complete their common intersection to hyperbolic pairs. A transverse one-dimensional pair has Clifford quotient generated by \(1\), of even parity. A coincident pair has quotient generated by its dual vector, of odd parity. Consequently
\[
 p(\mathrm{Pf}_b(A,B))=\dim(A\cap B)\pmod2.
 \tag{PF.6}
\]
On a coefficient scheme the graded projective line has locally constant parity. This proves the corresponding parity constancy even when the intersection dimension jumps; the intersection itself need not be a bundle.

### 2.3. The determinant pairing and its sign choice

For orthogonal sums, the relations (PF.1) identify the Clifford algebra with the graded tensor product of the two Clifford algebras. Taking the two quotients gives a canonical multiplicative isomorphism
\[
 \mathrm{Pf}(W_1\oplus W_2;A_1\oplus A_2,B_1\oplus B_2)
 \simeq\mathrm{Pf}(W_1;A_1,B_1)\otimes
       \mathrm{Pf}(W_2;A_2,B_2).
 \tag{PF.7}
\]
All tensor interchanges here use the sign \((-1)^{pq}\) for parities \(p,q\).

There is a particularly explicit determinant case. For a projective module \(V\) without a form, give \(V\oplus V^\vee\) its hyperbolic form. For subbundles \(A,B\subset V\), the submodules \(A\oplus\operatorname{ann}(A)\) and \(B\oplus\operatorname{ann}(B)\) are Lagrangian. Use the Clifford module \(\Lambda V\). Its vectors killed by the first Lagrangian form \(\det A\). Quotienting by the second leaves \(\det(V/B)\): exterior multiplication kills \(B\), and contractions kill every degree below the top degree of \(V/B\). The matrix-unit calculation of §2.2 makes their ratio independent of this particular Clifford module. It proves
\[
 \mathrm{Pf}(V\oplus V^\vee;
 A\oplus\operatorname{ann}A,B\oplus\operatorname{ann}B)
 \simeq \det A\otimes\det(V/B)^{-1}.
 \tag{PF.8}
\]
Use determinants as graded lines of parity equal to rank modulo \(2\). Exact sequences define their wedge identifications, with the displayed ordering and these graded interchanges. A complex has determinant \(\det K^0\otimes(\det K^1)^{-1}\). Removing an acyclic direct summand uses its differential to contract those factors; this is the determinant convention throughout this construction.

Now take \(V=W\) with form \(b\). The map
\[
 (v,w)\longmapsto
 \left(v-w,\tfrac12b(v+w,-)\right)
 \tag{PF.9}
\]
identifies \((W,b)\oplus(W,-b)\) with \(W\oplus W^\vee\), with the hyperbolic form. Substitution gives \(b(v,v')-b(w,w')\); thus this is an actual isometry over the ring. It carries \(A\oplus A\) to \(A\oplus\operatorname{ann}(A)\), and similarly for \(B\). Equations (PF.7)–(PF.9), followed by the wedge identifications for the two exact sequences in \(W\), give a determinant pairing
\[
 \mathrm{Pf}_b(A,B)\otimes\mathrm{Pf}_{-b}(A,B)
 \simeq \det[\,B\longrightarrow W/A\,].
 \tag{PF.10}
\]
The subspace order is important: the differential is the inclusion followed by quotient. Formula (PF.8) initially gives \(\det A\otimes\det B\otimes(\det W)^{-1}\); the exact-sequence identification with the determinant on the right includes the graded interchange of the two rank-\(\operatorname{rk}A\) factors.

One can check the pairing entirely in ordered Clifford words. There is a graded anti-isomorphism from the algebra of \(-b\) to that of \(b\),
\[
 (v_1\cdots v_l)^\dagger
   =(-1)^{l(l-1)/2}v_l\cdots v_1.
 \tag{PF.11}
\]
Let \(\mathrm{top}:\mathrm{Cl}(W)\to\det W\) be the top PBW quotient. It satisfies
\(\mathrm{top}(xy)=(-1)^{p(x)p(y)}\mathrm{top}(yx)\):
moving a generator across a word changes its sign, and all contraction terms have lower PBW degree. With \(a_A\in\det A\), \(a_B\in\det B\), the multilinear expression
\[
 (a_B,x,a_A,y)\longmapsto
 \mathrm{top}(a_Bx\,a_Ay^\dagger)
 \tag{PF.12}
\]
descends to the two Clifford quotients in (PF.4). An extra generator from \(B\) or \(A\) meets the corresponding top wedge and kills it; the other two ideal terms are moved there by the graded top identity. To check nondegeneracy, use any exterior Clifford module \(M\). Multiplication by the top wedge \(a_A\) identifies its \(A\)-coinvariant line with its \(A\)-annihilator line: in a dual basis it contracts the top exterior vector to \(1\), with the unit sign \((-1)^{n(n-1)/2}\). The same holds for \(B\). The class of \(x\) is a map from the \(A\)-annihilator to the \(B\)-coinvariant; the class of \(y^\dagger\) is a map in the reverse direction. Their product with \(a_A,a_B\) is a rank-one endomorphism. The top PBW functional is its graded trace times the fixed exterior volume: for a diagonal matrix unit it is that volume with its parity sign, and for an off-diagonal unit it is zero, as the wedge and contraction matrices show. Thus (PF.12) pairs the two projective lines perfectly over the ring. In the doubled exterior module of (PF.9), the annihilator and coinvariant lines are exactly those in (PF.8); their ordered wedge identifications and graded interchanges give (PF.10). This is a coefficient-ring calculation; no reduced-point argument defines the pairing.

Multiplication by \(i\) is an isometry \((W,b)\to(W,-b)\), preserving both Lagrangians. It therefore identifies the two Pfaffian lines in (PF.10). We obtain
\[
 c_i:\mathrm{Pf}_b(A,B)^{\otimes2}
       \simeq\det[\,B\longrightarrow W/A\,].
 \tag{PF.13}
\]
Replacing \(i\) by \(-i\) changes this square identification by \((-1)^p\), where \(p\) is (PF.6): the extra automorphism is \(-1\) on \(W\), which acts by parity on the Clifford quotient. Thus the choice of \(i\) is retained explicitly.

### 2.4. Removing an isotropic submodule

Suppose \(U\subset A\) is a subbundle and \(U\cap B=0\) on every geometric fibre. Pairing with \(U\) gives a surjection \(B\to U^\vee\). Indeed its dual has kernel \(U\cap B^\perp=U\cap B=0\); the full-rank minors make the surjection split locally over any coefficient ring. Put
\[
 \bar W=U^\perp/U,\qquad
 \bar A=A/U,\qquad
 \bar B=B\cap U^\perp.
 \tag{PF.14}
\]
The last submodule injects into \(\bar W\), since \(B\cap U=0\), and both \(\bar A,\bar B\) are Lagrangian. All three modules are projective. Locally choose a splitting of \(B\to U^\vee\) inside \(B\). Its image \(U'\) is isotropic and pairs perfectly with \(U\). It gives an orthogonal decomposition
\[
 (W;A,B)=(U\oplus U';U,U')\ \oplus\
          (\bar W;\bar A,\bar B).
 \tag{PF.15}
\]
The first triple is transverse.

The Clifford map itself provides a choice-independent reduction. In the subalgebra generated by \(U^\perp\), the elements of \(U\) are killed in the quotient (PF.4). Hence its inclusion in \(\mathrm{Cl}(W)\) induces
\[
 Q_{\bar b}(\bar A,\bar B)\longrightarrow Q_b(A,B).
 \tag{PF.16}
\]
In the decomposition (PF.15), the transverse quotient is canonically generated by the class of \(1\); (PF.16) tensors with that class. It is an isomorphism. This also proves its validity over nilpotent rings, without requiring the field decomposition of §2.2. The map was defined by algebra inclusions, so changing the splitting does not change it.

Successive reductions compose: for \(U\subset U_1\subset A\), both composites in (PF.16) are induced by the same inclusion of their common Clifford subalgebra. This proves the cocycle, rather than choosing signs on each overlap.

The determinant pairing (PF.10) respects this reduction. First check a transverse factor with dual bases \(e_1,\ldots,e_d\) of \(U\) and \(\phi_1,\ldots,\phi_d\) of \(U'\). Its Clifford quotient is generated by \(1\). In the doubled exterior calculation (PF.8), this generator corresponds to the ratio of the \(e\)-volume in \(U\) and in \(W/U'\). The exact sequence starting with \(U'\) orders the full volume as \(\phi_1,\ldots,\phi_d,e_1,\ldots,e_d\), giving the sign \((-1)^{d^2}=(-1)^d\). The interchange that converts this ratio to \(\det[U'\to W/U]\) gives the same sign. They cancel. The inclusion \(U'\to W/U\) identifies the two \(\phi\)-volumes, so the determinant contraction is \(1\), exactly the square of the distinguished Clifford class. For the remaining factor, use (PF.15), (PF.8) and their ordered exterior bases. The signs from the factor interchanges are the same graded interchanges as in
\[
 \det A=\det U\otimes\det\bar A,\quad
 \det B=\det\bar B\otimes\det U^\vee,\quad
 \det W=\det U\otimes\det\bar W\otimes\det U^\vee.
 \tag{PF.17}
\]
Thus their cancellation is the determinant contraction of the acyclic transverse factor, with the convention of §2.3. This checks the pairing as a multilinear exterior identity. One may do one hyperbolic pair at a time using \(e\phi+\phi e=1\); associativity and the graded tensor rule give every rank. The same inclusion commutes with scalar multiplication by \(i\), so the square identification (PF.13) also respects reductions.

### 2.5. Finite residue models on the curve

Let \(V\) be a vector bundle on \(X\times S\) with a perfect symmetric pairing \(V\otimes V\to\omega_X\), and let its rank be \(r\). Such a bundle has degree \(r(g-1)\) on every fibre, since its determinant squared is \(\omega_X^r\). Thus its Euler characteristic is zero. Fix \(x\in X(k)\) and work first on a noetherian affine part of \(S\). For \(D=mx\), choose \(m\) large enough that
\[
 H^1(V_s(D))=0,\qquad H^0(V_s(-D))=0
 \quad\text{on every geometric fibre}.
 \tag{PF.18}
\]
Relative Serre generation and vanishing, and the universal cohomology complex proved in [*The moduli stack of bundles*](the-moduli-stack-of-bundles.md), §§1.1 and 4.1, supply the first condition uniformly. Projective duality there gives the second, because \(V^\vee\otimes\omega_X\simeq V\). The two-term cohomology complex has a fibrewise-surjective differential for \(V(D)\), hence a locally split surjective differential. It follows that \(H^0(V(D))\) is projective and commutes with every coefficient change, and that both vanishings in (PF.18) hold with arbitrary coefficient modules. Its rank is \(rm\).

Define
\[
 W_D=H^0(V(D)/V(-D)),\quad
 A_D=H^0(V/V(-D)),\quad
 B_D=H^0(V(D)).
 \tag{PF.19}
\]
The first two sheaves are supported on the fixed divisor, so their section modules are projective of ranks \(2rm\) and \(rm\), with all-base-change compatibility. The second vanishing in (PF.18) embeds \(B_D\) in \(W_D\). The symmetric form followed by residue gives a form on \(W_D\).

This form is perfect over the coefficient ring. On the formal disc choose a parameter \(t\), a bundle frame and a differential frame. The finite module has modes \(t^{-m},\ldots,t^{m-1}\) in each of its \(r\) coordinates. The residue of \(t^a u\) paired with \(t^b v\) is the coefficient of \(t^{-1}dt\) in their product form. Its matrix is block triangular along the antidiagonal \(a+b=-1\); that antidiagonal has the invertible constant Gram matrix. Thus the determinant is a unit. Frames and the calculation are available locally over \(S\); formal lifting of frames and its coefficient compatibility were proved in the previous lesson, §§7.6–7.9.

The residue coefficient is independent of its parameter. In characteristic zero, every Laurent differential except \(t^{-1}dt\) is a formal derivative, by integrating each mode with its nonzero integer denominator. Thus differentials modulo derivatives form the line generated by \(dt/t\). If \(u=t a(t)\) is another parameter, then \(du/u=dt/t+da/a\). The second term is the derivative of the formal logarithm of \(a(t)/a(0)\), and has residue zero. This proves parameter independence over \(k\) and over every coefficient algebra; all series used here converge in the formal \(t\)-adic sense.

We give the global residue argument needed to make \(B_D\) isotropic. Over \(k\), choose a nonconstant rational function on the smooth curve. Its local DVRs extend it to a morphism \(f:X\to\mathbb P^1\). It is finite: fibres of a nonconstant curve morphism are finite; choose a projective hyperplane avoiding the finitely many points of a fibre and remove the proper image of its intersection. The remaining projective scheme is affine over that base open, and its coordinate algebra is finite by projective coherent finiteness. These opens prove finiteness. The finite modules on the DVRs of \(\mathbb P^1\) are torsion-free, hence free, so \(f\) is finite flat. Its function-field extension is separable in characteristic zero.

Trace a rational differential through this extension. Locally the completions split into the branches above a point: idempotents of the finite residue algebra lift successively in the complete algebra, and each completed smooth DVR is \(k[[u]]\). In a branch its parameter satisfies \(z=u^e v(u)\), with \(v\) a unit. Choose its constant \(e\)-th root and solve its formal \(e\)-th root recursively, using invertibility of \(e\); a change of \(u\) makes \(z=u^e\). In the basis \(1,u,\ldots,u^{e-1}\), the field trace of \(u^j\) is zero unless \(e\mid j\), and is then \(e u^j\). This follows either by its cyclic multiplication matrix or by its \(e\) root-of-unity conjugates. As \(du=u^{1-e}dz/e\), extracting the coefficient of \(z^{-1}dz\) gives
\[
 \operatorname{Res}_{z}\operatorname{Tr}_f(\eta)
   =\sum_{p\mid z}\operatorname{Res}_p(\eta).
 \tag{PF.20}
\]
Matrix trace commutes with completion, so this computation is the trace of the original differential. On \(\mathbb P^1\), partial fractions show that a simple finite pole of residue \(c\) contributes residue \(-c\) at infinity; every higher pole and polynomial term has total residue zero. Apply that calculation to \(\operatorname{Tr}_f(\eta)\) and use (PF.20). It proves the global sum-of-residues theorem on \(X\).

For the fixed curve over an arbitrary \(k\)-algebra \(R\), sections of \(\omega_X(2D)\) are its finite \(k\)-vector space of sections tensored with \(R\). This follows directly by tensoring the finite affine Čech complex over the field. Residue is \(R\)-linear, so its sum is zero on those sections too. In particular the pairing of two sections of \(V(D)\) has zero residue sum. Hence \(B_D\) is isotropic. Regular sections have no residue, so \(A_D\) is isotropic as well. Both have half the rank of the perfect module \(W_D\); their fibre Lagrangian property and the full-rank minors give \(A_D=A_D^\perp\) and \(B_D=B_D^\perp\) over the entire coefficient ring.

The exact sequence \(0\to V\to V(D)\to V(D)/V\to0\), with (PF.18), gives the universal perfect representative
\[
 R\Gamma(X_S,V)\simeq
 [\,B_D\longrightarrow W_D/A_D\,]
 \quad\text{in degrees }0,1.
 \tag{PF.21}
\]
It retains all coefficient modules, not just field cohomology.

### 2.6. Independence of the residue cutoff and descent

If \(D\leq D'\) are both admissible divisors, the larger residue space contains
\[
 U=H^0(V(-D)/V(-D'))\subset A_{D'},\qquad
 U^\perp/U=W_D.
 \tag{PF.22}
\]
The equality follows from the finite Laurent modes of the residue pairing; no completion introduces a new finite polar part. Moreover \(U\cap B_{D'}=0\), since such an intersection would be a section of \(V(-D)\). Reducing by \(U\) in (PF.14) gives exactly \((W_D,A_D,B_D)\). The inclusion of Clifford algebras in (PF.16) therefore gives a canonical identification between their Pfaffian lines.

The cohomology representative (PF.21) changes by the acyclic transverse complex described in (PF.15). Equations (PF.10), (PF.13) and (PF.17) prove that its determinant and square identifications agree. For three cutoffs the comparison maps compose, by the actual Clifford inclusions in (PF.16). For incomparable cutoffs use a common larger cutoff; composition makes the answer independent of that larger choice.

Cover the parameter scheme by opens on which an admissible \(m\) exists. The comparisons just proved satisfy the descent cocycle, and define a line \(\mathrm{Pf}(V)\) with
\[
 \mathrm{Pf}(V)\otimes\mathrm{Pf}(V^{-})
    \simeq\det R\Gamma(X_S,V),\qquad
 c_i:\mathrm{Pf}(V)^2\simeq\det R\Gamma(X_S,V).
 \tag{PF.23}
\]
Here \(V^{-}\) has the negative form. Every quotient, reduction and cohomology comparison used above commutes with arbitrary base change. A family over a general ring and its finite presentation descend locally to a noetherian model; pulling back the construction there proves the same assertions over that ring. Independence of the model follows by passage to a common finitely generated model and the comparisons. Isometries act on the Clifford quotients and commute with the cutoffs, so all arrows descend too. This proves a line on the stack of these bundles, not merely a rule for geometric points.

### 2.7. The normalized determinant comparison

Let \(E\) have rank \(r\) and a specified determinant identification with the constant line \(\det E_0\), where \(E_0=\mathcal O_X\otimes W_0\) for a fixed vector space \(W_0\) of dimension \(r\). For a fixed line \(L\) on \(X\), write
\[
 \mathcal D_L(E)=\det R\Gamma(E\otimes L)
                   \otimes\det R\Gamma(E_0\otimes L)^{-1}.
 \tag{PF.24}
\]
We prove the family comparison without using a determinant-pairing theorem as an input. For a point \(y\), the short exact sequence for one positive modification gives
\[
 \frac{\det R\Gamma(E\otimes L(y))}
      {\det R\Gamma(E\otimes L)}
 =\det E_y\otimes\bigl(L(y)|_y\bigr)^{\otimes r}.
 \tag{PF.25}
\]
It follows by applying the determinant to the cohomology triangle and to its rank-\(r\) quotient at \(y\); the formula is an identity of line bundles over the coefficient base. The same quotient for \(E_0\) has exactly the same determinant, by the specified determinant identification. Dividing the two identities cancels those constants:
\[
 \mathcal D_{L(y)}(E)\simeq\mathcal D_L(E).
 \tag{PF.26}
\]
A negative modification is its inverse. A meromorphic section of \(L\) expresses it as \(\mathcal O(D_L)\). Apply (PF.26) to its finite positive and negative point terms, starting with \(\mathcal O\). This constructs
\[
 \mathcal D_L(E)\simeq\mathcal D_{\mathcal O}(E).
 \tag{PF.27}
\]
Changes in the order of the modifications have the same exterior permutations in numerator and denominator, so they cancel. A change of the meromorphic section multiplies by a rational function. Write it on a formal disc as \(t^a u(t)\), with \(u(0)\) a unit. The valuation factor changes the filtration by one-point quotients, already accounted for in (PF.26). On a quotient of length \(m\), multiplication by \(u(t)\) has a triangular matrix with \(m\) diagonal copies of \(u(0)I_r\), so its determinant is \(u(0)^{rm}\) for both \(E\) and \(E_0\). A change of bundle frame contributes the determinant of its transition matrix to each graded quotient; these determinants agree by the specified identification \(\det E\simeq\det E_0\). Thus every local determinant factor cancels. Away from the divisor the rational multiplication is an isomorphism of the two lattices; the exact-sequence determinant maps glue precisely these local quotient factors. Its normalized change is therefore the identity. The same calculation applies after every coefficient base change, using the formal-disc gluing in the previous lesson, §§7.1–7.3. This proves the independence and functoriality of (PF.27), including its value at \(E=E_0\). At that value numerator and denominator cancel canonically.

All cohomology determinants here are determinants of the universal finite complexes, and all point quotients are finite projective. Exact-sequence determinant identities can be checked in split bases and then descend; the divisor calculations therefore hold over rings with nilpotents. This proves the family determinant comparison required in §2.1.

### 2.8. The global half root for connected reductive groups

Choose a \(G\)-invariant nondegenerate symmetric form on \(\mathfrak g\). Such a form exists for every connected reductive group in our characteristic-zero setting: use the Killing form on its semisimple derived algebra and any nondegenerate form on its centre. The direct decomposition and its invariance were proved in the previous lesson, §§2.3 and 4.6. The same lesson proves \(\det\operatorname{Ad}=1\). Thus the determinant of \(\operatorname{ad}(P)\) is canonically the constant line \(\det\mathfrak g\), in every family.

The bundle \(V_P=\operatorname{ad}(P)\otimes\kappa\) has a perfect symmetric \(\omega_X\)-valued form. The construction of §§2.2–2.6 applies to every \(G\)-bundle family and every bundle isomorphism. Set
\[
 \mathcal L_{\kappa,i}|_P=
 \mathrm{Pf}(\operatorname{ad}(P)\otimes\kappa)
 \otimes\mathrm{Pf}(\mathfrak g\otimes\kappa)^{-1}.
 \tag{PF.28}
\]
The denominator is a constant line; its pullback to every parameter scheme is retained. Form the ratio with graded duality and the graded tensor interchanges already specified. In particular the square map on an inverse line is the dual square map with those interchanges. For a line of parity \(q\), its coefficient includes \((-1)^q\) relative to the ordinary ungraded inverse coefficient; this cancels the \((-1)^q\) from commuting the two middle factors in the square of that line divided by itself. Thus the ratio at the trivial bundle has the identity square map under its evaluation trivialization. Equation (PF.23), followed by (PF.27) for \(L=\kappa\), gives
\[
 \mathcal L_{\kappa,i}^{\otimes2}\simeq\mathcal D,\qquad
 \mathcal L_{\kappa,i}|_{P_0}\simeq k
 \quad\text{with its normalized square identification}.
 \tag{PF.29}
\]
Every map used to obtain this identity has been constructed on coefficient rings and checked on arrows. Descent along the bundle-stack atlas from the previous lesson therefore produces the line on the whole \(\operatorname{Bun}_G\). For the ordinary root gerbe (2.2), forget the parity grading after forming the ratio and its square map; the resulting ordinary line has the same square identification. No simply connectedness or semisimplicity hypothesis is needed. The central adjoint summand is a constant orthogonal bundle; orthogonal multiplicativity (PF.7) cancels its Pfaffian in the ratio (PF.28). For a torus this ratio is the trivial line. For the trivial group it is the empty determinant, also trivial.

A theta characteristic exists over our algebraically closed field. Choose any line \(A\) of degree \(g-1\), for example \(\mathcal O((g-1)x)\). The line \(\omega_X\otimes A^{-2}\) has degree zero. The connected smooth Picard group \(J\), constructed in [*The Picard functor and the Picard scheme of a curve*](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md), §§4–7, has an étale multiplication-by-two map: its differential is \(2\) times the identity at zero and everywhere by translation. Its image is an open subgroup. The complement is the union of its other open cosets, so this subgroup is closed as well; connectedness makes it all of \(J\). Hence the specified degree-zero line has a square root \(N\), and \(\kappa=A\otimes N\) is a theta characteristic. An isomorphism \(\kappa^2\simeq\omega_X\) is part of its choice.

The parity \(p(P)=h^0(\operatorname{ad}(P)\otimes\kappa)\bmod2\) is locally constant by (PF.6) and (PF.21). The square maps for \(i\) and \(-i\) differ in (PF.29) by
\[
 (-1)^{p(P)-p(P_0)}.
 \tag{PF.30}
\]
Multiplication on the root line by \(i^{\,p(P)-p(P_0)}\), taking the two parity representatives in \(\{0,1\}\), identifies the two roots with their square maps; at \(P_0\) it is \(1\). This states exactly how the auxiliary scalar choice changes the root. The existence of the twisted category in (2.2) remains intrinsic, and the chosen root now supplies its global untwisting equivalence. It supplies a root of this normalized bundle determinant, not of an arbitrary line on an arbitrary stack.

### 2.9. Coefficient examples and the Clifford picture

For one hyperbolic pair \(W=Re\oplus R\phi\), \(b(e,\phi)=1\), fix \(A=Re\). On \(M_A=R1\oplus R\phi\) the two Clifford operators are
\[
 e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
 \phi=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
 e\phi+\phi e=I.
 \tag{PF.31}
\]
For \(B=A\), the coinvariant quotient is generated by \([\phi]\), of odd parity; for \(B=R\phi\), it is generated by \([1]\), of even parity. The line exists in both cases, and its grading detects intersection parity.

Now take two hyperbolic pairs over \(R=k[\epsilon]/(\epsilon^2)\), with \(A=Re_1\oplus Re_2\), and
\[
 B=\operatorname{span}(e_1+\epsilon\phi_2,\ e_2-\epsilon\phi_1),
 \qquad
 B\longrightarrow W/A:
 \begin{pmatrix}0&-\epsilon\\ \epsilon&0\end{pmatrix}.
 \tag{PF.32}
\]
This graph is isotropic: the two mixed pairings are \(-\epsilon\) and \(\epsilon\). The operators on \(M_A=\Lambda(\phi_1,\phi_2)\) are \(\iota_1+\epsilon\,\phi_2\wedge\) and \(\iota_2-\epsilon\,\phi_1\wedge\). Their images kill \([\phi_1]\) and \([\phi_2]\) and impose
\[
 [1]=\epsilon[\phi_1\wedge\phi_2],\qquad
 Q_b(A,B)=R[\phi_1\wedge\phi_2].
 \tag{PF.33}
\]
Indeed their values on the two-form give \(\phi_2,-\phi_1\), and their values on \(\phi_1,\phi_2\) give \(1-\epsilon\phi_1\wedge\phi_2\). These list all relations. Mapping \(1\) to \(\epsilon\), both one-forms to zero, and \(\phi_1\wedge\phi_2\) to \(1\) identifies the quotient with \(R\).

In contrast, the degree-zero and degree-one cohomology modules of the matrix in (PF.32) are \((\epsilon R)^2\) and \((R/\epsilon)^2\). Neither is projective over \(R\). Thus taking the determinant of the pointwise \(H^0\) cannot define the family root. The Clifford quotient is an actual free line even in this infinitesimal example.

![Clifford contraction and exterior multiplication in one hyperbolic pair, and the free Clifford quotient for a two-pair nilpotent graph](figures/pfaffian-residue-clifford.svg)

**Figure 2. Finite coefficients underlying the family line.** The left panel shows the two basis vectors of (PF.31), with contraction \(e:\phi\mapsto1\) and exterior multiplication \(\phi:1\mapsto\phi\). The right panel shows the exact graph and relations (PF.32)–(PF.33), with \(\epsilon^2=0\). It compares the free Clifford quotient with the nonprojective cohomology modules. These are algebraic models of the finite residue construction, not sampled ranks of a geometric family. The full curve construction and descent are §§2.5–2.8. Free human-source reading for the normalized half twist is [Gaitsgory–Raskin, *Proof of the geometric Langlands conjecture I*, §1.1](https://arxiv.org/abs/2405.03599); for the Clifford and residue objects, see [Beilinson–Drinfeld, *Quantization of Hitchin's integrable system*, §§4.2–4.4](https://math.uchicago.edu/~drinfeld/langlands/QuantizationHitchin.pdf).

**Exercise 2.A.** Verify (PF.31), and compute the quotients for the coincident and transverse one-pair Lagrangians. Why is the output a line over every coefficient ring?

**Solution 2.A.** The matrix products are \(e\phi=\operatorname{diag}(1,0)\) and \(\phi e=\operatorname{diag}(0,1)\); both squares are zero. In the coincident case \(eM_A=R1\), so \(M_A/eM_A=R\phi\). In the transverse case \(\phi M_A=R\phi\), so \(M_A/\phi M_A=R1\). Both are split projections onto a free rank-one module. Their duals are the Pfaffian lines, respectively odd and even. There is no field or reducedness hypothesis in these equations.

**Exercise 2.B.** Check all relations in the nilpotent example, and explain why the kernel of (PF.32) is not a vector bundle over \(\operatorname{Spec}R\).

**Solution 2.B.** On the exterior basis \(1,\phi_1,\phi_2,\phi_1\wedge\phi_2\), the first operator has values \(\epsilon\phi_2,\ 1-\epsilon\phi_1\wedge\phi_2,\ 0,\ \phi_2\). The second has values \(-\epsilon\phi_1,\ 0,\ 1-\epsilon\phi_1\wedge\phi_2,\ -\phi_1\). Their span gives exactly (PF.33); the map to \(R\) specified there proves that no further relation survives. The matrix kernel consists of pairs annihilated by \(\epsilon\), namely \((\epsilon R)^2\). Its reduction modulo \(\epsilon\) has dimension two, so a projective kernel over the local ring \(R\) would be free of rank two and have \(k\)-dimension four. The actual kernel has \(k\)-dimension two. Thus it is not projective. Its fibrewise determinant is not a line construction compatible with this coefficient base.

**Exercise 2.C.** In (PF.25), remove the specified constant determinant identification. What term prevents the normalized cancellation? Apply the answer to the adjoint representation of a torus.

**Solution 2.C.** The two point quotients leave the ratio \(\det E_y\otimes(\det E_{0,y})^{-1}\), which is a line on the parameter scheme and need not be trivial. Equality of ranks alone does not cancel it. For the adjoint representation of a torus, the entire bundle is constant, not just its determinant. Thus that ratio is canonically trivial at every point, the two Pfaffians in (PF.28) coincide, and the normalized half root is the trivial line. Its normalized square map and its value at the trivial bundle are both the identity.

**Exercise 2.D.** For three admissible cutoffs \(D\leq D'\leq D''\), identify the isotropic modules removed in successive comparisons and verify their cocycle. Explain why a square-root choice made independently at every geometric bundle would not prove this.

**Solution 2.D.** The total removed module is \(H^0(V(-D)/V(-D''))\); its submodule \(H^0(V(-D')/V(-D''))\) has quotient \(H^0(V(-D)/V(-D'))\). Both Clifford comparison composites are induced by the inclusion of the same perpendicular subalgebra into \(\mathrm{Cl}(W_{D''})\), with those isotropic generators killed. Each transverse quotient has the distinguished class \(1\), so these maps agree over every ring, including rings with nilpotents. The determinant comparison follows the same ordered exact sequence in (PF.17), and scalar multiplication by \(i\) commutes with it. Independent pointwise root choices give neither these coefficient maps nor their composition identity; they cannot replace the descent construction.

## 3. Singular support and what nilpotence requires

For a coherent D-module on a smooth scheme, a good filtration produces a finitely generated module over
\(\operatorname{gr}\mathcal D_S=\operatorname{Sym}_{\mathcal O_S}T_S\).
Its support in \(T^*S\), independent of the good filtration, is its characteristic variety. On a smooth stack this condition is tested on smooth charts and descends. For arbitrary objects, §3.12 gives the cohomological union convention and proves its Serre and colimit rules; its union need not be closed. Thus a statement about the full category does not assign a finite good filtration to every object.

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

**Regularity theorem — not yet proved.** Under our characteristic-zero curve and group assumptions, (3.1) equals its subcategory obtained from ind-regular holonomic D-modules on affine charts, followed by descent. In particular its objects are locally ind-holonomic with regular singularities. The exact source is [AGKRRV, Corollary 16.5.6](https://arxiv.org/abs/2010.01906), headed “The regular singularity property”; [GLC I, §4.2.1 and its footnote](https://arxiv.org/abs/2405.03599) states the equality and the chartwise meaning of ind-completion. The spectral-projector construction and its geometric image and generation hypotheses remain necessary for a proof of this theorem. Sections 3.16–3.19 prove finite chart-point detection and the conditional generation argument. Sections 3.20–3.22 verify the nilpotent chart dimension hypothesis and its full unbounded detection consequence; regularity still requires the spectral construction.

The word “ind” matters. An infinite direct sum of regular connections is an allowed object, with no finite-rank assertion. On an unbounded stack, one must also distinguish global compactness, chartwise constructibility, and coherent or holonomic cohomology. The explicit counterexample in §5 prevents identifying these notions.

Extension from an arbitrary open can add characteristic directions at its boundary. Sections 3.2–3.15 prove that both extensions preserve nilpotent support on a cofinal system of suitable bounded opens, including arbitrary unbounded inputs. The free [AGKRRV paper, §19, “Preservation of nilpotence of singular support”](https://arxiv.org/abs/2010.01906v2), is further reading. The theorem does not assert preservation for every open.

### 3.2. The cotangent relation for proper direct image

We first prove a support estimate for bounded coherent D-modules. The large nilpotent category will require a further argument; no ind-completion assertion is part of this estimate.

Let \(f:V\to Z\) be a proper morphism of smooth finite-type schemes in characteristic zero. Write
\[
 C_f=V\times_ZT^*Z,
 \qquad a(v,\eta)=(v,df_v^*\eta),
 \qquad b(v,\eta)=(f(v),\eta).
                                                        \tag{NS.1}
\]
For a bounded coherent complex, \(\operatorname{Ch}\) means the union of the characteristic varieties of its cohomology modules. Then
\[
 \operatorname{Ch}(f_{\mathrm{dR},*}M)
       \subset b\bigl(a^{-1}\operatorname{Ch}(M)\bigr).
                                                        \tag{NS.2}
\]
The image on the right is closed: \(b\) is the base change of a proper morphism. The estimate also proves that the direct image is bounded and coherent. We give the argument, including the filtration step.

It suffices to treat one coherent right D-module and an affine open in \(Z\). Choose a good filtration \(F\) of \(M\), locally bounded below. Independence of good filtrations is proved in [*Good filtrations and the characteristic variety*](../../GL-DMOD/src/good-filtrations-and-the-characteristic-variety.md). We spell out the global lattice needed for this proof.

If \(K\) is a quasi-coherent sheaf on a Noetherian scheme and \(H\subset K|_U\) is coherent on a quasi-compact open, it extends to a coherent subsheaf of \(K\). First suppose the scheme is affine. Cover \(U\) by finitely many principal opens \(D(f_i)\), and lift finite generators of \(H|_{D(f_i)}\) to fractions of sections of \(K\). Multiply their numerators by a sufficiently large power of \(f_i\). The resulting sections belong to \(H\) on all of \(U\): their classes modulo \(H\) vanish on \(D(f_i)\), so are killed by powers of \(f_i\) on each chart of a finite cover of \(U\). A common exponent works. They still generate on \(D(f_i)\). The finite module generated by all these sections therefore restricts exactly to \(H\). For a general Noetherian scheme, adjoin one member of a finite affine cover at a time. The affine assertion extends the current coherent submodule across that chart with exactly the same restriction on the overlap; glue the two equal submodules there. This gives the assertion on the entire scheme.

Now choose finitely many local D-generators of \(M\). Extend the coherent \(\mathcal O\)-submodules that they generate by the preceding assertion, and take their finite sum \(F_0\). It generates \(M\) over \(\mathcal D_V\). Set \(F_pM=F_0\,F_p\mathcal D_V\), and set it to zero for negative \(p\). These are locally finite \(\mathcal O_V\)-modules, and their graded module is finite over \(\operatorname{Sym}T_V\). This supplies a global good filtration without requiring that \(V\) be affine or projective.

The transfer module is resolved by its Spencer complex. After tensoring with \(M\), its terms are
\[
 M\otimes_{\mathcal O_V}\bigwedge^r T_V
       \otimes_{\mathcal O_V}f^*\mathcal D_Z,
 \qquad 0\le r\le\dim V .                              \tag{NS.3}
\]
Use the total order filtration, with the exterior term shifted so that the differential has filtration degree zero. This computes the derived transfer tensor, even when \(M\) has \(\mathcal O_V\)-torsion. Indeed, before tensoring, the Spencer terms are flat left \(\mathcal D_V\)-modules. Their graded differential is the Koszul differential for
\[
 \xi_V-df^*\xi_Z                                      \tag{NS.4}
\]
in \(\operatorname{Sym}T_V\otimes_{\mathcal O_V}f^*\operatorname{Sym}T_Z\). These form a regular sequence: successively eliminate the fibre coordinates \(\xi_V\), each of which has coefficient one. Thus the untensored complex is a resolution of the transfer module. The finite Koszul argument and the chain rule are the same ones used in [*Inverse images*](../../GL-DMOD/src/inverse-images.md).

The associated graded of (NS.3) is the Koszul complex for (NS.4) with coefficients in
\(\operatorname{gr}_F M\otimes f^*\operatorname{Sym}T_Z\). Every element of (NS.4) acts null-homotopically on this complex: wedge insertion supplies the homotopy. Its cohomology is therefore killed by the ideal of the cotangent relation. It is coherent on that relation, and its support lies in
\[
 a^{-1}\operatorname{Ch}(M)\subset C_f .                \tag{NS.5}
\]
This assertion concerns cohomology, not the individual Spencer terms, which need not be finite over \(f^*\operatorname{Sym}T_Z\). To fix the derived object being pushed, put \(T=T^*V\times_V C_f\) and regard the graded coefficient module as a sheaf on \(T\). The cotangent relation gives a closed immersion \(\iota:C_f\hookrightarrow T\). The graded Koszul complex is the underlying complex of its derived restriction \(L\iota^*\). Indeed tensoring a free resolution of the coefficient module with \(\mathcal O_{C_f}\) computes this restriction, whereas resolving \(\mathcal O_{C_f}\) by the monic Koszul complex computes the same derived tensor. In (NS.6), \(\operatorname{gr}(\mathrm{Sp}_fM)\) denotes that derived restriction on \(C_f\); we do not push the individual ambient Spencer terms by a map defined only on the relation.

Push the graded complex to \(T^*Z\). Its cohomology is coherent by proper coherent direct image, proved in [*Coherence of higher direct images under proper morphisms*](../../AG-QC/src/proper-morphisms-and-coherent-direct-images.md), Theorem 4.1. Apply that theorem to \(b:C_f\to T^*Z\); its hypotheses hold after the affine change of base \(Z\leftarrow T^*Z\). A finite affine cover computes quasi-coherent cohomology in a fixed finite range. The Spencer length is also finite. The hypercohomology spectral sequence therefore has finitely many cohomological rows, with coherent terms supported in the closed set on the right of (NS.2).

Here is why passing back from the graded complex loses no support information. Compute the filtered pushforward by a finite Čech complex on \(V\). Its filtration is exhaustive and has a common lower bound; every filtration piece of each Spencer term is \(\mathcal O_V\)-coherent. The first page of the resulting filtration spectral sequence is
\[
 E_1^i=\mathcal H^i Rb_*\operatorname{gr}(\mathrm{Sp}_fM),
                                                        \tag{NS.6}
\]
where the filtration grading is retained. The direct sum over the finite range of \(i\) is a finite graded module over \(\operatorname{Sym}T_Z\), on each affine chart of \(T^*Z\). All differentials are linear over that ring: they commute with the filtered right \(\mathcal D_Z\)-action, and a commutator lowers the order filtration.

Let \(B_r\subset E_1\) be the accumulated boundaries through page \(r\), pulled back to the first page. They form an increasing sequence of graded submodules. Noetherianity gives \(B_r=B_{r+1}=\cdots\) for some finite \(r\). Each subsequent differential has image measured by the next quotient of boundaries, so it is zero. The pages consequently stabilize at a finite stage. The common lower bound of the original filtration and this finite stabilization give an exhaustive separated induced filtration on the cohomology of the pushforward, whose graded module is \(E_\infty\). One can check convergence directly. Fix a filtration degree \(p\) and represent a class on the stable page by an approximate cycle. Each lifting correction lowers the degree of its differential. The next obstruction is precisely the corresponding later differential of the spectral sequence and vanishes after stabilization. Continue until that differential reaches the common lower bound, when it is zero. Only finitely many corrections occur for this fixed \(p\). A genuine boundary likewise has a primitive of finite filtration degree, so it appears among the accumulated boundaries and cannot survive the stable page. No completion or infinite-order boundary is introduced. The induced filtration is good, because \(E_\infty\) is a finite graded subquotient of \(E_1\). Its support is contained in the support of \(E_1\). This proves (NS.2) and coherence. The finite Čech and Spencer lengths prove boundedness.

For a bounded coherent complex, filter by its finite cohomological truncations. The one-module result, the exact-triangle support rule and the fixed amplitude bound give the same assertion for the complex. All density conventions and cohomological shifts in the right-module direct image leave characteristic varieties unchanged.

### 3.3. Smooth pullback and a closed embedding

Two local calculations will accompany (NS.2). If \(u:A\to Z\) is smooth, then
\[
 \operatorname{Ch}(u^!M)
  =du^*\bigl(A\times_Z\operatorname{Ch}(M)\bigr).        \tag{NS.7}
\]
Étale locally \(u\) is a projection. Its transfer tensor is the ordinary flat \(\mathcal O\)-pullback, with the trivial connection in the additional coordinates. Filter it by the pulled-back good filtration. The graded module is the flat pullback of \(\operatorname{gr}M\), with every additional tangent symbol acting by zero. Faithful flatness gives equality of supports. This proves (NS.7), and étale descent glues it. The normalization shift in \(u^!\) does not affect support.

For a closed immersion \(i:A\hookrightarrow Z\) of smooth schemes, let \(\rho:T^*Z|_A\to T^*A\) be restriction. Then
\[
 \operatorname{Ch}(i_*M)=\rho^{-1}\operatorname{Ch}(M).
                                                        \tag{NS.8}
\]
In normal coordinates the transfer module adjoins the normal derivatives freely. Give each of them order one. Its graded module is \(\operatorname{gr}M\) tensored with the polynomial ring in the normal covectors, supported over \(A\). This proves (NS.8). The underlying normal-coordinate module and its derived inverse are proved in [*Kashiwara's equivalence and singular spaces*](../../GL-DMOD/src/kashiwaras-equivalence-and-singular-spaces.md), §§1–3. These formulas apply to bounded coherent complexes by finite truncation.

### 3.4. A proper weighted blow-up

Fix positive integers \(d_1,\ldots,d_n\), with \(n>0\). Put \(E=\mathbb A^n\), and let \(\mathbb G_m\) act by \(\lambda v_i=\lambda^{d_i}v_i\). Define
\[
 Q=[(E\setminus0)/\mathbb G_m],\qquad
 B=[(\mathbb A^1_t\times(E\setminus0))/\mathbb G_m],
 \quad\lambda(t,v)=(\lambda^{-1}t,\lambda^{d_i}v_i).
                                                        \tag{NS.9}
\]
The map \(q:B\to Q\) is a line bundle. Its zero section is \(Q\). There is a morphism
\[
 p:B\longrightarrow E,\qquad x_i=t^{d_i}v_i .           \tag{NS.10}
\]
Outside the zero section, set \(t=1\) by the unique scaling \(\lambda=t\). Thus \(p:B\setminus Q\simeq E\setminus0\), and \(p^{-1}(0)=Q\).

Both \(Q\) and \(B\) are smooth Deligne–Mumford stacks. At \([v]\in Q\), the stabilizer is
\[
 \mu_{\gcd\{d_i:v_i\ne0\}}.                            \tag{NS.11}
\]
It is finite étale in characteristic zero. For \(t\ne0\) the extra weight \(-1\) makes the stabilizer trivial. More explicitly, on the chart \(v_i\ne0\), adjoin a \(d_i\)-th root and set \(v_i=1\). This gives étale quotient presentations by \(\mu_{d_i}\); the remaining coordinates and \(t\) form an affine space. The infinitesimal action is nonzero on the atlas, so the quotient is smooth.

We prove that \(p\) is proper. Let \(L\) be a common multiple of all \(d_i\). The coordinate power map
\[
 (v_i)\longmapsto(v_i^{L/d_i})
                                                        \tag{NS.12}
\]
is finite, equivariant for the weights \((d_i)\) on its source and the common weight \(L\) on its target, and preserves the complement of the origin. Its map of quotient stacks is finite representable: pulling back to the target atlas recovers the finite equivariant map of schemes. The common-weight quotient is a \(\mu_L\)-gerbe over \(\mathbb P^{n-1}\). On a standard projective chart it is \(B\mu_L\) times that chart, because taking an \(L\)-th root trivializes the torsor. The map \(B_T\mu_L\to T\) is proper: it has finite diagonal and finite presentation, and remains universally closed, as seen after its finite étale surjective atlas \(T\to B_T\mu_L\). Properness descends along these projective charts. Consequently \(Q\) is proper.

The morphism
\[
 (q,p):B\longrightarrow Q\times E                       \tag{NS.13}
\]
is finite representable. Pull it back to \(E\setminus0\to Q\), and work where \(v_i\) is invertible. The source algebra is generated by \(t\), with relations \(x_j=t^{d_j}v_j\); in particular \(t\) satisfies the monic equation \(t^{d_i}=x_i/v_i\). It is thus finite over the target algebra. Projection \(Q\times E\to E\) is proper, so (NS.13) proves properness of \(p\). Finiteness does not assert that (NS.13) is a closed immersion.

The coherent-pushforward argument in §3.2 also applies to this particular finite-inertia source. Here are the requisite quasi-coherent facts. On the charts just described, the coarse morphism is the quotient of an affine scheme by \(\mu_{d_i}\). Taking invariants is exact: the operator \(d_i^{-1}\sum_{\zeta\in\mu_{d_i}}\zeta\) is a projection onto invariants. The invariant algebra is Noetherian and the original algebra is finite over it. To see finiteness, choose finitely many algebra generators and use for each generator its monic orbit polynomial; bounded powers of those generators span a finite module over the invariant subalgebra. Invariants of a finite module are then finite. The same statements hold after arbitrary extension of the base field and after adjoining the cotangent coordinates of \(E\), on which the finite group acts trivially.

The coarse charts glue to a proper scheme over \(E\). An explicit construction is
\[
 B_{\mathrm c}=\operatorname{Proj}
       \bigoplus_{m\ge0}J_m z^m,
 \quad J_m=(x^a:\textstyle\sum_i d_i a_i\ge m).
                                                        \tag{NS.14}
\]
The graded algebra is generated over \(k[x]\) by the finitely many \(x_i z^r\), \(1\le r\le d_i\). Indeed distribute the integer \(m\) among the available \(d_i\) units of weight for each factor of a monomial. Its Proj charts \(D_+(x_i z^{d_i})\) cover: a positive generator \(x_i z^r\) has a power divisible by \(x_i z^{d_i}\). On this chart the degree-zero monomials are exactly \(k[t,v_j:j\ne i]^{\mu_{d_i}}\), using \(x_i=t^{d_i}\), \(x_j=t^{d_j}v_j\). The equality follows by comparing the nonnegative exponent of \(t\) and the congruence \(-a+\sum_{j\ne i}d_jb_j\equiv0\pmod {d_i}\). These identifications agree on overlaps. This proves the coarse-chart construction, including separation and finite type. Properness also follows from that of \(B\): finite-group quotient charts identify the coarse topological space with the orbit space after every field extension and base change, so the image of a closed set downstairs is the image of its closed inverse image upstairs. Thus \(B_{\mathrm c}\to E\) is universally closed as well as separated and of finite type.

Exact coarse pushforward followed by proper scheme pushforward now proves coherent direct image for quasi-coherent sheaves on \(B\), with a finite cohomological bound from a finite affine cover of \(B_{\mathrm c}\). The same argument works for \(B\times_E T^*E\). Good filtrations can be chosen on \(B\). On an open chart \([V_i/\mu_{d_i}]\), apply the coherent-submodule extension argument in §3.2 to the affine scheme \(V_i\), and then take the finite sum of all its group translates. If the submodule being extended is equivariant on the open overlap, this sum restricts exactly to it. It therefore descends to the quotient chart. Adjoining these finitely many open charts and gluing their equal submodules on overlaps proves the same extension assertion on \(B\). Extend the \(\mathcal O\)-submodules generated by finite local D-generators and take their sum, exactly as in §3.2. This is a global good lattice. The Spencer calculation is étale local, so the proof of (NS.2) applies unchanged. Products with a smooth affine base \(S\) retain all these properties. In particular no coefficient of a D-module on \(S\) has been replaced by its value at a point.

### 3.5. A horizontal covector survives contraction

Let \(S\) be a smooth affine scheme, and let \(j:S\times(E\setminus0)\hookrightarrow S\times E\). Suppose that \(F\) is a bounded coherent D-module complex with strong \(\mathbb G_m\)-equivariance for the weighted action, trivial on \(S\). It descends to a bounded coherent complex \(A\) on \(S\times Q\). Coherence of the descended complex follows on the finite étale charts of \(Q\), where descent is just finite-group equivariance.

On the weighted line bundle, its extension across \(t=0\) is, locally on \(Q\),
\[
 N\boxtimes A,
 \qquad N=(j_{\mathbb G_m})_*\mathcal O_{\mathbb G_m}
       =\mathcal D_{\mathbb A^1}/
          \mathcal D_{\mathbb A^1}(t\partial_t+1),
 \quad\operatorname{Ch}(N)=\{t\tau=0\}.                \tag{NS.15}
\]
The displayed cyclic presentation uses left modules and generator \(t^{-1}\). Repeated multiplication by \(t\) and differentiation generate every Laurent monomial; the relation reduces the PBW monomials to exactly those Laurent monomials, proving the presentation. The order filtration gives the equation \(t\tau=0\). Tensor good filtrations over the field; their graded tensor is exact, and hence
\[
 \operatorname{Ch}(N\boxtimes A)
       =\{t\tau=0\}\times\operatorname{Ch}(A).           \tag{NS.16}
\]
For complexes the formula follows by finite truncation and exactness of the external tensor with \(N\). In particular the slice \(t=0,\tau=0\) imposes exactly the characteristic condition on \(A\), including its base covector.

Proper pushforward by \(\mathrm{id}_S\times p\) gives \(j_*F\), since it is the identity on the punctured open and direct images compose. Thus (NS.2) proves both its bounded coherence and the implication
\[
 ((s,0);\xi,0)\in\operatorname{Ch}(j_*F)
 \ \Longrightarrow\quad
 \text{some }v\ne0\text{ satisfies }
       ((s,v);\xi,0)\in\operatorname{Ch}(F).             \tag{NS.17}
\]
Indeed the pullback of the covector \((\xi,0)\) through the proper map has zero line and quotient components, and unchanged component \(\xi\) along \(S\). Formula (NS.16) says that \((\xi,0_Q)\) lies in \(\operatorname{Ch}(A)\). Pull it back along the smooth torsor \(E\setminus0\to Q\), using (NS.7), to obtain the covector in (NS.17).

An arbitrary covector \(((s,0);\xi,\eta_i)\) in \(\operatorname{Ch}(j_*F)\) also supplies the horizontal one in (NS.17). For \(\lambda\ne0\), equivariance and codifferential pullback at the fixed point give
\[
 ((s,0);\xi,\lambda^{d_i}\eta_i)
       \in\operatorname{Ch}(j_*F).
                                                        \tag{NS.18}
\]
Closedness lets \(\lambda\) tend algebraically to zero. More precisely the preimage of the characteristic variety under this morphism from \(\mathbb A^1\) is closed and contains \(\mathbb G_m\), and hence contains zero. The operation in (NS.18) is the **codifferential pullback**, not the covariant cotangent action, whose fibre weights have the opposite sign.

This statement also holds for a smooth positively graded affine family \(W\to S\), with fixed section \(S\), whenever there is an equivariant closed immersion \(i:W\hookrightarrow S\times E\) taking that section to zero. Such an immersion was constructed in §1.14. Put \(W^\circ=W\setminus S\). Apply the ambient result to \(i_*F\) on the punctured family. A boundary covector of \(j_{W,*}F\) lifts by (NS.8) to an ambient covector. First apply (NS.18), and then (NS.17). The resulting point belongs to \(W^\circ\), since the ordinary support of \(i_*F\) is contained in \(W\). Restricting its horizontal covector by (NS.8) gives
\[
 (s;\xi,\eta)\in\operatorname{Ch}(j_{W,*}F)|_S
 \ \Longrightarrow\quad
 \exists w\in W^\circ_s:
       (w;d\pi_w^*\xi)\in\operatorname{Ch}(F),
 \qquad\pi:W\to S.                                    \tag{NS.19}
\]
Here \(\xi\) is the restriction of the boundary covector to the fixed section. The normal covector \(\eta\) is removed by codifferential contraction; the base covector is retained throughout. All these arguments are over the whole base \(S\).

![Weighted map and horizontal covector transfer](figures/nilpotent-support-transfer.svg)

*Figure 3.3.* The map has weights \(1,2\). The plotted normal-covector path is the exact slice \((\xi,\eta_1,\eta_2)=(2,\lambda,\lambda^2)\), \(0\le\lambda\le1\); the base covector remains \(2\). The lower diagram records the two nilpotence implications used in §3.7, under its stated characteristic-support hypothesis. The closed-orbit panel is the contradiction proving the whole boundary inverse image in §3.9; its point in the complementary component is an assumption for contradiction. The last panel shows the exact integer windows of Exercise 3.H and (NU.13), with output degree seven and the stated atlas bounds.

### 3.6. Two checks of the weighted construction

Take \(d_1=1,d_2=2\). The formula is
\[
 p(t,v_1,v_2)=(tv_1,t^2v_2).                            \tag{NS.20}
\]
The point \([0:1]\in Q\) has stabilizer \(\mu_2\). On the atlas with \(v_2=1\), the group acts by \((t,v_1)\mapsto(-t,-v_1)\), and the coarse invariant algebra is
\[
 k[t,v_1]^{\mu_2}
       =k[a,b,c]/(b^2-ac),
 \quad a=t^2,\ b=tv_1,\ c=v_1^2.                       \tag{NS.21}
\]
Every invariant monomial has even total degree. If both exponents are odd, divide by \(tv_1\); if both are even, use powers of \(t^2\) and \(v_1^2\). This proves generation, and comparison of the monomial bases proves that the displayed relation is the only one. The quotient chart can therefore have a singular coarse space although the stack chart is smooth.

Over \(v=(0,1)\), (NS.13) maps \(t\) to \((0,t^2)\). Two values \(t\) and \(-t\) can have the same image after this atlas change. It is finite but is not a closed immersion. At a boundary covector \((\xi,\eta_1,\eta_2)\), the operation used in the proof is
\[
 (\xi,\eta_1,\eta_2)
       \longmapsto(\xi,\lambda\eta_1,\lambda^2\eta_2).
                                                        \tag{NS.22}
\]
It preserves the base component exactly.

**Exercise 3.A.** Determine the stabilizer of \([1:0]\) and \([0:1]\) for weights \((2,3)\), and the stabilizer at a point with both coordinates nonzero. Explain why adding a nonzero line coordinate \(t\) in (NS.9) removes every stabilizer.

**Solution 3.A.** They are respectively \(\mu_2\), \(\mu_3\), and \(\mu_{\gcd(2,3)}=1\). A stabilizing scalar with \(t\ne0\) must satisfy \(\lambda^{-1}t=t\), and therefore \(\lambda=1\). This uses the line coordinate as well as the weighted projective coordinates.

**Exercise 3.B.** For weights \((1,2)\), compute the codifferential pullback at the fixed point and the covariant cotangent action. Which operation extends to \(\lambda=0\) on all covectors?

**Solution 3.B.** The tangent map is \(\operatorname{diag}(\lambda,\lambda^2)\), so codifferential pullback multiplies covector components by \(\lambda,\lambda^2\). The covariant cotangent action uses the inverse transpose and multiplies them by \(\lambda^{-1},\lambda^{-2}\). Only the first operation extends on all covectors to zero, where it gives the zero normal covector. A covector in an additional fixed base direction is unchanged by both operations.

**Exercise 3.C.** Let \(j:\mathbb A^2\setminus0\hookrightarrow\mathbb A^2\). Compute \(j_*\mathcal O_{\mathbb A^2\setminus0}\) as a complex of left D-modules. Does extension preserve zero characteristic support in this example?

**Solution 3.C.** Use the cover \(D(x)\cup D(y)\). The complex is
\[
 [\ k[x,y,x^{-1}]\oplus k[x,y,y^{-1}]
       \longrightarrow k[x,y,x^{-1},y^{-1}]\ ],
 \quad (a,b)\longmapsto b-a .                           \tag{NS.23}
\]
The kernel is \(k[x,y]\). In the cokernel only the monomials with both exponents negative remain. The class \(x^{-1}y^{-1}\) is killed by \(x\) and \(y\), and its repeated derivatives form a basis, with nonzero factorial coefficients. Hence the cokernel is \(\delta_0=\mathcal D/(\mathcal D x+\mathcal D y)\). There is no other cohomology. Consequently
\[
 \operatorname{Ch}(j_*\mathcal O)
       =0_{\mathbb A^2}\ \cup\ T^*_0\mathbb A^2 .        \tag{NS.24}
\]
Extension has added the entire boundary cotangent fibre. This is a direct reason why a suitable-open preservation theorem needs geometric hypotheses.

### 3.7. The Levi part of a nilpotent covector

Here is the Lie-algebra test needed to apply (NS.19). For a parabolic \(P\subset G\) with Levi \(M\), write \(x=x_M+x_U\in\mathfrak p\). Then
\[
 x\text{ is nilpotent in }\mathfrak g
       \quad\Longleftrightarrow\quad
 x_M\text{ is nilpotent in }\mathfrak m .               \tag{NS.25}
\]
Nilpotence includes vanishing of the reductive central component.

To prove the test, choose a faithful algebraic representation \(G\hookrightarrow GL(V)\). Intrinsic nilpotence is equivalent to nilpotence in this representation. For the derived algebra, this follows from preservation of Jordan decomposition in [*Complete reducibility: Casimir elements and Weyl's theorem*](../../RT-LIE/src/RT-LIE-04.md), Theorem 5.1, proved there over every characteristic-zero field. The connected central torus acts diagonally: its algebraic representation is a direct sum of character spaces, as proved by the Laurent-monomial coaction calculation in §1.13. Its semisimple operator commutes with the represented semisimple and nilpotent Jordan parts of the derived algebra. The operator semisimple part is thus the image of the central component plus the intrinsic semisimple part. Faithfulness makes its vanishing equivalent to the vanishing of both components. This proves the faithful-representation criterion for a reductive algebra, including \(M\).

A central cocharacter of \(M\) gives a finite weight filtration of \(V\), on which the radical strictly raises the weights and the Levi preserves them. The existence of this integral cocharacter is proved in §1.5. In a basis ordered by these weights, \(\rho(x)\) is block triangular, with diagonal blocks the restrictions of \(\rho(x_M)\). Therefore
\[
 \det(T-\rho(x))
       =\prod_a\det(T-\rho(x_M)|_{V_a}).                \tag{NS.26}
\]
Its characteristic polynomial is \(T^{\dim V}\) precisely when every diagonal block has that polynomial. Over the algebraic closure this is equivalent to nilpotence, and extension of scalars detects the equality. The faithful-representation criterion proves (NS.25). For families the test is on every geometric fibre; characteristic support uses the resulting underlying closed nilpotent locus.

Now use the opposite family \(W\to S\) of §1.14. Its negative radical has a filtration with semistable graded pieces of slopes \(-\beta(\nu)\). For every outside positive root, §1.4 proves \(\beta(\nu)>\max(0,2g-2)\). Twisting by \(\omega_X\) gives
\[
 -\beta(\nu)+2g-2<0,
 \qquad H^0(X,\mathfrak u^-_{F_{P^-}}\otimes\omega_X)=0.
                                                        \tag{NS.27}
\]
The vanishing holds also for nonsplit \(P^-\)-bundles: the radical-height filtration has the same Levi graded bundles, and the exact-sequence induction applies to every extension. The finite projective cohomology models of §1.4 show the vanishing with arbitrary coefficient modules and after every base change. Duality identifies it with the vanishing of \(H^1((\mathfrak g/\mathfrak p^-)_{F_{P^-}})\), which is the smoothness condition for the map to \(\operatorname{Bun}_G\) proved in §1.7.

At the split section a Higgs field consequently lies in \(\mathfrak p^+\otimes\omega_X\); its negative-radical component is zero. Restriction of its cotangent vector to the Levi section retains its \(\mathfrak m\)-component, say \(\phi_M\). Suppose the punctured-family complex is the smooth pullback of a bounded coherent complex with nilpotent support, and suppose the pullback of the boundary Higgs covector lies in the characteristic variety of its star extension. Formula (NS.19) supplies at some nonsplit point a covector \(\pi^*\phi_M\) in that pullback's characteristic variety. By (NS.7) it is the pullback of a nilpotent Higgs field \(\phi'\). Restriction from \(\mathfrak g^*\) to \((\mathfrak p^-)^*\) shows that \(\phi'\) annihilates \(\mathfrak u^-\), since \(\pi^*\phi_M\) does. Under the invariant form, the annihilator of \(\mathfrak u^-\) is \(\mathfrak p^-\). Thus
\[
 \phi'\in\mathfrak p^-\otimes\omega_X,
 \qquad (\phi')_M=\phi_M .                             \tag{NS.28}
\]
The first implication of (NS.25) makes \(\phi_M\) nilpotent. The reverse implication, applied to the original field in \(\mathfrak p^+\otimes\omega_X\), makes that field nilpotent. This proves the local boundary implication for the bounded coherent case in the stated good opposite-parabolic neighbourhood. Smooth charts of the Levi stack give precisely the affine bases \(S\) used above; their additional frame directions do not alter the Higgs component.

Sections 3.8–3.11 complete the bounded boundary assembly and dual-extension argument. Sections 3.12–3.15 prove the full-category passage. Regular singularities still require the spectral projector and its generation argument.

The free [AGKRRV paper, §19](https://arxiv.org/abs/2010.01906v2), gives the weighted contraction geometry. [Ginzburg’s *Lectures on D-modules*, §1.4](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), discusses filtered resolutions and support comparison; [Schnell’s *D-modules*, Lecture 18](https://www.math.stonybrook.edu/~cschnell/pdf/notes/d-modules.pdf), treats proper coherent direct image. The support argument and the finite-quotient case required here are proved in §§3.2–3.5.

### 3.8. Characteristic support and derived duality

For a smooth scheme \(A\) of dimension \(d\), the bounded coherent dual is
\[
 \mathbb D_A K=
 R\mathcal Hom_{\mathcal D_A}(K,\mathcal D_A)
       \otimes_{\mathcal O_A}\omega_A^{-1}[d]
                                                        \tag{ND.1}
\]
when \(K\) is a left module; the density line changes the right output back to a left module. The finite local operator resolutions and biduality are proved in [*Holonomic D-modules and duality*](../../GL-DMOD/src/holonomic-d-modules-and-duality.md), Lemma 3.0 and equation (3.4). Their hypotheses are bounded coherent algebraic complexes, with no regular-singularity assumption. In particular every coherent module locally has a strict filtered free resolution of length at most \(2d\). We use that actual bound rather than a holonomic Ext-concentration statement.

Let \(a:T^*A\to T^*A\) send a covector to its negative. Then
\[
 \operatorname{Ch}(\mathbb D_A K)
       =a\operatorname{Ch}(K)=\operatorname{Ch}(K).
                                                        \tag{ND.2}
\]
Here the last equality uses conicity. To prove the first containment, first take a coherent module \(K\) and its strict filtered resolution \(P^\bullet\). Filter \(\operatorname{Hom}_{\mathcal D_A}(P^\bullet,\mathcal D_A)\) by the shifts of its finite free terms. Its associated graded is
\[
 \operatorname{Hom}_{\operatorname{Sym}T_A}
       (\operatorname{gr}P^\bullet,\operatorname{Sym}T_A).
                                                        \tag{ND.3}
\]
Every cohomology module of (ND.3) is supported on \(\operatorname{Ch}(K)\). Indeed, off that support the resolved module is zero. Its finite projective resolution is split exact there: split its last surjection onto its final projective term, remove that two-term summand, and continue. Its Hom complex is consequently exact there too. The cohomology of (ND.3) is finite, since its terms are finite over the Noetherian symbol algebra.

The filtered spectral-sequence argument of §3.2 now gives good filtrations on the dual cohomology and support contained in that graded support. There are finitely many free terms, a common lower filtration bound, and a finite first page; the accumulated-boundary stabilization used for (NS.6) applies. Formal transpose has leading symbol
\[
 \sigma(t_\eta P)(x,\xi)=\sigma(P)(x,-\xi).
                                                        \tag{ND.4}
\]
For a vector field, its transpose is the negative vector field minus its divergence; the divergence has order zero. The product rule then proves (ND.4) for every operator. This gives the containment in (ND.2) after side change. Finite truncation triangles prove it for bounded coherent complexes. Apply the containment again to \(\mathbb D_AK\), and use biduality. Since \(a^2=1\), the reverse containment follows. Tensoring by any line changes neither the symbol algebra nor this calculation.

The same duality glues on a smooth stack, with the atlas normalization retained. If \(u:A\to Y\) is smooth of relative dimension \(r\), write its normalized chart object as \(u^!K[-r]\). The relevant compatibility is
\[
 u^!(\mathbb D_YK)[-r]
       \simeq\mathbb D_A\bigl(u^!K[-r]\bigr).
                                                        \tag{ND.5}
\]
We explain the compatibility rather than treating the shift as immaterial. Étale locally a smooth map is a projection with \(r\) extra coordinates. Ordinary left-module pullback tensors with the trivial connection in those coordinates. Resolve that connection by the commuting vertical derivatives. The Koszul complex has length \(r\); its dual has only its top cohomology, the vertical density line, in degree \(r\). The inverse-density side change in (ND.1) cancels that line, and the dimension shift cancels this Koszul degree. Thus duality commutes with ordinary pullback. Since exceptional pullback is ordinary pullback shifted by \(r\), its dual has the opposite shift. Equivalently \(\mathbb D u^!=u^!\mathbb D[-2r]\), which is exactly (ND.5). For a variable tangent frame the top exterior line is the determinant of that frame, so the construction agrees on overlaps. The chain-rule transfer and its composition identify the comparison maps on iterated projections. They therefore satisfy the smooth-nerve cocycle.

Apply these comparisons to the smooth-nerve definition of D-modules from §1.12. The local bounded coherent duals give a Cartesian object; their intrinsic evaluation maps give its biduality. This defines \(\mathbb D_Y\) on objects whose normalized smooth-chart complexes are bounded coherent. This is a chartwise finiteness condition, and does not declare those objects globally compact. By (NS.7), (ND.2) and descent, it preserves the nilpotent support condition. The invariant nilpotent cone is conic and is unchanged by covector negation. The normalized half root gives the same assertions in the half-twisted category: the line side change and the sign sector of \(\mu_2\) are exactly the Morita transport of §1.15.

### 3.9. The whole inverse image of a boundary block

We strengthen a geometric point in the contraction diagram. In (GT.20) the fixed section maps by an open immersion into the inverse image of the locally closed block. On the open image where the block is closed, that inverse image is in fact the entire fixed section.

Work after a smooth affine Levi chart \(S\). Let \(\pi:W_S\to S\) be the positive affine contraction and \(s:S\hookrightarrow W_S\) its section. Let \(f:W_S\to V\) be the smooth bundle map, where the boundary block \(Z\subset V\) is closed. The earlier diagram proves an open immersion
\[
 s(S)\hookrightarrow f^{-1}(Z).
                                                        \tag{ND.6}
\]
The section is also closed in \(W_S\). Consequently the complementary substack
\(C=f^{-1}(Z)\setminus s(S)\) is closed in \(W_S\): it is the complement of the open substack (ND.6) in a closed substack. For every unit \(t\), inner conjugation gives a coherent isomorphism \(f\rho_t\simeq f\), as proved in §1.7. Both \(f^{-1}(Z)\) and the fixed section are therefore stable, so \(C\) is stable under the unit action.

Suppose \(C\) had a geometric point \(w\). The orbit map
\[
 \mathbb A^1\longrightarrow W_S,
 \qquad t\longmapsto\rho_t(w)
                                                        \tag{ND.7}
\]
lies in \(C\) for every nonzero \(t\), and its value at zero is \(s\pi(w)\). The inverse image of the closed set \(C\) is closed and contains the dense open \(\mathbb G_m\), so it contains zero. This contradicts the definition of \(C\). Thus \(C\) has no geometric point and is empty. An open immersion with the same underlying points as its target is an isomorphism, including over nonreduced rings. Hence
\[
 f^{-1}(Z)=s(S)
                                                        \tag{ND.8}
\]
as substacks, not merely as a set of bundles. This argument applies after every base change, and smooth descent gives the corresponding equality before choosing \(S\).

The same reasoning verifies the locality needed below. Let \(O\subset V\) be any open. Replace \(S\) by the open on which \(f s\) belongs to \(O\). On every fibre over that open, \(f^{-1}(O)\) is a unit-stable open containing the fixed section. If its closed complement contained a geometric point, its contracting orbit would again force the fixed point into that complement. Thus
\[
 W_S\big|_{(fs)^{-1}(O)}\longrightarrow O .             \tag{ND.9}
\]
The full affine fibres remain available. The root cohomology estimates, smoothness, positive grading and equality (ND.8) survive this open base change. We can therefore apply the local support proof on ambient open restrictions without assuming that a sheaf on such an open already extends to a nilpotent sheaf on the original ambient stack.

Now let \(K\) on \(V\setminus Z\) have bounded coherent normalized chart complexes and nilpotent support. Equality (ND.8) gives the actual Cartesian open square with \(W_S\setminus s(S)\). Smooth open base change, proved by the localization complexes in [*Adjunctions, base change and the projection formula*](../../GL-DMOD/src/adjunctions-base-change-and-the-projection-formula.md), §§1–2, identifies
\[
 f^!j_*K\simeq j_{W,*}f^!K,
 \qquad j:V\setminus Z\hookrightarrow V .              \tag{ND.10}
\]
The affine chart's complex is strongly equivariant, because the coherent inner-conjugation isomorphisms act on its pullback from the bundle stack. Section 3.5 proves bounded coherence of the right side. The smooth charts over the Levi base cover \(W\), and \(W\to V\) is smooth surjective onto its image. Bounded coherence therefore descends. At a boundary Higgs covector, (NS.7) and (ND.10) supply precisely the characteristic-support hypothesis of §3.7. Its parabolic calculation makes that covector nilpotent. Off the boundary, the support is already nilpotent by the hypothesis on \(K\). We have proved
\[
 j_*K\text{ is chartwise bounded coherent and nilpotent}
                                                        \tag{ND.11}
\]
for a single good boundary block, including every open restriction in (ND.9).

### 3.10. Finite boundary assembly and the dual extension

Take nested bounded cuts \(U_\theta\subset U_{\theta'}\) of §1.9, with
\(\alpha_i(\theta)\ge\max(0,2g-2)\) for every simple root. Retain the fixed integral central and torsion labels; finite unions of such components are also allowed. Their closed difference is covered by finitely many locally closed admissible root blocks, by §§1.3 and 1.9. Each block has the smooth contraction neighbourhood of §1.7 and the stronger inverse-image equality (ND.8).

We prove star preservation by induction on the number of these blocks. The argument is local on the bounded ambient stack \(Y\). For a block \(Z_i\), choose its good neighbourhood and remove \(\overline Z_i\setminus Z_i\), so it is closed there. These neighbourhoods, together with \(Y\setminus Z\), cover \(Y\), where \(Z\) is the whole closed difference. A finite subcover exists because \(Y\) is quasicompact. On the neighbourhood of \(Z_i\), first extend from \(Y\setminus Z\) to the complement of \(Z_i\). The remaining difference is covered by the other blocks restricted to that complement. By (ND.9) they retain the single-block property. Induction gives a bounded coherent nilpotent extension to this intermediate open. Extend it once more across \(Z_i\), using (ND.11). Composition of open direct images gives the direct extension across the whole difference. Away from \(Z\) there is nothing to extend. Bounded coherence and the characteristic condition are checked on smooth charts and are local on this finite open cover. This proves
\[
 j_*:\operatorname{Dmod}^{b,\mathrm{coh}}_{1/2,\operatorname{Nilp}}
                      (U_\theta)
 \longrightarrow
 \operatorname{Dmod}^{b,\mathrm{coh}}_{1/2,\operatorname{Nilp}}
                      (U_{\theta'}).
                                                        \tag{ND.12}
\]
The notation here means bounded coherent normalized chart complexes. It does not require global compactness on a stack, nor does it denote the full unbounded nilpotent category.

For this bounded class put
\[
 j_!K=\mathbb D_{U_{\theta'}}
                   j_*\mathbb D_{U_\theta}K .           \tag{ND.13}
\]
Equations (ND.2), (ND.5) and (ND.12) make the result bounded coherent and nilpotent. We check that it agrees with the left extension constructed in §1.15, rather than merely assigning that name to a dual complex.

On a smooth affine chart of the target and its open inverse image, a bounded coherent operator complex is compact. Its finite local free resolutions give compactness on affine opens, and the finite Zariski mapping-fibre argument (FT.2) glues compactness on a quasicompact smooth scheme. For bounded coherent test objects \(N\), biduality and the ordinary star adjunction give
\[
 \operatorname{RHom}(\mathbb D j_*\mathbb DK,N)
   \simeq\operatorname{RHom}(\mathbb DN,j_*\mathbb DK)
   \simeq\operatorname{RHom}(K,j^*N).
                                                        \tag{ND.14}
\]
On these charts the source in the first Hom is coherent by (ND.12), and hence compact; \(K\) is compact on the open too. Both sides commute with colimits in \(N\). Free operator modules generate the affine categories, and their restrictions generate the categories on the quasicompact opens, by the star adjunction and its full faithfulness. Thus the equality extends from coherent tests to every chart object \(N\). These identities are natural: they are built from the intrinsic bidual evaluation and the transfer adjunction. The smooth comparison (ND.5) and open base change identify them on every term of the smooth nerve. Taking the limit of its mapping complexes proves (ND.14) for all \(N\) on the stack. This argument uses no interchange of that limit with a colimit and makes no compactness claim about \(K\) on the stack itself.

The uniqueness of a left adjoint identifies (ND.13) with the existing full extension functor when its input is in this bounded class. We have therefore proved both bounded extension assertions
\[
 j_*,j_!:
 \operatorname{Dmod}^{b,\mathrm{coh}}_{1/2,\operatorname{Nilp}}(U_\theta)
       \longrightarrow
 \operatorname{Dmod}^{b,\mathrm{coh}}_{1/2,\operatorname{Nilp}}(U_{\theta'}).
                                                        \tag{ND.15}
\]
The cuts remain cofinal among bounded opens, with every genus and every connected reductive group included. Sections 3.12–3.15 provide the supported-heart and finite-amplitude passage to the full nilpotent category. No equivalence with the ordinary derived category of that heart, or ind-completion of globally compact holonomic objects, is used. Regular singularities remain to be proved by the spectral projector.

**Exercise 3.D.** In the proof of (ND.8), can a nonempty closed unit-stable subset of \(W_S\) avoid the fixed section? Explain why the conclusion gives equality as substacks, including nonreduced test rings.

**Solution 3.D.** A geometric point of such a subset would give a contracting orbit whose nonzero values lie in the subset. Closedness forces its value at zero, on the fixed section, into the subset. This is impossible. Therefore the complement of the open immersion (ND.6) has no point and is empty. The open immersion consequently has the entire target as its image and is an isomorphism. A bijection on geometric points alone would not exclude a nilpotent thickening. Here the map is already a schematic open immersion, by (GT.20); that hypothesis is essential.

**Exercise 3.E.** Why would finite boundary induction fail if single-block preservation were known only for restrictions of objects already defined on the original larger open? Locate the remedy in the proof.

**Solution 3.E.** The intermediate extension is an object on a smaller complement; it need not have a nilpotent extension to the larger open where the original block was constructed. Applying a theorem only to restrictions of such extensions would assume the result being proved. Equation (ND.9) retains the entire positive affine family over the smaller fixed-section base, and the local proof (ND.10)–(ND.11) applies to every bounded coherent nilpotent object on that smaller complement. This supplies the induction hypothesis without a circular extension assumption.

### 3.11. The finite cohomological window

Here is the exact categorical step that a full support-preservation proof must use. Let \(T:\mathcal C\to\mathcal E\) be an exact functor of stable categories with t-structures. Suppose there are integers \(A\le B\) such that
\[
 T(\mathcal C^{\ge0})\subset\mathcal E^{\ge A},
 \qquad
 T(\mathcal C^{\le0})\subset\mathcal E^{\le B}.
                                                        \tag{NW.1}
\]
These hypotheses concern arbitrary objects in the two aisles. A bound only on the heart is not being substituted for them. For every \(M\in\mathcal C\) and integer \(n\), its image cohomology is determined by a finite window:
\[
 H^n(T M)
   \simeq H^n\!\left(T\,
       \tau_{[n-B,n-A]}M\right).
                                                        \tag{NW.2}
\]
The isomorphism means the two natural comparisons through the lower truncation; it does not require a map from that finite window to \(M\) in an arbitrarily chosen direction.

Indeed, apply \(T\) to the triangle with lower term \(\tau_{\le n-B-1}M\). The image of that lower term lies in \(\mathcal E^{\le n-1}\), by (NW.1), so both its degree-\(n\) and degree-\(n+1\) cohomology vanish. Thus \(H^n(TM)\) equals \(H^n(T\tau_{\ge n-B}M)\). Now truncate this last input above \(n-A\). The discarded term lies in \(\mathcal C^{\ge n-A+1}\), so its image lies in \(\mathcal E^{\ge n+1}\). Its degree-\(n-1\) and degree-\(n\) cohomology vanish. The remaining input is exactly the window in (NW.2). The two long exact sequences prove the assertion. There is no exchange of \(T\) with an infinite Postnikov limit.

For a quasicompact open immersion of our bounded stacks, the star functor has such a bound on the entire D-module category. Choose finitely many smooth affine charts of the target. In each chart the inverse image of the source is a quasicompact open, covered by finitely many principal opens. If at most \(N\) principal opens are required, its alternating localization complex has cohomological degrees \(0,\ldots,N-1\). Each localization is flat and exact on every underlying operator complex. Consequently, for all complexes and all integers \(a,b\),
\[
 j_*(\mathcal C^{\ge a})\subset\mathcal E^{\ge a},
 \qquad
 j_*(\mathcal C^{\le b})\subset\mathcal E^{\le b+N-1}.
                                                        \tag{NW.3}
\]
Take the maximum \(N\) over the finite atlas. The normalized smooth pullbacks are t-exact and jointly conservative, and open base change identifies their star images with these localization complexes. This proves (NW.3) on the stack. The finite complex also commutes with colimits; none of these assertions imposes a boundedness condition on its input.

To turn (ND.15) into the full nilpotent theorem, one must still verify the precise supported-heart criterion and approximation on the strong stack category, and the full lower cohomological bound for the left extension. If every supported heart object is a filtered colimit of bounded coherent supported objects, continuity first gives preservation on that heart. If the support condition is detected on all cohomology objects, (NW.2) then gives preservation on every object for a functor satisfying (NW.1): a finite window has a finite Postnikov filtration, and exactness and the Serre support rule retain the condition through that filtration. This is a proved implication with explicitly stated hypotheses. Sections 3.12–3.15 verify those additional stack and left-extension hypotheses and apply it to the full category.

**Exercise 3.F.** A functor has full cohomological amplitude \([0,2]\) in the sense of (NW.1). Which input cohomological degrees can affect \(H^5(TM)\)? Would bounds on bounded inputs alone suffice to invoke the proof?

**Solution 3.F.** Equation (NW.2) gives the window \([3,5]\). The proof discards tails that can be unbounded, so it requires the two full aisle bounds (NW.1). A bound verified only for bounded inputs cannot be applied to those tails without a further argument. Formula (NW.3) supplies that further argument for star extension, directly on arbitrary complexes.

The free [AGKRRV paper, §19 and the appendix section on support for nonquasicompact stacks](https://arxiv.org/abs/2010.01906v2), provides further reading on suitable-open preservation and its finite-amplitude passage. [Ginzburg’s *Lectures on D-modules*, §1.4](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), treats the filtered Hom construction. The duality support estimate, the whole inverse image of the block, and the finite bounded extension argument used here have been proved above.

### 3.12. Support on the entire D-module category

We make the large support convention of §3 precise. On a smooth affine scheme \(A\), let \(R=\Gamma(A,\mathcal D_A)\). For an arbitrary left operator module \(M\), put
\[
 \operatorname{SS}(M)=
   \bigcup_{L\subset M,\ L\text{ finite over }R}
                 \operatorname{Ch}(L),
 \qquad
 \operatorname{SS}(K)=\bigcup_{n\in\mathbb Z}
                 \operatorname{SS}(H^nK).
                                                        \tag{NU.1}
\]
The first union uses genuine submodules. No filtration on the infinite module, boundedness of the complex or finite rank is required. For a coherent module its own inclusion occurs in the union, and all other terms have characteristic variety contained in its variety by the exact-sequence support rule. Thus (NU.1) gives the original characteristic variety on coherent modules. It gives the union of the cohomology characteristic varieties on bounded coherent complexes. For arbitrary complexes the union need not be closed; we retain that union rather than take its closure. This is the cohomological extension of support used for the full category in (3.1).

The Noetherian property needed here is proved in [*Differential operators and the Weyl algebra*](../../GL-DMOD/src/differential-operators-and-the-weyl-algebra.md), §5. Every module is the filtered union of its finite submodules, and these are finitely presented. For a closed conic subset \(\Sigma\subset T^*A\), the condition \(\operatorname{SS}(M)\subset\Sigma\) is a Serre condition on all modules. To check extensions, take a finite submodule \(L\) of the middle term of a short exact sequence. Its intersection with the first term is finite by Noetherianity; its image in the third is finite too. The coherent exact-sequence rule gives
\[
 \operatorname{Ch}(L)
   =\operatorname{Ch}(L\cap M')\cup
       \operatorname{Ch}(\operatorname{im}(L\to M''))
 \quad\text{if }0\to M'\to M\to M''\to0.
                                                        \tag{NU.2}
\]
For a quotient, a finite submodule downstairs has finitely many lifted generators; their operator span is finite upstairs and maps onto it. The same rule proves the quotient assertion. The submodule assertion follows immediately from the union definition. These arguments prove all three Serre properties, including for infinite modules.

The condition also survives filtered colimits with arbitrary transition maps. A finite submodule \(L\) of the colimit is finitely presented, so its inclusion factors through one stage. The factor is injective: anything in its kernel maps to zero under the original inclusion. Thus its characteristic support is contained in the support of that stage. Images and quotients of finite supported modules also have the condition, so this argument applies whether the stages themselves are finite or infinite. The cohomological definition therefore defines a full stable category closed under colimits. Exact triangles give long exact sequences of cohomology and the Serre rule; filtered colimits are exact; coproducts are filtered colimits of finite coproducts. Realizations are built from coproducts and successive cofibres, so these checks include all colimits, not just sums of modules.

This convention is independent of the smooth chart. For a smooth map, normalized pullback is flat ordinary operator pullback. Any finite collection of sections of its pulled-back module is locally a finite sum of coefficients times sections downstairs. The operator span of those finitely many downstairs sections is coherent, and its smooth pullback contains that collection. The characteristic formula (NS.7), together with flatness, proves
\[
 \operatorname{SS}(u^\natural K)
   =du^*\bigl(B\times_A\operatorname{SS}(K)\bigr),
 \qquad u^\natural=u^![-\operatorname{reldim}(u)]
                                                        \tag{NU.3}
\]
for all complexes. In the reverse containment every coherent downstairs submodule pulls back injectively, and its coherent characteristic formula supplies its contribution to the right side. Finite presentations allow these affine arguments to be made on a common neighbourhood; they glue on any smooth scheme. Normalized smooth pullback commutes with cohomology, so the complex statement follows as well.

Consequently common smooth refinements identify the support tests on different atlases. Use the stack cotangent embedding and the normalized smooth-descent t-structure proved in [*D-modules on stacks, ind-schemes and the de Rham prestack*](../../GL-DMOD/src/stacks-ind-schemes-and-the-de-rham-prestack.md), Theorem 1.1. On a smooth stack \(Y\) and its closed conic cone \(\Sigma\), the full condition is exactly
\[
 \begin{gathered}
 K\in\operatorname{Dmod}_{\Sigma}(Y)\quad\Longleftrightarrow\quad\\
 \operatorname{Ch}(L)\subset\Sigma_A
       \text{ for every }n\in\mathbb Z\\
 \text{and every coherent }L\subset H^n(q^\natural K).
 \end{gathered}
                                                        \tag{NU.4}
\]
on a smooth affine atlas \(q:A\to Y\), with the corresponding pullback cone \(\Sigma_A\). The criterion extends to every smooth chart by (NU.3), and faithful flatness detects it back on an atlas. It is therefore a criterion on the original full unbounded D-module category. The supported subcategory is stable under the cohomological truncations and is detected on its heart cohomology. We have not identified the derived category on a quotient stack with the ordinary derived category of that heart. For the half-twisted category, apply the normalized root-line Morita equivalence before this calculation; its symbol algebra and all these support tests are unchanged.

### 3.13. Coherent approximation in the strong quotient heart

Every heart object on one of our bounded bundle opens is a filtered union of coherent strong heart subobjects. The assertion concerns objects and subobjects on the whole quotient, with the rational group action retained. An arbitrary nonequivariant finite submodule on an atlas is not enough.

First let \(Y=[Z/H]\), where \(Z\) is the smooth quasiaffine line-frame scheme and \(H=GL_a\times\mathbb G_m^s\) of §1.13. Embed \(Z\) equivariantly as a locally closed subscheme of a finite-dimensional representation \(E\) of \(H\). Here is the finite algebra behind that choice. The affine cone closure from (AF.9) has a finitely generated algebra with a rational coaction. Enlarge its finite list of algebra generators to their finite rational orbit spans. Such spans are finite-dimensional: write the coaction of a vector as a finite sum, and coassociativity shows that the span of its finitely many coefficient vectors is itself a subrepresentation. The resulting finite representation gives the closed embedding of the cone closure into an affine representation space. Its open subscheme \(Z\) is then locally closed in that space. If \(E_0\) is the complement of the closed boundary of \(Z\) in its closure, then
\[
 Z\xrightarrow{i}E_0\xrightarrow{v}E,
 \quad i\text{ closed},\qquad v\text{ quasicompact open},
                                                        \tag{NU.5}
\]
are equivariant maps, and \(E_0\) is smooth as an open in \(E\).

Let \(M\) be the strong equivariant module corresponding to a heart object on \(Y\). Kashiwara pushforward \(i_*M\) is a heart module on \(E_0\). The degree-zero open pushforward
\[
 P=H^0(v_*i_*M)
                                                        \tag{NU.6}
\]
is a quasi-coherent strong equivariant operator module on the affine scheme \(E\). These assertions also hold for infinite modules: the closed transfer is flat on its coefficient side, and the open pushforward is its finite localization complex. The rational action, its coaction and the infinitesimal moment identity commute with those constructions. Since open restriction is exact, \(P|_{E_0}=i_*M\). No support assertion on the added boundary in \(E\) is needed.

The space \(\Gamma(E,P)\) is a rational \(H\)-representation. This follows directly from equivariant quasi-coherent descent on an affine scheme: its action is a coaction into \(k[H]\otimes\Gamma(E,P)\). For any finite list of sections, choose the finite-dimensional rational subrepresentation \(V\) containing them, by the coefficient argument above. Its operator span
\[
 P_V=\mathcal D_E\,V\subset P
                                                        \tag{NU.7}
\]
is coherent, is rationally \(H\)-stable, and satisfies the strong infinitesimal identity. Coherence follows from the Noetherian operator algebra. Stability follows because the rational action on the operators is by algebra automorphisms, and the infinitesimal identity restricts from \(P\) to this stable submodule. The collection of these spans is directed by sums and exhausts \(P\).

Restrict \(P_V\) to \(E_0\). It is a coherent strong submodule of \(i_*M\), supported on \(Z\). The exact supported inverse in Kashiwara's equivalence gives a coherent strong submodule \(M_V\subset M\). It is a genuine submodule, because that inverse is exact on supported heart modules. Restriction and the inverse commute with the filtered union: in normal coordinates the inverse is the normal-annihilator module with its density line, computed by finitely many kernels, and filtered colimits are exact. Thus
\[
 M=\underset{V}{\operatorname{colim}}\,M_V,
 \qquad M_V\subset M_W\text{ whenever }P_V\subset P_W.
                                                        \tag{NU.8}
\]
Equivariant descent turns this into a filtered union of coherent subobjects on \([Z/H]\) itself. If \(M\) is supported in \(\Sigma\), every \(M_V\) is too, by (NU.4) and the submodule rule. We did not assume that the auxiliary module \(P\) has the support condition on all of \(E\).

The bounded bundle cuts admit these presentations, by the explicit frame construction in §1.13. At a fixed integral label a common large frame twist gives one quotient presentation; for a finite union of labels use the finite open-and-closed decomposition there. Apply (NU.8) in each of those components and take finite sums. This proves the assertion on every bounded cut in (ND.15). The half root transports the same subobjects and filtered union. The proof works in the strong descent heart, and does not discard the odd Cartan operators or higher descent maps on general complexes.

### 3.14. The full lower bound for left extension

We first note that coherence in §§3.5 and 3.9–3.10 did not use nilpotence. Nilpotence was needed for the characteristic implication, not for the proper weighted pushforward of \(N\boxtimes A\). Therefore both bounded extensions are chartwise bounded coherent for every bounded coherent input. The same finite boundary induction proves this statement, and the adjunction comparison (ND.14) applies once this coherence has been checked.

Fix a suitable bounded inclusion \(j:U_\theta\hookrightarrow U_{\theta'}\). Choose a finite smooth affine atlas of the target, let \(d\) bound its scheme dimensions, and let \(N\ge1\) bound the number of principal opens in the localization covers used in (NW.3). The inverse image of the source in any such chart has the same scheme dimension. For a coherent heart object \(K\), (ND.1) and the local free length bound give dual cohomology in \([-d,d]\). Star extension moves this into \([-d,d+N-1]\), by the full bound (NW.3). Applying duality once more and (ND.13) gives a bound independent of \(K\):
\[
 j_!K\in\operatorname{Dmod}(U_{\theta'})^{\ge-L},
 \qquad L=2d+N-1.
                                                        \tag{NU.9}
\]
All dimensions here refer to the fixed finite scheme atlas; normalized chart comparisons (ND.5) retain the stack shifts. This estimate makes no global compactness claim about a coherent heart object.

Now let \(M\) be any heart object. Its coherent union (NU.8) and continuity of the existing left adjoint \(j_!\) give the same lower bound for \(j_!M\). Filtered colimits commute with chart cohomology, so the lower aisle is closed under those colimits. For any \(M\in\operatorname{Dmod}(U_\theta)^{\ge0}\), the actual maps from upper truncations give
\[
 M\simeq\underset{m\ge0}{\operatorname{colim}}\,
                      \tau_{\le m}M.
                                                        \tag{NU.10}
\]
To verify the equality, pull to the normalized affine atlas. In each cohomological degree the filtered system stabilizes to that degree of \(M\); exactness of filtered colimits proves equality of all cohomology modules, and the conservative atlas and nondegenerate t-structure detect the equivalence. Each truncation in (NU.10) has a finite Postnikov filtration with pieces \(H^p(M)[-p]\), \(0\le p\le m\). Their left-extension images lie in degrees at least \(p-L\), hence at least \(-L\). Exactness and continuity prove the full lower-aisle bound.

For the full upper aisle use adjunction, not an approximation of an unbounded negative tail. If \(M\le0\) and \(Q\ge1\), t-exactness of open restriction and the existing adjunction give
\[
 \operatorname{Map}(j_!M,Q)
       \simeq\operatorname{Map}(M,j^*Q)=*.
                                                        \tag{NU.11}
\]
The right t-orthogonality criterion says exactly that \(j_!M\le0\). The two proven full bounds are therefore
\[
 j_!(\mathcal C^{\ge0})\subset\mathcal E^{\ge-L},
 \qquad j_!(\mathcal C^{\le0})\subset\mathcal E^{\le0}.
                                                        \tag{NU.12}
\]
The star amplitude remains \([0,N-1]\), by (NW.3). These are bounds on both full aisles of the strong category, with no replacement by the ordinary derived category of its heart.

### 3.15. Both extensions on the full nilpotent category

Let \(M\) be a nilpotent heart object on \(U_\theta\). Its union in (NU.8) consists of coherent nilpotent subobjects. Equation (ND.15) gives nilpotent cohomology for both extensions of each of those subobjects. The two extension functors commute with colimits; star continuity follows from the finite localization complexes and left continuity follows from adjunction. Taking the filtered colimit and applying the supported-heart rules of §3.12 proves that both extensions of \(M\) have nilpotent support in every cohomological degree.

For an arbitrary unbounded nilpotent object \(K\), (NU.4) gives nilpotent heart cohomology. A finite window of \(K\) has a finite Postnikov filtration by such heart objects. Exactness of the extension functors and the Serre support rule prove nilpotent support for their images of every finite window. We can now apply (NW.2), using the two full bounds just proved. More precisely,
\[
 H^n(j_*K)\simeq
       H^n\!\left(j_*\tau_{[n-N+1,n]}K\right),
 \qquad
 H^n(j_!K)\simeq
       H^n\!\left(j_!\tau_{[n,n+L]}K\right).
                                                        \tag{NU.13}
\]
The right sides have the nilpotent condition. Since this holds for every \(n\), (NU.4) proves the full result:
\[
 j_*,j_!:
 \operatorname{Dmod}_{1/2,\operatorname{Nilp}}(U_\theta)
       \longrightarrow
 \operatorname{Dmod}_{1/2,\operatorname{Nilp}}(U_{\theta'}).
                                                        \tag{NU.14}
\]
There is no boundedness, finite-rank, global compactness or regular-singularity assumption on the input in (NU.14).

Pass to the entire bundle stack using the cofinal cuts of §1.9. For a fixed cut \(U_i\), its global left extension has component \(j_{ik!}K\) on every later cut \(U_k\), as proved in (FT.8). Its global star extension has component \(j_{ik*}K\). Open base change identifies these components under restriction. For the star adjunction, the mapping-complex limit is
\[
 \operatorname{RHom}_{\operatorname{Bun}_G}(F,j_{i*}K)
  =\lim_{k\ge i}\operatorname{RHom}_{U_k}(F_k,j_{ik*}K)
  =\operatorname{RHom}_{U_i}(F_i,K).
                                                        \tag{NU.15}
\]
The diagram in the last equality is coherently constant by the open adjunction. This proves that the componentwise star extension is the global right adjoint, while (FT.9) already proves the global left adjoint. The composition comparisons are the intrinsic adjunction comparisons, so they retain all higher maps. By (NU.14) every later component is nilpotent. The stack condition is tested on these opens and then on their smooth charts, so
\[
 j_{i*},j_{i!}:
 \operatorname{Dmod}_{1/2,\operatorname{Nilp}}(U_i)
       \longrightarrow
 \operatorname{Dmod}_{1/2,\operatorname{Nilp}}(\operatorname{Bun}_G).
                                                        \tag{NU.16}
\]
The inequalities \(\alpha_i(\theta)\ge\max(0,2g-2)\) give the cofinal suitable cuts in every genus. Integral central and torsion labels are retained; finite unions cover the full reductive stack. If there are no roots, the degree components are already bounded and open-and-closed, so their finite-union extensions add no boundary directions. This proves suitable-open preservation for every connected reductive characteristic-zero group, including tori and every component.

Regularity is still a separate theorem. No step of (NU.14)–(NU.16) proves regular singularities, identifies the spectral projector or proves the Riemann–Hilbert comparison. Those obligations retain their original scope.

**Exercise 3.G.** Why can the finite rational orbit span in (NU.7) be used even when the auxiliary module \(P\) is infinite-dimensional? Why is a finite nonequivariant operator span insufficient?

**Solution 3.G.** A rational coaction of each vector is a finite sum. Coassociativity makes its finitely many coefficient vectors span a finite subrepresentation. A finite union of those spans contains any prescribed finite list. Its operator span is finite over the operator algebra and stable under the whole rational action. A nonequivariant operator span might move outside itself under the group; it would then define no subobject on the quotient. Strong moment compatibility is inherited only after taking a stable submodule.

**Exercise 3.H.** Suppose the chosen atlas has \(d=4\) and its source opens require at most \(N=3\) principal charts. Give the proved left bound and the two windows controlling output degree \(7\).

**Solution 3.H.** Formula (NU.9) gives \(L=2\cdot4+3-1=10\). The full left amplitude is bounded by \([-10,0]\), while star has bound \([0,2]\). Thus \(H^7(j_*K)\) is controlled by input degrees \([5,7]\), and \(H^7(j_!K)\) by \([7,17]\). These are proved bounds; neither is asserted to be optimal.

**Exercise 3.I.** Explain why (NU.10) does not permit expressing an arbitrary negative unbounded complex as the colimit of its lower truncations. Which step handles that tail?

**Solution 3.I.** The maps used in (NU.10) are from upper truncations to the original object, and their degreewise cohomology stabilizes. Lower truncations have the opposite natural comparison direction. Reversing it would change the argument. The full upper-aisle bound instead comes from adjunction in (NU.11), and the finite-window proof removes either unbounded tail using the two full aisle bounds. It never commutes an extension functor with an infinite Postnikov limit.

The free [AGKRRV paper, §19 and the appendix sections on singular support](https://arxiv.org/abs/2010.01906v2), gives further reading on this theorem and the cohomological union convention. Its constructible, ind-holonomic and renormalized categories must retain their stated meanings. The calculation here is on the full D-module category and its normalized strong descent heart. The spectral-projector argument needed for regularity remains to be proved.

### 3.16. A finite stratification adapted to characteristic support

The generation argument for a spectral projector needs test objects that detect its image. We prove the geometric detection step for the full D-module category. Let \(V\) be a smooth separated finite-type scheme, pure of dimension \(d\), over a characteristic-zero field \(k\). Let
\[
 N\subset T^*V\quad\text{be closed and conical},\qquad \dim N\le d.
                                                        \tag{FD.1}
\]
Here conical means invariant under ordinary scalar multiplication in the cotangent fibres. The support convention is §3.12: every coherent submodule of every cohomology module has its characteristic variety in \(N\). No boundedness or coherence is imposed on the object being tested. Empty support is allowed. A finite disjoint union of pure-dimensional components is handled component by component.

We first construct a finite partition into smooth connected locally closed subschemes \(S_a\) such that
\[
 c_a=d-\dim S_a,\qquad
 \dim N_v\le c_a\ (v\in S_a),\qquad
 F_c:=\bigcup_{c_a\ge c}S_a\ \text{is closed in }V.
                                                        \tag{FD.2}
\]
Fibre dimensions can be checked after an algebraic closure of the residue field. Smoothness refers to the reduced strata; the support condition and these dimensions concern underlying closed sets.

Here is a construction, including the required uniform fibre bound. Suppose that \(T\) is an irreducible component of the reduced closed set still to be partitioned, and write \(t=\dim T\). Work on an affine neighbourhood of its generic point, with coordinate domain \(A\), fraction field \(K\), and coordinate algebra \(B\) for \(N\) over that neighbourhood in \(T\). Cotangent bundles are affine over their base, so \(B\) is of finite type over \(A\). If \(B\otimes_AK=0\), one nonzero element of \(A\) kills its unit, and the fibres are empty on the resulting principal open.

Otherwise put \(r=\dim(B\otimes_AK)\). A component of the generic fibre comes from a component of \(\operatorname{Spec}B\) dominating \(T\). The tower of function fields gives
\[
 \dim(\text{that component})
   =t+\operatorname{trdeg}_K(\text{its function field}),
 \qquad r\le d-t.
                                                        \tag{FD.3}
\]
We used \(\dim\operatorname{Spec}B\le d\), since its underlying set lies in \(N\). Dimension equals transcendence degree for a finite-type domain by [*Krull dimension and Noether normalization*](../../AG-CA/src/krull-dimension-and-noether-normalization.md), Theorem 4.2. The additivity in (FD.3) also follows directly: append a transcendence basis over \(K\) to one for \(K/k\); the resulting extension of the generated field is algebraic. Taking the largest component gives the formula for the possibly reducible generic fibre.

Corollary 3.2 of that same earlier lesson gives a finite algebra over a polynomial subalgebra,
\[
 K[z_1,\ldots,z_r]\ \longrightarrow\ B\otimes_AK.
                                                        \tag{FD.4}
\]
Choose representatives for the \(z_i\). The finitely many algebra generators of \(B\) satisfy monic equations over this polynomial algebra. Clear the finitely many denominators in the representatives and in these equations. After inverting one nonzero \(f\in A\), we obtain a finite algebra over \(A_f[z_1,\ldots,z_r]\). Every fibre is therefore finite over a quotient of a polynomial ring in \(r\) variables over its residue field; its dimension is at most \(r\). The dimension bound is preserved under algebraic field extension. This proves the uniform inequality needed on an open subset of \(T\), rather than only at its generic point.

Intersect that open with the smooth dense open of \(T\), supplied in characteristic zero by [*Smooth algebras over a field and the Jacobian criterion*](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md), Corollary 3.3. Remove its intersections with the other components. To ensure the closed-filtration assertion, remove components in decreasing order of dimension: at a stage of dimension \(t\), take these disjoint smooth dense opens in all remaining \(t\)-dimensional components, leaving every smaller component in the closed remainder. Each selected open is open in that remainder, because the other components have been removed from it. After all such opens are removed, the remainder is closed and has smaller dimension. Repeat. Dimensions decrease, and each stage has finitely many components, so the construction terminates. The remainder after the strata of dimension at least \(d-c+1\) have been removed is exactly \(F_c\). This proves (FD.2). Splitting a smooth stratum into its finitely many connected components preserves the construction.

Choose one closed point in each nonempty stratum,
\[
 y_a:\operatorname{Spec}E_a\longrightarrow S_a,
 \qquad [E_a:k]<\infty.
                                                        \tag{FD.5}
\]
The existence and the finite residue-field assertion are the weak Nullstellensatz, proved in [*The Nullstellensatz and Jacobson rings*](../../AG-CA/src/the-nullstellensatz-and-jacobson-rings.md), Theorem 1.3 and §2. In characteristic zero these fields are separable. When \(k\) is algebraically closed, the points can all be \(k\)-rational. It would be incorrect to require a rational point on every stratum over an arbitrary characteristic-zero field.

### 3.17. Zero-support modules and unbounded point fibres

We record carefully the passage from finite connections to arbitrary complexes. On a smooth connected scheme \(S\), a coherent D-module of zero characteristic support is a finite-rank flat vector bundle, by the good-filtration and Taylor argument following Proposition 3.1. Thus a module \(A\) satisfying the full zero-support condition is a filtered union of such bundles:
\[
 A=\mathop{\operatorname{colim}}_i A_i,
 \qquad A_i\subset A\text{ coherent over }\mathcal D_S,
 \qquad A_i\text{ finite locally free over }\mathcal O_S.
                                                        \tag{FD.6}
\]
The union is the actual union of finitely generated submodules over the Noetherian operator algebra, not a claim of global compactness. It can be checked on affine charts. Globally the coherent-extension construction used in §3.2 places any finite set of local sections in a coherent \(\mathcal O_S\)-submodule of \(A\); its \(\mathcal D_S\)-span is coherent over the locally Noetherian operator algebra and is an actual submodule of \(A\). Thus these submodules exhaust \(A\), and a nonzero \(A\) has a nonzero global one. The support Serre rule of §3.12 implies that every quotient \(A/A_i\) has the same zero-support condition. Consequently both \(A\) and \(A/A_i\) are flat over \(\mathcal O_S\): tensoring a short exact sequence of ordinary modules with (FD.6) is exact, since filtered colimits are exact and each \(A_i\) is flat.

If \(A\ne0\), choose a nonzero \(A_i\). Its locally constant rank is positive everywhere on the connected scheme \(S\). At every point \(y\) the sequence
\[
 0\longrightarrow (A_i)_y\otimes\kappa(y)
 \longrightarrow A_y\otimes\kappa(y)
 \longrightarrow (A/A_i)_y\otimes\kappa(y)
 \longrightarrow0
                                                        \tag{FD.7}
\]
is exact, because the quotient is flat. Its first term is nonzero. This proves that one point detects every nonzero zero-support module on a fixed connected \(S\), including modules of infinite rank. Flatness of the quotient is essential; tensoring an arbitrary injection with a residue field would not justify this argument.

Now let \(L\) be any D-module complex on \(S\), and suppose that each \(H^n(L)\) has zero support. For a closed point \(y:\operatorname{Spec}E\to S\), with \(s=\dim S\), the left-transfer formula gives
\[
 y^!L\simeq
 \left(E\otimes^{\mathbf L}_{\mathcal O_{S,y}}
                 \operatorname{oblv}L_y\right)[-s].
                                                        \tag{FD.8}
\]
The shift is the same convention as the normalized smooth pullback \(q^![-\dim(q)]\) in §1.10. In particular a connection in degree zero has point \(!\)-fibre in degree \(s\).

There is a finite justification for using (FD.8) on an unbounded complex. The regular local ring at a closed point has a regular parameter sequence of length \(s\), by [*Regular local rings*](../../AG-CA/src/regular-local-rings.md), Theorem 1.1, with its parameter proof in [*Regular sequences, depth and Cohen–Macaulay modules*](../../AG-CA/src/regular-sequences-depth-and-cohen-macaulay-modules.md), Theorem 6.1. Its finite Koszul complex resolves \(E\): the one-parameter complex is the injective multiplication map with its quotient in degree zero, and induction tensors it with the next such complex; regularity makes the next multiplication injective on the preceding quotient. Tensor this finite resolution with \(\operatorname{oblv}L_y\). Its spectral sequence has only \(s+1\) columns, even though its cohomological rows may be unbounded. Flatness in (FD.6) makes all higher Tor terms zero. Hence
\[
 H^{n+s}(y^!L)
    \simeq H^n(L)_y\otimes_{\mathcal O_{S,y}}E
       \quad(n\in\mathbb Z).
                                                        \tag{FD.9}
\]
This is a finite-column argument for each total degree; it assumes no equivalence with an ordinary derived category of a stack heart. Equations (FD.7)–(FD.9) show that \(y^!L=0\) implies \(L=0\) on a connected zero-support stratum.

### 3.18. Finite points detect the full supported category

**Theorem 3.18.** Under (FD.1), the finite collection (FD.5), composed with the inclusions in \(V\), is jointly conservative on \(\operatorname{Dmod}_N(V)\). Explicitly,
\[
 M\in\operatorname{Dmod}_N(V),\qquad
 y_a^!M=0\text{ for all }a
 \quad\Longrightarrow\quad M=0.
                                                        \tag{FD.10}
\]
It applies to every unbounded complex in the cohomological support convention of §3.12.

**Proof.** Suppose \(M\ne0\). The finite closed filtration (FD.2) has a least \(c\) for which \(M\) restricts nontrivially to \(W=V\setminus F_{c+1}\). Its restriction to \(V\setminus F_c\) is zero. The localization triangle therefore makes \(M|_W\) an object supported on the smooth closed subscheme
\[
 S=F_c\setminus F_{c+1}
     =\coprod_{c_a=c}S_a\ \subset W.
                                                        \tag{FD.11}
\]
Here the components are open and closed in \(S\); equal-dimensional components only meet in the discarded lower-dimensional remainder.

Kashiwara's equivalence identifies \(M|_W\) with \(i_*L\) for an unbounded complex on \(S\). The normal-coordinate polynomial calculation and the density factor are proved in [*Kashiwara's equivalence and singular spaces*](../../GL-DMOD/src/kashiwaras-equivalence-and-singular-spaces.md), §§1–3. For clarity, the unbounded extension uses the same finite normal Koszul complex: on a supported module it has only its inverse-module cohomology, since a normal coordinate acts as a surjective lowering operator on the polynomial normal form. The finite-column spectral sequence thus gives \(H^n(i^!M|_W)=K_i(H^n(M|_W))\) for all \(n\). Its counit is the module reconstruction on every cohomology group, hence an equivalence. Direct image is exact. This justifies the equivalence and its cohomological use on \(M\).

Choose a component \(S_a\) on which \(L\ne0\). Let \(A\) be a coherent D-submodule of any \(H^n(L|_{S_a})\). Exactness and coherence of \(i_*\) make \(i_*A\) a coherent submodule of \(H^n(M|_W)\). Write \(\rho:T^*W|_{S_a}\to T^*S_a\) for restriction of covectors. The normal good filtration gives
\[
 \rho^{-1}\operatorname{Ch}(A)=\operatorname{Ch}(i_*A)
       \subset N|_{S_a}.
                                                        \tag{FD.12}
\]
The fibre of \(\rho\) over a covector is an affine space of dimension \(c\). Thus the fibre dimension on the left over a base point \(v\) is \(c+\dim\operatorname{Ch}(A)_v\), whenever that fibre is nonempty. The bound (FD.2) forces \(\dim\operatorname{Ch}(A)_v\le0\). A closed cone of dimension zero in a vector space contains no nonzero vector: over an algebraic closure the scalar orbit of a nonzero vector has dimension one. Consequently \(\operatorname{Ch}(A)\) lies in the zero section. This holds for every coherent submodule and every cohomological degree of \(L|_{S_a}\).

Equation (FD.9) now implies \(y_a^!(L|_{S_a})\ne0\). Composition of inverse images identifies this with \(y_a^!M\), since \(y_a\) lies in \(W\) and \(i^!i_*\simeq\operatorname{Id}\). This contradicts the hypothesis. \(\square\)

This theorem concerns a fixed support \(N\). The points need not detect objects whose characteristic varieties lie outside that support. It asserts detection, not the existence of a left projector onto the support subcategory.

![A real coordinate slice of the plane, its three adapted strata and detectors, and the corresponding zero, line and full cotangent fibres.](figures/finite-point-detectors.svg)

*Figure 3.4.* Take \(V=\mathbb A^2\), \(D=\{y=0\}\), and \(N\) the union of the zero section, the conormal bundle of \(D\), and the full cotangent fibre at the origin. The drawing shows a real coordinate slice of this algebraic example; it is not a dimension drawing of its complex total space. The strata are \(V\setminus D\), \(D\setminus\{0\}\), and \(\{0\}\), with detectors \((0,1),(1,0),(0,0)\). Writing a covector as \(\alpha\,dx+\beta\,dy\), their fibres in \(N\) are respectively \(\{(0,0)\}\), \(\{\alpha=0\}\), and all of \(\mathbb A^2_{\alpha,\beta}\). Each stratum dimension plus its fibre dimension is two. The projection and the full normal fibres are the ones used in (FD.2) and (FD.12); the zero-support point calculation is (FD.9).

### 3.19. From detectors to generators, and the remaining projector geometry

There are two useful extensions of the theorem. First, on a smooth stack with a finite smooth atlas, normalized atlas pullbacks are conservative by §1.10. If the induced conical support on each pure-dimensional atlas component satisfies (FD.1), apply Theorem 3.18 there. The resulting finite collection of chart pullback followed by point \(!\)-fibre functors detects all supported objects on that stack. On a chart with a chosen half line, tensoring by that line gives the operator-module equivalence of §2; it preserves characteristic support and point-fibre vanishing. Thus this detector statement applies to the half-twisted chart categories too. For a nonquasicompact stack, apply this to every member of a cofinal open exhaustion; restriction to the opens is conservative by (FT.9). Each stage has finitely many detectors. We make no additional claim that their union is locally finite as a set of intrinsic stack points.

Second, the following adjunction argument explains the generators required from an enhanced spectral projector. Let \(\mathcal B\) be a presentable stable \(k\)-linear category and suppose that
\[
 \begin{gathered}
 P:\operatorname{Dmod}(V)\rightleftarrows\mathcal B:U,
 \qquad P\dashv U,\\
 U\text{ continuous and conservative},\qquad
 U(\mathcal B)\subset\operatorname{Dmod}_N(V).
 \end{gathered}
                                                        \tag{FD.13}
\]
These are stated hypotheses; neither \(P\) nor its image is constructed by the detection theorem. Put \(\delta_a=(y_a)_*E_a\), with the unit connection on the finite residue field. The point map into \(V\) is closed and proper. Its delta module is coherent and bounded. Such modules are compact on the smooth quasicompact separated \(V\): the finite operator resolutions in [*Holonomic D-modules and duality*](../../GL-DMOD/src/holonomic-d-modules-and-duality.md), Lemma 3.0, compute local Hom by finite complexes of finitely generated projective operator modules. A finite affine cover computes global Hom by its finite alternating Čech complex; intersections are affine because \(V\) is separated. All these finite operations commute with filtered colimits. This proves compactness also against unbounded targets.

Adjunction now gives
\[
 \begin{gathered}
 \operatorname{RHom}_{\mathcal B}(P\delta_a,B)
   \simeq\operatorname{RHom}_{\operatorname{Dmod}(V)}(\delta_a,UB)
   \simeq y_a^!(UB),\\
 \{P\delta_a\}_a\text{ are compact generators of }\mathcal B.
 \end{gathered}
                                                        \tag{FD.14}
\]
For a residue field extension the last expression is regarded as a complex over \(k\); forgetting its \(E_a\)-module structure is conservative. Continuity of \(U\) and compactness of \(\delta_a\) prove compactness of \(P\delta_a\). Theorem 3.18 and conservativity of \(U\) show that an object right orthogonal to all their shifts is zero.

Here is a direct proof that this last statement gives generation. Starting from \(B_0=B\), form \(B_{m+1}\) as the cofiber of the coproduct of all maps from shifts of the finite set \(P\delta_a\) to \(B_m\). At the next stage every such map becomes null. Compactness makes maps to \(B_\infty=\operatorname{colim}_mB_m\) factor through a finite stage. The transition maps on all homotopy groups of these mapping complexes are zero, so \(B_\infty\) is right orthogonal and hence zero. Each cofiber of \(B_m\to B_{m+1}\) lies in the stable colimit closure of the \(P\delta_a\). By the octahedral triangle the same holds for the cofiber of \(B\to B_m\), and then for its colimit, the cofiber of \(B\to0\). Shifting proves that \(B\) lies in that closure. This establishes (FD.14).

For the nilpotent category on \(\operatorname{Bun}_G\), the sufficient atlas upper bound is now proved in [*The moduli stack of bundles*](the-moduli-stack-of-bundles.md), §§6.3.1–6.3.2, equations (SG.8)–(SG.9). Sections 3.20–3.22 below apply that bound to the actual cone; its lower dimension equality is unnecessary for these detectors. The enhanced spectral construction must still supply the action, \(P\dashv U\), the continuity and conservativity used in (FD.13), and the identification of its image with the prescribed support category. Finally its Hecke-colimit description must preserve the chartwise ind-regular holonomic category. The finite detection and the adjunction calculation above prove the generation step when these precise hypotheses hold; they do not establish those geometric hypotheses or regularity.

Free further reading for this construction is Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky, [*The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support*, §16, “A set of generators”](https://arxiv.org/abs/2010.01906v2). The stratification, residue-field choice, flat quotient, finite-column and generation arguments required here have been supplied explicitly.

**Exercise 3.J.** For the plane support in Figure 3.4, verify (FD.2), give the closed filtration \(F_c\), and explain why removing the origin detector loses conservativity.

**Solution 3.J.** The three fibre dimensions are \(0,1,2\) and the codimensions are \(0,1,2\). Thus \(F_0=\mathbb A^2\), \(F_1=D\), \(F_2=\{0\}\), and \(F_3=\varnothing\), all closed. The delta module at the origin has characteristic variety \(T^*_0\mathbb A^2\subset N\). Its point fibres at \((0,1)\) and \((1,0)\) are zero, since it is supported at the origin, while its fibre at the origin is the coefficient field by Kashiwara's equivalence. Hence the first two detectors alone miss a nonzero supported object.

**Exercise 3.K.** On \(\mathbb A^1_k\), let \(M=k[t,t^{-1}]e\) with \(\partial_te=-t^{-2}e\). Prove that it is a coherent D-module with characteristic variety the union of the zero section and \(T^*_0\mathbb A^1\). Show that the detectors \(1,0\) apply, and that \(M\) is nevertheless irregular at zero.

**Solution 3.K.** The equation \(\partial_te=-t^{-2}e\), multiplied by \(t\), produces \(t^{-1}e\). Inductively \(\partial_t(t^{-n}e)=-nt^{-n-1}e-t^{-n-2}e\) produces every negative Laurent power. Thus \(e\) generates \(M\) over the Noetherian operator ring. The relation \((t^2\partial_t+1)e=0\) gives a surjection from \(\mathcal D/(\mathcal D(t^2\partial_t+1))\); its order filtration bounds \(\operatorname{Ch}(M)\) by \(\{t^2\xi=0\}\). Away from zero the module is a nonzero connection, so its characteristic variety contains the zero section and its closure. The module is not finite over \(k[t]\) near zero, because a finite list of Laurent polynomials has a common lower exponent bound whereas \(M\) does not. The zero-support converse following Proposition 3.1 therefore forces a nonzero vertical characteristic direction. Closed conical support then contains the entire fibre at zero, proving the asserted equality. This support has dimension one, and its strata are \(\mathbb A^1\setminus\{0\}\) and \(\{0\}\), so Theorem 3.18 applies to \(1,0\). In fact the detector at \(1\) already sees this particular \(M\).

To check irregularity directly, work over \(k((t))\). Every rank-one lattice is \(t^a k[[t]]e\): a unit multiplying its generator does not change this submodule. On \(t^ae\) the operator \(t\partial_t\) has coefficient \(a-t^{-1}\), which is not a power series. Thus no lattice is stable under logarithmic differentiation, the rank-one regular-singular condition. Detection and the half-dimensional support bound therefore do not imply regularity.

**Exercise 3.L.** Let \(S\) be smooth and connected, and let \(L=\bigoplus_{m\in\mathbb Z}\mathcal O_S[m]\) with its constant connections. Determine its cohomology and its point \(!\)-fibre. Identify precisely where the proof of Theorem 3.18 controls this unbounded example.

**Solution 3.L.** With cohomological shifts, \(H^n(L)=\mathcal O_S\) for every integer \(n\), coming from the summand with \(m=-n\). If \(y\) is a closed point of residue field \(E\) and \(s=\dim S\), then \(y^!L=\bigoplus_{m\in\mathbb Z}E[m-s]\); its cohomology is \(E\) in every degree. Each cohomology module is flat, so the finite parameter Koszul complex in (FD.8) has no higher Tor cohomology and (FD.9) applies degree by degree. On the minimal support stratum in Theorem 3.18, Kashiwara's finite normal Koszul complex gives the same control. The argument requires neither a bounded input nor a finite number of nonzero cohomology groups.

### 3.20. The nilpotent chart bound and holonomic cohomology

We now apply the detectors to the actual global nilpotent cone. Keep the algebraically closed characteristic-zero field, the smooth projective connected curve and an arbitrary connected reductive group from §1. Write \(Y=\operatorname{Bun}_G(X)\). If \(q:A\to Y\) is a smooth chart with \(A\) smooth affine of pure dimension \(d\), its cotangent pullback is a closed immersion into \(T^*A\). Let
\[
 N_A=\left(A\times_Y\operatorname{Nilp}_G\right)_{\mathrm{red}}
       \subset T^*A,
 \qquad \dim N_A\leq d.
                                                        \tag{NC.1}
\]
Reduction does not affect a characteristic-support containment. The cone is closed and conical: the closed cotangent pullback retains the stack moment equations, and the nilpotence equations are homogeneous in the Higgs field. Its upper bound is proved in [*The moduli stack of bundles*](the-moduli-stack-of-bundles.md), §§6.3.1–6.3.2, equations (SG.8)–(SG.9).

We recall the argument to specify exactly which dimension statement is used. On a reduced irreducible component \(W\) of \(N_A\), pass to a nonempty smooth open. The generic nilpotent Higgs field has the intrinsic parabolic reduction of Lesson 2, §6.2.3; its reduction on the whole generic curve spreads to a dense open \(W_0\) by §6.2.4. Thus one fixed parabolic \(Q\) suffices on \(W_0\). Its section atlas and nilradical section scheme are constructed in §§6.3.1–6.3.2. Put \(Z=A\times_Y\operatorname{Bun}_Q\), with projection \(F:Z\to A\), and let \(r:W_0\to Z\) be the reduction. The covector annihilates the lifted parabolic deformation because the nilradical is perpendicular to the parabolic Lie algebra. Consequently
\[
 \left.\lambda_A\right|_{W_0}(v)
       =\xi\bigl(dF(dr(v))\bigr)=0,
 \qquad \left.d\lambda_A\right|_{W_0}=0.
                                                        \tag{NC.2}
\]
In a cotangent coordinate chart the symplectic form is nondegenerate on a space of dimension \(2d\). An isotropic tangent subspace \(L\) satisfies \(L\subset L^\perp\) and \(\dim L^\perp=2d-\dim L\); hence \(\dim W=\dim W_0\leq d\). This proves (NC.1) component by component. Relative smoothness of the forgetful map is unnecessary: the tangent vector is lifted through the actual reduction \(r\). Neither a countable union of reduction images nor equality of dimensions is used. The lower bound needed for the full Lagrangian assertion of Lesson 2 is a separate statement.

Choose the relative dimension \(r_q\) constant on this chart. Normalize \(q^!M\) by \([-r_q]\), and use the line-twist equivalence of §2 to write its left D-module complex as \(L_A\). For \(M\) in (3.1), every coherent submodule of every \(H^n(L_A)\) has characteristic variety contained in \(N_A\). On the affine chart the operator ring is Noetherian, as used in §3.12, so each cohomology module is the filtered union of its actual finitely generated submodules. These submodules are coherent. Therefore
\[
 H^n(L_A)=\operatorname*{colim}_{\alpha} L_{n,\alpha},
 \qquad \operatorname{Ch}(L_{n,\alpha})\subset N_A,
 \qquad \dim\operatorname{Ch}(L_{n,\alpha})\leq d.
                                                        \tag{NC.3}
\]
Here the index consists of finite submodules ordered by inclusion: their sum provides an upper bound for two indices. The final inequality is exactly the definition of holonomicity in [*Holonomic D-modules and duality*](../../GL-DMOD/src/holonomic-d-modules-and-duality.md), §1, equation (1.1), including the zero module. Thus every chart cohomology module is ind-holonomic. This conclusion allows arbitrary rank and arbitrary cohomological degrees. It concerns cohomology modules; it does not identify an unbounded derived category with an ind-completion of a category of bounded complexes. Regular singularities are a further condition and are not implied by (NC.3).

### 3.21. Finite detectors on each bounded bundle-stack open

Let \(U\subset Y\) be any quasicompact open in the cofinal exhaustion of §1.15. Its finite-type smooth atlas can be chosen to be a finite union of smooth affine schemes \(A_i\): cover a smooth atlas by affine opens and use quasicompactness to choose finitely many whose images cover \(U\). Further split into the finitely many open-and-closed dimension components, so that both \(d_i=\dim A_i\) and the relative dimension \(r_i\) of \(q_i:A_i\to U\) are constant. The bundle-stack atlas is proved in Lesson 2, §1.5, and the conservativity of normalized smooth descent is proved here in §1.10.

Apply Theorem 3.18 to \(A_i\) and its fixed cone \(N_{A_i}\) from (NC.1). It gives finitely many closed points \(y_{i,a}\), with residue fields \(E_{i,a}\). Over the present algebraically closed field these residue fields equal \(k\). Write \(\mathsf T_i\) for the line untwisting on this chart and define
\[
 \begin{gathered}
 L_i(M)=\mathsf T_i\bigl(q_i^!(M|_U)[-r_i]\bigr),\\
 \Psi_U(M)=
   \bigl(y_{i,a}^!L_i(M)\bigr)_{i,a}
   \in\prod_{i,a}\operatorname{Dmod}(\operatorname{Spec}E_{i,a}).
 \end{gathered}
                                                        \tag{NC.4}
\]
The chart and point indices in this product are both finite. The normalized smooth pullback and line untwisting preserve the support condition, so each \(L_i(M)\) lies in the full category \(\operatorname{Dmod}_{N_{A_i}}(A_i)\). Theorem 3.18, applied to every chart, and normalized smooth descent give
\[
 \Psi_U(M)=0\quad\Longleftrightarrow\quad M|_U=0
 \qquad
 \bigl(M\in\operatorname{Dmod}_{1/2,\operatorname{Nilp}}(Y)\bigr).
                                                        \tag{NC.5}
\]
This is a theorem for every connected reductive group, every genus and every bundle component under our characteristic-zero assumptions. The missing lower dimension equality for the cone is not a hypothesis of it.

Detection also applies to morphisms. The support convention of §3.12 is closed under triangles, so the cone of a morphism \(f:M\to M'\) in the supported category is supported. Smooth pullback, shifts, line untwisting and point exceptional pullback are exact functors. Apply (NC.5) to that cone to obtain
\[
 \Psi_U(f)\text{ is an equivalence}
       \quad\Longleftrightarrow\quad
 f|_U\text{ is an equivalence}.
                                                        \tag{NC.6}
\]
Thus it is the induced maps of complexes, rather than just their fibre dimensions, that test a morphism.

Take one such finite atlas and detector family for every open \(U_b\) of the cofinal exhaustion. Equation (FT.9) proves that restriction to these opens is conservative. Together with (NC.5)–(NC.6), it yields
\[
 \begin{gathered}
 M=0\quad\Longleftrightarrow\quad
       \Psi_{U_b}(M)=0\text{ for every }b,\\
 f\text{ is an equivalence}\quad\Longleftrightarrow\quad
       \Psi_{U_b}(f)\text{ is an equivalence for every }b.
 \end{gathered}
                                                        \tag{NC.7}
\]
There is no cohomological bound in these statements. Indeed the point calculation on a smooth stratum \(S\) of dimension \(s\) in the proof of Theorem 3.18 is
\[
 H^{n+s}(y^!L)=H^n(L)_y\otimes_{\mathcal O_{S,y}}E
       \qquad(n\in\mathbb Z),
                                                        \tag{NC.8}
\]
when all the cohomology modules of \(L\) have zero support on \(S\). Their coherent submodules and quotients are flat connections by §3.17. The residue field is resolved by a Koszul complex of length \(s\), so only finitely many columns enter any total degree even for an unbounded \(L\). The flatness kills higher Tor groups, proving (NC.8) in every degree. The supported inverse image used to reach \(S\) has the same finite-column control. Checking only degree-zero fibres would discard this information.

### 3.22. What the detectors do and do not imply

The finite family in (NC.4) is finite for one quasicompact open; its union over the whole exhaustion need not be finite. This is already forced by the elementary bundle stack
\[
 X=\mathbf P^1,\qquad G=\mathbb G_m,
 \qquad Y\simeq\coprod_{d\in\mathbb Z}B\mathbb G_m,
 \qquad U_m=\coprod_{|d|\leq m}B\mathbb G_m.
                                                        \tag{NC.9}
\]
The Picard splitting in §6 gives this equivalence on families and arrows: a degree-\(d\) line bundle on \(\mathbf P^1\) is \(\mathcal O(d)\) tensored with a line from the parameter scheme. The degree is locally constant, and a quasicompact parameter has only finitely many degree values. Thus the \(U_m\) are cofinal among quasicompact opens of this stack. For each component its atlas \(\operatorname{Spec}k\to B\mathbb G_m\) is smooth of relative dimension one; its source has dimension zero and its pulled-back nilpotent cone is the zero cotangent point. One atlas point per degree gives the detectors in (NC.4), with the normalization \([-1]\).

Let \(j_d:B\mathbb G_m\hookrightarrow Y\) be the degree component and put
\[
 M_d=(j_d)_*\mathbf 1_{B\mathbb G_m}\ne0,
 \qquad \operatorname{SS}(M_d)\subset\operatorname{Nilp}_{\mathbb G_m}.
                                                        \tag{NC.10}
\]
The constant object has zero support by Proposition 3.1, and extension across an open-and-closed component adds no directions. Any finite collection of intrinsic points of \(Y\) lies in finitely many degrees. Choose \(d\) outside that set. All of their exceptional fibres on \(M_d\) vanish, although \(M_d\) is nonzero. This proves that one cannot replace (NC.7) by a finite set of intrinsic points for the entire bundle stack. Nor does chart detection prove global compactness of these constant objects; §5 gives the separate compactness calculation on \(B\mathbb G_m\).

Regularity also requires more than the upper bound. On the separate affine chart \(A=\mathbb A^1\), consider the rank-one left module
\[
 K=k[t]e,\qquad \partial_t e=2t e,
 \qquad \operatorname{Ch}(K)=\text{zero section of }T^*A.
                                                        \tag{NC.11}
\]
The constant good filtration of Proposition 3.1 proves the support equality, so this is holonomic and any one point detects it. At infinity write \(s=t^{-1}\). The connection has \(\partial_s e=-2s^{-3}e\). Every full lattice in the one-dimensional space \(k((s))e\) is \(s^a k[[s]]e\), for some integer \(a\), because \(k[[s]]\) is a discrete valuation ring. Its logarithmic operator satisfies
\[
 s\partial_s(s^ae)=(a-2s^{-2})s^ae
          \notin s^a k[[s]]e.
                                                        \tag{NC.12}
\]
No lattice is stable under this operator. This is the logarithmic-lattice obstruction to a regular singularity at infinity; the connection is therefore irregular there. Its exceptional fibre at a point is \(k[-1]\), by (NC.8). Detection of that nonzero complex gives no control of the pole in (NC.12). This example concerns a connection on an affine line; it makes no assertion that such an irregular object belongs to the bundle-stack nilpotent category.

![The nilradical reduction makes a chart tangent space isotropic, giving the upper bound and finite detectors; the degree components require a stagewise family, and a separate exponential connection illustrates the regularity boundary.](figures/nilpotent-chart-detectors.svg)

*Figure 3.5.* The geometric implication is (NC.1)–(NC.3), using the parabolic-family proof (SG.8)–(SG.9) of [*The moduli stack of bundles*](the-moduli-stack-of-bundles.md). The normalized atlas and finite point tests are (NC.4)–(NC.8); the symbols \(d_i,r_i\) denote chart and relative dimensions. The bottom examples retain the actual degree components of (NC.9) and the logarithmic coefficient of (NC.12). The arrows describe implications proved above, rather than an embedding of a bundle stack into a finite-dimensional drawing. For related finite generators and the subsequent regularity argument, see the freely accessible [AGKRRV paper, §§16.2, 16.5](https://arxiv.org/abs/2010.01906v2).

**Exercise 3.M.** Let \(f:M\to M'\) be a morphism in the nilpotent category, and suppose all the maps in (NC.7) are equivalences. Prove that \(f\) is an equivalence. Explain why equality of the dimensions of the detector cohomology groups would not suffice.

**Solution 3.M.** The cone \(C\) has nilpotent support by the triangle rule of §3.12. Exactness gives \(\Psi_{U_b}(C)=0\) for every stage. The finite detector theorem and normalized descent give \(C|_{U_b}=0\), and (FT.9) gives \(C=0\). Hence \(f\) is an equivalence. Two one-dimensional vector spaces can have a zero map between them; their dimensions agree while that map is not an equivalence. The induced detector maps, not just dimensions of their source and target, are required.

**Exercise 3.N.** In (NC.9), construct a nilpotent object missed by any prescribed finite set of intrinsic points. Does this contradict the finiteness assertion on \(U_m\)?

**Solution 3.N.** Record the finitely many degrees of the points and choose an integer \(d\) outside them. The object \(M_d\) of (NC.10) is nonzero and nilpotent. Disjointness of the open-and-closed components makes all the prescribed fibres zero. If \(d\) belongs to \([-m,m]\), the degree-\(d\) atlas point in the finite family on \(U_m\) detects its nonzero restriction, by normalized smooth descent. If \(d\) is outside that interval, its restriction to \(U_m\) is zero. Both cases agree with (NC.5).

**Exercise 3.O.** Replace \(2t\) in (NC.11) by \(m t^{m-1}\), where \(m\geq2\) is an integer. Compute the support, the point exceptional fibre, and the logarithmic-lattice coefficient at infinity.

**Solution 3.O.** This is still a free rank-one module over \(k[t]\) with integrable connection, so its characteristic variety is the zero section by the same good filtration. Its point exceptional fibre is \(k[-1]\). Since \(\partial_s e=-m s^{-m-1}e\), the coefficient on the lattice \(s^a k[[s]]e\) is \(a-ms^{-m}\). Its negative-power term is nonzero in characteristic zero and cannot lie in \(k[[s]]\), so no full lattice is stable under \(s\partial_s\). The connection is holonomic with an irregular singularity at infinity for every such \(m\). This verifies directly the distinction needed before proving nilpotent regularity by the spectral projector.

### 3.23. Jordan components and a covector-detecting cocharacter

The Hecke argument needs more than a nilpotent dimension bound: a nonnilpotent Higgs value must produce a nonzero covector in the curve direction. We first construct the group-theoretic data for that calculation. Keep the algebraically closed characteristic-zero field, an arbitrary connected reductive \(G\), and a nondegenerate invariant form \(B\) on \(\mathfrak g\). Fix a faithful closed representation \(G\hookrightarrow GL(V)\). Here is its existence proof. For each of finitely many algebra generators \(f\) of \(k[G]\), expand \(\Delta f=\sum_i a_i\otimes b_i\) with independent first factors. Coassociativity, followed by coefficient functionals on these first factors, gives \(\Delta b_i\in k[G]\otimes\operatorname{span}(b_j)\). The counit shows that \(f\) belongs to this span. Sum these finite-dimensional subcomodules to obtain \(V\) containing all generators. The coaction and antipode give a representation with invertible matrices; applying the counit in the second factor writes each element of \(V\) as a linear combination of its matrix coefficients. Thus those coefficients generate \(k[G]\), and the coordinate-algebra map from \(k[GL(V)]\) is surjective. This is precisely a closed immersion. All matrix calculations below take place in this representation, while their Lie-algebra conclusions are intrinsic.

We need the Jordan components of a Lie element to remain inside the Lie algebra. Here is an algebraic proof that also constructs its semisimple torus. For \(C\in\mathfrak g\), write its matrix Jordan decomposition
\[
 C=H+N,\qquad [H,N]=0,\qquad H\text{ semisimple},
       \qquad N^r=0.
                                                        \tag{HC.1}
\]
This decomposition is polynomial in \(C\): factor its minimal polynomial as \(\prod_i(z-c_i)^{r_i}\). Bézout identities for the pairwise coprime factors give complementary polynomial idempotents \(E_i\); then \(H=\sum_i c_iE_i\), and \(N=C-H\) is nilpotent on every summand. This proves the decomposition and the commutation assertion without a choice of analytic exponential.

The formal exponential of any Lie element lies in the group. Indeed let \(I\) be the Hopf ideal of \(G\) in \(k[GL(V)]\). A Lie vector \(Z\) is a derivation at the identity that kills \(I\). The left-invariant derivation \(D_Z\), obtained by applying this derivation to the second factor of the coproduct, preserves \(I\) by its Hopf-ideal identity. Evaluation of a coordinate function on the formal matrix exponential is
\[
 f(\exp(zZ))=\sum_{j\geq0}
              \frac{\epsilon(D_Z^jf)}{j!}z^j.
                                                        \tag{HC.2}
\]
The chain rule, or coefficient induction on the equation \(E'=EZ\), proves this equality for the matrix entries and inverse determinant, hence for every coordinate function. Its coefficients vanish for \(f\in I\). Thus the formal point belongs to \(G(k[[z]])\). The same proof works over every coefficient algebra over \(k\).

Diagonalize \(H\), with weights \(w_1,\ldots,w_v\in k\) on \(V\). Put
\[
 \Lambda=\{(m_i)\in\mathbb Z^v:\sum_i m_iw_i=0\},
 \qquad S=D(\mathbb Z^v/\Lambda)\subset(\mathbb G_m)^v.
                                                        \tag{HC.3}
\]
The lattice \(\Lambda\) is saturated: if a nonzero integer multiple of a weight sum is zero, that sum is zero in characteristic zero. Its quotient is therefore free, so \(S\) is a split torus. It contains \(H\) in its Lie algebra, by the displayed linear equations. Also \(S\) commutes with \(N\): a nonzero entry of \(N\) can join only equal \(w_i\), and the two corresponding characters restrict equally to \(S\).

To prove that this torus and the nilpotent one-parameter group belong to \(G\), apply (HC.2) to \(C\). A coordinate function evaluated on \(\exp(zH)\exp(zN)\) is a finite sum \(\sum_i p_i(z)e^{a_i z}\), with distinct \(a_i\in k\) and polynomials \(p_i\). This description includes inverse determinant: the determinant of the nilpotent exponential is one. Such a sum can vanish as a formal series only when every polynomial vanishes. If their degrees are at most \(D\), apply \(\prod_{j\ne i}(\partial_z-a_j)^{D+1}\). All other terms die; on the \(i\)-th polynomial the resulting operator is a product of \(\partial_z+(a_i-a_j)\), each invertible on polynomials of degree at most \(D\). Hence \(p_i=0\).

The same grouped polynomials are exactly the coefficients of the distinct characters of \(S\) in \(f(s\exp(bN))\). Thus every \(f\in I\) vanishes in \(k[S][b]\), not just at field points. The multiplication map \((s,b)\mapsto s\exp(bN)\) factors through \(G\). Differentiating its two factors proves
\[
 H,N\in\mathfrak g,\qquad
 S\subset G,\qquad \exp(bN)\in G(k[b]).
                                                        \tag{HC.4}
\]
In particular nilpotence here includes the central directions: a nonzero toral Lie element is semisimple in a faithful representation, even though its adjoint endomorphism can be zero.

Set \(M=C_G(S)\). This is smooth, connected and reductive by [*Regular elements and centralizers*](../../AG-RG/AG-RG-02.md), Lemma 1.1 and Theorem 2.1. It is also the scheme centralizer of \(H\). In the diagonal faithful representation, commuting with \(H\) forces a matrix entry joining different \(w_i\) to be zero. Commuting with \(S\) imposes exactly the same condition, because its corresponding characters differ precisely when the two weights differ. A nonzero weight difference is a unit over every test algebra. This verifies the equality on nonreduced tests as well. Both \(H\) and \(N\) belong to \(\mathfrak m\), and \(H\) is central there.

The finite root decomposition relative to a maximal torus \(T\supset S\), proved in [*Root data, Weyl chambers and the Bruhat decomposition*](../../AG-RG/AG-RG-04.md), gives \(\mathfrak m\) the roots with \(\alpha(H)=0\). Let \(\mathfrak n\) be the sum of the other \(H\)-weight spaces. Invariance of \(B\) pairs only opposite weights. Therefore
\[
 \mathfrak g=\mathfrak m\oplus\mathfrak n,
 \quad B(\mathfrak m,\mathfrak n)=0,
 \quad B|_{\mathfrak m}\text{ is nondegenerate},
 \quad B(\mathfrak z(\mathfrak m),[\mathfrak m,\mathfrak m])=0.
                                                        \tag{HC.5}
\]
Here is the needed reductive Lie splitting. In the toral Lie algebra, the common kernel of the roots of \(M\) is complementary to their coroot span. To see the nondegeneracy on that span, average a positive rational inner product over the finite Weyl group of this root system. Each root reflection is then orthogonal; its formula gives \(\langle v,\alpha^\vee\rangle=2(v,\alpha)/(\alpha,\alpha)\) on the rational root span. Consequently the root span and coroot span pair nondegenerately. The resulting nonzero rational determinants stay nonzero in characteristic zero. The brackets \([E_\alpha,E_{-\alpha}]=H_\alpha\) and \([H_\alpha,E_\alpha]=2E_\alpha\) show that the derived Lie algebra consists exactly of the coroot span and the root spaces. The center is exactly the common root kernel: commuting with the torus eliminates every root-space component, and commuting with each root space imposes its root equation. Thus \(\mathfrak m=\mathfrak z(\mathfrak m)\oplus[\mathfrak m,\mathfrak m]\). The connected subtorus cut out by the same root characters centralizes the torus and every root subgroup, so its Lie algebra identifies this center with \(\operatorname{Lie}Z(M)^0\). These root and reflection formulas are proved in the root-data lesson, §§1–2. Together with the orthogonality in (HC.5), the splitting makes the restriction of \(B\) to this center nondegenerate.

We also verify directly that \(B(Z,N)=0\) for central \(Z\in\mathfrak m\). Decompose the faithful representation into its finitely many \(Z(M)^0\)-weight spaces \(V_\theta\). These spaces are \(M\)-stable, so \(\chi_\theta=\det(M|V_\theta)\) is an algebraic character of \(M\). On the central torus its derivative is \((\dim V_\theta)d\theta\). Faithfulness makes the weights span the dual of the central Lie algebra; their nonzero dimension factors are invertible in characteristic zero. Thus these character derivatives span that dual. They kill the derived Lie algebra, and so does \(B(Z,-)\) by (HC.5); the splitting shows that \(B(Z,-)\) is a linear combination of them. But \(b\mapsto\chi_\theta(\exp(bN))\) is an invertible polynomial on \(\mathbb A^1\), hence constant, and has value one at zero. Differentiation gives \(d\chi_\theta(N)=0\), proving the assertion.

Suppose now that \(C\) is nonnilpotent, so \(H\ne0\). Define the rational cocharacter space
\[
 V_0=\{v\in X_*(T)\otimes\mathbb Q:
          \alpha(v)=0\text{ whenever }\alpha(H)=0\}.
                                                        \tag{HC.6}
\]
Its scalar extension to \(k\) is the central Lie algebra of \(\mathfrak m\), and contains \(H\). For a root with \(\beta(H)\ne0\), the functional \(\beta\) is nonzero on \(V_0\): otherwise that root would be a rational linear combination of the vanishing roots, and would vanish on \(H\). Also \(B(H,-)\) is nonzero on \(V_0\otimes k\), by nondegeneracy on the center. We can consequently choose an integral cocharacter \(\lambda\) such that
\[
 \alpha(\lambda)=0\quad(\alpha(H)=0),\qquad
 \beta(\lambda)\ne0\quad(\beta(H)\ne0),\qquad
 B(H,d\lambda)\ne0.
                                                        \tag{HC.7}
\]
Here is a finite algebraic choice argument, including when the entries of \(H\) are not rational. Take integral vectors \(v_1,\ldots,v_\ell\) spanning \(V_0\) over \(\mathbb Q\). Evaluate the finitely many nonzero functionals just listed on \(v_1+zv_2+\cdots+z^{\ell-1}v_\ell\). Each gives a nonzero polynomial over \(k\); their union has only finitely many roots. An integer \(z\) outside that union gives (HC.7).

The root subgroup description makes this cocharacter central in \(M\). Its centralizer has exactly the same roots as \(M\); both centralizers are smooth and connected, and the inclusion of \(M\) has equal tangent dimension, so they agree as schemes. The vanishing just proved on \(N\) now gives
\[
 C_G(\lambda)=M,\qquad
 B(C,d\lambda)=B(H,d\lambda)\ne0.
                                                        \tag{HC.8}
\]
For \(G=\mathbb G_m\), a nonzero \(C=a\) has \(M=G\), and the identity cocharacter already gives this nonzero pairing. Thus the argument retains the torus factor of a general reductive group.

### 3.24. Formal Levi normalization over coefficient rings

The same centralizer controls a whole formal Higgs series. First consider the field point of §3.23. On an \(H\)-weight space of \(\mathfrak n\) with nonzero weight \(c\), the operator \(\operatorname{ad}C\) is \(c+\operatorname{ad}N\). If \(N^r=0\) in the faithful representation, then \((\operatorname{ad}N)^{2r-1}=0\): expand the commuting left and right multiplication operators, and each term contains at least \(r\) copies of \(N\) on one side. Hence
\[
 (\operatorname{ad}C)^{-1}|_{\mathfrak n_c}
       =c^{-1}\sum_{j=0}^{2r-2}
                  (-\operatorname{ad}N/c)^j.
                                                        \tag{HC.9}
\]
This proves invertibility on the complement, including a nonzero nilpotent part inside the Levi.

We prove a coefficient-ring statement. Let \(R\) be any \(k\)-algebra, let \(M\) be this Levi subgroup, and let
\[
 A(u)\in\mathfrak g(R[[u]]),\qquad
 A_0\in\mathfrak m(R),\qquad
 \operatorname{ad}A_0|_{\mathfrak n_R}
       \text{ an invertible }R\text{-linear map}.
                                                        \tag{HC.10}
\]
The complement is \(M\)-stable, because \(M\) commutes with the torus whose nonzero weights define it. The last condition is an open determinant condition on the constant term. It holds at the field point \(C\) by (HC.9); no constant-rank assertion for a general family is being made.

**Formal normalization theorem.** Under (HC.10) there is \(h(u)\in G(R[[u]])\), with \(h(0)=1\), such that
\[
 \operatorname{Ad}_{h(u)}A(u)\in\mathfrak m(R[[u]]).
                                                        \tag{HC.11}
\]
The left \(M(R[[u]])\)-coset of such normalized frames is unique.

**Proof.** Suppose the coefficients below degree \(n\) already belong to \(\mathfrak m_R\), and write \(Y_n\) for the complementary part of its degree-\(n\) coefficient. For \(n\ge1\), put
\[
 X_n=(\operatorname{ad}A_0|_{\mathfrak n_R})^{-1}Y_n,
 \qquad h_n=\exp(u^nX_n).
                                                        \tag{HC.12}
\]
Equation (HC.2), with its coefficient-ring proof, shows that this exponential belongs to \(G(R[[u]])\). Modulo \(u^{n+1}\), conjugation changes the complementary coefficient to \(Y_n+[X_n,A_0]=0\). Lower coefficients are unchanged: terms involving a positive-degree coefficient have degree at least \(n+1\), and terms involving two copies of \(u^nX_n\) have degree at least \(2n\ge n+1\). Iterate. The products \(h_n\cdots h_1\) stabilize modulo each power of \(u\). Their limit is a matrix and its inverse over \(R[[u]]\); every defining equation of \(G\) holds modulo every power, hence holds in the separated complete ring. This gives (HC.11), over nonreduced \(R\) as well.

For uniqueness, let \(B,B'\in\mathfrak m(R[[u]])\) have the same constant term \(A_0\), and let \(g(0)=1\) with \(\operatorname{Ad}_gB=B'\). If \(g\equiv1\pmod{u^n}\), its degree-\(n\) coefficient is some \(Z_n\in\mathfrak g_R\): the defining group equations at that order are exactly the Lie equations. The complementary part of the conjugation identity is \([Z_n,A_0]_{\mathfrak n}=0\). Invertibility in (HC.10) forces \(Z_n\in\mathfrak m_R\). Multiplication by \(\exp(-u^nZ_n)\in M(R[[u]])\) removes that coefficient and keeps both sides in the Levi. Induction expresses \(g\) modulo each power as an \(M\)-valued frame. Closedness of \(M\) and completeness give \(g\in M(R[[u]])\). Apply this to \(g=h'h^{-1}\) for two normalizations. \(\square\)

All operations are coefficient-linear inverses and formal exponentials with rational denominators, so commute with coefficient change as long as (HC.10) holds. The theorem is the identity branch of formal Levi normalization. It does not assert uniqueness of all Levi reductions across Weyl branches, or a global decomposition on a parameter space where the determinant condition fails.

We will use the exact example
\[
 \begin{gathered}
 G=SL_3,\quad C=\operatorname{diag}(1,1,-2)+E_{12},\quad
 M=S(GL_2\times GL_1),\\
 \lambda(u)=\operatorname{diag}(u,u,u^{-2}),\qquad
 B(C,d\lambda)=6\quad(B=\operatorname{tr}).
 \end{gathered}
                                                        \tag{HC.13}
\]
For \(A(u)=C+uE_{23}\), the first correction is
\[
 X_1=\tfrac13 E_{23}-\tfrac19 E_{13},\qquad
 h(u)=1+uX_1,\qquad
 h(u)A(u)h(u)^{-1}=C.
                                                        \tag{HC.14}
\]
Indeed \([C,E_{23}]=3E_{23}+E_{13}\) and \([C,E_{13}]=3E_{13}\), so \([C,X_1]=E_{23}\). Also \(X_1^2=0\) and \([X_1,E_{23}]=0\). These identities prove the conjugation equality exactly, rather than only through the first power of \(u\).

### 3.25. Local Hecke cotangents and the moving-point residue

Put \(D_R=\operatorname{Spec}R[[u]]\) and \(D_R^\times=\operatorname{Spec}R((u))\). The local Hecke groupoid consists of two \(G\)-torsors on \(D_R\) and an isomorphism \(\alpha:P_2|_{D_R^\times}\to P_1|_{D_R^\times}\). Their disc frames exist étale locally on \(\operatorname{Spec}R\), by [*Loop groups and the affine Grassmannian*](../../GL-SAT/src/GL-SAT-02.md), Lemma 4.1. In frames, \(\alpha\) is a loop \(g\); changing the frames replaces it by \(a g b^{-1}\), with two arcs \(a,b\). Conversely a loop gives these data, and torsor descent supplies every arrow. Thus as an étale stack of groupoids,
\[
 \operatorname{Hecke}^{\mathrm{loc}}_x
       \simeq[L^+G\backslash LG/L^+G].
                                                        \tag{HC.15}
\]
This is a quotient prestack with its torsor sheafification, not an assertion that it is an ordinary finite-type scheme. The loop and arc functors, including their nilpotents, are represented in that earlier lesson, Proposition 1.1. [*Beauville–Laszlo gluing and the moduli interpretation*](../../GL-SAT/src/GL-SAT-03.md), Proposition 2.1 and Theorem 3.1, prove that these disc data glue effectively to modifications of curve torsors, including families, frames and arrows.

At a field-valued framed loop \(g\), write a first-order variation as \(g(1+\varepsilon X)\). The Lie equations say exactly \(X\in\mathfrak g((u))\). Two infinitesimal arc changes give \(X\mapsto X+\operatorname{Ad}_{g^{-1}}a-b\). Retaining the automorphisms as well as the deformations gives the tangent complex
\[
 [\,\mathfrak g[[u]]\oplus\mathfrak g[[u]]
       \xrightarrow{(a,b)\mapsto\operatorname{Ad}_{g^{-1}}a-b}
       \mathfrak g((u))\,],
 \qquad\text{in degrees }-1,0.
                                                        \tag{HC.16}
\]
This is obtained directly from the dual-number groupoid, so a coarse quotient of field points has not discarded its degree-minus-one stabilizers.

The continuous dual of \(\mathfrak g((u))\) is \(\mathfrak g^*((u))du\), by the residue pairing. To check this, a continuous functional kills \(u^m\mathfrak g[[u]]\) for some \(m\). Its values on the remaining Laurent monomials give a series with only finitely many negative powers. Conversely such a Laurent covector pairs by a finite coefficient sum against each Laurent vector and kills a sufficiently high power. Hence the continuous classical cotangent space, the degree-zero kernel in the dual complex of (HC.16), is
\[
 \operatorname{Ann}\bigl(\mathfrak g[[u]]+
          \operatorname{Ad}_{g^{-1}}\mathfrak g[[u]]\bigr)
       \subset\mathfrak g^*((u))du.
                                                        \tag{HC.17}
\]
The first annihilator condition says \(\eta\) is regular: test against each nonnegative Laurent monomial to kill its negative coefficients. The second says that \((\operatorname{Ad}_{g^{-1}})^*\eta\) is regular. Taking \(\eta_2=\eta\) and \(\eta_1=(\operatorname{Ad}_{g^{-1}})^*\eta\) identifies (HC.17) with
\[
 \eta_i\in\mathfrak g_{P_i}^*[[u]]du,\qquad
       \eta_2=\alpha^*\eta_1\text{ on the punctured disc}.
                                                        \tag{HC.18}
\]
The pullback here is ordinary covector pullback under \(\alpha:P_2\to P_1\); this fixes the coadjoint convention and the orientation of the modification.

For the curve term we compare two horizontal lifts, instead of assigning a constant covector to moving coordinates. Write the absolute local coordinate as \(t\) and the moving center as \(x\), so \(u=t-x\). If \(\delta^N=0\) in a coefficient ring, the ideals \((t)\) and \((t-\delta)\) have cofinal powers: expansion gives \((t-\delta)^{m+N-1}\subset(t)^m\), and exchanging them gives the reverse inclusion. Their completions are canonically the same absolute-coordinate ring. Their punctured completions coincide too, because
\[
 (t-\delta)^{-1}=t^{-1}\sum_{j=0}^{N-1}(\delta/t)^j.
                                                        \tag{HC.19}
\]
The complement of the graph and its formal and punctured neighborhoods therefore remain the same under an infinitesimal change of center. Keeping their torsors, frames and gluing isomorphism fixed gives crystal transport of the local and global modification groupoids. This assertion holds on ordinary nonreduced test rings; it is not a transport chosen only for field points. On a smooth curve the same argument applies in an étale coordinate; the graph is a relative Cartier divisor by the monic-coordinate proof in §3.28.

Now take \(x=\varepsilon\), with \(\varepsilon^2=0\). Keeping the absolute loop \(g(t)\) fixed represents the crystal lift. In the moving coordinate it is \(g(u+\varepsilon)=g(u)+\varepsilon g'(u)\). The coordinate lift keeps \(g(u)\) fixed. Consequently
\[
 \text{crystal lift}-\text{coordinate lift}
       =g^{-1}g'\in\mathfrak g((u))
                                                        \tag{HC.20}
\]
after left tangent trivialization. It belongs to the Lie algebra by differentiation of the defining group equations, or the Maurer–Cartan form. Evaluating \(\eta\) from (HC.17) gives the discrepancy covector
\[
 \xi_x=\operatorname{Res}_{u=0}
          \langle\eta,g^{-1}g'\rangle\,dx.
                                                        \tag{HC.21}
\]
The expression descends under arc-frame changes. For \(\widetilde g=a g b^{-1}\), differentiate this product; after carrying the covector through its tangent trivialization, its logarithmic derivative differs by left- and right-arc tangent vectors, from the regular logarithmic derivatives of \(a,b\). Equation (HC.17) annihilates both differences. This proves descent of the formula rather than just independence of a scalar at one representative. In (HC.21), a covector having zero curve component in the coordinate splitting has the displayed positive curve component in the crystal splitting. Reversing the difference of lifts reverses the sign.

For \(g=u^\lambda\), differentiation on the faithful weight spaces gives \(g^{-1}g'=d\lambda/u\). A regular covector \(\eta=A(u)du\) consequently gives
\[
 \xi_x=\langle A(0),d\lambda\rangle\,dx.
                                                        \tag{HC.22}
\]
Only the constant coefficient contributes to the residue. The factor \(dx\) is essential: the scalar coefficient is being written in the chosen coordinate on the curve. Equivalently the pairing of the Higgs value with \(d\lambda\) is a member of \(T_x^*X\). Formal coordinate change preserves residues of one-forms: for \(v=f(u)\) of order one, the residue of \(f^n f' du\) is zero for \(n\ne-1\), since it is an exact derivative, and is one for \(n=-1\), since \(f'/f=u^{-1}+\) a regular series. These checks prove the one-form assertion on Laurent series by their finite principal parts. The discrepancy in (HC.21) compares the intrinsic crystal splitting with the chosen coordinate splitting; declaring the latter curve component zero refers to that choice. For the cocharacter point in (HC.22), a parameter change \(v=u a(u)\), with \(a(0)\ne0\), changes \(u^\lambda\) by the arc factor \(a(u)^\lambda\), annihilated by (HC.17). Moreover the constant Higgs coefficient transforms reciprocally to the base differential: if \(y=f(x)\), then \(A_y(0)dy=A_x(0)dx\). This proves directly that the cocharacter formula (HC.22) is the intrinsic pairing with the Higgs value, including nonlinear coordinate changes.

Equations (HC.8), (HC.11) and (HC.22) are the local algebraic ingredients for testing a nonnilpotent Higgs value: the Levi normalization puts the series in the centralizer Lie algebra, its central cocharacter gives the loop point, and the constant pairing is nonzero. The normalized series commutes with this cocharacter. Identifying adjoint and coadjoint bundles by \(B\) therefore gives the same regular Higgs series on both disc torsors at \(u^\lambda\); it satisfies (HC.18), so the covector really belongs to the local cotangent model (HC.17). The normalizing frame has value one, and hence leaves the constant Higgs value unchanged. For (HC.13) the curve term is exactly \(6\,dx\). We have not yet proved that this covector survives a proper bounded Hecke pushforward. Section 3.26 proves the bounded affine-Springer isolation in both directions. Sections 3.27–3.29 prove global cotangent compatibility, the global compatible-Higgs fibre and the moving relation. Sections 3.30–3.32 prove the bounded intersection-complex fibre at its open orbit and actual source-covector membership. The full Hecke/spectral action and its regularity identification remain required. Nor do these local computations construct the spectral projector or prove regular singularities. Those are the remaining geometric steps in §9.

![The compatible Jordan components select a Levi and a cocharacter; formal correction removes off-Levi coefficients; crystal minus coordinate transport gives the positive residue, with an exact SL3 example.](figures/formal-hecke-covectors.svg)

*Figure 3.6.* The center and root conditions are (HC.3)–(HC.8), the correction and its uniqueness are (HC.9)–(HC.12), and the framed quotient, cotangent pairs and curve residue are (HC.15)–(HC.22). The lower matrix example is exactly (HC.13)–(HC.14); its value \(6\,dx\) includes the nilpotent block and the specified trace form. The diagram displays these formal maps and coefficients, not a global Hecke image theorem. Free further reading is [Gaitsgory–Kazhdan–Rozenblyum–Varshavsky, *A toy model for the Drinfeld–Lafforgue shtuka construction*, Appendix B, §B.6](https://arxiv.org/abs/1908.05420v5), and [AGKRRV, §§20.4–20.8](https://arxiv.org/abs/2010.01906v2).

**Exercise 3.P.** Verify (HC.14) over \(R[[u]]\) for an arbitrary \(k\)-algebra \(R\). Compute the residue for the constant Higgs matrix \(C\) and the loop \(\lambda(u)\) of (HC.13).

**Solution 3.P.** The two root matrices in \(X_1\) have zero pairwise products, so \(X_1^2=0\), \(h^{-1}=1-uX_1\), and \(\det h=1\). The displayed commutators give \([X_1,C]=-E_{23}\) and \([X_1,E_{23}]=0\). Their further commutator is zero, so conjugation adds just \(-uE_{23}\) and kills the off-Levi coefficient exactly. These are polynomial identities with denominators three and nine, which remain units over every \(R\). The logarithmic derivative of the diagonal loop is \(u^{-1}\operatorname{diag}(1,1,-2)\). The trace pairing with \(C\,du\) has residue \(1+1+4=6\); the off-diagonal \(E_{12}\) has zero trace against that diagonal matrix. Thus the curve covector is \(6\,dx\).

**Exercise 3.Q.** Over \(k[\varepsilon]/\varepsilon^2\), compare the completions and punctured rings for centers zero and \(\varepsilon\). For \(G=\mathbb G_m\) and loop \(u^m\), determine the crystal-minus-coordinate tangent and its pairing with \(a(u)du\).

**Solution 3.Q.** The cofinal-ideal calculation gives the same completion, and \((t-\varepsilon)^{-1}=t^{-1}+\varepsilon t^{-2}\) gives the same punctured ring. Absolute transport becomes \((u+\varepsilon)^m=u^m+\varepsilon m u^{m-1}\), including negative integers by the finite nilpotent binomial identity. Left trivialization gives \(m/u\). Its residue against the regular covector is \(m a(0)\), so the discrepancy is \(m a(0)dx\). Using the coordinate-minus-crystal tangent instead would negate it.

**Exercise 3.R.** For a nonzero Lie element \(a\) of \(\mathbb G_m\), compute \(H,N,M\) and the formal normalization in (HC.10)–(HC.11). Explain why adjoint nilpotence alone would miss the covector in (HC.22).

**Solution 3.R.** In the faithful one-dimensional representation, \(H=a\) and \(N=0\). The torus centralizes itself, so \(M=G\) and \(\mathfrak n=0\); every formal series is already Levi-valued and the identity frame normalizes it. The identity cocharacter has nonzero pairing \(B(a,1)\), since the form on the one-dimensional Lie algebra is nondegenerate. But every adjoint endomorphism is zero for an abelian Lie algebra. Defining nilpotence only by that endomorphism would incorrectly include \(a\) and lose this nonzero central curve covector. Faithful-representation nilpotence, as in (HC.1)–(HC.4), retains it.

### 3.26. Tangent rigidity at the central Levi modification

We now use formal Levi invertibility to isolate the actual cocharacter modification. Keep the field and group assumptions of §3.23. Let \(M\) be the Levi centralizing the chosen cocharacter \(\lambda\), and write \(\mathfrak g=\mathfrak m\oplus\mathfrak n\) for its zero and nonzero weight spaces. After (HC.11), take
\[
 A(u)\in\mathfrak m(k[[u]]),\qquad
 D_0=\operatorname{ad}A(0)|_{\mathfrak n}\text{ invertible},\qquad
 g_0=u^\lambda.
                                                        \tag{AS.1}
\]
The full affine Grassmannian retains its nilpotent coefficient tests. The bound used below is the reduced Schubert closure of the arc orbit \(\mathcal O_\lambda=L^+G\cdot u^\lambda\), as in [*Orbits and Schubert varieties in the affine Grassmannian*](../../GL-SAT/src/GL-SAT-04.md), Theorem 3.5. In particular it is the closure of this orbit, rather than the whole possibly nonreduced affine Grassmannian. The same orbit is defined for a nondominant cocharacter; its dominant Weyl representative names the same bound.

Define the affine-Springer functor and its bounded part by
\[
 \operatorname{Spr}_{G,A}(R)
 =\{gL^+G:\operatorname{Ad}_{g^{-1}}A(u)
                       \in\mathfrak g(R[[u]])\},\qquad
 Z_{A,\lambda}=\operatorname{Spr}_{G,A}
                       \cap\overline{\mathcal O_\lambda}.
                                                        \tag{AS.2}
\]
Here the formula is interpreted on étale local frames with descent, so it specifies the scheme condition on families. A right arc change preserves it. By centrality of \(\lambda\) in \(M\), the displayed point \(g_0L^+G\) belongs to this functor.

**Isolation theorem.** Under (AS.1), \(u^\lambda\) is an isolated reduced point of \(Z_{A,\lambda}\). Equivalently, it has an open neighborhood in this bounded affine-Springer scheme isomorphic to \(\operatorname{Spec}k\).

**Proof.** We first identify an actual finite-type neighborhood. The finite-jet stabilizer calculation in the Schubert lesson, §2, works on every coefficient algebra. For an arc \(a\), the stabilizer condition is \(u^{-\lambda}a u^\lambda\in L^+G\); its root parameter for \(\alpha\) is divisible by \(u^{\max(0,\langle\alpha,\lambda\rangle)}\). A sufficiently deep congruence group belongs to the stabilizer. The orbit is therefore the quotient of a smooth finite-type jet group by its smooth stabilizer. The full proof there gives its scheme structure and tangent space, including nonreduced tests.

The orbit is locally closed in the finite-type stages and open in its Schubert closure. One can check the last assertion scheme-theoretically: for a locally closed immersion \(Y\hookrightarrow X\), choose an open \(U\subset X\) in which \(Y\) is closed. The kernel ideal defining the schematic closure restricts on \(U\) to the original ideal of \(Y\), by localization. Thus its intersection with \(U\) is exactly \(Y\); reduction preserves this equality when \(Y\) is smooth. This also explains why nilpotents of the full ambient affine Grassmannian do not enlarge the orbit neighborhood of this reduced bound.

On this neighborhood the Springer condition is closed. On a smooth finite-jet cover of the orbit a representative is \(a(u)u^\lambda\). In a faithful weight representation let \(D\) be the maximum of the absolute differences of the integral \(\lambda\)-weights. Conjugation by \(u^\lambda\) shifts every matrix coefficient by at most \(D\) powers. Thus only the jets through degree \(D\) of \(a\), \(a^{-1}\) and the fixed series \(A\) can contribute a negative coefficient of \(u^{-\lambda}\operatorname{Ad}_{a^{-1}}A\). Choose the jet order greater than \(D\) and than every positive root pairing. This both puts its congruence kernel in the stabilizer and makes these negative coefficients independent of the chosen arc lift. The finitely many coefficient equations are polynomial regular functions on that jet group. The condition is invariant under the stabilizer on every coefficient algebra, since right arcs preserve regular Lie series; hence its defining ideals agree on the two pullbacks of the faithfully flat orbit cover and descend. This is closed-ideal descent, proved by the module equalizer and affine descent in [*Beauville–Laszlo gluing and the moduli interpretation*](../../GL-SAT/src/GL-SAT-03.md), §2. Consequently \(Z_{A,\lambda}\cap\mathcal O_\lambda\) is a finite-type closed subscheme of the smooth orbit. We have used equations on test algebras, rather than a condition only on geometric points.

Left tangent trivialization writes a deformation as \(g_0(1+\varepsilon X)\). The arc-orbit tangent space is
\[
 T_{g_0}\mathcal O_\lambda
 =\frac{\operatorname{Ad}_{g_0^{-1}}\mathfrak g[[u]]}
 {\operatorname{Ad}_{g_0^{-1}}\mathfrak g[[u]]
                  \cap\mathfrak g[[u]]}.
                                                        \tag{AS.3}
\]
Every class has a representative in \(\mathfrak n((u))\). Indeed the zero-weight part is \(\mathfrak m[[u]]\) and vanishes in this quotient. Root weights with positive \(\langle\alpha,\lambda\rangle\) contribute only their finite principal parts; the others contribute nothing. This is also immediate by conjugating the integral tangent quotient in the Schubert lesson.

Because \(g_0\) commutes with \(A\), differentiating the closed Springer equations gives
\[
 \operatorname{Ad}_{(g_0(1+\varepsilon X))^{-1}}A
       =A+\varepsilon[A,X],\qquad
                 [A,X]\in\mathfrak g[[u]].
                                                        \tag{AS.4}
\]
Changing \(X\) by a right-arc tangent changes its bracket by a regular series, so this condition is well-defined on (AS.3).

The operator \(D(u)=\operatorname{ad}A(u)|_{\mathfrak n[[u]]}\) is an invertible formal matrix. To prove this, put \(E(u)=D_0^{-1}(D(u)-D_0)\), whose constant term is zero. Then
\[
 D(u)^{-1}=\left(\sum_{j\geq0}(-E(u))^j\right)D_0^{-1}
                \in\operatorname{End}(\mathfrak n)[[u]].
                                                        \tag{AS.5}
\]
Every coefficient receives only finitely many terms. This proof works over arbitrary coefficient algebras whenever \(D_0\) is invertible. Since \(A\) is Levi-valued, its bracket preserves the complement. For the representative \(X\in\mathfrak n((u))\), (AS.4) therefore says \(D(u)X\in\mathfrak n[[u]]\). Applying (AS.5) forces \(X\in\mathfrak n[[u]]\), whose tangent class is zero. Consequently
\[
 T_{u^\lambda}Z_{A,\lambda}=0.
                                                        \tag{AS.6}
\]

This proves scheme isolation, including the absence of infinitesimal thickening at the chosen point. We spell out the local algebra needed for that conclusion. Finite-type algebras over a field are Noetherian: inductively, if \(B\) is Noetherian, the leading coefficients of an ideal in \(B[t]\) form a finitely generated ideal. Choose polynomials realizing those generators, and let \(d\) bound their degrees. They cancel the leading coefficient of every ideal element of degree at least \(d\), reducing to degree less than \(d\). The remaining elements form a submodule of \(B^d\), which is finitely generated: induction on the number of coordinates uses the finitely generated image ideal and the kernel in one fewer coordinates. These finitely many polynomials generate the original ideal. Starting with the field proves the polynomial-ring assertion; ideals in a quotient are generated by images of generators of their preimages. Ideals in a localization are extensions of their contractions, so those local rings are Noetherian too.

The maximal ideal \(\mathfrak q\) of our local ring has \(\mathfrak q/\mathfrak q^2=0\) by (AS.6). Write a finite vector of ideal generators as \(v=Cv\), with every entry of \(C\) in \(\mathfrak q\). The determinant of \(I-C\) has residue one, hence is a unit; its adjugate identity forces \(v=0\). This is the needed Nakayama argument, and proves that the local ring is the residue field \(k\). To see that an open neighborhood is actually this point, choose an affine neighborhood with ring \(B\) and maximal ideal \(p\). Each of its finitely many ideal generators becomes zero in \(B_p=k\), so a product \(f\notin p\) of their annihilating denominators kills \(p\). Thus \(pB_f=0\) and \(B_f=B_f/pB_f=k\). This is the required open reduced singleton. \(\square\)

In particular every nonreduced coefficient test into this open neighborhood is the constant section. Replacing \(\lambda\) by \(-\lambda\) preserves its centralizer and the adjoint invertibility hypothesis. The same proof therefore isolates the inverse modification in the opposite Schubert bound, the closure of \(\mathcal O_{-\lambda}\). Its positive-weight roots are the opposite ones. The theorem concerns these bounded Springer schemes near the specified modifications. Sections 3.27–3.29 prove global cotangent compatibility and transfer this isolation to the global compatible-Higgs fibre. Sections 3.30–3.32 put the corresponding covector in the actual bounded intersection-complex source support. Survival under proper Hecke direct image, in its applicable regular holonomic context, still has to be proved before the isolation gives an automorphic support conclusion. It also gives no spectral projector or regularity conclusion by itself. Free further reading for this geometric step is [AGKRRV, §§20.7–20.8](https://arxiv.org/abs/2010.01906v2).

![The finite principal parts of the arc-orbit tangent are killed by the formal adjoint inverse; zero tangent gives an open reduced Springer point, with six exact SL3 coefficients and a torus infinitesimal direction outside the bound.](figures/affine-springer-tangent-isolation.svg)

*Figure 3.7.* The orbit tangent and regularity equation are (AS.3)–(AS.4); the formal inverse and the zero tangent are (AS.5)–(AS.6). The finite-type local-ring argument then gives the open reduced point. The six \(SL_3\) coefficients are computed in Exercise 3.S, and Exercise 3.U verifies their coupled equations over coefficient rings. Exercise 3.T explains the separate torus direction in the full Grassmannian. The reduced Schubert bound and the full nonreduced moduli functor both retain their stated meanings.

**Exercise 3.S.** For the trace-form \(SL_3\) example (HC.13), list the six tangent coefficients of the orbit at \(u^\lambda\). Verify directly that none survives the Springer condition for the constant series \(A=C\).

**Solution 3.S.** The two roots \(E_{13}\) and \(E_{23}\) have weight three, so each contributes the powers \(u^{-3},u^{-2},u^{-1}\); all other roots and the torus contribute zero. Write the principal part as \(X=\sum_{j=1}^3 u^{-j}(a_jE_{13}+b_jE_{23})\). Its bracket with \(C\) has coefficients \((3a_j+b_j)E_{13}+3b_jE_{23}\). Regularity requires \(3b_j=0\) and \(3a_j+b_j=0\) for every \(j\), so all six coefficients vanish. The invertible block is \(\begin{pmatrix}3&1\\0&3\end{pmatrix}\), including the nilpotent \(E_{12}\) term. Thus the actual bounded Springer point is isolated and reduced by the local-ring argument.

**Exercise 3.T.** For \(G=\mathbb G_m\) and \(A=a(u)\), compare the bounded Springer scheme for the orbit of \(u^m\) with the full Springer functor over \(k[\varepsilon]/\varepsilon^2\).

**Solution 3.T.** The adjoint action is trivial, so the full Springer functor is the full affine Grassmannian. The arc orbit of \(u^m\) is a single reduced point, and its reduced Schubert closure is the same point; its bounded Springer scheme is therefore \(\operatorname{Spec}k\). Nevertheless \(u^m(1+\varepsilon/u)\) is a valid loop, with inverse \(u^{-m}(1-\varepsilon/u)\), and represents a nontrivial infinitesimal Grassmannian point: the quotient factor \(1+\varepsilon/u\) is not an arc. This direction lies in the full Springer functor and outside the bound. It confirms both bounded isolation and the need to retain nilpotents in the full moduli problem.

**Exercise 3.U.** Over any coefficient \(k\)-algebra \(R\), replace the constant matrix in Exercise 3.S by \(A(u)=\operatorname{diag}(1,1,-2)+(1+u\vartheta)E_{12}\), with \(\vartheta\in R\). Compute the complementary adjoint block on \(E_{13},E_{23}\), its formal inverse, and the principal-part tangent equations. No reducedness hypothesis on \(R\) is allowed.

**Solution 3.U.** In this ordered root basis the block and its inverse are \(\begin{pmatrix}3&1+u\vartheta\\0&3\end{pmatrix}\) and \(\begin{pmatrix}1/3&-(1+u\vartheta)/9\\0&1/3\end{pmatrix}\). Their products in both orders are the identity. For the six coefficients \((a_j,b_j)\), the negative powers impose \(3b_j=0\) and \(3a_j+b_j+\vartheta b_{j+1}=0\), where \(b_4=0\). Since three is a unit, these equations first kill all \(b_j\), then all \(a_j\). This works for nilpotent \(\vartheta\), nonreduced \(R\), or an arbitrary parameter. In the order \((a_1,b_1,a_2,b_2,a_3,b_3)\), the six-by-six coefficient matrix is block upper triangular with three diagonal blocks of determinant nine, so its determinant is \(9^3=729\). Thus no coefficient-ring tangent is lost by replacing the constant field calculation with this family.

### 3.27. Global Hecke cotangents from the gluing groupoid

Work at a geometric point over an algebraically closed field \(k\) of characteristic zero. Let \(X\) be a smooth connected projective curve, \(x\in X(k)\), and \(U=X-\{x\}\). A global modification is an isomorphism \(\alpha:P_2|_U\to P_1|_U\). Write \(p_i\) for its two bundle projections and \(r_x\) for restriction to the local Hecke groupoid. We retain the orientation of (HC.18).

First, \(U\) is affine. The Euler-characteristic calculation in [*The moduli stack of bundles*](the-moduli-stack-of-bundles.md), §2.4, (DS.13), gives \(h^0(\mathcal O_X(nx))\ge n+1-g\). For \(n>g\), choose a nonconstant rational function with poles supported at \(x\). The finite-morphism argument of §2.5 makes it a finite map to \(\mathbb P^1\). Its inverse image of \(\mathbb A^1\) is precisely \(U\), hence is affine. We will use the affine vanishing and Čech comparison proved in [*Cohomology of affine schemes and Serre's criterion*](../../AG-QC/src/affine-cohomology-and-serres-criterion.md), Theorems 2.2 and 3.1.

Identify the adjoint bundles on \(U\) using \(\alpha\). Their common bundle there is \(E\), and set \(V=\Gamma(U,E)\). Choose disc frames and a parameter \(u\); use the second frame to transport all punctured sections into the common space
\[
 W=\mathfrak g((u)),\qquad
 L_2=\mathfrak g[[u]],\qquad
 L_1=\operatorname{Ad}_{g^{-1}}\mathfrak g[[u]],\qquad
 V\hookrightarrow W.
                                                        \tag{HG.1}
\]
Here \(g\) represents \(\alpha:P_2\to P_1\). The last injection follows by restricting to the function field and then to its Laurent-series completion. A nonzero rational section cannot acquire zero Laurent expansion: a nonzero element of the local DVR has a finite valuation. No trivialization of the bundle on all of \(U\) is required.

For either global adjoint bundle \(E_i\), principal parts at \(x\) give
\[
 H^1(X,E_i)=W/(V+L_i).
                                                        \tag{HG.2}
\]
Indeed, \(E_i(*x)=j_*(E_i|_U)\), where \(j:U\hookrightarrow X\): locally a section on the complement of a Cartier divisor has a finite pole, and a finite affine cover clears these poles uniformly for each section. The quotient \(E_i(*x)/E_i\) has section space \(W/L_i\), since each principal part is a finite Laurent polynomial in a disc frame. Its higher cohomology vanishes: it is the filtered union of finite-length sheaves supported at \(x\), whose affine section functor is exact; finite affine Čech complexes commute with that union. Affine vanishing on \(U\) gives \(H^1(X,E_i(*x))=0\). The long exact sequence therefore gives (HG.2).

We fix the cotangent–Higgs identification by the perfect residue pairing
\[
 \xi_i([a_i])=
    \operatorname{Res}_x\langle A_i,a_i\rangle,
 \qquad A_i\in\Gamma(X,E_i^*\otimes\omega_X).
                                                        \tag{HG.3}
\]
Regularity annihilates \(L_i\). The global residue theorem proved in §2.5 annihilates \(V\), because \(\langle A_i,v\rangle\) has its only possible pole at \(x\). Thus (HG.3) is well defined. It is injective: a nonzero Laurent coefficient of \(A_i\) pairs nontrivially with an opposite Laurent monomial in \(W\). The dimensions of its source and target are equal by Theorem 4.2 of [*Dualizing sheaves and Serre duality for projective schemes*](../../AG-QC/src/dualizing-sheaves-and-serre-duality-for-projective-schemes.md). For this application its dualizing line is \(\omega_X\): a local Koszul resolution in projective space gives \(\det(I/I^2)^\vee\otimes\omega_{\mathbb P}|_X\), and the determinant of the conormal sequence identifies that line with \(\Omega_X^1\). Hence (HG.3) is an isomorphism. This proves the residue normalization rather than assuming a sign for a connecting homomorphism.

We now compute the entire first-order groupoid at the modification, with \(x\) fixed. The square-zero torsor deformation calculation of the previous lesson, §§2.1–2.2, and affine vanishing trivialize each deformation relative to the fixed bundle on \(U\) and on the disc. The disc trivialization also follows directly from smooth formal lifting, §7.9 of that lesson. Effective gluing, including arrows, is proved in [*Beauville–Laszlo gluing and the moduli interpretation*](../../GL-SAT/src/GL-SAT-03.md), Theorem 3.1. Thus a deformation is a triple \((a_1,a_2,b)\in W^2\oplus V\): the first two entries change the bundle gluing maps, and \(1+\varepsilon b\) changes \(\alpha\) on \(\,U\).

Changing the chosen identifications on \(U\) by \(U_1,U_2\in V\), and on the discs by \(v_i\in L_i\), gives the tangent complex
\[
 [\,V^2\oplus L_1\oplus L_2
   \xrightarrow{d}W^2\oplus V\,],\qquad
 d(U_1,U_2,v_1,v_2)
   =(U_1-v_1,U_2-v_2,U_1-U_2),
                                                        \tag{HG.4}
\]
in degrees \(-1,0\). Its kernel retains the infinitesimal automorphisms. The bundle projections send the triple to \([a_i]\) in (HG.2). The local projection sends it to
\[
 q=b-a_1+a_2\pmod{L_1+L_2}.
                                                        \tag{HG.5}
\]
To verify the sign, let \(\psi_i\) be the two original disc-to-complement gluing maps, after identifying the complement bundles. The deformed local isomorphism is
\(\psi_1^{-1}(1-\varepsilon a_1)(1+\varepsilon b)(1+\varepsilon a_2)\psi_2\).
After tangent trivialization by \(\psi_2\), its relative right factor is \(1+\varepsilon(b-a_1+a_2)\). Applying (HG.5) to a boundary in (HG.4) gives \(v_1-v_2\), exactly the local arc boundary. Thus it defines the actual map of deformation groupoids.

**Global compatibility theorem.** Let \(\eta\) be a local cotangent vector as in (HC.17), and let \(\xi_i\) be the global covectors (HG.3). Then
\[
 p_1^*\xi_1+r_x^*\eta=p_2^*\xi_2
 \quad\Longleftrightarrow\quad
 \begin{cases}
 A_2=\alpha^*A_1\text{ on }U,\\
 \eta\text{ is their common local covector in the second frame.}
 \end{cases}
                                                        \tag{HG.6}
\]
**Proof.** Suppose first that the equality holds. Evaluate it on \((a_1,0,0)\) for every \(a_1\in W\). Equations (HG.3) and (HG.5) give \(\operatorname{Res}\langle A_1-\eta,a_1\rangle=0\), with \(A_1\) transported into the common frame. The perfect Laurent coefficient pairing forces \(A_1=\eta\) on the punctured disc. Evaluating on \((0,a_2,0)\) similarly gives \(A_2=\eta\). Equality of Laurent expansions is equality of rational sections, so the two fields agree on \(U\).

Conversely, let \(A\) be their common field on \(U\), and use its common local covector for \(\eta\). The term \(\operatorname{Res}_x\langle A,b\rangle\) vanishes by the global residue theorem: this is a rational differential with no other possible pole. Hence evaluation on any triple gives
\[
 r_x^*\eta(a_1,a_2,b)
  =\operatorname{Res}_x\langle A,-a_1+a_2\rangle
  =(p_2^*\xi_2-p_1^*\xi_1)(a_1,a_2,b).
                                                        \tag{HG.7}
\]
All three functionals annihilate the boundaries in (HG.4), so this is equality on the classical tangent space, with its automorphisms retained in the displayed complex. \(\square\)

### 3.28. The compatible global fibre and nilpotent coefficients

The gluing consequence holds on every ordinary coefficient \(k\)-algebra \(R\), including nonreduced ones. Fix \((P_1,A_1,x)\), extend these data to \(R\), and fix a formal frame of \(P_1\). Use an invariant nondegenerate bilinear form \(B\) to identify the coadjoint field with an adjoint-valued differential, writing its disc expression as \(A(u)du\). A modification represented by \(gL^+G\) admits a compatible regular global field on \(P_2\) exactly when
\[
 A_2|_U=\alpha^*A_1|_U,
 \qquad A_2|_{D_R}=\operatorname{Ad}_{g^{-1}}A(u)\,du
       \text{ is regular.}
                                                        \tag{HG.8}
\]
The forward implication is restriction. For the converse, these two sections agree on the punctured disc, and effective vector-bundle gluing in the previous lesson, §§7.1–7.4, gives their global section. Apply its fully faithful map gluing to the maps from the trivial line into the coadjoint differential bundle. This works with every coefficient ring and commutes with coefficient change. It is unique: restriction to the complement of the graph is injective on a locally free sheaf. Here is the relative Cartier argument on all coefficient rings. In an étale curve coordinate the graph is locally the pullback of \(t-a=0\). Multiplication by the monic polynomial \(t-a\) on \(R[t]\) is injective by its leading coefficient; localization and flat étale base change preserve this injection. Thus the graph has a local defining nonzerodivisor \(f\), even for nonreduced \(R\). Multiplication by every \(f^n\) is then injective on a free module, so localization at \(f\) is injective. This also proves the injectivity needed for moving graphs.

Consequently, with the input object fixed by a specified identification, the functor of compatible Higgs modifications is
\[
 \{(P_2,\alpha,A_2):\alpha^*A_1=A_2\text{ on }U_R\}
   \simeq\operatorname{Spr}_{G,A}(R).
                                                        \tag{HG.9}
\]
This is an equivalence of the full test functors, not only a bijection of field points. Changing the second disc frame is precisely right multiplication by an arc; (HG.8) is invariant under it, and faithfully flat descent removes the frame. There are no extra automorphisms in this fibre. An automorphism fixing the identified input and commuting with \(\alpha\) is the identity on \(U_R\); apply the same Cartier injectivity to its difference from the identity in a faithful associated vector bundle. Faithfulness then makes it the identity everywhere. Thus the fibre has the Grassmannian functor, rather than an additional coarse quotient by the input automorphisms.

Restricting (HG.9) to the reduced Schubert bound gives the bounded Springer scheme of §3.26. Under its exact hypotheses, the point \(u^\lambda\) is therefore an open reduced point of the **global compatible-Higgs modification fibre**. Fixing the output instead and inverting \(\alpha\) gives the same conclusion in the opposite bound for \(u^{-\lambda}\). All the coefficient tests of these open points are constant, as proved after (AS.6). This transfers the local isolation to the global fibre without asserting a direct-image theorem.

We also retain the scheme-theoretic nilpotent conditions. If \(F\in k[\mathfrak g]^G\) is homogeneous of positive degree \(d\), evaluation on an adjoint Higgs field gives a section of \(\omega_{X_R/R}^{\otimes d}\). Homogeneity makes the local differential-frame expressions agree; invariance makes conjugate fields agree on \(U_R\). Cartier injectivity therefore gives
\[
 F(A_1)=F(A_2)
       \quad\text{in }\Gamma(X_R,\omega_{X_R/R}^{\otimes d}).
                                                        \tag{HG.10}
\]
Invariance here is an identity of the group coaction on the polynomial algebra, so it remains valid for \(G(R((u)))\), not just for field-valued conjugations. Thus the simultaneous vanishing of all positive-degree invariant sections, the zero-Hitchin-fibre conditions, is preserved on all these tests:
\[
 (P_1,A_1)\text{ lies in the global nilpotent fibre}
 \quad\Longleftrightarrow\quad
 (P_2,A_2)\text{ does}.
                                                        \tag{HG.11}
\]
The field-valued criterion agrees with the nilpotence convention of §3.7. Over nonreduced rings it is the invariant equations themselves that (HG.11) preserves. Nilpotence of a matrix over a ring by itself is a weaker condition, as Exercise 3.X shows.

### 3.29. The global moving-point covector

Let \(\mathcal H_X\) be the moving global Hecke groupoid, \(r:\mathcal H_X\to\mathcal H_X^{\mathrm{loc}}\) its restriction, and \(s:\mathcal H_X\to X\) the point projection. The crystal transport constructed in (HC.19) fixes both global bundles and their isomorphism on the common complement when the center changes infinitesimally. Restriction commutes with this transport. It therefore gives compatible splittings of the tangent spaces into their fixed-point parts and their \(T_xX\) directions. In particular, the global bundle projections have zero derivative on the crystal horizontal direction:
\[
 p_i^*\xi_i\text{ has crystal curve component }0,
 \qquad r\text{ respects the crystal splittings.}
                                                        \tag{HG.12}
\]
This follows from the actual nilpotent-ring identity of complements and completions, not from a choice of a locally constant bundle in a coordinate chart.

Take a local moving covector \(\theta\) whose fixed-point restriction is \(\eta\) and whose curve component is zero in the coordinate splitting \(u=t-x\). For a general loop its curve component in the crystal splitting is the discrepancy computed in (HC.21). Combining (HG.6) with (HG.12) proves the full moving relation
\[
 p_1^*\xi_1+r^*\theta=p_2^*\xi_2+s^*\xi_x,
 \qquad
 \xi_x=\operatorname{Res}_{u=0}
       \langle\eta,g^{-1}g'\rangle\,dx,
                                                        \tag{HG.13}
\]
provided the fields are compatible. Conversely the displayed cotangent equality forces the fixed-point compatibility and this curve term: evaluate it first on all fixed-point tangents, then on the crystal horizontal tangent. The positive sign corresponds to crystal lift minus coordinate lift. The formula for a general loop uses the stated coordinate splitting.

Now suppose the input Higgs field has a nonnilpotent value at \(x\). Write that value as \(C=H+N\) and use §3.23 to choose a centralizer-detecting cocharacter with
\[
 M=C_G(H)=C_G(\lambda),\qquad
 B(C,d\lambda)=B(H,d\lambda)\ne0.
                                                        \tag{HG.14}
\]
The formal normalization of §3.24, whose initial coefficient is the identity, puts \(A(u)\) in \(\mathfrak m[[u]]\) while retaining \(A(0)=C\). Its complementary adjoint is invertible. Since \(u^\lambda\) commutes with this series, (HG.8) glues a compatible global field on the modified bundle. The two disc fields are this same series in their chosen frames. Equations (HC.22) and (HG.13) give
\[
 g=u^\lambda,\qquad
 \xi_x=B(C,d\lambda)\,dx\ne0.
                                                        \tag{HG.15}
\]
This cocharacter covector is intrinsic by the parameter-change calculation following (HC.22). Both bounded compatible-Higgs fibres, for the modification and its inverse, have the open reduced points proved in §3.28. We have therefore constructed
\[
 \begin{gathered}
 \xi_x\ne0,\\
 u^{\pm\lambda}\text{ is an open reduced point in its bounded compatible fibre.}
 \end{gathered}
                                                        \tag{HG.16}
\]
The assertion is conditional on a nonnilpotent global input value; it does not assume that every curve admits such a value.

The actual Satake object must still be shown to contain the required local covector in its singular support, and an isolated canonical-relation point must still be shown to survive the proper Hecke direct image. Neither follows merely from (HG.16). The full spectral action, projector image and regularity argument remain to be proved. Free further reading for the global cotangent diagram and the compatible crystal splittings is [Gaitsgory–Kazhdan–Rozenblyum–Varshavsky, Appendix B.6.5–B.6.8](https://arxiv.org/abs/1908.05420v5).

![The fixed-point gluing tangent maps to b minus a1 plus a2; the global residue theorem supplies the compatibility identity. Compatible Higgs fields glue uniquely on all coefficient tests. At the normalized central cocharacter the moving curve covector is nonzero, and both bounded global compatible fibres are isolated reduced points.](figures/global-hecke-cotangent.svg)

*Figure 3.8.* The tangent maps are (HG.4)–(HG.5), and the residue equality is (HG.7). The all-ring fibre equivalence and invariant equations are (HG.9)–(HG.11). The moving relation and its nonzero cocharacter term are (HG.13)–(HG.15), with the sign fixed by (HC.20). The two isolated fibres use (AS.6). The numerical value shown is computed in Exercise 3.V. The global cotangent diagram has free further reading in [Gaitsgory–Kazhdan–Rozenblyum–Varshavsky, Appendix B.6](https://arxiv.org/abs/1908.05420v5).

**Exercise 3.V.** Let \(X\) have a nonzero regular differential \(\omega\), choose \(x\) with \(\omega(x)\ne0\), and write \(\omega=q(u)du\) on the disc. Take the trivial \(SL_3\)-bundle with Higgs matrix \(C\omega\), where \(C=\operatorname{diag}(1,1,-2)+E_{12}\). Modify by \(g=\operatorname{diag}(u,u,u^{-2})\). Determine the modified vector bundle and field, the invariant polynomial, and the moving curve covector for the trace form. Verify both isolation hypotheses.

**Solution 3.V.** The new lattice in the original punctured trivial bundle is \(u\mathcal O_D\oplus u\mathcal O_D\oplus u^{-2}\mathcal O_D\). Hence its global vector bundle is \(\mathcal O_X(-x)\oplus\mathcal O_X(-x)\oplus\mathcal O_X(2x)\), with its determinant trivialization. The first two summands are equal, so \(E_{12}\) defines a global homomorphism between them. The diagonal endomorphism and that homomorphism, multiplied by \(\omega\), give the compatible global field; on the disc it is again \(Cq(u)du\). In a differential frame the characteristic polynomial is \((T-1)^2(T+2)=T^3-3T+2\); on the curve its last two coefficients are \(-3\omega^2\) and \(2\omega^3\). They agree before and after modification and do not vanish. The cocharacter derivative is \(H=\operatorname{diag}(1,1,-2)\), so \(\operatorname{tr}(CH)=6\) and (HG.15) gives \(6q(0)dx\ne0\). The complementary adjoint blocks are \(q(0)\begin{pmatrix}3&1\\0&3\end{pmatrix}\) and \(q(0)\begin{pmatrix}-3&0\\-1&-3\end{pmatrix}\). Their determinants are \(9q(0)^2\ne0\). Thus §3.26 and the fibre equivalence isolate both directions, including the nilpotent Jordan summand.

**Exercise 3.W.** On \(X=\mathbb P^1\), take \(x=\infty\), \(u=1/z\) and \(G=\mathbb G_m\). The local cotangent vector \(\eta=du\) is regular for the modification \(u^m\). Show directly that it cannot satisfy (HG.6) with global Higgs fields. Identify a deformation that detects the failure.

**Solution 3.W.** A regular differential on \(\mathbb A^1_z\) is \(f(z)dz\) with \(f\) polynomial. At infinity it is \(-f(u^{-1})u^{-2}du\), which is regular only when \(f=0\). Thus all global torus Higgs fields vanish. Nevertheless \(L_1=L_2=k[[u]]\), so \(du\) is a valid local cotangent. Set \(a_1=a_2=0\), \(b=z=u^{-1}\). This is the dual-number change \(\alpha\mapsto(1+\varepsilon z)\alpha\) on the affine complement, keeping both bundles fixed. Its local tangent is \(q=u^{-1}\), and \(r_x^*\eta\) evaluates to \(\operatorname{Res}(du/u)=1\). Both global bundle covectors evaluate to zero. This proves the failure. In particular, the complement-isomorphism tangent \(b\) cannot be omitted from the gluing calculation. This deformation is in the full Hecke functor; the reduced torus Schubert bound of Exercise 3.T excludes its nilpotent Laurent direction.

**Exercise 3.X.** Over \(R=k[\varepsilon]/(\varepsilon^2)\), verify the invariant argument in (HG.10) without passing to reduced points. Then distinguish the invariant zero-fibre condition from matrix nilpotence using \(S=\varepsilon I_2\).

**Solution 3.X.** If two regular matrix series are conjugate after inverting \(u\), their characteristic polynomials are equal in \(R((u))[T]\): determinant multiplicativity cancels the conjugating matrix and its inverse. Every coefficient difference is in \(R[[u]]\) and becomes zero after localization. Multiplication by \(u\) is injective coefficient by coefficient even though \(R\) is nonreduced, so those differences are already zero. For any group-invariant polynomial the coaction identity gives the same argument. Globally a local defining equation of the Cartier graph replaces \(u\), and its injectivity on the relevant differential line gives (HG.10). Now \(S^2=0\), whereas \(\det(TI_2-S)=(T-\varepsilon)^2=T^2-2\varepsilon T\). Its trace invariant is \(2\varepsilon\ne0\). Thus \(S\) is a nilpotent matrix over \(R\), but it is not an \(R\)-point of the invariant zero fibre. The transport proof preserves the stronger invariant equations on every test ring, rather than only their vanishing on field points.

### 3.30. The bounded intersection complex at its open orbit

Fix an algebraically closed field of characteristic zero. Write \(O_\lambda=L^+G\,u^\lambda\) for the smooth arc orbit and \(B_\lambda=\overline{O_\lambda}_{\mathrm{red}}\) for its reduced Schubert closure. The finite-jet stabilizer and smoothness of the orbit are proved in Orbits and Schubert varieties in the affine Grassmannian, §2. The finite stages \(Y_N\) of the full Grassmannian retain their original scheme structures and arbitrary coefficient tests, by Loop groups and the affine Grassmannian, Lemma 7.3. In particular, replacing \(Y_N\) by its reduction is not part of this construction.

The bounded intersection-complex module \(K_\lambda\) is the middle extension of the constant connection on \(O_\lambda\), supported on \(B_\lambda\). We use left differential-operator modules; the constant connection on a smooth variety is its structure sheaf with the usual derivations. The image definition, restriction and uniqueness of middle extension are proved in Preservation of holonomicity and minimal extensions, Theorem 4.1. The conventional cohomological normalization of the intersection complex does not change characteristic support.

Choose a finite stage containing \(B_\lambda\) and a local closed embedding \(Y_N\hookrightarrow Z\) into a smooth variety. Such local embeddings exist: a finite-type affine coordinate ring is a quotient of a polynomial ring, giving a closed embedding into affine space. Near a point \(y\in O_\lambda\), remove the closed boundary \(B_\lambda\setminus O_\lambda\) from \(Z\). The remaining part of \(B_\lambda\) is exactly the smooth closed subvariety \(O_\lambda\). If \(i:O_\lambda\hookrightarrow Z\) denotes this local embedding, restriction of the middle extension is

\[
 K_\lambda|_Z=i_+\mathcal O_{O_\lambda}.
 \tag{BK.1}
\]

Here and below an ambient representative is extended by zero from its closed support. This use of a smooth ambient space is the intrinsic supported-module construction proved in Kashiwara's equivalence and D-modules on singular spaces, Theorems 3.1 and 5.1.

We compute (BK.1), including every normal direction. Take adapted étale coordinates \(z_1,\ldots,z_d,w_1,\ldots,w_c\), with the \(w_j\) cutting out the orbit and the \(z_i\) restricting to coordinates on it. These coordinates can be constructed by choosing generators of the conormal bundle and lifts of a cotangent basis on the smooth orbit. Their differentials form a basis at the point; the resulting map to affine space is étale on a neighbourhood. Trivialize the transfer density line in this coordinate chart. The delta generator \(e\) of the closed direct image satisfies

\[
 w_j e=0,\qquad \partial_{z_i}e=0,\qquad
 i_+\mathcal O_{O_\lambda}
 =\mathcal D_Z\big/
 \left(\sum_j\mathcal D_Zw_j+
       \sum_i\mathcal D_Z\partial_{z_i}\right).
 \tag{BK.2}
\]

The ideals displayed are left ideals. Commuting coordinates to the right and derivatives to the left gives the normal form \(\sum_\alpha f_\alpha(z)\partial_w^\alpha e\), with a finite sum for each section. Normal multiplication acts by lowering:

\[
 w_j\bigl(f\partial_w^\alpha e\bigr)
 =-\alpha_j f\partial_w^{\alpha-e_j}e.
 \tag{BK.3}
\]

The normal form is unique. Indeed, for one normal pair with \([\partial_w,w]=1\), the finite operator
\(\pi(m)=\sum_{r\geq0}\partial_w^r w^r m/r!\) projects to \(\ker w\). Applying \(\pi w^r\) to a normal polynomial recovers its coefficient of \(\partial_w^r\), multiplied by \((-1)^rr!\). For several normal pairs the projectors commute, and their product recovers each coefficient. Characteristic zero makes these scalars invertible. This is also the full-module proof of the normal decomposition, not just an argument for a finitely generated module; the formulas are finite on every supported section.

Filter by normal derivative degree, using the degree-zero constant connection on the orbit. Uniqueness of the normal form gives the actual associated graded module

\[
 \operatorname{gr}\bigl(i_+\mathcal O_{O_\lambda}\bigr)
 =\mathcal O_{O_\lambda}[\xi_{w_1},\ldots,\xi_{w_c}],
 \qquad w_j=0,\quad \xi_{z_i}=0.
 \tag{BK.4}
\]

Normal coordinates lower filtration degree, tangent derivatives act by differentiating degree-zero coefficients, and normal derivatives raise degree. Thus the symbols have precisely the stated action. The graded module is finitely generated over the ambient symbol ring, so this is a good filtration. Its support contains every normal covector, and contains no nonzero tangent covector. Density changes multiply the generator by an invertible function and modify tangent operators by order-zero terms. Their principal symbols, and hence this description, agree on overlaps.

**Proposition.** At every point \(y\in O_\lambda\), the ambient characteristic fibre of \(K_\lambda\) is the entire conormal vector space \(\operatorname{Ann}(T_yO_\lambda)\subset T_y^*Z\). In the original, possibly nonreduced finite stage, its intrinsic fibre is

\[
 \operatorname{SS}(K_\lambda)_y
 =\operatorname{Ann}\bigl(T_yO_\lambda\subset T_yY_N\bigr).
 \tag{BK.5}
\]

**Proof.** Formula (BK.4) proves the ambient assertion. The cotangent space of \(Y_N\) is the quotient of \(T_y^*Z\) by the differentials of its defining ideal. Equivalently, restriction \(T_y^*Z\twoheadrightarrow T_y^*Y_N\) is dual to the injection \(T_yY_N\hookrightarrow T_yZ\). A covector on \(T_yY_N\) annihilating \(T_yO_\lambda\) extends to one on \(T_yZ\) annihilating the same subspace: extend a basis of the orbit tangent first to the stage tangent and then to the ambient tangent. Conversely, every ambient conormal restricts to such a covector. The inverse image of this annihilator is the entire ambient conormal, since the kernel of restriction itself annihilates the stage tangent. This proves (BK.5) and its independence of the chosen smooth ambient embedding for this module. No smoothness or reducedness of \(Y_N\) was used. ∎

For two stages containing the bound, the inclusion \(Y_N\hookrightarrow Y_{N'}\) induces an injection on tangent spaces and a restriction map on cotangents. The same basis argument gives

\[
 \rho_{N'N}^{-1}\operatorname{SS}(K_\lambda)_y^{(N)}
 =\operatorname{SS}(K_\lambda)_y^{(N')},\qquad
 \rho_{N'N}:T_y^*Y_{N'}\twoheadrightarrow T_y^*Y_N.
 \tag{BK.6}
\]

The ambient modules represent the same middle extension: closed direct image is the supported-module equivalence, and the no-boundary-submodule and no-boundary-quotient characterization is unchanged. Thus (BK.6) is compatibility of the actual kernel, in addition to compatibility of vector-space annihilators.

At \(g=u^\lambda\), use \(W=\mathfrak g((u))\), \(L_2=\mathfrak g[[u]]\), \(L_1=\operatorname{Ad}(g^{-1})\mathfrak g[[u]]\). The full Grassmannian tangent is \(W/L_2\); its arc-orbit subspace is \((L_1+L_2)/L_2\). A compatible regular local covector from (HC.17) lies in \(\operatorname{Ann}(L_1+L_2)\), using the residue pairing. Every finite-stage tangent embeds into this full tangent, because the stage represents a subfunctor on dual numbers. Restriction therefore gives

\[
 \eta\in\operatorname{Ann}(L_1+L_2)
 \quad\Longrightarrow\quad
 \eta_N\in\operatorname{SS}(K_\lambda)_g^{(N)}
 \quad\text{for every stage containing the bound.}
 \tag{BK.7}
\]

This is membership in the kernel's characteristic fibre. The finite-stage restrictions form the compatible family (BK.6). Computing this fibre does not require a description of the characteristic support at boundary orbits.

### 3.31. External products for the full unbounded category

Let \(S\) be a smooth finite-type parameter chart, and let \(M\) be a coherent left \(\mathcal D_S\)-module. On \(S\times Z\), take its external product with (BK.1). A good filtration on \(M\), combined with normal derivative degree as in (BK.4), gives

\[
 \begin{aligned}
 \operatorname{gr}\bigl(M\boxtimes i_+\mathcal O_{O_\lambda}\bigr)
 &=\operatorname{gr}M\boxtimes
   \mathcal O_{O_\lambda}[\xi_w],\\
 \operatorname{Ch}\bigl(M\boxtimes i_+\mathcal O_{O_\lambda}\bigr)
 &=\operatorname{Ch}(M)\times T^*_{O_\lambda}Z.
 \end{aligned}
 \tag{BK.8}
\]

The support equality is exact. Locally the graded module is obtained by extending the input symbol module by the orbit coordinate algebra and the polynomial normal symbols. At any geometric point of the orbit and any values of the normal symbols, that extension has a nonzero localized fibre precisely when the input symbol module does. This follows by tensoring over the ground field and applying the finitely generated module version of Nakayama's lemma in the two symbol charts. The additional tangent symbols act as zero. Consequently there is no restriction on a normal covector and no enlargement of the input characteristic support.

For a full unbounded complex \(F\), use the cohomological support convention of §3.22: take the union of characteristic supports of coherent submodules of every \(H^mF\). No closure of this union is implicit. The functor
\(E(N)=N\boxtimes i_+\mathcal O_{O_\lambda}\) is exact on modules. Tensor over the ground field is exact, the constant connection has no extra derived tensor terms, and closed direct image is exact by the normal decomposition. Applying the functor degree by degree therefore commutes with cohomology even for an unbounded complex.

We also need the converse to the inclusion obtained from coherent input submodules. Work locally. A finitely generated submodule \(A\subset E(N)\) has finitely many generators. Expand them into normal polynomials. Each of their finitely many coefficients in \(N\boxtimes\mathcal O_{O_\lambda}\) is a finite sum of input sections tensored with orbit functions. Choose the \(\mathcal D_S\)-submodule \(N_0\subset N\) generated by these finitely many input sections. The differential-operator ring on a smooth finite-type chart is Noetherian, so \(N_0\) is coherent. Exactness embeds \(E(N_0)\) into \(E(N)\). This image is stable under all ambient differential operators, by the transfer construction, and it contains the chosen generators. Hence \(A\subset E(N_0)\). Characteristic support of a coherent submodule is contained in that of its containing coherent module, by the strict induced good filtration argument used in §3.22. Conversely each \(E(N_0)\) is itself a coherent submodule. Taking both unions proves

\[
 \operatorname{SS}_{\infty}(E(F))
 =\operatorname{SS}_{\infty}(F)\times T^*_{O_\lambda}Z.
 \tag{BK.9}
\]

This proof uses individual finite generators; it imposes no boundedness on \(F\). Passing to a singular finite stage means taking the cotangent quotient in (BK.5), giving the same product with the stage annihilator. On the smooth open orbit itself, the relative factor is simply the zero section. The smooth chart-transfer formula (NS.7) makes these computations compatible with further smooth parameter charts. They establish the needed full-category product calculation without asserting that the unbounded derived category is the derived category of an ind-holonomic heart.

### 3.32. Finite frames and membership in the global Hecke source

We now realize the parameter product used above at the open orbit of the bounded global Hecke correspondence. Fix a finite-type smooth chart \(Q\to\operatorname{Bun}_G\) carrying the input bundle, and choose an étale curve coordinate near the modification point. For a moving point with coordinate \(a\), put \(u=t-a\). The completion along its graph is \(R[[u]]\) on every affine coefficient test. To see this, the formal completion of an étale coordinate chart lifts the chosen graph section uniquely through each nilpotent thickening of the coordinate graph; induction identifies its quotients with \(R[u]/u^n\). Their inverse limit is \(R[[u]]\). The graph is Cartier by the monic-coordinate argument in §3.28.

Choose \(M\) larger than all positive root pairings with \(\lambda\), and set

\[
 G_M(R)=G(R[u]/u^M),\qquad
 K_M=\ker\bigl(L^+G\longrightarrow G_M\bigr),\qquad
 O_\lambda=G_M/(H_\lambda/K_M).
 \tag{BK.10}
\]

The stabilizer proof cited in §3.30 establishes \(K_M\subset H_\lambda\) on all rings. Since \(K_M\) is normal in \(L^+G\), it fixes every point of the orbit, also on nonreduced tests: for an arc \(h\), the stabilizer of \(hu^\lambda\) is \(hH_\lambda h^{-1}\), which still contains \(K_M\). Thus (BK.10) is a quotient of actual functors, not only a description of geometric points.

Let \(\mathrm{Fr}_M\) be the scheme of frames of the input bundle on the graph modulo \(u^M\). It is a \(G_M\)-torsor over \(Q\times X\), restricted to the coordinate neighbourhood. It is affine and of finite presentation: in a faithful matrix representation, substitute a matrix polynomial of degree below \(M\) into the group's equations and the frame equations, and equate its finitely many coefficients modulo \(u^M\); invert the determinant of its constant term. Descent from local frames identifies these equations intrinsically. The group \(G_M\) is smooth. Reduction to \(G\) has successive kernels \(\mathfrak g\otimes u^r/u^{r+1}\), with addition as their group law, and the lifting equations are the smooth lifting equations of \(G\). The finite-jet description in (BK.10) proves the same assertion in root coordinates. Consequently the frame torsor is a smooth finite-type chart over the base.

A frame to order \(M\) lifts to a formal frame on any affine test. Here are the details needed for arbitrary coefficient rings. Suppose a frame is chosen to order \(n\). Smoothness supplies local lifts to order \(n+1\). Differences between two lifts are sections of the pulled-back Lie algebra tensored with \(u^n/u^{n+1}\), since multiplication in this square-zero kernel is addition. They form an additive Čech cocycle. This coefficient sheaf is quasi-coherent on the affine test; the affine Čech exactness used in §3.27 solves the cocycle. Adjusting the local lifts by that solution glues them to a global lift. Induction gives compatible frames to every order. Their limit is a formal frame: the torsor is affine of finite presentation, so an algebra map from its coordinate algebra to the inverse limit is exactly a compatible family of algebra maps to these quotients. Every defining equation holds at each order and hence in the complete ring. In a matrix frame its determinant is invertible because the constant determinant is invertible.

Two such lifts of a prescribed order-\(M\) frame differ by \(K_M\). This group acts trivially on \(O_\lambda\), as just proved. Effective gluing of the bundle on the complement with the modified formal bundle is proved, with arrows and arbitrary base change, in The moduli stack of bundles, §§7.1–7.4. Applying that construction in a formal frame identifies the global modifications of relative position \(\lambda\) with the associated orbit bundle. Pulling it to the frame torsor gives

\[
 \mathcal H^{\lambda}\times_{Q\times X}\mathrm{Fr}_M
 \simeq \mathrm{Fr}_M\times O_\lambda.
 \tag{BK.11}
\]

The inverse sends an orbit point to its glued modification. Changing the lifted formal frame does not change its class; changing the finite frame acts by \(G_M\). These statements hold on every affine test and for arrows, so they give the asserted isomorphism and its descent. This argument concerns the open relative-position stratum. It requires no claim that a chosen congruence group acts trivially on every boundary stratum of the Schubert closure.

The bounded global intersection-complex kernel restricts on this stratum to the relative constant connection, with its conventional shift. Indeed it is defined by middle extension from this smooth stratum, and exact restriction recovers the defining connection by (BK.1). Take a smooth affine chart \(S\) of \(\mathrm{Fr}_M\). After normalized smooth pullback, the source object for an input \(F\) therefore restricts on \(S\times O_\lambda\) to

\[
 F_S\boxtimes\mathcal O_{O_\lambda},\qquad
 \operatorname{SS}_{\infty}
   (F_S\boxtimes\mathcal O_{O_\lambda})
 =\operatorname{SS}_{\infty}(F_S)\times\{0\}.
 \tag{BK.12}
\]

Here \(F_S\) is the pullback of \(F\) from the bundle chart, together with the constant curve and frame directions. Formula (NS.7) supplies its smooth-transfer support formula, and (BK.9) supplies (BK.12). The statements are unaffected by normalization shifts. Ambient finite presentations add exactly the normal annihilators in (BK.5).

**Source-covector proposition.** Suppose \((P_1,\xi_1)\) is a geometric point of \(\operatorname{SS}_\infty(F)\). At a bounded cocharacter modification, let \(\xi_2\), \(\eta\) and \(\xi_x\) be the compatible bundle, local and moving-point covectors constructed in §§3.27–3.29. Then the pullback of \((\xi_2,\xi_x)\) to the bounded Hecke source belongs to the characteristic support of its actual kernel-weighted input, on each of the finite smooth presentations above.

**Proof.** Formula (HG.15), with the coordinate-horizontal local covector \(\theta\) used there, is

\[
 p_2^*\xi_2+s^*\xi_x
 =p_1^*\xi_1+r^*\theta.
 \tag{BK.13}
\]

On the product (BK.11), the local modification coordinate is the orbit point. The parameter coordinates consist of the input frame and the moving curve coordinate; the chosen \(\theta\) has zero coordinate-horizontal component. Its pairing with every orbit tangent is zero by \(\eta\in\operatorname{Ann}(L_1+L_2)\). Hence \(r^*\theta=0\) on this smooth open stratum. Frame changes give arc-gauge directions, which are annihilated by the same condition. Thus the left side of (BK.13) becomes the pullback input covector with zero orbit component. Smooth transfer puts its input part in \(\operatorname{SS}_\infty(F_S)\), and (BK.12) puts the resulting pair in the actual source support. In any ambient finite presentation, (BK.5) and (BK.9) retain the normal covectors, giving the same intrinsic conclusion. ∎

For the nonnilpotent value treated in §§3.23–3.29, the curve component is the nonzero value \(B(C,d\lambda)dx\); the two bounded compatible-Higgs fibres are isolated by (AS.6) and (HG.9). These are source-support and geometric-fibre statements. Covector survival under proper direct image additionally requires a lower-bound theorem in an applicable sheaf category. The lower-bound theorem in the free reading below is stated for regular holonomic sheaves; its stronger support-only extension to arbitrary D-modules is conjectural. The ordinary Hecke-lisse extension to arbitrary D-modules uses the field-extension argument of §17.8 of that reading. The full spectral action, its projector and the resulting nilpotent-regularity identification remain among the proof obligations in §9.

![The constant orbit module contains every normal covector; nilpotent stage tangents and the SL3 trace pairing remain visible.](figures/bounded-hecke-kernel-conormal.svg)

**Figure 3.9.** The first panel is the exact symbol module (BK.4), drawn as a schematic normal fibre. The second compares the classical cotangents of a reduced point and its square-zero thickening. The third shows the six root jets and the transverse diagonal direction computed below, with trace pairing \(6q(0)\). The final panel displays the finite-frame product and the source membership (BK.11)–(BK.13). Free further reading: [Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky, §§16.5, 20.4–20.9](https://arxiv.org/abs/2010.01906v2).

**Exercise 3.Y.** In \(\mathbb A^2_{z,w}\), let \(i\) be the smooth axis \(w=0\). Compute the differential-operator module \(i_+\mathcal O_{\mathbb A^1}\), its characteristic scheme, and the action of \(w\) on normal derivatives. Decide whether \(dz\), \(dw\) and \(dz+dw\) occur at the origin.

**Solution 3.Y.** The cyclic module is \(\mathcal D/(\mathcal Dw+\mathcal D\partial_z)\). Its normal basis is \(k[z,\partial_w]e\), with \(w\partial_w^re=-r\partial_w^{r-1}e\). The normal-degree filtration has associated graded \(k[z,\xi_w]\), annihilated by \(w\) and \(\xi_z\). The characteristic scheme is therefore \(w=0,\xi_z=0\) in \(T^*\mathbb A^2\). At the origin every multiple of \(dw\) occurs, including \(dw\) itself; \(dz\) and \(dz+dw\) do not, because their \(\xi_z\) coordinate is nonzero. The unrestricted normal variable is essential to (BK.7).

**Exercise 3.Z.** Compare \(Y=\operatorname{Spec}k[s]/(s^2)\) and \(Y_0=\operatorname{Spec}k\), both supported at the origin of \(\mathbb A^1_s\). Compute their classical cotangent spaces at that point and the intrinsic characteristic fibre of the point module. Explain how the answer agrees with nil-invariance of the supported D-module category.

**Solution 3.Z.** The cotangent presentation for \(Y\) is generated by \(ds\) with relation \(d(s^2)=2s\,ds\). At the residue point this relation is zero, so \(T_0^*Y=k\,ds\). For \(Y_0\) the relation is \(ds=0\), and its cotangent is zero. In the smooth ambient line the point module is \(\delta_0=\mathcal D/(\mathcal Ds)\). Its basis is \(k[\partial_s]e\), and its graded module is \(k[\xi_s]\) at \(s=0\). Thus its ambient characteristic fibre is the entire vertical line. Restriction to \(T_0^*Y\) is the identity on this line, whereas restriction to \(T_0^*Y_0\) has zero target. The categories of ambient modules supported on \(Y\) and on \(Y_0\) agree, since support is the same closed subset, as proved in the singular-spaces lesson. The spaces in which their intrinsic characteristic supports are recorded have different classical cotangents. Category nil-invariance does not erase a tangent test in a chosen nonreduced Grassmannian stage.

**Exercise 3.AA.** Take \(G=SL_3\), \(g=u^\lambda=\operatorname{diag}(u,u,u^{-2})\), \(H=\operatorname{diag}(1,1,-2)\), \(C=H+E_{12}\), and \(\eta=Cq(u)du\) with \(q(0)\ne0\). Check that \(\eta\) annihilates the six arc-orbit root jets. Then evaluate it on the full-Grassmannian dual-number deformation \(g(1+\varepsilon H/u)\), and locate that covector in the kernel fibre.

**Solution 3.AA.** The two positive root blocks are \(E_{13}\) and \(E_{23}\), each with pairing \(3\) with \(\lambda\). In the right-translated Grassmannian tangent the orbit is spanned by \(u^{-r}E_{13},u^{-r}E_{23}\), \(r=1,2,3\). Matrix multiplication gives \(\operatorname{tr}(CE_{13})=\operatorname{tr}(CE_{23})=0\), so every one of these residue pairings vanishes. Both \(\eta\) and its \(g\)-conjugate are regular, since \(C\) commutes with \(g\). This also verifies \(\eta\in\operatorname{Ann}(L_1+L_2)\) directly.

Over \(k[\varepsilon]/(\varepsilon^2)\), the matrix \(1+\varepsilon H/u\) has determinant \(1+\varepsilon\operatorname{tr}(H)/u=1\), and inverse \(1-\varepsilon H/u\). It is an actual loop in \(SL_3\). Its right-translated tangent is \(H/u\), which is nonzero modulo \(\mathfrak{sl}_3[[u]]\) and is outside the displayed six-dimensional orbit tangent. The residue is

\[
 \operatorname{Res}\operatorname{tr}
   \bigl(Cq(u)\,H/u\bigr)du=6q(0)\ne0.
 \tag{BK.14}
\]

The finite-stage union represents every coefficient test, so some \(Y_N\) contains this deformation. The restricted \(\eta_N\) is a nonzero conormal covector, and (BK.5) places it in the actual characteristic fibre of \(K_\lambda\) in that stage. It is excluded as a tangent to the reduced Schubert bound near \(g\), where the open orbit is the whole local bound. This agrees with the different cotangent quotients, and with the nonzero moving-point term in Exercise 3.V.

### 3.33. Quadratic tests at smooth cotangent points

We isolate the geometric mechanism used by the proper-direct-image lower bound. Work first over an algebraically closed field of characteristic zero. Let \(V\) have dimension \(n\), and let \(W\subset V\oplus V^*\) have dimension at most \(n\). There exists a symmetric linear map \(Q:V\to V^*\) whose graph has zero intersection with \(W\).

Here is a construction, including tangent planes that are not Lagrangian. Enlarge \(W\), if necessary, to dimension \(n\). Write \(U\) for its projection to \(V\) and \(K=W\cap V^*\). Put \(r=\dim U\). Then \(\dim K=n-r\), and \(W\) determines a well-defined linear map

\[
 A:U\longrightarrow V^*/K,
 \qquad W=\{(u,\alpha):u\in U,
                  \ \alpha\bmod K=A(u)\}.
 \tag{IS.1}
\]

Let \(L=\operatorname{Ann}(K)\subset V\), so \(\dim L=r\) and \(V^*/K=L^*\). Choose a symmetric bilinear form \(B\) on \(V\) whose pairing \(U\times L\) is perfect. To do this, put \(D=U\cap L\), choose complements \(U_0,L_0\), and extend \(D\oplus U_0\oplus L_0\) to a direct-sum decomposition of \(V\). Pair a basis of \(D\) with itself by the identity matrix; pair bases of \(U_0\) and \(L_0\) with each other by the identity matrix, in both symmetric positions. Set all other pairings involving these three subspaces to zero. The resulting \(U\times L\) matrix is the identity in the chosen bases. The unused complement may be assigned any symmetric form.

Consequently \(B_U:U\to L^*\) is invertible, and

\[
 \det(tB_U-A)\ne0
 \quad\text{for all but finitely many }t\in k.
 \tag{IS.2}
\]

Indeed its leading coefficient is \(\det B_U\ne0\). Choose such a scalar and take \(Q=tB\). A vector in its graph and in \(W\) would give \((tB_U-A)u=0\), hence \(u=0\), then \(Qu=0\). This proves the assertion. If \(r=0\), \(W=V^*\) and every graph already has zero intersection; the determinant of the empty matrix is one.

Now let \(Y\) be smooth of dimension \(n\), and let \(C\subset T^*Y\) be a closed reduced subset. Suppose \(p=(y,\xi)\in C\), \(\xi\ne0\), is a smooth point of \(C\) and \(\dim_p C\le n\). Choose étale coordinates \(z\) centred at \(y\) and use their differential frame for cotangent coordinates \(\alpha\). The tangent plane of \(C\) is a subspace of \(V\oplus V^*\). Apply the preceding construction and set

\[
 g(z)=\langle\xi,z\rangle+\tfrac12 B_Q(z,z),
 \qquad g(y)=0,\quad dg_y=\xi.
 \tag{IS.3}
\]

Here \(B_Q(v,w)=Q(v)(w)\). Symmetry is what makes the derivative of the quadratic term equal \(Qz\). Define \(h:C\to V^*\) by \(h(z,\alpha)=\alpha-dg_z\). At \(p\), its tangent kernel is \(T_pC\cap\operatorname{graph}(Q)=0\). Thus the Zariski tangent of the zero fibre at \(p\) is zero. The finite-type local algebra argument of §3.26 applies: its maximal ideal has zero quotient by its square, and the finite-generator Nakayama calculation gives zero maximal ideal. The point is open and reduced in that fibre. Removing the closed complement of this isolated point gives a neighbourhood where the fibre is just \(p\), since the fibre is Noetherian and has finitely many components. Therefore

\[
 \operatorname{graph}(dg)\cap C=\{p\}
 \quad\text{on a neighbourhood of }p.
 \tag{IS.4}
\]

Shrink the base neighbourhood too: the graph of \(dg\) near \(y\) stays in the chosen cotangent neighbourhood by continuity, and \(dg\) remains nonzero because one of its coordinate coefficients is invertible at \(y\). This gives an isolated characteristic test at a smooth cotangent point. It proves the smooth-point case needed at a generic cotangent point; it makes no assertion about a singular point of \(C\).

We also record precisely how isolation transfers through a codifferential. Let \(f:Y_1\to Y_2\), with \(Y_2\) smooth, and write

\[
 D_C=(df^*)^{-1}(C)
 \subset T^*Y_2\times_{Y_2}Y_1,
 \qquad q:D_C\longrightarrow T^*Y_2.
 \tag{IS.5}
\]

Use smooth ambient presentations for a singular \(Y_1\), as in §3.30. Suppose an irreducible component \(D\) contains \((\xi_2,y_1)\); its image closure is \(C_2\). Assume \(q|_D\) is quasi-finite there and no other component of \(D_C\) passes through that point. If \(g\) isolates \((y_2,\xi_2)\) in \(C_2\), then \(g\circ f\) isolates \(y_1\) with respect to \(C\).

**Proof.** Remove the other finitely many components near \((\xi_2,y_1)\). A characteristic point for \(g\circ f\) determines a point of \(D\) with target cotangent \(dg\). The image lies in \(C_2\), so isolation on \(Y_2\) forces that target cotangent to be \((y_2,\xi_2)\). Quasi-finiteness says its fibre is finite near our point. Remove the other points of this fibre. The only remaining characteristic point is \(y_1\). ∎

This proof needs neither finite degree of \(f\) nor injectivity of \(df\). It uses exactly the finite cotangent fibre and the exclusion of other components.

### 3.34. Why the isolated cycle is a functorial summand

For a complex variety and a function \(g\), write \(\phi_g\) for the unshifted vanishing-cycle cone and \(\Phi_g=\phi_g[-1]\) for its perverse normalization. The elementary cone and monodromy definitions are given in Nearby and vanishing cycles, §4. We distinguish the formal splitting below from the general microlocal detection and perverse-exactness inputs.

Let \(E\) be a bounded constructible complex on a space \(Z\), and suppose its closed support lies in \(\{y\}\cup T\), where \(T\) is closed and disjoint from \(y\). With \(i_y:\{y\}\hookrightarrow Z\), there is a canonical splitting

\[
 E\simeq i_{y,*}V\oplus E_{\mathrm{away}},
 \qquad V=i_y^*E\simeq i_y^!E,
 \qquad y\notin\operatorname{supp}(E_{\mathrm{away}}).
 \tag{IS.6}
\]

Here is the full support argument. The inclusions of \(\{y\}\) and \(T\) in their disjoint union are both open and closed. Sheaves on this union are pairs of sheaves, with section and restriction maps taken componentwise. This is an exact product decomposition before passing to the derived category. Closed direct image identifies sheaves supported on this union with these sheaves: a section is determined by its restriction to the closed support, and extension gives zero stalk off the support. The same assertion for complexes follows by stalk detection and the closed-support adjunction. Thus it preserves all mapping complexes and gives (IS.6). A morphism to or from a complex supported away from \(y\) is zero on its point component, in every derived degree; this also follows from the zero inverse-image and exceptional-inverse-image restrictions. Consequently the projector onto \(i_{y,*}V\) is unique and natural. Enlarging \(T\) does not change it.

Apply this to a cycle complex whose support has \(y\) as an isolated point. It gives an actual projector, not merely a decomposition of cohomology vector spaces. If an exact functor sends the cycle to another category, it carries the inclusion and projection to maps whose composite is still the identity. The isolated complex cannot disappear by cancellation with another summand.

The extension to unbounded objects requires a precise completion assertion. The following abstract lemma states that assertion as a hypothesis, rather than replacing it with a derived-heart claim.

**Completion lemma.** Let \(\mathcal A_0\) be a small stable category of bounded objects with a t-structure. Let \(T_0:\mathcal A_0\to\mathcal B_0\) be exact and suppose there is a natural finite splitting \(T_0=P_0\oplus R_0\). Assume these functors are t-exact. Form their colimit-preserving extensions to ind-categories. Assume the actual categories \(\mathcal A,\mathcal B\) under consideration are the left completions of those ind-categories, and the functors on them are the extensions specified by truncation limits. Then

\[
 T(F)=\lim_n T(\tau^{\ge -n}F)
 \simeq
 \left(\lim_nP(\tau^{\ge -n}F)\right)
 \oplus
 \left(\lim_nR(\tau^{\ge -n}F)\right).
 \tag{IS.7}
\]

**Proof.** The ind-extension is computed by colimits of diagrams in \(\mathcal A_0\). A finite direct sum commutes with every colimit, so the natural inclusions, projections and their identity relations extend, giving the splitting on the ind-category. On each truncation they remain compatible with the transition maps. Limits commute with finite products, and in a stable category a finite product is the same as a finite direct sum. Taking the limit gives (IS.7) with the same identities. This proves a functorial splitting, not just an isomorphism for each object. T-exactness and the stated completion description identify these formulas with the actual functors; they are indispensable hypotheses of this assertion. ∎

For closed point support in classical sheaf complexes, \(i_{y,*}\) commutes with these limits: on an open set its sections are the coefficient complex if the open contains \(y\), and zero otherwise. Thus a limit of the point summands remains \(i_{y,*}V\). The lemma imposes no cohomological boundedness on \(F\).

Suppose additionally that \(P\) is t-exact and detects the characteristic test on a coherent heart subobject \(A\subset H^mF\). Then

\[
 P(A)\ne0\quad\Longrightarrow\quad
 0\ne P(A)\hookrightarrow P(H^mF)=H^m(P(F))
 \quad\Longrightarrow\quad P(F)\ne0.
 \tag{IS.8}
\]

The middle injection follows because a t-exact stable functor is exact on its heart: applying it to the triangle of a short exact sequence and taking cohomology gives a short exact sequence. This proves the full-unbounded detection deduction once the coherent test detection, t-exactness and completion premises have been established. It does not establish those geometric premises by itself.

### 3.35. Proper image of the isolated summand

Consider a proper map \(f:Y_1\to Y_2\), a function \(g\) on \(Y_2\), and the induced map \(f_0\) of zero fibres. Proper base change, when valid for the chosen sheaf theory and coefficient scope, gives the actual comparison

\[
 \Phi_g\,Rf_*F\simeq
 Rf_{0,*}\,\Phi_{g\circ f}F.
 \tag{IS.9}
\]

We spell out this deduction. Let \(U_i\) be the complements of the zero fibres, \(j_i\) their inclusions, and \(\pi_i:\widetilde U_i\to U_i\) the pullbacks of the universal cover of the punctured parameter disc. Nearby cycles are \(i_i^*Rj_{i,*}R\pi_{i,*}\pi_i^*j_i^*F\). Open restriction commutes with direct image by restricting sections. Proper base change for the square over the covering space identifies \(\pi_2^*Rf_{U,*}\) with \(R\widetilde f_*\pi_1^*\). Composition of the three direct-image right adjoints gives

\[
 Rj_{2,*}R\pi_{2,*}R\widetilde f_*
 =Rf_*Rj_{1,*}R\pi_{1,*}.
 \tag{IS.10}
\]

Proper base change at the zero fibre then gives the nearby-cycle comparison. These are maps induced by restriction and adjunction, and take the specialization map to the specialization map: both are induced by pulling a section to the same covering space. Taking its cone and then the shift \([-1]\) proves (IS.9). This verifies the normalization and the particular comparison, subject to the two proper-base-change assertions just named. It does not assert an arithmetic or unbounded base-change theorem without its own proof.

Suppose \(\Phi_{g\circ f}F\) has the natural splitting \(i_{y_1,*}V\oplus R(F)\), with \(V\ne0\). Pushing it forward in (IS.9) gives

\[
 \Phi_gRf_*F\simeq
 i_{y_2,*}V\oplus Rf_{0,*}R(F),
 \qquad y_2=f(y_1).
 \tag{IS.11}
\]

Direct image of the point summand has exactly coefficient complex \(V\): its sections over an open set containing \(y_2\) are \(V\), and otherwise zero. In particular, the stalk of the left side at \(y_2\) contains \(V\) as a retract and is nonzero. Other cycle summands may map to \(y_2\), but their contributions cannot change the identity on \(V\).

This proves a formal lower-bound principle with explicit inputs. To conclude that \((y_2,dg_{y_2})\) lies in the support of \(Rf_*F\), the chosen support theory must detect this nonzero isolated test. To obtain \(V\ne0\) from a source support component, it must detect the source isolated characteristic test. For unbounded \(F\), (IS.7)–(IS.8) also require the actual completion and t-exactness statements. Those are mathematical premises, not consequences of properness or of the isolated compatible-Higgs fibre alone.

The usual generic-point proof uses a component \(D\) in (IS.5) of the target's dimension and its image closure \(C_2\). At a generic point of \(C_2\), a finite nonempty cotangent fibre and exclusion of other components give the source isolation. Formula (IS.3) supplies the target test at the smooth generic point. Formula (IS.11) then supplies the lower bound once the detection and base-change inputs apply. Field-extension compatibility and characteristic-component dimension assertions are additional inputs to that generic-point reduction; they are not proved by the symmetric-form calculation.

For the bounded Hecke correspondence, §§3.26–3.32 already establish the actual source membership and the isolated compatible-Higgs fibre in both directions. They supply the geometric starting data. The full regular-holonomic lower bound still requires the isolated-cycle detection, actual full-category cycle t-exactness/completion and the generic-point field-extension comparison in the applicable characteristic-support theory. The source's stronger support-only assertion for all D-modules remains conjectural. Its ordinary Hecke-lisse equality for all D-modules follows instead through the separate spectral field-extension argument. The spectral projector and nilpotent regularity therefore remain unproved here.

Free further reading for this mechanism is [Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky, Appendix H, especially H.1–H.4](https://arxiv.org/abs/2010.01906v2). The isolated controlled-Morse theorem is in [Massey, A Little Microlocal Morse Theory, Theorem 1.1](https://arxiv.org/abs/math/0006185v2). These are reading sources, not proofs of the remaining premises. The programme's isolated holomorphic test, exact geometric imports and Nearby and vanishing cycles, §5 retain the controlled-Morse and general t-exactness prerequisites explicitly.

![A quadratic graph isolates a cotangent point; a point-cycle retract survives proper image, while a positive-dimensional fibre can cancel its cohomology.](figures/isolated-cycle-summand.svg)

**Figure 3.10.** The first panel records the exact symmetric-form construction (IS.1)–(IS.4). The second shows the actual inclusion and projection whose composite is the identity in (IS.11); the sheaf comparisons needed for its application are indicated. The last two panels are the complete finite-ramification and positive-dimensional-fibre computations below. All arrows are categorical maps or indicated differentials, not numerical approximations. Free human-source reading is the preceding Appendix A and Massey theorem.

**Exercise 3.AB.** Let \(V=k^2\) with bases \(e_1,e_2\) and \(e_1^*,e_2^*\). For \(W=\operatorname{span}\{(e_1,0),(0,e_1^*)\}\), find a symmetric \(Q\) whose graph is transverse to \(W\). Then do the same for \(W'=\operatorname{graph}(A)\), \(A=\begin{pmatrix}0&1\\0&0\end{pmatrix}\). Explain why an arbitrary linear graph need not be the derivative of a quadratic function.

**Solution 3.AB.** For \(W\), take \(Q=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). If \((v,Qv)\in W\), its first component forces \(v=ae_1\). The second is then \(ae_2^*\), and belonging to \(ke_1^*\) forces \(a=0\). For \(W'\), take \(Q=2I\); \(\det(Q-A)=4\ne0\) gives zero intersection. The first form is the Hessian of \(z_1z_2\), and the second of \(z_1^2+z_2^2\). In characteristic zero mixed partial derivatives agree, so a quadratic Hessian is symmetric. The nonsymmetric \(A\) is not such a Hessian. This exercise concerns abstract tangent planes; no claim that \(W\) is a characteristic component is made.

**Exercise 3.AC.** For the finite map \(f:\mathbb C_z\to\mathbb C_t\), \(t=z^m\), \(m\ge2\), compute the normalized vanishing cycle at zero of \(Rf_*\mathbb C[1]\) for \(g=t\). Prove directly that every nonzero target cotangent at zero is detected, and compute the scheme length of the relevant cotangent fibre.

**Solution 3.AC.** The polynomial is monic, so \(\mathbb C[z]\) is a free \(\mathbb C[t]\)-module with basis \(1,z,\ldots,z^{m-1}\): division by \(z^m-t\) gives spanning and uniqueness. The map is finite and proper. Topologically properness is immediate from \(|z|^m=|t|\): inverse images of compact sets are closed and bounded. A small nonzero fibre has \(m\) points, and a small total disc is contractible. The specialization map of the constant source is therefore the diagonal map

\[
 \mathbb C\longrightarrow\mathbb C^m,
 \qquad v\longmapsto(v,\ldots,v),\qquad
 \Phi_t(Rf_*\mathbb C[1])_0
 =\mathbb C^m/\mathbb C(1,\ldots,1).
 \tag{IS.12}
\]

The quotient is in degree zero: taking the unshifted cone of the injective diagonal on complexes in degree minus one and then \([-1]\) gives precisely that degree. Its dimension is \(m-1\). Parameter monodromy cyclically permutes the \(m\) sheets. The quotient is isomorphic to the sum-zero subspace by subtracting the average; this is valid over every characteristic-zero coefficient field.

Here is also a direct supported-test computation, without the general isolated-Morse theorem. For any \(\eta\ne0\), use the half-plane test \(\operatorname{Re}(\eta t)\ge0\) near zero. Its open complement pulls back to \(m\) disjoint contractible sectors in the source disc. The relative section complex is the fibre of the diagonal \(\mathbb C\to\mathbb C^m\), shifted by \([1]\). Thus it is the same nonzero quotient in degree zero. Rotating \(\eta\) changes the sectors' angles but not their number or the maps. Each nonzero covector is therefore in the target's classical support-test microsupport; no rank-only heuristic is needed.

The constant input has zero-section characteristic support. Its codifferential lift satisfies \(mz^{m-1}\eta=0\). Fix \(\eta\ne0\). The fibre at zero has local ring

\[
 \mathbb C[z]_{(z)}/(z^{m-1}),
 \qquad\text{length }m-1.
 \tag{IS.13}
\]

Its reduced support is a single isolated point, so the cotangent projection is quasi-finite despite this multiplicity. The target image component is the nonzero vertical cotangent over zero. The length agrees with the vanishing-cycle dimension. For \(m=2\) the source point is reduced; for larger \(m\) the nilpotent multiplicity must be retained.

**Exercise 3.AD.** Let \(E=\mathbb C/(\mathbb Z+i\mathbb Z)\) be the compact complex torus. Choose a rank-one complex local system \(L\) with monodromy \(2\) around the first generator and \(1\) around the second. For the proper projection \(f:E\times\Delta\to\Delta\), let \(F=i_*L[1]\), supported on \(E\times\{0\}\). Compute \(Rf_*F\) and explain exactly which isolation hypothesis fails, even though the source contains the pulled-back nonzero target covector.

**Solution 3.AD.** The square presentation of the torus has one vertex, two oriented edges and one two-cell. A cellular filtration computes local-system cohomology: relative cohomology of one attached interval with its endpoints is one copy in degree one, and that of the square with its boundary is one copy in degree two, by cutting the boundary circle into two intervals and applying the section Mayer–Vietoris triangle. Transport around the two edge identifications supplies the differences of their monodromies from the identity. Thus, with the corresponding choices of cell orientations, the full cochain complex is

\[
 \mathbb C\xrightarrow{d^0}\mathbb C^2
 \xrightarrow{d^1}\mathbb C,
 \qquad d^0(v)=(v,0),\quad d^1(a,b)=b.
 \tag{IS.14}
\]

The finite cellular filtration has these relative complexes in their respective degrees; its differential is exactly the edge transport just calculated. It therefore gives the actual total section complex. Set \(h^1(a,b)=a\) and \(h^2(v)=(0,v)\). Direct substitution gives \(dh+hd=1\) in degrees zero, one and two. Consequently \(R\Gamma(E,L)=0\), and sections of \(Rf_*i_*L[1]\) over an open containing zero are this zero complex. The output is zero.

Locally \(L\) is a constant connection along \(E\). The supported half-plane test normal to \(E\times\{0\}\) is nonzero at every point: on its support the normal function is zero, so the supported-test functor is the identity. Equivalently the normal Weyl calculation (BK.4) gives the full conormal fibre, with arbitrary \(dt\) coefficient. For a fixed nonzero target covector, the cotangent fibre is the entire \(E\), of complex dimension one. It is not quasi-finite; its cotangent correspondence component has dimension two, whereas the target has dimension one. This is a proper holomorphic example, so no algebraization or elliptic-curve uniformization theorem is being used. It shows why nonzero local source tests do not alone force nonzero proper pushforward. The isolated-point projector in (IS.11) is the mechanism that excludes this cancellation.

### 3.36. Residue fields detect unbounded complexes

Field extension is essential when point tests are used without a fixed characteristic-support bound. The finite detectors of §3.18 apply to its specified supported category. We now prove a different statement that tests arbitrary complexes, using every prime and allowing the ground field to grow.

**Theorem 3.36.** Let \(R\) be a commutative Noetherian ring of finite Krull dimension. Write \(D(R)\) for its unbounded derived category and \(\kappa(\mathfrak p)=\operatorname{Frac}(R/\mathfrak p)\) for the residue field at a prime. For every \(F\in D(R)\),
\[
 \bigl(\kappa(\mathfrak p)\otimes_R^{\mathbf L}F=0
       \text{ for every }\mathfrak p\in\operatorname{Spec}R\bigr)
       \quad\Longrightarrow\quad F=0.
                                                        \tag{FE.1}
\]
Neither boundedness nor finite generation of the cohomology of \(F\) is required. An ordinary residue fibre of a cohomology module cannot replace the derived fibre in this statement. For example, over \(k[t]\), put \(Q=k(t)/k[t]\). Its generic ordinary fibre is zero, because localization makes \(k[t]\to k(t)\) an isomorphism. Multiplication by every nonzero polynomial on \(Q\) is surjective: divide a representative fraction by that polynomial. Hence its ordinary fibre at each closed prime is also zero. But multiplication by \(t-b\) kills the nonzero class of \(1/(t-b)\), so the two-term residue resolution has nonzero degree-minus-one cohomology. The derived fibre detects \(Q\).

We first explain the finiteness hypotheses for affine schemes of finite type over a field. If \(A\) is Noetherian, so is \(A[T]\): for an ideal \(J\), the possible coefficients of \(T^n\) in its polynomials of degree at most \(n\) form ideals \(I_n\subset A\). Multiplication by \(T\) makes these an increasing sequence. It stabilizes, and each of its finitely many initial ideals has finitely many generators. Choose polynomials in \(J\) realizing these generators. Subtracting multiples of those polynomials cancels the highest coefficient of any polynomial in \(J\); induction on degree shows that the chosen finite list generates \(J\). Iteration and passage to a quotient prove the assertion for every finitely generated algebra over a field.

Its Krull dimension is also finite. For a finitely generated domain \(A\) and a nonzero prime \(\mathfrak q\), choose algebraically independent elements \(\bar b_1,\ldots,\bar b_r\) among generators of \(A/\mathfrak q\), maximal with this property. Its fraction field is algebraic over \(k(\bar b_1,\ldots,\bar b_r)\). Lift the \(\bar b_i\) to \(A\) and choose \(0\ne a\in\mathfrak q\). A polynomial relation between \(a,b_1,\ldots,b_r\), after division by its smallest power of \(a\), would reduce modulo \(\mathfrak q\) to a nonzero polynomial relation between the \(\bar b_i\). Thus these \(r+1\) elements are independent, and
\[
 \operatorname{trdeg}_k\operatorname{Frac}(A/\mathfrak q)
       <\operatorname{trdeg}_k\operatorname{Frac}(A).
                                                        \tag{FE.2}
\]
Every strict step in a prime chain decreases this nonnegative integer. The integer is at most the number of algebra generators. This bounds every prime chain, including chains in quotients by an initial prime. In particular the affine coordinate rings used below satisfy the hypotheses of Theorem 3.36.

**Prime filtrations.** Every finitely generated module over a Noetherian ring has a finite filtration with prime cyclic quotients. Here is the proof needed for this argument. Finite free modules are Noetherian: induct on their rank, using the intersection of a submodule with the last summand and its projection to the other summands. Quotients preserve this property. In a nonzero finite module, choose an element whose annihilator \(I\) is maximal among annihilators of nonzero elements. If \(ab\in I\) and \(b\notin I\), maximality gives \(\operatorname{Ann}(bx)=I\), so \(a\in I\). Therefore \(I\) is prime. Insert \(Rx\), and repeat in the quotient. Infinitely many repetitions would produce a strictly increasing chain of submodules of the original Noetherian module. Consequently the process terminates:
\[
 0=M_0\subset M_1\subset\cdots\subset M_s=M,
 \qquad M_j/M_{j-1}\simeq R/\mathfrak p_j.
                                                        \tag{FE.3}
\]
The freely readable [*Support and dimension of modules*](https://stacks.math.columbia.edu/tag/00KY), Lemma 10.62.1, gives another prime-filtration proof.

**Proof of Theorem 3.36.** Let \(\mathcal L\) be the smallest full stable subcategory of \(D(R)\) closed under colimits and containing all the \(\kappa(\mathfrak p)\). We show that it contains each \(R/\mathfrak p\), by induction on \(\dim(R/\mathfrak p)\). Set \(A=R/\mathfrak p\) and \(K=\operatorname{Frac}A\). If \(A\) has dimension zero, every nonzero element is a unit: a proper ideal generated by such an element would lie in a nonzero maximal prime. Hence \(A=K\in\mathcal L\).

For positive dimension, every finite submodule of \(K/A\) is annihilated by a nonzero element of \(A\). Indeed, represent its finitely many generators by fractions and take the product of their denominators. Apply (FE.3) to this finite submodule as an \(A\)-module. Each prime in its filtration contains the nonzero common denominator; each quotient is therefore \(A/\mathfrak q\) with \(\mathfrak q\ne0\). Prefixing a prime chain by \(0\subsetneq\mathfrak q\) shows that its dimension is smaller than \(\dim A\). The induction hypothesis, interpreted as a statement about \(R\)-modules, puts every such quotient in \(\mathcal L\). Finite extensions then put the submodule in \(\mathcal L\).

All finite submodules form a filtered system, since the sum of two is again finite. Thus
\[
 K/A=\mathop{\operatorname{colim}}_{M\subset K/A,\ M\text{ finite}}M,
 \qquad A\longrightarrow K\longrightarrow K/A
       \quad\text{is a triangle in }D(R).
                                                        \tag{FE.4}
\]
The colimit here is also the derived colimit. Filtered colimits of modules are exact: a finite relation or the vanishing of a represented element holds at some common later index. Applied degree by degree, this also shows that cohomology commutes with such colimits of complexes. Equivalently, in the simplicial complex computing a derived colimit, a finite cycle lies in a diagram with a common upper index; inserting that index contracts its positive simplicial degrees. This identifies the derived colimit of the displayed degree-zero diagram with its ordinary union. We have proved \(K/A\in\mathcal L\); since \(K=\kappa(\mathfrak p)\in\mathcal L\), its triangle proves \(A\in\mathcal L\). Finally use (FE.3) for \(R\) itself to obtain
\[
 R/\mathfrak p\in\mathcal L\text{ for every prime},
 \qquad R\in\mathcal L.
                                                        \tag{FE.5}
\]

For the given unbounded \(F\), derived tensoring with \(F\) is exact and preserves colimits. One can see these properties from its adjunction with derived Hom; on a flat resolution they are also the usual tensor identities for cones and colimits. Its kernel is therefore a stable colimit-closed subcategory. If the hypothesis of (FE.1) holds, this kernel contains the generators defining \(\mathcal L\), hence contains \(R\). But
\[
 R\otimes_R^{\mathbf L}F\simeq F,
 \qquad \mathcal L\subset
   \ker\bigl(-\otimes_R^{\mathbf L}F\bigr).
                                                        \tag{FE.6}
\]
This proves \(F=0\). Notice that the finite filtrations in this proof are filtrations of auxiliary ordinary modules, not of \(F\). No truncation limit, bounded spectral sequence or completeness assertion about a stack category occurs in this proof. □

### 3.37. A detecting prime becomes a closed rational point

Let \(R\) be a finitely generated \(k\)-algebra. If \(F\in D(R)\) is nonzero, Theorem 3.36 supplies a prime \(\mathfrak p\) with nonzero derived residue fibre. Put \(K=\kappa(\mathfrak p)\), or take any extension of this field, such as an algebraic closure. Define
\[
 R_K=R\otimes_k K,
 \qquad R_K\longrightarrow K,
 \qquad r\otimes a\longmapsto\bar r a.
                                                        \tag{FE.7}
\]
Here \(\bar r\) is the image of \(r\) in \(\kappa(\mathfrak p)\subset K\). This map is surjective because its restriction to \(1\otimes K\) is the identity. Its kernel is maximal, so it defines a **closed \(K\)-rational point** \(y\) of \(\operatorname{Spec}R_K\). The point under it in \(\operatorname{Spec}R\) may be generic rather than closed. Associativity of tensor gives
\[
 K\otimes_{R_K}^{\mathbf L}(F\otimes_k K)
 \simeq
 \bigl(\kappa(\mathfrak p)\otimes_R^{\mathbf L}F\bigr)
       \otimes_{\kappa(\mathfrak p)}K\ne0.
                                                        \tag{FE.8}
\]
For completeness, take a flat resolution of \(F\) over \(R\). Extension to \(R_K\) is still a flat resolution: field extension is exact, and its terms are flat after base change. Both sides of (FE.8) are computed by tensoring this same resolution with \(K\). Extension of vector spaces between fields is faithful and exact: a basis identifies it with a direct sum of copies of the new field. Therefore it preserves nonzero cohomology even for an unbounded complex.

We next identify the actual D-module point test. Let \(U\) be a smooth affine scheme of dimension \(d\) over a characteristic-zero field \(K\), and let \(y\) be a closed \(K\)-rational point. Shrink to an affine neighbourhood with étale coordinates \(t_1,\ldots,t_d\) vanishing at \(y\). The existence of these coordinates is the smooth local-coordinate construction used in §1.10. Their zero fibre consists of finitely many reduced points. Removing the other points makes its ideal \((t_1,\ldots,t_d)\) precisely the ideal of \(y\). They are a regular sequence: the coordinate map is flat and pulls back the successive injective multiplications in the polynomial coordinate ring. Localization preserves those injections.

Write \(D=\Gamma(U,\mathcal D_U)\). The coordinate PBW proof in [*Differential operators and the Weyl algebra*](../../GL-DMOD/src/differential-operators-and-the-weyl-algebra.md), §3, gives the right-coefficient form of its ordered basis:
\[
 D=\bigoplus_{\alpha\in\mathbb N^d}\partial^\alpha\mathcal O(U),
 \qquad [\partial_i,t_j]=\delta_{ij},
 \qquad [\partial_i,\partial_j]=0.
                                                        \tag{FE.9}
\]
Moving coefficients past derivatives changes only lower orders; thus the left-coefficient PBW basis gives this right-coefficient basis by an invertible triangular change, order by order. In particular \(D\) is flat as a right \(\mathcal O(U)\)-module. Tensor its right module with the finite Koszul resolution of \(K=\mathcal O(U)/(t_1,\ldots,t_d)\). The one-variable resolution is injective multiplication by its parameter followed by its quotient; tensoring the next such two-term resolution proves exactness inductively, using regularity on the preceding quotient. This produces a resolution
\[
 \Delta_{y,t}=D/\sum_i D t_i,
 \qquad
 0\longrightarrow D\otimes\bigwedge^d K^d
 \longrightarrow\cdots\longrightarrow D\otimes K^d
 \longrightarrow D\longrightarrow\Delta_{y,t}\longrightarrow0.
                                                        \tag{FE.10}
\]
The differentials use **right multiplication** by the \(t_i\); these maps are left \(D\)-linear. The normal closed-transfer formula in [*Kashiwara’s equivalence and singular spaces*](../../GL-DMOD/src/kashiwaras-equivalence-and-singular-spaces.md), §3, identifies this cyclic module with the point delta module after choosing the one-dimensional normal determinant factor. A different choice tensors the chosen presentation by a one-dimensional \(K\)-space, which changes no vanishing test. We use the notation \(\Delta_{y,t}\) to retain this choice explicitly.

Applying Hom into any unbounded \(D\)-module complex \(M\) computes derived Hom by this finite free resolution. A bounded complex of finite free modules sends acyclic complexes to acyclic Hom complexes: its finite filtration has shifted copies of the acyclic target as successive quotients. Thus this computation has no boundedness requirement on \(M\). It is the cochain Koszul complex with terms \(M\otimes\bigwedge^r(K^d)^*\) in degrees \(r=0,\ldots,d\), and differential given by the commuting left actions of the \(t_i\). Wedge pairing with a chosen volume form identifies it, with the usual differential signs, with the homological Koszul fibre shifted by \(-d\). Consequently
\[
 \operatorname{RHom}_D(\Delta_{y,t},M)=0
 \quad\Longleftrightarrow\quad
 K\otimes_{\mathcal O(U)}^{\mathbf L}\operatorname{oblv}M=0.
                                                        \tag{FE.11}
\]
This is the general version of the finite normal calculation behind (FD.8); it does not assume the flat-cohomology hypothesis used for (FD.9).

Operator algebras themselves commute with field extension. There is a natural filtered map \(D_{R/k}\otimes_k K\to D_{R_K/K}\). On an étale coordinate chart, both sides have (FE.9), with the same derivative basis and the extended coefficient ring; the map is an isomorphism on every associated graded order. Induction in the exact sequences for successive orders makes it an isomorphism on every filtered piece, and their union proves it for all operators. These local identities agree with restriction, so they give the identity of operator sheaves. On an affine scheme, sections of a quasi-coherent sheaf commute with field extension, as is seen from its module and localization description. The induced scalar extension of any operator-module complex has underlying complex \(M\otimes_k K\). This assertion concerns the actual module construction; it does not assert a tensor-product presentation of a spectral stack category.

Combining these observations proves the promised detector statement:

**Theorem 3.37.** For a smooth affine finite-type \(k\)-scheme \(U\), every nonzero object \(M\) of the full unbounded operator-module category is detected by a point delta module on an affine open of \(U_K\), for some field extension \(K/k\):
\[
 M\ne0\quad\Longrightarrow\quad
 \operatorname{RHom}_{D_{W/K}}
       (\Delta_{y,t},M_K|_W)\ne0,
 \qquad y\in W(K)\text{ closed},\quad W\subset U_K\text{ affine open}.
                                                        \tag{FE.12}
\]
Indeed, forgetting the operator action is conservative on module complexes, since it does not change their underlying differentials or cohomology. Apply (FE.1) and (FE.8) to that nonzero underlying complex, then shrink around the detecting rational point and use (FE.11). Localization around the point leaves its derived fibre unchanged. A general smooth finite-type scheme is handled by choosing an affine chart on which the object is nonzero. □

### 3.38. Orthogonality, chart tests and the remaining global adjunction

Theorem 3.37 gives a useful exact criterion. Suppose \(M\) is an unbounded D-module complex on a smooth finite-type scheme \(U\). If for every extension \(K/k\), every affine coordinate open \(W\subset U_K\) and every closed rational point in it one has
\[
 \operatorname{RHom}_{D_{W/K}}
       (\Delta_{y,t},M_K|_W)=0,
                                                        \tag{FE.13}
\]
then \(M=0\). If it were nonzero, a nonzero affine restriction and (FE.12) would contradict (FE.13). Thus point tests over varying fields detect the full category, including complexes with infinitely many nonzero cohomology modules.

For a smooth stack, §1.10 makes atlas pullbacks conservative. Choose a chart on which a nonzero object remains nonzero, and apply (FE.12) there. This proves conservativity of the **chart pullback followed by point test** family. It does not identify that test with a mapping complex from an intrinsic stack point. A point of an Artin stack can have a positive-dimensional automorphism group; its map to the stack need not be a closed immersion. The affine closed-transfer computation (FE.10) cannot be substituted for such a map's left adjoint.

Here is the precise formal implication needed later. Suppose a presentable stable category \(\mathcal B\) has a conservative functor \(U\) to D-modules on a smooth stack \(\mathcal Y\), compatible with the field extensions under consideration. Suppose there is an adjunction \(P_K\dashv U_K\) for each such field, and that every chart point test \(T\) used above has an actual left adjoint \(L_T\) into \(\operatorname{Dmod}(\mathcal Y_K)\). Finally suppose a full subcategory \(\mathcal A_K\subset\mathcal B_K\) contains all \(P_KL_T(K)\), and that the given \(F\in\mathcal B\), after extension, is right-orthogonal to \(\mathcal A_K\). Then
\[
 \operatorname{RHom}_{\mathcal B_K}(P_KL_T(K),F_K)
 \simeq
 \operatorname{RHom}_{\operatorname{Dmod}(\mathcal Y_K)}(L_T(K),U_KF_K)
 \simeq T(U_KF_K)=0.
                                                        \tag{FE.14}
\]
The first equality is the stated projector adjunction and the second is the stated chart-test adjunction. A mapping complex from \(K\) to a \(K\)-complex is that complex itself. The detector theorem now implies \(UF=0\); conservativity gives \(F=0\). This proves the implication under exactly its displayed hypotheses. It supplies no missing geometric left adjoint, no base-change equivalence for \(\mathcal A\), and no projector construction.

The field-extension orthogonality argument appears in [Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky, *The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support*](https://arxiv.org/abs/2010.01906v2), §20.9. The residue-field and affine point computations above give complete proofs of their chart-level ingredients. For the nilpotent regularity assertion of this lesson, the enhanced spectral action and projector, its regular image, the relevant field-extension equivalence and the actual global point or chart-test adjunction remain not yet proved. The general isolated-cycle comparison of §§3.33–3.35 remains a separate requirement. In particular this point-detector argument adds no stronger support-only conjecture to the ordinary all-D-module Hecke-lisse statement.

![A detecting generic prime becomes a closed rational point after scalar extension; finite normal Koszul complexes detect unbounded D-modules; the global stack adjunction remains explicit.](figures/field-extension-point-detectors.svg)

*Figure 3.11.* The first panel uses \(R=k[t]\), \(F=k(t)\), \(K=k(a)\) with \(a\) transcendental: the evaluation \(K[t]\to K\), \(t\mapsto a\), defines a closed rational point over the original generic point. The second panel shows the homological fibre-resolution in normal degrees \(-d,\ldots,0\) and the cochain point-Hom direction in normal degrees \(0,\ldots,d\), related by the finite Koszul duality of (FE.10)–(FE.11). These finite normal directions are tensored with the possibly unbounded target; they are not bounds on its total cohomology. The last panel distinguishes the proved chart detector from the explicit adjunction premises of (FE.14). The arrows describe actual algebraic maps or stated categorical assumptions; the panels are schematics, not geometric dimension drawings.

**Exercise 3.AE.** Let \(k\) be algebraically closed of characteristic zero, \(R=k[t]\) and \(F=k(t)\). Show that every original closed-point derived fibre vanishes. Choose \(K=k(a)\), where \(a\) is transcendental over \(k\), and compute the derived fibre at \(t=a\) of \(F_K=F\otimes_k K\). Equip \(F\) with its differentiation action and compute its point delta Hom on \(\mathbb A^1_K\).

**Solution 3.AE.** For \(b\in k\), the resolution of \(k_b\) is multiplication by \(t-b\) on \(R\) in degrees \(-1,0\). Tensoring with \(k(t)\) makes this map invertible, so its complex is acyclic. More generally any nonzero irreducible polynomial becomes invertible in \(k(t)\). The detecting prime is \((0)\), whose field \(k(t)\) has a nonzero fibre: localization gives \(k(t)\otimes_R k(t)\simeq k(t)\).

Over \(K\), write \(S=k[t]\setminus\{0\}\). Then \(F_K=S^{-1}K[t]\). Every \(s(a)\) with \(s\in S\) is nonzero, by transcendence. Hence evaluation at \(a\) survives this localization, and its kernel is \((t-a)\). Multiplication by \(t-a\) on \(S^{-1}K[t]\) is injective, with cokernel \(K\). Thus the derived fibre is \(K\) in degree zero. The point module \(D_K/D_K(t-a)\) has Hom complex \(F_K\xrightarrow{t-a}F_K\) in degrees \(0,1\), whose only cohomology is \(K\) in degree one. The differentiation action extends with \(\partial a=0\); it makes this a valid operator-module calculation but does not alter the normal multiplication map. This new closed point lies above the generic point, since no nonzero polynomial over \(k\) vanishes at \(a\).

**Exercise 3.AF.** On \(\mathbb A^1_K\), consider the rank-one connection \(M=K[t]e\) with \(\partial e=2te\). For a rational point \(b\), compute \(\operatorname{RHom}_D(D/D(t-b),M)\). Verify directly the Weyl relation for this action, and explain whether the point calculation uses the coefficient \(2t\).

**Solution 3.AF.** On \(fe\), the operator is \(\partial(fe)=(f'+2tf)e\). Its commutator with multiplication by \(t\) is the identity, since differentiating \(tf\) contributes the extra term \(f\). Thus it defines a D-module. The finite free point resolution gives multiplication by \(t-b\) on \(K[t]e\) in degrees \(0,1\). This map is injective, and its quotient is \(Ke\). Its only Hom cohomology is therefore \(Ke\) in degree one. The connection coefficient does not enter this multiplication complex. Point detection tests the underlying derived fibre and works for every connection coefficient, including the irregular-at-infinity example considered in §3.22; it is not a criterion for regularity.

**Exercise 3.AG.** Take \(M=\bigoplus_{m\in\mathbb Z}K[t][m]\), with zero complex differential and the usual coordinate derivative on each summand. Compute the point Hom at \(t=b\) in every cohomological degree. Explain why the finite free resolution is legitimate even though \(M\) is bounded in neither direction.

**Solution 3.AG.** The point Hom complex is the two-term multiplication complex \(M\xrightarrow{t-b}M\), with its total grading. Its computation commutes with the indicated direct sum because only two finite free modules occur in the resolution. On each summand the kernel is zero and the cokernel is \(K[m-1]\). Consequently the Hom complex is quasi-isomorphic to \(\bigoplus_{m\in\mathbb Z}K[m-1]\), and its cohomology is one copy of \(K\) in every integer degree. The underlying derived fibre is \(\bigoplus_{m\in\mathbb Z}K[m]\). Tensor and Hom here each have a finite normal direction, so each total degree uses finitely many terms. No infinite product, convergence assertion or replacement of \(M\) by a bounded truncation is involved.

### 3.39. Scalar extension of categories, including infinite fields

The field in (FE.8) can be an infinite extension. We must therefore prove the categorical comparison without treating it as tensoring finite-dimensional vector spaces. We work with presentable stable \(k\)-linear categories and functors preserving colimits. Tensor products of such categories are characterized by functors that are \(k\)-linear and preserve colimits in each variable. All modules, mapping complexes, tensors and realizations below are derived and unbounded.

For an extension \(K/k\), let \(\operatorname{Vect}_K=\operatorname{Mod}_K\), the category of complexes of \(K\)-vector spaces. For a presentable \(k\)-linear category \(\mathcal C\), its scalar extension has an explicit description:
\[
 \mathcal C_K:=\mathcal C\otimes_{\operatorname{Vect}_k}\operatorname{Vect}_K
       \simeq\operatorname{Mod}_K(\mathcal C).
                                                        \tag{KF.1}
\]
The right side consists of objects of \(\mathcal C\) with a coherently associative unital \(K\)-action. Its free and forgetful functors are \(q(F)=K\otimes_k F\) and \(r\). Colimits of such modules are computed on the underlying objects, with the induced action; therefore \(r\) preserves colimits. Their limits are computed similarly, since tensoring by the algebra supplies the action maps to each component of the limiting cone. Mapping complexes are the limits imposing the action compatibilities, including their higher homotopies.

Here is a proof of (KF.1) and the module-category identities we will use. For any unital associative DG algebra \(A\), a module \(M\) has its augmented free bar resolution
\[
 B_n(M)=A^{\otimes_k(n+1)}\otimes_k\operatorname{oblv}M,
 \qquad |B_\bullet(M)|\simeq M.
                                                        \tag{KF.2}
\]
Adjacent factors are multiplied by the faces, the last face acts on \(M\), and degeneracies insert a unit. After forgetting the first module structure, inserting a unit at the first position gives an extra degeneracy. The alternating differential satisfies the contracting identity for the augmented simplicial direction; the contraction commutes with the internal differential with the total-complex signs. Thus its augmentation is an equivalence, for arbitrary unbounded input. Geometric realization uses a direct sum in its simplicial direction; the contracting identity concerns each finite simplicial expression and requires no boundedness. This same split augmented bar calculation works for algebra actions inside \(\mathcal C\).

A colimit-preserving \(k\)-linear functor out of \(\operatorname{Mod}_A\) is determined by its value \(P\) on the free module \(A\), with the right \(A\)-action given by its endomorphisms. On a free module \(A\otimes_k V\), it must take the value \(P\otimes_k V\). Applying the functor to (KF.2) then forces its value on every \(M\) to be \(P\otimes_A M\), computed by the two-sided bar construction. Conversely that construction gives a colimit-preserving functor with precisely the required action. The same argument identifies transformations and all higher transformations: on free terms they are maps respecting the actions, and the bar face and degeneracy maps impose exactly those compatibilities. With two module variables, it requires two commuting actions. Hence the universal bilinear property gives
\[
 \operatorname{Mod}_A\otimes_{\operatorname{Vect}_k}\operatorname{Mod}_B
       \simeq\operatorname{Mod}_{A\otimes_k B}.
                                                        \tag{KF.3}
\]
Here \(A,B\) may be arbitrary associative DG algebras; over a field their algebra tensor is already the derived tensor. Taking one variable in \(\mathcal C\) instead gives (KF.1): the free internal modules and their bar resolutions have exactly the same bilinear universal property. This proves the assertions at the level of DG categories and mapping complexes, rather than only of ordinary module hearts.

The category \(\operatorname{Mod}_A\) is dualizable as a \(k\)-linear category, with dual \(\operatorname{Mod}_{A^{\mathrm{op}}}\). Its actual duality maps are
\[
 \epsilon(P,M)=P\otimes_A M,
 \qquad
 \eta:\operatorname{Vect}_k\longrightarrow
       \operatorname{Mod}_{A\otimes_k A^{\mathrm{op}}},
 \quad V\longmapsto A\otimes_k V.
                                                        \tag{KF.4}
\]
In \(\eta\), the algebra \(A\) has its regular bimodule structure. Both functors preserve colimits, as follows directly from their bar models. Under (KF.3), they are evaluation and coevaluation in the category of presentable categories. Their two triangle composites are the natural augmentations
\[
 A\otimes_A M\longrightarrow M,
 \qquad P\otimes_A A\longrightarrow P.
                                                        \tag{KF.5}
\]
The same extra-unit contraction of the two-sided bar proves these equivalences, naturally and with their action maps. It also makes the comparisons compatible with further tensor products. Thus the triangle identities hold as coherent natural transformations. No compactness of the diagonal bimodule is required for these colimit-preserving duality maps.

In particular \(\operatorname{Vect}_K\) is its own categorical dual. Inserting \(\eta\), applying a given functor, and then applying \(\epsilon\) supplies inverse mate constructions
\[
 \operatorname{Map}_{\mathrm{Cat}_k}(\mathcal D\otimes\operatorname{Vect}_K,\mathcal E)
       \simeq
 \operatorname{Map}_{\mathrm{Cat}_k}(\mathcal D,\mathcal E\otimes\operatorname{Vect}_K).
                                                        \tag{KF.6}
\]
Here \(\operatorname{Map}_{\mathrm{Cat}_k}\) denotes the space of colimit-preserving \(k\)-linear functors. The triangle identities make the two constructions inverse; applying them to transformations gives the same coherent equivalence. Tensoring by \(\operatorname{Vect}_K\) is therefore both a left and a right adjoint on presentable \(k\)-linear categories. It preserves colimits and limits. More explicitly, for any small diagram of such categories and any test category \(\mathcal D\), apply (KF.6) to maps from \(\mathcal D\), then use the limiting cone universal property. Applying (KF.6) back identifies the result with the maps from \(\mathcal D\) to the limit of the extended categories. Yoneda proves
\[
 (\lim_i\mathcal C_i)\otimes\operatorname{Vect}_K
       \simeq\lim_i(\mathcal C_i\otimes\operatorname{Vect}_K).
                                                        \tag{KF.7}
\]
This works for every field extension. It says nothing about tensoring an individual infinite product of vector spaces by \(K\); Exercise 3.AI shows why that different assertion fails.

### 3.40. The actual smooth-descent D-module category after extension

On a smooth affine finite-type scheme \(U=\operatorname{Spec}R\), the category of unbounded D-module complexes is \(\operatorname{Mod}_{D_{R/k}}\). The localization of the operator algebra and its quasi-coherent module description give this affine realization. The operator base-change proof of §3.37 and (KF.3) now give the canonical equivalence
\[
 \operatorname{Dmod}(U)\otimes\operatorname{Vect}_K
       \simeq\operatorname{Mod}_{D_{R/k}\otimes_k K}
       \simeq\operatorname{Dmod}(U_K).
                                                        \tag{KF.8}
\]
This is an equivalence of the entire category; its source contains modules made using new \(K\)-linear morphisms as well as free extensions of old objects.

We check the actual descent maps. A smooth pullback is computed by its transfer module, with the relative dimension shift specified in §1.10. In coordinates, this module uses the extended coefficient ring and the commuting coordinate derivatives. Tensoring its tensor or Spencer model by \(K\) gives exactly the transfer model of the extended map. Relative dimensions, wedge degrees and differential signs stay the same. Flatness of the field extension preserves its augmentations. A regular closed embedding uses the finite normal Koszul transfer construction of §3.37 and the normal determinant line. Extending its coefficients gives the same normal equations, Koszul differential and line on the extended scheme. These constructions use canonical coefficient maps and multiplication, so their comparison maps respect composition, units, and the chain-rule transitions on overlaps. Thus (KF.8) is an equivalence of descent diagrams, not just a collection of equivalences on their levels.

Let \(\mathcal Y\) be a smooth algebraic stack with affine diagonal. On a quasicompact part, choose an affine smooth atlas \(U\); the nerve schemes \(U_n\) are affine and smooth. Face maps are smooth and degeneracies are sections of smooth maps, hence regular embeddings; the preceding transfer comparisons apply. Strong descent here means the homotopy-coherent limit used in [*D-modules on stacks, ind-schemes and the de Rham prestack*](../../GL-DMOD/src/stacks-ind-schemes-and-the-de-rham-prestack.md), §§1–2, and in §1.10. Its full category, including unbounded complexes, satisfies
\[
 \begin{aligned}
 \operatorname{Dmod}(\mathcal Y)\otimes\operatorname{Vect}_K
 &\simeq\left(\lim_{[n]\in\Delta}\operatorname{Dmod}(U_n)\right)
                       \otimes\operatorname{Vect}_K\\
 &\simeq\lim_{[n]\in\Delta}\operatorname{Dmod}((U_n)_K)
 \simeq\operatorname{Dmod}(\mathcal Y_K).
 \end{aligned}
                                                        \tag{KF.9}
\]
The middle equivalence is (KF.7), which handles the infinite categorical limit without any finiteness hypothesis on \(K\). For a nonquasicompact smooth stack, use its diagram of affine smooth charts or a quasicompact open exhaustion followed by these presentations. Restrictions are conservative, and (KF.7) applies to this further limit too. Common smooth refinements give the same comparison: its coefficient and transfer maps commute with every refinement arrow, and the iterated limits satisfy the same cone universal property. Thus (KF.9) is independent of the presentation and compatible with its higher descent maps.

**Theorem 3.40.** For every characteristic-zero field extension and every smooth algebraic stack with affine diagonal, (KF.9) gives scalar extension of the full strong-descent D-module category. It applies to \(\operatorname{Bun}_G(X)\) and to its bounded opens for every connected reductive \(G\). The smooth presentations and open-exhaustion construction of §§1.3–1.15 supply precisely this stack scope. The atlas, nerve and open diagrams remain diagrams of all unbounded complexes; no comparison with the ordinary derived category of the equivariant heart is used. The local half-line operator equivalences of §2 also commute with field extension, since both their line and chain-rule transition functions do. Hence the same argument applies to the specified half-twisted category.

Free scalar extension is conservative. On an affine chart it tensors each underlying cohomology module by the faithfully flat field extension. If the extended object is zero, those modules were zero; chart conservativity then proves that the original stack object was zero. This is a statement about the free-extension functor into the category (KF.9), not about descent of each target object to the original field.

### 3.41. Compact tests and the fixed-support boundary

Write \(q:\mathcal C\rightleftarrows\mathcal C_K:r\) for free extension and forgetful in (KF.1). The adjunction is the usual free-action universal property, at the level of mapping complexes. In particular
\[
 q\dashv r,\qquad r q(F)\simeq F\otimes_k K.
                                                        \tag{KF.10}
\]
If \(c\) is compact, \(q(c)\) is compact: its mapping functor is \(\operatorname{RHom}_{\mathcal C}(c,r(-))\), and \(r\) preserves colimits. Moreover
\[
 \operatorname{RHom}_{\mathcal C_K}(q(c),q(F))
       \simeq\operatorname{RHom}_{\mathcal C}(c,F)\otimes_k K.
                                                        \tag{KF.11}
\]
To prove this last comparison, use (KF.10). Choose a basis of \(K\) as a \(k\)-vector space; \(F\otimes_k K\) is the corresponding sum of copies of \(F\). Compactness makes the mapping functor commute with this sum, since it is the filtered colimit of its finite subsums. The resulting identification is the canonical scalar comparison map, so the isomorphism does not depend on the chosen basis. Exactness also retains the entire mapping complex, including all its cohomological degrees.

If a collection \(c_i\) compactly generates \(\mathcal C\), its extensions compactly generate \(\mathcal C_K\). Indeed,
\[
 \operatorname{RHom}_{\mathcal C_K}(q(c_i),M)=0\text{ for all }i
 \ \Longrightarrow\ rM=0\ \Longrightarrow\ M=0.
                                                        \tag{KF.12}
\]
The first implication is the same adjunction and original generation; forgetful is conservative because an action on a zero underlying object is zero. This gives the compact generator comparison for the full automorphic category whose compact generation was proved in §1.15.

There is also a useful fully faithful comparison. Given a colimit-preserving fully faithful inclusion \(i:\mathcal A\hookrightarrow\mathcal C\) of presentable stable \(k\)-linear categories, internal \(K\)-module objects give
\[
 i_K:\mathcal A\otimes\operatorname{Vect}_K
       \hookrightarrow\mathcal C\otimes\operatorname{Vect}_K,
 \qquad M\in\operatorname{im}(i_K)
       \Longleftrightarrow rM\in\operatorname{im}(i).
                                                        \tag{KF.13}
\]
Full faithfulness identifies all the mapping complexes imposing the action and its coherent relations. If an underlying object lies in \(\mathcal A\), every action map, relation and higher homotopy lifts uniquely through that full inclusion, proving the essential-image statement. The converse follows by forgetting the lifted action. This argument presupposes the displayed continuous presentable inclusion; it does not construct such an inclusion for an arbitrary support condition.

Fixed characteristic support can obstruct essential surjectivity to the geometrically extended support category. There is an explicit example, which we compute without any spectral-projector premise. Take \(K=k(a)\) with \(a\) transcendental, and consider on \(\mathbb A^1_K\)
\[
 M_a=K[t]e,\qquad \partial(fe)=(f'+af)e,
 \qquad M_a\simeq D_K/D_K(\partial-a).
                                                        \tag{KF.14}
\]
The Weyl commutator is the identity. Moving derivatives to the right and then using \((\partial-a)e=0\) reduces every class to a unique polynomial times \(e\); independence follows by its displayed action. Right multiplication by \(\partial-a\) on \(D_K\) is injective: the leading derivative order of a nonzero operator increases by one. Thus \(M_a\) is the cofiber of this map between copies of \(D_K\), a valid object of the full category (KF.8). Its good filtration can be constant in nonnegative degrees, \(F_nM_a=K[t]e\). Derivatives preserve this filtration, so its characteristic variety is the zero section.

But forget the \(K\)-action and regard it as a \(D_k\)-module. The map \(D_k\to M_a\), \(P\mapsto Pe\), sends its PBW expression \(\sum_j f_j(t)\partial^j\) to \(\sum_j f_j(t)a^je\). It is injective by transcendence of \(a\), and its image \(k[t,a]e\) is stable under both operators. This is an actual coherent submodule isomorphic to the free \(D_k\)-module, whose characteristic variety is all of \(T^*\mathbb A^1_k\). Therefore the underlying object fails the zero-support convention of §3.12. Whenever the fixed-zero-support category has the continuous presentable inclusion required in (KF.13), \(M_a\) cannot be in its scalar-extended image. Its zero characteristic variety over \(K\) does not repair the original-field support failure.

For the nilpotent spectral category, proving its actual continuous inclusion, enhanced projected point generators and their field-extension comparison is still required. The full-category theorem (KF.9) and compact comparison (KF.11) do not establish essential surjectivity for that subcategory. The distinction is also present in [Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky, *The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support*](https://arxiv.org/abs/2010.01906v2), §20.9. The complete explicit module duality above can be compared with the free author chapter [Gaitsgory–Rozenblyum, *Some higher algebra*](https://people.mpim-bonn.mpg.de/gaitsgde/Book/HA.pdf), §8.6. These references accompany the proofs; the enhanced spectral action/projector, its regular image, global point adjunction and general microlocal comparison remain not yet proved here.

![Module-category duality carries infinite descent limits through field extension, while an individual vector-space product and a fixed support category retain different comparison requirements.](figures/categorical-field-extension.svg)

*Figure 3.12.* The diagonal regular \(K\)-bimodule is the coevaluation object; tensoring it over \(K\) supplies the two triangle identities (KF.4)–(KF.5). This gives categorical limit comparison (KF.7) and the strong-descent diagram (KF.9). The lower panel uses the exact transcendental connection (KF.14): its extended characteristic variety is zero, while its original-field coherent free-operator submodule has the full cotangent plane as characteristic variety. The figure is a schematic of these algebraic and categorical maps, with the support dimensions explicitly labeled.

**Exercise 3.AH.** For \(M_a\) in (KF.14), verify the Weyl action and the coherent free \(D_k\)-submodule. Compute both characteristic varieties. Explain why construction from a \(K\)-linear cofiber in the full category does not imply construction from the fixed-zero-support scalar extension.

**Solution 3.AH.** The difference between \(\partial(tfe)\) and \(t\partial(fe)\) is \(fe\). The ordered vector \(t^i\partial^je\) equals \(t^ia^je\); those vectors are linearly independent over \(k\), since a finite relation is a polynomial in the transcendental \(a\) with coefficients in \(k[t]\). They span \(k[t,a]e\), and differentiation acts there as \(\partial_t+a\), so this span is the free coherent \(D_k\)-submodule. Its order filtration has associated graded \(k[t,\xi]\), giving the full cotangent plane, of dimension two. Over \(K\), the constant good filtration of \(K[t]e\) has associated graded \(K[t]\) with \(\xi\) acting by zero, giving the zero section, of dimension one. The full-category cofiber uses \(D_K\), whose own support is the full plane; it is not a construction inside a fixed-zero-support subcategory. The membership criterion of (KF.13) excludes the underlying original-field object from that image.

**Exercise 3.AI.** Let \(c=\bigoplus_{n\geq0}k\) and \(K=k(a)\). Show that the natural map \(\operatorname{Hom}_k(c,k)\otimes_k K\to\operatorname{Hom}_K(c\otimes_k K,K)\) is injective but not surjective. Does this contradict categorical limit comparison (KF.7)?

**Solution 3.AI.** The map is \((\prod_{n\geq0}k)\otimes_k K\to\prod_{n\geq0}K\). For injectivity, express a tensor as a finite sum with linearly independent coefficients in \(K\). Vanishing at each coordinate forces every corresponding scalar sequence to vanish. Every sequence in its image has all its coordinates in one finite-dimensional \(k\)-subspace of \(K\), namely the span of those finitely many coefficients. The sequence \((a^n)_{n\geq0}\) does not, because its powers are linearly independent over \(k\). This proves failure of surjectivity. The object \(c\) is not compact: its identity cannot factor through any finite subsum of itself. Thus (KF.11) does not apply. Equation (KF.7) concerns a limit of presentable categories under categorical tensor product, not this product of objects in \(\operatorname{Vect}_k\).

**Exercise 3.AJ.** Let \(k=\mathbb Q\), \(K=k(u)\) with \(u^2=2\). In \(K\otimes_k K=k[u,v]/(u^2-2,v^2-2)\), compute the diagonal idempotent and identify the coevaluation module. Verify the triangle operation on a \(K\)-module and explain which part extends to an arbitrary field extension.

**Solution 3.AJ.** The diagonal idempotent is \(e_+=1/2+uv/4\). Substitution gives \(e_+^2=e_+\) and \((v-u)e_+=0\). Its value on \(v=u\) is one and on \(v=-u\) is zero. To verify the decomposition directly, regard the ring as \(K[v]/((v-u)(v+u))\); the two factors are comaximal because \(2u\) is invertible. The remainder map to the two evaluations is an isomorphism, with inverse built from \(e_+\) and \(1-e_+\). Thus \((K\otimes_k K)e_+\) is precisely the regular diagonal bimodule \(K\) used by coevaluation. Evaluation over one of its \(K\)-actions sends \(K\otimes_K M\) to \(M\) by multiplication; inserting the unit is its inverse, with the bar contraction proving the derived identity. For any field extension the regular diagonal bimodule and this bar contraction still exist, proving categorical duality. The finite idempotent decomposition in this example is not needed for that general proof.

### 3.42. The regular algebra of a specified rigid action

The enhanced projector needs an algebra, an action and an adjunction. We construct its categorical part explicitly. Work in the unbounded presentable stable \(k\)-linear categories of §3.39. Let \(\mathcal A\) be a symmetric monoidal such category, with tensor preserving colimits separately, compact unit and a small set of compact dualizable generators. Here “dualizable” refers to the monoidal tensor in \(\mathcal A\). Choose a small full DG subcategory \(\mathcal E\) of compact dualizable objects, containing that family and the unit and closed under duals, finite cones, tensor products and retracts. Such a choice exists: a dual is compact because \(\operatorname{RHom}(a^\vee,-)=\operatorname{RHom}(\mathbf1,a\otimes-)\); duality is preserved by finite cones and retracts by its tensor–Hom identity; tensor products are dualizable and preserve compactness by the same identity. Put \(\mathcal B=\mathcal A\otimes_k\mathcal A\). The tensor between categories is distinguished from the monoidal tensor between their objects by \(\boxtimes\).

We first justify the module models needed for the construction. The restricted Yoneda functor and its left adjoint are
\[
 Y(c)(a)=\operatorname{RHom}_{\mathcal A}(a,c),
 \qquad W(M)=\int^{a\in\mathcal E}M(a)\otimes_k a,
 \qquad \mathcal A\simeq\operatorname{Mod}_{\mathcal E}.
                                                        \tag{EP.1}
\]
Modules on the right are DG functors \(\mathcal E^{\mathrm{op}}\to\operatorname{Vect}_k\). The coend is the geometric realization of the free multi-object bar: its terms sum over finite strings of objects and tensor their DG morphism complexes with the module value and the last representing object. Faces compose morphisms or act, and degeneracies insert identity morphisms. On a representable module the augmentation contracts by inserting its first identity, just as in (KF.2). Thus the adjunction unit is an equivalence on representables. Each DG module is the realization of its augmented free bar; after forgetting the action the same identity insertion contracts that augmentation. This proves the unit on every module. Compactness and exactness make \(Y\) preserve sums and their bar realizations. The counit becomes an equivalence under every \(\operatorname{RHom}(a,-)\); those tests detect zero by the generating assumption, so it is an equivalence. This proves (EP.1), with all DG morphisms and their coherent relations retained.

Applying this free-bar universal property to two variables gives \(\mathcal B\simeq\operatorname{Mod}_{\mathcal E\otimes_k\mathcal E}\): functors out of either side are exactly the bilinear functors with the two commuting DG actions. In particular the objects \(x\boxtimes y\), for \(x,y\in\mathcal E\), compactly generate \(\mathcal B\). Tensor in \(\mathcal A\) preserves compactness on them: \(\operatorname{RHom}(x\otimes y,-)\simeq\operatorname{RHom}(y,x^\vee\otimes-)\), and both functors on the right preserve colimits. Consequently the monoidal multiplication \(\mu:\mathcal B\to\mathcal A\) has the following explicitly constructed continuous right adjoint:
\[
 \operatorname{RHom}_{\mathcal B}(x\boxtimes y,r(c))
       =\operatorname{RHom}_{\mathcal A}(x\otimes y,c),
 \qquad \mu\dashv r.
                                                        \tag{EP.2}
\]
The right side is a DG module on \(\mathcal E\otimes\mathcal E\); (EP.1) realizes it as \(r(c)\). The free bar proves the displayed adjunction on every object of \(\mathcal B\). It also proves continuity of \(r\), since all \(x\otimes y\) are compact and colimits of DG modules are computed on their values.

The regular algebra is the following actual object, with its bar presentation:
\[
 \mathcal R_{\mathcal A}=r(\mathbf1_{\mathcal A})
   \simeq\int^{a\in\mathcal E}a^\vee\boxtimes a,
 \qquad
 B_n=\bigoplus_{a_0,\ldots,a_n\in\mathcal E}
  \left(\bigotimes_{i=1}^{n}\operatorname{RHom}(a_{i-1},a_i)\right)
              \otimes_k(a_n^\vee\boxtimes a_0).
                                                        \tag{EP.3}
\]
To check the coend identification, map \(x\boxtimes y\) into its bar. These compact tests commute with the realization. Dualization identifies the resulting augmented morphism bar with paths from \(y\) to \(x^\vee\); composition augments it to \(\operatorname{RHom}(y,x^\vee)\simeq\operatorname{RHom}(x\otimes y,\mathbf1)\). Inserting the identity of \(y\) at the start contracts the augmented bar. It therefore gives precisely (EP.2) for \(c=\mathbf1\). Compact generators detect the claimed equivalence. The bar uses direct sums in its simplicial direction, with the usual internal differential and alternating face differential with total-complex signs. Identity insertion is a contraction in every simplicial degree, including for unbounded internal complexes.

We need strict compatibility with the \(\mathcal B\)-action. The canonical adjunction mate gives
\[
 b\otimes r(c)\longrightarrow r(\mu(b)\otimes c),
 \qquad b\otimes r(c)\simeq r(\mu(b)\otimes c).
                                                        \tag{EP.4}
\]
For dualizable compact \(b\), map a compact test \(t\) into it. Moving \(b\) across Hom gives \(\operatorname{RHom}_{\mathcal B}(b^\vee\otimes t,r(c))\); (EP.2) turns this into \(\operatorname{RHom}_{\mathcal A}(\mu(t),\mu(b)\otimes c)\). This is exactly the right side of (EP.4), since \(\mu\) preserves these monoidal duals. Thus the canonical map is an equivalence. The products \(x\boxtimes y\) are such dualizable compacts and generate \(\mathcal B\). Both sides preserve colimits in \(b\), so it is an equivalence for every \(b\). Its unit, composition and higher compatibilities are the mates of the same counit and monoidal multiplication maps. The adjunction triangle identities identify these mates, giving coherent \(\mathcal B\)-linearity of \(r\).

The right adjoint of the symmetric monoidal functor \(\mu\) has its lax symmetric monoidal maps: their mates multiply the counits \(\mu r(c)\to c\). At the unit these give
\[
 \mathbf1_{\mathcal B}\longrightarrow\mathcal R_{\mathcal A},
 \qquad
 \mathcal R_{\mathcal A}\otimes\mathcal R_{\mathcal A}
                    \longrightarrow\mathcal R_{\mathcal A},
 \qquad
 (a\boxtimes\mathbf1)\otimes\mathcal R_{\mathcal A}
       \simeq r(a)
       \simeq(\mathbf1\boxtimes a)\otimes\mathcal R_{\mathcal A}.
                                                        \tag{EP.5}
\]
The algebra is commutative, with coherent associativity and unit: their mates are the associative, symmetric and unital multiplication maps in \(\mathcal A\). Equivalently, the coend multiplies the \(a,b\) summands into the \(a\otimes b\) summand, using \((a\otimes b)^\vee\simeq a^\vee\otimes b^\vee\) with its symmetry. The identity-object summand supplies the unit. These maps respect the bar relations. The last two equivalences in (EP.5) are (EP.4). They give the tensor-compatible balancing used for Hecke eigen-objects.

### 3.43. Enhanced induction and its entire module category

Let \(\mathcal N\) be a specified continuous \(\mathcal B\)-module category, writing its action as \(\star\). Define its category of balanced eigen-objects by continuous module functors:
\[
 \mathcal H(\mathcal A,\mathcal N)
   =\operatorname{Fun}^{\mathrm L}_{\mathcal B}(\mathcal A,\mathcal N),
 \qquad U(F)=F(\mathbf1),
 \qquad L(n)(a)=r(a)\star n.
                                                        \tag{EP.6}
\]
Here \(\mathcal A\) is a \(\mathcal B\)-module via \(\mu\). Formula (EP.4) makes \(L(n)\) a continuous module functor. A module functor \(F\) has \(F(a)\simeq(a\boxtimes\mathbf1)\star F(\mathbf1)\), with all coherences included. Thus \(U\) is conservative; its colimits are the pointwise colimits of module functors. Evaluation at the unit identifies \(\operatorname{Fun}^{\mathrm L}_{\mathcal B}(\mathcal B,\mathcal N)\) with \(\mathcal N\).

Under this identification \(U\) is precomposition with \(\mu\), while \(L\) is precomposition with \(r\). They are adjoint, with the explicit mapping-complex equivalence
\[
 \operatorname{RHom}_{\mathcal H}(L(n),F)
            \simeq\operatorname{RHom}_{\mathcal N}(n,U(F)),
 \qquad L\dashv U,
 \qquad UL(n)=\mathcal R_{\mathcal A}\star n.
                                                        \tag{EP.7}
\]
For completeness, a transformation \(\tau:G\circ r\to F\) is sent to \(G\to G\circ r\circ\mu\to F\circ\mu\), using the adjunction unit and then \(\tau\circ\mu\). A transformation \(\sigma:G\to F\circ\mu\) is sent to \(G\circ r\to F\circ\mu\circ r\to F\), using \(\sigma\circ r\) and the counit. The triangle identities prove these maps inverse on transformations and their higher homotopies. They respect module structures because the unit and counit do. This proves the full adjunction, without restricting objects to a heart.

The resulting monad is the action of the algebra (EP.5). Its multiplication is \(r(\epsilon_{\mathbf1})\), after (EP.4) identifies \(r\mu r(\mathbf1)\) with \(\mathcal R_{\mathcal A}\otimes\mathcal R_{\mathcal A}\); this is exactly the lax-monoidal multiplication already constructed. Moreover
\[
 \mathcal H(\mathcal A,\mathcal N)
       \simeq\operatorname{Mod}_{\mathcal R_{\mathcal A}}(\mathcal N),
 \qquad
 |\cdots\,L(UL)^2U(F)\rightrightarrows LULU(F)
                         \rightrightarrows LU(F)|\simeq F.
                                                        \tag{EP.8}
\]
Here the simplicial degree \(n\) term is \(L(UL)^nU(F)\). After \(U\), this is the free augmented algebra-action bar of \(U(F)\). Inserting its first unit contracts it, so its realization is \(U(F)\). The functor \(U\) preserves colimits and is conservative, proving the augmentation in (EP.8). Conversely, given a module for \(T=UL\), realize \(L(T^n n)\), with faces from its module action and the monad multiplication, and degeneracies from the unit. Applying \(U\) gives the same split augmented module bar and recovers \(n\) with its action. These constructions are inverse on objects, morphism complexes and coherent action relations by the augmented-bar contraction. They prove the displayed equivalence and presentability of \(\mathcal H\). No boundedness or completion of ordinary equivariant hearts is used.

We now include affine spectral coefficients. Let \(R\) be a commutative DG \(k\)-algebra, let \(\mathcal M\) be a continuous \(\mathcal A\)-module category, and specify a continuous symmetric monoidal functor \(\Phi:\mathcal A\to\operatorname{Mod}_R\). Put
\[
 \begin{aligned}
 \mathcal N_R&=\mathcal M\otimes_k\operatorname{Mod}_R
                  \simeq\operatorname{Mod}_R(\mathcal M),\\
 (a\boxtimes b)\star(m\boxtimes Q)
          &=(a\star m)\boxtimes(\Phi(b)\otimes_R Q),\\
 \mathcal R_R&=(\operatorname{Id}\otimes\Phi)(\mathcal R_{\mathcal A}).
 \end{aligned}
                                                        \tag{EP.9}
\]
The internal-module comparison is the same free-bar proof as (KF.1), valid for this algebra as for a field. This defines the full coefficient Hecke category \(\mathcal H_R=\mathcal H(\mathcal A,\mathcal N_R)\). Its regular-algebra action is equivalently the action of \(\mathcal R_R\in\mathcal A\otimes_k\operatorname{Mod}_R\). The balancing (EP.5) gives its tensor-compatible eigen-isomorphisms \(a\star n\simeq n\otimes_R\Phi(a)\).

Let \(s:\mathcal M\to\mathcal N_R\) be free \(R\)-action and \(v\) its forgetful right adjoint. It preserves colimits and is conservative, because module colimits are underlying colimits and an action on zero is zero. The enhanced induction is now constructed, together with its actual adjunction:
\[
 P_R^{\mathrm{enh}}=L\circ s:\mathcal M\to\mathcal H_R,
 \qquad J_R=v\circ U,
 \qquad
 \operatorname{RHom}_{\mathcal H_R}(P_R^{\mathrm{enh}}c,F)
      \simeq\operatorname{RHom}_{\mathcal M}(c,J_RF).
                                                        \tag{EP.10}
\]
If \(c_i\) are compact generators of \(\mathcal M\), then
\[
 P_R^{\mathrm{enh}}c_i\text{ are compact generators of }\mathcal H_R.
                                                        \tag{EP.11}
\]
Compactness follows from (EP.10) and continuity of \(J_R\). Vanishing of all their mapping complexes gives \(J_RF=0\); its two forgetful factors are conservative, so \(F=0\). These statements apply to every object of the unbounded category. They establish free enhanced induction; they assert no idempotence of its monad and no identification with a geometrically specified support category.

### 3.44. Extension of the specified action and its enhanced generators

Let \(K/k\) be any field extension. Extend \(\mathcal A,\mathcal M,R,\Phi\) and their monoidal/module structure maps by \(K\), using the actual categorical scalar extension of §3.39. In particular \(R_K=R\otimes_k K\). Tensoring the continuous adjunction \(\mu\dashv r\), including its unit and counit, gives an adjunction on the extended categories. It is the multiplication adjunction there: free extensions of the original compact dualizable generators generate and remain compact by (KF.11)–(KF.12). Hence
\[
 r_K(q_{\mathcal A}a)\simeq q_{\mathcal B}(r(a)),
 \qquad
 \mathcal R_{\mathcal A_K}\simeq q_{\mathcal B}(\mathcal R_{\mathcal A}),
 \qquad
 J_{R_K}P_{R_K}^{\mathrm{enh}}(q_{\mathcal M}c)
       \simeq q_{\mathcal M}(J_RP_R^{\mathrm{enh}}c).
                                                        \tag{EP.12}
\]
The first identity is the extended functor \(r\) on a free extension; uniqueness of right adjoints supplies its canonical identification. The second sets \(a=\mathbf1\); the units and multiplications also extend, since their mates are the extended counits. For the last identity, use (EP.9): the regular-algebra action, the free coefficient module and its underlying object extend by exactly these tensor maps. This also proves compatibility with all their coherent action relations.

Assume \(\mathcal M\) is compactly generated. Extending the module actions constructs a continuous \(K\)-linear functor \(E:\mathcal H_R\otimes_k\operatorname{Vect}_K\to\mathcal H_{R_K}\). On free extensions it takes \(P_R^{\mathrm{enh}}c\) to \(P_{R_K}^{\mathrm{enh}}q_{\mathcal M}c\). Its comparison on compact generators is an equivalence, because (EP.10), (EP.12) and (KF.11) give
\[
 \operatorname{RHom}_{\mathcal H_{R_K}}
       (P_{R_K}^{\mathrm{enh}}q c_i,P_{R_K}^{\mathrm{enh}}q c_j)
   \simeq
 \operatorname{RHom}_{\mathcal H_R}
       (P_R^{\mathrm{enh}}c_i,P_R^{\mathrm{enh}}c_j)\otimes_k K.
                                                        \tag{EP.13}
\]
This identifies the canonical comparison, not only the dimensions of its cohomology. For a fixed compact source generator, both mapping functors preserve colimits in the target object; equivalence on generators therefore gives equivalence on all target objects. Now fix a target object. Both mapping functors in the source variable take colimits to limits, and \(E\) preserves colimits. The same generation argument gives equivalence for every source object. Thus \(E\) is fully faithful. By (EP.11) and (KF.12) its image contains compact generators of the target. Its full image is closed under colimits, cones and retracts: compute colimits in the source, and lift retract idempotents through full faithfulness. Consequently its image is the whole target. We have proved
\[
 \mathcal H_R\otimes_k\operatorname{Vect}_K
        \simeq\mathcal H_{R_K},
 \qquad q(P_R^{\mathrm{enh}}c_i)
          \longmapsto P_{R_K}^{\mathrm{enh}}q(c_i).
                                                        \tag{EP.14}
\]
All fields and all unbounded objects are included. This is the full eigen-category for the specified extended action. An identification of that action with the geometric Ran Hecke action, or of its eigen-category with the regular nilpotent relative spectral category, still has to be proved.

An explicit example shows what the algebra and enhancement do. Take \(\mathcal A=\operatorname{Vect}_k^{\mathbb Z}\) with graded convolution: \(k_n\otimes k_m=k_{n+m}\). Its compact generators \(k_n\) have duals \(k_{-n}\). Take \(\mathcal M=\operatorname{Vect}_k\) with the forgetful action and \(\Phi(k_n)=R\), with the identity tensor coherences. Directly from (EP.2) and the multiplication, we obtain
\[
 \begin{aligned}
 \mathcal R_{\mathcal A}&=\bigoplus_{n\in\mathbb Z}k_n\boxtimes k_{-n},
 &\mathcal R_R&=R[z,z^{-1}],\\
 \mathcal H_R&\simeq\operatorname{Mod}_{R[z,z^{-1}]},
 &P_R^{\mathrm{enh}}(V)&=R[z,z^{-1}]\otimes_k V.
 \end{aligned}
                                                        \tag{EP.15}
\]
Indeed a bidegree \((i,j)\) maps to the unit after multiplication exactly when \(i+j=0\). Its algebra multiplication sends the \(n,m\) basis vectors to the \(n+m\) vector. After the two forgetful actions this is precisely the Laurent algebra. A balanced eigen-object is a complex of \(R\)-modules with its coherently invertible integer action; the group-algebra module bar gives that entire DG category. Its free rank-one module is a compact generator. For \(R=k\), the monad multiplication sends \(z^i\otimes z^j\) to \(z^{i+j}\). The nonzero vector \(z\otimes1-1\otimes z\) lies in its kernel. Thus this enhanced induction is not an idempotent localization.

For the geometric application, \(\mathcal A\) must be the proper-curve Ran representation category, with its actual fusion Hecke action on the chosen automorphic sheaf category and its actual spectral coefficient functor. The free source [Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky, *The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support*](https://arxiv.org/abs/2010.01906v2), §§11–13 and 15, constructs the regular Ran algebra and enhanced induction; §§16.2 and 20.9 use projected point generators. In that construction compact Ran generators use Verdier duality and the trace on the proper curve. Geometric Satake/fusion, that geometric rigidity and the spectral functor must supply the specified data of (EP.9). The actual regular nilpotent image and its projected point generators require the additional microlocal and support arguments. These geometric identifications are not yet proved here. No step above identifies the full free eigen-category with a fixed-support subcategory, and the original arbitrary-field and full connected-reductive regularity obligations remain.

![The regular algebra produces free enhanced Hecke induction and its conservative forgetful adjoint. The entire specified eigen-category extends with its compact generators; the Laurent example has a nonidempotent monad.](figures/enhanced-hecke-induction.svg)

*Figure 3.13.* The upper two panels show the explicitly constructed regular algebra and adjunctions (EP.2)–(EP.10). The middle comparison is (EP.14) for the same action and coefficient functor extended by \(K\). The lower panel is the exact Laurent model (EP.15), including a nonzero element killed by monad multiplication. The diagram assumes the compact rigid action specified in §3.42; it makes no geometric identification with the nilpotent spectral category.

**Exercise 3.AK.** Compute the unit and multiplication of the Laurent monad in (EP.15), verify its compact generator in the full unbounded category and prove that its multiplication is not an equivalence.

**Solution 3.AK.** The unit is \(v\mapsto1\otimes v\). Multiplication is \(z^i\otimes z^j\otimes v\mapsto z^{i+j}\otimes v\); the exponent law proves associativity and the exponent zero proves both unit identities. The mapping complex from the free module \(k[z,z^{-1}]\) to a module \(M\) is the whole underlying complex of \(M\), by the free-module adjunction. It commutes with colimits and detects zero, so the free module compactly generates even for unbounded \(M\). The tensors \(z\otimes1\) and \(1\otimes z\) are different Laurent basis vectors, whose difference maps to zero. Hence multiplication is not injective on degree-zero cohomology and is not an equivalence. This does not contradict its induction adjunction.

**Exercise 3.AL.** Take \(R=k\) and replace \(\mathbb Z\) by \(\mathbb Z/2\), over a field with \(2\ne0\). Compute the regular algebra, the free induction and its adjunction under the decomposition into its two idempotents. Check its extension to an arbitrary field \(K/k\).

**Solution 3.AL.** The compact generators are \(k_0,k_1\), each self-dual; the regular algebra has the two bidegrees \((0,0),(1,1)\), with the latter square equal to the former. After the forgetful actions it is \(k[g]/(g^2-1)\). Its idempotents are \(e_\pm=(1\pm g)/2\); they sum to one, have product zero and square to themselves. A DG module is therefore the pair \((e_+M,e_-M)\), giving the entire module category \(\operatorname{Vect}_k\times\operatorname{Vect}_k\). Free induction sends \(V\) to \((V,V)\); forgetful sends a pair to its direct sum. The adjunction on mapping complexes is
\[
 \operatorname{RHom}(V,M_+)\oplus\operatorname{RHom}(V,M_-)
    \simeq\operatorname{RHom}(V,M_+\oplus M_-),
\]
since this sum is finite. Tensoring gives the same algebra, idempotents, free pair and adjunction over \(K\). No finite-dimensional restriction on \(K\) or boundedness restriction on either component is needed.

**Exercise 3.AM.** Let \(R=k[s,s^{-1}]\), \(D=R[z,z^{-1}]\) and \(Q=D/(z-s)=R\). Compute \(\operatorname{RHom}_D(Q,Q)\) and \(Q\otimes_D^{\mathrm L}Q\). Is restriction \(\operatorname{Mod}_R\to\operatorname{Mod}_D\) a fully faithful functor of DG categories? Does this quotient define an idempotent derived projector?

**Solution 3.AM.** Multiplication by \(z-s\) is injective in the Laurent polynomial domain \(D\). Substitution \(z=s\) identifies its cokernel with \(R\): multiply a Laurent polynomial by a power of \(z\), use polynomial division by \(z-s\), and invert the unit \(s\) afterwards. Thus \(D\xrightarrow{z-s}D\), placed in degrees \(-1,0\), is a free resolution of \(Q\). Applying Hom into \(Q\), or tensoring with \(Q\), kills its differential. With cohomological shifts this gives
\[
 \operatorname{RHom}_D(Q,Q)\simeq R\oplus R[-1],
 \qquad Q\otimes_D^{\mathrm L}Q\simeq R\oplus R[1].
                                                        \tag{EP.16}
\]
In the first formula the extra cohomology is in degree \(1\); in the second it is in degree \(-1\). But \(\operatorname{RHom}_R(R,R)=R\) is concentrated in degree zero. Restriction therefore fails full faithfulness. The extension–restriction counit on \(Q\) has this additional negative-degree Tor term and is not an equivalence, so the quotient does not define an idempotent derived localization. The ordinary degree-zero quotient and the entire derived module category have different adjunction behavior, as these explicit complexes demonstrate.

### 3.45. Compact D-modules on the projective powers of the curve

Let \(k\) be a field of characteristic zero and let \(X\) be a smooth projective curve over \(k\). Empty powers mean \(\operatorname{Spec}k\). We use the full unbounded category \(\operatorname{Dmod}(Y)\) of algebraic D-modules with quasi-coherent underlying structure-sheaf complexes. Left and right modules are related by the density-line equivalence. In this section, coherent always means coherent over \(\mathcal D_Y\); it does not mean coherent over \(\mathcal O_Y\).

We first establish the compactness statement needed for the actual Ran diagram. On a separated scheme with a finite affine cover \(U_1,\ldots,U_r\), the intersections \(U_H=\bigcap_{h\in H}U_h\) are affine. For every unbounded quasi-coherent complex \(Q\),

\[
 R\Gamma(Y,Q)\simeq
 \operatorname{Tot}\left[
  \bigoplus_i\Gamma(U_i,Q)\longrightarrow
  \bigoplus_{i<j}\Gamma(U_{ij},Q)\longrightarrow\cdots
  \longrightarrow\Gamma(U_{\{1,\ldots,r\}},Q)
 \right].
 \tag{RN.1}
\]

All section complexes on the right are derived affine sections; there are only \(r\) horizontal degrees. Here is why this formula also holds without a lower cohomological bound. The affine module–sheaf equivalence identifies complexes on an affine with complexes of modules, and localization is flat. Thus affine sections and restriction to a principal open are exact functors on these complexes. For each \(U_H\), its inclusion in \(Y\) is affine: on an affine target chart its inverse image is an intersection of two affine opens in a separated scheme. Its direct image on quasi-coherent modules is therefore exact. Form the finite ordered augmented Čech complex of these direct images. Near a point choose one covering index whose open contains a neighborhood of that point. Insertion of that index, with the alternating deletion signs, contracts the augmented complex on that neighborhood. The contraction works degree by degree for \(Q\). Taking its finite horizontal totalization preserves this identity. Consequently this is a resolution of \(Q\) by complexes of affine direct images. Their derived global sections are their affine section complexes, giving (RN.1).

The affine acyclicity and the insertion contraction are proved in Cohomology of affine schemes and Serre's criterion, §§2–3 and Čech cohomology, §§2–4. The finite-complex argument above supplies the unbounded extension; it uses neither an infinite product totalization nor a convergence assumption. In particular, \(R\Gamma(Y,-)\) commutes with all colimits. Each affine section functor does so, and finite limits and finite colimits coincide in a stable category.

Now suppose \(Y\) is smooth projective, and choose a very ample line bundle \(L\). Put

\[
 P_n=\mathcal D_Y\otimes_{\mathcal O_Y}L^n,\qquad
 \operatorname{RHom}_{\mathcal D_Y}(P_n,F)
 \simeq R\Gamma\bigl(Y,L^{-n}\otimes_{\mathcal O_Y}
       \operatorname{oblv}F\bigr),\qquad n\in\mathbf Z .
 \tag{RN.2}
\]

The tensor in \(P_n\) uses the right structure-sheaf action on \(\mathcal D_Y\); \(P_n\) is a left module. The displayed adjunction is obtained first on a free structure-sheaf module, then by the local line-bundle trivializations and their transition functions. The line is flat, so this is also the derived induction adjunction. Formula (RN.1) proves that every \(P_n\) is compact.

They detect every unbounded object. To prove this, let \(Q=\operatorname{oblv}F\) and suppose all complexes in (RN.2) vanish. For a section \(s\in\Gamma(Y,L^a)\), \(a>0\), whose nonvanishing open \(Y_s\) is affine, write \(j:Y_s\hookrightarrow Y\). There is an equality in the full derived quasi-coherent category

\[
 j_*j^*Q\simeq
 \underset{m\ge0}{\operatorname{colim}}\,
 \left(Q\otimes L^{am}
       \xrightarrow{\ s\ }Q\otimes L^{a(m+1)}\right).
 \tag{RN.3}
\]

Trivialize \(L^a\) on an affine chart. The right side becomes localization of the coefficient complex at the function representing \(s\), and the left side is that same localization. Flatness makes this a derived equality in every degree. The local equalities respect the line's transition functions and glue. Applying (RN.1) and the vanishing of the twists shows \(R\Gamma(Y_s,Q)=0\). Affine sections are conservative on the full module category, so \(Q|_{Y_s}=0\). The coordinate sections of a projective embedding supply finitely many such affine opens covering \(Y\). Thus \(Q=0\), and forgetting the operator action is conservative, so \(F=0\).

This also identifies all the compact objects:

\[
 \operatorname{Dmod}(Y)^c
     =D^b_{\mathrm{coh}}(\mathcal D_Y)
     =\operatorname{thick}\{P_n:n\in\mathbf Z\}.
 \tag{RN.4}
\]

For the inclusion from right to left, Holonomic D-modules and duality, Lemma 3.0 proves that every coherent operator module on a smooth \(d\)-dimensional variety has a local finite free operator resolution of length at most \(2d\). That lemma applies to all coherent modules. Finite truncation triangles therefore make every bounded coherent complex locally a finite complex of finite projective operator modules. Refine a finite affine cover to such neighborhoods. On each affine intersection, the full D-module category is the operator module category. The finite projective resolution shows that its derived Hom from the restricted complex commutes with colimits.

Use the full D-module descent of §3.40 to glue these local mapping complexes. The full Čech mapping complex reduces to the finite ordered complex by the support-preserving sorting and insertion homotopy proved in Čech cohomology, Theorem 2.1. Apply that identity to complexes of local derived maps: restrictions commute with the differential and with every insertion; compatible functorial resolution models implement those restrictions and their coherence maps. Equivalently, repeated two-open gluing gives the finite homotopy limit over all nonempty subsets of the covering indices. For two opens it is the pullback of the two local mapping complexes over the intersection; induction adds one open and its intersections and gives that same finite limit. Each entry commutes with colimits, and a finite limit of exact continuous functors is continuous. Thus the global mapping complex commutes with colimits, proving compactness. Operator actions can make the differentials of a local Hom complex fail to be structure-sheaf linear; this proof uses D-module mapping descent and does not assume that internal operator Hom is quasi-coherent.

Conversely, the free multi-object module bar of (EP.1), applied to the compact generators \(P_n\), identifies this full category with modules over their small DG category. Representable modules are compact, and every compact module is a retract of a finite construction from them. Indeed the free-cell bar presents every module as a colimit of finite cells; mapping out of a compact object makes its identity factor through a finite cell. A factorization of the identity supplies the retract. Finite shifts, cones and retracts of the \(P_n\) have bounded coherent cohomology: the operator sheaf is Noetherian locally, so its coherent modules are closed under finite kernels and quotients. This proves the other inclusion and the last equality in (RN.4).

Every coordinate map needed below is proper. If \(\beta:J_2\to J_1\) is a map of finite sets, let \(H=\operatorname{im}\beta\). Its coordinate map factors as

\[
 \Delta_\beta:X^{J_1}\longrightarrow X^{J_2},\qquad
 (x_j)_{j\in J_1}\longmapsto(x_{\beta(h)})_{h\in J_2},
 \qquad
 X^{J_1}\longrightarrow X^H\longrightarrow X^{J_2}.
 \tag{RN.5}
\]

The first map forgets the unused coordinates; it is a base change of a projective power of \(X\), hence proper. The second repeats coordinates and is a closed diagonal embedding, hence proper. This includes a map to the empty power. All the source and target powers are smooth projective. Theorem 3.4 of Adjunctions, base change and the projection formula proves proper direct-image coherence for every bounded coherent operator complex. Combining it with (RN.4) gives

\[
 (\Delta_\beta)_*:
   \operatorname{Dmod}(X^{J_1})^c
   \longrightarrow\operatorname{Dmod}(X^{J_2})^c .
 \tag{RN.6}
\]

We use the continuous direct-image functor on the full unbounded category. In right-module conventions it is the derived tensor with the transfer bimodule followed by sheaf direct image. Derived tensor preserves colimits. The bounded Spencer resolution of the transfer has finitely many coefficient columns, each quasi-coherent in the input complex's cohomological direction. Over an affine target open choose a finite affine cover of its inverse image, apply (RN.1) to each coefficient column, and then totalize the finite Spencer and Čech directions. Every column operation preserves colimits, so the total operation does too. The Spencer maps can involve differential operators; columnwise computation does not assume they are structure-sheaf linear. Neither finite direction depends on a cohomological bound for the input.

Theorem 4.1 of Direct images and the relative de Rham complex proves the composition isomorphism and its associativity on bounded complexes by the transfer chain rule and finite affine Čech computation. It therefore supplies it on all compacts here. The same free-cell bar used in (RN.4) extends that natural isomorphism, including its higher compatibility homotopies, uniquely to continuous functors on the whole category. Thus compositions of coordinate direct images are coherently the direct images of the composite coordinate maps. There is no replacement of the full category by its bounded part.

### 3.46. The actual twisted-finite-set diagram and its full colimit

Let \(\mathcal C\) be a compactly generated, \(k\)-linear, symmetric monoidal stable category with tensor preserving colimits in each variable. Assume its unit is compact and every compact object has a monoidal dual. Let \(\mathsf T\) be the twisted-arrow category of finite sets, including the empty set. An object is a function \(\psi:I\to J\). A morphism from \(\psi_1\) to \(\psi_2\) consists of functions

\[
 \alpha:I_1\to I_2,\qquad
 \beta:J_2\to J_1,\qquad
 \psi_1=\beta\circ\psi_2\circ\alpha .
 \tag{RN.7}
\]

The direction of \(\beta\) matters. Define the stage and its transition by

\[
 \mathcal A_\psi=
       \mathcal C^{\otimes I}\otimes\operatorname{Dmod}(X^J),
 \qquad
 F_{\alpha,\beta}=
       \operatorname{mult}_{\mathcal C}^{\alpha}
                 \otimes(\Delta_\beta)_* .
 \tag{RN.8}
\]

Multiplication tensors the labels in each fibre of \(\alpha\), inserting the unit in an empty fibre. The transfer composition just proved and the symmetric monoidal coherences of \(\mathcal C\) make this an actual homotopy-coherent diagram of continuous functors.

For clarity, the exterior-product equivalence used by this diagram is

\[
 \operatorname{Dmod}(Y)\otimes\operatorname{Dmod}(Z)
       \simeq\operatorname{Dmod}(Y\times Z)
 \quad\text{for smooth projective }Y,Z .
 \tag{RN.9}
\]

On smooth affine charts, the operator algebra of a product is the tensor product of the two operator algebras. The two kinds of vector fields commute; the PBW symbols on both sides are the symmetric algebra of the direct sum of the two tangent modules. The order filtration then proves the operator map is an isomorphism, by lifting and subtracting leading symbols. The free module bar proves the corresponding equivalence of full module categories, with no cohomological bound. To globalize, express each D-module category by its affine Čech descent diagram, as in §3.40. An affine module category is categorically dualizable by (KF.4), so tensoring with it preserves these limits. The compact-generation proof (RN.4) and the multi-object version of that same duality give this property for the projective category as well. First commute tensor past one affine descent diagram, then past the other. On every rectangular affine intersection the affine operator equality applies. The resulting double descent diagram is precisely that of \(Y\times Z\), proving (RN.9).

For coordinate maps, exterior product commutes with their direct images. The product transfer bimodule is the exterior product of the two transfers: this follows from the operator equality and the defining coefficient pullbacks. Their bounded Spencer resolutions tensor to the product resolution, with the usual complex tensor signs. Direct image on rectangular affine covers is the totalization of the two finite Čech directions. Iterated totalization equals the totalization of their double complex; finite horizontal length permits every interchange. This proves the product compatibility on full complexes, together with its associativity.

Each stage is compactly generated by tensor products of compact objects of \(\mathcal C\) and the objects in (RN.2) for \(X^J\). This follows from the multi-object free module bar: tensoring two module presentations gives the module category of the tensor product of the small DG categories, whose representables are the tensor products of their representables. A tensor product of compact dualizable objects of \(\mathcal C\) is compact. In fact its Hom is Hom from the compact unit after tensoring the target with the product of the duals, and that tensor operation is continuous. Formula (RN.6) now shows that every \(F_{\alpha,\beta}\) preserves compact objects.

We define the full D-module Ran category, its insertion functors and its tensor by

\[
 \begin{aligned}
 \mathcal C_{\operatorname{Ran}}^{\mathrm{dr}}
      &=\operatorname*{colim}_{\psi\in\mathsf T}\mathcal A_\psi,
       &\operatorname{ins}_\psi&:\mathcal A_\psi
                           \to\mathcal C_{\operatorname{Ran}}^{\mathrm{dr}},\\
 \operatorname{ins}_{\psi_1}(V_1\otimes F_1)\star
 \operatorname{ins}_{\psi_2}(V_2\otimes F_2)
      &=\operatorname{ins}_{\psi_1\sqcup\psi_2}
                       ((V_1\otimes V_2)\otimes(F_1\boxtimes F_2)),\\
 \mathbf1&=\operatorname{ins}_{\emptyset\to\emptyset}(k).
 \end{aligned}
 \tag{RN.10}
\]

The colimit is in presentable stable \(k\)-linear categories and continuous functors. We prove its compact-generation assertion, including why these are the insertion functors into that full colimit.

Choose a small DG category \(E_\psi\) of all compact objects at each stage, closed under finite constructions and retracts. The stages are their full module categories by (EP.1). Since the transitions preserve compacts they restrict to a coherent diagram of the \(E_\psi\). Form its enriched Grothendieck construction \(G\). In a strict diagram its objects are \((\psi,e)\) and

\[
 \operatorname{Hom}_G((\psi,e),(\chi,f))
   =\bigoplus_{\gamma:\psi\to\chi}
       \operatorname{Hom}_{E_\chi}(F_\gamma e,f),\qquad
 \xi_{\gamma,e}:(\psi,e)\longrightarrow(\chi,F_\gamma e).
 \tag{RN.11}
\]

Composition uses the transition composition and ordinary composition in \(E_\chi\). For a homotopy-coherent diagram the construction uses its bar resolution: strings of composable arrows, their transition maps, and their specified coherence homotopies. The \(n\)-simplex records an \(n\)-arrow string; inner faces compose arrows, outer faces apply the transition or compose the coefficient morphism, and degeneracies insert identities. These are exactly the face identities of the diagram's coherence data. Thus its functors to another DG category are families of stage functors with coherent comparison maps along all strings. This bar construction retains those higher comparisons rather than replacing the diagram by equations in its homotopy category. Formula (RN.11) describes the strict case and the structural edge in either construction.

Let \(h_g=\operatorname{Hom}_G(-,g)\) be a representable right module. Let \(\Sigma\) be the set of cones of the representable maps induced by all edges \(\xi_{\gamma,e}\). Each is compact. The full subcategory of \(\operatorname{Mod}_G\) consisting of modules \(M\) with \(\operatorname{RHom}(S,M)=0\) for every \(S\in\Sigma\) is a reflective continuous localization. Here is a direct construction. For \(M_0=M\), define functorially

\[
 M_{n+1}=
 \operatorname{cofib}\left(
     \bigoplus_{S\in\Sigma}
          S\otimes_k\operatorname{RHom}(S,M_n)
          \xrightarrow{\ \mathrm{ev}\ }M_n\right),
 \qquad
 L(M)=\operatorname*{colim}_{n\ge0}M_n .
 \tag{RN.12}
\]

Applying \(\operatorname{RHom}(S,-)\) to the evaluation map gives a split surjection of complexes: its section is the identity of \(S\) in the summand indexed by \(S\). Compactness of \(S\) identifies Hom into its tensor with a coefficient complex with the tensor of its Hom complex; this identification follows by constructing the coefficient complex from shifts and colimits of \(k\). Consequently each transition from \(\operatorname{RHom}(S,M_n)\) to \(\operatorname{RHom}(S,M_{n+1})\) is nullhomotopic. Compactness lets Hom commute with the sequential colimit, which is therefore zero. So \(L(M)\) is local.

The cone of \(M\to L(M)\) belongs to the subcategory generated under colimits by the \(S\). Each successive cone does, since the evaluation source is a sum of \(S\)'s tensored with coefficient complexes. A local object \(N\) receives zero Hom from this entire subcategory: Hom converts colimits in its source to limits, and it vanishes on every \(S\) and its shifts. Hence \(\operatorname{RHom}(L(M),N)\simeq\operatorname{RHom}(M,N)\). This proves the reflector adjunction. Every operation in (RN.12) is continuous because the \(S\) are compact. The inclusion of the local subcategory is continuous too: its defining Hom-vanishing conditions are preserved by colimits. The construction therefore gives a presentable full stable category, generated by the objects \(L(h_g)\).

A continuous functor from \(\operatorname{Mod}_G\) kills the \(S\) exactly when it carries all edges \(\xi_{\gamma,e}\) to equivalences. In one direction this is the cone test. In the other it kills their shifts, cones and all colimits. The reflector construction then shows it factors uniquely through \(L\), including the natural transformations and their homotopies. By the universal property of the enriched Grothendieck bar, these functors are exactly coherent compatible families of stage functors. This is the defining mapping property of the colimit in (RN.10). The argument proves that the localization just constructed is that colimit; its stage maps are the continuous extensions of \(e\mapsto L(h_{(\psi,e)})\).

These images are compact: Hom from \(L(h_g)\) in the local category is Hom from \(h_g\) after its continuous inclusion, namely evaluation of the module at \(g\). They generate because zero evaluation at every \(g\) means the module is zero. Applying the finite-cell argument once more yields

\[
 \begin{aligned}
 (\mathcal C_{\operatorname{Ran}}^{\mathrm{dr}})^c
    &=\operatorname{thick}\{
          \operatorname{ins}_\psi(e):
                 \psi\in\mathsf T,\ e\in\mathcal A_\psi^c\},\\
 \mathbf1&\text{ is compact},\qquad
 (\mathcal C_{\operatorname{Ran}}^{\mathrm{dr}})^c\star
 (\mathcal C_{\operatorname{Ran}}^{\mathrm{dr}})^c
    \subset(\mathcal C_{\operatorname{Ran}}^{\mathrm{dr}})^c .
 \end{aligned}
 \tag{RN.13}
\]

The exterior-product compatibility proves that the tensor in (RN.10) respects every transition relation. Its associativity, symmetry and unit maps come from disjoint union and exterior product, with their coherent identities. Since tensor of presentable categories preserves colimits, the stage operations extend to a continuous operation on the full colimit. Exterior products of compact stage generators are compact by (RN.4) and the local finite resolutions, proving the last assertion in (RN.13) first on generators and then under finite constructions and retracts.

This proves the actual D-module Ran diagram, its full category, its symmetric monoidal structure and its compact generators over any characteristic-zero field. It has not yet proved that every compact Ran object is dualizable. That requires the proper geometric duality evaluation, coevaluation and their triangle identities. It also has not constructed the fusion Hecke action, the spectral coefficient functor or the nilpotent regular image. Those remain necessary for applying the rigid-action theorem of §§3.42–3.44 to this category.

![The twisted finite-set map, its proper coordinate factorization and the full Ran localization](figures/ran-dmodule-diagram.svg)

*Figure 3.14.* The top panel is the morphism (RN.7) with both input labels sent to \(w\), both output coordinates sent to \(a\), and \(\psi_1(u)=\psi_1(v)=a\), \(\psi_2(w)=d\). The middle panel is the exact coordinate map \((x_a,x_b,x_c)\mapsto(x_a,x_a)\) from (RN.5): projective projection followed by a closed diagonal. The bottom panel is the full module localization (RN.11)–(RN.13), whose compact objects are the finite constructions and retracts of the inserted stage compacts. The diagram makes no assertion about the remaining Ran duality or the nilpotent image.

### 3.47. Two points, the empty stage, and a nonproper boundary

The index category is easiest to understand on a finite proper scheme. Take \(X=S\), a disjoint union of \(N>0\) rational points. Then \(\operatorname{Dmod}(S^J)\) is a product of copies of \(\operatorname{Vect}_k\) indexed by functions \(x:J\to S\). Direct image along a coordinate map sums the coefficients over its fibres. We claim, with the same full definition (RN.10), that

\[
 \mathcal C_{\operatorname{Ran}}^{\mathrm{dr}}(S)
       \simeq\mathcal C^{\otimes S},\qquad
 (V_i)_{i\in I}\otimes k_x
       \longmapsto
       \bigotimes_{p\in S}
          \left(\bigotimes_{\{i:x(\psi(i))=p\}}V_i\right).
 \tag{RN.14}
\]

The outside tensor denotes the object in the tensor product of the \(N\) categories, not a Cartesian product of them. In an empty inner fibre we insert \(\mathbf1_{\mathcal C}\). This formula defines a continuous stage functor: use the finite direct sum decomposition over \(x\), and extend the label multiplication from tensor-product generators. It is compatible with a transition. In a source configuration \(x_1:J_1\to S\), direct image gives \(x_2=x_1\beta\). The relation (RN.7) says \(x_1\psi_1=x_2\psi_2\alpha\). Thus regrouping the source labels along \(\alpha\) gives exactly the same label at every point of \(S\). Sums over configurations give the compatibility for arbitrary stage objects.

Here is a complete inverse, including the transition identifications. Insert the stage \(S\xrightarrow{\mathrm{id}}S\) at the configuration \(\mathrm{id}_S\), with one label for every point. Its composite with (RN.14) is the identity. Conversely, for a generator at \((\psi:I\to J,x:J\to S)\), form the intermediate stage \(x\psi:I\to S\), at configuration \(\mathrm{id}_S\). There is a span of index morphisms

\[
 (\psi:I\to J)
       \ \longleftarrow\
 (x\psi:I\to S)
       \ \longrightarrow\
 (\mathrm{id}:S\to S).
\]

For the left arrow use \(\alpha=\mathrm{id}_I\), \(\beta=x\). Its coordinate direct image takes the point \(\mathrm{id}_S\) to the point \(x\). For the right arrow use \(\alpha=x\psi\), \(\beta=\mathrm{id}_S\); its label multiplication is the inner tensor in (RN.14). Thus the two inserted objects are canonically identified in the colimit. These spans commute with stage morphisms: the configuration equality above composes the two coordinate maps, and the two successive label multiplications agree by associativity. Their longer compatibilities are those same composition and associativity coherences. The free-cell presentations extend the resulting natural isomorphisms from generators to the whole stages. This proves that the two continuous functors are inverse. Disjoint union of two presentations multiplies their labels independently at each point, so the equivalence is symmetric monoidal.

The unit is included in this argument. The configuration \(\mathrm{id}_S\) at \(\emptyset\to S\) maps both to \(\emptyset\to\emptyset\), by the map \(\emptyset\to S\) on coordinates, and to \(\mathrm{id}:S\to S\), by the map \(\emptyset\to S\) on labels. The first direct image is \(k\); the second inserts the unit at every point. Hence the empty stage gives the tensor unit under (RN.14), even though there is no twisted-arrow morphism directly from \(\emptyset\to\emptyset\) to \(\mathrm{id}:S\to S\).

For two points \(S=\{p,q\}\), the labels at the two points remain separate. For example, three input labels \(A,B,C\) at the configuration \((p,q,p)\) become \(A\otimes C\) at \(p\) and \(B\) at \(q\). They do not all become \(A\otimes B\otimes C\) at one point. Compact labels give compact objects and their duals are taken independently at the two points. This verifies geometric compact rigidity for this finite-point example, without proving it for a curve.

Properness of the coordinate projection in (RN.5) has mathematical content. On \(\mathbf A^1_k\), use right modules and write \(D=k[t]\langle\partial\rangle\), with \(\partial t-t\partial=1\). The regular right module \(D\) is compact in \(\operatorname{Mod}_D\). For \(p:\mathbf A^1\to\operatorname{Spec}k\), the left Spencer resolution of the trivial connection gives

\[
 p_*D\simeq
       [D\xrightarrow{\ u\mapsto u\partial\ }D],
       \quad\text{in degrees }-1,0,\qquad
 H^{-1}=0,\quad H^0=k[t].
 \tag{RN.15}
\]

Indeed \(D\otimes_D^{\mathrm L}k[t]\) is computed by the free left-module resolution with differential right multiplication by \(\partial\). In the PBW basis \(t^i\partial^j\), this differential sends \(t^i\partial^j\) to \(t^i\partial^{j+1}\). It is injective, and the quotient has precisely the basis \(1,t,t^2,\ldots\). The affine sheaf direct image adds no positive cohomology. A compact complex in \(\operatorname{Vect}_k\) has bounded finite-dimensional cohomology, by the finite-cell characterization with generator \(k\). Thus \(p_*D\) is not compact. The full Ran definition still makes sense on a nonproper curve; this example proves that its stage-transition compactness cannot be justified by (RN.6) there. It makes no claim that the particular Ran category for \(\mathcal C=\operatorname{Vect}\) is nonrigid.

Finally take \(\mathcal C\) to be the full category of \(\mathbf Z\)-graded complexes, with convolution of weights. Its compact objects have finite weight support and finite-dimensional bounded cohomology; their duals reverse the weights and take the ordinary complex dual. For \(S=\{p,q\}\), (RN.14) is the category of \(\mathbf Z^2\)-graded complexes. Write \(k_{(m,n)}\) for its one-dimensional weight object. The regular algebra constructed in (EP.3) is

\[
 R_{\mathcal A}
    =\bigoplus_{(m,n)\in\mathbf Z^2}
            k_{(m,n)}\boxtimes k_{(-m,-n)},\qquad
 \text{after forgetting weights: }\
 k[z_p^{\pm1},z_q^{\pm1}].
 \tag{RN.16}
\]

Each weight object has endomorphism algebra \(k\), and Hom between distinct weights is zero. These objects compactly generate: a graded complex is the sum of its weight complexes, and every complex of vector spaces is generated by shifts and colimits of \(k\). The multi-object free-module presentation (EP.1) therefore computes the coend using this generator category. Its representable bar contraction in (EP.3) gives precisely the displayed sum; passing to finite sums, cones and retracts changes the presentation, not this represented object. Tensor of the weights adds \((m,n)\), so multiplication of the corresponding basis elements is multiplication of the two independent Laurent monomials. This checks both the regular-algebra indexing and its multiplication in an actual Ran example.

The full geometric diagram is described in the freely accessible [Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky paper, §11.1 and Remark 11.1.9](https://arxiv.org/abs/2010.01906v2). Its proper-curve rigidity argument in §11.3 requires the geometric duality maps beyond the compact-generation proof above. The proofs here establish (RN.1)–(RN.16); a reference to that argument is not a substitute for the remaining duality proof.

**Exercise 3.AN.** Apply the localization construction (RN.12) in \(\operatorname{Vect}_k\) with \(\Sigma=\{k\oplus k\}\), starting from \(M_0=k\). Compute \(M_n\), the transition maps, and the colimit. Does one evaluation cofiber already produce a local object?

**Solution 3.AN.** For any complex \(M\), the evaluation source is \(M^{\oplus4}\). In matrix coordinates the evaluation is \((a,b,c,d)\mapsto a+d\), which has section \(m\mapsto(m,0,0,0)\). Its kernel is isomorphic to \(M^{\oplus3}\); a basis of the kernel is given by the three maps \(m\mapsto(0,m,0,0)\), \(m\mapsto(0,0,m,0)\), and \(m\mapsto(m,0,0,-m)\). Its cofiber is therefore \(M^{\oplus3}[1]\). The map from \(M\) to this cofiber is nullhomotopic because the evaluation is split surjective. Induction gives \(M_n=k^{\oplus3^n}[n]\), with nullhomotopic transitions. The sequential homotopy colimit is the cofiber of \(1-\mathrm{shift}\) on \(\bigoplus_n M_n\). The shift is nullhomotopic, so \(1-\mathrm{shift}\) is an equivalence and this colimit is zero. Every \(M_n\) is nonzero and has nonzero Hom from \(k\oplus k\). Thus a single cofiber is not local; the sequential construction is essential in this example.

**Exercise 3.AO.** For \(S=\{p,q\}\), start with four labels \(A,B,C,D\) at coordinates \((p,q,p,q)\). Multiply the first and third labels and the second and fourth labels along a map of label sets. Verify (RN.7) for this operation, compute the resulting two-point object, and explain the tensor unit's two-arrow presentation.

**Solution 3.AO.** Let \(I_1=J_1=\{1,2,3,4\}\), \(\psi_1=\mathrm{id}\), and \(x(1)=x(3)=p\), \(x(2)=x(4)=q\). Work first at the intermediate stage \(x:I_1\to S\), with configuration \(\mathrm{id}_S\). For its map to \(\mathrm{id}:S\to S\), take \(\alpha=x\) and \(\beta=\mathrm{id}_S\). Then \(\beta\psi_2\alpha=x=\psi_1\) at this intermediate stage, as required. The other arrow from the intermediate stage to the original stage has \(\alpha=\mathrm{id}_{I_1}\), \(\beta=x\), and its coordinate image is the original configuration. The normal form is \((A\otimes C)\otimes(B\otimes D)\) in \(\mathcal C\otimes\mathcal C\). The displayed tensor separates the two category factors. For the unit use the stage \(\emptyset\to S\) at \(\mathrm{id}_S\). Its arrow to \(\emptyset\to\emptyset\) sends this point to the point, giving \(k\); its arrow to \(S\xrightarrow{\mathrm{id}}S\) inserts \(\mathbf1_{\mathcal C}\) in both empty label fibres. This proves the unit identification using valid index morphisms.

**Exercise 3.AP.** Compute the direct image of the regular right Weyl module along \(\mathbf A^1\to\operatorname{Spec}k\) and test compactness. In the two-point graded example, compute the product of the regular-algebra basis elements indexed by \((2,-1)\) and \((-3,4)\), and their weights in the two tensor factors.

**Solution 3.AP.** The free left Spencer resolution has terms in degrees \(-1,0\) and differential right multiplication by \(\partial\). Tensoring with the regular right module gives exactly (RN.15). PBW makes the differential injective, and the cokernel \(k[t]\) has one basis element for every nonnegative power of \(t\). It is infinite-dimensional in degree zero, hence not compact in \(\operatorname{Vect}_k\). In (RN.16), the product is indexed by \((-1,3)\); its first weight is \((-1,3)\) and its second is \((1,-3)\). After forgetting weights it is \(z_p^{-1}z_q^3\). The two calculations concern different assertions: the first detects failure of a nonproper transition to preserve compacts, and the second computes multiplication in the proper finite-point Ran regular algebra.

### 3.48. Proper coherent duality and the two normalized objects

Let \(k\) be any characteristic-zero field and let \(Y/k\) be smooth projective of pure dimension \(d\). Write \(\Omega_Y=\bigwedge^d\Omega^1_{Y/k}\). All operator modules below are left modules. Write \(p:Y\to\operatorname{Spec}k\).

Use the full unbounded category \(\mathcal D(Y)\) constructed in GL-GLC-03, §§3.45–3.46. Its compacts are exactly the bounded coherent operator complexes, and \(p_*\) is continuous and preserves compacts. The proofs use finite Spencer columns and finite affine Čech totalization; their differentials need not be structure-sheaf linear.

The earlier lesson Holonomic D-modules and duality, Lemma3.0, proves finite local operator resolutions and the intrinsic bidual evaluation for all bounded coherent complexes. Its §5, equations(5.1)–(5.5), computes the dual of a connection, including the side-changing line. Consequently

\[
\mathbb D_YF=\Omega_Y^{-1}\otimes_{\mathcal O_Y}
 R\mathcal Hom_{\mathcal D_Y}(F,\mathcal D_Y)[d],
\qquad
\mathbb D_Y\mathcal O_Y=\mathcal O_Y .
\]

The Hom has a right operator action; tensoring with \(\Omega_Y^{-1}\) is the right-to-left side change. It is not an arbitrary line-bundle twist equipped with a guessed connection.

The earlier lesson Adjunctions, base change, and the projection formula, §4.1 and Theorem4.2, proves

\[
p_*\mathbb D_YF \simeq (p_*F)^\vee
\]

for every bounded coherent \(F\). For this projective structure map its proof factors through a projective embedding and the projective-product projection. The proof uses coherent direct-image Theorem3.4, finite local operator-duality bounds, projective D-affinity, the ordered residue trace and bounded dévissage. It does not assume holonomicity or the existence of a globally bounded free resolution.

In particular \(p_*F\) is a perfect \(k\)-complex. No assertion of finite-dimensionality of all operator-module mapping spaces on \(Y\) follows from this.

Set

\[
\mathbf k_Y=\mathcal O_Y[-d],
\qquad
\boldsymbol\omega_Y=\mathcal O_Y[d].
\]

For every unbounded \(Q\in\mathcal D(Y)\), there is a natural equivalence

\[
R\operatorname{Hom}_{\mathcal D(Y)}(\mathbf k_Y,Q)
 \simeq p_*Q. \tag{GD.1}
\]

Here is the full calculation, including shifts. The intrinsic Spencer resolution of \(\mathcal O_Y\) has terms
\(\mathcal D_Y\otimes_{\mathcal O_Y}\bigwedge^iT_Y\) in degrees \(-i\), \(0\le i\le d\). Its Hom into \(Q\) has coefficient terms
\(\Omega^i_{Y/k}\otimes_{\mathcal O_Y}Q\) in form degrees \(i\), with the connection and bracket differential. This is the ordinary unshifted algebraic de Rham complex. Hom out of \(\mathcal O_Y[-d]\) shifts this complex by \([d]\).

The backward transfer to the point is the right operator module \(\Omega_Y\); its right Spencer resolution, tensored with \(Q\), is exactly the same de Rham complex shifted by \([d]\), with the side-changing and exterior-order signs proved in Direct images and the relative de Rham complex, Theorem 2.1. This computes \(p_*Q\).

The resolution has finitely many Spencer degrees. A finite affine cover of the separated \(Y\) has affine intersections and finite Čech length. In both computations, compute each structure-sheaf quasi-coherent coefficient column before totalizing these two finite directions. Thus the identification applies to full unbounded \(Q\); it uses no invalid structure-sheaf linearity of the de Rham differential. Operator-module mapping descent glues the local Hom calculation. This proves(GD.1).

For every \(E\in\operatorname{Vect}_k\), tensor–Hom adjunction therefore gives

\[
R\operatorname{Hom}_{\mathcal D(Y)}(\mathbf k_Y\otimes_kE,Q)
 \simeq R\operatorname{Hom}_k(E,p_*Q). \tag{GD.2}
\]

Hence \(p^*E=\mathbf k_Y\otimes_kE\) is left adjoint to \(p_*\), in these normalized D-module conventions. This statement is about the actual full categories, not just bounded holonomic objects.

### 3.49. Full structure-map adjunctions and compact external duality

Define \(p^!E=\boldsymbol\omega_Y\otimes_kE\). Then

\[
p_*\dashv p^! \tag{GD.3}
\]

on the full unbounded categories.

First let \(F\) be compact and \(E\) a perfect \(k\)-complex. All objects to which \(\mathbb D\) is applied below are bounded coherent. Finite projective evaluation, proper duality, (GD.2) and biduality give the natural sequence

\[
\begin{aligned}
R\operatorname{Hom}_k(p_*F,E)
&\simeq R\operatorname{Hom}_k(E^\vee,(p_*F)^\vee)\\
&\simeq R\operatorname{Hom}_k(E^\vee,p_*\mathbb D_YF)\\
&\simeq R\operatorname{Hom}_{\mathcal D(Y)}
       (p^*E^\vee,\mathbb D_YF)\\
&\simeq R\operatorname{Hom}_{\mathcal D(Y)}
       (F,\mathbb D_Y(p^*E^\vee))\\
&\simeq R\operatorname{Hom}_{\mathcal D(Y)}(F,p^!E).
\end{aligned}
\tag{GD.4}
\]

The last equality uses the connection-dual calculation, reversal of shifts, and finite-dimensional tensor duality:
\(\mathbb D_Y(\mathcal O_Y[-d]\otimes_kE^\vee)
 =\mathcal O_Y[d]\otimes_kE\).

For this compact \(F\), both ends of(GD.4) preserve colimits in \(E\). On the left this follows because \(p_*F\) is perfect; on the right it follows because \(F\) is compact and \(p^!\) is tensoring by a fixed object. Every \(k\)-complex is a filtered union of finite-dimensional bounded subcomplexes: a finite list of vectors and their differentials spans such a subcomplex, and unions of finite lists are again contained in one. Thus the equivalence extends naturally to all \(E\).

For fixed arbitrary \(E\), both ends send colimits in \(F\) to limits, since \(p_*\) is continuous. The compact generators of §3.45 give the requisite presentation explicitly. Restrict the enriched Yoneda module of \(F\) to the small category of compact objects and take its representable bar resolution. Realize that bar in \(\mathcal D(Y)\). The augmentation becomes an equivalence after Hom from every compact generator: Hom commutes with the realization and the bar is the usual Yoneda resolution. The generators detect its cone, so the augmentation is an equivalence. Each term is a sum of compact objects tensored by \(k\)-complexes, hence a colimit of compacts. The two contravariant functors and their natural equivalence on compacts extend over this presentation: applying either gives the same limit of compact-level equivalences. This proves(GD.3) for every unbounded \(F\), without extending coherent Verdier duality to arbitrary unbounded objects.

The maps needed at the empty-labelled Ran stages now have exact meanings:

\[
\eta:k\longrightarrow p_*\mathbf k_Y,
\qquad
\operatorname{Tr}:p_*\boldsymbol\omega_Y\longrightarrow k .
\tag{GD.5}
\]

The first is the unit of \(p^*\dashv p_*\) at \(k\), corresponding to \(\mathrm{id}_{\mathbf k_Y}\) under(GD.2). The second is the counit of \(p_*\dashv p^!\) at \(k\), corresponding to \(\mathrm{id}_{\boldsymbol\omega_Y}\) under(GD.4). The proper-duality comparison identifies the trace with the dual of \(\eta\). In the projective-product computation this is exactly the ordered residue trace used by the earlier proper-duality theorem, including its coefficient \(+1\).

Each of these two adjunctions satisfies its own triangle identities: under its natural Hom equivalence the unit and counit are the two images of identity maps, and composing the Hom equivalence with its inverse sends an identity to itself. This establishes the structure-map triangles. The two Ran-object triangles additionally require the diagonal kernel maps and the twisted-finite-set structural spans.

For smooth projective \(Y,Z\) and bounded coherent \(F,G\), there is an intrinsic equivalence

\[
\mathbb D_{Y\times Z}(F\boxtimes G)
 \simeq \mathbb D_YF\boxtimes\mathbb D_ZG. \tag{GD.6}
\]

To prove it, take finite local projective operator resolutions on affine coordinate opens. The product operator algebra is the tensor product of the two operator algebras over \(k\), as proved in §3.45. For finite free terms, dual-Hom of their tensor product is the tensor product of the two dual-Hom terms. Split summands give the same identity for finite projectives. Totalizing the bounded resolutions with the Koszul interchange sign proves the identity for the local complexes.

The density factors satisfy
\(\Omega_{Y\times Z}=\Omega_Y\boxtimes\Omega_Z\), with \(Y\)-forms first, and dimensions add. Thus the side changes and shifts agree. Evaluation maps are intrinsic and natural in the projective resolutions, so the local identifications agree on restrictions and glue. This proof assumes neither holonomicity nor finite-dimensional global Hom.

### 3.50. Residue normalization and a nonproper obstruction

**Exercise 3.AQ.** For \(Y=\mathbf P^1_k\), compute \(p_*\mathcal O_Y\), \(p_*\mathbf k_Y\) and \(p_*\boldsymbol\omega_Y\). Identify the unit and trace of(GD.5), including the residue sign.

**Solution 3.AQ.** Use the standard two-chart cover with coordinates \(t\) and \(u=t^{-1}\). Čech Laurent monomials give \(R\Gamma(\mathcal O_Y)=k\): polynomial monomials account for the whole overlap except the common constants in degree zero. For the canonical bundle, \(du=-t^{-2}dt\). The \(t\)-chart removes \(t^m dt\) for \(m\ge0\), and the \(u\)-chart removes \(m\le-2\). There are no global canonical forms and exactly the class \(dt/t\) remains in Čech degree one. Thus \(R\Gamma(\Omega_Y)=k[-1]\).

The one-form term of the ordinary de Rham complex is in degree one. Over a field the resulting two cohomology spaces split in the derived category: choose complements to boundaries in cycles and to cycles in each cochain group; the latter complements and their images form contractible two-term complexes. After the normalized direct-image shift \([1]\), they give

\[
p_*\mathcal O_Y=k[1]\oplus k[-1],\qquad
p_*\mathbf k_Y=k\oplus k[-2],\qquad
p_*\boldsymbol\omega_Y=k[2]\oplus k.
\tag{GD.7}
\]

The unit selects the constant class in degree zero, and the trace selects the shifted top class in degree zero:

\[
\eta:1\longmapsto(1,0),\qquad
\operatorname{Tr}|_{k[2]}=0,\qquad
\operatorname{Tr}\bigl([dt/t]\bigr)=1.
\tag{GD.8}
\]

These are maps of graded complexes; the summand \(k[2]\) lies in degree \(-2\). The trace annihilates Čech boundaries because neither chart contributes the exponent \(-1\). It annihilates de Rham derivatives because a derivative with exponent \(-1\) could only arise by differentiating exponent zero, whose derivative coefficient is zero. The ordered projective trace convention of the earlier adjunction lesson fixes its sign as \(+1\). This also agrees with the dual of the constant-unit map.

![Figure3.15. The projective-line residue and its two normalized structure-map adjunctions.](figures/proper-dmodule-trace.svg)

*Figure3.15.* In the cohomology table, \(k[a]\) lies in degree \(-a\). The constant unit uses the degree-zero summand of \(p_*\mathbf k_Y\), and the proper trace uses the degree-zero summand of \(p_*\boldsymbol\omega_Y\); the other two summands have opposite shifts. The residue calculation in Solution3.AQ fixes the coefficient and sign. Solution3.AR tests all-coherent proper duality on a nonholonomic compact, and Solution3.AS gives the exact nonproper obstruction.

**Exercise 3.AR.** Let \(Y=\mathbf P^n_k\). Calculate the direct image of the compact left regular operator module and the direct image of its coherent dual. Check whether holonomicity was used.

**Solution 3.AR.** Tensoring backward transfer with the left regular module cancels the derived tensor over the operator algebra. Its remaining coefficient is \(\Omega_Y\), so the ordered projective Čech calculation of the earlier adjunction lesson gives

\[
p_*\mathcal D_Y=R\Gamma(Y,\Omega_Y)=k[-n],
\qquad
p_*\mathbb D_Y\mathcal D_Y=k[n].
\tag{GD.9}
\]

The second equality is proper coherent duality applied to the first. Locally, finite free operator duality gives

\[
\mathbb D_Y\mathcal D_Y
 =\Omega_Y^{-1}\otimes_{\mathcal O_Y}
   (\mathcal D_Y)_{\mathrm{right}}[n],
\qquad
\operatorname{Char}(\mathcal D_Y)=T^*Y.
\tag{GD.10}
\]

The first displayed tensor uses the right-to-left side change, including its derivative action. It is not a line-bundle twist of a left module with an unspecified connection. The order filtration on the left regular module has associated graded \(\mathcal O_{T^*Y}\), which proves the characteristic-support statement. For \(n>0\) the support has dimension \(2n\), so this module is nonholonomic; it is compact because it is bounded coherent. Thus(GD.9) checks the all-coherent content of proper duality. At \(n=0\) both shifts are zero, as they should be.

**Exercise 3.AS.** On \(Y=\mathbf A^1_k\), test whether the formula \(Q\mapsto\mathcal O_Y[1]\otimes_kQ\) is right adjoint to de Rham direct image on all D-modules.

**Solution 3.AS.** Write \(D=k\langle t,\partial\rangle/(\partial t-t\partial-1)\), and take the compact left regular module \(F=D\). Its backward transfer to the point is the right module \(k[t]\,dt\), and tensoring it with \(D\) leaves that module in degree zero. The trivialization \(dt\) therefore gives

\[
p_*F=k[t],\qquad
\mathbb D_YF=D[1],\qquad
p_*\mathbb D_YF=k[t][1]\not\simeq (k[t])^\vee.
\tag{GD.11}
\]

The side change uses formal adjoint \(\partial\mapsto-\partial\); the regular right module thereby becomes the regular left module. The dual \(k[t]^\vee=\operatorname{Hom}_k(k[t],k)\) is in degree zero, while \(k[t][1]\) has its nonzero cohomology in degree \(-1\).

More directly, with \(W=\mathcal O_Y[1]\), freeness of \(F\) gives

\[
R\operatorname{Hom}_k(p_*F,k)=k[t]^\vee,\qquad
R\operatorname{Hom}_{\mathcal D(Y)}(F,W)=k[t][1].
\tag{GD.12}
\]

These complexes cannot be equivalent, so the proposed right adjunction fails. The left adjunction in(GD.2) still holds: its proof was the finite Spencer calculation and did not require properness. This distinguishes the two uses of the normalized constant and dualizing objects and locates the properness requirement in(GD.4), rather than in a guessed shift.

The next geometric step uses the diagonal kernel evaluation
\(F\boxtimes\mathbb D_YF\to\Delta_*\boldsymbol\omega_Y\)
and its dual coevaluation
\(\Delta_*\mathbf k_Y\to F\boxtimes\mathbb D_YF\).
Their kernel contraction identities and the resulting Ran triangles are additional assertions beyond the two structure-map adjunctions proved here.

Further reading: [The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support](https://arxiv.org/pdf/2010.01906v2), §11.3, gives the corresponding proper Ran duality construction.

### 3.51. The full operator pairing

Let \(Y/k\) be smooth projective of pure dimension \(d\), with structure map \(p\). Keep the full unbounded D-module category and the normalized objects \(\mathbf k_Y=\mathcal O_Y[-d]\), \(\boldsymbol\omega_Y=\mathcal O_Y[d]\) from §§3.45–3.49. Write \(\mathbb D\) for coherent Verdier duality and \(\otimes^!=\Delta_Y^!\boxtimes\) for the diagonal tensor. The earlier lesson Adjunctions, base change, and the projection formula, §3, proves \(P\otimes^!Q=(P\otimes_{\mathcal O_Y}^LQ)[-d]\), with its Leibniz operator action and its dualizing unit.

**Operator pairing.** For every compact \(F\in\mathcal D(Y)\) and every full unbounded \(G\in\mathcal D(Y)\), there is a natural equivalence

\[
p_*(\mathbb D F\otimes^!G)
 \simeq R\operatorname{Hom}_{\mathcal D(Y)}(F,G).
\tag{KG.1}
\]

The pairing need not be a perfect vector complex. Even for compact \(F,G\), their diagonal tensor can fail to be coherent, so proper coherent direct image gives no finiteness assertion for this expression.

**Proof.** Work first on an affine commuting-coordinate chart and take \(F=\mathcal D_Y\). Its dual is the side change of the right regular module shifted by \([d]\). The shift \([-d]\) in the diagonal tensor cancels it. Right side change of the resulting coefficient gives the right module

\[
N=(\mathcal D_Y)_{\rm right}\otimes_{\mathcal O_Y}G,
\qquad
(a\otimes g)\cdot\xi=a\xi\otimes g-a\otimes\xi g.
\tag{KG.2}
\]

Here the structure-sheaf balancing uses right multiplication on \(a\). Moving a function across the tensor introduces the same derivative of that function on both sides, by the operator relation and the Leibniz rule. Thus the displayed action is well defined.

The right Spencer complex for the map to the point is the finite Koszul complex of the commuting right coordinate derivatives, in degrees \(-d,\ldots,0\). It has augmentation

\[
N\longrightarrow G,\qquad a\otimes g\longmapsto ag.
\tag{KG.3}
\]

Every derivative boundary maps to zero. Filter by operator order and shifted exterior degree. Its associated graded augmented complex is the polynomial Koszul resolution
\(\operatorname{Sym}(T_Y)\otimes_{\mathcal O_Y}G\to G\).
Polynomial variables are a regular sequence on a polynomial module with arbitrary coefficient module: quotienting by the preceding variables leaves a polynomial module in the remaining ones, and multiplication by the next variable is injective by uniqueness of monomial coefficients. No flatness of \(G\) over the structure sheaf is required.

A cycle has finite operator order. Lift a symbol boundary and subtract it; this lowers order, and iteration terminates at the lower filtration bound. This proves exactness for every coefficient module. For an arbitrary complex \(G\), apply the argument in each vertical degree. The augmented horizontal complex has uniformly finite length, so its exactness survives totalization even when the vertical complex is unbounded. The augmentation therefore computes the pairing as \(G\), exactly the operator Hom from the free rank-one module.

Finite sums, split finite projectives and bounded projective resolutions extend the calculation to every local perfect operator complex. Such resolutions exist for every compact \(F\) by Holonomic D-modules and duality, Lemma 3.0, and §3.45. Their operator terms are structure-sheaf flat by PBW, so they also compute the derived tensor against arbitrary \(G\).

For clarity, the signs in the finite-complex tensor–Hom comparison can be fixed before restoring the density and dimension shift. If \(P\) is a bounded finite projective operator complex, \(P^\vee=\operatorname{Hom}_{\mathcal D_Y}(P,\mathcal D_Y)\), and \(f,g,x\) are homogeneous, the comparison and bidual evaluation are

\[
\begin{gathered}
f\otimes g\longmapsto
 \bigl(x\longmapsto(-1)^{|g||x|}f(x)g\bigr),\\
d_{P^\vee}f=-(-1)^{|f|}f\,d_P,\qquad
u_P(x)(f)=(-1)^{|x||f|}f(x).
\end{gathered}
\tag{KG.4}
\]

The comparison commutes with the differential: the term involving \(f\,d_P\) has coefficient \(-(-1)^{|f|+|g||x|}\) on both sides, while the term involving \(d_Gg\) has coefficient \((-1)^{|g||x|}\), since \(f(x)\ne0\) requires \(|f|+|x|=0\). Finite projective evaluation proves it is an isomorphism term by term. It is natural for operator matrices and split summands. Restoring side change and the dimension shift gives precisely the coherent dual in §3.48; the finite Spencer contraction signs are those proved in Direct images and the relative de Rham complex, Theorem 2.1.

The augmentation \(a\otimes g\mapsto ag\) is intrinsic, so the local comparisons agree with coordinate changes and projective-resolution comparisons. Compare these natural maps of Hom/evaluation complexes before taking global sections. Operator-module mapping descent and a finite affine Čech cover then glue the maps and their inverses. This compares the actual Čech complexes; equality of local Ext classes alone would not establish equality of global derived morphisms. Both the Spencer and Čech directions have finite length, so the calculation retains full unbounded \(G\). This proves(KG.1).

### 3.52. The diagonal kernels and their contraction

We first record the relative adjunctions needed to move between two coordinates. For the projections \(\pi_1,\pi_2:Y^2\to Y\), the full categories satisfy

\[
\pi_2^*F=\mathbf k_Y\boxtimes F,\quad
\pi_2^*\dashv\pi_{2,*},\qquad
\pi_1^!F=F\boxtimes\boldsymbol\omega_Y,\quad
\pi_{1,*}\dashv\pi_1^!.
\tag{KG.5}
\]

**Proof.** Test the left adjunction on compact \(F\) and compact exterior generators \(A\boxtimes B\). Exterior-product equivalence in §3.45 identifies the mapping complex on the product with
\(R\operatorname{Hom}(\mathbf k_Y,A)\otimes_kR\operatorname{Hom}(F,B)\).
The first factor is \(p_*A\) by(GD.1). This is a perfect vector complex by proper coherent direct image. Hence the expression equals
\(R\operatorname{Hom}(F,(p_*A)\otimes_kB)\), which is the mapping complex into \(\pi_{2,*}(A\boxtimes B)\). The external-push identification is the finite Spencer–Čech Fubini comparison of §3.45.

Both expressions preserve colimits in the product target: the source is compact, while \(F\) is compact and \(\pi_{2,*}\) is continuous. Compact exterior generators generate the full product category, so their enriched bar extends the equivalence to every target. Both expressions then turn colimits in \(F\) into limits, giving the full left adjunction.

For compact source \(Q\) and compact target \(F\), coherent duality reverses this adjunction. Proper coherent duality for the projection and compact external duality identify
\(\mathbb D(\pi_1^*\mathbb D F)=\pi_1^!F\).
This gives the right adjunction on those compact objects. Extend in the target using compactness of both \(Q\) and its proper image \(\pi_{1,*}Q\), then extend in the source over its compact bar. This proves(KG.5). These are equivalences under contravariant coherent duality of categories; they do not take a vector-space dual of an arbitrary operator-module mapping complex.

Write \(\Delta:Y\hookrightarrow Y^2\). Closed adjunction, (GD.1), (KG.1) and biduality give

\[
\begin{aligned}
R\operatorname{Hom}_{\mathcal D(Y^2)}
 (\Delta_*\mathbf k_Y,F\boxtimes\mathbb D F)
&\simeq p_*\Delta^!(F\boxtimes\mathbb D F)\\
&\simeq R\operatorname{Hom}_{\mathcal D(Y)}
 (\mathbb D F,\mathbb D F).
\end{aligned}
\tag{KG.6}
\]

The closed adjunction, including its determinant and shift, is proved in the earlier adjunction lesson, Lemma 1.2. Its finite normal Koszul resolution also computes arbitrary unbounded inputs. Define \(c_F:\Delta_*\mathbf k_Y\to F\boxtimes\mathbb D F\) to be the mate of \(\mathrm{id}_{\mathbb D F}\).

All objects in the next coherent-duality calculation are compact: proper closed push preserves coherence, and exterior products of bounded coherent operator complexes are bounded coherent. Proper coherent duality for \(\Delta\) and(GD.6) give

\[
\begin{aligned}
R\operatorname{Hom}_{\mathcal D(Y^2)}
 (F\boxtimes\mathbb D F,\Delta_*\boldsymbol\omega_Y)
&\simeq R\operatorname{Hom}_{\mathcal D(Y^2)}
 (\Delta_*\mathbf k_Y,\mathbb D F\boxtimes F)\\
&\simeq R\operatorname{Hom}_{\mathcal D(Y)}(F,F).
\end{aligned}
\tag{KG.7}
\]

Define \(e_F:F\boxtimes\mathbb D F\to\Delta_*\boldsymbol\omega_Y\) to be the mate of \(\mathrm{id}_F\). These definitions retain all dual-shift, determinant and interchange signs. If \(\sigma\) swaps the factors, intrinsic biduality gives

\[
c_{\mathbb D F}=\sigma^*c_F,\qquad
e_{\mathbb D F}=\sigma^*e_F,
\quad\text{under }F\simeq\mathbb D\mathbb D F.
\tag{KG.8}
\]

To verify this, use(KG.4) on a finite homogeneous projective complex. Swapping homogeneous factors contributes its Koszul sign, and the bidual evaluation contributes the displayed sign of \(u_P\); the resulting endomorphism is the same identity on either side of(KG.6) or(KG.7). Naturality for finite operator matrices and the intrinsic density contraction glues this calculation.

For the contraction, use the two partial diagonals and their common small diagonal:

\[
i_{12}(u,v)=(u,u,v),\quad
i_{23}(u,v)=(u,v,v),\quad
j(y)=(y,y),\quad t(y)=(y,y,y).
\tag{KG.9}
\]

The square with \(j,j,i_{12},i_{23}\) is cartesian and its fibre product is the smooth \(Y\). Put \(S=\mathbf k_Y\boxtimes F\) and \(T=F\boxtimes\boldsymbol\omega_Y\). There are canonical maps

\[
a_F:S\longrightarrow j_*F,\qquad
b_F:j_*F\longrightarrow T.
\tag{KG.10}
\]

For \(b_F\), closed adjunction gives
\(R\operatorname{Hom}(j_*F,T)=R\operatorname{Hom}(F,j^!T)\),
and the normalized diagonal tensor gives \(j^!T=F\); take the mate of the identity.
For \(a_F\), dualize the compact objects and use
\(\mathbb D S=\boldsymbol\omega_Y\boxtimes\mathbb D F\),
\(\mathbb D(j_*F)=j_*\mathbb D F\),
and \(j^!(\boldsymbol\omega_Y\boxtimes\mathbb D F)=\mathbb D F\).
Its mapping complex therefore also identifies with \(R\operatorname{Hom}(F,F)\); take the identity. This defines the needed left mate on this particular input, without requiring coherence of arbitrary coherent inverse images.

Base change, proved with its composition comparisons in the earlier adjunction lesson, Theorem 2.1, now gives

\[
R\operatorname{Hom}_{\mathcal D(Y^3)}
 (i_{12,*}S,i_{23,*}T)
 \simeq R\operatorname{Hom}_{\mathcal D(Y)}(F,F).
\tag{KG.11}
\]

Indeed, transpose along \(i_{12}\), replace
\(i_{12}^!i_{23,*}T\) by \(j_*j^!T=j_*F\), and use the just-constructed left mate for \(S\). Only bounded quasi-coherent complexes are needed in this base-change step.

**Kernel contraction.** With the bidual identification in(KG.8), the following two maps are equal:

\[
\begin{aligned}
(\mathrm{id}_F\boxtimes e_{\mathbb D F})
 \circ(c_F\boxtimes\mathrm{id}_F)
&=(i_{23,*}b_F)\circ(i_{12,*}a_F):\\
i_{12,*}S&\longrightarrow i_{23,*}T.
\end{aligned}
\tag{KG.12}
\]

The right-hand route factors through \(t_*F\). The identity is in the three-coordinate D-module category, before forgetting any coefficient-labelled coordinate.

**Proof.** Compute the transpose under(KG.11) on the finite operator Hom complexes used to prove(KG.1). More generally let \(c_\alpha\) be the mate in(KG.6) of an endomorphism \(\alpha\) of \(\mathbb D F\). Tensor–Hom evaluation of the middle coefficient gives

\[
\text{transpose of }
(\mathrm{id}_F\boxtimes e_{\mathbb D F})
\circ(c_\alpha\boxtimes\mathrm{id}_F)
 =\mathbb D(\alpha)
\quad\text{on }F\simeq\mathbb D\mathbb D F.
\tag{KG.13}
\]

Here is the coefficient computation. The Spencer augmentation is exactly \(a\otimes g\mapsto ag\), so its finite projective Hom transpose is ordinary operator evaluation. For a finite free module an endomorphism of its right module dual is a matrix acting on the left of its right-module coordinates. Dual evaluation turns it into the transposed matrix acting on the right of the original left-module coordinates. For the identity matrix the contraction coefficient is
\(\sum_b\delta_{ab}\delta_{bc}=\delta_{ac}\).
For a split finite projective module restrict this same equality to its split summand.

For a bounded projective complex, use the differential and bidual map in(KG.4). On homogeneous cochains the tensor–Hom rule is

\[
(\phi_1\otimes\phi_2)(p_1\otimes p_2)
=(-1)^{|p_1||\phi_2|}
 \phi_1(p_1)\phi_2(p_2).
\tag{KG.14}
\]

This is precisely the interchange sign in the graded transpose. Together with(KG.4), it proves(KG.13) as an equality of natural DG Hom/evaluation maps, compatible with their differentials, restrictions and resolution comparisons. Applying the signed inverse-image and closed-adjunction maps performs the same coefficient contraction in the two independent normal-coordinate blocks.

For completeness, their signs can be retained explicitly. Order \(c\) normal coordinates, write \(e_J\) for the normal Koszul wedge in degree \(-|J|\), \(f_I\) for its Hom dual, and \(s(I)=\sum_{i\in I}i\). In the notation of the earlier closed-adjunction proof the actual coefficient and normal proper-dual maps are

\[
\begin{gathered}
T(f_I)=(-1)^{s(I)+c|I|-|I|(|I|-1)/2}
 e_{I^c}\otimes\det(\mathcal I/\mathcal I^2)^{-1},\\
H(e_J)=(-1)^{s(J)+|J|(|J|+1)/2}f_{J^c},\\
\rho^{\rm normal}=\varepsilon_cH,\qquad
\varepsilon_c=(-1)^{c(c-1)/2}.
\end{gathered}
\tag{KG.15}
\]

The backward-transfer density cancels the inverse determinant in \(T\). Its top coefficient alone is positive, while the actual ordered closed counit has coefficient \(\varepsilon_c\). Both factors are required. Here is the chain-map check in every codimension. Put \(n=|I|\), let \(j\notin I\), and let \(\ell\) count the elements of \(I\) smaller than \(j\). The Hom differential inserts \(j\) with exponent \(n+\ell+1\). The exponent of \(T\) changes by \(j+c-n\), so the composite exponent is the old exponent plus \(\ell+1+j+c\). The shifted complementary Koszul differential has exponent \(c+j-1-\ell\). The difference is \(2\ell+2\), which is even.

For \(H\), put \(m=|J|\), take \(j\in J\), and let \(\ell\) count the elements of \(J\) smaller than \(j\). Removing \(j\) changes its exponent by \(-j-m\), so applying \(H\) after the Koszul differential gives the old exponent plus \(\ell-j-m\). The proper-dual differential on the complementary wedge has exponent \(2c-m+j-\ell\). Their difference is \(2(\ell-j-c)\), again even. The top coefficients of both \(T\) and \(H\) are \(+1\), since their exponents there equal \(c(c+1)\). These calculations prove the coefficient chain identities; the intrinsic backward-transfer density and determinant contraction make them invariant under changes of ordered normal coordinates.

When two normal blocks of lengths \(r,s\) compose, the tensor–Hom rule gives

\[
\varepsilon_r\varepsilon_s(-1)^{rs}
 =(-1)^{(r+s)(r+s-1)/2}
 =\varepsilon_{r+s}.
\tag{KG.16}
\]

Both routes in(KG.12), and the base-change comparison between them, use this same ordered counit. Therefore their signed normal and density contractions agree. This supplies(KG.13) with the actual closed transfer comparisons, rather than a separately chosen endpoint duality. The coefficient calculation is natural before derived global sections, so its coherent Čech descent gives the global identity of morphisms; checking local cohomology classes alone would not suffice.

For \(\alpha=\mathrm{id}_{\mathbb D F}\), the transpose in(KG.13) is \(\mathrm{id}_F\). By their definition, \(a_F,b_F\) give the same identity under(KG.11). That comparison is an equivalence, so the two maps in(KG.12) are equal. This proves the contraction.

The two outside maps also cancel with their exact adjunction meanings. Since \(\pi_2j=\pi_1j=\mathrm{id}_Y\), the product unit and the left mate in(KG.10) give

\[
F\xrightarrow{\eta_{\pi_2}}\pi_{2,*}\pi_2^*F
 \xrightarrow{\pi_{2,*}a_F}\pi_{2,*}j_*F=F
 =\mathrm{id}_F .
\tag{KG.17}
\]

To check it, transpose under the left product adjunction and the restricted closed adjunction defining \(a_F\). The transpose is the identity for the identity composite on \(F\). Under exterior-product pushforward the first arrow is \(k\to p_*\mathbf k_Y\), tensored with \(F\).

Likewise the closed and proper product counits give

\[
F=\pi_{1,*}j_*F
 \xrightarrow{\pi_{1,*}b_F}\pi_{1,*}\pi_1^!F
 \xrightarrow{\varepsilon_{\pi_1}}F
 =\mathrm{id}_F .
\tag{KG.18}
\]

This is the counit of the composite adjunction
\(\pi_{1,*}j_*\dashv j^!\pi_1^!\), identified with the identity adjunction on \(F\). Under exterior-product pushforward the last arrow is the proper trace \(p_*\boldsymbol\omega_Y\to k\), tensored with \(F\). Thus a section followed by its projection has normalized coefficient \(+1\). This statement retains the ordered normal signs in(KG.15); it does not replace the raw higher-codimension counit coefficient by \(+1\).

### 3.53. Compact rigidity of the actual D-module Ran category

Return to the actual category \(\mathcal R=\mathcal C_{\operatorname{Ran}}\) constructed in §§3.45–3.47. Here \(X/k\) is a smooth projective curve over any characteristic-zero field. The specified symmetric monoidal coefficient category \(\mathcal C\) has compact unit and dualizable compact generators. Its tensor-power compact objects are therefore dualizable: pure exterior compact generators have their componentwise duals, and finite cofibers, sums and split retracts preserve duals by the tensor-adjunction argument below.

For \(\psi:I\to J\), put \(Y=X^J\), \(V\in(\mathcal C^{\otimes I})^c\), and \(F\in\mathcal D(Y)^c\). The dual of its inserted compact generator is

\[
A=\operatorname{ins}_{\psi}(V\otimes F),
\qquad
A^\vee=\operatorname{ins}_{\psi}
 (V^\vee\otimes\mathbb D_YF).
\tag{KG.19}
\]

We construct the two maps and prove both triangles, rather than inferring rigidity from compact generation.

Write \(\psi^{(2)}=\psi\sqcup\psi:I\sqcup I\to J\sqcup J\), and let \(\psi^{\Delta}:I\sqcup I\to J\) apply \(\psi\) on both copies. Evaluation is the composite

\[
\begin{aligned}
A\circledast A^\vee
&=\operatorname{ins}_{\psi^{(2)}}
 ((V\boxtimes V^\vee)\otimes(F\boxtimes\mathbb D F))\\
&\longrightarrow
 \operatorname{ins}_{\psi^{(2)}}
 ((V\boxtimes V^\vee)\otimes\Delta_*\boldsymbol\omega_Y)\\
&\simeq
 \operatorname{ins}_{\psi^\Delta}
 ((V\boxtimes V^\vee)\otimes\boldsymbol\omega_Y)\\
&\simeq
 \operatorname{ins}_{\psi}
 ((V\otimes V^\vee)\otimes\boldsymbol\omega_Y)\\
&\longrightarrow
 \operatorname{ins}_{\psi}
 (\mathbf1_{\mathcal C^{\otimes I}}\otimes\boldsymbol\omega_Y)\\
&\simeq
 \operatorname{ins}_{\emptyset\to J}
 (k\otimes\boldsymbol\omega_Y)\\
&\simeq
 \mathbf1_{\mathcal R}\otimes_kp_*\boldsymbol\omega_Y
 \longrightarrow\mathbf1_{\mathcal R}.
\end{aligned}
\tag{KG.20}
\]

The first arrow is \(e_F\), the second arrow is coefficient evaluation, and the last is the proper trace of(GD.5). The geometric structural equivalence uses \(\alpha=\mathrm{id}_{I\sqcup I}\) and the fold \(\beta:J\sqcup J\to J\); its coordinate map is \(\Delta_Y\). The next equivalence uses the coefficient fold \(\alpha:I\sqcup I\to I\) and \(\beta=\mathrm{id}_J\). The unit-label insertion uses \(\emptyset\to I\). The final empty-labelled transition uses \(\beta:\emptyset\to J\), whose coordinate map is \(p:Y\to\mathrm{pt}\). These are exactly morphisms satisfying \(\psi_{\rm source}=\beta\psi_{\rm target}\alpha\) in the actual twisted-finite-set diagram.

Coevaluation uses the constant-object unit and the coefficient coevaluation in the folded coefficient category:

\[
\begin{aligned}
\mathbf1_{\mathcal R}
&\longrightarrow\mathbf1_{\mathcal R}\otimes_kp_*\mathbf k_Y\\
&\simeq\operatorname{ins}_{\emptyset\to J}(k\otimes\mathbf k_Y)\\
&\simeq\operatorname{ins}_{\psi}
 (\mathbf1_{\mathcal C^{\otimes I}}\otimes\mathbf k_Y)\\
&\longrightarrow\operatorname{ins}_{\psi}
 ((V\otimes V^\vee)\otimes\mathbf k_Y)\\
&\simeq\operatorname{ins}_{\psi^\Delta}
 ((V\boxtimes V^\vee)\otimes\mathbf k_Y)\\
&\simeq\operatorname{ins}_{\psi^{(2)}}
 ((V\boxtimes V^\vee)\otimes\Delta_*\mathbf k_Y)\\
&\longrightarrow\operatorname{ins}_{\psi^{(2)}}
 ((V\boxtimes V^\vee)\otimes(F\boxtimes\mathbb D F))\\
&=A\circledast A^\vee .
\end{aligned}
\tag{KG.21}
\]

The last arrow is \(c_F\). Proper coherent duality identifies \(\Delta_*\mathbf k_Y\) with its compact !-direct image, so no additional nonholonomic !-pushforward is being assumed. Coefficient coevaluation is taken in \(\mathcal C^{\otimes I}\); it is not a map from the unit into \(V\boxtimes V^\vee\) in two independent coefficient categories.

For the first triangle, expand these maps on three coordinate copies and retain the corresponding three coefficient-label copies. Between the coefficient coevaluation and evaluation, the coefficient object is the fixed exterior object \(V\boxtimes V^\vee\boxtimes V\). Its geometric composite is exactly the left side of(KG.12), with the symmetric duality convention in(KG.8). Tensor(KG.12) by this fixed coefficient object and apply the insertion functor. The equality is valid before the colimit localization.

Replace that composite by the route through \(t_*F\) on the right side of(KG.12). The small diagonal makes all three coordinate copies equal. The actual structural equivalence for the fold \(J\sqcup J\sqcup J\to J\) now identifies this inserted object with the stage \(I\sqcup I\sqcup I\to J\). At that stage the three copies of each coefficient label have the same coordinate, so the coefficient fold \(I\sqcup I\sqcup I\to I\) is allowed.

This also checks compatibility with the two earlier folds. Folding the first two copies and then the result with the third, or folding the last two and then with the first, gives the same set map from three copies to one. Their coordinate folds give the same small diagonal. The coherent composition comparisons in the actual diagram of §3.45 therefore identify these paths with the common threefold fold; its coefficient map is ordinary associativity and symmetry in \(\mathcal C^{\otimes I}\). Thus the coefficient composite is its \(V,V^\vee,V\) triangle and equals \(\mathrm{id}_V\).

The outside geometric maps are now precisely the section–projection maps(KG.17) and(KG.18). The first is the constant unit tensored with \(F\), followed by \(a_F\); the second is \(b_F\), followed by the proper trace tensored with \(F\). Both are identities. Consequently the full first Ran triangle is \(\mathrm{id}_A\). This argument keeps the middle coefficient label until the small-diagonal comparison; forgetting that coordinate earlier would not prove this triangle.

For the second triangle repeat the same calculation with \(V^\vee,\mathbb D F\). Intrinsic coefficient biduality and(KG.8) identify its maps with the symmetric versions of(KG.20) and(KG.21). The coefficient triangle is \(\mathrm{id}_{V^\vee}\), the kernel transpose is \(\mathrm{id}_{\mathbb D F}\), and both section–projection maps are identities. It therefore gives \(\mathrm{id}_{A^\vee}\), retaining the graded braiding signs. This proves(KG.19) for every inserted compact generator, without imposing holonomicity on \(F\).

The following tensor-adjunction calculation completes the passage from generators to all compacts:

\[
\begin{gathered}
\bigl(\operatorname{cofib}(U\to W)\bigr)^\vee
 =\operatorname{fib}(W^\vee\to U^\vee),\\
R\operatorname{Hom}_{\mathcal R}(B,T)
 =R\operatorname{Hom}_{\mathcal R}
 (\mathbf1_{\mathcal R},B^\vee\circledast T)
 \quad(B\text{ dualizable}).
\end{gathered}
\tag{KG.22}
\]

For the first identity, apply Hom to the cofiber after tensoring by an arbitrary object. The resulting fibre of the two Hom complexes equals Hom into the displayed fibre of the reversed dual map, tensored with the target. Tensor is exact, so this supplies the dual adjunction and its unit/counit. Finite sums follow in the same way. A split retract has the reversed split retract of the dual, and its two triangles restrict to that summand.

By §3.46 the actual Ran compacts are the thick closure of the inserted compact generators, so they are all dualizable. Conversely, the second line of(KG.22) and compactness of the unit show that every dualizable object is compact, since tensoring with its dual is continuous. Therefore the actual full D-module Ran category is rigid, and its compact objects are exactly its dualizable objects.

These constructions also specify duality across the original diagram: coefficient folds preserve duals as strong symmetric monoidal functors, and proper coherent duality identifies the dual of a coordinate direct image with the direct image of the dual. Their composition comparisons are the signed adjunction comparisons already used above. Thus stage presentations give compatible duals; alternatively, any two duals are canonically identified by composing their units and counits, whose triangles make those comparison maps inverse.

The regular-algebra construction of §3.42 now applies to this actual rigid category. If \(\mu:\mathcal R\otimes\mathcal R\to\mathcal R\) is multiplication and \(r\) its right adjoint, its regular commutative algebra is

\[
R_{\mathcal R}=r(\mathbf1_{\mathcal R})
 \simeq\int^{B\in\mathcal R^c}B^\vee\boxtimes B.
\tag{KG.23}
\]

All hypotheses of that earlier proof are now supplied: the actual category is compactly generated, its unit is compact, and its compacts are monoidally dualizable. The coend uses the whole compact DG category, including its finite cones, retracts and coherent localization morphisms. It is not a coend over only the underlying set of inserted generators. The proof in §3.42 constructs its multiplication and unit, proves the projection formula and identifies it with \(r(\mathbf1)\), so(KG.23) supplies the actual Ran regular algebra. Constructing its geometric Hecke action and spectral coefficient functor, and identifying its nilpotent regular image, remain separate geometric assertions.

### 3.54. Graded signs, a nonholonomic pairing and the common diagonal

**Exercise 3.AT.** At the empty stage, let \(A_m=\mathbf1_{\mathcal R}[m]\) and \(B_m=\mathbf1_{\mathcal R}[-m]\). Compute coevaluation, reversed evaluation and both triangle signs.

**Solution 3.AT.** Model the two shifts by homogeneous generators \(e,e^\vee\) of degrees \(-m,m\). The ordinary evaluation \(e^\vee\otimes e\mapsto1\) has no interchange sign. In the order used in(KG.20) and(KG.21),

\[
\operatorname{coev}(1)=e\otimes e^\vee,\qquad
\operatorname{ev}(e\otimes e^\vee)=(-1)^m,\qquad
\operatorname{braid}(e^\vee\otimes e)=(-1)^m e\otimes e^\vee.
\tag{KG.24}
\]

The first triangle contracts the last two factors in \(e\otimes e^\vee\otimes e\). Swapping them contributes \((-1)^m\), and reversed evaluation contributes another \((-1)^m\); their product is \(+1\). For the second triangle, swapping the coevaluation to \(e^\vee\otimes e\) supplies the first factor, and reversed evaluation supplies the second. It too is \(+1\). Omitting the graded braiding would give \(-1\) for odd \(m\), contradicting the triangle. At this stage \(Y=\mathrm{pt}\), so all geometric constant/dualizing shifts are zero; these are actual unit shifts in the curve Ran category.

**Exercise 3.AU.** In the local proof of(KG.1), take \(F=D_{\mathbf A^1}\) and \(G=\mathcal O_{\mathbf A^1}e^{at}\), for arbitrary \(a\in k\). Calculate the right Spencer complex and its augmentation without assuming a finite-dimensional underlying vector space.

**Solution 3.AU.** As a right \(k[t]\)-module, the Weyl algebra has PBW basis \(1,\partial,\partial^2,\ldots\). Identify its right tensor with \(G\) with \(k[t,z]e\), where \(z^nf(t)e\) represents \(\partial^n\otimes f(t)e\). Formula(KG.2) gives

\[
\begin{gathered}
\bigl[k[t,z]e\xrightarrow{\rho}k[t,z]e\bigr],
\quad \rho=z-(\partial_t+a),
\quad\text{degrees }-1,0,\\
z^nf(t)e\longmapsto(\partial_t+a)^nf(t)e
 \quad\text{under the augmentation}.
\end{gathered}
\tag{KG.25}
\]

Indeed \(\partial(f(t)e)=(f'(t)+af(t))e\), and right multiplication by \(\partial\) on the PBW basis increases its index. The leading \(z\)-degree of \(\rho h\) is one higher than that of any nonzero finite polynomial \(h\); thus \(\rho\) is injective. Modulo its image, reduce every \(z^nf\) to \((\partial_t+a)^nf\) by descending \(z\)-degree. The augmentation kills each relation and is the identity on the degree-zero representative \(f(t)e\), proving that the cokernel is exactly \(k[t]e\).

For example, with \(a=2,n=2,f=t^2\),

\[
(\partial_t+2)t^2=2t^2+2t,\qquad
(\partial_t+2)^2t^2=4t^2+8t+2.
\tag{KG.26}
\]

This is the operator Hom from the nonholonomic free module \(D_{\mathbf A^1}\) to \(G\). In the pairing, the dual shift \([1]\) and diagonal-tensor shift \([-1]\) cancel before taking this Spencer complex. Its exactness uses finite polynomial degree, while its cokernel remains infinite-dimensional over \(k\); no finite-rank vector-space dual has been substituted for coherent operator duality.

**Exercise 3.AV.** In the affine polynomial model for a single curve coordinate, describe the two partial diagonals inside three coordinates and compute the transverse-normal Hom degrees for \(F=\mathcal O\). Retain the ordered normal counit sign.

**Solution 3.AV.** On the polynomial model \(\mathbf A^3_k\), use base coordinate first and normal coordinates next:

\[
z=t_2,\quad a=t_2-t_1,\quad b=t_3-t_2,
\qquad
t_1=z-a,\quad t_2=z,\quad t_3=z+b,
\qquad \det=+1.
\tag{KG.27}
\]

The matrix of this coordinate change, with rows \(z,a,b\), is
\(\left(\begin{smallmatrix}0&1&0\\-1&1&0\\0&-1&1\end{smallmatrix}\right)\), whose determinant is \(1\). Thus \(i_{12}\) is \(a=0\), \(i_{23}\) is \(b=0\), and their common small diagonal is \(a=b=0\). The independent normal equations form the corresponding two-step regular sequence.

Write \(\delta_a=D_a/D_aa\) and \(\delta_b=D_b/D_bb\). Applying Hom from the free resolution \(D_a\xrightarrow{\,\cdot a\,}D_a\) into \(\mathcal O_a\) gives multiplication by \(a\), whose kernel is zero and whose cokernel is \(k\) in degree one. Applying Hom from \(D_b\xrightarrow{\,\cdot\partial_b\,}D_b\) into \(\delta_b=k[\partial_b]\delta_b\) gives multiplication by \(\partial_b\), again injective with cokernel \(k\) in degree one. Therefore

\[
R\operatorname{Hom}_{D_a}(\delta_a,\mathcal O_a)=k[-1],
\qquad
R\operatorname{Hom}_{D_b}(\mathcal O_b,\delta_b)=k[-1].
\tag{KG.28}
\]

In the tangential direction, the Hom from \(\mathcal O_z\) to itself is the polynomial de Rham complex \(k[z]\xrightarrow{d/dz}k[z]dz\). Characteristic zero makes its derivative surjective, with kernel \(k\). The tensor of the two transverse Hom complexes is thus \(k[-2]\). The source \(i_{12,*}S\) has the constant shift \([-1]\), and the target \(i_{23,*}T\) has the dualizing shift \([1]\); their mapping shift is \(+2\). It cancels the transverse \([-2]\), leaving the degree-zero tangential identity in(KG.11).

The raw ordered tensor–Hom counit for the two normal directions and its comparison coefficient are

\[
\varepsilon_2=-1,\qquad
\varepsilon_1\varepsilon_1(-1)^{1\cdot1}=-1,
\qquad
\frac{\text{composite ordered coefficient}}
      {\text{small-diagonal ordered coefficient}}=1.
\tag{KG.29}
\]

Both routes use the same ordered normal density and counit. Their normalized endomorphism coefficient is therefore \(+1\), as(KG.12) asserts. The raw top coefficient \(-1\) has not been discarded.

![Figure 3.16. Two partial diagonals meet on the small diagonal, where both coordinate and coefficient contractions become the original object.](figures/ran-duality-triangles.svg)

*Figure 3.16.* The upper panel shows the exact one-coordinate linear equations of Solution 3.AV; the projected real cube only illustrates these equations. The middle panel is the equality of actual D-module kernel maps in(KG.12). The lower panel follows its small-diagonal factor through the two projection adjunctions(KG.17)–(KG.18) and the coefficient-category triangle. The full proof applies one such normal block to every coordinate of \(Y=X^J\), with the ordered higher-codimension signs(KG.15)–(KG.16).

Further reading: [The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support](https://arxiv.org/pdf/2010.01906v2), §11.3 and Remark 11.3.8, gives the proper Ran duality construction and its full D-module form.

### 3.55. Riemann–Hilbert on the full chartwise ind-regular category

In §§3.55–3.58 the ground and coefficient field is \(\mathbf C\). Regularity is algebraic regularity, including every point at infinity on a curve test. Let \(U\) be a smooth separated finite-type complex variety, and use DG categories with their full derived mapping complexes. Put

\[
 \begin{gathered}
 \mathscr R(U)=D^b_{\mathrm{rh}}(\mathcal D_U),\qquad
 \mathscr B(U)=D^b_{c,\mathrm{alg}}(U^{\mathrm{an}},\mathbf C),\\
 \mathscr R_\infty(U)=\operatorname{Ind}\mathscr R(U),\qquad
 \mathscr B_\infty(U)=\operatorname{Ind}\mathscr B(U).
 \end{gathered}
 \tag{RH.1}
\]

The bounded categories are idempotent complete: a retract has retract cohomology and hence retains boundedness, regular holonomicity, or finite algebraic constructibility, respectively. A small skeleton fixes the size of each ind-completion. The right-hand category is the ind-completion of the **full derived sheaf category** in the first line. It is not formed by deriving an abelian category of local systems.

Here the required general theorem has a complete earlier proof. The Riemann–Hilbert correspondence, §1, Theorems 1.2–1.23 proves the following, for all these varieties, arbitrary singular supports, and every bounded degree:

\[
 \operatorname{DR}_U:\mathscr R(U)\xrightarrow{\sim}\mathscr B(U),
 \qquad
 \operatorname{DR}_U(\mathcal O_U)=\mathbf C_U[d_U].
 \tag{RH.2}
\]

Its proof is useful here because it retains the actual functor. Finite generation by regular connection standards and the SNC comparison prove the direct-image map. Finite Spencer resolves the Hom connection and compares **all** its higher morphisms with the sheaf Hom complex. Two supported approximation functors then reduce the higher-Hom assertion to lower-dimensional supports. Essential surjectivity lifts the actual connecting morphism of a support-localization triangle, after full faithfulness has been proved. Theorems 1.12–1.13 therefore supply the map of derived Hom complexes and its inverse, including the attaching data; an equivalence of hearts is not their replacement. The subsequent evaluation and transfer calculations prove the four-map comparisons and their compositions. These are the earlier proofs used below.

**Proposition.** Ind-extension of this actual functor is an equivalence

\[
 \operatorname{DR}^{\mathrm{ind}}_U:
 \mathscr R_\infty(U)\xrightarrow{\sim}\mathscr B_\infty(U).
 \tag{RH.3}
\]

For an algebraic map \(f:U\to V\) between varieties in this scope it comes with the coherent comparison

\[
 \beta_f^{\mathrm{ind}}:
 \operatorname{DR}^{\mathrm{ind}}_U f^!
 \xrightarrow{\sim}
 f^{\mathrm{an},!}_{\mathrm{ind}}\operatorname{DR}^{\mathrm{ind}}_V.
 \tag{RH.4}
\]

The sheaf functor in (RH.4) means ind-extension of its bounded constructible functor. On an affine chart, the left category embeds fully faithfully in the full unbounded \(\operatorname{Dmod}(U)\), and its \(f^!\) is the restriction of the full algebraic functor.

**Proof.** In the actual DG de Rham model, the map on each mapping complex is the map whose degree-\(r\) cohomology is Theorem 1.12's map, for every integer \(r\). Thus it is a quasi-isomorphism. Theorem 1.13 supplies all target objects. This proves DG equivalence, rather than only an equivalence on degree-zero morphisms.

Ind-extension can be checked directly. Write \(M=\mathop{\mathrm{colim}}_i M_i\) and \(N=\mathop{\mathrm{colim}}_j N_j\) as filtered ind-objects, with \(M_i,N_j\) in the small category. Its defining mapping complex is

\[
 \operatorname{RHom}_{\operatorname{Ind}\mathscr R(U)}(M,N)
 =
 \lim_i\mathop{\mathrm{colim}}_j
 \operatorname{RHom}_{\mathscr R(U)}(M_i,N_j).
 \tag{RH.5}
\]

Applying the quasi-isomorphisms in (RH.2) to this entire diagram gives the same formula for the target ind-objects. Limits here are derived limits. Essential surjectivity follows by lifting the filtered diagram along the DG equivalence, including its arrows and coherent relations. Alternatively ind-extend a DG inverse and its two inverse equivalences. Both arguments prove (RH.3) with all unbounded ind-diagrams retained.

We justify the asserted affine embedding. The complete finite-operator resolution proof in Holonomic D-modules and duality, §§2–3 gives a finite locally projective operator resolution for every bounded coherent input. Such an input is compact in the full unbounded affine D-module category. One may verify compactness on a finite affine refinement on which that resolution is finite projective. Restrict the second input to the finite ordered cover and use the augmented Čech resolution of §3.45, with the open restriction/direct adjunction. The resulting mapping complex is a finite totalization of the local finite-projective Hom complexes. Intersections stay affine by separatedness. Each local Hom commutes with filtered colimits; finite totalization does too. The finite locally projective resolutions can be further restricted to the intersections. This proves compactness without a bound on the second input. The argument applies to every bounded regular holonomic input.

Consequently the functor from \(\operatorname{Ind}\mathscr R(U)\) to full \(\operatorname{Dmod}(U)\) is fully faithful: compactness gives the inner colimit in (RH.5), and mapping out of the first colimit gives its outer limit. Its essential image is precisely the ind-generated regular subcategory. This assertion does not replace ind-generation by a condition merely on the cohomology modules of an arbitrary unbounded complex.

On bounded inputs the actual \(f^!\) preserves regular holonomicity by the earlier four-map theorem used in (RH.2). The full \(f^!\) is continuous by the unbounded transfer construction of §§1.10–1.12: its coefficient tensor, the finite Spencer directions, and restrictions commute with colimits. It therefore agrees on ind-generated inputs with ind-extension of its bounded restriction. Theorem 1.20 of the RH lesson supplies the actual map \(\beta_f\), preserving units, counits and composition. Ind-extension gives (RH.4) and the same identities on all objects.

For precision, the higher coherence is retained as well. The direct comparison is restriction of coefficient complexes followed by the ordered Spencer augmentation; refinements give the same derived comparison. Its inverse-image comparisons are constructed from the evaluation maps and enriched adjunction mates. The mapping-complex adjunction is natural in the full complexes; the space of a right adjoint with specified adjunction data is contractible, since the representing mapping functor fixes it by enriched Yoneda. Thus the same mates for a string of maps compose coherently, with the derived associativity of the transfer tensors. Ind-extension preserves those transformations and their homotopies. This constructs a comparison of the descent diagrams, not a list of unrelated object isomorphisms. ∎

The normalization in (RH.4) must be retained. On a smooth map of relative complex dimension \(r\), with flat connection coefficients in the positive untwisted local frames, the earlier signed-chain proof gives

\[
 \begin{gathered}
 q_U=(2\pi i)^{-d_U},\qquad
 \beta_f=(2\pi i)^{-r}\operatorname{id},\\
 \operatorname{DR}_U(f^!\mathcal O_V)
   \simeq\mathbf C_U[d_V+2r]
   \simeq f^{\mathrm{an},!}\mathbf C_V[d_V].
 \end{gathered}
 \tag{RH.6}
\]

The middle coefficient is a value **in these frames**, not a formula for an arbitrary complex or a replacement for its transfer map. On a smooth closed map of codimension \(c\), the corresponding normal coefficient is \((2\pi i)^c\). The residue-one algebraic trace and the positive analytic period fix these values; see the RH lesson's Theorem 1.14 and signed chain identifications (1.vak)–(1.val). In particular using a raw flat-frame identity for every extraordinary comparison would lose the trace normalization.

### 3.56. Descent after ind-completion

Let \(Y\) be a smooth locally finite-type complex algebraic stack with the smooth affine-chart descent construction of §§1.10–1.12. The application is \(Y=\operatorname{Bun}_G\), for every connected reductive complex \(G\), every genus and every component. The bundle-stack atlas and its affine finite-presentation diagonal are proved in Lesson 2. Its fibre products of finite-type affine chart members are affine, smooth and finite type, so the same comparison applies to their nerves and refinements. An infinite cover is kept as a family of such members, not regarded as one finite-type variety.

Write \(\mathcal I_Y\) for the homotopy-coherent diagram of **all** smooth finite-type affine charts over \(Y\), with their maps, stack arrows and \(f^!\)-transitions. This is the smooth-chart limit description of the full D-module category in §1; it is not a limit over only the field-valued points. Define

\[
 \begin{gathered}
 \operatorname{Dmod}_{\mathrm{ind-rh}}(Y)
   =\lim_{\mathcal I_Y}\mathscr R_\infty(U),\\
 \operatorname{Shv}^{\mathrm{Betti,constr}}(Y;\mathbf C)
   =\lim_{\mathcal I_Y}\mathscr B_\infty(U).
 \end{gathered}
 \tag{RH.7}
\]

The first line is a full subcategory of \(\operatorname{Dmod}(Y)\): its objects are exactly the Cartesian D-modules whose chart restrictions belong to the affine ind-generated regular subcategories. The second line specifies the chartwise ind-constructible Betti theory. It makes no assertion that this limit is the category of all unbounded analytic sheaves.

**Theorem.** The actual comparisons (RH.4) give

\[
 \operatorname{DR}^{\mathrm{ind}}_Y:
 \operatorname{Dmod}_{\mathrm{ind-rh}}(Y)
 \xrightarrow{\sim}
 \operatorname{Shv}^{\mathrm{Betti,constr}}(Y;\mathbf C).
 \tag{RH.8}
\]

No global boundedness, finite atlas, or global compactness hypothesis on an object is required.

**Proof.** The affine inclusions proved above are fully faithful. A limit of these inclusions is fully faithful. Explicitly a mapping complex between Cartesian objects is the homotopy-coherent end of the chart mapping complexes: resolve that end by its cosimplicial replacement and take its derived totalization. Inserting fully faithful mapping comparisons in each component gives an equivalence of these ends. Its objects are just those descent objects whose components lie in the given full subcategories. This proves the assertion about the first line of (RH.7).

Now take a Cartesian family \(M_U\) in that line. For an arrow \(f:U\to V\), its specified isomorphism \(f^!M_V\to M_U\), composed with the inverse of (RH.4), gives

\[
 f^{\mathrm{an},!}_{\mathrm{ind}}
       \operatorname{DR}^{\mathrm{ind}}_V M_V
 \xrightarrow{(\beta_f^{\mathrm{ind}})^{-1}}
 \operatorname{DR}^{\mathrm{ind}}_U f^!M_V
 \longrightarrow\operatorname{DR}^{\mathrm{ind}}_U M_U.
 \tag{RH.9}
\]

Composition and the higher relations hold because they hold for the original family and for the diagram comparison in (RH.4). This gives the actual functor in (RH.8). On mapping ends it is a componentwise quasi-isomorphism, hence fully faithful.

For essential surjectivity choose the inverse DG equivalences in (RH.3). Conjugate every transition of a Betti family by those inverses and by (RH.4). The unit and counit of the equivalences carry each coherent simplex of its descent data to the corresponding coherent simplex on the operator side. They supply a Cartesian lift and the two inverse comparisons. Equivalently, limits preserve equivalences of diagrams: the constructed inverse diagrams and their unit/counit transformations remain inverse after taking the limit. This proves (RH.8).

The limit uses all smooth charts, so its definition is independent of an atlas choice. The comparison applies to every chart of an atlas, every member of its nerve, and every refinement, with their actual arrows. No step discards the other charts from the full diagram or infers ind-generation on a chart merely from its smooth pullbacks. Computing this ind-category from a single atlas alone would require that additional descent statement; it is not needed for the intrinsic chartwise limit in (RH.7). The same limit proof handles an infinite chart family and imposes no uniform bound on its components. ∎

The order of operations in (RH.7) is part of the statement. We have not interchanged an infinite limit with ind-completion:

\[
 \lim_{\mathcal I_Y}\operatorname{Ind}\mathscr R(U)
 \quad\hbox{is not being identified with}\quad
 \operatorname{Ind}\!\left(\lim_{\mathcal I_Y}\mathscr R(U)\right).
 \tag{RH.10}
\]

The left side allows chartwise bounds with no uniform bound and no global compactness requirement. Exercises 1.D and 1.I already exhibit failures of inferring global compactness from chartwise compactness, on \(B\mathbb G_m\) and on an infinite discrete stack. Ind-equivalence on a chart and equivalence of descent limits prove (RH.8), independently of those compactness failures.

This is a regular-category comparison. It does not show that a nilpotent D-module is regular. Nor does it identify algebraic characteristic support with sheaf microlocal singular support by definition. Restricting (RH.8) to the independently defined nilpotent support conditions additionally requires the matching microlocal comparison on bounded regular inputs and its chartwise ind-extension. The spectral projector, its regular image, and that support comparison retain their own proof obligations.

### 3.57. The half twist and cancellation in correspondence kernels

Let \(L\) be an ordinary line bundle on a smooth chart \(U\), and let \(\mathcal D_L=\operatorname{Diff}(L,L)\). It need not admit a flat connection. The two operator bimodules

\[
 P_L=\operatorname{Diff}(\mathcal O_U,L)
     =L\otimes_{\mathcal O_U}\mathcal D_U,\qquad
 Q_L=\operatorname{Diff}(L,\mathcal O_U)
     =\mathcal D_U\otimes_{\mathcal O_U}L^{-1}
 \tag{RH.11}
\]

have sides \((\mathcal D_L,\mathcal D_U)\) and \((\mathcal D_U,\mathcal D_L)\), respectively. The tensor notation includes these operator actions. It does not assign a connection to the bare line.

**Proposition.** Composition gives the Morita identities and their full unbounded equivalences

\[
 \begin{gathered}
 Q_L\otimes_{\mathcal D_L}^{L}P_L\simeq\mathcal D_U,\qquad
 P_L\otimes_{\mathcal D_U}^{L}Q_L\simeq\mathcal D_L,\\
 \mathcal T_L(M)=Q_L\otimes_{\mathcal D_L}^{L}M,\qquad
 \mathcal T_L^{-1}(N)=P_L\otimes_{\mathcal D_U}^{L}N.
 \end{gathered}
 \tag{RH.12}
\]

They commute coherently with the twisted and untwisted inverse transfers. They preserve coherence and characteristic support. After untwisting, regularity is exactly ordinary algebraic regularity.

**Proof.** In a frame \(e\) of \(L\), both bimodules are free rank one over the corresponding operator algebra on either indicated side; composition in (RH.12) is multiplication. Hence there is no higher Tor in these two compositions. Associativity of composition proves the two Morita triangles. These statements are local isomorphisms of bimodules and therefore glue.

To check that gluing retains derivatives, write \(e_b=e_a g_{ab}\). An operator in the \(b\)-frame is the following operator in the \(a\)-frame:

\[
 P_b\longmapsto g_{ab}P_b g_{ab}^{-1},\qquad
 \partial\longmapsto\partial-\frac{\partial g_{ab}}{g_{ab}}.
 \tag{RH.13}
\]

This is an algebra isomorphism because it is composition of actual operators on sections of the line. On a triple overlap \(g_{ac}=g_{ab}g_{bc}\), so the two conjugations compose to the third. The transitions of \(P_L\) and \(Q_L\) are inverse transitions; their evaluations into the two operator algebras are invariant. Tensoring any complex with these bimodules thus gives the equivalences in (RH.12) on every unbounded degree and every arrow.

For \(f:U\to V\), use \(f^*L\) on the source chart. In local frames the twisted inverse transfer is the ordinary transfer conjugated on its two operator sides. Its Leibniz formula differentiates the pulled-back transition by the chain rule. The two occurrences of \(d\log g_{ab}\) in (RH.13) cancel under the Morita evaluation. Therefore its entire tensor complex, including the finite Spencer differential and the dimension shift, is the ordinary inverse transfer after untwisting:

\[
 \mathcal T_{f^*L}\,f^!_L
 \xrightarrow{\sim} f^!\,\mathcal T_L.
 \tag{RH.14}
\]

This map is the identity of the transfer formula in local frames and the invariant evaluation on overlaps. A string of maps uses the same composition of operators and transfer tensors, so its comparison is coherent. It is not obtained by selecting a connection on \(L\).

Conjugation preserves the operator order filtration: its derivative correction in (RH.13) has order zero. The associated graded conjugation is the identity on \(\operatorname{Sym}T_U\). A good filtration on a coherent module is carried to a good filtration with the same cotangent support, with its rank-one coefficient line retained. This proves coherence and characteristic-support preservation. The regular twisted subcategory is the inverse image of the ordinary regular category under \(\mathcal T_L\); (RH.14) shows that this definition is compatible with the chart transitions. ∎

For \(Y=\operatorname{Bun}_G\), the **actual global** line \(L=\mathcal L_{\kappa,i}\), with its normalized square map \(L^2\simeq\mathcal D\), was constructed on families and arrows in §§2.2–2.8. Forget its parity only after the normalized ratio and square map have been formed, as in (PF.29). The neutralized root gerbe has a \(B\mu_2\) factor. Its prescribed sign sector is equivalent to complexes: the two character projectors \((1\pm s)/2\) split every complex, and the sign component is the ordinary complex tensored with that character. The operator category in that sector is consequently the line-twisted category above. Apply (RH.12) and (RH.14) on the smooth descent diagram, then (RH.8). This proves

\[
 \operatorname{Dmod}_{1/2,\mathrm{ind-rh}}(\operatorname{Bun}_G)
 \xrightarrow{\ \mathcal T_L\ }
 \operatorname{Dmod}_{\mathrm{ind-rh}}(\operatorname{Bun}_G)
 \xrightarrow{\ \operatorname{DR}^{\mathrm{ind}}\ }
 \operatorname{Shv}^{\mathrm{Betti,constr}}(\operatorname{Bun}_G;\mathbf C).
 \tag{RH.15}
\]

The choice of the proved normalized root is part of this displayed trivialization. Equivalently one can retain its sign sector on the Betti side. The argument includes the central summand, every genus, and all components; it uses neither a simply connected hypothesis on \(G\) nor a hypothetical flat connection on the root.

There is also an exact transport statement for an already defined correspondence kernel or action. Describe a kernel by its operator bimodule \(B_{21}\), with output side \(\mathcal D_{Y_2}\) and input side \(\mathcal D_{Y_1}\). On a correspondence these two algebras and the lines are pulled back along the two legs; keep all backward-transfer densities and cohomological shifts in \(B_{21}\). Its line-twisted bimodule is

\[
 B^L_{21}
 =P_{L_2}\otimes_{\mathcal D_{Y_2}}^L B_{21}
     \otimes_{\mathcal D_{Y_1}}^L Q_{L_1}.
 \tag{RH.16}
\]

It acts by the conjugated functor
\(\mathcal T_{L_2}^{-1}\Phi_{21}\mathcal T_{L_1}\).
This statement holds for any DG functor, without assuming that every functor on a nonquasicompact stack has an integral-kernel presentation. When a correspondence presentation is supplied, (RH.16) is its actual Morita bimodule formula.

For two composable presented kernels, the middle factor cancels **before** the correspondence pushforward:

\[
 \begin{gathered}
 B^L_{32}\star B^L_{21}\\
 \simeq
 P_{L_3}\otimes
 \bigl(B_{32}\star B_{21}\bigr)\otimes Q_{L_1},\\
 Q_{L_2}\otimes_{\mathcal D_{L_2}}^L P_{L_2}
 \simeq\mathcal D_{Y_2}.
 \end{gathered}
 \tag{RH.17}
\]

The unlabelled outside tensors in this display are over the corresponding untwisted operator algebras, as in (RH.16). On the fibre product of the correspondences, both occurrences of \(L_2\) are pulled back from the very same middle point. Their inverse-line evaluation is intrinsic and has coefficient one in every frame. The remaining composition is exactly the original convolution, with its original transfer density, shifts and base-change maps. Since the line factors are invertible and the evaluations are maps of the operator bimodules, the cancellation is valid in the derived tensor before any stated pushforward is applied.

For three kernels there are two middle factors. Either association evaluates the same two pairs \(Q_{L_j},P_{L_j}\). Associativity of composition of differential operators makes the routes equal. For any number of kernels every intermediate evaluation occurs once; this gives all the associativity and unit coherences. At the functor level the same proof cancels the adjacent equivalences \(\mathcal T_{L_j}\mathcal T_{L_j}^{-1}\) with their actual Morita triangles. Natural transformations, restriction maps and any already supplied fusion diagram are conjugated by those equivalences, so their coherent relations are preserved.

This proves twisting and cancellation for an existing action. It does not construct its missing Satake kernels, fusion isomorphisms, or spectral coefficient functor, and does not identify a transported action with a separately normalized action without comparing their kernels. Those are the remaining geometric inputs of the Hecke construction.

![Chartwise Riemann–Hilbert descent and the cancellation of the middle twisting line](src/figures/rh-stack-morita.svg)

**Figure 3.17.** The upper panels are diagrams of categories and actual inverse-image comparisons, (RH.1)–(RH.9), rather than an embedding of every analytic sheaf into a D-module category. The lower panel shows two operator kernels with their intermediate Morita factors retained, followed by their evaluation in (RH.17). All arrows carry the maps proved above; the displayed \((2\pi i)^{-r}\) is the coefficient only in the smooth flat frames of (RH.6). This is a schematic of descent and operator composition, with no numerical sample. The earlier proof source is The Riemann–Hilbert correspondence, §1.

### 3.58. Higher attaching maps, trace constants, and a nonflat twisting line

**Exercise 3.AW.** On \(\mathbf P^1_\mathbf C\), calculate the derived endomorphisms of the constant sheaf and their algebraic D-module counterpart. Explain why deriving finite-dimensional vector spaces and then forming constant sheaves loses a higher attaching map. Keep the residue/period normalization.

**Solution 3.AW.** The finite Spencer calculation in §3.51 and the explicit two-chart calculation of §3.50 compute the unshifted algebraic de Rham cohomology:

\[
 \operatorname{RHom}_{\mathcal D_{\mathbf P^1}}(\mathcal O,\mathcal O)
 \simeq \mathbf C\oplus\mathbf C[-2].
 \tag{RH.18}
\]

For clarity, that Čech calculation has \(U_0=\mathbf A^1_z\), \(U_\infty=\mathbf A^1_w\), \(w=z^{-1}\). Polynomial de Rham forms on each affine chart have only the constant degree-zero class: integrate each nonconstant monomial by dividing by its nonzero positive integer exponent. On their intersection, Laurent forms have that constant and the single extra class \(dz/z\), because all monomials other than \(z^{-1}dz\) integrate to Laurent monomials. In the two-chart Mayer–Vietoris complex the difference map on constants \(\mathbf C^2\to\mathbf C\) is surjective with diagonal kernel. The extra intersection degree-one class moves to total degree two. There is no degree-one class and no other degree. Over a field the cohomology splitting yields the displayed complex equivalence. The generator is this Čech/form class, not a global holomorphic one-form.

The fully faithful actual comparison (RH.2) and the common shift \([1]\) identify (RH.18) with
\(\operatorname{RHom}(\mathbf C_{\mathbf P^1},\mathbf C_{\mathbf P^1})\).
Thus there is a nonzero
\(\alpha:\mathbf C_{\mathbf P^1}\to\mathbf C_{\mathbf P^1}[2]\).
Let \(K=\operatorname{Cone}(\alpha)\). Its ordinary cohomology is constant of rank one in degrees \(-2,-1\) and zero otherwise. Its canonical truncation triangle has connecting map \(\alpha[1]\), up to the triangle rotation sign, so it does not split. In contrast every bounded complex of finite-dimensional vector spaces splits into its cohomology, since kernels and images have linear complements, and it has no degree-two endomorphism of \(\mathbf C\). Applying the constant-sheaf functor to such a complex produces a split constant complex. It cannot produce this \(K\). This demonstrates the lost higher map without assuming that a heart equivalence derives to an equivalence.

The algebraic residue trace of the generator \([dz/z]\) is \(1\). Its actual analytic comparison has positive complex-oriented integral \(2\pi i\). Therefore the proper extraordinary comparison for \(\mathbf P^1\to\mathrm{pt}\) multiplies by \((2\pi i)^{-1}\), exactly as in (RH.6); rescaling an unnamed generator would hide this check.

**Exercise 3.AX.** Prove, for all nonnegative integers \(s,r,c\), the two sign cancellations used to obtain the smooth and closed coefficients in (RH.6). Check smooth relative dimension two and closed codimension two without replacing the ordinary inverse comparison or the raw closed counit by a positive identity.

**Solution 3.AX.** Use the actual positive untwisted frames of the RH lesson and put

\[
 \sigma_n=(-1)^{n(n+1)/2},\qquad
 \varepsilon_n=(-1)^{n(n-1)/2}.
 \tag{RH.19}
\]

In those frames the connection evaluation has coefficient \(\sigma_n q\), and shifting the connection by \(k\) contributes \((-1)^{nk}\). The ordinary smooth inverse comparison has coefficient \(\varepsilon_r\); the ordinary closed inverse comparison has coefficient \(\sigma_c\). Substitution into its actual dual-defined extraordinary comparison gives

\[
 \frac{\sigma_{s+r}(-1)^{(s+r)r}}{\varepsilon_r\sigma_s}=1,
 \qquad
 \frac{\sigma_s(-1)^{sc}}{\sigma_c\sigma_{s+c}}=1.
 \tag{RH.20}
\]

The exponent of the first quotient is \(2sr+r(r+1)\); the exponent of the second is \(-c(c+1)\). Both are even for every integer involved. Thus these are general identities, not an inference from a table of low dimensions. What remains is the ratio of the \(q\)'s, namely \((2\pi i)^{-r}\) and \((2\pi i)^c\).

For \(r=2\) and \(s=0\), \(\sigma_2=\varepsilon_2=-1\), and the shift factor is \((-1)^4=1\), so the first quotient is \(1\), leaving \((2\pi i)^{-2}\). For \(c=2\) and \(s=0\), the denominator of the second quotient is \((-1)(-1)=1\). The **raw** ordered closed counit in the untwisted top Hom frame still has coefficient \(\varepsilon_2=-1\), as computed in (KG.15) and (KG.16). Its raw normal evaluation has the same sign times the normal period; their comparison cancels those signs. None of those individual maps has been replaced by an identity.

Composition preserves the period constants because dimension differences add. The ordinary frame signs instead satisfy
\(\varepsilon_{r+t}=(-1)^{rt}\varepsilon_r\varepsilon_t\):
the exponent difference is \(rt\). This is exactly the determinant/tensor frame interchange in a composed ordinary inverse. Dropping that interchange would make the two-dimensional check fail even though the object shifts looked correct.

**Exercise 3.AY.** For \(L=\mathcal O_{\mathbf P^1}(1)\), use frames \(e_0=X_0\), \(e_\infty=X_1=z e_0\) on the standard charts. Write the operator transition, prove that \(L\) has no algebraic flat connection, and nevertheless perform one middle-line cancellation for a kernel.

**Solution 3.AY.** On the overlap \(z\ne0\), express both operators using the derivation \(\partial_z\) (on the other chart it is \(-w^2\partial_w\)). Formula (RH.13) gives

\[
 z\,\partial_z\,z^{-1}=\partial_z-z^{-1}.
 \tag{RH.21}
\]

If a connection existed, write its connection forms as \(a_0(z)\,dz\) and \(a_\infty(w)\,dw\), with \(a_0,a_\infty\) polynomials, since the respective frames are regular on their whole affine charts. The frame relation forces

\[
 a_\infty(z^{-1})(-z^{-2}dz)
   =a_0(z)\,dz+\frac{dz}{z}.
 \tag{RH.22}
\]

The left side has only Laurent exponents at most \(-2\); the first right term has only exponents at least zero. The \(z^{-1}\) coefficient on the right is \(1\), a contradiction. Thus even an algebraic connection on \(L\) is impossible; flatness cannot repair this obstruction.

Nonetheless \(L\) is the tautological \(\mathcal D_L\)-module and
\(\mathcal T_L(L)=\mathcal O\) with its ordinary connection. Locally the tensor in (RH.12) sends \(1\otimes e^{-1}\otimes e\) to \(1\). On an overlap the two factors multiply by \(z^{-1}\) and \(z\); the product is one, and the two logarithmic derivative terms cancel. This is an operator-bimodule evaluation, not a flat trivialization of \(L\).

For a middle occurrence of this line in two kernels, the local expression for (RH.17) is the same evaluation \(Q_L\otimes_{\mathcal D_L}P_L\to\mathcal D\). It is invariant under the just-checked transition. If three kernels are composed, the two middle evaluations contract independent inverse pairs, so both parenthesizations give the same operator multiplication. The example verifies both the gluing obstruction to a guessed connection and the valid Morita cancellation that the half twist requires.

### 3.59. A coefficient functor into the full spherical category

For §§3.59–3.62 the ground and coefficient field is \(\mathbf C\). Fix a connected reductive complex group \(G\), its torus and Borel, and the cycle pinning in Identifying the dual group, §8.6. The particular ordinary Satake equivalence used here is

\[
 s:\operatorname{Rep}^{\mathrm{fd}}_{\mathbf C}(\widehat G)
   \xrightarrow{\sim}\operatorname{Sat}_G(\mathbf C),
 \qquad s(V_\lambda)=IC_\lambda .
 \tag{SH.1}
\]

This is the actual symmetric tensor equivalence of that lesson's Theorem 8.3, with the component-adjusted fusion symmetry. It is not a derived equivalence. Its matching complete proofs are Convolution and rigidity, §§1–9, Fusion and the commutativity constraint, §§1–7, Tannakian categories, §§1–8 and Theorem 10.1, and The fibre functor and the Tannakian group, §§1–9. They construct the finite correspondence, normalized torsor coefficient, proper image, actual evaluation maps, both triangles, moving-point exchange, weight tensor maps, and the reconstructed group on every test algebra. Identifying the dual group, §§7–8, then identifies the integral root datum and removes every finite-stage unipotent kernel by the proved IC self-extension vanishing. These are the earlier proofs supplying (SH.1).

Write \(\mathcal S_{\rm amb}\) for the ambient spherical DG category, retaining all derived equivariance and mapping complexes, rather than deriving its perverse heart. On finite Schubert supports, its classical model uses the full finite-jet equivariant derived category. The actual free-frame quotients, acyclicity estimates and comparisons are proved in Equivariant perverse sheaves and perverse sheaves on stacks, Appendix B, Theorem B.9; its first action isomorphism and cocycle alone describe only the heart. The DG Hom models and the extra equivariant unit morphisms are specified in Derived Satake, §§1–2. In particular the ambient t-structure gives

\[
 H^n\operatorname{RHom}_{\mathcal S_{\rm amb}}(A,B)=0
 \quad(n<0,\ A,B\in\operatorname{Sat}_G).
 \tag{SH.2}
\]

There is no vanishing assertion for positive degrees.

**Lemma.** Let \(\mathcal A\) be a small semisimple abelian \(\mathbf C\)-linear category and \(j:\mathcal A\to\mathcal C^\heartsuit\) a \(\mathbf C\)-linear additive functor into the heart of a stable DG category. It extends to an exact DG functor \(D^b_{\rm dg}(\mathcal A)\to\mathcal C\). A supplied monoidal heart functor extends monoidally when the target product is exact in both variables. A specified symmetric coefficient constraint and its relations also extend; a symmetry on the whole target is not required.

**Proof.** Let \(\mathcal H\) be the full ordinary heart subcategory on the objects \(jA\). In the full DG model on those objects replace a mapping complex \(K\) by its good nonpositive truncation: retain \(K^n\) for \(n<0\), use \(\ker(d:K^0\to K^1)\) for degree zero, and use zero for positive degrees. Composition restricts, by its graded Leibniz identity. Projection to degree-zero cohomology gives a DG functor

\[
 q:\mathcal H_-\longrightarrow\mathcal H,\qquad
 \operatorname{RHom}_{\mathcal H_-}(jA,jB)
   =\tau_{\le0}\operatorname{RHom}_{\mathcal C}(jA,jB).
 \tag{SH.3}
\]

It is a quasi-isomorphism on every mapping complex, since the negative cohomology vanishes by heart orthogonality. It is onto the indicated objects. Compose the given ordinary \(j:\mathcal A\to\mathcal H\) with an enhanced inverse of \(q\), and then with the actual inclusion \(\mathcal H_-\to\mathcal C\).

Here an enhanced inverse retains its units, counits and coherent composition. One construction uses the graph bimodule of \(q\) and representable modules. Restriction and tensor extension along that bimodule have evaluation maps which are quasi-isomorphisms on representables by (SH.3). In their augmented composition bar, insertion of the identity contracts the augmentation. Its evaluations therefore give the two inverse comparisons on representables and on their finite sums, cones and retracts. This constructs the needed inverse with its data, not an inverse selected only on the triangulated homotopy category.

The tensor maps restrict to \(\mathcal H_-\), because products of nonpositive degrees are nonpositive and products of degree-zero cycles are cycles. The supplied associators and unitors restrict with their homotopies. The chosen coefficient exchange can be lifted along \(q\) with its relations: a difference of degree-zero composites representing the same heart map is a boundary and has a degree-minus-one homotopy; the next obstruction lies in degree-minus-one cohomology, and successive obstructions in successively lower cohomology. They all vanish. The same calculation applies in every tensor arity, since each coefficient product remains in the indicated heart. Each component of the mapping space with specified degree-zero class is contractible. Thus the naturality, associativity, unit, double-exchange and hexagon diagrams and their higher compatibilities lift coherently. Their images are the specified coefficient maps in the target, without a target-wide symmetry assertion.

Extend this enhanced functor to finite twisted complexes. It retains the differential arrows and their homotopies; representatives of a heart differential are not incorrectly assumed to compose to zero as chain maps. Explicitly a relation which is zero in \(H^0\) has its degree-minus-one homotopy, and (SH.2) kills each subsequent obstruction. Functoriality of the DG construction retains this data for maps between complexes as well.

Semisimplicity identifies these finite twisted complexes with the bounded derived category. For a bounded coefficient complex choose splittings

\[
 Z^i=B^i\oplus H^i,\qquad
 A^i=Z^i\oplus W^i,\qquad
 d:W^i\xrightarrow{\sim}B^{i+1}.
 \tag{SH.4}
\]

It is the sum of its zero-differential cohomology terms and these two-term isomorphism complexes. The latter contract by the inverse of \(d\). Every bounded acyclic complex is consequently contractible, and every quasi-isomorphism is a homotopy equivalence by the same calculation on its cone. Localization adds no mapping information to this finite pretriangulated model. Its idempotents split in the finite cohomology description. The target functor therefore descends to the stated bounded derived category.

On coefficient complexes the tensor differential and exchange are

\[
 d(x\otimes y)=dx\otimes y+(-1)^{|x|}x\otimes dy,
 \qquad
 c(x\otimes y)=(-1)^{|x||y|}c_{\mathcal A}(x\otimes y).
 \tag{SH.5}
\]

Expanding \(d^2\) cancels the mixed terms. Associativity uses the same ordered triple degrees; the chain symmetry and hexagons use the identities \(p(q+r)=pq+pr\) and \((p+q)r=pr+qr\) modulo two. Exactness in each target variable extends the supplied heart tensor maps over the finite cones. This proves the lemma and every indicated coefficient relation. ∎

Apply the lemma to (SH.1) and the actual convolution product. Convolution on the ambient derived category is the proper endpoint image of the torsor-descended external product. On a finite frame model all arrows are pullback, external tensor, descent and proper direct image. They are exact DG functors. Three- and four-step correspondences identify the actual associator and its pentagon, as in the earlier convolution proof; the same resolution maps retain the derived morphisms. The lemma therefore constructs

\[
 S_{\rm fin}:D^b_{\rm dg}
      \bigl(\operatorname{Rep}^{\mathrm{fd}}_{\mathbf C}(\widehat G)\bigr)
       \longrightarrow\mathcal S_{\rm amb}.
 \tag{SH.6}
\]

Its products, duality maps and coefficient exchanges are the actual chosen Satake maps. Use the ordinary presentable spherical category, with its full derived equivariant descent, as the target of this finite functor. It admits colimits; this does not define it to be the ind-category of its IC objects. The finite functor extends continuously:

\[
 S:\operatorname{Ind}D^b_{\rm dg}
      \bigl(\operatorname{Rep}^{\mathrm{fd}}_{\mathbf C}(\widehat G)\bigr)
       \longrightarrow\mathcal S_{\rm amb},
 \qquad S(\mathop{\rm colim}_i V_i)=
                    \mathop{\rm colim}_i S_{\rm fin}(V_i).
 \tag{SH.7}
\]

The representable bar just used gives this extension independently of the presentation. On finite coefficients the tensor comparisons are already constructed; separate continuity extends them through the common double colimit. This does not say that the ICs become compact after equivariance, nor identify ordinary and renormalized spherical categories. All higher ambient morphisms remain present.

### 3.60. Actual regular D-module coefficients and fusion shifts

The coefficients in (SH.6) have a genuine regular D-module realization. For a singular finite support \(Z\), embed an affine open in a smooth ambient \(W\) and use regular holonomic D-modules supported on \(Z\). The actual RH equivalence on \(W\) restricts to sheaves supported on \(Z\): restrictions to the complementary open commute with RH, and each vanishes exactly when the other does. Thus all mapping complexes and attaching maps are retained. Smooth ambient comparisons are the projection/graph equivalences of Kashiwara's equivalence and singular spaces, Theorem 5.1 and §5. Their local proof applies Kashiwara to a smooth graph containing \(Z\), never to \(Z\) as a smooth scheme. Direct-image composition gives the comparisons for three or four ambients; the actual RH comparisons preserve them. On affine overlaps they glue with those units and counits. This is the supported regular theory, rather than the operator ring of a singular coordinate algebra.

The same construction on the finite-jet action nerve retains the full derived equivariance. On each of its finite chart/ambient models use the complete general RH equivalence and all its actual four-map comparisons, proved in the RH lesson's §1. Their composition data compare the entire nerve. Take the coherent limit as in (RH.7)–(RH.9), then ind-extend the finite coefficients when required. No equivalence of hearts is being used to reconstruct that ambient limit. Denote the resulting actual coefficient by \(S_D(V)\).

For a smooth map \(f\) of relative dimension \(e\), the perverse-normalized sheaf pullback \(f^*[e]\) is its extraordinary pullback \(f^![-e]\). Accordingly the operator normalization is

\[
 f^![-e]\quad\longleftrightarrow\quad f^{\mathrm{an},*}[e].
 \tag{SH.8}
\]

In a finite convolution frame both maps have relative dimension \(e_n=n\dim G\). Apply (SH.8) to the two sides of the torsor descent formula (2.1) in the convolution lesson. The two \([-e_n]\) shifts cancel; the actual smooth RH comparison has the same \((2\pi i)^{-e_n}\) on both sides in the specified flat frames, so that coefficient cancels as well. The descended D-module is therefore the actual twisted external coefficient with no unexplained jet shift. Proper image compares by the RH trace map, including its residue normalization. This proves that the operator convolution and its actual associators on these coefficients realize (SH.6), not merely that the two products have equal dimensions.

For an ordered tuple of coefficient heart objects \(P_1,\ldots,P_r\), the fusion lesson constructs a proper moving chain and its actual endpoint coefficient

\[
 \mathcal F_r(P_1,\ldots,P_r)
    =Rm_{r*}(\mathcal A_r[r])
    =j_{r!*}\bigl((P_1\boxtimes\cdots\boxtimes P_r)
                             \boxtimes\mathbf C_{U_r}[r]\bigr).
 \tag{SH.9}
\]

This is valid on every smooth complex curve after its proved full-coordinate descent. The family is universally locally acyclic over the ordered-point base. The proof uses the proper stratified-product construction, retains all attaching maps, and moves the actual proper image through the punctured-disc cover and special restriction. It does not assume a general nearby-cycle t-exactness theorem.

Let a partial diagonal have \(b\) distinct blocks, let \(c=r-b\), and convolve the labels within each block in their specified order. The actual collapse of intermediate bundles and proper composition give

\[
 i^*\mathcal F_r[-c]\simeq
      \mathcal F_b(P_{\mathrm{block}\,1},\ldots,
                                      P_{\mathrm{block}\,b}).
 \tag{SH.10}
\]

The shifts can also be read directly: the total source normalization is \([r]\), while the \(b\)-point family has \([b]\). Universal local acyclicity gives \(i^!\mathcal F_r=i^*\mathcal F_r[-2c]\), with the complex orientation of the normal parameter directions. Hence the actual D-module comparison is

\[
 i^!\mathcal F_{r,D}[c]\simeq
      \mathcal F_{b,D}(S_D(V_{\mathrm{block}\,1}),\ldots).
 \tag{SH.11}
\]

At a fixed \(r\)-tuple the normalization is \(i_{\vec x}^!\mathcal F_{r,D}[r]\). For the full diagonal followed by a point restriction, (SH.11) composes to precisely that normalization, since \((r-1)+1=r\). These are the actual inverse-transfer maps, with the RH comparison constants of §3.55 retained, not raw flat-frame identities.

On the distinct-point locus the coefficient permutation is the external-product exchange and the identity on the **one** base factor \(\mathbf C_{U_r}[r]\). It does not exchange \(r\) separately shifted base factors. On homogeneous components use

\[
 e(\lambda)=\langle2\rho,\lambda\rangle\bmod2,\qquad
 c'_{P,Q}=(-1)^{e(P)e(Q)}c_{P,Q}.
 \tag{SH.12}
\]

The fusion lesson proves that \(e\) is a component homomorphism and that ordinary cohomology on each component has that parity. Thus \(c'\) is the constraint in (SH.1). Its scalar is extended to the whole fusion family before restriction. Products of these scalars give the permutation maps in every arity. Their two hexagons and double exchange follow from bilinearity of \(ef\); their associators are the actual partial-collapse comparisons (SH.10). Adding coefficient cochain shifts uses the further Koszul factor in (SH.5).

The finite coefficient functors in every arity are complex-linear and additive on the semisimple tuple category. Their values in (SH.9) are perverse. Apply the proof of the lemma to their ordinary functors into the full perverse heart on the moving target; full faithfulness of those tuple functors is not required. The natural comparison maps (SH.10), after their indicated shifts, are maps between perverse values. Their negative Hom cohomology vanishes, so the same nonpositive truncation constructs their entire coherent DG relations. Finite twisted complexes and then colimits extend them. Consequently these fusion coefficients, all collision comparisons, exchanges and unit maps are constructed for the DG coefficient category of (SH.7). Their ambient higher morphisms have not been discarded.

### 3.61. The resulting complex coefficient Hecke functors

Let \(X\) be a smooth projective complex curve and \(Y=\operatorname{Bun}_G(X)\), with every genus and every component retained. Let \(\mathcal H_{X^r}\) be the endpoint Hecke stack: a source bundle, a target bundle, ordered marked sections, and an identification away from their graphs. For bounded coefficient supports the finite moving construction above bounds this correspondence, while the intermediate bundles belong to its proper chain resolution. Write

\[
 h_{\rm in}:\mathcal H_{X^r}\longrightarrow Y,\qquad
 h_{\rm out}:\mathcal H_{X^r}\longrightarrow Y\times X^r .
 \tag{SH.13}
\]

The bounded \(h_{\rm out}\) is projective. To check it over a smooth bundle chart, reverse the endpoint description and trivialize the target bundle on a sufficiently deep finite divisor. The source modifications have the inverse bounded types. The finite endpoint is the closed stable-lattice locus in the Plücker Grassmannian construction of the fusion lesson. A common finite bound and a product of its Plücker line bundles give an equivariant relatively ample line. Its finite-jet linearization descends through the target divisor-frame torsor; relative projectivity is therefore preserved on the bundle chart. The bounded chain is an iterated associated projective support and maps properly to this endpoint. Its maps preserve the fixed off-divisor identification. The construction and closed equations are retained after every parameter base change. This uses the full scheme constructions, including nilpotent parameter rings, rather than only the classification of geometric loop cosets.

We need the full unbounded correspondence calculus, including singular finite supports. Here is the extension that is used below.

**Projective correspondence lemma.** Let \(B\) be smooth, separated and of finite type. Let \(f:Z\to B\) be projective, with \(Z\) allowed to be singular. Define the full D-module category of \(Z\) by supported modules in a smooth ambient, with the projection/graph comparisons of Theorem 5.1 cited in §3.60. Direct image \(f_*\) preserves colimits. For a smooth finite-type \(B'\) and any map \(g:B'\to B\), its actual base-change comparison is

\[
 g^!f_*Q\simeq f'_*g_Z^!Q,\qquad
 Z'=Z\times_BB',
 \tag{SH.14}
\]

for every unbounded \(Q\). The projection formula with \(\otimes^!\) holds for unbounded inputs. These maps retain composition, localization, and ordered transfer evaluation; no smoothness of \(Z'\) is inferred.

**Proof.** The bounded smooth-variety proofs, including the maps themselves, are Adjunctions, base change and the projection formula, §§1–3, Theorems 2.1 and 3.1. We give the additional steps.

First work with a map of smooth finite-type schemes. Factor it into its closed graph followed by a product projection. Closed graph direct image is tensor with the backward transfer, flat on its right operator side. The projection uses its finite relative Spencer complex. Over an affine target, a finite affine intersection cover computes every quasi-coherent coefficient column before totalizing the finite Spencer and Čech directions. Each column operation preserves colimits. The differential may be a differential operator; it is retained between these computed columns, rather than treated as a structure-sheaf-linear map. This defines the full unbounded direct image, proves continuity, and gives a cohomological amplitude bound independent of the input.

Inverse transfer is computed by a finite structure Koszul resolution on the closed graph and flat pullback on the projection, with the chain-rule operator action and dimension shift. It too is continuous with an input-independent finite amplitude. The bounded comparison maps consequently extend to all inputs without interchanging an infinite product and a sum: in any selected output degree, choose an input window larger than the two amplitude bounds. The truncation triangles identify that output cohomology with the cohomology computed from the bounded window. The bounded comparison is an isomorphism there. The same argument in every degree proves the unbounded comparison.

The closed part of base change uses the localization triangle. Its local complement computation is a finite Čech complex of principal localizations. The normal Koszul complex on a term where a normal coordinate is invertible contracts by that coordinate's inverse. On a supported cohomology module the Kashiwara inverse is exact; the finite normal complex and the preceding window argument give the same assertion for an unbounded supported complex. Thus the actual map is still the localization augmentation followed by the signed normal counit of equations (1.5a)–(1.5g) of the cited lesson. Product base change uses the same external tensor and finite Spencer–Čech permutation maps. Their compositions are precisely the bounded maps in every output degree, so they retain all multiple-square coherences.

For the projection formula, retain the graph against the diagonal as in equations (3.4)–(3.5) of that lesson. Resolve both unbounded inputs by semifree operator complexes; their underlying structure modules are flat on smooth affine charts. Derived exterior tensor and diagonal inverse transfer therefore give the actual derived tensor product, with its total differential and Koszul signs. The base-change map just established and the external Spencer–Čech comparison give the same graph computation on these complexes. All sums and realizations in either input are preserved by these operations. This proves the formula with two unbounded inputs, including the shift \([-d_B]\); the unit remains \(\omega_B=\mathcal O_B[d_B]\).

Now embed \(Z\) over \(B\) in \(E=B\times\mathbf P^N\). Regard \(Q\) as its actual supported object \(\widetilde Q\) on the smooth \(E\), and define \(f_*Q=\pi_*\widetilde Q\). The supported ambient comparisons also apply unboundedly: locally lift the coordinate functions of a second ambient to the first one and use the smooth graph containing \(Z\), as in Theorem 5.1. On supported cohomology modules its normal Kashiwara inverse is exact; finite normal transfer and the window argument above retain its derived unit and counit on an arbitrary complex. Common product ambients then give the same triple and fourfold comparisons.

The other ambient is \(E'=B'\times\mathbf P^N\), which is smooth. Apply the already proved smooth-square comparison to the projective projection \(\pi\) and \(g\). The inverse transfer of \(\widetilde Q\) is supported on the possibly singular \(Z'\): outside \(Z'\) it is inverse transfer of zero, as its open restrictions show. By the supported ambient definition it represents \(g_Z^!Q\). This proves (SH.14), with no smooth transfer formula on \(Z'\). The common ambient comparisons identify different projective embeddings and their maps. The same graph–diagonal calculation on supported objects proves the projection formula there.

Finally, for a representable projective correspondence over a stack, apply this construction on every smooth finite-type affine target chart. Formula (SH.14) supplies its transitions. On chart refinements and their higher nerves they are the same composed transfer tensors, localization maps and evaluations. They therefore define a coherent descent object. Colimits are computed chartwise; conservative chart restrictions prove continuity of the descended functor. No interchange of the entire infinite chart limit with an ind-category has been used. This proves the lemma. ∎

We describe the coefficient kernel on the actual common frame diagram. Let \(u:U\to Y\) be a smooth affine source bundle chart, and write \(\mathcal H_U\) for its base change. The finite divisor-frame torsor over \(U\times X^r\), pulled to the bounded moving Grassmannian, gives two smooth maps

\[
 U\times\operatorname{Gr}^{\rm bd}_{G,X^r}
       \xleftarrow{\ p\ } A_U
       \xrightarrow{\ q\ }\mathcal H_U .
\]

For the order-\(n\) thickening of the degree-\(r\) marked divisor, both have relative dimension \(e_{n,r}=nr\dim G\). In a local curve coordinate its defining monic polynomial has degree \(nr\), so its quotient is finite free of rank \(nr\) over every parameter ring, including repeated sections and nilpotents. Smoothness of \(G\) makes the corresponding divisor-frame group smooth of that dimension by its infinitesimal lifting criterion. Choose the same sufficient jet level for the two maps. The map \(p\) forgets the divisor frame; \(q\) uses it to identify the modification with one of the input bundle. Define \(K_{\vec V}\) by the torsor descent

\[
 q^!K_{\vec V,U}
       \simeq p^!\bigl(\omega_U\boxtimes\mathcal F_{r,D}
                              (S_D(V_1),\ldots,S_D(V_r))\bigr).
 \tag{SH.15}
\]

Here \(\omega_U=\mathcal O_U[d_U]\) is the D-module dualizing object, the unit for \(\otimes^!\). Equivalently, apply \([-e_{n,r}]\) on both sides to obtain the normalized torsor formula of (SH.8). The formula includes the source-chart factor; a bare vertical IC is not its replacement. It does not assume that a divisor-frame torsor varying with the marked points is globally a product over \(U\).

These expressions descend to an actual kernel. The spherical coefficient action gives the descent datum along the actual \(q\)-torsor nerve. A change of curve parameter uses the normalized full-coordinate structure constructed in fusion §6. Both have their specified cocycles, commute with each other in the semidirect coordinate action, and preserve the proper moving-chain maps. A smooth change of bundle chart pulls \(\omega_U\) to its dualizing object and pulls the common frame diagram to the corresponding one. On a common chart refinement the formulas are consequently the same pulled external coefficient and evaluation maps. Their transitions include every nerve relation, as in (RH.9). They glue (SH.15), preserving both finite-support enlargements and deeper jet levels.

Define the coefficient Hecke functor on the full unbounded D-module category by

\[
 \mathsf H^r_{\vec V}(M)
      =(h_{\rm out})_{\mathrm{dR},*}
                  \bigl(h_{\rm in}^!M\otimes^!K_{\vec V}\bigr).
 \tag{SH.16}
\]

All input degrees are retained. Put \(M_U=u^!M\), with the actual bundle-chart inverse transfer. On the common frame diagram the product formula is

\[
 q^!\bigl(h_{\rm in,U}^!M_U\otimes^!K_{\vec V,U}\bigr)
                \simeq p^!(M_U\boxtimes\mathcal F_{r,D}).
 \tag{SH.17}
\]

Indeed the two maps from \(A_U\) to \(U\) are equal. Thus \(q^!h_{\rm in,U}^!M_U=p^!\operatorname{pr}_U^!M_U\). Actual \(!\)-inverse transfer preserves \(!\)-tensor, by the same diagonal/graph comparison proved in the lemma. Apply it to (SH.15). In the product model, \(\operatorname{pr}_U^!M_U\) is external tensor with the dualizing object of the other factor. That object is the unit for \(!\)-tensor there, while \(\omega_U\) is the unit on the first factor. Their evaluation leaves \(M_U\boxtimes\mathcal F_{r,D}\), proving (SH.17). The normalized functor \(q^![-e_{n,r}]\) by itself is not asserted to be monoidal. In the full operator complexes these are the same transfer tensor, finite Spencer differential and evaluation identities as in §§1.10–1.12 and §§3.48–3.51; the calculation puts no bound on \(M\). It is not an RH comparison for a nonregular \(M\).

For a bounded coefficient support, the projective correspondence lemma proves continuity in \(M\), with actual inverse transfer, base change and projection formula on singular supports. For an arbitrary coefficient, (SH.16) means the colimit of these bounded-support functors along its finite-coefficient presentation, as in (SH.7). This definition retains every arrow in that presentation; it does not assert continuity of a star direct image on an unbounded ind-proper correspondence. Continuity in \(M\) and the coefficient follows from the common double colimit. On chart overlaps, the lemma's actual base-change and transfer composition maps give the transitions of (SH.17). An infinite chart family is kept as the descent family; no uniform bound on its components or compactness of \(M\) is inferred.

The unit normalization is especially useful. For \(r\) trivial labels the moving chain is the marked-point base, its endpoint is the identity-bundle section, and its coefficient is \(\mathcal O_{X^r}\). Consequently

\[
 \mathsf H^r_{\mathbf1,\ldots,\mathbf1}(M)
       =M\boxtimes\mathcal O_{X^r}
       =p_Y^!M[-r].
 \tag{SH.18}
\]

There is no extra product of jet shifts. At a fixed marked tuple use the inverse-transfer normalization of (SH.11), giving the identity functor for these unit labels.

We prove the composition and fusion relations for (SH.16). Composing two bounded modifications retains the intermediate bundle. On a common finite frame chart, the two coefficient factors and their proper chain image are exactly the twisted external product and convolution coefficient of §3.60. The source pullbacks of \(M\) are the same in both routes. Projection formula and proper composition identify the iterated (SH.16) with its single proper chain image. Collapsing the intermediate bundle gives the actual tensor map \(S_D(V)\star S_D(W)\simeq S_D(V\otimes W)\). Three modifications give the actual associator, and four modifications give its pentagon, since both routes are composition on the same four-step correspondence with the same operator transfer tensors. The identity correspondence gives both unit triangles.

For distinct marked points, formal divisor gluing identifies independent modifications and their coefficients. Along a partial diagonal the same collapse on each collision block gives (SH.11), with shift \(r-b\). Proper base change identifies this normalized inverse transfer of (SH.16) with the \(b\)-point action whose block labels are tensor products. These are finite correspondence identities on the entire operator coefficient complexes; (SH.17) keeps an arbitrary unbounded \(M\) as the unchanged first factor. The three- and four-step correspondences show that repeated collisions give the same maps in every grouping. Permutations use the chosen family exchange (SH.12), with its one base factor and the additional coefficient cochain signs. This constructs the complex classical-coefficient fusion Hecke action and all these relations on the full unbounded \(D\)-module category.

Finally use the actual normalized global root \(L=\mathcal L_{\kappa,i}\) already proved in §§2.2–2.8. Let \(\mathcal T_{Y\times X^r}\) untwist the pullback of that line from \(Y\), and let \(\mathcal T_Y\) be its source version. Define

\[
 \mathsf H^{r,L}_{\vec V}
     =\mathcal T_{Y\times X^r}^{-1}
                       \mathsf H^r_{\vec V}\mathcal T_Y.
 \tag{SH.19}
\]

This is an actual transported half-twist action. In a composable correspondence the two middle lines come from the same intermediate bundle. Their operator factors cancel by (RH.17) before pushforward. Its Morita triangles and every multiple cancellation preserve the unit, composition, partial-diagonal and permutation relations just proved. All genus and component dependence lies in the actual global line already constructed, so no new simply connected hypothesis is introduced.

The construction has precise remaining boundaries. It does not prove derived tempered Satake, identify its coefficient functor with a separately normalized factorization equivalence, or extend the complex RH argument to an arbitrary characteristic-zero ground field. It also does not yet construct the full \(D\)-module-valued unital Ran coefficient category and the spectral coefficient functor used for the regular Hecke algebra. The actual classical coefficient functors and finite-tuple fusion relations above are inputs to that further construction. No assertion about the projector's nilpotent image, nilpotent regularity, or the independent microlocal support comparison follows merely from their existence.



![Complex coefficient fusion, actual projective correspondence and full unbounded Hecke action](figures/complex-fusion-hecke.svg)

**Figure 3.18.** The coefficient functor retains the full ambient spherical mapping complexes (SH.6)–(SH.7). Collision uses the exact inverse-transfer shift (SH.11). The common divisor-frame diagram defines the kernel with its source dualizing factor (SH.15), and evaluates it on every unbounded input by (SH.17). The projective correspondence lemma (SH.14) supplies its actual base-change and projection maps on singular supports. Units and transported half twists are (SH.18)–(SH.19). The diagram is a schematic of these proved maps; it does not identify ordinary and renormalized spherical categories or construct the further spectral Ran functor. The matching complete programme proofs are linked in §§3.59–3.61. For the classical geometric construction, see I. Mirković and K. Vilonen, [*Geometric Langlands duality and representations of algebraic groups over commutative rings*, free corrected preprint v5](https://arxiv.org/abs/math/0401222v5). The proofs above and those earlier programme proofs establish the results used here.

### 3.62. Three normalization checks

**Exercise 3.AZ.** Give a spherical example in which (SH.6) fails to be fully faithful on higher shifts although its heart functor is an equivalence.

**Solution 3.AZ.** Take \(G=\mathbf G_m\) and its unit at the zero coweight. The coefficient heart is finite supported integer-graded vector spaces. Choose complements to boundaries inside cycles and to cycles inside each term; (SH.4) makes every bounded coefficient complex the sum of its cohomology terms and contractible complexes. Thus

\[
 \operatorname{Hom}_{D^b\operatorname{Rep}(\widehat{\mathbf G}_m)}
                  (\mathbf1,\mathbf1[2])=0 .
 \tag{SH.20}
\]

The full ambient spherical category instead has the classifying-space unit. Derived Satake, §§2–3.1, proves its actual endomorphism algebra by the closed-unit embedding and compatible frame/bar models. Substitution \(g(t)\mapsto g(st)\) contracts the jet kernel compatibly with every nerve face and degeneracy; constant loops give its section. The unit algebra is therefore \(R\Gamma(B\mathbf G_m,\mathbf C)\). The circle universal bundle and its finite projective models give

\[
 H^*(B\mathbf G_m,\mathbf C)=\mathbf C[c],\qquad |c|=2 .
 \tag{SH.21}
\]

Its generator is normalized by \(c=-c_1(\gamma)\), evaluating to one on the complex-oriented projective line. The finite projective cell filtration has one cell in each even degree; its Gysin sequence multiplies consecutive even groups by this class, so the powers give precisely this polynomial ring and no odd groups. Thus the ambient degree-two unit morphism is nonzero, whereas (SH.20) is zero. The actual coefficient functor does not become a full derived equivalence by ind-extension. This example retains equivariance: the extra class vanishes after forgetting to the point, which is why computing only the underlying point Hom would miss it.

**Exercise 3.BA.** For \(G=GL_2\) and the standard minuscule coefficient \(P=IC_{(1,0)}\), compute the exchange on both convolution summands and then on the two coefficient shifts \(P[1],P[1]\).

**Solution 3.BA.** The actual two-step surface is the \(\mathbf F_2\) cone resolution. Its exceptional section has normal line \(\mathcal O(-2)\). The two maps from and to its central point have composite \(-2\); dividing the second by \(-2\) gives a retraction. The remaining strict-boundary summand is the largest IC. This is the explicit proof in convolution §10:

\[
 P\star P=IC_{(2,0)}\oplus IC_{(1,1)}.
 \tag{SH.22}
\]

Its cohomology basis has \(v_-\) in degree \(-1\) and \(v_+\) in degree \(1\). Raw geometric exchange is \(-\mathrm{flip}\). On the largest IC it has scalar \(-1\): that IC contains \(v_-\otimes v_-\), and all three symmetric tensor vectors are its cohomology. On the central point IC it has scalar \(+1\), with antisymmetric cohomology line. The component parity is one, so (SH.12) reverses those two scalars. The actual ordinary Satake exchange on the summands is therefore \(+1,-1\), respectively.

Each generator of the further coefficient shift \([1]\) has cochain degree \(-1\) relative to its heart coefficient. Equation (SH.5) contributes one more minus sign, separately from the component correction. On the shifted summands the scalars are

\[
 c'_{P[1],P[1]}:\quad -1\ \text{on }IC_{(2,0)}[2],
       \qquad +1\ \text{on }IC_{(1,1)}[2].
 \tag{SH.23}
\]

The total-cohomology degrees \(-1,1\) used to determine the raw geometric heart map are not the coefficient cochain degree used in this last shift calculation. Keeping those two gradings separate explains both signs. The unit has component and coefficient degree zero and retains its identity map.

**Exercise 3.BB.** Normalize a three-point coefficient family first along \(x_1=x_2\), then along the full diagonal, and finally at a point. Compare that route with direct point restriction, on both sheaves and D-modules.

**Solution 3.BB.** The three-point family carries its one base normalization \([3]\). The first collision has codimension one and changes it to the two-point family by ordinary restriction and shift \([-1]\). The next collision changes the two-point family to the one-point spread by another \([-1]\); restricting that spread to a selected point uses \([-1]\) again. Thus the route uses total shift \([-3]\) with its ordinary sheaf restriction. The block labels are \((P_1\star P_2)\star P_3\). Direct restriction to the selected three-tuple also uses \([-3]\).

On operators each step is the actual extraordinary inverse transfer and shift \([1]\), by (SH.11). The three normal parameter directions compose to codimension three:

\[
 i_{\vec x}^!\mathcal F_{3,D}[3]
     \simeq S_D\bigl((V_1\otimes V_2)\otimes V_3\bigr).
 \tag{SH.24}
\]

Universal local acyclicity changes the sheaf extraordinary restriction to ordinary restriction with shift \([-6]\); adding \([3]\) gives the same \([-3]\) as above. In the other association the label is \(V_1\otimes(V_2\otimes V_3)\). Both maps are the proper image of the same three-step chain with its ordered external coefficient. Proper composition and the actual convolution associator identify them, as proved in fusion equation (3.7). The four-step chain gives the pentagon. This calculation keeps every normal shift and applies the actual inverse-transfer comparison; its individual flat-frame period coefficients are not silently replaced by identities.

### 3.63. The parameter dualizing normalization

The ground and coefficient field in §§3.63–3.67 is \(\mathbf C\). Keep every connected reductive \(G\), genus and bundle component from §§3.59–3.62. Put

\[
 \mathcal C=\operatorname{Ind}D^b_{\rm dg}
              \operatorname{Rep}^{\rm fd}_{\mathbf C}(\widehat G),
 \qquad
 \mathcal R=\mathcal C_{\operatorname{Ran}}^{\rm dr},
 \qquad
 \mathcal M=\operatorname{Dmod}(Y),\quad Y=\operatorname{Bun}_G(X).
 \tag{RA.1}
\]

Here \(\mathcal R\) is the full category of (RN.7)–(RN.13), with every finite-set function, empty set, operator complex and localization morphism. It is rigid by (KG.19)–(KG.23). The coefficient category has compact unit and dualizable compacts: its finite complexes split as (SH.4), their duals reverse cochain degrees and take representation duals, and the two evaluation triangles hold with the complex tensor signs. Its ind-category is generated by these finite objects. Thus it satisfies the hypotheses used to construct \(\mathcal R\).

We now construct an actual action of this category, rather than an action only of its point coefficients. The finite-tuple functor (SH.16) has unit \(M\boxtimes\mathcal O_{X^I}\). Full D-module parameter calculus instead has unit \(\omega_{X^I}\). Define the normalized family

\[
 \widehat{\mathsf H}_I(\vec V;M)
       =\mathsf H_I(\vec V;M)[|I|],
 \qquad
 \widehat{\mathsf H}_{\emptyset}(M)=M .
 \tag{RA.2}
\]

The empty family uses the identity correspondence and its dualizing kernel. The structural maps in (RA.2) use the actual parameter dualizing comparisons, with their density and complex shift signs. One must not replace them by the permutation of \(|I|\) shifted vector-space generators alone.

For a collision of an \(r\)-point family into \(b\) blocks, (SH.11) and the full correspondence proof give

\[
 i^!\widehat{\mathsf H}_{r}(\vec V;M)
   \simeq
 \widehat{\mathsf H}_{b}
       \left(\bigotimes_{\rm block}\vec V;M\right),
 \qquad
 \widehat{\mathsf H}_{I}(\mathbf1,\ldots,\mathbf1;M)
       \simeq M\boxtimes\omega_{X^I}.
 \tag{RA.3}
\]

Indeed \(i^!\mathsf H_r[r]=\mathsf H_b[-(r-b)+r]=\mathsf H_b[b]\). For the second identity, (SH.18) shifts \(M\boxtimes\mathcal O_{X^I}\) by \([|I|]\). Both statements concern every unbounded \(M\). They use the actual inverse-transfer and proper base-change maps, not an RH comparison on \(M\).

We record the parameter permutation sign. In right-operator conventions the dualizing object of a smooth \(d\)-fold is its top density \(\Omega[d]\). For ordered curve coordinates \(x_1,\ldots,x_r\), use the density \(dx_1\wedge\cdots\wedge dx_r\). A permutation \(\sigma\) changes this frame by \(\operatorname{sgn}\sigma\). Its inverse-transfer density ratio contributes that same sign; the permutation of the \(r\) degree-minus-one suspension factors contributes another \(\operatorname{sgn}\sigma\). Their product is one. Side change to left modules uses the same contracted density in source and target, preserving this comparison. Consequently the parameter factor in (RA.3) has precisely its dualizing-unit permutation, with no extra permutation sign. The coefficient exchange remains the component correction (SH.12) and the coefficient cochain Koszul sign (SH.5). This computation includes unit labels; it would fail if one kept just the suspension-factor flip and omitted the density ratio.

To explain empty label fibres, consider a tuple containing a unit at one of the marked points. On the moving chain its unit coefficient is supported on the identity modification. Removing that step identifies the coefficient-supported chain with the shorter chain and its extra freely marked point. The proper endpoint image makes this identification on the entire operator coefficient. With (RA.2) the extra point contributes its dualizing object. The maps are the actual coefficient unit evaluation and inverse-transfer product comparison. They continue to hold when that extra point coincides with another marked point: the identity modification still does nothing, and its coefficient remains the actual unit section. This does not classify an infinitesimal Grassmannian by its reduced geometric points.

More generally let \(\alpha:I_1\to I_2\) be any function, and let
\(\Delta_\alpha:X^{I_2}\to X^{I_1}\) be its coordinate map. Tensor the coefficients over its fibres, inserting \(\mathbf1\) in each empty fibre. Then

\[
 (\operatorname{id}_Y\times\Delta_\alpha)^!
        \widehat{\mathsf H}_{I_1}(\vec V;M)
 \simeq
        \widehat{\mathsf H}_{I_2}
               (\operatorname{mult}^{\alpha}\vec V;M).
 \tag{RA.4}
\]

Factor \(\alpha\) as its surjection to its image followed by inclusion in \(I_2\). The coordinate map first forgets the unused coordinates, then repeats the coordinates of each fibre. The latter part is (RA.3); the former is the just-proved unit-label insertion, with its freely varying parameter dualizing factors. Permutations supply arbitrary orderings. This proves (RA.4) for every function, including maps from the empty set.

These are coherent maps, not just objectwise isomorphisms. Two successive functions tensor the same original labels over the fibres of their composite; an inserted empty-fibre unit is evaluated by the same unit triangle. Their common moving chain collapses the same intermediate bundles. All inverse transfers and proper images compose on that chain by the projective correspondence lemma. The coefficient associativity, unit and exchange maps have the entire enhanced relations proved in §3.59. Their extensions through finite complexes and colimits retain those relations. For an arbitrary arrow string, use the ordered uncollapsed chain and the same transfer tensor; faces compose its consecutive arrows and degeneracies insert their identity tensors. Transfer composition and its evaluation give the simplicial identities on these actual complexes. Thus longer strings retain their higher comparisons. This proves the coherent finite-set family used below.

### 3.64. The action with full D-module coefficients

Let \(\psi:I\to J\). Denote its coordinate map by
\(\Delta_\psi:X^J\to X^I\), and put

\[
 \begin{aligned}
 B_\psi(\vec V;M)
   &=(\operatorname{id}_Y\times\Delta_\psi)^!
                    \widehat{\mathsf H}_I(\vec V;M),\\
 p_{Y,J}&:Y\times X^J\to Y,\qquad
 p_{X,J}:Y\times X^J\to X^J .
 \end{aligned}
 \tag{RA.5}
\]

The output projection is \(p_{Y,J}\). Define the stage operation by

\[
 \Phi_\psi(\vec V,N;M)
   =(p_{Y,J})_*
          \left(B_\psi(\vec V;M)
                    \otimes^!p_{X,J}^!N\right),
 \qquad N\in\operatorname{Dmod}(X^J).
 \tag{RA.6}
\]

This uses the full unbounded category of parameter coefficients. No holonomicity, regularity, boundedness or external-product decomposition of \(N\) is required.

Every functor in (RA.6) exists on these full categories. The coordinate inverse image is the actual finite-transfer construction of §3.61. Pullback of \(N\) along the stack projection is defined on all smooth affine charts by inverse transfer and strong descent. The projection \(p_{Y,J}\) is representable projective since \(X^J\) is projective. The projective correspondence lemma proves its continuous unbounded direct image and the required base-change and projection maps, including singular finite coefficient supports. Tensor product is derived. For coefficients of arbitrary support, the finite-support Hecke functors are first constructed and then extended through their actual coefficient colimits as in (SH.7); no continuity of an unbounded ind-proper star image is assumed. These observations show joint continuity in \(\vec V,N,M\).

They also define an exact enhanced functor on the entire tensor-product stage
\(\mathcal A_\psi=\mathcal C^{\otimes I}\otimes\operatorname{Dmod}(X^J)\).
The multi-object free module bar (EP.1) presents that stage by its compact representables, which are exterior tensors of finite coefficient complexes and compact operator complexes. Applying (RA.6) to those complexes and their actual maps, then to the bar, gives its continuous extension. It is independent of a presentation by the representable augmentation contraction. In particular this is not a functor defined only on a set of simple coefficients.

We prove that these stage functors respect every transition in (RN.8). Take
\[
 \alpha:I_1\to I_2,\quad \beta:J_2\to J_1,\quad
 \psi_1=\beta\psi_2\alpha,
 \qquad
 b=\operatorname{id}_Y\times\Delta_\beta .
 \tag{RA.7}
\]

Coordinate inverse images compose contravariantly. Applying (RA.4) and then composing the coordinate maps gives

\[
 b^!B_{\psi_2}
       (\operatorname{mult}^{\alpha}\vec V;M)
          \simeq B_{\psi_1}(\vec V;M).
 \tag{RA.8}
\]

The map \(\Delta_\beta\) is the projective projection followed by a closed diagonal of (RN.5), even when \(\beta\) is not surjective. The square with \(p_{X,J_1}\) and \(p_{X,J_2}\) gives actual full base change

\[
 p_{X,J_2}^!(\Delta_\beta)_*N
        \simeq b_*p_{X,J_1}^!N .
 \tag{RA.9}
\]

Check this square on each smooth affine bundle chart; it is the projective comparison (SH.14) with input \(N\). Its coherent chart comparisons glue the displayed map. No quasi-compactness of \(Y\), or common bound on all its charts, is needed.

The projection formula and proper composition now yield the whole transition map:

\[
 \begin{aligned}
 &\Phi_{\psi_2}
       (\operatorname{mult}^{\alpha}\vec V,
                        (\Delta_\beta)_*N;M)\\
 &\quad\simeq
 (p_{Y,J_2})_*
       \left(B_{\psi_2}\otimes^!b_*p_{X,J_1}^!N\right)\\
 &\quad\simeq
 (p_{Y,J_2})_*b_*
       \left(b^!B_{\psi_2}\otimes^!p_{X,J_1}^!N\right)\\
 &\quad\simeq
 (p_{Y,J_1})_*
       \left(B_{\psi_1}\otimes^!p_{X,J_1}^!N\right)
   =\Phi_{\psi_1}(\vec V,N;M).
 \end{aligned}
 \tag{RA.10}
\]

In this calculation \(B_{\psi_2}\) has the coefficient of (RA.8). Every comparison is the actual operator transfer, tensor and evaluation map from the preceding proofs. There is no scalar replacement of the direct image of \(N\).

For a string of transitions the two routes use the same composite \(\alpha\), the same composite \(\beta\), and the same uncollapsed coefficient chain. Equations (RA.8)–(RA.10) use the coherent family maps of §3.63, transfer composition and projection evaluation. On semifree coefficient resolutions their augmented bars have the same inner faces, outer evaluation faces and identity degeneracies. Thus their higher string comparisons are retained too. The argument first applies to finite coefficient objects and full \(N,M\); continuity extends it to every coefficient object. This proves the compatible enhanced stage family.

The target category of continuous endofunctors is presentable. To see this here, use compact generation of \(\mathcal M\) proved in §§1.13–1.15 and a small DG category \(E\) of its compact generators. The free bar identifies \(\mathcal M\) with right \(E\)-modules. A continuous endofunctor is specified by the images of the representables, as a DG functor \(E\to\operatorname{Mod}_E\). Such a functor is an \(E\)-\(E\) bimodule. Its value on a general module is the corresponding balanced tensor bar; the representable augmentation proves both constructions inverse, including natural transformations and higher homotopies. Bimodule categories are full module categories, hence presentable. Applying the full colimit property proved in (RN.11)–(RN.13) to (RA.10) therefore constructs

\[
 \Phi:\mathcal R
     \longrightarrow\operatorname{End}_{\rm cont}(\mathcal M),
 \qquad
 \Phi(\operatorname{ins}_\psi(\vec V\otimes N))(M)
       =\Phi_\psi(\vec V,N;M).
 \tag{RA.11}
\]

Equivalently, apply that colimit property after tensoring every stage with \(\mathcal M\); tensor of presentable categories preserves colimits. The resulting action is continuous in both variables. We have constructed it on all stage morphisms and localization edges, not merely on their objects.

### 3.65. Composition, dual adjunctions and the global half twist

We prove the monoidal relation for the constructed functor. For two stages put

\[
 A_t=\operatorname{ins}_{\psi_t}(\vec V_t\otimes N_t),\qquad
 A_1\circledast A_2
  =\operatorname{ins}_{\psi_1\sqcup\psi_2}
       ((\vec V_1\boxtimes\vec V_2)\otimes(N_1\boxtimes N_2)).
 \tag{RA.12}
\]

This is disjoint union of the label and parameter sets, followed by exterior product of the parameter modules. It is not multiplication of two modules on the same \(X^J\) followed by a separate integration at that stage.

First take finite coefficient objects, retaining arbitrary \(N_1,N_2,M\). Apply (RA.6) twice. Before taking endpoint images its two steps are the correspondence of a chain
\[
 E_0\xrightarrow{I_2}E_1\xrightarrow{I_1}E_2,
 \qquad \text{parameters }X^{J_1}\times X^{J_2}.
 \tag{RA.13}
\]

Pull the inner proper image through the outer inverse transfer using (SH.14). Pull its parameter module through the same Cartesian square, and use the projection formula to put both parameter modules on the chain. Their tensor is the inverse image of \(N_1\boxtimes N_2\). Proper composition, first in the intermediate bundle and then in the projective parameter factors, replaces the iterated image by the endpoint image of this chain. These are comparisons of the actual full operator complexes; both arbitrary parameter modules remain in the calculation.

The coefficient on that chain is the composed finite-support coefficient kernel of §3.61. The normalized family of its disjoint blocks has shift \([|I_1|+|I_2|]\), equal to the sum of their two shifts in (RA.2). The inverse-transfer product comparison identifies its density with the density of the product parameter space. There is no repeated copy of a parameter-space unit: the two parameter blocks are distinct before restriction. Restricting by \(\Delta_{\psi_1}\times\Delta_{\psi_2}\) produces the coordinate restrictions in (RA.12). The actual coefficient block exchange of §3.59 identifies the ordered chain \(I_2,I_1\) with the coefficient of \(I_1\sqcup I_2\). It includes the component-adjusted exchange and the cochain signs, and the parameter comparison is the dualizing comparison of §3.63. Thus the preceding calculation gives

\[
 \begin{aligned}
 \Phi(A_1)\Phi(A_2)(M)
  &\simeq(p_{Y,J_1\sqcup J_2})_*
    \left(B_{\psi_1\sqcup\psi_2}
               (\vec V_1\boxtimes\vec V_2;M)
         \otimes^!p_{X,J_1\sqcup J_2}^!(N_1\boxtimes N_2)\right)\\
  &=\Phi(A_1\circledast A_2)(M).
 \end{aligned}
 \tag{RA.14}
\]

The full unbounded input comparison in (SH.14) proves this calculation without a cohomological bound on any input. Coefficient colimits then extend it to arbitrary coefficient objects; all displayed operations are jointly continuous. Exterior compact generators and their bar presentations extend it from exterior stage inputs to every object of each stage tensor product.

For three inputs both parenthesizations of (RA.14) use the uncollapsed chain \(I_3,I_2,I_1\), the same three parameter modules and the same block permutation to \(I_1,I_2,I_3\). On that chain, inverse transfers compose by balanced tensor, proper images compose by their augmented transfer bars, and tensor evaluation is the same evaluation before any pushforward. Their associativity maps agree by the bar face identities. The coefficient associativity and block-exchange relations agree by the enhanced relations of §3.59. For four inputs this identifies the five routes around the pentagon with that same four-step transfer and coefficient comparison. For an arbitrary string it identifies each face with contraction of its adjacent steps; inserting an identity step gives the degeneracy, whose evaluation triangle supplies the simplicial identities. Hence these are the coherent monoidal comparisons, including all higher strings.

They commute with transitions (RA.10). Indeed the combined transition has the disjoint unions of the two \(\alpha\)'s and the two \(\beta\)'s. Both routes pull back and push forward the same chain and parameter modules, and evaluate the same transfer tensors. This proves compatibility on each generator of the stage localization relations and on its coherent strings. The full colimit construction in (RN.11)–(RN.13) and joint continuity consequently extend (RA.14) to every pair of objects of \(\mathcal R\).

At the empty stage the output projection is the identity of \(Y\), the Hecke kernel is its unit, and the inverse image of the scalar unit is \(\omega_Y\). Therefore

\[
 \begin{gathered}
 \Phi(\mathbf1_{\mathcal R})=\operatorname{Id}_{\mathcal M},
 \\
 \mathcal R\otimes\mathcal M\longrightarrow\mathcal M,\quad
 (A,M)\longmapsto\Phi(A)(M),\\
 \quad\text{is a continuous unital module action}.
 \end{gathered}
 \tag{RA.15}
\]

Removing this empty step in (RA.13) is the transfer evaluation triangle and the coefficient unit triangle. It proves both unit constraints and their compatibility with associativity. The symmetric coefficient exchange supplies an exchange map between the two composites in the image of \(\Phi\). No symmetry of the whole category of continuous endofunctors under composition is being asserted.

Rigidity supplies a useful full adjunction. If \(A\) is compact in \(\mathcal R\), use its actual dual, evaluation and coevaluation from §3.53 and apply the action to their maps. For a map \(\Phi(A)M\to T\), insert coevaluation into \(M\), then apply that map after \(\Phi(A^\vee)\). Conversely, apply \(\Phi(A)\) to a map \(M\to\Phi(A^\vee)T\), then evaluate. The two module triangles and the two duality triangles prove these constructions inverse, on the mapping complexes and their homotopies. Thus

\[
 \operatorname{RHom}_{\mathcal M}(\Phi(A)M,T)
   \simeq
 \operatorname{RHom}_{\mathcal M}(M,\Phi(A^\vee)T),
 \qquad
 \Phi(A)\dashv\Phi(A^\vee).
 \tag{RA.16}
\]

Both functors are continuous by construction. If \(M\) is compact, the right side of (RA.16) preserves colimits in \(T\); hence \(\Phi(A)M\) is compact. This proves preservation of compacts for every compact Ran coefficient, including compact nonholonomic parameter modules. It does not require arbitrary inverse images of coherent operator modules to be coherent.

Let \(\mathcal M_L\) be the global half-twisted category of §3.56 and \(\mathcal T_Y:\mathcal M_L\to\mathcal M\) its actual operator Morita equivalence. Define

\[
 \Phi^L(A)=\mathcal T_Y^{-1}\Phi(A)\mathcal T_Y .
 \tag{RA.17}
\]

The middle \(\mathcal T_Y\mathcal T_Y^{-1}\) in two successive factors cancels by the actual \(P\)-\(Q\) tensor evaluation (RH.17), before taking endpoint images. The same evaluation identifies each longer factor with the same transported chain. Unit, multiplication, transition and duality comparisons in (RA.15)–(RA.16) are therefore transported with all coherences. This proves the continuous unital full Ran action on the normalized global half twist, on every genus and bundle component. No flat connection on the half-root line is chosen.

This action admits arbitrary derived scalar parameters. If \(A\) is a commutative DG \(\mathbf C\)-algebra, write

\[
 \mathcal R_A=\mathcal R\otimes_{\mathbf C}\operatorname{Mod}_A,
 \qquad
 \mathcal M_{L,A}=\mathcal M_L\otimes_{\mathbf C}\operatorname{Mod}_A,
 \qquad
 \Phi^L_A:\mathcal R_A\otimes_{\operatorname{Mod}_A}
                    \mathcal M_{L,A}\longrightarrow\mathcal M_{L,A}.
 \tag{RA.18}
\]

On free \(A\)-modules use (RA.17) tensored with \(A\), and on arbitrary \(A\)-modules use the full free-module bar of (KF.1) and (EP.1). Its augmentation contracts by inserting the first unit. The tensor and transfer maps of the action are \(\mathbf C\)-linear, so their scalar extensions define the maps of this bar, with its \(A\)-module faces and total differential. This constructs (RA.18) on the entire derived module categories. Units, composition maps and their higher relations are scalar extensions of the same bar maps; the augmentation contraction proves independence of free presentations. No flatness, finite dimensionality or cohomological bound on \(A\) is used. This extends the scalar parameters of the proved complex geometry; it does not change the geometric ground field to an arbitrary characteristic-zero field.

### 3.66. The actual universal enhanced Ran Hecke category

The action just proved lets us apply the regular-algebra construction to an actual geometric module category. Set

\[
 \mathcal B=\mathcal R\otimes\mathcal R,\qquad
 \mathcal N=\mathcal M_L\otimes\mathcal R,\qquad
 (A\boxtimes B)\star(M\boxtimes C)
       =\Phi^L(A)M\boxtimes(B\circledast C).
 \tag{RA.19}
\]

Exterior generators and the full free bar extend this formula to the entire categories. The two actions commute because they occur in the two separate factors, and (RA.15) supplies the first action's actual module relations. Denote multiplication of \(\mathcal R\) by \(\mu\), and its continuous right adjoint from §3.42 by \(r\). By (KG.23) its actual regular algebra is

\[
 R_{\mathcal R}=r(\mathbf1)
     \simeq\int^{B\in\mathcal R^c}B^\vee\boxtimes B,
 \qquad
 \mathcal H_{\rm univ}
       =\operatorname{Fun}^{\rm L}_{\mathcal B}(\mathcal R,\mathcal N)
       \simeq\operatorname{Mod}_{R_{\mathcal R}}(\mathcal N).
 \tag{RA.20}
\]

All hypotheses of (EP.6)–(EP.8) are now specified: the actual full rigid category \(\mathcal R\), its regular commutative algebra, the actual geometric first action, and the regular second action. In particular (RA.20) defines a presentable category of full enhanced module functors. The coend is over the entire compact DG category, including finite cones, retracts and localization morphisms.

For clarity, its induction and forgetful maps are

\[
 U(F)=F(\mathbf1),\qquad
 L(n)(B)=r(B)\star n,\qquad
 UL(n)=R_{\mathcal R}\star n,
 \qquad L\dashv U.
 \tag{RA.21}
\]

The adjunction maps are the unit and counit of \(\mu\dashv r\), under precomposition, as proved explicitly in (EP.7). Its monad multiplies the regular algebra by the lax multiplication whose mate is the multiplication of the two counits. The module equivalence in (RA.20) uses the realized free action bar of (EP.8); its augmentation contracts after \(U\), by the first unit insertion. Since \(U\) preserves colimits and is conservative, that contraction proves the equivalence on every object, all morphisms and all action homotopies.

If \(c_i\) are compact generators of \(\mathcal M_L\) and \(B_j\) compact generators of \(\mathcal R\), then

\[
 \begin{gathered}
 \operatorname{RHom}_{\mathcal H_{\rm univ}}
             (L(c_i\boxtimes B_j),F)
     \simeq
 \operatorname{RHom}_{\mathcal N}(c_i\boxtimes B_j,U(F)),\\
 \{L(c_i\boxtimes B_j)\}_{i,j}
       \text{ compactly generates }\mathcal H_{\rm univ}.
 \end{gathered}
 \tag{RA.22}
\]

Indeed exterior compact generators compactly generate \(\mathcal N\) by the multi-object tensor bar. Continuity of \(U\) proves compactness of the left-hand sources. Vanishing of all displayed mapping complexes forces \(U(F)=0\), then \(F=0\) by conservativity. This tests every unbounded object. One cannot discard all the \(B_j\)'s and use only the unit without proving that the unit generates \(\mathcal R\).

The balancing map (EP.5) supplies, with tensor-compatible higher relations,

\[
 \Phi^L(A)\star_{\rm first}U(F)
      \simeq A\star_{\rm second}U(F).
 \tag{RA.23}
\]

Thus (RA.20) is an actual universal enhanced Ran Hecke category. Its second factor is \(\mathcal R\) with its regular action. To obtain the geometric spectral category one must still construct its continuous symmetric monoidal coefficient functor to the appropriate local-systems category and prove the required base-change and image comparisons. Neither (RA.20) nor its free induction is asserted to be an idempotent Beilinson projector. Nilpotent regularity, the projector's singular-support image, the independent microlocal support comparison and derived tempered Satake remain unproved here. The full action of §§3.63–3.66 has complex geometric ground field; its extension to arbitrary characteristic-zero geometric ground fields also remains required.

The finite-set description and the Hecke family formula also appear in [Arinkin, Gaitsgory, Kazhdan, Raskin, Rozenblyum and Varshavsky, *The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support*, free preprint v2](https://arxiv.org/abs/2010.01906v2), §§11.1 and 15.1.

![Figure3.19. Every finite-set transition, the full operator-valued Ran Hecke action and its dual adjunction.](figures/full-unital-ran-action.svg)

*Figure3.19.* The upper panel gives the dualizing family normalization (RA.2)–(RA.4). The finite-set square records the opposite direction of \(\beta\) and the exact repeated-coordinate map of Solution3.BC. The action panel projects to \(Y=\operatorname{Bun}_G(X)\), keeps every full parameter module, and shows the proper transition (RA.10). The lower panels give compact dual adjunction, actual half-twist transport and the universal enhanced category. The diagrams are schematic; the shifts, map domains and category factors are exact. Proofs are in §§3.63–3.66, and Solutions3.BC–3.BE test forgotten coordinates, the graded triangles and nonholonomic inputs.

### 3.67. Unused coordinates, point adjunctions and nonholonomic coefficients

**Exercise 3.BC.** Take \(I_1=\{u,v\}\), \(J_1=\{a,b,c\}\), with \(\psi_1(u)=\psi_1(v)=a\). Take \(I_2=\{w\}\), \(J_2=\{d,e\}\), with \(\psi_2(w)=d\). Let \(\alpha(u)=\alpha(v)=w\) and \(\beta(d)=\beta(e)=a\). Write the coordinate transition and family comparison, including both unused source coordinates. Then take \(X=\mathbf P^1_{\mathbf C}\) and \(N=\mathcal D_{X^3}\); calculate its transition coefficient.

**Solution 3.BC.** The label identity is \(\psi_1=\beta\psi_2\alpha\), and the coordinate map is

\[
 \Delta_\beta:X^3\to X^2,\qquad
 (x_a,x_b,x_c)\longmapsto(x_a,x_a),
 \qquad
 \Delta_\beta=i_{\rm diag}\circ\operatorname{pr}_a.
 \tag{RA.24}
\]

The coordinates \(b,c\) are unused, while the target coordinates \(d,e\) coincide. Write \(F=\widehat{\mathsf H}_{\{w\}}(V_u\otimes V_v;M)\). The \(e\)-coordinate has a unit label, so \(B_{\psi_2}=F\boxtimes\omega_{X_e}\). On \(Y\times X^2\) this is \((\operatorname{id}_Y\times\operatorname{pr}_d)^!F\). Since the diagonal is a section of that projection, composition of actual inverse transfers gives
\(i_{\rm diag}^!(F\boxtimes\omega_{X_e})=F\), for every full \(F\). Pullback through \(\operatorname{pr}_a\) then gives

\[
 b^!B_{\psi_2}=F\boxtimes\omega_{X_b}\boxtimes\omega_{X_c}
                  =B_{\psi_1}.
 \tag{RA.25}
\]

There is no further diagonal shift: it has already been absorbed by (RA.2). For the specified \(N\), the product PBW identification gives
\(\mathcal D_{X^3}=\mathcal D_{X_a}\boxtimes\mathcal D_{X_b}\boxtimes\mathcal D_{X_c}\).
Equation (GD.9), or its one-form Čech calculation, gives
\((p_X)_*\mathcal D_X=\mathbf C[-1]\).
The two forgotten factors therefore give

\[
 (\operatorname{pr}_a)_*N=\mathcal D_{X_a}[-2],
 \qquad
 (\Delta_\beta)_*N=(i_{\rm diag})_*\mathcal D_X[-2].
 \tag{RA.26}
\]

These are operator modules, not their fibres. Substituting (RA.25) and (RA.26) into (RA.10) verifies the two action formulas agree, with the shift \([-2]\). The order filtration has characteristic support \(T^*X^3\) of dimension six; \(N\) is therefore nonholonomic on the three-dimensional base. For arbitrary \(N\), the same transition holds by full base change and projection formula, without assuming this exterior-product calculation.

**Exercise 3.BD.** Let \(G=\mathbf G_m\), let \(V_n\) be the dual-torus character of weight \(n\), and let \(x\in X(\mathbf C)\). Insert \(A_{n,p}=V_n\otimes\delta_x[p]\) at the identity one-label stage. Identify its action and its right adjoint. Check both triangle signs when \(p\) is odd.

**Solution 3.BD.** Write \(i_x:Y\to Y\times X\). Proper projection and the projection formula for the closed point give
\(\Phi(A_{n,p})M=i_x^!\widehat{\mathsf H}_1(V_n;M)[p]\).
The one-point restriction normalization (RA.2) identifies the unshifted expression with the fixed-point Hecke operator \(\mathsf H_{n,x}\). The point module is self-dual by proper coherent duality from the point; the character dual has weight \(-n\). Hence

\[
 A_{n,p}^{\vee}=A_{-n,-p},\qquad
 \Phi(A_{n,p})=\mathsf H_{n,x}[p],\qquad
 \mathsf H_{n,x}[p]\dashv\mathsf H_{-n,x}[-p].
 \tag{RA.27}
\]

Here the unshifted torus coefficient is supported on its actual coweight modification, whose inverse modification has weight \(-n\). Composing them contracts the common intermediate bundle to the identity chain, so its two unshifted coefficient evaluations satisfy the two unit triangles. For the additional shift take generators \(e,e^\vee\) of degrees \(-p,p\). Coevaluation is \(1\mapsto e\otimes e^\vee\); reversed evaluation is \((-1)^p\), and its preceding exchange contributes \((-1)^p\). Each triangle has product \((-1)^{2p}=1\), including odd \(p\), exactly as in (KG.24). Transport by \(\mathcal T_Y\) gives the same actual adjunction on the global half twist.

**Exercise 3.BE.** At the stage \(\emptyset\to\{j\}\), with \(X=\mathbf P^1_{\mathbf C}\), compute the action of \(N=\mathcal D_X\), \(N=\omega_X\) and \(N=\mathbf k_X\). Explain why replacing every full parameter coefficient by a rank-one constant sheaf changes the action.

**Solution 3.BE.** The empty coefficient family is \(M\), and its coordinate inverse image is \(p_{Y,\{j\}}^!M\). The full projective product comparison consequently gives

\[
 \begin{aligned}
 \Phi_{\emptyset\to\{j\}}(N;M)&=M\otimes_{\mathbf C}(p_X)_*N,\\
 \Phi_{\emptyset\to\{j\}}(\mathcal D_X;M)&=M[-1],\\
 \Phi_{\emptyset\to\{j\}}(\omega_X;M)&=M[2]\oplus M,\\
 \Phi_{\emptyset\to\{j\}}(\mathbf k_X;M)&=M\oplus M[-2].
 \end{aligned}
 \tag{RA.28}
\]

For the first line, use \(p_{Y}^!M=M\boxtimes\omega_X\) and \(p_X^!N=\omega_Y\boxtimes N\); their !-tensor is \(M\boxtimes N\) because both dualizing factors are the tensor units. Proper product pushforward integrates just \(N\). The remaining lines are (GD.7) and (GD.9), whose Čech representatives are the constant class and \(dt/t\), with the stated normalized shifts. The operator module \(\mathcal D_X\) is compact and nonholonomic, with full cotangent characteristic support. It gives a single shift rather than either of the two constant/dualizing cohomology sums. Finally the actual diagram arrow from \(\emptyset\to\{j\}\) to \(\emptyset\to\emptyset\) has \(\beta:\emptyset\to\{j\}\), so its coordinate pushforward is \(N\mapsto(p_X)_*N\). It identifies (RA.28) with the scalar empty-stage action. This checks the empty-label transition itself, not just a calculation of its dimensions.

### 3.68. The tautological de Rham spectral coefficient

In §§3.68–3.72 the geometric and coefficient field is \(\mathbf C\). Keep the full categories \(\mathcal C,\mathcal R,\mathcal M_L\) of (RA.1) and (RA.17). We use the tensor-functor definition of the derived de Rham local-systems prestack. For a connective commutative DG \(\mathbf C\)-algebra \(A\), put

\[
 \begin{gathered}
 \mathcal D_A(X)=\operatorname{Dmod}(X)\otimes_{\mathbf C}\operatorname{Mod}_A,\\
 \mathcal Z=\operatorname{LocSys}^{\rm dR}_{\widehat G}(X),\qquad
 \mathcal Z(A)=
   \left(\operatorname{Fun}^{\otimes,{\rm L},\,{\rm right}\ t{\rm\text{-}exact}}
        (\mathcal C,\mathcal D_A(X))\right)^{\simeq}.
 \end{gathered}
 \tag{SPC.1}
\]

The superscript \(\simeq\) means the entire maximal infinity-groupoid, not the set of isomorphism classes. A point includes its coherent tensor maps, unit, symmetry and higher relations. The target uses !-tensor with unit \(\omega_X\otimes_{\mathbf C}A\). Right \(t\)-exact means that the functor carries connective objects of the standard representation \(t\)-structure to connective objects of the D-module \(t\)-structure with derived \(A\)-coefficients. No representability or finite-type theorem for \(\mathcal Z\) is used below.

The definition supplies a tautological functor for every point \(z\in\mathcal Z(A)\), and a canonical comparison for every arrow \((A,z)\to(B,z')\) of affine points:

\[
 E_z:\mathcal C\longrightarrow\mathcal D_A(X),\qquad
 E_{z'}(V)\simeq E_z(V)\otimes_A^L B.
 \tag{SPC.2}
\]

Here \(z'\) is the specified pullback point, including the specified path to that pullback. A path of tensor functors gives a path of the corresponding coefficient functors; every higher path is retained. Thus (SPC.2) is defined by evaluation on a groupoid, not by choosing one representative of each point.

For a finite label set \(I\), let \(E_z^I\) be its exterior family with all tensor products over \(A\). The full exterior operator comparison (RN.9), followed by the scalar module bar of (KF.1), places it in \(\mathcal D_A(X^I)\). If \(\alpha:I_1\to I_2\), its coordinate inverse transfer gives

\[
 \Delta_\alpha^!E_z^{I_1}(\vec V)
      \simeq E_z^{I_2}(\operatorname{mult}^{\alpha}\vec V),
 \qquad E_z^\emptyset(\mathbf1)=A.
 \tag{SPC.3}
\]

To prove this, first take a surjection \(\alpha\). Its diagonal inverse image is precisely the definition of !-tensor of the factors in each fibre. The coherent tensor map of \(E_z\) therefore identifies those factors with \(E_z\) of their representation tensor. For an inclusion, coordinate pullback adds the dualizing unit at each unused coordinate; its coefficient is \(E_z(\mathbf1)=\omega_X\otimes A\). Factor any function as the surjection to its image followed by inclusion, and use permutations to order its fibres. The operator unit comparison includes the density and suspension signs of §3.63. This proves (SPC.3) for every function, including empty label fibres and maps from the empty set. The associativity, symmetry and unit constraints of the specified tensor functor, composed with the actual inverse-transfer comparisons, identify the maps for composites. On longer strings the ordered exterior tensor and its successive diagonal evaluations give the same bar faces and identity degeneracies. Their tensor and transfer identities give all higher comparisons.

This construction does not use a Riemann–Hilbert comparison on the full coefficient category. In particular an arbitrary parameter module will remain an operator module in the spectral operation.

### 3.69. The full spectral Ran functor and derived base change

Let \(\psi:I\to J\), let \(N\in\operatorname{Dmod}(X^J)\), and write \(N_A=N\otimes_{\mathbf C}A\). Define

\[
 F_{z,\psi}(\vec V,N)=
   (p_{X^J})_*
       \left(\Delta_\psi^!E_z^I(\vec V)\otimes_A^!N_A\right)
       \in\operatorname{Mod}_A,\qquad p_{X^J}:X^J\to\mathrm{pt}.
 \tag{SPC.4}
\]

The inverse image and !-tensor are the actual full operator operations; the latter tensor is relative to \(A\). The structure map is projective. The projective correspondence lemma (SH.14) constructs its direct image, base-change and projection formula on arbitrary unbounded operator complexes. Scalar extension by \(A\) is the derived module bar of (KF.1): on a semifree \(A\)-presentation use those same \(\mathbf C\)-linear transfer maps, then realize. Its unit insertion contracts the augmentation. Consequently (SPC.4) is an enhanced functor on the full stage \(\mathcal C^{\otimes I}\otimes\operatorname{Dmod}(X^J)\), continuous in both inputs.

For a transition \(\alpha:I_1\to I_2\), \(\beta:J_2\to J_1\), \(\psi_1=\beta\psi_2\alpha\), equation (SPC.3) supplies

\[
 \Delta_\beta^!\Delta_{\psi_2}^!
          E_z^{I_2}(\operatorname{mult}^{\alpha}\vec V)
       \simeq\Delta_{\psi_1}^!E_z^{I_1}(\vec V).
 \tag{SPC.5}
\]

Put \(Q=\Delta_{\psi_2}^!E_z^{I_2}(\operatorname{mult}^{\alpha}\vec V)\). Since \(\Delta_\beta\) is a projective projection followed by a closed diagonal, the full projection formula and proper composition give

\[
 \begin{aligned}
 F_{z,\psi_2}(\operatorname{mult}^{\alpha}\vec V,(\Delta_\beta)_*N)
    &=(p_{X^{J_2}})_*
            \left(Q\otimes_A^!(\Delta_\beta)_*N_A\right)\\
    &\simeq(p_{X^{J_2}})_*(\Delta_\beta)_*
            \left(\Delta_\beta^!Q\otimes_A^!N_A\right)\\
    &\simeq(p_{X^{J_1}})_*
            \left(\Delta_{\psi_1}^!E_z^{I_1}(\vec V)
                                 \otimes_A^!N_A\right).
 \end{aligned}
 \tag{SPC.6}
\]

Each displayed map is the actual transfer evaluation or projection map. Two successive transitions use the same composite \(\alpha\), composite \(\beta\), diagonal tensor map and proper image. The corresponding augmented transfer bars have the same faces, identity degeneracies and evaluation augmentations. This proves compatibility for coherent strings. The full Ran localization construction of (RN.11)–(RN.13) therefore supplies

\[
 F_z:\mathcal R\longrightarrow\operatorname{Mod}_A,\qquad
 F_z(\operatorname{ins}_\psi(\vec V\otimes N))
      =F_{z,\psi}(\vec V,N).
 \tag{SPC.7}
\]

It respects every localization edge and higher relation; it is not just a rule on inserted objects.

We next prove that \(F_z\) is symmetric monoidal. Disjoint union gives the exterior product of two coefficients \(E_z^I\) and two parameter modules. The two normalized parameter units are the exterior factors of the single product dualizing unit. Proper Fubini then identifies the direct image of that exterior product with the derived \(A\)-tensor of the two direct images:

\[
 F_z(B_1\circledast B_2)
        \simeq F_z(B_1)\otimes_A^L F_z(B_2),\qquad
 F_z(\mathbf1_{\mathcal R})=A.
 \tag{SPC.8}
\]

Here is the full unbounded product comparison. Choose finite affine covers of the two projective products of curves. The relative Spencer direction has finite length, and each Čech direction has finite length. On exterior affine terms the transfer comparison is the balanced tensor of the two transfer tensors, with the complex Koszul sign. Tensoring the two finite Čech–Spencer complexes gives their product total complex. Finite horizontal lengths mean that only finitely many horizontal degrees enter a given total degree; no convergence of an infinite first-quadrant spectral sequence is used. Resolve the remaining \(A\)-module inputs by their semifree bars. Derived \(A\)-tensor and direct image preserve their realizations, so the affine comparison extends to every unbounded input. The proper product comparison is exactly its global augmentation. This proves the first map in (SPC.8). At the empty stage the structure map is the identity point and the unit is \(A\), proving the second.

Associativity, symmetry and the unit maps in (SPC.8) are those of the same exterior coefficient and transfer tensor before image. For three and four blocks every route contracts the same ordered product tensor. The associativity pentagon and exchange hexagons are the tensor relations of \(E_z\) and the complex tensor relations of the transfers. Higher strings are the augmented bar strings with their identity degeneracies. Compatibility with (SPC.6) follows from that same product transfer evaluation. Joint continuity and the full Ran colimit extend these comparisons to all objects of \(\mathcal R\). This proves the asserted symmetric monoidal functor.

For an arbitrary morphism of affine spectral points \((A,z)\to(B,z')\), use (SPC.2) in (SPC.4). The Spencer, finite Čech and derived module bars yield the actual comparison

\[
 F_z(T)\otimes_A^L B\simeq F_{z'}(T),\qquad T\in\mathcal R.
 \tag{SPC.9}
\]

All tensor products in this argument are derived. A semifree presentation over \(A\) supplies the map even when \(B\) is not flat. Finite horizontal lengths let scalar extension pass through the finite transfer directions; the bar realization supplies every remaining unbounded input degree. Two scalar maps give the same composed tensor bar, and paths of points give the same evaluated paths. Thus (SPC.9) has the entire coherent affine-point comparison, without a flatness or boundedness assumption on the map.

The same construction has an \(A\)-linear extension on \(\mathcal R\otimes\operatorname{Mod}_A\): on exterior generators it sends \(T\otimes Q\) to \(F_z(T)\otimes_A^LQ\). Resolve an arbitrary object by the exterior generator bar and realize this rule. Its unit insertion contracts the augmentation, and the balanced tensor identities give its maps and all bar relations. The two orders of applying that bar and the scalar bar \(A\to B\) have the same bisimplicial realization. Hence (SPC.9) also holds for the entire \(A\)-linear extension and its actual pulled-back objects; it does not replace a derived fibre by its degree-zero quotient.

If \(T\) is compact in \(\mathcal R\), it is dualizable by (KG.22). Applying the strong symmetric monoidal functor (SPC.8) to its two evaluation triangles shows that \(F_z(T)\) is dualizable over \(A\). This implies it is compact: its mapping complex is
\(\operatorname{RHom}_A(A,F_z(T)^\vee\otimes_A-)\), which preserves colimits since the unit \(A\) is compact. A compact \(A\)-module is a retract of a finite semifree module by the module bar and compact factorization through its finite cell stages. Therefore

\[
 T\in\mathcal R^c\quad\Longrightarrow\quad
 F_z(T)\in\operatorname{Perf}(A),\qquad
 F_z(T^\vee)=F_z(T)^\vee.
 \tag{SPC.10}
\]

The argument includes compact nonholonomic parameter modules. It does not assume their geometric fibres have finite-dimensional underlying operator modules.

### 3.70. Gluing the actual spectral coefficient functor

Quasicoherent complexes on a prestack are coherent Cartesian families over its derived affine points. The index is the opposite of affine schemes over \(\mathcal Z\). Throughout, an arrow of points labelled by algebras \(A\to B\) means the scheme arrow \(\operatorname{Spec}B\to\operatorname{Spec}A\) and its specified spectral path. Thus in the present case

\[
 \operatorname{QCoh}(\mathcal Z)
       =\lim_{(A,z)\in(\operatorname{Aff}/\mathcal Z)^{\rm op}}
                        \operatorname{Mod}_A,\qquad
 \mathsf{Loc}(T)_z=F_z(T).
 \tag{SPC.11}
\]

The transition functor in this diagram is derived scalar extension. The limit includes every morphism of affine points and every higher path. Formula (SPC.9) and its coherent comparisons consequently make the right-hand expression an object of that limit, for every \(T\), and make its mapping-complex and higher functorial maps Cartesian too. The tensor maps (SPC.8) are Cartesian by their transfer construction. They therefore glue to

\[
 \mathsf{Loc}:\mathcal R\longrightarrow
          \operatorname{QCoh}(\mathcal Z)
     \quad\text{continuous symmetric monoidal},\qquad
 \mathsf{Loc}(\mathbf1)=\mathcal O_{\mathcal Z}.
 \tag{SPC.12}
\]

Continuity can be checked directly on Cartesian families: their colimits are the pointwise module colimits, because every transition is derived tensor and preserves colimits. Each \(F_z\) preserves colimits, so the glued family does too. Similarly the symmetric tensor and unit are pointwise tensor and unit, with their coherent comparisons. A family of equivalences is an equivalence in the limit, proving the tensor comparisons of (SPC.12). No algebraicity theorem for \(\mathcal Z\), or interchange of an ind-completion and a limit over its points, enters this construction.

We will use a categorical limit comparison for full compactly generated categories. If \(\mathcal P=\operatorname{Mod}_E\), where \(E\) is its small compact-generator DG category, its presentable dual is \(\operatorname{Mod}_{E^{\rm op}}\). Evaluation is balanced tensor over \(E\); coevaluation is its regular bimodule. On representables both duality triangles are the representable tensor augmentation. Its unit insertion contracts the entire augmented bar. Realization extends this to all objects, morphisms and higher maps, proving both triangles on the full unbounded module categories. Hence tensor by \(\mathcal P\) has both adjoints, given by tensor by its dual, and preserves limits as well as colimits. Applying this proved comparison to the full compactly generated \(\mathcal R\) and \(\mathcal M_L\) gives

\[
 \begin{aligned}
 \mathcal R\otimes\operatorname{QCoh}(\mathcal Z)
       &\simeq\lim_{(A,z)}(\mathcal R\otimes\operatorname{Mod}_A),\\
 \mathcal M_L\otimes\operatorname{QCoh}(\mathcal Z)
       &\simeq\lim_{(A,z)}\mathcal M_{L,A}.
 \end{aligned}
 \tag{SPC.13}
\]

These are comparisons of full presentable categories using their actual duals. They do not commute a bounded coherent or perverse ind-completion through a prestack limit. In particular a Cartesian family of operator-valued spectral coefficients retains every affine point and its higher descent data.

The continuous limit in (SPC.11) may equivalently be constructed as the Cartesian coherent section category. One chooses a common accessibility cardinal for the small affine-point diagram in the chosen larger universe. Lax coherent sections are the section module category obtained from the free path bar on that diagram. Requiring each transition's cone to vanish defines its Cartesian subcategory. This is an accessible condition: each cone is an accessible functor, and zero objects form an accessible subcategory; the set of transition conditions admits the same enlarged cardinal. Pointwise colimits remain Cartesian since the transition functors preserve colimits. An accessible category with these colimits is presentable, and its full enhanced section maps supply the limit. This also explains why pointwise colimits in the Cartesian-family description agree with its continuous category limit. Higher sections are represented by the same augmented path bar, so the construction does not replace the affine-point infinity-category by its homotopy category.

The accessibility assertion can be seen from presentations, rather than inferred from a finite diagram. Enlarge the regular cardinal to dominate the sizes of the diagram, its path simplices, its algebra presentations and the functors' accessibility bounds. A section is a filtered union of presentations of that size. To approximate a Cartesian section, enlarge a presentation successively to include the images of its generators under each transition, inverse maps for the specified transition equivalences, and homotopies for the two inverse identities. Repeat for every higher simplex and relation. Each step adds fewer generators and relations than the chosen enlarged bound; a regular enlargement bounds the union of this sequence as well. The resulting presentations are Cartesian, their maps retain the chosen homotopies, and their filtered union is the original section. The same enlargement for a set of maps and homotopies gives the mapping version. Thus the Cartesian sections form an accessible full category. Together with the already proved pointwise colimits this is the definition of presentability. This argument proves presentability and the limit comparison; it does not assert compact generation of global quasicoherent complexes or compactness of their unit.

### 3.71. The actual enhanced spectral category and its affine generators

Use the proved geometric first action (RA.17) and the actual spectral functor (SPC.12) to set

\[
 \begin{gathered}
 \mathcal B=\mathcal R\otimes\mathcal R,\qquad
 \mathcal N_{\mathcal Z}
       =\mathcal M_L\otimes\operatorname{QCoh}(\mathcal Z),\\
 (T\boxtimes S)\star(M\boxtimes Q)
       =\Phi^L(T)M\boxtimes(\mathsf{Loc}(S)\otimes Q),\\
 \mathfrak R_{\mathcal Z}
       =(\operatorname{Id}_{\mathcal R}\otimes\mathsf{Loc})(R_{\mathcal R})
       \in\mathcal R\otimes\operatorname{QCoh}(\mathcal Z).
 \end{gathered}
 \tag{SPC.14}
\]

The full tensor bar extends the exterior action to all objects and morphisms. The two factors act separately, so they commute with coherent comparisons. The algebra is commutative since \(R_{\mathcal R}\) is the actual commutative regular algebra (KG.23) and \(\mathsf{Loc}\) is symmetric monoidal. Thus all geometric and spectral inputs of the module construction (EP.6)–(EP.8) have now been supplied:

\[
 \mathcal H_{\mathcal Z}
   =\operatorname{Fun}^{\rm L}_{\mathcal B}
                 (\mathcal R,\mathcal N_{\mathcal Z})
   \simeq\operatorname{Mod}_{\mathfrak R_{\mathcal Z}}
                 (\mathcal N_{\mathcal Z}).
 \tag{SPC.15}
\]

The right-hand expression means modules for the action of this algebra on \(\mathcal N_{\mathcal Z}\). It does not require an object of \(\mathcal N_{\mathcal Z}\) to be a sheaf in an ordinary abelian heart.

Let \(r\) be the continuous right adjoint of the multiplication of \(\mathcal R\). Its induction and forgetful functors are

\[
 U_{\mathcal Z}(F)=F(\mathbf1),\qquad
 L_{\mathcal Z}(n)(T)=r(T)\star n,\qquad
 L_{\mathcal Z}\dashv U_{\mathcal Z},\qquad
 U_{\mathcal Z}L_{\mathcal Z}(n)=\mathfrak R_{\mathcal Z}\star n.
 \tag{SPC.16}
\]

The full adjunction is (EP.7), whose transformation maps insert the unit and evaluate the counit of multiplication and its right adjoint. Their two triangles prove the inverse maps on the whole mapping complexes and higher transformations. Its monad multiplication is the regular algebra multiplication, because both are the mate of the multiplication of the same counits. The split augmented free action bar of (EP.8) identifies its entire module category with (SPC.15). Its contraction after \(U_{\mathcal Z}\) and the conservativity of \(U_{\mathcal Z}\) prove the equivalence for every unbounded object and coherent action. The forgetful \(U_{\mathcal Z}\) preserves colimits, since the underlying action-module colimits are the underlying colimits.

The regular balancing map (EP.5), now with its actual second coefficient functor, gives the full eigen-comparison

\[
 \Phi^L(T)\star_{\rm first}U_{\mathcal Z}(F)
       \simeq\mathsf{Loc}(T)\star_{\rm coeff}U_{\mathcal Z}(F),
 \qquad T\in\mathcal R.
 \tag{SPC.17}
\]

These maps have the tensor, unit, symmetry and higher relations of the balanced module functor. The coefficient on the right is the actual full spectral complex (SPC.4), with arbitrary parameter modules.

For a point \(z\in\mathcal Z(A)\), denote the corresponding categories and algebra by
\(\mathcal N_z=\mathcal M_{L,A}\), \(\mathfrak R_z=(\operatorname{Id}\otimes F_z)(R_{\mathcal R})\), and \(\mathcal H_z=\operatorname{Mod}_{\mathfrak R_z}(\mathcal N_z)\). Compose induction with free \(A\)-coefficients:

\[
 \begin{gathered}
 s_A(M)=M\otimes_{\mathbf C}A,\qquad
 P_z^{\rm enh}=L_zs_A,\qquad J_z=v_AU_z,\\
 \operatorname{RHom}_{\mathcal H_z}(P_z^{\rm enh}c,F)
        \simeq\operatorname{RHom}_{\mathcal M_L}(c,J_zF),\\
 \{P_z^{\rm enh}c_i\}_i
       \text{ compactly generates }\mathcal H_z
       \quad(c_i\text{ compact generators of }\mathcal M_L).
 \end{gathered}
 \tag{SPC.18}
\]

Here \(v_A\) forgets the \(A\)-module action. Its full adjunction with \(s_A\) is the free \(A\)-module bar, including all differential and homotopy maps. It preserves colimits and is conservative: colimits of modules are underlying colimits, and an action on a zero underlying object is zero. The same properties hold for \(U_z\) by its constructed action bar. The displayed adjunction proves compactness of each free enhanced source, because \(J_z\) is continuous. Vanishing of all those mapping complexes forces \(J_zF=0\), then \(F=0\), proving generation of the full category. No finiteness or flatness of \(A\) is assumed.

For a morphism of affine points \((A,z)\to(B,z')\), (SPC.9) identifies the scalar extension of the regular algebra with \(\mathfrak R_{z'}\). It gives

\[
 \mathcal H_z\otimes_{\operatorname{Mod}_A}\operatorname{Mod}_B
       \simeq\mathcal H_{z'},\qquad
 (P_z^{\rm enh}c)\otimes_A^L B=P_{z'}^{\rm enh}c.
 \tag{SPC.19}
\]

We prove the full category comparison. Its functor is the scalar extension of the regular action maps and their free action bars. The generators in (SPC.18) go to the indicated generators of the target. For two such sources its mapping comparison reduces by the free adjunction to
\(\operatorname{RHom}_{\mathcal M_{L,A}}
(c_i\otimes A,\mathfrak R_z\star(c_j\otimes A))\).
The continuous mapping functor out of the compact \(c_i\) commutes with scalar extension by the same free coefficient bar as (KF.1), including the induced \(A\)-action. The right-hand source therefore becomes exactly the analogous mapping complex over \(B\), using (SPC.9). These are the canonical comparison maps; their composition is the same regular-algebra multiplication and transfer evaluation. The multi-object module bar now identifies the scalar extension with the full target: it is fully faithful on its compact generating DG category, and both categories are the full module categories generated by those images. The representable augmentation contraction proves the inverse on arbitrary modules and higher maps. This proves (SPC.19) for an arbitrary DG algebra map, including nonflat maps.

Equations (SPC.13), (SPC.14) and (SPC.19) also identify the global category with its entire Cartesian affine-point family:

\[
 \mathcal H_{\mathcal Z}
       \simeq\lim_{(A,z)\in(\operatorname{Aff}/\mathcal Z)^{\rm op}}\mathcal H_z.
 \tag{SPC.20}
\]

Indeed (SPC.13) identifies the underlying objects with full Cartesian \(\mathcal M_{L,A}\)-families. The action of the regular algebra restricts to its action at each point, by (SPC.9). Giving its module multiplication, unit, and their coherent homotopies in the limit is precisely giving their Cartesian maps and homotopies at every affine point. The same statement for maps of modules gives the entire mapping complexes. Conversely those coherent maps define the global action by that limit comparison. This proves (SPC.20) without commuting an ind-completion through a point diagram.

Finally let \(s_{\mathcal Z}(c)=c\boxtimes\mathcal O_{\mathcal Z}\), and let \(s_{\mathcal Z}^R\) be its right adjoint. The global enhanced induction has the actual adjunction

\[
 P_{\mathcal Z}^{\rm enh}=L_{\mathcal Z}s_{\mathcal Z}
       \dashv J_{\mathcal Z}=s_{\mathcal Z}^RU_{\mathcal Z}.
 \tag{SPC.21}
\]

One can construct this right adjoint on the compact-generator module model of \(\mathcal M_L\). An object of \(\mathcal N_{\mathcal Z}\) is an \(E\)-module in quasicoherent complexes; apply
\(\Gamma(\mathcal Z,-)=\operatorname{RHom}_{\operatorname{QCoh}(\mathcal Z)}
(\mathcal O_{\mathcal Z},-)\)
to its coefficients. Its \(E\)-action is induced by the adjunction mate
\(W\otimes\Gamma(Q)\to\Gamma(W\otimes Q)\).
For a representable \(c_i\), mapping from \(c_i\boxtimes\mathcal O_{\mathcal Z}\) is exactly \(\Gamma\) of that coefficient. The full representable bar extends this comparison to every source object: both sides send its colimits to mapping limits. This constructs \(s_{\mathcal Z}^R\), its unit and counit, and their actual adjunction triangles. Composing with (SPC.16) proves (SPC.21).

The affine result (SPC.18) does not prove that this global \(J_{\mathcal Z}\) is continuous or conservative: those properties would require additional global assertions about \(\mathcal O_{\mathcal Z}\) and global sections. Nor does free enhanced induction prove idempotence or full faithfulness of an ordinary spectral projector. The comparison of the transported Ran regular algebra with the spectral diagonal, the resulting localization and projector-image theorems, nilpotent singular-support image and regularity, and the required global generation remain to be proved. Derived tempered Satake and the arbitrary characteristic-zero geometric ground-field extension also remain required.

![The full spectral stage at a derived affine point, its proper Ran transition, a nonflat scalar fibre, Cartesian quasicoherent gluing and the enhanced spectral regular algebra.](figures/spectral-coefficient-gluing.svg)

**Figure 3.20.** The five panels give the actual maps of (SPC.1)–(SPC.21). The parameter in the second panel is an arbitrary full operator module; the third panel displays the complete cohomology degrees of the nonflat fibre in Solution3.BH. The fourth panel indexes the opposite of affine schemes over the prestack and includes every affine-point morphism and higher path. In the last panel \(\Gamma_{\mathcal Z}\) means the right adjoint on operator-valued coefficient modules constructed after (SPC.21). The compact generation statement is affine; continuity of that global right adjoint and the nilpotent projector image are not claimed. Further reading is the free AGKRRV preprint cited below.

### 3.72. Full operator parameters and a nonflat derived fibre

**Exercise 3.BF.** Use the finite-set square of Solution3.BC, put \(X=\mathbf P^1_{\mathbf C}\), and take the trivial dual-torus local system with coefficients in a connective DG algebra \(A\). Put \(V_u=V_p\), \(V_v=V_q\), and \(N=\mathcal D_{X^3}\). Calculate the spectral value on both sides of that transition.

**Solution 3.BF.** The trivial coefficient functor sends every character to \(\omega_X\otimes A\), with the unit's tensor comparisons; exterior products consequently give the dualizing unit on every parameter product. Thus (SPC.4) retains \(N_A\) itself. Proper product pushforward and (GD.9) give

\[
 F_{z,\psi_1}(V_p\boxtimes V_q,\mathcal D_{X^3})=A[-3].
 \tag{SPC.22}
\]

On the second stage the combined coefficient is \(V_{p+q}\), and the unused \(e\)-coordinate has a unit. Its restricted exterior coefficient is again the full dualizing unit on \(X^2\). Equation (RA.26) gives the transition module
\((i_{\rm diag})_*\mathcal D_X[-2]\), so

\[
 F_{z,\psi_2}(V_{p+q},(\Delta_\beta)_*\mathcal D_{X^3})
     =(p_X)_*\mathcal D_X[-2]\otimes_{\mathbf C}A=A[-3].
 \tag{SPC.23}
\]

The comparison is proper composition through the actual diagonal and forgotten coordinates, not an identification just of dimensions. The full nonholonomic input is compact, and its result \(A[-3]\) is perfect, as predicted by (SPC.10).

**Exercise 3.BG.** Let \(G=\mathbf G_m\), and let a dual-torus spectral point \(z\) be given by a flat line bundle \(E_A\) on \(X\) with derived \(A\)-coefficients, locally free of rank one over \(\mathcal O_X\otimes A\). For \(x\in X(\mathbf C)\), compute the spectral coefficient of \(A_{n,p}=V_n\otimes\delta_x[p]\), its dual, and the corresponding enhanced eigen-comparison.

**Solution 3.BG.** First construct the stated point. A finite-dimensional dual-torus representation is the finite sum of its weight spaces. Send its weight-\(n\) summand to the flat line power \(E_A^{\otimes n}\), with dual powers for negative \(n\), and use line multiplication for the tensor maps. Weight decompositions identify tensor products with the sums of these maps; line associativity, exchange and inverse evaluation give their unit, symmetry and dual relations. The representation module bar extends this rule continuously to \(\mathcal C\). In the right-D-module convention its normalized character coefficient is
\((E_A^{\otimes n}\otimes_{\mathcal O_X}\Omega_X^1)[1]\).
Local freeness and the shift by \([1]\) make this functor right \(t\)-exact, including derived connective \(A\)-coefficients. It is consequently an actual point of (SPC.1).

Along the closed point the inverse-transfer tensor is the derived quotient by the local coordinate, shifted by \([-1]\), and contracts the right density factor. Local freeness identifies this quotient with the actual derived fibre \(E_{A,x}^{\otimes n}\); the normalization \([1]\) cancels the transfer shift. Proper point pushforward and projection formula in (SPC.4) therefore give

\[
 F_z(A_{n,p})=E_{A,x}^{\otimes n}[p],\qquad
 F_z(A_{n,p}^{\vee})=E_{A,x}^{\otimes(-n)}[-p]
                      =F_z(A_{n,p})^\vee.
 \tag{SPC.24}
\]

Its evaluation contracts the line and its inverse, and coevaluation inserts their identity. For homogeneous shift generators of degrees \(-p,p\), reversed evaluation and the preceding exchange each have sign \((-1)^p\). Their product in both triangles is \(+1\), exactly as in (RA.27). Formula (SPC.17), or its affine restriction, now reads

\[
 \mathsf H_{n,x}^L[p](U_zF)
       \simeq U_zF\otimes_A^L E_{A,x}^{\otimes n}[p].
 \tag{SPC.25}
\]

Both sides have the same full coefficient shift, and the coherent comparison includes those same tensor signs. At \(n=p=0\) it is the module unit map. This is the actual affine spectral eigen-comparison on every unbounded underlying object.

**Exercise 3.BH.** Let \(A=\mathbf C[\epsilon]/(\epsilon^2)\), \(B=A/(\epsilon)=\mathbf C\), and let \(z\) be the trivial dual-torus spectral point. Extend \(F_z\) \(A\)-linearly to \(\mathcal R\otimes\operatorname{Mod}_A\), and take \(T=\mathbf1_{\mathcal R}\otimes B\). Compute its spectral coefficient after derived base change to \(B\), and compare it with ordinary tensor.

**Solution 3.BH.** The \(A\)-linear extension uses the free coefficient bar and satisfies

\[
 F_z^A(\mathbf1_{\mathcal R}\otimes Q)=Q,\qquad
 F_z^A(T)\otimes_A^L B=B\otimes_A^L B.
 \tag{SPC.26}
\]

A free \(A\)-resolution of \(B\) has one copy of \(A\) in every degree \(0,-1,-2,\ldots\), with all negative differentials multiplication by \(\epsilon\) and the degree-zero augmentation the quotient to \(B\). It is a complex because \(\epsilon^2=0\). The kernel and image of multiplication by \(\epsilon\) are both \(\epsilon A\), so it is exact in every negative degree, and its augmentation gives degree-zero cohomology \(B\). Tensoring this semifree bounded-above resolution with \(B\) makes all differentials zero. Consequently

\[
 B\otimes_A^L B\simeq\bigoplus_{r\ge0}B[r],\qquad
 H^{-r}(B\otimes_A^L B)=B\quad(r\ge0).
 \tag{SPC.27}
\]

The pulled-back object is
\(\mathbf1_{\mathcal R}\otimes(B\otimes_A^L B)\) in the full \(B\)-linear Ran category. Its coefficient under the pulled-back trivial point is the same complex by the \(B\)-linear version of (SPC.26), which checks the actual comparison (SPC.9). Ordinary tensor would give only

\[
 B\otimes_A B=B
 \tag{SPC.28}
\]

and would lose every negative cohomology group. Thus even empty labels require the entire derived module bar for nonflat scalar maps. There is no contradiction with (SPC.10): the inserted \(A\)-module \(B\) in this exercise is not perfect over \(A\), as its nonzero derived fibre in every negative degree demonstrates.

Further reading: [Arinkin, Gaitsgory, Kazhdan, Raskin, Rozenblyum and Varshavsky, *The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support*](https://arxiv.org/abs/2010.01906v2), §6.1 for the de Rham tensor-functor definition and §12.6 for the enhanced spectral construction. The full-parameter transition, derived fibre, Cartesian gluing and adjunction proofs used here are (SPC.1)–(SPC.28).

### 3.73. The full operator-valued universal property of Ran

Keep the complex-field categories of (RA.1), and put \(\mathcal D=\operatorname{Dmod}(X)\). All tensor functors below preserve colimits and have their entire coherent strong symmetric monoidal structure. We first prove the actual categorical self-duality used to recover a coefficient from all its parameter tests:

\[
 \begin{gathered}
 \operatorname{ev}_{\mathcal D}(Q,N)
     =p_*(Q\otimes^!N),\qquad
 \operatorname{coev}_{\mathcal D}(\mathbf C)
     =\Delta_*\omega_X\in\operatorname{Dmod}(X^2),\\
 \mathcal D\simeq\mathcal D^\vee,\qquad
 \mathcal A\otimes\mathcal D
     \simeq\operatorname{Fun}^{\rm L}(\mathcal D,\mathcal A).
 \end{gathered}
 \tag{SDG.1}
\]

Here \(\mathcal A\) can be any presentable symmetric monoidal DG category whose tensor preserves colimits in each variable. The tensor-product identification with the full product operator category is (RN.9); the evaluations are full continuous functors by (SH.14). To check the first triangle, identify the endofunctor determined by a full product kernel \(K\) with

\[
 M\longmapsto(p_1)_*(K\otimes^!p_2^!M).
 \tag{SDG.2}
\]

On an exterior kernel \(Q\boxtimes N\), proper product Fubini and the unit \(\omega_X\) identify this with \(Q\otimes_{\mathbf C}p_*(N\otimes^!M)\), precisely the evaluation–coevaluation composite. Exterior generators and their full module bar extend the identification to every kernel and mapping complex. For \(K=\Delta_*\omega_X\), the actual proper projection formula gives

\[
 \begin{aligned}
 (p_1)_*(\Delta_*\omega_X\otimes^!p_2^!M)
   &\simeq(p_1)_*\Delta_*
                (\omega_X\otimes^!\Delta^!p_2^!M)\\
   &\simeq M .
 \end{aligned}
 \tag{SDG.3}
\]

The second line is the composite-map identity \(p_1\Delta=p_2\Delta=\mathrm{id}_X\) and the !-tensor unit. It is an identity of the actual full transfer functors; it includes unbounded inputs and all their maps. Exchanging the two coordinates proves the other triangle. These triangles give the categorical dual and the last equivalence in (SDG.1): its forward functor evaluates against the second factor, and its inverse tensors with coevaluation and then evaluates the given functor on the first factor. The same two triangles prove that these are inverse on entire mapping complexes and higher maps. No finiteness of a nonholonomic object's underlying vector space enters this duality.

We claim the following universal property of the *actual* full Ran category:

\[
 \operatorname{Fun}^{\otimes,{\rm L}}(\mathcal R,\mathcal A)
   \simeq
 \operatorname{Fun}^{\otimes,{\rm L}}
       (\mathcal C,\mathcal A\otimes\mathcal D).
 \tag{SDG.4}
\]

For an operator-valued coefficient functor \(E\) on the right, use the full stage formula

\[
 F_{E,\psi}(\vec V,N)
    =(\operatorname{Id}_{\mathcal A}\otimes p_{X^J,*})
           (\Delta_\psi^!E^I(\vec V)\otimes^!N),
 \qquad \psi:I\to J.
 \tag{SDG.5}
\]

The operator operations here are tensored with \(\mathcal A\); the tensor bar defines the formula on its whole presentable coefficient category. The proof of (SPC.3)–(SPC.8) applies to these actual functors: arbitrary functions multiply their coefficient fibres or insert the dualizing unit, the opposite parameter arrow is carried by proper projection formula, and disjoint unions use full proper product Fubini. The transfer compositions, tensor constraints and identity bar degeneracies give all higher comparisons. None of these proofs uses a special property of \(\operatorname{Mod}_A\); they use the continuous operator functors tensored with the coefficient category. The full Ran colimit (RN.11)–(RN.13) therefore produces the left-hand functor.

Conversely, let \(F:\mathcal R\to\mathcal A\) be a continuous strong symmetric monoidal functor. On the singleton stage restrict it to

\[
 G_V(N)=F(\operatorname{ins}_{\mathrm{id}_{\{1\}}}(V\otimes N)),
 \qquad E_F(V)\in\mathcal A\otimes\mathcal D
       \text{ represents }G_V\text{ under (SDG.1).}
 \tag{SDG.6}
\]

This constructs the entire continuous functor \(E_F\), not merely its values on finite-dimensional representations. The inverse in (SDG.1) supplies its maps and all their higher homotopies, naturally in \(V\).

We now recover its tensor maps. Let \(c:\{1,2\}\to\{1\}\) be the fold. There are actual structural equivalences in the Ran category

\[
 \operatorname{ins}_{\mathrm{id}_{\{1\}}}(V\otimes W\otimes N)
 \simeq \operatorname{ins}_c((V\boxtimes W)\otimes N)
 \simeq \operatorname{ins}_{\mathrm{id}_{\{1,2\}}}
                 ((V\boxtimes W)\otimes\Delta_*N).
 \tag{SDG.7}
\]

The first is the coefficient fold \(\alpha=c,\beta=\mathrm{id}\); the second is the parameter fold \(\alpha=\mathrm{id},\beta=c\), with \(\beta\) pointing opposite to the parameter-stage direction. On exterior parameter objects \(N_1\boxtimes N_2\), monoidality of \(F\) identifies its two-point stage with \(G_V(N_1)\otimes_{\mathcal A}G_W(N_2)\). The full exterior module bar (RN.9) extends that equality to every parameter object of \(\operatorname{Dmod}(X^2)\), including the actual \(\Delta_*N\) in (SDG.7). Apply proper projection formula to (SDG.5). The resulting identity on every \(N\) is represented, by the full faithful comparison (SDG.1), by

\[
 E_F(V\otimes W)\simeq E_F(V)\otimes^!E_F(W).
 \tag{SDG.8}
\]

These are the actual representing maps. An equality only on holonomic parameters or ordinary stalks would not recover them.

The empty coefficient-label transition, followed by the structural map \(X\to\mathrm{pt}\), gives

\[
 \operatorname{ins}_{\mathrm{id}_{\{1\}}}(\mathbf1\otimes N)
   \simeq\operatorname{ins}_{\emptyset\to\{1\}}
                      (\mathbf C\otimes N)
   \simeq\mathbf1_{\mathcal R}\otimes_{\mathbf C}p_*N.
 \tag{SDG.9}
\]

After applying \(F\), (SDG.1) consequently represents this singleton parameter functor by
\(E_F(\mathbf1)=\mathbf1_{\mathcal A}\boxtimes\omega_X\).
Thus (SDG.8) has the specified strong unit map too.

For associativity, expand (SDG.7) on three label and coordinate copies. The two successive folds have the same composite function, and the two diagonal transfers have the same small diagonal. The coherent Ran composition maps identify them before evaluation. Applying the representing equivalence (SDG.1) gives the associativity relation for (SDG.8). Four copies give its pentagon. Parameter and coefficient permutations give its exchange and symmetry relations, with the density and suspension normalization of §3.63. Empty fibres give its unit relations. The same argument on each longer function string and each bar simplex retains all higher comparisons. This proves the strong symmetric monoidal \(E_F\).

Finally any stage reduces by its coefficient function \(\alpha=\psi\) to

\[
 \operatorname{ins}_{\psi}(\vec V\otimes N)
    \simeq
 \operatorname{ins}_{\mathrm{id}_J}
          ((\operatorname{mult}^{\psi}\vec V)\otimes N).
 \tag{SDG.10}
\]

On exterior parameters at the right-hand stage, monoidality splits the functor into the singleton tests just reconstructed. The full exterior bar then extends this to arbitrary \(N\), yielding exactly (SDG.5). These comparisons respect all original finite-set transitions, by their common folds and transfers; hence they extend to the actual enhanced Ran colimit and its localization morphisms. Conversely reconstructing \(E\) from (SDG.5) is the evaluation–coevaluation triangle of (SDG.1). Naturality and the full bar prove the same two inverse comparisons for transformations and higher paths. This proves (SDG.4).

### 3.74. The regular algebra encodes entire spectral path spaces

Let \(A\) be a connective commutative DG algebra and let \(z,w\in\mathcal Z(A)\) be the actual points of (SPC.1). Transport the Ran regular algebra and multiply its two \(A\)-coefficient factors:

\[
 \begin{gathered}
 D_{z,w}
   =\operatorname{mult}_A
          (F_z\otimes F_w)(R_{\mathcal R})\in\operatorname{CAlg}_A,\\
 D_{z,w}\simeq
     \int^{T\in\mathcal R^c}F_z(T)^\vee\otimes_A^L F_w(T).
 \end{gathered}
 \tag{SDG.11}
\]

The second line follows from the actual entire compact-DG-category coend (KG.23), continuity of both coefficient functors, and their monoidal dual comparison (SPC.10). It includes the coend's higher bar faces and degeneracies; it is not a sum over representatives of inserted objects. Its multiplication is the one constructed for the regular algebra: two terms use the coefficient exchange and then the term for \(T\circledast S\); its unit is the term for \(\mathbf1\).

For every connective commutative DG \(A\)-algebra \(B\), all tensor comparisons in (SPC.9) yield

\[
 D_{z,w}\otimes_A^L B\simeq D_{z_B,w_B}.
 \tag{SDG.12}
\]

Indeed duality of the finite perfect \(F_z(T)\) commutes with derived scalar extension, by the evaluation–coevaluation triangles; arbitrary derived tensor then commutes with the coend realization. On each bar simplex these are the same tensor maps, so the comparison includes the algebra multiplication, unit and every higher relation. No flatness of \(A\to B\) is used.

We prove the full natural-transformation meaning of this algebra:

\[
 \operatorname{Map}_{\operatorname{CAlg}_B}
       (D_{z_B,w_B},B)
    \simeq
 \operatorname{Isom}^{\otimes}
       (F_{w_B},F_{z_B}).
 \tag{SDG.13}
\]

For a compact \(T\), perfect duality identifies a map
\(F_{z_B}(T)^\vee\otimes_B F_{w_B}(T)\to B\)
with a map \(F_{w_B}(T)\to F_{z_B}(T)\). This fixes the orientation: the algebra's first, dual factor is the *target* of the corresponding transformation. Maps from the full coend are precisely coherently natural such maps on the compact DG category. This is its defining universal property on mapping spaces: applying \(\operatorname{Map}(-,B)\) turns its realization into the complete limit of the bar mapping spaces. The unit condition is the transformation at \(\mathbf1\); its multiplication condition is

\[
 \eta_{T\circledast S}
   =\eta_T\otimes_B\eta_S
 \quad\text{under the given monoidal comparisons}.
 \tag{SDG.14}
\]

The regular algebra's associative, symmetric and higher multiplication maps impose exactly the corresponding coherent tensor relations. One may compute those algebra mapping spaces by the augmented free commutative-algebra resolution: in each degree its faces multiply or apply the algebra action, its degeneracies insert the free unit, and the augmentation is split by unit insertion. Thus its total mapping space retains the multiplication homotopies and all their iterated compatibility; it does not replace a commutative DG algebra map by a map of its degree-zero cohomology rings. The same bar comparison proves that these assignments are inverse as spaces with all higher paths.

Such a tensor transformation is automatically invertible. For a dualizable compact \(T\), construct the inverse to \(\eta_T:F_{w_B}(T)\to F_{z_B}(T)\) by

\[
 \begin{aligned}
 F_{z_B}(T)&\longrightarrow
 F_{w_B}(T)\otimes_B F_{w_B}(T^\vee)\otimes_B F_{z_B}(T)\\
 &\xrightarrow{\mathrm{id}\otimes\eta_{T^\vee}\otimes\mathrm{id}}
 F_{w_B}(T)\otimes_B F_{z_B}(T^\vee)\otimes_B F_{z_B}(T)\\
 &\longrightarrow F_{w_B}(T).
 \end{aligned}
 \tag{SDG.15}
\]

The outside maps are source coevaluation and target evaluation in the ordered dual–object convention. Equivalently, the last map uses the transported Ran evaluation with its required exchange. Naturality for evaluation and coevaluation, tensor compatibility (SDG.14), and the transformation's unit map reduce each composite with \(\eta_T\) to the corresponding duality triangle. They therefore give both identity composites, with the complex exchange signs. All objects of \(\mathcal R\) are generated from the compact DG category by the full representable bar. Both coefficient functors preserve its realization, so this inverse extends naturally to every unbounded object and all maps. Higher inverse comparisons follow from those same triangles. This proves the asserted isomorphism space, rather than a space of possibly noninvertible natural transformations.

Apply the entire universal comparison (SDG.4) with \(\mathcal A=\operatorname{Mod}_B\). The actual coefficient functor associated to a point is precisely (SPC.4). Thus

\[
 \begin{aligned}
 \operatorname{Map}_{\operatorname{CAlg}_A}(D_{z,w},B)
   &\simeq\operatorname{Isom}^{\otimes}(E_{w_B},E_{z_B})\\
   &\simeq\operatorname{Path}_{\mathcal Z(B)}(w_B,z_B).
 \end{aligned}
 \tag{SDG.16}
\]

The second line is the defining maximal infinity-groupoid in (SPC.1). It retains right \(t\)-exact objects, their tensor isomorphisms and every higher path. Every map used in the first line is the scalar coend comparison, its tensor-dual mate or the full universal representing comparison; consequently it is natural in \(B\), in the points and in their coherent paths.

This identifies the *entire derived point-pair path functor* of the actual de Rham prestack. It does not yet prove that \(D_{z,w}\) is connective, or that its spectrum is an affine scheme in the connective derived-affine convention. Identifying the algebra (SDG.11) with the quasicoherent direct image of the diagonal unit requires that further geometry and its derived base-change proof. Nor does (SDG.16) by itself prove a tensor-product equivalence for global quasicoherent categories, a continuous fully faithful localization right adjoint, global enhanced generation, the ordinary projector or its nilpotent image and regularity. Those assertions remain required.

![The full operator self-duality kernel, recovery of the tensor coefficient from all Ran parameters, the regular coend representing derived tensor paths, and the projective-line torus derived fibre.](figures/spectral-paths.svg)

**Figure 3.21.** Panels1–3 give the actual full-category maps of (SDG.1)–(SDG.16). The first panel distinguishes the dualizing coevaluation kernel from its incorrectly shifted constant replacement. In the third, the first dual coefficient is the target of the tensor isomorphism. Panel4 is the complete worked derived fibre of Solution3.BK, including its degree-two paths. Panel5 records which general diagonal, localization and nilpotent-image assertions still need proofs. The source reading is the free AGKRRV preprint cited below.

### 3.75. The kernel shift, enriched naturality and a derived diagonal fibre

**Exercise 3.BI.** Replace the coevaluation kernel in (SDG.1) by \(\Delta_*\mathbf k_X\). Compute its endofunctor on an arbitrary full D-module \(M\), and compare it with the correct kernel on \(M=\mathcal D_X\).

**Solution 3.BI.** On the curve, (GD.3) gives \(\mathbf k_X=\omega_X[-2]\). The same actual proper projection and composite-map calculation as (SDG.3) gives

\[
 \begin{aligned}
 (p_1)_*(\Delta_*\mathbf k_X\otimes^!p_2^!M)
   &\simeq\mathbf k_X\otimes^!M=M[-2],\\
 (p_1)_*(\Delta_*\omega_X\otimes^!p_2^!M)
   &\simeq M .
 \end{aligned}
 \tag{SDG.17}
\]

In particular the first kernel gives \(\mathcal D_X[-2]\), whereas coevaluation must give \(\mathcal D_X\). The calculation holds for every unbounded \(M\), including this nonholonomic compact operator module. The two kernels differ by an actual dimension shift; agreement on their ordinary support would not detect the error.

**Exercise 3.BJ.** In the coefficient field \(\mathbf C\), a rule on the shifted units of \(\mathcal R\) multiplies the value of \(\mathbf1[r]\) by \(a^r\), where \(a\in\mathbf C^\times\). Its degree-zero maps and tensor products look compatible. Determine whether this can be an enriched tensor transformation with identity unit map.

**Solution 3.BJ.** The shifted identity supplies a closed homogeneous morphism

\[
 f_r\in\operatorname{Hom}_{\mathcal R}^{\,r}
                   (\mathbf1[r],\mathbf1).
 \tag{SDG.18}
\]

Both coefficient functors carry it to the canonical degree-\(r\) morphism \(\mathbf C[r]\to\mathbf C\). Enriched naturality therefore requires

\[
 \eta_{\mathbf1}\,F(f_r)
       =F(f_r)\,\eta_{\mathbf1[r]},
 \qquad 1=a^r.
 \tag{SDG.19}
\]

There is no interchange sign here: the transformation has degree zero. Taking \(r=1\) gives \(a=1\), and then all the equations hold. In contrast, the ordinary degree-zero category of shifted vector lines has no nonzero map between different shifts; the grading-dilation rule would pass that weaker naturality test. This explains why the compact *DG* coend and its enriched bar in (SDG.11) cannot be replaced by a coend over ordinary isomorphism classes and degree-zero maps.

**Exercise 3.BK.** Let \(X=\mathbf P^1_{\mathbf C}\), let \(\widehat G=\mathbf G_m\), and let \(z\) be the trivial normalized coefficient functor. Determine \(D_{z,z}\). For the connective DG algebra
\(B=\mathbf C[\delta]/(\delta^2)\), with \(|\delta|=-2\) and zero differential, compute the components and positive homotopy groups of the corresponding spectral path space.

**Solution 3.BK.** A finite representation of \(\mathbf G_m\) is the finite sum of its weight spaces: in its coaction write \(v\mapsto\sum_n v_n\otimes t^n\). Coassociativity and uniqueness of Laurent coefficients give the coaction \(v_n\mapsto v_n\otimes t^n\), and the counit gives \(v=\sum_n v_n\). Thus the regular coefficient coend has one generator for each weight, with multiplication adding weights; it is \(\mathbf C[u,u^{-1}]\). Under the two trivial coefficient functors its regular algebra in \(\operatorname{Dmod}(X)\) is
\(\omega_X\otimes_{\mathbf C}\mathbf C[u,u^{-1}]\).
The target-category version of the duality and coend argument (SDG.13) identifies its maps to the unit with invertible endomorphisms of \(\omega_X\), with all their homotopies. It consequently gives

\[
 \operatorname{Map}_{\operatorname{CAlg}_{\mathbf C}}(D_{z,z},B')
   \simeq
 \operatorname{GL}_1\!
       \left(\operatorname{RHom}_{\operatorname{Dmod}_{B'}(X)}
                    (\omega_X\otimes B',\omega_X\otimes B')\right).
 \tag{SDG.20}
\]

For this particular constant coefficient construction the same proof works for every commutative DG \(B'\), including a nonconnective one: the constant tensor functor and its derived scalar bar are still defined, and no \(t\)-exactness condition is used in the algebra mapping calculation. For connective \(B'\) these functors are the actual spectral point pullbacks of (SDG.16). Testing all DG target algebras in (SDG.20) will let us identify the algebra itself, rather than infer it only from ordinary points.

Here is a full multiplicative model of the endomorphism complex over \(\mathbf C\). The normalized unit becomes the trivial connection after right-density side change; its Spencer Hom is the de Rham complex. Use the charts \(U=\mathbf A^1_t\), \(V=\mathbf A^1_s\), \(s=t^{-1}\), and \(W=U\cap V=\mathbf G_m\). Their affine ordered Čech–de Rham total complex has terms

\[
 \begin{gathered}
 C^0=\mathbf C[t]\oplus\mathbf C[s],\\
 C^1=\mathbf C[t]\,dt\oplus\mathbf C[s]\,ds
                         \oplus\mathbf C[t,t^{-1}],\\
 C^2=\mathbf C[t,t^{-1}]\,dt,\\
 d^0(f_U,f_V)=(df_U,df_V,f_V-f_U),\qquad
 d^1(\alpha_U,\alpha_V,h)=\alpha_V-\alpha_U-dh .
 \end{gathered}
 \tag{SDG.21}
\]

All forms and functions in differences are restricted to \(W\). The displayed differentials compose to zero. Degree-zero cycles are equal constants. For a degree-one cycle, integrate each polynomial form to \(f_U,f_V\); this is possible in characteristic zero. The cycle equation then says that \(h-f_V+f_U\) is constant. Adjust the constant of one primitive to obtain exactly that cycle as \(d^0(f_U,f_V)\). Thus \(H^1=0\). In degree two, forms from \(U\) have exponents at least zero, and forms from \(V\), using \(ds=-t^{-2}dt\), have exponents at most \(-2\). Derivatives of Laurent functions have zero residue and span all monomials other than \(t^{-1}dt\). The quotient is consequently the single residue class

\[
 H^0(C^\bullet)=\mathbf C,\qquad
 H^1(C^\bullet)=0,\qquad
 H^2(C^\bullet)=\mathbf C\eta,\qquad
 \eta=[dt/t].
 \tag{SDG.22}
\]

The complex has its ordered Čech cup product with form exchange sign
\((-1)^{rq}\), where \(r\) is the first factor's de Rham degree and \(q\) the second factor's Čech degree. Restrictions, associative form multiplication and that sign make it an associative DG algebra: the two parts of the total differential obey the graded Leibniz identity, and both association routes restrict the same three factors to the same intersection. This is the endomorphism cup product. Indeed the coordinate Spencer diagonal sends a tangent generator to its two primitive factors; its exterior extension, with the same Koszul sign, commutes with the Spencer differential by the operator Leibniz rule. Applying Hom gives the form product locally. Ordered Čech composition gives exactly the product just described on global derived maps.

Choose \(dt/t\) as an actual degree-two cocycle. Its square is zero already in this total complex, whose terms stop in degree two. Sending \(1\) to the actual constant unit and the degree-two generator to this cocycle therefore gives a unital associative DG algebra quasi-isomorphism

\[
 \mathbf C[\eta]/(\eta^2)\longrightarrow C^\bullet,\qquad
 |\eta|=2.
 \tag{SDG.23}
\]

This proves the multiplicative model as well as its cohomology; an equality just of dimensions would not identify invertible endomorphisms. The full finite Spencer–Čech scalar comparison of (SPC.9) extends this model by derived tensor to every \(B'\). Thus its scalar form is \(B'\oplus B'[-2]\), with square-zero second summand.

An invertible endomorphism is a unit \(u\) in the first summand together with a degree-zero element \(q\) in the second. Multiplication by the coherent inverse of \(u\) identifies this space naturally with

\[
 \operatorname{GL}_1(B')\times
                 \operatorname{Map}_{\operatorname{Mod}_{\mathbf C}}
                                   (\mathbf C[2],B').
 \tag{SDG.24}
\]

Both factors include their full higher mapping spaces; invertibility restricts the components of the first without discarding any of its higher homotopies. The first factor is represented by the free degree-zero Laurent generator, and the second by a free degree-\(-2\) commutative generator. By (SDG.20) for all DG \(B'\) and the algebraic Yoneda comparison, we have the actual algebra

\[
 D_{z,z}\simeq
 \mathbf C[u,u^{-1}]\otimes_{\mathbf C}
                          \operatorname{Sym}_{\mathbf C}(\mathbf C[2]).
 \tag{SDG.25}
\]

This particular diagonal algebra is connective. It does not prove the corresponding general-group connectivity and diagonal-pushforward theorem.

For the algebra \(B\) in the exercise, the degree-zero unit in
\(B[\eta]/(\eta^2)\) is \(u+q\delta\eta\), where \(u\in\mathbf C^\times\) and \(q\in\mathbf C\). Their multiplication and all integer character values are

\[
 \begin{gathered}
 (u+q\delta\eta)(u'+q'\delta\eta)
      =uu'+(uq'+qu')\delta\eta,\\
 (u+q\delta\eta)^n=u^n+n u^{n-1}q\delta\eta,\qquad n\in\mathbf Z .
 \end{gathered}
 \tag{SDG.26}
\]

The square of \(\delta\eta\) is zero; the inverse formula gives the displayed equality for negative \(n\) too. Dividing \(q\) by \(u\) identifies the component group with the product of the multiplicative and additive groups. Above a fixed component, the higher homotopy groups are the negative cohomology of the endomorphism complex. Its only negative degree is \(-2\), coming from \(\delta\) in the first summand. Therefore

\[
 \begin{gathered}
 \pi_0\operatorname{Path}_{\mathcal Z(B)}(z_B,z_B)
        =\mathbf C^\times\times\mathbf C,\\
 \pi_2\operatorname{Path}_{\mathcal Z(B)}(z_B,z_B)=\mathbf C,\qquad
 \pi_i=0\quad(i\ge1,\ i\ne2).
 \end{gathered}
 \tag{SDG.27}
\]

For \(B'=\mathbf C\), in contrast, the path space has only the ordinary units \(\mathbf C^\times\) and no positive homotopy groups. The extra degree-\(-2\) diagonal coordinate and the degree-two paths of the derived coefficient test are therefore invisible if one tests only ordinary field-valued points.

Free further reading for the regular-algebra/path argument is [Arinkin, Gaitsgory, Kazhdan, Raskin, Rozenblyum and Varshavsky, *The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support*](https://arxiv.org/abs/2010.01906v2), §12.3. The full operator pairing and universal reconstruction used here are (SDG.1)–(SDG.10); the entire coend, derived scalar and path-space comparisons are (SDG.11)–(SDG.16); the three complete solutions are (SDG.17)–(SDG.27).

### 3.76. Tensor powers force finite projective coefficients

We continue over \(\mathbf C\), with every connective commutative DG coefficient algebra \(A\). On a smooth affine curve chart \(U=\operatorname{Spec}R\), put \(R_A=R\otimes_{\mathbf C}A\). The normalized forgetful functor is

\[
 \begin{gathered}
 \mathsf u_A:\mathcal D_A(X)\longrightarrow
                       \operatorname{QCoh}(X_A),\\
 \mathsf u_A(M)=
       \bigl(\Omega_X^{-1}\otimes_{\mathcal O_X}M_{\rm right}\bigr)[-1]
       =M_{\rm left}[-1],\\
 \mathsf u_A(M\otimes_A^!N)
       \simeq\mathsf u_A(M)\otimes_{\mathcal O_{X_A}}^L\mathsf u_A(N),
 \qquad \mathsf u_A(\omega_X\otimes A)=\mathcal O_{X_A}.
 \end{gathered}
 \tag{CSD.1}
\]

These identities follow from the actual density side change and diagonal transfer in §§3.48 and 3.63. In left conventions the !-tensor is ordinary derived structure-sheaf tensor shifted by \([-1]\). The two copies of the normalization in (CSD.1) give its displayed strong tensor comparison; the density and suspension exchanges are precisely the ordered signs of §3.63. Forgetting the operator action is conservative and preserves colimits. In particular it carries a dualizable operator object to a dualizable quasicoherent complex.

Here are the needed local derived-algebra facts, including the finite-projectivity conclusion. A module over a connective DG algebra has a semifree resolution using cells in degrees at most its upper cohomology bound: start with cycles in its highest degree, kill the kernel with cells one degree lower, and continue downward. The cycle equation defines each new differential and guarantees its square is zero. The resulting exhaustive union maps quasi-isomorphically to the module in every fixed degree. Tensor two such resolutions; their generator degrees add. Consequently

\[
 P\in\operatorname{Mod}_{S}^{\le a},\quad
 Q\in\operatorname{Mod}_{S}^{\le b}
 \quad\Longrightarrow\quad
 P\otimes_S^LQ\in\operatorname{Mod}_{S}^{\le a+b},
 \qquad H^i(S)=0\ (i>0).
 \tag{CSD.2}
\]

Every dualizable \(S\)-module is perfect. Its dual supplies
\(\operatorname{RHom}_S(P,-)=P^\vee\otimes_S^L-\), which preserves colimits, so \(P\) is compact. The full semifree-cell argument of §5.1 makes it a retract of a finite cell module. Conversely duals of those finite cells and their retracts give perfect duality. In particular a perfect module and its dual have finite upper cohomology bounds, even when \(S\) has arbitrarily negative cohomology.

Let \(S_0=H^0(S)\). The fibre of \(S\to S_0\) is in degrees at most \(-1\). By (CSD.2), for any bounded-above \(P\),

\[
 P\in\operatorname{Mod}_S^{\le b}
 \quad\Longrightarrow\quad
 H^b(P)\xrightarrow{\ \sim\ }
                     H^b(P\otimes_S^LS_0).
 \tag{CSD.3}
\]

Apply the tensor triangle for that fibre: its first term is in degrees at most \(b-1\), which proves the stated isomorphism without a convergence assumption. Thus if \(P\otimes_S^LS_0\) is in degrees at most zero, a bounded-above \(P\) is connective: otherwise choose its largest nonzero cohomology degree and contradict (CSD.3).

We will use the following precise residue criterion:

\[
 \begin{gathered}
 P\text{ perfect over }S,\qquad
 P\otimes_S^L\kappa(\mathfrak p)
        \text{ concentrated in degree }0
        \quad(\mathfrak p\in\operatorname{Spec}S_0)\\
 \Longrightarrow
 P\text{ is a retract of a finite sum of unshifted copies of }S.
 \end{gathered}
 \tag{CSD.4}
\]

To prove it, first reduce \(P\) to \(S_0\). It remains a retract of a finite cell complex. The earlier lesson Perfect complexes and duals on a ringed space, §2 and Corollary3.3, proves that such an ordinary-ring retract has local bounded finite-projective models. At a local ring make their terms finite free, using its Lemma1.2. Whenever a differential matrix has an entry outside the maximal ideal, that entry is a unit. Row and column changes make it an identity block. The equation \(d^2=0\) kills the adjacent row and column, so this block is a contractible two-term summand and can be removed. There are finitely many terms and entries. After finitely many such cancellations all differentials reduce to zero in the residue field. The residue hypothesis then says that all remaining terms except degree zero have rank zero. Hence the complex is a finite free module in degree zero at this local ring. The finitely many row changes and inverse entries spread after inverting one element outside the prime. Thus \(P\otimes_S^LS_0\) is locally a finite locally free module in degree zero. Its finite ranks have a common bound on the affine spectrum, and its degree-zero module has finitely many generators: choose a finite principal cover, choose bases there, clear denominators and then use powers of the principal elements generating the unit ideal to generate globally. This also applies to its dual.

It follows from (CSD.3) that both \(P\) and \(P^\vee\) are connective, and that \(H^0(P)\) is finitely generated. Lift its finite generators to a map \(S^r\to P\). Its fibre \(K\) is connective, by surjectivity on \(H^0\) and the cohomology exact sequence. The connecting map \(P\to K[1]\) is zero, since

\[
 \begin{gathered}
 \operatorname{Hom}_{\operatorname{Mod}_S}(P,K[1])
       =H^1(P^\vee\otimes_S^LK)=0,\\
 K\longrightarrow S^r\longrightarrow P\longrightarrow K[1].
 \end{gathered}
 \tag{CSD.5}
\]

The vanishing uses (CSD.2). Exactness of Hom therefore lifts \(1_P\) to a section of \(S^r\to P\), proving (CSD.4) as an actual derived-module retract. It does not assume a strict lift of an idempotent matrix from \(S_0\).

Now let \(z\in\mathcal Z(A)\) and let \(V\) be a finite representation in degree zero. Put \(P=\mathsf u_AE_z(V)|_U\). Representation duality and (CSD.1) make \(P\) perfect. Right \(t\)-exactness, applied to every tensor power of \(V\) and \(V^\vee\), gives

\[
 P^{\otimes_{R_A}^Ln}\in\operatorname{Mod}_{R_A}^{\le1},
 \qquad
 (P^\vee)^{\otimes_{R_A}^Ln}
                      \in\operatorname{Mod}_{R_A}^{\le1},
 \qquad n\ge1.
 \tag{CSD.6}
\]

The bound is one because the normalized forgetful functor shifts the underlying left module by \([-1]\). Derived scalar extension to a residue field preserves this upper bound by (CSD.2). A perfect complex over a field is its finite cohomology complex plus contractible disks: choose complements to cycles and boundaries in each degree. If its largest nonzero cohomology degree is \(b>0\), the largest degree of its \(n\)-fold tensor is \(nb\), with nonzero coefficient \((H^b)^{\otimes n}\). This contradicts (CSD.6) for large \(n\). Applying the same argument to the dual excludes negative cohomology. Every residue fibre of \(P\) is therefore concentrated in degree zero. Criterion (CSD.4) proves:

\[
 \mathsf u_AE_z(V)|_U
       \text{ is finite projective over }R_A.
 \tag{CSD.7}
\]

The proof includes arbitrary connective \(A\), all its negative degrees and arbitrary residue fields of \(H^0(R_A)\). It does not require flatness of a scalar change. The actual operator action remains the specified derived connection; forgetting it only establishes its coefficient finiteness.

### 3.77. The full commutative-algebra left adjoint

Write \(s_A(B)=\omega_X\otimes_{\mathbf C}B\). Proper adjunction (GD.7) and its full scalar comparison give

\[
 p_{A,*}:\mathcal D_A(X)\rightleftarrows
                         \operatorname{Mod}_A:s_A,
 \qquad p_{A,*}\dashv s_A.
 \tag{CSD.8}
\]

The functor \(s_A\) is continuous and strong symmetric monoidal. Its induced functor on commutative algebra objects has the following explicit left adjoint \(L_A\):

\[
 L_A(Q)=
 \left|
  [n]\longmapsto
       \operatorname{Sym}_A
       \bigl(p_{A,*}\,T^{\,n}UQ\bigr)
 \right|,
 \qquad
 T=U\operatorname{Sym}_{\mathcal D_A(X)}.
 \tag{CSD.9}
\]

Here \(U\) forgets the commutative algebra structure, not the operator action. We explain the maps and the entire adjunction. The free algebra resolution of \(Q\) has degree \(n\) term \(\operatorname{Sym}_{\mathcal D_A}(T^nUQ)\). Its faces multiply two successive free layers or use the action on \(Q\); its degeneracies insert a free layer. The underlying augmented object has the extra degeneracy given by the free-algebra unit, so its realization is \(Q\). Sifted realizations are preserved by \(U\): the symmetric powers are built from tensor powers and finite-group homotopy coinvariants, each commuting with sifted colimits. This proves the resolution assertion on full underlying objects and maps.

For a free term there is an actual mapping-space equivalence

\[
 \begin{aligned}
 \operatorname{Map}_{\operatorname{CAlg}(\mathcal D_A)}
       (\operatorname{Sym}_{\mathcal D_A}M,s_A(B))
  &\simeq\operatorname{Map}_{\mathcal D_A}(M,s_A(B))\\
  &\simeq\operatorname{Map}_{\operatorname{Mod}_A}(p_{A,*}M,B)\\
  &\simeq\operatorname{Map}_{\operatorname{CAlg}_A}
                              (\operatorname{Sym}_A p_{A,*}M,B).
 \end{aligned}
 \tag{CSD.10}
\]

A map between two free operator algebras is specified by a map \(M\to T N\). Compose it with \(TN\to T(s_Ap_{A,*}N)\), induced by the adjunction unit. Since \(s_A\) is continuous and strong monoidal, this last target is \(s_A\operatorname{Sym}_A(p_{A,*}N)\). Its adjoint specifies the map between the two free algebras in (CSD.9). These are precisely the maps representing (CSD.10), so they respect compositions, identities and every higher homotopy. This defines the simplicial diagram, including all its coherent relations.

Mapping out of its realization is the total limit of (CSD.10). The operator free-algebra resolution then gives

\[
 \operatorname{Map}_{\operatorname{CAlg}_A}(L_A(Q),B)
       \simeq
 \operatorname{Map}_{\operatorname{CAlg}(\mathcal D_A)}
                                  (Q,s_A(B)).
 \tag{CSD.11}
\]

This holds for every commutative DG \(A\)-algebra \(B\), including nonconnective ones. It constructs \(L_A\) and the whole adjunction on mapping spaces. It does not identify the underlying object of \(L_A(Q)\) with \(p_{A,*}UQ\); the algebra relations require the entire resolution.

We next prove the required connectivity of the construction. The projective curve has an affine cover by two opens with affine intersection. Indeed embed it in projective space. Choose a hyperplane not containing the curve. Its intersection with the integral curve is a finite set. Choose a second hyperplane avoiding that set and not containing the curve; this is possible over the infinite field \(\mathbf C\), since finitely many point conditions are proper linear subspaces. The two complements cover the curve and are closed in the corresponding affine projective-space charts. Their intersection is a principal open in either chart. The full ordered Čech complex consequently has degrees zero and one, so it adds at most one to an upper cohomology bound. Its two-term totalization and the full affine comparison compute arbitrary unbounded quasicoherent complexes by the descent and sorting contraction of §3.40.

If \(\mathsf u_A(M)\) is connective, the actual right Spencer transfer for \(p_{A,*}M\) has columns

\[
 \mathsf u_A(M)[2]\longrightarrow
       \bigl(\Omega_X^1\otimes_{\mathcal O_X}\mathsf u_A(M)\bigr)[1].
 \tag{CSD.12}
\]

This is the curve de Rham complex shifted by \([2]\). The differential includes the specified connection and the internal differential; the Spencer operator Leibniz rule makes their total differential square zero. The columns have upper bounds \(-2\) and \(-1\). Applying the two-term affine Čech complex gives upper bound zero. Finite column totalizations need no boundedness below. Thus

\[
 \mathsf u_A(M)\text{ connective}
       \quad\Longrightarrow\quad
 p_{A,*}M\text{ connective over }A.
 \tag{CSD.13}
\]

The normalized functor \(\mathsf u_A\) is strong monoidal and continuous. If \(\mathsf u_A(UQ)\) is connective, every \(\mathsf u_A(T^nUQ)\) is connective: tensor powers of connective modules are connective by (CSD.2), and their homotopy coinvariants and sums are connective. In characteristic zero one can also use the averaging projection for each finite symmetric group. Equations (CSD.9), (CSD.13) and (CSD.2) now show that every free algebra term of \(L_A(Q)\) is connective. Sifted realization remains connective; its underlying normalized simplicial total complex places simplicial degree \(n\) in cochain degree \(-n\). We have proved

\[
 \mathsf u_A(UQ)\text{ connective}
       \quad\Longrightarrow\quad
 L_A(Q)\text{ connective}.
 \tag{CSD.14}
\]

### 3.78. The actual affine diagonal and its unit pushforward

For the actual points \(z,w\in\mathcal Z(A)\), let

\[
 Q_{z,w}=
 \operatorname{mult}_{\mathcal D_A}
              (E_z\otimes E_w)(R_{\mathcal C})
       \in\operatorname{CAlg}(\mathcal D_A(X)).
 \tag{CSD.15}
\]

Use the same target-dual orientation as (SDG.11). The regular algebra \(R_{\mathcal C}\) is the degree-zero regular representation algebra, as constructed in (EP.3) and the earlier tensor/regular-coend proofs. Its matrix coefficients are filtered unions of finite representations: a finite set of regular functions has a coaction involving finitely many coefficient functions; coassociativity makes their finite span a subcomodule, and the counit recovers the original functions. The exterior pair has the same property. Equation (CSD.7), tensor compatibility and filtered colimits show that \(\mathsf u_A(UQ_{z,w})\) is connective.

There is an actual algebra equivalence

\[
 D_{z,w}\simeq L_A(Q_{z,w}).
 \tag{CSD.16}
\]

To prove it, test every commutative DG \(A\)-algebra \(B\), with no connectivity restriction. The scalar extensions \(E_z\otimes_A^LB,E_w\otimes_A^LB\) are still defined continuous tensor functors even if \(B\) is nonconnective. Their full Ran functors are obtained by (SDG.4), which has no \(t\)-exactness requirement. The compact-coend, scalar and tensor-inverse proofs (SDG.11)–(SDG.15) then give

\[
 \begin{aligned}
 \operatorname{Map}_{\operatorname{CAlg}_A}(D_{z,w},B)
 &\simeq
   \operatorname{Isom}^{\otimes}(E_w\otimes_A^LB,E_z\otimes_A^LB)\\
 &\simeq
   \operatorname{Map}_{\operatorname{CAlg}(\mathcal D_A)}
                                     (Q_{z,w},s_A(B))\\
 &\simeq
   \operatorname{Map}_{\operatorname{CAlg}_A}(L_A(Q_{z,w}),B).
 \end{aligned}
 \tag{CSD.17}
\]

The middle equivalence is the target-category version of the same full representation-DG coend argument: duality identifies each coefficient functional with the corresponding transformation component, algebra multiplication imposes tensor compatibility, and the free-algebra bar retains every higher relation. Scalar adjunction carries its target unit to \(s_A(B)\). These are natural inverse maps on entire spaces, as in (SDG.13)–(SDG.15). Algebra Yoneda for all DG targets proves (CSD.16), without assuming connectivity of \(D_{z,w}\) beforehand. Equations (CSD.14)–(CSD.16) therefore prove

\[
 D_{z,w}\in\operatorname{CAlg}^{\le0}_A.
 \tag{CSD.18}
\]

For connective \(B\), equation (SDG.16) identifies its entire represented path functor with the fibre of the diagonal. Hence the actual Cartesian square is

\[
 \begin{CD}
 \operatorname{Spec}D_{z,w} @>>> \mathcal Z\\
 @VVV @VV{\Delta_{\mathcal Z}}V\\
 \operatorname{Spec}A @>{(z,w)}>> \mathcal Z\times\mathcal Z .
 \end{CD}
 \tag{CSD.19}
\]

It is Cartesian as a square of prestacks, including all higher paths, because its value on every connective derived affine test is exactly the path space (SDG.16). Equation (SDG.12) gives every nonflat derived base-change comparison of this fibre algebra. Thus \(\Delta_{\mathcal Z}\) is representable and affine in the connective derived convention. No finite-type or global compact-generation theorem for \(\mathcal Z\) is required for this conclusion.

We give the quasicoherent pushforward statement explicitly, rather than using a global tensor-product assertion. Assemble

\[
 \mathcal D_\Delta|_{(A,z,w)}=D_{z,w}
 \quad\text{in}\quad
 \operatorname{CAlg}(\operatorname{QCoh}(\mathcal Z\times\mathcal Z)).
 \tag{CSD.20}
\]

The affine-point comparisons are (SDG.12), with all higher coherences, so this is a Cartesian quasicoherent algebra. For any representable affine map \(f:Y\to T\) of prestacks with these fibre algebras \(D_A\), there is a full equivalence

\[
 \operatorname{QCoh}(Y)
      \simeq
 \operatorname{Mod}_{\mathcal D_f}(\operatorname{QCoh}(T)).
 \tag{CSD.21}
\]

Here is a direct proof from the affine-point definition of quasicoherence. From a quasicoherent object on \(Y\), evaluate it on the actual affine fibre \(\operatorname{Spec}D_A\) over each affine point of \(T\). Retain that \(D_A\)-module and its underlying \(A\)-module. Scalar compatibility on the Cartesian fibre squares makes these a Cartesian \(\mathcal D_f\)-module over \(T\). Conversely, at a point \(\operatorname{Spec}B\to Y\), compose with \(f\) to get a point of \(T\). The chosen lift to \(Y\) supplies the actual algebra map \(D_B\to B\). Assign to it

\[
 N_B=M_B\otimes_{D_B}^L B .
 \tag{CSD.22}
\]

The full derived module bar and the Cartesian algebra comparisons make these assignments compatible with every affine-point map and all higher paths. In the first inverse comparison, the map \(\operatorname{Spec}B\to\operatorname{Spec}D_B\to Y\) and quasicoherent pullback give precisely the original \(N_B\). For the other comparison, evaluate (CSD.22) at the universal fibre \(\operatorname{Spec}D_A\). Its base-point algebra is \(D_A\otimes_A^LD_A\), and its universal lift has algebra map given by multiplication. The required derived cancellation is

\[
 (M_A\otimes_A^LD_A)
       \otimes_{D_A\otimes_A^LD_A}^L D_A
      \simeq M_A .
 \tag{CSD.23}
\]

To check it, write the first factor as
\(M_A\otimes_{D_A}^L(D_A\otimes_A^LD_A)\), with the first \(D_A\) acting on \(M_A\); then apply associative derived tensor and the multiplication map. The augmented free-module bar proves that associativity and this cancellation hold for arbitrary unbounded modules and entire mapping complexes. Both comparisons are canonical and coherent. This proves (CSD.21).

Under (CSD.21), \(f^*\) is the free \(\mathcal D_f\)-module functor and \(f_*\) is its forgetful right adjoint. The free/forgetful module adjunction proves this on all mapping spaces. Forgetting modules preserves colimits, so the right adjoint is continuous. Affine evaluation shows that it has full arbitrary derived base change and the quasicoherent projection formula. Applying this to (CSD.19) gives

\[
 \begin{gathered}
 (\Delta_{\mathcal Z})_*\mathcal O_{\mathcal Z}
            \simeq\mathcal D_\Delta,\\
 \operatorname{QCoh}(\mathcal Z)
       \simeq
 \operatorname{Mod}_{\mathcal D_\Delta}
           (\operatorname{QCoh}(\mathcal Z\times\mathcal Z)).
 \end{gathered}
 \tag{CSD.24}
\]

Finally let
\(\pi:\operatorname{QCoh}(\mathcal Z)\otimes
\operatorname{QCoh}(\mathcal Z)\to
\operatorname{QCoh}(\mathcal Z\times\mathcal Z)\)
be the canonical exterior-product functor. Evaluation on each pair \((A,z,w)\), using the actual regular coend, identifies

\[
 \pi\bigl((\mathsf{Loc}\otimes\mathsf{Loc})(R_{\mathcal R})\bigr)
       \simeq(\Delta_{\mathcal Z})_*\mathcal O_{\mathcal Z}.
 \tag{CSD.25}
\]

All those affine comparisons are the same coend scalar maps, so they give an equivalence of Cartesian algebras, not just their ordinary fibres. This proves the complex affine-diagonal and regular-algebra pushforward assertions. It does not prove that \(\pi\) is an equivalence, or that \(\mathsf{Loc}\) has a continuous fully faithful right adjoint. The global tensor comparison and localization, global enhanced generation, the ordinary projector with its nilpotent image and regularity, the derived tempered assertion and arbitrary characteristic-zero geometric ground-field extension remain required.

![Normalized tensor-power coefficient bounds, the full shifted curve Spencer and two-chart calculation, the entire commutative-algebra left adjoint, and the actual Cartesian affine diagonal and unit pushforward.](figures/connective-spectral-diagonal.svg)

**Figure 3.22.** Panels1–3 show the finite-projectivity and connectivity mechanisms of (CSD.1)–(CSD.18). Panel4 is the actual Cartesian square (CSD.19), with its full quasicoherent module and diagonal-unit pushforward calculation (CSD.20)–(CSD.24). Panel5 distinguishes the proved algebra comparison (CSD.25) from the remaining global categorical equivalence and localization assertions.

### 3.79. Why tensor powers and the full algebra resolution matter

**Exercise 3.BL.** Over \(\mathbf C\), consider the normalized coefficient \(P=\mathbf C[-1]\), with its dual. Explain why the associated shifted operator objects can individually pass the right \(t\)-exact upper-bound test, but cannot be the image of a degree-zero representation under a right \(t\)-exact tensor functor.

**Solution 3.BL.** The normalized operator coefficient is \(M=P[1]=\mathbf C\), and its !-dual is \(P^\vee[1]=\mathbf C[2]\). Both are in cohomological degrees at most zero. However the second tensor power has

\[
 M\otimes^!M=P^{\otimes2}[1]=\mathbf C[-1],
 \qquad H^1(\mathbf C[-1])=\mathbf C .
 \tag{CSD.26}
\]

It is not connective. A degree-zero representation's second tensor power remains degree zero, so its image would have to be connective. This is the explicit failure. Testing only an object and its dual misses it; the uniform bound for all powers in (CSD.6) excludes it.

**Exercise 3.BM.** Let \(X=\mathbf P^1\). Apply \(L_A\) to the free commutative operator algebra generated by \(s_A(A)=\omega_X\otimes A\). Determine the resulting commutative DG algebra and explain why its negative degrees cannot be truncated away.

**Solution 3.BM.** Equation (CSD.10) gives \(L_A(\operatorname{Sym}_{\mathcal D_A}s_A(A))=\operatorname{Sym}_A(p_{A,*}s_A(A))\). The complete Čech–de Rham calculation (SDG.21)–(SDG.22), with the normalization (CSD.12), gives \(p_{A,*}s_A(A)=A[2]\oplus A\). Hence

\[
 L_A(\operatorname{Sym}_{\mathcal D_A}s_A(A))
       \simeq A[x,v],\qquad |x|=0,\quad |v|=-2,
 \qquad d x=d v=0.
 \tag{CSD.27}
\]

The formula denotes the derived free symmetric \(A\)-algebra on those two cells; if \(A\) has a nonzero differential, it also retains that differential on coefficients. Even for \(A=\mathbf C\), every monomial \(v^n\) contributes nonzero degree \(-2n\), so the underlying complex is unbounded below. Testing against \(\mathbf C[\delta]/(\delta^2)\), \(|\delta|=-2\), includes maps with \(v\mapsto q\delta\). Replacing the algebra by its degree-zero ring would remove that parameter. This free algebra is a worked term of (CSD.9); it is not asserted to be the regular pair algebra.

**Exercise 3.BN.** For \(X=\mathbf P^1\), \(\widehat G=\mathbf G_m^r\) and the trivial point \(z\), determine the affine diagonal fibre. For \(B=\mathbf C[\delta]/(\delta^2)\), \(|\delta|=-2\), compute the component group and all positive homotopy groups, including \(r=0\).

**Solution 3.BN.** The Laurent coaction proof of Solution3.BK works with \(r\) exponents: its coefficient weights are \(\mathbf Z^r\). A tensor isomorphism is specified by the \(r\) commuting images of the weight basis; tensor powers and inverse weights determine every other component. In the symmetric endomorphisms of the unit those images commute coherently, with precisely the tensor exchange and unit constraints. Equivalently, repeat the full coend calculation on the \(r\)-fold tensor product of the Laurent representation category; its tensor functors and regular-algebra products separate the \(r\) weight coordinates. The full scalar and enriched bars retain every higher path. Equation (SDG.25) for each coordinate therefore gives

\[
 \begin{gathered}
 D_{z,z}\simeq
  \mathbf C[u_1^{\pm1},\ldots,u_r^{\pm1}]
       \otimes
    \operatorname{Sym}_{\mathbf C}(\mathbf C^r[2]),\\
 \pi_0\operatorname{Path}_{\mathcal Z(B)}(z_B,z_B)
       \simeq(\mathbf C^\times)^r\times\mathbf C^r,\qquad
 \pi_2\simeq\mathbf C^r,\qquad
 \pi_i=0\ (i\ge1,\ i\ne2).
 \end{gathered}
 \tag{CSD.28}
\]

Each unit is \(u_i+q_i\delta\eta\); divide \(q_i\) by \(u_i\) to obtain the additive coordinate, as in (SDG.26). Each endomorphism complex has its sole negative degree \(-2\), which proves the displayed homotopy groups. For \(r=0\), the algebra is \(\mathbf C\) and the entire path space is contractible. This includes the empty product and its unit, rather than silently assuming a positive torus rank.

Free further reading is [Arinkin, Gaitsgory, Kazhdan, Raskin, Rozenblyum and Varshavsky, *The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support*](https://arxiv.org/abs/2010.01906v2), §§12.2–12.3, for the commutative-algebra and diagonal framework, and [Lurie, *Derived Algebraic Geometry*](https://www.math.ias.edu/~lurie/papers/DAG.pdf), §2.5, for connective derived modules. The coefficient-projectivity, full algebra adjunction, connective diagonal and affine-module pushforward proofs used here are (CSD.1)–(CSD.25); the complete solutions are (CSD.26)–(CSD.28).

## 4. Betti, constructible, and tempered categories

Now suppose \(k=\mathbb C\), and choose a coefficient field \(E\) of characteristic zero. The **large Betti** category consists of complexes of \(E\)-sheaves on the analytic stack, with no finite-dimensional stalk requirement. Its automorphic subcategory is

\[
\operatorname{Shv}^{\mathrm{Betti}}_{1/2,\operatorname{Nilp}}(Y)
 \subset\operatorname{Shv}^{\mathrm{Betti}}_{1/2}(Y).
                                                        \tag{4.1}
\]

Here singular support is the microlocal support on smooth analytic charts. The zero-support condition on a smooth space says that a sheaf is locally constant as a derived sheaf. “Derived” is essential on a stack: local systems include higher coherent monodromy, not just representations of its ordinary fundamental group.

There is also a chartwise ind-constructible theory: on each finite-type affine chart, ind-complete the category of bounded complexes with algebraically constructible finite-dimensional cohomology, then descend. This is the theory denoted \(\operatorname{Shv}^{\mathrm{Betti,constr}}\) in GLC I. Its nilpotent subcategory is the **restricted** automorphic variant. It can be smaller than the large category. Compact objects of the large category are not defined by finite-dimensional stalks; §7 gives a rank-one example.

Sections 3.55–3.58 prove Riemann–Hilbert with ind-completion on charts for the full chartwise ind-regular categories over complex coefficients. Its restriction to the independently defined de Rham and Betti nilpotent support conditions additionally requires the matching microlocal support comparison on bounded regular inputs and its ind-extension; that support comparison remains a proof obligation here. It does not identify every algebraic D-module with every arbitrary topological sheaf. The precise comparison appears in GLC I §4.2.1; the large and restricted Betti variants are separated in §§3.1 and 3.6. In particular the Betti spectral stack has a restricted-variation version distinct from the entire character stack, even though they have the same field-valued local systems. Point sets cannot specify their categories of families.

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

We proved the full connected-reductive truncatability, compact generation and co-duality with its actual star-transition diagram and half-twist transport, the normalized global family half root with its Clifford reductions, residue descent and determinant comparison, the quasicompact-open restriction limit, the local half-operator gluing formula, the zero-support calculation for connections, the derived \(B\mathbb G_m\) algebra and its noncompact constant object, the Picard-stack splitting on families and arrows, its D-module factorization, the discrete duality calculation, and the full rank-one Betti nilpotent category. We also proved finite point detection on the full unbounded category under the stated conical dimension bound, its half-twisted chart descent, and compact generation under the specified continuous conservative adjunction. Sections 3.20–3.22 apply the proved general nilpotent upper bound, establish ind-holonomic chart cohomology, and detect all unbounded nilpotent objects and morphisms by finite families on each bounded open. Sections 3.23–3.25 also prove the local algebraic Hecke and formal Levi ingredients, including their coefficient-ring hypotheses and the signed curve covector. Section 3.26 proves bounded affine-Springer isolation in both directions and distinguishes the reduced bound from the full nonreduced Grassmannian. Sections 3.27–3.29 prove the global Hecke cotangent and compatible-Higgs fibre statements and the signed moving relation, with invariant equations on nonreduced coefficient tests. The five original exercises and the additional proof exercises have checked solutions.

The smooth strong-descent construction is supplied by the proved earlier programme lesson linked in §1.10; the specific unbounded transfer and quotient-category arguments are proved in §§1.10–1.15. Picard representability has the proof and remaining boundaries specified in Lesson 2. General descent and derived foundations beyond these proved cases remain separate obligations. The normalized square-root construction on \(\operatorname{Bun}_G\) is now proved in §§2.2–2.8 from the written earlier curve and adjoint results. Suitable-open preservation on the full unbounded category is proved in §§3.2–3.15. Nilpotent regularity, the microlocal restriction of Riemann–Hilbert to the nilpotent conditions, and the local tempered construction and its point independence retain the explicit unproved arguments below. The full chartwise ind-regular Riemann–Hilbert equivalence, stack descent and half-twist transport over complex coefficients are proved in §§3.55–3.58 from the complete earlier general theorem. We have proved the truncatability estimates and categorical consequences in §§1.3–1.15. The spectral projector and derived Satake remain unproved here. No positive-characteristic geometric Langlands equivalence is asserted.

The geometric hypotheses of the initial formal compact-generation and co-duality lemmas are proved in §§1.3–1.15. The following list records that result and the other geometric arguments within this lesson's scope:

1. **Truncatability for arbitrary connected reductive \(G\) — proved here.** Sections 1.3–1.9 construct the cofinal bounded opens, admissible root blocks, radical cohomology and actual opposite-parabolic contractions in every genus and coefficient family. Sections 1.10–1.14 prove strong unbounded equivariance, bounded framed-quotient compact generation and duality, and contraction retaining the Levi action. Section 1.15 handles finite singular boundary unions, both extension adjunctions, global compact generation, the star-transition co-dual and the normalized half twist. Central and torsion component labels are included.

2. **Normalized global half root — proved here.** Sections 2.2–2.8 construct the line and its square map over every ordinary coefficient ring, prove cutoff composition and all base changes, and normalize at the trivial bundle. The point-modification calculation proves the determinant comparison; the constant central adjoint summand gives the full connected reductive result. The explicit scalar choice and its parity change are retained in (PF.13) and (PF.30). Hecke, Levi and Whittaker compatibility of chosen normalizations are further statements, not consequences claimed by this line construction. The earlier curve, reductive-group and local-algebra arguments retain their recursive foundational boundaries.

3. **Nilpotent regularity.** Prove the spectral action and the Beilinson projector, identify its image with the singular-support subcategory, and prove that this image is chartwise ind-regular holonomic. The definition \(\operatorname{SS}(M)\subset \operatorname{Nilp}\) and the flat-connection calculation do not imply regular singularities for a general nilpotent covector. An irregular rank-one connection on an affine line has zero characteristic variety, so even zero characteristic variety on a nonproper chart is insufficient by itself. For the torus on the proper Picard variety the elementary argument is valid: its nilpotent cone is zero, coherent zero-support modules are flat vector bundles by the existing Taylor proof, and the proper Picard variety itself is a compactification with empty boundary. The general descent and nonabelian theorem remain separate obligations.

4. **Preservation by suitable opens — proved here.** Sections 3.2–3.15 prove the proper support estimate, weighted contraction and local parabolic implication, duality and whole boundary inverse image, finite HN-boundary assembly, coherent approximation in the strong quotient heart, both full cohomological amplitude bounds, the unbounded finite-window passage and global extension over the cofinal cuts. Both extensions preserve nilpotent support for every connected reductive group in every genus and component. Arbitrary opens can still add conormal directions, as Exercise 3.C shows.

5. **Tempered and anti-tempered statements actually used in §4.** Prove the derived spherical action, the quotient/full-subcategory realization, point independence, and the irregular-support criterion used to put the constant \(SL_2\) object in the anti-tempered category. Ordinary geometric Satake would not by itself prove any of these derived statements.

6. **Riemann–Hilbert generality — chartwise ind-regular comparison proved.** Sections 3.55–3.58 use the complete earlier general algebraic regular-holonomic proof, including every higher morphism and the actual inverse-image comparisons, to prove ind-extension, stack descent and the normalized global half twist over complex coefficients. This proves the regular-category comparison on every smooth chart, with no global boundedness or compactness assumption. The additional identification of the independently defined nilpotent singular-support subcategories requires its separate microlocal comparison and ind-extension.

Nilpotent regularity, tempered statements and the nilpotent microlocal restriction of Riemann–Hilbert remain active proof work; suitable-open support preservation and the full complex chartwise ind-regular stack comparison are proved. The categorical descent and recursive foundational boundaries remain active too. External references identify comparison sources; they do not replace the required programme proofs.

The source locators above are for the consulted versions. In addition to the inline references, the central rank-one comparison is AG §11.2, remark in “The case of a torus”; the large Betti definitions and torus calculation are Ben-Zvi–Nadler §§4.2–4.3. These older conjectural formulations are used for their category constructions, not presented as the current status of the theorem.

The [next lesson](hecke-functors-and-hecke-eigensheaves.md) constructs Hecke functors on these automorphic categories and formulates their coherent eigencondition. Local systems and their derived moduli will be developed later, before the spectral categories.
