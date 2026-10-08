# Constructible sheaves on a triangulation

A triangulation turns local changes of a sheaf into algebra attached to faces. A module sits on each open simplex, and a homomorphism records how a germ on a face continues into a larger simplex. This lesson constructs the sheaf from that data, proves that sections on an open star have no higher cohomology, and compares the resulting diagram category with the derived category of constructible sheaves.

The prerequisite model is Constructible gluing on an interval. The constant-sheaf input is the proved convex acyclicity calculation, applied to the intersection of a closed simplex with an open star. This intersection is convex and locally closed in the affine span of that simplex. Consequently the stated coefficient scope of the calculation applies, including arbitrary modules.

The derived comparison uses enough injective sheaves, bounded-below resolutions, derived adjunction and truncation. Proposition 4 constructs the ordinary adjunction and explains why its right adjoint preserves injectives; Theorem 3 supplies the acyclicity needed for the displayed unit and counit calculations. For the resolution input, Sheaves of modules and their derived categories, Section 5 constructs enough injectives for modules and module sheaves; its Theorem 6.1 and Lemmas 6.2–6.3 construct bounded-below resolutions, comparison maps and computation by acyclic terms. The bounded-below hypercohomology proof constructs the finite truncation filtration and identifies the actual edge to cohomology-sheaf sections and then to a stalk. Its linked good-truncation and resolution proofs supply those steps. General derived-category localization remains a separate foundational input. Theorem 5 retains its stated uniform dimension and finite-global-dimension hypotheses, and Theorem 7 retains Noetherianity.

*Original exposition by GPT-6.1 Sol (OpenAI), Ultra, September 2026, with the direct module proof by GPT-6 Astra (OpenAI), Ultra, October 2026. Original lesson text is public domain (CC0).*

## From the interval diagram to all face diagrams

At an interior vertex of a triangulated line, its star has the vertex and the two incident open edges. The face arrows are exactly \(V\to L\) and \(V\to R\) in the fixed interval diagram. The following general construction uses this same direction of arrows.

For the categorical step, use the [direct module calculation below](#the-algebra-of-face-diagrams), which constructs kernels, quotients and their universal maps for an arbitrary set of simplices. Consider a natural map \(a:M\to N\). On a face arrow \(\sigma\le\tau\), the equality \(a_\tau r^M_{\sigma\tau}=r^N_{\sigma\tau}a_\sigma\) means that \(r^M_{\sigma\tau}\) carries \(\ker a_\sigma\) into \(\ker a_\tau\). The induced kernel arrow is uniquely determined by its inclusion into \(M_\tau\). Dually the quotient arrow is induced by \(r^N_{\sigma\tau}\), because it carries \(\operatorname{im}a_\sigma\) into \(\operatorname{im}a_\tau\). These are the actual natural kernel/cokernel diagrams. Their coimage-to-image maps are pointwise isomorphisms with natural inverses, so the face-diagram category is abelian.

That calculation supplies the categorical assertion used after (2). It does not construct a sheaf or compute ambient sheaf cohomology. The étalé construction in Theorem 1 supplies the first task. The closed-simplex injective resolution in (4)–(8) supplies the second. For a fixed star \(U_\sigma\), only cofaces of \(\sigma\) contribute to its product: at a point of \(\rho^\circ\subset U_\sigma\), a nonzero factor requires \(\sigma\le\rho\le\tau\). There are finitely many such \(\tau\) by local finiteness. Thus that restricted product is finite, without asserting exactness of arbitrary products of sheaves.

The full bounded derived equivalence (12), and finite-coefficient equivalence (15) with its Noetherian hypothesis and finite-at-each-face projective covers, are retained below. The interval model is an entry calculation; these proofs supply the additional generality.

## Faces and open stars

Let \(S\) be a locally finite abstract simplicial complex. Its simplices are finite nonempty vertex sets; every nonempty subset of a simplex is a simplex. Each vertex belongs to finitely many simplices. Its realization \(|S|\) consists of barycentric points

\[
x=(x_v),\qquad x_v\geq0,\quad\sum_vx_v=1,
\]

whose positive-coordinate support is a simplex. The open simplex \(\sigma^\circ\) consists of points with positive support exactly \(\sigma\). We write \(\sigma\leq\tau\) when \(\sigma\) is a face of \(\tau\). The open star of \(\sigma\) is

\[
U_\sigma=\bigcup_{\tau\geq\sigma}\tau^\circ
=\{x:x_v>0\text{ for every }v\in\sigma\}.
\tag{1}
\]

This is open in the realization. Every simplex has finitely many cofaces: choose one of its vertices and use local finiteness. Thus each star lies in a finite subcomplex. If \(\sigma\leq\tau\), then \(U_\tau\subset U_\sigma\). Two stars intersect in \(U_{\sigma\cup\tau}\) when \(\sigma\cup\tau\) is a simplex, and have empty intersection otherwise.

Near a point of \(\sigma^\circ\), choose a sufficiently small barycentric neighborhood inside \(U_\sigma\). It meets only cofaces of \(\sigma\), and its intersection with each such open simplex can be chosen convex. These neighborhoods are what will make the gluing construction local.

The complex need not have finitely many simplices or vertices. No countability assumption is made here. A uniform dimension bound will be imposed separately for the stated bounded derived comparison.

## Modules that continue into larger faces

Fix a commutative coefficient ring \(k\). A face diagram consists of modules \(M_\sigma\) and homomorphisms

\[
r_{\sigma\tau}:M_\sigma\longrightarrow M_\tau
\quad(\sigma\leq\tau),
\tag{2}
\]

with \(r_{\sigma\sigma}=\mathrm{id}\) and
\(r_{\tau\upsilon}r_{\sigma\tau}=r_{\sigma\upsilon}\).
Thus a face diagram is a covariant functor from the face poset to \(k\)-modules. Write \(\mathcal A_S\) for this abelian category. Exactness is evaluated at each simplex.

### The algebra of face diagrams {#the-algebra-of-face-diagrams}

Here is a direct verification of the abelian-category assertion for the modules and arrows in (2). It applies to an arbitrary set of simplices; neither local finiteness nor a dimension bound is needed for this algebraic step.

A morphism \(a:M\to N\) is a family of \(k\)-linear maps satisfying
\[
a_\tau r^M_{\sigma\tau}=r^N_{\sigma\tau}a_\sigma
\qquad(\sigma\le\tau).
\]
Such families can be added, negated and multiplied by scalars, and composition is bilinear. The diagram whose modules are all zero is a zero object. The diagram with values \(M_\sigma\oplus N_\sigma\) and transition maps \(r^M_{\sigma\tau}\oplus r^N_{\sigma\tau}\) is both a product and a coproduct of two diagrams: its coordinate inclusions and projections commute with every transition, and the required maps into or out of it are the ordinary pairs of module maps. Thus the category is additive.

For the morphism \(a\), form the following submodules and quotient modules:
\[
K_\sigma=\{m\in M_\sigma:a_\sigma(m)=0\},
\qquad
Q_\sigma=N_\sigma/a_\sigma(M_\sigma).
\]
Their transition maps have the explicit formulas
\[
r^K_{\sigma\tau}(m)=r^M_{\sigma\tau}(m),
\qquad
r^Q_{\sigma\tau}([n])=[r^N_{\sigma\tau}(n)].
\]
The first formula lands in \(K_\tau\), since its image under \(a_\tau\) is \(r^N_{\sigma\tau}(a_\sigma(m))=0\). For the second, replacing \(n\) by \(n+a_\sigma(m)\) changes its proposed image by
\(r^N_{\sigma\tau}a_\sigma(m)=a_\tau r^M_{\sigma\tau}(m)\), which is zero in the quotient. Hence both formulas define \(k\)-linear maps. Their identity and composition laws follow by applying the corresponding laws for \(r^M\) and \(r^N\) to an element or to a representative of a class. The inclusions \(K_\sigma\hookrightarrow M_\sigma\) and quotient maps \(N_\sigma\twoheadrightarrow Q_\sigma\) are morphisms of diagrams.

These are categorical kernels and cokernels, not only lists of modules. If \(b:L\to M\) satisfies \(ab=0\), define \(\widetilde b_\sigma(l)=b_\sigma(l)\), now regarded as an element of \(K_\sigma\). Its transition equation is the transition equation for \(b\), so \(\widetilde b:L\to K\) is a diagram map. It is the unique factorization through the inclusions, because an element of a submodule has the same underlying element in its ambient module. If \(c:N\to L\) satisfies \(ca=0\), define \(\overline c_\sigma([n])=c_\sigma(n)\). It is well-defined because \(c_\sigma\) kills \(a_\sigma(M_\sigma)\); its transition equation follows by evaluating both sides on \([n]\). It is the unique factorization through the quotient maps, because every class has a representative. This proves both universal properties, including their compatibility with all faces.

The image diagram has modules \(a_\sigma(M_\sigma)\subset N_\sigma\), with the restricted transitions of \(N\). The map from the coimage to the image is
\[
M_\sigma/K_\sigma\longrightarrow a_\sigma(M_\sigma),
\qquad [m]\longmapsto a_\sigma(m).
\]
It is bijective: its values exhaust the image, and two representatives have the same value exactly when their difference is in \(K_\sigma\). Its inverse sends \(a_\sigma(m)\) to \([m]\), independently of the chosen preimage. Both maps commute with transitions, because the transition of \(a_\sigma(m)\) is \(a_\tau(r^M_{\sigma\tau}(m))\). Thus the coimage-to-image comparison is an isomorphism of diagrams. Together with the additive structure and the universal kernel and cokernel constructions, this proves that \(\mathcal A_S\) is abelian.

In particular, a sequence of diagrams is exact exactly when its sequence of modules at every simplex is exact. Kernels and images were computed as the corresponding submodules, and equality of those submodules is precisely module exactness. For a complex \(C^\bullet\), evaluation therefore gives the specified natural identification
\[
H^j(C^\bullet)_\sigma
=\ker(d^j_\sigma)/\operatorname{im}(d^{j-1}_\sigma)
=H^j(C^\bullet_\sigma).
\]
These identifications commute with face maps and cochain maps, because all induced maps send the class of a cycle to the class of its image. This is the exactness calculation used in the injective resolutions and derived comparisons below.

A sheaf is weakly constructible for this triangulation if its restriction to every open simplex is constant. No finite-generation condition is included.

**Theorem 1.** Face diagrams are equivalent, by an exact equivalence, to weakly constructible sheaves on \(|S|\).

**Proof.** Start with a face diagram. Over a point \(x\in\sigma^\circ\), put the fibre \(M_\sigma\). An element \(m\in M_\sigma\) defines a local section on a small neighborhood of \(x\) as follows: at a point in \(\tau^\circ\), for \(\tau\geq\sigma\), its value is \(r_{\sigma\tau}(m)\). Use the small neighborhoods described after (1).

These sections define an étalé space. To check compatibility of its basic neighborhoods, suppose two prescribed sections agree at a point of \(\tau^\circ\). Shrink to a neighborhood meeting only cofaces of \(\tau\). At every such coface their values are images of the same element of \(M_\tau\), so they still agree by the composition identity in (2). The projection is therefore a local homeomorphism. The module operations are defined in each fibre and are continuous on these basic sections. Its sheaf of sections, denoted \(E(M)\), restricts to the constant sheaf \(M_\sigma\) on \(\sigma^\circ\).

Conversely, let \(F\) be weakly constructible. Constant transport on the contractible open simplex identifies its stalks there with a module \(M_\sigma\). A germ on a face \(\sigma^\circ\) has a representative in a small neighborhood meeting a coface \(\tau^\circ\). Restrict the representative to that coface and use its constant transport to obtain \(r_{\sigma\tau}\).

This does not depend on the representative: two representatives of one germ agree after shrinking, and their restrictions meet a connected small part of \(\tau^\circ\). It does not depend on the point chosen in \(\sigma^\circ\): the same local argument shows that the resulting homomorphism is locally constant along \(\sigma^\circ\), which is connected. For \(\sigma\leq\tau\leq\upsilon\), choose a representative near a point of \(\sigma^\circ\), then a nearby point of \(\tau^\circ\). Its restriction near the latter point is a representative of \(r_{\sigma\tau}(m)\), and its value in \(\upsilon^\circ\) is already \(r_{\sigma\upsilon}(m)\). This proves the composition identity.

Every local section of \(F\) determines a section of the constructed étalé space by taking its stalk values. On a sufficiently small neighborhood of a point in \(\sigma^\circ\), these values have exactly the prescribed form in (2). The resulting map \(F\to E(M)\) is an isomorphism on all stalks, hence an isomorphism. The same construction identifies morphisms with compatible module maps. Finally, both sheaf exactness and diagram exactness are detected at the modules on the open simplices. \(\square\)

This gives more than stalk values: the maps in (2) are part of the sheaf. Two diagrams with the same modules and different face maps can have different cohomology.

## Sections on a star

**Proposition 2.** For a face diagram \(M\),

\[
\Gamma(U_\sigma;E(M))\simeq M_\sigma.
\tag{3}
\]

**Proof.** A section is constant on each connected set \(\tau^\circ\subset U_\sigma\). Its value on \(\sigma^\circ\) is some \(m\in M_\sigma\). The restriction rule forces its value on each coface \(\tau^\circ\) to be \(r_{\sigma\tau}(m)\). Conversely, these values define a local section near every point: near a point of \(\rho^\circ\), their further values are \(r_{\rho\tau}r_{\sigma\rho}(m)\), which agree with \(r_{\sigma\tau}(m)\). Thus they glue to a section on the whole star. \(\square\)

It follows immediately that star sections are exact on the category of weakly constructible sheaves and detect the zero sheaf. Their higher *ambient sheaf cohomology* still requires a separate argument.

## An acyclic resolution built from closed simplices

For a simplex \(\tau\) and a module \(J\), define a diagram

\[
I_\tau(J)_\sigma=
\begin{cases}J,&\sigma\leq\tau,\\0,&\sigma\not\leq\tau,\end{cases}
\tag{4}
\]

with identity maps between faces of \(\tau\). This is right adjoint to evaluation at \(\tau\):

\[
\operatorname{Hom}_{\mathcal A_S}(M,I_\tau(J))
\simeq\operatorname{Hom}_k(M_\tau,J).
\tag{5}
\]

Indeed, the component at any face \(\sigma\leq\tau\) is the component at \(\tau\) composed with \(r_{\sigma\tau}\); all other components are zero. If \(J\) is injective over \(k\), (5) makes \(I_\tau(J)\) injective in the diagram category.

Choose embeddings \(M_\tau\hookrightarrow J_\tau\) into injective modules for all \(\tau\). They give an injection

\[
M\longrightarrow\prod_\tau I_\tau(J_\tau).
\tag{6}
\]

At \(\sigma\), the factor \(\tau=\sigma\) detects injectivity. Products of these injective diagrams are injective: applying Hom turns the product into a product of exact module-Hom sequences, and products of surjections of modules are surjective. Thus \(\mathcal A_S\) has enough injectives.

The sheaf corresponding to \(I_\tau(J)\) is the constant sheaf \(J\) on the closed simplex \(|\tau|\), extended by its closed embedding. Its intersection with \(U_\sigma\) is empty if \(\sigma\not\leq\tau\); otherwise it is the convex set in \(|\tau|\) where the coordinates indexed by \(\sigma\) are positive. Hence

\[
R\Gamma(U_\sigma;E(I_\tau(J)))
\simeq\begin{cases}J,&\sigma\leq\tau,\\0,&\sigma\not\leq\tau,\end{cases}
\tag{7}
\]

in degree zero, by constant-sheaf acyclicity on that convex set.

On a fixed star \(U_\sigma\), only finitely many factors in (6) have nonzero restriction: they are indexed by cofaces of \(\sigma\). At a point in a coface \(\rho\), a nonzero factor requires \(\rho\leq\tau\), hence \(\sigma\leq\tau\). The product therefore restricts to a finite product of the sheaves in (7). In particular, it is acyclic for star sections. Every injective diagram is a direct summand of such a product, by splitting an embedding (6), so its corresponding sheaf is also acyclic for star sections.

**Theorem 3.** For any weakly constructible sheaf \(F\),

\[
R\Gamma(U_\sigma;F)\simeq F_x
\quad\text{for every }x\in\sigma^\circ,
\tag{8}
\]

where \(F_x\) is in degree zero. In particular, \(H^q(U_\sigma;F)=0\) for \(q>0\).

**Proof.** Resolve its face diagram by injective diagrams. The exact equivalence in Theorem 1 turns this into a sheaf resolution. By the preceding paragraph its terms are acyclic for \(\Gamma(U_\sigma;- )\), so it calculates ambient derived sections. Proposition 2 identifies its section complex with evaluation of the diagram resolution at \(\sigma\). Evaluation is exact, so this complex has cohomology only in degree zero, equal to \(M_\sigma=F_x\). The natural restriction to a stalk is this identification. \(\square\)

The role of local finiteness is now visible. It made the product in (6) finite after restriction to a star; no interchange of an arbitrary product with a stalk or a cohomology functor was used.

On the open simplex \(\sigma^\circ\) itself, constant-sheaf acyclicity also gives \(R\Gamma(\sigma^\circ;F)\simeq F_x\). The natural restriction from the star to that simplex induces the identity of \(M_\sigma\) in degree zero, so it too is an isomorphism of these derived section complexes.

## Approximating an arbitrary sheaf by face data

For an arbitrary sheaf \(G\), take the diagram

\[
(\mathsf T G)_\sigma=\Gamma(U_\sigma;G),
\tag{9}
\]

with restriction along \(U_\tau\subset U_\sigma\). Here we regard \(\mathsf T G\) either as the diagram or as its weakly constructible sheaf. Each star section restricts to germs, giving a natural map
\(E(\mathsf T G)\to G\).

**Proposition 4.** The functor \(\mathsf T\) is right adjoint to the exact inclusion of weakly constructible sheaves into all sheaves. It is left exact. For every \(q\geq0\),

\[
(R^q\mathsf T G)_\sigma\simeq H^q(U_\sigma;G).
\tag{10}
\]

It fixes weakly constructible sheaves, and those sheaves have \(R^q\mathsf T=0\) for \(q>0\).

**Proof.** A sheaf map \(E(M)\to G\) gives maps
\(M_\sigma=\Gamma(U_\sigma;E(M))\to\Gamma(U_\sigma;G)\)
commuting with restrictions. Conversely, such maps give a local sheaf morphism: a germ from \(M_\sigma\) is represented near a point of \(\sigma^\circ\) by its associated star section of \(G\). Compatibility with cofaces makes these morphisms agree on overlaps. This proves the adjunction.

Left exactness follows because star sections are left exact and evaluation is exact. Resolve \(G\) by injective sheaves. Evaluation of \(\mathsf T\) on this resolution is precisely its star-section complex, so its cohomology is \(H^q(U_\sigma;G)\). This proves (10). The last assertions follow from Proposition 2 and Theorem 3. \(\square\)

The adjunction also implies that \(\mathsf T\) sends injective sheaves to injective face diagrams: its left adjoint is exact. Thus its bounded-below right derived functor is the usual derived right adjoint.

Call a sheaf star-acyclic when its higher cohomology vanishes on every star. Formula (10) says exactly that it is \(\mathsf T\)-acyclic. If \(C^\bullet\) is bounded below, each term is star-acyclic, and every cohomology sheaf is weakly constructible, then the natural map

\[
E(\mathsf T C^\bullet)\longrightarrow C^\bullet
\tag{11}
\]

is a quasi-isomorphism. To verify this, evaluate at a point of \(\sigma^\circ\). The left side is the star-section complex. Its cohomology is \(H^j(U_\sigma;C^\bullet)\), since the terms are star-acyclic. The proved bounded-below hypercohomology sequence has
\(H^p(U_\sigma;H^q(C^\bullet))\)
as its second page. Theorem 3 makes all its rows with \(p>0\) vanish; it identifies the surviving term with \(H^q(C^\bullet)_x\). The sequence converges in each total degree because \(p\geq0\) and \(q\) has one lower bound. The proof of the natural edge identifies the composite from hypercohomology to sections of the cohomology sheaf and then to its germ at $x$. On an injective replacement of $C^\bullet$, the map in (11) is the same section-to-germ map; passing from the acyclic-term complex to that replacement commutes with restriction. Theorem 3 identifies cohomology-sheaf sections on the star with that germ. Thus the isomorphism just obtained is induced by the actual map (11), proving that it is a quasi-isomorphism.

## Bounded derived constructibility

For this section assume that \(k\) has finite global dimension and that all simplices have dimension at most one fixed integer \(n\). Let \(D^b_{wS}(k_{|S|})\) be bounded sheaf complexes with weakly constructible cohomology sheaves.

**Theorem 5.** The exact inclusion gives an equivalence

\[
D^b(\mathcal A_S)\xrightarrow{\sim}D^b_{wS}(k_{|S|}),
\tag{12}
\]

with inverse the restriction of \(R\mathsf T\).

**Proof.** Work first in bounded-below derived categories, where \(R\mathsf T\) is defined by injective resolutions and is right adjoint to the exact inclusion. For a bounded complex of face diagrams, Theorem 3 and Proposition 4 give that the adjunction unit is an isomorphism. At each simplex, apply the natural hypercohomology edge to the corresponding star. Higher derived \(\mathsf T\) of each cohomology sheaf vanishes by Theorem 3; compatibility of the edge with restriction identifies the cohomology map of this actual adjunction unit with the identity on the face module. An adjunction with invertible unit makes its left adjoint fully faithful.

Now take \(F\in D^b_{wS}(k_{|S|})\) and choose a bounded-below injective resolution. Its terms are star-acyclic. Formula (11) shows that the adjunction counit
\(E(R\mathsf T F)\to F\)
is a quasi-isomorphism. Moreover, at each simplex the cohomology of \(R\mathsf T F\) is \(H^j(F)_x\), by the same sequence. If \(F\) is cohomologically bounded in \([a,b]\), the diagram complex has zero cohomology outside that same global interval. Truncating in the diagram category gives a bounded representative. Thus the adjunction and its unit/counit restrict to exactly the categories in (12), proving the equivalence. \(\square\)

The uniform dimension hypothesis is retained in this bounded theorem. This proof calculates the right adjoint on objects with weakly constructible cohomology; it has not asserted a boundedness result for its value on every arbitrary bounded sheaf complex.

## Finite coefficients and projective covers

Continue to assume finite global dimension. A bounded sheaf complex is \(S\)-constructible when its cohomology is weakly constructible and its stalk at every point is perfect. Perfect means represented by a bounded complex of finitely generated projective \(k\)-modules. It does not mean merely that its terms have finite dimension unless \(k\) is a field.

If \(k\) is Noetherian, a bounded module complex is perfect exactly when its cohomology modules are finitely generated, as proved in the interval lesson. Thus \(S\)-constructible sheaves in degree zero correspond exactly to diagrams of finitely generated modules. They form an abelian category \(\mathcal A_S^{\mathrm{fg}}\): kernels and cokernels are finitely generated by Noetherianity, and extensions of two finitely generated modules are finitely generated.

For a simplex \(\sigma\), let

\[
P_\sigma(M)_\tau=
\begin{cases}M,&\sigma\leq\tau,\\0,&\sigma\not\leq\tau,\end{cases}
\tag{13}
\]

with identity maps among cofaces. This is left adjoint to evaluation at \(\sigma\), so it is projective when \(M\) is projective over \(k\).

**Lemma 6.** Suppose \(u:F\to G\) is an epimorphism of face diagrams and every \(G_\sigma\) is finitely generated. There is a diagram \(H\), projective in \(\mathcal A_S\), with finite free values, and a map \(H\to F\) whose composite to \(G\) is an epimorphism.

**Proof.** Choose finitely many generators of \(G_\sigma\), and lift them along the surjection \(F_\sigma\to G_\sigma\). Their lifts define a map from \(P_\sigma(k^{m_\sigma})\) to \(F\). Take

\[
H=\bigoplus_\sigma P_\sigma(k^{m_\sigma}).
\tag{14}
\]

At \(\tau\), only its faces \(\sigma\leq\tau\) contribute. There are finitely many, so \(H_\tau\) is finite free. At \(\sigma\), the chosen generators from its own summand make the composite onto \(G_\sigma\) surjective. Each summand is projective, and an arbitrary direct sum of projectives is projective: Hom from the sum is the product of the exact Hom functors. This proves the claim. The sheaf corresponding to \(H\) is constructible, since its stalks are finite free. \(\square\)

When \(k\) is Noetherian of finite global dimension, apply this with \(F=G\) and \(u=\mathrm{id}\). The resulting epimorphism \(H\to G\) has finitely generated kernel at every simplex. Iterate to obtain a projective resolution within \(\mathcal A_S^{\mathrm{fg}}\), whose terms are also projective in \(\mathcal A_S\).

**Theorem 7.** Assume the uniform dimension bound and assume \(k\) is Noetherian of finite global dimension. Then

\[
D^b(\mathcal A_S^{\mathrm{fg}})\xrightarrow{\sim}D^b_S(k_{|S|}).
\tag{15}
\]

**Proof.** The common projective resolutions just constructed calculate Ext between two finite-type diagrams both in \(\mathcal A_S^{\mathrm{fg}}\) and in \(\mathcal A_S\). Their Hom complexes and differentials are identical. Hence all Ext groups agree. Finite truncation triangles show that the inclusion on bounded derived categories is fully faithful.

Every bounded diagram complex with finitely generated cohomology is in its essential image. Induct on its cohomological interval. A single cohomology sheaf is already in \(\mathcal A_S^{\mathrm{fg}}\). A truncation triangle expresses a longer object as an extension of its shorter truncation by its highest cohomology sheaf with a shift. Full faithfulness lifts the connecting morphism, and its cone gives a preimage. Finally, Theorem 5 identifies bounded diagram complexes with bounded weakly constructible sheaf complexes, and the perfect-stalk criterion above identifies their finite-type cohomology exactly with \(D^b_S\). This proves (15). \(\square\)

## Examples and exercises with solutions

### Values around a shared edge

*Difficulty: Introductory.*

Take two triangles joined along one common edge, with no higher simplices. A face diagram assigns \(M\) to the shared open edge and modules \(A,B\) to the two open triangles, with maps \(a:M\to A\) and \(b:M\to B\). Describe sections on the edge's open star and their higher cohomology.

**Solution.** The open star contains the open edge and the two open triangles. A section has values \(m,a(m),b(m)\), so its module is \(M\), regardless of injectivity or surjectivity of \(a,b\). Theorem 3 gives zero higher cohomology. Values at the edge's endpoints play no role here, because the endpoints are not in this star.

### Global cohomology despite local acyclicity

*Difficulty: Intermediate.*

Triangulate a circle by four edges and four vertices. Put \(k\) on each open edge and zero on each vertex, so all face maps from vertices are zero. Assume \(k\neq0\). Compute global sheaf cohomology and compare the star calculations.

**Solution.** The sheaf is the direct sum of extensions by zero from the four open edges. The ambient circle is compact, so global cohomology of each summand is compact-support cohomology of an open interval, namely \(k[-1]\). Thus the whole sheaf has \(H^1=k^4\) and all other cohomology zero. At a vertex star, the section module is zero and all higher cohomology vanishes. At an edge star, the section module is \(k\) and higher cohomology again vanishes. Star acyclicity supplies local calculations; it does not make global cohomology vanish.

### Why a projective cover is still finite at each stalk

*Difficulty: Intermediate.*

Let \(S\) be an infinite locally finite triangulation of a line, and put \(k\) at every simplex. In the construction (14), choose one generator at every simplex. Compute the rank of \(H\) at a vertex and at an edge.

**Solution.** A vertex has only itself as a nonempty face, so its value is one copy of \(k\). An edge has its two vertices and itself as faces, so its value is \(k^3\). There are infinitely many summands globally, but only finitely many contribute at any stalk. The conclusion comes from face finiteness, rather than a claim that the global direct sum is finite.

### Which hypothesis supports which argument

*Difficulty: Advanced.*

Explain why local finiteness and a uniform dimension bound are distinct. Identify where local finiteness was used, and state the additional coefficient hypothesis in Theorem 7.

**Solution.** Local finiteness says that each vertex has finitely many cofaces. It allows different connected components to have arbitrarily large finite dimension. For example, the disjoint union of one simplex of each positive dimension is locally finite and has no uniform dimension bound. Local finiteness made the product of elementary injective diagrams finite on a star in the acyclicity proof. A uniform dimension bound is expressly retained in Theorems 5 and 7. Theorem 7 additionally requires the ring to be Noetherian, as well as to have finite global dimension; Noetherianity keeps the kernels in its projective resolutions finitely generated. The ordinary diagram equivalence and star acyclicity did not require Noetherianity or a uniform dimension bound.

## Source comparison and references {#references}

Curry's [exact arXiv version 1607.06942v1](https://arxiv.org/abs/1607.06942v1), submitted 23 July 2016, provides the comparison for the direction of face maps and the elementary objects. The section “Sheaves and Cosheaves on Posets” constructs the Alexandrov sheaf from a functor by sections on upper sets. “Elementary Injectives and Projectives” gives the closed-cell and open-star diagrams and proves the first injectivity statement by its evaluation adjunction. Its default cellular coefficients are vector spaces, and its decomposition of all injectives into elementary objects is stated for a finite cell complex.

The module-valued and locally finite argument here is supplied directly. Injective coefficient modules enter through the right adjoint to evaluation; local finiteness makes the elementary product finite on each star. The convex calculation then computes ambient sheaf cohomology, rather than only cohomology in an Alexandrov diagram category. Theorem 5 identifies the actual derived unit and counit, and the finite-at-each-face projective construction in (13)–(15) supplies the Noetherian finite-coefficient extension. These additional steps are not claimed as consequences of Curry's finite vector-space decomposition theorem.

The lesson is organized around recovering sections from a germ, proving ambient star acyclicity, and then comparing the bounded and finite-coefficient categories. The existing interval, shared-edge, circle and infinite-line calculations are retained. The module proof under (2) supplies the categorical input directly. For the general pointwise-limit theorem, see the separate categorical reading below.

- Tom Leinster, *Basic Category Theory*, Theorem 6.2.5 and its dual, [arXiv:1612.09375v2](https://arxiv.org/abs/1612.09375v2), for the general pointwise-limit formulation. The programme reading Pointwise abelian structure and natural splittings provides further categorical background; the face-module proof above is complete without it.

- Justin Curry, *Dualities between Cellular Sheaves and Cosheaves*, arXiv:1607.06942v1, 2016, the poset equivalence and elementary-object sections. [Open preprint](https://arxiv.org/abs/1607.06942v1).
- Pierre Schapira, *An Introduction to Sheaves on Grothendieck Topologies*, work in progress, title page dated 1 August 2026. [Open text](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf).
- Extending sections on convex sets, the constant-coefficient calculation used in (7)–(8), with its exact Stacks foundation comparisons.
